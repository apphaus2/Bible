"""Shared helpers for the Nehemiah chapters: line builders for discourse.pack, roll cells for lists, and the cast's faces.

Nehemiah: black beard, a deep slate-blue headcloth with a gold cord (a Jew in the Persian court), gold rim light; grieving
in cold light with a tear, afraid with sweat, stern in red light. Artaxerxes: black curled beard, purple headcloth with the
gold band. Sanballat the Horonite: dark-red headcloth with the band, black beard, scowl. Tobiah the Ammonite: dark-green
headcloth, stubble. Geshem the Arabian: white headcloth with a black cord, kohl. Ezra the priest the scribe: white hair and
beard, indigo headcloth with the gold band. Eliashib the high priest: white headcloth with the gold band."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from discourse import seg, pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from neh import G

v, sp = G.v, G.span
CODE = "NEH"
def say(ref, frm=None, to=None, after=None): return ("say", v(ref, frm=frm, to=to, after=after))
def gd(ref, frm=None, to=None, after=None): return ("god", v(ref, frm=frm, to=to, after=after))
def cp(ref, frm=None, to=None, after=None): return ("cap", v(ref, frm=frm, to=to, after=after))
def sg(ref, frm=None, to=None, after=None): return ("song", v(ref, frm=frm, to=to, after=after))
def says(refs): return ("say", sp(refs))
def gods(refs): return ("god", sp(refs))
def caps(refs): return ("cap", sp(refs))
def sgs(refs): return ("song", sp(refs))
def joined(kind, *parts):
    """One box from several cuts: joined("say", ("1:2", "Let there", None), "1:3") — a ref alone is the whole verse."""
    return (kind, " ".join(v(p) if isinstance(p, str) else v(p[0], frm=p[1], to=p[2] if len(p) > 2 else None) for p in parts))

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 0.92)
    k.setdefault("min_size", 12.5)
    return _pack(segs, prefix, start, book="Nehemiah", code=CODE, **k)

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
    return roll_pages(items, prefix, start, "Nehemiah", CODE, tag=tag, **k)

# Nehemiah cast
_neh = dict(skin="#C98E66", shadow="#5A3A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#2A3A5A", cord=True)
NEHEMIAH = F("adam", light="#FFE680", **_neh)
NEHEMIAH_GRIEF = F("adam", brow="sorrow", tear=True, light="#9AA8C8", **_neh)
NEHEMIAH_PRAY = F("adam", brow="sorrow", light="#FFF4C2", **_neh)
NEHEMIAH_AFRAID = F("adam", brow="sorrow", sweat=True, light="#FFC14D", **_neh)
NEHEMIAH_STERN = F("adam", brow="scowl", light="#D7261E", **_neh)
_neh_old = dict(_neh, hair="#5A544E", hl="#8A847A", beard_color="#6A645E")
NEHEMIAH_OLD = F("adam", light="#FFE680", **_neh_old)
NEHEMIAH_OLD_STERN = F("adam", brow="scowl", light="#D7261E", **_neh_old)
ARTAXERXES = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#5A1A6A", band=True, light="#FFC14D")
QUEEN = F("eve", skin="#D9A27A", shadow="#6A3A4A", hair="#0D0D0F", scarf="#5A1A6A", band=True, kohl=True, light="#FFE680")
HANANI = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#3A2A1A", scarf="#4A5A3A", cord=True, brow="sorrow", sweat=True, light="#FFC14D")
SANBALLAT = F("adam", skin="#C47A5A", shadow="#4A1A1A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#5A1A1E", band=True, brow="scowl", light="#D7261E")
TOBIAH = F("adam", skin="#B98A6E", shadow="#2A3A2A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#1F4A34", cord=True, brow="scowl", light="#9CCB5E")
GESHEM = F("adam", skin="#8A5A3A", shadow="#3A2014", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#E8E2D6", cord=True, kohl=True, light="#FFC14D")
EZRA = F("adam", skin="#C98E66", shadow="#5A4A4A", hair="#E8E2D6", hl="#F3EFE6", beard=True, beard_color="#E8E2D6", scarf="#2A2A6A", band=True, light="#FFE680")
ELIASHIB = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#D8D2C6", hl="#F3EFE6", beard=True, beard_color="#D8D2C6", scarf="#F3EFE6", band=True, light="#FFE680")
SHEMAIAH = F("adam", skin="#B98A6E", shadow="#3A2A3A", hair="#5A544E", hl="#8A847A", beard=True, beard_color="#5A544E", scarf="#3A3A4A", cord=True, brow="sorrow", sweat=True, light="#9AA8C8")
LEVITE = F("adam", skin="#B98A6E", shadow="#5A4A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#F3EFE6", cord=True, light="#FFF4C2")
PEOPLE = F("adam", skin="#B98A6E", shadow="#3A2A3A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#6A5A3A", brow="sorrow", sweat=True, light="#9AA8C8")
MOTHER = F("eve", skin="#C98E66", shadow="#3A2A3A", hair="#2A1A10", scarf="#4A3A5A", brow="sorrow", tear=True, light="#9AA8C8")
JUDAH_MAN = F("adam", skin="#C47A5A", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#4A4A3A", brow="sorrow", sweat=True, light="#FFC14D")
NOBLE = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#3A2A1A", hl="#5A4A3E", beard=True, beard_color="#3A2A1A", scarf="#6A3A5A", band=True, light="#FFC14D")

def _rng(refs_list):
    a = refs_list[0].split("-")[0]
    last = refs_list[-1].split("-")[-1]
    if ":" not in last: last = refs_list[-1].split(":")[0] + ":" + last
    if a == last: return a
    return f"{a}–{last.split(':')[1]}" if a.split(":")[0] == last.split(":")[0] else f"{a}–{last}"

def plan_pages(pages, prefix, start, tag="", stamp=None, end=""):
    """Pages of a list told along a drawing: each page is one picture panel on top (art(w, h), ph px tall) over roll cells
    for the verses, every word. pages: [(head, art, ph, [(name, refs, accent), ...])]; returns [(file, board title, fn)]
    like discourse.pack. The cells take the largest type size (up to 16px) at which they fit under the picture."""
    import re, mk
    from fx import page, new, vref
    from genesis.ch02 import grid
    from genesis.ch03 import clan
    from rolls import need
    out = []
    for k, (head, art, ph, items) in enumerate(pages):
        cells = [(nm, sp(refs), label(refs), acc) for nm, refs, acc in items]
        e = end if k == len(pages) - 1 else ""
        room = 1022 - ph - 12 * len(cells) - (64 if e else 0)
        s = 16.0
        while s > 10 and sum(need(t, s) for _, t, _, _ in cells) > room: s -= 0.5
        hs = [need(t, s) for _, t, _, _ in cells]
        ph = max(ph, min(int(ph * 1.6), 1022 - 12 * len(cells) - (64 if e else 0) - int(sum(hs))))   # spare room goes to the picture
        if e: hs[-1] += 64
        fr = f"{ph}px " + " ".join(f"{x:.0f}fr" for x in hs)
        over = (mk.stamp(stamp, "right: 12px; top: 10px") if stamp and k == 0 else "") + (vref(tag, "right: 8px; bottom: 7px") if tag else "")
        pan = new("#0B1A2E", 702, ph - 6, art(702, ph - 6), over)
        body = grid([pan] + [clan(nm, t, ref, c, size=s) for nm, t, ref, c in cells], fr, ncol=1) + e
        rng = _rng([refs for _, refs, _ in items])
        title = f"Nehemiah {rng} — {head}"
        slug = re.sub(r"[^A-Za-z]", "", head.title())[:18]
        out.append((f"{prefix}-P{k + 1:02d}-{slug}", f"{start + k} · {head}", (lambda title=title, body=body, n=start + k: page(title, "minmax(0, 1fr)", body, n))))
    return out
