"""Shared helpers for the 2 Samuel chapters: line builders for discourse.pack, the cast's faces, and the digest's two
2 Samuel books lifted for reuse (D("A3", 0) is Book One page 3, first panel; "B…" is Book Two)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import samuel4 as S4
from faces_ex import F
from reuse import panels, fill
from discourse import seg, pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from sa2 import G

v, sp = G.v, G.span
def say(ref, frm=None, to=None, after=None): return ("say", v(ref, frm=frm, to=to, after=after))
def gd(ref, frm=None, to=None, after=None): return ("god", v(ref, frm=frm, to=to, after=after))
def cp(ref, frm=None, to=None, after=None): return ("cap", v(ref, frm=frm, to=to, after=after))
def sg(ref, frm=None, to=None): return ("song", v(ref, frm=frm, to=to))
def says(refs): return ("say", sp(refs))
def gods(refs): return ("god", sp(refs))
def caps(refs): return ("cap", sp(refs))
def sgs(refs): return [sg(f"{c}:{x}") for c, x in _refs(refs)]
def _refs(refs):
    a, _, b = refs.partition("-"); c, x = map(int, a.split(":")); y = int(b) if b else x
    return [(c, k) for k in range(x, y + 1)]

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 0.92)
    k.setdefault("min_size", 12.5)
    return _pack(segs, prefix, start, book="2 Samuel", code="2SAM", **k)

_T = S4.tokens()
def tok(name): return _T[f"__FACE_{name}__"]
DAVID, DAVID_BOLD, DAVID_GRIEVED, JONATHAN, SAUL_KING = tok("DAVID"), tok("DAVID_BOLD"), tok("DAVID_GRIEVED"), tok("JONATHAN"), tok("SAUL_KING")
DAVID_KING, DAVID_JOY, DAVID_WRATH, DAVID_GRIEF, DAVID_MOURN = tok("DAVID_KING"), tok("DAVID_KING_JOY"), tok("DAVID_KING_WRATH"), tok("DAVID_KING_GRIEF"), tok("DAVID_MOURN")
NATHAN, NATHAN_STERN, MICHAL, MEPHIBOSHETH = tok("NATHAN"), tok("NATHAN_STERN"), tok("MICHAL"), tok("MEPHIBOSHETH")
ABSALOM, ABSALOM_SLY, DAVID_OLD, DAVID_OLD_ALARM, DAVID_OLD_WEEP, CUSHITE, GAD = (tok("ABSALOM"), tok("ABSALOM_SLY"), tok("DAVID_OLD"), tok("DAVID_OLD_ALARM"),
                                                                              tok("DAVID_OLD_WEEP"), tok("CUSHITE"), tok("GAD"))
# The sons of Zeruiah and the house of Saul
JOAB = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#6A2A1A", cord=True, brow="scowl", light="#D7261E")
ABISHAI = F("adam", skin="#C98E66", shadow="#5A2A1E", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", brow="scowl", light="#9AA8C8")
ABNER = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#5A5A2A", cord=True, light="#FFC14D")
ISHBOSHETH = F("adam", skin="#C98E66", shadow="#5A3A4A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#8A1E2E", band=True, brow="sorrow", sweat=True)
AMALEKITE = F("adam", skin="#9A6A4A", shadow="#4A3A3A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", scarf="#8A6A4A", light="#FF8A3D")
ISRAELITE = F("adam", skin="#C47A5A", shadow="#5A3A2A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#6A5A3A", cord=True, light="#FFC14D")
MESSENGER = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", sweat=True, light="#FFE680")

def face(lines, ref, tok, bg=GOLDEN, **k): return seg(lines, ref, tok=tok, bg=bg, **k)
def drawn(lines, ref, art, bg, **k): return seg(lines, ref, bg=bg, art=art, **k)

_B = {"A": ("digest/2samuel/book-01/", ["SB1-P01-Mourning", "SB1-P02-King", "SB1-P03-Ark", "SB1-P04-Dancing", "SB1-P05-ForEver", "SB1-P06-Mephibosheth",
                                         "SB1-P07-Letter", "SB1-P08-Lamb", "SB1-P09-Man"]),
      "B": ("digest/2samuel/book-02/", ["SB2-P01-Absalom", "SB2-P02-Hearts", "SB2-P03-Flee", "SB2-P04-Olives", "SB2-P05-Gently", "SB2-P06-Oak", "SB2-P07-Tidings",
                                         "SB2-P08-MySon", "SB2-P09-Altar"])}
_cache = {}
def D(page, i, align="xMidYMid"):
    if page not in _cache:
        base, names = _B[page[0]]
        _cache[page] = panels(base + names[int(page[1:]) - 1] + ".dc.html")
    a = _cache[page][i]
    return a.bg, fill(a, align)

def over(lines, ref, page, i, align="xMidYMid", **k):
    bg, art = D(page, i, align)
    return seg(lines, ref, bg=bg, art=art, **k)
