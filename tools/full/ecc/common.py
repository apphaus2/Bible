"""Shared helpers for the Ecclesiastes chapters: line builders for discourse.pack and the Preacher's faces (Solomon old, from
2 Kings' cast)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from discourse import seg, pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from kg2.common import SOLOMON_OLD
from ecc import G

v, sp = G.v, G.span
CODE = "ECCL"
def say(ref, frm=None, to=None, after=None): return ("say", v(ref, frm=frm, to=to, after=after))
def cp(ref, frm=None, to=None, after=None): return ("cap", v(ref, frm=frm, to=to, after=after))
def sg(ref, frm=None, to=None, after=None): return ("song", v(ref, frm=frm, to=to, after=after))
def caps(refs): return ("cap", sp(refs))
def _refs(refs):
    a, _, b = refs.partition("-"); c, x = map(int, a.split(":")); y = int(b) if b else x
    return [f"{c}:{k}" for k in range(x, y + 1)]
def sgs(refs): return [sg(r) for r in _refs(refs)]
def says(refs): return [say(r) for r in _refs(refs)]

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 0.92)
    k.setdefault("min_size", 12.5)
    return _pack(segs, prefix, start, book="Ecclesiastes", code=CODE, **k)

def label(refs):
    a, _, b = refs.partition("-")
    return f"{CODE} {a}" + (f"–{b}" if b else "")

def face(refs, tok, lines=None, bg=GOLDEN, **k):
    """The Preacher's face beside his words: refs "1:8-9" (each verse its own speech box) unless lines are given."""
    return seg(lines or says(refs), label(refs), tok=tok, bg=bg, **k)

def drawn(refs, art, bg, lines=None, **k):
    """Song lines (each verse its own box) over a drawing: words at the top, the drawing below."""
    return seg(lines or sgs(refs), label(refs), bg=bg, art=art, **k)

DUSK = "radial-gradient(circle at 70% 30%, #FFB04A 0 20px, #8A3A5A 200px, #1A1028 420px)"
DAWN = "radial-gradient(circle at 70% 30%, #FFF4C2 0 24px, #8FD0E2 170px, #2A4A6A 420px)"

# the Preacher (Solomon old): grey beard, deep-blue headcloth with the gold band
_P = dict(skin="#C98E66", shadow="#5A3A4A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#1F3A7A", band=True)
PREACHER = SOLOMON_OLD
PREACHER_GOLD = F("adam", light="#FFE680", **_P)
PREACHER_WARM = F("adam", light="#FF8A3D", brow="sorrow", **_P)
PREACHER_STERN = F("adam", light="#D7261E", brow="scowl", **_P)
PREACHER_NIGHT = F("adam", **dict(_P, skin="#9A7A8A", shadow="#3A2A4E"), brow="sorrow", light="#CFE0FF")
