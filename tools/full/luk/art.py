"""Drawings for the Luke volume. Luke shares many scenes with Matthew and Mark, so this starts from all of their drawings
(`from mrk.art9 import *`, which carries mat.art … mat.art11 and mrk.art … mrk.art8) and adds Luke's own: here the first
two chapters — the preface's writing-desk, the priest's house in the hill country, the holy place with the golden altar of
incense, Gabriel in the house at Nazareth, the visitation, the naming of John, the dayspring; the journey to Bethlehem,
the manger, the shepherds and the heavenly host, the temple with Simeon and Anna, the boy among the doctors.

Jesus at a distance is only ever ntcast.jesus_fig; the infant Jesus is swaddled, small, in soft light (no face drawn).
Angels are figures of white light with a gold rim and no face (mat.art.angel), without wings; God is never drawn (light,
the Voice box). Every function takes (p, w, h, seed, ...) — p, a prefix unique to the panel, names the figure defs and
gradients."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from mrk.art9 import *
from mrk.art9 import (f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, gerasene_fig, jesus_risen,
                      roman_fig, torch, jesus_kneel, light_seated, WOMEN3, PURPLE)
import mk
from ntcast import jesus_fig, ROBES, JESUS_TUNIC, JESUS_MANTLE, JESUS_SKIN, JESUS_HAIR
from exo import art as A
from job.art import smoke, seated
import ruth1 as R1, numbers1 as N, exodus as E

GOLD = "#E8B830"
ZACH_C, ELIS_C, ELIS_VEIL = "#F3EFE6", "#3A5A5A", "#1F5A5A"
SHEP = ["#6A5A3A", "#7A5A3A", "#5A4A3A", "#8A6A4A"]

def footed(fn, color="#8A6A4A", room=76):
    """A drawing fn(w, h) kept clear of the chapter's end mark: drawn in the panel less `room` px at the bottom, over a strip
    of ground in `color` (the end mark sits on the strip, never over a figure)."""
    return lambda w, h: (f'<rect x="-10" y="{f(h - room - 4)}" width="{f(w + 20)}" height="{f(room + 14)}" fill="{color}" stroke="{INK}" stroke-width="2"></rect>'
                         f'<g>{fn(w, h - room)}</g>')

# ---- people -------------------------------------------------------------------------------------------------------------
def zach_fig(p, x, y, s, flip=False, up=None, extra=""):
    """Zacharias the priest at a distance: a white robe, a white headcloth with a blue band, a white beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=ZACH_C, kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth("#E8E2D6", cord="#3A6AA8") + A.WHITE_BEARD + extra)

def elis_fig(p, x, y, s, flip=False, up=None, extra=""):
    """Elisabeth at a distance: a slate-teal robe, a deep teal veil."""
    return woman_fig(p, x, y, s, ELIS_C, ELIS_VEIL, flip=flip, up=up, extra=extra)

def shepherd_fig(p, x, y, s, i=0, flip=False, up=None):
    """One of the shepherds: a rough tunic, a headcloth with a cord, a staff; i=1 the old one with a grey beard."""
    c = SHEP[i % 4]
    staff = '<path d="M30 -170 C 40 -186 52 -182 50 -168 M30 -170 L 30 4" stroke="#5A3A22" stroke-width="5" fill="none"></path>'
    beard = A.WHITE_BEARD.replace("#E8E2D6", "#9A948A") if i % 4 == 1 else A.BLACK_BEARD
    return mk.person(p, round(x), round(y), round(s, 3), body="#B98A6E", cloth=c, kind="Tunic", sw=3, flip=flip, up=up,
                     extra=A.headcloth(["#7A6A4A", "#8A7A5A", "#6A5A3A", "#9A8A6A"][i % 4]) + beard + (staff if up is None else ""))

def swaddled(x, y, s=1.0, uid="sw", light=True):
    """The babe wrapped in swaddling clothes: a small bundle of white linen, the bands across it, the head a plain round of
    skin (no face drawn), in a soft light."""
    o = glow(x, y - 4 * s, 60 * s, "#FFF4C2", 0.8, uid) if light else ""
    return o + (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><ellipse cx="0" cy="0" rx="24" ry="11" fill="#FFFDF0" stroke="{INK}" stroke-width="2"></ellipse>'
                '<path d="M-16 -7 L 8 8 M-8 -10 L 16 4 M-20 0 L -2 10" stroke="#D8C8A0" stroke-width="2"></path>'
                f'<circle cx="22" cy="-3" r="8" fill="{JESUS_SKIN}" stroke="{INK}" stroke-width="2"></circle>'
                '<path d="M14 -6 C 16 -14 28 -14 30 -6" fill="#FFFDF0" stroke="#0D0D0F" stroke-width="1.4"></path></g>')

def kneel_w(x, y, s, color, veil_c, flip=False, skin=SKIN):
    """A woman kneeling (exodus.kneel) with her veil over her head and falling down her back to the shoulders."""
    sx = -s if flip else s
    return (E.kneel(x, y, s, color=color, flip=flip, skin=skin)
            + f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})"><path d="M0 -110 C -2 -136 14 -142 26 -137 C 33 -134 35 -127 33 -121 '
              f'L 29 -123 C 27 -131 13 -133 9 -122 L 8 -100 L -8 -92 Z" fill="{veil_c}" stroke="#0D0D0F" stroke-width="1.8"></path></g>')

def boy_fig(p, x, y, s, flip=False, up=None):
    """The boy Jesus at twelve at a distance: the undyed robe, dark-brown hair, beardless, a little shorter than the men."""
    hair = f'<path d="M-13.5 -186 C -16 -205 16 -205 13.5 -186 L 14 -176 C 10 -192 -10 -192 -14 -176 Z" fill="{JESUS_HAIR}" stroke="{INK}" stroke-width="1.3"></path>'
    return mk.person(p, round(x), round(y), round(s, 3), body=JESUS_SKIN, cloth=JESUS_TUNIC, kind="Robe", sw=3, flip=flip, up=up, extra=hair)

def lampstand(x, b, s=1.0):
    """The golden candlestick of the holy place: seven lamps on branches, each lit."""
    o = [f'<path d="M{f(x)} {f(b)} L {f(x)} {f(b - 150 * s)}" stroke="{GOLD}" stroke-width="{f(7 * s)}"></path>',
         f'<path d="M{f(x - 26 * s)} {f(b)} L {f(x + 26 * s)} {f(b)} L {f(x + 10 * s)} {f(b - 14 * s)} L {f(x - 10 * s)} {f(b - 14 * s)} Z" fill="{GOLD}" stroke="{INK}" stroke-width="1.6"></path>']
    for k in (1, 2, 3):
        o.append(f'<path d="M{f(x - 22 * k * s)} {f(b - 150 * s)} C {f(x - 22 * k * s)} {f(b - (100 - 14 * k) * s)} {f(x)} {f(b - 80 * s)} {f(x)} {f(b - 80 * s)} '
                 f'M{f(x + 22 * k * s)} {f(b - 150 * s)} C {f(x + 22 * k * s)} {f(b - (100 - 14 * k) * s)} {f(x)} {f(b - 80 * s)} {f(x)} {f(b - 80 * s)}" stroke="{GOLD}" stroke-width="{f(5 * s)}" fill="none"></path>')
    for k in range(-3, 4):
        lx = x + 22 * k * s
        o.append(f'<ellipse cx="{f(lx)}" cy="{f(b - 152 * s)}" rx="{f(7 * s)}" ry="{f(3 * s)}" fill="{GOLD}" stroke="{INK}" stroke-width="1.2"></ellipse>' + E.flame(lx, b - 154 * s, 4 * s, 14 * s, 4))
    return "".join(o)

def incense_altar(x, b, s=1.0, seed=1, smoke_=True):
    """The golden altar of incense: a small square altar with horns at its corners, a cloud of incense rising."""
    o = []
    if smoke_: o.append(smoke(x, b - 110 * s, 9, seed, color="#E8E2F0", op=0.45, k=s * 1.4))
    o.append(f'<rect x="{f(x - 40 * s)}" y="{f(b - 100 * s)}" width="{f(80 * s)}" height="{f(100 * s)}" fill="{GOLD}" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(x - 46 * s)}" y="{f(b - 106 * s)}" width="{f(92 * s)}" height="{f(10 * s)}" fill="#C8963E" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(x - 30 * s)} {f(b - 70 * s)} L {f(x + 30 * s)} {f(b - 70 * s)} M{f(x - 30 * s)} {f(b - 30 * s)} L {f(x + 30 * s)} {f(b - 30 * s)}" stroke="#A8762E" stroke-width="2"></path>')
    for dx in (-44, 44):
        o.append(f'<path d="M{f(x + dx * s - 6 * s)} {f(b - 106 * s)} L {f(x + dx * s)} {f(b - 122 * s)} L {f(x + dx * s + 6 * s)} {f(b - 106 * s)} Z" fill="{GOLD}" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(f'<ellipse cx="{f(x)}" cy="{f(b - 108 * s)}" rx="{f(18 * s)}" ry="{f(5 * s)}" fill="#D7261E" stroke="{INK}" stroke-width="1.4"></ellipse>')
    return "".join(o)

def veil_curtain(x0, x1, top, b):
    """The veil before the most holy place: a heavy curtain of blue, purple and scarlet, hanging in folds."""
    o = [f'<rect x="{f(x0)}" y="{f(top)}" width="{f(x1 - x0)}" height="{f(b - top)}" fill="#3A1A4A" stroke="{INK}" stroke-width="2.4"></rect>']
    n = 9
    for k in range(n):
        xx = x0 + (x1 - x0) * (k + 0.5) / n
        c = ["#2A3A7A", "#5A1A6A", "#8A1A2A"][k % 3]
        o.append(f'<rect x="{f(xx - (x1 - x0) / n / 2)}" y="{f(top)}" width="{f((x1 - x0) / n)}" height="{f(b - top)}" fill="{c}" opacity="0.7"></rect>'
                 f'<path d="M{f(xx)} {f(top)} L {f(xx)} {f(b)}" stroke="#0D0D0F" stroke-width="1" opacity="0.5"></path>')
    o.append(f'<rect x="{f(x0 - 6)}" y="{f(top - 10)}" width="{f(x1 - x0 + 12)}" height="12" fill="{GOLD}" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o)

# ---- Luke 1 -------------------------------------------------------------------------------------------------------------
def writing_desk(p, w, h, seed):
    """To write unto thee in order, most excellent Theophilus: a writing-desk at evening, a scroll unrolled on it half written
    (ruled lines, no letters), a reed pen and an inkhorn, other rolls stacked beside, a clay lamp."""
    b = h * 0.9
    o = [bgr(w, h, "#2A2030"), glow(w * 0.5, h * 0.55, h * 0.8, "#FFE680", 0.4, f"{p}g"),
         f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<path d="M-10 {f(h * 0.62)} L {f(w + 10)} {f(h * 0.62)}" stroke="#8A6A4A" stroke-width="4"></path>',
         scroll(w * 0.46, h * 0.72, min(w * 0.5, h * 1.0), h * 0.2, lines=5)]
    for i in range(3):                                           # rolls stacked on the desk's near edge
        x = w * 0.84 + i * 14; y = h * 0.86 - i * 16
        o.append(f'<rect x="{f(x - 40)}" y="{f(y - 10)}" width="80" height="20" rx="9" fill="#E8D8B0" stroke="{INK}" stroke-width="2"></rect>'
                 f'<ellipse cx="{f(x + 40)}" cy="{f(y)}" rx="5" ry="10" fill="#C8A878" stroke="{INK}" stroke-width="1.6"></ellipse>')
    o.append(f'<path d="M{f(w * 0.7)} {f(h * 0.7)} L {f(w * 0.6)} {f(h * 0.52)}" stroke="#C8A060" stroke-width="4" stroke-linecap="round"></path>'
             f'<rect x="{f(w * 0.72)}" y="{f(h * 0.66)}" width="26" height="22" fill="#3A2A1E" stroke="{INK}" stroke-width="2"></rect>')
    o.append(clay_lamp(w * 0.12, h * 0.8, max(0.7, h / 260)))
    return "".join(o)

def priest_home(p, w, h, seed):
    """Zacharias and Elisabeth, both righteous, well stricken in years: their house in the hill country of Judæa at evening,
    the two old ones standing at the door, a vine on the wall, the terraced hills behind."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5A4A7A", "#FFC890"), sun(w * 0.86, h * 0.42, 16, color="#FFE680", op=0.35),
         hills(w, h, h * 0.4, seed, color="#8A7A6A", amp=18, step=80), hills(w, h, h * 0.52, seed + 1, color="#7A8A5A", amp=12, step=60),
         ground(w, h, h * 0.8, "#A8946A", dy=0)]
    hx0, hx1, top = w * 0.08, w * 0.52, h * 0.3
    o.append(f'<rect x="{f(hx0)}" y="{f(top)}" width="{f(hx1 - hx0)}" height="{f(b - top)}" fill="#E0CFA8" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(hx0 - 6)}" y="{f(top - 8)}" width="{f(hx1 - hx0 + 12)}" height="10" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.24)} {f(b)} L {f(w * 0.24)} {f(b - h * 0.32)} Q {f(w * 0.3)} {f(b - h * 0.4)} {f(w * 0.36)} {f(b - h * 0.32)} L {f(w * 0.36)} {f(b)} Z" fill="#3A2A1E" stroke="{INK}" stroke-width="2"></path>'
             f'<rect x="{f(w * 0.42)}" y="{f(top + h * 0.1)}" width="{f(w * 0.05)}" height="{f(h * 0.07)}" fill="#FFC14D" stroke="{INK}" stroke-width="1.6"></rect>')
    s = fit(b, max(h * 0.2, b - 230))
    o.append(zach_fig(p, w * 0.62, b, s, flip=True))
    o.append(elis_fig(p, w * 0.74, b, s * 0.94, flip=True))
    return "".join(o)

def hour_incense(p, w, h, seed):
    """The whole multitude of the people praying without at the hour of incense: the court of the temple, the sanctuary
    front high above, a thin smoke of incense going up from within, the people standing with hands lifted."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), temple(w * 0.5, h * 0.58, w * 0.62), pavement(w, h, h * 0.58),
         smoke(w * 0.5, h * 0.2, 7, seed, color="#F3EFE6", op=0.55, k=max(0.6, h / 360))]
    s = fit(b, max(h * 0.4, b - 180))
    r = random.Random(seed)
    for i in range(9):
        x = w * (0.06 + 0.88 * i / 8) + r.uniform(-6, 6)
        if i % 3 == 1: o.append(woman_fig(p, x, b - r.uniform(0, 6), s * 0.9, r.choice(HEB), r.choice(["#4A5A6A", "#6A3A4A", "#3A4A3A"]), up=UP_HIGH if i % 2 else None))
        else: o.append(man(p, x, b - r.uniform(0, 6), s, r.choice(HEB), up=UP_HIGH if i % 2 else None))
    return "".join(o)

def holy_place(p, w, h, seed, angel_=True, zach=True, afraid=False):
    """Within the temple of the Lord: the holy place in lamplight, the veil hanging behind, the golden candlestick, the altar
    of incense with its cloud going up; Zacharias in white with the censer; angel_=True: the angel of the Lord standing on
    the right side of the altar — a figure of white light with a gold rim, no face; afraid=True: Zacharias drawn back."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bgr(w, h, "#2A1A2A"), veil_curtain(w * 0.3, w * 0.98, h * 0.04, b),
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A6A3A" stroke="{INK}" stroke-width="2"></rect>',
         glow(w * 0.56, b - h * 0.3, h * 0.6, "#FFE680", 0.35, f"{p}g")]
    k = max(0.45, min(1.0, h / 420))
    o.append(lampstand(w * 0.12, b, k * 1.1))
    o.append(incense_altar(w * 0.56, b, k, seed))
    s = fit(b, max(h * 0.12, b - 250))
    if angel_:
        o.append(glow(w * 0.76, b - 110 * s, 170 * s, "#FFFFFF", 0.7, f"{p}ag"))
        o.append(angel(p, w * 0.76, b, s * 1.02, flip=False, up=UP_BLESS))
    if zach:
        censer = '<path d="M-60 -150 L -62 -120" stroke="#E8B830" stroke-width="2"></path><path d="M-72 -120 L -52 -120 L -56 -108 L -68 -108 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>'
        if afraid: o.append(zach_fig(p, w * 0.32, b, s * 0.96, up=[(-22, -158), (-34, -184), (-30, -206)]))
        else: o.append(zach_fig(p, w * 0.34, b, s * 0.96, flip=True, up=[(-22, -158), (-44, -152), (-60, -150)], extra=censer))
    return "".join(o)

def dumb_signs(p, w, h, seed):
    """When he came out he could not speak unto them, and continued making signs: Zacharias on the steps of the porch with his
    hand lifted, the people below looking up at him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), temple(w * 0.42, h * 0.62, w * 0.7), pavement(w, h, h * 0.62)]
    for k in range(4):                                         # the steps
        y = h * 0.62 + k * h * 0.04
        o.append(f'<rect x="{f(w * 0.18 - k * w * 0.03)}" y="{f(y)}" width="{f(w * 0.48 + k * w * 0.06)}" height="{f(h * 0.04)}" fill="#E8DCC0" stroke="{INK}" stroke-width="1.6"></rect>')
    s = fit(h * 0.62, max(h * 0.24, h * 0.62 - 170))
    o.append(zach_fig(p, w * 0.42, h * 0.62, s, up=UP_HIGH))
    s2 = fit(b, max(h * 0.5, b - 160))
    o.append(crowd(p, w * 0.06, w * 0.96, b, b - 160 * s2 / 0.8, 8, seed, flip=None))
    return "".join(o)

def hid_herself(p, w, h, seed):
    """She hid herself five months: Elisabeth alone within her house, by the window, the lamp lit, the hills beyond."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#B8987A", window=(w * 0.64, w * 0.12)),
         f'<g transform="translate({f(w * 0.64)} {f(h * 0.2)})">{hills(w * 0.12, w * 0.156, w * 0.1, seed, color="#7A8A5A", amp=4, step=20)}</g>',
         f'<path d="M{f(w * 0.64)} {f(h * 0.2)} L {f(w * 0.76)} {f(h * 0.2)} L {f(w * 0.56)} {f(b)} L {f(w * 0.24)} {f(b)} Z" fill="#FFF4C2" opacity="0.3"></path>',
         clay_lamp(w * 0.1, b - 2, max(0.6, h / 300))]
    s = fit(b, max(h * 0.16, b - 250))
    o.append(elis_fig(p, w * 0.42, b, s, flip=False))
    return "".join(o)

def annunciation(p, w, h, seed, departed=False):
    """The angel Gabriel came in unto her: Mary in the house at Nazareth, the doorway full of light, the angel a figure of
    white light with a gold rim, no face; departed=True: Mary alone, bowed, the light fading from the door."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#B8987A", window=(w * 0.1, w * 0.08)),
         f'<path d="M{f(w * 0.62)} {f(b)} L {f(w * 0.62)} {f(h * 0.26)} Q {f(w * 0.74)} {f(h * 0.16)} {f(w * 0.86)} {f(h * 0.26)} L {f(w * 0.86)} {f(b)} Z" fill="#FFF4C2" stroke="{INK}" stroke-width="2.4"></path>',
         clay_lamp(w * 0.08, b - 2, max(0.6, h / 300))]
    s = fit(b, max(h * 0.14, b - 250))
    if not departed:
        o.append(glow(w * 0.74, b - 120 * s, 220 * s, "#FFFFFF", 0.8, f"{p}ag"))
        o.append(f'<path d="M{f(w * 0.62)} {f(b)} L {f(w * 0.3)} {f(b)} L {f(w * 0.62)} {f(b - 60)} Z" fill="#FFF4C2" opacity="0.4"></path>')
        o.append(angel(p, w * 0.74, b, s * 1.02, flip=False, up=UP_BLESS))
        o.append(mary_fig(p, w * 0.36, b, s * 0.94, up=[(-22, -158), (-6, -140), (8, -150)]))
    else:
        o.append(glow(w * 0.74, b - 120 * s, 160 * s, "#FFF4C2", 0.4, f"{p}ag"))
        o.append(kneel_w(w * 0.4, b, s * 0.9, MARY_C, "#3A6AA8"))
    return "".join(o)

def hill_road(p, w, h, seed, who="mary"):
    """Mary arose and went into the hill country with haste: the road winding up through the terraced hills of Judah, a city
    on a height, Mary walking quickly."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, color="#A89A7A", amp=22, step=70),
         hill_town(w * 0.78, h * 0.5, w * 0.3, h * 0.2, seed, hill="#9A8A6A"),
         hills(w, h, h * 0.56, seed + 1, color="#8A9A6A", amp=14, step=60)]
    for k in range(3):
        y = h * (0.62 + 0.08 * k)
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 10)} {f(w * 0.6)} {f(y + 6)} {f(w + 10)} {f(y - 4)}" stroke="#6A7A4A" stroke-width="2" fill="none"></path>')
    o.append(ground(w, h, h * 0.82, "#B8A06A", dy=-8))
    o.append(f'<path d="M-10 {f(b + 8)} C {f(w * 0.3)} {f(b - h * 0.02)} {f(w * 0.6)} {f(h * 0.7)} {f(w * 0.78)} {f(h * 0.52)}" stroke="#D8C08A" stroke-width="{f(h * 0.06)}" fill="none" opacity="0.8"></path>')
    s = fit(b, max(h * 0.3, b - 220))
    o.append(mary_fig(p, w * 0.34, b, s, up=[(-22, -158), (-40, -140), (-52, -118)]))
    return "".join(o)

def visitation(p, w, h, seed):
    """Mary entered into the house of Zacharias and saluted Elisabeth: at the door of the house in the hill country, the two
    women meeting, Elisabeth's arms held out to her, a warm light about them; Zacharias standing back in the doorway."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFE6B0"), hills(w, h, h * 0.42, seed, color="#8A9A6A", amp=16, step=70)]
    hx0, hx1, top = w * 0.56, w * 1.02, h * 0.24
    o.append(f'<rect x="{f(hx0)}" y="{f(top)}" width="{f(hx1 - hx0)}" height="{f(b - top)}" fill="#E0CFA8" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(hx0 - 6)}" y="{f(top - 8)}" width="{f(hx1 - hx0 + 12)}" height="10" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.74)} {f(b)} L {f(w * 0.74)} {f(b - h * 0.4)} Q {f(w * 0.81)} {f(b - h * 0.5)} {f(w * 0.88)} {f(b - h * 0.4)} L {f(w * 0.88)} {f(b)} Z" fill="#3A2A1E" stroke="{INK}" stroke-width="2"></path>')
    o.append(ground(w, h, b, "#B8A06A", dy=0))
    s = fit(b, max(h * 0.16, b - 240))
    o.append(zach_fig(p, w * 0.81, b - 4, s * 0.86, flip=True))
    o.append(glow(w * 0.48, b - 110 * s, 190 * s, "#FFF4C2", 0.7, f"{p}g"))
    o.append(mary_fig(p, w * 0.4, b, s * 0.94, up=[(-22, -158), (-46, -150), (-64, -146)], flip=True))
    o.append(elis_fig(p, w * 0.56, b, s * 0.94, flip=False, up=[(-22, -158), (-46, -150), (-64, -146)]))
    return "".join(o)

def magnify(p, w, h, seed):
    """My soul doth magnify the Lord: the hill country at morning under a great clear sky, the light breaking over the hills,
    Mary standing on the height with her hands lifted (God never drawn: the light only)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#3A5AA8", "#FFE6B0"), rays(w * 0.7, h * 0.5, 30, w * 0.05, h * 1.2, color="#FFF4C2", op=0.25, a0=180, a1=360),
         sun(w * 0.7, h * 0.5, max(18, h * 0.07), color="#FFF4C2", op=0.6), hills(w, h, h * 0.56, seed, color="#6A7A8A", amp=20, step=80),
         hills(w, h, h * 0.68, seed + 1, color="#7A8A5A", amp=12, step=60),
         f'<path d="M{f(w * 0.06)} {f(h + 10)} C {f(w * 0.14)} {f(h * 0.74)} {f(w * 0.4)} {f(h * 0.72)} {f(w * 0.52)} {f(h + 10)} Z" fill="#9AAA5A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(h * 0.82, max(h * 0.4, h * 0.82 - 190))
    o.append(mary_fig(p, w * 0.28, h * 0.82, s, up=UP_HIGH, flip=True))
    return "".join(o)

def john_born(p, w, h, seed):
    """Her neighbors and her kinsfolk rejoiced with her: in the house, Elisabeth holding her son wrapped in white, the women
    of the hill country about her, lamps lit, the door open on the evening."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#A88A6A", window=(w * 0.84, w * 0.1)), glow(w * 0.4, b - h * 0.3, h * 0.5, "#FFE680", 0.5, f"{p}g"),
         clay_lamp(w * 0.08, b - 2, max(0.6, h / 300))]
    s = fit(b, max(h * 0.16, b - 250))
    o.append(elis_fig(p, w * 0.4, b, s, up=R1.HOLD_BABY, extra=R1.baby(10, -130, 0.8)))
    r = random.Random(seed)
    for i, x in enumerate((0.16, 0.26, 0.58, 0.7)):
        o.append(woman_fig(p, w * x, b - r.uniform(0, 4), s * r.uniform(0.88, 0.94), r.choice(["#6A3A4A", "#4A5A3A", "#7A5A3A", "#3A4A6A"]),
                           r.choice(["#8A5A3A", "#3A4A6A", "#6A2A3A", "#5A6A4A"]), flip=x > 0.45, up=UP_HIGH if i == 2 else None))
    return "".join(o)

def tablet(p, w, h, seed):
    """He asked for a writing tablet, and wrote, saying, His name is John: Zacharias seated, a waxed tablet in his hands, the
    stylus lifted; the kinsfolk about him leaning to read; Elisabeth with the child."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#A88A6A"), glow(w * 0.4, b - h * 0.3, h * 0.5, "#FFE680", 0.45, f"{p}g")]
    s = fit(b, max(h * 0.14, b - 250))
    o.append(seated(w * 0.34, b, s * 1.05, ZACH_C, head="#E8E2D6", beard="#E8E2D6"))
    tx, ty = w * 0.34 + 46 * s, b - 76 * s
    o.append(f'<rect x="{f(tx - 4 * s)}" y="{f(ty - 34 * s)}" width="{f(46 * s)}" height="{f(34 * s)}" fill="#C8963E" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(tx)}" y="{f(ty - 30 * s)}" width="{f(38 * s)}" height="{f(26 * s)}" fill="#4A3A22" stroke="{INK}" stroke-width="1.2"></rect>'
             f'<path d="M{f(tx + 4 * s)} {f(ty - 20 * s)} l {f(8 * s)} {f(-4 * s)} l {f(6 * s)} {f(6 * s)} l {f(10 * s)} {f(-6 * s)} M{f(tx + 6 * s)} {f(ty - 10 * s)} l {f(20 * s)} 0" stroke="#E8D8B0" stroke-width="1.6" fill="none"></path>')
    o.append(elis_fig(p, w * 0.14, b, s, up=R1.HOLD_BABY, extra=R1.baby(10, -130, 0.8)))
    for i, x in enumerate((0.6, 0.72, 0.84)):
        o.append(man(p, w * x, b, s * (0.96 - 0.02 * i), HEB[i + 1], flip=True) if i != 1 else woman_fig(p, w * x, b, s * 0.92, "#6A3A4A", "#8A5A3A", flip=True))
    return "".join(o)

def dayspring(p, w, h, seed):
    """The dayspring from on high shall visit us, to shine upon them that sit in darkness: night going from the hills of Judah,
    the first light of the sun rising over the rim of the land, a road lit toward it."""
    b = h
    o = [sky(w, h, "#0B0B2A", "#FFB07A"), mk.stars(30, w, h * 0.3, seed), rays(w * 0.5, h * 0.62, 34, w * 0.04, h * 1.3, color="#FFF4C2", op=0.25, a0=190, a1=350),
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.64)}" r="{f(h * 0.12)}" fill="#FFE680" stroke="#FFC14D" stroke-width="3"></circle>',
         hills(w, h, h * 0.62, seed, color="#2A2238", amp=16, step=80), hills(w, h, h * 0.74, seed + 1, color="#1A1426", amp=10, step=60),
         f'<path d="M{f(w * 0.42)} {f(h + 10)} L {f(w * 0.49)} {f(h * 0.74)} L {f(w * 0.51)} {f(h * 0.74)} L {f(w * 0.58)} {f(h + 10)} Z" fill="#C8905A" opacity="0.7"></path>']
    return "".join(o)

def deserts(p, w, h, seed):
    """The child grew, and waxed strong in spirit, and was in the deserts: the bare wilderness of Judæa at morning, a young man
    alone on a rock looking out over it, in a garment of skins."""
    b = h * 0.9
    o = [wilderness(p, w, h, seed, john=False, tone="dawn")]
    rx = w * 0.62
    o.append(f'<path d="M{f(rx - 70)} {f(b + 6)} C {f(rx - 60)} {f(b - 40)} {f(rx + 60)} {f(b - 44)} {f(rx + 70)} {f(b + 6)} Z" fill="#8A6A5A" stroke="{INK}" stroke-width="2.2"></path>')
    s = fit(b - 36, max(h * 0.3, b - 36 - 180))
    o.append(mk.person(p, round(rx), round(b - 36), round(s, 3), body="#9A6A4A", cloth=ROBES["baptist"], kind="Tunic", sw=3, flip=True,
                       extra='<path d="M-14 -186 C -20 -206 18 -210 15 -186 L 17 -174 L 12 -180 L -12 -180 L -17 -172 Z" fill="#2A1A10" stroke="#0D0D0F" stroke-width="1.4"></path>'))
    return "".join(o)

# ---- Luke 2 -------------------------------------------------------------------------------------------------------------
def enrolment(p, w, h, seed):
    """A decree from Cæsar Augustus, that all the world should be enrolled: a Roman official at a table in a town gate with
    the scroll of the roll, a soldier by him, the people waiting in a line to be enrolled."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), walls(w * 0.52, w * 1.06, h * 0.7, h * 0.4, seed, towers=2, houses=False),
         ground(w, h, h * 0.7, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.3, b - 210))
    o.append(f'<rect x="{f(w * 0.62)}" y="{f(b - 70 * s)}" width="{f(110 * s)}" height="{f(14 * s)}" fill="#7A4A2A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.62 + 10 * s)} {f(b - 56 * s)} L {f(w * 0.62 + 10 * s)} {f(b)} M{f(w * 0.62 + 100 * s)} {f(b - 56 * s)} L {f(w * 0.62 + 100 * s)} {f(b)}" stroke="#5A3A1E" stroke-width="{f(6 * s)}"></path>'
             + scroll(w * 0.62 + 55 * s, b - 80 * s, 70 * s, 14 * s, lines=1))
    o.append(roman_fig(p, w * 0.78, b, s, flip=True))
    o.append(soldier_fig(p, w * 0.9, b, s, flip=True))
    r = random.Random(seed)
    for i in range(6):
        x = w * (0.06 + 0.09 * i)
        o.append(man(p, x, b - r.uniform(0, 4), s * r.uniform(0.9, 0.98), r.choice(HEB)) if i % 3 else woman_fig(p, x, b, s * 0.9, r.choice(HEB), r.choice(["#4A5A6A", "#6A3A4A"])))
    return "".join(o)

def to_bethlehem(p, w, h, seed):
    """Joseph went up from Galilee to Bethlehem with Mary his betrothed, being great with child: the road over the hills at
    evening, Joseph leading the ass, Mary riding, Bethlehem on its hill ahead."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#4A3A6A", "#FFB07A"), sun(w * 0.12, h * 0.5, 16, color="#FFE680", op=0.35),
         hills(w, h, h * 0.52, seed, color="#6A5A5A", amp=16, step=80), hill_town(w * 0.8, h * 0.66, w * 0.32, h * 0.26, seed, lit=True, hill="#5A4A4A"),
         ground(w, h, h * 0.72, "#8A7A5A", dy=-4),
         f'<path d="M-10 {f(b + 6)} C {f(w * 0.3)} {f(b - h * 0.04)} {f(w * 0.6)} {f(h * 0.76)} {f(w * 0.78)} {f(h * 0.7)}" stroke="#A8946A" stroke-width="{f(h * 0.07)}" fill="none" opacity="0.8"></path>']
    sk = min(fit(b, max(h * 0.3, b - 220)), 1.1)
    d = 1
    o.append(N.ass(w * 0.34, b, sk, color="#8A8478") + woman_fig(p, w * 0.34 - 4 * sk, b - 66 * sk, sk * 0.62, MARY_C, "#3A6AA8")
             + joseph_fig(p, w * 0.34 + d * 104 * sk, b, sk * 0.98, up=[(-22, -158), (-50, -140), (-74, -122)]))
    return "".join(o)

def manger_(x, b, s=1.0, babe=True, uid="mg"):
    """A manger of stone and timber filled with straw; babe=True: the child laid in it, swaddled, in a soft light."""
    o = [f'<path d="M{f(x - 60 * s)} {f(b - 50 * s)} L {f(x + 60 * s)} {f(b - 50 * s)} L {f(x + 46 * s)} {f(b - 10 * s)} L {f(x - 46 * s)} {f(b - 10 * s)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(x - 40 * s)} {f(b - 10 * s)} L {f(x - 50 * s)} {f(b)} M{f(x + 40 * s)} {f(b - 10 * s)} L {f(x + 50 * s)} {f(b)}" stroke="#5A3A22" stroke-width="{f(6 * s)}"></path>']
    r = random.Random(int(x))
    o.append("".join(f'<path d="M{f(x + r.uniform(-56, 56) * s)} {f(b - 50 * s)} l {f(r.uniform(-12, 12) * s)} {f(-r.uniform(6, 14) * s)}" stroke="#E8C060" stroke-width="2"></path>' for _ in range(22)))
    if babe: o.append(swaddled(x, b - 58 * s, s * 1.0, uid))
    return "".join(o)

def stable(p, w, h, seed, shepherds=False, night_=True):
    """There was no room for them in the inn: a stable cut in the rock beside the inn, lamplight within, the ox and the ass
    in the stall; Mary kneeling by the manger where the babe lies swaddled in a soft light, Joseph standing by;
    shepherds=True: the shepherds come in and kneeling."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bgr(w, h, "#2A2030"),
         f'<path d="M-10 -10 L {f(w + 10)} -10 L {f(w + 10)} {f(h * 0.14)} C {f(w * 0.7)} {f(h * 0.24)} {f(w * 0.3)} {f(h * 0.2)} -10 {f(h * 0.16)} Z" fill="#4A3A3A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#5A4030" stroke="{INK}" stroke-width="2"></rect>',
         glow(w * 0.5, b - h * 0.2, h * 0.6, "#FFE680", 0.55, f"{p}g")]
    o.append(f'<path d="M{f(w * 0.04)} {f(b)} L {f(w * 0.04)} {f(h * 0.3)} M{f(w * 0.24)} {f(b)} L {f(w * 0.24)} {f(h * 0.26)}" stroke="#6A4A2A" stroke-width="10"></path>')
    k = max(0.4, min(0.9, h / 520))
    o.append(N.ass(w * 0.12, b, k * 0.8, color="#6A6458"))
    s = fit(b, max(h * 0.14, b - 250))
    o.append(manger_(w * 0.5, b, max(0.7, s * 1.1), uid=f"{p}bb"))
    o.append(kneel_w(w * 0.36, b, s * 0.86, MARY_C, "#3A6AA8"))
    o.append(joseph_fig(p, w * 0.66, b, s, flip=True))
    if shepherds:
        for i, x in enumerate((0.8, 0.9)):
            o.append(E.kneel(w * x, b, s * 0.84, color=SHEP[i], flip=True, skin="#B98A6E"))
    o.append(clay_lamp(w * 0.9 if not shepherds else w * 0.28, h * 0.3, max(0.6, h / 320)))
    return "".join(o)

def field_night(p, w, h, seed, angel_=False, host=False, gone=False):
    """Shepherds in the field, keeping watch by night over their flock: the hills under the stars, the sheep, a small fire,
    Bethlehem far off; angel_=True: the angel of the Lord standing over them and the glory of the Lord shining round about
    (white light), the shepherds fallen back afraid; host=True: the sky full of figures of light; gone=True: the light gone
    up, the shepherds setting off toward Bethlehem."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), night(w, h, seed, n=90, top="#0B0B2A", bot="#2A2050"), hills(w, h, h * 0.62, seed, color="#1E1838", amp=16, step=80),
         hill_town(w * 0.84, h * 0.7, w * 0.26, h * 0.2, seed, lit=True, hill="#2A2238"), ground(w, h, h * 0.74, "#2A2438", dy=-4)]
    if angel_ or host:
        o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#FFF4C2" opacity="0.18"></rect>')
        o.append(glow(w * 0.5, h * 0.3, max(w, h) * 0.7, "#FFFFFF", 0.7, f"{p}gl"))
    if host:
        r = random.Random(seed)
        for i in range(16):
            x, y = w * r.uniform(0.04, 0.96), h * r.uniform(0.3, 0.6)
            o.append(angel(p, x, y, max(0.12, h / 2600) * r.uniform(0.8, 1.2), flip=r.random() < 0.5, up=UP_HIGH if i % 2 else None))
    if angel_:
        sa = max(0.36, h / 640)
        o.append(glow(w * 0.54, h * 0.5 - 110 * sa, 200 * sa, "#FFFFFF", 0.8, f"{p}ag"))
        o.append(angel(p, w * 0.54, h * 0.52, sa, up=UP_BLESS, flip=True))
    o.append(sheep_row(w * 0.04, w * 0.5, h * 0.88, 7, seed, s=max(0.25, min(0.5, h / 900))))
    if not gone:
        o.append(E.blaze(w * 0.68, h * 0.9, 34, 40, seed, n=5))
    s = fit(b, max(h * 0.36, b - 200))
    if gone:
        for i in range(3): o.append(shepherd_fig(p, w * (0.58 + 0.1 * i), b - 2 * i, s * (0.94 - 0.03 * i), i))
    elif angel_ or host:
        o.append(E.kneel(w * 0.3, b, s * 0.9, color=SHEP[0], skin="#B98A6E", flip=False))
        o.append(shepherd_fig(p, w * 0.78, b, s, 1, flip=True, up=[(-22, -158), (-36, -184), (-34, -206)]))
        o.append(E.kneel(w * 0.9, b, s * 0.88, color=SHEP[2], skin="#B98A6E", flip=True))
    else:
        o.append(shepherd_fig(p, w * 0.58, b, s, 0) + seated(w * 0.78, b, s * 0.86, SHEP[1], head="#8A7A5A", beard="#9A948A", flip=True)
                 + shepherd_fig(p, w * 0.9, b, s * 0.96, 2, flip=True))
    return "".join(o)

def shepherds_tell(p, w, h, seed):
    """They made known the saying, and the shepherds returned, glorifying and praising God: the street of Bethlehem at dawn,
    the shepherds going back with their arms lifted, the townsfolk at their doors wondering."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A9A", "#FFC890"), houses(w, h, h * 0.8, seed, hmin=0.3, hmax=0.46, lit=True), pavement(w, h, h * 0.8)]
    s = fit(b, max(h * 0.3, b - 210))
    for i in range(3): o.append(shepherd_fig(p, w * (0.3 + 0.12 * i), b - 2 * i, s * (0.96 - 0.03 * i), i, up=UP_HIGH if i != 1 else None))
    o.append(woman_fig(p, w * 0.08, b, s * 0.88, "#6A3A4A", "#8A5A3A") + man(p, w * 0.86, b, s * 0.92, "#5A4A6A", flip=True))
    return "".join(o)

def pondered(p, w, h, seed):
    """Mary kept all these sayings, pondering them in her heart: the stable at night, quiet, Mary sitting by the manger with
    the child in her arms, the lamp burning low."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bgr(w, h, "#1E1828"), f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#4A3628" stroke="{INK}" stroke-width="2"></rect>',
         glow(w * 0.46, b - h * 0.24, h * 0.5, "#FFE680", 0.45, f"{p}g"), manger_(w * 0.7, b, max(0.6, h / 420), babe=False), clay_lamp(w * 0.86, b - 60 * max(0.6, h / 420) - 4, max(0.5, h / 380))]
    s = fit(b, max(h * 0.2, b - 220))
    o.append(seated(w * 0.42, b, s, MARY_C, head="#3A6AA8", beard=None))
    o.append(swaddled(w * 0.42 + 26 * s, b - 70 * s, s * 0.7, f"{p}bb"))
    return "".join(o)

def presented(p, w, h, seed, simeon=False, anna=False):
    """They brought him up to Jerusalem, to present him to the Lord: in the court of the temple, Mary with the child in her
    arms, Joseph carrying the pair of turtledoves in a little cage; simeon=True: old Simeon taking the child up in his
    arms, his face lifted; anna=True: Anna the prophetess coming in, bent with age."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), temple(w * 0.56, h * 0.5, w * 0.6), pavement(w, h, h * 0.5)]
    s = fit(b, max(h * 0.2, b - 230))
    cage = ('<path d="M44 -132 L 44 -110 L 72 -110 L 72 -132 C 72 -144 44 -144 44 -132 Z" fill="none" stroke="#6A4A2A" stroke-width="2.4"></path>'
            '<path d="M52 -140 L 52 -110 M58 -142 L 58 -110 M64 -140 L 64 -110" stroke="#6A4A2A" stroke-width="1.4"></path>'
            '<ellipse cx="54" cy="-116" rx="5" ry="4" fill="#C8C0B0"></ellipse><ellipse cx="64" cy="-118" rx="5" ry="4" fill="#B8B0A0"></ellipse>')
    if simeon:
        glow_ = glow(w * 0.44, b - 130 * s, 140 * s, "#FFF4C2", 0.7, f"{p}g")
        o.append(glow_)
        o.append(mk.person(p, round(w * 0.44), round(b), round(s, 3), body=SKIN, cloth="#4A5A7A", kind="Robe", sw=3, up=R1.HOLD_BABY,
                           extra=A.headcloth("#3A4A6A") + A.WHITE_BEARD + swaddled(10, -132, 0.7, f"{p}bb", light=False)))
        o.append(mary_fig(p, w * 0.24, b, s * 0.94) + joseph_fig(p, w * 0.12, b, s))
    else:
        o.append(mary_fig(p, w * 0.32, b, s * 0.94, up=R1.HOLD_BABY) + swaddled(w * 0.32 + 10 * s * 0.94, b - 132 * s * 0.94, s * 0.66, f"{p}bb"))
        o.append(joseph_fig(p, w * 0.18, b, s, up=[(22, -158), (38, -132), (50, -122)]) + f'<g transform="translate({f(w * 0.18)} {f(b)}) scale({f(s)})">{cage}</g>')
    if anna:
        o.append(woman_fig(p, w * 0.7, b + 4, s * 0.84, "#4A3A4A", "#3A2A3A", flip=True, up=[(-22, -158), (-40, -176), (-50, -196)]))
    return "".join(o)

def nazareth_home(p, w, h, seed):
    """They returned into Galilee, to their own city Nazareth; and the child grew, and waxed strong: Nazareth on its hill at
    morning, the family on the road up to it."""
    return nazareth(p, w, h, seed)

def passover_road(p, w, h, seed, seeking=False, boy=True):
    """His parents went every year to Jerusalem at the feast of the passover: the company of kinsfolk on the road among the
    hills, the city far off; seeking=True: Joseph and Mary turned back alone on the road toward the city, seeking him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.44, seed, color="#A89A7A", amp=16, step=80)]
    o.append(walls(w * 0.62, w * 0.96, h * 0.52, h * 0.16, seed, towers=3) + temple(w * 0.8, h * 0.4, w * 0.14))
    o.append(hills(w, h, h * 0.6, seed + 1, color="#8A9A6A", amp=10, step=60))
    o.append(ground(w, h, h * 0.76, "#B8A06A", dy=-6))
    s = fit(b, max(h * 0.34, b - 200))
    if seeking:
        o.append(joseph_fig(p, w * 0.46, b, s, up=[(-22, -158), (-46, -170), (-64, -186)]) + mary_fig(p, w * 0.36, b, s * 0.94))
    else:
        r = random.Random(seed)
        o.append(crowd(p, w * 0.04, w * 0.6, b, b - 180 * s, 8, seed, flip=True))
        o.append(joseph_fig(p, w * 0.66, b, s, flip=True) + mary_fig(p, w * 0.74, b, s * 0.94, flip=True) + (boy_fig(p, w * 0.82, b, s * 0.8, flip=True) if boy else ""))
    return "".join(o)

def among_doctors(p, w, h, seed, found=False):
    """They found him in the temple, sitting in the midst of the teachers, both hearing them, and asking them questions: under
    the colonnade, the boy Jesus seated among the grey-bearded teachers, the scrolls open; found=True: Joseph and Mary coming
    in from the left."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bgr(w, h, "#C8B490"), f'<rect x="-10" y="{f(h * 0.06)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>']
    for x in (0.06, 0.26, 0.74, 0.94):
        o.append(f'<rect x="{f(w * x - 14)}" y="{f(h * 0.12)}" width="28" height="{f(b - h * 0.12)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(w * x - 20)}" y="{f(h * 0.12)}" width="40" height="10" fill="{GOLD}" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="-10" y="{f(b - h * 0.06)}" width="{f(w + 20)}" height="{f(h)}" fill="#B8A07A" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.2, b - 230))
    o.append(glow(w * 0.52, b - 70 * s, 110 * s, "#FFF4C2", 0.6, f"{p}g"))
    teachers = [(0.32, "#E8E2D6", "#F3EFE6", "#9A948A", False), (0.42, "#3A4A6A", "#3A4A6A", "#6A645E", False), (0.64, "#E8E2D6", "#F3EFE6", "#B8B2A6", True),
                (0.76, "#5A4A3A", "#3A4A6A", "#9A948A", True)]
    for x, cl, hd, bd, fl in teachers:
        o.append(seated(w * x, b, s * 0.84, cl, head=hd, beard=bd, flip=fl, band=True))
    o.append(scroll(w * 0.53, b - 20 * s, 80 * s, 16 * s, lines=1))
    hair = f'<path d="M-10 -94 C -10 -108 2 -112 10 -104" fill="none" stroke="{JESUS_HAIR}" stroke-width="7"></path>'
    o.append(seated(w * 0.53, b - 30 * s, s * 0.74, JESUS_TUNIC, head=None, beard=None))
    o.append(f'<g transform="translate({f(w * 0.53)} {f(b - 30 * s)}) scale({f(s * 0.74)})"><path d="M-20 -116 C -22 -134 10 -138 14 -120 C 6 -126 -10 -126 -18 -110 Z" fill="{JESUS_HAIR}" stroke="{INK}" stroke-width="1.4"></path></g>')
    if found:
        o.append(joseph_fig(p, w * 0.1, b, s) + mary_fig(p, w * 0.18, b, s * 0.94, up=[(-22, -158), (-44, -150), (-62, -152)], flip=True))
    return "".join(o)

def subject(p, w, h, seed):
    """He went down with them, and came to Nazareth; and he was subject unto them: the carpenter's workshop at Nazareth, the
    boy at the bench with Joseph, planks and tools, Mary in the doorway (the floor left clear below them for the end mark)."""
    b = min(h * 0.92, h - 76)
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#B8987A", floor="#8A6A4A", window=(w * 0.78, w * 0.1)),
         f'<rect x="{f(w * 0.3)}" y="{f(b - h * 0.18)}" width="{f(w * 0.34)}" height="{f(h * 0.04)}" fill="#A8784A" stroke="{INK}" stroke-width="2"></rect>'
         f'<path d="M{f(w * 0.32)} {f(b - h * 0.14)} L {f(w * 0.32)} {f(b)} M{f(w * 0.62)} {f(b - h * 0.14)} L {f(w * 0.62)} {f(b)}" stroke="#6A4A2A" stroke-width="6"></path>']
    for k in range(3):
        o.append(f'<rect x="{f(w * 0.04)}" y="{f(b - h * (0.1 + 0.05 * k))}" width="{f(w * 0.16)}" height="{f(h * 0.04)}" fill="#C8985A" stroke="{INK}" stroke-width="1.6"></rect>')
    s = fit(b, max(h * 0.2, b - 230))
    o.append(joseph_fig(p, w * 0.7, b, s, flip=False, up=[(-22, -158), (-46, -136), (-66, -128)]))
    o.append(boy_fig(p, w * 0.42, b, s * 0.82, up=[(-22, -158), (-44, -132), (-60, -128)], flip=True))
    o.append(mary_fig(p, w * 0.88, b, s * 0.92, flip=True))
    return "".join(o)
