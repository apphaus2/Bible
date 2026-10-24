"""Drawings for Luke 5–6: the lake of Gennesaret — the two boats drawn up, the fishermen washing their nets; Simon's boat put
out into the deep; the draught of fishes, the nets breaking and both boats filled so that they began to sink; Simon fallen
at Jesus' knees among the fish; the boats brought to land and all left. The twelve named in Luke's order; the level place
at the foot of the mountain with the great multitude; the good measure running over into the bosom; the mote and the beam.
Built on luk.art2."""
from luk.art2 import *
from luk.art2 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch, \
    jesus_kneel, light_seated, WOMEN3, PURPLE, GOLD, kneel_w, boy_fig, zach_fig, elis_fig, shepherd_fig, swaddled
import random, math

def fish_heap(x, y, wd, n, seed, color="#B8C8D0"):
    """Silver fish heaped or caught in a net: small leaf shapes with tails."""
    r = random.Random(seed); o = []
    for _ in range(n):
        cx, cy = x + r.uniform(-wd / 2, wd / 2), y + r.uniform(-wd * 0.08, wd * 0.08); a = r.uniform(-40, 40); k = r.uniform(0.7, 1.2)
        o.append(f'<g transform="translate({f(cx)} {f(cy)}) rotate({f(a)}) scale({f(k)})"><path d="M-12 0 C -6 -6 6 -6 10 0 C 6 6 -6 6 -12 0 Z M10 0 L 16 -5 L 16 5 Z" '
                 f'fill="{r.choice([color, "#D8E0E4", "#9AAAB4"])}" stroke="#0D0D0F" stroke-width="1.2"></path></g>')
    return "".join(o)

def washing_nets(p, w, h, seed):
    """He was standing by the lake of Gennesaret, the multitude pressing upon him; and he saw two boats standing by the lake,
    the fishermen gone out of them washing their nets: the beach, the two boats drawn up, the nets spread on the stones."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.3, seed, color="#7A8A6A", amp=14, step=90), lake(w, h, h * 0.38, seed),
         shore(w, h, h * 0.64, x0=-10, x1=w + 10)]
    s = fit(b, max(h * 0.3, b - 220))
    o.append(boat(p, w * 0.22, h * 0.6, s * 0.8, mast=True) + boat(p, w * 0.5, h * 0.58, s * 0.72, mast=True, flip=True))
    o.append(f'<path d="M{f(w * 0.3)} {f(b - 6)} C {f(w * 0.4)} {f(b - 30)} {f(w * 0.5)} {f(b - 30)} {f(w * 0.6)} {f(b - 4)}" stroke="#E8D8B0" stroke-width="1.6" stroke-dasharray="3 3" fill="none"></path>')
    o.append(seated(w * 0.36, b, s * 0.8, ROBES["peter"], beard="#4A4440") + seated(w * 0.5, b, s * 0.78, ROBES["andrew"], head="#6A7A5A", beard="#3A2A1A", flip=True))
    o.append(jesus(p, w * 0.7, b, s, flip=True))
    o.append(crowd(p, w * 0.76, w * 1.0, b, b - 170 * s, 4, seed, flip=True))
    return "".join(o)

def the_deep(p, w, h, seed, stage="cast"):
    """Put out into the deep, and let down your nets for a draught: stage='cast' Simon's boat on the open water, Jesus seated
    in the stern, Simon and Andrew letting the net down over the side; 'full' the net so full of fish it breaks, the partners'
    boat come alongside, both boats loaded so low they begin to sink; 'knees' Simon fallen down at Jesus' knees among the
    heaped fish, James and John standing amazed."""
    b = h * 0.96
    o = [mk.defs(p, *ALL), sky(w, h, "#5A8AC8", "#FFE6B0"), hills(w, h, h * 0.26, seed, color="#7A8A9A", amp=10, step=90), lake(w, h, h * 0.32, seed, n=20)]
    s = fit(b, max(h * 0.3, b - 220))
    k = s * 1.2
    if stage == "cast":
        o.append(boat(p, w * 0.46, h * 0.74, k, crew=[(-60, "jesus"), (20, ("up", ROBES["peter"])), (56, ROBES["andrew"])], mast=True))
        o.append(f'<path d="M{f(w * 0.46 + 90 * k)} {f(h * 0.72)} C {f(w * 0.46 + 140 * k)} {f(h * 0.8)} {f(w * 0.46 + 130 * k)} {f(h * 0.94)} {f(w * 0.46 + 100 * k)} {f(h * 1.0)}" '
                 f'stroke="#E8D8B0" stroke-width="2" stroke-dasharray="4 3" fill="none"></path>')
    elif stage == "full":
        k = s * 1.45
        o.append(boat(p, w * 0.3, h * 0.78, k * 0.9, crew=[(-50, "jesus"), (10, ("up", ROBES["peter"])), (50, ("up", ROBES["andrew"]))], mast=False, tilt=-3))
        o.append(boat(p, w * 0.74, h * 0.78, k * 0.86, crew=[(-40, ("up", ROBES["james"])), (30, ("up", ROBES["john"])), (64, ("old", "#5A5A6A"))], mast=False, flip=True, tilt=4))
        o.append(fish_heap(w * 0.3, h * 0.78 - 34 * k, 140 * k, 30, seed) + fish_heap(w * 0.74, h * 0.78 - 34 * k, 130 * k, 26, seed + 1))
        nx, ny = w * 0.52, h * 0.86
        o.append(f'<path d="M{f(nx - 70 * k)} {f(ny - 30 * k)} C {f(nx - 40 * k)} {f(ny + 30 * k)} {f(nx + 40 * k)} {f(ny + 30 * k)} {f(nx + 70 * k)} {f(ny - 30 * k)}" fill="#E8D8B0" fill-opacity="0.15" '
                 f'stroke="#E8D8B0" stroke-width="2" stroke-dasharray="3 3"></path>' + fish_heap(nx, ny, 110 * k, 24, seed + 2))
        o.append(f'<path d="M{f(nx + 10 * k)} {f(ny + 8 * k)} l {f(14 * k)} {f(12 * k)} M{f(nx + 26 * k)} {f(ny + 4 * k)} l {f(8 * k)} {f(14 * k)}" stroke="#F3EFE6" stroke-width="3"></path>')
    else:
        hull = boat(p, w * 0.5, h * 0.86, k * 1.3, mast=False)
        o.append(hull + fish_heap(w * 0.5, h * 0.86 - 44 * k * 1.3, 200 * k, 40, seed))
        o.append(jesus_seated(w * 0.3, h * 0.86 - 40 * k * 1.3, k * 0.72))
        o.append(E.kneel(w * 0.46, h * 0.86 - 40 * k * 1.3, k * 0.66, color=ROBES["peter"], flip=True, skin="#B98A6E"))
        o.append(mk.person(p, round(w * 0.66), round(h * 0.86 - 40 * k * 1.3), round(k * 0.6, 3), body="#B98A6E", cloth=ROBES["james"], kind="Tunic", sw=3, flip=True, up=UP_HIGH)
                 + mk.person(p, round(w * 0.74), round(h * 0.86 - 40 * k * 1.3), round(k * 0.6, 3), body="#B98A6E", cloth=ROBES["john"], kind="Tunic", sw=3, flip=True))
    return "".join(o)

def left_all(p, w, h, seed):
    """When they had brought their boats to land, they left all, and followed him: the boats drawn up on the beach full of
    fish and the nets lying, Jesus going up the shore, Simon, Andrew, James and John following him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFE6B0"), hills(w, h, h * 0.3, seed, color="#7A8A6A", amp=14, step=90), lake(w, h, h * 0.38, seed),
         shore(w, h, h * 0.62, x0=-10, x1=w + 10)]
    s = fit(b, max(h * 0.3, b - 220))
    o.append(boat(p, w * 0.18, h * 0.62, s * 0.7, mast=False) + fish_heap(w * 0.18, h * 0.62 - 26 * s * 0.7, 120 * s * 0.7, 18, seed))
    o.append(boat(p, w * 0.42, h * 0.6, s * 0.62, mast=False, flip=True) + fish_heap(w * 0.42, h * 0.6 - 26 * s * 0.62, 100 * s * 0.62, 14, seed + 1))
    o.append(jesus(p, w * 0.86, b, s, flip=True))
    for i, who in enumerate(("peter", "andrew", "james", "john")):
        o.append(disciple(p, w * (0.5 + 0.08 * i), b - 2 * i, s * (0.94 - 0.02 * i), who, flip=True))
    return "".join(o)

LUKE_TWELVE = [("SIMON PETER", ROBES["peter"]), ("ANDREW", ROBES["andrew"]), ("JAMES", ROBES["james"]), ("JOHN", ROBES["john"]), ("PHILIP", "#4A6A4A"),
               ("BARTHOLOMEW", "#7A5A2A"), ("MATTHEW", ROBES["matthew"]), ("THOMAS", ROBES["thomas"]), ("JAMES OF ALPHÆUS", "#5A5A7A"), ("SIMON THE ZEALOT", "#3A5A5A"),
               ("JUDAS OF JAMES", "#6A3A3A"), ("JUDAS ISCARIOT", ROBES["judas"])]
def twelve_luke(p, w, h, seed):
    """He chose from them twelve, whom also he named apostles: the twelve in a row on the blueprint grid, each in his colour,
    his name beneath, in Luke's order — Simon Peter and Andrew his brother, James and John … Judas Iscariot."""
    b = h * 0.7
    o = [mk.defs(p, *ALL), grid_bg(w, h)]
    s = min(fit(b, max(h * 0.12, b - 230)) * 0.9, w * 0.84 / 12 / 80)
    for i, (nm, c) in enumerate(LUKE_TWELVE):
        x = w * (0.06 + 0.88 * i / 11)
        o.append(mk.person(p, round(x), round(b), round(s, 3), body="#B98A6E", cloth=c, kind="Robe", sw=3))
        o.append(f'<path d="M{f(x)} {f(b + 4)} L {f(x)} {f(b + 10 + (i % 2) * 16)}" stroke="#4A7A9A" stroke-width="1.4"></path>')
        o.append(label(x, b + 20 + (i % 2) * 16, nm, "#FFD23F" if i < 4 else "#8FD0E2", 8))
    return "".join(o)

def level_place(p, w, h, seed, touching=False):
    """He came down with them, and stood on a level place: the plain at the foot of the mountain, Jesus standing in the midst,
    the disciples about him and a great multitude from every side; touching=True: the people reaching to touch him, the sick
    raised up on their beds; his eyes lifted on his disciples."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, *LIE), sky(w, h, "#8FD0E2", "#F3E8C8"),
         f'<path d="M{f(w * 0.0)} {f(h * 0.5)} L {f(w * 0.2)} {f(h * 0.12)} L {f(w * 0.34)} {f(h * 0.3)} L {f(w * 0.5)} {f(h * 0.5)} Z" fill="#7A8A9A" stroke="{INK}" stroke-width="2"></path>',
         hills(w, h, h * 0.46, seed, color="#8A9A6A", amp=10, step=80), ground(w, h, h * 0.56, "#B8B070", dy=0)]
    s = fit(b, max(h * 0.32, b - 210))
    o.append(crowd(p, w * 0.02, w * 0.98, h * 0.7, h * 0.7 - 120 * s, 14, seed, flip=None))
    o.append(glow(w * 0.5, b - 120 * s, 130 * s, "#FFF4C2", 0.6, f"{p}g"))
    o.append(jesus(p, w * 0.5, b, s, up=UP_BLESS if touching else None))
    for i, (x, who) in enumerate(((0.3, "peter"), (0.38, "john"), (0.64, "andrew"), (0.72, "james"))):
        o.append(disciple(p, w * x, b - 2, s * 0.92, who, flip=x > 0.5, up=[(-22, -158), (-44, -150), (-62, -152)] if touching and i % 2 else None))
    if touching:
        o.append(on_bed(p, w * 0.14, b - 14, w * 0.16) + on_bed(p, w * 0.86, b - 14, w * 0.16, flip=True))
    return "".join(o)

def measure(p, w, h, seed):
    """Good measure, pressed down, shaken together, running over, shall they give into your bosom: a wooden measure heaped
    with grain and overflowing, the grain pouring into the gathered fold of a robe held out below."""
    b = h * 0.92
    r = random.Random(seed)
    o = [bgr(w, h, "#C8A060"), glow(w * 0.5, h * 0.4, h * 0.7, "#FFE680", 0.5, f"{p}g"),
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A6A3A" stroke="{INK}" stroke-width="2"></rect>']
    k = max(0.5, h / 360)
    cx, cy = w * 0.44, h * 0.42
    o.append(f'<path d="M{f(cx - 60 * k)} {f(cy)} L {f(cx + 60 * k)} {f(cy)} L {f(cx + 50 * k)} {f(cy + 80 * k)} L {f(cx - 50 * k)} {f(cy + 80 * k)} Z" fill="#8A5A2A" stroke="{INK}" stroke-width="2.6"></path>'
             f'<path d="M{f(cx - 56 * k)} {f(cy + 26 * k)} L {f(cx + 56 * k)} {f(cy + 26 * k)} M{f(cx - 53 * k)} {f(cy + 54 * k)} L {f(cx + 53 * k)} {f(cy + 54 * k)}" stroke="#5A3A1A" stroke-width="3"></path>'
             f'<path d="M{f(cx - 64 * k)} {f(cy + 2)} C {f(cx - 50 * k)} {f(cy - 40 * k)} {f(cx + 50 * k)} {f(cy - 40 * k)} {f(cx + 64 * k)} {f(cy + 2)} Z" fill="#E8C060" stroke="{INK}" stroke-width="2"></path>')
    for _ in range(60):                                       # grain running over
        t = r.uniform(0, 1); x = cx + 60 * k + t * 70 * k + r.uniform(-6, 6) * k; y = cy + t * (b - cy - 40 * k) + r.uniform(-4, 4)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(2.2 * k)}" ry="{f(3.4 * k)}" fill="#E8C060" stroke="#8A6A2A" stroke-width="0.8"></ellipse>')
    fx = cx + 130 * k
    o.append(f'<path d="M{f(fx - 70 * k)} {f(b - 50 * k)} C {f(fx - 50 * k)} {f(b + 6)} {f(fx + 50 * k)} {f(b + 6)} {f(fx + 70 * k)} {f(b - 50 * k)} C {f(fx + 30 * k)} {f(b - 30 * k)} {f(fx - 30 * k)} {f(b - 30 * k)} {f(fx - 70 * k)} {f(b - 50 * k)} Z" '
             f'fill="#3A5A7A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(fx - 46 * k)} {f(b - 34 * k)} C {f(fx - 20 * k)} {f(b - 50 * k)} {f(fx + 20 * k)} {f(b - 50 * k)} {f(fx + 46 * k)} {f(b - 34 * k)}" fill="#E8C060" stroke="#8A6A2A" stroke-width="1.4"></path>')
    for side in (-1, 1):
        o.append(f'<path d="M{f(fx + side * 70 * k)} {f(b - 50 * k)} l {f(side * 18 * k)} {f(-14 * k)}" stroke="{SKIN}" stroke-width="{f(10 * k)}" stroke-linecap="round"></path>')
    return "".join(o)

def mote_beam(p, w, h, seed):
    """The mote that is in thy brother's eye, and the beam that is in thine own eye: on a carpenter's bench, a great squared
    beam of timber laid across the trestles, and beside it on the bench a single tiny splinter — the one beside the other."""
    b = h * 0.92
    o = [bgr(w, h, "#B8987A"), f'<rect x="-10" y="{f(h * 0.06)}" width="{f(w + 20)}" height="{f(h * 0.04)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>']
    ty = h * 0.62
    for x in (0.16, 0.84):
        o.append(f'<path d="M{f(w * x - 30)} {f(b)} L {f(w * x)} {f(ty)} L {f(w * x + 30)} {f(b)}" stroke="#5A3A1E" stroke-width="10" fill="none"></path>')
    bh = max(30, h * 0.16)
    o.append(f'<rect x="{f(w * 0.04)}" y="{f(ty - bh)}" width="{f(w * 0.92)}" height="{f(bh)}" fill="#C8904A" stroke="{INK}" stroke-width="2.6"></rect>'
             f'<path d="M{f(w * 0.04)} {f(ty - bh)} L {f(w * 0.08)} {f(ty - bh - 12)} L {f(w * 1.0)} {f(ty - bh - 12)} L {f(w * 0.96)} {f(ty - bh)} Z" fill="#E0A860" stroke="{INK}" stroke-width="2"></path>')
    r = random.Random(seed)
    for _ in range(8):
        y = ty - bh + r.uniform(4, bh - 4)
        o.append(f'<path d="M{f(w * r.uniform(0.06, 0.4))} {f(y)} C {f(w * 0.5)} {f(y + r.uniform(-4, 4))} {f(w * 0.7)} {f(y + r.uniform(-4, 4))} {f(w * r.uniform(0.7, 0.94))} {f(y)}" stroke="#8A5A2A" stroke-width="1.4" fill="none"></path>')
    o.append(f'<path d="M{f(w * 0.5)} {f(b - 8)} L {f(w * 0.53)} {f(b - 10)}" stroke="#C8904A" stroke-width="2.4" stroke-linecap="round"></path>'
             f'<circle cx="{f(w * 0.515)}" cy="{f(b - 9)}" r="12" fill="none" stroke="#FFF4C2" stroke-width="1.6" stroke-dasharray="3 3"></circle>')
    return "".join(o)
