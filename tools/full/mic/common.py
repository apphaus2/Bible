"""Shared helpers for the Micah chapters: the book's Kit (oba.minor) and the prophet's faces."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from oba.minor import Kit, F, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT
from mic import G

K = Kit(G, "MIC", "Micah")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j

# Micah the Morashtite: a grey-black beard, a dark brown headcloth with a cord
_M = dict(skin="#B98A6E", shadow="#4A3A3A", hair="#5A544E", hl="#8A847A", beard=True, beard_color="#5A544E", scarf="#3A2A22", cord=True)
MICAH = F("adam", light="#FFC14D", **_M)
MICAH_GRIEF = F("adam", **dict(_M, skin="#9A8A9A", shadow="#3A3A5E"), brow="sorrow", tear=True, light="#CFE0FF")
MICAH_STERN = F("adam", brow="scowl", light="#D7261E", **_M)
MICAH_GOLD = F("adam", light="#FFE680", **_M)
WORSHIPPER = F("adam", skin="#C98E66", shadow="#5A3A4A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#5A4A6A", cord=True, brow="sorrow", light="#FFC14D")
