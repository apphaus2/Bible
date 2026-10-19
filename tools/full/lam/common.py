"""Shared helpers for the Lamentations chapters: song lines for the laments (lament: one song box per verse, panels of whole
verses over drawings or beside a mourner's face), and the mourners' faces."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from discourse import seg
from jer.pagepack import pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from jos.art import below
from lam import G

v, sp = G.v, G.span
CODE = "LAM"

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 0.92)
    k.setdefault("min_size", 12.5)
    return _pack(segs, prefix, start, book="Lamentations", code=CODE, **k)

def label(c, a, b):
    return f"{CODE} {c}:{a}" + (f"–{b}" if b != a else "")

def songs(c, a, b):
    """One song box per verse, c:a–b, every word."""
    return [("song", v(f"{c}:{x}")) for x in range(a, b + 1)]

def L(c, a, b=None, d=None, t=None, k=0.5, **kw):
    """One panel of the lament c:a–b as song lines; d = (bg, fn) sets them over a drawing (below(fn, k)), t = (face, bg) beside
    a mourner's face."""
    b = b or a
    if d:
        bg, fn = d
        return seg(songs(c, a, b), label(c, a, b), bg=bg, art=below(fn, k) if k else fn, hi=20, **kw)
    return seg(songs(c, a, b), label(c, a, b), tok=t[0], bg=t[1], hi=20, **kw)

# the mourners
ZION = F("eve", skin="#B98A6E", shadow="#3A2A3A", hair="#3A3430", scarf="#5A5A6A", brow="sorrow", tear=True, light="#9AA8C8")
ZION_PLEA = F("eve", skin="#C98E66", shadow="#4A3A4A", hair="#3A3430", scarf="#5A5A6A", brow="sorrow", light="#FFE680")
MOURNER = F("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#A8A29A", scarf="#3A3434", brow="sorrow", tear=True, light="#9AA8C8")
MOURNER_HOPE = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#A8A29A", scarf="#3A3434", light="#FFE680")
ELDER = F("adam", skin="#A88A7A", shadow="#3A2A3A", hair="#C8C2B6", hl="#E8E2D6", beard=True, beard_color="#D8D2C6", scarf="#4A4038", brow="sorrow", light="#9AA8C8")
