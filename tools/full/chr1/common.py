"""Shared helpers for the 1 Chronicles chapters: line builders for discourse.pack, roll cells for the genealogies and
courses, and the cast's faces (David's house from 2 Samuel, Solomon and the court from 1 Kings)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from discourse import seg, pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from sa2.common import (DAVID, DAVID_BOLD, DAVID_KING, DAVID_JOY, DAVID_WRATH, DAVID_GRIEF, DAVID_OLD, DAVID_OLD_ALARM, DAVID_OLD_WEEP, NATHAN,
                        NATHAN_STERN, MICHAL, GAD, JOAB, ABISHAI, SAUL_KING, JONATHAN, ISRAELITE, MESSENGER)
from kg2.common import SOLOMON, SOLOMON_WISE, ZADOK, BENAIAH, HIRAM, PROPHET
from chr1 import G

v, sp = G.v, G.span
CODE = "1CHR"
def say(ref, frm=None, to=None, after=None): return ("say", v(ref, frm=frm, to=to, after=after))
def gd(ref, frm=None, to=None, after=None): return ("god", v(ref, frm=frm, to=to, after=after))
def cp(ref, frm=None, to=None, after=None): return ("cap", v(ref, frm=frm, to=to, after=after))
def sg(ref, frm=None, to=None, after=None): return ("song", v(ref, frm=frm, to=to, after=after))
def says(refs): return ("say", sp(refs))
def gods(refs): return ("god", sp(refs))
def caps(refs): return ("cap", sp(refs))
def sgs(refs):
    a, _, b = refs.partition("-"); c, x = map(int, a.split(":")); y = int(b) if b else x
    return [sg(f"{c}:{k}") for k in range(x, y + 1)]
def joined(kind, *parts):
    """One box from several cuts: joined("say", ("1:2", "Let there", None), "1:3") — a ref alone is the whole verse."""
    return (kind, " ".join(v(p) if isinstance(p, str) else v(p[0], frm=p[1], to=p[2] if len(p) > 2 else None) for p in parts))

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 0.92)
    k.setdefault("min_size", 12.5)
    return _pack(segs, prefix, start, book="1 Chronicles", code=CODE, **k)

def face(lines, ref, tok, bg=GOLDEN, **k): return seg(lines, ref, tok=tok, bg=bg, **k)
def drawn(lines, ref, art, bg, **k): return seg(lines, ref, bg=bg, art=art, **k)

def label(refs):
    a, _, b = refs.partition("-")
    return f"{CODE} {a}" + (f"–{b}" if b else "")

def cell(name, refs, accent="#FFD23F", head=None):
    """One roll cell: a name over verses refs ("2:3-8"), every word."""
    return (name, sp(refs), label(refs), accent, head)

def cells(c, a, b, name, accent, head=None, budget=520, brk=None):
    from rolls import verse_cells
    return verse_cells(G, CODE, c, a, b, name, accent, head=head, budget=budget, brk=brk)

def roll(items, prefix, start, tag, **k):
    from rolls import roll_pages
    return roll_pages(items, prefix, start, "1 Chronicles", CODE, tag=tag, **k)

# 1 Chronicles cast
JABEZ = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#6A5A3A", cord=True, brow="sorrow", light="#FFF4C2")
