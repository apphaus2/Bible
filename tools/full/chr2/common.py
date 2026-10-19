"""Shared helpers for the 2 Chronicles chapters: line builders for discourse.pack, roll cells for lists and reigns, and the
cast's faces (Solomon and the kings from 1 and 2 Kings)."""
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
from chr2 import G

v, sp = G.v, G.span
CODE = "2CHR"
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
    return _pack(segs, prefix, start, book="2 Chronicles", code=CODE, **k)

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
    return roll_pages(items, prefix, start, "2 Chronicles", CODE, tag=tag, **k)

# 2 Chronicles cast
ASA = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#1F3A7A", band=True, light="#FFE680")
ASA_OLD = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#1F3A7A", band=True, brow="scowl", light="#D7261E")
ABIJAH = F("adam", skin="#D9A27A", shadow="#5A3A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#1F3A7A", band=True, light="#FFC14D")
AZARIAH_P = F("adam", skin="#B98A6E", shadow="#3A3A5A", hair="#C8C2B6", hl="#E8E2D6", beard=True, beard_color="#D8D2C6", scarf="#4A3A6A", cord=True, light="#FFF4C2")
HANANI = F("adam", skin="#B98A6E", shadow="#4A3A4A", hair="#6A645E", hl="#9A948A", beard=True, beard_color="#7A746A", scarf="#3A4A3A", cord=True, brow="scowl", light="#9AA8C8")
JAHAZIEL = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#F3EFE6", cord=True, light="#FFF4C2")
ZECHARIAH_P = F("adam", skin="#D9A27A", shadow="#4A3A4A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#F3EFE6", band=True, light="#FFF4C2")
AMAZIAH = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#1F3A7A", band=True, brow="scowl", light="#D7261E")
UZZIAH = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#1F3A7A", band=True, light="#FFE680")
UZZIAH_LEPER = F("adam", skin="#E8E2E0", shadow="#A8A0A8", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#1F3A7A", band=True, brow="sorrow", light="#E8ECF8")
AHAZ = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", scarf="#1F3A7A", band=True, brow="scowl", light="#D7261E")
ODED = F("adam", skin="#B98A6E", shadow="#3A3A5A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#5A4A3A", cord=True, light="#FFF4C2")
NECO = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#0D0D0F", hl="#2A2220", false_beard=True, egypt=("#0D0D0F", "#E8B830"), collar=True, kohl=True, light="#FFC14D")
