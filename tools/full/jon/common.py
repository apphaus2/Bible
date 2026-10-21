"""Shared helpers for the Jonah chapters: the book's Kit (oba.minor) and the cast's faces."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from oba.minor import Kit, F, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT
from jon import G

K = Kit(G, "JONAH", "Jonah")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j

# Jonah: brown beard, a sea-blue headcloth with a cord
_J = dict(skin="#C98E66", shadow="#5A3A3A", hair="#4A2A1A", hl="#7A5A3E", beard=True, beard_color="#4A2A1A", scarf="#1F5A7A", cord=True)
JONAH = F("adam", light="#FFC14D", **_J)
JONAH_STORM = F("adam", **dict(_J, skin="#9A8A9A", shadow="#3A3A5E"), brow="sorrow", sweat=True, light="#CFE0FF")
JONAH_ANGRY = F("adam", brow="scowl", light="#D7261E", **_J)
JONAH_FAINT = F("adam", brow="sorrow", sweat=True, light="#FFE680", **_J)
# the shipmaster: weathered, grey beard, a charcoal headcloth; a mariner: bareheaded, stubble
SHIPMASTER = F("adam", skin="#A8704E", shadow="#3A2A3A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#3A3A4A", cord=True, brow="sorrow", sweat=True, light="#CFE0FF")
MARINER = F("adam", skin="#A8704E", shadow="#3A2A3A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", brow="scowl", sweat=True, light="#CFE0FF")
# the king of Nineveh in sackcloth: black beard, a sackcloth hood over the gold band
KING_SACK = F("adam", skin="#B9785A", shadow="#4A2A2A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#6A5A48", band=True, brow="sorrow", light="#9AA8C8")
