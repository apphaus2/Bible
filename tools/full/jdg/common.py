"""Shared helpers for the Judges chapters: line builders for discourse.pack, the cast's faces, and the digest's two Judges
books lifted for reuse (D("A3", 0) is Book One page 3, first panel; "B…" is Book Two, Samson)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import judges1 as J1, judges2 as J2
from faces_ex import F
from reuse import panels, fill
from discourse import seg, pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from genesis.ch02 import NIGHT
from jdg import G

v, sp = G.v, G.span
def say(ref, frm=None, to=None): return ("say", v(ref, frm=frm, to=to))
def gd(ref, frm=None, to=None): return ("god", v(ref, frm=frm, to=to))
def cp(ref, frm=None, to=None): return ("cap", v(ref, frm=frm, to=to))
def sg(ref, frm=None, to=None): return ("song", v(ref, frm=frm, to=to))
def says(refs): return ("say", sp(refs))
def gods(refs): return ("god", sp(refs))
def caps(refs): return ("cap", sp(refs))
def songs(refs): return [("song", v(f"{refs.split(':')[0]}:{n}")) for n in range(int(refs.split(':')[1].split('-')[0]), int(refs.split('-')[-1]) + 1)]

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    return _pack(segs, prefix, start, book="Judges", code="JDG", **k)

# ---- faces --------------------------------------------------------------------------------------------------------------
_T = {**J1.tokens(), **J2.tokens()}
def tok(name): return _T[f"__FACE_{name}__"]
DEBORAH, BARAK, BARAK_BOLD, JAEL = tok("DEBORAH"), tok("BARAK"), tok("BARAK_BOLD"), tok("JAEL")
GIDEON, GIDEON_BOLD, GIDEON_CALM = tok("GIDEON"), tok("GIDEON_BOLD"), tok("GIDEON_CALM")
SAMSON, SAMSON_SLEEP, SAMSON_PRAY, DELILAH, MANOAH_WIFE = tok("SAMSON"), tok("SAMSON_SLEEP"), tok("SAMSON_PRAY"), tok("DELILAH"), tok("MANOAH_WIFE")
KING_CANAAN = F("adam", skin="#B98A6E", shadow="#4A1A26", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#3A2A5A", band=True, brow="scowl", light="#D7261E")
ISRAELITE = F("adam", skin="#C47A5A", shadow="#5A3A2A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#6A5A3A", cord=True, light="#FFC14D")
CALEB_OLD = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#D8D2C6", hl="#A8A296", beard=True, beard_color="#D8D2C6", scarf="#2E6B3A", cord=True, light="#FFC14D")
GIDEON_OLD = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#B8B2A6", hl="#8A867E", beard=True, beard_color="#B8B2A6", scarf="#C9A86A", cord=True, light="#FFE680")
ABIMELECH = F("adam", skin="#C47A5A", shadow="#4A1A26", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#5A1A3A", band=True, brow="scowl", light="#D7261E")
JOTHAM = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", light="#FFE680")
GAAL = F("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#8A6A2A", cord=True, light="#FF8A3D")
ZEBUL = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#6A6460", hl="#8A867E", beard=True, beard_color="#6A6460", scarf="#2A4A5A", cord=True, light="#9AA8C8")
KING_MIDIAN = F("adam", skin="#B98A6E", shadow="#4A1A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#6A2A7A", band=True, light="#FFC14D")
ACHSAH = F("eve", skin="#C98E66", shadow="#8A5A3E", hair="#1A1210", scarf="#C8A030", light="#FFE680")

def over(lines, ref, page, i, **k):
    """A segment with its words over a lifted digest panel."""
    bg, art = D(page, i)
    return seg(lines, ref, bg=bg, art=art, **k)

def face(lines, ref, tok, bg=GOLDEN, **k):
    return seg(lines, ref, tok=tok, bg=bg, **k)

def drawn(lines, ref, art, bg, **k):
    return seg(lines, ref, bg=bg, art=art, **k)

# ---- the digest's Judges books, lifted ----------------------------------------------------------------------------------
_B = {"A": ("digest/judges/book-01/", ["JG1-P01-Deborah", "JG1-P02-Tabor", "JG1-P03-Jael", "JG1-P04-Valor", "JG1-P05-Fleece", "JG1-P06-Three", "JG1-P07-Sword", "JG1-P08-Rule"]),
      "B": ("digest/judges/book-02/", ["JG2-P01-Nazirite", "JG2-P02-Lion", "JG2-P03-Foxes", "JG2-P04-Jawbone", "JG2-P05-Gaza", "JG2-P06-Delilah", "JG2-P07-Shaven", "JG2-P08-Pillars"])}
_cache = {}
def D(page, i):
    """(bg, f(w, h)) for panel i of a digest page: "A1".."A8" (Deborah, Gideon), "B1".."B8" (Samson)."""
    if page not in _cache:
        base, names = _B[page[0]]
        _cache[page] = panels(base + names[int(page[1:]) - 1] + ".dc.html")
    a = _cache[page][i]
    return a.bg, fill(a)
