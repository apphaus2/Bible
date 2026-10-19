"""Shared helpers for the Jeremiah chapters: line builders for discourse.pack, run() for long oracles, roll cells, and the
cast's faces (Jeremiah at four ages, the kings of Judah from 2 Kings, the men of his story)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from discourse import seg
from jer.pagepack import pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from jos.art import below
from kg2.common import ZEDEKIAH, GEDALIAH, JEHOIACHIN, JOSIAH, BABYLONIAN, CAPTAIN, MESSENGER, ISRAELITE, PROPHET, WIDOW
from jer import G

v, sp = G.v, G.span
CODE = "JER"
NIGHT = "#0F0E2A"
def say(ref, frm=None, to=None, after=None): return ("say", v(ref, frm=frm, to=to, after=after))
def gd(ref, frm=None, to=None, after=None): return ("god", v(ref, frm=frm, to=to, after=after))
def cp(ref, frm=None, to=None, after=None): return ("cap", v(ref, frm=frm, to=to, after=after))
def sg(ref, frm=None, to=None, after=None): return ("song", v(ref, frm=frm, to=to, after=after))
def says(refs): return ("say", sp(refs))
def gods(refs): return ("god", sp(refs))
def caps(refs): return ("cap", sp(refs))
def sgs(refs): return ("song", sp(refs))
def joined(kind, *parts):
    """One box from several cuts: joined("say", ("1:2", "Let there", None), "1:3") — a ref alone is the whole verse."""
    return (kind, " ".join(v(p) if isinstance(p, str) else v(p[0], frm=p[1], to=p[2] if len(p) > 2 else None) for p in parts))

def cut(ref, at, k1="cap", k2="god"):
    """A verse split after the words `at`: [(k1, up to and including at), (k2, the rest)] — "Jehovah said unto me," + his words."""
    return [(k1, v(ref, to=at)), (k2, v(ref, after=at))]

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 0.92)
    k.setdefault("min_size", 12.5)
    return _pack(segs, prefix, start, book="Jeremiah", code=CODE, **k)

def face(lines, ref, tok, bg=GOLDEN, **k): return seg(lines, ref, tok=tok, bg=bg, **k)
def drawn(lines, ref, art, bg, k=None, **kw):
    """Words over a drawing; with k the drawing is set below the words (jos.art.below)."""
    return seg(lines, ref, bg=bg, art=below(art, k) if k else art, **kw)

def label(refs):
    a, _, b = refs.partition("-")
    return f"{CODE} {a}" + (f"–{b}" if b else "")

def cell(name, refs, accent="#FFD23F", head=None):
    """One roll cell: a name over verses refs ("2:3-8"), every word."""
    return (name, sp(refs), label(refs), accent, head)

def cells(c, a, b, name, accent, head=None, budget=520, brk=None):
    from rolls import verse_cells
    return verse_cells(G, CODE, c, a, b, name, accent, head=head, budget=budget, brk=brk)

def roll(items, prefix, start, tag, **k):
    from rolls import roll_pages
    return roll_pages(items, prefix, start, "Jeremiah", CODE, tag=tag, **k)

def S(lines, refs, a=None, t=None, k=0.5, **kw):
    """One panel: lines, labelled refs ("2:4-6"); a = (bg, fn(w, h)) sets the words over a drawing (below(fn, k)),
    t = (face, bg) beside a face; neither: over the night sky."""
    if a:
        bg, fn = a
        return seg(lines, label(refs), bg=bg, art=below(fn, k) if k else fn, **kw)
    if t: return seg(lines, label(refs), tok=t[0], bg=t[1], **kw)
    return seg(lines, label(refs), bg=NIGHT, **kw)

def O(refs, a=None, t=None, kind="god", pre=(), post=(), **kw):
    """One panel of whole verses refs ("2:4-6") in one kind of box (God's words by default), with lines before/after."""
    return S(list(pre) + [(kind, sp(refs))] + list(post), refs, a=a, t=t, **kw)

def run(refs, kind="god", faces=(), arts=(), every=2, budget=520, head=None, stamp=None, pre=(), k=0.5, offset=0, hi=21, heads=None):
    """A run of whole verses ("4:5-18") in one kind of box, cut into panels of about `budget` characters. Panels alternate
    between faces (tok, bg), cycling, and drawings (bg, fn(w, h)), cycling: every `every`-th panel (counting from `offset`)
    is a drawing, set below its words (below(fn, k)). pre: lines set before the first panel's words. heads: {verse: head}
    starts a panel (and a page head) at that verse."""
    c, vs = refs.split(":"); a, _, b = vs.partition("-"); a, b = int(a), int(b or a)
    heads = heads or {}
    groups, cur, n = [], [], sum(len(t) for _, t in pre)
    for x in range(a, b + 1):
        t = len(G.verses[(int(c), x)])
        if cur and (n + t > budget or x in heads):
            groups.append(cur); cur, n = [], 0
        cur.append(x); n += t
    if cur: groups.append(cur)
    segs, fi, ai = [], 0, 0
    for gi, g in enumerate(groups):
        ref = f"{CODE} {c}:{g[0]}" + (f"–{g[-1]}" if g[-1] != g[0] else "")
        lines = (list(pre) if gi == 0 else []) + [(kind, " ".join(v(f"{c}:{x}") for x in g))]
        kw = dict(hi=hi)
        if gi == 0:
            if head: kw["head"] = head
            if stamp: kw["stamp"] = stamp
        if g[0] in heads: kw["head"] = heads[g[0]]
        if arts and (not faces or (gi + offset) % every == every - 1):
            bg, fn = arts[ai % len(arts)]; ai += 1
            segs.append(seg(lines, ref, bg=bg, art=below(fn, k), **kw))
        else:
            tok, bg = faces[fi % len(faces)]; fi += 1
            segs.append(seg(lines, ref, tok=tok, bg=bg, **kw))
    return segs

# ---- Jeremiah at four ages: 0 at his call (beardless, a young man), 1 black-bearded, 2 greying, 3 grey ----------------------
SCARF = "#3A4656"            # his dark blue-grey headcloth
_HAIR = {0: ("#2A1A10", "#5A4A3E"), 1: ("#1A1210", "#4A3A2E"), 2: ("#4A4440", "#7A746E"), 3: ("#8A847A", "#B8B2A6")}
_BEARD = {0: None, 1: "#1A1210", 2: "#5A5450", 3: "#A8A29A"}
_SKIN = {0: ("#D9A27A", "#6A4A3A"), 1: ("#C98E66", "#5A3A3A"), 2: ("#C08A66", "#4A3A3A"), 3: ("#B98A6E", "#4A3A4A")}
_MOOD = {"calm": dict(light="#FFE680"), "word": dict(light="#FFF4C2"), "grief": dict(brow="sorrow", tear=True, light="#9AA8C8"),
         "stern": dict(brow="scowl", light="#D7261E"), "afraid": dict(brow="sorrow", sweat=True, light="#9AA8C8"),
         "weary": dict(brow="sorrow", light="#9AA8C8")}
_BG = {"calm": GOLDEN, "word": GOLDEN, "grief": COLD, "stern": RED, "afraid": COLD, "weary": COLD}

def jer(age=1, mood="calm"):
    """Jeremiah's face at an age (0–3) and in a mood (calm, word, grief, stern, afraid, weary)."""
    skin, shadow = _SKIN[age]; hair, hl = _HAIR[age]; beard = _BEARD[age]
    k = dict(skin=skin, shadow=shadow, hair=hair, hl=hl, scarf=SCARF, **_MOOD[mood])
    if beard: k.update(beard=True, beard_color=beard)
    else: k.update(stubble="#5A4A3E")
    return F("adam", cord=True, **k)

def J(age=1, *moods):
    """[(face, bg)] for run(): Jeremiah at an age, in the moods given (cycling)."""
    return [(jer(age, m), _BG[m]) for m in (moods or ("calm",))]

# ---- the cast --------------------------------------------------------------------------------------------------------
JEHOIAKIM = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#1F3A7A", band=True, brow="scowl", light="#D7261E")
PASHHUR = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#F3EFE6", band=True, brow="scowl", light="#FFC14D")
PRIEST = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#F3EFE6", band=True, light="#FFE680")
HANANIAH = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#8A6A2A", cord=True, light="#FFC14D")
BARUCH = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#5A6A4A", cord=True, light="#FFE680")
BARUCH_GRIEF = F("adam", skin="#C98E66", shadow="#3A2A4A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#5A6A4A", cord=True, brow="sorrow", tear=True, light="#9AA8C8")
EBEDMELECH = F("adam", skin="#6A4030", shadow="#2A1410", hair="#0D0D0F", hl="#2A2220", stubble="#0D0D0F", scarf="#E8B830", light="#FFE680")
PRINCE = F("adam", skin="#C98E66", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#6A2A3A", band=True, brow="scowl", light="#D7261E")
PRINCE_CALM = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#2A5A5A", band=True, light="#FFE680")
ELDER = F("adam", skin="#B98A6E", shadow="#4A3A4A", hair="#C8C2B6", hl="#E8E2D6", beard=True, beard_color="#D8D2C6", scarf="#5A4A3A", cord=True, light="#FFF4C2")
RECHABITE = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#7A6A4A", light="#FFE680")
JOHANAN = F("adam", skin="#C98E66", shadow="#4A2A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#6A4A2A", cord=True, brow="scowl", light="#FFC14D")
ISHMAEL = F("adam", skin="#B98A6E", shadow="#3A1A2A", hair="#0D0D0F", hl="#2A2220", stubble="#0D0D0F", scarf="#3A1A2A", band=True, brow="scowl", light="#D7261E")
NEBUZARADAN = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#2A4A6A", band=True, light="#FFC14D")
WOMAN = F("eve", skin="#C98E66", shadow="#5A3A3A", hair="#1A1210", scarf="#7A2A4A", band=True, brow="scowl", light="#FFC14D")
SERAIAH = F("adam", skin="#C98E66", shadow="#4A3A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#4A5A7A", cord=True, light="#FFE680")
PENITENT = F("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#6A5A3A", cord=True, brow="sorrow", tear=True, light="#9AA8C8")
PEOPLE = F("adam", skin="#C47A5A", shadow="#5A3A2A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#6A5A3A", cord=True, brow="scowl", light="#FFC14D")
ZEDEKIAH_CALM = F("adam", skin="#C98E66", shadow="#3A2A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#1F3A7A", band=True, light="#FFE680")
