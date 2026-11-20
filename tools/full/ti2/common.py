"""Shared helpers for the 2 Timothy chapter: the letter's kit (epistle.EpistleKit with fit_faces and clip), its line builders,
Paul's faces in his lights — and one more, PAUL_OFFERED, Paul in a grave gold light for "I am already being offered"
(4:6) — the pastoral letters' cast from ti1.common, and the people greeted at the end (4:19–21)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     nxt, fin, face_of, greetings, face_portrait, _paul)
from num.pages import Pages
from ti2 import G
from ti1.common import TIMOTHY, TIMOTHY_OLD, TIMOTHY_LAMP, LOIS, EUNICE, LUKE, TITUS, TIMOTHY_LOOK, LUKE_LOOK, LOIS_LOOK, EUNICE_LOOK

CODE = "2TI"
K = EpistleKit(G, CODE, "2 Timothy", credit="2 Timothy · Volume Fifty-Five", fit_faces=True, clip=True)
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title = K.D, K.F, K.glory, K.title
v, sp = G.v, G.span

# Paul near his end (4:6): his face in a grave gold light, the ground falling away to dark
PAUL_OFFERED = _paul(skin="#D8A070", shadow="#5A3A1E", light="#FFD27A")
OFFER_BG = "radial-gradient(circle at 70% 32%, #FFF8DC 0 24px, #F0C060 170px, #8A5A20 360px, #2A1A0A 520px)"
CELL_BG = "radial-gradient(circle at 70% 30%, #FFD08A 0 16px, #A8642A 150px, #3A2418 330px, #140C08 470px)"    # Paul in the cell, by its one lamp

# ---- the people greeted (4:19–21), each in a cool, dark or off-white headcloth or veil -----------------------------------------
from act.common import AQUILA, PRISCILLA                         # Prisca and Aquila, as Acts draws them
def _m(skin, hair, scarf=None, beard=None, stubble=None, light="#FFE680"):
    k = dict(skin=skin, shadow="#5A3A3A", hair=hair, hl="#6A5A4A", light=light)
    if scarf: k.update(scarf=scarf, cord=True)
    if beard: k.update(beard=True, beard_color=beard)
    if stubble: k.update(stubble=stubble)
    return face_of("adam", **k)
def _w(skin, hair, veil, light="#FFE680"): return face_of("eve", skin=skin, shadow="#5A3A4A", hair=hair, scarf=veil, light=light)
ONESIPHORUS = _m("#C98E66", "#4A3A2A", "#3A4A5A", beard="#5A4A3A")                     # of Ephesus: a slate headcloth, a brown beard
ERASTUS = _m("#D9A27A", "#2A1A10", "#E8E2D6", beard="#2A1A10")                          # an off-white headcloth, a black beard
TROPHIMUS = _m("#E3B08A", "#3A2214")                                                     # the Ephesian, a Greek: bareheaded, clean-shaven
EUBULUS = _m("#D9A27A", "#6A645E", stubble="#6A645E")                                  # a Roman of the church at Rome: bareheaded, grey
PUDENS = _m("#E3B08A", "#4A3A2A")                                                        # a Roman: bareheaded, clean-shaven
LINUS = _m("#C98E66", "#1A1210", "#1F2F3A", beard="#1A1210")
CLAUDIA = _w("#E3B08A", "#3A2214", "#2A3A5A")
