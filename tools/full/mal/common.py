"""Shared helpers for the Malachi chapter: the book's Kit (oba.minor) and the prophet's faces."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from oba.minor import Kit, F, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT
from mal import G

K = Kit(G, "MAL", "Malachi")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j

# Malachi: young, stubble, an off-white headcloth with a dark cord
_M = dict(skin="#D9A27A", shadow="#6A4A3A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#E8E2D6", cord=True)
MALACHI = F("adam", light="#FFC14D", **_M)
MALACHI_STERN = F("adam", brow="scowl", light="#D7261E", **_M)
MALACHI_GRIEF = F("adam", **dict(_M, skin="#9A8A9A", shadow="#3A3A5E"), brow="sorrow", light="#CFE0FF")
MALACHI_GOLD = F("adam", light="#FFE680", **_M)
