"""Shared helpers for the 2 Peter chapters: the letter's kit (epistle.EpistleKit), its line builders and panels, and Peter's
faces in the kit's five lights, old (from jas.common, where the writers of the general letters are kept)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import EpistleKit, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG, nxt, fin
from jas.common import PETER_OLD, PETER_LAMP, PETER_GRIEF, PETER_JOY, PETER_STERN
from num.pages import Pages
from pe2 import G

CODE = "2PE"
K = EpistleKit(G, CODE, "2 Peter", credit="2 Peter · Volume Sixty-One", fit_faces=True, clip=True)
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title = K.D, K.F, K.glory, K.title
v, sp = G.v, G.span
