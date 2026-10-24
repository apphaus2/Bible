"""Drawings for Matthew 5–7, the sermon on the mount: Jesus seated on the mountain with the disciples and the multitudes, and
the sayings drawn as their own small scenes (salt, the city on a hill and the lamp on the stand, the gift left before the
altar, the second mile, the sun and the rain, the inner chamber, the field of bread, treasures and moth and rust, the birds
of the heaven and the lilies of the field, the narrow gate, the trees and their fruits, the houses on the rock and on the
sand). Built on mat.art."""
from mat.art import *
from mat.art import f, INK, HEB, TWELVE, JOSEPH_C
from ntcast import JESUS_SKIN, JESUS_HAIR, JESUS_TUNIC, JESUS_MANTLE
import random, math
from job.art import seated
from ecc.art import dog, loaf
from hos.art import lily
from lev.art3 import creature
from samuel1 import cow
import exodus as E

def jesus_seated(x, y, s, flip=False, glow_=True):
    """Jesus sitting on the ground or a rock (job.art.seated in his colours): his hair falling behind to the shoulders, his
    beard, the undyed robe and the blue-grey mantle over the shoulder; (x, y) the ground under him."""
    g = seated(x, y, s, JESUS_TUNIC, head=JESUS_HAIR, beard=JESUS_HAIR, flip=flip).replace(SKIN, JESUS_SKIN)
    mantle = (f'<path d="M-28 -92 C -16 -96 0 -96 6 -92 C 2 -70 -6 -40 -14 -2 L -34 -2 C -30 -40 -30 -70 -28 -92 Z" fill="{JESUS_MANTLE}" stroke="#0D0D0F" stroke-width="2.2"></path>')
    g = g[:-4] + mantle + "</g>"
    halo = f'<circle cx="{f(x)}" cy="{f(y - 90 * s)}" r="{f(80 * s)}" fill="#FFE680" opacity="0.2"></circle>' if glow_ else ""
    return halo + g

def disciple_seated(x, y, s, i, flip=False):
    """One of the disciples sitting on the grass, in his colour (bare-headed, bearded)."""
    beard = ["#4A4440", None, "#1A1210", None, "#1A1210", "#2A1A10", "#1A1210", "#3A2A1A", "#2A1A10", None, "#5A4A3A", "#3A2A1A"][i % 12]
    return seated(x, y, s, TWELVE[i % 12], head=None, beard=beard or "", flip=flip)

def soldier_fig(p, x, y, s, flip=False, up=None, pack=False):
    """A Roman soldier at a distance: red tunic, a brass helmet with a crest, a short sword at the side."""
    helm = ('<path d="M-14 -190 C -14 -206 14 -206 14 -190 L 14 -180 L -14 -180 Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M-10 -204 C -4 -214 6 -214 12 -204" stroke="#B5121B" stroke-width="5" fill="none"></path>'
            '<path d="M-24 -150 L 24 -150 L 22 -110 L -22 -110 Z" fill="#9A8A6A" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M24 -100 L 40 -60" stroke="#5A4A3A" stroke-width="5"></path>')
    if pack: helm += '<rect x="-34" y="-176" width="20" height="40" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="1.6"></rect>'
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#A8281E", kind="Tunic", sw=3, flip=flip, up=up, extra=helm)

def mount_teach(p, w, h, seed, astonished=False):
    """He went up into the mountain, and when he had sat down his disciples came unto him: the green slope above the lake,
    Jesus seated on a rock, the twelve seated on the grass before him, the multitudes coming up the hill behind
    (astonished=True: the crowd standing, hands raised)."""
    b = h * 0.96
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.86, h * 0.12, 14, color="#FFE680", op=0.25),
         hills(w, h, h * 0.3, seed, color="#7A8A9A", amp=10, step=90), lake(w, h, h * 0.36, seed, n=8),
         f'<path d="M-10 {f(h * 0.42)} C {f(w * 0.2)} {f(h * 0.32)} {f(w * 0.5)} {f(h * 0.4)} {f(w + 10)} {f(h * 0.56)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8AB84A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.3, b - 220))
    jx, jy = w * 0.22, h * 0.6
    o.append(f'<path d="M{f(jx - 60 * s)} {f(jy + 4)} C {f(jx - 50 * s)} {f(jy - 30 * s)} {f(jx + 50 * s)} {f(jy - 34 * s)} {f(jx + 64 * s)} {f(jy + 4)} Z" fill="#9A8A7A" stroke="{INK}" stroke-width="2"></path>')
    o.append(jesus_seated(jx, jy - 22 * s, s * 0.82))
    r = random.Random(seed)
    spots = [(0.38, 0.72), (0.5, 0.7), (0.62, 0.74), (0.44, 0.84), (0.56, 0.86), (0.7, 0.84), (0.34, 0.94), (0.48, 0.97), (0.64, 0.98), (0.8, 0.96)]
    for i, (x, y) in enumerate(spots):
        k = 0.7 + 0.5 * (y - 0.7) / 0.3
        o.append(disciple_seated(w * x, h * y, s * 0.62 * k, i, flip=True))
    if astonished:
        o.append(crowd(p, w * 0.72, w * 0.98, h * 0.66, h * 0.66 - 90 * s, 6, seed, flip=True, up=[(-22, -158), (-30, -180), (-24, -206)]))
    else:
        o.append(crowd(p, w * 0.76, w * 0.98, h * 0.66, h * 0.66 - 80 * s, 5, seed, flip=True))
    return "".join(o)

def hillside(p, w, h, seed):
    """The multitudes sitting on the grass of the hillside, listening; the lake below, the hills of Galilee across it."""
    b = h * 0.98
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.24, seed, color="#7A8A9A", amp=10, step=90), lake(w, h, h * 0.3, seed, n=6),
         f'<path d="M-10 {f(h * 0.4)} C {f(w * 0.3)} {f(h * 0.34)} {f(w * 0.7)} {f(h * 0.42)} {f(w + 10)} {f(h * 0.38)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8AB84A" stroke="{INK}" stroke-width="2"></path>']
    r = random.Random(seed)
    for _ in range(14):
        x = r.uniform(0, w); y = r.uniform(h * 0.45, h * 0.95)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="2.4" fill="{r.choice(["#F3EFE6", "#D7261E", "#FFD23F"])}"></circle>')
    s = fit(b, max(h * 0.3, b - 200)) * 0.62
    items = sorted((r.uniform(h * 0.46, h * 0.98), r.uniform(0.02, 0.98) * w) for _ in range(16))
    for y, x in items:
        k = 0.55 + 0.45 * (y - h * 0.46) / (h * 0.52)
        c = r.choice(HEB)
        o.append(seated(x, y, s * k, c, head=r.choice([c, "#E8E2D6", "#6A5A3A", None]), beard=r.choice(["#2A1A10", "#6A645E", ""]), flip=True))
    return "".join(o)

def salt(p, w, h, seed):
    """If the salt have lost its savor: white salt spilt from a broken jar on the road, trodden under foot — sandal-prints
    across it."""
    b = h * 0.9
    r = random.Random(seed)
    o = [sky(w, h, "#C8D8E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, color="#B8A88A", amp=10, step=90), ground(w, h, h * 0.46, "#C8A878", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.46)} {f(h * 0.46)} L {f(w * 0.56)} {f(h * 0.46)} L {f(w * 0.9)} {f(h + 10)} Z" fill="#B89870" stroke="{INK}" stroke-width="1.6"></path>',
         f'<ellipse cx="{f(w * 0.56)}" cy="{f(h * 0.8)}" rx="{f(w * 0.16)}" ry="{f(h * 0.08)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></ellipse>']
    for _ in range(50):
        o.append(f'<circle cx="{f(w * 0.56 + r.uniform(-w * 0.15, w * 0.15))}" cy="{f(h * 0.8 + r.uniform(-h * 0.07, h * 0.07))}" r="1.4" fill="#C8C0B8"></circle>')
    for k in range(5):                                      # sandal prints over the salt
        x = w * (0.46 + 0.05 * k); y = h * (0.88 - 0.05 * k)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(h * 0.022)}" ry="{f(h * 0.045)}" fill="#8A6A4A" opacity="0.6" transform="rotate(-30 {f(x)} {f(y)})"></ellipse>')
    jx, jy, js = w * 0.3, h * 0.82, h / 220
    o.append(f'<g transform="translate({f(jx)} {f(jy)}) rotate(-70) scale({f(js)})"><path d="M-22 0 C -30 -20 -24 -44 -10 -50 L -12 -60 L 12 -60 L 10 -50 C 24 -44 30 -20 22 0 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-20 -14 L -4 -24 L 6 -10 L 22 -20" stroke="#0D0D0F" stroke-width="2" fill="none"></path></g>')
    return "".join(o)

def city_light(p, w, h, seed):
    """A city set on a hill cannot be hid: a walled city on its hill at night, every window lit; and in a house in front,
    a lamp burning on its stand, the bushel set aside."""
    o = [night(w, h, seed, n=60, top="#05051A", bot="#2A2050"), hills(w, h, h * 0.6, seed, color="#1E1838", amp=14, step=80),
         f'<path d="M{f(w * 0.3)} {f(h * 0.72)} C {f(w * 0.42)} {f(h * 0.3)} {f(w * 0.74)} {f(h * 0.3)} {f(w * 0.86)} {f(h * 0.72)} Z" fill="#2A2238" stroke="{INK}" stroke-width="2"></path>',
         glow(w * 0.58, h * 0.38, h * 0.36, "#FFE680", 0.45, f"{p}c"),
         walls(w * 0.42, w * 0.74, h * 0.5, h * 0.2, seed, lit=True, towers=3, color="#8A7A6A"), ground(w, h, h * 0.74, "#14102A", dy=0)]
    lx, ly, ls = w * 0.14, h * 0.96, h / 300
    o.append(f'<path d="M{f(lx)} {f(ly)} L {f(lx)} {f(ly - 120 * ls)}" stroke="#6A4A2A" stroke-width="{f(6 * ls)}"></path>'
             f'<path d="M{f(lx - 22 * ls)} {f(ly)} L {f(lx + 22 * ls)} {f(ly)}" stroke="#6A4A2A" stroke-width="{f(6 * ls)}"></path>'
             + glow(lx, ly - 130 * ls, 90 * ls, "#FFE680", 0.8, f"{p}l") + A.lamp(lx, ly - 126 * ls, ls))
    bx = w * 0.26                                           # the bushel, set aside, upturned
    o.append(f'<path d="M{f(bx - 20 * ls)} {f(ly)} L {f(bx - 16 * ls)} {f(ly - 34 * ls)} L {f(bx + 16 * ls)} {f(ly - 34 * ls)} L {f(bx + 20 * ls)} {f(ly)} Z" fill="#8A6A3A" stroke="{INK}" stroke-width="2"></path>')
    return "".join(o)

def law_scroll(p, w, h, seed):
    """Till heaven and earth pass away, one jot or one tittle shall in no wise pass away from the law: the scroll of the
    law open on its rollers, every small mark of its writing lit gold."""
    r = random.Random(seed)
    o = [bgr(w, h, "#1A1630"), glow(w * 0.5, h * 0.5, max(w, h) * 0.5, "#FFE680", 0.35, f"{p}g")]
    sw, sh = min(w * 0.8, h * 1.8), min(h * 0.7, w * 0.4)
    x0, y0 = w * 0.5 - sw / 2, h * 0.5 - sh / 2
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(sw)}" height="{f(sh)}" fill="#F3E8C8" stroke="{INK}" stroke-width="2.4"></rect>')
    for side in (0, 1):
        cx = x0 + side * sw
        o.append(f'<rect x="{f(cx - 12)}" y="{f(y0 - 10)}" width="24" height="{f(sh + 20)}" rx="10" fill="#C8A878" stroke="{INK}" stroke-width="2.2"></rect>')
    cols = 3
    for c in range(cols):
        cx0 = x0 + 24 + c * (sw - 48) / cols
        for k in range(7):
            yy = y0 + sh * (k + 1) / 8
            xx = cx0
            while xx < cx0 + (sw - 48) / cols - 16:
                ww = r.uniform(4, 12)
                o.append(f'<rect x="{f(xx)}" y="{f(yy - 3)}" width="{f(ww)}" height="5" fill="#3A2A1A"></rect>')
                if r.random() < 0.18: o.append(f'<circle cx="{f(xx + ww / 2)}" cy="{f(yy - 7)}" r="1.6" fill="#E8B830"></circle>')
                xx += ww + r.uniform(3, 6)
    return "".join(o)

def altar_gift(p, w, h, seed):
    """Leave there thy gift before the altar, and go thy way, first be reconciled to thy brother: the great altar in the
    temple court, smoke rising; a lamb left tied before it; the man going out the gate to find his brother."""
    from kg1.art import horned_altar
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#E8D8B8", "#F3E8C8"), pavement(w, h, h * 0.66),
         f'<rect x="{f(w * 0.62)}" y="{f(h * 0.2)}" width="{f(w * 0.36)}" height="{f(h * 0.46)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.74)} {f(h * 0.66)} L {f(w * 0.74)} {f(h * 0.36)} Q {f(w * 0.8)} {f(h * 0.28)} {f(w * 0.86)} {f(h * 0.36)} L {f(w * 0.86)} {f(h * 0.66)} Z" fill="#5A4A3A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.24, b - 220))
    ax = w * 0.24
    o.append(E.blaze(ax, b - 98 * s * 0.9, 50 * s, 60 * s, seed, n=5))
    o.append(horned_altar(ax, b, s * 0.9))
    o.append(E.sheep(ax + 120 * s, b, s * 0.5, flip=True))
    o.append(man(p, w * 0.8, h * 0.66 + 4, s * 0.7, "#6A4A3A"))
    return "".join(o)

def prison_door(p, w, h, seed):
    """Thou shalt by no means come out thence, till thou have paid the last farthing: a prison door of iron bars in a stone
    wall, dark within; a single small copper coin on the step."""
    r = random.Random(seed)
    o = [bgr(w, h, "#5A5048")]
    for k in range(9):
        y = h * k / 8
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#3A322C" stroke-width="2"></path>')
        for m in range(8):
            x = w * (m + (0.5 if k % 2 else 0)) / 7
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y + h / 8)}" stroke="#3A322C" stroke-width="2"></path>')
    dx0, dx1, dy0 = w * 0.36, w * 0.64, h * 0.12
    o.append(f'<rect x="{f(dx0)}" y="{f(dy0)}" width="{f(dx1 - dx0)}" height="{f(h * 0.8)}" fill="#0D0A0C" stroke="{INK}" stroke-width="3"></rect>')
    for k in range(7):
        x = dx0 + (dx1 - dx0) * (k + 0.5) / 7
        o.append(f'<rect x="{f(x - 4)}" y="{f(dy0)}" width="8" height="{f(h * 0.8)}" fill="#6A6A72" stroke="{INK}" stroke-width="1.4"></rect>')
    for yy in (0.3, 0.6):
        o.append(f'<rect x="{f(dx0)}" y="{f(h * yy)}" width="{f(dx1 - dx0)}" height="8" fill="#6A6A72" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.92)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A322C" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<circle cx="{f(w * 0.72)}" cy="{f(h * 0.9)}" r="{f(max(6, h * 0.025))}" fill="#C8783A" stroke="{INK}" stroke-width="1.6"></circle>')
    return "".join(o)

def oaths(p, w, h, seed):
    """Neither by the heaven, for it is the throne of God; nor by the earth, for it is the footstool of his feet; nor by
    Jerusalem, the city of the great King: the heavens one blaze of light above (no form in it), the earth below, and
    Jerusalem on her hill."""
    o = [sky(w, h, "#FFE680", "#8FD0E2"), rays(w * 0.5, -h * 0.2, 40, h * 0.1, h * 1.2, color="#FFFDF0", op=0.35, a0=10, a1=170),
         clouds(w, h * 0.3, seed, n=5, color="#FFFFFF", op=0.6, h=h),
         hills(w, h, h * 0.66, seed, color="#8A9A6A", amp=12, step=80)]
    o.append(f'<path d="M{f(w * 0.36)} {f(h * 0.82)} C {f(w * 0.44)} {f(h * 0.56)} {f(w * 0.66)} {f(h * 0.56)} {f(w * 0.74)} {f(h * 0.82)} Z" fill="#B89A6A" stroke="{INK}" stroke-width="2"></path>')
    o.append(walls(w * 0.42, w * 0.68, h * 0.76, h * 0.16, seed, towers=3) + temple(w * 0.58, h * 0.63, w * 0.12))
    o.append(ground(w, h, h * 0.82, "#9AAA5A", dy=0))
    return "".join(o)

def two_miles(p, w, h, seed):
    """Whosoever shall compel thee to go one mile, go with him two: a Roman road over the hills, a milestone, a soldier
    walking on and a man of the land carrying his pack beside him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#A89A6A", amp=14, step=90), ground(w, h, h * 0.52, "#C8B07A", dy=0),
         f'<path d="M-10 {f(h * 0.96)} C {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.6)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.54)} L {f(w + 10)} {f(h * 0.6)} C {f(w * 0.6)} {f(h * 0.7)} {f(w * 0.3)} {f(h * 0.94)} -10 {f(h + 10)} Z" fill="#B8A890" stroke="{INK}" stroke-width="1.6"></path>']
    s = fit(b, max(h * 0.3, b - 220))
    mx = w * 0.16
    o.append(f'<path d="M{f(mx - 14 * s)} {f(b)} L {f(mx - 12 * s)} {f(b - 70 * s)} C {f(mx - 10 * s)} {f(b - 84 * s)} {f(mx + 10 * s)} {f(b - 84 * s)} {f(mx + 12 * s)} {f(b - 70 * s)} L {f(mx + 14 * s)} {f(b)} Z" fill="#D8D0C0" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(mx - 5 * s)} {f(b - 56 * s)} L {f(mx - 5 * s)} {f(b - 36 * s)} M{f(mx + 5 * s)} {f(b - 56 * s)} L {f(mx + 5 * s)} {f(b - 36 * s)}" stroke="#3A322C" stroke-width="{f(3 * s)}"></path>')
    o.append(soldier_fig(p, w * 0.56, b - 6, s * 0.92))
    o.append(man(p, w * 0.44, b, s * 0.9, "#6A5A3A", up=[(-22, -158), (-20, -186), (-4, -200)],
                 extra='<rect x="-26" y="-226" width="44" height="28" rx="6" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2"></rect>'))
    return "".join(o)

def sun_rain(p, w, h, seed):
    """He maketh his sun to rise on the evil and the good, and sendeth rain on the just and the unjust: one field, the sun
    rising over the left half and the rain falling on the right, two farmsteads alike under both."""
    o = [sky(w, h, "#FFC890", "#F3E8C8"),
         f'<rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#7A8A9A"></rect>',
         sun(w * 0.2, h * 0.32, max(12, h * 0.07), color="#FFE680", op=0.4),
         f'<path d="M{f(w * 0.5)} {f(h * 0.06)} C {f(w * 0.6)} -10 {f(w * 0.9)} -10 {f(w + 10)} {f(h * 0.08)} L {f(w + 10)} {f(h * 0.22)} C {f(w * 0.8)} {f(h * 0.26)} {f(w * 0.6)} {f(h * 0.2)} {f(w * 0.5)} {f(h * 0.24)} Z" fill="#4A5A6A" stroke="{INK}" stroke-width="2"></path>',
         hills(w, h, h * 0.56, seed, color="#7A9A5A", amp=10, step=80), ground(w, h, h * 0.66, "#9AAA5A", dy=0),
         grain(-10, w + 10, h * 0.98, h * 0.2, seed)]
    r = random.Random(seed)
    o.append("".join(f'<path d="M{f(x)} {f(y)} l -5 18" stroke="#CFE0F2" stroke-width="1.6" opacity="0.8"></path>'
                     for x, y in ((r.uniform(w * 0.52, w), r.uniform(h * 0.22, h * 0.9)) for _ in range(50))))
    from job.art import house
    o.append(house(w * 0.24, h * 0.7, w * 0.12, h * 0.14) + house(w * 0.74, h * 0.7, w * 0.12, h * 0.14))
    o.append(f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="{INK}" stroke-width="1.4" stroke-dasharray="6 6" opacity="0.4"></path>')
    return "".join(o)

def trumpet_street(p, w, h, seed):
    """Sound not a trumpet before thee, as the hypocrites do in the streets: a corner of a street, a man in a fine robe
    giving alms with a trumpeter blowing before him, a beggar seated by the wall."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.86, seed, hmin=0.4, hmax=0.6, stairs=False), pavement(w, h, h * 0.86)]
    s = fit(b, max(h * 0.24, b - 220))
    o.append(man(p, w * 0.42, b, s, "#7A2A6A", kind="Robe", up=UP_BLESS, extra=A.headcloth("#E8E2D6", cord="#E8B830") + A.BLACK_BEARD))
    horn = '<path d="M20 -168 L 70 -186 L 74 -170 L 22 -160 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
    o.append(man(p, w * 0.58, b, s * 0.94, "#3A4A6A", up=[(22, -158), (30, -166), (24, -166)], extra=horn))
    o.append(seated(w * 0.18, b, s * 0.8, "#6A5A4A", head="#8A7A6A", beard="#4A3A2A"))
    return "".join(o)

def inner_chamber(p, w, h, seed):
    """Enter into thine inner chamber, and having shut thy door, pray: a small room with the door shut and barred, a lamp,
    a man kneeling alone."""
    b = h * 0.92
    o = [room(w, h, b, wall="#6A5048", floor="#4A3A30"),
         f'<rect x="{f(w * 0.72)}" y="{f(b - h * 0.6)}" width="{f(w * 0.16)}" height="{f(h * 0.6)}" fill="#5A3A22" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.7)} {f(b - h * 0.32)} L {f(w * 0.9)} {f(b - h * 0.32)}" stroke="#2A1A10" stroke-width="5"></path>',
         glow(w * 0.4, b - h * 0.3, h * 0.5, "#FFE680", 0.5, f"{p}g"), A.lamp(w * 0.56, b - h * 0.3, max(0.7, h / 280))]
    s = fit(b, max(h * 0.2, b - 220))
    o.append(E.kneel(w * 0.36, b, s * 0.9, color="#6A5A3A", skin=SKIN))
    return "".join(o)

def prayer_field(p, w, h, seed):
    """Give us this day our daily bread: a field of ripe wheat at sunrise under the open heaven, a loaf and a jug set on a
    cloth at its edge."""
    o = [sky(w, h, "#3A3A7A", "#FFC890"), sun(w * 0.5, h * 0.62, max(14, h * 0.08), color="#FFE680", op=0.5),
         hills(w, h, h * 0.6, seed, color="#6A5A6A", amp=10, step=90), ground(w, h, h * 0.66, "#C8A060", dy=0),
         grain(-10, w + 10, h * 0.8, h * 0.14, seed), grain(-10, w + 10, h * 0.98, h * 0.18, seed + 1)]
    return "".join(o)

def treasures(p, w, h, seed):
    """Where moth and rust consume, and where thieves break through and steal: a chest broken open in a dark store-room,
    moth-eaten garments, rusted vessels, a hole dug through the mud-brick wall."""
    r = random.Random(seed); b = h * 0.92
    o = [bgr(w, h, "#4A3A30")]
    for k in range(7):
        y = h * k / 6
        for m in range(9):
            x = w * (m + (0.5 if k % 2 else 0)) / 8
            o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w / 8 - 4)}" height="{f(h / 6 - 4)}" fill="#6A5040" stroke="#3A2A20" stroke-width="1.4"></rect>')
    hx, hy = w * 0.8, h * 0.5
    o.append(f'<path d="M{f(hx - w * 0.08)} {f(hy)} C {f(hx - w * 0.08)} {f(hy - h * 0.3)} {f(hx + w * 0.08)} {f(hy - h * 0.3)} {f(hx + w * 0.08)} {f(hy)} L {f(hx + w * 0.08)} {f(hy + h * 0.2)} L {f(hx - w * 0.08)} {f(hy + h * 0.2)} Z" fill="#0B0B1A" stroke="{INK}" stroke-width="2"></path>')
    o.append(mk.stars(5, w * 0.12, h * 0.3, seed).replace("<g ", f'<g transform="translate({f(hx - w * 0.06)} {f(hy - h * 0.24)})" ', 1))
    for _ in range(8):
        x = hx + r.uniform(-w * 0.12, w * 0.12); y = hy + h * 0.28 + r.uniform(-6, 6)
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.02)}" height="{f(h * 0.03)}" fill="#6A5040" stroke="#3A2A20" stroke-width="1"></rect>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A2A20" stroke="{INK}" stroke-width="2"></rect>')
    cx, cw, ch = w * 0.32, w * 0.3, h * 0.24
    o.append(f'<rect x="{f(cx - cw / 2)}" y="{f(b - ch)}" width="{f(cw)}" height="{f(ch)}" fill="#7A5A30" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(cx - cw / 2)} {f(b - ch)} L {f(cx - cw / 2 + 20)} {f(b - ch * 1.9)} L {f(cx + cw / 2 + 20)} {f(b - ch * 1.9)} L {f(cx + cw / 2)} {f(b - ch)} Z" fill="#8A6A3A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(cx - cw * 0.4)} {f(b - ch)} C {f(cx - cw * 0.3)} {f(b - ch * 1.3)} {f(cx)} {f(b - ch * 1.2)} {f(cx + cw * 0.3)} {f(b - ch * 1.25)} L {f(cx + cw * 0.4)} {f(b - ch)} Z" fill="#7A2A5A" stroke="{INK}" stroke-width="1.8"></path>')
    for _ in range(10):                                     # moth holes
        o.append(f'<circle cx="{f(cx + r.uniform(-cw * 0.3, cw * 0.3))}" cy="{f(b - ch * r.uniform(1.04, 1.18))}" r="{f(r.uniform(2, 4))}" fill="#3A2A20"></circle>')
    for k in range(3):                                      # rusted vessels
        x = w * (0.08 + k * 0.06)
        o.append(f'<path d="M{f(x - 12)} {f(b)} C {f(x - 18)} {f(b - 30)} {f(x - 8)} {f(b - 40)} {f(x)} {f(b - 40)} C {f(x + 8)} {f(b - 40)} {f(x + 18)} {f(b - 30)} {f(x + 12)} {f(b)} Z" fill="#8A4A2A" stroke="{INK}" stroke-width="1.8"></path>'
                 f'<circle cx="{f(x - 4)}" cy="{f(b - 20)}" r="4" fill="#B8642A"></circle><circle cx="{f(x + 5)}" cy="{f(b - 28)}" r="3" fill="#5A2A1A"></circle>')
    for _ in range(3):
        x, y = r.uniform(w * 0.2, w * 0.5), r.uniform(h * 0.2, h * 0.5)
        o.append(f'<path d="M{f(x)} {f(y)} c -6 -6 -12 -2 -10 4 c 4 2 8 0 10 -4 c 2 -6 8 -8 12 -2 c -2 6 -8 6 -12 2" fill="#C8B8A0" stroke="{INK}" stroke-width="1"></path>')
    return "".join(o)

def eye_lamp(p, w, h, seed):
    """The lamp of the body is the eye: one half full of light, a lamp burning; the other half full of darkness, the lamp
    gone out, a thread of smoke."""
    o = [bgr(w, h, "#05050E"), f'<rect x="-10" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#FFE6A0"></rect>',
         glow(w * 0.25, h * 0.5, h * 0.6, "#FFFDF0", 0.9, f"{p}g")]
    s = max(0.8, h / 160)
    o.append(A.lamp(w * 0.25, h * 0.66, s) + A.lamp(w * 0.75, h * 0.66, s).replace(E.flame(26, -4, 8, 22, 0.1), ""))
    o.append(f'<path d="M{f(w * 0.75 + 26 * s)} {f(h * 0.66 - 6 * s)} C {f(w * 0.75 + 16 * s)} {f(h * 0.5)} {f(w * 0.75 + 36 * s)} {f(h * 0.4)} {f(w * 0.75 + 22 * s)} {f(h * 0.24)}" stroke="#4A4458" stroke-width="3" fill="none"></path>')
    return "".join(o)

def birds_heaven(p, w, h, seed):
    """Behold the birds of the heaven, that they sow not, neither do they reap, nor gather into barns: swallows wheeling
    over a reaped field and a barn, the sky wide open."""
    o = [sky(w, h, "#5AB0D8", "#F3E8C8"), hills(w, h, h * 0.62, seed, color="#8A9A6A", amp=10, step=90), ground(w, h, h * 0.72, "#D8B860", dy=0),
         grain(-10, w + 10, h * 0.98, h * 0.08, seed, color="#C8A060")]
    from job.art import house
    o.append(house(w * 0.8, h * 0.76, w * 0.14, h * 0.18, color="#B89A6A"))
    o.append(birds(16, w * 0.06, w * 0.94, h * 0.08, h * 0.56, seed, smin=0.9, smax=2.2))
    return "".join(o)

def lilies_field(p, w, h, seed):
    """Consider the lilies of the field, how they grow: the hillside in spring, covered with lilies and red flowers, the
    grass that to-day is; far off, the smoke of an oven."""
    r = random.Random(seed)
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.34, seed, color="#8A9A6A", amp=10, step=90), ground(w, h, h * 0.42, "#7AAA4A", dy=0)]
    from job.art import smoke
    o.append(f'<rect x="{f(w * 0.86)}" y="{f(h * 0.36)}" width="{f(w * 0.04)}" height="{f(h * 0.06)}" fill="#8A6A4A" stroke="{INK}" stroke-width="1.4"></rect>' + smoke(w * 0.88, h * 0.34, 6, seed, k=0.4))
    items = sorted((r.uniform(h * 0.46, h * 1.02), r.uniform(-10, w + 10)) for _ in range(46))
    for y, x in items:
        k = 0.3 + 1.1 * (y - h * 0.46) / (h * 0.56)
        if r.random() < 0.55: o.append(lily(x, y, k * h / 300))
        else:
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 30 * k * h / 300)}" stroke="#3A6A2A" stroke-width="2"></path>'
                     f'<circle cx="{f(x)}" cy="{f(y - 34 * k * h / 300)}" r="{f(7 * k * h / 300)}" fill="#D7261E" stroke="{INK}" stroke-width="1.2"></circle>'
                     f'<circle cx="{f(x)}" cy="{f(y - 34 * k * h / 300)}" r="{f(2.4 * k * h / 300)}" fill="#1A1210"></circle>')
    return "".join(o)

def pearls(p, w, h, seed):
    """Neither cast your pearls before the swine, lest they trample them under their feet: a string of pearls broken in the
    mire, the swine trampling past, a dog behind."""
    r = random.Random(seed); b = h * 0.9
    o = [sky(w, h, "#A8A08A", "#E8D8B8"), ground(w, h, h * 0.5, "#6A5A3A", dy=0)]
    for _ in range(12):
        o.append(f'<ellipse cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.56, h))}" rx="{f(r.uniform(10, 30))}" ry="{f(r.uniform(3, 8))}" fill="#4A3A22"></ellipse>')
    for _ in range(14):
        x = w * 0.5 + r.uniform(-w * 0.2, w * 0.2); y = h * 0.86 + r.uniform(-h * 0.06, h * 0.06)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(max(3, h * 0.016))}" fill="#F8F4EC" stroke="{INK}" stroke-width="1"></circle>')
    k = max(1.2, h / 110)
    for i, x in enumerate((0.16, 0.34, 0.74)):
        o.append(creature("swine", w * x, h * (0.7 + 0.06 * i), k * (0.9 + 0.1 * i), color="#C89080"))
    o.append(dog(w * 0.9, h * 0.66, k * 0.4, flip=True, color="#8A6A4A"))
    return "".join(o)

def door_knock(p, w, h, seed):
    """Knock, and it shall be opened unto you: a door in a white wall opening, the light of the house streaming out over
    the step and the one who knocked."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bgr(w, h, "#2A2050"), mk.stars(30, w, h * 0.4, seed),
         f'<rect x="{f(w * 0.3)}" y="{f(h * 0.08)}" width="{f(w * 0.6)}" height="{f(b - h * 0.08)}" fill="#C8B8A0" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.5)}" y="{f(h * 0.3)}" width="{f(w * 0.16)}" height="{f(b - h * 0.3)}" fill="#FFF4C2" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.5)} {f(h * 0.3)} L {f(w * 0.43)} {f(h * 0.26)} L {f(w * 0.43)} {f(b + 6)} L {f(w * 0.5)} {f(b)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.5)} {f(b)} L {f(w * 0.66)} {f(b)} L {f(w * 0.86)} {f(h + 10)} L {f(w * 0.3)} {f(h + 10)} Z" fill="#FFE680" opacity="0.6"></path>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A3048" opacity="0.5"></rect>']
    s = fit(b, max(h * 0.2, b - 220))
    o.append(man(p, w * 0.22, b, s, "#5A4A3A", up=[(-22, -158), (-40, -160), (-56, -168)], flip=True))
    return "".join(o)

def loaf_stone(p, w, h, seed):
    """If his son shall ask him for a loaf, will give him a stone? or for a fish, a serpent?: on a table, a loaf beside a
    stone, a fish beside a coiled serpent."""
    from snake import snake
    b = h * 0.78
    o = [bgr(w, h, "#3A2A2A"), glow(w * 0.5, h * 0.3, h * 0.5, "#FFE680", 0.3, f"{p}g"),
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A5A30" stroke="{INK}" stroke-width="2.4"></rect>']
    s = max(1.0, h / 80)
    o.append(loaf(w * 0.14, b - 6 * s, s))
    o.append(f'<ellipse cx="{f(w * 0.3)}" cy="{f(b - 7 * s)}" rx="{f(15 * s)}" ry="{f(8 * s)}" fill="#9A9488" stroke="{INK}" stroke-width="1.6"></ellipse>')
    o.append(label(w * 0.22, b + 0.12 * h + 8, "A LOAF · A STONE", "#F3EFE6", 10))
    o.append(creature("fish", w * 0.64, b - 6 * s, s * 0.7, color="#8FB8C8"))
    k = s * 0.8
    o.append(snake([(w * 0.8, b - 4), (w * 0.86, b - 8 * k), (w * 0.82, b - 18 * k), (w * 0.88, b - 26 * k)], 3.5 * k, f"{p}sn", 0.6))
    o.append(label(w * 0.74, b + 0.12 * h + 8, "A FISH · A SERPENT", "#F3EFE6", 10))
    return "".join(o)

def two_gates(p, w, h, seed):
    """Wide is the gate, and broad is the way, that leadeth to destruction; narrow is the gate, and straitened the way, that
    leadeth unto life: on the left a broad road down to a great gate in red smoke, many walking it; on the right a narrow
    steep path up to a small gate in the light, one climbing."""
    b = h * 0.96
    o = [mk.defs(p, *ALL), sky(w, h, "#3A1A2A", "#FFC890"),
         f'<rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#8FD0E2"></rect>',
         glow(w * 0.82, h * 0.16, h * 0.3, "#FFF4C2", 0.9, f"{p}g"),
         ground(w, h, h * 0.4, "#5A3A3A", dy=0),
         f'<path d="M{f(w * 0.5)} {f(h * 0.4)} L {f(w * 0.5)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} L {f(w + 10)} {f(h * 0.4)} L {f(w * 0.86)} {f(h * 0.2)} L {f(w * 0.74)} {f(h * 0.3)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></path>']
    o.append(f'<path d="M-10 {f(h + 10)} L {f(w * 0.48)} {f(h + 10)} L {f(w * 0.3)} {f(h * 0.48)} L {f(w * 0.14)} {f(h * 0.48)} Z" fill="#8A6A5A" stroke="{INK}" stroke-width="1.6"></path>')
    gx = w * 0.22
    o.append(f'<rect x="{f(gx - w * 0.12)}" y="{f(h * 0.22)}" width="{f(w * 0.24)}" height="{f(h * 0.28)}" fill="#6A4A3A" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(gx - w * 0.08)} {f(h * 0.5)} L {f(gx - w * 0.08)} {f(h * 0.32)} Q {f(gx)} {f(h * 0.24)} {f(gx + w * 0.08)} {f(h * 0.32)} L {f(gx + w * 0.08)} {f(h * 0.5)} Z" fill="#2A0A0A" stroke="{INK}" stroke-width="2"></path>')
    from job.art import smoke
    o.append(smoke(gx, h * 0.24, 6, seed, color="#5A2A2A", op=0.5, k=max(0.4, h / 400)))
    o.append(f'<path d="M{f(w * 0.62)} {f(h + 10)} C {f(w * 0.66)} {f(h * 0.8)} {f(w * 0.76)} {f(h * 0.6)} {f(w * 0.8)} {f(h * 0.3)}" stroke="#C8B898" stroke-width="{f(max(4, h * 0.025))}" fill="none"></path>')
    o.append(f'<rect x="{f(w * 0.785)}" y="{f(h * 0.16)}" width="{f(w * 0.04)}" height="{f(h * 0.14)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.795)}" y="{f(h * 0.2)}" width="{f(w * 0.02)}" height="{f(h * 0.1)}" fill="#FFE680" stroke="{INK}" stroke-width="1.2"></rect>')
    s = fit(b, max(h * 0.3, b - 200))
    r = random.Random(seed)
    for i in range(9):
        y = h * (0.56 + 0.05 * i); x = w * (0.3 - 0.02 * i) + r.uniform(-w * 0.06, w * 0.06) - (y - h * 0.5) * 0.2
        o.append(figure(p, x, y, y - (y - h * 0.4) * 0.5, r.choice(HEB), "man" if r.random() < 0.6 else "woman", flip=True))
    y1 = h * 0.62
    o.append(figure(p, w * 0.72, y1, y1 - h * 0.14, "#5A6A8A", "man"))
    return "".join(o)

def wolf(x, y, s=1.0, flip=False, fleece=False):
    """A grey wolf standing, head low, eyes burning yellow; fleece=True: a sheep's fleece thrown over its back."""
    sx = -s if flip else s
    body = ("M-50 -30 C -54 -48 -36 -58 -10 -56 L 30 -54 C 40 -56 46 -62 52 -70 L 56 -84 L 62 -72 L 70 -82 L 72 -66 C 80 -60 92 -54 100 -50 "
            "L 98 -44 C 88 -42 78 -40 70 -40 C 62 -38 54 -36 48 -32 L 46 0 L 38 0 L 36 -28 L -30 -28 L -34 0 L -42 0 L -44 -28 Z")
    o = (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
         '<path d="M-48 -44 C -66 -46 -80 -36 -86 -20 C -76 -30 -64 -34 -50 -36" fill="#5A5A62" stroke="#0D0D0F" stroke-width="2"></path>'
         f'<path d="{body}" fill="#6A6A72" stroke="#0D0D0F" stroke-width="2.2" stroke-linejoin="round"></path>'
         '<circle cx="70" cy="-56" r="3.4" fill="#FFD23F" stroke="#0D0D0F" stroke-width="0.8"></circle>'
         '<path d="M88 -46 L 96 -44 M84 -44 l 2 4 M90 -44 l 2 4" stroke="#F3EFE6" stroke-width="1.6"></path>')
    if fleece:
        o += ('<path d="M-48 -40 C -50 -58 -40 -70 -24 -66 C -16 -76 -2 -76 4 -68 C 14 -76 30 -74 34 -62 C 44 -60 46 -48 40 -40 '
              'C 36 -30 20 -34 14 -38 C 4 -30 -10 -32 -16 -38 C -26 -30 -42 -32 -48 -40 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2"></path>'
              '<path d="M-40 -42 l -4 12 M30 -42 l 4 12" stroke="#E8E2D6" stroke-width="5"></path>')
    return o + "</g>"

def wolves(p, w, h, seed):
    """False prophets in sheep's clothing, inwardly ravening wolves: the flock at dusk by the fold, and among them one whose
    eyes burn yellow and whose fleece hangs loose over a grey hide."""
    r = random.Random(seed); b = h * 0.92
    o = [sky(w, h, "#2A1A3A", "#C8682E"), hills(w, h, h * 0.5, seed, color="#3A2A3A", amp=10, step=80), ground(w, h, h * 0.6, "#5A4A3A", dy=0),
         f'<path d="M{f(w * 0.7)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.5)} L {f(w * 0.7)} {f(h * 0.5)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></path>']
    k = max(0.5, h / 260)
    for i in range(6):
        x = w * (0.08 + 0.14 * i); y = b - (i % 2) * h * 0.06
        if i == 3:
            o.append(wolf(x, y, k * 0.7, fleece=True))
        else:
            o.append(E.sheep(x, y, k * 0.62, flip=r.random() < 0.3))
    return "".join(o)

def fruit_trees(p, w, h, seed):
    """By their fruits ye shall know them: a good tree heavy with fruit, a vine with its grapes; a corrupt tree bare, and
    the thorns and thistles; the axe and the fire for the tree that beareth not."""
    b = h * 0.94
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"),
         hills(w, h, h * 0.6, seed, color="#8A9A6A", amp=10, step=80), ground(w, h, h * 0.7, "#9AAA5A", dy=0),
         f'<rect x="{f(w * 0.5)}" y="{f(h * 0.7)}" width="{f(w * 0.5 + 10)}" height="{f(h)}" fill="#A8885A" stroke="{INK}" stroke-width="2"></rect>']
    k = max(0.5, (b - h * 0.1) / 160)
    o.append(fig_tree(w * 0.18, b, k, fruit=True, seed=seed))
    o.append(vines(w * 0.3, w * 0.46, b, b, seed, rows=1))
    o.append(fig_tree(w * 0.66, b, k, bare=True, seed=seed + 1))
    for i in range(5):
        x = w * (0.56 + 0.08 * i)
        o.append(f'<path d="M{f(x)} {f(b)} l -8 -18 M{f(x)} {f(b)} l 0 -22 M{f(x)} {f(b)} l 9 -16" stroke="#5A4A2A" stroke-width="2"></path>'
                 f'<circle cx="{f(x)}" cy="{f(b - 24)}" r="4" fill="#8A4A9A" stroke="{INK}" stroke-width="1"></circle>')
    o.append(E.blaze(w * 0.88, b, w * 0.14, h * 0.3, seed, n=5))
    return "".join(o)

def house_storm(p, w, h, seed, rock=True):
    """The rain descended, and the floods came, and the winds blew: rock=True, the wise man's house on the rock standing in
    the storm; rock=False, the foolish man's house on the sand, the flood undercutting it, falling."""
    r = random.Random(seed); b = h * 0.8
    o = [sky(w, h, "#14141E", "#4A4A5E"), rain(w, h, seed, n=80), bolt(w * 0.8, 0, h * 0.4, seed)]
    hx, hw, hh = w * 0.48, w * 0.3, h * 0.32
    if rock:
        o.append(f'<path d="M{f(hx - hw)} {f(h + 10)} L {f(hx - hw * 0.8)} {f(b)} C {f(hx - hw * 0.4)} {f(b - h * 0.06)} {f(hx + hw * 0.4)} {f(b - h * 0.06)} {f(hx + hw * 0.8)} {f(b)} L {f(hx + hw)} {f(h + 10)} Z" fill="#6A6A72" stroke="{INK}" stroke-width="2.4"></path>'
                 f'<path d="M{f(hx - hw * 0.5)} {f(b + h * 0.06)} L {f(hx - hw * 0.3)} {f(h)} M{f(hx + hw * 0.4)} {f(b + h * 0.04)} L {f(hx + hw * 0.5)} {f(h)}" stroke="#3A3A42" stroke-width="2"></path>')
        o.append(f'<rect x="{f(hx - hw / 2)}" y="{f(b - h * 0.04 - hh)}" width="{f(hw)}" height="{f(hh)}" fill="#C8B8A0" stroke="{INK}" stroke-width="2.4"></rect>'
                 f'<rect x="{f(hx - hw / 2 - 6)}" y="{f(b - h * 0.04 - hh - 8)}" width="{f(hw + 12)}" height="8" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(hx - hw * 0.1)}" y="{f(b - h * 0.04 - hh * 0.6)}" width="{f(hw * 0.2)}" height="{f(hh * 0.6)}" fill="#3A2A1E" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(hx + hw * 0.24)}" y="{f(b - h * 0.04 - hh * 0.8)}" width="{f(hw * 0.12)}" height="{f(hh * 0.18)}" fill="#FFC14D" stroke="{INK}" stroke-width="1.6"></rect>')
        o.append(f'<path d="M-10 {f(h * 0.9)} Q {f(w * 0.1)} {f(h * 0.84)} {f(w * 0.2)} {f(h * 0.9)} T {f(w * 0.3)} {f(h * 0.9)} L {f(w * 0.3)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A5A7A" stroke="{INK}" stroke-width="2"></path>'
                 f'<path d="M{f(w * 0.72)} {f(h * 0.9)} Q {f(w * 0.82)} {f(h * 0.84)} {f(w * 0.92)} {f(h * 0.9)} T {f(w + 10)} {f(h * 0.9)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.72)} {f(h + 10)} Z" fill="#3A5A7A" stroke="{INK}" stroke-width="2"></path>')
    else:
        o.append(f'<path d="M-10 {f(h * 0.82)} C {f(w * 0.3)} {f(h * 0.76)} {f(w * 0.6)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.76)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#D8C090" stroke="{INK}" stroke-width="2"></path>')
        g = (f'<rect x="{f(-hw / 2)}" y="{f(-hh)}" width="{f(hw)}" height="{f(hh)}" fill="#C8B8A0" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(-hw / 2 - 6)}" y="{f(-hh - 8)}" width="{f(hw + 12)}" height="8" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(-hw * 0.1)} 0 L {f(-hw * 0.2)} {f(-hh * 0.7)} L {f(hw * 0.05)} {f(-hh * 0.4)} L {f(hw * 0.2)} {f(-hh)}" stroke="#2A1A10" stroke-width="3" fill="none"></path>')
        o.append(f'<g transform="translate({f(hx)} {f(b - 4)}) rotate(14)">{g}</g>')
        for _ in range(6):
            x = hx + r.uniform(-hw, hw)
            o.append(f'<rect x="{f(x)}" y="{f(b + r.uniform(-4, 10))}" width="{f(r.uniform(8, 18))}" height="{f(r.uniform(6, 12))}" fill="#C8B8A0" stroke="{INK}" stroke-width="1.4" transform="rotate({r.randint(-30, 30)} {f(x)} {f(b)})"></rect>')
        o.append(f'<path d="M-10 {f(h * 0.86)} Q {f(w * 0.15)} {f(h * 0.78)} {f(w * 0.3)} {f(h * 0.86)} T {f(w * 0.6)} {f(h * 0.86)} T {f(w * 0.9)} {f(h * 0.86)} T {f(w + 40)} {f(h * 0.86)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A5A7A" stroke="{INK}" stroke-width="2"></path>')
    return "".join(o)
