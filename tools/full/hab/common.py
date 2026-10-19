"""Shared helpers for the Habakkuk chapter: the book's Kit (oba.minor) and the prophet's faces."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from oba.minor import Kit, F, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT
from hab import G

K = Kit(G, "HAB", "Habakkuk")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j

# Habakkuk: white hair and beard, an indigo headcloth with a cord
_H = dict(skin="#C98E66", shadow="#4A3A4A", hair="#E8E2D6", hl="#F3EFE6", beard=True, beard_color="#E8E2D6", scarf="#2A2A5A", cord=True)
HABAKKUK = F("adam", light="#FFC14D", **_H)
HABAKKUK_GRIEF = F("adam", **dict(_H, skin="#9A8A9A", shadow="#3A3A5E"), brow="sorrow", tear=True, light="#CFE0FF")
HABAKKUK_TREMBLE = F("adam", **dict(_H, skin="#9A8A9A", shadow="#3A3A5E"), brow="sorrow", sweat=True, light="#CFE0FF")
HABAKKUK_GLAD = F("adam", light="#FFE680", **_H)
