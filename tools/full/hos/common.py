"""Shared helpers for the Hosea chapters: the speakers, the line and panel builders (dan.kit.Lines), and the faces.

Hosea: an olive headcloth with a dark cord, black beard (grieving: cold light and a tear). Gomer: a dark plum headscarf
with a woven gold hem, black hair. The people's words (6:1–3, 14:2–3) are tagged THE PEOPLE."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from exo.art import HEM
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from dan.kit import Lines, NIGHT
from hos import G

SPK = {"hosea": ("HOSEA", "#5E7A2A"), "people": ("THE PEOPLE", "#8A6A3A"), "jehovah": ("JEHOVAH", "#12113A")}
L = Lines(G, "HOS", "Hosea", SPK)
v, sp = G.v, G.span

_H = dict(skin="#C98E66", shadow="#5A4A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#3A4A22", cord=True)
HOSEA = F("adam", light="#FFE680", **_H)
HOSEA_GRIEF = F("adam", **dict(_H, skin="#B0988A", shadow="#3A3A5A"), brow="sorrow", tear=True, light="#9AA8C8")
HOSEA_STERN = F("adam", brow="scowl", light="#D7261E", **_H)
HOSEA_WORD = F("adam", **dict(_H, skin="#C9A28A"), light="#FFF4C2")
GOMER = F("eve", skin="#D9A27A", shadow="#6A3A4A", hair="#0D0D0F", scarf="#3A1A3A", light="#FFC14D") + HEM
GOMER_SAD = F("eve", skin="#B8A0A0", shadow="#3A2A4A", hair="#0D0D0F", scarf="#3A1A3A", brow="sorrow", light="#9AA8C8") + HEM
