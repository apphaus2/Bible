"""Shared helpers for the Hebrews chapters: the letter's kit (epistle.EpistleKit, drawings clipped to their panels), its line
builders and panels. Hebrews names no writer, so there are no face panels (K.F): every panel is a drawing (D), a picture
(pic) or a glory panel, and the letter boxes over them are untailed."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import EpistleKit, GLORY_BG, nxt, fin
from num.pages import Pages
from heb import G

CODE = "HEB"
K = EpistleKit(G, CODE, "Hebrews", credit="Hebrews · Volume Fifty-Eight", clip=True)
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
glory, title, pic = K.glory, K.title, K.pic

def D(lines, fn, bg, size=14, **k):
    """The words over a drawing (K.D), the words at 14 px at most: Hebrews packs more words to a page than the other letters."""
    return K.D(lines, fn, bg, size=size, **k)
v, sp = G.v, G.span

def gj(*parts):
    """One Voice box from several cuts (K.j("god", …))."""
    return K.j("god", *parts)

def sj(*parts):
    """One song box from several cuts."""
    return K.j("song", *parts)
