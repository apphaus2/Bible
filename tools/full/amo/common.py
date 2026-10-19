"""Shared helpers for the Amos volume: the speakers, the line and panel builders (dan.kit.Lines), and the faces.

Amos, the herdsman of Tekoa: sun-browned, black beard, a brown herdsman's headcloth with a cord (stern: red light).
Amaziah the priest of Beth-el: grey beard, a white headcloth with a gold band, scowling."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from dan.kit import Lines, NIGHT
from amo import G

SPK = {"amos": ("AMOS", "#8A5A2A"), "amaziah": ("AMAZIAH THE PRIEST OF BETH-EL", "#5A3A7A"), "people": ("THEY SAY", "#6A6A6A")}
L = Lines(G, "AMOS", "Amos", SPK)
v, sp = G.v, G.span

_A = dict(skin="#B9784E", shadow="#5A3A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#6A4A2A", cord=True)
AMOS = F("adam", light="#FFE680", **_A)
AMOS_STERN = F("adam", brow="scowl", light="#D7261E", **_A)
AMOS_GRIEF = F("adam", **dict(_A, skin="#A88A7A", shadow="#3A3A5A"), brow="sorrow", tear=True, light="#9AA8C8")
AMOS_PRAY = F("adam", **dict(_A, skin="#A88A7A", shadow="#3A3A5A"), brow="sorrow", sweat=True, light="#FFF4C2")
AMAZIAH = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#F3EFE6", band=True, brow="scowl", light="#B89AFF")
