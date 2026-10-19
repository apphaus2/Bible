"""Drawings for the Joel volume, on top of Hosea's (hos.art: Israel's land, olive trees, lilies; hos.art2: the land
mourning, the latter rain, the israel_map). The locusts: a plate of the four kinds (the palmer-worm, the locust, the
canker-worm, the caterpillar) and swarms darkening the sky over the fields and climbing the walls — never anything gory.
Joel at a distance: a dark teal headcloth, brown beard, a slate robe (joel_fig)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from hos.art import *
from hos.art import f, K2
from hos.art2 import land_mourns, latter_rain, israel_map, PL, FIELD, oaks
import joshua1 as J1x, samuel1 as S1x, samuel4 as S4x, judges1 as J1y, judges2 as JG
from genesis.art3 import flock
from kg1.art import temple_front, priest

JOEL_C = "#4A5A6A"

def joel_fig(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=JOEL_C, sw=3, flip=flip, up=up, extra=A.headcloth("#1F4A4A", cord="#2A1A10") + A.BLACK_BEARD.replace("#2A1A10", "#4A3424"))

def joel_land(p, w, h, seed):
    """Joel calling the old men and all the inhabitants of the land: the prophet standing on the slope, the elders gathered."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), land(w, h, seed, tone="grey", olives=2)]
    s = fit(b, b - h * 0.5)
    o.append(joel_fig(p, w * 0.78, b, s, flip=True, up=[(-22, -158), (-46, -176), (-70, -186)]))
    for i in range(6):
        o.append(A.elder(("#8A7A6A", "#6A5A4A", "#7A6A5A")[i % 3], i)(p, w * (0.08 + i * 0.09), b - (i % 2) * 8, s * (0.84 + (i % 2) * 0.04)))
    return "".join(o)

def locust(x, y, s=1.0,color="#8A7A3A", wing="#C8B878", flip=False, rot=0):
    """A locust in profile, head to the right: the long body, the folded wings, the great hind leg, the antennae."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(sx)} {f(s)})">'
            '<path d="M-34 -2 C -36 -10 -20 -14 0 -14 L 22 -14 C 30 -14 34 -8 34 -2 C 34 4 28 8 20 8 L -20 6 C -30 6 -34 4 -34 -2 Z" fill="' + color + '" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M-40 -6 C -20 -20 10 -22 20 -14 C 0 -10 -24 -6 -40 -6 Z" fill="' + wing + '" stroke="#0D0D0F" stroke-width="1.2" opacity="0.9"></path>'
            '<path d="M-6 6 L -18 -18 L -34 14" fill="none" stroke="#0D0D0F" stroke-width="3" stroke-linejoin="round"></path>'
            '<path d="M-6 6 L -18 -18 L -34 14" fill="none" stroke="' + color + '" stroke-width="1.6" stroke-linejoin="round"></path>'
            '<path d="M14 8 L 12 18 M22 6 L 24 16" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M30 -10 C 40 -24 46 -28 54 -30 M28 -12 C 34 -26 38 -30 44 -34" fill="none" stroke="#0D0D0F" stroke-width="1.2"></path>'
            '<circle cx="28" cy="-6" r="2.4" fill="#0D0D0F"></circle></g>')

def worm(x, y, s=1.0, color="#7A8A3A", hairy=False):
    """A crawling larva: a row of segments, head to the right."""
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">']
    for i in range(8):
        cx = -28 + i * 8; cy = -6 - math.sin(i * 0.7) * 4
        o.append(f'<circle cx="{cx}" cy="{f(cy)}" r="6" fill="{color}" stroke="#0D0D0F" stroke-width="1.2"></circle>')
        if hairy: o.append(f'<path d="M{cx} {f(cy - 6)} l -2 -6 M{cx + 2} {f(cy - 6)} l 2 -6" stroke="#3A2A1A" stroke-width="1"></path>')
    o.append('<circle cx="32" cy="-8" r="2" fill="#0D0D0F"></circle></g>')
    return "".join(o)

def locust_plate(w, h):
    """That which the palmer-worm hath left hath the locust eaten: the four, as a technical plate, each eating after the other."""
    o = [grid_bg(w, h)]
    k = min(1.6, h / 120, w / 520)
    kinds = [("THE PALMER-WORM", lambda x, y: worm(x, y, k, "#8A9A3A")), ("THE LOCUST", lambda x, y: locust(x, y, k)),
             ("THE CANKER-WORM", lambda x, y: locust(x, y, k * 0.8, color="#6A7A3A", wing="#6A7A3A")), ("THE CATERPILLAR", lambda x, y: worm(x, y, k, "#9A6A3A", hairy=True))]
    for i, (t, fn) in enumerate(kinds):
        x = w * (0.13 + i * 0.25); y = h * 0.56
        o.append(f'<rect x="{f(x - w * 0.11)}" y="{f(h * 0.2)}" width="{f(w * 0.22)}" height="{f(h * 0.56)}" fill="none" stroke="#1E5A7A" stroke-width="1.4"></rect>'
                 + fn(x, y) + label(x, h * 0.12, t, "#FFD23F", max(7, min(10, 8 * k))))
        if i < 3: o.append(route([(x + w * 0.11, h * 0.48), (x + w * 0.14, h * 0.48)], color="#FF8A6A"))
    o.append(label(w * 0.5, h * 0.92, "THAT WHICH THE ONE HATH LEFT HATH THE NEXT EATEN", "#FF8A6A", 8))
    return "".join(o)

def swarm(w, h, seed, n=None, y0=0.0, y1=0.6, color="#3A3A1A", dark=True):
    """A cloud of locusts filling the sky."""
    r = random.Random(seed)
    o = []
    if dark: o.append(f'<path d="M-10 {f(h * y0)} C {f(w * 0.3)} {f(h * (y0 + 0.1))} {f(w * 0.7)} {f(h * (y0 - 0.04))} {f(w + 10)} {f(h * y0)} L {f(w + 10)} {f(h * y1)} C {f(w * 0.6)} {f(h * (y1 + 0.06))} {f(w * 0.3)} {f(h * (y1 - 0.04))} -10 {f(h * y1)} Z" fill="#3A3424" opacity="0.45"></path>')
    for i in range(n or int(w * h / 900)):
        x = r.uniform(-10, w + 10); y = r.uniform(h * y0, h * y1)
        o.append(locust(x, y, r.uniform(0.16, 0.34), color=color, wing="#8A8460", rot=r.uniform(-20, 20), flip=r.random() < 0.3))
    return "".join(o)

def bare_vine(w, h, seed):
    """He hath laid my vine waste, and barked my fig-tree: stripped vines, a fig-tree with its bark gone white, locusts on
    the ground."""
    o = [land(w, h, seed, tone="grey", olives=0, horizon=0.4)]
    k = min(1.4, h / 240)
    for i in range(6):
        x = w * (0.06 + i * 0.1); by = h * 0.92
        o.append(f'<path d="M{f(x)} {f(by)} C {f(x - 6 * k)} {f(by - 30 * k)} {f(x + 8 * k)} {f(by - 50 * k)} {f(x)} {f(by - 70 * k)} M{f(x)} {f(by - 50 * k)} l {f(18 * k)} {f(-10 * k)} M{f(x)} {f(by - 36 * k)} l {f(-16 * k)} {f(-8 * k)}" fill="none" stroke="#6A4A2A" stroke-width="{f(3 * k)}" stroke-linecap="round"></path>')
    fx, by = w * 0.8, h * 0.92
    o.append(f'<path d="M{f(fx - 10 * k)} {f(by)} L {f(fx - 6 * k)} {f(by - 90 * k)} L {f(fx + 6 * k)} {f(by - 90 * k)} L {f(fx + 10 * k)} {f(by)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></path>')
    for a, l in ((-40, 60), (-140, 56), (-70, 50), (-110, 46), (-20, 40)):
        o.append(f'<path d="M{f(fx)} {f(by - 80 * k)} l {f(math.cos(math.radians(a)) * l * k)} {f(math.sin(math.radians(a)) * l * k)}" stroke="#0D0D0F" stroke-width="{f(6 * k)}" stroke-linecap="round"></path>'
                 f'<path d="M{f(fx)} {f(by - 80 * k)} l {f(math.cos(math.radians(a)) * l * k)} {f(math.sin(math.radians(a)) * l * k)}" stroke="#F3EFE6" stroke-width="{f(4 * k)}" stroke-linecap="round"></path>')
    r = random.Random(seed)
    o.append("".join(locust(r.uniform(0, w), r.uniform(h * 0.86, h * 0.98), 0.3 * k, rot=r.uniform(-10, 10)) for _ in range(10)))
    return "".join(o)

def priests_mourn(p, w, h, seed, porch=False):
    """The priests, Jehovah's ministers, in sackcloth before the altar of the house of Jehovah; porch=True: weeping between
    the porch and the altar."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A5A6A", "#A89A8A"), temple_front(w * 0.66, h * 0.8, w * 0.5, seed), ground(w, h, h * 0.8, "#8A7A6A", dy=0)]
    k = min(1.4, h / 260)
    o.append(f'<rect x="{f(w * 0.26 - 30 * k)}" y="{f(h * 0.8 - 40 * k)}" width="{f(60 * k)}" height="{f(40 * k)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>')
    s = fit(b, b - h * 0.36)
    for i in range(4):
        x = w * (0.06 + i * 0.11) if not porch else w * (0.32 + i * 0.09)
        o.append(E.kneel(x, b, s * 1.1, color="#6A5E4A", skin="#C98E66", flip=i % 2 == 1))
    return "".join(o)

def withered(w, h, seed):
    """All the trees of the field are withered: the vine, the fig-tree, the pomegranate, the palm and the apple-tree, bare and
    grey on a grey field."""
    o = [K2.sky(w, h, "#9A9A9A", "#D8D0C0"), hills(w, h, h * 0.56, seed, "#A8A090", amp=10, step=100), ground(w, h, h * 0.66, "#B8A890", dy=0)]
    k = min(1.4, h / 260)
    for i, (x, t) in enumerate(((0.1, "VINE"), (0.3, "FIG-TREE"), (0.5, "POMEGRANATE"), (0.7, "PALM-TREE"), (0.9, "APPLE-TREE"))):
        bx, by = w * x, h * 0.86
        if t == "PALM-TREE":
            o.append(f'<path d="M{f(bx)} {f(by)} C {f(bx + 4 * k)} {f(by - 50 * k)} {f(bx + 10 * k)} {f(by - 90 * k)} {f(bx + 12 * k)} {f(by - 110 * k)}" stroke="#8A7A6A" stroke-width="{f(7 * k)}" fill="none"></path>'
                     + "".join(f'<path d="M{f(bx + 12 * k)} {f(by - 110 * k)} q {f(d * 20 * k)} {f(-10 * k)} {f(d * 34 * k)} {f(14 * k)}" stroke="#8A8A6A" stroke-width="{f(3 * k)}" fill="none"></path>' for d in (-1, -0.5, 0.5, 1)))
        else:
            o.append(f'<path d="M{f(bx)} {f(by)} L {f(bx)} {f(by - 60 * k)}" stroke="#7A6A5A" stroke-width="{f(6 * k)}"></path>'
                     + "".join(f'<path d="M{f(bx)} {f(by - 50 * k)} l {f(math.cos(math.radians(a)) * 34 * k)} {f(math.sin(math.radians(a)) * 34 * k)}" stroke="#7A6A5A" stroke-width="{f(3 * k)}" stroke-linecap="round"></path>' for a in (-40, -80, -110, -150)))
        o.append(label(bx, h * 0.96, t, "#3A3A3A", max(7, min(9, 7 * k))))
    return "".join(o)

def barns_broken(w, h, seed):
    """The garners laid desolate, the barns broken down: roofless storehouses, the seed rotting under the clods."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8A8A9A", "#D8C8B0"), ground(w, h, h * 0.66, "#8A6A4A", dy=0)]
    for i, x in enumerate((0.2, 0.5, 0.8)):
        bx, by, bw, bh = w * x, h * 0.86, w * 0.18, h * 0.32
        o.append(f'<path d="M{f(bx - bw / 2)} {f(by)} L {f(bx - bw / 2)} {f(by - bh)} L {f(bx - bw * 0.1)} {f(by - bh * 0.8)} L {f(bx + bw * 0.2)} {f(by - bh * 1.05)} L {f(bx + bw / 2)} {f(by - bh * 0.7)} L {f(bx + bw / 2)} {f(by)} Z" fill="#B8A07A" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<rect x="{f(bx - bw * 0.1)}" y="{f(by - bh * 0.4)}" width="{f(bw * 0.2)}" height="{f(bh * 0.4)}" fill="#3A2A1A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
        for j in range(5):
            o.append(f'<rect x="{f(bx + r.uniform(-bw, bw) * 0.7)}" y="{f(by - r.uniform(0, 10))}" width="{f(r.uniform(8, 18))}" height="{f(r.uniform(5, 9))}" fill="#9A8A6A" stroke="#0D0D0F" stroke-width="1"></rect>')
    return "".join(o)

def beasts_groan(w, h, seed):
    """How do the beasts groan! the herds perplexed for want of pasture, the flocks desolate on the bare ground."""
    o = [K2.sky(w, h, "#C8A880", "#F0D8B0"), hills(w, h, h * 0.5, seed, "#B89A6A", amp=12, step=110), ground(w, h, h * 0.6, "#C8A070", dy=0)]
    k = min(0.9, h / 360)
    for i in range(3): o.append(S1x.cow(w * (0.16 + i * 0.18), h * (0.84 + (i % 2) * 0.04), k * (0.7 + i * 0.05), color=("#8A6A4A", "#C9A27A", "#6A4A3A")[i], low=i == 1))
    o.append(flock(w * 0.62, w * 0.96, h * 0.72, h * 0.94, 9, seed))
    return "".join(o)

def fire_pastures(w, h, seed):
    """The fire hath devoured the pastures of the wilderness, the flame hath burned all the trees of the field; the water
    brooks dried up."""
    o = [K2.sky(w, h, "#3A1A1A", "#C8603A"), hills(w, h, h * 0.5, seed, "#5A3A2A", amp=12, step=100), ground(w, h, h * 0.62, "#6A4A2A", dy=0)]
    for i in range(5):
        o.append(E.blaze(w * (0.1 + i * 0.2), h * 0.66, w * 0.14, h * 0.26, seed + i, n=5))
    o.append(f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.82)} {f(w * 0.6)} {f(h * 0.92)} {f(w + 10)} {f(h * 0.86)}" fill="none" stroke="#8A6A4A" stroke-width="{f(max(6, h * 0.03))}"></path>'
             f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.82)} {f(w * 0.6)} {f(h * 0.92)} {f(w + 10)} {f(h * 0.86)}" fill="none" stroke="#5A3A2A" stroke-width="2" stroke-dasharray="8 6"></path>')
    o.append(smoke(w * 0.5, h * 0.36, 6, seed, color="#3A2A2A", op=0.6, k=min(1.6, h / 260)))
    return "".join(o)

def zion_trumpet(p, w, h, seed, swarm_on=True):
    """Blow ye the trumpet in Zion: a watchman on the wall of Jerusalem blowing the ram's horn, the day of darkness coming over
    the mountains as a dark dawn, a cloud of locusts behind it."""
    b = h * 0.62
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A2230", "#C86A3A"), hills(w, h, h * 0.52, seed, "#3A2A2A", amp=16, step=110)]
    if swarm_on: o.append(swarm(w, h, seed, y0=0.04, y1=0.48))
    o.append(J.city_hill(w * 0.6, h * 0.98, w * 0.5, h * 0.3, seed) + f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w * 0.36)}" height="{f(h * 0.4)}" fill="#A8906A" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    for i in range(int(w * 0.36 / 26) + 1):
        o.append(f'<rect x="{f(i * 26)}" y="{f(h * 0.59)}" width="14" height="{f(h * 0.03)}" fill="#A8906A" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    s = fit(b, b - h * 0.36)
    o.append(mk.person(p, round(w * 0.18), round(b), round(s, 3), body=SKIN, cloth="#5A4A6A", sw=3, up=J1x.TRUMPET_ARM,
                       extra=A.headcloth("#3A3A5A", cord="#2A1A10") + A.BLACK_BEARD + J1x.shofar(8, -188, 0.9, rot=-14)) + J1x.blasts(w * 0.18 + 60 * s, b - 200 * s, s))
    return "".join(o)

def army_dawn(w, h, seed, labels=True):
    """A great people and a strong, as the dawn spread upon the mountains: the dark army of locusts pouring over the ridge,
    fire before them, the garden of Eden before and a desolate wilderness behind."""
    o = [K2.sky(w, h, "#1A1220", "#8A4A3A"), hills(w, h, h * 0.42, seed, "#2A2028", amp=18, step=110)]
    o.append(f'<path d="M-10 {f(h * 0.6)} L {f(w * 0.5)} {f(h * 0.6)} L {f(w * 0.5)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="1.6"></path>'
             f'<path d="M{f(w * 0.5)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.5)} {f(h + 10)} Z" fill="#5E8F26" stroke="#0D0D0F" stroke-width="1.6"></path>')
    for i in range(8):
        o.append(tree(w * (0.56 + i * 0.06), h * 0.8 + (i % 2) * 10, min(1.0, h / 360), color="#2E6B3A", kind="round", seed=seed + i))
    o.append(swarm(w * 0.62, h, seed, y0=0.2, y1=0.9, dark=True))
    o.append(E.blaze(w * 0.58, h * 0.9, w * 0.12, h * 0.3, seed, n=5))
    if labels: o.append(label(w * 0.24, h * 0.98, "BEHIND THEM · A DESOLATE WILDERNESS", "#F3EFE6", 8) + label(w * 0.78, h * 0.98, "BEFORE THEM · AS THE GARDEN OF EDEN", "#F3EFE6", 8))
    return "".join(o)

def horses_plate(w, h):
    """The appearance of them is as the appearance of horses: the locust's head beside a war-horse's, as a plate."""
    o = [grid_bg(w, h)]
    k = min(2.6, h / 70)
    o.append(locust(w * 0.3, h * 0.6, k))
    o.append(f'<path d="M{f(w * 0.62)} {f(h * 0.8)} C {f(w * 0.6)} {f(h * 0.5)} {f(w * 0.66)} {f(h * 0.3)} {f(w * 0.74)} {f(h * 0.24)} L {f(w * 0.86)} {f(h * 0.4)} L {f(w * 0.84)} {f(h * 0.48)} L {f(w * 0.76)} {f(h * 0.44)} C {f(w * 0.72)} {f(h * 0.56)} {f(w * 0.74)} {f(h * 0.7)} {f(w * 0.76)} {f(h * 0.8)} Z" fill="none" stroke="#C8D0D8" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.74)} {f(h * 0.24)} C {f(w * 0.7)} {f(h * 0.3)} {f(w * 0.66)} {f(h * 0.4)} {f(w * 0.64)} {f(h * 0.5)}" fill="none" stroke="#C8D0D8" stroke-width="1.4" stroke-dasharray="4 4"></path>')
    o.append(label(w * 0.3, h * 0.9, "THE LOCUST", "#FFD23F", 9) + label(w * 0.74, h * 0.9, "AS THE APPEARANCE OF HORSES", CYAN, 9))
    return "".join(o)

def wall_locusts(w, h, seed):
    """They run upon the wall; they climb up into the houses; they enter in at the windows like a thief: a city wall and
    houses crawling with locusts."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#5A4A3A", "#B89A7A"), f'<rect x="-10" y="{f(h * 0.3)}" width="{f(w + 20)}" height="{f(h * 0.72)}" fill="#C8B08A" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    for i in range(int(w / 30) + 2):
        o.append(f'<rect x="{f(i * 30)}" y="{f(h * 0.26)}" width="16" height="{f(h * 0.05)}" fill="#C8B08A" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    for i in range(int(h * 0.7 / 20)):
        o.append(f'<path d="M-10 {f(h * 0.32 + i * 20)} L {f(w + 10)} {f(h * 0.32 + i * 20)}" stroke="#A8906A" stroke-width="1"></path>')
    for x in (0.2, 0.5, 0.8):
        o.append(f'<rect x="{f(w * x - 16)}" y="{f(h * 0.5)}" width="32" height="40" fill="#2A1A10" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append("".join(locust(r.uniform(0, w), r.uniform(h * 0.2, h), r.uniform(0.2, 0.36), rot=r.uniform(-80, 20)) for _ in range(int(w * h / 1400))))
    return "".join(o)

def sky_dark(w, h, seed, blood=False, smoke_=False, quake=False):
    """The sun and the moon darkened, the stars withdrawing their shining; blood=True: the moon turned into blood, the sun
    into darkness, with fire and pillars of smoke; quake=True: the earth shaking under it."""
    o = [K2.sky(w, h, "#08080F", "#2A1A2A")]
    o.append(mk.stars(30, w, h * 0.5, seed, color="#3A3A4A"))
    k = min(h / 300, w / 500)
    o.append(f'<circle cx="{f(w * 0.3)}" cy="{f(h * 0.28)}" r="{f(44 * k)}" fill="#1A1A1A" stroke="#FF8A3D" stroke-width="{f(3 * k)}"></circle>')
    o.append(f'<circle cx="{f(w * 0.72)}" cy="{f(h * 0.24)}" r="{f(32 * k)}" fill="{"#8A0E16" if blood else "#3A3A4A"}" stroke="#0D0D0F" stroke-width="2"></circle>')
    o.append(ground(w, h, h * 0.78, "#1A1218", dy=0))
    if smoke_:
        for i, x in enumerate((0.16, 0.5, 0.84)):
            o.append(E.blaze(w * x, h * 0.8, w * 0.08, h * 0.12, seed + i, n=3) + f'<path d="M{f(w * x)} {f(h * 0.7)} C {f(w * x - 20)} {f(h * 0.5)} {f(w * x + 20)} {f(h * 0.3)} {f(w * x)} -10" stroke="#5A4A5A" stroke-width="{f(max(14, w * 0.04))}" fill="none" opacity="0.7" stroke-linecap="round"></path>')
    if quake:
        o.append("".join(f'<path d="M{f(w * (0.1 + i * 0.2))} {f(h * 0.8)} l 10 10 l -8 8 l 12 10" stroke="#C8A06A" stroke-width="2" fill="none"></path>' for i in range(5)))
    return "".join(o)

def assembly(p, w, h, seed):
    """Gather the people, sanctify the assembly: old men, children, the bridegroom and the bride, all gathered before the
    house of Jehovah; the priests weeping between the porch and the altar."""
    b = h * 0.96
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#6A6A7A", "#C8B898"), temple_front(w * 0.78, h * 0.72, w * 0.36, seed), ground(w, h, h * 0.72, "#A88A6A", dy=0)]
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.58, h * 0.76, b, 22, 0.24, 0.42))
    s = fit(b, b - h * 0.28)
    for i in range(3): o.append(E.kneel(w * (0.62 + i * 0.08), b, s * 1.0, color="#6A5E4A", skin="#C98E66"))
    return "".join(o)

def army_map(w, h):
    """The northern army removed far off: driven into a land barren and desolate, its forepart into the eastern sea and its
    hinder part into the western sea, as a map."""
    o = [grid_bg(w, h),
         f'<path d="M-10 -10 L {f(w * 0.14)} -10 C {f(w * 0.18)} {f(h * 0.4)} {f(w * 0.12)} {f(h * 0.7)} {f(w * 0.08)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>',
         f'<ellipse cx="{f(w * 0.8)}" cy="{f(h * 0.7)}" rx="{f(w * 0.05)}" ry="{f(h * 0.2)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>']
    o.append(label(w * 0.06, h * 0.08, "THE WESTERN SEA", CYAN, 8, anchor="start") + label(w * 0.8, h * 0.96, "THE EASTERN SEA", CYAN, 8))
    o.append(f'<rect x="{f(w * 0.4)}" y="{f(h * 0.12)}" width="{f(w * 0.2)}" height="{f(h * 0.14)}" fill="#D7261E" fill-opacity="0.25" stroke="#D7261E" stroke-width="2"></rect>'
             + label(w * 0.5, h * 0.21, "THE NORTHERN ARMY", "#FF8A6A", 9))
    o.append(route([(w * 0.42, h * 0.26), (w * 0.2, h * 0.5)], color="#FF8A6A") + route([(w * 0.58, h * 0.26), (w * 0.76, h * 0.56)], color="#FF8A6A")
             + route([(w * 0.5, h * 0.26), (w * 0.5, h * 0.7)], color="#FF8A6A") + label(w * 0.5, h * 0.8, "A LAND BARREN AND DESOLATE", "#FF8A6A", 8))
    o.append(node(w * 0.46, h * 0.6, "ZION", "#FFD23F", r=6, dy=-12, size=9))
    return "".join(o)

def plenty(w, h, seed):
    """The floors shall be full of wheat, and the vats shall overflow with new wine and oil: a threshing-floor heaped high, the
    vats running over, the rain clouds passing."""
    o = [land(w, h, seed, tone="day", olives=2, horizon=0.36)]
    k = min(1.4, h / 260)
    o.append(S4x.threshing_floor(w * 0.32, h * 0.86, w * 0.4)
             + f'<path d="M{f(w * 0.16)} {f(h * 0.86)} C {f(w * 0.22)} {f(h * 0.6)} {f(w * 0.42)} {f(h * 0.6)} {f(w * 0.48)} {f(h * 0.86)} Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></path>')
    for i, (x, c) in enumerate(((0.68, "#7A1A3A"), (0.86, "#C8A030"))):
        o.append(f'<path d="M{f(w * x - 30 * k)} {f(h * 0.9)} L {f(w * x - 26 * k)} {f(h * 0.9 - 50 * k)} L {f(w * x + 26 * k)} {f(h * 0.9 - 50 * k)} L {f(w * x + 30 * k)} {f(h * 0.9)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<ellipse cx="{f(w * x)}" cy="{f(h * 0.9 - 50 * k)}" rx="{f(26 * k)}" ry="{f(6 * k)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
                 f'<path d="M{f(w * x + 24 * k)} {f(h * 0.9 - 50 * k)} C {f(w * x + 34 * k)} {f(h * 0.9 - 30 * k)} {f(w * x + 30 * k)} {f(h * 0.9 - 10 * k)} {f(w * x + 36 * k)} {f(h * 0.92)}" fill="none" stroke="{c}" stroke-width="{f(4 * k)}"></path>')
    return "".join(o)

def spirit(p, w, h, seed):
    """I will pour out my Spirit upon all flesh: light coming down from above upon old men and young men, sons and daughters,
    servants and handmaids."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A3A6A", "#E8C8A0"), V.rays(w * 0.5, -h * 0.2, 40, 20, h * 1.4, color="#FFF4C2", op=0.3),
         ground(w, h, h * 0.72, "#B89A6A", dy=0)]
    s = fit(b, b - h * 0.42)
    cast = [("elder", 0.1), ("man", 0.24), ("son", 0.36), ("woman", 0.48), ("girl", 0.6), ("man2", 0.74), ("woman2", 0.88)]
    for kind, x in cast:
        X = w * x
        if kind == "elder": o.append(A.elder("#8A7A6A", 2)(p, X, b, s, up=[(-22, -158), (-34, -190), (-30, -220)]))
        elif kind == "man": o.append(man(p, X, b, s, "#5A6A8A", up=[(-22, -158), (-34, -190), (-30, -220)]))
        elif kind == "son": o.append(child_fig(p, X, b, s * 0.7, "#C8BCA6"))
        elif kind == "woman": o.append(woman(p, X, b, s * 0.94, "#7A3A5A"))
        elif kind == "girl": o.append(woman(p, X, b, s * 0.7, "#3A7A6A"))
        elif kind == "man2": o.append(man(p, X, b, s, "#6A5A3A"))
        else: o.append(woman(p, X, b, s * 0.92, "#8A7A5A", up=[(-22, -152), (-34, -184), (-30, -212)]))
    return "".join(o)

NATIONS = {"TYRE": (0.26, 0.3), "SIDON": (0.38, 0.14), "PHILISTIA": (0.2, 0.62), "JERUSALEM": (0.44, 0.5), "THE VALLEY OF JEHOSHAPHAT": (0.6, 0.66),
           "THE GRECIANS": (0.04, 0.3), "SHEBA": (0.86, 0.94), "EGYPT": (0.12, 0.94), "EDOM": (0.6, 0.86), "SHITTIM": (0.82, 0.5)}
def nations_map(w, h, show, moves=(), hi=(), title=""):
    """The land with the nations about it, as a technical map; moves = [(from, to)] as arrows; hi = places lit red."""
    o = [grid_bg(w, h),
         f'<path d="M-10 -10 L {f(w * 0.18)} -10 C {f(w * 0.24)} {f(h * 0.4)} {f(w * 0.16)} {f(h * 0.7)} {f(w * 0.12)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.72)} -10 C {f(w * 0.7)} {f(h * 0.3)} {f(w * 0.74)} {f(h * 0.5)} {f(w * 0.7)} {f(h * 0.62)}" stroke="#2C9DB8" stroke-width="4" fill="none"></path>'
         f'<ellipse cx="{f(w * 0.7)}" cy="{f(h * 0.76)}" rx="{f(w * 0.03)}" ry="{f(h * 0.14)}" fill="#2C9DB8"></ellipse>']
    for nm in show:
        x, y = NATIONS[nm]
        o.append(node(w * x, h * y, nm, "#FF8A6A" if nm in hi else "#FFD23F", r=6, dy=-12 if y > 0.1 else 18, size=9, anchor="start" if x < 0.1 else "middle"))
    for a, b2 in moves:
        (x0, y0), (x1, y1) = NATIONS[a], NATIONS[b2]
        o.append(route([(w * x0, h * y0), (w * x1, h * y1)], color="#FF8A6A"))
    if title: o.append(label(w * 0.96, h * 0.08, title, "#F3EFE6", 9, anchor="end"))
    return "".join(o)

def valley(w, h, seed, crowds=True, light=False):
    """The valley of Jehoshaphat, the valley of decision: steep sides, its floor filled with multitudes, the sky darkened."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#1A1220" if not light else "#8FD0E2", "#5A3A4A" if not light else "#F3E8C8"),
         f'<path d="M-10 {f(h * 0.3)} L {f(w * 0.3)} {f(h * 0.7)} L {f(w * 0.7)} {f(h * 0.7)} L {f(w + 10)} {f(h * 0.26)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#4A3A3A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.24)} {f(h * 0.66)} L {f(w * 0.76)} {f(h * 0.66)} L {f(w * 0.9)} {f(h + 10)} L {f(w * 0.1)} {f(h + 10)} Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="1.6"></path>']
    if crowds:
        for i in range(int(w * h / 220)):
            y = r.uniform(h * 0.68, h); x = w * 0.5 + r.uniform(-1, 1) * (w * 0.26 + (y - h * 0.66) * 0.5)
            hh = 3 + (y - h * 0.66) / h * 18
            o.append(f'<rect x="{f(x)}" y="{f(y - hh * 2)}" width="{f(hh * 0.7)}" height="{f(hh * 2)}" rx="{f(hh * 0.3)}" fill="{r.choice(("#2A2228", "#3A2A2A", "#4A3A3A", "#2A2A3A"))}"></rect>')
    return "".join(o)

def plowshares(w, h):
    """Beat your plowshares into swords, and your pruning-hooks into spears: a plate, each tool beside what it becomes."""
    o = [grid_bg(w, h)]
    k = min(1.6, h / 140)
    cy = h * 0.5
    o.append(f'<path d="M{f(w * 0.1)} {f(cy + 20 * k)} L {f(w * 0.1 + 50 * k)} {f(cy - 10 * k)} L {f(w * 0.1 + 70 * k)} {f(cy + 20 * k)} Z" fill="#8A9AA8" fill-opacity="0.4" stroke="#C8D0D8" stroke-width="2"></path>'
             + route([(w * 0.24, cy), (w * 0.3, cy)], color="#FF8A6A")
             + f'<path d="M{f(w * 0.33)} {f(cy)} L {f(w * 0.45)} {f(cy)} L {f(w * 0.47)} {f(cy - 4 * k)} L {f(w * 0.45)} {f(cy - 8 * k)} L {f(w * 0.33)} {f(cy - 8 * k)} Z" fill="#C8D0D8" stroke="#0D0D0F" stroke-width="1.4"></path>'
             + f'<rect x="{f(w * 0.31)}" y="{f(cy - 14 * k)}" width="{f(4 * k)}" height="{f(20 * k)}" fill="#C8963E"></rect>')
    o.append(f'<path d="M{f(w * 0.58)} {f(cy + 20 * k)} L {f(w * 0.58)} {f(cy - 10 * k)} C {f(w * 0.58)} {f(cy - 30 * k)} {f(w * 0.62)} {f(cy - 30 * k)} {f(w * 0.63)} {f(cy - 16 * k)}" fill="none" stroke="#C8D0D8" stroke-width="3"></path>'
             + route([(w * 0.68, cy), (w * 0.74, cy)], color="#FF8A6A")
             + f'<path d="M{f(w * 0.77)} {f(cy)} L {f(w * 0.94)} {f(cy)}" stroke="#8A6A3A" stroke-width="3"></path><path d="M{f(w * 0.94)} {f(cy - 6 * k)} L {f(w * 0.98)} {f(cy)} L {f(w * 0.94)} {f(cy + 6 * k)} Z" fill="#C8D0D8" stroke="#0D0D0F" stroke-width="1.2"></path>')
    o.append(label(w * 0.2, h * 0.86, "PLOWSHARES → SWORDS", "#FFD23F", 9) + label(w * 0.76, h * 0.86, "PRUNING-HOOKS → SPEARS", "#FFD23F", 9))
    return "".join(o)

def sickle_press(w, h, seed):
    """Put ye in the sickle; for the harvest is ripe: come, tread ye; for the winepress is full: ripe grain standing and a
    winepress brimming dark under a red sky."""
    o = [K2.sky(w, h, "#3A1A2A", "#C86A3A"), ground(w, h, h * 0.58, "#8A6A4A", dy=0)]
    import ruth1 as R1x
    o.append(R1x.field(-10, w * 0.56, h * 0.86, h * 0.3, seed, rows=3))
    o.append(J1y.winepress(w * 0.78, h * 0.8, w * 0.3, h * 0.18) + f'<ellipse cx="{f(w * 0.78)}" cy="{f(h * 0.82)}" rx="{f(w * 0.13)}" ry="{f(h * 0.06)}" fill="#4A0A1A"></ellipse>')
    k = min(1.4, h / 240)
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.4)} C {f(w * 0.3 + 40 * k)} {f(h * 0.4 - 30 * k)} {f(w * 0.3 + 70 * k)} {f(h * 0.4)} {f(w * 0.3 + 60 * k)} {f(h * 0.4 + 26 * k)}" fill="none" stroke="#C8D0D8" stroke-width="{f(5 * k)}"></path>'
             f'<path d="M{f(w * 0.3)} {f(h * 0.4)} L {f(w * 0.3 - 30 * k)} {f(h * 0.4 + 30 * k)}" stroke="#8A6A3A" stroke-width="{f(6 * k)}" stroke-linecap="round"></path>')
    return "".join(o)

def zion_refuge(w, h, seed):
    """Jehovah will roar from Zion: Jerusalem on its hill, rings of sound going out over the shaking heavens and earth, and a
    light over the city — a refuge unto his people."""
    o = [K2.sky(w, h, "#2A2A4A", "#8A6A7A"), V.rays(w * 0.5, h * 0.4, 30, 20, w * 0.7, color="#FFF4C2", op=0.2),
         J.city_hill(w * 0.5, h * 0.9, w * 0.36, h * 0.4, seed), ground(w, h, h * 0.9, "#3A3030", dy=0)]
    for i in range(4):
        o.append(f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.5)}" r="{f(w * (0.14 + i * 0.1))}" fill="none" stroke="#FFD23F" stroke-width="1.6" opacity="{0.6 - i * 0.12}"></circle>')
    o.append("".join(f'<path d="M{f(w * (0.04 + i * 0.16))} {f(h * 0.92)} l 8 8 l -6 6 l 10 8" stroke="#C8A06A" stroke-width="2" fill="none"></path>' for i in range(6)))
    return "".join(o)

def sweet_wine(w, h, seed):
    """The mountains shall drop down sweet wine, the hills shall flow with milk, the brooks of Judah shall flow with waters, and
    a fountain shall come forth from the house of Jehovah and water the valley of Shittim."""
    o = [K2.sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.86, h * 0.16, max(10, h * 0.04), color="#FFE680", op=0.3)]
    o.append(f'<path d="M-10 {f(h * 0.6)} L {f(w * 0.2)} {f(h * 0.28)} L {f(w * 0.42)} {f(h * 0.6)} Z" fill="#5E8F26" stroke="#0D0D0F" stroke-width="2"></path>'
             + vine_rows(w * 0.42, h, h * 0.4, h * 0.6, seed, rows=2, grapes=True))
    o.append(hills(w, h, h * 0.56, seed, "#9CCB5E", amp=10, step=90) + ground(w, h, h * 0.66, "#8AB84A", dy=0))
    o.append(temple_front(w * 0.6, h * 0.58, w * 0.18, seed))
    o.append(f'<path d="M{f(w * 0.6)} {f(h * 0.58)} C {f(w * 0.62)} {f(h * 0.7)} {f(w * 0.74)} {f(h * 0.76)} {f(w * 0.82)} {f(h * 0.9)} L {f(w + 10)} {f(h * 0.96)}" fill="none" stroke="#2C9DB8" stroke-width="{f(max(6, h * 0.025))}" stroke-linecap="round"></path>')
    o.append(flock(w * 0.06, w * 0.4, h * 0.74, h * 0.94, 8, seed))
    o.append(label(w * 0.9, h * 0.86, "SHITTIM", "#1F4A34", 9))
    return "".join(o)
