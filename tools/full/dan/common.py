"""Shared helpers for the Daniel chapters: the speakers (name and colour), the line and panel builders (dan.kit.Lines), and
the cast's faces.

Daniel: a blue headcloth with a dark cord; a youth (stubble) in chapter 1, black-bearded in 2–5, greying in 6, grey in the
visions of 7–12. Nebuchadnezzar: black curled beard, a deep red headcloth with a gold band. Belshazzar: young, stubble,
purple with the gold band. Darius the Mede: grey beard, crimson with the band. Hananiah, Mishael and Azariah (Shadrach,
Meshach and Abed-nego): rust, green and teal headcloths. The Chaldeans: black beards, violet headcloths, kohl."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from dan.kit import Lines, NIGHT
from dan import G

SPK = {"daniel": ("DANIEL", "#1F5FAD"), "king": ("NEBUCHADNEZZAR", "#C8962E"), "chald": ("THE CHALDEANS", "#7A3BA8"),
       "eunuch": ("THE PRINCE OF THE EUNUCHS", "#8A8A4A"), "arioch": ("ARIOCH", "#B5421E"), "three": ("SHADRACH, MESHACH AND ABED-NEGO", "#2E8A6A"),
       "herald": ("THE HERALD", "#8A6A3A"), "counsel": ("HIS COUNSELLORS", "#6A6A8A"), "belsh": ("BELSHAZZAR", "#7A2A8A"),
       "queen": ("THE QUEEN", "#B8862E"), "darius": ("DARIUS", "#A8283A"), "princes": ("THE PRESIDENTS AND THE SATRAPS", "#6A4A3A"),
       "watcher": ("A WATCHER, A HOLY ONE", "#D8A820"), "voice": ("A VOICE FROM HEAVEN", "#D8A820"), "angel": ("ONE THAT STOOD BY", "#D8A820"),
       "holy": ("A HOLY ONE", "#D8A820"), "gabriel": ("GABRIEL", "#D8A820"), "linen": ("THE MAN CLOTHED IN LINEN", "#D8A820"),
       "touch": ("ONE LIKE THE SONS OF MEN", "#D8A820"), "ulai": ("A MAN'S VOICE", "#D8A820")}
L = Lines(G, "DAN", "Daniel", SPK)
v, sp = G.v, G.span

# ---- the cast ---------------------------------------------------------------------------------------------------------
_DAN = dict(scarf="#1F4A8A", cord=True)
DANIEL_Y = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#1A1210", hl="#4A3A2E", stubble="#2A1A10", light="#FFE680", **_DAN)
DANIEL_Y_PRAY = F("adam", skin="#C9A28A", shadow="#3A3A5A", hair="#1A1210", hl="#4A3A2E", stubble="#2A1A10", light="#FFF4C2", **_DAN)
_D1 = dict(skin="#D9A27A", shadow="#6A4A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", **_DAN)
DANIEL = F("adam", light="#FFE680", **_D1)
DANIEL_PRAY = F("adam", **dict(_D1, skin="#C9A28A", shadow="#3A3A5A"), light="#FFF4C2")
DANIEL_STERN = F("adam", brow="scowl", light="#FF8A3D", **_D1)
_D2 = dict(skin="#C98E66", shadow="#5A4A4A", hair="#5A544E", hl="#8A847A", beard=True, beard_color="#6A645E", **_DAN)
DANIEL_GREY = F("adam", light="#FFE680", **_D2)
DANIEL_GREY_PRAY = F("adam", **dict(_D2, skin="#B9A08E", shadow="#3A3A5A"), light="#FFF4C2")
_D3 = dict(skin="#C08A66", shadow="#4A3A4A", hair="#A8A29A", hl="#D8D2C6", beard=True, beard_color="#B8B2A8", **_DAN)
DANIEL_OLD = F("adam", light="#FFE680", **_D3)
DANIEL_OLD_PRAY = F("adam", **dict(_D3, skin="#B0988A", shadow="#3A3A5A"), light="#FFF4C2")
DANIEL_OLD_AWE = F("adam", **dict(_D3, skin="#A8A0AE", shadow="#2A2A4A"), brow="sorrow", sweat=True, light="#9FB8FF")
DANIEL_OLD_GRIEF = F("adam", **dict(_D3, skin="#A8A0AE", shadow="#2A2A4A"), brow="sorrow", tear=True, light="#9AA8C8")

_NEB = dict(skin="#C98E66", shadow="#5A3A3A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#1A2A5A", band=True)
NEB = F("adam", light="#FFC14D", **_NEB)
NEB_TROUBLED = F("adam", **dict(_NEB, skin="#A89AA8", shadow="#2A2A4A"), brow="sorrow", sweat=True, light="#9FB8FF")
NEB_ANGRY = F("adam", **dict(_NEB, skin="#C47A5A", shadow="#4A1A1A"), brow="scowl", light="#D7261E")
NEB_AWE = F("adam", **dict(_NEB, skin="#C9A28A"), brow="sorrow", light="#FFE680")
_NEB_W = dict(skin="#B08A6E", shadow="#4A3A3A", hair="#5A544E", hl="#8A847A", beard=True, beard_color="#4A4440")
NEB_RESTORED = F("adam", light="#FFE680", scarf="#1A2A5A", band=True, **_NEB_W)
_BEL = dict(skin="#D9A27A", shadow="#5A3A4A", hair="#0D0D0F", hl="#2A2220", stubble="#1A1210", scarf="#5A1A6A", band=True)
BELSH = F("adam", laugh=True, light="#FFC14D", **_BEL)
BELSH_AFRAID = F("adam", **dict(_BEL, skin="#B8A8B0", shadow="#2A2A4A"), brow="sorrow", sweat=True, light="#E8ECF8")
BELSH_KING = F("adam", light="#FFC14D", **_BEL)
QUEEN = F("eve", skin="#D9A27A", shadow="#6A3A4A", hair="#3A3430", scarf="#1F5A6A", band=True, kohl=True, light="#FFE680")
_DAR = dict(skin="#C98E66", shadow="#4A3A4A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#2A3A3A", band=True)
DARIUS = F("adam", light="#FFC14D", **_DAR)
DARIUS_GRIEF = F("adam", **dict(_DAR, skin="#B0A0A0", shadow="#2A2A4A"), brow="sorrow", light="#9AA8C8")
DARIUS_GLAD = F("adam", light="#FFE680", laugh=True, **_DAR)
ASHPENAZ = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#1A1210", hl="#4A3A2E", scarf="#E8E2D6", band=True, brow="sorrow", sweat=True, light="#FFC14D")
STEWARD = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#1A1210", hl="#4A3A2E", scarf="#8A8A4A", cord=True, light="#FFE680")
ARIOCH = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#3A3A3A", cord=True, brow="scowl", light="#D7261E")
CHALDEAN = F("adam", skin="#C98E66", shadow="#3A2A4A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#4A2A6A", band=True, kohl=True, brow="sorrow", sweat=True, light="#B89AFF")
CHALDEAN_SLY = F("adam", skin="#C98E66", shadow="#3A2A4A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#4A2A6A", band=True, kohl=True, brow="scowl", light="#B89AFF")
SHADRACH = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#5A2A1A", cord=True, light="#FFC14D")
MESHACH = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", scarf="#2E7A3A", cord=True, light="#FFE680")
ABEDNEGO = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#1F7A8A", cord=True, light="#FFE680")
SATRAP = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#2A3A5A", band=True, brow="scowl", light="#D7261E")
