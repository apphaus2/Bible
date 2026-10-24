"""Drawings for Matthew 23–25: Moses' seat; the heavy burdens; the phylacteries and broad borders; the gnat and the camel;
the cup clean without; the whited sepulchres (nothing within drawn); the hen gathering her chickens over Jerusalem; the
great stones of the temple; the mount of Olives at evening; wars and earthquakes far off; the flight to the mountains; the
lightning from east to west; the eagles; the sun darkened and the stars falling; the sign in heaven, the clouds and the
angels' trumpet; the fig tree in leaf; the ark and the flood; two at the mill; the thief at night; the faithful steward;
the ten virgins and the shut door; the talents; the throne of glory, the sheep and the goats; the six works of mercy.
Built on mat.art8."""
from mat.art8 import *
from mat.art8 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE
from ntcast import JESUS_SKIN, JESUS_HAIR, JESUS_TUNIC, JESUS_MANTLE, ROBES
import random, math
from job.art import seated, smoke
from ecc.art import loaf
from genesis.art2 import ark_afloat
from lev.art import goat
import exodus as E

def moses_seat(p, w, h, seed):
    """The scribes and the Pharisees sit on Moses' seat: in the synagogue, a scribe seated on the carved stone chair, his
    broad phylactery on his brow and the wide blue borders of his robe; men standing before him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bgr(w, h, "#C8B490"), f'<rect x="-10" y="{f(b - h * 0.06)}" width="{f(w + 20)}" height="{f(h)}" fill="#A8906A" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.24, b - 230))
    cx = w * 0.3
    o.append(f'<path d="M{f(cx - 70 * s)} {f(b)} L {f(cx - 70 * s)} {f(b - 190 * s)} C {f(cx - 60 * s)} {f(b - 220 * s)} {f(cx + 60 * s)} {f(b - 220 * s)} {f(cx + 70 * s)} {f(b - 190 * s)} L {f(cx + 70 * s)} {f(b)} Z" fill="#B8A88A" stroke="{INK}" stroke-width="2.4"></path>')
    o.append(seated(cx - 10 * s, b, s * 0.9, "#E8E2D6", head="#F3EFE6", beard="#6A645E", band=True))
    o.append(f'<rect x="{f(cx - 22 * s)}" y="{f(b - 132 * s)}" width="{f(10 * s)}" height="{f(10 * s)}" fill="#2A1A10"></rect>'
             f'<path d="M{f(cx - 50 * s)} {f(b - 4)} L {f(cx + 54 * s)} {f(b - 4)}" stroke="#1F5FAD" stroke-width="{f(8 * s)}"></path>')
    for i in range(4):
        o.append(man(p, w * (0.58 + 0.1 * i), b, s * 0.94, random.Random(seed + i).choice(HEB), flip=True))
    return "".join(o)

def burdens(p, w, h, seed):
    """They bind heavy burdens and grievous to be borne, and lay them on men's shoulders: men bent under great bundles on the
    road, and beside them a scribe walking upright, his hands empty."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#C8A890", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#A89A7A", amp=10, step=80), ground(w, h, h * 0.6, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.24, b - 230))
    load = '<path d="M-40 -230 L 40 -230 L 46 -150 L -46 -150 Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2"></path><path d="M-40 -200 L 44 -200 M-44 -176 L 46 -176" stroke="#5A3A1E" stroke-width="3"></path>'
    for i, x in enumerate((0.14, 0.32, 0.5)):
        o.append(f'<g transform="translate({f(w * x)} {f(b)}) rotate(8) translate({f(-w * x)} {f(-b)})">' + man(p, w * x, b, s * 0.9, random.Random(seed + i).choice(HEB), up=[(-22, -158), (-26, -184), (-14, -196)], extra=load) + '</g>')
    o.append(scribe_fig(p, w * 0.78, b, s, white=True, flip=True))
    return "".join(o)

def gnat_camel(p, w, h, seed):
    """Ye tithe mint and anise and cummin; ye strain out the gnat, and swallow the camel: on a table, the little scales with
    sprigs of herbs weighed out, a strainer over a cup with a gnat caught in it, and beyond the window a whole camel."""
    b = h * 0.8
    o = [bgr(w, h, "#C8A878"), f'<rect x="{f(w * 0.56)}" y="{f(h * 0.1)}" width="{f(w * 0.38)}" height="{f(h * 0.5)}" fill="#FFD89A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#7A4A2A" stroke="{INK}" stroke-width="2.4"></rect>']
    o.append(f'<g transform="translate({f(w * 0.75)} {f(h * 0.58)}) scale({f(h * 0.26 / 200)})">' + J1.camel(0, 0, 1, color="#B5844A") + '</g>')
    k = max(0.6, h / 240)
    sx = w * 0.18
    o.append(f'<path d="M{f(sx)} {f(b)} L {f(sx)} {f(b - 60 * k)} M{f(sx - 40 * k)} {f(b - 60 * k)} L {f(sx + 40 * k)} {f(b - 60 * k)}" stroke="#8A6A3A" stroke-width="{f(3 * k)}"></path>')
    for dx in (-40, 40):
        o.append(f'<path d="M{f(sx + dx * k - 16 * k)} {f(b - 40 * k)} L {f(sx + dx * k + 16 * k)} {f(b - 40 * k)} L {f(sx + dx * k)} {f(b - 60 * k)} Z" fill="#C8963E" stroke="{INK}" stroke-width="1.6"></path>'
                 f'<path d="M{f(sx + dx * k - 8 * k)} {f(b - 42 * k)} l 4 -10 l 4 8 l 4 -12 l 4 12" stroke="#3A7A2A" stroke-width="2" fill="none"></path>')
    o.append(cup(w * 0.4, b, k * 0.5, color="#C8963E") + f'<ellipse cx="{f(w * 0.4)}" cy="{f(b - 48 * k)}" rx="{f(24 * k)}" ry="{f(6 * k)}" fill="none" stroke="#5A5A64" stroke-width="2" stroke-dasharray="2 2"></ellipse>'
             + f'<circle cx="{f(w * 0.4 + 4)}" cy="{f(b - 50 * k)}" r="2" fill="#0D0D0F"></circle>')
    return "".join(o)

def cup_platter(p, w, h, seed):
    """Ye cleanse the outside of the cup and of the platter: a cup and a platter polished bright outside, the inside dark and
    stained."""
    b = h * 0.8
    o = [bgr(w, h, "#2A1A2A"), glow(w * 0.5, h * 0.4, h * 0.6, "#FFE680", 0.3, f"{p}g"),
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#4A2A1E" stroke="{INK}" stroke-width="2"></rect>']
    k = max(0.6, h / 200)
    o.append(f'<ellipse cx="{f(w * 0.62)}" cy="{f(b - 8 * k)}" rx="{f(80 * k)}" ry="{f(18 * k)}" fill="#E8C060" stroke="{INK}" stroke-width="2.4"></ellipse>'
             f'<ellipse cx="{f(w * 0.62)}" cy="{f(b - 10 * k)}" rx="{f(56 * k)}" ry="{f(11 * k)}" fill="#3A2A1A"></ellipse>')
    o.append(cup(w * 0.3, b, k * 0.9, color="#E8C060").replace("#5A0A1A", "#1A1210"))
    return "".join(o)

def sepulchres(p, w, h, seed):
    """Whited sepulchres, which outwardly appear beautiful: a row of tombs freshly whitewashed, gleaming in the sun on the
    hillside, their doors sealed (nothing within drawn)."""
    o = [sky(w, h, "#5AB0D8", "#FFF4C2"), sun(w * 0.86, h * 0.16, 14, color="#FFE680", op=0.4), hills(w, h, h * 0.36, seed, color="#C8A06A", amp=12, step=80),
         ground(w, h, h * 0.5, "#B89A6A", dy=0)]
    for i in range(5):
        x = w * (0.1 + 0.2 * i); y = h * (0.84 - 0.04 * (i % 2)); k = max(0.5, h / 300)
        o.append(f'<path d="M{f(x - 40 * k)} {f(y)} L {f(x - 40 * k)} {f(y - 60 * k)} L {f(x)} {f(y - 100 * k)} L {f(x + 40 * k)} {f(y - 60 * k)} L {f(x + 40 * k)} {f(y)} Z" fill="#FFFFFF" stroke="{INK}" stroke-width="2.2"></path>'
                 f'<rect x="{f(x - 12 * k)}" y="{f(y - 36 * k)}" width="{f(24 * k)}" height="{f(36 * k)}" fill="#E8E2D6" stroke="{INK}" stroke-width="1.6"></rect>')
    return "".join(o)

def prophets_tombs(p, w, h, seed):
    """Ye build the sepulchres of the prophets, and garnish the tombs of the righteous: masons setting carved stones on a
    fine monument, garlands hung on it."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.7, "#C8B07A", dy=0)]
    cx = w * 0.5; k = max(0.5, (b - h * 0.1) / 260)
    o.append(f'<rect x="{f(cx - 80 * k)}" y="{f(b - 180 * k)}" width="{f(160 * k)}" height="{f(180 * k)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(cx - 90 * k)} {f(b - 180 * k)} L {f(cx)} {f(b - 240 * k)} L {f(cx + 90 * k)} {f(b - 180 * k)} Z" fill="#D8C8A0" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(cx - 80 * k)} {f(b - 150 * k)} Q {f(cx)} {f(b - 120 * k)} {f(cx + 80 * k)} {f(b - 150 * k)}" stroke="#3A7A2A" stroke-width="6" fill="none"></path>')
    s = fit(b, max(h * 0.24, b - 230))
    o.append(man(p, w * 0.18, b, s, "#6A5A3A", up=UP_HIGH) + scribe_fig(p, w * 0.82, b, s, white=True, flip=True))
    return "".join(o)

def hen_chickens(p, w, h, seed):
    """O Jerusalem, Jerusalem: how often would I have gathered thy children, as a hen gathereth her chickens under her wings:
    a hen with her wings spread over her brood in the foreground, Jerusalem on its hill behind in the evening light."""
    o = [jerusalem_far(w, h, seed, tone="dusk", lit=True)]
    k = max(0.6, h / 220)
    hx, hy = w * 0.22, h * 0.94
    o.append(f'<g transform="translate({f(hx)} {f(hy)}) scale({f(k)})">'
             '<path d="M-50 0 C -60 -30 -40 -56 -10 -58 C 10 -60 24 -54 30 -46 C 36 -60 50 -62 54 -52 L 62 -48 L 54 -44 C 56 -30 52 -10 40 0 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-56 -10 C -70 -40 -50 -60 -20 -50 C -30 -40 -40 -24 -40 -6 Z" fill="#8A4A1E" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M50 -56 l 2 -8 l 4 6 l 2 -6 l 2 8" fill="#D7261E" stroke="#0D0D0F" stroke-width="1"></path><circle cx="50" cy="-50" r="1.6" fill="#0D0D0F"></circle>'
             '<circle cx="-30" cy="-4" r="7" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.2"></circle><circle cx="-12" cy="-2" r="7" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.2"></circle>'
             '<circle cx="62" cy="-6" r="7" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.2"></circle></g>')
    return "".join(o)

def temple_stones(p, w, h, seed):
    """The buildings of the temple: the great white walls and the gold of the sanctuary towering over the road, huge
    squared stones in the wall; Jesus and the disciples below, one pointing up."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2")]
    for row in range(7):
        y = h * 0.7 - row * h * 0.1
        for k in range(8):
            x = -w * 0.04 + k * w * 0.14 + (w * 0.07 if row % 2 else 0)
            o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.138)}" height="{f(h * 0.098)}" fill="#E8DCC0" stroke="#A89878" stroke-width="1.6"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.0)}" width="{f(w + 20)}" height="{f(h * 0.04)}" fill="#E8B830" stroke="{INK}" stroke-width="2"></rect>')
    o.append(ground(w, h, h * 0.8, "#C8B07A", dy=0))
    s = fit(b, max(h * 0.4, b - 200))
    o.append(jesus(p, w * 0.24, b, s) + disciple(p, w * 0.42, b, s * 0.96, "andrew", flip=True, up=UP_HIGH) + disciple(p, w * 0.54, b, s * 0.94, "thomas", flip=True))
    return "".join(o)

def olivet(p, w, h, seed):
    """He sat on the mount of Olives: Jesus seated under the olive trees at evening, Peter, James, John and Andrew about him,
    and across the valley the temple shining on its hill."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), jerusalem_far(w, h, seed, tone="dusk", lit=True),
         f'<path d="M-10 {f(h * 0.74)} C {f(w * 0.3)} {f(h * 0.68)} {f(w * 0.6)} {f(h * 0.76)} {f(w + 10)} {f(h * 0.72)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A6A3A" stroke="{INK}" stroke-width="2"></path>']
    o.append(olive(w * 0.08, b, h / 300, seed=seed) + olive(w * 0.92, b, h / 320, seed=seed + 1))
    s = fit(b, max(h * 0.3, b - 220))
    o.append(jesus_seated(w * 0.3, b, s * 0.8))
    for i, x in enumerate((0.48, 0.58, 0.68, 0.78)):
        o.append(disciple_seated(w * x, b, s * 0.74, i, flip=True))
    return "".join(o)

def wars_far(p, w, h, seed):
    """Wars and rumors of wars, famines and earthquakes: far across a wide plain under a red sky, the smoke of burning
    cities, and in the foreground the earth split by a long crack (no one drawn)."""
    o = [sky(w, h, "#2A1A2A", "#C8503A"), hills(w, h, h * 0.5, seed, color="#3A2A2A", amp=14, step=80), ground(w, h, h * 0.58, "#6A4A3A", dy=0),
         smokes([w * 0.2, w * 0.5, w * 0.8], h * 0.5, seed, k=max(0.5, h / 340))]
    for x in (0.2, 0.5, 0.8):
        o.append(walls(w * x - w * 0.07, w * x + w * 0.07, h * 0.56, h * 0.08, seed + int(x * 10), towers=2, color="#5A4A44"))
    o.append(f'<path d="M{f(w * 0.1)} {f(h + 10)} L {f(w * 0.3)} {f(h * 0.82)} L {f(w * 0.36)} {f(h * 0.86)} L {f(w * 0.52)} {f(h * 0.72)} L {f(w * 0.58)} {f(h * 0.76)} L {f(w * 0.7)} {f(h * 0.64)}" stroke="#1A0A08" stroke-width="7" fill="none"></path>')
    return "".join(o)

def flee(p, w, h, seed):
    """Let them that are in Judaea flee unto the mountains: small figures streaming up the road into the mountains, a house
    left with its door open, a cloak lying in the field."""
    o = [mk.defs(p, *ALL), sky(w, h, "#3A2A4A", "#C8906A"),
         f'<path d="M{f(w * 0.3)} {f(h * 0.7)} L {f(w * 0.56)} {f(h * 0.14)} L {f(w * 0.66)} {f(h * 0.24)} L {f(w * 0.8)} {f(h * 0.1)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h * 0.7)} Z" fill="#6A5A6A" stroke="{INK}" stroke-width="2.4"></path>',
         ground(w, h, h * 0.7, "#9A8A5A", dy=0), houses(w, h, h * 0.8, seed, x0=-10, x1=w * 0.3, hmin=0.18, hmax=0.26)]
    o.append(f'<path d="M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.5)} {f(h * 0.8)} {f(w * 0.6)} {f(h * 0.5)} {f(w * 0.68)} {f(h * 0.3)}" stroke="#C8B898" stroke-width="{f(max(5, h * 0.03))}" fill="none"></path>')
    r = random.Random(seed)
    for i in range(9):
        t = (i + 0.5) / 9; x = w * (0.34 + 0.32 * t); y = h * (0.94 - 0.6 * t)
        o.append(figure(p, x, y, y - h * (0.12 - 0.08 * t), r.choice(HEB), "man" if i % 2 else "woman"))
    o.append(f'<path d="M{f(w * 0.12)} {f(h * 0.94)} L {f(w * 0.2)} {f(h * 0.92)} L {f(w * 0.22)} {f(h * 0.96)} L {f(w * 0.1)} {f(h * 0.97)} Z" fill="#7A2A5A" stroke="{INK}" stroke-width="1.4"></path>')
    return "".join(o)

def lightning_sky(p, w, h, seed):
    """As the lightning cometh forth from the east, and is seen even unto the west: one great fork of lightning across the
    whole night sky over the dark land."""
    o = [night(w, h, seed, n=30, top="#05051A", bot="#2A2A5A"), hills(w, h, h * 0.72, seed, color="#14102A", amp=12, step=80)]
    pts = [(-10, h * 0.3)]; r = random.Random(seed)
    for i in range(1, 12): pts.append((w * i / 11, h * (0.2 + 0.2 * r.random())))
    d = "M" + " L ".join(f"{f(x)} {f(y)}" for x, y in pts)
    o.append(f'<path d="{d}" stroke="#FFF4C2" stroke-width="14" fill="none" opacity="0.3"></path><path d="{d}" stroke="#FFFFFF" stroke-width="4" fill="none"></path>')
    return "".join(o)

def eagles_gather(p, w, h, seed):
    """Wheresoever the carcase is, there will the eagles be gathered together: great birds circling low over a hollow in the
    desert (nothing in it drawn)."""
    o = [sky(w, h, "#FFD89A", "#F3B870"), hills(w, h, h * 0.6, seed, color="#C8985A", amp=12, step=80), ground(w, h, h * 0.7, "#D8B07A", dy=0)]
    r = random.Random(seed)
    for i in range(6):
        a = math.pi * 2 * i / 6
        o.append(eagle(w * 0.5 + math.cos(a) * w * 0.3, h * 0.36 + math.sin(a) * h * 0.14, max(0.4, h / 400) * r.uniform(0.7, 1.1), flip=i % 2 == 0))
    return "".join(o)

def darkened(p, w, h, seed):
    """The sun shall be darkened, and the moon shall not give her light, and the stars shall fall from heaven: a black sun
    with a thin rim of fire, a dark moon, stars streaking down over a dark land."""
    r = random.Random(seed)
    o = [bgr(w, h, "#05050E"), f'<circle cx="{f(w * 0.3)}" cy="{f(h * 0.3)}" r="{f(h * 0.12)}" fill="#0D0D0F" stroke="#C8502A" stroke-width="4"></circle>',
         f'<circle cx="{f(w * 0.76)}" cy="{f(h * 0.22)}" r="{f(h * 0.06)}" fill="#2A2A3A" stroke="#4A4A5A" stroke-width="2"></circle>']
    for _ in range(14):
        x = r.uniform(0, w); y = r.uniform(0, h * 0.6); L = r.uniform(30, 90)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(-L * 0.3)} {f(L)}" stroke="#F3EFE6" stroke-width="2" opacity="0.8"></path><circle cx="{f(x - L * 0.3)}" cy="{f(y + L)}" r="2.6" fill="#FFFFFF"></circle>')
    o.append(hills(w, h, h * 0.8, seed, color="#14101A", amp=10, step=80))
    return "".join(o)

def clouds_glory(p, w, h, seed):
    """The Son of man coming on the clouds of heaven with power and great glory, and his angels with a great sound of a
    trumpet: the heavens opened in a blaze of light above the clouds, figures of white light with trumpets at the four
    winds."""
    o = [sky(w, h, "#2A2A6A", "#FFE680"), rays(w * 0.5, h * 0.3, 40, 20, max(w, h), color="#FFFDF0", op=0.35), glow(w * 0.5, h * 0.3, h * 0.4, "#FFFFFF", 0.95, f"{p}g"),
         clouds(w, h * 0.5, seed, n=7, color="#F3EFE6", op=0.9, h=h), clouds(w, h * 0.66, seed + 1, n=6, color="#C8C0D8", op=0.9, h=h)]
    k = fit(h * 0.5, h * 0.28)
    o.append(mk.defs(p, *ALL))
    for x, fl in ((0.12, False), (0.88, True)):
        o.append(angel(p, w * x, h * 0.56, k, flip=fl, up=UP_HIGH))
    return "".join(o)

def fig_leaf(p, w, h, seed):
    """From the fig tree learn her parable: a fig tree putting forth its tender leaves in spring sunshine."""
    b = h * 0.94
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.56, seed, color="#9AAA7A", amp=10, step=80), ground(w, h, h * 0.7, "#9AAA5A", dy=0),
         fig_tree(w * 0.5, b, max(0.6, (b - h * 0.1) / 160), fruit=False, seed=seed)]
    return "".join(o)

def flood_ark(p, w, h, seed):
    """As were the days of Noah: the ark riding the flood under a heavy sky, nothing else above the water."""
    o = [sky(w, h, "#2A2A3A", "#6A7A8A"), rain(w, h, seed, n=50), sea(w, h, h * 0.62, seed, color="#2A4A6A", deep="#14243A", rough=True),
         ark_afloat(w * 0.5, h * 0.66, w * 0.6, f"{p}ak")]
    return "".join(o)

def taken_left(p, w, h, seed):
    """Two men in the field, one taken and one left; two women grinding at the mill: a field with one man at work and,
    beside him, only his hoe lying where the other stood; a hand-mill with one woman at it and the other place empty."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#9AAA7A", amp=10, step=80), ground(w, h, h * 0.5, "#A8885A", dy=0),
         f'<path d="M{f(w * 0.5)} {f(h * 0.5)} L {f(w * 0.5)} {f(h + 10)}" stroke="#F3EFE6" stroke-width="2" stroke-dasharray="6 6"></path>']
    s = fit(b, max(h * 0.3, b - 220))
    hoe = '<path d="M-30 -150 L -50 0 M-60 -6 L -40 6" stroke="#5A3A22" stroke-width="5"></path>'
    o.append(man(p, w * 0.16, b, s, "#6A5A3A", extra=hoe))
    o.append(f'<path d="M{f(w * 0.3)} {f(b - 4)} L {f(w * 0.42)} {f(b - 14)} M{f(w * 0.3)} {f(b - 4)} l -8 6" stroke="#5A3A22" stroke-width="5"></path>')
    mx = w * 0.74
    o.append(f'<ellipse cx="{f(mx)}" cy="{f(b - 10 * s)}" rx="{f(40 * s)}" ry="{f(12 * s)}" fill="#8A8478" stroke="{INK}" stroke-width="2"></ellipse>'
             f'<ellipse cx="{f(mx)}" cy="{f(b - 20 * s)}" rx="{f(34 * s)}" ry="{f(10 * s)}" fill="#A89A8A" stroke="{INK}" stroke-width="2"></ellipse>')
    o.append(E.kneel(mx - 70 * s, b, s * 0.8, color="#7A3A5A", skin=SKIN))
    return "".join(o)

def thief(p, w, h, seed):
    """If the master of the house had known in what watch the thief was coming: a house at night, a hole broken through its
    mud-brick wall, the lamp out, the street empty."""
    o = [night(w, h, seed, n=60, top="#05051A", bot="#1E1838"), moon(w * 0.82, h * 0.18, max(8, h * 0.04))]
    o.append(f'<rect x="{f(w * 0.2)}" y="{f(h * 0.3)}" width="{f(w * 0.56)}" height="{f(h * 0.6)}" fill="#6A5A54" stroke="{INK}" stroke-width="2.4"></rect>')
    for k in range(6):
        y = h * (0.34 + 0.1 * k)
        o.append(f'<path d="M{f(w * 0.2)} {f(y)} L {f(w * 0.76)} {f(y)}" stroke="#4A3E3A" stroke-width="1.4"></path>')
    o.append(f'<path d="M{f(w * 0.46)} {f(h * 0.9)} L {f(w * 0.44)} {f(h * 0.7)} L {f(w * 0.5)} {f(h * 0.62)} L {f(w * 0.58)} {f(h * 0.7)} L {f(w * 0.56)} {f(h * 0.9)} Z" fill="#05050A" stroke="{INK}" stroke-width="2"></path>')
    r = random.Random(seed)
    for _ in range(7):
        x = w * 0.5 + r.uniform(-w * 0.12, w * 0.12)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.9 + r.uniform(-4, 10))}" width="{f(w * 0.03)}" height="{f(h * 0.025)}" fill="#6A5A54" stroke="{INK}" stroke-width="1"></rect>')
    o.append(ground(w, h, h * 0.92, "#1E1A20", dy=0))
    return "".join(o)

def steward(p, w, h, seed, evil=False):
    """The faithful and wise servant, set over the household to give them their food in due season: the steward handing out
    loaves to the household at the door; evil=True: the same house at night, the cups overturned, the servant asleep among
    the drunken."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#B8987A" if not evil else "#4A3438", floor="#8A6A4A" if not evil else "#3A2A2A")]
    s = fit(b, max(h * 0.24, b - 230))
    if evil:
        o.append(f'<rect x="{f(w * 0.2)}" y="{f(b - 30 * s)}" width="{f(w * 0.6)}" height="{f(12 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
        for x in (0.3, 0.5, 0.7):
            o.append(f'<g transform="rotate(80 {f(w * x)} {f(b - 30 * s)})">' + cup(w * x, b - 30 * s, s * 0.2) + '</g>')
        o.append(seated(w * 0.14, b, s * 0.8, "#6A2A3A", head=None, beard="#2A1A10") + seated(w * 0.86, b, s * 0.8, "#5A4A3A", head=None, beard="#2A1A10", flip=True))
    else:
        bread = '<ellipse cx="-58" cy="-152" rx="14" ry="7" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
        o.append(man(p, w * 0.32, b, s, "#3A5A4A", up=UP_BLESS, extra=bread))
        for i, x in enumerate((0.52, 0.62, 0.72)):
            o.append(man(p, w * x, b, s * (0.94 - 0.08 * (i == 2)), random.Random(seed + i).choice(HEB), flip=True) if i != 1 else woman_fig(p, w * x, b, s * 0.9, "#8A3A5A", flip=True))
        o.append(mk.person(p, round(w * 0.84), round(b), round(s * 0.5, 3), body=SKIN, cloth="#C8783A", kind="Tunic", sw=3, flip=True))
    return "".join(o)

def virgins(p, w, h, seed, stage="wait"):
    """The ten virgins with their lamps: stage='wait' the ten sitting asleep by the road at night, lamps beside them;
    'cry' at midnight the ten risen, five lamps burning bright and five guttering; 'shut' the door of the feast shut and lit
    from within, five standing outside in the dark with dead lamps."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), night(w, h, seed, n=70, top="#05051A", bot="#1E1838")]
    o.append(f'<rect x="{f(w * 0.66)}" y="{f(h * 0.3)}" width="{f(w * 0.34 + 10)}" height="{f(b - h * 0.3)}" fill="#B8987A" stroke="{INK}" stroke-width="2.4"></rect>')
    door = "#5A3A22" if stage == "shut" else "#FFC14D"
    o.append(f'<rect x="{f(w * 0.76)}" y="{f(h * 0.5)}" width="{f(w * 0.12)}" height="{f(b - h * 0.5)}" fill="{door}" stroke="{INK}" stroke-width="2"></rect>')
    if stage == "shut":
        o.append(f'<path d="M{f(w * 0.76)} {f(h * 0.5)} L {f(w * 0.88)} {f(h * 0.5)}" stroke="#FFC14D" stroke-width="3"></path>')
    o.append(ground(w, h, b, "#1E1A20", dy=0))
    s = fit(b, max(h * 0.4, b - 200))
    k = max(0.5, s)
    def lamp_(x, y, lit):
        g = A.lamp(x, y, k * 0.5)
        return (glow(x + 8 * k, y - 6 * k, 30 * k, "#FFE680", 0.8, f"{p}l{int(x)}") + g) if lit else g.replace(E.flame(26, -4, 8, 22, 0.1), "")
    n = 10 if stage != "shut" else 5
    for i in range(n):
        x = w * (0.04 + 0.064 * i) if stage != "shut" else w * (0.08 + 0.12 * i)
        lit = (stage == "cry" and i % 2 == 0)
        if stage == "wait":
            o.append(seated(x, b, s * 0.6, "#F3EFE6", head="#E8E2D6", beard=""))
            o.append(lamp_(x + 20 * s, b - 2, False))
        else:
            o.append(woman_fig(p, x, b, s * 0.8, "#F3EFE6", "#E8E2D6", up=[(-22, -158), (-34, -150), (-44, -142)]))
            o.append(lamp_(x - 50 * s * 0.8, b - 140 * s * 0.8, lit))
    return "".join(o)

def talents(p, w, h, seed, stage="give"):
    """The talents: stage='give' the master at his door delivering the bags of money to three servants; 'dig' the third
    servant digging a hole in the field to hide his one talent; 'reckon' the master seated, the two servants presenting
    their doubled bags and the third holding out his one, earth still on it."""
    b = h * 0.94
    s = fit(b, max(h * 0.3, b - 220))
    bag = lambda n: "".join(f'<path d="M{-62 + i * 8} -130 C {-72 + i * 8} -118 {-66 + i * 8} -104 {-56 + i * 8} -104 C {-46 + i * 8} -104 {-40 + i * 8} -118 {-50 + i * 8} -130 Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="1.4"></path>' for i in range(n))
    hold = [(-22, -158), (-40, -136), (-56, -120)]
    master = lambda x, fl=False: man(p, x, b, s, "#2A4A6A", kind="Robe", flip=fl, extra=A.headcloth("#E8E2D6", cord="#E8B830") + GREY_BEARD)
    if stage == "dig":
        o = [mk.defs(p, *ALL), sky(w, h, "#5A3A6A", "#FFC890"), hills(w, h, h * 0.5, seed, color="#8A7A5A", amp=10, step=80), ground(w, h, h * 0.6, "#8A6A4A", dy=0),
             f'<ellipse cx="{f(w * 0.6)}" cy="{f(b - 4)}" rx="{f(60 * s)}" ry="{f(16 * s)}" fill="#3A2A1A" stroke="{INK}" stroke-width="2"></ellipse>',
             f'<path d="M{f(w * 0.7)} {f(b)} C {f(w * 0.72)} {f(b - 30 * s)} {f(w * 0.8)} {f(b - 30 * s)} {f(w * 0.84)} {f(b)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></path>']
        mattock = '<path d="M-30 -160 L -60 -40 M-70 -46 L -48 -36" stroke="#5A3A22" stroke-width="6"></path>'
        o.append(man(p, w * 0.4, b, s, "#6A6A72", extra=mattock))
        return "".join(o)
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.8, seed, hmin=0.36, hmax=0.5, stairs=False), pavement(w, h, h * 0.8)]
    if stage == "give":
        o.append(master(w * 0.2, False))
        for i, n in enumerate((5, 2, 1)):
            o.append(man(p, w * (0.44 + 0.16 * i), b, s * 0.94, ["#5A6A3A", "#6A5A3A", "#6A6A72"][i], flip=True, up=hold, extra=bag(n)))
    else:
        o.append(seated(w * 0.16, b, s * 0.9, "#2A4A6A", head="#E8E2D6", beard="#9A948A", band=True))
        for i, n in enumerate((10, 4, 1)):
            o.append(man(p, w * (0.42 + 0.18 * i), b, s * 0.94, ["#5A6A3A", "#6A5A3A", "#6A6A72"][i], flip=True, up=hold, extra=bag(n)))
    return "".join(o)

def throne_glory(p, w, h, seed):
    """When the Son of man shall come in his glory and sit on the throne of his glory, and all the nations gathered before
    him: a throne of white and gold light high on steps, Jesus seated in the light, figures of light about it; below, the
    sheep set on the right hand and the goats on the left."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#1A1A4A", "#5A4A8A"), glow(w * 0.5, h * 0.3, h * 0.5, "#FFE680", 0.9, f"{p}g"), rays(w * 0.5, h * 0.3, 40, 30, max(w, h), color="#FFF4C2", op=0.25)]
    tx, ty = w * 0.5, h * 0.52
    for k in range(4):
        o.append(f'<rect x="{f(tx - (90 - 14 * k) * h / 400)}" y="{f(ty - k * 10 * h / 400)}" width="{f((180 - 28 * k) * h / 400)}" height="{f(10 * h / 400)}" fill="#F3EFE6" stroke="#E8B830" stroke-width="1.6"></rect>')
    s = fit(ty, h * 0.12) * 0.9
    o.append(f'<path d="M{f(tx - 50 * s)} {f(ty - 40 * h / 400)} L {f(tx - 50 * s)} {f(ty - 40 * h / 400 - 200 * s)} L {f(tx + 50 * s)} {f(ty - 40 * h / 400 - 200 * s)} L {f(tx + 50 * s)} {f(ty - 40 * h / 400)} Z" fill="#FFF4C2" stroke="#E8B830" stroke-width="3"></path>')
    o.append(jesus_seated(tx, ty - 40 * h / 400, s * 0.9).replace(JESUS_TUNIC, "#FFFFFF"))
    ks = max(0.3, h / 900)
    for i in range(5):
        o.append(E.sheep(w * (0.08 + 0.07 * i), b - (i % 2) * 10, ks, flip=True))
        o.append(goat(w * (0.64 + 0.07 * i), b - (i % 2) * 10, ks * 0.9))
    o.append(angel(p, w * 0.14, h * 0.6, s * 0.7) + angel(p, w * 0.86, h * 0.6, s * 0.7, flip=True))
    return "".join(o)

def mercies(p, w, h, seed):
    """I was hungry, thirsty, a stranger, naked, sick, in prison: six small square frames in a row — a loaf, a cup of water,
    an open door, a cloak, a bed with a lamp, prison bars with a hand at them."""
    o = [bgr(w, h, "#12113A")]
    n = 6; pad = 10; cw = (w - pad * (n + 1)) / n; ch = min(cw * 1.1, h - 40)
    y0 = (h - ch) / 2
    labels = ("HUNGRY", "THIRSTY", "A STRANGER", "NAKED", "SICK", "IN PRISON")
    for i in range(n):
        x0 = pad + i * (cw + pad); cx, cy = x0 + cw / 2, y0 + ch * 0.5; k = cw / 100
        o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(cw)}" height="{f(ch)}" fill="#F3E8C8" stroke="#E8B830" stroke-width="2"></rect>')
        if i == 0: o.append(loaf(cx, cy, k * 2))
        elif i == 1: o.append(cup(cx, cy + 30 * k, k * 0.5, color="#B5652E").replace("#5A0A1A", "#4AA0D0"))
        elif i == 2: o.append(f'<rect x="{f(cx - 20 * k)}" y="{f(cy - 36 * k)}" width="{f(40 * k)}" height="{f(66 * k)}" fill="#FFE680" stroke="{INK}" stroke-width="2"></rect><path d="M{f(cx - 20 * k)} {f(cy - 36 * k)} L {f(cx - 34 * k)} {f(cy - 30 * k)} L {f(cx - 34 * k)} {f(cy + 36 * k)} L {f(cx - 20 * k)} {f(cy + 30 * k)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></path>')
        elif i == 3: o.append(f'<path d="M{f(cx - 30 * k)} {f(cy + 34 * k)} L {f(cx - 22 * k)} {f(cy - 30 * k)} L {f(cx + 22 * k)} {f(cy - 30 * k)} L {f(cx + 30 * k)} {f(cy + 34 * k)} Z" fill="#7A2A5A" stroke="{INK}" stroke-width="2"></path>')
        elif i == 4: o.append(f'<rect x="{f(cx - 36 * k)}" y="{f(cy + 6 * k)}" width="{f(72 * k)}" height="{f(14 * k)}" fill="#8A5A30" stroke="{INK}" stroke-width="2"></rect><circle cx="{f(cx - 26 * k)}" cy="{f(cy)}" r="{f(8 * k)}" fill="#C98E66" stroke="{INK}" stroke-width="1.6"></circle>' + A.lamp(cx + 20 * k, cy - 24 * k, k * 0.5))
        else: o.append("".join(f'<rect x="{f(cx - 30 * k + j * 15 * k)}" y="{f(cy - 36 * k)}" width="{f(5 * k)}" height="{f(72 * k)}" fill="#6A6A72" stroke="{INK}" stroke-width="1"></rect>' for j in range(5)))
        o.append(label(cx, y0 + ch - 8, labels[i], "#0D0D0F", 8))
    return "".join(o)
