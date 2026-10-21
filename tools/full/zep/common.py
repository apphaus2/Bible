"""Shared helpers for the Zephaniah chapter: the book's Kit (oba.minor) and the prophet's faces."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from oba.minor import Kit, F, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT
from zep import G

K = Kit(G, "ZEPH", "Zephaniah")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j

# Zephaniah, of the line of Hezekiah: a black beard, a plum headcloth with a cord
_Z = dict(skin="#D9A27A", shadow="#5A3A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#5A2A4A", cord=True)
ZEPHANIAH = F("adam", light="#FFC14D", **_Z)
ZEPHANIAH_STERN = F("adam", brow="scowl", light="#D7261E", **_Z)
ZEPHANIAH_GLAD = F("adam", light="#FFE680", **_Z)
