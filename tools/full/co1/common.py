"""Shared helpers for the 1 Corinthians chapters: the letter's kit (epistle.EpistleKit), its line builders and panels, Paul's
faces in his five lights (from epistle), and the letter's own cast (Sosthenes, Stephanas, Fortunatus, Achaicus, the
household of Chloe), each the same in every chapter; Apollos, Aquila, Priscilla, Timothy and James as Acts draws them,
Cephas as ntcast's Peter."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     nxt, fin, face_of, greetings, face_portrait, portrait)
from num.pages import Pages
from co1 import G

CODE = "1CO"
K = EpistleKit(G, CODE, "1 Corinthians", credit="1 Corinthians · Volume Forty-Six")
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title, pic = K.D, K.F, K.glory, K.title, K.pic
v, sp = G.v, G.span

# ---- the letter's own cast: looks for the figures (co1.art) and faces for the face panels ---------------------------------
SOSTHENES_LOOK = dict(cloth="#4A5A6A", head="#7A848E", cord="#1E242A", beard="#3E3A38")      # slate-grey headcloth, grey-black beard
STEPHANAS_LOOK = dict(cloth="#5A4A3A", head="#E8E2D6", cord="#5A4A3A", beard="#9A948A")      # the eldest: off-white headcloth, grey beard
FORTUNATUS_LOOK = dict(cloth="#2E5A4A", head="#1E2A3A", cord="#0D1018", beard="#1A1210")     # navy headcloth, black beard
ACHAICUS_LOOK = dict(cloth="#6A5A7A", hair="#2A1A10")                                         # young, bareheaded, beardless
CHLOE_LOOK = dict(cloth="#4A6A6A", head="#1F4A4A", beard="#2A1A10")                            # Chloe's messenger: dark-teal headcloth

SOSTHENES = face_of("adam", skin="#C98E66", shadow="#5A3A3A", hair="#3E3A38", hl="#6A645E", beard=True, beard_color="#3E3A38", scarf=SOSTHENES_LOOK["head"], cord=True, light="#FFC14D")
STEPHANAS = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#9A948A", hl="#C8C2B6", beard=True, beard_color="#9A948A", scarf=STEPHANAS_LOOK["head"], cord=True, light="#FFE680")
FORTUNATUS = face_of("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf=FORTUNATUS_LOOK["head"], cord=True, light="#FFE680")
ACHAICUS = face_of("adam", skin="#D9A27A", shadow="#7A4A3A", hair="#2A1A10", hl="#5A4A3E", light="#FFE680")

from act.common import APOLLOS, AQUILA, PRISCILLA, TIMOTHY, JAMES_LORD                      # as Acts draws them
from ntcast import PETER as CEPHAS, JOHN, ANDREW, JAMES, MATTHEW, THOMAS, PHILIP, JESUS, JESUS_RISEN
