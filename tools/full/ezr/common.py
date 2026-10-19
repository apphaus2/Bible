"""Shared helpers for the Ezra chapters: line builders for discourse.pack, roll cells for lists and reigns, and the
cast's faces (the returned exiles, and the kings of Persia)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from discourse import seg, pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from kg2.common import (SOLOMON, SOLOMON_WISE, SOLOMON_STERN, SOLOMON_OLD, HIRAM, SHEBA, JEROBOAM, REHOBOAM, AHIJAH, AHAB, AHAB_ANGRY, MICAIAH, JEHOSHAPHAT,
                        PROPHET, ELIJAH, ISRAELITE, MESSENGER, JEHOIADA, ATHALIAH, JOASH, HEZEKIAH, HEZEKIAH_GRIEF, HEZEKIAH_SICK, RABSHAKEH, ISAIAH, MANASSEH,
                        JOSIAH, JOSIAH_GRIEF, HILKIAH, SHAPHAN, HULDAH, ZEDEKIAH, BABYLONIAN, JEHORAM, ZADOK, CAPTAIN)
from ezr import G

v, sp = G.v, G.span
CODE = "EZRA"
def say(ref, frm=None, to=None, after=None): return ("say", v(ref, frm=frm, to=to, after=after))
def gd(ref, frm=None, to=None, after=None): return ("god", v(ref, frm=frm, to=to, after=after))
def cp(ref, frm=None, to=None, after=None): return ("cap", v(ref, frm=frm, to=to, after=after))
def sg(ref, frm=None, to=None, after=None): return ("song", v(ref, frm=frm, to=to, after=after))
def says(refs): return ("say", sp(refs))
def gods(refs): return ("god", sp(refs))
def caps(refs): return ("cap", sp(refs))
def joined(kind, *parts):
    """One box from several cuts: joined("say", ("1:2", "Let there", None), "1:3") — a ref alone is the whole verse."""
    return (kind, " ".join(v(p) if isinstance(p, str) else v(p[0], frm=p[1], to=p[2] if len(p) > 2 else None) for p in parts))

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 0.92)
    k.setdefault("min_size", 12.5)
    return _pack(segs, prefix, start, book="Ezra", code=CODE, **k)

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
    return roll_pages(items, prefix, start, "Ezra", CODE, tag=tag, **k)

# Ezra cast
CYRUS = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#7A2A6A", band=True, light="#FFE680")
PERSIAN = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#2A5A6A", band=True, brow="scowl", light="#FFC14D")
ZERUBBABEL = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#1F3A7A", band=True, light="#FFE680")
JESHUA = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#6A645E", hl="#9A948A", beard=True, beard_color="#7A746A", scarf="#F3EFE6", band=True, light="#FFE680")
ELDER = F("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#E8E2D6", hl="#F3EFE6", beard=True, beard_color="#E8E2D6", scarf="#5A4A3A", brow="sorrow", tear=True, light="#9AA8C8")
HAGGAI = F("adam", skin="#B98A6E", shadow="#3A3A5A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#4A3A6A", cord=True, light="#FFF4C2")
ZECHARIAH = F("adam", skin="#D9A27A", shadow="#4A3A4A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#3A5A6A", cord=True, light="#FFF4C2")
TATTENAI = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#8A5A1A", band=True, light="#FFC14D")
DARIUS = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#7A2A6A", band=True, brow="scowl", light="#FFD23F")
ARTAXERXES = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#7A2A6A", band=True, light="#FFE680")
EZRA = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#5A5450", scarf="#E8E2D6", cord=True, light="#FFE680")
EZRA_GRIEF = F("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#5A5450", scarf="#E8E2D6", cord=True, brow="sorrow", tear=True, light="#9AA8C8")
SHECANIAH = F("adam", skin="#C98E66", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#6A5A3A", cord=True, light="#FFC14D")
