"""Shared helpers for the Esther chapters: line builders for discourse.pack, roll cells, and the cast's faces.

Ahasuerus: black hair and long black beard, bareheaded under a gold Persian crown (crowned()), purple light. Vashti: black
hair, kohl, the crown. Esther: young, long dark hair, bareheaded; crowned from 2:17. Mordecai: grey-black beard, olive-green
headcloth with a cord; sackcloth (a coarse grey-brown cloth over his head, ash-pale skin) in ch. 4; royal apparel of blue and
white with a great crown of gold in ch. 8. Haman: dark-red headcloth with a gold band, black beard, scowl, red light. Zeresh:
plum headscarf, kohl. Hegai, Hathach and Harbonah: beardless chamberlains (white, tan and teal headcloths). Memucan: blue
headcloth with a gold band."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from faces_ex import F
from discourse import seg, pack as _pack
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from est import G

v, sp = G.v, G.span
CODE = "ESTH"
def say(ref, frm=None, to=None, after=None): return ("say", v(ref, frm=frm, to=to, after=after))
def cp(ref, frm=None, to=None, after=None): return ("cap", v(ref, frm=frm, to=to, after=after))
def says(refs): return ("say", sp(refs))
def caps(refs): return ("cap", sp(refs))
def joined(kind, *parts):
    """One box from several cuts: joined("say", ("1:2", "Let there", None), "1:3") — a ref alone is the whole verse."""
    return (kind, " ".join(v(p) if isinstance(p, str) else v(p[0], frm=p[1], to=p[2] if len(p) > 2 else None) for p in parts))

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 0.92)
    k.setdefault("min_size", 12.5)
    return _pack(segs, prefix, start, book="Esther", code=CODE, **k)

def face(lines, ref, tok, bg=GOLDEN, **k): return seg(lines, ref, tok=tok, bg=bg, **k)
def drawn(lines, ref, art, bg, **k): return seg(lines, ref, bg=bg, art=art, **k)

def label(refs):
    a, _, b = refs.partition("-")
    return f"{CODE} {a}" + (f"–{b}" if b else "")

def cell(name, refs, accent="#FFD23F", head=None):
    """One roll cell: a name over verses refs ("9:7-10"), every word."""
    return (name, sp(refs), label(refs), accent, head)

def roll(items, prefix, start, tag, **k):
    from rolls import roll_pages
    return roll_pages(items, prefix, start, "Esther", CODE, tag=tag, **k)

def tshade(svg, top=440):
    """A chapter title's art: the dark band at the top (deu.common.shade) and another at the foot, so the credit line reads."""
    from deu.common import shade
    return (shade(svg, top) + '<defs><linearGradient id="tfoot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1A1028" stop-opacity="0"></stop>'
            '<stop offset="1" stop-color="#1A1028" stop-opacity="0.9"></stop></linearGradient></defs><rect x="0" y="940" width="760" height="140" fill="url(#tfoot)"></rect>')

# a Persian crown on a close-up face (face coordinates: the head's band runs from x 100 to 238 at y ~104)
def _crown(big=False, color="#E8B830"):
    top = 40 if big else 58
    n = 9
    xs = [236 - i * (130 / n) for i in range(n + 1)]
    d = "M238 106"
    for i in range(n):
        y = top + (0 if i % 2 == 0 else 11) + i * 0.8
        d += f" L {xs[i]:.1f} {y:.1f} L {xs[i + 1]:.1f} {y:.1f}"
    d += " L 102 110 C 160 96 206 98 238 106 Z"
    gems = "".join(f'<circle cx="{x}" cy="{(top + 104) / 2 + 6 + (236 - x) * 0.04:.1f}" r="4.5" fill="{c}" stroke="#0D0D0F" stroke-width="1.2"></circle>'
                   for x, c in ((214, "#2C9DB8"), (170, "#D7261E"), (128, "#2C9DB8")))
    return (f'\n<path d="{d}" fill="{color}" stroke="#0D0D0F" stroke-width="2.2" stroke-linejoin="round"></path>'
            f'\n<path d="M236 {top + 18} C 200 {top + 12} 150 {top + 12} 108 {top + 22}" fill="none" stroke="#0D0D0F" stroke-width="1.4" opacity="0.5"></path>' + gems
            + f'\n<path d="M238 106 C 206 98 160 96 102 110" fill="none" stroke="#FFF4C2" stroke-width="2" opacity="0.6"></path>')
def crowned(tok, big=False): return tok + _crown(big)

# Esther cast
AHASUERUS = crowned(F("adam", skin="#C98E66", shadow="#4A3A5A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", light="#FFD23F"))
AHAS_MERRY = crowned(F("adam", skin="#D99A6E", shadow="#6A3A3A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", laugh=True, light="#FFC14D"))
AHAS_WROTH = crowned(F("adam", skin="#C47A5A", shadow="#4A1A1A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", brow="scowl", light="#D7261E"))
AHAS_NIGHT = crowned(F("adam", skin="#A88A8A", shadow="#3A2A4A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", brow="sorrow", light="#FFC14D"))
VASHTI = crowned(F("eve", skin="#D9A27A", shadow="#6A3A3A", hair="#0D0D0F", kohl=True, brow="scowl", light="#FFC14D"))
ESTHER = F("eve", skin="#E3B08A", shadow="#9A6A5A", hair="#1A1210", light="#FFE680")
ESTHER_QUEEN = crowned(F("eve", skin="#E3B08A", shadow="#9A6A5A", hair="#1A1210", light="#FFE680"))
ESTHER_GRIEF = crowned(F("eve", skin="#C8A08A", shadow="#4A3A5A", hair="#1A1210", brow="sorrow", tear=True, light="#9AA8C8"))
ESTHER_RESOLVE = crowned(F("eve", skin="#D9A27A", shadow="#5A3A4A", hair="#1A1210", brow="scowl", light="#FFD23F"))
MORDECAI = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#4A4440", hl="#7A746A", beard=True, beard_color="#5A5450", scarf="#4A6A4A", cord=True, light="#FFE680")
MORDECAI_SACK = F("adam", skin="#A89A90", shadow="#4A4448", hair="#5A5450", hl="#8A847A", beard=True, beard_color="#6A645E", scarf="#5A4E3E", brow="sorrow", tear=True, light="#9AA8C8")
MORDECAI_ROYAL = crowned(F("adam", skin="#C98E66", shadow="#4A4A6A", hair="#4A4440", hl="#7A746A", beard=True, beard_color="#5A5450", scarf="#F3EFE6", light="#8FD0E2"), big=True)
HAMAN = F("adam", skin="#C47A5A", shadow="#4A1A1A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#7A1A1A", band=True, brow="scowl", light="#D7261E")
HAMAN_GLAD = F("adam", skin="#D99A6E", shadow="#6A3A2A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#7A1A1A", band=True, laugh=True, light="#FFC14D")
HAMAN_AFRAID = F("adam", skin="#B8A0A0", shadow="#3A2A4A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#7A1A1A", band=True, brow="sorrow", sweat=True, light="#9AA8C8")
HAMAN_MOURN = F("adam", skin="#A88A80", shadow="#3A2A3A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#3A3438", brow="sorrow", light="#9AA8C8")
ZERESH = F("eve", skin="#D9A27A", shadow="#5A2A3A", hair="#0D0D0F", scarf="#5A1A3A", band=True, kohl=True, brow="scowl", light="#D7261E")
ZERESH_FEAR = F("eve", skin="#C8A08A", shadow="#3A2A4A", hair="#0D0D0F", scarf="#5A1A3A", band=True, kohl=True, brow="sorrow", light="#9AA8C8")
MEMUCAN = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#1F3A7A", band=True, light="#FFC14D")
HEGAI = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#1A1210", hl="#4A3A2E", scarf="#E8E2D6", band=True, light="#FFE680")
HATHACH = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#1A1210", hl="#4A3A2E", scarf="#C8A06A", cord=True, light="#FFE680")
HARBONAH = F("adam", skin="#B98A6E", shadow="#3A3A4A", hair="#1A1210", hl="#4A3A2E", scarf="#2A5A6A", band=True, light="#FFC14D")
SERVANT = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#1A1210", hl="#4A3A2E", stubble="#2A1A10", scarf="#8A6A3A", cord=True, light="#FFE680")
