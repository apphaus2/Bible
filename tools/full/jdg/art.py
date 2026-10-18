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

# ---- Judges 3–5 ---------------------------------------------------------------------------------------------------------
def nations_left(w, h):
    """The nations left to prove Israel, as a technical map: the five lords of the Philistines, the Sidonians, the Hivites of
    Lebanon unto Hamath, Israel among the Canaanites."""
    from jos.art import remaineth_map
    return remaineth_map(w, h)

def tribute(p, w, h, seed):
    """Ehud and the men that bare the tribute before Eglon king of Moab in his palace (a seated king at a distance)."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#6A2A3A"></rect>']
    for x in (0.06, 0.94):
        o.append(f'<rect x="{f(w * x - 16)}" y="-10" width="32" height="{f(b + 10)}" fill="#C8962E" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(ground(w, h, b, "#4A1A2A", dy=0) + S3.throne(w * 0.8, b, min(1.2, h / 260)))
    s = fit(b, h * 0.44)
    o.append(mk.person(p, round(w * 0.8), round(b - 30 * s), round(s * 1.15, 3), body=SKIN, cloth="#5A2A6A", sw=3, flip=True,
                       extra='<path d="M-14 -200 L -14 -214 L -7 -206 L 0 -218 L 7 -206 L 14 -214 L 14 -200 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>'))
    for i in range(4):
        x = w * (0.16 + i * 0.1)
        o.append(man(p, x, b, s, ("#6A5A3A", "#5A4A3A", "#7A6A4A", "#5A6E8A")[i], up=[(-22, -158), (-6, -176), (12, -182)])
                 + f'<rect x="{f(x - 6 * s)}" y="{f(b - 200 * s)}" width="{f(30 * s)}" height="{f(20 * s)}" rx="3" fill="#C8A06A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)

def locked_door(p, w, h, seed, servants=True):
    """The doors of the cool upper room shut and locked; the king's servants tarrying outside (nothing within is shown)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#C8A87A"></rect>',
         f'<rect x="{f(w * 0.36)}" y="{f(h * 0.12)}" width="{f(w * 0.28)}" height="{f(b - h * 0.12)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="3"></rect>',
         f'<path d="M{f(w * 0.5)} {f(h * 0.12)} L {f(w * 0.5)} {f(b)}" stroke="#0D0D0F" stroke-width="3"></path>',
         f'<rect x="{f(w * 0.48)}" y="{f(h * 0.5)}" width="{f(w * 0.04)}" height="{f(h * 0.08)}" rx="3" fill="#8A8A9A" stroke="#0D0D0F" stroke-width="2"></rect>',
         ground(w, h, b, "#8A6A4A", dy=0)]
    if servants:
        s = fit(b, h * 0.36)
        for i, x in enumerate((0.12, 0.22, 0.78, 0.88)):
            o.append(man(p, w * x, b, s, ("#5A2A6A", "#6A3A5A")[i % 2], flip=x > 0.5))
    return "".join(o)

def trumpet_hills(p, w, h, seed):
    """Ehud blew a trumpet in the hill-country of Ephraim; the children of Israel went down with him."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3B86A"></rect>', sun(w * 0.86, h * 0.2, 18, color="#FF8A3D", op=0.35),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.4)} {f(w * 0.6)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} Z" fill="#7A6A3A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = fit(h * 0.5, h * 0.22)
    o.append(J.trumpeter(p, w * 0.14, h * 0.5, s) + J.blasts(w * 0.18, h * 0.5 - 200 * s, s * 1.2))
    for i in range(10):
        t = i / 9; x = w * (0.28 + 0.66 * t); y = h * (0.5 + 0.34 * t) + 6
        o.append(man(p, x, y, fit(y, y - h * (0.16 + 0.1 * t)), random.Random(seed + i).choice(WAR), extra=E4.SPEAR))
    return "".join(o)

def ox_goad(p, w, h, seed):
    """Shamgar the son of Anath with an ox-goad; the Philistines' feathered head-dresses far off."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.86, h * 0.16, 16, op=0.3),
         hills(w, h, h * 0.5, seed, color="#C8A06A", amp=12), ground(w, h, h * 0.58, "#B89A6A", dy=0)]
    o.append(J2.philistines(p, 9, w * 0.56, w * 0.98, h * 0.62, h * 0.7, seed, 0.16, 0.22, flip=True))
    s = fit(b, h * 0.36)
    goad = '<path d="M30 -150 L 120 -250" stroke="#6A4A2A" stroke-width="6" stroke-linecap="round"></path><path d="M120 -250 L 128 -262" stroke="#C8C2D6" stroke-width="4"></path>'
    o.append(man(p, w * 0.24, b, s, "#8A5A2A", up=[(-22, -158), (4, -150), (30, -150)], extra=goad))
    return "".join(o)

def palm_judge(p, w, h, seed):
    """Deborah under the palm-tree between Ramah and Beth-el; the children of Israel coming up to her for judgment."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', hills(w, h, h * 0.5, seed, color="#9A8A6A", amp=12),
         ground(w, h, h * 0.6, "#C8A06A", dy=0), J1.palm(w * 0.2, b, min(1.4, h / 300))]
    s = fit(b, h * 0.42)
    o.append(woman(p, w * 0.3, b, s, "#E8B830"))
    o.append(crowd_at(p, w, h, seed, w * 0.44, w + 10, h * 0.66, b, 14, fit(h * 0.66, h * 0.5) * 0.8, s * 0.94, flip=True))
    return "".join(o)

def kishon(w, h, seed):
    """The river Kishon swept them away: the torrent in flood, wheels and a broken chariot in it, stars above."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0F0E2A"></rect>', mk.stars(60, w, h * 0.45, seed, color="#FFE680")]
    o.append(f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.46)} {f(w * 0.6)} {f(h * 0.56)} {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1F4A7A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for i in range(10):
        y = h * (0.56 + i * 0.045)
        o.append(f'<path d="M{f(-10 + (i % 3) * 30)} {f(y)} C {f(w * 0.3)} {f(y - 10)} {f(w * 0.6)} {f(y + 10)} {f(w + 10)} {f(y)}" fill="none" stroke="#8FD0E2" stroke-width="2" opacity="0.6"></path>')
    for i in range(3):
        x = w * (0.2 + i * 0.3); y = h * (0.7 + (i % 2) * 0.1)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(h * 0.06)}" fill="none" stroke="#C8962E" stroke-width="5" transform="rotate({i * 30} {f(x)} {f(y)})"></circle>'
                 + "".join(f'<path d="M{f(x)} {f(y)} L {f(x + h * 0.06 * c)} {f(y + h * 0.06 * s_)}" stroke="#C8962E" stroke-width="3"></path>' for c, s_ in ((1, 0), (0, 1), (-1, 0), (0, -1))))
    return "".join(o)

def lattice(w, h, seed):
    """The mother of Sisera looking forth through the lattice of a window, a dark figure at evening (no face drawn)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#7A5A4A"></rect>']
    ww, wh = w * 0.3, h * 0.5
    o.append(S3.window(w * 0.5, h * 0.36, ww, wh, inner="#FF8A3D"))
    o.append(f'<path d="M{f(w * 0.5 - ww * 0.2)} {f(h * 0.36 + wh)} L {f(w * 0.5 - ww * 0.2)} {f(h * 0.36 + wh * 0.3)} C {f(w * 0.5 - ww * 0.2)} {f(h * 0.36)} {f(w * 0.5 + ww * 0.2)} {f(h * 0.36)} {f(w * 0.5 + ww * 0.2)} {f(h * 0.36 + wh * 0.3)} L {f(w * 0.5 + ww * 0.2)} {f(h * 0.36 + wh)} Z" fill="#12090A"></path>')
    for k in range(1, 6):
        x = w * 0.5 - ww / 2 + k * ww / 6
        o.append(f'<path d="M{f(x)} {f(h * 0.36 - ww * 0.4)} L {f(x)} {f(h * 0.36 + wh)}" stroke="#5A3A22" stroke-width="4"></path>')
    for k in range(1, 6):
        y = h * 0.36 + (k - 1) * wh / 5
        o.append(f'<path d="M{f(w * 0.5 - ww / 2)} {f(y)} L {f(w * 0.5 + ww / 2)} {f(y)}" stroke="#5A3A22" stroke-width="4"></path>')
    return "".join(o)
