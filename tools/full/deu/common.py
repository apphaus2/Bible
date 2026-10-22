"""Shared helpers for the Deuteronomy chapters: line builders for speech panels and the standard panels."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from speech import orate
from asv import ems, UNSPACED
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
        if cur and n + ems(t) > budget:
            out.append(cur); cur, n = [], 0
        cur.append(r); n += ems(t)
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

def heading(text, n=6):
    """A cell heading from a law's opening words: up to the first stop if that comes within n+1 words, else n words."""
    import re as _re
    t = text.strip()
    for _ in range(3):                         # drop filler openings: "And it shall be, when ..." → "When ..."
        t = _re.sub(r"^(And it shall come to pass,?|And it shall be,?|It shall be,?|And|But|For|Moreover|Also|Then|Now|Notwithstanding,|Therefore)\s+", "", t)
    t = t[:1].upper() + t[1:]
    if UNSPACED:                               # an unspaced script (Japanese): up to the first stop, at most 3n characters
        h = _re.split(r"[,;:.!?(、。，；：！？（「『」』]", t.lstrip("「『"))[0]
        return h if len(h) <= 3 * n else h[:3 * n - 1] + "…"
    first = _re.split(r"[,;:.!?(]", t)[0].split()
    words = first if len(first) <= n + 1 else _re.split(r"\s+", t)[:n]
    return _re.sub(r"[,;:.!?()]+$", "", " ".join(words)).upper()

def laws(c, groups, head=None, lead=None):
    """Law cells for law_pages: groups = list of (a, b) verse spans in chapter c; heading and pictogram from the words."""
    import picto
    items = []
    for i, (a, b) in enumerate(groups):
        refs = f"{c}:{a}" + (f"-{b}" if b != a else "")
        text = sp(refs) if b != a else v(f"{c}:{a}")
        uid = f"lw{c}x{a}"
        en = " ".join(G.verses[(c, n)] for n in range(a, b + 1))     # the pictogram is picked by the ASV's words
        items.append((heading(text), refs, (lambda p, en=en: picto.pick(en, p)), "", head if i == 0 else None))
    return items

def law_groups(c, a, b, budget=380):
    """Consecutive verses c:a–b grouped into law cells of about `budget` characters."""
    out, cur, n = [], [], 0
    for k in range(a, b + 1):
        t = v(f"{c}:{k}")
        if cur and n + ems(t) > budget:
            out.append((cur[0], cur[-1])); cur, n = [], 0
        cur.append(k); n += ems(t)
    if cur: out.append((cur[0], cur[-1]))
    return out

def codify(c, a, b, head=None, budget=380):
    """Law cells for verses c:a–b (deu.common.laws over law_groups)."""
    return laws(c, law_groups(c, a, b, budget), head=head)

def law_chapter(prev, num, kanji, name, rng, sections, title_art, title_bg, quote, nxt, prefix):
    """A whole chapter of statutes: a title page, then law cells for each section (c, a, b, page head), spoken by Moses.
    Returns (START, PAGES)."""
    from num.pages import Pages
    from fx import chapter_title, end_mark
    from exo.kit import law_pages, set_book
    set_book(G)
    PG = Pages(prev.START + len(prev.PAGES) - 1)
    art = shade(f'<rect x="0" y="0" width="760" height="1080" fill="{title_bg}"></rect><g transform="translate(0 420)">{title_art}</g>')
    PG.P(f"{prefix}-00-Title", f"Chapter {num} · {name}", title=True)(
        lambda n: chapter_title(num, kanji, name, rng, art, title_bg, quote, "Deuteronomy · Volume Five"))
    items = []
    for c, a, b, head in sections:
        items += codify(c, a, b, head=head)
    PG.extend(law_pages(items, f"{prefix}-L", PG.next(), sections[0][3], title_book="Deuteronomy", carry=True, spoken=True,
                        end=end_mark(f"NEXT · {nxt.upper()}", "right: 10px; top: 10px")))
    return PG.start, PG.pages

def shade(svg, h=440):
    """A chapter title's art with a dark band at the top, so the title reads on a light picture."""
    return (svg + f'<defs><linearGradient id="shd{h}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1A1028" stop-opacity="0.95"></stop>'
            f'<stop offset="0.7" stop-color="#1A1028" stop-opacity="0.7"></stop><stop offset="1" stop-color="#1A1028" stop-opacity="0"></stop></linearGradient></defs>'
            f'<rect x="0" y="0" width="760" height="{h}" fill="url(#shd{h})"></rect>')

def sing(c, a, b, arts, budget=300, code="DEUT", **k):
    """A song (poetry), verses c:a–b, as song lines over drawings: each panel about `budget` characters, the arts
    (bg, f(w, h) -> svg) cycling; every third panel is the singer's face instead."""
    out, cur, n = [], [], 0
    for x in range(a, b + 1):
        t = v(f"{c}:{x}")
        if cur and n + ems(t) > budget:
            out.append(cur); cur, n = [], 0
        cur.append(f"{c}:{x}"); n += ems(t)
    if cur: out.append(cur)
    segs = []
    for i, g in enumerate(out):
        ref = f"{code} {g[0]}" + (f"–{g[-1].split(':')[1]}" if g[-1] != g[0] else "")
        lines = [("song", v(r)) for r in g]
        if i % 3 == 2:
            segs.append(seg(lines, ref, tok=K.MOSES_FIRE, bg=GOLDEN, **k))
        else:
            bg, art = arts[i % len(arts)]
            segs.append(seg(lines, ref, tok=None, bg=bg, art=art, **k))
        k.pop("head", None); k.pop("stamp", None)
    return segs
