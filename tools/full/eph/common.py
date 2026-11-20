"""Shared helpers for the Ephesians chapters: the letter's kit (epistle.EpistleKit with fit_faces and clip on), its line
builders and panels, Paul's faces in his five lights (from epistle), and the faces of the letter's own cast — the soldier
that guarded Paul (epistle.GUARD) and Tychicus — each the same in every chapter."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     GUARD, nxt, fin, face_of)
from num.pages import Pages
from eph import G

CODE = "EPH"
K = EpistleKit(G, CODE, "Ephesians", credit="Ephesians · Volume Forty-Nine", fit_faces=True, clip=True)
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title = K.D, K.F, K.glory, K.title
v, sp = G.v, G.span

# ---- the letter's own cast ------------------------------------------------------------------------------------------------
TYCHICUS = face_of("adam", skin="#C8946C", shadow="#5A3A2A", hair="#4A2E1A", hl="#6A4A30", beard=True, beard_color="#5A3A22",
                   scarf="#2E5A5E", cord=True, light="#FFE680")                   # an Asian brother: slate-teal headcloth, short brown beard
TYCHICUS_LOOK = dict(cloth="#5E6E7E", head="#2E5A5E", cord="#132A2C", beard="#5A3A22", mantle="#7A7A80")   # grey-blue robe, grey travelling cloak
SCRIBE_LOOK = dict(cloth="#4A4E5A", head="#2A2E3A", cord="#0D0F18", beard="#1A1210")    # the scribe at Rome (not named): dark slate headcloth
