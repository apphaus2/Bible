"""Shared helpers for the Nahum chapter: the book's Kit (oba.minor) and the prophet's faces."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from oba.minor import Kit, F, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT
from nam import G

K = Kit(G, "NAH", "Nahum")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j

# Nahum the Elkoshite: a grey beard, a charcoal headcloth with a cord
_N = dict(skin="#C98E66", shadow="#4A3A4A", hair="#9A948A", hl="#C8C2B6", beard=True, beard_color="#A8A29A", scarf="#2A2A3A", cord=True)
NAHUM = F("adam", light="#FFC14D", **_N)
NAHUM_STERN = F("adam", brow="scowl", light="#D7261E", **_N)
NAHUM_STORM = F("adam", **dict(_N, skin="#9A8A9A", shadow="#3A3A5E"), light="#CFE0FF")
