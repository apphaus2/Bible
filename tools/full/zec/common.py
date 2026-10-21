"""Shared helpers for the Zechariah chapters: the book's Kit (oba.minor) and the cast's faces — Zechariah, Joshua (Jeshua)
and Zerubbabel as in Ezra (ezr.common)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from oba.minor import Kit, F, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT
from ezr.common import ZECHARIAH, ZERUBBABEL, JESHUA
from zec import G

K = Kit(G, "ZECH", "Zechariah")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j

# Zechariah (ezr.common.ZECHARIAH: black beard, a slate-teal headcloth with a cord) in other lights
_Z = dict(skin="#D9A27A", shadow="#4A3A4A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#3A5A6A", cord=True)
ZECH_NIGHT = F("adam", **dict(_Z, skin="#9A8AA0", shadow="#3A3A5E"), light="#CFE0FF")
ZECH_AWE = F("adam", **dict(_Z, skin="#9A8AA0", shadow="#3A3A5E"), sweat=True, brow="sorrow", light="#FFE680")
ZECH_STERN = F("adam", brow="scowl", light="#D7261E", **_Z)
ZECH_GOLD = F("adam", light="#FFE680", **_Z)
# the men of Bethel (7:2–3): Sharezer, a dark slate headcloth with a cord; the shepherd's face is Zechariah's own (11:4–17)
SHAREZER = F("adam", skin="#C98E66", shadow="#5A3A3A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E", scarf="#3A4048", cord=True, light="#FFC14D")
