"""Drawings for the Zephaniah volume, on the minor prophets' kit (oba.minor), with Micah's and Nahum's where they fit. The
day of Jehovah is darkness, clouds, trumpets and fire over the land — no one slain is drawn (1:17 is words over the dark
plain); the housetops where the host of heaven is worshipped; the fish gate; Jerusalem searched with lamps; the coast of
the Philistines as a map and then as pastures; Moab's nettles and saltpits; Nineveh a ruin with the pelican and the
porcupine in its capitals; the oppressing city at evening; and Zion singing."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from oba.minor import *
from mic.art import remnant, mountain_house
from nam.art import nineveh_wall
import joshua1 as J1

ZEPH_C = "#5A2A4A"

def desolate(w, h, seed):
    """I will utterly consume all things from off the face of the ground — man and beast, the birds of the heavens and the
    fishes of the sea: an empty land and a dry shore under a dark sky, nothing living."""
    o = [sky(w, h, "#1A1418", "#6A4A3A"), hills(w, h, h * 0.5, seed, color="#3A2A2A", amp=14), ground(w, h, h * 0.56, "#6A5040", dy=0),
         f'<path d="M{f(w * 0.6)} {f(h * 0.56)} C {f(w * 0.7)} {f(h * 0.7)} {f(w * 0.8)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.86)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.5)} {f(h + 10)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></path>']
    r = random.Random(seed)
    for i in range(9):
        x, y = r.uniform(0, w * 0.6), r.uniform(h * 0.62, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(10, 30))} {f(r.uniform(-4, 4))}" stroke="#3A2A20" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.2)} {f(h * 0.92)} l 14 -30 l 4 30 M{f(w * 0.2 + 2)} {f(h * 0.8)} l -12 -8 M{f(w * 0.2 + 8)} {f(h * 0.76)} l 12 -10" stroke="#2A1A14" stroke-width="3" fill="none"></path>')
    return "".join(o)

def housetops(p, w, h, seed):
    """Them that worship the host of heaven upon the housetops: flat roofs at night under the stars, small figures bowed on
    them, a pillar of Baal in a courtyard."""
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#2A1E4A"), starfield(w, h, seed, 90, 0.6), J.moon(w * 0.84, h * 0.14, max(10, h * 0.04))]
    r = random.Random(seed)
    x = -10
    while x < w:
        bw = r.uniform(w * 0.12, w * 0.2); top = h * r.uniform(0.5, 0.66)
        o.append(f'<rect x="{f(x)}" y="{f(top)}" width="{f(bw)}" height="{f(h - top + 10)}" fill="#3A3048" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(x + bw * 0.4)}" y="{f(top + h * 0.12)}" width="{f(bw * 0.16)}" height="{f(h * 0.08)}" fill="#FFC14D"></rect>')
        if r.random() < 0.6: o.append(E.kneel(x + bw * 0.5, top, fit(top, top - h * 0.12) * 0.9, color="#1A1220", flip=r.random() < 0.5))
        x += bw
    o.append(f'<path d="M{f(w * 0.46)} {f(h + 10)} L {f(w * 0.47)} {f(h * 0.42)} L {f(w * 0.5)} {f(h * 0.4)} L {f(w * 0.51)} {f(h + 10)} Z" fill="#6A5A5A" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def sacrifice_day(w, h, seed):
    """Hold thy peace: the day of Jehovah is at hand; Jehovah hath prepared a sacrifice — the princes in foreign apparel, those
    that leap over the threshold: a palace threshold and its open door, rich garments thrown on it, the altar smoking beyond
    under a red sky."""
    import samuel4 as S4
    o = [sky(w, h, "#3A0A10", "#C8603A"), S4.altar(w * 0.76, h * 0.7, min(1.0, h / 300), seed=seed), ground(w, h, h * 0.7, "#5A3A2A", dy=0),
         f'<rect x="{f(w * 0.06)}" y="{f(h * 0.1)}" width="{f(w * 0.4)}" height="{f(h * 0.8)}" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.14)}" y="{f(h * 0.28)}" width="{f(w * 0.24)}" height="{f(h * 0.62)}" fill="#120A0A" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.1)}" y="{f(h * 0.88)}" width="{f(w * 0.32)}" height="{f(h * 0.05)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.18)} {f(h * 0.88)} l 30 -16 l 40 6 l 14 10 Z" fill="#7A2A6A" stroke="#0D0D0F" stroke-width="1.6"></path>'
         f'<path d="M{f(w * 0.28)} {f(h * 0.88)} l 24 -10 l 30 4 l 6 6 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>']
    return "".join(o)

def fish_gate(w, h, seed):
    """The noise of a cry from the fish gate, a wailing from the second quarter, a great crashing from the hills: the
    gate of Jerusalem with its sign, sound lines bursting from it and rocks tumbling on the hills."""
    o = [sky(w, h, "#3A2A3A", "#C8906A"), hills(w, h, h * 0.44, seed, color="#5A4040", amp=24), walls(-10, w + 10, h * 0.78, h * 0.5, seed, color="#B8986A", towers=2),
         label(w * 0.42, h * 0.38, "THE FISH GATE", "#F3EFE6", 11), ground(w, h, h * 0.78, "#7A5A40", dy=0)]
    o.append(mk.speed(w * 0.42, h * 0.62, 20, h * 0.12, h * 0.4, seed, color="#FFF4C2", op=0.7))
    r = random.Random(seed)
    for i in range(8):
        x, y = r.uniform(w * 0.6, w), r.uniform(h * 0.2, h * 0.42)
        o.append(f'<path d="M{f(x)} {f(y)} l 10 -6 l 8 8 l -10 6 Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="1.2"></path>')
    return "".join(o)

def lamps(w, h, seed):
    """I will search Jerusalem with lamps: a dark street between houses, lamps carried along it throwing pools of light."""
    from genesis.art4 import clay_lamp
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0B0B1A"></rect>']
    for side in (0, 1):
        for i in range(4):
            x = w * (i * 0.12) if side == 0 else w * (0.62 + i * 0.12)
            o.append(f'<rect x="{f(x)}" y="{f(h * (0.14 + (i % 2) * 0.08))}" width="{f(w * 0.12)}" height="{f(h)}" fill="#2A2438" stroke="#0D0D0F" stroke-width="2"></rect>'
                     f'<rect x="{f(x + w * 0.04)}" y="{f(h * 0.62)}" width="{f(w * 0.04)}" height="{f(h * 0.38)}" fill="#120E1A"></rect>')
    o.append(f'<path d="M{f(w * 0.48)} {f(h * 0.5)} L {f(w * 0.52)} {f(h * 0.5)} L {f(w * 0.62)} {f(h + 10)} L {f(w * 0.38)} {f(h + 10)} Z" fill="#3A3448"></path>')
    for i, (x, y) in enumerate(((0.44, 0.66), (0.54, 0.8), (0.5, 0.56))):
        o.append(halo(w * x, h * y, h * 0.16, "#FFC14D", 0.5) + clay_lamp(w * x, h * y, min(0.7, h / 400)))
    return "".join(o)

def day_dark(w, h, seed):
    """A day of darkness and gloominess, of clouds and thick darkness, of the trumpet and alarm against the fortified cities
    and the high battlements: black clouds rolling over the battlements, a ram's horn raised against the sky."""
    o = [sky(w, h, "#05050A", "#2A2030"), clouds(w, h * 0.16, seed, n=9, color="#1A1420", op=0.95, h=h), clouds(w, h * 0.32, seed + 1, n=7, color="#2A2030", op=0.9, h=h),
         walls(-10, w + 10, h * 0.9, h * 0.5, seed, color="#4A4048", towers=4, gate=False), bolt(w * 0.62, 0, h * 0.4, seed, color="#C8C0E0")]
    k = min(1.2, h / 260)
    o.append(f'<g transform="translate({f(w * 0.16)} {f(h * 0.5)}) scale({f(k)}) rotate(-30)"><path d="M0 0 C 30 -10 70 -10 100 -40 C 104 -30 102 -20 96 -16 C 70 6 30 14 0 12 Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.4"></path></g>'
             + mk.speed(w * 0.24, h * 0.36, 10, 20 * k, 80 * k, seed, color="#F3EFE6", op=0.6))
    return "".join(o)

def fire_land(w, h, seed):
    """Neither their silver nor their gold shall be able to deliver them; the whole land shall be devoured by the fire of
    his jealousy: the land burning to the horizon, silver and gold lying useless in the foreground."""
    o = [sky(w, h, "#1A0505", "#8A2A10"), ground(w, h, h * 0.5, "#2A1008", dy=0), fires(-10, w + 10, h * 0.6, h * 0.2, seed, n=8), fires(-10, w + 10, h * 0.76, h * 0.3, seed + 3, n=6)]
    r = random.Random(seed)
    for i in range(8):
        x, y = r.uniform(w * 0.05, w * 0.95), r.uniform(h * 0.86, h * 0.98)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="9" ry="4" fill="{r.choice(["#E8B830", "#C8C8D0"])}" stroke="#0D0D0F" stroke-width="1.2"></ellipse>')
    return "".join(o)

def chaff(p, w, h, seed):
    """Before the day pass as the chaff: seek ye Jehovah, all ye meek of the earth — chaff driven by the wind across a
    threshing-floor, the meek kneeling in the field."""
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A8A", "#E8D8B8"), hills(w, h, h * 0.5, seed, color="#8A8A6A", amp=12), ground(w, h, h * 0.56, "#B8A070", dy=0),
         wind_lines(w, h, seed, n=12, color="#F3E8C8", op=0.6, y0=0.1, y1=0.6)]
    r = random.Random(seed)
    for i in range(50):
        x, y = r.uniform(0, w), r.uniform(h * 0.1, h * 0.7)
        o.append(f'<path d="M{f(x)} {f(y)} l 6 -2" stroke="#E8C870" stroke-width="2"></path>')
    for i in range(4):
        o.append(E.kneel(w * (0.2 + i * 0.18), h * 0.95, fit(h * 0.95, h * 0.62) * 0.8, color=["#5A4A6A", "#4A5A3A", "#6A4A3A", "#3A4A6A"][i], flip=i % 2 == 1))
    return "".join(o)

COAST = [("GAZA", 0.3, 0.84), ("ASHKELON", 0.36, 0.64), ("ASHDOD", 0.42, 0.44), ("EKRON", 0.58, 0.32)]

def coast_map(w, h):
    """Gaza forsaken, Ashkelon a desolation, Ashdod driven out at noonday, Ekron rooted up: the coast of the Philistines as
    a technical map."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.36)} -10 C {f(w * 0.3)} {f(h * 0.3)} {f(w * 0.26)} {f(h * 0.6)} {f(w * 0.2)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             + label(w * 0.12, h * 0.4, "THE SEA", "#8FD0E2", 10))
    for name, x, y in COAST:
        o.append(node(w * x, h * y, "", color="#FF8A6A", r=5) + label(w * x + 12, h * y + 4, name, "#FF8A6A", 10, anchor="start")
                 + f'<path d="M{f(w * x - 8)} {f(h * y - 8)} L {f(w * x + 8)} {f(h * y + 8)} M{f(w * x + 8)} {f(h * y - 8)} L {f(w * x - 8)} {f(h * y + 8)}" stroke="#D7261E" stroke-width="2"></path>')
    o.append(node(w * 0.84, h * 0.4, "JUDAH", color="#FFD23F", r=6))
    o.append(label(w * 0.96, h * 0.08, "THE LAND OF THE PHILISTINES", "#FF8A6A", 9, anchor="end"))
    return "".join(o)

def coast_pasture(p, w, h, seed):
    """The sea-coast shall be pastures, with cottages for shepherds and folds for flocks: the shore green with flocks, a
    shepherd's hut and a stone fold, the ruin of Ashkelon behind, evening."""
    o = [vista(w, h, seed, tone="dusk", horizon=0.52, hills_n=0, sea_=False, sheep=7, ground_=True)]
    o.append(sea(w, h * 0.6, h * 0.42, seed) if False else "")
    o.append(f'<rect x="-10" y="{f(h * 0.42)}" width="{f(w * 0.4)}" height="{f(h * 0.14)}" fill="#1F6F9A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(ruin(w * 0.44, w * 0.74, h * 0.56, h * 0.12, seed))
    x = w * 0.84
    o.append(f'<path d="M{f(x - 40)} {f(h * 0.74)} L {f(x - 40)} {f(h * 0.6)} L {f(x)} {f(h * 0.5)} L {f(x + 40)} {f(h * 0.6)} L {f(x + 40)} {f(h * 0.74)} Z" fill="#A8906A" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<rect x="{f(x - 8)}" y="{f(h * 0.64)}" width="16" height="{f(h * 0.1)}" fill="#2A1A10"></rect>')
    return "".join(o)

def saltpits(w, h, seed):
    """Moab shall be as Sodom, and the children of Ammon as Gomorrah, a possession of nettles, and saltpits, and a perpetual
    desolation: white salt flats by the dead sea, nettles, the bare hills of Moab beyond."""
    r = random.Random(seed)
    o = [sky(w, h, "#C8A880", "#F3E8D8"), hills(w, h, h * 0.4, seed, color="#9A6A5A", amp=24, step=100),
         f'<rect x="-10" y="{f(h * 0.44)}" width="{f(w + 20)}" height="{f(h * 0.12)}" fill="#5AA8B8" stroke="#0D0D0F" stroke-width="1.6"></rect>',
         ground(w, h, h * 0.56, "#E8E2D6", dy=0)]
    for i in range(20):
        x, y = r.uniform(0, w), r.uniform(h * 0.6, h)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(r.uniform(10, 30))}" ry="{f(r.uniform(3, 7))}" fill="#F8F4EC" stroke="#B8B0A0" stroke-width="1"></ellipse>')
    for i in range(14):
        x, y = r.uniform(0, w), h * r.uniform(0.7, 1.0)
        o.append(f'<path d="M{f(x)} {f(y)} l -6 -18 M{f(x)} {f(y)} l 2 -22 M{f(x)} {f(y)} l 8 -16" stroke="#4A6A2A" stroke-width="2"></path>')
    return "".join(o)

def isles(w, h, seed):
    """He will famish all the gods of the earth; and men shall worship him, every one from his place, even all the isles of
    the nations: islands in a wide sea, each with a small figure bowed toward a light on the horizon."""
    o = [sky(w, h, "#2A3A6A", "#FFD8A0"), halo(w * 0.5, h * 0.42, h * 0.4, "#FFF4C2", 0.6), sea(w, h, h * 0.44, seed, color="#2C7DA8", deep="#1F4A6A")]
    r = random.Random(seed)
    for i in range(5):
        x, y = w * (0.1 + i * 0.2), h * (0.62 + (i % 2) * 0.16)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.07)}" ry="{f(h * 0.04)}" fill="#C8A06A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
                 + E.kneel(x, y - h * 0.01, fit(y, y - h * 0.1) * 0.9, color="#3A2A2A", flip=x > w * 0.5))
    return "".join(o)

def nineveh_ruin(w, h, seed):
    """Nineveh a desolation: the pelican and the porcupine shall lodge in the capitals thereof; their voice shall sing in the
    windows; he hath laid bare the cedar-work — broken columns and a window in a ruined wall, a pelican on a capital, herds
    lying down among the stones."""
    from samuel1 import cow
    o = [sky(w, h, "#8A7A8A", "#E8D0B0"), ground(w, h, h * 0.76, "#A8906A", dy=0), ruin(w * 0.5, w + 10, h * 0.78, h * 0.4, seed, color="#B8A07A")]
    k = min(1.0, h / 300)
    for i, x in enumerate((0.14, 0.32)):
        top = h * (0.3 + i * 0.1)
        o.append(f'<rect x="{f(w * x - 14 * k)}" y="{f(top)}" width="{f(28 * k)}" height="{f(h * 0.76 - top)}" fill="#C8B090" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(w * x - 26 * k)}" y="{f(top - 14 * k)}" width="{f(52 * k)}" height="{f(14 * k)}" fill="#C8B090" stroke="#0D0D0F" stroke-width="2"></rect>')
    px, py = w * 0.14, h * 0.3 - 14 * k
    o.append(f'<g transform="translate({f(px)} {f(py)}) scale({f(k)})"><ellipse cx="0" cy="-16" rx="20" ry="14" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.8"></ellipse>'
             '<path d="M10 -26 C 14 -44 22 -46 26 -40 L 50 -30 L 26 -26 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M28 -32 L 50 -30 L 30 -24" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></path>'
             '<path d="M-4 0 L -6 14 M4 0 L 6 14" stroke="#E8A040" stroke-width="2.4"></path></g>')
    hx, hy = w * 0.36, h * 0.96
    o.append(f'<g transform="translate({f(hx)} {f(hy)}) scale({f(k)})"><ellipse cx="0" cy="-12" rx="24" ry="14" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
             + "".join(f'<path d="M{-20 + j * 5} -20 l {-6 + j} -18" stroke="#2A1A10" stroke-width="1.6"></path>' for j in range(9)) + '</g>')
    o.append(cow(w * 0.62, h * 0.98, k * 0.5) + cow(w * 0.82, h * 0.96, k * 0.45, flip=True))
    return "".join(o)

def wolves_city(w, h, seed):
    """Woe to the oppressing city: her princes roaring lions, her judges evening wolves — the city wall at evening, wolves
    prowling at its gate, a lion's shape on the rampart."""
    import judges2 as JG2
    o = [sky(w, h, "#1A1030", "#B8603A"), walls(-10, w + 10, h * 0.7, h * 0.46, seed, color="#7A6A6A", towers=3), ground(w, h, h * 0.7, "#3A2A2A", dy=0)]
    k = min(0.8, h / 320)
    for i, x in enumerate((0.4, 0.62, 0.8)):
        y = h * (0.92 + (i % 2) * 0.04)
        o.append(f'<g transform="translate({f(w * x)} {f(y)}) scale({f(k * (1 if i % 2 else -1))} {f(k)})"><path d="M-50 -20 C -40 -36 20 -40 36 -30 L 52 -44 L 58 -40 L 56 -30 L 66 -26 L 54 -20 L 40 -20 L 36 0 L 30 0 L 26 -14 L -26 -14 L -32 0 L -38 0 L -40 -18 C -50 -14 -60 -10 -66 -4 L -62 -14 Z" fill="#1A1418" stroke="#0D0D0F" stroke-width="1.6"></path></g>')
    o.append(JG2.lion(w * 0.2, h * 0.3, k * 0.7, roar=True))
    return "".join(o)

def empty_streets(w, h, seed):
    """I have cut off nations; their battlements are desolate; I have made their streets waste, so that none passeth by: a
    long empty street between broken houses, no one in it."""
    o = [sky(w, h, "#6A6A7A", "#D8C8B0")]
    for side in (-1, 1):
        for i in range(5):
            t = i / 5
            x = w * 0.5 + side * w * (0.5 - t * 0.38); hh = h * (0.7 - t * 0.4)
            o.append(f'<path d="M{f(x)} {f(h * 0.86 - t * h * 0.3)} L {f(x)} {f(h * 0.86 - t * h * 0.3 - hh)} L {f(x - side * w * 0.07)} {f(h * 0.86 - t * h * 0.3 - hh * 0.8)} L {f(x - side * w * 0.07)} {f(h * 0.86 - t * h * 0.3)} Z" fill="{["#A8906A", "#B8A07A", "#C8B08A", "#B89A6A", "#A88A5A"][i]}" stroke="#0D0D0F" stroke-width="1.8"></path>')
    o.append(f'<path d="M{f(w * 0.12)} {f(h + 10)} L {f(w * 0.46)} {f(h * 0.56)} L {f(w * 0.54)} {f(h * 0.56)} L {f(w * 0.88)} {f(h + 10)} Z" fill="#C8B898" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return "".join(o)

def suppliants(p, w, h, seed):
    """From beyond the rivers of Ethiopia my suppliants, even the daughter of my dispersed, shall bring mine offering: a
    procession coming up from the rivers of the south with gifts, under a pure light."""
    o = [mk.defs(p, *ALL), sky(w, h, "#3A4A8A", "#FFE6A0"), halo(w * 0.85, h * 0.2, h * 0.4, "#FFF4C2", 0.6), hills(w, h, h * 0.5, seed, color="#8A9A6A", amp=12),
         ground(w, h, h * 0.56, "#C8B080", dy=0), river(w, h * 0.62, h * 0.06, seed=seed)]
    b = h * 0.96
    for i in range(6):
        x = w * (0.08 + i * 0.13)
        o.append(figure(p, x, b - i * h * 0.02, h * 0.56 - i * h * 0.02, ["#E8B830", "#2E6B3A", "#B5421E", "#5A2A6A", "#1F5FAD", "#E8E2D6"][i], "woman" if i % 2 else "man",
                        up=[(22, -158), (30, -176), (26, -196)] if i % 2 == 0 else None))
        if i % 2 == 0: o.append(f'<rect x="{f(x + 4)}" y="{f(b - i * h * 0.02 - h * 0.44)}" width="14" height="10" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    return "".join(o)

def zion_sings(p, w, h, seed):
    """Sing, O daughter of Zion; shout, O Israel: the people on mount Zion in the morning light, arms raised, the city bright
    behind them."""
    o = [vista(w, h, seed, tone="dawn", far="zion", cx=0.6, cw=0.7, sun_at=(0.2, 0.3), hills_n=1, horizon=0.6), mk.defs(p, *ALL)]
    o.append(crowd(p, w * 0.04, w * 0.96, h * 0.96, h * 0.6, 8, seed, colors=("#E8B830", "#2E6B3A", "#B5421E", "#5A2A6A", "#1F5FAD", "#E8E2D6"), up=[(22, -158), (40, -176), (58, -196)]))
    return "".join(o)

def flock_rest(w, h, seed):
    """They shall feed and lie down, and none shall make them afraid: a flock lying in a green pasture below mount Zion,
    evening."""
    o = [vista(w, h, seed, tone="dusk", far="zion", cx=0.7, cw=0.5, hills_n=1, horizon=0.56)]
    r = random.Random(seed)
    k = min(0.5, h / 560)
    for i in range(9):
        o.append(E.sheep(w * r.uniform(0.05, 0.95), h * r.uniform(0.8, 0.96), k, flip=r.random() < 0.5))
    return "".join(o)
