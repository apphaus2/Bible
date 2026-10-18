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

# ---- Judges 6–7 ---------------------------------------------------------------------------------------------------------
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "digest"))

def midian(w, h, seed, night_=False):
    """The Midianites came in as locusts for multitude, they and their camels without number: tents and camels filling the valley."""
    import judges_book1 as JB
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{"#14123A" if night_ else "#E8B880"}"></rect>']
    if night_: o.append(mk.stars(50, w, h * 0.4, seed))
    o += [hills(w, h, h * 0.36, seed, color="#3A2A4A" if night_ else "#B5824A", amp=14), ground(w, h, h * 0.42, "#2A2030" if night_ else "#C8A06A", dy=0),
          JB.midian_camp(44, -20, w + 20, h * 0.46, h * 0.96, seed)]
    return "".join(o)

def dens(w, h, seed):
    """The dens which are in the mountains, and the caves, and the strongholds."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8A6A4A"></rect>',
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.2)} L {f(w * 0.3)} {f(h * 0.1)} L {f(w * 0.6)} {f(h * 0.24)} L {f(w + 10)} {f(h * 0.16)} L {f(w + 10)} {f(h + 10)} Z" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for x, y, s in ((0.18, 0.5, 1), (0.5, 0.66, 1.3), (0.8, 0.44, 0.8), (0.34, 0.86, 0.9), (0.72, 0.84, 1.1)):
        o.append(f'<path d="M{f(w * x - w * 0.07 * s)} {f(h * y)} C {f(w * x - w * 0.07 * s)} {f(h * y - h * 0.16 * s)} {f(w * x + w * 0.07 * s)} {f(h * y - h * 0.16 * s)} {f(w * x + w * 0.07 * s)} {f(h * y)} Z" fill="#12090A" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def rock_fire(w, h, seed):
    """The flesh and the unleavened cakes upon the rock, and fire going up out of the rock and consuming them."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A1E"></rect>', V.rays(w * 0.5, h * 0.5, 30, 20, max(w, h), color="#FFE680", op=0.25),
         ground(w, h, h * 0.8, "#4A3A2A", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h * 0.82)} C {f(w * 0.32)} {f(h * 0.64)} {f(w * 0.68)} {f(h * 0.62)} {f(w * 0.7)} {f(h * 0.82)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         E.blaze(w * 0.5, h * 0.68, w * 0.26, h * 0.5, seed, n=8)]
    return "".join(o)

def baal_down(w, h, seed, dawn=True):
    """In the morning: the altar of Baal broken down, the Asherah cut down by it, and a new altar with the offering burning."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{"#F3B86A" if dawn else "#14123A"}"></rect>', sun(w * 0.86, h * 0.3, 20, color="#FF8A3D", op=0.35),
         ground(w, h, h * 0.74, "#8A6A4A", dy=0)]
    for i in range(9):
        x = w * (0.08 + r.uniform(0, 0.3)); y = h * (0.7 + r.uniform(0, 0.12))
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.05)}" height="{f(h * 0.05)}" fill="#5A4A4A" stroke="#0D0D0F" stroke-width="1.6" transform="rotate({r.randint(-40, 40)} {f(x)} {f(y)})"></rect>')
    o.append(f'<path d="M{f(w * 0.42)} {f(h * 0.8)} L {f(w * 0.56)} {f(h * 0.74)}" stroke="#3A2214" stroke-width="10" stroke-linecap="round"></path>')
    o.append(f'<rect x="{f(w * 0.66)}" y="{f(h * 0.6)}" width="{f(w * 0.18)}" height="{f(h * 0.14)}" fill="#A89A86" stroke="#0D0D0F" stroke-width="2.4"></rect>' + E.blaze(w * 0.75, h * 0.6, w * 0.12, h * 0.26, seed, n=6))
    return "".join(o)

def dream_cake(w, h, seed):
    """The dream: a cake of barley bread tumbling into the camp of Midian and turning the tent upside down."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#14123A"></rect>', mk.stars(50, w, h * 0.5, seed), ground(w, h, h * 0.78, "#2A2030", dy=0)]
    o.append(E4.tent(w * 0.66, h * 0.8, w * 0.3, h * 0.24, color="#3A2A3E").replace("<path", f'<path transform="rotate(160 {f(w * 0.66)} {f(h * 0.72)})"', 1))
    cx, cy, rr = w * 0.32, h * 0.6, h * 0.14
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(rr)}" fill="#D9A25A" stroke="#0D0D0F" stroke-width="2.4"></circle>'
             + "".join(f'<circle cx="{f(cx + dx * rr)}" cy="{f(cy + dy * rr)}" r="3" fill="#8A5A2E"></circle>' for dx, dy in ((-0.4, -0.2), (0.3, 0.1), (0, 0.5), (-0.2, 0.4), (0.4, -0.4)))
             + "".join(f'<path d="M{f(cx - rr - 10 - k * 18)} {f(cy - 10 + k * 10)} L {f(cx - rr - 40 - k * 18)} {f(cy - 14 + k * 10)}" stroke="#FFE680" stroke-width="3" opacity="0.7"></path>' for k in range(3)))
    return "".join(o)

def ephraim_waters(p, w, h, seed):
    """The men of Ephraim take the waters as far as Beth-barah, even the Jordan, by the rock of Oreb."""
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3B86A"></rect>', sun(w * 0.14, h * 0.2, 18, color="#FF8A3D", op=0.35),
         hills(w, h, h * 0.4, seed, color="#9A8A6A", amp=12), ground(w, h, h * 0.5, "#B89A6A", dy=0),
         f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.3)} {f(h * 0.56)} {f(w * 0.6)} {f(h * 0.66)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.7)} C {f(w * 0.6)} {f(h * 0.76)} {f(w * 0.3)} {f(h * 0.66)} -10 {f(h * 0.7)} Z" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.74)} {f(h * 0.6)} L {f(w * 0.78)} {f(h * 0.36)} L {f(w * 0.9)} {f(h * 0.34)} L {f(w * 0.96)} {f(h * 0.6)} Z" fill="#7A6A5A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i in range(12):
        x = w * (0.04 + i * 0.06); y = h * 0.9 + (i % 2) * 6
        o.append(man(p, x, y, fit(y, y - h * 0.34), random.Random(seed + i).choice(WAR), extra=E4.SPEAR))
    return "".join(o)

# ---- Judges 8–9 ---------------------------------------------------------------------------------------------------------
def tower(w, h, seed, night_=False, people_on_roof=False, fire=False):
    """A strong tower of a city (Penuel, Shechem, Thebez): a tall square tower with its door and roof."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{"#14123A" if night_ else "#E8B880"}"></rect>']
    if night_: o.append(mk.stars(40, w, h * 0.5, seed))
    tx, tw, top, b = w * 0.5, w * 0.26, h * 0.16, h * 0.88
    o.append(hills(w, h, h * 0.6, seed, color="#5A3A3A" if night_ else "#B5824A", amp=12) + ground(w, h, b, "#4A3A2A" if night_ else "#9A7A4A", dy=0))
    o.append(f'<rect x="{f(tx - tw / 2)}" y="{f(top)}" width="{f(tw)}" height="{f(b - top)}" fill="#B5824A" stroke="#0D0D0F" stroke-width="2.6"></rect>'
             + "".join(f'<rect x="{f(tx - tw / 2 + i * tw / 5)}" y="{f(top - 16)}" width="{f(tw / 8)}" height="17" fill="#B5824A" stroke="#0D0D0F" stroke-width="2"></rect>' for i in range(5))
             + f'<path d="M{f(tx - tw * 0.14)} {f(b)} L {f(tx - tw * 0.14)} {f(b - h * 0.12)} C {f(tx - tw * 0.14)} {f(b - h * 0.18)} {f(tx + tw * 0.14)} {f(b - h * 0.18)} {f(tx + tw * 0.14)} {f(b - h * 0.12)} L {f(tx + tw * 0.14)} {f(b)} Z" fill="#2A140C" stroke="#0D0D0F" stroke-width="2"></path>'
             + f'<rect x="{f(tx - 6)}" y="{f(top + h * 0.12)}" width="12" height="22" fill="#2A140C"></rect>')
    if people_on_roof:
        for i in range(5):
            o.append(f'<circle cx="{f(tx - tw * 0.36 + i * tw * 0.18)}" cy="{f(top - 26)}" r="7" fill="#2A1A14" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    if fire:
        o += [E.blaze(tx + dx * tw, b, tw * 0.5, h * 0.4, seed + i, n=7) for i, dx in enumerate((-0.6, 0, 0.6))]
    return "".join(o)

def earrings(w, h, seed):
    """A garment spread, and every man casting therein the golden ear-rings of his spoil; the crescents too."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A1E"></rect>', ground(w, h, h * 0.4, "#5A4A3A", dy=0),
         f'<path d="M{f(w * 0.1)} {f(h * 0.62)} L {f(w * 0.9)} {f(h * 0.56)} L {f(w * 0.94)} {f(h * 0.94)} L {f(w * 0.06)} {f(h * 0.96)} Z" fill="#6A2A7A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for _ in range(60):
        x, y = r.uniform(w * 0.2, w * 0.8), r.uniform(h * 0.66, h * 0.9); rr = r.uniform(4, 8)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rr)}" fill="none" stroke="#E8B830" stroke-width="2.6"></circle>')
    for x in (0.26, 0.7):
        o.append(f'<path d="M{f(w * x - 16)} {f(h * 0.74)} A 16 16 0 1 0 {f(w * x + 16)} {f(h * 0.74)}" fill="none" stroke="#FFD23F" stroke-width="5"></path>')
    return "".join(o)

def ephod(w, h, seed):
    """The ephod Gideon made of the gold and set in Ophrah: a gold garment on a stand, glowing."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A2E"></rect>', V.rays(w * 0.5, h * 0.5, 30, 20, max(w, h), color="#FFD23F", op=0.18),
         ground(w, h, h * 0.86, "#3A2A2A", dy=0)]
    cx, cy, s = w * 0.5, h * 0.5, min(w, h) / 300
    o.append(f'<rect x="{f(cx - 4)}" y="{f(cy + 80 * s)}" width="8" height="{f(h * 0.86 - cy - 80 * s)}" fill="#5A3A22"></rect>'
             f'<path d="M{f(cx - 60 * s)} {f(cy - 80 * s)} L {f(cx + 60 * s)} {f(cy - 80 * s)} L {f(cx + 70 * s)} {f(cy + 90 * s)} L {f(cx - 70 * s)} {f(cy + 90 * s)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.6"></path>'
             f'<path d="M{f(cx - 64 * s)} {f(cy)} L {f(cx + 64 * s)} {f(cy)}" stroke="#7A3BA8" stroke-width="{f(10 * s)}"></path>')
    for dx, dy, c in ((-20, -40, "#D7261E"), (0, -40, "#1F5FAD"), (20, -40, "#2E9A4A"), (-20, -20, "#E8F0F6"), (0, -20, "#7A3BA8"), (20, -20, "#FF8A3D")):
        o.append(f'<circle cx="{f(cx + dx * s)}" cy="{f(cy + dy * s)}" r="{f(6 * s)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.2"></circle>')
    return "".join(o)

def jotham(p, w, h, seed):
    """Jotham on the top of mount Gerizim, lifting up his voice to the men of Shechem far below."""
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8FD0E2"></rect>', sun(w * 0.86, h * 0.16, 16, op=0.3)]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.5)} L {f(w * 0.24)} {f(h * 0.3)} L {f(w * 0.5)} {f(h * 0.6)} L {f(w * 0.5)} {f(h + 10)} Z" fill="#5A8A4A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(ground(w, h, h * 0.8, "#B89A6A", dy=0) + J.city_hill(w * 0.78, h * 0.86, w * 0.2, h * 0.14, seed))
    s = fit(h * 0.3, h * 0.12)
    o.append(man(p, w * 0.24, h * 0.3 + 2, s, "#3A6A8A", up=[(-22, -158), (-6, -196), (8, -228)]))
    return "".join(o)

LEAF = "M0 0 c -26 -6 -30 -30 -10 -38 c 6 10 20 6 24 -6 c 16 14 8 38 -14 44 Z"
def fable(w, h, which, seed):
    """Jotham's fable: the olive-tree, the fig-tree, the vine, the bramble with fire coming out of it."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{"#2A0A0A" if which == "bramble" else "#E8E2C8"}"></rect>',
         ground(w, h, h * 0.82, "#3A1A14" if which == "bramble" else "#8A7A4A", dy=0)]
    cx, b = w * 0.5, h * 0.82
    if which == "olive":
        o.append(J2.olive(cx, b, min(1.6, h / 220), seed=seed))
    elif which == "fig":
        o.append(f'<path d="M{f(cx - 10)} {f(b)} L {f(cx - 8)} {f(b - h * 0.3)} L {f(cx + 8)} {f(b - h * 0.3)} L {f(cx + 10)} {f(b)} Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2"></path>')
        for _ in range(9):
            x, y = cx + r.uniform(-w * 0.16, w * 0.16), b - h * r.uniform(0.32, 0.6)
            o.append(f'<path transform="translate({f(x)} {f(y)})" d="{LEAF}" fill="#3F7A3A" stroke="#0D0D0F" stroke-width="1.6"></path>')
        for _ in range(7):
            o.append(f'<circle cx="{f(cx + r.uniform(-w * 0.12, w * 0.12))}" cy="{f(b - h * r.uniform(0.3, 0.5))}" r="7" fill="#6A2A5A" stroke="#0D0D0F" stroke-width="1.2"></circle>')
    elif which == "vine":
        o.append(f'<path d="M{f(cx)} {f(b)} C {f(cx - 30)} {f(b - h * 0.2)} {f(cx + 30)} {f(b - h * 0.3)} {f(cx)} {f(b - h * 0.5)}" fill="none" stroke="#5A3A22" stroke-width="8"></path>')
        for k in range(4):
            x, y = cx + (-1) ** k * w * 0.08, b - h * (0.2 + k * 0.08)
            o.append("".join(f'<circle cx="{f(x + (i % 3) * 8 - 8)}" cy="{f(y + (i // 3) * 8)}" r="5" fill="#6A2A7A" stroke="#0D0D0F" stroke-width="1"></circle>' for i in range(9)))
    else:
        for _ in range(14):
            a = r.uniform(-1, 1)
            o.append(f'<path d="M{f(cx)} {f(b)} Q {f(cx + a * w * 0.1)} {f(b - h * 0.14)} {f(cx + a * w * 0.18)} {f(b - h * r.uniform(0.12, 0.26))}" fill="none" stroke="#3A2A1A" stroke-width="3"></path>')
        o.append(E.blaze(cx, b - h * 0.08, w * 0.3, h * 0.5, seed, n=8))
    return "".join(o)

def salt(w, h, seed):
    """Shechem beaten down and sowed with salt: rubble, and white salt scattered over it."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8A8A9A"></rect>', J.collapse(-10, w + 10, h * 0.8, h * 0.2, seed, color="#7A6A5A"),
         ground(w, h, h * 0.8, "#6A5A4A", dy=0)]
    for _ in range(140):
        o.append(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.6, h))}" r="{f(r.uniform(1, 2.6))}" fill="#F3F7FA"></circle>')
    return "".join(o)

BOUGH = ('<path d="M-30 -186 L 40 -176" stroke="#5A3A22" stroke-width="6"></path><circle cx="40" cy="-180" r="16" fill="#3F7A3A" stroke="#0D0D0F" stroke-width="1.4"></circle>'
         '<circle cx="22" cy="-190" r="12" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.4"></circle>')
def boughs(p, w, h, seed):
    """Abimelech and his people each with a bough cut down from the trees of mount Zalmon on his shoulder."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8B880"></rect>', hills(w, h, h * 0.42, seed, color="#3F6A3A", amp=18),
         ground(w, h, h * 0.56, "#9A7A4A", dy=0)]
    for i in range(9):
        x = w * (0.06 + i * 0.11); y = b - (i % 2) * 8
        o.append(man(p, x, y, fit(y, h * 0.46) * (1.05 if i == 0 else 0.92), "#5A1A3A" if i == 0 else random.Random(seed + i).choice(WAR), up=[(-22, -158), (-28, -178), (-20, -190)], extra=BOUGH))
    return "".join(o)

# ---- Judges 10–12 -------------------------------------------------------------------------------------------------------
def ass_colts(p, w, h, seed, n=6):
    """Sons that rode on ass colts (Jair; Abdon): a file of riders on grey asses."""
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', hills(w, h, h * 0.5, seed, color="#9A8A6A", amp=12),
         ground(w, h, h * 0.6, "#C8A06A", dy=0)]
    for i in range(n):
        x = w * (0.1 + i * 0.8 / max(1, n - 1)); y = h * 0.9 - (i % 2) * h * 0.04
        o.append(N.mount(x, y, min(0.7, h / 420), color="#8A8478", rider_cloth=random.Random(seed + i).choice(WAR), p=p))
    return "".join(o)

def daughter_door(p, w, h, seed):
    """Jephthah's house at Mizpah: his daughter coming out of the doors to meet him with timbrels and with dances."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3B86A"></rect>', sun(w * 0.86, h * 0.2, 20, color="#FF8A3D", op=0.35),
         f'<rect x="{f(w * 0.56)}" y="{f(h * 0.2)}" width="{f(w * 0.4)}" height="{f(b - h * 0.2)}" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.68)}" y="{f(h * 0.5)}" width="{f(w * 0.12)}" height="{f(b - h * 0.5)}" fill="#2A140C" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         ground(w, h, b, "#9A7A4A", dy=0)]
    s = fit(b, h * 0.44)
    tim = '<circle cx="-30" cy="-214" r="14" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></circle>'
    o.append(woman(p, w * 0.56, b, s * 0.92, "#F3EFE6", flip=True, up=[(-22, -158), (-28, -190), (-30, -214)]) + "")
    o.append(f'<circle cx="{f(w * 0.56 + 30 * s * 0.92)}" cy="{f(b - 214 * s * 0.92)}" r="{f(14 * s)}" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></circle>')
    o.append(mk.person(p, round(w * 0.16), round(b), round(s, 3), body=SKIN, cloth="#4A5A2A", sw=3, extra=A.headcloth("#4A5A2A") + A.BLACK_BEARD))
    return "".join(o)

def mountains_women(p, w, h, seed):
    """Upon the mountains: the daughter and her companions, small figures on the heights, two months."""
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A6E8A"></rect>', sun(w * 0.2, h * 0.3, 22, color="#FFE680", op=0.25),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.6)} L {f(w * 0.3)} {f(h * 0.36)} L {f(w * 0.5)} {f(h * 0.52)} L {f(w * 0.72)} {f(h * 0.3)} L {f(w + 10)} {f(h * 0.56)} L {f(w + 10)} {f(h + 10)} Z" fill="#3A4A5A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i in range(6):
        x = w * (0.62 + i * 0.03); y = h * 0.36 + abs(i - 2.5) * h * 0.02
        o.append(woman(p, x, y, fit(y, y - h * 0.12), ("#F3EFE6", "#8A6A7A", "#6A7A8A", "#9A7A6A", "#7A6A8A", "#8A7A6A")[i]))
    return "".join(o)

def fords(p, w, h, seed):
    """The fords of the Jordan held by the men of Gilead; a fugitive of Ephraim come to pass over."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8C88A"></rect>', hills(w, h, h * 0.4, seed, color="#9A8A6A", amp=12),
         ground(w, h, h * 0.5, "#B89A6A", dy=0),
         f'<path d="M{f(w * 0.36)} {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.44)} {f(h * 0.8)} {f(w * 0.38)} {f(h + 10)} L {f(w * 0.62)} {f(h + 10)} C {f(w * 0.66)} {f(h * 0.8)} {f(w * 0.54)} {f(h * 0.7)} {f(w * 0.58)} {f(h * 0.5)} Z" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></path>']
    s = fit(b, h * 0.44)
    for i in range(3): o.append(man(p, w * (0.7 + i * 0.09), b - i * 4, s, ("#4A5A2A", "#5A6A3A", "#3A4A2A")[i], flip=True, extra=E4.SPEAR))
    o.append(man(p, w * 0.2, b, s * 0.96, "#3A3A5A"))
    return "".join(o)

# ---- Judges 13–15 -------------------------------------------------------------------------------------------------------
def honey(w, h, seed):
    """A swarm of bees and honey: a honeycomb in the dry bones of the lion under a vine, bees about it."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8C88A"></rect>', ground(w, h, h * 0.76, "#C8A06A", dy=0)]
    cx, cy = w * 0.5, h * 0.7
    for i in range(6):
        o.append(f'<path d="M{f(cx - w * 0.16 + i * w * 0.06)} {f(cy + 10)} C {f(cx - w * 0.16 + i * w * 0.06)} {f(cy - h * 0.18)} {f(cx - w * 0.1 + i * w * 0.06)} {f(cy - h * 0.2)} {f(cx - w * 0.1 + i * w * 0.06)} {f(cy - h * 0.12)}" fill="none" stroke="#F3EFE6" stroke-width="6" stroke-linecap="round"></path>')
    for k in range(12):
        x = cx - w * 0.08 + (k % 4) * 16; y = cy - h * 0.08 + (k // 4) * 14
        o.append(f'<path d="M{f(x)} {f(y - 8)} L {f(x + 7)} {f(y - 4)} L {f(x + 7)} {f(y + 4)} L {f(x)} {f(y + 8)} L {f(x - 7)} {f(y + 4)} L {f(x - 7)} {f(y - 4)} Z" fill="#E8A317" stroke="#8A5A10" stroke-width="1.4"></path>')
    for _ in range(40):
        x, y = cx + r.uniform(-w * 0.3, w * 0.3), cy - r.uniform(0, h * 0.5)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="4" ry="2.4" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    return "".join(o)

def feast(p, w, h, seed):
    """The feast at Timnah: Samson and the thirty companions about a table, seven days."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#6A3A2A"></rect>', ground(w, h, b, "#3A2218", dy=0),
         S3.table(w * 0.5, b, w * 0.7, min(1.3, h / 260))]
    s = fit(b, h * 0.36)
    for i in range(10):
        x = w * (0.04 + i * 0.105)
        if abs(x - w * 0.5) < w * 0.06: continue
        o.append(man(p, x, b - h * 0.14, s * 0.8, ("#1F5FAD", "#B5121B", "#E8B830", "#7A3BA8")[i % 4], flip=x > w * 0.5,
                     extra='<path d="M-12 -200 L -8 -224 L -2 -204 L 4 -226 L 8 -204 L 14 -222 L 14 -198 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.2"></path>'))
    o.append(J2.samson(p, w * 0.5, b - h * 0.14, s * 0.84))
    return "".join(o)

def etam(p, w, h, seed, judah=False):
    """The cleft of the rock of Etam; judah=True: the men of Judah come down to it with new ropes."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#C8A06A"></rect>',
         f'<path d="M{f(w * 0.4)} {f(h + 10)} L {f(w * 0.46)} -10 L {f(w + 10)} -10 L {f(w + 10)} {f(h + 10)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.62)} {f(h * 0.3)} L {f(w * 0.66)} {f(h * 0.6)} L {f(w * 0.6)} {f(h * 0.62)} Z" fill="#12090A"></path>',
         ground(w, h, b, "#9A7A4A", dy=0)]
    o.append(J2.samson(p, w * 0.64, h * 0.62, fit(h * 0.62, h * 0.4)))
    if judah:
        for i in range(8):
            x = w * (0.04 + i * 0.045); o.append(man(p, x, b - (i % 2) * 6, fit(b, h * 0.5) * 0.9, random.Random(seed + i).choice(WAR)))
        o.append(f'<path d="M{f(w * 0.3)} {f(b - h * 0.12)} C {f(w * 0.34)} {f(b - h * 0.04)} {f(w * 0.36)} {f(b - h * 0.16)} {f(w * 0.4)} {f(b - h * 0.08)}" fill="none" stroke="#C8A06A" stroke-width="5"></path>')
    return "".join(o)

def en_hakkore(w, h, seed):
    """En-hakkore: God clave the hollow place in Lehi, and water came out of it."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3B86A"></rect>', sun(w * 0.2, h * 0.2, 20, color="#FF8A3D", op=0.4), ground(w, h, h * 0.78, "#B89A6A", dy=0),
         E4.rock(w * 0.3, h * 0.8, w * 0.4, h * 0.46), E4.gush(w * 0.5, h * 0.6, seed, scale=min(1.4, h / 300))]
    return "".join(o)

# ---- Judges 17–18 -------------------------------------------------------------------------------------------------------
def house_of_gods(w, h, seed, empty=False):
    """Micah's house of gods: the graven image and the molten image on a shelf, the ephod, the teraphim (empty=True: taken away)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A1E"></rect>', clay(w, h),
         f'<rect x="{f(w * 0.12)}" y="{f(h * 0.66)}" width="{f(w * 0.76)}" height="{f(h * 0.06)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>', ground(w, h, h * 0.9, "#2A1A10", dy=0)]
    if not empty:
        s = min(w, h) / 300
        cx = w * 0.32
        o.append(f'<path d="M{f(cx - 16 * s)} {f(h * 0.66)} L {f(cx - 12 * s)} {f(h * 0.66 - 90 * s)} C {f(cx - 10 * s)} {f(h * 0.66 - 110 * s)} {f(cx + 10 * s)} {f(h * 0.66 - 110 * s)} {f(cx + 12 * s)} {f(h * 0.66 - 90 * s)} L {f(cx + 16 * s)} {f(h * 0.66)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></path>')
        cx = w * 0.46
        o.append(f'<path d="M{f(cx - 14 * s)} {f(h * 0.66)} L {f(cx - 10 * s)} {f(h * 0.66 - 80 * s)} C {f(cx - 8 * s)} {f(h * 0.66 - 100 * s)} {f(cx + 8 * s)} {f(h * 0.66 - 100 * s)} {f(cx + 10 * s)} {f(h * 0.66 - 80 * s)} L {f(cx + 14 * s)} {f(h * 0.66)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>')
        cx = w * 0.62
        o.append(f'<path d="M{f(cx - 30 * s)} {f(h * 0.66 - 100 * s)} L {f(cx + 30 * s)} {f(h * 0.66 - 100 * s)} L {f(cx + 34 * s)} {f(h * 0.66)} L {f(cx - 34 * s)} {f(h * 0.66)} Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2"></path>')
        for i in range(3):
            x = w * (0.74 + i * 0.04)
            o.append(f'<rect x="{f(x - 6 * s)}" y="{f(h * 0.66 - 34 * s)}" width="{f(12 * s)}" height="{f(34 * s)}" rx="{f(5 * s)}" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.4)}" r="{f(w * 0.3)}" fill="#FFC14D" opacity="0.08"></circle>')
    return "".join(o)

def clay(w, h):
    return "".join(f'<path d="M0 {f(y)} L {f(w)} {f(y)}" stroke="#4A3A2A" stroke-width="2" opacity="0.6"></path>' for y in range(int(h * 0.1), int(h * 0.9), 26))

def laish(w, h, seed, burning_=False):
    """Laish in the valley by Beth-rehob: a quiet city among green hills, far from Sidon."""
    if burning_:
        from jos.art import burning
        return burning(w, h, seed, city="laish")
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8FD0E2"></rect>', sun(w * 0.86, h * 0.16, 16, op=0.3),
         hills(w, h, h * 0.4, seed, color="#5A8A4A", amp=18), J.city_hill(w * 0.5, h * 0.8, w * 0.3, h * 0.3, seed), ground(w, h, h * 0.8, "#7AAA5A", dy=0)]
    return "".join(o)

def danites_march(p, w, h, seed):
    """The six hundred Danites going their way, the little ones, the cattle and the goods before them, the priest with the ephod."""
    r = random.Random(seed); b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8C88A"></rect>', hills(w, h, h * 0.44, seed, color="#9A8A6A", amp=12),
         ground(w, h, h * 0.52, "#C8A06A", dy=0)]
    for i in range(14):
        x = w * (0.04 + i * 0.07); y = b - (i % 2) * h * 0.05
        if i < 4: o.append(E.sheep(x, y, 0.3))
        else: o.append(man(p, x, y, fit(y, y - h * 0.34), r.choice(WAR), flip=True, extra=E4.SPEAR))
    return "".join(o)

# ---- Judges 19–21 -------------------------------------------------------------------------------------------------------
def travellers(p, w, h, seed, dusk=True, city=None):
    """The Levite, his servant and a couple of asses on the road at evening (city: a walled city far off on its hill)."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{"#B5524A" if dusk else "#F3D8A0"}"></rect>',
         sun(w * 0.84, h * 0.46, 26, color="#FF8A3D", op=0.45), hills(w, h, h * 0.5, seed, color="#6A3A3A" if dusk else "#9A8A6A", amp=14)]
    if city: o.append(J.city_hill(w * 0.76, h * 0.62, w * 0.2, h * 0.2, seed))
    o.append(ground(w, h, h * 0.62, "#5A3A2A" if dusk else "#C8A06A", dy=0))
    s = fit(b, h * 0.38)
    o.append(N.ass(w * 0.42, b, s * 0.55) + N.ass(w * 0.62, b - 4, s * 0.5))
    o.append(man(p, w * 0.24, b, s, "#5A6E8A") + man(p, w * 0.78, b, s * 0.92, "#7A6A4A"))
    return "".join(o)

def bethlehem_meal(p, w, h, seed):
    """In the damsel's father's house in Beth-lehem-judah: bread and wine on the table, a lamp, the evening coming on."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A3A2A"></rect>', ground(w, h, b, "#3A2218", dy=0),
         S3.table(w * 0.5, b, w * 0.6, min(1.3, h / 260))]
    from genesis.art4 import clay_lamp
    o.append(clay_lamp(w * 0.86, h * 0.36, min(1.4, h / 240)))
    s = fit(b, h * 0.4)
    o.append(man(p, w * 0.16, b, s, "#5A6E8A", flip=False) + mk.person(p, round(w * 0.84), round(b), round(s, 3), body=SKIN, cloth="#7A5A3A", sw=3, flip=True, extra=A.WHITE_BEARD))
    return "".join(o)

def empty_street(p, w, h, seed):
    """The street of Gibeah at sundown: shut doors on either side, the wayfarers sitting in the street, no man taking them in."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#6A3A4A"></rect>', sun(w * 0.5, h * 0.36, 24, color="#FF8A3D", op=0.4)]
    for side in (0, 1):
        for k in range(3):
            x0 = (w * 0.02 + k * w * 0.11) if side == 0 else (w * 0.98 - (k + 1) * w * 0.11)
            hh = h * (0.5 - k * 0.08)
            o.append(f'<rect x="{f(x0)}" y="{f(b - hh)}" width="{f(w * 0.1)}" height="{f(hh)}" fill="#8A6A5A" stroke="#0D0D0F" stroke-width="2"></rect>'
                     f'<rect x="{f(x0 + w * 0.03)}" y="{f(b - hh * 0.4)}" width="{f(w * 0.04)}" height="{f(hh * 0.4)}" fill="#2A140C" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(ground(w, h, b, "#4A2A2A", dy=0))
    s = fit(b, h * 0.62)
    o.append(E.kneel(w * 0.44, b, s * 0.8, color="#5A6E8A", skin="#7A4A3A") + E.kneel(w * 0.56, b, s * 0.76, color="#7A6A4A", skin="#7A4A3A", flip=True))
    return "".join(o)

def shut_door(w, h, seed, dawn=False):
    """The shut door of the old man's house in Gibeah, by night or in the grey of the dawning (no one is drawn)."""
    b = h * 0.92
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{"#7A7A8A" if dawn else "#14123A"}"></rect>']
    if not dawn: o.append(mk.stars(30, w, h * 0.2, seed))
    o.append(f'<rect x="{f(w * 0.2)}" y="{f(h * 0.08)}" width="{f(w * 0.6)}" height="{f(b - h * 0.08)}" fill="{"#8A7A6A" if dawn else "#3A2A2E"}" stroke="#0D0D0F" stroke-width="2.6"></rect>'
             f'<rect x="{f(w * 0.38)}" y="{f(h * 0.34)}" width="{f(w * 0.24)}" height="{f(b - h * 0.34)}" fill="{"#5A4A3A" if dawn else "#1A0E10"}" stroke="#0D0D0F" stroke-width="2.6"></rect>'
             + "".join(f'<path d="M{f(w * 0.38)} {f(y)} L {f(w * 0.62)} {f(y)}" stroke="#0D0D0F" stroke-width="2" opacity="0.6"></path>' for y in range(int(h * 0.42), int(b), 24))
             + f'<rect x="{f(w * 0.34)}" y="{f(b)}" width="{f(w * 0.32)}" height="{f(h * 0.03)}" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(ground(w, h, b + h * 0.03, "#4A4A5A" if dawn else "#0E0A14", dy=0))
    if dawn: o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#E8C8A0" opacity="0.25"></rect>')
    return "".join(o)

TRIBES12 = ["REUBEN", "SIMEON", "JUDAH", "ISSACHAR", "ZEBULUN", "DAN", "NAPHTALI", "GAD", "ASHER", "BENJAMIN", "EPHRAIM", "MANASSEH"]
def borders(w, h):
    """Sent throughout all the borders of Israel: twelve routes out from the hill-country of Ephraim, as a technical figure."""
    import math
    o = [grid_bg(w, h)]
    cx, cy = w * 0.5, h * 0.54
    r = min(w * 0.4, h * 0.38)
    for i, t in enumerate(TRIBES12):
        a = -math.pi / 2 + i * 2 * math.pi / 12
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        o.append(route([(cx, cy), (x, y)], color="#D7261E", sw=1.8))
        o.append(node(x, y, t, TRIBE_C[t], r=4, dy=-9 if y < cy else 16, size=8))
    o.append(node(cx, cy, "", "#FFD23F", r=6))
    return "".join(o)

def gibeah_plan(w, h, stage=0):
    """The third day at Gibeah as a technical map: the city, the two highways to Beth-el and to Gibeah, the array at
    Baal-tamar, the liers-in-wait at Maareh-geba; stage=1 adds the pillar of smoke and the flight toward the wilderness."""
    o = [grid_bg(w, h)]
    gx, gy = w * 0.5, h * 0.36
    o.append(f'<rect x="{f(gx - 34)}" y="{f(gy - 20)}" width="68" height="40" fill="#B5824A" opacity="0.7" stroke="#FFD23F" stroke-width="2"></rect>' + label(gx, gy + 5, "GIBEAH", "#F3EFE6", 11))
    o.append(route([(gx, gy + 20), (w * 0.2, h * 0.86)], color="#8FD0E2", arrow=False) + label(w * 0.2, h * 0.92, "TO BETH-EL", "#8FD0E2", 8))
    o.append(route([(gx + 20, gy + 20), (w * 0.62, h * 0.9)], color="#8FD0E2", arrow=False) + label(w * 0.62, h * 0.95, "THE FIELD", "#8FD0E2", 8))
    o.append(node(w * 0.36, h * 0.74, "BAAL-TAMAR", "#5AD87A", r=5, dy=18, size=8))
    o.append(f'<rect x="{f(w * 0.68)}" y="{f(h * 0.2)}" width="{f(w * 0.14)}" height="{f(h * 0.14)}" fill="#D7261E" opacity="0.3" stroke="#D7261E" stroke-width="2" stroke-dasharray="5 4"></rect>'
             + label(w * 0.75, h * 0.18, "MAAREH-GEBA", "#FF6A5A", 8))
    if stage:
        o.append(f'<path d="M{f(gx)} {f(gy - 20)} C {f(gx - 20)} {f(h * 0.2)} {f(gx + 20)} {f(h * 0.12)} {f(gx)} {f(h * 0.02)}" fill="none" stroke="#C8C2D6" stroke-width="14" opacity="0.6"></path>')
        o.append(route([(w * 0.68, h * 0.27), (gx + 36, gy)], color="#FF6A5A"))
        o.append(route([(w * 0.4, h * 0.6), (w * 0.9, h * 0.72)], color="#FFB04A") + label(w * 0.9, h * 0.68, "THE WILDERNESS", "#C8A06A", 8, "end"))
    return "".join(o)

def rimmon(p, w, h, seed):
    """The rock of Rimmon in the wilderness, where six hundred men of Benjamin abode four months."""
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8B880"></rect>', sun(w * 0.86, h * 0.18, 18, color="#FF8A3D", op=0.35),
         ground(w, h, h * 0.8, "#C8A06A", dy=0), E4.rock(w * 0.2, h * 0.82, w * 0.6, h * 0.6, color="#9A6A4A", dark="#5A3A2A")]
    for i in range(7):
        x = w * (0.34 + i * 0.05); y = h * 0.3 + abs(i - 3) * h * 0.03
        o.append(man(p, x, y, fit(y, y - h * 0.08), "#3A2A2A"))
    return "".join(o)

def dances(p, w, h, seed):
    """The feast of Jehovah at Shiloh: the daughters of Shiloh coming out to dance in the dances, the vineyards about."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.86, h * 0.14, 16, op=0.3),
         hills(w, h, h * 0.4, seed, color="#7A9A5A", amp=14), ground(w, h, h * 0.48, "#9CCB5E", dy=0)]
    for k in range(2):
        for i in range(9):
            x = w * (0.04 + i * 0.12) + (k % 2) * w * 0.06; y = h * (0.56 + k * 0.08) if i % 4 else h * (0.86 + k * 0.06)
            if i % 4 == 0: continue
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 20)}" stroke="#5A3A22" stroke-width="3"></path><circle cx="{f(x - 6)}" cy="{f(y - 22)}" r="8" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.2"></circle><circle cx="{f(x + 5)}" cy="{f(y - 16)}" r="4" fill="#6A2A7A"></circle>')
    b = h * 0.9
    for i in range(7):
        x = w * (0.2 + i * 0.1); y = b - (i % 2) * 8
        o.append(woman(p, x, y, fit(y, h * 0.56), r.choice(["#F3EFE6", "#E8B830", "#C2456A", "#5AC8C8", "#B88AE8"]), flip=i % 2 == 1))
    return "".join(o)
