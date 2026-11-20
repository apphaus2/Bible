"""Shared helpers for the Philemon chapter: the letter's kit (epistle.EpistleKit with face panels sized to their words and
drawings clipped to their panels), its line builders and panels, Paul's faces (from epistle), and the cast of the prison
letters as Philippians defines them (php.common): Philemon, Apphia, Archippus, Onesimus, Timothy, Tychicus, Epaphras, Mark,
Aristarchus, Demas, Luke."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GUARD, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     nxt, fin, face_of)
from num.pages import Pages
from phm import G
from php.common import PHILEMON, APPHIA, ARCHIPPUS, ONESIMUS, TIMOTHY, TYCHICUS, EPAPHRAS, MARK, ARISTARCHUS, DEMAS, LUKE

CODE = "PHM"
K = EpistleKit(G, CODE, "Philemon", credit="Philemon · Volume Fifty-Seven", fit_faces=True, clip=True)
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title = K.D, K.F, K.glory, K.title
v, sp = G.v, G.span
