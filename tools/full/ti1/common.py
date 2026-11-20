"""Shared helpers for the 1 Timothy chapters: the letter's kit (epistle.EpistleKit with fit_faces and clip), its line
builders and panels, Paul's faces in his five lights (from epistle), and the cast of the pastoral letters (1 Timothy,
2 Timothy, Titus), defined once here and imported by ti2 and tit: Timothy (Acts' face; older and with a short beard in
2 Timothy), Titus (2 Corinthians' face), Lois and Eunice, Luke — each the same in every volume."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     nxt, fin, face_of)
from num.pages import Pages
from ti1 import G

CODE = "1TI"
K = EpistleKit(G, CODE, "1 Timothy", credit="1 Timothy · Volume Fifty-Four", fit_faces=True, clip=True)
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title = K.D, K.F, K.glory, K.title
v, sp = G.v, G.span

# ---- the cast of the pastoral letters (faces) ------------------------------------------------------------------------------
from act.common import TIMOTHY                                  # Acts' Timothy: young, beardless, bareheaded, brown hair
TIMOTHY_LAMP = face_of("adam", skin="#D9A27A", shadow="#6A3A22", hair="#3A2214", hl="#6A5A4E", light="#FF9A3D")   # reading by lamplight
TIMOTHY_OLD = face_of("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#4A2E1A", light="#FFE680")  # 2 Timothy: a few years on, a short beard
from co2.common import TITUS                                   # 2 Corinthians' Titus: a Greek, bareheaded, short black hair, clean-shaven
LOIS = face_of("eve", skin="#C98E66", shadow="#5A3A4A", hair="#B8B2A6", scarf="#1F2A4A", light="#FFE680")        # old, grey hair, a dark-blue veil
EUNICE = face_of("eve", skin="#D9A27A", shadow="#6A4A3A", hair="#3A2214", scarf="#4A5A4E", light="#FFE680")      # a grey-green veil
LUKE = face_of("adam", skin="#C98E66", shadow="#5A3A3A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#E8E2D6", cord=True, light="#FFC14D")  # the physician: short grey beard, off-white headcloth

# the same people at a distance (epistle.robed looks): ti1.art draws them
TIMOTHY_LOOK = dict(cloth="#7A8A9A", hair="#3A2214", belt="#3A4A5A")                   # Acts' grey-blue tunic (co2.art.timothy_fig)
TITUS_LOOK = dict(cloth="#C8B080", hair="#1A1210", mantle="#2A4A7A", belt="#6A4A2A")   # a sand tunic, a blue mantle (co2.art.titus_fig)
LOIS_LOOK = dict(cloth="#4A4A5A", veil="#1F2A4A", hair="#B8B2A6")
EUNICE_LOOK = dict(cloth="#5A6A5E", veil="#4A5A4E")
LUKE_LOOK = dict(cloth="#8A8478", head="#E8E2D6", cord="#5A4A3A", beard="#9A948A", mantle="#5A5A64")
