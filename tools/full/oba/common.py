"""Shared helpers for the Obadiah chapter: the book's Kit (oba.minor) and the prophet's faces."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from oba.minor import Kit, F, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT
from oba import G

K = Kit(G, "OBAD", "Obadiah")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j

# Obadiah: a black beard, a dark green headcloth with a cord
_O = dict(skin="#C98E66", shadow="#5A3A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#2E4A3A", cord=True)
OBADIAH = F("adam", light="#FFC14D", **_O)
OBADIAH_NIGHT = F("adam", **dict(_O, skin="#9A7A8A", shadow="#3A2A4E"), brow="scowl", light="#CFE0FF")
OBADIAH_GLAD = F("adam", light="#FFE680", **_O)
