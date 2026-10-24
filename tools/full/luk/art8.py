"""Drawings for Luke 12–13: the rich man's fields and his barns, and the night his soul was required (God never drawn: the
Voice box only); the little flock; the servants girded with their lamps burning, waiting at the door in the night; the fire
kindled upon the earth; five in one house divided; the Galilæans whose blood Pilate mingled (words only, over the empty
altar court); the fallen tower in Siloam (stones only, no one drawn under them); the woman bowed together eighteen years,
then made straight; the narrow door shut and men knocking without. Built on luk.art7."""
from luk.art7 import *
from luk.art7 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch, \
    jesus_kneel, light_seated, WOMEN3, PURPLE, GOLD, kneel_w, boy_fig, zach_fig, elis_fig, shepherd_fig, swaddled, fish_heap, WIDOW_C, WIDOW_V, SINNER_C, SINNER_V, \
    JOANNA, SUSANNA, SAMARITAN_C, samaritan_fig, priest_fig, levite_fig
import random, math

RICH_C = "#5A1A5A"
def rich_fig(p, x, y, s, flip=False, up=None):
    """The rich man of the parables: purple and fine linen, a gold-banded purple headcloth, a black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=RICH_C, kind="Robe", sw=3, flip=flip, up=up,
                     extra='<path d="M-24 -150 L 24 -150 L 22 -144 L -22 -144 Z" fill="#F3EFE6"></path>' + A.headcloth("#6A2A6A", cord="#E8B830") + A.BLACK_BEARD)

def barn(x, b, wd, ht, color="#B8946A", new=False):
    """A barn of stone with a timber roof and a wide door."""
    return (f'<rect x="{f(x - wd / 2)}" y="{f(b - ht)}" width="{f(wd)}" height="{f(ht)}" fill="{color}" stroke="{INK}" stroke-width="2.2"></rect>'
            f'<path d="M{f(x - wd / 2 - 8)} {f(b - ht)} L {f(x)} {f(b - ht - ht * 0.4)} L {f(x + wd / 2 + 8)} {f(b - ht)} Z" fill="{"#A8704A" if new else "#7A5A3A"}" stroke="{INK}" stroke-width="2.2"></path>'
            f'<rect x="{f(x - wd * 0.16)}" y="{f(b - ht * 0.6)}" width="{f(wd * 0.32)}" height="{f(ht * 0.6)}" fill="#3A2A1E" stroke="{INK}" stroke-width="1.8"></rect>')

def rich_fool(p, w, h, seed, stage="plenty"):
    """The ground of a certain rich man brought forth plentifully: stage='plenty' his wide fields heavy with grain, the old
    barns too small, sheaves heaped about them, the rich man looking on; 'build' the old barns pulled down and great new
    barns rising; 'night' the same barns full under a night sky, the house dark but for one lamp — this night is thy soul
    required of thee (God never drawn: the words in the Voice box)."""
    b = h * 0.92
    night_ = stage == "night"
    o = [mk.defs(p, *ALL), night(w, h, seed, n=50) if night_ else sky(w, h, "#8FD0E2", "#FFE6B0"),
         hills(w, h, h * 0.44, seed, color="#2A2238" if night_ else "#8A9A6A", amp=12, step=80),
         ground(w, h, h * 0.56, "#2A2430" if night_ else "#D8B860", dy=0)]
    if not night_: o.append(grain(-10, w + 10, h * 0.72, h * 0.12, seed))
    if stage == "plenty":
        o.append(barn(w * 0.62, h * 0.8, w * 0.12, h * 0.14) + barn(w * 0.78, h * 0.8, w * 0.1, h * 0.12))
        for i in range(7):
            x = w * (0.5 + 0.06 * i); o.append(f'<path d="M{f(x - 10)} {f(b)} L {f(x)} {f(b - 40)} L {f(x + 10)} {f(b)} Z" fill="#E8C060" stroke="#7A5A1A" stroke-width="1.4"></path>')
    else:
        o.append(barn(w * 0.6, h * 0.84, w * 0.26, h * 0.3, new=True, color="#2E2A3A" if night_ else "#C8A478")
                 + barn(w * 0.86, h * 0.84, w * 0.2, h * 0.26, new=True, color="#2E2A3A" if night_ else "#C8A478"))
    if night_:
        o.append(f'<rect x="{f(w * 0.06)}" y="{f(h * 0.5)}" width="{f(w * 0.24)}" height="{f(h * 0.34)}" fill="#3A3448" stroke="{INK}" stroke-width="2.2"></rect>'
                 f'<rect x="{f(w * 0.16)}" y="{f(h * 0.58)}" width="{f(w * 0.04)}" height="{f(h * 0.06)}" fill="#FFC14D" stroke="{INK}" stroke-width="1.4"></rect>')
    else:
        s = fit(b, max(h * 0.3, b - 220))
        o.append(rich_fig(p, w * 0.24, b, s, up=UP_BLESS if stage == "plenty" else UP_HIGH, flip=True))
    return "".join(o)

def little_flock(p, w, h, seed):
    """Fear not, little flock: a few sheep gathered close on a green hillside at evening, their shepherd standing over them
    with his staff, the fold behind."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A9A", "#FFC890"), hills(w, h, h * 0.5, seed, color="#6A7A5A", amp=12, step=80),
         ground(w, h, h * 0.62, "#7A9A4A", dy=0),
         f'<path d="M{f(w * 0.66)} {f(h * 0.66)} L {f(w * 0.98)} {f(h * 0.66)} L {f(w * 0.98)} {f(h * 0.76)} L {f(w * 0.66)} {f(h * 0.76)} Z" fill="#A8946A" stroke="{INK}" stroke-width="2"></path>']
    o.append(sheep_row(w * 0.1, w * 0.56, b - h * 0.02, 6, seed, s=max(0.3, min(0.6, h / 700))))
    s = fit(b, max(h * 0.3, b - 220))
    o.append(shepherd_fig(p, w * 0.6, b, s, 0, flip=True))
    return "".join(o)

def watching(p, w, h, seed, lord=False):
    """Let your loins be girded about, and your lamps burning: the door of a great house at night, the servants waiting by
    it girded, each with his lamp lit, looking down the dark road for their lord; lord=True: the lord come in, girded, setting
    the meat before them at the table."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), night(w, h, seed, n=60), ground(w, h, b, "#2A2438", dy=0)]
    hx0, hx1, top = w * 0.04, w * 0.56, h * 0.2
    o.append(f'<rect x="{f(hx0)}" y="{f(top)}" width="{f(hx1 - hx0)}" height="{f(b - top)}" fill="#5A5068" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(w * 0.36)} {f(b)} L {f(w * 0.36)} {f(b - h * 0.42)} Q {f(w * 0.44)} {f(b - h * 0.52)} {f(w * 0.52)} {f(b - h * 0.42)} L {f(w * 0.52)} {f(b)} Z" fill="#FFC14D" stroke="{INK}" stroke-width="2"></path>')
    s = fit(b, max(h * 0.2, b - 230))
    if lord:
        o.append(f'<rect x="{f(w * 0.6)}" y="{f(b - 40 * s)}" width="{f(w * 0.34)}" height="{f(14 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
                 + "".join(loaf(w * (0.66 + 0.08 * i), b - 44 * s, s * 0.6) for i in range(4)))
        o.append(seated(w * 0.64, b, s * 0.76, HEB[1], head=HEB[1], beard="#2A1A10") + seated(w * 0.9, b, s * 0.76, HEB[3], head=HEB[3], beard="#2A1A10", flip=True))
        o.append(man(p, w * 0.78, b, s, "#E8E2D6", up=[(-22, -158), (-46, -140), (-60, -128)], extra=A.headcloth("#5A2A6A", cord="#E8B830")))
    else:
        for i, x in enumerate((0.6, 0.72, 0.84)):
            o.append(man(p, w * x, b - 2 * i, s * (0.96 - 0.02 * i), HEB[i + 1], flip=False, up=[(-22, -158), (-40, -150), (-52, -152)]))
            lx, ly = w * x - 52 * s, b - 152 * s * (0.96 - 0.02 * i)
            o.append(glow(lx, ly, 30 * s, "#FFE680", 0.9, f"{p}l{i}") + A.lamp(lx, ly, s * 0.5))
    return "".join(o)

def fire_earth(p, w, h, seed):
    """I came to cast fire upon the earth: a fire kindled on a bare hilltop at dusk, its flame going up, the land dark about
    it — no one drawn."""
    b = h * 0.94
    o = [sky(w, h, "#2A1A3A", "#E8803A"), hills(w, h, h * 0.62, seed, color="#3A2A3A", amp=12, step=80),
         f'<path d="M{f(w * 0.2)} {f(b)} C {f(w * 0.36)} {f(h * 0.5)} {f(w * 0.64)} {f(h * 0.5)} {f(w * 0.8)} {f(b)} Z" fill="#4A3030" stroke="{INK}" stroke-width="2.2"></path>',
         glow(w * 0.5, h * 0.5, h * 0.4, "#FF8A3D", 0.6, f"{p}g"), E.blaze(w * 0.5, h * 0.6, w * 0.12, h * 0.3, seed, n=6), ground(w, h, b, "#2A1A1A", dy=0)]
    return "".join(o)

def divided(p, w, h, seed):
    """Five in one house divided, three against two: within a house, a low table, and on one side three standing turned away,
    on the other side two — father and son, mother and daughter — their backs to each other."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#A88A6A"), f'<path d="M{f(w * 0.5)} {f(h * 0.1)} L {f(w * 0.5)} {f(b)}" stroke="#6A4A2A" stroke-width="3" stroke-dasharray="8 6"></path>']
    s = fit(b, max(h * 0.2, b - 230))
    o.append(man(p, w * 0.14, b, s, "#5A4A3A", extra=A.WHITE_BEARD.replace("#E8E2D6", "#9A948A")) + woman_fig(p, w * 0.26, b, s * 0.92, "#6A3A4A", "#4A2A3A") + woman_fig(p, w * 0.38, b, s * 0.9, "#4A5A6A", "#3A4A5A"))
    o.append(man(p, w * 0.66, b, s * 0.96, "#6A6A3A", flip=True) + woman_fig(p, w * 0.8, b, s * 0.9, "#7A5A3A", "#8A6A2A", flip=True))
    return "".join(o)

def altar_court(p, w, h, seed):
    """The Galilæans whose blood Pilate had mingled with their sacrifices — told in words only: the court of the altar of
    burnt-offering, empty, a thin smoke going up from the altar, the shadow of a Roman spear across the pavement."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#6A6A8A", "#E8C8A0"), temple(w * 0.72, h * 0.5, w * 0.4), pavement(w, h, h * 0.5)]
    ax, aw, ah = w * 0.4, w * 0.26, h * 0.24
    o.append(f'<rect x="{f(ax - aw / 2)}" y="{f(b - ah)}" width="{f(aw)}" height="{f(ah)}" fill="#A8A098" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(ax - aw / 2)} {f(b - ah)} L {f(ax - aw / 2 - 8)} {f(b - ah - 12)} M{f(ax + aw / 2)} {f(b - ah)} L {f(ax + aw / 2 + 8)} {f(b - ah - 12)}" stroke="{INK}" stroke-width="3"></path>'
             + smoke(ax, b - ah - 10, 8, seed, color="#8A8090", op=0.5, k=max(0.6, h / 360)))
    o.append(f'<path d="M{f(w * 0.02)} {f(b)} L {f(w * 0.36)} {f(b - h * 0.12)}" stroke="#3A3440" stroke-width="5" opacity="0.6"></path>')
    return "".join(o)

def siloam(p, w, h, seed):
    """The tower in Siloam fell: below the city wall by the pool of Siloam, a tower fallen in a heap of great stones, dust
    still hanging over it — no one drawn among the stones."""
    b = h * 0.94
    r = random.Random(seed)
    o = [sky(w, h, "#8A9AB0", "#E8D8B8"), walls(w * 0.0, w * 1.0, h * 0.56, h * 0.3, seed, towers=3, houses=True), ground(w, h, h * 0.56, "#B8A07A", dy=0),
         f'<ellipse cx="{f(w * 0.24)}" cy="{f(h * 0.8)}" rx="{f(w * 0.18)}" ry="{f(h * 0.06)}" fill="#3A7A9A" stroke="{INK}" stroke-width="2"></ellipse>']
    cx = w * 0.66
    for _ in range(24):
        x = cx + r.uniform(-w * 0.16, w * 0.16); y = b - r.uniform(0, h * 0.22) * (1 - abs(x - cx) / (w * 0.2)); s = r.uniform(10, 22) * h / 300
        o.append(f'<rect x="{f(x - s)}" y="{f(y - s * 0.7)}" width="{f(s * 2)}" height="{f(s * 1.4)}" fill="{r.choice(["#C8B088", "#B8A078", "#D8C098"])}" stroke="{INK}" stroke-width="1.6" transform="rotate({r.randint(-25, 25)} {f(x)} {f(y)})"></rect>')
    o.append(smoke(cx, b - h * 0.2, 7, seed, color="#C8B8A0", op=0.4, k=max(0.6, h / 300)))
    return "".join(o)

def bowed(p, w, h, seed, straight=False):
    """A woman that had a spirit of infirmity eighteen years, bowed together: in the synagogue on the sabbath, a woman in grey
    bent over double, her staff in her hand, Jesus calling her; straight=True: the woman standing straight with her arms
    lifted, Jesus' hands just lifted from her, the ruler of the synagogue frowning at the side (no spirit drawn)."""
    b = h * 0.94
    o = [synagogue(p, w, h, seed, teaching=False, crowd_n=7)]
    s = fit(b, max(h * 0.2, b - 230))
    o.append(jesus(p, w * 0.36, b, s, flip=True, up=UP_BLESS))
    if straight:
        o.append(glow(w * 0.52, b - 110 * s, 120 * s, "#FFF4C2", 0.6, f"{p}g"))
        o.append(woman_fig(p, w * 0.52, b, s * 0.9, "#6A6A6E", "#4A4A52", up=UP_HIGH))
        o.append(scribe_fig(p, w * 0.86, b, s * 0.96, flip=True))
    else:
        o.append(f'<g transform="translate({f(w * 0.56)} {f(b)}) rotate(-26) translate({f(-w * 0.56)} {f(-b)})">'
                 + woman_fig(p, w * 0.56, b, s * 0.78, "#6A6A6E", "#4A4A52") + '</g>'
                 f'<path d="M{f(w * 0.47)} {f(b)} L {f(w * 0.45)} {f(b - 90 * s)}" stroke="#5A3A22" stroke-width="{f(5 * s)}"></path>')
    return "".join(o)

def narrow_door(p, w, h, seed, shut=False):
    """Strive to enter in by the narrow door: a house at evening, its narrow door standing open with light within, a few
    going in one by one; shut=True: night, the door shut to, and many standing without, knocking."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), night(w, h, seed, n=50) if shut else sky(w, h, "#4A3A6A", "#FFB07A"),
         f'<rect x="{f(w * 0.3)}" y="{f(h * 0.2)}" width="{f(w * 0.4)}" height="{f(b - h * 0.2)}" fill="{"#4A4058" if shut else "#C8B490"}" stroke="{INK}" stroke-width="2.4"></rect>',
         ground(w, h, b, "#2A2438" if shut else "#8A7A5A", dy=0)]
    dx, dw = w * 0.5, w * 0.06
    o.append(f'<rect x="{f(dx - dw / 2)}" y="{f(b - h * 0.36)}" width="{f(dw)}" height="{f(h * 0.36)}" fill="{"#4A3020" if shut else "#FFE680"}" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.24, b - 220))
    if shut:
        r = random.Random(seed)
        for i, x in enumerate((0.08, 0.18, 0.28, 0.6, 0.72, 0.84, 0.94)):
            o.append(man(p, w * x, b - r.uniform(0, 4), s * r.uniform(0.86, 0.96), r.choice(HEB), flip=x < 0.5, up=UP_HIGH if i in (2, 3) else None))
    else:
        o.append(glow(dx, b - h * 0.18, h * 0.3, "#FFE680", 0.6, f"{p}g") + man(p, dx + dw * 1.6, b, s * 0.9, "#5A6A4A") + woman_fig(p, w * 0.72, b, s * 0.86, "#6A3A4A", "#4A2A3A", flip=True))
    return "".join(o)
