"""Shared helpers for the Joshua chapters: line builders for discourse.pack, the cast's faces, and the digest's Jericho
panels lifted for reuse (D["P02"][3] is the second digest page's fourth panel, as f(w, h) drawings with their bg)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import joshua1 as J, numbers1 as N
from faces_ex import F
from reuse import panels, fill
from discourse import seg, pack as _pack
from jos import G

v, sp = G.v, G.span
def say(ref, frm=None, to=None): return ("say", v(ref, frm=frm, to=to))
def gd(ref, frm=None, to=None): return ("god", v(ref, frm=frm, to=to))
def cp(ref, frm=None, to=None): return ("cap", v(ref, frm=frm, to=to))
def says(refs): return ("say", sp(refs))
def gods(refs): return ("god", sp(refs))
def caps(refs): return ("cap", sp(refs))

def pack(segs, prefix, start, **k):
    return _pack(segs, prefix, start, book="Joshua", code="JOSH", **k)

# ---- faces --------------------------------------------------------------------------------------------------------------
_T = J.tokens()
JOSHUA, JOSHUA_AWE, JOSHUA_OLD, RAHAB = _T["__FACE_JOSHUA_LEAD__"], _T["__FACE_JOSHUA_AWE__"], _T["__FACE_JOSHUA_OLD__"], _T["__FACE_RAHAB__"]
CALEB, SPY = _T["__FACE_CALEB__"], _T["__FACE_SPY__"]
JOSHUA_CALM = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#2A1A10", hl="#6A5A4E", beard=True, scarf="#B5421E", cord=True, light="#FFE680")
JOSHUA_GRIEF = F("adam", skin="#B98A7E", shadow="#4A3A5A", hair="#2A1A10", hl="#6A5A4E", beard=True, scarf="#B5421E", cord=True, brow="sorrow", light="#9AA8C8")
SPY2 = F("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", stubble="#2A1A10", sweat=True, light="#FFC14D")
ACHAN = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#5A4A3A", cord=True, brow="sorrow", sweat=True, light="#9AA8C8")
GIBEONITE = F("adam", skin="#B98A6E", shadow="#5A4A3A", hair="#8A8478", hl="#6A645E", beard=True, beard_color="#8A8478", scarf="#7A6A5A", light="#FFE680")
KING_CANAAN = F("adam", skin="#B98A6E", shadow="#4A1A26", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#3A2A5A", band=True, brow="scowl", light="#D7261E")
ELEAZAR = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#B8B2A6", hl="#8A867E", beard=True, beard_color="#B8B2A6", scarf="#F3EFE6", band=True, light="#FFE680")
PHINEHAS = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#F3EFE6", band=True, light="#FFE680")
CALEB_OLD = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#D8D2C6", hl="#A8A296", beard=True, beard_color="#D8D2C6", scarf="#2E6B3A", cord=True, light="#FFC14D")
REUBENITE = F("adam", skin="#C47A5A", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#C8202A", cord=True, light="#FFC14D")

# moods for discourse segments: (face, background)
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
MOODS = {"calm": (JOSHUA_CALM, GOLDEN), "lead": (JOSHUA, RED), "awe": (JOSHUA_AWE, GOLDEN), "grief": (JOSHUA_GRIEF, COLD), "old": (JOSHUA_OLD, GOLDEN)}

# ---- the digest's Joshua Book One, lifted -------------------------------------------------------------------------------
_B = "digest/joshua/book-01/"
_NAMES = {"P01": "JO1-P01-Strong", "P02": "JO1-P02-Rahab", "P03": "JO1-P03-Jordan", "P04": "JO1-P04-Prince", "P05": "JO1-P05-Compass",
          "P06": "JO1-P06-Wall", "P07": "JO1-P07-Sun", "P08": "JO1-P08-Choose"}
_cache = {}
def D(page, i):
    """(bg, f(w, h)) for panel i of a digest page, for seg(..., bg=, art=)."""
    if page not in _cache: _cache[page] = panels(_B + _NAMES[page] + ".dc.html")
    a = _cache[page][i]
    return a.bg, fill(a)

def over(lines, ref, page, i, **k):
    """A segment with its words over a lifted digest panel."""
    bg, art = D(page, i)
    return seg(lines, ref, bg=bg, art=art, **k)

def face(lines, ref, mood_or_tok, bg=None, **k):
    """A segment beside a close-up face: a Joshua mood name, or (face token) with bg."""
    if isinstance(mood_or_tok, str) and mood_or_tok in MOODS:
        tok, b = MOODS[mood_or_tok]
    else:
        tok, b = mood_or_tok, GOLDEN
    return seg(lines, ref, tok=tok, bg=bg or b, **k)

def drawn(lines, ref, art, bg, **k):
    return seg(lines, ref, bg=bg, art=art, **k)
