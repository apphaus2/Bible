"""Shared helpers for the 1 Samuel chapters: line builders for discourse.pack, the cast's faces, and the digest's two
1 Samuel books lifted for reuse (D("A3", 0) is Book One page 3, first panel; "B…" is Book Two)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import samuel1 as S1, samuel2 as S2
from faces_ex import F
from reuse import panels, fill
from discourse import seg, pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from sa1 import G

v, sp = G.v, G.span
def say(ref, frm=None, to=None): return ("say", v(ref, frm=frm, to=to))
def gd(ref, frm=None, to=None): return ("god", v(ref, frm=frm, to=to))
def cp(ref, frm=None, to=None): return ("cap", v(ref, frm=frm, to=to))
def sg(ref, frm=None, to=None): return ("song", v(ref, frm=frm, to=to))
def says(refs): return ("say", sp(refs))
def gods(refs): return ("god", sp(refs))
def caps(refs): return ("cap", sp(refs))

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 0.92)
    return _pack(segs, prefix, start, book="1 Samuel", code="1SAM", **k)

_T = {**S1.tokens(), **S2.tokens()}
def tok(name): return _T[f"__FACE_{name}__"]
HANNAH, HANNAH_JOY, ELI, ELI_AWE = tok("HANNAH"), tok("HANNAH_JOY"), tok("ELI"), tok("ELI_AWE")
SAMUEL_CHILD, SAMUEL_NIGHT, SAMUEL_OLD, SAMUEL_GRIEVED = tok("SAMUEL_CHILD"), tok("SAMUEL_NIGHT"), tok("SAMUEL_OLD"), tok("SAMUEL_GRIEVED")
SAUL, SAUL_ANOINTED, SAUL_KING, SAUL_MAD, SAUL_WEEP = tok("SAUL"), tok("SAUL_ANOINTED"), tok("SAUL_KING"), tok("SAUL_MAD"), tok("SAUL_WEEP")
DAVID, DAVID_BOLD, DAVID_GRIEVED, GOLIATH, JONATHAN, JESSE = tok("DAVID"), tok("DAVID_BOLD"), tok("DAVID_GRIEVED"), tok("GOLIATH"), tok("JONATHAN"), tok("JESSE")
ELKANAH = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#2A6A5A", cord=True, light="#FFC14D")
ISRAELITE = F("adam", skin="#C47A5A", shadow="#5A3A2A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#6A5A3A", cord=True, light="#FFC14D")
PHILISTINE = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", scarf="#1F5FAD", band=True, brow="scowl", light="#D7261E")
MAN_OF_GOD = F("adam", skin="#B98A6E", shadow="#3A3A5A", hair="#C8C2B6", hl="#8A867E", beard=True, beard_color="#C8C2B6", scarf="#3A3A5A", light="#9AA8C8")

def face(lines, ref, tok, bg=GOLDEN, **k): return seg(lines, ref, tok=tok, bg=bg, **k)
def drawn(lines, ref, art, bg, **k): return seg(lines, ref, bg=bg, art=art, **k)

_B = {"A": ("digest/1samuel/book-01/", ["SA1-P01-Hannah", "SA1-P02-Asked", "SA1-P03-HereAmI", "SA1-P04-Speak", "SA1-P05-Taken", "SA1-P06-Dagon", "SA1-P07-Kine", "SA1-P08-King", "SA1-P09-Anointed"]),
      "B": ("digest/1samuel/book-02/", ["SA2-P01-Youngest", "SA2-P02-Anoint", "SA2-P03-Goliath", "SA2-P04-LivingGod", "SA2-P05-Stones", "SA2-P06-Name", "SA2-P07-Stone", "SA2-P08-Jonathan", "SA2-P09-Cave", "SA2-P10-Gilboa"])}
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
