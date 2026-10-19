"""Drawings for the Psalms: scenes taken from the psalms' own images, each a full panel f(p, w, h, seed) with its subject in
the lower part (the song lines sit over the sky). SCENES maps a plan key to (panel background, scene). The seed varies each
scene (time of day, the lie of the hills) so a drawing repeated in one psalm is never the same twice. God is never drawn:
his presence is light, rays, cloud, fire and storm.

Builds on the earlier volumes: chr2.art (and through it chr1, kg2, kg1), sa2.art, the kit (samuel2's David and harp,
exodus' sheep and fire, judges' lion and chaff, ruth's field and reapers)."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, joshua1 as J, judges1 as J1, judges2 as J2, ruth1 as R1, samuel1 as S1, samuel2 as S2, samuel3 as S3, samuel4 as S4
from genesis.art2 import fit, ground, hills, bird, birds, rain as rain_lines, sea as sea_band, SKIN
from genesis.art3 import sun, label, man, woman, king, grid_bg, node, route
from genesis import art as GA
from exo import art as A, art6 as A6
from num.art import ALL
from sa2 import art as SA
from sa2.art import sky, king_fig
from kg1 import art as K1
from kg2 import art as K2
from chr1 import art as C1

def f(v): return f"{v:.1f}"
R = random.Random

# ---- palettes: time of day by seed -----------------------------------------------------------------------------------------
DAY = ("#8FD0E2", "#F3E8C8")
DAWN = ("#5A5A8A", "#FFC89A")
DUSK = ("#3A2A5A", "#FF9A5A")
NIGHT = ("#0B0B2A", "#2A2A5A")
GOLD = ("#FFB04A", "#FFF0C8")
def tod(seed, opts=(DAY, DAWN, DAY, DUSK)):
    return opts[seed % len(opts)]

def bgrect(w, h, c): return f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{c}"></rect>'

# ---- figures -----------------------------------------------------------------------------------------------------------------
PRAY = [(-22, -158), (-14, -200), (-4, -236)]          # one arm lifted (the figures are drawn front-on)
def singer(p, x, y, s, cloth="#F3EFE6", flip=False, up=None, beard=None):
    """A Levite singer at a distance: white linen robe and headcloth."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, sw=3, flip=flip, up=up, extra=A.headcloth(cloth) + (beard or A.BLACK_BEARD))
def prayer(p, x, y, s, cloth="#5A4A7A"):
    """A man with both hands lifted up (front-on), headcloth and beard."""
    uid = f"{p}pb{int(x)}"
    return (E4.figure_both(x, y, s, SKIN, cloth, [(-22, -158), (-44, -194), (-54, -230)], [(22, -158), (44, -194), (54, -230)], uid)
            + f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">' + A.headcloth(cloth) + A.BLACK_BEARD + '</g>')

def walker(p, x, y, s, cloth="#6A5A3A", flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind="Tunic", sw=3, flip=flip, up=up, extra=A.headcloth(cloth) + A.BLACK_BEARD)
def shepherd(p, x, y, s, flip=False):
    return S2.david(p, round(x), round(y), round(s, 3), flip=flip)

# ---- shared pieces -----------------------------------------------------------------------------------------------------------
def tree(x, base, s, seed=1, fruit=True, leaf=("#3F8A44", "#2E6A32", "#5E8F26")):
    """A broad tree: trunk and a round crown of leaves (fruit=True: red fruit among them). About 260 units tall at s=1."""
    r = R(seed)
    o = [f'<g transform="translate({f(x)} {f(base)}) scale({f(s)})">',
         '<path d="M-16 0 C -10 -50 -14 -100 -40 -150 L -22 -152 C -6 -120 0 -110 6 -150 L 22 -150 C 12 -100 10 -50 18 0 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for _ in range(14):
        o.append(f'<circle cx="{f(r.uniform(-90, 90))}" cy="{f(r.uniform(-250, -150))}" r="{f(r.uniform(32, 52))}" fill="{r.choice(leaf)}" stroke="#0D0D0F" stroke-width="2"></circle>')
    if fruit:
        for _ in range(12):
            o.append(f'<circle cx="{f(r.uniform(-90, 90))}" cy="{f(r.uniform(-250, -150))}" r="6" fill="#D7261E" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    o.append("</g>")
    return "".join(o)

def stream(w, y0, y1, seed, color="#2C9DB8"):
    """A stream winding across the foot of the panel between y0 (far) and y1 (near)."""
    r = R(seed)
    xs = [-20, w * 0.25, w * 0.55, w * 0.8, w + 20]
    ys = [y0 + (y1 - y0) * k for k in (0.2, 0.6, 0.3, 0.8, 0.5)]
    top = " ".join(f"{f(x)} {f(y)}" for x, y in zip(xs, ys))
    bot = " ".join(f"{f(x)} {f(y + 18 + 10 * i)}" for i, (x, y) in reversed(list(enumerate(zip(xs, ys)))))
    o = [f'<path d="M{top.split()[0]} {top.split()[1]} L {top} L {bot} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2" stroke-linejoin="round"></path>']
    for i in range(10):
        x = r.uniform(0, w); k = r.uniform(0, 1)
        o.append(f'<path d="M{f(x)} {f(y0 + (y1 - y0) * k + 12)} l 22 0" stroke="#E8F6FA" stroke-width="2" opacity="0.7"></path>')
    return "".join(o)

def clouds(w, h, seed, n=6, color="#F3EFE6", op=0.9, y0=0.05, y1=0.35):
    r = R(seed)
    return "".join(f'<ellipse cx="{f(r.uniform(0, w))}" cy="{f(h * r.uniform(y0, y1))}" rx="{f(w * r.uniform(0.08, 0.18))}" ry="{f(h * r.uniform(0.03, 0.06))}" fill="{color}" opacity="{op}"></ellipse>' for _ in range(n))

def moon(x, y, r_, color="#F3EFE6"):
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r_ * 2.6)}" fill="{color}" opacity="0.12"></circle>'
            f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r_)}" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></circle>'
            f'<circle cx="{f(x + r_ * 0.35)}" cy="{f(y - r_ * 0.15)}" r="{f(r_ * 0.86)}" fill="#1A1A3A" opacity="0.0"></circle>')

def mountain(cx, base, wd, ht, color="#6A5A7A", snow=False, lit="#8A7A9A"):
    o = [f'<path d="M{f(cx - wd / 2)} {f(base)} L {f(cx - wd * 0.08)} {f(base - ht)} L {f(cx + wd * 0.04)} {f(base - ht * 0.94)} L {f(cx + wd / 2)} {f(base)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>',
         f'<path d="M{f(cx - wd * 0.08)} {f(base - ht)} L {f(cx + wd * 0.04)} {f(base - ht * 0.94)} L {f(cx + wd * 0.2)} {f(base)} L {f(cx + wd * 0.02)} {f(base)} Z" fill="{lit}" opacity="0.6"></path>']
    if snow:
        o.append(f'<path d="M{f(cx - wd * 0.08)} {f(base - ht)} L {f(cx - wd * 0.17)} {f(base - ht * 0.78)} L {f(cx - wd * 0.08)} {f(base - ht * 0.82)} L {f(cx)} {f(base - ht * 0.76)} L {f(cx + wd * 0.1)} {f(base - ht * 0.8)} L {f(cx + wd * 0.04)} {f(base - ht * 0.94)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.8"></path>')
    return "".join(o)

def glow(x, y, rad, color="#FFE680", op=0.18):
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rad)}" fill="{color}" opacity="{op}"></circle>'
            f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rad * 0.55)}" fill="{color}" opacity="{op}"></circle>')

def zion_city(cx, base, wd, ht, seed, lit=False):
    """Jerusalem on its hill with the house of Jehovah at the top."""
    return J.city_hill(cx, base, wd * 0.5, ht * 0.62, seed) + K1.temple_front(cx, base - ht * 0.58, wd * 0.3, seed)

def lightning(x, y, l, sw=4, color="#FFF4C2"):
    return f'<path d="M{f(x)} {f(y)} l -{f(l * 0.12)} {f(l * 0.35)} l {f(l * 0.14)} 0 l -{f(l * 0.2)} {f(l * 0.65)}" stroke="{color}" stroke-width="{sw}" fill="none" stroke-linejoin="round"></path>'

def dog(x, y, s=1.0, flip=False, color="#3A2A1E"):
    """A lean dog prowling (side view, facing right), about 90 units long."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})"><path d="M-44 -30 C -30 -40 10 -40 28 -36 L 40 -50 L 50 -48 L 48 -40 L 58 -34 L 46 -28 L 34 -28 '
            f'L 30 -20 L 32 0 L 26 0 L 22 -18 L -20 -18 L -26 0 L -32 0 L -32 -20 C -40 -22 -46 -26 -56 -40 L -50 -42 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path></g>')

def bull(x, y, s=1.0, flip=False, color="#3A2418"):
    """A bull of Bashan: heavy shoulders, horns lowered (side view, facing right), about 150 units long."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})"><path d="M-70 -50 C -70 -80 -30 -96 20 -96 C 50 -96 62 -84 70 -70 L 84 -66 C 92 -60 92 -48 84 -42 L 70 -38 '
            f'L 60 -30 L 56 0 L 46 0 L 42 -26 L -40 -26 L -46 0 L -56 0 L -58 -30 C -66 -34 -70 -40 -70 -50 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>'
            f'<path d="M66 -80 C 76 -96 92 -98 98 -90 C 88 -90 80 -86 74 -76 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></path><circle cx="80" cy="-62" r="2.4" fill="#D7261E"></circle></g>')

def hart(x, y, s=1.0, flip=False, color="#A8642E", drink=False):
    """A hart with antlers (side view, facing right), about 120 units long; drink=True: neck stretched down to the water."""
    sx = -s if flip else s
    legs = "".join(f'<path d="M{a} -46 L {b} 0" stroke="{color}" stroke-width="6" stroke-linecap="round"></path>' for a, b in ((-40, -44), (-30, -26), (24, 20), (34, 38)))
    if drink:
        neck = '<path d="M24 -70 L 52 -28 L 66 -30 L 44 -62 Z" fill="{c}" stroke="#0D0D0F" stroke-width="2"></path>'
        head = '<ellipse cx="0" cy="0" rx="14" ry="8" transform="translate(64 -20) rotate(62)" fill="{c}" stroke="#0D0D0F" stroke-width="2"></ellipse><path d="M54 -36 l -10 -6 l 6 10 Z" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></path>'
        ant = "M56 -34 l -8 -24 m 4 12 l -12 -4 M60 -36 l 0 -26 m 0 10 l 10 -8"
    else:
        neck = '<path d="M24 -72 L 40 -106 L 54 -104 L 44 -64 Z" fill="{c}" stroke="#0D0D0F" stroke-width="2"></path>'
        head = '<ellipse cx="0" cy="0" rx="15" ry="8" transform="translate(58 -104) rotate(24)" fill="{c}" stroke="#0D0D0F" stroke-width="2"></ellipse><path d="M42 -112 l -12 -8 l 4 12 Z" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></path>'
        ant = "M46 -112 l -8 -28 m 3 12 l -12 -8 m 14 -6 l 6 -12 M52 -112 l 6 -28 m -2 12 l 12 -8"
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">{legs}'
            f'<path d="M-50 -62 C -46 -80 26 -82 40 -70 C 46 -60 44 -48 36 -44 L -42 -44 C -52 -48 -54 -56 -50 -62 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.2"></path>'
            + neck.format(c=color) + head.format(c=color)
            + f'<path d="M-50 -64 l -8 -4 l 4 8 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.2"></path>'
            f'<path d="{ant}" stroke="#4A2A14" stroke-width="3.4" fill="none" stroke-linecap="round"></path></g>')

def cedar(x, base, s, seed=1):
    """A cedar of Lebanon: a thick trunk and broad flat tiers of dark green, about 300 units tall at s=1."""
    o = [f'<g transform="translate({f(x)} {f(base)}) scale({f(s)})"><path d="M-14 0 L -8 -280 L 8 -280 L 14 0 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i, (y, wd) in enumerate(((-90, 150), (-150, 130), (-205, 104), (-255, 72), (-296, 40))):
        o.append(f'<path d="M{-wd} {y} C {-wd * 0.6} {y - 34} {wd * 0.6} {y - 34} {wd} {y} C {wd * 0.5} {y + 12} {-wd * 0.5} {y + 12} {-wd} {y} Z" fill="{("#1F4A34", "#2E6A32")[i % 2]}" stroke="#0D0D0F" stroke-width="2.2"></path>')
    return "".join(o) + "</g>"

def pots(x, y, s, seed, broken=True):
    """Potter's vessels: whole jars, or (broken) dashed in pieces."""
    r = R(seed); o = []
    for i in range(4):
        px = x + (i - 1.5) * 70 * s
        if broken:
            for k in range(4):
                a = r.uniform(0, math.pi)
                o.append(f'<path d="M{f(px + r.uniform(-30, 30) * s)} {f(y - r.uniform(0, 10) * s)} l {f(20 * s * math.cos(a))} {f(-14 * s)} l {f(16 * s)} {f(6 * s)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.8"></path>')
        else:
            o.append(f'<path d="M{f(px - 16 * s)} {f(y)} C {f(px - 34 * s)} {f(y - 40 * s)} {f(px - 20 * s)} {f(y - 66 * s)} {f(px - 10 * s)} {f(y - 70 * s)} L {f(px + 10 * s)} {f(y - 70 * s)} C {f(px + 20 * s)} {f(y - 66 * s)} {f(px + 34 * s)} {f(y - 40 * s)} {f(px + 16 * s)} {f(y)} Z" fill="#C8783A" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def bow_arrow(x, y, s, rot=0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(s)})"><path d="M0 -60 C 30 -40 30 40 0 60" stroke="#5A3A22" stroke-width="5" fill="none"></path>'
            f'<path d="M0 -60 L -20 0 L 0 60" stroke="#E8E2D6" stroke-width="1.4" fill="none"></path><path d="M-20 0 L 60 0" stroke="#3A2A1E" stroke-width="3"></path>'
            f'<path d="M60 0 l -10 -5 l 0 10 Z" fill="#8A8A9A" stroke="#0D0D0F" stroke-width="1"></path></g>')

def nest(x, y, s, young=3):
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-40 0 C -40 -20 40 -20 40 0 C 30 12 -30 12 -40 0 Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2"></path>']
    for i in range(young):
        cx = (i - (young - 1) / 2) * 22
        o.append(f'<circle cx="{f(cx)}" cy="-16" r="9" fill="#C8A06A" stroke="#0D0D0F" stroke-width="1.6"></circle><path d="M{f(cx + 6)} -18 l 8 -2 l -7 5 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></path>')
    return "".join(o) + "</g>"

def small_bird(x, y, s=1.0, color="#6A4A2A", flip=False, fly=False):
    """A sparrow or swallow (side view, facing right), about 50 units long; fly=True: wings raised in flight."""
    sx = -s if flip else s
    dark = "#2A1A10"
    wing = ('<path d="M-6 -6 C -10 -30 4 -42 14 -40 C 8 -30 6 -18 6 -6 Z" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></path>' if fly
            else '<path d="M-12 -4 C -6 -14 8 -12 10 -4 C 2 0 -6 0 -12 -4 Z" fill="{d}" stroke="#0D0D0F" stroke-width="1.2"></path>').format(c=color, d=dark)
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})"><path d="M-14 0 L -30 -8 L -26 0 L -30 8 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.4"></path>'
            f'<ellipse cx="0" cy="0" rx="16" ry="9" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></ellipse><circle cx="14" cy="-7" r="7.5" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></circle>'
            f'<path d="M20 -9 l 8 2 l -8 3 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></path><circle cx="16" cy="-9" r="1.5" fill="#0D0D0F"></circle>'
            f'<path d="M-6 4 C 0 8 8 8 12 2" fill="none" stroke="#F3EFE6" stroke-width="1.6" opacity="0.6"></path>{wing}</g>')

def fish(x, y, s=1.0, flip=False, color="#C8B87A"):
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})"><path d="M-20 0 C -10 -12 14 -12 22 0 C 14 12 -10 12 -20 0 Z M-20 0 L -32 -10 L -30 10 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></path>'
            f'<circle cx="12" cy="-2" r="1.6" fill="#0D0D0F"></circle></g>')

# ---- scenes -------------------------------------------------------------------------------------------------------------------
def s_tree(p, w, h, seed):
    """Like a tree planted by the streams of water, that bringeth forth its fruit in its season."""
    t, b = tod(seed, (DAY, DAWN))
    o = [sky(w, h, t, b), sun(w * 0.82, h * 0.3, 18, color="#FFE680", op=0.35), hills(w, h, h * 0.62, seed, color="#7AA85A", amp=10), ground(w, h, h * 0.7, "#9CCB5E", dy=0),
         stream(w, h * 0.8, h * 0.9, seed), tree(w * 0.44, h * 0.84, min(1.3, h * 0.5 / 260), seed)]
    o.append(tree(w * 0.86, h * 0.74, min(0.5, h * 0.22 / 260), seed + 1, fruit=False))
    return "".join(o)

def s_chaff(p, w, h, seed):
    """The wicked are like the chaff which the wind driveth away: the threshing-floor at evening, the chaff blown off."""
    b = h * 0.86
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A5A", "#FFB070"), hills(w, h, h * 0.66, seed, color="#6A4A4A", amp=8), ground(w, h, h * 0.74, "#B89A6A", dy=0),
         f'<ellipse cx="{f(w * 0.36)}" cy="{f(b)}" rx="{f(w * 0.2)}" ry="{f(h * 0.05)}" fill="#D8B878" stroke="#0D0D0F" stroke-width="2"></ellipse>',
         R1.heap(w * 0.3, b, w * 0.1, h * 0.08)]
    s = fit(b, h * 0.52)
    o.append(walker(p, w * 0.46, b, s, cloth="#8A6A4A", up=[(-22, -158), (-30, -200), (-24, -238)]))
    o.append(J1.chaff(140, w * 0.42, w * 1.05, h * 0.3, h * 0.8, seed))
    for i in range(8):
        y = h * (0.35 + i * 0.05)
        o.append(f'<path d="M{f(w * 0.5)} {f(y)} C {f(w * 0.7)} {f(y - 10)} {f(w * 0.85)} {f(y + 6)} {f(w * 1.02)} {f(y - 4)}" stroke="#F3EFE6" stroke-width="1.6" fill="none" opacity="0.5"></path>')
    return "".join(o)

def s_path(p, w, h, seed):
    """The way of the righteous: a path climbing through the fields toward the dawn, a traveller on it."""
    t, b = tod(seed, (DAWN, DAY))
    o = [mk.defs(p, *ALL), sky(w, h, t, b), sun(w * 0.62, h * 0.52, 22, color="#FFE680", op=0.5), hills(w, h, h * 0.54, seed, color="#6A8A5A", amp=10), ground(w, h, h * 0.6, "#8AB85A", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.4)} {f(h * 0.82)} {f(w * 0.66)} {f(h * 0.74)} {f(w * 0.6)} {f(h * 0.6)} L {f(w * 0.63)} {f(h * 0.6)} C {f(w * 0.72)} {f(h * 0.74)} {f(w * 0.56)} {f(h * 0.84)} {f(w * 0.6)} {f(h + 10)} Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></path>']
    o.append(walker(p, w * 0.5, h * 0.86, fit(h * 0.86, h * 0.62), cloth="#5A6A8A"))
    return "".join(o)

def s_kings(p, w, h, seed):
    """Why do the nations rage? The kings of the earth set themselves: crowned kings and their spears under a red sky."""
    b = h * 0.92; r = R(seed)
    o = [mk.defs(p, *ALL), sky(w, h, "#3A0A1A", "#C8402A"), hills(w, h, h * 0.62, seed, color="#3A1A2A", amp=12), ground(w, h, h * 0.7, "#5A2A2A", dy=0)]
    for i in range(16):
        x = w * (0.04 + i * 0.062); y = h * 0.72
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - h * 0.16)}" stroke="#0D0D0F" stroke-width="2"></path><path d="M{f(x - 3)} {f(y - h * 0.16)} l 3 -9 l 3 9 Z" fill="#8A8A9A"></path>')
    s = fit(b, h * 0.54)
    for i, c in enumerate(("#5A1A4A", "#1F4A7A", "#7A3A1A", "#3A5A2A", "#6A2A2A")):
        o.append(king(p, w * (0.14 + i * 0.18), b - (i % 2) * 6, s * (0.92 + 0.08 * (i % 2)), c, flip=i > 2))
    return "".join(o)

def s_throne(p, w, h, seed):
    """Yet I have set my king upon my holy hill of Zion: the king crowned, on Zion's height, the city below in gold light."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#FFB04A", "#FFF0C8"), V.rays(w * 0.5, h * 0.1, 30, 20, max(w, h), color="#FFF4C2", op=0.2),
         zion_city(w * 0.74, h * 0.8, w * 0.5, h * 0.5, seed), ground(w, h, h * 0.8, "#C8A06A", dy=0),
         S3.throne(w * 0.3, b, min(1.4, h / 330))]
    o.append(king_fig(p, w * 0.3, b - h * 0.1, fit(b, h * 0.5) * 0.8))
    return "".join(o)

def s_potsherd(p, w, h, seed):
    """Thou shalt dash them in pieces like a potter's vessel: the rod of iron and the jars broken on the stones."""
    o = [sky(w, h, "#3A2A3A", "#8A5A4A"), ground(w, h, h * 0.66, "#6A5A4A", dy=0), pots(w * 0.5, h * 0.9, min(1.6, h / 240), seed),
         f'<path d="M{f(w * 0.2)} {f(h * 0.55)} L {f(w * 0.62)} {f(h * 0.82)}" stroke="#4A4A5A" stroke-width="12" stroke-linecap="round"></path>',
         f'<path d="M{f(w * 0.2)} {f(h * 0.55)} L {f(w * 0.62)} {f(h * 0.82)}" stroke="#8A8A9A" stroke-width="4" stroke-linecap="round"></path>',
         mk.speed(w * 0.62, h * 0.84, 18, 20, 120, seed, color="#F3EFE6", op=0.5)]
    return "".join(o)

def s_camp_round(p, w, h, seed):
    """Ten thousands of the people that have set themselves against me round about: a lone tent on a hill at night, the
    enemies' camp-fires all round it."""
    r = R(seed)
    o = [sky(w, h, *NIGHT), mk.stars(80, w, h * 0.5, seed), hills(w, h, h * 0.66, seed, color="#1A1430", amp=8)]
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.82)} C {f(w * 0.4)} {f(h * 0.6)} {f(w * 0.6)} {f(h * 0.6)} {f(w * 0.7)} {f(h * 0.82)} Z" fill="#2A2440" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(E4.tent(w * 0.5, h * 0.66, w * 0.08, h * 0.08, color="#5A3A22"))
    for i in range(24):
        x = r.uniform(0, w); y = r.uniform(h * 0.72, h * 0.98)
        if abs(x - w * 0.5) < w * 0.16 and y < h * 0.84: continue
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(3, 6))}" fill="#FF8A3D"></circle><circle cx="{f(x)}" cy="{f(y)}" r="12" fill="#FF6A2A" opacity="0.25"></circle>')
    return "".join(o)

def s_night(p, w, h, seed):
    """I laid me down and slept: a sleeper on his bed by the window at night, a clay lamp burning low."""
    from genesis.art4 import clay_lamp
    b = h * 0.9
    o = [bgrect(w, h, "#1A1430"), f'<rect x="{f(w * 0.56)}" y="{f(h * 0.12)}" width="{f(w * 0.3)}" height="{f(h * 0.4)}" fill="#0B0B2A" stroke="#0D0D0F" stroke-width="3"></rect>',
         f'<g transform="translate({f(w * 0.56)} {f(h * 0.12)})">{mk.stars(30, w * 0.3, h * 0.4, seed)}</g>', moon(w * 0.78, h * 0.24, min(16, h * 0.04)),
         f'<rect x="{f(w * 0.56)}" y="{f(h * 0.12)}" width="{f(w * 0.3)}" height="{f(h * 0.4)}" fill="none" stroke="#3A2A1E" stroke-width="8"></rect>',
         f'<rect x="-10" y="{f(h * 0.78)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2034" stroke="#0D0D0F" stroke-width="2"></rect>',
         S1.mat_sleeper(w * 0.4, b, min(1.4, h / 300), color="#E8E2D6"), glow(w * 0.12, b - 20, h * 0.3, "#FFC14D", 0.12), clay_lamp(w * 0.12, b, min(1.4, h / 300))]
    return "".join(o)

def s_harvest(p, w, h, seed):
    """Thou hast put gladness in my heart, more than when their grain and their new wine are increased: reapers in the ripe
    field, sheaves standing, the vineyard on the hill."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, *GOLD), sun(w * 0.15, h * 0.3, 20, color="#FFE680", op=0.4), hills(w, h, h * 0.56, seed, color="#8A9A4A", amp=10),
         ground(w, h, h * 0.64, "#D8B86A", dy=0), R1.field(-10, w + 10, h * 0.66, h * 0.16, seed, rows=3)]
    s = fit(b, h * 0.56)
    o.append(R1.reaper(p, w * 0.3, b, s) + R1.sheaf(w * 0.5, b, s * 2.4) + R1.sheaf(w * 0.62, b - 6, s * 2.1) + R1.reaper(p, w * 0.8, b, s * 0.95, flip=True, cloth="#6A5A3A"))
    return "".join(o)

def s_lions(p, w, h, seed):
    """Lest they tear my soul like a lion: a lion roaring in the dark thicket."""
    r = R(seed)
    o = [sky(w, h, "#1A0A0A", "#5A2A1A"), hills(w, h, h * 0.6, seed, color="#2A1A14", amp=14)]
    for i in range(12):
        x = r.uniform(0, w)
        o.append(f'<path d="M{f(x)} {f(h + 10)} L {f(x + r.uniform(-40, 40))} {f(h * r.uniform(0.5, 0.7))}" stroke="#1A120A" stroke-width="{f(r.uniform(3, 7))}"></path>')
    o.append(J2.lion(w * 0.3, h * 0.94, min(1.6, h / 220), roar=True))
    if w > 500: o.append(J2.lion(w * 0.78, h * 0.9, min(1.0, h / 360), flip=True, roar=False))
    return "".join(o)

def s_bow(p, w, h, seed):
    """The wicked bend the bow, they make ready their arrow upon the string, that they may shoot in darkness."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#0B0B2A", "#3A2A4A"), mk.stars(40, w, h * 0.4, seed), hills(w, h, h * 0.7, seed, color="#1A1430", amp=10)]
    s = fit(b, h * 0.48)
    o.append(mk.person(p, round(w * 0.22), round(b), s, body="#0D0D0F", cloth="#1A1A1A", kind="Tunic", sw=3, up=[(22, -158), (60, -160), (96, -164)]))
    o.append(bow_arrow(w * 0.22 + 100 * s, b - 164 * s, s * 0.9))
    for i in range(3):
        y = h * (0.42 + i * 0.08)
        o.append(f'<path d="M{f(w * (0.5 + i * 0.06))} {f(y)} l 70 -6" stroke="#F3EFE6" stroke-width="2" opacity="0.7"></path>')
    return "".join(o)

def s_pit(p, w, h, seed):
    """He brought me up also out of a horrible pit, out of the miry clay; and he set my feet upon a rock: the pit's dark mouth
    below, a figure standing on the rock in the light above it."""
    b = h * 0.74
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A8A", "#F3E8C8"), V.rays(w * 0.7, -20, 24, 20, max(w, h) * 1.2, color="#FFF4C2", op=0.2),
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A2A1E" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.08)} {f(b)} C {f(w * 0.1)} {f(h * 1.1)} {f(w * 0.4)} {f(h * 1.1)} {f(w * 0.46)} {f(b)} Z" fill="#0D0A08" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.12)} {f(h * 0.96)} C {f(w * 0.2)} {f(h * 0.92)} {f(w * 0.34)} {f(h * 0.94)} {f(w * 0.42)} {f(h * 0.9)} L {f(w * 0.44)} {f(h * 1.0)} L {f(w * 0.14)} {f(h * 1.0)} Z" fill="#4A3A22" opacity="0.8"></path>',
         f'<path d="M{f(w * 0.56)} {f(b)} L {f(w * 0.62)} {f(b - h * 0.08)} L {f(w * 0.8)} {f(b - h * 0.1)} L {f(w * 0.88)} {f(b)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    o.append(prayer(p, w * 0.72, b - h * 0.09, fit(b - h * 0.09, h * 0.42), cloth="#5A4A7A"))
    return "".join(o)

def s_heavens(p, w, h, seed):
    """When I consider thy heavens, the moon and the stars, which thou hast ordained: a small figure on a hill under the night."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#2A2A5A"), mk.stars(220, w, h * 0.8, seed),
         f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.2)} {f(w * 0.6)} {f(h * 0.3)} {f(w + 10)} {f(h * 0.05)}" stroke="#8A8AC8" stroke-width="{f(h * 0.12)}" fill="none" opacity="0.18"></path>',
         moon(w * 0.82, h * 0.2, min(22, h * 0.06)), hills(w, h, h * 0.84, seed, color="#0B0B1A", amp=10)]
    o.append(mk.person(p, round(w * 0.3), round(h * 0.86), fit(h * 0.86, h * 0.7), body="#0D0D0F", cloth="#14142A", sw=2, up=PRAY))
    return "".join(o)

def s_creation(p, w, h, seed):
    """All sheep and oxen, and the beasts of the field, the birds of the heavens, and the fish of the sea."""
    b = h * 0.7
    o = [sky(w, h, *DAY), hills(w, h, h * 0.52, seed, color="#7AA85A", amp=10), ground(w, h, h * 0.58, "#9CCB5E", dy=0),
         birds(7, w * 0.1, w * 0.9, h * 0.2, h * 0.4, seed, 0.8, 1.4)]
    s = min(1.0, h / 360)
    for i in range(5): o.append(E.sheep(w * (0.08 + i * 0.07), b - (i % 2) * 8, s * 0.9))
    o.append(S1.cow(w * 0.52, b, s * 0.9) + S1.cow(w * 0.66, b + 6, s * 0.8, flip=True))
    o.append(sea_band(w, h, h * 0.78, seed, amp=6))
    for i in range(6): o.append(fish(w * (0.1 + i * 0.16), h * (0.86 + (i % 2) * 0.06), s * 1.2, flip=i % 2))
    return "".join(o)

def s_gates(p, w, h, seed):
    """Lift up your heads, O ye gates: the gate of the city open, its doors lifted, light streaming through."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#FFB04A", "#FFF0C8"), V.rays(w * 0.5, h * 0.6, 30, 20, max(w, h), color="#FFF4C2", op=0.3),
         S4.gatehouse(w * 0.5, b, w * 0.62, h * 0.56, lit=True), ground(w, h, b, "#C8A06A", dy=0)]
    s = fit(b, h * 0.66)
    for i in range(4):
        o.append(walker(p, w * (0.12 + i * 0.06), b, s * (0.9 + 0.04 * i), cloth=("#5A6A8A", "#8A5A3A", "#3A6A5A", "#7A3A4A")[i]))
    return "".join(o)

def s_court(p, w, h, seed):
    """The house of Jehovah and its courts, the people gathered."""
    return K1.court_scene(p, w, h, seed, crowd=True, smoke=seed % 2 == 0)

def s_music(p, w, h, seed):
    """Sing praises unto Jehovah: Levites with harps and cymbals."""
    return C1.singers(p, w, h, seed, n=6 if w > 500 else 3, top=0.56)

def s_glory(p, w, h, seed):
    """Jehovah in his holy temple, his throne in heaven: light breaking through the clouds (God is never drawn)."""
    o = [sky(w, h, "#2A2A6A", "#FFE6A0"), V.rays(w * 0.5, h * 0.12, 40, 20, max(w, h) * 1.3, color="#FFF4C2", op=0.35),
         glow(w * 0.5, h * 0.12, h * 0.4, "#FFF4C2", 0.25), clouds(w, h, seed, 8, "#E8E2F0", 0.85, 0.05, 0.3), hills(w, h, h * 0.84, seed, color="#3A3A5A", amp=10)]
    return "".join(o)

def s_waves(p, w, h, seed):
    return SA.waves(w, h, seed)

def s_net(p, w, h, seed):
    """The net which they hid: a fowler's net spread on the path in the dusk, a bird caught in its mesh."""
    o = [sky(w, h, *DUSK), hills(w, h, h * 0.6, seed, color="#3A2A3A", amp=10), ground(w, h, h * 0.68, "#6A5A3A", dy=0)]
    cx, cy, rw, rh = w * 0.5, h * 0.84, w * 0.3, h * 0.1
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rw)}" ry="{f(rh)}" fill="#4A3A22" opacity="0.5" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    for i in range(-6, 7):
        o.append(f'<path d="M{f(cx + i * rw / 7)} {f(cy - rh * math.sqrt(max(0, 1 - (i / 7) ** 2)))} L {f(cx + i * rw / 7)} {f(cy + rh * math.sqrt(max(0, 1 - (i / 7) ** 2)))}" stroke="#C8A06A" stroke-width="1.4"></path>')
    for j in range(-3, 4):
        o.append(f'<path d="M{f(cx - rw * math.sqrt(max(0, 1 - (j / 4) ** 2)))} {f(cy + j * rh / 4)} L {f(cx + rw * math.sqrt(max(0, 1 - (j / 4) ** 2)))} {f(cy + j * rh / 4)}" stroke="#C8A06A" stroke-width="1.4"></path>')
    o.append(f'<path d="M{f(cx + rw)} {f(cy)} L {f(cx + rw + 40)} {f(cy - h * 0.2)}" stroke="#5A3A22" stroke-width="4"></path>')
    o.append(small_bird(cx - rw * 0.2, cy - 4, min(2.2, h / 160)))
    return "".join(o)

def s_snare(p, w, h, seed):
    """Our soul is escaped as a bird out of the snare of the fowlers: the snare broken, birds flying free into the morning."""
    o = [sky(w, h, *DAWN), sun(w * 0.8, h * 0.6, 22, color="#FFE680", op=0.5), hills(w, h, h * 0.7, seed, color="#4A4A5A", amp=10), ground(w, h, h * 0.8, "#6A6A4A", dy=0)]
    o.append(f'<path d="M{f(w * 0.2)} {f(h * 0.9)} L {f(w * 0.3)} {f(h * 0.82)} M{f(w * 0.36)} {f(h * 0.8)} L {f(w * 0.46)} {f(h * 0.9)}" stroke="#C8A06A" stroke-width="3"></path>')
    for i in range(5):
        o.append(small_bird(w * (0.38 + i * 0.1), h * (0.7 - i * 0.06), min(1.6, h / 220), color="#5A4A3A", fly=True))
    return "".join(o)

def s_fire(p, w, h, seed):
    """Fire and brimstone and burning wind: fire across the plain under smoke."""
    o = [sky(w, h, "#1A0A0A", "#5A1A0A")]
    for i in range(5):
        o.append(f'<ellipse cx="{f(w * (0.1 + i * 0.2))}" cy="{f(h * 0.3)}" rx="{f(w * 0.16)}" ry="{f(h * 0.1)}" fill="#2A1A1A" opacity="0.8"></ellipse>')
    o.append(ground(w, h, h * 0.84, "#2A0A0A", dy=0))
    o.append("".join(E.blaze(w * (0.08 + i * 0.21), h * 0.96, w * 0.2, h * 0.42, seed + i) for i in range(5)))
    return "".join(o)

def s_furnace(p, w, h, seed):
    """As silver tried in a furnace on the earth, purified seven times: the refiner's furnace and the melting-pot glowing."""
    cx, b = w * 0.5, h * 0.94
    o = [bgrect(w, h, "#1A0E0A"), glow(cx, h * 0.7, h * 0.5, "#FF8A3D", 0.2),
         f'<path d="M{f(cx - w * 0.18)} {f(b)} L {f(cx - w * 0.14)} {f(h * 0.56)} C {f(cx - w * 0.1)} {f(h * 0.46)} {f(cx + w * 0.1)} {f(h * 0.46)} {f(cx + w * 0.14)} {f(h * 0.56)} L {f(cx + w * 0.18)} {f(b)} Z" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="3"></path>',
         f'<path d="M{f(cx - w * 0.08)} {f(b)} L {f(cx - w * 0.08)} {f(h * 0.78)} C {f(cx - w * 0.04)} {f(h * 0.72)} {f(cx + w * 0.04)} {f(h * 0.72)} {f(cx + w * 0.08)} {f(h * 0.78)} L {f(cx + w * 0.08)} {f(b)} Z" fill="#FF6A2A" stroke="#0D0D0F" stroke-width="2"></path>',
         E.blaze(cx, b, w * 0.12, h * 0.16, seed),
         f'<path d="M{f(cx - w * 0.07)} {f(h * 0.5)} L {f(cx + w * 0.07)} {f(h * 0.5)} L {f(cx + w * 0.05)} {f(h * 0.58)} L {f(cx - w * 0.05)} {f(h * 0.58)} Z" fill="#8A8A9A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<ellipse cx="{f(cx)}" cy="{f(h * 0.5)}" rx="{f(w * 0.07)}" ry="{f(h * 0.015)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></ellipse>']
    return "".join(o)

def s_zion(p, w, h, seed):
    """Mount Zion, the city of the great King, the house of Jehovah on its height."""
    t, b = tod(seed, (DAY, GOLD, DAWN))
    o = [sky(w, h, t, b), sun(w * 0.15, h * 0.24, 18, color="#FFE680", op=0.35), hills(w, h, h * 0.72, seed, color="#8A9A6A", amp=10),
         zion_city(w * 0.55, h * 0.92, w * 0.84, h * 0.6, seed), ground(w, h, h * 0.92, "#B89A6A", dy=0)]
    return "".join(o)

def s_tent(p, w, h, seed):
    """Who shall sojourn in thy tabernacle? Who shall dwell in thy holy hill? The tent on the hill in its court of linen."""
    o = [sky(w, h, *tod(seed, (DAY, GOLD))), hills(w, h, h * 0.7, seed, color="#7A8A5A", amp=10),
         f'<path d="M{f(w * 0.1)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.62)} {f(w * 0.7)} {f(h * 0.62)} {f(w * 0.9)} {f(h + 10)} Z" fill="#9A8A5A" stroke="#0D0D0F" stroke-width="2"></path>',
         S1.shiloh(w * 0.5, h * 0.76, w * 0.5, h * 0.3)]
    return "".join(o)

def s_land(p, w, h, seed):
    """The lines are fallen unto me in pleasant places: fields marked out by boundary stones under a clear sky."""
    o = [sky(w, h, *DAY), hills(w, h, h * 0.5, seed, color="#7AA85A", amp=10)]
    cols = ("#9CCB5E", "#C8B86A", "#7AA85A", "#E8C88A", "#8AB85A")
    for i in range(5):
        y0 = h * (0.56 + i * 0.09); y1 = h * (0.65 + i * 0.09)
        o.append(f'<path d="M-10 {f(y0)} L {f(w + 10)} {f(y0 - 10)} L {f(w + 10)} {f(y1)} L -10 {f(y1 + 10)} Z" fill="{cols[i]}" stroke="#0D0D0F" stroke-width="1.6"></path>')
        for k in range(4):
            x = w * (0.15 + k * 0.24 + (i % 2) * 0.1)
            o.append(f'<path d="M{f(x)} {f(y0 + 2)} L {f(x - 8)} {f(y1)}" stroke="#5A3A22" stroke-width="1.4" stroke-dasharray="4 3"></path>')
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(h * 0.8)}" width="10" height="16" fill="#A89E92" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)

def s_wings(p, w, h, seed):
    """Hide me under the shadow of thy wings: an eagle spreading its wings over its young upon the crag."""
    o = [sky(w, h, *tod(seed, (DAY, DAWN, GOLD))), hills(w, h, h * 0.72, seed, color="#8A7A6A", amp=14),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.4)} {f(h * 0.7)} L {f(w * 0.62)} {f(h * 0.66)} L {f(w * 0.72)} {f(h + 10)} Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         nest(w * 0.5, h * 0.68, min(1.6, h / 220))]
    s = min(2.4, h / 160)
    o.append(f'<g transform="translate({f(w * 0.5)} {f(h * 0.58)}) scale({f(s)})"><path d="M0 0 C -30 -30 -80 -40 -120 -20 C -90 -14 -60 0 -40 12 Z M0 0 C 30 -30 80 -40 120 -20 C 90 -14 60 0 40 12 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M-14 6 C -14 -12 14 -12 14 6 C 10 18 -10 18 -14 6 Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></path><circle cx="0" cy="-14" r="8" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></circle>'
             f'<path d="M6 -14 l 8 3 l -8 3 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></path></g>')
    return "".join(o)

def s_war(p, w, h, seed):
    """Some trust in chariots, and some in horses: chariots and horsemen on the plain in a cloud of dust."""
    r = R(seed); b = h * 0.92
    o = [sky(w, h, "#C8A07A", "#F3D8A0"), clouds(w, h, seed, 5, "#D8C0A0", 0.7, 0.5, 0.8), ground(w, h, h * 0.7, "#B89A6A", dy=0)]
    s = min(1.0, h / 360)
    for i in range(3):
        o.append(E3.chariot(w * (0.18 + i * 0.3), b - i * 10, s * (0.9 - i * 0.1), color="#3A2214"))
    return "".join(o)

def s_broken(p, w, h, seed):
    """He breaketh the bow, and cutteth the spear in sunder; he burneth the chariots in the fire."""
    o = [sky(w, h, "#5A4A6A", "#FFC89A"), hills(w, h, h * 0.66, seed, color="#5A5A5A", amp=10), ground(w, h, h * 0.74, "#8A7A5A", dy=0),
         E.blaze(w * 0.7, h * 0.94, w * 0.24, h * 0.3, seed)]
    o.append(f'<path d="M{f(w * 0.12)} {f(h * 0.9)} C {f(w * 0.2)} {f(h * 0.8)} {f(w * 0.28)} {f(h * 0.8)} {f(w * 0.3)} {f(h * 0.84)}" stroke="#5A3A22" stroke-width="6" fill="none"></path>')
    o.append(f'<path d="M{f(w * 0.34)} {f(h * 0.86)} C {f(w * 0.36)} {f(h * 0.82)} {f(w * 0.42)} {f(h * 0.82)} {f(w * 0.46)} {f(h * 0.9)}" stroke="#5A3A22" stroke-width="6" fill="none"></path>')
    o.append(f'<path d="M{f(w * 0.1)} {f(h * 0.95)} L {f(w * 0.24)} {f(h * 0.93)} M{f(w * 0.28)} {f(h * 0.94)} L {f(w * 0.44)} {f(h * 0.96)}" stroke="#3A2A1E" stroke-width="4"></path>')
    return "".join(o)

def s_sun(p, w, h, seed):
    """In them hath he set a tabernacle for the sun, which is as a bridegroom coming out of his chamber: the sun rising in
    glory over the rim of the earth."""
    o = [sky(w, h, "#2A3A8A", "#FFC890"), V.rays(w * 0.5, h * 0.8, 40, 30, max(w, h) * 1.2, color="#FFF4C2", op=0.3),
         sun(w * 0.5, h * 0.8, min(60, h * 0.16), color="#FFD23F", op=0.5), clouds(w, h, seed, 5, "#FFB890", 0.7, 0.2, 0.5),
         hills(w, h, h * 0.86, seed, color="#3A2A4A", amp=6)]
    return "".join(o)

def s_honey(p, w, h, seed):
    """More to be desired than gold, sweeter than honey and the droppings of the honeycomb."""
    o = [bgrect(w, h, "#3A2A14"), glow(w * 0.5, h * 0.7, h * 0.5, "#FFC14D", 0.15)]
    cx, cy, s = w * 0.36, h * 0.74, min(1.6, h / 260)
    for i in range(-2, 3):
        for j in range(-1, 2):
            x = cx + (i * 26 + (j % 2) * 13) * s; y = cy + j * 22 * s
            pts = " ".join(f"{f(x + 14 * s * math.cos(a))} {f(y + 14 * s * math.sin(a))}" for a in [k * math.pi / 3 for k in range(6)])
            o.append(f'<polygon points="{pts}" fill="#E8A317" stroke="#0D0D0F" stroke-width="1.6"></polygon>')
    o.append(f'<path d="M{f(cx)} {f(cy + 34 * s)} q 4 20 0 30 q -4 -10 0 -30" fill="#FFC14D"></path>')
    gx = w * 0.72
    for i in range(5):
        o.append(f'<rect x="{f(gx - 50 * s + i * 8 * s)}" y="{f(cy + 30 * s - i * 14 * s)}" width="{f(80 * s)}" height="{f(12 * s)}" rx="3" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)

def s_scroll(p, w, h, seed):
    """The law of Jehovah is perfect: the book of the law open on its stand by lamplight."""
    from genesis.art4 import clay_lamp
    o = [bgrect(w, h, "#2A1A14"), glow(w * 0.5, h * 0.7, h * 0.5, "#FFC14D", 0.14)]
    cx, cy, s = w * 0.5, h * 0.8, min(1.6, h / 260)
    o.append(f'<path d="M{f(cx - 140 * s)} {f(cy)} L {f(cx + 140 * s)} {f(cy)} L {f(cx + 120 * s)} {f(cy - 60 * s)} L {f(cx - 120 * s)} {f(cy - 60 * s)} Z" fill="#F3E8C8" stroke="#0D0D0F" stroke-width="2"></path>')
    for k in (-1, 1):
        o.append(f'<rect x="{f(cx + k * 130 * s - 10 * s)}" y="{f(cy - 72 * s)}" width="{f(20 * s)}" height="{f(84 * s)}" rx="{f(8 * s)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>')
    for i in range(6):
        y = cy - 50 * s + i * 8 * s
        o.append(f'<path d="M{f(cx - 100 * s)} {f(y)} L {f(cx - 10 * s)} {f(y)} M{f(cx + 10 * s)} {f(y)} L {f(cx + 100 * s)} {f(y)}" stroke="#5A4A3A" stroke-width="1.6"></path>')
    o.append(f'<rect x="{f(cx - 100 * s)}" y="{f(cy)}" width="{f(200 * s)}" height="{f(h)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(clay_lamp(w * 0.86, h * 0.9, s * 0.8))
    return "".join(o)

def s_lamp(p, w, h, seed):
    return SA.lamp(w, h, seed)

def s_banners(p, w, h, seed):
    """In the name of our God we will set up our banners: the host with its standards raised and the trumpets sounding."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E0B0"), hills(w, h, h * 0.66, seed, color="#8A8A5A", amp=10), ground(w, h, h * 0.72, "#C8A06A", dy=0)]
    s = fit(b, h * 0.66)
    for i, c in enumerate(("#D7261E", "#1F5FAD", "#E8B830", "#2E6B3A")):
        x = w * (0.16 + i * 0.22)
        o.append(f'<path d="M{f(x)} {f(b)} L {f(x)} {f(h * 0.58)}" stroke="#3A2214" stroke-width="4"></path><path d="M{f(x)} {f(h * 0.58)} L {f(x + 60)} {f(h * 0.62)} L {f(x)} {f(h * 0.66)} Z" fill="{c}" stroke="#0D0D0F" stroke-width="2"></path>')
        o.append(walker(p, x + 22, b, s * (0.92 + 0.06 * (i % 2)), cloth=("#8A3A1E", "#5A5A2A", "#3A4A6A", "#6A2A1A")[i]))
    o.append(J.trumpeter(p, w * 0.06, b, s))
    return "".join(o)

def s_crown(p, w, h, seed):
    """Thou settest a crown of fine gold on his head: the crown in light upon its cushion."""
    o = [bgrect(w, h, "#2A0A2A"), V.rays(w * 0.5, h * 0.72, 30, 20, max(w, h), color="#FFE680", op=0.25), glow(w * 0.5, h * 0.72, h * 0.3, "#FFE680", 0.2),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.86)}" rx="{f(w * 0.16)}" ry="{f(h * 0.06)}" fill="#7A1A3A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>',
         S2.crown(w * 0.5, h * 0.8, min(3.0, h / 120))]
    return "".join(o)

def s_bulls(p, w, h, seed):
    """Many bulls have compassed me; strong bulls of Bashan have beset me round."""
    b = h * 0.94
    o = [sky(w, h, "#3A2A2A", "#A86A4A"), hills(w, h, h * 0.6, seed, color="#3A2A2A", amp=12), ground(w, h, h * 0.7, "#5A4A3A", dy=0)]
    s = min(1.4, h / 260)
    o.append(bull(w * 0.2, b, s) + bull(w * 0.8, b - 10, s * 0.9, flip=True) + bull(w * 0.5, b - h * 0.12, s * 0.6))
    return "".join(o)

def s_dogs(p, w, h, seed):
    """For dogs have compassed me; they return at evening, they howl like a dog, and go round about the city."""
    b = h * 0.92
    o = [sky(w, h, "#1A1A3A", "#8A4A5A"), moon(w * 0.8, h * 0.2, min(18, h * 0.05)), K1.city_dusk(p, w, h, seed)]
    s = min(1.6, h / 220)
    o.append(dog(w * 0.2, b, s) + dog(w * 0.42, b - 6, s * 0.9, flip=True) + dog(w * 0.7, b + 2, s))
    return "".join(o)

def s_lots(p, w, h, seed):
    """They part my garments among them, and upon my vesture do they cast lots: the garment on the ground and the lots cast."""
    o = [sky(w, h, "#3A2A3A", "#A86A4A"), ground(w, h, h * 0.6, "#6A5A4A", dy=0)]
    cx, cy, s = w * 0.42, h * 0.84, min(1.6, h / 260)
    pts = [(-110, -40), (-40, -44), (-30, -58), (30, -58), (40, -44), (110, -40), (110, -12), (50, -14), (62, 30), (-62, 30), (-50, -14), (-110, -12)]
    o.append('<path d="M' + " L ".join(f"{f(cx + a * s)} {f(cy + b * s)}" for a, b in pts) + ' Z" fill="#8A3A1E" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(f'<path d="M{f(cx - 16 * s)} {f(cy - 58 * s)} C {f(cx - 8 * s)} {f(cy - 46 * s)} {f(cx + 8 * s)} {f(cy - 46 * s)} {f(cx + 16 * s)} {f(cy - 58 * s)} M{f(cx)} {f(cy - 40 * s)} L {f(cx)} {f(cy + 26 * s)}" stroke="#5A2A10" stroke-width="2" fill="none"></path>')
    r = R(seed)
    for i in range(4):
        x = w * 0.72 + r.uniform(-50, 50) * s; y = cy + r.uniform(-10, 10) * s
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(14 * s)}" height="{f(14 * s)}" transform="rotate({r.randint(0, 60)} {f(x)} {f(y)})" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)

def s_nations(p, w, h, seed):
    """All the ends of the earth shall remember and turn unto Jehovah: the lands about the great sea as a technical map, every
    route leading to Zion."""
    o = [grid_bg(w, h)]
    pts = [("ZION", 0.5, 0.56), ("EGYPT", 0.2, 0.86), ("ETHIOPIA", 0.16, 0.98), ("TARSHISH", 0.05, 0.3), ("THE ISLES", 0.22, 0.2), ("SHEBA", 0.62, 0.95),
           ("ASSHUR", 0.84, 0.18), ("BABYLON", 0.92, 0.5), ("TYRE", 0.42, 0.34), ("SEIR", 0.58, 0.8), ("KEDAR", 0.82, 0.76)]
    o.append(f'<path d="M-10 {f(h * 0.1)} C {f(w * 0.2)} {f(h * 0.2)} {f(w * 0.36)} {f(h * 0.4)} {f(w * 0.38)} {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.76)} {f(w * 0.1)} {f(h * 0.7)} -10 {f(h * 0.72)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    for name, x, y in pts[1:]:
        o.append(route([(w * x, h * y), (w * 0.5, h * 0.56)], color="#8FD0E2"))
    for name, x, y in pts:
        o.append(node(w * x, h * y, name, color="#FFD23F" if name == "ZION" else "#8FD0E2", r=8 if name == "ZION" else 5))
    return "".join(o)

def s_pasture(p, w, h, seed):
    """He maketh me to lie down in green pastures; he leadeth me beside still waters: the shepherd, his flock and the pool."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, *tod(seed, (DAY, GOLD, DAWN))), hills(w, h, h * 0.56, seed, color="#6A9A4A", amp=10), ground(w, h, h * 0.62, "#9CCB5E", dy=0),
         f'<ellipse cx="{f(w * 0.66)}" cy="{f(h * 0.78)}" rx="{f(w * 0.22)}" ry="{f(h * 0.06)}" fill="#5AB8D0" stroke="#0D0D0F" stroke-width="2"></ellipse>',
         f'<path d="M{f(w * 0.5)} {f(h * 0.78)} l 40 0 M{f(w * 0.68)} {f(h * 0.8)} l 50 0" stroke="#E8F6FA" stroke-width="2" opacity="0.8"></path>']
    s = min(0.9, h / 420)
    r = R(seed)
    for i in range(6):
        o.append(E.sheep(w * (0.12 + i * 0.13) + r.uniform(-10, 10), b - (i % 3) * 10, s, flip=i % 2 == 1))
    o.append(shepherd(p, w * 0.22, b, fit(b, h * 0.5)))
    return "".join(o)

def s_valley(p, w, h, seed):
    """Though I walk through the valley of the shadow of death: a dark gorge, the shepherd with rod and staff leading the
    flock along the narrow way."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A4A", "#6A6A8A"),
         f'<path d="M-10 -10 L {f(w * 0.36)} -10 L {f(w * 0.4)} {f(h * 0.4)} L {f(w * 0.3)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1A1A2A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w + 10)} -10 L {f(w * 0.66)} -10 L {f(w * 0.6)} {f(h * 0.44)} L {f(w * 0.72)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} Z" fill="#14142A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.36)} {f(h + 10)} L {f(w * 0.48)} {f(h * 0.5)} L {f(w * 0.52)} {f(h * 0.5)} L {f(w * 0.66)} {f(h + 10)} Z" fill="#4A4A5A"></path>']
    s = min(0.7, h / 500)
    for i in range(3): o.append(E.sheep(w * (0.46 + i * 0.05), h * (0.7 + i * 0.07), s * (0.7 + i * 0.15)))
    o.append(shepherd(p, w * 0.5, b, fit(b, h * 0.56)))
    return "".join(o)

def s_table(p, w, h, seed):
    """Thou preparest a table before me in the presence of mine enemies: the table spread, the cup running over, the horn of oil."""
    b = h * 0.9
    o = [bgrect(w, h, "#3A2A1A"), glow(w * 0.5, h * 0.6, h * 0.5, "#FFC14D", 0.14)]
    o.insert(0, mk.defs(p, *ALL))
    for x in (0.08, 0.18, 0.82, 0.92):
        o.append(mk.person(p, round(w * x), round(h * 0.8), fit(h * 0.8, h * 0.42), body="#120C08", cloth="#1A120A", sw=2, flip=x > 0.5))
    o.append(S3.table(w * 0.5, b, w * 0.6, min(1.4, h / 300)))
    s = min(1.6, h / 260)
    cx, cy = w * 0.5, b - 70 * min(1.4, h / 300)
    o.append(f'<path d="M{f(cx - 16 * s)} {f(cy - 40 * s)} L {f(cx + 16 * s)} {f(cy - 40 * s)} L {f(cx + 8 * s)} {f(cy - 14 * s)} L {f(cx + 4 * s)} {f(cy)} L {f(cx - 4 * s)} {f(cy)} L {f(cx - 8 * s)} {f(cy - 14 * s)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(f'<path d="M{f(cx + 14 * s)} {f(cy - 40 * s)} q 6 10 4 34" stroke="#8A0E16" stroke-width="{f(3 * s)}" fill="none"></path>')
    o.append(S1.vial(w * 0.3, cy - 10 * s, s * 0.6) + f'<ellipse cx="{f(w * 0.68)}" cy="{f(cy - 6)}" rx="{f(30 * s)}" ry="{f(10 * s)}" fill="#D8A060" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    return "".join(o)

def s_earth(p, w, h, seed):
    """The earth is Jehovah's, and the fulness thereof; for he hath founded it upon the seas: the hills standing over the deep."""
    o = [sky(w, h, *DAY), clouds(w, h, seed, 4), mountain(w * 0.3, h * 0.72, w * 0.5, h * 0.32, color="#6A8A5A", lit="#9CCB5E"),
         mountain(w * 0.66, h * 0.72, w * 0.56, h * 0.42, color="#5A7A5A", lit="#8AB85A", snow=True),
         f'<rect x="-10" y="{f(h * 0.72)}" width="{f(w + 20)}" height="{f(h)}" fill="#0F4C68" stroke="#0D0D0F" stroke-width="2"></rect>',
         sea_band(w, h, h * 0.74, seed, color="#1F6F9A", deep="#0B2E4A")]
    return "".join(o)

def s_altar(p, w, h, seed):
    """I will wash my hands in innocency; so will I compass thine altar, O Jehovah: the laver and the altar with its fire."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5A4A6A", "#E8C890"), ground(w, h, h * 0.7, "#C8B88A", dy=0),
         K1.horned_altar(w * 0.62, b, min(1.4, h / 260), fire=True, seed=seed), E3.basin(w * 0.26, b, w * 0.16)]
    o.append(K1.priest(p, w * 0.4, b, fit(b, h * 0.5)))
    return "".join(o)

def s_rock(p, w, h, seed):
    """Lead me to the rock that is higher than I: a high rock in the sea, a man standing on it above the waves."""
    o = [mk.defs(p, *ALL), sky(w, h, *tod(seed, (DAWN, DAY, DUSK))), sea_band(w, h, h * 0.8, seed, color="#1F6F9A"),
         f'<path d="M{f(w * 0.36)} {f(h + 10)} L {f(w * 0.42)} {f(h * 0.72)} L {f(w * 0.5)} {f(h * 0.66)} L {f(w * 0.6)} {f(h * 0.7)} L {f(w * 0.66)} {f(h + 10)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    o.append(prayer(p, w * 0.52, h * 0.68, fit(h * 0.68, h * 0.42), cloth="#5A4A7A"))
    return "".join(o)

def s_cedars(p, w, h, seed):
    """The cedars of Lebanon on the mountainside."""
    o = [sky(w, h, *tod(seed, (DAY, DAWN, DUSK))), mountain(w * 0.3, h * 0.8, w * 0.7, h * 0.5, color="#5A6A7A", snow=True),
         mountain(w * 0.8, h * 0.8, w * 0.6, h * 0.42, color="#4A5A6A", snow=True), ground(w, h, h * 0.8, "#4A6A3A", dy=0)]
    k = min(1.0, h * 0.62 / 300)
    for i, x in enumerate((0.12, 0.34, 0.58, 0.84)):
        o.append(cedar(w * x, h * (0.94 + 0.02 * (i % 2)), k * (0.85 + 0.15 * (i % 2)), seed + i))
    return "".join(o)

def s_wilderness(p, w, h, seed):
    """The wilderness: the camp of Israel in the desert, the pillar of cloud over it by day (seed odd: fire by night)."""
    night = seed % 2 == 1
    o = [sky(w, h, *(NIGHT if night else ("#C8A07A", "#F3D8A0"))), ground(w, h, h * 0.7, "#B89A6A" if not night else "#3A2A2A", dy=0),
         (E3.pillar_fire(w * 0.7, h * 0.72, h * 0.06, w * 0.1, seed) if night else E3.pillar_cloud(w * 0.7, h * 0.72, h * 0.06, w * 0.12, seed)),
         __import__("numbers1").camp(14, w * 0.04, w * 0.96, h * 0.74, h * 0.94, seed)]
    return "".join(o)

def s_mountains(p, w, h, seed):
    """Thy righteousness is like the mountains of God: the ranges under a high clear sky."""
    o = [sky(w, h, *tod(seed, (DAY, DAWN, GOLD))), clouds(w, h, seed, 5), mountain(w * 0.2, h * 0.9, w * 0.6, h * 0.46, snow=True),
         mountain(w * 0.62, h * 0.9, w * 0.7, h * 0.6, color="#5A4A6A", snow=True), mountain(w * 0.96, h * 0.9, w * 0.5, h * 0.38, color="#7A6A8A"),
         ground(w, h, h * 0.9, "#6A7A5A", dy=0)]
    return "".join(o)

def s_dance(p, w, h, seed):
    """Thou hast turned for me my mourning into dancing: dancers with timbrels."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, *GOLD), hills(w, h, h * 0.62, seed, color="#C8A06A", amp=10), ground(w, h, h * 0.7, "#D8B87A", dy=0)]
    s = fit(b, h * 0.54)
    for i in range(5 if w > 500 else 3):
        o.append(S3.musician(p, w * (0.1 + i * 0.2), b, s, kind=("timbrel", "harp", "timbrel", "cymbals", "timbrel")[i], cloth=("#C2456A", "#F3EFE6", "#E8A317", "#F3EFE6", "#7A3BA8")[i], woman=i % 2 == 0, seed=seed + i))
    o.append(S3.notes(w * 0.5, h * 0.36, 8, seed))
    return "".join(o)

def s_sackcloth(p, w, h, seed):
    """I clothed myself with sackcloth; I humbled my soul with fasting: a mourner bowed in sackcloth and ashes."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#3A3A4A", "#8A8A9A"), ground(w, h, h * 0.74, "#6A6A5A", dy=0)]
    o.append(E.kneel(w * 0.4, b, min(1.6, h / 230), color="#5A5040"))
    return "".join(o)

def s_drought(p, w, h, seed):
    """My moisture was changed as with the drought of summer: a cracked field under a white sun."""
    return SA.famine(w, h, seed)

def s_horse(p, w, h, seed):
    """Be ye not as the horse, or as the mule, which have no understanding, whose trappings must be bit and bridle."""
    b = h * 0.92
    o = [sky(w, h, *DAY), hills(w, h, h * 0.66, seed, color="#8A9A6A", amp=10), ground(w, h, h * 0.74, "#B89A6A", dy=0)]
    s = min(1.3, h / 280)
    o.append(E3.horse(w * 0.36, b, s, color="#5A3A22") + __import__("numbers1").ass(w * 0.72, b, s * 0.9, flip=True))
    return "".join(o)

def s_sea(p, w, h, seed):
    """He gathereth the waters of the sea together as a heap: the open sea under the sky, the swell rolling in."""
    o = [sky(w, h, *tod(seed, (DAY, DUSK, DAWN))), sun(w * 0.75, h * 0.4, 20, color="#FFE680", op=0.4), sea_band(w, h, h * 0.56, seed, amp=14),
         E3.crash(w, h, seed) if seed % 3 == 2 else ""]
    return "".join(o)

def s_smoke(p, w, h, seed):
    """They shall consume; in smoke shall they consume away: smoke rising off the plain and blown away."""
    o = [sky(w, h, "#6A6A7A", "#C8B8A8"), hills(w, h, h * 0.72, seed, color="#5A5A5A", amp=10), ground(w, h, h * 0.8, "#7A6A5A", dy=0)]
    r = R(seed)
    for i in range(10):
        x = w * (0.2 + i * 0.07); y = h * (0.8 - i * 0.07)
        o.append(f'<ellipse cx="{f(x + r.uniform(-20, 20))}" cy="{f(y)}" rx="{f(w * 0.06 + i * 6)}" ry="{f(h * 0.04 + i * 2)}" fill="#3A3A3A" opacity="{f(0.6 - i * 0.05)}"></ellipse>')
    return "".join(o)

def s_grass(p, w, h, seed):
    """In the morning it flourisheth, and groweth up; in the evening it is cut down, and withereth: the grass and its flowers."""
    r = R(seed)
    o = [sky(w, h, *tod(seed, (DAY, DUSK))), sun(w * 0.8, h * 0.3, 18, color="#FFE680", op=0.4), ground(w, h, h * 0.66, "#8AB85A", dy=0)]
    for i in range(90):
        x = r.uniform(0, w); y = r.uniform(h * 0.7, h); k = r.uniform(0.6, 1.4)
        c = "#C8A86A" if x > w * 0.6 else "#5E8F26"
        o.append(f'<path d="M{f(x)} {f(y)} q {f(r.uniform(-6, 6))} {f(-20 * k)} {f(r.uniform(-8, 8))} {f(-34 * k)}" stroke="{c}" stroke-width="2.4" fill="none"></path>')
    for i in range(14):
        x = r.uniform(0, w * 0.6); y = r.uniform(h * 0.72, h * 0.95)
        o.append(f'<circle cx="{f(x)}" cy="{f(y - 30)}" r="5" fill="{r.choice(["#D7261E", "#E8B830", "#F3EFE6", "#C2456A"])}" stroke="#0D0D0F" stroke-width="1.2"></circle>')
    return "".join(o)

def s_mist(p, w, h, seed):
    """Surely every man walketh in a vain show: figures walking into the mist and fading."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8A8A9A", "#D8D8E0"), ground(w, h, h * 0.76, "#9A9A9A", dy=0)]
    for i in range(4):
        x = w * (0.2 + i * 0.2); s = fit(b - i * h * 0.04, h * (0.5 + i * 0.06))
        o.append(f'<g opacity="{f(0.9 - i * 0.2)}">' + walker(p, x, b - i * h * 0.04, s, cloth="#5A5A6A") + '</g>')
    o.append(clouds(w, h, seed, 8, "#E8E8F0", 0.6, 0.55, 0.85))
    return "".join(o)

def s_city(p, w, h, seed):
    return K1.city_dusk(p, w, h, seed)

def s_ruins(p, w, h, seed):
    return K2.burning_city(w, h, seed)

def s_sickbed(p, w, h, seed):
    """Jehovah will support him upon the couch of languishing: a man on his sickbed by lamplight."""
    from genesis.art4 import clay_lamp
    b = h * 0.9
    o = [bgrect(w, h, "#2A2034"), glow(w * 0.2, b, h * 0.4, "#FFC14D", 0.12), K1.bed(w, h, w * 0.3, w * 0.86, b, cover="#5A5A7A"), clay_lamp(w * 0.16, b, min(1.4, h / 280))]
    return "".join(o)

def s_brook(p, w, h, seed):
    """He will drink of the brook in the way: a brook running down among the rocks."""
    o = [sky(w, h, *tod(seed, (DAY, DAWN))), hills(w, h, h * 0.56, seed, color="#6A8A5A", amp=12), ground(w, h, h * 0.64, "#8AA85A", dy=0),
         S2.brook(-10, w + 10, h * 0.8, h * 0.08, seed)]
    for i in range(5):
        o.append(f'<ellipse cx="{f(w * (0.1 + i * 0.2))}" cy="{f(h * 0.94)}" rx="{f(w * 0.04)}" ry="{f(h * 0.03)}" fill="#8A8478" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    return "".join(o)

def s_hart(p, w, h, seed):
    """As the hart panteth after the water brooks: a hart by the stream in the forest."""
    o = [sky(w, h, *tod(seed, (DAY, DAWN, GOLD))), hills(w, h, h * 0.56, seed, color="#4A7A4A", amp=12), ground(w, h, h * 0.64, "#6A9A4A", dy=0)]
    for i in range(4):
        o.append(tree(w * (0.06 + i * 0.3), h * 0.66, min(0.5, h * 0.28 / 260), seed + i, fruit=False, leaf=("#2E6A32", "#1F4A34", "#3F8A44")))
    o.append(S2.brook(-10, w + 10, h * 0.86, h * 0.07, seed))
    o.append(hart(w * 0.48, h * 0.86, min(1.5, h / 220), drink=seed % 2 == 0))
    return "".join(o)

def s_nest(p, w, h, seed):
    """Yea, the sparrow hath found her a house, and the swallow a nest for herself, where she may lay her young, even thine
    altars: the swallows' nest under the eaves of the house, the altar's fire below."""
    o = [sky(w, h, "#FFB04A", "#FFF0C8"), ground(w, h, h * 0.8, "#C8B88A", dy=0)]
    o.append(f'<rect x="{f(w * 0.46)}" y="{f(h * 0.3)}" width="{f(w * 0.6)}" height="{f(h * 0.6)}" fill="#E8DCC0" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    o.append(f'<rect x="{f(w * 0.42)}" y="{f(h * 0.26)}" width="{f(w * 0.66)}" height="{f(h * 0.05)}" fill="#C8BC9C" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(nest(w * 0.6, h * 0.36, min(1.4, h / 260)))
    o.append(small_bird(w * 0.3, h * 0.46, min(2.0, h / 200), color="#3A3A5A") + small_bird(w * 0.82, h * 0.42, min(1.4, h / 260), color="#6A4A2A", flip=True))
    o.append(K1.horned_altar(w * 0.2, h * 0.94, min(1.0, h / 360), fire=True, seed=seed))
    return "".join(o)

def s_willows(p, w, h, seed):
    """By the rivers of Babylon, there we sat down, yea, we wept: the harps hung on the willows over the river."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#3A3A6A", "#C89A8A"), ground(w, h, h * 0.62, "#6A6A4A", dy=0), stream(w, h * 0.72, h * 0.84, seed, color="#3A7A9A")]
    for i, x in enumerate((0.16, 0.84)):
        X = w * x
        o.append(f'<path d="M{f(X - 10)} {f(h * 0.7)} C {f(X - 6)} {f(h * 0.4)} {f(X)} {f(h * 0.3)} {f(X + 4)} {f(h * 0.2)} L {f(X + 16)} {f(h * 0.2)} C {f(X + 10)} {f(h * 0.36)} {f(X + 10)} {f(h * 0.5)} {f(X + 12)} {f(h * 0.7)} Z" fill="#4A3A2A" stroke="#0D0D0F" stroke-width="2"></path>')
        for k in range(12):
            a = X + (k - 6) * 9
            o.append(f'<path d="M{f(X + 8)} {f(h * 0.22)} C {f(a)} {f(h * 0.28)} {f(a - 6)} {f(h * 0.44)} {f(a - 4)} {f(h * 0.6)}" stroke="#7A9A5A" stroke-width="3" fill="none"></path>')
        o.append(S2.harp(X + 20 * (1 if i == 0 else -1), h * 0.44, min(0.9, h / 400)))
    for i in range(3):
        o.append(E.kneel(w * (0.36 + i * 0.12), b, min(1.0, h / 360), color=("#4A4A5A", "#5A4A3A", "#3A4A5A")[i], flip=i == 2))
    return "".join(o)

def s_watch(p, w, h, seed):
    """My soul waiteth for the Lord more than watchmen wait for the morning: a watchman on the wall at night, dawn breaking."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#0B0B2A", "#5A4A7A"), mk.stars(60, w, h * 0.5, seed),
         f'<path d="M-10 {f(h * 0.64)} C {f(w * 0.3)} {f(h * 0.58)} {f(w * 0.7)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.56)} L {f(w + 10)} {f(h * 0.7)} L -10 {f(h * 0.7)} Z" fill="#FF9A5A" opacity="0.35"></path>',
         f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A3048" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    o.append("".join(f'<rect x="{f(i * w / 12)}" y="{f(h * 0.66)}" width="{f(w / 24)}" height="{f(h * 0.04)}" fill="#3A3048" stroke="#0D0D0F" stroke-width="2"></rect>' for i in range(13)))
    o.append(walker(p, w * 0.4, h * 0.7, fit(h * 0.7, h * 0.4), cloth="#3A4A6A"))
    o.append(f'<path d="M{f(w * 0.4 + 22)} {f(h * 0.7)} L {f(w * 0.4 + 22)} {f(h * 0.34)}" stroke="#3A2214" stroke-width="3"></path>')
    return "".join(o)

def s_rain(p, w, h, seed):
    """He will come down like rain upon the mown grass, as showers that water the earth."""
    o = [sky(w, h, "#5A6A8A", "#C8D8E0"), clouds(w, h, seed, 8, "#6A7A9A", 0.9, 0.02, 0.2), hills(w, h, h * 0.66, seed, color="#5E8F26", amp=10),
         ground(w, h, h * 0.74, "#7AB84A", dy=0), rain_lines(w, h, seed)]
    return "".join(o)

def s_ships(p, w, h, seed):
    """They that go down to the sea in ships, that do business in great waters: ships on the high sea."""
    return K1.navy(p, w, h, seed, port=False)

def s_dark(p, w, h, seed):
    """The darkness and the light are both alike to thee: the night sky with the first light rising at its edge."""
    o = [sky(w, h, "#05051A", "#1A1A4A"), mk.stars(140, w, h, seed),
         f'<rect x="-10" y="{f(h * 0.72)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#FFB070" opacity="0.25"></rect>',
         sea_band(w, h, h * 0.82, seed, color="#14143A", deep="#05051A", foam="#5A5A8A", amp=6)]
    return "".join(o)

def s_vine(p, w, h, seed):
    """Thou broughtest a vine out of Egypt: the vine filling the land, its boughs over the hills."""
    o = [sky(w, h, *DAY), hills(w, h, h * 0.56, seed, color="#7A9A5A", amp=12), ground(w, h, h * 0.64, "#9AB86A", dy=0)]
    r = R(seed)
    for i in range(5):
        y = h * (0.7 + i * 0.06)
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 20)} {f(w * 0.6)} {f(y + 20)} {f(w + 10)} {f(y - 10)}" stroke="#5A3A22" stroke-width="4" fill="none"></path>')
        for k in range(7):
            x = r.uniform(0, w)
            o.append(f'<circle cx="{f(x)}" cy="{f(y - 8)}" r="{f(r.uniform(10, 16))}" fill="{r.choice(["#3F8A44", "#5E8F26", "#2E6A32"])}" stroke="#0D0D0F" stroke-width="1.6"></circle>')
        o.append(__import__("numbers1").grapes(r.uniform(w * 0.1, w * 0.9), y, min(0.5, h / 800), seed + i))
    return "".join(o)

def s_olive(p, w, h, seed):
    """I am like a green olive-tree in the house of God."""
    o = [sky(w, h, *tod(seed, (DAY, GOLD))), hills(w, h, h * 0.66, seed, color="#8A9A6A", amp=10), ground(w, h, h * 0.74, "#B8A87A", dy=0),
         J2.olive(w * 0.4, h * 0.94, min(1.4, h / 260), seed=seed)]
    if w > 500: o.append(K1.temple_front(w * 0.8, h * 0.76, w * 0.22, seed))
    return "".join(o)

def s_dawn(p, w, h, seed):
    """In the morning will I order my prayer unto thee, and will keep watch: a man with hands lifted on a hill at sunrise."""
    b = h * 0.9
    o = [sky(w, h, *DAWN), sun(w * 0.7, h * 0.74, 30, color="#FFE680", op=0.5), hills(w, h, h * 0.74, seed, color="#4A3A5A", amp=10),
         f'<path d="M-10 {f(h + 10)} L -10 {f(b)} C {f(w * 0.2)} {f(b - h * 0.04)} {f(w * 0.4)} {f(b - h * 0.02)} {f(w * 0.55)} {f(b + h * 0.06)} L {f(w * 0.55)} {f(h + 10)} Z" fill="#3A2A3A" stroke="#0D0D0F" stroke-width="2"></path>']
    o.append(prayer(p, w * 0.24, b - h * 0.01, fit(b, h * 0.62), cloth="#5A4A7A"))
    return "".join(o)

def s_fortress(p, w, h, seed):
    """Jehovah is my rock, and my fortress: a stronghold on the crags, a high tower over the valley."""
    o = [sky(w, h, *tod(seed, (DAY, DUSK, DAWN))), clouds(w, h, seed, 4, y0=0.3, y1=0.5), hills(w, h, h * 0.84, seed, color="#6A7A5A", amp=8),
         f'<path d="M{f(w * 0.36)} {f(h + 10)} L {f(w * 0.44)} {f(h * 0.8)} L {f(w * 0.5)} {f(h * 0.74)} L {f(w * 0.62)} {f(h * 0.76)} L {f(w * 0.7)} {f(h * 0.84)} L {f(w * 0.8)} {f(h + 10)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    tx, tb = w * 0.55, h * 0.76
    tw, th = min(w * 0.1, h * 0.12), h * 0.2
    o.append(f'<rect x="{f(tx - tw / 2)}" y="{f(tb - th)}" width="{f(tw)}" height="{f(th)}" fill="#B59A7A" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    o.append("".join(f'<rect x="{f(tx - tw / 2 + i * tw / 5)}" y="{f(tb - th - 8)}" width="{f(tw / 10)}" height="8" fill="#B59A7A" stroke="#0D0D0F" stroke-width="1.6"></rect>' for i in range(5)))
    o.append(f'<rect x="{f(tx - tw * 0.1)}" y="{f(tb - th * 0.7)}" width="{f(tw * 0.2)}" height="{f(th * 0.14)}" fill="#12090A"></rect>')
    o.append(f'<rect x="{f(tx - tw * 1.4)}" y="{f(tb - th * 0.45)}" width="{f(tw * 0.9)}" height="{f(th * 0.45)}" fill="#A88A6A" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(tx + tw * 0.5)} {f(tb - th * 0.5)} L {f(tx + tw * 1.6)} {f(tb - th * 0.5)} L {f(tx + tw * 1.6)} {f(tb)} L {f(tx + tw * 0.5)} {f(tb)} Z" fill="#9A7E5E" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def s_storm(p, w, h, seed):
    """The earth shook and trembled; thick darkness and the clouds, hailstones and coals of fire, the lightnings manifold
    (God is never drawn: only the storm)."""
    r = R(seed); sea = seed % 2 == 1
    o = [sky(w, h, "#0B0B2A", "#3A2A5A")]
    for i in range(9):
        o.append(f'<ellipse cx="{f(r.uniform(0, w))}" cy="{f(h * r.uniform(0.3, 0.55))}" rx="{f(w * r.uniform(0.15, 0.3))}" ry="{f(h * 0.08)}" fill="{r.choice(["#1A1430", "#2A2440", "#14102A"])}" opacity="0.95"></ellipse>')
    if sea:
        o.append(sea_band(w, h, h * 0.8, seed, color="#0F3A5A", deep="#05101A", foam="#8FA8C8", amp=14))
    else:
        o.append(mountain(w * 0.3, h * 0.92, w * 0.6, h * 0.3, color="#2A1E2E", lit="#5A3A4A") + mountain(w * 0.76, h * 0.92, w * 0.6, h * 0.24, color="#241A2A", lit="#4A3A4A"))
        o.append(ground(w, h, h * 0.92, "#1A1420", dy=0))
    for i in range(3):
        x = w * (0.2 + i * 0.3) + r.uniform(-30, 30)
        o.append(lightning(x, h * 0.5, h * 0.4, sw=5) + lightning(x, h * 0.5, h * 0.4, sw=2, color="#FFFFFF"))
    for i in range(40):
        o.append(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.55, h * 0.95))}" r="{f(r.uniform(1.5, 3))}" fill="{r.choice(["#E8ECF8", "#FF8A3D"])}"></circle>')
    return "".join(o)

def s_large(p, w, h, seed):
    """He brought me forth also into a large place: a broad sunlit plain under an open sky, a man with his hands lifted."""
    b = h * 0.94
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.7, h * 0.62, 26, color="#FFE680", op=0.5),
         hills(w, h, h * 0.72, seed, color="#9CCB5E", amp=6), ground(w, h, h * 0.76, "#B8C86A", dy=0)]
    o.append(prayer(p, w * 0.3, b, fit(b, h * 0.62), cloth="#4A2A7A"))
    return "".join(o)

def s_hinds(p, w, h, seed):
    """He maketh my feet like hinds' feet, and setteth me upon my high places: a man on the crag above the valley, hinds
    leaping on the rocks beside him."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#E8F6FA"), hills(w, h, h * 0.86, seed, color="#8A9A7A", amp=8),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.42)} {f(h * 0.74)} L {f(w * 0.52)} {f(h * 0.7)} L {f(w * 0.6)} {f(h * 0.78)} L {f(w * 0.74)} {f(h + 10)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.6"></path>',
         f'<path d="M{f(w * 0.7)} {f(h + 10)} L {f(w * 0.8)} {f(h * 0.82)} L {f(w * 0.92)} {f(h * 0.84)} L {f(w + 10)} {f(h + 10)} Z" fill="#7A5A3A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    o.append(king_fig(p, w * 0.5, h * 0.71, fit(h * 0.71, h * 0.44), up=[(-22, -158), (-6, -196), (8, -228)]))
    o.append(hart(w * 0.84, h * 0.83, min(0.9, h / 360), color="#A8742E"))
    return "".join(o)


# ---- Book II ---------------------------------------------------------------------------------------------------------------
def s_flock(p, w, h, seed):
    """We are accounted as sheep for the slaughter; like sheep they are laid in Sheol: a flock crowded together at dusk,
    no shepherd with them."""
    r = R(seed); b = h * 0.94
    o = [sky(w, h, *tod(seed, (DUSK, ("#4A4A6A", "#B8A0A0")))), hills(w, h, h * 0.66, seed, color="#4A4A3A", amp=10), ground(w, h, h * 0.72, "#6A6A4A", dy=0)]
    k = min(0.9, h / 400)
    pts = sorted(((r.uniform(0.05, 0.95), r.uniform(0.76, 0.96)) for _ in range(14)), key=lambda t: t[1])
    for x, y in pts:
        o.append(E.sheep(w * x, h * y, k * (0.7 + (y - 0.76) * 2), flip=r.random() < 0.5, wool=r.choice(["#E8E2D6", "#D8D0C0", "#C8C0B0"])))
    return "".join(o)

def s_bride(p, w, h, seed):
    """The queen in gold of Ophir at thy right hand; the king's daughter brought in raiment of needlework, the virgins her
    companions after her: the hall of the palace of ivory."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bgrect(w, h, "#5A2A3A"), glow(w * 0.7, h * 0.6, h * 0.6, "#FFE680", 0.18)]
    for i in range(5):
        x = w * (0.08 + i * 0.22)
        o.append(f'<rect x="{f(x - 12)}" y="{f(h * 0.2)}" width="24" height="{f(h * 0.8)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(x - 18)}" y="{f(h * 0.2)}" width="36" height="10" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.86)}" width="{f(w + 20)}" height="{f(h)}" fill="#C8A86A" stroke="#0D0D0F" stroke-width="2"></rect>')
    s = fit(b, h * 0.52)
    o.append(S3.throne(w * 0.82, b, s * 0.9) + king_fig(p, w * 0.82, b - 50 * s, s * 0.8))
    o.append(woman(p, w * 0.66, b, s * 0.95, "#E8B830"))
    for i, c in enumerate(("#F3EFE6", "#C2456A", "#F3EFE6", "#7A3BA8")):
        o.append(woman(p, w * (0.14 + i * 0.1), b, s * (0.8 + 0.03 * i), c))
    return "".join(o)

def s_river(p, w, h, seed):
    """There is a river, the streams whereof make glad the city of God: the river running below the walled city on its
    hill, trees along its banks."""
    o = [sky(w, h, *tod(seed, (DAY, GOLD))), zion_city(w * 0.6, h * 0.76, w * 0.6, h * 0.42, seed), ground(w, h, h * 0.76, "#8AB85A", dy=0),
         stream(w, h * 0.82, h * 0.92, seed)]
    for i in range(3):
        o.append(tree(w * (0.08 + i * 0.12), h * 0.84, min(0.4, h * 0.2 / 260), seed + i, fruit=False))
    return "".join(o)

def s_trumpets(p, w, h, seed):
    """Clap your hands, all ye peoples; God is gone up with a shout, Jehovah with the sound of a trumpet: the people with
    their hands lifted and the trumpeters before Zion."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, *GOLD), V.rays(w * 0.7, h * 0.5, 30, 20, max(w, h), color="#FFF4C2", op=0.25),
         zion_city(w * 0.72, h * 0.74, w * 0.44, h * 0.34, seed), ground(w, h, h * 0.74, "#C8A06A", dy=0)]
    s = fit(b, h * 0.6)
    o.append(J.trumpeter(p, w * 0.08, b, s) + J.trumpeter(p, w * 0.2, b, s * 0.95))
    for i in range(5):
        o.append(prayer(p, w * (0.34 + i * 0.12), b - (i % 2) * 6, s * (0.8 + 0.04 * (i % 3)), cloth=("#5A6A8A", "#8A5A3A", "#3A6A5A", "#7A3A4A", "#6A5A2A")[i]))
    return "".join(o)

def s_tempest(p, w, h, seed):
    """With the east wind thou breakest the ships of Tarshish: ships tossed on the great waves under a black sky."""
    r = R(seed)
    o = [sky(w, h, "#1A1A3A", "#4A4A6A")]
    for i in range(7):
        o.append(f'<ellipse cx="{f(r.uniform(0, w))}" cy="{f(h * r.uniform(0.25, 0.45))}" rx="{f(w * 0.2)}" ry="{f(h * 0.07)}" fill="#14142A" opacity="0.9"></ellipse>')
    o.append(sea_band(w, h, h * 0.74, seed, color="#0F3A5A", deep="#05101A", foam="#CFEFFF", amp=22))
    o.append(f'<g transform="rotate(-14 {f(w * 0.32)} {f(h * 0.78)})">' + K1.ship(w * 0.32, h * 0.8, min(1.0, h / 330), sail="#B8B0A0") + '</g>')
    o.append(f'<g transform="rotate(18 {f(w * 0.72)} {f(h * 0.82)})">' + K1.ship(w * 0.72, h * 0.84, min(0.8, h / 400), sail="#8A8478", flip=True) + '</g>')
    o.append(lightning(w * 0.55, h * 0.4, h * 0.36, sw=4))
    for i in range(12):
        x = r.uniform(0, w)
        o.append(f'<path d="M{f(x)} {f(h * 0.5)} l -40 {f(h * 0.12)}" stroke="#CFEFFF" stroke-width="1.6" opacity="0.6"></path>')
    return "".join(o)

def s_riches(p, w, h, seed):
    """They that trust in their wealth, and boast themselves in the multitude of their riches: the gold and silver heaped
    in the dark treasure-house."""
    r = R(seed); b = h * 0.92
    o = [bgrect(w, h, "#1A140E"), glow(w * 0.5, b, h * 0.6, "#FFC14D", 0.14), f'<rect x="-10" y="{f(h * 0.84)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2018" stroke="#0D0D0F" stroke-width="2"></rect>']
    k = min(1.4, h / 260)
    for cx, wd in ((0.3, 0.22), (0.62, 0.16)):
        o.append(f'<path d="M{f(w * (cx - wd))} {f(b)} C {f(w * (cx - wd * 0.5))} {f(b - 70 * k)} {f(w * (cx + wd * 0.5))} {f(b - 70 * k)} {f(w * (cx + wd))} {f(b)} Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2"></path>')
        for _ in range(16):
            x = w * cx + r.uniform(-wd * 0.7, wd * 0.7) * w; y = b - r.uniform(4, 50) * k
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(7 * k)}" ry="{f(3 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></ellipse>')
    for i in range(4):
        o.append(f'<rect x="{f(w * 0.8 - 30 * k + i * 6)}" y="{f(b - 12 * k - i * 12 * k)}" width="{f(60 * k)}" height="{f(10 * k)}" fill="#C8C8D8" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)

def s_tomb(p, w, h, seed):
    """Their graves are their houses for ever: tombs hewn in the rock of the hillside, their doors sealed with stones."""
    o = [sky(w, h, *tod(seed, (DUSK, ("#6A6A7A", "#C8B8A8")))), f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.6)} C {f(w * 0.3)} {f(h * 0.5)} {f(w * 0.7)} {f(h * 0.54)} {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i, x in enumerate((0.2, 0.46, 0.72)):
        X, Y, rw = w * x, h * 0.84, min(w * 0.08, h * 0.12)
        o.append(f'<path d="M{f(X - rw)} {f(Y)} L {f(X - rw)} {f(Y - rw * 1.2)} C {f(X - rw)} {f(Y - rw * 2)} {f(X + rw)} {f(Y - rw * 2)} {f(X + rw)} {f(Y - rw * 1.2)} L {f(X + rw)} {f(Y)} Z" fill="#1A1410" stroke="#0D0D0F" stroke-width="2"></path>')
        o.append(f'<circle cx="{f(X + rw * 0.9)}" cy="{f(Y - rw * 0.9)}" r="{f(rw)}" fill="#A89E92" stroke="#0D0D0F" stroke-width="2.4"></circle>')
    o.append(f'<path d="M{f(w * 0.9)} {f(h * 0.9)} C {f(w * 0.88)} {f(h * 0.7)} {f(w * 0.9)} {f(h * 0.5)} {f(w * 0.9)} {f(h * 0.44)} C {f(w * 0.92)} {f(h * 0.5)} {f(w * 0.94)} {f(h * 0.7)} {f(w * 0.92)} {f(h * 0.9)} Z" fill="#1F3A2A" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

NOMIRROR = {"nations"}

SCENES = {
    "tree": ("#8FD0E2", s_tree), "chaff": ("#5A3A5A", s_chaff), "path": ("#5A5A8A", s_path), "kings": ("#3A0A1A", s_kings), "throne": ("#FFB04A", s_throne),
    "potsherd": ("#3A2A3A", s_potsherd), "camp": ("#0B0B2A", s_camp_round), "night": ("#1A1430", s_night), "dawn": ("#5A5A8A", s_dawn),
    "harvest": ("#FFB04A", s_harvest), "lions": ("#1A0A0A", s_lions), "bow": ("#0B0B2A", s_bow), "pit": ("#5A6A8A", s_pit), "heavens": ("#05051A", s_heavens),
    "creation": ("#8FD0E2", s_creation), "gates": ("#FFB04A", s_gates), "court": ("#E8E2D6", s_court), "music": ("#FFB04A", s_music), "glory": ("#2A2A6A", s_glory),
    "storm": ("#0B0B2A", s_storm), "waves": ("#0B1A2E", s_waves), "net": ("#3A2A5A", s_net), "snare": ("#5A5A8A", s_snare), "fire": ("#1A0A0A", s_fire),
    "furnace": ("#1A0E0A", s_furnace), "zion": ("#8FD0E2", s_zion), "tent": ("#8FD0E2", s_tent), "land": ("#8FD0E2", s_land), "wings": ("#8FD0E2", s_wings),
    "fortress": ("#8FD0E2", s_fortress), "war": ("#C8A07A", s_war), "broken": ("#5A4A6A", s_broken), "sun": ("#2A3A8A", s_sun), "honey": ("#3A2A14", s_honey),
    "scroll": ("#2A1A14", s_scroll), "lamp": ("#0B0B1A", s_lamp), "banners": ("#8FD0E2", s_banners), "crown": ("#2A0A2A", s_crown), "bulls": ("#3A2A2A", s_bulls),
    "dogs": ("#1A1A3A", s_dogs), "lots": ("#3A2A3A", s_lots), "nations": ("#0B1A2E", s_nations), "pasture": ("#8FD0E2", s_pasture), "valley": ("#2A2A4A", s_valley),
    "table": ("#3A2A1A", s_table), "earth": ("#8FD0E2", s_earth), "altar": ("#5A4A6A", s_altar), "rock": ("#5A5A8A", s_rock), "cedars": ("#8FD0E2", s_cedars),
    "wilderness": ("#C8A07A", s_wilderness), "mountains": ("#8FD0E2", s_mountains), "dance": ("#FFB04A", s_dance), "sackcloth": ("#3A3A4A", s_sackcloth),
    "drought": ("#F3E0B0", s_drought), "horse": ("#8FD0E2", s_horse), "sea": ("#8FD0E2", s_sea), "smoke": ("#6A6A7A", s_smoke), "grass": ("#8FD0E2", s_grass),
    "mist": ("#8A8A9A", s_mist), "city": ("#2A1A3A", s_city), "ruins": ("#2A0A0A", s_ruins), "sickbed": ("#2A2034", s_sickbed), "brook": ("#8FD0E2", s_brook),
    "hart": ("#8FD0E2", s_hart), "nest": ("#FFB04A", s_nest), "willows": ("#3A3A6A", s_willows), "watch": ("#0B0B2A", s_watch), "rain": ("#5A6A8A", s_rain),
    "ships": ("#8FD0E2", s_ships), "dark": ("#05051A", s_dark), "vine": ("#8FD0E2", s_vine), "olive": ("#8FD0E2", s_olive),
    "large": ("#8FD0E2", s_large), "hinds": ("#8FD0E2", s_hinds),
    "flock": ("#3A2A5A", s_flock), "bride": ("#5A2A3A", s_bride), "river": ("#8FD0E2", s_river), "trumpets": ("#FFB04A", s_trumpets),
    "tempest": ("#1A1A3A", s_tempest), "riches": ("#1A140E", s_riches), "tomb": ("#3A2A5A", s_tomb),
}
