"""Drawings for the Judges volume (chapter by chapter, added below). Many Joshua drawings are reused (jos.art: crowds,
cities on hills, maps, the burning city); the digest's Deborah, Gideon and Samson panels come in through jdg.common.D."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, numbers1 as N, joshua1 as J, judges1 as J1, judges2 as J2
import samuel3 as S3
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg, node, route
from genesis.art4 import light_figure
from exo import art as A
from num.art import ALL, TRIBE_C
from jos.art import crowd_at, below, night, WAR

def f(v): return f"{v:.1f}"

# ---- Judges 1–2 ---------------------------------------------------------------------------------------------------------
def empty_table(w, h, seed):
    """Threescore and ten kings gathered their food under my table: a king's table in a dark hall, crumbs beneath it."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1418"></rect>', ground(w, h, h * 0.8, "#3A2420", dy=0)]
    o.append(S3.table(w * 0.5, h * 0.8, w * 0.6, min(1.4, h / 220)))
    for _ in range(40):
        o.append(f'<circle cx="{f(r.uniform(w * 0.2, w * 0.8))}" cy="{f(r.uniform(h * 0.84, h * 0.96))}" r="{f(r.uniform(1.5, 3.5))}" fill="#D9A25A"></circle>')
    return "".join(o)

def bochim(p, w, h, seed):
    """The angel of Jehovah at Bochim: a tall shape of white light before the people, who lifted up their voice and wept."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A3450"></rect>', hills(w, h, h * 0.46, seed, color="#4A4460", amp=14),
         ground(w, h, h * 0.56, "#4A4A5A", dy=0), light_figure(w * 0.82, b, min(1.3, h / 300))]
    for i in range(12):
        x = w * (0.04 + i * 0.055); y = b - (i % 3) * 10
        o.append(E.kneel(x, y, fit(y, h * 0.5) * 0.9, color=random.Random(seed + i).choice(["#3A3430", "#4A3A3E", "#2A2A3A", "#5A4A4E"]), skin="#6A4A3A", flip=False))
    return "".join(o)

def baalim(w, h, seed):
    """The Baalim and the Ashtaroth: standing stones and a carved pole on a high place under a red evening sky."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A1A2A"></rect>', sun(w * 0.2, h * 0.5, 30, color="#FF6A2A", op=0.4),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.74)} C {f(w * 0.3)} {f(h * 0.6)} {f(w * 0.7)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h + 10)} Z" fill="#2A0E14" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i, x in enumerate((0.36, 0.48, 0.6)):
        hh = h * (0.26 + 0.06 * (i == 1))
        o.append(f'<path d="M{f(w * x - w * 0.03)} {f(h * 0.66)} L {f(w * x - w * 0.025)} {f(h * 0.66 - hh)} C {f(w * x - w * 0.01)} {f(h * 0.62 - hh)} {f(w * x + w * 0.01)} {f(h * 0.62 - hh)} {f(w * x + w * 0.025)} {f(h * 0.66 - hh)} L {f(w * x + w * 0.03)} {f(h * 0.66)} Z" fill="#1A0A0E" stroke="#0D0D0F" stroke-width="2"></path>')
    px = w * 0.76
    o.append(f'<rect x="{f(px - 6)}" y="{f(h * 0.24)}" width="12" height="{f(h * 0.44)}" fill="#1A0A0E"></rect>'
             + "".join(f'<path d="M{f(px)} {f(h * (0.3 + k * 0.08))} L {f(px + (18 if k % 2 else -18))} {f(h * (0.26 + k * 0.08))}" stroke="#1A0A0E" stroke-width="6"></path>' for k in range(4)))
    return "".join(o)

CYCLE = ["DID EVIL", "DELIVERED TO SPOILERS", "GROANING", "A JUDGE RAISED UP", "SAVED · REST", "THE JUDGE DEAD"]
def cycle(w, h, hi=None):
    """The round of the judges as a technical diagram: evil, spoilers, groaning, a judge, deliverance, the judge's death."""
    import math
    o = [grid_bg(w, h)]
    cx, cy, r = w * 0.5, h * 0.52, min(w * 0.34, h * 0.36)
    pts = [(cx + r * math.cos(-math.pi / 2 + i * 2 * math.pi / 6), cy + r * math.sin(-math.pi / 2 + i * 2 * math.pi / 6)) for i in range(6)]
    o.append(route(pts + [pts[0]], color="#FFD23F"))
    for i, ((x, y), nm) in enumerate(zip(pts, CYCLE)):
        c = "#D7261E" if i in (0, 1) else "#5AD87A" if i in (3, 4) else "#FFD23F"
        o.append(node(x, y, nm, c, r=7 if hi == i else 5, dy=-14 if y < cy else 22, size=9))
    return "".join(o)
