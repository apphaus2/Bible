"""Shared helpers for the Ruth chapters: line builders, the cast's faces, and the digest's Ruth book lifted for reuse."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import ruth1 as R
from faces_ex import F
from reuse import panels, fill
from discourse import seg, pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from rut import G

v, sp = G.v, G.span
def say(ref, frm=None, to=None): return ("say", v(ref, frm=frm, to=to))
def gd(ref, frm=None, to=None): return ("god", v(ref, frm=frm, to=to))
def cp(ref, frm=None, to=None): return ("cap", v(ref, frm=frm, to=to))
def says(refs): return ("say", sp(refs))
def caps(refs): return ("cap", sp(refs))

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    return _pack(segs, prefix, start, book="Ruth", code="RUTH", **k)

_T = R.tokens()
def tok(name): return _T[f"__FACE_{name}__"]
NAOMI, MARA, NAOMI_JOY, RUTH, RUTH_WEEP, ORPAH, BOAZ = (tok(n) for n in ("NAOMI", "MARA", "NAOMI_JOY", "RUTH", "RUTH_WEEP", "ORPAH", "BOAZ"))
KINSMAN = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#6A5A3A", cord=True, light="#FFC14D")
REAPER = F("adam", skin="#B9785A", shadow="#5A3A2A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", light="#FFE680")
NEIGHBOR = F("eve", skin="#D9A27A", shadow="#8A5A3E", hair="#3A2214", scarf="#5AC8C8", light="#FFE680")

def face(lines, ref, tok, bg=GOLDEN, **k): return seg(lines, ref, tok=tok, bg=bg, **k)
def drawn(lines, ref, art, bg, **k): return seg(lines, ref, bg=bg, art=art, **k)

_NAMES = {"P01": "RU1-P01-Moab", "P02": "RU1-P02-Return", "P03": "RU1-P03-Whither", "P04": "RU1-P04-Mara", "P05": "RU1-P05-Field",
          "P06": "RU1-P06-Wings", "P07": "RU1-P07-Threshing", "P08": "RU1-P08-Obed"}
_cache = {}
def D(page, i, align="xMidYMid"):
    """(bg, f(w, h)) for panel i of a page of the digest's Ruth book."""
    if page not in _cache: _cache[page] = panels("digest/ruth/book-01/" + _NAMES[page] + ".dc.html")
    a = _cache[page][i]
    return a.bg, fill(a, align)

def over(lines, ref, page, i, align="xMidYMid", **k):
    bg, art = D(page, i, align)
    return seg(lines, ref, bg=bg, art=art, **k)
