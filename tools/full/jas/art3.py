"""Drawings for James 3–5: the tongue (the bit, the rudder, the little fire, the beasts tamed, the fountain and the trees),
the wisdom from above, wars, draw nigh to God, the vapor, ye rich, the husbandman, the elders, the erring brother (see
jas/art.py)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from jas.art2 import *
from jas.art import art, plate_label, light_fig, _street, _road
from act.art15 import grain_ship
from dan.art import lion_walk
from genesis.art2 import dove
import snake as SN
from mrk.art import on_bed
from mrk.art9 import LIE
import numbers1 as N1

# ---- James 3 ----------------------------------------------------------------------------------------------------------------
def horse_head(x, y, s=1.0):
    """A horse's head and neck in profile facing right, bridled, the bit in its mouth and the reins drawn back; (x, y) the
    foot of the neck."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
            '<path d="M-40 0 C -46 -60 -30 -110 0 -140 C 10 -150 22 -156 34 -152 L 40 -166 L 48 -150 C 70 -138 96 -110 112 -84 C 118 -74 116 -64 106 -62 '
            'C 92 -60 80 -66 66 -74 C 52 -60 40 -40 36 0 Z" fill="#7A4A2A" stroke="#0D0D0F" stroke-width="3"></path>'
            '<path d="M0 -140 C -20 -120 -36 -80 -38 -30 C -28 -70 -14 -110 6 -136 Z" fill="#2A1A10" stroke="#0D0D0F" stroke-width="2"></path>'
            '<circle cx="50" cy="-120" r="4" fill="#0D0D0F"></circle><path d="M102 -70 C 106 -74 110 -72 110 -68" fill="none" stroke="#0D0D0F" stroke-width="2"></path>'
            # the bridle: the headstall, the noseband, the bit ring at the corner of the mouth
            '<path d="M40 -150 C 46 -120 60 -96 76 -80" fill="none" stroke="#3A2A1A" stroke-width="5"></path>'
            '<path d="M60 -112 C 76 -104 96 -96 108 -90" fill="none" stroke="#3A2A1A" stroke-width="5"></path>'
            '<circle cx="80" cy="-74" r="8" fill="none" stroke="#C8C8D0" stroke-width="4"></circle>'
            '<path d="M80 -74 C 40 -60 0 -50 -60 -40" fill="none" stroke="#3A2A1A" stroke-width="4"></path></g>')

def bit_rudder(w, h):
    """We put the horses' bridles into their mouths, … the ships, though so great, are turned about by a very small rudder:
    a technical plate — at the left a horse's head, bridled, the bit and the reins; at the right a great ship under sail
    and, enlarged, the small steering oar at her stern and the steersman's hand on its tiller."""
    o = [plate_bg(w, h, "JAMES 3:3–4 · THE BIT · THE RUDDER")]
    k = min(w / 702, h / 300)
    o.append(horse_head(w * 0.13, h * 0.94, k * 1.15))
    o.append(tag(w * 0.13 + 80 * k * 1.15, h * 0.94 - 74 * k * 1.15, "THE BRIDLE · THE BIT", w * 0.3, h * 0.22, color=GOLD, size=9))
    o.append(tag(w * 0.08, h * 0.94 - 44 * k, "THE WHOLE BODY", w * 0.04, h * 0.36, color=CY, size=9))
    o.append(f'<path d="M{f(w * 0.46)} {f(h * 0.12)} L {f(w * 0.46)} {f(h * 0.96)}" stroke="{CY}" stroke-width="1" stroke-dasharray="4 4" opacity="0.6"></path>')
    sea_y = h * 0.8
    o.append(f'<path d="M{f(w * 0.48)} {f(sea_y)} C {f(w * 0.6)} {f(sea_y - 6)} {f(w * 0.8)} {f(sea_y + 6)} {f(w + 10)} {f(sea_y - 2)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.48)} {f(h + 10)} Z" fill="#14304A" stroke="{CY}" stroke-width="1.4"></path>')
    sk = k * 0.62
    sx = w * 0.72
    o.append(f'<defs><clipPath id="brc"><rect x="{f(w * 0.47)}" y="0" width="{f(w * 0.53)}" height="{f(h)}"></rect></clipPath></defs><g clip-path="url(#brc)">'
             + grain_ship("br", sx, sea_y, sk, sail="full") + '</g>')
    rx, ry = sx - 190 * sk, sea_y - 10 * sk                          # the steering oar at the stern, ringed
    o.append(f'<circle cx="{f(rx)}" cy="{f(ry)}" r="{f(26 * k)}" fill="none" stroke="#FF6A4A" stroke-width="2"></circle>')
    o.append(tag(rx - 18 * k, ry + 18 * k, "A VERY SMALL RUDDER", w * 0.5, h * 0.94, color="#FF6A4A", size=9))
    o.append(dim(sx - 210 * sk, sea_y - 330 * sk, sx + 210 * sk, sea_y - 330 * sk, "SO GREAT", size=9, color=CY))
    return "".join(o)

def tree_shape(x, y, s, kind=0, color="#2E5A2A"):
    """A forest tree: a pine (kind 0) or a broad oak (kind 1), (x, y) its foot."""
    if kind == 0:
        return (f'<path d="M{f(x - 3 * s)} {f(y)} L {f(x - 3 * s)} {f(y - 20 * s)} L {f(x - 24 * s)} {f(y - 20 * s)} L {f(x - 4 * s)} {f(y - 56 * s)} L {f(x - 18 * s)} {f(y - 56 * s)} '
                f'L {f(x)} {f(y - 96 * s)} L {f(x + 18 * s)} {f(y - 56 * s)} L {f(x + 4 * s)} {f(y - 56 * s)} L {f(x + 24 * s)} {f(y - 20 * s)} L {f(x + 3 * s)} {f(y - 20 * s)} L {f(x + 3 * s)} {f(y)} Z" '
                f'fill="{color}" stroke="#0D0D0F" stroke-width="{f(max(1.2, 1.8 * s))}"></path>')
    return (f'<rect x="{f(x - 4 * s)}" y="{f(y - 30 * s)}" width="{f(8 * s)}" height="{f(30 * s)}" fill="#4A2A1A" stroke="#0D0D0F" stroke-width="1.4"></rect>'
            f'<path d="M{f(x - 30 * s)} {f(y - 34 * s)} C {f(x - 44 * s)} {f(y - 60 * s)} {f(x - 20 * s)} {f(y - 86 * s)} {f(x)} {f(y - 80 * s)} C {f(x + 24 * s)} {f(y - 90 * s)} {f(x + 46 * s)} {f(y - 60 * s)} {f(x + 30 * s)} {f(y - 34 * s)} Z" '
            f'fill="{color}" stroke="#0D0D0F" stroke-width="{f(max(1.2, 1.8 * s))}"></path>')

def flame(x, y, s=1.0, seed=1):
    """A tongue of fire, (x, y) its foot."""
    r = random.Random(seed); t = r.uniform(-8, 8)
    return (f'<path d="M{f(x - 18 * s)} {f(y)} C {f(x - 26 * s)} {f(y - 30 * s)} {f(x - 6 * s)} {f(y - 40 * s)} {f(x + t * s)} {f(y - 80 * s)} C {f(x + 8 * s)} {f(y - 50 * s)} {f(x + 28 * s)} {f(y - 34 * s)} {f(x + 18 * s)} {f(y)} Z" fill="#FF6A2A" stroke="#0D0D0F" stroke-width="{f(max(1, 1.6 * s))}"></path>'
            f'<path d="M{f(x - 9 * s)} {f(y)} C {f(x - 12 * s)} {f(y - 18 * s)} {f(x)} {f(y - 26 * s)} {f(x + t * 0.5 * s)} {f(y - 48 * s)} C {f(x + 6 * s)} {f(y - 30 * s)} {f(x + 14 * s)} {f(y - 18 * s)} {f(x + 9 * s)} {f(y)} Z" fill="#FFD23F"></path>')

def little_fire(w, h, seed):
    """Behold, how much wood is kindled by how small a fire: a forest on the hills at night; at the left one small flame
    in the dry grass at its edge, and from it the fire running up through the trees until the whole wood blazes at the
    right, the smoke rolling up."""
    r = random.Random(seed)
    base = h * 0.92
    o = [sky(w, h, "#0B0B1A", "#3A1A1A"), halo(w * 0.8, h * 0.7, h * 0.8, "#FF6A2A", 0.45),
         hills(w, h, h * 0.56, seed, color="#1A1420", amp=14, step=80), ground(w, h, base, "#2A1A12", dy=0)]
    o.append(smoke(w * 0.78, h * 0.3, 6, seed, color="#4A3A3A", op=0.6, k=max(0.8, h / 260)))
    for i in range(int(w / 26)):
        x = i * 26 + r.uniform(-6, 6); t = x / w
        yb = base - r.uniform(0, h * 0.18) * (0.3 + t)
        s = (h / 300) * r.uniform(0.6, 1.0) * (0.8 + 0.5 * t)
        burnt = t > 0.55
        o.append(tree_shape(x, yb, s, r.randint(0, 1), color="#1A1410" if burnt else "#2E4A2A"))
        if t > 0.42:
            o.append(flame(x, yb - 6 * s, s * (0.6 + 1.6 * (t - 0.42)), seed + i))
    o.append(flame(w * 0.12, base - 2, h / 900, seed))
    o.append(halo(w * 0.12, base - 10, h * 0.08, "#FFC14D", 0.7))
    o.append(tag(w * 0.12, base - 16, "HOW SMALL A FIRE", w * 0.2, h * 0.3, color=GOLD, size=9).replace(f'fill="{GOLD}"', f'fill="{GOLD}"'))
    o.append(plate_label(w * 0.72, h * 0.1, "HOW MUCH WOOD IS KINDLED", "#FFE6A0", 10, halo_="#2A0A0A"))
    return "".join(o)

def dolphin(x, y, s=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-60 0 C -40 -26 0 -34 40 -22 C 52 -18 62 -14 70 -10 L 64 -4 C 50 -2 30 4 0 6 C -24 8 -44 6 -60 0 Z" fill="#5A7A9A" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M-6 -30 C -2 -44 10 -50 16 -50 C 12 -40 12 -32 14 -26 Z" fill="#4A6A8A" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M-58 0 C -70 -10 -80 -14 -84 -10 C -78 -4 -76 2 -84 10 C -76 12 -68 8 -58 2 Z" fill="#4A6A8A" stroke="#0D0D0F" stroke-width="2"></path>'
            '<circle cx="48" cy="-14" r="2" fill="#0D0D0F"></circle></g>')

def tamed(w, h):
    """Every kind of beasts and birds, of creeping things and things in the sea, is tamed: a plate of four cells — a lion
    led on a cord, a falcon on the hand, a serpent charmed in its basket, a dolphin following the ship — and across them
    the tongue, which no man can tame."""
    o = [plate_bg(w, h, "JAMES 3:7–8 · TAMED BY MANKIND")]
    cw = w / 4; base = h * 0.78; k = min(cw / 175, h / 300)
    for i, name in enumerate(("BEASTS", "BIRDS", "CREEPING THINGS", "THINGS IN THE SEA")):
        x0 = cw * i; cx = x0 + cw / 2
        o.append(f'<rect x="{f(x0 + 8)}" y="{f(h * 0.14)}" width="{f(cw - 16)}" height="{f(h * 0.7)}" fill="none" stroke="{CY}" stroke-width="1.2" opacity="0.7"></rect>')
        if i == 0:
            o.append(lion_walk(cx + 6 * k, base, 1.15 * k) + f'<path d="M{f(cx + 64 * k)} {f(base - 40 * k)} C {f(cx + 74 * k)} {f(base - 70 * k)} {f(cx + 70 * k)} {f(base - 90 * k)} {f(cx + 74 * k)} {f(base - 110 * k)}" stroke="{GOLD}" stroke-width="2" fill="none"></path>')
        elif i == 1:
            o.append(f'<path d="M{f(cx - 40 * k)} {f(base)} C {f(cx - 30 * k)} {f(base - 40 * k)} {f(cx - 10 * k)} {f(base - 70 * k)} {f(cx + 4 * k)} {f(base - 86 * k)} L {f(cx + 30 * k)} {f(base - 82 * k)} '
                     f'L {f(cx + 28 * k)} {f(base - 66 * k)} C {f(cx + 10 * k)} {f(base - 50 * k)} {f(cx - 6 * k)} {f(base - 24 * k)} {f(cx - 12 * k)} {f(base)} Z" fill="#8A5A3A" stroke="{INK}" stroke-width="2"></path>'
                     + dove(cx + 6 * k, base - 92 * k, 1.1 * k, wings="up").replace("#F3EFE6", "#B8A07A"))
        elif i == 2:
            o.append(f'<path d="M{f(cx - 34 * k)} {f(base)} L {f(cx - 40 * k)} {f(base - 44 * k)} L {f(cx + 40 * k)} {f(base - 44 * k)} L {f(cx + 34 * k)} {f(base)} Z" fill="#B8864A" stroke="{INK}" stroke-width="2"></path>'
                     + "".join(f'<path d="M{f(cx - 38 * k)} {f(base - 44 * k + j * 11 * k)} L {f(cx + 38 * k)} {f(base - 44 * k + j * 11 * k)}" stroke="#8A5A2A" stroke-width="1.4"></path>' for j in range(1, 4)))
            pts = [(cx - 10 * k, base - 46 * k), (cx + 6 * k, base - 70 * k), (cx - 8 * k, base - 96 * k), (cx + 4 * k, base - 120 * k)]
            o.append(SN.snake(pts[::-1], 7 * k, "tmsn", head_scale=0.6))
        else:
            o.append(f'<path d="M{f(x0 + 8)} {f(base - 20 * k)} C {f(x0 + cw * 0.4)} {f(base - 28 * k)} {f(x0 + cw * 0.6)} {f(base - 12 * k)} {f(x0 + cw - 8)} {f(base - 22 * k)} L {f(x0 + cw - 8)} {f(h * 0.84)} L {f(x0 + 8)} {f(h * 0.84)} Z" fill="#14304A"></path>'
                     + dolphin(cx, base - 44 * k, 0.95 * k))
        o.append(label(cx, h * 0.2, name, CY, 9) + label(cx, h * 0.8, "TAMED", GOLD, 9))
    o.append(f'<rect x="{f(w * 0.2)}" y="{f(h * 0.865)}" width="{f(w * 0.6)}" height="{f(h * 0.09)}" fill="#3A0A10" stroke="#FF6A4A" stroke-width="1.6"></rect>'
             + label(w * 0.5, h * 0.925, "THE TONGUE CAN NO MAN TAME", "#FF8A6A", 10))
    return "".join(o)

def fountain_trees(w, h, seed):
    """Doth the fountain send forth from the same opening sweet water and bitter? can a fig tree yield olives, or a vine
    figs?: a plate of four cells — a spring in the rock running sweet, a fig tree with its figs, an olive with its olives, a
    vine with its grapes — each bearing after its own kind."""
    o = [plate_bg(w, h, "JAMES 3:11–12 · EACH AFTER ITS KIND")]
    cw = w / 4; base = h * 0.84; k = min(cw / 175, h / 300)
    for i, name in enumerate(("THE FOUNTAIN · SWEET WATER", "THE FIG TREE · FIGS", "THE OLIVE · OLIVES", "THE VINE · GRAPES")):
        x0 = cw * i; cx = x0 + cw / 2
        o.append(f'<rect x="{f(x0 + 8)}" y="{f(h * 0.14)}" width="{f(cw - 16)}" height="{f(h * 0.76)}" fill="#0F2238" stroke="{CY}" stroke-width="1.2" opacity="0.9"></rect>'
                 f'<path d="M{f(x0 + 8)} {f(base)} L {f(x0 + cw - 8)} {f(base)}" stroke="#6A5A3A" stroke-width="3"></path>')
        if i == 0:
            o.append(f'<path d="M{f(cx - 60 * k)} {f(base)} L {f(cx - 50 * k)} {f(base - 90 * k)} C {f(cx - 20 * k)} {f(base - 120 * k)} {f(cx + 30 * k)} {f(base - 110 * k)} {f(cx + 54 * k)} {f(base - 80 * k)} L {f(cx + 60 * k)} {f(base)} Z" fill="#7A7068" stroke="{INK}" stroke-width="2"></path>'
                     f'<ellipse cx="{f(cx)}" cy="{f(base - 60 * k)}" rx="{f(10 * k)}" ry="{f(7 * k)}" fill="#0D0D0F"></ellipse>'
                     f'<path d="M{f(cx)} {f(base - 56 * k)} C {f(cx + 4 * k)} {f(base - 30 * k)} {f(cx + 10 * k)} {f(base - 14 * k)} {f(cx + 4 * k)} {f(base)}" stroke="#8FD0E2" stroke-width="{f(6 * k)}" fill="none"></path>'
                     f'<ellipse cx="{f(cx + 6 * k)}" cy="{f(base + 2)}" rx="{f(36 * k)}" ry="{f(6 * k)}" fill="#3A8AB0" stroke="{INK}" stroke-width="1.4"></ellipse>')
        elif i == 1:
            o.append(fig_tree(cx, base, 0.9 * k, fruit=True, seed=seed))
        elif i == 2:
            o.append(olive(cx, base, 0.9 * k, seed=seed))
            r = random.Random(seed)
            o.append("".join(f'<ellipse cx="{f(cx + r.uniform(-40, 40) * k)}" cy="{f(base - r.uniform(70, 130) * k)}" rx="{f(3.4 * k)}" ry="{f(2.4 * k)}" fill="#3A3A1A" stroke="{INK}" stroke-width="0.8"></ellipse>' for _ in range(16)))
        else:
            o.append(f'<path d="M{f(cx - 40 * k)} {f(base)} L {f(cx - 40 * k)} {f(base - 110 * k)} M{f(cx + 40 * k)} {f(base)} L {f(cx + 40 * k)} {f(base - 110 * k)} M{f(cx - 48 * k)} {f(base - 106 * k)} L {f(cx + 48 * k)} {f(base - 106 * k)}" stroke="#6A4A2A" stroke-width="{f(4 * k)}"></path>'
                     f'<path d="M{f(cx)} {f(base)} C {f(cx - 10 * k)} {f(base - 40 * k)} {f(cx + 10 * k)} {f(base - 70 * k)} {f(cx)} {f(base - 104 * k)} C {f(cx - 20 * k)} {f(base - 110 * k)} {f(cx - 40 * k)} {f(base - 104 * k)} {f(cx - 46 * k)} {f(base - 100 * k)} M{f(cx)} {f(base - 104 * k)} C {f(cx + 20 * k)} {f(base - 112 * k)} {f(cx + 40 * k)} {f(base - 104 * k)} {f(cx + 46 * k)} {f(base - 100 * k)}" fill="none" stroke="#5A3A1A" stroke-width="{f(4 * k)}"></path>')
            for gx in (-30, 0, 28):
                for j, (dx, dy) in enumerate(((0, 0), (-5, 7), (5, 7), (-3, 14), (3, 14), (0, 21))):
                    o.append(f'<circle cx="{f(cx + (gx + dx) * k)}" cy="{f(base - (92 - dy) * k)}" r="{f(4.2 * k)}" fill="#5A2A6A" stroke="{INK}" stroke-width="1"></circle>')
                o.append(f'<ellipse cx="{f(cx + (gx + 9) * k)}" cy="{f(base - 96 * k)}" rx="{f(9 * k)}" ry="{f(5 * k)}" fill="#4A8A3A" stroke="{INK}" stroke-width="1"></ellipse>')
        o.append(label(cx, h * 0.2, name, CY, 8))
    return "".join(o)

def sown_in_peace(p, w, h, seed):
    """The fruit of righteousness is sown in peace for them that make peace: a quiet valley at dawn, a sower walking his
    field scattering the seed, the furrows, olive trees and a village asleep, a dove in the sky."""
    b = h * 0.92
    o = [D_(p), vista(w, h, seed, tone="dawn", horizon=0.5, sun_at=(0.82, 0.42), hills_n=2, ground_=False),
         f'<path d="M-10 {f(h * 0.56)} C {f(w * 0.3)} {f(h * 0.52)} {f(w * 0.7)} {f(h * 0.54)} {f(w + 10)} {f(h * 0.56)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A6A44" stroke="{INK}" stroke-width="2"></path>']
    for k in range(9):                                               # the furrows, running away to the hills
        y = h * 0.58 + (b - h * 0.58) * (k / 8) ** 1.4
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 4)} {f(w * 0.7)} {f(y + 3)} {f(w + 10)} {f(y)}" stroke="#6A4A2A" stroke-width="{f(1 + k * 0.3)}" fill="none"></path>')
    o.append(olive(w * 0.06, h * 0.6, h / 520, seed=seed) + olive(w * 0.94, h * 0.6, h / 600, seed=seed + 1))
    s = fit(b, max(h * 0.2, b - 210))
    bag = '<path d="M14 -110 C 30 -104 34 -86 26 -74 L 8 -80 Z" fill="#C8A060" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(man_r(p, w * 0.42, b, s, 0, flip=True, up=[(-22, -158), (-46, -150), (-70, -140)], pose="walk", extra=bag, cloth="#6A6A4A"))
    r = random.Random(seed)
    for i in range(18):
        a = r.uniform(0, 1)
        o.append(f'<circle cx="{f(w * 0.42 + (70 + a * 120) * s)}" cy="{f(b - (140 - a * a * 160) * s)}" r="{f(1.8 * s + 0.6)}" fill="#E8D8A0"></circle>')
    o.append(dove(w * 0.7, h * 0.22, h / 360, wings="up"))
    o.append(plate_label(w * 0.5, h * 0.1, "SOWN IN PEACE", "#2A1A3A", 10, halo_="#FFE0C0"))
    return "".join(o)

# ---- James 4 ----------------------------------------------------------------------------------------------------------------
def empty_war(w, h, seed):
    """Whence come wars and whence come fightings among you?: a field after the fighting at dusk, no one in it — broken
    spears standing in the earth, a shield face down, a fallen standard, and the smoke going up from a burned village."""
    r = random.Random(seed)
    base = h * 0.94
    o = [sky(w, h, "#2A1A3A", "#C8603A"), halo(w * 0.2, h * 0.56, h * 0.4, "#FF8A3D", 0.5),
         f'<circle cx="{f(w * 0.2)}" cy="{f(h * 0.56)}" r="{f(h * 0.08)}" fill="#FFB07A"></circle>',
         hills(w, h, h * 0.58, seed, color="#3A2A3A", amp=12, step=90),
         walls(w * 0.62, w * 0.9, h * 0.62, h * 0.12, seed, color="#5A4A4A", towers=2),
         smoke(w * 0.7, h * 0.46, 5, seed, color="#5A5060", op=0.6, k=max(0.7, h / 280)), smoke(w * 0.84, h * 0.48, 4, seed + 3, color="#5A5060", op=0.5, k=max(0.7, h / 300)),
         f'<path d="M-10 {f(h * 0.64)} C {f(w * 0.3)} {f(h * 0.62)} {f(w * 0.7)} {f(h * 0.66)} {f(w + 10)} {f(h * 0.64)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#4A3428" stroke="{INK}" stroke-width="2"></path>']
    for i in range(9):
        x = w * (0.06 + i * 0.11 + r.uniform(-0.03, 0.03)); y = h * r.uniform(0.7, 0.92); L = h * r.uniform(0.18, 0.34) * (0.6 + (y / h - 0.64))
        a = r.uniform(-18, 18)
        o.append(f'<g transform="rotate({f(a)} {f(x)} {f(y)})"><path d="M{f(x)} {f(y)} L {f(x)} {f(y - L)}" stroke="#6A4A2A" stroke-width="{f(max(2, h / 120))}"></path>'
                 + (f'<path d="M{f(x - 4)} {f(y - L)} L {f(x)} {f(y - L - 14)} L {f(x + 4)} {f(y - L)} Z" fill="#8A8A94" stroke="{INK}" stroke-width="1.2"></path>' if i % 3 else
                    f'<path d="M{f(x)} {f(y - L)} l 6 -8 M{f(x)} {f(y - L)} l -5 -7" stroke="#6A4A2A" stroke-width="2"></path>') + '</g>')
    o.append(f'<ellipse cx="{f(w * 0.36)}" cy="{f(base - h * 0.04)}" rx="{f(h * 0.12)}" ry="{f(h * 0.035)}" fill="#8A6A3A" stroke="{INK}" stroke-width="2"></ellipse>'
             f'<circle cx="{f(w * 0.36)}" cy="{f(base - h * 0.045)}" r="{f(h * 0.018)}" fill="#C8A060" stroke="{INK}" stroke-width="1.4"></circle>'
             f'<path d="M{f(w * 0.56)} {f(base)} L {f(w * 0.64)} {f(base - h * 0.2)} M{f(w * 0.64)} {f(base - h * 0.2)} L {f(w * 0.72)} {f(base - h * 0.16)} L {f(w * 0.65)} {f(base - h * 0.13)}" stroke="#3A2A1A" stroke-width="3" fill="#8A1A1A"></path>')
    o.append(plate_label(w * 0.5, h * 0.1, "WARS · FIGHTINGS", "#FFE0C0", 10, halo_="#2A1A3A"))
    return "".join(o)

def draw_nigh(p, w, h, seed):
    """Draw nigh to God, and he will draw nigh to you … Humble yourselves in the sight of the Lord: a man kneeling alone on a
    bare hilltop at evening, his hands lifted, a light falling down upon him from the opened sky (no figure in it)."""
    b = h * 0.9
    o = [D_(p), sky(w, h, "#14102A", "#4A3A6A"), starfield(w, h, seed, 40, 0.5),
         f'<defs><linearGradient id="{p}dl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.9"></stop><stop offset="1" stop-color="#FFE680" stop-opacity="0.25"></stop></linearGradient></defs>',
         f'<path d="M{f(w * 0.46)} -10 L {f(w * 0.58)} -10 L {f(w * 0.68)} {f(b)} L {f(w * 0.4)} {f(b)} Z" fill="url(#{p}dl)"></path>',
         halo(w * 0.52, -10, h * 0.5, "#FFFFFF", 0.7),
         hills(w, h, h * 0.66, seed, color="#2A2440", amp=10, step=90),
         f'<path d="M-10 {f(h + 10)} L -10 {f(b + 4)} C {f(w * 0.3)} {f(b - h * 0.06)} {f(w * 0.7)} {f(b - h * 0.06)} {f(w + 10)} {f(b + 4)} L {f(w + 10)} {f(h + 10)} Z" fill="#4A3A4A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.2, b - 220))
    o.append(E.kneel(w * 0.54, b - h * 0.03, s * 1.05, color="#6A6458", skin=SKIN))
    o.append(plate_label(w * 0.2, h * 0.12, "DRAW NIGH TO GOD", "#FFE6A0", 10, halo_="#14102A"))
    return "".join(o)

def vapor(p, w, h, seed):
    """To-day or to-morrow we will go into this city, and spend a year there, and trade …: a caravan of merchants setting
    out at sunrise on the road to a far city, their asses laden; and over the valley the morning mist, already thinning
    and vanishing in the sun — what is your life? a vapor."""
    b = h * 0.92
    o = [D_(p), vista(w, h, seed, tone="dawn", horizon=0.52, sun_at=(0.78, 0.36), hills_n=2, city="walls", cx=0.8, cw=0.24, ground_=True)]
    o.append(f'<path d="M-10 {f(b + 6)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.6)} {f(w * 0.74)} {f(h * 0.57)}" stroke="#D8C08A" stroke-width="{f(max(10, h * 0.08))}" fill="none" opacity="0.9"></path>')
    s = fit(b, max(h * 0.3, b - 180))
    load = '<rect x="-24" y="-96" width="40" height="22" rx="5" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
    o.append(f'<g>{N1.ass(w * 0.18, b, s * 0.9, flip=True)}</g>' + f'<g transform="translate({f(w * 0.18)} {f(b)}) scale({f(-s * 0.9)} {f(s * 0.9)})">{load}</g>')
    o.append(man_r(p, w * 0.34, b, s, 1, flip=True, pose="walk"))
    o.append(rich_man(p, w * 0.46, b - 4, s * 0.98, flip=True, pose="walk"))
    o.append(man_r(p, w * 0.06, b, s * 0.96, 0, flip=True, pose="walk"))
    r = random.Random(seed)                                          # the mist: bands of vapor, the right-hand ones thinning in the sun
    for i in range(7):
        y = h * r.uniform(0.44, 0.7); x = w * r.uniform(-0.1, 0.8); L = w * r.uniform(0.3, 0.6)
        op = 0.55 * (1 - min(1, (x + L * 0.5) / w)) + 0.08
        o.append(f'<ellipse cx="{f(x + L / 2)}" cy="{f(y)}" rx="{f(L / 2)}" ry="{f(h * 0.035)}" fill="#F8F4F0" opacity="{op:.2f}"></ellipse>')
    o.append(plate_label(w * 0.5, h * 0.1, "A VAPOR THAT APPEARETH FOR A LITTLE TIME", "#3A2A4A", 9, halo_="#FFE0C8"))
    return "".join(o)

# ---- James 5 ----------------------------------------------------------------------------------------------------------------
def moth(x, y, s=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M0 0 C -10 -12 -22 -10 -20 0 C -22 8 -10 10 0 2 C 10 10 22 8 20 0 C 22 -10 10 -12 0 0 Z" fill="#C8B898" stroke="#0D0D0F" stroke-width="1.4"></path>'
            '<path d="M0 -4 L 0 6" stroke="#0D0D0F" stroke-width="2"></path></g>')

def rusted(w, h, seed):
    """Your riches are corrupted, and your garments are moth-eaten. Your gold and your silver are rusted: a strongroom by
    lamplight, the lid of the treasure chest thrown open on gold and silver gone dark and eaten with rust, a fine robe
    hanging full of holes, moths about it."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1E18"></rect>', lamp_glow(w * 0.2, h * 0.3, h * 0.8, "rs", op=0.4),
         f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#3A2A22" stroke="{INK}" stroke-width="2"></rect>']
    k = h / 300
    cx, cb = w * 0.36, h * 0.86                                      # the chest
    o.append(f'<path d="M{f(cx - 120 * k)} {f(cb - 120 * k)} L {f(cx - 110 * k)} {f(cb - 200 * k)} L {f(cx + 110 * k)} {f(cb - 200 * k)} L {f(cx + 120 * k)} {f(cb - 120 * k)} Z" fill="#5A3418" stroke="{INK}" stroke-width="2.4"></path>'
             f'<rect x="{f(cx - 120 * k)}" y="{f(cb - 120 * k)}" width="{f(240 * k)}" height="{f(120 * k)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(cx - 120 * k)} {f(cb - 80 * k)} L {f(cx + 120 * k)} {f(cb - 80 * k)} M{f(cx - 70 * k)} {f(cb - 120 * k)} L {f(cx - 70 * k)} {f(cb)} M{f(cx + 70 * k)} {f(cb - 120 * k)} L {f(cx + 70 * k)} {f(cb)}" stroke="#4A4A4A" stroke-width="{f(5 * k)}"></path>')
    for i in range(26):                                              # the coins, heaped, tarnished, eaten
        x = cx + r.uniform(-104, 104) * k; y = cb - 120 * k - r.uniform(0, 30) * k * (1 - abs(x - cx) / (120 * k))
        col = r.choice(("#8A7A3A", "#7A6A4A", "#8A8A84", "#6A5A3A"))
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(11 * k)}" ry="{f(5 * k)}" fill="{col}" stroke="{INK}" stroke-width="1.2"></ellipse>'
                 f'<circle cx="{f(x + r.uniform(-5, 5) * k)}" cy="{f(y)}" r="{f(2.4 * k)}" fill="#5A7A4A" opacity="0.8"></circle>')
    ex, ey = cx + 74 * k, cb - 130 * k                              # a silver ewer gone black, spotted with rust
    o.append(f'<path d="M{f(ex - 14 * k)} {f(ey)} C {f(ex - 26 * k)} {f(ey - 20 * k)} {f(ex - 20 * k)} {f(ey - 44 * k)} {f(ex - 8 * k)} {f(ey - 52 * k)} L {f(ex - 10 * k)} {f(ey - 66 * k)} L {f(ex + 14 * k)} {f(ey - 70 * k)} '
             f'L {f(ex + 10 * k)} {f(ey - 52 * k)} C {f(ex + 22 * k)} {f(ey - 44 * k)} {f(ex + 26 * k)} {f(ey - 20 * k)} {f(ex + 14 * k)} {f(ey)} Z" fill="#6A6A68" stroke="{INK}" stroke-width="2"></path>'
             f'<circle cx="{f(ex - 6 * k)}" cy="{f(ey - 26 * k)}" r="{f(4 * k)}" fill="#5A7A4A"></circle><circle cx="{f(ex + 8 * k)}" cy="{f(ey - 14 * k)}" r="{f(3 * k)}" fill="#7A4A2A"></circle>')
    rx, ry = w * 0.76, h * 0.1                                       # the robe on its peg, full of holes
    o.append(f'<circle cx="{f(rx)}" cy="{f(ry)}" r="4" fill="#6A4A2A"></circle>'
             f'<path d="M{f(rx)} {f(ry)} L {f(rx - 60 * k)} {f(ry + 40 * k)} L {f(rx - 70 * k)} {f(ry + 230 * k)} L {f(rx + 70 * k)} {f(ry + 230 * k)} L {f(rx + 60 * k)} {f(ry + 40 * k)} Z" fill="#6A2A6A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(rx - 66 * k)} {f(ry + 218 * k)} L {f(rx + 66 * k)} {f(ry + 218 * k)}" stroke="#C8A040" stroke-width="{f(5 * k)}"></path>')
    for i in range(11):
        o.append(f'<ellipse cx="{f(rx + r.uniform(-50, 50) * k)}" cy="{f(ry + r.uniform(60, 200) * k)}" rx="{f(r.uniform(4, 9) * k)}" ry="{f(r.uniform(3, 6) * k)}" fill="#2A1E18" stroke="#3A1A3A" stroke-width="1"></ellipse>')
    for i in range(5):
        o.append(moth(rx + r.uniform(-110, 110) * k, ry + r.uniform(20, 160) * k, 0.7 * k))
    o.append(plate_label(w * 0.36, h * 0.1, "YOUR GOLD AND YOUR SILVER ARE RUSTED", "#E8C060", 9, halo_="#2A1E18"))
    return "".join(o)

def mowers(p, w, h, seed):
    """The hire of the laborers who mowed your fields, which is of you kept back by fraud, crieth out: the field half
    reaped at evening, the sheaves stacked, the mowers standing at its edge with their sickles and their empty hands held
    out; up on the hill the rich man's house, lit, its door shut."""
    b = h * 0.92
    o = [D_(p), sky(w, h, "#3A2A5A", "#FFB07A"), hills(w, h, h * 0.42, seed, color="#6A5A6A", amp=12, step=90)]
    hx = w * 0.78                                                    # the house on the hill
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.5)} C {f(w * 0.7)} {f(h * 0.3)} {f(w * 0.9)} {f(h * 0.3)} {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h * 0.6)} L {f(w * 0.56)} {f(h * 0.6)} Z" fill="#6A6A4A" stroke="{INK}" stroke-width="2"></path>'
             f'<rect x="{f(hx - w * 0.08)}" y="{f(h * 0.2)}" width="{f(w * 0.16)}" height="{f(h * 0.14)}" fill="#E0C8A0" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(hx - w * 0.015)}" y="{f(h * 0.25)}" width="{f(w * 0.03)}" height="{f(h * 0.09)}" fill="#3A2214" stroke="{INK}" stroke-width="1.4"></rect>'
             f'<rect x="{f(hx + w * 0.04)}" y="{f(h * 0.23)}" width="{f(w * 0.02)}" height="{f(h * 0.03)}" fill="#FFC14D"></rect><rect x="{f(hx - w * 0.06)}" y="{f(h * 0.23)}" width="{f(w * 0.02)}" height="{f(h * 0.03)}" fill="#FFC14D"></rect>')
    o.append(ground(w, h, h * 0.58, "#B89A5A", dy=0) + grain(w * 0.5, w + 10, h * 0.66, h * 0.1, seed, color="#E8C060"))
    for i in range(4):                                               # the sheaves on the reaped half
        x = w * (0.08 + i * 0.1)
        o.append(f'<path d="M{f(x - 10)} {f(h * 0.68)} L {f(x)} {f(h * 0.6)} L {f(x + 10)} {f(h * 0.68)} Z" fill="#D8B050" stroke="{INK}" stroke-width="1.4"></path>')
    s = fit(b, max(h * 0.24, b - 200))
    sick = '<path d="M-72 -150 C -86 -164 -84 -184 -66 -190" fill="none" stroke="#8A8A94" stroke-width="4"></path>'
    for i, x in enumerate((0.12, 0.26, 0.4)):
        o.append(robed(p, w * x, b, s * (1 - i * 0.02), ["#7A6A52", "#5A5A4A", "#6A5A4A"][i], head=["#E8E2D6", "#3A4A3A", "#2A3A4A"][i], cord="#2A1A10",
                       beard="#2A1A10", flip=True, up=[(-22, -158), (-44, -140), (-66, -144)], extra=sick if i == 1 else "",
                       belt="#4A3A2A"))
    o.append(plate_label(w * 0.3, h * 0.1, "THE HIRE KEPT BACK BY FRAUD", "#3A1A2A", 9, halo_="#FFE0C0"))
    return "".join(o)

def early_latter(p, w, h, seed):
    """Behold, the husbandman waiteth for the precious fruit of the earth, being patient over it, until it receive the
    early and latter rain: the husbandman standing at the edge of his sown field, the green blade just up, looking to the
    rain clouds coming over the hills, the rain falling far off; the two rains named on a calendar bar below."""
    b = h * 0.86
    o = [D_(p), sky(w, h, "#5A6A8A", "#D8D8C8"), clouds(w, h * 0.12, seed, n=6, color="#6A7088", op=0.95, ry=0.08, h=h),
         hills(w, h, h * 0.5, seed, color="#6A7A6A", amp=12, step=90)]
    r = random.Random(seed)
    for i in range(30):                                              # the rain over the far hills
        x = w * r.uniform(0.45, 1.0); y = h * r.uniform(0.18, 0.44)
        o.append(f'<path d="M{f(x)} {f(y)} l -4 14" stroke="#C8D8E8" stroke-width="1.6" opacity="0.8"></path>')
    o.append(f'<path d="M-10 {f(h * 0.56)} C {f(w * 0.3)} {f(h * 0.54)} {f(w * 0.7)} {f(h * 0.57)} {f(w + 10)} {f(h * 0.55)} L {f(w + 10)} {f(b + 6)} L -10 {f(b + 6)} Z" fill="#7A5A3A" stroke="{INK}" stroke-width="2"></path>')
    for k in range(8):
        y = h * 0.58 + (b - h * 0.58) * k / 8
        for j in range(int(w / 16)):
            x = j * 16 + (k % 2) * 8
            o.append(f'<path d="M{f(x)} {f(y + 6)} l -2 -6 M{f(x)} {f(y + 6)} l 2 -7" stroke="#6AAA3A" stroke-width="1.6"></path>')
    s = fit(b, max(h * 0.2, b - 190))
    staff = '<path d="M-52 -176 L -46 4" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"></path>'
    o.append(man_r(p, w * 0.18, b, s, 2, flip=True, up=[(-22, -158), (-38, -124), (-48, -96)], extra=staff))
    bar_y = b + (h - b) * 0.25; bh = (h - b) * 0.55
    o.append(f'<rect x="-10" y="{f(b + 6)}" width="{f(w + 20)}" height="{f(h - b)}" fill="#0B1A2E"></rect>')
    for i, (lab, x0, x1, c) in enumerate((("THE EARLY RAIN · AUTUMN · SOWING", 0.03, 0.42, "#3A8AB0"), ("THE LATTER RAIN · SPRING · THE EAR", 0.45, 0.84, "#3AB08A"))):
        o.append(f'<rect x="{f(w * x0)}" y="{f(bar_y)}" width="{f(w * (x1 - x0))}" height="{f(bh)}" fill="{c}" stroke="{INK}" stroke-width="1.4"></rect>'
                 + label(w * (x0 + x1) / 2, bar_y + bh * 0.68, lab, "#F3EFE6", 8))
    o.append(plate_label(w * 0.5, h * 0.08, "THE HUSBANDMAN WAITETH", "#1A2A3A", 10, halo_="#E8E8E0"))
    return "".join(o)

def anointing(p, w, h, seed):
    """Is any among you sick? let him call for the elders of the church; and let them pray over him, anointing him with oil:
    a house by lamplight, the sick man lying on his bed, two elders standing over him — one pouring the oil from a horn on
    his head, one with his hands lifted in prayer — and his wife at the door."""
    b = h * 0.94
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp", *LIE), room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * 0.5, h * 0.4, h * 0.8, f"{p}an", op=0.45)]
    s = fit(b, max(h * 0.16, b - 225))
    o.append(clay_lamp(w * 0.86, b - 120 * s, s * 0.8) + f'<rect x="{f(w * 0.82)}" y="{f(b - 112 * s)}" width="{f(w * 0.08)}" height="8" fill="#6A4A2A" stroke="{INK}" stroke-width="1.4"></rect>')
    bx = w * 0.48
    o.append(f'<rect x="{f(bx - 130 * s)}" y="{f(b - 40 * s)}" width="{f(260 * s)}" height="{f(14 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(xx)}" y="{f(b - 26 * s)}" width="{f(10 * s)}" height="{f(26 * s)}" fill="#4A2412" stroke="{INK}" stroke-width="1.4"></rect>' for xx in (bx - 124 * s, bx + 114 * s)))
    o.append(on_bed(p, bx, b - 54 * s, 250 * s, cloth="#C8B898", flip=False))
    horn = '<path d="M-72 -160 C -80 -170 -96 -170 -100 -158 L -86 -150 Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M-98 -156 l -3 10" stroke="#E8C060" stroke-width="2.4"></path>'
    o.append(elder_r(p, bx - 130 * s, b, s, 0, flip=True, up=[(-22, -158), (-50, -150), (-74, -158)], extra=horn))
    o.append(elder_r(p, bx + 150 * s, b, s, 1, flip=False, up=UP_HEAVEN))
    o.append(woman_r(p, w * 0.08, b, s, 3, flip=True))
    o.append(plate_label(w * 0.5, h * 0.08, "ANOINTING HIM WITH OIL IN THE NAME OF THE LORD", "#FFE6A0", 9, halo_="#2A1A12"))
    return "".join(o)

def brought_back(p, w, h, seed):
    """If any among you err from the truth, and one convert him …: a road at dusk running back to a lit town; at the right
    the road's edge breaking off into the dark wilderness, a man who had strayed from the way, and a brother taking him by
    the hand to lead him back."""
    b = h * 0.92
    o = [D_(p), sky(w, h, "#2A1A3A", "#E8903A"), halo(w * 0.16, h * 0.5, h * 0.4, "#FFC14D", 0.5),
         walls(w * 0.02, w * 0.3, h * 0.56, h * 0.14, seed, lit=True, towers=2),
         f'<path d="M-10 {f(h * 0.6)} L {f(w * 0.58)} {f(h * 0.6)} L {f(w * 0.64)} {f(h * 0.7)} L {f(w * 0.7)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.58)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.7)} {f(h + 10)} L {f(w * 0.64)} {f(h * 0.7)} Z" fill="#2A1E2A" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.3)} {f(h * 0.62)} C {f(w * 0.36)} {f(h * 0.72)} {f(w * 0.42)} {f(h * 0.82)} {f(w * 0.44)} {f(h + 10)}" stroke="#D8C08A" stroke-width="{f(max(12, h * 0.1))}" fill="none"></path>']
    for i in range(6):
        r = random.Random(seed + i)
        o.append(f'<path d="M{f(w * r.uniform(0.74, 1.0))} {f(h * r.uniform(0.66, 0.96))} l {f(r.uniform(-14, 14))} {f(r.uniform(-20, -8))} l 8 -4" stroke="#4A3A4A" stroke-width="2.4" fill="none"></path>')
    s = fit(b, max(h * 0.2, b - 210))
    o.append(man_r(p, w * 0.3, b, s, 1, flip=True, up=[(-22, -158), (-48, -142), (-72, -138)]))
    o.append(poor_man(p, w * 0.48, b, s * 0.97, flip=False, up=[(-22, -158), (-46, -144), (-66, -140)]))
    o.append(plate_label(w * 0.46, h * 0.1, "FROM THE ERROR OF HIS WAY", "#FFE0C0", 10, halo_="#2A1A3A"))
    return "".join(o)
