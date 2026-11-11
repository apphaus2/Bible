"""Shared helpers for the 2 Corinthians chapters: the letter's kit (epistle.EpistleKit), its line builders and panels,
Paul's faces in his five lights (from epistle), and the letter's own cast (Timothy, Titus, Moses), each the same in every
chapter."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     nxt, fin, face_of)
from num.pages import Pages
from co2 import G

CODE = "2CO"
K = EpistleKit(G, CODE, "2 Corinthians", credit="2 Corinthians · Volume Forty-Seven")
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory = K.D, K.F, K.glory

def title(num, name, rng, svg, bg, quote):
    """K.title, the name set a little smaller when it is long enough to run to three lines at the opener's 96 px (it would
    cover the verse range under it)."""
    html = K.title(num, name, rng, svg, bg, quote)
    return html.replace("font-size: 96px; line-height: 1.0", "font-size: 80px; line-height: 1.0", 1) if len(name) > 28 else html
v, sp = G.v, G.span

def lps(*refs, most=280):
    """Paragraphs across a chapter break: lps("1:23-24", "2:1-2") (K.lp keeps to one chapter)."""
    return [x for r in refs for x in lp(r, most=most)]

# ---- the letter's own cast (faces) ----------------------------------------------------------------------------------------
from act.common import TIMOTHY                                                             # young, beardless, bareheaded (Acts)
TITUS = face_of("adam", skin="#C98E66", shadow="#6A4A3A", hair="#1A1210", hl="#4A3A2E", light="#FFE680")   # a Greek: bareheaded, clean-shaven
