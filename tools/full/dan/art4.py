"""Drawings for Daniel chapter 4 (Daniel 7–8): the visions as technical, symbolic plates. The four winds upon the great sea;
the four beasts as heraldic emblems in flat colour on a dark field (the lion with eagle's wings, the bear raised up on one
side, the leopard with four wings and four heads, the fourth beast with iron teeth and ten horns and the little horn with
eyes) — never gory; the thrones placed and the throne of fiery flames with its burning wheels and the fiery stream, light
only where one sat (no figure is ever drawn); one like unto a son of man coming with the clouds (light in the clouds); the
ram with two horns and the he-goat with the notable horn, by the river Ulai at Shushan; Gabriel as a figure of light."""
from dan.art import *
from dan.art import f, K2
import random, math

FIELD = "#12102A"

def field(w, h, seed=1, color=FIELD, ring=True):
    """A dark heraldic field: a ruled border and faint stars."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{color}"></rect>', mk.stars(30, w, h, seed, color="#5A5A8A")]
    if ring: o.append(f'<rect x="8" y="8" width="{f(w - 16)}" height="{f(h - 16)}" fill="none" stroke="#FFD23F" stroke-width="1.4" opacity="0.5"></rect>')
    return "".join(o)

def wing(x, y, s, color="#E8E2D6", flip=False, rot=0):
    """An eagle's wing raised from the shoulder at (x, y)."""
    sx = -s if flip else s
    d = "M0 0 C -20 -50 0 -96 52 -106 C 42 -88 46 -80 56 -74 C 42 -70 42 -62 50 -56 C 36 -54 34 -46 40 -40 C 26 -38 18 -26 18 -12 Z"
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(sx)} {f(s)})"><path d="{d}" fill="{color}" stroke="#0D0D0F" stroke-width="{f(2.2 / s)}" stroke-linejoin="round"></path>'
            + "".join(f'<path d="M{6 + i * 4} {-10 - i * 14} L {30 + i * 6} {-24 - i * 16}" stroke="#0D0D0F" stroke-width="{f(1.2 / s)}" opacity="0.6"></path>' for i in range(5)) + '</g>')

def lion_beast(x, y, s, plucked=False):
    """The first beast: like a lion, with eagle's wings; plucked=True: the wings plucked, lifted up to stand upon two feet."""
    if plucked:
        body = (f'<g transform="translate({f(x)} {f(y)}) rotate(-62) scale({f(s)})">' + lion_walk(0, 0, 1, color="#E8B830").replace('translate(0.0 0.0) scale(1.0 1.0)', '') + '</g>')
        return body + V.rays(x, y - 80 * s, 16, 10, 120 * s, color="#FFF4C2", op=0.2)
    return wing(x - 6 * s, y - 38 * s, s * 0.9, color="#F3EFE6") + lion_walk(x, y, s, color="#E8B830") + wing(x + 4 * s, y - 40 * s, s * 0.9, color="#E8E2D6", rot=8)

def bear_beast(x, y, s):
    """The second beast: like to a bear, raised up on one side, three ribs in its mouth."""
    d = "M-60 0 L -54 -22 C -72 -44 -56 -78 -22 -80 C 12 -84 38 -70 50 -54 C 64 -56 78 -46 78 -36 C 78 -26 68 -22 60 -24 L 52 -14 L 54 0 L 42 0 L 38 -16 L -32 -16 L -34 0 Z"
    return (f'<g transform="translate({f(x)} {f(y)}) rotate(-10) scale({f(s)})"><path d="{d}" fill="#8A5A3A" stroke="#0D0D0F" stroke-width="{f(2.4 / s)}" stroke-linejoin="round"></path>'
            '<circle cx="66" cy="-40" r="2.4" fill="#0D0D0F"></circle><path d="M44 -66 C 46 -76 56 -76 56 -66" fill="#8A5A3A" stroke="#0D0D0F" stroke-width="1.6"></path>'
            + "".join(f'<path d="M{70 + i * 4} -30 C {78 + i * 4} -26 {78 + i * 4} -18 {72 + i * 4} -14" fill="none" stroke="#F3EFE6" stroke-width="3.4" stroke-linecap="round"></path>' for i in range(3))
            + '</g>')

def leopard_beast(x, y, s):
    """The third beast: like a leopard, four wings of a bird upon its back, four heads."""
    o = [wing(x - 26 * s, y - 36 * s, s * 0.6, color="#8FD0E2", rot=-14), wing(x - 4 * s, y - 38 * s, s * 0.66, color="#8FD0E2")]
    o.append(lion_walk(x, y, s, color="#E8A040"))
    r = random.Random(3)
    o.append("".join(f'<circle cx="{f(x + r.uniform(-40, 14) * s)}" cy="{f(y - r.uniform(18, 36) * s)}" r="{f(2.6 * s)}" fill="#3A2210"></circle>' for _ in range(14)))
    for i, (dx, dy) in enumerate(((50, -64), (62, -54), (64, -72), (40, -78))):
        o.append(f'<ellipse cx="{f(x + dx * s)}" cy="{f(y + dy * s)}" rx="{f(11 * s)}" ry="{f(9 * s)}" fill="#E8A040" stroke="#0D0D0F" stroke-width="2"></ellipse>'
                 f'<circle cx="{f(x + (dx + 4) * s)}" cy="{f(y + (dy - 2) * s)}" r="{f(1.6 * s)}" fill="#0D0D0F"></circle>')
    o.append(wing(x + 6 * s, y - 40 * s, s * 0.66, color="#C8E8F0", rot=10) + wing(x + 20 * s, y - 38 * s, s * 0.58, color="#C8E8F0", rot=24))
    return "".join(o)

def fourth_beast(x, y, s, little=True, three_fallen=True):
    """The fourth beast: terrible and powerful, great iron teeth, nails of brass, ten horns; the little horn with eyes like the
    eyes of a man (three of the first horns plucked up before it)."""
    d = ("M-80 0 L -74 -30 C -92 -50 -80 -84 -40 -88 L 30 -90 C 50 -100 76 -96 88 -78 C 100 -66 98 -48 88 -40 L 70 -36 L 66 -14 L 70 0 L 54 0 "
         "L 48 -18 L -36 -20 L -40 0 L -56 0 L -58 -18 Z")
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="{d}" fill="#4A4A5A" stroke="#0D0D0F" stroke-width="{f(2.6 / s)}" stroke-linejoin="round"></path>']
    o.append("".join(f'<path d="M{-60 + i * 14} -86 L {-54 + i * 14} -100 L {-48 + i * 14} -88" fill="#6A6A7A" stroke="#0D0D0F" stroke-width="1.6"></path>' for i in range(7)))
    o.append('<path d="M70 -50 L 96 -50 L 92 -40 L 88 -48 L 84 -40 L 80 -48 L 76 -40 L 72 -48 Z" fill="#B8C0C8" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append("".join(f'<path d="M{a} 0 l -4 6 M{a + 6} 0 l 0 7 M{a + 12} 0 l 4 6" stroke="#C8783A" stroke-width="3" stroke-linecap="round"></path>' for a in (-56, -36, 52)))
    o.append('<circle cx="80" cy="-70" r="3" fill="#D7261E"></circle>')
    horns = []
    for i in range(10):
        a = -150 + i * 12
        hx, hy = 70 + math.cos(math.radians(a)) * 20, -92 + math.sin(math.radians(a)) * 10
        tx, ty = hx + math.cos(math.radians(a)) * 34, hy + math.sin(math.radians(a)) * 40 - 10
        fallen = three_fallen and i in (5, 6, 7)
        if fallen:
            horns.append(f'<path d="M{f(hx + 30)} {f(-4)} L {f(hx + 46)} {f(-10)} L {f(hx + 44)} {f(-2)} Z" fill="#B8B2A6" stroke="#0D0D0F" stroke-width="1.4" opacity="0.8"></path>')
        else:
            horns.append(f'<path d="M{f(hx - 3)} {f(hy)} L {f(tx)} {f(ty)} L {f(hx + 3)} {f(hy)} Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.4"></path>')
    o.append("".join(horns))
    if little:
        o.append('<path d="M78 -96 C 82 -116 90 -126 98 -132 C 98 -118 94 -106 86 -96 Z" fill="#D7261E" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 '<ellipse cx="90" cy="-116" rx="3.6" ry="2.4" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1"></ellipse><circle cx="90.6" cy="-116" r="1.3" fill="#0D0D0F"></circle>'
                 '<ellipse cx="86" cy="-106" rx="3.4" ry="2.2" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1"></ellipse><circle cx="86.6" cy="-106" r="1.2" fill="#0D0D0F"></circle>'
                 '<path d="M84 -100 C 88 -98 90 -98 92 -100" fill="none" stroke="#0D0D0F" stroke-width="1.4"></path>')
    o.append('</g>')
    return "".join(o)

def sea_winds(w, h, seed, beasts=0):
    """The four winds of heaven breaking forth upon the great sea by night; beasts=n: the backs of n beasts rising from it."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#0B0B2A", "#2A2A5A"), mk.stars(40, w, h * 0.5, seed)]
    for i in range(6):
        y = h * (0.56 + i * 0.08)
        d = f"M-10 {f(y)} " + " ".join(f"Q {f(x + 30)} {f(y - 14 - r.uniform(0, 10))} {f(x + 60)} {f(y)}" for x in range(-10, int(w) + 60, 60))
        o.append(f'<path d="{d} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{("#0F2A4A", "#15365A", "#1F4A6A")[i % 3]}" stroke="#0D0D0F" stroke-width="2"></path>')
    for a, (x0, y0) in enumerate(((0.04, 0.1), (0.96, 0.1), (0.04, 0.5), (0.96, 0.5))):
        x1 = w * 0.5 + (w * x0 - w * 0.5) * 0.4
        o.append(f'<path d="M{f(w * x0)} {f(h * y0)} C {f(w * (x0 + 0.5) / 2)} {f(h * (y0 - 0.06))} {f(x1)} {f(h * 0.3)} {f(x1)} {f(h * 0.54)}" fill="none" stroke="#C8E8F0" stroke-width="2.4" stroke-dasharray="10 6"></path>')
    o.append(label(w * 0.5, h * 0.08, "THE FOUR WINDS OF HEAVEN · THE GREAT SEA", "#C8E8F0", max(8, min(11, h / 30))))
    return "".join(o)

def beast_plate(w, h, which, stage=0):
    """One beast as a heraldic emblem on the dark field, with its name: which 1 (lion, stage 1 plucked), 2 (bear),
    3 (leopard), 4 (the fourth beast; stage 1: the little horn come up)."""
    o = [field(w, h, which)]
    s = min(h / 150, w / 260)
    x, y = w * 0.56, h * 0.88
    if which == 1: o.append(lion_beast(x, y, s * 1.1, plucked=stage == 1))
    if which == 2: o.append(bear_beast(x, y, s * 1.1))
    if which == 3: o.append(leopard_beast(x, y, s * 1.05))
    if which == 4: o.append(fourth_beast(x, y, s * 0.92, little=stage >= 1, three_fallen=stage >= 1))
    names = {1: "I · LIKE A LION · EAGLE'S WINGS", 2: "II · LIKE TO A BEAR · THREE RIBS", 3: "III · LIKE A LEOPARD · FOUR WINGS · FOUR HEADS", 4: "IV · TERRIBLE AND POWERFUL · TEN HORNS"}
    o.append(label(w * 0.04, h * 0.14, names[which], "#FFD23F", max(8, min(11, h / 22)), anchor="start"))
    return "".join(o)

def four_beasts(w, h, seed=1):
    """The four beasts as a row of emblems: four kings that shall arise out of the earth."""
    o = [field(w, h, seed)]
    s = min(h / 260, w / 1100)
    fns = [lambda x, y: lion_beast(x, y, s), lambda x, y: bear_beast(x, y, s), lambda x, y: leopard_beast(x, y, s), lambda x, y: fourth_beast(x, y, s * 0.8, little=True)]
    for i, fn in enumerate(fns):
        x = w * (0.13 + i * 0.245)
        o.append(fn(x, h * 0.72) + label(x, h * 0.88, ("I", "II", "III", "IV")[i] + " · A KING", "#FFD23F", max(8, min(10, h / 24))))
    return "".join(o)

def fiery_throne(w, h, seed, son=False, books=True):
    """Thrones placed, and the throne of fiery flames with its wheels of burning fire; a fiery stream issuing from before it;
    thousands of thousands as ranks of small lights; the books opened. Where one sat there is only white light, no figure.
    son=True: clouds of heaven coming near, a light within them."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#0B0B2A", "#2A1A4A")]
    cx, cy = w * 0.5, h * 0.36
    k = min(h / 400, w / 600)
    for i in range(int(w / 9)):
        x = r.uniform(0, w); y = r.uniform(h * 0.05, h * 0.75)
        if abs(x - cx) < 120 * k and y < h * 0.7: continue
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(0.8, 2))}" fill="#FFF4C2" opacity="{f(r.uniform(0.4, 0.9))}"></circle>')
    for dx in (-1, 1):
        tx = cx + dx * 200 * k
        o.append(f'<rect x="{f(tx - 24 * k)}" y="{f(cy + 30 * k)}" width="{f(48 * k)}" height="{f(60 * k)}" fill="#3A2A5A" stroke="#FFD23F" stroke-width="1.6" opacity="0.8"></rect>')
    o.append(f'<path d="M{f(cx - 40 * k)} {f(cy + 120 * k)} C {f(cx - 60 * k)} {f(h * 0.8)} {f(cx + 60 * k)} {f(h * 0.82)} {f(cx + 30 * k)} {f(h + 10)} L {f(cx + 110 * k)} {f(h + 10)} '
             f'C {f(cx + 130 * k)} {f(h * 0.84)} {f(cx + 40 * k)} {f(h * 0.8)} {f(cx + 40 * k)} {f(cy + 120 * k)} Z" fill="#FF8A3D" stroke="#D7261E" stroke-width="2" opacity="0.9"></path>')
    o.append(V.rays(cx, cy, 36, 30 * k, max(w, h) * 0.8, color="#FFE680", op=0.18))
    o.append(E.blaze(cx, cy + 110 * k, 220 * k, 230 * k, seed, n=9))
    for dx in (-1, 1):
        wx = cx + dx * 96 * k; wy = cy + 116 * k
        o.append(f'<circle cx="{f(wx)}" cy="{f(wy)}" r="{f(30 * k)}" fill="none" stroke="#FFD23F" stroke-width="{f(6 * k)}"></circle>'
                 + "".join(f'<path d="M{f(wx)} {f(wy)} L {f(wx + math.cos(a) * 30 * k)} {f(wy + math.sin(a) * 30 * k)}" stroke="#FFD23F" stroke-width="{f(3 * k)}"></path>' for a in [i * math.pi / 4 for i in range(8)])
                 + E.flame(wx, wy + 30 * k, 26 * k, 40 * k, 2))
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(46 * k)}" ry="{f(70 * k)}" fill="#FFFFFF" opacity="0.92"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(80 * k)}" ry="{f(110 * k)}" fill="#FFF4C2" opacity="0.35"></ellipse>')
    if books:
        for dx in (-1, 1):
            bx = cx + dx * 250 * k; by = h * 0.86
            o.append(f'<path d="M{f(bx - 40 * k)} {f(by)} L {f(bx)} {f(by + 8 * k)} L {f(bx + 40 * k)} {f(by)} L {f(bx + 40 * k)} {f(by - 26 * k)} L {f(bx)} {f(by - 18 * k)} L {f(bx - 40 * k)} {f(by - 26 * k)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></path>'
                     f'<path d="M{f(bx)} {f(by + 8 * k)} L {f(bx)} {f(by - 18 * k)}" stroke="#0D0D0F" stroke-width="1.6"></path>')
    if son:
        for i in range(6):
            x = w * (0.04 + i * 0.07); y = h * (0.3 + (i % 2) * 0.06)
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(60 * k)}" ry="{f(30 * k)}" fill="#C8C0D8" opacity="0.7" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
        o.append(f'<ellipse cx="{f(w * 0.2)}" cy="{f(h * 0.3)}" rx="{f(40 * k)}" ry="{f(50 * k)}" fill="#FFF4C2" opacity="0.6"></ellipse>'
                 + route([(w * 0.26, h * 0.32), (cx - 90 * k, cy)], color="#FFF4C2"))
    return "".join(o)

def burned(w, h, seed):
    """The beast slain and given to be burned with fire: only fire on the dark field, the emblem's outline consumed."""
    o = [field(w, h, seed), E.blaze(w * 0.5, h * 0.92, w * 0.5, h * 0.7, seed, n=9)]
    o.append(f'<g opacity="0.35">{fourth_beast(w * 0.46, h * 0.86, min(h / 200, w / 300), little=True)}</g>')
    return "".join(o)

def kingdom_light(w, h, seed):
    """The kingdom given to the saints of the Most High: the earth under the whole heaven in light, the dominions bowing."""
    o = [K2.sky(w, h, "#FFE680", "#FFF4C2"), V.rays(w * 0.5, h * 0.1, 40, 20, max(w, h), color="#FFFFFF", op=0.35),
         hills(w, h, h * 0.62, seed, "#9CCB5E", amp=10, step=90), ground(w, h, h * 0.7, "#7AA84A", dy=0)]
    r = random.Random(seed)
    k = min(0.9, h / 500)
    for row in range(3):
        for i in range(9):
            x = w * (0.06 + i * 0.11 + (row % 2) * 0.05); y = h * (0.78 + row * 0.08)
            o.append(N.prostrate(x, y, k * (0.7 + row * 0.15), color=r.choice(PRINCE + ["#5A3A22", "#8A6A4A"]), skin="#C98E66"))
    return "".join(o)

def time_bars(w, h):
    """A time and times and half a time, as a chart; with the ten horns become ten kings, and another after them putting down three."""
    o = [grid_bg(w, h)]
    y = h * 0.3
    for i in range(10):
        x = w * (0.06 + i * 0.065)
        o.append(f'<path d="M{f(x)} {f(y + 20)} L {f(x + 8)} {f(y - 20)} L {f(x + 16)} {f(y + 20)} Z" fill="{"#5A5A6A" if i in (6, 7, 8) else "#E8E2D6"}" stroke="#0D0D0F" stroke-width="1.4"></path>')
    o.append(f'<path d="M{f(w * 0.72)} {f(y + 20)} L {f(w * 0.74)} {f(y - 30)} L {f(w * 0.76)} {f(y + 20)} Z" fill="#D7261E" stroke="#0D0D0F" stroke-width="1.4"></path>'
             + label(w * 0.38, y + 40, "TEN KINGS", CYAN, 9) + label(w * 0.74, y + 40, "ANOTHER · DIVERSE", "#FF8A6A", 9))
    by = h * 0.68
    for i, (n, lab) in enumerate(((1, "A TIME"), (2, "TIMES"), (0.5, "HALF A TIME"))):
        x0 = w * 0.1 + sum((1, 2, 0.5)[:i]) * w * 0.22
        o.append(f'<rect x="{f(x0)}" y="{f(by)}" width="{f(n * w * 0.22 - 6)}" height="{f(h * 0.1)}" fill="#FFD23F" fill-opacity="0.3" stroke="#FFD23F" stroke-width="2"></rect>'
                 + label(x0 + n * w * 0.11, by + h * 0.16 + 6, lab, "#FFD23F", 9))
    return "".join(o)

# ---- Daniel 8 ------------------------------------------------------------------------------------------------------------------
def ram(x, y, s, broken=False):
    """The ram with two horns, one higher than the other (the higher came up last)."""
    o = (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
         '<path d="M-60 0 L -56 -26 C -70 -40 -60 -66 -30 -68 L 30 -66 C 46 -76 66 -72 72 -56 C 78 -44 72 -34 62 -34 L 52 -20 L 54 0 L 42 0 L 38 -18 L -34 -20 L -38 0 Z" '
         'fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>'
         + "".join(f'<circle cx="{-46 + i * 12}" cy="{-50 + (i % 2) * 8}" r="7" fill="none" stroke="#B8B2A6" stroke-width="1.6"></circle>' for i in range(7))
         + '<circle cx="64" cy="-54" r="2.4" fill="#0D0D0F"></circle>')
    if broken:
        o += '<path d="M44 -70 l 8 -6 l 2 6 Z M56 -72 l 10 -4 l 0 6 Z" fill="#C8783A" stroke="#0D0D0F" stroke-width="1.4"></path>'
    else:
        o += ('<path d="M44 -68 C 30 -96 54 -110 62 -90 C 56 -100 44 -92 52 -74" fill="#C8783A" stroke="#0D0D0F" stroke-width="2"></path>'
              '<path d="M56 -70 C 50 -112 84 -132 90 -100 C 84 -114 66 -108 66 -74" fill="#E8A040" stroke="#0D0D0F" stroke-width="2"></path>')
    return o + '</g>'

def goat(x, y, s, horns="one", fly=False):
    """The he-goat from the west with a notable horn between his eyes; horns "one", "four" (four notable horns toward the four
    winds), "little" (the little horn come out of one of them); fly=True: touching not the ground."""
    o = (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
         '<path d="M-62 0 L -58 -24 C -70 -40 -60 -62 -30 -62 L 34 -62 C 50 -76 72 -72 76 -54 C 80 -42 72 -32 64 -30 L 60 -14 L 52 -18 L 52 0 L 40 0 L 36 -18 L -34 -18 L -38 0 Z" '
         'fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>'
         '<path d="M62 -30 L 58 -16 L 66 -22 Z" fill="#3A2A1A" stroke="#0D0D0F" stroke-width="1.4"></path><circle cx="66" cy="-52" r="2.4" fill="#F3EFE6"></circle>')
    if horns == "one":
        o += '<path d="M60 -66 C 70 -96 80 -112 92 -124 C 88 -104 80 -84 70 -64 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2"></path>'
    else:
        for i, a in enumerate((-150, -115, -80, -45)):
            ex, ey = 66 + math.cos(math.radians(a)) * 40, -66 + math.sin(math.radians(a)) * 40
            o += f'<path d="M{63 + i * 2} -66 L {f(ex)} {f(ey)} L {67 + i * 2} -64 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></path>'
        if horns == "little":
            o += '<path d="M90 -84 C 100 -100 110 -112 118 -118 C 116 -104 106 -92 94 -82 Z" fill="#D7261E" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o += '</g>'
    if fly:
        o += "".join(f'<path d="M{f(x - (80 + i * 30) * s)} {f(y - (20 + i * 10) * s)} l {f(-40 * s)} 0" stroke="#C8E8F0" stroke-width="2.4" opacity="0.7"></path>' for i in range(4))
    return o

def ulai(p, w, h, seed, stage="ram"):
    """By the river Ulai at Shushan, as a vision plate: the river across the field, the ram standing before it pushing
    westward, northward and southward (stage "ram"); the he-goat flying from the west ("goat"); the goat smiting the ram,
    the two horns broken ("smite"); the four horns toward the four winds ("four"); the little horn waxing great toward the
    south, the east and the glorious land, up to the host of heaven, stars cast down ("little")."""
    o = [field(w, h, seed, ring=False)]
    o.append(f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.76)} {f(w * 0.6)} {f(h * 0.86)} {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h * 0.9)} C {f(w * 0.6)} {f(h * 0.96)} {f(w * 0.3)} {f(h * 0.86)} -10 {f(h * 0.9)} Z" fill="#1F4A6A" stroke="#8FD0E2" stroke-width="1.6"></path>'
             + label(w * 0.86, h * 0.98, "THE RIVER ULAI", CYAN, 8))
    s = min(h / 200, w / 420)
    if stage == "ram":
        o.append(ram(w * 0.56, h * 0.78, s))
        for (dx, dy, t) in ((-1, 0, "WESTWARD"), (0, -1, "NORTHWARD"), (0, 1, "SOUTHWARD")):
            x1, y1 = w * 0.56 + dx * w * 0.3, h * 0.5 + dy * h * 0.36
            o.append(route([(w * 0.56, h * 0.5), (x1, max(h * 0.08, min(h * 0.92, y1)))], color="#FFD23F") + label(x1, max(h * 0.08, min(h * 0.94, y1)) + (14 if dy >= 0 else -6), t, "#FFD23F", 8))
    if stage == "goat":
        o.append(ram(w * 0.78, h * 0.78, s) + goat(w * 0.3, h * 0.6, s, fly=True) + label(w * 0.1, h * 0.14, "FROM THE WEST", "#FFD23F", 9, anchor="start"))
    if stage == "smite":
        o.append(f'<g transform="rotate(16 {f(w * 0.7)} {f(h * 0.8)})">{ram(w * 0.7, h * 0.8, s, broken=True)}</g>' + goat(w * 0.42, h * 0.78, s))
    if stage == "four":
        o.append(goat(w * 0.46, h * 0.78, s * 1.1, horns="four"))
        for a, t in ((-150, "W"), (-115, "N"), (-80, "E"), (-45, "S")):
            pass
        o.append(label(w * 0.5, h * 0.12, "THE GREAT HORN BROKEN · FOUR NOTABLE HORNS TOWARD THE FOUR WINDS", "#FFD23F", max(7, min(9, h / 30))))
    if stage == "little":
        o.append(goat(w * 0.3, h * 0.8, s, horns="little"))
        for t, pt in (("TOWARD THE SOUTH", (0.62, 0.86)), ("TOWARD THE EAST", (0.9, 0.5)), ("THE GLORIOUS LAND", (0.66, 0.6))):
            o.append(route([(w * 0.36, h * 0.5), (w * pt[0], h * pt[1])], color="#FF8A6A") + label(w * pt[0], h * pt[1] - 6, t, "#FF8A6A", 8))
        r = random.Random(seed)
        for i in range(9):
            x, y = r.uniform(0.3, 0.9) * w, r.uniform(0.06, 0.3) * h
            o.append(f'<path d="M{f(x)} {f(y)} l 0 {f(h * 0.12)}" stroke="#FFF4C2" stroke-width="1.2" stroke-dasharray="3 4" opacity="0.6"></path>'
                     f'<circle cx="{f(x)}" cy="{f(y + h * 0.12)}" r="2.4" fill="#FFF4C2"></circle>')
        o.append(label(w * 0.6, h * 0.05 + 8, "EVEN TO THE HOST OF HEAVEN", "#FFF4C2", 8))
    return "".join(o)

def evenings(w, h):
    """Two thousand and three hundred evenings and mornings, as a chart of marks; then shall the sanctuary be cleansed."""
    o = [grid_bg(w, h)]
    n = 230
    cols = 46
    for i in range(n):
        x = w * 0.05 + (i % cols) * (w * 0.9 / cols); y = h * 0.18 + (i // cols) * h * 0.11
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.9 / cols * 0.5)}" height="{f(h * 0.06)}" fill="#0F0E2A" stroke="#FFD23F" stroke-width="0.8"></rect>'
                 f'<rect x="{f(x + w * 0.9 / cols * 0.5)}" y="{f(y)}" width="{f(w * 0.9 / cols * 0.4)}" height="{f(h * 0.06)}" fill="#FFE680" opacity="0.7"></rect>')
    o.append(label(w * 0.5, h * 0.12, "2,300 EVENINGS AND MORNINGS · EACH MARK TEN", "#FFD23F", 9) + label(w * 0.5, h * 0.88, "THEN SHALL THE SANCTUARY BE CLEANSED", CYAN, 9))
    return "".join(o)

def gabriel_bank(p, w, h, seed, fallen=True):
    """Between the banks of the Ulai: one standing as the appearance of a man, a shape of light (Gabriel); Daniel fallen upon
    his face before him."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A2A5A", "#8A7AA8"), ground(w, h, h * 0.7, "#5A6A5A", dy=0),
         f'<path d="M-10 {f(h * 0.78)} C {f(w * 0.3)} {f(h * 0.74)} {f(w * 0.6)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.78)} L {f(w + 10)} {f(h * 0.88)} C {f(w * 0.6)} {f(h * 0.94)} {f(w * 0.3)} {f(h * 0.84)} -10 {f(h * 0.88)} Z" fill="#3A6A8A" stroke="#0D0D0F" stroke-width="1.6"></path>']
    s = fit(h * 0.72, h * 0.12)
    o.append(V.rays(w * 0.66, h * 0.4, 24, 20, w * 0.5, color="#FFF4C2", op=0.2) + glow_fig(w * 0.66, h * 0.72, s))
    if fallen: o.append(N.prostrate(w * 0.3, h * 0.97, s * 0.7, color=DAN_C, skin="#C98E66"))
    else: o.append(dan_fig(p, w * 0.3, h * 0.97, s * 0.9, age=3))
    return "".join(o)
