"""Shared helpers for the Deuteronomy chapters: line builders for speech panels and the standard panels."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from speech import orate
from deu import G, art as K
from genesis import art as X
from genesis.ch02 import W1, NIGHT
from genesis.ch06 import GOLDEN

v, sp = G.v, G.span
INK = "#0B1A2E"

def say(ref, frm=None, to=None): return ("say", v(ref, frm=frm, to=to))
def gd(ref, frm=None, to=None): return ("god", v(ref, frm=frm, to=to))
def cp(ref, frm=None, to=None): return ("cap", v(ref, frm=frm, to=to))
def says(refs): return ("say", sp(refs))
def gods(refs): return ("god", sp(refs))
def caps(refs): return ("cap", sp(refs))

def mo(h, lines, ref, tok=None, bg=GOLDEN, flip=False, w=W1, **k):
    """Moses speaking (calm by default)."""
    return orate(tok or K.MOSES_CALM, h, bg, lines, w=w, ref=ref, flip=flip, **k)

def voice(h, lines, ref, w=W1, **k):
    """Words over the night sky, no face (God's words, or narration)."""
    return orate(None, h, NIGHT, lines, w=w, ref=ref, art=X.cosmic(w, h), **k)

def over(h, bg, art, lines, ref, w=W1, **k):
    """Words in a column over a drawing."""
    return orate(None, h, bg, lines, w=w, ref=ref, art=art, top=True, **k)
