"""Shared helpers for the Romans chapters: the letter's kit (epistle.EpistleKit), its line builders and panels, Paul's
faces in his five lights (from epistle), and Romans' own cast (Tertius, Phoebe), each the same in every chapter."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     nxt, fin, face_of, TERTIUS_LOOK, PHOEBE_LOOK)
from num.pages import Pages
from rom import G

CODE = "ROM"
K = EpistleKit(G, CODE, "Romans", credit="Romans · Volume Forty-Five")
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title = K.D, K.F, K.glory, K.title
v, sp = G.v, G.span

# ---- Romans' own cast (faces) ---------------------------------------------------------------------------------------------
TERTIUS = face_of("adam", skin="#D9A27A", shadow="#7A4A3A", hair="#2A1A10", hl="#5A4A3E", scarf=TERTIUS_LOOK["head"], cord=True, light="#FFC14D")
PHOEBE = face_of("eve", skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", scarf=PHOEBE_LOOK["veil"], light="#FFE680")

# the saints Paul greets (Romans 16), faces for the greetings roll: every headcloth and veil cool, dark or off-white
from act.common import AQUILA, PRISCILLA                                                   # Prisca and Aquila, as Acts draws them
EPAENETUS = face_of("adam", skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#3A4A5A", cord=True, light="#FFE680")
MARY_ROME = face_of("eve", skin="#B98A6E", shadow="#4A3A4A", hair="#2A1A10", scarf="#2A2A3A", light="#FFE680")
ANDRONICUS = face_of("adam", skin="#C98E66", shadow="#4A3A4A", hair="#9A948A", hl="#C8C2B6", beard=True, beard_color="#A8A296", scarf="#E8E2D6", cord=True, light="#FFE680")
JUNIAS = face_of("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", scarf="#2A2A4A", cord=True, light="#FFE680")
def _m(skin, hair, scarf=None, beard=None, stubble=None, light="#FFE680"):
    k = dict(skin=skin, shadow="#4A3A3A", hair=hair, hl="#6A5A4E", light=light)
    if scarf: k.update(scarf=scarf, cord=True)
    if beard: k.update(beard=True, beard_color=beard)
    if stubble: k.update(stubble=stubble)
    return face_of("adam", **k)
def _w(skin, hair, veil, light="#FFE680"): return face_of("eve", skin=skin, shadow="#5A3A4A", hair=hair, scarf=veil, light=light)
AMPLIATUS = _m("#C98E66", "#2A1A10", "#4A4A5A", beard="#2A1A10")
URBANUS = _m("#E3B08A", "#5A4A3A")                                                          # a Roman, bareheaded, clean-shaven
STACHYS = _m("#D9A27A", "#3A2214", "#E8E2D6", stubble="#3A2214")
APELLES = _m("#C98E66", "#1A1210", "#1F3A4A", beard="#1A1210")
ARISTOBULUS_H = _w("#D9A27A", "#2A1A10", "#3A3A5A")                                           # one of his household
HERODION = _m("#B98A6E", "#1A1210", "#3A2A4A", beard="#1A1210")
NARCISSUS_H = _m("#E3B08A", "#4A3A2A", stubble="#4A3A2A")
TRYPHAENA = _w("#D9A27A", "#2A1A10", "#2A4A5A")
TRYPHOSA = _w("#C98E66", "#2A1A10", "#4A4A6A")
PERSIS = _w("#B98A6E", "#1A1210", "#E8E2D6")
RUFUS = _m("#C98E66", "#3A2214", "#2A3A2A", beard="#3A2214")
RUFUS_MOTHER = _w("#C98E66", "#9A948A", "#3A3A4A")
ASYNCRITUS = _m("#D9A27A", "#6A645E", "#5A5A6A", beard="#7A746A")
HERMAS = _m("#E3B08A", "#2A1A10", stubble="#2A1A10")
PHILOLOGUS = _m("#C98E66", "#2A1A10", "#1F2F4A", beard="#2A1A10")
JULIA = _w("#E3B08A", "#3A2214", "#1F4A5A")
NEREUS = _m("#D9A27A", "#1A1210", "#3A4A3A", stubble="#1A1210")
OLYMPAS = _m("#B98A6E", "#8A847A", "#E8E2D6", beard="#9A948A")
from act.common import TIMOTHY
