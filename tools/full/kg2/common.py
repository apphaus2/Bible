"""Shared helpers for the 2 Kings chapters: line builders for discourse.pack and the cast's faces (most from 1 Kings)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import samuel4 as S4
from faces_ex import F
from discourse import seg, pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from kg2 import G

v, sp = G.v, G.span
def say(ref, frm=None, to=None, after=None): return ("say", v(ref, frm=frm, to=to, after=after))
def gd(ref, frm=None, to=None, after=None): return ("god", v(ref, frm=frm, to=to, after=after))
def cp(ref, frm=None, to=None, after=None): return ("cap", v(ref, frm=frm, to=to, after=after))
def sg(ref, frm=None, to=None, after=None): return ("song", v(ref, frm=frm, to=to, after=after))
def says(refs): return ("say", sp(refs))
def gods(refs): return ("god", sp(refs))
def caps(refs): return ("cap", sp(refs))
def joined(kind, *parts):
    """One box from several cuts: joined("say", ("1:2", "Let there", None), "1:3") — a ref alone is the whole verse."""
    out = []
    for p in parts:
        out.append(v(p) if isinstance(p, str) else v(p[0], frm=p[1], to=p[2] if len(p) > 2 else None))
    return (kind, " ".join(out))

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 0.92)
    k.setdefault("min_size", 12.5)
    return _pack(segs, prefix, start, book="2 Kings", code="2KGS", **k)

_T = S4.tokens()
def tok(name): return _T[f"__FACE_{name}__"]
DAVID_OLD, DAVID_OLD_WEEP, NATHAN, NATHAN_STERN = tok("DAVID_OLD"), tok("DAVID_OLD_WEEP"), tok("NATHAN"), tok("NATHAN_STERN")
# Solomon: black hair and a short black beard, a deep-blue headcloth with the gold band; old Solomon greying.
_sol = dict(skin="#D9A27A", shadow="#7A4A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#1F3A7A", band=True)
SOLOMON, SOLOMON_WISE, SOLOMON_STERN = F("adam", light="#FFE680", **_sol), F("adam", light="#FFF4C2", brow="sorrow", **_sol), F("adam", light="#D7261E", brow="scowl", **_sol)
SOLOMON_OLD = F("adam", skin="#C98E66", shadow="#5A3A4A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#1F3A7A", band=True, brow="sorrow", light="#9AA8C8")
BATHSHEBA = F("eve", skin="#D9A27A", shadow="#7A4A4A", hair="#1A1210", scarf="#7A3A6A", band=True, light="#FFE680")
ADONIJAH = F("adam", skin="#E3B08A", shadow="#8A4A3A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#B5652E", band=True, light="#FF8A3D")
ADONIJAH_AFRAID = F("adam", skin="#E3B08A", shadow="#5A3A4A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#B5652E", band=True, brow="sorrow", sweat=True, light="#9AA8C8")
JOAB = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#6A645E", hl="#9A948A", beard=True, beard_color="#6A645E", scarf="#6A2A1A", cord=True, brow="scowl", light="#D7261E")
ZADOK = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#E8E2D6", hl="#F3EFE6", beard=True, beard_color="#E8E2D6", scarf="#F3EFE6", band=True, light="#FFE680")
BENAIAH = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#3A4A6A", cord=True, brow="scowl", light="#FFC14D")
JONATHAN_PR = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#2A1A10", hl="#5A4A3E", stubble="#2A1A10", sweat=True, light="#FFE680")
SHIMEI = F("adam", skin="#C47A5A", shadow="#5A2A1E", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#8A847A", scarf="#6A5A3A", brow="sorrow", light="#9AA8C8")
HIRAM = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#6A1A5A", band=True, light="#FFC14D")
SHEBA = F("eve", skin="#8A5A3A", shadow="#3A2014", hair="#0D0D0F", scarf="#2A2A6A", band=True, kohl=True, light="#FFE680")
JEROBOAM = F("adam", skin="#C47A5A", shadow="#4A2A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#2E6B3A", band=True, light="#FFC14D")
REHOBOAM = F("adam", skin="#E3B08A", shadow="#6A4A4A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", scarf="#1F3A7A", band=True, brow="scowl", light="#D7261E")
AHIJAH = F("adam", skin="#B98A6E", shadow="#4A3A4A", hair="#E8E2D6", hl="#F3EFE6", beard=True, beard_color="#E8E2D6", scarf="#5A5A6A", cord=True, light="#9AA8C8")
ELIJAH = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#3A3430", light="#FFC14D")
ELIJAH_FIRE = F("adam", skin="#C98E66", shadow="#5A2A1E", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#3A3430", brow="scowl", light="#FF6A2A")
ELIJAH_WEARY = F("adam", skin="#A87A5E", shadow="#3A2A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#3A3430", brow="sorrow", sweat=True, light="#9AA8C8")
AHAB = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#7A1A2A", band=True, light="#FFC14D")
AHAB_ANGRY = F("adam", skin="#C98E66", shadow="#4A1A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#7A1A2A", band=True, brow="scowl", light="#D7261E")
AHAB_SAD = F("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#7A1A2A", band=True, brow="sorrow", light="#9AA8C8")
JEZEBEL = F("eve", skin="#D9A27A", shadow="#6A3A4A", hair="#0D0D0F", band=True, kohl=True, collar=True, brow="scowl", light="#D7261E")
OBADIAH = F("adam", skin="#C98E66", shadow="#5A3A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#2A5A6A", cord=True, sweat=True, light="#FFE680")
ELISHA = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", scarf="#8A6A3A", cord=True, light="#FFE680")
PROPHET = F("adam", skin="#B98A6E", shadow="#4A3A4A", hair="#6A645E", hl="#9A948A", beard=True, beard_color="#7A746A", scarf="#4A3A2A", cord=True, light="#9AA8C8")
MICAIAH = F("adam", skin="#B98A6E", shadow="#3A2A3A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#3A3A4A", cord=True, light="#FFF4C2")
JEHOSHAPHAT = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#1F3A7A", band=True, light="#FFE680")
WIDOW = F("eve", skin="#B98A6E", shadow="#3A2A3A", hair="#3A3430", scarf="#3A3A3E", brow="sorrow", light="#9AA8C8")
ISRAELITE = F("adam", skin="#C47A5A", shadow="#5A3A2A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#6A5A3A", cord=True, light="#FFC14D")
MESSENGER = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", sweat=True, light="#FFE680")

def face(lines, ref, tok, bg=GOLDEN, **k): return seg(lines, ref, tok=tok, bg=bg, **k)
def drawn(lines, ref, art, bg, **k): return seg(lines, ref, bg=bg, art=art, **k)

# Reigns as roll cells: Judah's kings in gold, Israel's in red (rolls.roll_pages items).
JUDAH_C, ISRAEL_C = "#FFD23F", "#FF8A6A"
def reign(name, refs, judah=True, head=None):
    a, _, b = refs.partition("-")
    c = a.split(":")[0]
    label = f"2KGS {a}" + (f"–{b}" if b else "")
    return (name, sp(refs), label, JUDAH_C if judah else ISRAEL_C, head)

def reign_pages(items, prefix, start, **k):
    from rolls import roll_pages
    k.setdefault("tag", "THE KINGS OF JUDAH AND OF ISRAEL")
    return roll_pages(items, prefix, start, "2 Kings", "2KGS", **k)

# 2 Kings cast
ELISHA_OLD = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#6A645E", hl="#9A948A", beard=True, beard_color="#6A645E", light="#FFE680")
ELISHA_STERN = F("adam", skin="#D9A27A", shadow="#5A2A2A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", brow="scowl", light="#FFD23F")
ELISHA_BARE = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", light="#FFE680")
AHAZIAH = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", scarf="#7A1A2A", band=True, brow="sorrow", sweat=True, light="#9AA8C8")
JEHORAM = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#7A1A2A", band=True, light="#FFC14D")
CAPTAIN = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#6A2A1A", cord=True, brow="scowl", light="#D7261E")
SONS_PROPHETS = F("adam", skin="#C98E66", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#6A645E", light="#FFC14D")
