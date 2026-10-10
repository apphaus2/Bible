"""Generators and faces for Judges Book Two (Samson): Samson with his seven locks, the young lion, foxes with
firebrands, the jawbone, the gates of Gaza, Philistines in feathered helmets, silver, the mill, the house of Dagon
and its two middle pillars, and new faces (Samson, blind Samson, Delilah, Manoah's wife)."""
import math, random
import mk, exodus as E, exodus4 as Z, judges1 as G, joshua1 as J
from faces_ex import F
def f(v): return f"{v:.1f}"

def _locks(color="#1A1210", hl="#4A3A2E", n=7, x0=86, x1=150, top=120, bottom=400, seed=1):
    """Seven long braided locks hanging down the back, drawn behind a face token."""
    r = random.Random(seed); o = []
    for i in range(n):
        x = x0 + (x1 - x0) * i / (n - 1); b = bottom - r.uniform(0, 40)
        d = f"M{f(x + 30)} {f(top)} C {f(x - 10)} {f(top + 80)} {f(x + 16)} {f((top + b) / 2)} {f(x - 4)} {f(b)}"
        o.append(f'<path d="{d}" fill="none" stroke="#0D0D0F" stroke-width="17" stroke-linecap="round"></path>'
                 f'<path d="{d}" fill="none" stroke="{color}" stroke-width="13" stroke-linecap="round"></path>'
                 f'<path d="{d}" fill="none" stroke="{hl}" stroke-width="3" stroke-dasharray="5 7" stroke-linecap="round"></path>')
    return "".join(o)

BANDAGE = ('<path d="M120 150 C 160 140 220 150 266 166 L 262 196 C 220 184 160 176 124 182 Z" fill="#C8B89A" stroke="#0D0D0F" stroke-width="2.4"></path>'
           '<path d="M130 166 C 170 158 220 166 262 180" fill="none" stroke="#8A7A5A" stroke-width="2"></path>')

def tokens():
    t = G.tokens()
    t["__FACE_SAMSON__"] = _locks() + F("adam", skin="#B9785A", shadow="#6A3A2A", hair="#1A1210", hl="#4A3A2E", beard=True, brow="scowl", light="#FF8A3D")
    t["__FACE_SAMSON_SLEEP__"] = _locks() + F("adam", skin="#C98E66", shadow="#5A3A4A", hair="#1A1210", hl="#4A3A2E", beard=True, light="#C2456A")
    t["__FACE_SAMSON_PRAY__"] = F("adam", skin="#B9785A", shadow="#3A1A1A", hair="#1A1210", hl="#4A3A2E", beard=True, brow="sorrow", sweat=True, light="#FFE680") + BANDAGE
    t["__FACE_DELILAH__"] = F("eve", skin="#D9A27A", shadow="#8A5A5A", hair="#1A1210", band=True)
    t["__FACE_MANOAH_WIFE__"] = F("eve", skin="#C98E66", shadow="#8A5A3E", hair="#2A1A10", scarf="#5A6E8A", light="#FFF4C2")
    return t

LOCKS_FIG = "".join(f'<path d="M{dx} -194 C {dx * 1.5} -180 {dx * 1.3} -164 {dx * 1.7 + (2 if dx > 0 else -2)} -140" fill="none" stroke="#1A1210" stroke-width="3.6" stroke-linecap="round"></path>' for dx in (-12, -10, -8, 8, 10, 12, -13))
def samson(p, x, y, s, flip=False, up=None, extra="", cloth="#8A3A1E", body="#3A1E14", locks=True, kind="Tunic", stroke="#0D0D0F", sw=3):
    """Samson at a distance: a powerful man in a short tunic, his seven locks hanging to his shoulders."""
    return mk.person(p, round(x), round(y), s, body=body, cloth=cloth, kind=kind, stroke=stroke, sw=sw, flip=flip, up=up, extra=(LOCKS_FIG if locks else "") + extra)

def lion(x, y, s=1.0, flip=False, roar=True):
    """A young lion leaping or roaring, facing right."""
    sx = -s if flip else s
    mane = "".join(f'<path d="M{f(60 + 30*math.cos(a))} {f(-100 + 34*math.sin(a))} L {f(60 + 46*math.cos(a + 0.12))} {f(-100 + 50*math.sin(a + 0.12))} L {f(60 + 30*math.cos(a + 0.26))} {f(-100 + 34*math.sin(a + 0.26))} Z" fill="#8A4A16" stroke="#0D0D0F" stroke-width="1.6"></path>'
                   for a in [i * 2 * math.pi / 18 for i in range(18)])
    jaw = ('<path d="M84 -96 L 112 -86 L 100 -72 L 84 -78 Z" fill="#5A0E16" stroke="#0D0D0F" stroke-width="2"></path>'
           '<path d="M88 -92 L 92 -86 L 96 -92 M92 -78 L 96 -84 L 100 -78" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1"></path>') if roar else ""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            '<path d="M-90 -70 C -110 -80 -126 -100 -120 -120 C -116 -110 -108 -96 -92 -84 Z" fill="#C8862E" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M-124 -126 C -132 -130 -132 -120 -122 -118 Z" fill="#5A3A22"></path>'
            '<path d="M-96 -84 C -90 -104 -40 -110 0 -106 C 30 -104 44 -112 56 -110 L 70 -80 C 64 -60 50 -56 40 -50 L 54 -6 L 66 0 L 40 0 L 26 -42 C 4 -40 -30 -40 -52 -44 L -70 -8 L -60 0 L -86 0 L -78 -46 C -90 -56 -98 -68 -96 -84 Z" fill="#C8862E" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>'
            f'{mane}'
            '<path d="M48 -122 C 70 -128 96 -118 108 -100 C 114 -90 112 -80 104 -72 C 90 -64 70 -66 58 -74 C 46 -84 42 -106 48 -122 Z" fill="#D9964A" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M58 -124 L 62 -134 L 70 -126 Z" fill="#C8862E" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M84 -108 L 94 -106" stroke="#0D0D0F" stroke-width="3" stroke-linecap="round"></path><circle cx="88" cy="-108" r="2.2" fill="#FFD23F"></circle>'
            f'{jaw}</g>')

def fox(x, y, s=1.0, flip=False, brand=True, seed=1):
    """A fox running, brush streaming behind; brand = a firebrand burning at its tail."""
    sx = -s if flip else s
    fire = E.flame(-66, -26, 10, 34, -14) if brand else ""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            '<path d="M-24 -26 C -40 -30 -56 -26 -70 -18 C -60 -32 -44 -40 -24 -36 Z" fill="#D9641E" stroke="#0D0D0F" stroke-width="1.8"></path>'
            '<path d="M-64 -22 C -68 -20 -70 -18 -70 -18 L -62 -18 Z" fill="#F3EFE6"></path>'
            '<path d="M-28 -30 C -20 -40 10 -40 22 -34 L 34 -44 L 38 -54 L 44 -46 L 52 -40 C 58 -38 60 -34 54 -32 L 40 -28 C 34 -22 26 -18 18 -18 L 30 0 L 22 0 L 8 -16 L -12 -16 L -30 0 L -38 0 L -24 -18 C -30 -22 -30 -26 -28 -30 Z" fill="#D9641E" stroke="#0D0D0F" stroke-width="2" stroke-linejoin="round"></path>'
            '<circle cx="44" cy="-38" r="1.8" fill="#0D0D0F"></circle>'
            f'<path d="M-66 -24 L -54 -20" stroke="#5A3A22" stroke-width="4"></path>{fire}</g>')

def grain(x0, x1, y, h, seed, burning=False):
    r = random.Random(seed); o = []
    x = x0
    while x < x1:
        hh = h * r.uniform(0.8, 1.1)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x + r.uniform(-3, 3))} {f(y - hh)}" stroke="#C9A86A" stroke-width="2"></path>'
                 f'<ellipse cx="{f(x)}" cy="{f(y - hh)}" rx="2.6" ry="7" fill="#E8C88A" stroke="#8A6A3A" stroke-width="1"></ellipse>')
        x += r.uniform(5, 9)
    if burning:
        o.append(E.blaze((x0 + x1) / 2, y, (x1 - x0) / 2, h * 3, seed, n=9))
    return "".join(o)

def olive(x, y, s=1.0, burning=False, seed=1):
    r = random.Random(seed)
    leaves = "".join(f'<circle cx="{f(r.uniform(-50, 50))}" cy="{f(r.uniform(-110, -60))}" r="{f(r.uniform(18, 28))}" fill="{r.choice(["#5E7A4A", "#4E6A3A", "#7A8A5A"])}" stroke="#0D0D0F" stroke-width="1.6"></circle>' for _ in range(9))
    fire = E.blaze(0, -60, 70, 120, seed, n=6) if burning else ""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-8 0 C -14 -30 0 -50 -10 -70 L 6 -70 C 10 -50 12 -30 8 0 Z" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2"></path>'
            f'{leaves}{fire}</g>')

JAW = ("M0 0 C 10 -14 30 -20 60 -18 L 96 -16 C 104 -16 108 -10 104 -4 L 70 -2 C 50 0 34 4 26 16 C 20 26 16 40 6 44 C -4 46 -8 36 -4 26 C 0 16 -4 8 0 0 Z")
def jawbone(x, y, s=1.0, rot=0):
    teeth = "".join(f'<path d="M{f(40 + i*10)} -17 L {f(43 + i*10)} -26 L {f(47 + i*10)} -17 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.2"></path>' for i in range(6))
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">{teeth}<path d="{JAW}" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M10 4 C 24 -6 50 -10 92 -10" fill="none" stroke="#B8B2A6" stroke-width="2"></path></g>')

FEATHERS = "".join(f'<path d="M{dx} -198 L {dx * 1.5} -218 L {dx * 1.5 + 4} -216 L {dx + 4} -198 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1"></path>' for dx in (-12, -8, -4, 0, 4, 8))
FEATHER_BAND = '<rect x="-14" y="-200" width="28" height="5" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="1"></rect>'
def philistines(p, n, x0, x1, y0, y1, seed, smin, smax, flip=False, spear=True):
    """Philistine warriors in feathered head-dresses with round shields."""
    r = random.Random(seed); items = sorted((r.uniform(y0, y1), r.uniform(x0, x1)) for _ in range(n)); o = []
    for y, x in items:
        s = smin + (smax - smin) * (y - y0) / max(1, y1 - y0)
        o.append(mk.person(p, round(x), round(y), round(s, 3), body="#5A2A16", cloth=r.choice(["#1F5FAD", "#B5121B", "#E8B830", "#2C9DB8"]), kind="Tunic", sw=4, flip=flip,
                           extra=FEATHERS + FEATHER_BAND + (Z.SPEAR if spear else "") + '<ellipse cx="22" cy="-120" rx="20" ry="20" fill="#C8962E" stroke="#0D0D0F" stroke-width="3"></ellipse>'))
    return "".join(o)

def gates(x, y, s=1.0, rot=0):
    """The doors of the city gate with the two posts and the bar, as one burden."""
    planks = "".join(f'<path d="M{-80 + i*16} -150 L {-80 + i*16} 0" stroke="#5A3A22" stroke-width="2"></path>' for i in range(11))
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">'
            '<rect x="-96" y="-170" width="16" height="190" fill="#6B4A2A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
            '<rect x="80" y="-170" width="16" height="190" fill="#6B4A2A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
            '<rect x="-80" y="-150" width="80" height="150" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></rect>'
            '<rect x="0" y="-150" width="80" height="150" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></rect>'
            f'{planks}'
            '<path d="M-80 -110 L 80 -110 M-80 -40 L 80 -40" stroke="#3A3A4A" stroke-width="5"></path>'
            '<rect x="-104" y="-84" width="208" height="14" fill="#5A5A6A" stroke="#0D0D0F" stroke-width="2"></rect></g>')

def silver(x, y, n, seed, spread=50):
    r = random.Random(seed)
    return "".join(f'<ellipse cx="{f(x + r.uniform(-spread, spread))}" cy="{f(y + r.uniform(-spread*0.2, spread*0.2))}" rx="9" ry="4" fill="#E8E2D6" stroke="#5A5A6A" stroke-width="1.4"></ellipse>' for _ in range(n))

def mill(x, y, s=1.0):
    """A great millstone turned by a beam (Samson grinding in the prison-house)."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
            '<ellipse cx="0" cy="0" rx="110" ry="30" fill="#5A5A6A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
            '<path d="M-110 0 L -110 30 C -110 70 110 70 110 30 L 110 0" fill="#4A4A5A" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<ellipse cx="0" cy="-30" rx="70" ry="20" fill="#7A7A8A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
            '<path d="M-70 -30 L -70 0 C -70 18 70 18 70 0 L 70 -30" fill="#6A6A7A" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M0 -40 L 210 -70" stroke="#0D0D0F" stroke-width="12" stroke-linecap="round"></path><path d="M0 -40 L 210 -70" stroke="#8A5A30" stroke-width="8" stroke-linecap="round"></path></g>')

def fetters(x, y, s=1.0):
    return f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})" fill="none" stroke="#C8962E" stroke-width="4">' + "".join(f'<ellipse cx="{i*12}" cy="0" rx="7" ry="4"></ellipse>' for i in range(6)) + '</g>'

def temple(W, H, top, pillars_x, uid="dg", lords=True, seed=1):
    """The house of Dagon: a roof full of people on columns, the two middle pillars at pillars_x."""
    r = random.Random(seed); o = []
    o.append(f'<rect x="-10" y="{f(top)}" width="{f(W + 20)}" height="40" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    o.append(f'<path d="M-10 {f(top)} L {f(W/2)} {f(top - 60)} L {f(W + 10)} {f(top)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2.4"></path>')
    if lords:
        for i in range(26):
            x = 20 + i * (W - 40) / 25
            o.append(mk.person(uid, round(x), round(top + 2 - r.uniform(0, 30)), 0.16, body="#2A140C", cloth=r.choice(["#1F5FAD", "#B5121B", "#E8B830", "#7A3BA8"]), kind="Robe", sw=6))
    for px in [W * k for k in (0.06, 0.22)] + list(pillars_x) + [W * k for k in (0.78, 0.94)]:
        mid = px in pillars_x
        w = 34 if mid else 26
        o.append(f'<rect x="{f(px - w/2)}" y="{f(top + 40)}" width="{f(w)}" height="{f(H - top - 40)}" fill="{"#E8C88A" if mid else "#C8A06A"}" stroke="#0D0D0F" stroke-width="2.4"></rect>'
                 f'<rect x="{f(px - w/2 - 6)}" y="{f(top + 40)}" width="{f(w + 12)}" height="10" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 + "".join(f'<path d="M{f(px - w/2 + k*w/4)} {f(top + 50)} L {f(px - w/2 + k*w/4)} {f(H)}" stroke="#8A6A3A" stroke-width="1.2"></path>' for k in (1, 2, 3)))
    return "".join(o)

def cracks_on(px, top, bottom, seed):
    r = random.Random(seed); y = top; x = px; d = f"M{f(x)} {f(y)}"
    while y < bottom:
        y += r.uniform(14, 26); x = px + r.uniform(-12, 12); d += f" L {f(x)} {f(y)}"
    return f'<path d="{d}" fill="none" stroke="#0D0D0F" stroke-width="2.4"></path>'
