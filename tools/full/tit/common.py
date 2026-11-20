"""Shared helpers for the Titus chapter: the letter's kit (epistle.EpistleKit with fit_faces and clip), its line builders,
Paul's faces in his lights, and the pastoral letters' cast from ti1.common (Titus: 2 Corinthians' face)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     nxt, fin, face_of)
from num.pages import Pages
from tit import G
from ti1.common import TITUS, TITUS_LOOK

CODE = "TIT"
K = EpistleKit(G, CODE, "Titus", credit="Titus · Volume Fifty-Six", fit_faces=True, clip=True)
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title = K.D, K.F, K.glory, K.title
v, sp = G.v, G.span
