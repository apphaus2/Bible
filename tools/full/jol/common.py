"""Shared helpers for the Joel volume: the speakers, the line and panel builders (dan.kit.Lines), and the faces.

Joel: a dark teal headcloth with a cord, brown beard (calling: warm light; lamenting: cold light and a tear)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from dan.kit import Lines, NIGHT
from jol import G

SPK = {"joel": ("JOEL", "#2A7A7A"), "priests": ("THE PRIESTS", "#8A6A3A")}
L = Lines(G, "JOEL", "Joel", SPK)
v, sp = G.v, G.span

_J = dict(skin="#C98E66", shadow="#5A4A3A", hair="#3A2A1A", hl="#6A5A4A", beard=True, beard_color="#4A3424", scarf="#1F4A4A", cord=True)
JOEL = F("adam", light="#FFE680", **_J)
JOEL_CRY = F("adam", brow="scowl", light="#D7261E", **_J)
JOEL_GRIEF = F("adam", **dict(_J, skin="#B0988A", shadow="#3A3A5A"), brow="sorrow", tear=True, light="#9AA8C8")
JOEL_GLAD = F("adam", **dict(_J, skin="#D9A27A"), light="#FFF4C2")
