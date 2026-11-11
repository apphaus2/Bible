"""Shared helpers for the Galatians chapters: the letter's kit (epistle.EpistleKit), its line builders and panels, Paul's
faces in his five lights (from epistle), and the faces of the others the letter names (Cephas, John, James the Lord's
brother, Barnabas, Titus; Abraham, Hagar and Sarah as Genesis draws them), each the same in every chapter."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     nxt, fin, face_of)
from num.pages import Pages
from gal import G

CODE = "GAL"
K = EpistleKit(G, CODE, "Galatians", credit="Galatians · Volume Forty-Eight")
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title = K.D, K.F, K.glory, K.title
v, sp = G.v, G.span

# ---- the others the letter names (faces) ----------------------------------------------------------------------------------
from ntcast import PETER, JOHN                                                             # Cephas and John, as ntcast draws them
from act.common import BARNABAS, JAMES_LORD                                               # as Acts draws them
from genesis.art4 import HAGAR, SARAH                                                      # Genesis' Hagar (cerulean, kohl) and Sarah (mulberry veil)
from genesis.art3 import ABRAM as ABRAHAM
TITUS = face_of("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#1A1210", hl="#4A3A2E", light="#FFE680")   # a Greek: bareheaded, short black hair, clean-shaven
TITUS_LOOK = dict(cloth="#D8C090", mantle="#2A4A7A", hair="#1A1210")                      # a sand tunic with a blue mantle
