"""Emblems for the sayings of Proverbs: small drawn pictures, one over each saying cell, in a 320 x 120 viewBox (ground at
y = 104). Each emblem paints its own background far past the box, so a cell of any shape shows it centred with no bare
edges. EMB[name](p) -> svg (p = a unique id prefix for gradients and figure defs).

The emblems follow the things the sayings name: a lamp lit or put out, a tree of life, a well, a crown, a balance, a
sluggard's field, a dog, a door on its hinges, the ant ... and for the sayings that name no thing, the antitheses of the
righteous and the wicked (a house standing and a house fallen, a path into the dawn and a path into the dark), faces for
the lips of the wise and the mouth of the fool, and rays of light for the ways of Jehovah (God is never drawn)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, faces
import exodus as E, exodus2 as E2, exodus3 as E3, numbers1 as N, judges1 as J1, judges2 as J2, samuel1 as S1, samuel2 as S2, ruth1 as R
from faces_ex import F
from genesis.art3 import man, woman, king
from genesis.art2 import bird, dove

INK = "#0D0D0F"
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
def f(v): return f"{v:.1f}"
EMB = {}
def emb(*names):
    def deco(fn):
        for n in names: EMB[n] = fn
        return fn
    return deco

# ---- backgrounds ------------------------------------------------------------------------------------------------------
def sky(p, top, bot, ground=None, gy=104, line=True):
    o = (f'<defs><linearGradient id="{p}sk" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="{gy}"><stop offset="0" stop-color="{top}"></stop>'
         f'<stop offset="1" stop-color="{bot}"></stop></linearGradient></defs><rect x="-500" y="-400" width="1320" height="920" fill="url(#{p}sk)"></rect>')
    if ground:
        o += f'<rect x="-500" y="{gy}" width="1320" height="420" fill="{ground}"></rect>'
        if line: o += f'<path d="M-500 {gy} L 820 {gy}" stroke="{INK}" stroke-width="2"></path>'
    return o

def glow(cx, cy, r, color="#FFE680", op=0.35):
    return (f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{color}" opacity="{op * 0.5}"></circle>'
            f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r * 0.66)}" fill="{color}" opacity="{op * 0.7}"></circle>')

def rays(cx, cy, n, r0, r1, color="#FFF4C2", op=0.5, w=8, a0=0, a1=360):
    o = []
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * (i + 0.5) / n); da = math.radians(w / 2) * 0.5
        o.append(f'<path d="M{f(cx + r0 * math.cos(a - da))} {f(cy + r0 * math.sin(a - da))} L {f(cx + r1 * math.cos(a - da * 3))} {f(cy + r1 * math.sin(a - da * 3))} '
                 f'L {f(cx + r1 * math.cos(a + da * 3))} {f(cy + r1 * math.sin(a + da * 3))} L {f(cx + r0 * math.cos(a + da))} {f(cy + r0 * math.sin(a + da))} Z"></path>')
    return f'<g fill="{color}" opacity="{op}">' + "".join(o) + "</g>"

def hills(gy, seed, color="#6A8A4A", amp=8, step=40):
    r = random.Random(seed)
    d = "M-500 " + f(gy) + " L " + " L ".join(f"{x} {f(gy - 10 - r.uniform(0, amp))}" for x in range(-500, 840, step)) + f" L 820 {f(gy)} Z"
    return f'<path d="{d}" fill="{color}" stroke="{INK}" stroke-width="1.6"></path>'

def flame(x, y, w, h, lean=3):
    return E.flame(x, y, w, h, lean)

def figdefs(p): return mk.defs(p, *ALL)

# ---- light and dark ---------------------------------------------------------------------------------------------------
def lamp_shape(x, y, s=1.0, lit=True):
    o = (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
         '<path d="M-44 0 L 44 0 L 38 8 L -38 8 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>'
         '<path d="M-40 -4 C -44 -22 -10 -30 16 -24 L 46 -28 C 54 -28 54 -18 46 -16 L 30 -12 C 24 -2 6 0 -10 0 C -26 0 -38 0 -40 -4 Z" fill="#C8682E" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>'
         '<path d="M-40 -10 C -54 -12 -56 -24 -44 -24" fill="none" stroke="#0D0D0F" stroke-width="5"></path><path d="M-40 -10 C -54 -12 -56 -24 -44 -24" fill="none" stroke="#C8682E" stroke-width="2.6"></path>'
         '<ellipse cx="-10" cy="-20" rx="9" ry="3.4" fill="#2A1408"></ellipse><path d="M-26 -12 C -14 -8 4 -8 18 -14" fill="none" stroke="#E8A06A" stroke-width="2"></path></g>')
    if lit:
        o += flame(x + 48 * s, y - 26 * s, 9 * s, 30 * s, 4)
    else:
        o += (f'<path d="M{f(x + 48 * s)} {f(y - 28 * s)} C {f(x + 40 * s)} {f(y - 44 * s)} {f(x + 58 * s)} {f(y - 54 * s)} {f(x + 48 * s)} {f(y - 70 * s)} '
              f'C {f(x + 40 * s)} {f(y - 82 * s)} {f(x + 54 * s)} {f(y - 92 * s)} {f(x + 50 * s)} {f(y - 104 * s)}" fill="none" stroke="#8A8478" stroke-width="{f(4 * s)}" stroke-linecap="round" opacity="0.8"></path>')
    return o

@emb("lamp")
def e_lamp(p):
    return sky(p, "#0B0B2A", "#2A1A4A", "#1A1010") + glow(170, 64, 70, "#FFC14D", 0.5) + lamp_shape(150, 100, 1.2)

@emb("lamp_out")
def e_lamp_out(p):
    return sky(p, "#05050A", "#1A1A2A", "#100C0C") + lamp_shape(150, 100, 1.2, lit=False)

@emb("lamps")
def e_lamps(p):
    return (sky(p, "#0B0B2A", "#2A1A4A", "#1A1010") + glow(110, 70, 56, "#FFC14D", 0.5) + lamp_shape(90, 100, 0.95)
            + '<path d="M160 20 L 160 104" stroke="#F3EFE6" stroke-width="1.4" stroke-dasharray="4 4" opacity="0.5"></path>' + lamp_shape(220, 100, 0.95, lit=False))

@emb("dawn")
def e_dawn(p):
    return (sky(p, "#2A1A5E", "#FFC14D") + rays(160, 104, 22, 20, 300, "#FFF4C2", 0.35, 6, 180, 360)
            + f'<circle cx="160" cy="104" r="26" fill="#FFE680" stroke="{INK}" stroke-width="2"></circle>' + hills(104, 3, "#5A3A4A", 6)
            + f'<rect x="-500" y="104" width="1320" height="420" fill="#3A2A3A"></rect>'
            + f'<path d="M110 160 L 150 104 L 170 104 L 210 160 Z" fill="#E8C88A" stroke="{INK}" stroke-width="2"></path>')

@emb("path_light")
def e_path_light(p):
    return (sky(p, "#8FD0E2", "#FFE3B8", "#9CCB5E", gy=80) + rays(160, 58, 20, 18, 260, "#FFF4C2", 0.45, 7, 180, 360)
            + f'<circle cx="160" cy="58" r="16" fill="#FFE680" stroke="{INK}" stroke-width="1.6"></circle>' + hills(80, 4, "#6A8A4A", 6)
            + f'<path d="M40 130 C 110 112 140 96 156 80 L 164 80 C 180 96 210 112 280 130 Z" fill="#E8C88A" stroke="{INK}" stroke-width="2"></path>')

@emb("path_dark")
def e_path_dark(p):
    st = "".join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r * 0.6}" fill="#3A3430" stroke="{INK}" stroke-width="1.4"></ellipse>' for x, y, r in ((120, 112, 8), (178, 98, 6), (150, 90, 5), (200, 116, 9)))
    return (sky(p, "#05050A", "#1E1E30", "#2A2420", gy=80) + hills(80, 5, "#14141E", 6)
            + f'<path d="M40 130 C 110 112 140 96 156 80 L 164 80 C 180 96 210 112 280 130 Z" fill="#4A4038" stroke="{INK}" stroke-width="2"></path>' + st)

@emb("fork")
def e_fork(p):
    return (f'<rect x="-500" y="-400" width="660" height="920" fill="#FFE3B8"></rect><rect x="160" y="-400" width="660" height="920" fill="#1A1A2A"></rect>'
            + rays(60, 30, 14, 20, 140, "#FFC14D", 0.4, 8) + f'<circle cx="60" cy="30" r="16" fill="#FFE680" stroke="{INK}" stroke-width="1.6"></circle>' + mk.stars(14, 160, 60, 3).replace('<g fill', '<g transform="translate(170 0)" fill')
            + f'<rect x="-500" y="70" width="660" height="460" fill="#9CCB5E"></rect><rect x="160" y="70" width="660" height="460" fill="#2A2420"></rect><path d="M-500 70 L 820 70" stroke="{INK}" stroke-width="2"></path>'
            + f'<path d="M136 130 L 150 100 L 70 70 L 90 70 L 160 94 L 230 70 L 250 70 L 170 100 L 184 130 Z" fill="#E8C88A" stroke="{INK}" stroke-width="2" stroke-linejoin="round"></path>'
            + f'<path d="M170 100 L 250 70 L 230 70 L 160 94 Z" fill="#4A4038"></path>')

@emb("night")
def e_night(p):
    return (sky(p, "#05050A", "#1E1650", "#14141E") + mk.stars(40, 320, 100, 7) + f'<circle cx="230" cy="36" r="16" fill="#F3EFE6"></circle><circle cx="238" cy="30" r="14" fill="#14123A"></circle>'
            + hills(104, 6, "#0D0D18", 8))

@emb("rays")
def e_rays(p):
    return (sky(p, "#1F4A8A", "#8FC0E0", "#6A8A4A", gy=96) + glow(160, -10, 70, "#FFF4C2", 0.7) + rays(160, -20, 11, 30, 260, "#FFE680", 0.5, 5, 25, 155)
            + hills(96, 8, "#4E7A3A", 8) + f'<rect x="-500" y="96" width="1320" height="420" fill="#5E8A3A"></rect>'
            + "".join(f'<path d="M{x} 96 L {x - 4} 112 L {x + 4} 112 Z" fill="#3A5A2A"></path>' for x in range(-40, 380, 30)))

@emb("sun")
def e_sun(p):
    return (sky(p, "#8FD0E2", "#FFF4C2", "#C8A06A") + rays(160, 50, 24, 26, 220, "#FFF4C2", 0.6, 6)
            + f'<circle cx="160" cy="50" r="22" fill="#FFD23F" stroke="{INK}" stroke-width="2"></circle>' + hills(104, 9, "#B89A6A", 6))

# ---- trees, plants, fields --------------------------------------------------------------------------------------------
def tree(x, y, s=1.0, fruit=True, color="#2E6B3A", hl="#4E8A4A"):
    blobs = [(-30, -70, 26), (0, -84, 30), (30, -70, 26), (-16, -56, 22), (18, -56, 22)]
    o = (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-8 0 C -6 -20 -6 -40 -10 -56 L 10 -56 C 6 -40 6 -20 8 0 Z" fill="#5A3A22" stroke="{INK}" stroke-width="2"></path>'
         + "".join(f'<circle cx="{a}" cy="{b}" r="{r}" fill="{color}" stroke="{INK}" stroke-width="2"></circle>' for a, b, r in blobs)
         + "".join(f'<circle cx="{a}" cy="{b - 6}" r="{r * 0.55}" fill="{hl}"></circle>' for a, b, r in blobs))
    if fruit:
        o += "".join(f'<circle cx="{a}" cy="{b}" r="4" fill="#D7261E" stroke="{INK}" stroke-width="1.2"></circle>' for a, b in ((-30, -64), (-6, -90), (20, -78), (34, -60), (6, -60), (-18, -50)))
    return o + "</g>"

def dead_tree(x, y, s=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})" fill="none" stroke-linecap="round">'
            f'<path d="M0 0 L 0 -50 M0 -40 L -22 -66 M-12 -54 L -16 -74 M0 -50 L 18 -76 M10 -62 L 30 -70 M0 -50 L 2 -84" stroke="{INK}" stroke-width="9"></path>'
            f'<path d="M0 0 L 0 -50 M0 -40 L -22 -66 M-12 -54 L -16 -74 M0 -50 L 18 -76 M10 -62 L 30 -70 M0 -50 L 2 -84" stroke="#6A5A4A" stroke-width="5.5"></path></g>')

@emb("tree")
def e_tree(p):
    return sky(p, "#8FD0E2", "#E8F6FA", "#9CCB5E") + hills(104, 11, "#6A9A4A", 6) + tree(160, 104, 1.05)

@emb("trees")
def e_trees(p):
    return (sky(p, "#8FD0E2", "#E8F6FA", "#9CCB5E") + f'<rect x="160" y="-400" width="660" height="504" fill="#C8B8A0"></rect><rect x="160" y="104" width="660" height="420" fill="#B89A6A"></rect>'
            + tree(90, 104, 0.95) + dead_tree(232, 104, 0.95) + '<path d="M160 0 L 160 104" stroke="#0D0D0F" stroke-width="1.4" stroke-dasharray="4 4" opacity="0.4"></path>')

@emb("dead_tree")
def e_dead_tree(p):
    return sky(p, "#C8B8A0", "#E8D8C0", "#B89A6A") + dead_tree(160, 104, 1.05) + J1.chaff(30, 40, 290, 30, 90, 3)

@emb("chaff")
def e_chaff(p):
    wind = "".join(f'<path d="M{x} {y} C {x + 30} {y - 8} {x + 60} {y + 6} {x + 100} {y - 4}" fill="none" stroke="#F3EFE6" stroke-width="2" opacity="0.7"></path>' for x, y in ((20, 30), (90, 54), (160, 22), (60, 80), (190, 70)))
    return sky(p, "#5E6E8A", "#A9B8C8", "#8A7A5A") + wind + J1.chaff(60, 20, 300, 20, 96, 4) + R.heap(80, 104, 70, 16, "#C8B070")

@emb("field")
def e_field(p):
    return (sky(p, "#8FD0E2", "#FFF4C2", "#C8A06A") + R.field(-40, 360, 104, 44, 5, rows=3)
            + R.sheaf(250, 104, 0.9) + R.sheaf(276, 104, 0.8))

@emb("reaper")
def e_reaper(p):
    return figdefs(p) + sky(p, "#8FD0E2", "#FFF4C2", "#C8A06A") + R.field(-40, 360, 104, 40, 6, rows=3) + R.reaper(p, 110, 108, 0.42) + R.sheaf(200, 104, 0.9) + R.sheaf(230, 104, 0.9)

@emb("thorns")
def e_thorns(p):
    r = random.Random(4); o = []
    for i in range(16):
        x = r.uniform(-20, 340); y = 104 + r.uniform(-2, 4); hh = r.uniform(20, 44)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x - 8)} {f(y - hh * 0.5)} {f(x + 10)} {f(y - hh * 0.7)} {f(x + 2)} {f(y - hh)} M{f(x)} {f(y - hh * 0.4)} L {f(x + 12)} {f(y - hh * 0.55)} M{f(x + 2)} {f(y - hh * 0.6)} L {f(x - 10)} {f(y - hh * 0.75)}" fill="none" stroke="#4A3A22" stroke-width="2.4"></path>')
    wall = "".join(f'<rect x="{x}" y="{y}" width="22" height="12" fill="#A89E92" stroke="{INK}" stroke-width="1.4"></rect>' for x, y in ((150, 92), (172, 92), (194, 92), (160, 80), (182, 80), (230, 96), (254, 98)))
    return sky(p, "#C8B8A0", "#E8D8C0", "#9A8A6A") + wall + "".join(o)

@emb("vineyard")
def e_vineyard(p):
    o = sky(p, "#8FD0E2", "#E8F6FA", "#8A6A4A")
    for x in (40, 110, 180, 250, 320):
        o += f'<path d="M{x} 104 L {x} 52 M{x - 30} 60 L {x + 30} 60" stroke="#5A3A22" stroke-width="4"></path><path d="M{x - 30} 60 C {x - 10} 50 {x + 10} 70 {x + 30} 60" fill="none" stroke="#2E6B3A" stroke-width="5"></path>'
        o += N.grapes(x - 12, 64, 0.24, x) + N.grapes(x + 14, 62, 0.22, x + 1)
    return o

@emb("fig")
def e_fig(p):
    leaves = "".join(f'<path d="M{a} {b} c -14 -6 -18 -20 -8 -26 c 2 -8 12 -10 16 -2 c 8 -6 18 2 12 12 c 6 8 -4 18 -20 16 Z" fill="#3F6A3A" stroke="{INK}" stroke-width="1.6"></path>' for a, b in ((130, 50), (160, 38), (190, 52), (146, 66), (178, 68), (116, 72), (204, 74)))
    figs = "".join(f'<ellipse cx="{a}" cy="{b}" rx="5" ry="6" fill="#6A2A5A" stroke="{INK}" stroke-width="1.2"></ellipse>' for a, b in ((140, 70), (170, 56), (196, 80), (126, 84), (160, 82)))
    return sky(p, "#8FD0E2", "#E8F6FA", "#C8A06A") + '<path d="M156 104 C 156 90 152 80 160 70 L 166 70 C 162 80 166 90 166 104 Z" fill="#7A6A5A" stroke="#0D0D0F" stroke-width="2"></path>' + leaves + figs

@emb("hedge")
def e_hedge(p):
    return e_thorns(p).replace("#9A8A6A", "#8A7A5A") + f'<path d="M100 130 C 130 116 150 106 156 96 L 166 96 C 172 106 190 116 220 130 Z" fill="#E8C88A" stroke="{INK}" stroke-width="2"></path>'

# ---- water ------------------------------------------------------------------------------------------------------------
def waves(y, color="#1F6F9A", foam="#E8F6FA", amp=5, step=40):
    d = f"M-500 {y} " + " ".join(f"Q {x + step / 2} {y - amp} {x + step} {y}" for x in range(-500, 820, step)) + " L 820 520 L -500 520 Z"
    return f'<path d="{d}" fill="{color}" stroke="{INK}" stroke-width="1.6"></path>' + "".join(f'<path d="M{x} {y + 12} q 10 -4 20 0" fill="none" stroke="{foam}" stroke-width="1.6"></path>' for x in range(-20, 340, 46))

@emb("well")
def e_well(p):
    stones = "".join(f'<path d="M{x} {y} L {x + 24} {y}" stroke="#6A6058" stroke-width="1.2"></path>' for y in (82, 92) for x in range(118, 200, 30))
    return (sky(p, "#8FD0E2", "#FFE3B8", "#C8A06A") + '<path d="M120 40 L 120 76 M200 40 L 200 76 M114 40 L 206 40" stroke="#5A3A22" stroke-width="5" fill="none"></path>'
            + '<path d="M160 40 L 160 58" stroke="#3A2214" stroke-width="1.6"></path><path d="M152 58 L 168 58 L 166 70 L 154 70 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></path>'
            + f'<path d="M112 74 L 112 102 C 130 108 190 108 208 102 L 208 74 Z" fill="#A89E92" stroke="{INK}" stroke-width="2"></path>' + stones
            + f'<ellipse cx="160" cy="74" rx="48" ry="8" fill="#1F6F9A" stroke="{INK}" stroke-width="2"></ellipse><ellipse cx="160" cy="74" rx="38" ry="5" fill="#2C9DB8"></ellipse>')

@emb("fountain")
def e_fountain(p):
    return (sky(p, "#8FD0E2", "#E8F6FA", "#9CCB5E") + E4rock(150, 104, 130, 64)
            + '<path d="M166 62 C 186 60 196 74 200 100" fill="none" stroke="#E8F6FA" stroke-width="9" stroke-linecap="round"></path><path d="M166 62 C 186 60 196 74 200 100" fill="none" stroke="#2C9DB8" stroke-width="4" stroke-linecap="round"></path>'
            + '<path d="M164 70 C 176 74 180 84 182 100" fill="none" stroke="#8FD0E2" stroke-width="3" stroke-linecap="round"></path>'
            + f'<ellipse cx="206" cy="106" rx="60" ry="9" fill="#2C9DB8" stroke="{INK}" stroke-width="2"></ellipse>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#E8F6FA"></circle>' for x, y in ((206, 94), (214, 90), (196, 92), (220, 98))))

def E4rock(x, y, w, h):
    return (f'<path d="M{f(x - w / 2)} {f(y)} L {f(x - w * 0.42)} {f(y - h * 0.6)} L {f(x - w * 0.2)} {f(y - h)} L {f(x + w * 0.16)} {f(y - h * 0.9)} L {f(x + w * 0.4)} {f(y - h * 0.5)} L {f(x + w * 0.46)} {f(y)} Z" '
            f'fill="#8A6A5A" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"></path><path d="M{f(x - w * 0.2)} {f(y - h)} L {f(x - w * 0.1)} {f(y - h * 0.5)} L {f(x - w * 0.3)} {f(y)}" fill="none" stroke="#4A3A3A" stroke-width="2"></path>')

@emb("waters")
def e_waters(p):
    return sky(p, "#0B2E4A", "#1F6F9A") + waves(40, "#1F6F9A", amp=6) + waves(66, "#155A80", amp=6) + waves(92, "#0F4C68", amp=6)

@emb("sea")
def e_sea(p):
    return sky(p, "#8FD0E2", "#E8F6FA") + waves(80, "#1F6F9A") + Kship(160, 86, 0.45)

def Kship(x, y, s):
    from kg1.art import ship
    return ship(x, y, s)

@emb("cistern")
def e_cistern(p):
    return (sky(p, "#C8A06A", "#E8C88A", "#C8A06A") + f'<ellipse cx="160" cy="80" rx="90" ry="20" fill="#6A5A4A" stroke="{INK}" stroke-width="2.4"></ellipse>'
            + f'<ellipse cx="160" cy="82" rx="74" ry="14" fill="#1F6F9A" stroke="{INK}" stroke-width="2"></ellipse><ellipse cx="150" cy="80" rx="40" ry="5" fill="#8FD0E2" opacity="0.6"></ellipse>'
            + f'<path d="M206 70 L 230 40 L 240 44 L 216 74 Z" fill="#B5652E" stroke="{INK}" stroke-width="1.6"></path>')

@emb("reflection")
def e_reflection(p):
    tok = F("adam", skin="#D9A27A", shadow="#7A4A3A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", light="#FFE680")
    return (sky(p, "#8FD0E2", "#E8F6FA") + f'<g>{mk.face(tok, 110, -10, 0.2)}</g>'
            + f'<rect x="-500" y="62" width="1320" height="420" fill="#2C7DA0"></rect><path d="M-500 62 L 820 62" stroke="{INK}" stroke-width="2"></path>'
            + f'<g opacity="0.5" transform="translate(0 124) scale(1 -1)">{mk.face(tok, 110, -10, 0.2)}</g>'
            + "".join(f'<path d="M{x} {y} l 24 0" stroke="#E8F6FA" stroke-width="1.6"></path>' for x, y in ((60, 84), (200, 92), (120, 104), (230, 80))))

@emb("cup")
def e_cup(p):
    drops = "".join(f'<path d="M{x} {y} c 3 5 3 8 0 9 c -3 -1 -3 -4 0 -9 Z" fill="#CFEFFF" stroke="#2C7DA0" stroke-width="1"></path>' for x, y in ((128, 60), (196, 50), (204, 74), (120, 84)))
    return (sky(p, "#8FD0E2", "#E8C88A", "#C8A06A") + f'<path d="M130 40 L 190 40 L 180 96 L 140 96 Z" fill="#B5652E" stroke="{INK}" stroke-width="2.4"></path>'
            + f'<ellipse cx="160" cy="40" rx="30" ry="6" fill="#2C9DB8" stroke="{INK}" stroke-width="2"></ellipse><path d="M140 96 L 180 96 L 186 104 L 134 104 Z" fill="#8A4A1E" stroke="{INK}" stroke-width="2"></path>' + drops)

@emb("rain")
def e_rain(p):
    clouds = "".join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#5E6E8A" stroke="{INK}" stroke-width="1.6"></ellipse>' for x, y, rx, ry in ((80, 22, 60, 18), (170, 16, 70, 20), (260, 24, 60, 18), (120, 30, 50, 14), (220, 32, 50, 14)))
    r = random.Random(5)
    drops = "".join(f'<path d="M{f(x)} {f(y)} l -4 12" stroke="#CFEFFF" stroke-width="1.6"></path>' for x, y in ((r.uniform(10, 320), r.uniform(44, 96)) for _ in range(46)))
    return sky(p, "#3A4A6A", "#8A9AB8", "#5E8A3A") + clouds + drops + "".join(f'<path d="M{x} 104 l -3 -12 M{x + 4} 104 l 3 -14" stroke="#2E6B3A" stroke-width="2"></path>' for x in range(0, 330, 18))

@emb("clouds_dry")
def e_clouds_dry(p):
    clouds = "".join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#C8C2D6" stroke="{INK}" stroke-width="1.6"></ellipse>' for x, y, rx, ry in ((80, 26, 54, 16), (190, 20, 64, 18), (130, 32, 44, 12)))
    wind = "".join(f'<path d="M{x} {y} C {x + 30} {y - 8} {x + 60} {y + 6} {x + 100} {y - 4}" fill="none" stroke="#F3EFE6" stroke-width="2"></path>' for x, y in ((20, 56), (120, 70), (200, 52)))
    cracks = "".join(f'<path d="M{x} 110 l 8 6 l -4 6" fill="none" stroke="#6A4A2A" stroke-width="1.4"></path>' for x in range(0, 330, 34))
    return sky(p, "#C8B8A0", "#F3E8C8", "#C8A06A") + clouds + wind + cracks

@emb("snow")
def e_snow(p):
    r = random.Random(6)
    flakes = "".join(f'<circle cx="{f(r.uniform(0, 320))}" cy="{f(r.uniform(0, 100))}" r="{f(r.uniform(1.4, 2.8))}" fill="#F3EFE6"></circle>' for _ in range(60))
    return sky(p, "#8A9AB8", "#C8D6E8", "#E8ECF8") + R.field(-40, 360, 104, 36, 7, rows=2) + flakes

@emb("wind")
def e_wind(p):
    return e_clouds_dry(p)

# ---- fire, smoke, metal -----------------------------------------------------------------------------------------------
@emb("fire")
def e_fire(p):
    logs = f'<path d="M110 102 L 210 88 M110 88 L 210 102" stroke="{INK}" stroke-width="11" stroke-linecap="round"></path><path d="M110 102 L 210 88 M110 88 L 210 102" stroke="#5A3A22" stroke-width="7" stroke-linecap="round"></path>'
    coals = "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="#FF6A2A" stroke="{INK}" stroke-width="1"></circle>' for x, y in ((130, 104), (150, 106), (172, 104), (192, 106), (160, 100)))
    return sky(p, "#1A0A0A", "#3A1A10", "#1A1010") + glow(160, 70, 80, "#FF8A3D", 0.5) + logs + coals + E.blaze(160, 96, 70, 76, 4)

@emb("coals")
def e_coals(p):
    coals = "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="5" fill="{c}" stroke="{INK}" stroke-width="1.2"></ellipse>' for x, y, c in
                    ((110, 104, "#FF6A2A"), (130, 100, "#D7261E"), (150, 104, "#FFC14D"), (170, 100, "#FF6A2A"), (190, 104, "#D7261E"), (210, 100, "#FF6A2A"), (140, 108, "#8A2A10"), (180, 108, "#8A2A10")))
    return sky(p, "#1A0A0A", "#3A1A10", "#1A1010") + glow(160, 96, 60, "#FF6A2A", 0.5) + coals + flame(140, 96, 6, 16, 2) + flame(184, 96, 6, 18, -2)

@emb("crucible")
def e_crucible(p):
    return (sky(p, "#1A0A0A", "#3A1A10", "#2A1A14") + f'<path d="M100 104 L 110 60 L 210 60 L 220 104 Z" fill="#6A4A3A" stroke="{INK}" stroke-width="2.4"></path>'
            + f'<path d="M140 104 C 140 92 180 92 180 104 Z" fill="#12090A"></path>' + flame(160, 102, 12, 16, 2)
            + f'<path d="M128 44 L 192 44 L 184 62 L 136 62 Z" fill="#8A8478" stroke="{INK}" stroke-width="2"></path><ellipse cx="160" cy="44" rx="32" ry="6" fill="#E8ECF8" stroke="{INK}" stroke-width="1.6"></ellipse>'
            + glow(160, 40, 40, "#FFF4C2", 0.4))

@emb("sword")
def e_sword(p):
    return (sky(p, "#2A1A3A", "#5A2A4A") + rays(160, 60, 16, 20, 200, "#D7261E", 0.25, 8)
            + f'<g transform="rotate(-24 160 60)"><path d="M60 60 L 230 54 L 252 60 L 230 66 Z" fill="#C8C8D0" stroke="{INK}" stroke-width="2"></path><path d="M70 60 L 236 60" stroke="#8A8A9A" stroke-width="1.4"></path>'
            + f'<rect x="44" y="44" width="10" height="32" fill="#E8B830" stroke="{INK}" stroke-width="1.6"></rect><rect x="16" y="56" width="30" height="8" fill="#5A3A22" stroke="{INK}" stroke-width="1.6"></rect></g>')

@emb("arrows")
def e_arrows(p):
    def arrow(x, y, rot):
        return (f'<g transform="translate({x} {y}) rotate({rot})"><path d="M-60 0 L 50 0" stroke="#5A3A22" stroke-width="3"></path><path d="M50 -6 L 66 0 L 50 6 Z" fill="#8A8A9A" stroke="{INK}" stroke-width="1.4"></path>'
                f'<path d="M-60 0 L -70 -7 M-60 0 L -70 7 M-52 0 L -62 -7 M-52 0 L -62 7" stroke="#D7261E" stroke-width="2"></path></g>')
    bow = f'<path d="M70 20 C 110 40 110 90 70 110" fill="none" stroke="{INK}" stroke-width="7"></path><path d="M70 20 C 110 40 110 90 70 110" fill="none" stroke="#8A5A30" stroke-width="4"></path><path d="M70 20 L 70 110" stroke="#F3EFE6" stroke-width="1.4"></path>'
    return sky(p, "#3A2A4A", "#8A4A5A") + bow + arrow(190, 40, -8) + arrow(200, 70, 4) + arrow(180, 96, 14)

@emb("iron")
def e_iron(p):
    sparks = "".join(f'<path d="M160 60 L {f(160 + 40 * math.cos(a))} {f(60 + 40 * math.sin(a))}" stroke="#FFC14D" stroke-width="2"></path>' for a in [i * 0.55 for i in range(12)])
    blade = lambda rot: (f'<g transform="rotate({rot} 160 60)"><path d="M40 60 L 196 56 L 214 60 L 196 64 Z" fill="#9AA2AE" stroke="{INK}" stroke-width="2"></path>'
                         f'<rect x="20" y="54" width="24" height="12" fill="#5A3A22" stroke="{INK}" stroke-width="1.6"></rect></g>')
    return sky(p, "#1A1A2A", "#3A3A4A") + glow(160, 60, 40, "#FFC14D", 0.5) + blade(-14) + blade(194) + sparks

# ---- treasure -----------------------------------------------------------------------------------------------------------
def coin_pile(x, y, n, color="#C8C8D0", seed=1):
    r = random.Random(seed); o = []
    for i in range(n):
        cx = x + r.uniform(-34, 34) * (1 - i / n); cy = y - i * 2.2
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="9" ry="3.6" fill="{color}" stroke="{INK}" stroke-width="1.1"></ellipse>')
    return "".join(o)

@emb("silver")
def e_silver(p):
    return sky(p, "#1A1430", "#3A2A5A", "#2A1A14") + glow(160, 80, 60, "#E8ECF8", 0.3) + coin_pile(130, 104, 18, "#C8C8D0", 2) + coin_pile(196, 104, 14, "#E8B830", 3)

@emb("gold")
def e_gold(p):
    return sky(p, "#3A2214", "#6A3A1A", "#2A1A14") + glow(160, 80, 60, "#FFD23F", 0.4) + coin_pile(160, 104, 26, "#E8B830", 4)

@emb("chest", "rubies", "treasure")
def e_chest(p):
    gems = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="{INK}" stroke-width="1.2"></circle>' for x, y, r, c in
                   ((140, 62, 6, "#B5121B"), (156, 58, 5, "#E8B830"), (170, 62, 7, "#B5121B"), (184, 58, 5, "#2C9DB8"), (150, 66, 5, "#E8B830"), (176, 66, 5, "#E8B830")))
    return (sky(p, "#1A1430", "#3A2A5A", "#2A1A14") + glow(160, 60, 70, "#FFD23F", 0.4)
            + f'<path d="M116 30 L 204 30 L 214 50 L 106 50 Z" fill="#8A4A1E" stroke="{INK}" stroke-width="2.2"></path>'
            + f'<rect x="110" y="64" width="100" height="40" fill="#8A4A1E" stroke="{INK}" stroke-width="2.4"></rect><rect x="110" y="74" width="100" height="6" fill="#E8B830" stroke="{INK}" stroke-width="1.4"></rect>'
            + f'<path d="M110 64 C 130 54 190 54 210 64 Z" fill="#E8B830" stroke="{INK}" stroke-width="1.6"></path>' + gems)

@emb("scales")
def e_scales(p):
    return sky(p, "#12113A", "#2A2458", "#1A1430") + glow(160, 40, 60, "#FFD23F", 0.25) + S4balance(160, 104, 0.62)

def S4balance(x, y, s, tilt=0):
    pan = lambda px, py: f'<path d="M{px - 40} {py} C {px - 30} {py + 18} {px + 30} {py + 18} {px + 40} {py} Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2"></path>'
    cords = lambda px, py, top: f'<path d="M{px} {top} L {px - 38} {py} M{px} {top} L {px + 38} {py}" stroke="#5A3A22" stroke-width="1.6"></path>'
    ly, ry = -66 + tilt, -66 - tilt
    weights = "".join(f'<rect x="{82 + i * 16}" y="{ry - 12 - (i % 2) * 4}" width="13" height="{10 + (i % 2) * 4}" fill="#8A8A9A" stroke="#0D0D0F" stroke-width="1.4"></rect>' for i in range(3))
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
            '<path d="M-40 0 L 40 0 L 10 -10 L 10 -150 L -10 -150 L -10 -10 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<g transform="rotate({tilt * 0.3} 0 -150)"><path d="M-108 -150 L 108 -150" stroke="#0D0D0F" stroke-width="8" stroke-linecap="round"></path><path d="M-108 -150 L 108 -150" stroke="#E8B830" stroke-width="4" stroke-linecap="round"></path></g>'
            + cords(-105, ly, -150 - tilt * 0.3 * 1.8) + cords(105, ry, -150 + tilt * 0.3 * 1.8) + pan(-105, ly)
            + f'<path d="M-130 {ly - 4} C -126 {ly - 22} -84 {ly - 22} -80 {ly - 4} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></path>' + weights + pan(105, ry) + '</g>')

@emb("weights")
def e_weights(p):
    stones = "".join(f'<path d="M{x - w} 104 L {x - w * 0.8} {104 - h} L {x + w * 0.8} {104 - h} L {x + w} 104 Z" fill="{c}" stroke="{INK}" stroke-width="2"></path>' for x, w, h, c in
                     ((96, 22, 34, "#8A8A9A"), (140, 16, 24, "#6A6A7A"), (196, 26, 40, "#8A8A9A"), (240, 12, 18, "#6A6A7A")))
    bag = f'<path d="M262 104 C 250 100 250 80 264 76 L 260 66 L 280 66 L 276 76 C 290 80 290 100 278 104 Z" fill="#8A6A3A" stroke="{INK}" stroke-width="2"></path>'
    from exo.art7 import ban
    return sky(p, "#12113A", "#2A2458", "#1A1430") + stones + bag + ban(168, 46, 22)

@emb("gift")
def e_gift(p):
    return (figdefs(p) + sky(p, "#3A2A2A", "#8A5A4A", "#4A3A30") + man(p, 100, 108, 0.46, "#5A3A6A", flip=True, up=[(-22, -158), (-50, -120), (-80, -112)])
            + man(p, 226, 108, 0.46, "#2A3A5A", flip=True)
            + f'<path d="M156 52 C 150 52 148 42 156 40 L 154 34 L 166 34 L 164 40 C 172 42 170 52 164 52 Z" fill="#E8B830" stroke="{INK}" stroke-width="1.6"></path>')

@emb("apples")
def e_apples(p):
    net = "".join(f'<path d="M{x} 66 L {x + 20} 100" stroke="#C8C8D0" stroke-width="2"></path><path d="M{x + 20} 66 L {x} 100" stroke="#C8C8D0" stroke-width="2"></path>' for x in range(110, 210, 20))
    apples = "".join(f'<circle cx="{x}" cy="{y}" r="13" fill="#E8B830" stroke="{INK}" stroke-width="1.8"></circle><path d="M{x} {y - 13} l 2 -6" stroke="#5A3A22" stroke-width="2"></path><circle cx="{x - 4}" cy="{y - 4}" r="4" fill="#FFF4C2"></circle>' for x, y in ((136, 58), (162, 52), (188, 58), (148, 44), (176, 42)))
    return (sky(p, "#2A1A3A", "#5A3A5A", "#2A1A2A") + glow(160, 60, 64, "#FFD23F", 0.35)
            + f'<path d="M104 64 L 216 64 L 204 104 L 116 104 Z" fill="#8A8A9A" stroke="{INK}" stroke-width="2.2"></path>' + net + apples)

@emb("jewel", "earring")
def e_jewel(p):
    return (sky(p, "#2A1A3A", "#5A3A5A", "#3A1A3A") + glow(160, 60, 60, "#FFD23F", 0.4)
            + f'<circle cx="140" cy="62" r="22" fill="none" stroke="{INK}" stroke-width="9"></circle><circle cx="140" cy="62" r="22" fill="none" stroke="#E8B830" stroke-width="5"></circle>'
            + f'<path d="M196 40 L 214 62 L 196 88 L 178 62 Z" fill="#2C9DB8" stroke="{INK}" stroke-width="2"></path><path d="M196 40 L 196 88 M178 62 L 214 62" stroke="#8FD0E2" stroke-width="1.2"></path>'
            + f'<circle cx="140" cy="86" r="5" fill="#B5121B" stroke="{INK}" stroke-width="1.2"></circle>')

@emb("chain", "chaplet")
def e_chain(p):
    links = "".join(f'<ellipse cx="{f(160 + 70 * math.cos(a))}" cy="{f(54 + 34 * math.sin(a))}" rx="7" ry="4.4" transform="rotate({f(math.degrees(a) + 90)} {f(160 + 70 * math.cos(a))} {f(54 + 34 * math.sin(a))})" fill="none" stroke="#E8B830" stroke-width="3"></ellipse>' for a in [i * 2 * math.pi / 22 for i in range(22)])
    leaves = "".join(f'<path d="M{f(160 + 40 * math.cos(a))} {f(54 + 22 * math.sin(a))} l 6 -8 l 6 8 z" fill="#4E8A4A" stroke="{INK}" stroke-width="1"></path>' for a in [i * 2 * math.pi / 12 for i in range(12)])
    return sky(p, "#2A1A3A", "#5A3A5A") + glow(160, 54, 60, "#FFD23F", 0.3) + links + leaves

# ---- royal ------------------------------------------------------------------------------------------------------------
@emb("crown")
def e_crown(p):
    return (sky(p, "#2A1A3A", "#5A2470", "#1A1028") + glow(160, 60, 70, "#FFD23F", 0.4)
            + f'<ellipse cx="160" cy="92" rx="60" ry="14" fill="#7A3BA8" stroke="{INK}" stroke-width="2"></ellipse><path d="M100 92 C 100 104 220 104 220 92" fill="#5A2470" stroke="{INK}" stroke-width="2"></path>'
            + S2.crown(160, 86, 1.6))

@emb("throne", "king")
def e_throne(p):
    return (figdefs(p) + sky(p, "#3A1A2A", "#7A3A3A", "#4A2A1A") + glow(160, 50, 70, "#FFD23F", 0.3)
            + f'<path d="M110 104 L 110 92 L 210 92 L 210 104 Z" fill="#C8962E" stroke="{INK}" stroke-width="2"></path>'
            + f'<path d="M130 92 L 130 22 C 130 12 190 12 190 22 L 190 92 Z" fill="#7A3BA8" stroke="{INK}" stroke-width="2.2"></path><path d="M124 92 L 124 60 L 196 60 L 196 92" fill="none" stroke="#E8B830" stroke-width="5"></path>'
            + king(p, 160, 98, 0.36, "#1F3A7A"))

@emb("king_people")
def e_king_people(p):
    o = figdefs(p) + sky(p, "#8FD0E2", "#FFE3B8", "#C8A06A") + king(p, 160, 104, 0.44, "#1F3A7A")
    for i, x in enumerate((60, 90, 230, 260, 290, 30)):
        o += man(p, x, 106, 0.3, ("#5A3A22", "#6A5A3A", "#3A4A3A", "#5A4A6A", "#7A5A3A", "#4A3A2A")[i], flip=x > 160)
    return o

@emb("army", "war")
def e_army(p):
    o = figdefs(p) + sky(p, "#C8B8A0", "#E8D8C0", "#B89A6A")
    for i in range(9):
        x = 20 + i * 34
        o += man(p, x, 106, 0.34, ("#8A3A1E", "#5A2A16", "#3A2214")[i % 3], up=[(-22, -158), (-24, -200), (-26, -236)])
        o += f'<path d="M{x - 9} {106 - 0.34 * 236 - 20} L {x - 9} {106 - 0.34 * 120}" stroke="#5A3A22" stroke-width="2"></path><path d="M{x - 12} {106 - 0.34 * 236 - 20} L {x - 9} {106 - 0.34 * 236 - 30} L {x - 6} {106 - 0.34 * 236 - 20} Z" fill="#C8C8D0"></path>'
    return o

@emb("tower")
def e_tower(p):
    return (figdefs(p) + sky(p, "#8FD0E2", "#E8F6FA", "#C8A06A") + f'<path d="M180 104 L 186 20 L 250 20 L 256 104 Z" fill="#B8A88A" stroke="{INK}" stroke-width="2.4"></path>'
            + "".join(f'<rect x="{x}" y="10" width="10" height="10" fill="#B8A88A" stroke="{INK}" stroke-width="1.6"></rect>' for x in (184, 200, 216, 232, 246))
            + f'<path d="M206 104 L 206 76 C 206 66 230 66 230 76 L 230 104 Z" fill="#2A1A10" stroke="{INK}" stroke-width="1.6"></path><rect x="212" y="40" width="12" height="16" fill="#12090A"></rect>'
            + man(p, 120, 106, 0.38, "#5A3A6A", flip=True, up=[(-22, -158), (-46, -150), (-70, -156)]))

@emb("gate", "judge")
def e_gate(p):
    o = figdefs(p) + sky(p, "#FFE3B8", "#E8C88A", "#C8A06A")
    o += f'<rect x="100" y="14" width="120" height="90" fill="#B8A88A" stroke="{INK}" stroke-width="2.4"></rect>' + "".join(f'<rect x="{x}" y="4" width="12" height="10" fill="#B8A88A" stroke="{INK}" stroke-width="1.6"></rect>' for x in (104, 128, 152, 176, 200))
    o += f'<path d="M136 104 L 136 60 C 136 44 184 44 184 60 L 184 104 Z" fill="#2A1A10" stroke="{INK}" stroke-width="2"></path>'
    for x, c in ((52, "#5A4A3A"), (76, "#4A3A6A"), (248, "#3A4A3A"), (272, "#6A4A3A")):
        o += E.kneel(x, 106, 0.3, color=c, flip=x > 160)
    return o

@emb("city")
def e_city(p):
    from genesis.art2 import city
    return sky(p, "#8FD0E2", "#FFE3B8", "#B89A6A") + hills(104, 12, "#A8986A", 4) + city(160, 104, 220, 70, 3, color="#C8B090", lit="#FFC14D", wall="#A89878")

@emb("city_broken", "broken_wall")
def e_city_broken(p):
    wall = f'<path d="M40 104 L 40 50 L 90 50 L 96 70 L 110 58 L 120 104 Z M170 104 L 176 64 L 190 76 L 200 52 L 280 52 L 280 104 Z" fill="#A89E92" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"></path>'
    rub = "".join(f'<rect x="{x}" y="{y}" width="14" height="9" transform="rotate({r} {x} {y})" fill="#8A8478" stroke="{INK}" stroke-width="1.4"></rect>' for x, y, r in ((124, 96, 10), (140, 98, -12), (156, 94, 20), (132, 88, 5), (150, 86, -20)))
    return sky(p, "#C8B8A0", "#E8D8C0", "#9A8A6A") + wall + rub

# ---- houses and doors -------------------------------------------------------------------------------------------------
def house(x, y, w=100, h=56, color="#D8C8A0", door=True, lit=False):
    o = (f'<rect x="{f(x - w / 2)}" y="{f(y - h)}" width="{f(w)}" height="{f(h)}" fill="{color}" stroke="{INK}" stroke-width="2.4"></rect>'
         f'<path d="M{f(x - w / 2 - 6)} {f(y - h)} L {f(x + w / 2 + 6)} {f(y - h)}" stroke="#5A4A3A" stroke-width="4"></path>')
    if door: o += f'<path d="M{f(x - 10)} {f(y)} L {f(x - 10)} {f(y - 26)} C {f(x - 10)} {f(y - 34)} {f(x + 10)} {f(y - 34)} {f(x + 10)} {f(y - 26)} L {f(x + 10)} {f(y)} Z" fill="{"#FFC14D" if lit else "#3A2214"}" stroke="{INK}" stroke-width="1.6"></path>'
    o += f'<rect x="{f(x + w * 0.22)}" y="{f(y - h * 0.7)}" width="12" height="12" fill="{"#FFC14D" if lit else "#2A1A10"}" stroke="{INK}" stroke-width="1.4"></rect>'
    return o

@emb("house")
def e_house(p):
    return sky(p, "#8FD0E2", "#FFE3B8", "#9CCB5E") + f'<path d="M80 104 L 96 86 L 230 86 L 244 104 Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></path>' + house(162, 88, 120, 60)

@emb("house_fallen", "ruin")
def e_house_fallen(p):
    return (sky(p, "#5E6E8A", "#A9B8C8", "#8A7A5A") + f'<path d="M100 104 L 100 64 L 130 74 L 150 58 L 160 104 Z M180 104 L 186 80 L 210 70 L 222 104 Z" fill="#B8A88A" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"></path>'
            + "".join(f'<rect x="{x}" y="{y}" width="16" height="9" transform="rotate({r} {x} {y})" fill="#A89878" stroke="{INK}" stroke-width="1.4"></rect>' for x, y, r in ((160, 96, 14), (172, 94, -10), (230, 98, 20), (90, 98, -16)))
            + f'<path d="M150 58 L 200 66" stroke="#5A3A22" stroke-width="5"></path>')

@emb("houses")
def e_houses(p):
    return (sky(p, "#8FD0E2", "#FFE3B8", "#9CCB5E") + f'<rect x="160" y="-400" width="660" height="504" fill="#7A8A9A"></rect><rect x="160" y="104" width="660" height="420" fill="#8A7A5A"></rect>'
            + house(86, 104, 90, 52) + f'<path d="M200 104 L 200 70 L 222 78 L 236 64 L 244 104 Z" fill="#B8A88A" stroke="{INK}" stroke-width="2"></path>'
            + "".join(f'<rect x="{x}" y="{y}" width="14" height="8" transform="rotate({r} {x} {y})" fill="#A89878" stroke="{INK}" stroke-width="1.2"></rect>' for x, y, r in ((250, 98, 14), (266, 96, -10), (186, 98, 20))))

@emb("door")
def e_door(p):
    return (sky(p, "#5A3A22", "#3A2214", "#2A1A10") + f'<rect x="110" y="8" width="100" height="96" fill="#12090A" stroke="{INK}" stroke-width="2.4"></rect>'
            + f'<path d="M116 12 L 176 20 L 176 100 L 116 104 Z" fill="#8A5A30" stroke="{INK}" stroke-width="2.4"></path>'
            + "".join(f'<path d="M{116} {y} L {176} {y + 4}" stroke="#5A3A22" stroke-width="1.6"></path>' for y in (34, 58, 82))
            + f'<rect x="108" y="24" width="18" height="7" fill="#3A3A3A" stroke="{INK}" stroke-width="1.2"></rect><rect x="108" y="84" width="18" height="7" fill="#3A3A3A" stroke="{INK}" stroke-width="1.2"></rect>'
            + f'<path d="M190 30 C 210 40 210 70 190 80" fill="none" stroke="#FFD23F" stroke-width="2" stroke-dasharray="4 4"></path><path d="M186 76 L 192 82 L 196 74" fill="none" stroke="#FFD23F" stroke-width="2"></path>')

@emb("housetop", "roof")
def e_housetop(p):
    return (figdefs(p) + sky(p, "#8FD0E2", "#E8F6FA") + f'<rect x="60" y="64" width="210" height="80" fill="#D8C8A0" stroke="{INK}" stroke-width="2.4"></rect>'
            + f'<path d="M54 64 L 276 64" stroke="#5A4A3A" stroke-width="5"></path>' + "".join(f'<path d="M{x} 64 L {x} 56" stroke="#5A4A3A" stroke-width="2"></path>' for x in range(60, 280, 12))
            + E.kneel(250, 60, 0.26, color="#4A3A6A", flip=True)
            + f'<rect x="96" y="84" width="14" height="14" fill="#2A1A10"></rect><rect x="150" y="84" width="14" height="14" fill="#2A1A10"></rect>')

@emb("dripping")
def e_dripping(p):
    drops = "".join(f'<path d="M{x} {y} c 3 5 3 8 0 9 c -3 -1 -3 -4 0 -9 Z" fill="#CFEFFF" stroke="#2C7DA0" stroke-width="1"></path>' for x, y in ((90, 50), (120, 66), (150, 54), (180, 74), (210, 58), (240, 70), (110, 90), (200, 92)))
    return (sky(p, "#3A4A6A", "#7A8AA8", "#4A4A5A") + f'<path d="M40 20 L 280 20 L 270 36 L 50 36 Z" fill="#8A6A4A" stroke="{INK}" stroke-width="2.2"></path>'
            + "".join(f'<path d="M{x} 36 l 0 6" stroke="#2C7DA0" stroke-width="2"></path>' for x in range(60, 280, 30)) + drops
            + "".join(f'<ellipse cx="{x}" cy="106" rx="10" ry="2.4" fill="none" stroke="#8FD0E2" stroke-width="1.2"></ellipse>' for x in (110, 200, 150)))

@emb("bed", "sleep")
def e_bed(p):
    return (sky(p, "#14123A", "#2A1A4A", "#1A1428") + f'<rect x="70" y="72" width="190" height="20" fill="#5A3A22" stroke="{INK}" stroke-width="2"></rect><rect x="70" y="92" width="10" height="14" fill="#3A2214"></rect><rect x="250" y="92" width="10" height="14" fill="#3A2214"></rect>'
            + f'<path d="M100 72 C 100 52 140 46 200 52 C 240 56 260 62 260 72 Z" fill="#4A2A7A" stroke="{INK}" stroke-width="2"></path>'
            + f'<circle cx="88" cy="60" r="12" fill="#C98E66" stroke="{INK}" stroke-width="1.8"></circle><path d="M78 56 C 80 46 96 44 100 54" fill="#2A1A10"></path>'
            + "".join(f'<text x="{x}" y="{y}" font-family="Anton, sans-serif" font-size="{s}" fill="#8FD0E2">z</text>' for x, y, s in ((104, 40, 12), (116, 28, 15), (130, 16, 18))))

# ---- people ------------------------------------------------------------------------------------------------------------
@emb("family", "father", "son")
def e_family(p):
    return (figdefs(p) + sky(p, "#FFE3B8", "#FFC890", "#C8A06A") + man(p, 116, 106, 0.46, "#1F3A7A")
            + woman(p, 158, 106, 0.42, "#7A3A6A") + man(p, 206, 106, 0.32, "#C8A06A", flip=True))

@emb("mother")
def e_mother(p):
    return figdefs(p) + sky(p, "#FFE3B8", "#FFC890", "#C8A06A") + woman(p, 140, 106, 0.44, "#7A3A6A") + man(p, 186, 106, 0.28, "#C8A06A", flip=True)

@emb("child", "rod")
def e_rod(p):
    return (figdefs(p) + sky(p, "#FFE3B8", "#E8C88A", "#C8A06A") + man(p, 120, 106, 0.46, "#1F3A7A", up=[(-22, -158), (-40, -176), (-56, -196)])
            + f'<path d="M96 30 L 104 104" stroke="#5A3A22" stroke-width="4" stroke-linecap="round"></path>' + man(p, 196, 106, 0.3, "#C8A06A", flip=True))

@emb("old", "grey")
def e_old(p):
    beard = '<path d="M-14 -176 C -14 -150 0 -140 14 -150 L 14 -176 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2"></path><circle cx="0" cy="-186" r="13" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2"></circle>'
    return (figdefs(p) + sky(p, "#FFE3B8", "#FFC890", "#C8A06A") + glow(150, 30, 40, "#FFE680", 0.5)
            + man(p, 150, 106, 0.46, "#5A4A3A", extra=beard, kind="Robe") + man(p, 210, 106, 0.32, "#3A5A7A", flip=True) + man(p, 236, 106, 0.24, "#C8A06A", flip=True))

@emb("friends", "neighbor", "brother")
def e_friends(p):
    return (figdefs(p) + sky(p, "#8FD0E2", "#FFE3B8", "#C8A06A") + man(p, 136, 106, 0.46, "#3A5A7A", up=[(-22, -158), (0, -150), (24, -150)])
            + man(p, 184, 106, 0.46, "#7A5A3A", flip=True))

@emb("strife", "anger")
def e_strife(p):
    return (figdefs(p) + sky(p, "#3A0A0A", "#8A1A16", "#3A1A14") + rays(160, 60, 18, 10, 200, "#FF6A2A", 0.3, 8)
            + man(p, 122, 108, 0.4, "#5A2A16", flip=True, up=[(-22, -158), (-50, -170), (-74, -186)]) + man(p, 198, 108, 0.4, "#3A2A4A", up=[(-22, -158), (-50, -170), (-74, -186)]))

@emb("poor")
def e_poor(p):
    return (sky(p, "#5E6E8A", "#A9B8C8", "#8A7A6A") + E.kneel(150, 106, 0.42, color="#6A6058")
            + f'<path d="M176 92 C 176 102 196 102 196 92 Z" fill="#8A6A4A" stroke="{INK}" stroke-width="1.6"></path>')

@emb("rich")
def e_rich(p):
    return (figdefs(p) + sky(p, "#3A2214", "#8A5A2A", "#3A2A1A") + glow(200, 80, 50, "#FFD23F", 0.3) + man(p, 120, 106, 0.48, "#7A2A4A", kind="Robe")
            + coin_pile(200, 104, 20, "#E8B830", 7))

@emb("poor_rich")
def e_poor_rich(p):
    return (figdefs(p) + sky(p, "#5E6E8A", "#A9B8C8", "#8A7A6A") + f'<rect x="160" y="-400" width="660" height="504" fill="#8A5A2A"></rect><rect x="160" y="104" width="660" height="420" fill="#4A3A2A"></rect>'
            + E.kneel(96, 106, 0.38, color="#6A6058") + man(p, 210, 106, 0.44, "#7A2A4A", kind="Robe") + coin_pile(260, 104, 14, "#E8B830", 8))

@emb("witness")
def e_witness(p):
    return (figdefs(p) + sky(p, "#FFE3B8", "#E8C88A", "#C8A06A") + f'<rect x="200" y="20" width="120" height="84" fill="#B8A88A" stroke="{INK}" stroke-width="2"></rect>'
            + f'<path d="M232 104 L 232 64 C 232 50 270 50 270 64 L 270 104 Z" fill="#2A1A10" stroke="{INK}" stroke-width="1.6"></path>'
            + man(p, 130, 106, 0.3, "#5A3A6A", up=[(-22, -158), (-30, -186), (-32, -212)]) + E.kneel(70, 106, 0.3, color="#5A4A3A") + E.kneel(190, 106, 0.3, color="#3A4A3A", flip=True))

@emb("messenger", "runner")
def e_runner(p):
    legs = '<path d="M-6 -90 L -30 -40 L -50 -6 M6 -90 L 20 -46 L 46 -30" fill="none" stroke="#3A1E14" stroke-width="11" stroke-linecap="round"></path>'
    fig = (f'<g transform="translate(160 104) scale(0.5)">{legs}<path d="M-24 -170 C -30 -140 -28 -110 -20 -86 L 24 -86 C 30 -110 26 -140 20 -170 C 10 -176 -14 -176 -24 -170 Z" fill="#F3EFE6" stroke="{INK}" stroke-width="3"></path>'
           f'<path d="M-20 -160 L -50 -130 L -70 -140 M20 -160 L 50 -136 L 70 -150" fill="none" stroke="#3A1E14" stroke-width="10" stroke-linecap="round"></path><circle cx="2" cy="-190" r="16" fill="#3A1E14" stroke="{INK}" stroke-width="2"></circle></g>')
    return sky(p, "#8FD0E2", "#FFE3B8", "#C8A06A") + hills(104, 14, "#A8986A", 6) + fig + "".join(f'<path d="M{x} {y} l -34 0" stroke="#0D0D0F" stroke-width="2"></path>' for x, y in ((128, 46), (120, 60), (130, 74)))

@emb("woman", "wife")
def e_woman(p):
    return figdefs(p) + sky(p, "#FFE3B8", "#FFC890", "#C8A06A") + house(220, 104, 100, 56, lit=True) + woman(p, 120, 106, 0.46, "#2C6A7A")

@emb("lot")
def e_lot(p):
    stones = "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="6" fill="{c}" stroke="{INK}" stroke-width="1.6"></ellipse>' for x, y, c in ((136, 84, "#F3EFE6"), (160, 90, "#2A2420"), (182, 82, "#F3EFE6"), (150, 74, "#2A2420"), (172, 72, "#F3EFE6")))
    return (sky(p, "#12113A", "#2A2458", "#3A2A5A") + glow(160, 80, 70, "#FFE680", 0.3)
            + f'<path d="M80 104 C 90 70 230 70 240 104 Z" fill="#B5402A" stroke="{INK}" stroke-width="2.2"></path><path d="M96 98 C 110 80 210 80 224 98" fill="none" stroke="#E8B830" stroke-width="2"></path>' + stones)

@emb("altar", "sacrifice")
def e_altar(p):
    from kg1.art import horned_altar
    return sky(p, "#3A2A2A", "#8A5A4A", "#4A3A30") + horned_altar(160, 104, 0.7, fire=True, seed=3)

@emb("feast", "table")
def e_feast(p):
    import samuel3 as S3
    return (sky(p, "#3A2214", "#6A3A1A", "#2A1A10") + glow(160, 70, 70, "#FFC14D", 0.3) + S3.table(160, 104, 200, 0.8)
            + "".join(f'<ellipse cx="{x}" cy="78" rx="14" ry="5" fill="#E8D8B0" stroke="{INK}" stroke-width="1.4"></ellipse>' for x in (110, 160, 210))
            + f'<path d="M150 64 C 150 50 170 50 170 64 Z" fill="#8A5A30" stroke="{INK}" stroke-width="1.6"></path>')

@emb("bread")
def e_bread(p):
    return (sky(p, "#3A2214", "#8A5A2A", "#4A2A14") + glow(160, 80, 60, "#FFC14D", 0.3)
            + "".join(f'<ellipse cx="{x}" cy="{y}" rx="26" ry="13" fill="#C8862E" stroke="{INK}" stroke-width="2"></ellipse><path d="M{x - 14} {y - 4} l 8 -4 M{x - 2} {y - 6} l 8 -4 M{x + 10} {y - 4} l 8 -4" stroke="#8A4A1E" stroke-width="2"></path>' for x, y in ((126, 96), (180, 96), (152, 80)))
            + f'<path d="M216 90 C 216 106 256 106 256 90 Z" fill="#8A5A30" stroke="{INK}" stroke-width="1.8"></path>')

@emb("morsel")
def e_morsel(p):
    return (sky(p, "#5E6E8A", "#A9B8C8", "#6A5A4A") + f'<path d="M126 96 C 120 84 150 76 170 82 C 190 88 194 98 180 102 C 160 106 132 104 126 96 Z" fill="#B88A4E" stroke="{INK}" stroke-width="2"></path>'
            + f'<path d="M140 90 l 10 -2 M160 92 l 8 -1" stroke="#7A5A30" stroke-width="2"></path>')

@emb("wine", "drink")
def e_wine(p):
    return (sky(p, "#2A0A1A", "#5A1A3A", "#2A1018") + glow(160, 60, 60, "#B5121B", 0.35)
            + f'<path d="M190 104 C 172 98 168 66 186 52 L 186 38 L 218 38 L 218 52 C 236 66 232 98 214 104 Z" fill="#8A3A2A" stroke="{INK}" stroke-width="2.2"></path>'
            + f'<path d="M110 50 L 160 50 C 158 72 146 78 135 78 C 124 78 112 72 110 50 Z" fill="#C8C8D0" stroke="{INK}" stroke-width="2"></path><ellipse cx="135" cy="51" rx="24" ry="4" fill="#8A0E16"></ellipse>'
            + f'<path d="M135 78 L 135 96 M120 100 L 150 100" stroke="#C8C8D0" stroke-width="4"></path><path d="M135 78 L 135 96 M120 100 L 150 100" stroke="{INK}" stroke-width="1" opacity="0.4"></path>')

@emb("honey")
def e_honey(p):
    hexes = []
    for row in range(3):
        for col in range(6):
            cx = 108 + col * 20 + (10 if row % 2 else 0); cy = 46 + row * 17
            pts = " ".join(f"{f(cx + 11 * math.cos(math.radians(60 * k + 30)))},{f(cy + 11 * math.sin(math.radians(60 * k + 30)))}" for k in range(6))
            hexes.append(f'<polygon points="{pts}" fill="#E8A317" stroke="#8A5A10" stroke-width="1.6"></polygon>')
    drips = "".join(f'<path d="M{x} 82 C {x} 92 {x - 4} 96 {x} 100 C {x + 4} 96 {x} 92 {x} 82" fill="#E8A317" stroke="#8A5A10" stroke-width="1.2"></path>' for x in (124, 158, 196))
    return sky(p, "#3A2214", "#8A5A2A", "#4A2A14") + glow(160, 60, 70, "#FFD23F", 0.35) + "".join(hexes) + drips

@emb("scroll", "instruction", "law")
def e_scroll(p):
    lines = "".join(f'<path d="M126 {y} L {194 - (y % 3) * 6} {y}" stroke="#5A4A3A" stroke-width="2"></path>' for y in range(34, 92, 8))
    return (sky(p, "#12113A", "#2A2458", "#1A1430") + glow(160, 60, 70, "#FFE680", 0.3)
            + f'<rect x="118" y="24" width="84" height="76" fill="#F3E8C8" stroke="{INK}" stroke-width="2"></rect>' + lines
            + f'<rect x="104" y="18" width="16" height="88" rx="6" fill="#8A5A30" stroke="{INK}" stroke-width="2"></rect><rect x="200" y="18" width="16" height="88" rx="6" fill="#8A5A30" stroke="{INK}" stroke-width="2"></rect>')

@emb("landmark")
def e_landmark(p):
    return (sky(p, "#8FD0E2", "#FFE3B8", "#9CCB5E") + R.field(-40, 150, 104, 26, 9, rows=2)
            + f'<path d="M146 104 L 150 50 L 170 50 L 174 104 Z" fill="#A89E92" stroke="{INK}" stroke-width="2.2"></path><path d="M146 104 L 174 104" stroke="{INK}" stroke-width="2"></path>'
            + '<path d="M-20 100 L 340 100" stroke="#FFD23F" stroke-width="1.6" stroke-dasharray="5 4"></path>' + N.grapes(240, 80, 0.24, 3) + N.grapes(280, 78, 0.24, 4))

@emb("mortar")
def e_mortar(p):
    return (sky(p, "#3A2A2A", "#6A4A3A", "#2A1A14") + f'<path d="M110 60 L 210 60 C 206 96 190 104 160 104 C 130 104 114 96 110 60 Z" fill="#8A8478" stroke="{INK}" stroke-width="2.4"></path>'
            + f'<ellipse cx="160" cy="60" rx="50" ry="10" fill="#4A4038" stroke="{INK}" stroke-width="2"></ellipse>'
            + f'<path d="M150 62 L 196 10" stroke="{INK}" stroke-width="13" stroke-linecap="round"></path><path d="M150 62 L 196 10" stroke="#A89E92" stroke-width="9" stroke-linecap="round"></path>'
            + "".join(f'<ellipse cx="{x}" cy="{y}" rx="3" ry="2" fill="#E8C060"></ellipse>' for x, y in ((130, 60), (140, 63), (176, 60), (186, 62), (120, 62))))

@emb("stone")
def e_stone(p):
    return (sky(p, "#C8B8A0", "#E8D8C0", "#B89A6A") + f'<path d="M80 104 C 70 80 90 50 130 46 C 170 44 190 70 186 104 Z" fill="#8A8478" stroke="{INK}" stroke-width="2.4"></path>'
            + R.heap(240, 104, 90, 30, "#E8D0A0"))

@emb("pit")
def e_pit(p):
    return (sky(p, "#C8B8A0", "#E8D8C0", "#9A8A6A") + f'<ellipse cx="160" cy="104" rx="80" ry="14" fill="#12090A" stroke="{INK}" stroke-width="2.4"></ellipse>'
            + f'<path d="M80 104 C 90 116 230 116 240 104" fill="none" stroke="#5A4A3A" stroke-width="2"></path>'
            + f'<circle cx="250" cy="82" r="20" fill="#8A8478" stroke="{INK}" stroke-width="2.4"></circle><path d="M236 70 C 220 64 210 74 206 84" fill="none" stroke="#0D0D0F" stroke-width="1.6" stroke-dasharray="3 3"></path>'
            + f'<path d="M120 100 L 112 120 M200 100 L 208 120" stroke="#5A4A3A" stroke-width="2"></path>')

@emb("grave", "death", "sheol")
def e_grave(p):
    return (sky(p, "#14141E", "#3A3A4A", "#2A2420") + f'<path d="M-500 104 L 40 104 C 60 40 260 30 300 104 L 820 104 L 820 520 L -500 520 Z" fill="#3A3430" stroke="{INK}" stroke-width="2"></path>'
            + f'<path d="M110 104 C 110 64 210 64 210 104 Z" fill="#05050A" stroke="{INK}" stroke-width="2.2"></path>' + f'<circle cx="236" cy="88" r="20" fill="#5A544E" stroke="{INK}" stroke-width="2.2"></circle>')

@emb("snare", "net")
def e_snare(p):
    net = "".join(f'<path d="M{x} 104 L {x + 40} 76" stroke="#5A4A3A" stroke-width="1.4"></path><path d="M{x + 40} 104 L {x} 76" stroke="#5A4A3A" stroke-width="1.4"></path>' for x in range(90, 220, 20))
    return (sky(p, "#8FD0E2", "#E8F6FA", "#9CCB5E") + f'<path d="M90 104 C 120 70 220 70 250 104" fill="none" stroke="#5A4A3A" stroke-width="2"></path>' + net
            + f'<path d="M260 104 L 300 60" stroke="#5A3A22" stroke-width="3"></path>' + E4quail(150, 44))

def E4quail(x, y):
    import exodus4 as E4
    return E4.quail(x, y, 0.8, flip=False, flying=True)

@emb("bird", "birds", "sparrow")
def e_birds(p):
    return sky(p, "#8FD0E2", "#E8F6FA") + E4quail(110, 54) + "".join(bird(x, y, s) for x, y, s in ((200, 40, 1.4), (240, 60, 1.1), (180, 76, 1.0), (260, 30, 0.8)))

@emb("eagle")
def e_eagle(p):
    wing = "M0 0 C -20 -10 -60 -30 -100 -20 C -80 -14 -70 -6 -60 0 C -80 4 -90 10 -96 18 C -60 10 -30 10 0 10 Z"
    return (sky(p, "#5A8FC8", "#E8F6FA") + rays(250, 10, 14, 10, 160, "#FFF4C2", 0.4, 8)
            + f'<g transform="translate(160 66) rotate(-14)"><path d="{wing}" fill="#5A3A22" stroke="{INK}" stroke-width="2"></path><path d="{wing}" transform="scale(-1 1)" fill="#5A3A22" stroke="{INK}" stroke-width="2"></path>'
            + f'<ellipse cx="0" cy="4" rx="12" ry="20" fill="#5A3A22" stroke="{INK}" stroke-width="2"></ellipse><circle cx="0" cy="-16" r="8" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></circle><path d="M0 -20 L 8 -14 L 0 -12 Z" fill="#E8B830"></path></g>')

# ---- beasts ------------------------------------------------------------------------------------------------------------
@emb("lion")
def e_lion(p):
    return sky(p, "#E8A35A", "#FFE3B8", "#C8A06A") + J2.lion(170, 104, 0.62)

@emb("bear")
def e_bear(p):
    body = ("M-70 0 L -66 -30 C -80 -50 -70 -84 -30 -90 C 10 -96 50 -88 60 -70 C 76 -76 92 -70 96 -56 C 100 -44 92 -36 80 -36 L 64 -34 L 58 0 L 44 0 L 40 -26 "
            "C 10 -22 -20 -22 -40 -26 L -48 0 Z")
    return (sky(p, "#5E6E8A", "#C8B8A0", "#8A7A5A") + f'<g transform="translate(160 104) scale(0.85)"><path d="{body}" fill="#4A3020" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"></path>'
            + f'<circle cx="62" cy="-78" r="6" fill="#4A3020" stroke="{INK}" stroke-width="2"></circle><circle cx="84" cy="-58" r="2.4" fill="#F3EFE6"></circle><path d="M94 -48 L 82 -42 L 92 -40" fill="#5A0E16" stroke="{INK}" stroke-width="1.4"></path></g>')

@emb("dog")
def e_dog(p):
    body = ("M-60 -40 C -50 -52 20 -54 40 -50 L 52 -70 C 58 -76 66 -76 70 -70 L 80 -62 L 90 -58 C 92 -52 88 -48 80 -48 L 66 -46 L 58 -36 L 56 0 L 46 0 L 44 -30 "
            "C 20 -26 -20 -26 -40 -30 L -44 0 L -54 0 L -56 -34 C -66 -36 -78 -46 -86 -60 C -76 -52 -66 -46 -60 -40 Z")
    return (sky(p, "#C8B8A0", "#E8D8C0", "#9A8A6A") + f'<g transform="translate(150 104) scale(0.95)"><path d="{body}" fill="#8A6A3A" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"></path>'
            + f'<path d="M58 -72 L 54 -84 L 64 -76 Z" fill="#6A4A2A" stroke="{INK}" stroke-width="1.4"></path><circle cx="72" cy="-62" r="2.2" fill="#0D0D0F"></circle></g>')

@emb("horse")
def e_horse(p):
    return sky(p, "#C8B8A0", "#E8D8C0", "#B89A6A") + E3.horse(160, 104, 0.62)

@emb("ass")
def e_ass(p):
    return sky(p, "#8FD0E2", "#FFE3B8", "#C8A06A") + N.ass(160, 104, 0.62) + '<path d="M196 50 L 214 44 L 220 60" fill="none" stroke="#5A3A22" stroke-width="2"></path>'

@emb("ox")
def e_ox(p):
    crib = f'<path d="M210 104 L 214 70 L 290 70 L 294 104 Z" fill="#8A5A30" stroke="{INK}" stroke-width="2"></path><path d="M214 72 L 290 72" stroke="#C8B070" stroke-width="6"></path>'
    return sky(p, "#5A3A22", "#8A6A4A", "#5A4A30") + crib + S1.cow(130, 104, 0.6, color="#8A5A30", patch="#E8E2D6")

@emb("sheep", "flock")
def e_sheep(p):
    return sky(p, "#8FD0E2", "#E8F6FA", "#9CCB5E") + "".join(E.sheep(x, y, s, flip=x > 160) for x, y, s in ((70, 104, 0.6), (130, 100, 0.55), (200, 104, 0.62), (256, 100, 0.55), (160, 108, 0.6)))

@emb("goats")
def e_goats(p):
    from lev.art import goat
    return sky(p, "#8FD0E2", "#E8F6FA", "#9CCB5E") + goat(100, 104, 0.6) + goat(170, 104, 0.55) + f'<path d="M234 104 C 222 100 220 74 236 66 L 234 56 L 256 56 L 254 66 C 270 74 268 100 256 104 Z" fill="#E8E2D6" stroke="{INK}" stroke-width="2"></path>'

@emb("swine")
def e_swine(p):
    body = "M-60 -20 C -64 -48 -30 -60 10 -58 C 40 -56 56 -46 62 -34 L 76 -34 C 80 -28 80 -20 76 -16 L 62 -14 C 56 -8 50 -6 44 -6 L 44 0 L 34 0 L 32 -6 L -30 -6 L -32 0 L -42 0 L -44 -8 C -52 -10 -58 -14 -60 -20 Z"
    return (sky(p, "#8A7A5A", "#C8B8A0", "#6A5A3A") + f'<g transform="translate(150 104) scale(1.05)"><path d="{body}" fill="#D8A0A0" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"></path>'
            + f'<path d="M30 -52 L 36 -64 L 42 -50 Z" fill="#D8A0A0" stroke="{INK}" stroke-width="1.4"></path><circle cx="52" cy="-40" r="2" fill="#0D0D0F"></circle>'
            + f'<circle cx="76" cy="-22" r="7" fill="none" stroke="#0D0D0F" stroke-width="4.4"></circle><circle cx="76" cy="-22" r="7" fill="none" stroke="#E8B830" stroke-width="2.6"></circle></g>')

@emb("serpent", "adder")
def e_serpent(p):
    import snake
    P = [(70, 96), (110, 80), (150, 96), (190, 82), (220, 64), (236, 46)]
    return sky(p, "#C8A06A", "#E8C88A", "#B89A6A") + snake.snake(P, 12, p + "sn", 0.9)

@emb("ant")
def e_ant(p):
    def ant(x, y, s, grain=True):
        return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})" stroke="{INK}" stroke-width="2">'
                '<path d="M-14 -6 L -26 6 M-14 -6 L -20 8 M0 -6 L 0 8 M0 -6 L 6 8 M10 -6 L 22 6 M10 -6 L 16 8" fill="none" stroke-width="2.4"></path>'
                '<ellipse cx="-22" cy="-10" rx="13" ry="9" fill="#3A1A10"></ellipse><ellipse cx="0" cy="-10" rx="7" ry="5" fill="#3A1A10"></ellipse><circle cx="16" cy="-12" r="7" fill="#3A1A10"></circle>'
                '<path d="M20 -18 C 26 -30 34 -30 36 -24 M18 -18 C 20 -32 28 -36 32 -34" fill="none" stroke-width="1.6"></path>'
                + ('<ellipse cx="28" cy="-6" rx="7" ry="4" fill="#E8C060" stroke-width="1.4"></ellipse>' if grain else "") + "</g>")
    return (sky(p, "#FFE3B8", "#E8C88A", "#C8A06A") + ant(150, 98, 2.0) + "".join(ant(x, 108, 0.6) for x in (40, 70, 230, 260, 290))
            + "".join(f'<ellipse cx="{x}" cy="104" rx="4" ry="2.6" fill="#E8C060" stroke="{INK}" stroke-width="1"></ellipse>' for x in (220, 300, 20)))

@emb("locusts")
def e_locusts(p):
    return sky(p, "#C8B070", "#FFE3B8", "#B89A6A") + E2.locusts(18, 20, 300, 16, 96, 3, 0.3, 0.7)

@emb("coney", "conies")
def e_conies(p):
    rock = E4rock(160, 104, 220, 80)
    con = lambda x, y, s: (f'<g transform="translate({x} {y}) scale({s})"><path d="M-22 0 C -26 -16 -12 -26 6 -24 C 18 -22 26 -14 26 -4 L 22 0 Z" fill="#9A7A5A" stroke="{INK}" stroke-width="1.8"></path>'
                           f'<path d="M-14 0 L -14 4 M14 0 L 14 4" stroke="{INK}" stroke-width="3"></path><circle cx="18" cy="-14" r="2.2" fill="#0D0D0F"></circle><path d="M6 -24 C 6 -32 14 -32 12 -22" fill="#9A7A5A" stroke="{INK}" stroke-width="1.4"></path></g>')
    return sky(p, "#8FD0E2", "#E8F6FA", "#9A8A6A") + rock + con(118, 66, 1.4) + con(176, 44, 1.2) + con(206, 84, 1.3)

@emb("lizard", "spider")
def e_lizard(p):
    body = "M-60 0 C -40 -6 -20 -6 0 -8 C 20 -10 34 -8 44 -4 C 50 -2 50 2 44 4 C 34 8 20 8 0 6 C -20 6 -40 4 -60 0 Z"
    legs = "M-10 -6 L -16 -18 L -22 -16 M-10 6 L -16 18 L -22 16 M20 -8 L 26 -20 L 32 -18 M20 8 L 26 20 L 32 18"
    return (sky(p, "#3A2214", "#6A3A1A", "#4A2A14") + f'<rect x="-500" y="-400" width="1320" height="920" fill="#C8A06A" opacity="0.2"></rect>'
            + f'<path d="M80 20 L 240 20 L 240 104 L 80 104 Z" fill="#E8D8B0" stroke="{INK}" stroke-width="2"></path><path d="M80 20 L 240 20" stroke="#E8B830" stroke-width="6"></path>'
            + f'<g transform="translate(170 64) rotate(-20)"><path d="{legs}" fill="none" stroke="{INK}" stroke-width="3"></path><path d="{body}" fill="#6A7A4A" stroke="{INK}" stroke-width="2"></path><circle cx="38" cy="-2" r="1.6" fill="#0D0D0F"></circle></g>')

@emb("greyhound", "he_goat")
def e_greyhound(p):
    return e_dog(p)

# ---- faces ------------------------------------------------------------------------------------------------------------
WISE = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#F3EFE6", cord=True, light="#FFE680")
FOOL = F("adam", skin="#E3B08A", shadow="#8A4A3A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", laugh=True, light="#FF8A3D")
ANGRY = F("adam", skin="#C47A5A", shadow="#5A1A16", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#5A2A16", cord=True, brow="scowl", light="#FF6A4A")
LISTEN = F("adam", skin="#D9A27A", shadow="#7A4A3A", hair="#2A1A10", hl="#4A3A2E", scarf="#8FB8D8", cord=True, light="#FFF4C2")
LIAR = F("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", brow="scowl", light="#9A6AC8")
SAD = F("adam", skin="#C98E66", shadow="#3A3A5A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", brow="sorrow", tear=True, light="#9AA8C8")
GLAD = F("eve", skin="#E3B08A", shadow="#B97A58", hair="#2A1A10", scarf="#2C6A7A", light="#FFE680")

def face_emb(p, tok, top, bot, ray_color, flip=False, lines=True):
    o = sky(p, top, bot) + rays(150, 60, 16, 30, 260, ray_color, 0.3, 8)
    o += mk.face(tok, 206 if flip else 112, 16, 0.27, flip=flip)
    if lines:
        x0 = 192 if not flip else 126
        sgn = 1 if not flip else -1
        o += "".join(f'<path d="M{x0 + sgn * 6} {y} q {sgn * 10} {-4 * k} {sgn * 22} {-2 * k}" fill="none" stroke="#F3EFE6" stroke-width="2.4" stroke-linecap="round"></path>' for y, k in ((80, 1), (88, 0), (96, -1)))
    return o

@emb("face_wise", "lips", "speak")
def e_face_wise(p): return face_emb(p, WISE, "#5A3A1A", "#C8862E", "#FFE680")
@emb("face_fool", "fool")
def e_face_fool(p): return face_emb(p, FOOL, "#3A1A3A", "#8A3A5A", "#FF8A3D")
@emb("face_angry", "wrath")
def e_face_angry(p): return face_emb(p, ANGRY, "#3A0A0A", "#8A1A16", "#FF6A2A", lines=False)
@emb("face_listen", "ear", "hear")
def e_face_listen(p):
    o = face_emb(p, LISTEN, "#1A3A5A", "#5A8FB8", "#FFF4C2", flip=True, lines=False)
    return o + "".join(f'<path d="M{x} 60 q 8 14 0 28" fill="none" stroke="#F3EFE6" stroke-width="2.4" stroke-linecap="round"></path>' for x in (24, 36, 48))
@emb("face_liar", "liar", "tongue")
def e_face_liar(p): return face_emb(p, LIAR, "#1A1030", "#4A2A6A", "#9A6AC8")
@emb("face_sad", "sorrow", "heaviness")
def e_face_sad(p): return face_emb(p, SAD, "#14143A", "#4A5A7A", "#9AA8C8", lines=False)
@emb("face_glad", "joy", "glad")
def e_face_glad(p): return face_emb(p, GLAD, "#8A4A1A", "#FFC14D", "#FFF4C2", lines=False)

# ---- misc ---------------------------------------------------------------------------------------------------------------
@emb("plough", "plow")
def e_plough(p):
    return (sky(p, "#8A9AB8", "#C8D0D8", "#7A6A5A") + "".join(f'<path d="M-20 {y} L 340 {y + 4}" stroke="#5A4A3A" stroke-width="1.6"></path>' for y in (110, 116))
            + f'<path d="M110 100 L 150 70 L 230 64" fill="none" stroke="#5A3A22" stroke-width="6"></path><path d="M150 70 L 140 104 L 156 104 Z" fill="#8A8478" stroke="{INK}" stroke-width="1.6"></path>'
            + f'<path d="M104 92 L 116 104" stroke="#5A3A22" stroke-width="5"></path>' + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#F3EFE6"></circle>' for x, y in ((40, 30), (90, 50), (200, 30), (260, 44), (300, 20))))

@emb("churn", "milk")
def e_churn(p):
    return (sky(p, "#8FD0E2", "#FFE3B8", "#C8A06A") + f'<path d="M120 20 L 150 50 M200 20 L 170 50" stroke="#5A3A22" stroke-width="4"></path>'
            + f'<path d="M120 54 C 110 40 210 40 200 54 C 214 70 206 86 190 88 L 130 88 C 114 86 106 70 120 54 Z" fill="#B8A07A" stroke="{INK}" stroke-width="2.2"></path>'
            + f'<path d="M150 50 L 170 50" stroke="#5A3A22" stroke-width="4"></path><ellipse cx="160" cy="100" rx="24" ry="5" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></ellipse>')

@emb("ship")
def e_ship(p): return e_sea(p)

@emb("harvest")
def e_harvest(p): return e_reaper(p)

@emb("spindle", "distaff")
def e_spindle(p):
    return (sky(p, "#3A2214", "#8A5A2A", "#4A2A14") + glow(160, 60, 60, "#FFC14D", 0.3)
            + f'<path d="M110 20 L 110 104" stroke="{INK}" stroke-width="8"></path><path d="M110 20 L 110 104" stroke="#C8862E" stroke-width="5"></path><ellipse cx="110" cy="34" rx="16" ry="14" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></ellipse>'
            + f'<path d="M124 38 C 150 50 170 40 196 30" fill="none" stroke="#F3EFE6" stroke-width="1.6"></path><path d="M196 24 L 196 92" stroke="#8A5A30" stroke-width="3"></path>'
            + f'<ellipse cx="196" cy="84" rx="12" ry="4" fill="#5A3A22" stroke="{INK}" stroke-width="1.4"></ellipse><ellipse cx="196" cy="56" rx="8" ry="12" fill="#B5121B" stroke="{INK}" stroke-width="1.4"></ellipse>')

@emb("wool", "flax")
def e_wool(p):
    return (sky(p, "#8FD0E2", "#FFE3B8", "#C8A06A") + J1.fleece(110, 100, 0.8) + "".join(f'<path d="M{x} 104 L {x + 2} 56" stroke="#7A8A4A" stroke-width="2"></path><circle cx="{x + 2}" cy="54" r="3" fill="#6A8AC8"></circle>' for x in range(190, 280, 10)))

def pick_bg(name): return name in EMB
