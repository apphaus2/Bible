"""Drawings for the Matthew volume: Galilee and Judaea (the lake and its boats, the hill-country, the wilderness, the Jordan,
Jerusalem and the temple), houses and synagogues, crowds, and the scenes chapter by chapter. Built on the minor prophets' kit
(oba.minor: vista, figure, crowd, walls, halo, rays) and the older drawing kits.

Jesus at a distance is only ever ntcast.jesus_fig; the disciples at a distance wear ntcast.ROBES. An angel of the Lord is a
figure of white light with a gold rim and no face (angel); the Spirit is a dove of light (dove_light); God is never drawn.
The devil is never drawn: the temptation's pictures show Jesus alone. Every function takes (p, w, h, seed, ...) — p, a
prefix unique to the panel, names the figure defs and gradients."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from oba.minor import (vista, figure, crowd, halo, rays, starfield, walls, ruin, river, fig_tree, olive, scroll, mount_zion, TONES, HILL, EARTH,
                       UP_RIGHT, UP_LEFT, sheep_row, eagle, rain, bolt, grain, vines)
from genesis.art2 import fit, ground, hills, bird, birds, SKIN
from genesis.art2 import dove as _dove
from genesis.art3 import man, woman, sun, label, grid_bg, node, route, king
from genesis.art4 import shining, clay_lamp
from num.art import ALL
from jer.art import glow, shaft
from sa2.art import sky
from ecc.art import tree
from kg1.art import temple_front, bed
from job.art import seated, clouds
import exodus as E, numbers1 as N, judges1 as J1, ruth1 as R1, egypt as EG, exodus5 as V, joshua1 as J
from exo import art as A
from ntcast import jesus_fig, ROBES, JESUS_TUNIC, JESUS_MANTLE

INK = "#0D0D0F"
def f(v): return f"{v:.1f}"
NIGHT_TOP, NIGHT_BOT = "#0B0B2A", "#2A2050"
HEB = A.HEBREW + ["#C2456A", "#5A6E8A", "#2A5A6A", "#8A3A2A"]
TWELVE = [ROBES[k] for k in ("peter", "andrew", "james", "john", "matthew", "thomas", "judas")] + ["#4A6A4A", "#7A5A2A", "#5A5A7A", "#6A3A3A", "#3A5A5A"]
JOSEPH_C, JOSEPH_HEAD, MARY_C = "#7A5A30", "#4A4A3A", ROBES["mary"]
MAGI_C = ("#5A2A7A", "#1F5A6A", "#8A2A2A")
BROWN_BEARD = A.BLACK_BEARD.replace("#2A1A10", "#3A2214")
GREY_BEARD = A.WHITE_BEARD.replace("#E8E2D6", "#9A948A")

def bgr(w, h, color):
    return f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{color}"></rect>'

def night(w, h, seed, n=80, frac=0.62, top=NIGHT_TOP, bot=NIGHT_BOT):
    return sky(w, h, top, bot) + mk.stars(n, w, h * frac, seed)

def moon(x, y, r, color="#F3EFE6"):
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r * 2.4)}" fill="{color}" opacity="0.12"></circle>'
            f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{color}" stroke="{INK}" stroke-width="1.4"></circle>')

def star_of(x, y, r, uid="st"):
    """The star that went before the wise-men: a bright eight-pointed star with long rays."""
    pts = []
    for i in range(16):
        a = math.pi / 8 * i - math.pi / 2; rr = r if i % 4 == 0 else (r * 0.5 if i % 2 == 0 else r * 0.18)
        pts.append(f"{f(x + rr * math.cos(a))} {f(y + rr * math.sin(a))}")
    return (glow(x, y, r * 2.8, "#FFF4C2", 0.7, uid) + rays(x, y, 24, r * 0.4, r * 3.4, color="#FFF4C2", op=0.3, sw=2)
            + f'<path d="M{" L ".join(pts)} Z" fill="#FFFDF0" stroke="#FFD23F" stroke-width="1.4"></path>')

# ---- people -------------------------------------------------------------------------------------------------------------
def joseph_fig(p, x, y, s, flip=False, up=None):
    """Joseph the husband of Mary at a distance: an ochre robe and headcloth, a brown beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=JOSEPH_C, kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth(JOSEPH_HEAD, cord="#3A2214") + BROWN_BEARD)

def veil(color, hair="#2A1A10"):
    """A woman's veil framing her face (hair showing at the brow), falling to the shoulders."""
    return (f'<path d="M-11 -190 C -8 -197 8 -197 11 -190 L 11 -184 L -11 -184 Z" fill="{hair}"></path>'
            f'<path d="M-15 -186 C -17 -207 17 -207 15 -186 L 21 -156 L 11 -160 L 11 -186 C 9 -196 -9 -196 -11 -186 L -11 -160 L -21 -156 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.8"></path>')

def woman_fig(p, x, y, s, cloth, scarf=None, flip=False, up=None, extra=""):
    """A woman at a distance: her robe, and a veil in the scarf colour (her face showing)."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, woman=True, sw=3, flip=flip, up=up, extra=veil(scarf or cloth) + extra)

def mary_fig(p, x, y, s, flip=False, up=None, child=False):
    """Mary at a distance, in blue with a blue veil; child=True: holding the young child."""
    up = up or ([(-22, -158), (-10, -128), (14, -124)] if child else None)
    return woman_fig(p, x, y, s, MARY_C, "#3A6AA8", flip=flip, up=up, extra=R1.baby(10, -130, 0.8) if child else "")

def magus_fig(p, x, y, s, i, flip=False, up=None):
    """One of the wise-men standing: his robe and headcloth in his colour, a gold band."""
    c = MAGI_C[i % 3]
    beard = [A.BLACK_BEARD, A.WHITE_BEARD, BROWN_BEARD][i % 3]
    return mk.person(p, round(x), round(y), round(s, 3), body="#9A6A4A" if i % 3 == 0 else SKIN, cloth=c, kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth(c, cord="#E8B830") + beard)

def herod_fig(p, x, y, s, flip=False, up=None):
    """Herod the king: purple robe, a gold crown, a grey beard."""
    from genesis.art3 import CROWN
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#5A1A4A", kind="Robe", sw=3, flip=flip, up=up, extra=GREY_BEARD + CROWN)

def scribe_fig(p, x, y, s, white=False, flip=False, up=None):
    """A chief priest (white) or a scribe (slate-blue headcloth with a band) at a distance."""
    c = "#E8E2D6" if white else "#3A4A6A"
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=c, kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth("#F3EFE6" if white else "#3A4A6A", cord="#E8B830") + (GREY_BEARD if white else A.BLACK_BEARD))

FUR = "".join(f'<path d="M{x} -150 l -4 10 M{x + 6} -118 l -4 10 M{x - 4} -86 l -4 10 M{x + 3} -54 l -4 10" stroke="#3A2414" stroke-width="2"></path>' for x in (-18, -4, 10))
GIRDLE = '<path d="M-24 -96 L 24 -96 L 24 -88 L -24 -88 Z" fill="#4A2A14" stroke="#0D0D0F" stroke-width="1.6"></path>'
def john_fig(p, x, y, s, flip=False, up=None):
    """John the Baptist at a distance: raiment of camel's hair (shaggy brown), a leathern girdle, wild dark hair and beard."""
    hair = '<path d="M-14 -186 C -20 -206 18 -210 15 -186 L 17 -172 L 12 -178 L -12 -178 L -17 -170 Z" fill="#2A1A10" stroke="#0D0D0F" stroke-width="1.4"></path>'
    return mk.person(p, round(x), round(y), round(s, 3), body="#9A6A4A", cloth=ROBES["baptist"], kind="Tunic", sw=3, flip=flip, up=up,
                     extra=FUR + GIRDLE + hair + A.BLACK_BEARD)

def jesus(p, x, y, s, flip=False, up=None, glow=True):
    return jesus_fig(p, x, y, s, flip=flip, up=up, glow=glow)

def disciple(p, x, y, s, who, flip=False, up=None, kind="Robe"):
    return mk.person(p, round(x), round(y), round(s, 3), body="#B98A6E", cloth=ROBES.get(who, who), kind=kind, sw=3, flip=flip, up=up)

ANGEL_LIGHT, ANGEL_RIM = "#FFF6D8", "#E8B830"
def angel(p, x, y, s, flip=False, up=None):
    """An angel of the Lord: a figure of white light with a gold rim — the head and hands light too, no face, no skin
    (genesis.art4.shining, the men in white at Mamre, keeps its flesh-coloured head; an angel does not)."""
    halo = f'<ellipse cx="{f(x)}" cy="{f(y - 110 * s)}" rx="{f(80 * s)}" ry="{f(130 * s)}" fill="#FFF4C2" opacity="0.45"></ellipse>'
    fig = mk.person(p, round(x), round(y), round(s, 3), body=ANGEL_LIGHT, cloth="#FFFFFF", stroke=ANGEL_RIM, sw=3, flip=flip, up=up)
    fig = fig.replace(f'fill="{ANGEL_LIGHT}">', f'fill="{ANGEL_LIGHT}" stroke="{ANGEL_RIM}" stroke-width="3">', 1).replace('stroke="#0D0D0F"', f'stroke="{ANGEL_RIM}"')
    return halo + fig

def dove_light(x, y, s=1.0, uid="dv"):
    """The Spirit of God descending as a dove: a white dove in a glow of light, wings spread."""
    return glow(x, y, 110 * s, "#FFF4C2", 0.9, uid) + _dove(x - 4 * s, y + 10 * s, s * 1.4, wings="up")

UP_BLESS = [(-22, -158), (-44, -150), (-66, -158)]     # an arm stretched out (forward at shoulder height)
UP_HIGH = [(-22, -158), (-40, -190), (-46, -226)]      # an arm lifted up
UP_TOUCH = [(-22, -158), (-40, -128), (-60, -112)]     # an arm reaching down and out
UP_CALL = [(-22, -158), (-46, -176), (-70, -196)]      # beckoning

# ---- scenery ------------------------------------------------------------------------------------------------------------
def lake(w, h, y, seed, color="#1F6F9A", deep="#0F4C68", foam="#E8F6FA", n=16, op=0.7):
    """The sea of Galilee from y down: calm water with small wave strokes."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="{f(y)}" width="{f(w + 20)}" height="{f(h - y + 10)}" fill="{color}" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(y + (h - y) * 0.5)}" width="{f(w + 20)}" height="{f(h)}" fill="{deep}" opacity="0.45"></rect>']
    for _ in range(n):
        x = r.uniform(0, w); yy = r.uniform(y + 6, h); L = r.uniform(14, 44) * (0.6 + (yy - y) / max(1, h - y))
        o.append(f'<path d="M{f(x)} {f(yy)} q {f(L / 4)} -4 {f(L / 2)} 0 t {f(L / 2)} 0" stroke="{foam}" stroke-width="1.6" fill="none" opacity="{op}"></path>')
    return "".join(o)

def shore(w, h, y, color="#C8A878", x0=None, x1=None):
    """A strip of beach from x0 to x1 (default the whole width) at the water's edge y."""
    x0 = -10 if x0 is None else x0; x1 = w + 10 if x1 is None else x1
    return f'<path d="M{f(x0)} {f(y)} C {f(x0 + (x1 - x0) * 0.3)} {f(y - 6)} {f(x0 + (x1 - x0) * 0.7)} {f(y + 4)} {f(x1)} {f(y - 2)} L {f(x1)} {f(h + 10)} L {f(x0)} {f(h + 10)} Z" fill="{color}" stroke="{INK}" stroke-width="2"></path>'

def boat(p, x, y, s, crew=(), flip=False, mast=True, sail=None, tilt=0, net=False, hull="#6A4A2A"):
    """A fishing boat of Galilee, (x, y) the waterline at its middle (about 190 units long at s=1). crew: (dx, who) with who
    'jesus', a cloth colour, ('up', colour) one hauling with raised arms, ('old', colour) a grey-bearded man; the hull covers
    their legs."""
    sx = -s if flip else s
    o = [f'<g transform="translate({f(x)} {f(y)}) rotate({f(tilt)}) scale({f(sx)} {f(s)})">']
    if mast:
        o.append(f'<path d="M-6 -24 L -10 -170" stroke="#4A2A1A" stroke-width="5"></path><path d="M-52 -150 L 34 -158" stroke="#4A2A1A" stroke-width="3.4"></path>')
        if sail:
            o.append(f'<path d="M-50 -148 L 32 -156 C 40 -110 34 -70 26 -40 L -44 -40 C -54 -80 -56 -120 -50 -148 Z" fill="{sail}" stroke="{INK}" stroke-width="2.2"></path>')
        else:
            o.append(f'<path d="M-50 -150 C -30 -142 14 -146 32 -158" stroke="#E8E2D6" stroke-width="7" fill="none" stroke-linecap="round"></path>')
    for dx, who in crew:
        if who == "jesus":
            o.append(jesus_fig(p, dx, -10, 0.46, glow=False))
        elif isinstance(who, tuple) and who[0] == "up":
            o.append(mk.person(p, dx, -10, 0.46, body="#B98A6E", cloth=who[1], kind="Tunic", sw=4, up=[(-22, -158), (-46, -176), (-62, -200)]))
        elif isinstance(who, tuple) and who[0] == "old":
            o.append(mk.person(p, dx, -10, 0.46, body="#B98A6E", cloth=who[1], kind="Robe", sw=4, extra=A.WHITE_BEARD))
        elif isinstance(who, tuple) and who[0] == "mend":
            o.append(seated(dx, -24, 0.4, who[1], beard="#2A1A10", flip=len(who) > 2))
        else:
            o.append(mk.person(p, dx, -10, 0.46, body="#B98A6E", cloth=who, kind="Tunic", sw=4))
    o.append(f'<path d="M-96 -36 L 98 -40 C 86 -8 60 4 0 4 C -60 4 -86 -8 -96 -36 Z" fill="{hull}" stroke="{INK}" stroke-width="2.6"></path>'
             '<path d="M-92 -28 L 94 -32" stroke="#3A2414" stroke-width="2"></path><path d="M-80 -16 C -40 -10 40 -10 82 -18" stroke="#3A2414" stroke-width="1.6" fill="none"></path>')
    if net:
        o.append('<path d="M60 -30 C 90 -10 110 20 96 40 C 70 30 54 10 48 -20" fill="none" stroke="#E8D8B0" stroke-width="1.4" stroke-dasharray="3 3"></path>'
                 '<path d="M66 -24 L 82 30 M76 -20 L 100 22 M56 -10 L 92 0 M54 4 L 96 16" stroke="#E8D8B0" stroke-width="1" opacity="0.8"></path>')
    o.append("</g>")
    return "".join(o)

def net_cast(x, y, r, seed=1):
    """A round casting-net spread in the air over the water, (x, y) its middle."""
    rr = random.Random(seed); o = [f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(r)}" ry="{f(r * 0.32)}" fill="#E8D8B0" opacity="0.18" stroke="#E8D8B0" stroke-width="1.6"></ellipse>']
    for k in range(10):
        a = math.pi * 2 * k / 10
        o.append(f'<path d="M{f(x)} {f(y - r * 0.2)} L {f(x + r * math.cos(a))} {f(y + r * 0.32 * math.sin(a))}" stroke="#E8D8B0" stroke-width="1" opacity="0.8"></path>')
    for k in range(1, 3):
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(r * k / 3)}" ry="{f(r * 0.32 * k / 3)}" fill="none" stroke="#E8D8B0" stroke-width="1" opacity="0.8"></ellipse>')
    return "".join(o)

def houses(w, h, base, seed, x0=None, x1=None, hmin=0.18, hmax=0.3, lit=False, shut=False, color=("#E8D8B0", "#D8C098", "#C8B088", "#E0CFA8"), stairs=True):
    """A row of flat-roofed houses of white stone along base (doors, small windows, outside stairs); shut=True: every door
    shut and barred, every window dark."""
    r = random.Random(seed); x0 = -10 if x0 is None else x0; x1 = w + 10 if x1 is None else x1
    o = []; x = x0
    while x < x1:
        hw = w * r.uniform(0.1, 0.17); hh = h * r.uniform(hmin, hmax)
        o.append(f'<rect x="{f(x)}" y="{f(base - hh)}" width="{f(hw)}" height="{f(hh)}" fill="{r.choice(color)}" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(x - 3)}" y="{f(base - hh - 6)}" width="{f(hw + 6)}" height="6" fill="#8A6A4A" stroke="{INK}" stroke-width="1.6"></rect>')
        dw = min(hw * 0.26, hh * 0.3)
        dx = x + hw * 0.36
        o.append(f'<path d="M{f(dx)} {f(base)} L {f(dx)} {f(base - dw * 1.5)} C {f(dx)} {f(base - dw * 2.1)} {f(dx + dw)} {f(base - dw * 2.1)} {f(dx + dw)} {f(base - dw * 1.5)} L {f(dx + dw)} {f(base)} Z" fill="{"#5A3A22" if shut else "#3A2A1E"}" stroke="{INK}" stroke-width="1.6"></path>')
        if shut:
            o.append(f'<path d="M{f(dx)} {f(base - dw * 0.9)} L {f(dx + dw)} {f(base - dw * 0.9)}" stroke="#2A1A10" stroke-width="2.4"></path>'
                     f'<path d="M{f(dx + dw / 2)} {f(base)} L {f(dx + dw / 2)} {f(base - dw * 1.8)}" stroke="#2A1A10" stroke-width="1.2"></path>')
        o.append(f'<rect x="{f(x + hw * 0.72)}" y="{f(base - hh * 0.7)}" width="{f(hw * 0.12)}" height="{f(hh * 0.14)}" fill="{"#FFC14D" if lit else "#3A2A1E"}" stroke="{INK}" stroke-width="1.2"></rect>')
        if stairs and r.random() < 0.4:
            o.append(f'<path d="M{f(x + hw)} {f(base)} L {f(x + hw + hh * 0.5)} {f(base)} L {f(x + hw)} {f(base - hh * 0.9)} Z" fill="#B8A07A" stroke="{INK}" stroke-width="1.6"></path>')
        x += hw + w * r.uniform(0.01, 0.05)
    return "".join(o)

def hill_town(x, base, wd, ht, seed, lit=False, hill="#7A6A4A", color=("#E8D8B0", "#D8C098", "#C8B088")):
    """A small town of flat-roofed houses climbing a hill, seen from afar."""
    r = random.Random(seed)
    o = [f'<path d="M{f(x - wd * 0.7)} {f(base + 6)} C {f(x - wd * 0.4)} {f(base - ht * 0.9)} {f(x + wd * 0.4)} {f(base - ht * 0.9)} {f(x + wd * 0.7)} {f(base + 6)} Z" fill="{hill}" stroke="{INK}" stroke-width="2"></path>']
    items = []
    for _ in range(int(14 + wd / 20)):
        hx = x + r.uniform(-0.48, 0.42) * wd; k = 1 - abs(hx - x) / (wd * 0.6)
        hy = base - ht * (0.12 + 0.6 * max(0, k) * r.uniform(0.6, 1.0)); hw = wd * r.uniform(0.07, 0.11)
        items.append((hy, hx, hw))
    for hy, hx, hw in sorted(items):
        o.append(f'<rect x="{f(hx)}" y="{f(hy - hw * 0.7)}" width="{f(hw)}" height="{f(hw * 0.7)}" fill="{r.choice(color)}" stroke="{INK}" stroke-width="1.4"></rect>'
                 f'<rect x="{f(hx + hw * 0.4)}" y="{f(hy - hw * 0.42)}" width="{f(hw * 0.2)}" height="{f(hw * 0.22)}" fill="{"#FFC14D" if lit and r.random() < 0.6 else "#3A2A1E"}"></rect>')
    return "".join(o)

def temple(x, base, wd, lit=False):
    """Herod's temple seen across the court: the white-and-gold sanctuary front, the porch, colonnades either side."""
    u = wd / 100
    o = []
    for side in (-1, 1):                       # colonnades (Solomon's porch)
        x0 = x + side * 30 * u
        o.append(f'<rect x="{f(min(x0, x0 + side * 70 * u))}" y="{f(base - 26 * u)}" width="{f(70 * u)}" height="{f(26 * u)}" fill="#D8C8A8" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(min(x0, x0 + side * 70 * u) - 2)}" y="{f(base - 30 * u)}" width="{f(70 * u + 4)}" height="{f(4 * u)}" fill="#B8A888" stroke="{INK}" stroke-width="1.6"></rect>')
        for k in range(8):
            cx = x0 + side * (4 + k * 9) * u
            o.append(f'<rect x="{f(cx - 1.4 * u)}" y="{f(base - 25 * u)}" width="{f(2.8 * u)}" height="{f(25 * u)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1"></rect>')
    o.append(f'<rect x="{f(x - 30 * u)}" y="{f(base - 70 * u)}" width="{f(60 * u)}" height="{f(70 * u)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(x - 34 * u)}" y="{f(base - 74 * u)}" width="{f(68 * u)}" height="{f(5 * u)}" fill="#E8B830" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<rect x="{f(x - 12 * u)}" y="{f(base - 50 * u)}" width="{f(24 * u)}" height="{f(50 * u)}" fill="{"#FFC14D" if lit else "#E8B830"}" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(x - 7 * u)}" y="{f(base - 42 * u)}" width="{f(14 * u)}" height="{f(42 * u)}" fill="#7A2A3A" stroke="{INK}" stroke-width="1.4"></rect>')
    for k in range(-26, 30, 6):
        o.append(f'<path d="M{f(x + k * u)} {f(base - 74 * u)} L {f(x + k * u)} {f(base - 79 * u)}" stroke="#E8B830" stroke-width="{f(1.4 * u)}"></path>')
    o.append(f'<rect x="{f(x - 110 * u)}" y="{f(base - 2)}" width="{f(220 * u)}" height="6" fill="#B8A888" stroke="{INK}" stroke-width="1.4"></rect>')
    return "".join(o)

def jerusalem_far(w, h, seed, tone="day", lit=False):
    """Jerusalem on its hill: walls, the houses, the temple high in the midst."""
    top, bot = TONES[tone]; hc1, hc2 = HILL[tone]
    o = [sky(w, h, top, bot), hills(w, h, h * 0.58, seed, color=hc1, amp=14, step=80)]
    o.append(f'<path d="M{f(w * 0.08)} {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.42)} {f(w * 0.7)} {f(h * 0.42)} {f(w * 0.94)} {f(h * 0.8)} Z" fill="{hc2}" stroke="{INK}" stroke-width="2.2"></path>')
    o.append(walls(w * 0.16, w * 0.86, h * 0.72, h * 0.2, seed, lit=lit, towers=4))
    o.append(temple(w * 0.56, h * 0.53, w * 0.3, lit=lit))
    o.append(ground(w, h, h * 0.8, EARTH[tone], dy=0))
    return "".join(o)

def pavement(w, h, y, color="#C8B898", line="#A89878"):
    o = [f'<rect x="-10" y="{f(y)}" width="{f(w + 20)}" height="{f(h - y + 10)}" fill="{color}" stroke="{INK}" stroke-width="2"></rect>']
    for k in range(1, 7):
        yy = y + (h - y) * (k / 7) ** 1.3
        o.append(f'<path d="M-10 {f(yy)} L {f(w + 10)} {f(yy)}" stroke="{line}" stroke-width="1.4"></path>')
    for k in range(-6, 16):
        x = w * k / 10
        o.append(f'<path d="M{f(w * 0.5 + (x - w * 0.5) * 0.4)} {f(y)} L {f(x)} {f(h + 10)}" stroke="{line}" stroke-width="1.2"></path>')
    return "".join(o)

def room(w, h, b, wall="#C8A878", floor="#8A6A4A", window=None, night_=False, seed=1):
    """A plain room of a house: plastered wall, a beam, the floor at b; window=(x, wd) a small window (stars at night)."""
    o = [bgr(w, h, wall if not night_ else "#3A2E3A"),
         f'<rect x="-10" y="{f(h * 0.06)}" width="{f(w + 20)}" height="{f(h * 0.04)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h - b + 10)}" fill="{floor if not night_ else "#2A2228"}" stroke="{INK}" stroke-width="2"></rect>']
    if window:
        wx, ww = window
        o.append(f'<rect x="{f(wx)}" y="{f(h * 0.2)}" width="{f(ww)}" height="{f(ww * 1.3)}" fill="{"#0B0B2A" if night_ else "#8FD0E2"}" stroke="{INK}" stroke-width="2.4"></rect>')
        if night_: o.append(f'<g transform="translate({f(wx)} {f(h * 0.2)})">' + mk.stars(6, ww, ww * 1.2, seed) + '</g>')
    return "".join(o)

# ---- Matthew 1 ----------------------------------------------------------------------------------------------------------
ABRAHAM_DAVID = ["ABRAHAM", "ISAAC", "JACOB", "JUDAH", "PEREZ", "HEZRON", "RAM", "AMMINADAB", "NAHSHON", "SALMON", "BOAZ", "OBED", "JESSE", "DAVID"]
DAVID_BABYLON = ["SOLOMON", "REHOBOAM", "ABIJAH", "ASA", "JEHOSHAPHAT", "JORAM", "UZZIAH", "JOTHAM", "AHAZ", "HEZEKIAH", "MANASSEH", "AMON", "JOSIAH", "JECHONIAH"]
BABYLON_CHRIST = ["SHEALTIEL", "ZERUBBABEL", "ABIUD", "ELIAKIM", "AZOR", "SADOC", "ACHIM", "ELIUD", "ELEAZAR", "MATTHAN", "JACOB", "JOSEPH", "JESUS"]

def generations(w, h, top=0.2, bot=0.95, bands=(0, 1, 2)):
    """The three fourteens of Matthew 1 as one chart on the blueprint grid: each band two rows of seven names, snaking;
    Abraham to David gold, Solomon to Jechoniah cyan, Shealtiel to Jesus white, JESUS lit with a glow."""
    lines = [(ABRAHAM_DAVID, "#FFD23F", "FROM ABRAHAM UNTO DAVID"), (DAVID_BABYLON, "#8FD0E2", "FROM DAVID UNTO THE CARRYING AWAY TO BABYLON"),
             (BABYLON_CHRIST, "#F3EFE6", "FROM THE CARRYING AWAY TO BABYLON UNTO THE CHRIST")]
    lines = [lines[i] for i in bands]
    o = [grid_bg(w, h)]
    nb = len(lines); bh = (bot - top) * h / nb
    pts_all = []
    for bi, (names, color, tag) in enumerate(lines):
        y0 = top * h + bi * bh
        o.append(f'<rect x="10" y="{f(y0 + 4)}" width="{f(w - 20)}" height="{f(bh - 10)}" fill="none" stroke="{color}" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.5"></rect>')
        o.append(label(20, y0 + 18, tag, color, 9, anchor="start"))
        pts = []
        for i, nm in enumerate(names):
            r, c = divmod(i, 7)
            if r % 2: c = 6 - c
            x = w * (0.08 + 0.84 * c / 6)
            y = y0 + bh * (0.5 + 0.3 * r)
            pts.append((x, y, nm, color))
        pts_all += pts
    for a, b in zip(pts_all, pts_all[1:]):
        o.append(route([(a[0], a[1]), (b[0], b[1])], color="#4A7A9A", sw=2, dash="5 5", arrow=True))
    for x, y, nm, color in pts_all:
        if nm == "JESUS":
            o.append(glow(x, y, 46, "#FFE680", 0.9, "jsgl") + node(x, y, nm, "#FFD23F", r=8, dy=-14, size=13))
        else:
            o.append(node(x, y, nm, color, r=5, dy=-12, size=10))
    return "".join(o)

def fourteens(w, h, top=0.3):
    """So all the generations: one line from Abraham to the Christ, three runs of fourteen marks — Abraham to David, David to
    the carrying away to Babylon, the carrying away to the Christ — each run labelled 14."""
    o = [grid_bg(w, h)]
    y = h * (top + (1 - top) * 0.5)
    x0, x1 = w * 0.06, w * 0.94
    seg = (x1 - x0) / 3
    cols = ("#FFD23F", "#8FD0E2", "#F3EFE6")
    ends = ("ABRAHAM", "DAVID", "BABYLON", "THE CHRIST")
    for k in range(3):
        a = x0 + seg * k
        o.append(f'<path d="M{f(a)} {f(y)} L {f(a + seg)} {f(y)}" stroke="{cols[k]}" stroke-width="3"></path>')
        for i in range(14):
            xx = a + seg * (i + 0.5) / 14
            o.append(f'<circle cx="{f(xx)}" cy="{f(y)}" r="4" fill="{cols[k]}" stroke="{INK}" stroke-width="1"></circle>')
        o.append(f'<path d="M{f(a + 6)} {f(y + 18)} L {f(a + 6)} {f(y + 26)} L {f(a + seg - 6)} {f(y + 26)} L {f(a + seg - 6)} {f(y + 18)}" stroke="{cols[k]}" stroke-width="1.6" fill="none"></path>')
        o.append(label(a + seg / 2, y + 48, "14", cols[k], 20))
    for k, nm in enumerate(ends):
        xx = x0 + seg * k
        o.append(f'<path d="M{f(xx)} {f(y - 22)} L {f(xx)} {f(y + 12)}" stroke="#F3EFE6" stroke-width="2"></path>')
        if nm == "THE CHRIST": o.append(glow(xx, y, 34, "#FFE680", 0.9, "fcgl"))
        o.append(label(min(max(xx, w * 0.08), w * 0.9), y - 30, nm, "#FFD23F" if k in (0, 3) else "#F3EFE6", 11))
    return "".join(o)

def mary_alone(p, w, h, seed):
    """Mary betrothed to Joseph, in her mother's house at Nazareth: lamp-light, a soft light from the window falling on her."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#B8987A", window=(w * 0.62, w * 0.1)),
         f'<path d="M{f(w * 0.62)} {f(h * 0.2)} L {f(w * 0.72)} {f(h * 0.2)} L {f(w * 0.5)} {f(b)} L {f(w * 0.2)} {f(b)} Z" fill="#FFF4C2" opacity="0.35"></path>',
         glow(w * 0.38, b - h * 0.3, h * 0.42, "#FFF4C2", 0.6, f"{p}g"), clay_lamp(w * 0.86, b - 2, max(0.6, h / 300))]
    s = fit(b, max(h * 0.16, b - 260))
    o.append(mary_fig(p, w * 0.38, b, s))
    return "".join(o)

def dream(p, w, h, seed, egypt=False, flee=False):
    """An angel of the Lord appeared unto Joseph in a dream: Joseph asleep on his bed in the dark house, a clay lamp, and
    standing by him a figure of white light (egypt=True: a palm in the window; flee=True: the angel's arm lifted)."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), bgr(w, h, "#1A1630"), f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2238" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.12)}" y="{f(h * 0.12)}" width="{f(w * 0.12)}" height="{f(h * 0.22)}" fill="#0B0B2A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<g transform="translate({f(w * 0.12)} {f(h * 0.12)})">' + mk.stars(8, w * 0.12, h * 0.2, seed) + '</g>']
    if egypt:
        o.append(f'<g transform="translate({f(w * 0.17)} {f(h * 0.34)}) scale({f(h * 0.14 / 210)})">' + J1.palm(0, 0, 1) + '</g>')
    o.append(bed(w, h, w * 0.08, w * 0.6, b, cover=JOSEPH_C, head="#C98E66", hair="#3A2214"))
    o.append(clay_lamp(w * 0.66, b - 4, max(0.6, h / 300)))
    s = fit(b, max(h * 0.1, b - 270))
    o.append(glow(w * 0.82, b - 110 * s, 170 * s, "#FFF4C2", 0.55, f"{p}ag"))
    o.append(angel(p, w * 0.82, b, s, flip=True, up=UP_HIGH if flee else UP_BLESS))
    return "".join(o)

def prophecy(p, w, h, seed, tone="night"):
    """The word spoken by the prophet: an open scroll on a reading-desk under a lamp, light about it."""
    b = h * 0.92
    o = [bgr(w, h, "#1A1630" if tone == "night" else "#3A2A2A"), glow(w * 0.5, h * 0.5, h * 0.7, "#FFE680", 0.4, f"{p}g"),
         f'<path d="M{f(w * 0.3)} {f(b)} L {f(w * 0.36)} {f(h * 0.62)} L {f(w * 0.64)} {f(h * 0.62)} L {f(w * 0.7)} {f(b)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="2.4"></path>',
         scroll(w * 0.5, h * 0.5, min(w * 0.5, h * 0.9), h * 0.28, lines=5),
         clay_lamp(w * 0.82, h * 0.62, max(0.6, h / 280))]
    return "".join(o)

def born(p, w, h, seed):
    """She brought forth a son, and he called his name JESUS: the house at night, Mary with the child in her arms, Joseph
    beside them, a lamp."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#5A4048", window=(w * 0.08, w * 0.1), night_=True, seed=seed),
         glow(w * 0.48, b - h * 0.32, h * 0.5, "#FFE680", 0.55, f"{p}g"), clay_lamp(w * 0.66, b - 2, max(0.7, h / 280))]
    s = fit(b, max(h * 0.14, b - 250))
    o.append(mary_fig(p, w * 0.44, b, s * 0.96, child=True))
    o.append(joseph_fig(p, w * 0.58, b, s, flip=True))
    return "".join(o)

def wedded(p, w, h, seed):
    """Joseph took unto him his wife: Joseph and Mary walking together up the street of Nazareth at evening."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A6A", "#FFB07A"), sun(w * 0.84, h * 0.4, 16, color="#FFE680", op=0.3),
         hills(w, h, h * 0.42, seed, color="#6A5A5A", amp=14, step=80),
         houses(w, h, h * 0.86, seed, hmin=0.3, hmax=0.46, lit=True), ground(w, h, h * 0.86, "#8A6A4A", dy=0)]
    s = fit(b, max(h * 0.2, b - 230))
    o.append(joseph_fig(p, w * 0.42, b, s))
    o.append(mary_fig(p, w * 0.52, b, s * 0.93))
    return "".join(o)

# ---- Matthew 2 ----------------------------------------------------------------------------------------------------------
def bethlehem(w, h, seed, star=True, dark=False):
    """Bethlehem of Judaea at night on its hill; star=True: the star standing over the house where the young child was;
    dark=True: no star, the town under a heavy sky."""
    b = h * 0.86
    o = [night(w, h, seed, n=40 if dark else 90, top="#05051A" if dark else NIGHT_TOP, bot="#1A1430" if dark else NIGHT_BOT),
         hills(w, h, h * 0.66, seed, color="#14102A", amp=16, step=80),
         hill_town(w * 0.5, b, w * 0.62, h * 0.42, seed, lit=not dark, hill="#2A2238"),
         ground(w, h, b, "#1A1426", dy=0)]
    if star:
        o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.2)} L {f(w * 0.5)} {f(b - h * 0.3)}" stroke="#FFF4C2" stroke-width="3" opacity="0.5"></path>' + star_of(w * 0.5, h * 0.18, max(14, h * 0.07), f"bs{seed}"))
    return "".join(o)

def magi(p, w, h, seed, star=True, home=False, city=False):
    """Wise-men from the east: three riders on camels crossing the desert at night under the star; city=True: Jerusalem on
    its hill ahead; home=True: going back another way at dawn."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), night(w, h, seed, top="#0B0B2A", bot="#5B2470") if not home else sky(w, h, "#3A3A6A", "#FFB04A")]
    if home: o.append(sun(w * 0.12, h * 0.62, 18, color="#FFE680", op=0.3))
    o.append(hills(w, h, h * 0.66, seed, color="#3A2A3A" if not home else "#8A6A5A", amp=10, step=90))
    if city:
        o.append(walls(w * 0.58, w * 0.98, h * 0.7, h * 0.2, seed, lit=True, towers=3) + temple(w * 0.8, h * 0.55, w * 0.18, lit=True))
    o.append(ground(w, h, h * 0.74, "#5A4A4A" if not home else "#C8A06A", dy=-4))
    if star: o.append(star_of(w * (0.84 if not city else 0.3), h * 0.16, max(12, h * 0.06), f"mg{seed}"))
    k = min(0.9, (b - h * 0.3) / 200)
    xs = (0.18, 0.36, 0.54) if not home else (0.5, 0.68, 0.86)
    for i, (x, c) in enumerate(zip(xs, MAGI_C)):
        o.append(J1.camel(w * x, b - i * 3, k * (1 - i * 0.05), flip=home, color="#B5844A", rider=c))
    return "".join(o)

def herod_hall(p, w, h, seed, who="magi"):
    """Herod the king in his hall at Jerusalem: gold columns and purple hangings, the king on his throne; before him the
    wise-men (who='magi') or the chief priests and scribes (who='scribes')."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bgr(w, h, "#3A1A3A")]
    for x in (0.06, 0.34, 0.66, 0.94):
        o.append(f'<rect x="{f(w * x - 14)}" y="-10" width="28" height="{f(b + 10)}" fill="#E8B830" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(w * x - 20)}" y="{f(b - 14)}" width="40" height="14" fill="#C8963E" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<path d="M-10 -10 L {f(w + 10)} -10 L {f(w + 10)} {f(h * 0.14)} C {f(w * 0.7)} {f(h * 0.26)} {f(w * 0.3)} {f(h * 0.26)} -10 {f(h * 0.14)} Z" fill="#5A1A4A" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#6A4A3A" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.24, b - 240))
    o.append(f'<path d="M{f(w * 0.12)} {f(b)} L {f(w * 0.12)} {f(b - 150 * s)} L {f(w * 0.12 + 100 * s)} {f(b - 150 * s)} L {f(w * 0.12 + 100 * s)} {f(b)} Z" fill="#E8B830" stroke="{INK}" stroke-width="2.4"></path>')
    o.append(herod_fig(p, w * 0.12 + 50 * s, b, s * 1.02))
    if who == "magi":
        for i in range(3): o.append(magus_fig(p, w * (0.54 + i * 0.15), b, s * 0.96, i, flip=True))
    else:
        for i in range(4): o.append(scribe_fig(p, w * (0.5 + i * 0.13), b, s * 0.94, white=i % 2 == 0, flip=True))
    return "".join(o)

def star_road(p, w, h, seed):
    """The star went before them, till it came and stood over where the young child was: the camels on the road below
    Bethlehem, the star standing over one house, its light falling straight down."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), night(w, h, seed, n=70, top="#0B0B2A", bot="#3A2A6A"),
         hills(w, h, h * 0.6, seed, color="#1E1838", amp=14, step=80),
         hill_town(w * 0.66, h * 0.74, w * 0.5, h * 0.36, seed, lit=True, hill="#2A2238")]
    sx = w * 0.7
    o.append(f'<path d="M{f(sx - 6)} {f(h * 0.2)} L {f(sx + 6)} {f(h * 0.2)} L {f(sx + 22)} {f(h * 0.58)} L {f(sx - 22)} {f(h * 0.58)} Z" fill="#FFF4C2" opacity="0.4"></path>')
    o.append(star_of(sx, h * 0.15, max(12, h * 0.065), f"sr{seed}"))
    o.append(ground(w, h, h * 0.8, "#2A2238", dy=-4))
    k = min(0.62, (b - h * 0.44) / 200)
    for i, c in enumerate(MAGI_C):
        o.append(J1.camel(w * (0.1 + i * 0.13), b - i * 2, k * (1 - i * 0.04), color="#B5844A", rider=c))
    return "".join(o)

def gifts(p, w, h, seed):
    """They came into the house and saw the young child with Mary his mother, and fell down and worshipped him: Mary with
    the child in a lamp-lit room, the wise-men bowed before them, gold and frankincense and myrrh set down."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#4A3438", floor="#5A4A3A", window=(w * 0.06, w * 0.12), night_=True, seed=seed),
         star_of(w * 0.12, h * 0.3, max(6, h * 0.03), f"gf{seed}"),
         glow(w * 0.26, b - h * 0.3, h * 0.46, "#FFE680", 0.5, f"{p}g")]
    s = fit(b, max(h * 0.16, b - 250))
    o.append(mary_fig(p, w * 0.26, b, s, child=True))
    for i, c in enumerate(MAGI_C):
        o.append(E.kneel(w * (0.56 + i * 0.15), b, s * 0.9, color=c, flip=True, skin="#9A6A4A" if i == 0 else SKIN))
    for c, x in (("#E8B830", 0.38), ("#C8C0B0", 0.43), ("#8A3A2A", 0.48)):
        o.append(f'<rect x="{f(w * x - 12 * s)}" y="{f(b - 26 * s)}" width="{f(24 * s)}" height="{f(26 * s)}" fill="{c}" stroke="{INK}" stroke-width="2"></rect>'
                 f'<path d="M{f(w * x - 14 * s)} {f(b - 26 * s)} C {f(w * x - 10 * s)} {f(b - 38 * s)} {f(w * x + 10 * s)} {f(b - 38 * s)} {f(w * x + 14 * s)} {f(b - 26 * s)} Z" fill="{c}" stroke="{INK}" stroke-width="2"></path>')
    return "".join(o)

def holy_family(p, x, b, s, flip=False):
    """Joseph leading the ass, Mary riding with the young child."""
    d = -1 if flip else 1
    return (N.ass(x, b, s, flip=flip, color="#8A8478")
            + mary_fig(p, x - d * 4 * s, b - 66 * s, s * 0.62, flip=flip, child=True)
            + joseph_fig(p, x + d * 104 * s, b, s * 0.98, flip=flip, up=[(-22, -158), (-50, -140), (-74, -122)]))

def flight(p, w, h, seed, back=False):
    """He took the young child and his mother by night, and departed into Egypt: the road south by moonlight, the
    pyramids far off; back=True: the road home into the land of Israel at dawn."""
    b = h * 0.9
    if back:
        o = [mk.defs(p, *ALL), sky(w, h, "#5A6A9A", "#FFC890"), sun(w * 0.86, h * 0.5, 14, color="#FFE680", op=0.3),
             hills(w, h, h * 0.6, seed, color="#6A7A5A", amp=14, step=70), ground(w, h, h * 0.7, "#A8945A", dy=-6)]
    else:
        o = [mk.defs(p, *ALL), night(w, h, seed, top="#0B0B2A", bot="#2A3A6A"), moon(w * 0.82, h * 0.18, max(10, h * 0.05)),
             EG.pyramid(w * 0.82, h * 0.7, w * 0.2, h * 0.22, lit="#5A5A7A", dark="#3A3A5A", line="#2A2A4A"),
             EG.pyramid(w * 0.66, h * 0.7, w * 0.12, h * 0.13, lit="#5A5A7A", dark="#3A3A5A", line="#2A2A4A"),
             hills(w, h, h * 0.68, seed, color="#2A2A3A", amp=8, step=90), ground(w, h, h * 0.72, "#3A3448", dy=-4)]
    o.append(f'<path d="M{f(w * -0.02)} {f(b + 6)} C {f(w * 0.4)} {f(b - h * 0.04)} {f(w * 0.6)} {f(h * 0.78)} {f(w * 1.02)} {f(h * 0.74)}" stroke="{"#C8B080" if back else "#4A4458"}" stroke-width="{f(h * 0.08)}" fill="none" opacity="0.8"></path>')
    s = min(fit(b, max(h * 0.3, b - 220)), 1.1)
    o.append(holy_family(p, w * (0.3 if not back else 0.62), b, s, flip=back))
    return "".join(o)

def empty_street(p, w, h, seed):
    """Bethlehem in the night after Herod sent forth: an empty street between the houses, every door shut and barred,
    no one in the way, a heavy dark sky (the slaughter is told in words only)."""
    b = h * 0.86
    o = [night(w, h, seed, n=20, top="#05050E", bot="#2A1420"),
         houses(w, h, b, seed, x0=-10, x1=w * 0.34, hmin=0.34, hmax=0.52, shut=True, color=("#5A4A4E", "#4A3E44", "#6A5A5A"), stairs=False),
         houses(w, h, b, seed + 1, x0=w * 0.66, x1=w + 10, hmin=0.34, hmax=0.52, shut=True, color=("#5A4A4E", "#4A3E44", "#6A5A5A"), stairs=False),
         ground(w, h, b, "#1E1A20", dy=0),
         f'<path d="M{f(w * 0.2)} {f(h + 10)} L {f(w * 0.8)} {f(h + 10)} L {f(w * 0.58)} {f(b)} L {f(w * 0.42)} {f(b)} Z" fill="#3A3238" stroke="{INK}" stroke-width="1.6"></path>',
         f'<rect x="{f(w * 0.42)}" y="{f(b - h * 0.16)}" width="{f(w * 0.16)}" height="{f(h * 0.16)}" fill="#4A3E44" stroke="{INK}" stroke-width="2"></rect>'
         f'<path d="M{f(w * 0.47)} {f(b)} L {f(w * 0.47)} {f(b - h * 0.08)} Q {f(w * 0.5)} {f(b - h * 0.12)} {f(w * 0.53)} {f(b - h * 0.08)} L {f(w * 0.53)} {f(b)} Z" fill="#2A1A10" stroke="{INK}" stroke-width="1.6"></path>']
    return "".join(o)

def ramah(p, w, h, seed):
    """A voice was heard in Ramah: the bare hills at night, a single pillar of stone on the height (Rachel's grave), no one
    drawn — only the wind."""
    from ecc.art import wind_lines
    b = h * 0.86
    o = [night(w, h, seed, n=30, top="#05051A", bot="#3A2A4A"), moon(w * 0.2, h * 0.2, max(8, h * 0.04), color="#C8C0D8"),
         hills(w, h, h * 0.6, seed, color="#2A2238", amp=22, step=90),
         f'<path d="M{f(w * 0.3)} {f(b)} C {f(w * 0.46)} {f(h * 0.52)} {f(w * 0.7)} {f(h * 0.52)} {f(w * 0.9)} {f(b)} Z" fill="#3A2E44" stroke="{INK}" stroke-width="2"></path>',
         f'<rect x="{f(w * 0.6 - 8)}" y="{f(h * 0.5)}" width="16" height="{f(h * 0.12)}" fill="#8A8090" stroke="{INK}" stroke-width="2"></rect>',
         wind_lines(w, h, seed, n=8, color="#C8C0D8", op=0.35, y0=0.3, y1=0.8), ground(w, h, b, "#1A1426", dy=0)]
    return "".join(o)

def nazareth(p, w, h, seed):
    """He came and dwelt in a city called Nazareth: a small town on a hill in Galilee, morning, the family coming up the road."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.86, h * 0.18, 14, color="#FFE680", op=0.25),
         hills(w, h, h * 0.5, seed, color="#7A9A5A", amp=16, step=80), hill_town(w * 0.66, h * 0.66, w * 0.46, h * 0.3, seed, hill="#8A7A4A"),
         ground(w, h, h * 0.7, "#9AAA5A", dy=-4), tree(w * 0.1, h * 0.8, h / 320, color="#7A8A5A", kind="round", seed=seed),
         tree(w * 0.94, h * 0.82, h / 340, kind="tall", seed=seed + 1)]
    s = min(fit(b, max(h * 0.4, b - 200)), 0.9)
    o.append(holy_family(p, w * 0.32, b, s))
    return "".join(o)

# ---- Matthew 3 ----------------------------------------------------------------------------------------------------------
def wilderness(p, w, h, seed, john=True, crowd_n=0, tone="desert"):
    """The wilderness of Judaea: bare tawny hills, rocks, the Dead Sea's haze; John standing on a rock crying aloud."""
    r = random.Random(seed); b = h * 0.92
    top, bot = {"desert": ("#FFD89A", "#F3B870"), "night": ("#0B0B2A", "#3A2A5A"), "dawn": ("#3A2A5A", "#FFB07A")}[tone]
    hc = {"desert": ("#C8985A", "#A8784A"), "night": ("#2A2238", "#1E1A2A"), "dawn": ("#6A4A4A", "#4A3438")}[tone]
    o = [mk.defs(p, *ALL), sky(w, h, top, bot), hills(w, h, h * 0.5, seed, color=hc[0], amp=26, step=70),
         hills(w, h, h * 0.66, seed + 1, color=hc[1], amp=18, step=90), ground(w, h, h * 0.8, "#D8B07A" if tone == "desert" else "#3A3040", dy=-6)]
    if tone == "night": o.append(mk.stars(70, w, h * 0.45, seed))
    for _ in range(5):
        x = r.uniform(0, w); s = r.uniform(0.5, 1.2) * h / 300
        o.append(f'<path d="M{f(x - 30 * s)} {f(h * 0.86 + 10 * s)} C {f(x - 26 * s)} {f(h * 0.86 - 18 * s)} {f(x + 20 * s)} {f(h * 0.86 - 22 * s)} {f(x + 32 * s)} {f(h * 0.86 + 10 * s)} Z" fill="#A8885A" stroke="{INK}" stroke-width="1.8"></path>')
    if john:
        rx = w * 0.3
        o.append(f'<path d="M{f(rx - 70)} {f(b + 6)} C {f(rx - 60)} {f(b - 40)} {f(rx + 60)} {f(b - 44)} {f(rx + 70)} {f(b + 6)} Z" fill="#B8956A" stroke="{INK}" stroke-width="2.2"></path>')
        s = fit(b - 36, max(h * 0.12, b - 36 - 250))
        o.append(john_fig(p, rx, b - 36, s, up=UP_HIGH))
    if crowd_n:
        o.append(crowd(p, w * 0.48, w * 0.84, b, max(h * 0.4, b - 160), crowd_n, seed, flip=True))
    return "".join(o)

def jordan(p, w, h, seed, jesus_=False, crowd_n=7, john=True):
    """The river Jordan between its green banks: John standing in the water baptizing, the people on the bank, coming down
    to him confessing their sins; jesus_=True: Jesus coming down to the water."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, color="#C8A06A", amp=18, step=80),
         hills(w, h, h * 0.46, seed + 1, color="#7A9A5A", amp=10, step=60),
         f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.47)} {f(w * 0.6)} {f(h * 0.53)} {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.86)} C {f(w * 0.6)} {f(h * 0.9)} {f(w * 0.3)} {f(h * 0.84)} -10 {f(h * 0.88)} Z" fill="#2C7DA8" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M-10 {f(h * 0.88)} C {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.6)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.86)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#9AAA5A" stroke="{INK}" stroke-width="2"></path>']
    for k in range(6):
        x = w * (0.05 + 0.18 * k)
        o.append(f'<path d="M{f(x)} {f(h * 0.62 + (k % 3) * 8)} l 30 -2" stroke="#BFE6F2" stroke-width="2" opacity="0.7"></path>')
    for k in range(9):                                                          # reeds
        x = w * (0.02 + 0.11 * k)
        o.append(f'<path d="M{f(x)} {f(h * 0.86)} l -4 -{f(h * 0.08)} M{f(x + 4)} {f(h * 0.86)} l 3 -{f(h * 0.1)}" stroke="#4A6A2A" stroke-width="2"></path>')
    s = fit(b, max(h * 0.2, b - 240))
    jy = h * 0.62
    # John waist-deep in the water: the water covers him from the waist
    js = min(s * 0.62, (h * 0.84 - jy) / 96)
    if john: o.append(john_fig(p, w * 0.42, jy + 92 * js, js, up=UP_BLESS)
             + f'<rect x="{f(w * 0.42 - 40 * js)}" y="{f(jy)}" width="{f(80 * js)}" height="{f(94 * js)}" fill="#2C7DA8"></rect>'
             + f'<path d="M{f(w * 0.42 - 44 * js)} {f(jy)} q {f(22 * js)} -5 {f(44 * js)} 0 t {f(44 * js)} 0" stroke="#BFE6F2" stroke-width="2.4" fill="none"></path>')
    if crowd_n:
        o.append(crowd(p, w * 0.6, w * 0.98, b, max(h * 0.5, b - 150), crowd_n, seed, flip=True))
    if jesus_:
        o.append(jesus(p, w * 0.16, b, s * 0.62))
    return "".join(o)

def axe_root(p, w, h, seed):
    """Even now the axe lieth at the root of the trees: a barren tree, an axe struck into its root, a fire burning beside."""
    b = h * 0.88
    o = [sky(w, h, "#3A1A1A", "#C8682E"), hills(w, h, h * 0.6, seed, color="#4A2A20", amp=12, step=80), ground(w, h, b, "#5A3A28", dy=0)]
    tx = w * 0.42; s = h / 260
    o.append(f'<path d="M{f(tx)} {f(b)} C {f(tx - 6 * s)} {f(b - 60 * s)} {f(tx + 6 * s)} {f(b - 110 * s)} {f(tx)} {f(b - 150 * s)} M{f(tx)} {f(b - 110 * s)} L {f(tx - 50 * s)} {f(b - 170 * s)} M{f(tx)} {f(b - 120 * s)} L {f(tx + 56 * s)} {f(b - 176 * s)} M{f(tx - 30 * s)} {f(b - 140 * s)} L {f(tx - 44 * s)} {f(b - 196 * s)}" stroke="#4A3428" stroke-width="{f(10 * s)}" fill="none" stroke-linecap="round"></path>')
    o.append(f'<g transform="translate({f(tx + 14 * s)} {f(b - 12 * s)}) rotate(-24) scale({f(s)})"><path d="M0 0 L 70 -4" stroke="#8A5A30" stroke-width="7" stroke-linecap="round"></path>'
             '<path d="M-6 -14 C -20 -12 -26 4 -18 14 L 4 8 Z" fill="#B8B8C0" stroke="#0D0D0F" stroke-width="2"></path></g>')
    o.append(E.blaze(w * 0.78, b, w * 0.26, h * 0.42, seed, n=7))
    return "".join(o)

def threshing(p, w, h, seed):
    """Whose fan is in his hand: a threshing-floor at evening wind, the grain heaped and the wheat gathered into the garner,
    the chaff blown aside into a burning fire."""
    from ruth1 import heap
    b = h * 0.88
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A6A", "#FFB07A"), hills(w, h, h * 0.56, seed, color="#8A6A5A", amp=10, step=80), ground(w, h, h * 0.66, "#C8A06A", dy=0),
         f'<ellipse cx="{f(w * 0.4)}" cy="{f(b)}" rx="{f(w * 0.3)}" ry="{f(h * 0.08)}" fill="#D8B880" stroke="{INK}" stroke-width="2"></ellipse>',
         heap(w * 0.3, b, w * 0.2, h * 0.16)]
    r = random.Random(seed)
    for _ in range(40):
        o.append(f'<circle cx="{f(w * 0.5 + r.uniform(0, w * 0.28))}" cy="{f(b - r.uniform(h * 0.1, h * 0.5))}" r="{f(r.uniform(1, 2.6))}" fill="#E8D8A0" opacity="0.8"></circle>')
    o.append(f'<rect x="{f(w * 0.06)}" y="{f(b - h * 0.3)}" width="{f(w * 0.12)}" height="{f(h * 0.3)}" fill="#B89A6A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.05)} {f(b - h * 0.3)} L {f(w * 0.12)} {f(b - h * 0.4)} L {f(w * 0.19)} {f(b - h * 0.3)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></path>')
    o.append(E.blaze(w * 0.86, b, w * 0.2, h * 0.36, seed, n=6))
    return "".join(o)

def heavens_opened(p, w, h, seed):
    """Jesus went up straightway from the water: the heavens opened, light falling in a great shaft, the Spirit of God
    descending as a dove of light upon him; John in the water beside; no one else in the light."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A6A", "#8FD0E2"),
         f'<path d="M{f(w * 0.3)} -10 C {f(w * 0.4)} {f(h * 0.08)} {f(w * 0.6)} {f(h * 0.08)} {f(w * 0.7)} -10 Z" fill="#FFF4C2"></path>',
         shaft(w * 0.5, w, h, top_w=0.2, bot_w=0.1, color="#FFF4C2", op=0.5), rays(w * 0.5, -10, 26, 20, h * 1.2, color="#FFF4C2", op=0.25, a0=20, a1=160),
         hills(w, h, h * 0.62, seed, color="#5A7A4A", amp=12, step=80),
         f'<path d="M-10 {f(h * 0.74)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.78)} {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2C7DA8" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.32, b - 230))
    o.append(jesus(p, w * 0.5, b, s, up=None))
    o.append(f'<path d="M{f(w * 0.5 - 40 * s)} {f(h * 0.9)} q {f(20 * s)} -6 {f(40 * s)} 0 t {f(40 * s)} 0" stroke="#BFE6F2" stroke-width="3" fill="none"></path>')
    o.append(john_fig(p, w * 0.8, b + 30 * s, s * 0.8, flip=True, up=UP_BLESS))
    o.append(f'<rect x="{f(w * 0.68)}" y="{f(h * 0.9)}" width="{f(w * 0.3)}" height="{f(h)}" fill="#2C7DA8"></rect>')
    o.append(dove_light(w * 0.5, b - 230 * s - h * 0.04, max(0.6, h / 360), f"{p}dv"))
    return "".join(o)

# ---- Matthew 4 ----------------------------------------------------------------------------------------------------------
def alone(p, w, h, seed, tone="night", stones=False):
    """Jesus alone in the wilderness: bare hills under the stars (forty days and forty nights); stones=True: the round
    stones of the desert about him."""
    b = h * 0.92
    o = [wilderness(p, w, h, seed, john=False, tone=tone)]
    if stones:
        r = random.Random(seed)
        for _ in range(9):
            x = r.uniform(0.04, 0.96) * w; y = b - r.uniform(0, h * 0.08); rr = r.uniform(10, 22) * h / 300
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rr * 1.3)}" ry="{f(rr)}" fill="#C8B08A" stroke="{INK}" stroke-width="1.8"></ellipse>'
                     f'<path d="M{f(x - rr * 0.6)} {f(y - rr * 0.3)} q {f(rr * 0.4)} -{f(rr * 0.3)} {f(rr * 0.8)} 0" stroke="#8A7A5A" stroke-width="1.4" fill="none"></path>')
    s = fit(b, max(h * 0.3, b - 200))
    o.append(jesus(p, w * 0.64, b, s, flip=True, glow=tone != "night"))
    return "".join(o)

def stones_close(p, w, h, seed):
    """Command that these stones become bread: round desert stones close up on the sand, the evening light — no one drawn."""
    r = random.Random(seed); b = h
    o = [sky(w, h, "#5A3A5A", "#FFB07A"), hills(w, h, h * 0.36, seed, color="#8A6A5A", amp=10, step=80), ground(w, h, h * 0.44, "#D8B07A", dy=0)]
    items = sorted((r.uniform(h * 0.5, h * 0.98), r.uniform(0, w)) for _ in range(16))
    for y, x in items:
        rr = (8 + 40 * (y - h * 0.5) / (h * 0.5)) * r.uniform(0.7, 1.1)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rr * 1.35)}" ry="{f(rr)}" fill="{r.choice(["#C8B08A", "#B8A07A", "#D8C098"])}" stroke="{INK}" stroke-width="2"></ellipse>'
                 f'<path d="M{f(x - rr * 0.7)} {f(y - rr * 0.35)} q {f(rr * 0.5)} -{f(rr * 0.35)} {f(rr)} 0" stroke="#F3E8C8" stroke-width="2" fill="none" opacity="0.7"></path>')
    return "".join(o)

def pinnacle(p, w, h, seed):
    """The pinnacle of the temple: the high corner of the temple's wall over the Kidron valley, seen from below; Jesus a
    small figure alone on the height."""
    b = h * 0.3
    o = [mk.defs(p, *ALL), sky(w, h, "#2A3A7A", "#FFC890"),
         clouds(w, h * 0.2, seed, n=4, color="#F3E8C8", op=0.5, h=h)]
    x0 = w * 0.34
    o.append(f'<path d="M{f(x0)} {f(b)} L {f(w + 10)} {f(b)} L {f(w + 10)} {f(h + 10)} L {f(x0 - w * 0.04)} {f(h + 10)} Z" fill="#D8C8A8" stroke="{INK}" stroke-width="2.6"></path>')
    for k in range(1, 14):
        y = b + (h - b) * k / 14
        o.append(f'<path d="M{f(x0 - w * 0.04 * k / 14)} {f(y)} L {f(w + 10)} {f(y)}" stroke="#A89878" stroke-width="1.6"></path>')
        for m in range(8):
            xx = x0 + (w - x0) * (m + (0.5 if k % 2 else 0)) / 8
            o.append(f'<path d="M{f(xx)} {f(y - (h - b) / 14)} L {f(xx)} {f(y)}" stroke="#A89878" stroke-width="1.2"></path>')
    o.append(f'<rect x="{f(x0 - 6)}" y="{f(b - 10)}" width="{f(w)}" height="12" fill="#E8B830" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<path d="M-10 {f(h * 0.94)} C {f(w * 0.1)} {f(h * 0.86)} {f(w * 0.2)} {f(h * 0.9)} {f(w * 0.3)} {f(h * 0.96)} L {f(w * 0.3)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A7A4A" stroke="{INK}" stroke-width="2"></path>')
    s = max(0.18, h / 1400)
    o.append(jesus(p, x0 + 20, b - 10, s, flip=True))
    return "".join(o)

def high_mountain(p, w, h, seed):
    """An exceeding high mountain, and all the kingdoms of the world and the glory of them: Jesus alone on the peak at
    the left, below him the plains and the far cities glittering gold to the horizon."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), sky(w, h, "#3A1A4A", "#FFB04A"), sun(w * 0.8, h * 0.36, 16, color="#FFE680", op=0.3),
         hills(w, h, h * 0.56, seed, color="#8A5A5A", amp=8, step=60), ground(w, h, h * 0.62, "#B8805A", dy=0)]
    for i in range(7):
        cx = w * (0.4 + 0.09 * i) + r.uniform(-10, 10); cy = h * (0.6 + 0.05 * (i % 3)); s = r.uniform(0.6, 1.1) * h / 400
        o.append(walls(cx - 30 * s, cx + 30 * s, cy, 40 * s, seed + i, color="#E8C060", lit=True, towers=2, gate=False))
        o.append(glow(cx, cy - 20 * s, 50 * s, "#FFE680", 0.6, f"{p}k{i}"))
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.3)} L {f(w * 0.08)} {f(h * 0.26)} L {f(w * 0.18)} {f(h * 0.34)} L {f(w * 0.3)} {f(h * 0.62)} L {f(w * 0.44)} {f(h + 10)} Z" fill="#4A3040" stroke="{INK}" stroke-width="2.4"></path>')
    s = fit(h * 0.3, h * 0.06) * 0.5
    o.append(jesus(p, w * 0.1, h * 0.28, s))
    return "".join(o)

def ministered(p, w, h, seed):
    """The devil leaveth him; and behold, angels came and ministered unto him: Jesus seated on a rock at dawn in the
    wilderness, two figures of white light beside him."""
    b = h * 0.92
    o = [wilderness(p, w, h, seed, john=False, tone="dawn"), glow(w * 0.5, b - h * 0.3, h * 0.6, "#FFF4C2", 0.45, f"{p}g")]
    s = fit(b, max(h * 0.26, b - 220))
    o.append(jesus(p, w * 0.5, b, s))
    o.append(angel(p, w * 0.24, b, s, up=UP_BLESS))
    o.append(angel(p, w * 0.78, b, s, flip=True, up=UP_TOUCH))
    return "".join(o)

def galilee(p, w, h, seed, town=True, tone="day", people=None):
    """The sea of Galilee: the lake under the hills, Capernaum's white houses along the shore (town=True), boats at rest."""
    top, bot = {"day": ("#8FD0E2", "#F3E8C8"), "dawn": ("#3A3A7A", "#FFC890"), "dusk": ("#4A2A5A", "#FFB07A")}[tone]
    o = [mk.defs(p, *ALL), sky(w, h, top, bot)]
    if tone == "dawn":
        o.append(sun(w * 0.7, h * 0.4, 22, color="#FFE680", op=0.5))
    o += [hills(w, h, h * 0.36, seed, color="#7A8A6A" if tone == "day" else "#5A4A6A", amp=16, step=90),
          lake(w, h, h * 0.44, seed, color="#2A7FA8" if tone == "day" else "#4A6A9A")]
    if tone == "dawn":
        o.append(f'<path d="M{f(w * 0.6)} {f(h * 0.45)} L {f(w * 0.8)} {f(h * 0.45)} L {f(w * 0.74)} {f(h * 0.7)} L {f(w * 0.66)} {f(h * 0.7)} Z" fill="#FFE680" opacity="0.4"></path>')
    if town:
        o.append(shore(w, h, h * 0.66, x0=-10, x1=w * 0.5) + houses(w, h, h * 0.7, seed, x0=-10, x1=w * 0.44, hmin=0.14, hmax=0.24))
        o.append(boat(p, w * 0.62, h * 0.66, h / 900, mast=True))
    return "".join(o)

def fishers(p, w, h, seed):
    """Walking by the sea of Galilee he saw Simon and Andrew casting a net into the sea: Jesus on the shore, his arm out,
    the two brothers in the boat, the net flying."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.34, seed, color="#7A8A6A", amp=14, step=90), lake(w, h, h * 0.42, seed),
         shore(w, h, h * 0.78, x0=-10, x1=w * 0.42)]
    s = fit(b, max(h * 0.3, b - 240))
    o.append(boat(p, w * 0.7, h * 0.72, s * 0.95, crew=[(-30, ("up", ROBES["peter"])), (34, ROBES["andrew"])], mast=True, flip=True))
    o.append(net_cast(w * 0.5, h * 0.6, w * 0.1, seed))
    o.append(jesus(p, w * 0.2, b, s, up=UP_CALL))
    return "".join(o)

def zebedee(p, w, h, seed, leaving=False):
    """James and John in the boat with Zebedee their father, mending their nets; leaving=True: the two brothers stepping
    out onto the shore, the old man left in the boat."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.34, seed, color="#7A8A6A", amp=14, step=90), lake(w, h, h * 0.42, seed),
         shore(w, h, h * 0.76)]
    s = fit(b, max(h * 0.3, b - 240))
    if leaving:
        o.append(boat(p, w * 0.72, h * 0.7, s, crew=[(0, ("old", "#5A5A6A"))], mast=False))
        o.append(disciple(p, w * 0.42, b, s, "james") + disciple(p, w * 0.32, b, s * 0.98, "john"))
        o.append(jesus(p, w * 0.12, b, s))
    else:
        o.append(boat(p, w * 0.5, h * 0.72, s * 1.1, crew=[(-46, ("old", "#5A5A6A")), (10, ROBES["james"]), (54, ROBES["john"])], mast=False, net=True))
        o.append(jesus(p, w * 0.12, b, s, up=UP_CALL))
    return "".join(o)

def synagogue(p, w, h, seed, teaching=True, crowd_n=8):
    """A synagogue of Galilee: stone benches, columns, the lamp, the reading-desk; Jesus standing to teach, the people
    seated about him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bgr(w, h, "#C8B490"),
         f'<rect x="-10" y="{f(h * 0.08)}" width="{f(w + 20)}" height="{f(h * 0.05)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>']
    for x in (0.08, 0.3, 0.7, 0.92):
        o.append(f'<rect x="{f(w * x - 14)}" y="{f(h * 0.13)}" width="28" height="{f(b - h * 0.13)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(w * x - 20)}" y="{f(h * 0.13)}" width="40" height="10" fill="#D8C8A0" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="-10" y="{f(b - h * 0.08)}" width="{f(w + 20)}" height="{f(h)}" fill="#A8906A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(w * 0.19)} {f(h * 0.13)} L {f(w * 0.19)} {f(h * 0.3)}" stroke="#4A3A2A" stroke-width="2"></path>' + clay_lamp(w * 0.19, h * 0.34, max(0.6, h / 300)))
    s = fit(b, max(h * 0.2, b - 230))
    if teaching:
        o.append(f'<rect x="{f(w * 0.58)}" y="{f(b - 70 * s)}" width="{f(50 * s)}" height="{f(70 * s)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>')
        o.append(jesus(p, w * 0.5, b, s))
    r = random.Random(seed)
    for i in range(crowd_n):
        x = w * (0.04 + 0.92 * i / max(1, crowd_n - 1))
        if abs(x - w * 0.5) < w * 0.14: continue
        o.append(seated(x, b, s * 0.85, r.choice(HEB), head=r.choice(["#E8E2D6", "#3A4A6A", "#6A5A3A", None]), beard=r.choice(["#2A1A10", "#6A645E", None]), flip=x > w * 0.5))
    return "".join(o)

def multitudes(p, w, h, seed, sick=True):
    """Great multitudes following him from every side: Jesus on the road among the hills of Galilee, the people pressing
    after him, some carried on beds, the lame on staves."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#8A9A6A", amp=16, step=90),
         lake(w, h, h * 0.46, seed, n=6), hills(w, h, h * 0.56, seed + 2, color="#9AAA5A", amp=10, step=70), ground(w, h, h * 0.66, "#B8A86A", dy=0)]
    s = fit(b, max(h * 0.3, b - 230))
    yb = b - 80 * s
    o.append(crowd(p, w * 0.42, w * 0.96, yb, yb - 110 * s, 9, seed + 1, flip=True))
    o.append(crowd(p, w * 0.34, w * 0.92, b, b - 165 * s, 6, seed, flip=True))
    o.append(jesus(p, w * 0.16, b, s * 1.04))
    return "".join(o)

JESUS_HAIR = "#3A2416"
