"""Shared helpers for the Haggai chapter: the book's Kit (oba.minor) and the cast's faces — Haggai, Zerubbabel and Joshua
(Jeshua) the high priest as in Ezra (ezr.common)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from oba.minor import Kit, F, COLD, GOLDEN, RED, DUSK, DAWN, NIGHT
from ezr.common import HAGGAI, ZERUBBABEL, JESHUA
from hag import G

K = Kit(G, "HAG", "Haggai")
cp, gd, sg, sy, cps, gds, sgs, j = K.cp, K.gd, K.sg, K.sy, K.cps, K.gds, K.sgs, K.j

# Haggai (ezr.common.HAGGAI: grey beard, a violet headcloth with a cord) in other lights
_H = dict(skin="#B98A6E", shadow="#3A3A5A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#4A3A6A", cord=True)
HAGGAI_STERN = F("adam", brow="scowl", light="#D7261E", **_H)
HAGGAI_GOLD = F("adam", light="#FFE680", **_H)
# the priests asked concerning the law: a white headcloth, a grey beard
PRIEST = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#6A645E", hl="#9A948A", beard=True, beard_color="#7A746A", scarf="#F3EFE6", cord=True, light="#FFC14D")
