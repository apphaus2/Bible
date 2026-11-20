"""Shared helpers for the Philippians chapters: the letter's kit (epistle.EpistleKit, with face panels sized to their words
and drawings clipped to their panels), its line builders and panels, Paul's faces in his five lights and the guard's face
(from epistle), and the cast of Paul's prison letters — Philippians, Colossians and Philemon all import their people from
here, so each looks the same in all three books.

The cast (faces for K.F and greeting portraits; LOOKs for the figures in php.art). Every headcloth and veil is cool, dark or
off-white (a warm one reads as long hair):
  Timothy        as Acts draws him (act.common.TIMOTHY): young, beardless, bareheaded, light-brown hair, a grey-blue tunic
  Epaphroditus   the Philippians' messenger (Php 2:25, 4:18): a slate headcloth with a dark cord, a short brown beard, an olive
                 robe and a grey travelling cloak; EPAPHRODITUS_SICK pale, in sorrow (2:26–27)
  Euodia         a dark-teal veil;  Syntyche  an off-white veil (Php 4:2)
  Epaphras       of Colossæ (Col 1:7, 4:12; Phm 23): an indigo headcloth with a cord, a dark-grey beard, a slate-violet robe
  Onesimus       the runaway servant (Col 4:9; Phm 10): young, bareheaded, short black curls, clean-shaven, a plain undyed tunic
  Philemon       of Colossæ: a grey beard, an off-white headcloth with a brown cord, a deep-blue robe and mantle
  Apphia         a dark-blue veil, a grey-violet robe;  Archippus  a charcoal headcloth, a black beard, a brown robe
  Tychicus       an Asian brother (Col 4:7): a slate-teal headcloth with a cord, a short brown beard, a grey travelling cloak
  Mark           as Acts draws him (a sand-olive tunic, bareheaded, brown hair), a young man's stubble
  Luke           the beloved physician: bareheaded, greying brown hair and a short greying beard, a deep-blue robe, a cream mantle
  Aristarchus    of Thessalonica, Paul's fellow-prisoner: bareheaded, black hair and beard, a dark wine-red tunic
  Justus         of the circumcision: an off-white headcloth with a blue band, a black beard, a grey robe
  Demas          young, bareheaded, clean-shaven, light-brown hair, an olive-grey robe"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GUARD, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     nxt, fin, face_of)
from num.pages import Pages
from php import G

CODE = "PHP"
K = EpistleKit(G, CODE, "Philippians", credit="Philippians · Volume Fifty", fit_faces=True, clip=True)
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title = K.D, K.F, K.glory, K.title
v, sp = G.v, G.span

# ---- the cast of the prison letters (faces) -------------------------------------------------------------------------------
from act.common import TIMOTHY
EPAPHRODITUS = face_of("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#4A3020", hl="#7A6A5A", beard=True, beard_color="#4A3020", scarf="#4A5A6A", cord=True, light="#FFE680")
EPAPHRODITUS_SICK = face_of("adam", skin="#C8A088", shadow="#4A3A4A", hair="#4A3020", hl="#7A6A5A", beard=True, beard_color="#4A3020", scarf="#4A5A6A", cord=True,
                            brow="sorrow", sweat=True, light="#9AA8C8")
EUODIA = face_of("eve", skin="#D9A27A", shadow="#6A4A3A", hair="#2A1A10", scarf="#1F4A4A", light="#FFE680")
SYNTYCHE = face_of("eve", skin="#C98E66", shadow="#5A3A3A", hair="#1A1210", scarf="#E8E2D6", light="#FFE680")
EPAPHRAS = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#2A2420", hl="#6A645E", beard=True, beard_color="#4A4440", scarf="#2A2A5A", cord=True, light="#FFC14D")
ONESIMUS = face_of("adam", skin="#A8784E", shadow="#4A2A1A", hair="#1A1210", hl="#3A2A1E", light="#FFE680")
PHILEMON = face_of("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#9A948A", hl="#C8C2B6", beard=True, beard_color="#A8A296", scarf="#E8E2D6", cord=True, light="#FFE680")
APPHIA = face_of("eve", skin="#D9A27A", shadow="#6A4A4A", hair="#3A2A1A", scarf="#1F2F5A", light="#FFE680")
ARCHIPPUS = face_of("adam", skin="#C98E66", shadow="#5A3A2A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#2A2E36", cord=True, light="#FFC14D")
TYCHICUS = face_of("adam", skin="#C98E66", shadow="#5A3A3A", hair="#5A3A22", hl="#8A6A4E", beard=True, beard_color="#5A3A22", scarf="#3A6A6A", cord=True, light="#FFE680")
MARK = face_of("adam", skin="#C98E66", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", light="#FFE680")
LUKE = face_of("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#6A5A4A", hl="#9A8A7A", beard=True, beard_color="#7A6A5A", light="#FFF4C2")
ARISTARCHUS = face_of("adam", skin="#C98E66", shadow="#4A3A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", light="#FFC14D")
JUSTUS = face_of("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#E8E2D6", band=True, light="#FFE680")
DEMAS = face_of("adam", skin="#E3B08A", shadow="#7A5A4A", hair="#6A4A2A", hl="#9A7A5A", light="#FFE680")

# ---- the same people at a distance (php.art draws them on epistle.robed) --------------------------------------------------
TIMOTHY_LOOK = dict(cloth="#7A8A9A", hair="#3A2214", belt="#4A5A6A")
EPAPHRODITUS_LOOK = dict(cloth="#5A6A4A", head="#4A5A6A", cord="#1E2A34", beard="#4A3020", mantle="#6A6458", belt="#3A2A1A")
EUODIA_LOOK = dict(cloth="#5A7A7A", veil="#1F4A4A")
SYNTYCHE_LOOK = dict(cloth="#7A6A8A", veil="#E8E2D6")
EPAPHRAS_LOOK = dict(cloth="#4A4A6A", head="#2A2A5A", cord="#0D0D1A", beard="#4A4440", belt="#2A2A3A")
ONESIMUS_LOOK = dict(cloth="#D8CCB0", hair="#1A1210", skin="#A8784E", belt="#8A6A3A")
PHILEMON_LOOK = dict(cloth="#3A5A7A", head="#E8E2D6", cord="#6A5A3A", beard="#A8A296", mantle="#2A3A5A")
APPHIA_LOOK = dict(cloth="#6A6A7A", veil="#1F2F5A")
ARCHIPPUS_LOOK = dict(cloth="#5A4A3A", head="#2A2E36", cord="#0D0D0F", beard="#2A1A10", belt="#2A1A10")
TYCHICUS_LOOK = dict(cloth="#7A6A5A", head="#3A6A6A", cord="#1A2A2A", beard="#5A3A22", mantle="#6A6A70")
MARK_LOOK = dict(cloth="#8A7A4A", hair="#3A2214", belt="#4A3A1A")
LUKE_LOOK = dict(cloth="#2A4A6A", hair="#6A5A4A", beard="#7A6A5A", mantle="#C8BCA0")
ARISTARCHUS_LOOK = dict(cloth="#6A3A3A", hair="#1A1210", beard="#1A1210", mantle="#4A4A50")
JUSTUS_LOOK = dict(cloth="#5A5A6A", head="#E8E2D6", cord="#1F3A6A", beard="#2A1A10")
DEMAS_LOOK = dict(cloth="#8A8A6A", hair="#6A4A2A", belt="#4A4A3A")
