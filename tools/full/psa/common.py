"""Shared helpers for the Psalms chapters: song lines with their poetic line breaks, the psalm builder, and the singers' faces.

    psalm(23, "1 pasture | 4 valley | 5 table | 6 house")
A plan is a run of groups "first-verse key": the verses from that one up to the next group's first verse go over that
drawing (a scene key from psa.art.SCENES) or beside that face (a key of FACES, upper case). A group longer than a panel's
budget is split into several panels (the drawing repeated with a new seed). God's words quoted in a psalm go in the Voice
box: god={"2:7": "Thou art my son;"} (from that phrase to the end of the verse), {"50:7": None} (the whole verse) or
{"81:6": ("I removed", "basket.")} (a middle run). Every psalm opens with its head: PSALM N and the superscription."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from psa import G
from psa.text import TITLES, BOOKS, ALEPH, LINES, HEADS, lines_of
from psa.layout import seg, pack as _pack
from fx import end_mark
from sa2.common import (DAVID, DAVID_BOLD, DAVID_GRIEVED, DAVID_KING, DAVID_JOY, DAVID_WRATH, DAVID_GRIEF, DAVID_MOURN, DAVID_OLD, DAVID_OLD_ALARM,
                        DAVID_OLD_WEEP)
from kg2.common import SOLOMON, SOLOMON_WISE, SOLOMON_OLD
from deu.art import MOSES_CALM, MOSES_GRIEF, MOSES_STERN

v, sp = G.v, G.span
CODE = "PS"

def _key(ref):
    c, x = ref.split(":"); return int(c), int(x)

def _poem(ref, frm=None, to=None, after=None):
    """Cut ref from the ASV (G.v records it) and put back the poetic line breaks that fall inside the cut."""
    t = v(ref, frm=frm, to=to, after=after)
    c, x = _key(ref)
    full = G.verses[(c, x)]
    ls = lines_of(c, x, full)
    if len(ls) < 2: return t
    a = full.find(t)
    out, pos = [], 0
    for l in ls:
        lo, hi = pos, pos + len(l)
        s0, s1 = max(lo, a), min(hi, a + len(t))
        if s1 > s0: out.append(full[s0:s1].strip())
        pos = hi + 1
    return "\n".join(o for o in out if o)

def sg(ref, frm=None, to=None, after=None): return ("song", _poem(ref, frm, to, after))
def gd(ref, frm=None, to=None, after=None): return ("god", _poem(ref, frm, to, after))
def cp(ref, frm=None, to=None, after=None): return ("cap", v(ref, frm=frm, to=to, after=after))

def label(c, a, b=None):
    return f"{CODE} {c}:{a}" + (f"–{b}" if b and b != a else "")

# ---- the singers ------------------------------------------------------------------------------------------------------------
# Asaph and the sons of Korah are Levite singers in white linen (2 Chronicles 5:12): white headcloths, each with his own cord.
ASAPH = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#F3EFE6", cord=True, light="#FFE680")
ASAPH_GRIEF = F("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#F3EFE6", cord=True, brow="sorrow", tear=True, light="#9AA8C8")
ASAPH_STERN = F("adam", skin="#C98E66", shadow="#4A2A2A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#F3EFE6", cord=True, brow="scowl", light="#D7261E")
KORAH = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#E8E2D6", band=True, light="#FFE680")
KORAH_GRIEF = F("adam", skin="#C98E66", shadow="#3A2A4A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#E8E2D6", band=True, brow="sorrow", tear=True, light="#9AA8C8")
HEMAN = F("adam", skin="#B98A6E", shadow="#2A2A4A", hair="#3A2A20", hl="#6A5A4E", beard=True, beard_color="#3A2A20", scarf="#E8E2D6", cord=True, brow="sorrow", tear=True, light="#8A98C8")
ETHAN_GRIEF = F("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#C8C2B6", hl="#E8E2D6", beard=True, beard_color="#D8D2C6", scarf="#E8E2D6", band=True, brow="sorrow", tear=True, light="#9AA8C8")
ETHAN = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#C8C2B6", hl="#E8E2D6", beard=True, beard_color="#D8D2C6", scarf="#E8E2D6", band=True, light="#FFD23F")
LEVITE = F("adam", skin="#C47A5A", shadow="#5A3A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#F3EFE6", cord=True, light="#FFC14D")
LEVITE_GRIEF = F("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#F3EFE6", cord=True, brow="sorrow", light="#9AA8C8")
LEVITE_JOY = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", scarf="#F3EFE6", band=True, light="#FFE680")
EXILE = F("adam", skin="#B98A6E", shadow="#2A2A3A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#4A4440", scarf="#4A4A5A", brow="sorrow", tear=True, light="#8A98C8")
BRIDE = F("eve", skin="#D9A27A", shadow="#7A4A4A", hair="#1A1210", scarf="#B5121B", band=True, light="#FFE680")

FACES = {
    "DAVID": (DAVID, GOLDEN), "DAVID_BOLD": (DAVID_BOLD, RED), "DAVID_GRIEVED": (DAVID_GRIEVED, COLD), "DAVID_KING": (DAVID_KING, GOLDEN),
    "DAVID_JOY": (DAVID_JOY, GOLDEN), "DAVID_WRATH": (DAVID_WRATH, RED), "DAVID_GRIEF": (DAVID_GRIEF, COLD), "DAVID_MOURN": (DAVID_MOURN, COLD),
    "DAVID_OLD": (DAVID_OLD, GOLDEN), "DAVID_OLD_ALARM": (DAVID_OLD_ALARM, RED), "DAVID_OLD_WEEP": (DAVID_OLD_WEEP, COLD),
    "SOLOMON": (SOLOMON, GOLDEN), "SOLOMON_WISE": (SOLOMON_WISE, GOLDEN),
    "MOSES": (MOSES_CALM, GOLDEN), "MOSES_GRIEF": (MOSES_GRIEF, COLD), "MOSES_STERN": (MOSES_STERN, RED),
    "ASAPH": (ASAPH, GOLDEN), "ASAPH_GRIEF": (ASAPH_GRIEF, COLD), "ASAPH_STERN": (ASAPH_STERN, RED),
    "KORAH": (KORAH, GOLDEN), "KORAH_GRIEF": (KORAH_GRIEF, COLD), "HEMAN": (HEMAN, COLD), "ETHAN": (ETHAN, GOLDEN), "ETHAN_GRIEF": (ETHAN_GRIEF, COLD),
    "LEVITE": (LEVITE, GOLDEN), "LEVITE_GRIEF": (LEVITE_GRIEF, COLD), "LEVITE_JOY": (LEVITE_JOY, GOLDEN), "EXILE": (EXILE, COLD), "BRIDE": (BRIDE, GOLDEN),
}

# ---- the psalm builder ------------------------------------------------------------------------------------------------------
def _verse_lines(c, x, god):
    ref = f"{c}:{x}"
    g = god.get(ref, False) if god else False
    if g is False: return [sg(ref)]
    if g is None: return [gd(ref)]
    full = G.verses[(c, x)]
    if isinstance(g, str): frm, to = g, None
    else: frm, to = g
    a = full.find(frm)
    b = len(full) if to is None else full.find(to, a) + len(to)
    out = []
    if full[:a].strip(): out.append(sg(ref, to=full[:a].strip()))
    out.append(gd(ref, frm=frm, to=to))
    rest = full[b:].strip()
    if rest: out.append(sg(ref, frm=rest))
    return out

def _plain(c, x):
    """Psalm 119: a verse whose end carries the next letter's head (ב BETH.) is cut in two: the verse, and the head."""
    t = G.verses[(c, x)]
    m = re.search(r"[א-ת]", t)
    if HEADS: return (t, None)           # a translation with its own letter heads: the verse is whole, the head is its own line
    return (t[:m.start()].strip(), t[m.start():]) if m else (t, None)

def mirror(svg, w, on):
    """A drawing used twice in a run is flipped left to right the second time (maps and labelled plates never are)."""
    return f'<g transform="translate({w} 0) scale(-1 1)">{svg}</g>' if on else svg

def balance(n, verses, bud):
    """Split a run of verses into the fewest panels of about `bud` characters, as even as the verses allow."""
    import math
    ls = [len(G.verses[(n, x)]) for x in verses]
    k = max(1, math.ceil(sum(ls) / bud))
    if k >= len(verses): return [[x] for x in verses]
    best = None
    # greedy toward an even target; try a few targets and keep the most even split with k parts
    for tgt in [sum(ls) / k * f for f in (1.0, 0.95, 1.05, 0.9, 1.1, 0.85, 1.15)]:
        chunks, cur, nc = [], [], 0
        for x, l in zip(verses, ls):
            if cur and nc + l / 2 > tgt and len(chunks) < k - 1:
                chunks.append(cur); cur, nc = [], 0
            cur.append(x); nc += l
        chunks.append(cur)
        sizes = [sum(len(G.verses[(n, x)]) for x in c) for c in chunks]
        score = (abs(len(chunks) - k), max(sizes))
        if best is None or score < best[0]: best = (score, chunks)
    return best[1]

def parse_plan(plan):
    out = []
    for part in plan.split("|"):
        part = part.strip()
        if not part: continue
        a, *keys = part.split()
        out.append((int(a), keys))
    return out

def singer(n):
    """The face for psalm n, from its superscription: David, Asaph, the sons of Korah, Heman, Ethan, Moses, Solomon, or a
    Levite singer when the psalm names no one."""
    t = TITLES.get(n, "")
    for name, k in (("Heman", "HEMAN"), ("Ethan", "ETHAN"), ("Asaph", "ASAPH"), ("Korah", "KORAH"), ("Moses", "MOSES"), ("Solomon", "SOLOMON_WISE"), ("David", "DAVID_KING")):
        if name in t: return k
    return "LEVITE"

def psalm(n, plan, god=None, budget=380, fbudget=440, face=None, head=None, upto=None, start=None, title=None, book=True):
    """The segments of psalm n (or of verses start..upto of it). Returns a list of discourse segments for layout.pack."""
    from psa import art as K
    nv = max(x for (c, x) in G.verses if c == n)
    groups = parse_plan(plan)
    lo = start or groups[0][0]
    hi = upto or nv
    segs, ix = [], 0
    for gi, (a, keys) in enumerate(groups):
        b = (groups[gi + 1][0] - 1) if gi + 1 < len(groups) else hi
        verses = list(range(a, b + 1))
        # split into panels by budget
        key = keys[0]
        is_face = key.isupper()
        bud = fbudget if is_face else budget
        chunks = balance(n, verses, bud)
        for ci, ch in enumerate(chunks):
            lines = []
            first = not segs
            if first and (head is None):
                lines.append(("head", (n, TITLES.get(n), BOOKS.get(n) if book else None)))
            elif first and head:
                lines += [("head", hd) for hd in (head if isinstance(head, list) else [head])]
            for x in ch:
                if n == 119:
                    main, nxt = _plain(n, x)
                    lines.append(("song", _poem(f"{n}:{x}", to=main) if nxt else _poem(f"{n}:{x}")))
                else:
                    lines += _verse_lines(n, x, god)
            ref = label(n, ch[0], ch[-1])
            if is_face: k = key
            elif len(keys) > 1: k = keys[ci % len(keys)]
            else: k = key if ci % 2 == 0 else (face or singer(n))     # a long run over one drawing alternates with the singer's face
            seed = n * 100 + ix
            nm = (title or f"Psalm {n}") if first else None
            if k.isupper():
                tok, bg = FACES[k]
                segs.append(seg(lines, ref, tok=tok, bg=bg, head=nm, title=title or nm))
            else:
                bg, fn = K.SCENES[k]
                segs.append(seg(lines, ref, bg=bg, art=(lambda w, h, fn=fn, p=f"q{n}x{ix}", s=seed, k=k: mirror(fn(p, w, h, s), w, s % 2 == 1 and k not in K.NOMIRROR)), head=nm, title=title or nm))
            ix += 1
    return segs

def pack(segs, prefix, start, **k):
    return _pack(segs, prefix, start, book="Psalms", code=CODE, **k)

def chapter_open(num, name, rng, scene, quote, bg=None, seed=None):
    """A chapter's title page: the scene full-bleed under the title band, one line of the psalms as its quote."""
    import mk
    from fx import chapter_title
    from deu.common import shade
    from psa import art as K
    bgc, fn = K.SCENES[scene]
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="{bgc}"></rect><g transform="translate(0 300)">{fn("t%d" % num, 760, 780, seed or num * 1000 + 1)}</g>')
    return chapter_title(num, f"第{mk.kanji_num(num)}話", name, rng, svg, bg or bgc, quote, "Psalms · Volume Nineteen")
