"""Shared helpers for the Deuteronomy chapters: line builders for speech panels and the standard panels."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from speech import orate
from deu import G, art as K
from genesis import art as X
from genesis.ch02 import W1, NIGHT
from genesis.ch06 import GOLDEN

v, sp = G.v, G.span
INK = "#0B1A2E"

def say(ref, frm=None, to=None): return ("say", v(ref, frm=frm, to=to))
def gd(ref, frm=None, to=None): return ("god", v(ref, frm=frm, to=to))
def cp(ref, frm=None, to=None): return ("cap", v(ref, frm=frm, to=to))
def says(refs): return ("say", sp(refs))
def gods(refs): return ("god", sp(refs))
def caps(refs): return ("cap", sp(refs))

def mo(h, lines, ref, tok=None, bg=GOLDEN, flip=False, w=W1, **k):
    """Moses speaking (calm by default)."""
    return orate(tok or K.MOSES_CALM, h, bg, lines, w=w, ref=ref, flip=flip, **k)

def voice(h, lines, ref, w=W1, **k):
    """Words over the night sky, no face (God's words, or narration)."""
    return orate(None, h, NIGHT, lines, w=w, ref=ref, art=X.cosmic(w, h), **k)

def over(h, bg, art, lines, ref, w=W1, **k):
    """Words in a column over a drawing."""
    return orate(None, h, bg, lines, w=w, ref=ref, art=art, top=True, **k)

# ---- automatic segmentation ------------------------------------------------------------------------------------------
from discourse import seg
from genesis.ch04 import COLD
from genesis.ch07 import RED
MOODS = {"calm": (K.MOSES_CALM, GOLDEN), "stern": (K.MOSES_STERN, RED), "grief": (K.MOSES_GRIEF, COLD), "fire": (K.MOSES_FIRE, GOLDEN)}

def verses(c, a, b):
    return [f"{c}:{n}" for n in range(a, b + 1)]

def auto(c, a, b, moods=("calm",), budget=620, code="DEUT", arts=None, every=3, **k):
    """Moses' words, verses c:a–b, grouped into speech panels of about `budget` characters, the moods cycling. With
    arts (a list of (bg, f(w, h) -> svg)), every `every`-th panel sets the words over the next drawing instead of a face."""
    out, cur, n, mi = [], [], 0, 0
    vs = verses(c, a, b)
    for i, r in enumerate(vs):
        t = v(r)
        if cur and n + len(t) > budget:
            out.append(cur); cur, n = [], 0
        cur.append(r); n += len(t)
    if cur: out.append(cur)
    segs = []
    ai = 0
    for gi, g in enumerate(out):
        a0, b0 = g[0], g[-1]
        ref = f"{code} {a0}" + (f"–{b0.split(':')[1]}" if b0 != a0 else "")
        words = [("say", " ".join(v(r) for r in g))]
        if arts and gi % every == every - 1:
            bg, art = arts[ai % len(arts)]; ai += 1
            segs.append(seg(words, ref, tok=None, bg=bg, art=art, **k))
        else:
            tok, bg = MOODS[moods[mi % len(moods)]]; mi += 1
            segs.append(seg(words, ref, tok=tok, bg=bg, **k))
        k.pop("head", None); k.pop("stamp", None)
    return segs

def heading(text, n=5):
    import re as _re
    t = _re.sub(r"^(And|But|For|Moreover|Also|Then|Now)\s+", "", text.strip())
    words = _re.split(r"\s+", t)[:n]
    return _re.sub(r"[,;:.!?()]+$", "", " ".join(words)).upper()

def laws(c, groups, head=None, lead=None):
    """Law cells for law_pages: groups = list of (a, b) verse spans in chapter c; heading and pictogram from the words."""
    import picto
    items = []
    for i, (a, b) in enumerate(groups):
        refs = f"{c}:{a}" + (f"-{b}" if b != a else "")
        text = sp(refs) if b != a else v(f"{c}:{a}")
        uid = f"lw{c}x{a}"
        items.append((heading(text), refs, (lambda p, text=text: picto.pick(text, p)), "", head if i == 0 else None))
    return items

def law_groups(c, a, b, budget=380):
    """Consecutive verses c:a–b grouped into law cells of about `budget` characters."""
    out, cur, n = [], [], 0
    for k in range(a, b + 1):
        t = v(f"{c}:{k}")
        if cur and n + len(t) > budget:
            out.append((cur[0], cur[-1])); cur, n = [], 0
        cur.append(k); n += len(t)
    if cur: out.append((cur[0], cur[-1]))
    return out

def codify(c, a, b, head=None, budget=380):
    """Law cells for verses c:a–b (deu.common.laws over law_groups)."""
    return laws(c, law_groups(c, a, b, budget), head=head)
