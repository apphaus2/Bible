"""Shared helpers for the 2 Thessalonians chapter: the letter's kit (epistle.EpistleKit, its faces sized to their words and
its drawings clipped to their panels), its line builders and panels, Paul's faces in his lights (from epistle), and 1
Thessalonians' hand pager (th1.common.paged)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     nxt, fin, face_of)
from num.pages import Pages
from th1.common import paged
from th2 import G

CODE = "2TH"
K = EpistleKit(G, CODE, "2 Thessalonians", credit="2 Thessalonians · Volume Fifty-Three", fit_faces=True, clip=True)
lt, lts, ltj, lp, lj = K.lt, K.lts, K.ltj, K.lp, K.lj
F = K.F
v, sp = G.v, G.span

def D(lines, fn, bg, art_h=200, **kw):
    """K.D, remembering how much of the panel is its drawing (what paged() may grow or shrink to fill a page)."""
    s = K.D(lines, fn, bg, art_h=art_h, **kw)
    if "h" not in kw: s["flex"] = min(art_h, s["h"] - 150)
    return s

def glory(lines, flex=200, **kw):
    """K.glory, its burst of light free to grow or shrink by up to `flex` px (paged())."""
    s = K.glory(lines, **kw)
    s["flex"] = min(flex, s["h"] - 100)
    return s

def title(num, name, rng, svg, bg, quote):
    return K.title(num, name, rng, svg, bg, quote)
