"""Shared helpers for the 3 John chapter: 1 John's kit (jn1.common.kit: JohnKit, faces sized to their words, drawings
clipped, a page's spare height given to its drawings), John the elder's faces, and Gaius, Diotrephes and Demetrius, from
jn1.common."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from jn1.common import (kit, Pages, nxt, fin, JOHN_OLD, JOHN_LAMP, JOHN_GRIEF, JOHN_JOY, JOHN_STERN, GAIUS, DIOTREPHES, DEMETRIUS, GOLD_BG, LAMP_BG,
                        GRIEF_BG, JOY_BG, STERN_BG)
from jn3 import G

CODE = "3JN"
K = kit(G, CODE, "3 John", "3 John · Volume Sixty-Four")
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title, pic = K.D, K.F, K.glory, K.title, K.pic
v, sp = G.v, G.span
