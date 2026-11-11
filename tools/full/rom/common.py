"""Shared helpers for the Romans chapters: the letter's kit (epistle.EpistleKit), its line builders and panels, Paul's
faces in his five lights (from epistle), and Romans' own cast (Tertius, Phoebe), each the same in every chapter."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     nxt, fin, face_of, TERTIUS_LOOK, PHOEBE_LOOK)
from num.pages import Pages
from rom import G

CODE = "ROM"
K = EpistleKit(G, CODE, "Romans", credit="Romans · Volume Forty-Five")
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title = K.D, K.F, K.glory, K.title
v, sp = G.v, G.span

# ---- Romans' own cast (faces) ---------------------------------------------------------------------------------------------
TERTIUS = face_of("adam", skin="#D9A27A", shadow="#7A4A3A", hair="#2A1A10", hl="#5A4A3E", scarf=TERTIUS_LOOK["head"], cord=True, light="#FFC14D")
PHOEBE = face_of("eve", skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", scarf=PHOEBE_LOOK["veil"], light="#FFE680")

# the saints Paul greets (Romans 16), faces for the greetings roll: every headcloth and veil cool, dark or off-white
from act.common import AQUILA, PRISCILLA                                                   # Prisca and Aquila, as Acts draws them
EPAENETUS = face_of("adam", skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#3A4A5A", cord=True, light="#FFE680")
MARY_ROME = face_of("eve", skin="#B98A6E", shadow="#4A3A4A", hair="#2A1A10", scarf="#2A2A3A", light="#FFE680")
ANDRONICUS = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#9A948A", hl="#C8C2B6", beard=True, beard_color="#A8A296", scarf="#E8E2D6", cord=True, light="#FFE680")
JUNIAS = face_of("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", scarf="#2A2A4A", cord=True, light="#FFE680")
