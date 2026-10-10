"""New drawings for Genesis chapter 2 (Genesis 4–9): Cain's line, the generations, the ark, the flood, the covenant."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4, exodus5 as V, joshua1 as J, judges1 as G1, judges2 as S
import samuel1 as A, samuel2 as A2, samuel3 as A3, samuel4 as A4, numbers1 as N, ruth1 as R, snake as SN
from faces_ex import F
def f(v): return f"{v:.1f}"

# ---- faces ----------------------------------------------------------------------------------------------
EVE_MOTHER = F("eve", skin="#E3B08A", shadow="#B97A58", hair="#3A1E14", light="#FFD23F")
LAMECH = F("adam", skin="#B98A6E", shadow="#4A1A26", hair="#1A1210", hl="#4A3A2E", brow="scowl", stubble="#2A1A10", light="#FF6A4A", cord=True)
LAMECH_FATHER = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E", cord=True)
NOAH = F("adam", skin="#D9A27A", shadow="#9A6A4A", hair="#E8E2D6", hl="#B8B2A6", beard=True, light="#FFF4C2")
NOAH_GRAVE = F("adam", skin="#C98E66", shadow="#6A4A5A", hair="#E8E2D6", hl="#B8B2A6", beard=True, brow="sorrow")
NOAH_AWE = F("adam", skin="#E3B08A", shadow="#9A6A4A", hair="#E8E2D6", hl="#B8B2A6", beard=True, light="#9FE0FF")
NOAH_WAKE = F("adam", skin="#B98A6E", shadow="#5A3A4A", hair="#E8E2D6", hl="#B8B2A6", beard=True, brow="scowl", light="#FF8A3D")

# ---- people ---------------------------------------------------------------------------------------------
SKIN = "#5A2A16"
FUR = "".join(f'<path d="M{x} -150 l -4 10 M{x + 6} -120 l -4 10 M{x - 4} -90 l -4 10" stroke="#3A1A0A" stroke-width="2"></path>' for x in (-18, -4, 10))
SONS = {"shem": "#1F5FAD", "ham": "#B5421E", "japheth": "#5E8F26"}
WIVES = ["#C2456A", "#7A3BA8", "#E8A317"]
NOAH_ROBE = "#E2D8C4"
WHITE_BEARD = ('<path d="M-10 -172 C -10 -160 -4 -148 0 -142 C 4 -148 10 -160 10 -172 C 6 -166 -6 -166 -10 -172 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></path>'
               '<path d="M-13 -175 C -15 -191 15 -191 13 -175 C 9 -184 -9 -184 -13 -175 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.4"></path>')
FIG_H = 200          # a standing figure is about 200 units tall at scale 1
def fit(base, top):
    """The scale at which a standing figure on `base` reaches up to y = top."""
    return round(max(0.2, (base - top) / FIG_H), 3)

def noah(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=NOAH_ROBE, sw=3, flip=flip, up=up, extra=WHITE_BEARD)

def son(p, x, y, s, who, flip=False, up=None, extra=""):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=SONS[who], kind="Tunic", sw=3, flip=flip, up=up, extra=extra)

def wife(p, x, y, s, color, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=color, woman=True, hair="#1A1210", sw=3, flip=flip, up=up)

def family8(p, x0, x1, y, s, flip=False):
    """Noah, his wife, his three sons and their three wives, in a line."""
    who = [("n",), ("w", "#2C5F9A"), ("s", "shem"), ("w", WIVES[0]), ("s", "ham"), ("w", WIVES[1]), ("s", "japheth"), ("w", WIVES[2])]
    o = []
    for i, w in enumerate(who):
        x = x0 + (x1 - x0) * i / 7
        if w[0] == "n": o.append(noah(p, x, y, s, flip))
        elif w[0] == "s": o.append(son(p, x, y, s * 0.97, w[1], flip))
        else: o.append(wife(p, x, y, s * 0.92, w[1], flip))
    return "".join(o)

def ground(w, h, y, color, dy=-6):
    return f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y + dy)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'

def hills(w, h, y, seed, color="#1A1430", amp=14, step=60):
    r = random.Random(seed)
    d = "M-10 " + f(h + 10) + " L " + " L ".join(f"{f(x)} {f(y + r.uniform(-amp, amp))}" for x in range(-10, int(w) + step, step)) + f" L {f(w + 10)} {f(h + 10)} Z"
    return f'<path d="{d}" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'

def bird(x, y, s=1.0, color="#0D0D0F"):
    return f'<path d="M{f(x - 10 * s)} {f(y)} q {f(5 * s)} {f(-7 * s)} {f(10 * s)} 0 q {f(5 * s)} {f(-7 * s)} {f(10 * s)} 0" fill="none" stroke="{color}" stroke-width="{f(max(1.6, 2.6 * s))}" stroke-linecap="round"></path>'

def birds(n, x0, x1, y0, y1, seed, smin=0.6, smax=1.3, color="#0D0D0F"):
    r = random.Random(seed)
    return "".join(bird(r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(smin, smax), color) for _ in range(n))

# ---- Genesis 4 ------------------------------------------------------------------------------------------
def eve_with_cain(p, w, h):
    """The man and Eve outside, at evening; she holds her firstborn."""
    base = h * 0.86
    return (f'<circle cx="{f(w * 0.78)}" cy="{f(base - 10)}" r="{f(h * 0.22)}" fill="#FFD23F"></circle>'
            + V.rays(w * 0.78, base - 10, 30, h * 0.24, w, color="#FFF4C2", op=0.3)
            + hills(w, h, base, 41, color="#2A1A2E")
            + mk.person(p, round(w * 0.3), round(base), fit(base, h * 0.42), body=SKIN, cloth="#8A5A30", sw=3, extra=FUR)
            + mk.person(p, round(w * 0.46), round(base), round(fit(base, h * 0.42) * 0.95, 3), body=SKIN, cloth="#A8743A", woman=True, hair="#1A1210", sw=3, flip=True,
                        up=R.HOLD_BABY, extra=FUR + R.baby(10, -130, 0.8)))

def mother_and_child(w, h, tok=EVE_MOTHER, baby_xy=(250, 330), flip=False):
    """Eve's face close, with the newborn in the crook of her arm."""
    x = w * 0.62 if flip else -30
    return (mk.face(tok, x, 0, h / 380, flip=flip)
            + f'<path d="M{f(baby_xy[0] - 70)} {f(h + 10)} C {f(baby_xy[0] - 60)} {f(baby_xy[1] - 40)} {f(baby_xy[0] + 70)} {f(baby_xy[1] - 50)} {f(baby_xy[0] + 90)} {f(h + 10)} Z" fill="#A8743A" stroke="#0D0D0F" stroke-width="2.4"></path>'
            + R.baby(baby_xy[0], baby_xy[1], 1.7))

def line_of_cain(p, w, h, seed):
    """Enoch, Irad, Mehujael, Methushael and Lamech: five generations walking out of the city of Enoch."""
    base = h * 0.84
    o = []
    o.append(city(w * 0.12, base, w * 0.24, h * 0.42, seed))
    o.append(ground(w, h, base, "#8A6A4A", dy=-4))
    cl = ["#4A3A6A", "#2C5F9A", "#1F7A8C", "#5E8F26", "#B5421E"]
    for i in range(5):
        x = w * (0.34 + i * 0.145); s = fit(base, h * 0.36) * (0.72 + i * 0.07)
        o.append(f'<g opacity="{0.55 + i * 0.11:.2f}">' + mk.person(p, round(x), round(base + i * 2), round(s, 3), body=SKIN, cloth=cl[i], kind="Tunic", sw=3) + '</g>')
    return "".join(o)

def city(x, base, w, h, seed, color="#3A2A3E", lit="#FFC14D"):
    """A walled city of mud brick with towers, its windows lit."""
    r = random.Random(seed); o = []
    n = 6
    for i in range(n):
        bw = w / n * r.uniform(0.9, 1.3); bh = h * r.uniform(0.35, 1.0); bx = x - w / 2 + i * w / n
        o.append(f'<rect x="{f(bx)}" y="{f(base - bh)}" width="{f(bw)}" height="{f(bh)}" fill="{color}" stroke="#0D0D0F" stroke-width="2"></rect>')
        for k in range(int(bh // 22)):
            if r.random() < 0.45:
                o.append(f'<rect x="{f(bx + bw * r.uniform(0.2, 0.7))}" y="{f(base - bh + 10 + k * 22)}" width="5" height="8" fill="{lit}"></rect>')
    o.append(f'<rect x="{f(x - w / 2 - 6)}" y="{f(base - h * 0.28)}" width="{f(w + 12)}" height="{f(h * 0.28)}" fill="#5A4A4E" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(x - 12)} {f(base)} L {f(x - 12)} {f(base - h * 0.16)} Q {f(x)} {f(base - h * 0.24)} {f(x + 12)} {f(base - h * 0.16)} L {f(x + 12)} {f(base)} Z" fill="#12090A"></path>')
    return "".join(o)

def lamech_wives(p, w, h):
    base = h * 0.86
    return (hills(w, h, base, 19, color="#3A2A1E")
            + mk.person(p, round(w * 0.5), round(base), fit(base, h * 0.32), body=SKIN, cloth="#B5421E", kind="Tunic", sw=3)
            + wife(p, w * 0.3, base, fit(base, h * 0.38), "#C2456A")
            + wife(p, w * 0.7, base, fit(base, h * 0.38), "#7A3BA8", flip=True))

def tents_cattle(w, h, seed):
    """Jabal: the father of such as dwell in tents and have cattle."""
    base = h * 0.8
    return (ground(w, h, base, "#C8A06A", dy=-4)
            + G1.tent_big(w * 0.3, base - 4, w * 0.42, h * 0.42, color="#3A2214")
            + E4.tent(w * 0.75, base - 2, w * 0.26, h * 0.24)
            + A.cow(w * 0.62, base + 18, 0.38, color="#8A5A30") + A.cow(w * 0.86, base + 22, 0.34, flip=True)
            + E.sheep(w * 0.18, base + 26, 0.42) + E.sheep(w * 0.42, base + 30, 0.4, flip=True))

def pipe(x, y, s=1.0, rot=-30):
    holes = "".join(f'<circle cx="{-30 + i * 12}" cy="0" r="2.2" fill="#0D0D0F"></circle>' for i in range(5))
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(s)})"><rect x="-50" y="-5" width="100" height="10" rx="5" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></rect>'
            f'<path d="M46 -8 L 58 -12 L 58 12 L 46 8 Z" fill="#C9A86A" stroke="#0D0D0F" stroke-width="2"></path>{holes}</g>')

def harp_pipe(w, h, seed):
    """Jubal: the father of all such as handle the harp and pipe."""
    return (V.rays(w * 0.5, h * 0.6, 30, 20, w, color="#FFD23F", op=0.25)
            + A2.harp(w * 0.38, h * 0.88, 2.1, rot=-8) + pipe(w * 0.7, h * 0.56, 1.2, rot=-35)
            + A3.notes(w * 0.5, h * 0.3, 7, seed))

def forge(w, h, seed):
    """Tubal-cain: the forger of every cutting instrument of brass and iron."""
    r = random.Random(seed); base = h * 0.82
    sparks = "".join(f'<path d="M{f(w * 0.5)} {f(base - 70)} l {f(r.uniform(-90, 90))} {f(r.uniform(-90, -20))}" stroke="{r.choice(["#FFD23F", "#FF8A3D", "#FFF4C2"])}" stroke-width="2" stroke-linecap="round"></path>' for _ in range(22))
    anvil = (f'<path d="M{f(w * 0.3)} {f(base - 64)} L {f(w * 0.68)} {f(base - 64)} C {f(w * 0.74)} {f(base - 64)} {f(w * 0.8)} {f(base - 54)} {f(w * 0.84)} {f(base - 46)} L {f(w * 0.64)} {f(base - 44)} '
             f'L {f(w * 0.6)} {f(base - 20)} L {f(w * 0.66)} {f(base)} L {f(w * 0.36)} {f(base)} L {f(w * 0.42)} {f(base - 20)} L {f(w * 0.38)} {f(base - 44)} L {f(w * 0.3)} {f(base - 48)} Z" fill="#3A3A44" stroke="#0D0D0F" stroke-width="2.4"></path>')
    blade = f'<path d="M{f(w * 0.36)} {f(base - 70)} L {f(w * 0.62)} {f(base - 76)} L {f(w * 0.66)} {f(base - 70)} L {f(w * 0.62)} {f(base - 66)} L {f(w * 0.36)} {f(base - 66)} Z" fill="#FF8A3D" stroke="#0D0D0F" stroke-width="1.6"></path>'
    hammer = (f'<g transform="translate({f(w * 0.56)} {f(base - 92)}) rotate(-30)"><path d="M0 0 L 0 -80" stroke="#5A3A22" stroke-width="8" stroke-linecap="round"></path>'
              '<rect x="-22" y="-98" width="44" height="22" rx="3" fill="#6A6A74" stroke="#0D0D0F" stroke-width="2"></rect></g>')
    tools = "".join(f'<g transform="translate({f(x)} {f(base + 6)}) rotate({a})"><path d="M0 0 L 0 -46" stroke="#5A3A22" stroke-width="5"></path><path d="M-8 -44 L 8 -44 L 0 -70 Z" fill="#A8B0BA" stroke="#0D0D0F" stroke-width="1.6"></path></g>' for x, a in [(w * 0.12, -10), (w * 0.18, 8), (w * 0.88, 6)])
    return (f'<circle cx="{f(w * 0.5)}" cy="{f(base - 70)}" r="{f(h * 0.5)}" fill="#FF8A3D" opacity="0.25"></circle>' + sparks
            + f'<path d="M-10 {f(base)} L {f(w + 10)} {f(base)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A1A14"></path>' + anvil + blade + hammer + tools)

def call_upon(p, w, h, seed):
    """Then began men to call upon the name of Jehovah: hands lifted under the stars, smoke going up."""
    base = h * 0.84
    up = [(-22, -158), (-30, -196), (-36, -232)]
    o = [mk.stars(70, w, h * 0.6, seed), V.rays(w * 0.5, -40, 30, 40, h * 1.4, color="#FFF4C2", op=0.14),
         hills(w, h, base, seed, color="#1A1430", amp=8),
         A4.altar(w * 0.5, base, 0.55, seed=seed)]
    for i, x in enumerate([0.14, 0.26, 0.38, 0.62, 0.74, 0.86]):
        o.append(mk.person(p, round(w * x), round(base + 2), 0.62 - abs(x - 0.5) * 0.2, body="#12090A", flip=x > 0.5, up=up))
    return "".join(o)

# ---- Genesis 5 ------------------------------------------------------------------------------------------
def generations(w, h, seed, n=10, hi=None):
    """The book of the generations: a column of linked nodes rising out of the dust into the stars."""
    r = random.Random(seed); o = [mk.stars(90, w, h, seed)]
    pts = [(w * (0.12 + 0.76 * i / (n - 1)), h * (0.72 - 0.4 * math.sin(i / (n - 1) * math.pi) * 0.6) + r.uniform(-10, 10)) for i in range(n)]
    o.append('<path d="M' + " L ".join(f"{f(x)} {f(y)}" for x, y in pts) + '" fill="none" stroke="#FFD23F" stroke-width="2.4" stroke-dasharray="6 5"></path>')
    for i, (x, y) in enumerate(pts):
        c = "#D7261E" if hi is not None and i == hi else "#FFD23F"
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="13" fill="#12113A" stroke="{c}" stroke-width="3"></circle><circle cx="{f(x)}" cy="{f(y)}" r="5" fill="{c}"></circle>')
    return "".join(o)

def enoch(p, w, h, seed):
    """Enoch walked with God: and he was not. A road going up into the light; his footprints stop."""
    r = random.Random(seed)
    o = [V.rays(w * 0.7, h * 0.12, 40, 30, w * 1.3, color="#FFF4C2", op=0.4),
         f'<circle cx="{f(w * 0.7)}" cy="{f(h * 0.12)}" r="{f(h * 0.16)}" fill="#FFF4C2"></circle>',
         f'<path d="M-10 {f(h + 10)} L {f(w * 0.2)} {f(h * 0.64)} C {f(w * 0.4)} {f(h * 0.6)} {f(w * 0.6)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.46)} L {f(w + 10)} {f(h + 10)} Z" fill="#5A4A6E" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.08)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.5)} {f(h * 0.66)} {f(w * 0.68)} {f(h * 0.5)}" fill="none" stroke="#C8B8D8" stroke-width="22" stroke-linecap="round" opacity="0.7"></path>']
    for i in range(7):
        t = i / 7; x = w * (0.12 + 0.44 * t); y = h * (0.96 - 0.38 * t)
        o.append(f'<ellipse cx="{f(x + (6 if i % 2 else -6))}" cy="{f(y)}" rx="{f(5 - t * 2.5)}" ry="{f(2.6 - t)}" fill="#3A2A4A"></ellipse>')
    o.append(f'<ellipse cx="{f(w * 0.6)}" cy="{f(h * 0.4)}" rx="{f(h * 0.12)}" ry="{f(h * 0.26)}" fill="#FFF4C2" opacity="0.7"></ellipse>')
    o.append(f'<g opacity="0.75">' + mk.person(p, round(w * 0.6), round(h * 0.55), fit(h * 0.55, h * 0.2), body="#4A3A6A", cloth="#6A5A8A", sw=2) + '</g>')
    o += [f'<circle cx="{f(w * 0.6 + r.uniform(-30, 50))}" cy="{f(h * 0.3 + r.uniform(-60, 40))}" r="{f(r.uniform(1, 3))}" fill="#FFF4C2"></circle>' for _ in range(30)]
    return "".join(o)

def lamech_noah(p, w, h):
    """Lamech holds up his son Noah at dawn over the cursed ground."""
    base = h * 0.86
    hold = [(-22, -158), (-14, -196), (6, -230)]
    return (V.rays(w * 0.5, base, 30, 30, w, color="#FFF4C2", op=0.3) + f'<circle cx="{f(w * 0.5)}" cy="{f(base)}" r="{f(h * 0.22)}" fill="#FFD23F"></circle>'
            + ground(w, h, base, "#6A4A3A", dy=0) + "".join(f'<path d="M{f(x)} {f(base + 14)} l 30 -3" stroke="#3A2A1A" stroke-width="3"></path>' for x in range(0, int(w), 50))
            + mk.person(p, round(w * 0.17), round(base), round(fit(base, h * 0.3) * 200 / 262, 3), body=SKIN, cloth="#1F7A8C", sw=3, up=hold, extra=R.baby(16, -244, 0.8)))

def noah_and_sons(p, w, h, top=0.34):
    base = h * 0.86
    return (V.rays(w * 0.5, base, 30, 30, w, color="#FFF4C2", op=0.25)
            + hills(w, h, base, 7, color="#2A3A1E", amp=6)
            + noah(p, w * 0.22, base, fit(base, h * top))
            + son(p, w * 0.46, base, fit(base, h * (top + 0.04)), "shem", flip=True)
            + son(p, w * 0.62, base, fit(base, h * (top + 0.06)), "ham", flip=True)
            + son(p, w * 0.78, base, fit(base, h * (top + 0.08)), "japheth", flip=True))

# ---- Genesis 6 ------------------------------------------------------------------------------------------
def multitude(p, w, h, seed):
    """Men multiplying on the face of the ground: a crowd, the daughters of men in bright robes."""
    r = random.Random(seed); o = [city(w * 0.82, h * 0.6, w * 0.3, h * 0.36, seed), ground(w, h, h * 0.6, "#C8A06A", dy=-2)]
    items = sorted((r.uniform(h * 0.66, h * 1.02), r.uniform(-10, w + 10)) for _ in range(26))
    for y, x in items:
        s = 0.22 + 0.5 * (y - h * 0.62) / (h * 0.4)
        if r.random() < 0.4: o.append(wife(p, x, y, s, r.choice(WIVES + ["#E8E2D6"]), flip=r.random() < 0.5))
        else: o.append(mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=r.choice(["#3A2214", "#4A3A6A", "#2A1A10", "#5A3A22"]), kind="Tunic", flip=r.random() < 0.5))
    return "".join(o)

def nephilim(p, w, h, seed):
    """The Nephilim in the earth: giants in brass, the mighty men that were of old, towering over men."""
    base = h * 0.88
    o = [V.rays(w * 0.5, base, 30, 40, w, color="#FF8A3D", op=0.25), hills(w, h, base, seed, color="#2A1A2E", amp=6),
         A2.goliath(p, w * 0.64, base, fit(base, h * 0.14)), A2.goliath(p, w * 0.86, base, fit(base, h * 0.2), flip=True, shield=False)]
    for x in (0.06, 0.14, 0.22, 0.44, 0.52, 0.96):
        o.append(mk.person(p, round(w * x), round(base + 2), round(h / 900, 3), body="#12090A", flip=x > 0.5))
    return "".join(o)

def violence(w, h, seed):
    """The earth filled with violence: a burning plain, broken spears, smoke."""
    r = random.Random(seed); base = h * 0.7
    o = [ground(w, h, base, "#3A2A2A", dy=-4)]
    for _ in range(5):
        x = r.uniform(0.05, 0.95) * w
        o.append(E.blaze(x, base + r.uniform(4, 30), r.uniform(30, 60), r.uniform(50, 100), r.randint(1, 99)))
        o.append(f'<path d="M{f(x)} {f(base - 60)} C {f(x - 40)} {f(base - 140)} {f(x + 30)} {f(base - 200)} {f(x - 10)} {f(-20)}" fill="none" stroke="#5A4A5A" stroke-width="26" opacity="0.4" stroke-linecap="round"></path>')
    o.append(A2.spears_down([w * x for x in (0.2, 0.34, 0.58, 0.8)], base + 30, seed))
    return "".join(o)

def noah_kneels(p, w, h):
    base = h * 0.88
    return (V.rays(w * 0.5, -40, 40, 40, h * 1.6, color="#FFF4C2", op=0.25) + mk.stars(60, w, h * 0.7, 61)
            + ground(w, h, base, "#1A1430", dy=0)
            + E.kneel(w * 0.82, base + 2, round(h / 520, 3), color=NOAH_ROBE, skin="#5A2A16"))

def ark_hull(x, base, w, h, uid, door=True, open_=False, roof=True, light=True, covered=True):
    """The ark from the side: a long box of gopher wood, three stories, a light a cubit under the roof, a door in the side."""
    o = [f'<rect x="{f(x)}" y="{f(base - h)}" width="{f(w)}" height="{f(h)}" fill="#7A4A26" stroke="#0D0D0F" stroke-width="2.6"></rect>']
    for k in range(1, 3):
        o.append(f'<path d="M{f(x)} {f(base - h * k / 3)} L {f(x + w)} {f(base - h * k / 3)}" stroke="#3A2214" stroke-width="3"></path>')
    for k in range(1, 9):
        o.append(f'<path d="M{f(x)} {f(base - h * (k / 9))} L {f(x + w)} {f(base - h * (k / 9))}" stroke="#5A3418" stroke-width="1" opacity="0.6"></path>')
    if light:
        o.append(f'<rect x="{f(x + w * 0.04)}" y="{f(base - h - h * 0.12)}" width="{f(w * 0.92)}" height="{f(h * 0.12)}" fill="#FFD23F" stroke="#0D0D0F" stroke-width="2"></rect>')
        o += [f'<path d="M{f(x + w * 0.04 + i * w * 0.0575)} {f(base - h - h * 0.12)} l 0 {f(h * 0.12)}" stroke="#5A3418" stroke-width="3"></path>' for i in range(17)]
    if roof and covered:
        o.append(f'<path d="M{f(x - w * 0.02)} {f(base - h - h * 0.12)} L {f(x + w * 0.5)} {f(base - h - h * 0.34)} L {f(x + w * 1.02)} {f(base - h - h * 0.12)} Z" fill="#5A3418" stroke="#0D0D0F" stroke-width="2.6"></path>')
    if door:
        dx = x + w * 0.58; dw = w * 0.08
        if open_:
            o.append(f'<rect x="{f(dx)}" y="{f(base - h * 0.62)}" width="{f(dw)}" height="{f(h * 0.3)}" fill="#FFC14D" stroke="#0D0D0F" stroke-width="2"></rect>')
        else:
            o.append(f'<rect x="{f(dx)}" y="{f(base - h * 0.62)}" width="{f(dw)}" height="{f(h * 0.3)}" fill="#5A3418" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    return "".join(o)

def ark_ramp(p, w, h, seed, people=True):
    """The ark on dry ground with its door open and a ramp; Noah's house going up."""
    base = h * 0.8; ax, aw, ah = w * 0.2, w * 0.76, h * 0.42
    dx = ax + aw * 0.58; dy = base - ah * 0.32
    o = [ground(w, h, base, "#8A9A5A", dy=0), ark_hull(ax, base, aw, ah, "ar", open_=True),
         f'<path d="M{f(dx)} {f(dy)} L {f(dx + aw * 0.08)} {f(dy)} L {f(w * 0.32)} {f(base + 30)} L {f(w * 0.12)} {f(base + 30)} Z" fill="#9A6A3A" stroke="#0D0D0F" stroke-width="2"></path>']
    return "".join(o)

def pairs(p, w, h, seed, base_k=0.86, sky=True):
    """Two and two, male and female: lions, camels, kine, sheep, asses, foxes, horses, serpents and birds of every sort.
    The seed picks the order of the kinds and the way they walk, so no two panels are the same."""
    r = random.Random(seed); base = h * base_k; fl = r.random() < 0.5
    kinds = [lambda x, y, k: G1.camel(x, y - 6, 0.34 * k, flip=fl), lambda x, y, k: S.lion(x, y + 4, 0.34 * k, flip=fl, roar=False),
             lambda x, y, k: A.cow(x, y + 6, 0.3 * k, color=r.choice(["#8A5A30", "#C9A27A"]), flip=fl), lambda x, y, k: E.sheep(x, y + 10, 0.36 * k, flip=fl),
             lambda x, y, k: N.ass(x, y + 8, 0.2 * k, flip=fl), lambda x, y, k: S.fox(x, y + 14, 0.28 * k, flip=fl, brand=False),
             lambda x, y, k: E3.horse(x, y + 6, 0.3 * k, color=r.choice(["#3A2214", "#8A6A4A"]), flip=fl)]
    r.shuffle(kinds); kinds = kinds[:6]
    o = [ground(w, h, base - 10, "#B5A06A", dy=0)] if sky else []
    for i, kd in enumerate(kinds):
        x = w * (0.08 + i * 0.165)
        o.append(kd(x, base, 1.0)); o.append(kd(x + w * 0.065, base + 4, 0.9))
    sx = w * r.uniform(0.2, 0.7)
    o.append(SN.snake([(sx, base + 30), (sx + 14, base + 25), (sx + 28, base + 31), (sx + 42, base + 27)], 1.8, f"pa{seed}", head_scale=0.45))
    o.append(SN.snake([(sx + 60, base + 34), (sx + 72, base + 29), (sx + 84, base + 35), (sx + 96, base + 31)], 1.6, f"pb{seed}", head_scale=0.4))
    o.append(birds(16, w * 0.05, w * 0.95, h * 0.08, h * 0.4, seed))
    return "".join(o)

def provisions(w, h, seed):
    """All food that is eaten, gathered: sacks of grain, baskets, heaps, jars."""
    r = random.Random(seed); base = h * 0.86
    o = [ground(w, h, base, "#8A6A4A", dy=0), R.heap(w * 0.3, base + 4, w * 0.4, h * 0.26)]
    o += [R.sack(w * x, base + 8, 1.1) for x in (0.62, 0.72, 0.82)]
    o += [E4.basket(w * x, base + 14, 1.6) for x in (0.12, 0.5, 0.92)]
    o += [f'<g transform="translate({f(w * x)} {f(base + 4)})"><path d="M-14 0 C -22 -20 -18 -40 -8 -44 L -8 -52 L 8 -52 L 8 -44 C 18 -40 22 -20 14 0 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path></g>' for x in (0.67, 0.77)]
    return "".join(o)

def clean_sevens(w, h, seed):
    """Clean beasts by sevens and the birds of the heavens by sevens."""
    r = random.Random(seed); base = h * 0.8
    o = [ground(w, h, base, "#7A9A4A", dy=-4)]
    items = sorted((r.uniform(base + 6, h * 1.02), r.uniform(0, w)) for _ in range(14))
    for y, x in items:
        k = (y - base) / (h - base)
        o.append(E.sheep(x, y, 0.28 + 0.24 * k, flip=r.random() < 0.5) if r.random() < 0.7 else A.cow(x, y, 0.2 + 0.18 * k, color=r.choice(["#8A5A30", "#C9A27A"]), flip=r.random() < 0.5))
    o.append(birds(14, w * 0.05, w * 0.95, h * 0.08, h * 0.5, seed + 1))
    return "".join(o)

def storm_land(w, h, seed):
    """Seven days yet: black cloud coming over the land."""
    r = random.Random(seed); base = h * 0.84
    clouds = "".join(f'<ellipse cx="{f(r.uniform(-40, w + 40))}" cy="{f(r.uniform(-10, h * 0.4))}" rx="{f(r.uniform(80, 160))}" ry="{f(r.uniform(30, 60))}" fill="{r.choice(["#1A1A2E", "#2A2A40", "#12121E"])}" stroke="#0D0D0F" stroke-width="2"></ellipse>' for _ in range(16))
    return (hills(w, h, base, seed, color="#2A3A2E", amp=10) + clouds + E2.bolt(w * 0.66, h * 0.2, h * 0.6, seed)
            + "".join(f'<path d="M{f(x)} {f(h * 0.4)} l -18 {f(h * 0.5)}" stroke="#8FD0E2" stroke-width="1.4" opacity="0.5"></path>' for x in range(0, int(w) + 40, 24)))

def ark_lightning(w, h, seed):
    return storm_land(w, h, seed)

def rain(w, h, seed):
    r = random.Random(seed)
    return "".join(f'<path d="M{f(r.uniform(0, w + 60))} {f(r.uniform(-20, h))} l -10 40" stroke="#CFEFFF" stroke-width="{f(r.uniform(1, 2.4))}" opacity="0.7"></path>' for _ in range(160))

def sea(w, h, y, seed, color="#1F6F9A", deep="#0B2E4A", foam="#CFEFFF", amp=10):
    r = random.Random(seed)
    d = f"M-10 {f(y)} " + " ".join(f"Q {f(x + 30)} {f(y - amp - r.uniform(0, amp))} {f(x + 60)} {f(y + r.uniform(-3, 3))}" for x in range(-10, int(w) + 60, 60)) + f" L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z"
    lines = "".join(f'<path d="M{f(r.uniform(-20, w))} {f(r.uniform(y + 14, h))} c 20 -6 40 6 60 0" fill="none" stroke="{foam}" stroke-width="2" opacity="0.5"></path>' for _ in range(int(w / 30)))
    return f'<path d="{d}" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path><rect x="-10" y="{f(y + (h - y) * 0.55)}" width="{f(w + 20)}" height="{f(h)}" fill="{deep}" opacity="0.35"></rect>' + lines

def ark_afloat(x, y, w, uid):
    """The ark riding the water (hull partly sunk below the waterline y)."""
    h = w * 0.18
    return ark_hull(x, y + h * 0.35, w, h, uid, door=False)

def high_waters(w, h, seed):
    """The waters prevailed: the ark high on a swell, the last peak going under."""
    y = h * 0.64
    peak = f'<path d="M{f(w * 0.72)} {f(y + 30)} L {f(w * 0.84)} {f(y - 20)} L {f(w * 0.96)} {f(y + 30)} Z" fill="#5A4A4E" stroke="#0D0D0F" stroke-width="2"></path>'
    return (f'<rect x="-10" y="-10" width="{w + 20}" height="{h + 20}" fill="#5E6E8A"></rect>' + rain(w, h * 0.7, seed) + peak
            + sea(w, h, y, seed, amp=14) + ark_afloat(w * 0.28, y - 10, w * 0.3, "hw"))

def under_the_flood(w, h, seed):
    """Fifteen cubits upward: under the surface, the drowned hills, trees and towers of the world that was."""
    r = random.Random(seed); y = h * 0.16
    o = [f'<rect x="-10" y="-10" width="{w + 20}" height="{f(y + 10)}" fill="#3A4A5E"></rect>',
         f'<rect x="-10" y="{f(y)}" width="{w + 20}" height="{f(h)}" fill="#0F3A5A"></rect>',
         f'<rect x="-10" y="{f(h * 0.6)}" width="{w + 20}" height="{f(h)}" fill="#071E33" opacity="0.6"></rect>',
         hills(w, h, h * 0.72, seed, color="#12283A", amp=40, step=90),
         f'<g opacity="0.55">' + city(w * 0.7, h * 0.8, w * 0.3, h * 0.4, seed, color="#163248", lit="#2A5A7A") + '</g>']
    for x in (0.12, 0.3, 0.46):
        o.append(f'<g opacity="0.5">' + J.oak(w * x, h * 0.78, 0.7, seed=int(x * 100)) + '</g>')
    o += [f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(y + 20, h))}" r="{f(r.uniform(1.5, 4))}" fill="none" stroke="#9FD8E8" stroke-width="1.2" opacity="0.6"></circle>' for _ in range(40)]
    o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#CFEFFF" stroke-width="3"></path>')
    o.append(f'<path d="M{f(w * 0.36)} {f(y + 18)} L {f(w * 0.64)} {f(y + 18)} L {f(w * 0.66)} {f(y)} L {f(w * 0.34)} {f(y)} Z" fill="#5A3418" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.06)} {f(h * 0.4)} L {f(w * 0.06)} {f(h * 0.4 - (h * 0.24))}" stroke="#FFD23F" stroke-width="2"></path>')
    return "".join(o)

def lone_ark(w, h, seed):
    """Noah only was left: the ark alone on the waters under the stars."""
    y = h * 0.62
    return (mk.stars(120, w, y, seed) + f'<circle cx="{f(w * 0.8)}" cy="{f(h * 0.2)}" r="16" fill="#E8E2D6"></circle>'
            + sea(w, h, y, seed, color="#12305A", deep="#05101F", foam="#8FB8D8", amp=4) + ark_afloat(w * 0.42, y - 4, w * 0.16, "la")
            + f'<rect x="{f(w * 0.5)}" y="{f(y - w * 0.16 * 0.18 + 2)}" width="4" height="4" fill="#FFD23F"></rect>')

def parting(w, h, seed):
    """The windows of heaven stopped: the clouds breaking, light on the waters."""
    r = random.Random(seed); y = h * 0.66
    clouds = "".join(f'<ellipse cx="{f(x)}" cy="{f(r.uniform(10, h * 0.3))}" rx="{f(r.uniform(70, 130))}" ry="{f(r.uniform(24, 44))}" fill="#4A5A72" stroke="#0D0D0F" stroke-width="2"></ellipse>' for x in [w * 0.05, w * 0.2, w * 0.8, w * 0.95, w * 0.1, w * 0.9])
    return (V.rays(w * 0.5, h * 0.05, 26, 20, h * 1.3, color="#FFF4C2", op=0.45) + clouds + sea(w, h, y, seed, color="#2C7DA0", amp=6))

def peaks(w, h, seed):
    """The tops of the mountains seen."""
    r = random.Random(seed); y = h * 0.66; o = []
    for x in (0.08, 0.24, 0.42, 0.6, 0.78, 0.94):
        pw = r.uniform(60, 110); ph = r.uniform(20, 60)
        o.append(f'<path d="M{f(w * x - pw)} {f(y + 10)} L {f(w * x - pw * 0.2)} {f(y - ph)} L {f(w * x)} {f(y - ph * 0.8)} L {f(w * x + pw)} {f(y + 10)} Z" fill="#6A5A4E" stroke="#0D0D0F" stroke-width="2"></path>')
    return (V.rays(w * 0.5, h * 0.9, 30, 30, w, color="#FFF4C2", op=0.25) + "".join(o) + sea(w, h, y, seed, color="#2C7DA0", amp=4))

def ark_window(w, h, tok=NOAH, open_=True, dove=None):
    """Noah at the window of the ark."""
    wx, wy, ww, wh = w * 0.22, h * 0.14, w * 0.56, h * 0.72
    planks = "".join(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#4A2A12" stroke-width="2"></path>' for y in range(0, int(h) + 20, 22))
    inner = mk.face(tok, wx + ww * 0.05, wy + wh * 0.06, wh / 400)
    return (f'<rect x="-10" y="-10" width="{w + 20}" height="{h + 20}" fill="#7A4A26"></rect>' + planks
            + f'<rect x="{f(wx - 10)}" y="{f(wy - 10)}" width="{f(ww + 20)}" height="{f(wh + 20)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="3"></rect>'
            + f'<svg x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}" viewBox="{f(wx)} {f(wy)} {f(ww)} {f(wh)}"><rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}" fill="#12090A"></rect>{inner}</svg>'
            + (f'<path d="M{f(wx + ww)} {f(wy)} L {f(wx + ww + 40)} {f(wy - 14)} L {f(wx + ww + 40)} {f(wy + wh + 14)} L {f(wx + ww)} {f(wy + wh)} Z" fill="#5A3418" stroke="#0D0D0F" stroke-width="2.4"></path>' if open_ else "")
            + (dove or ""))

def dove(x, y, s=1.0, flip=False, leaf=False, wings="up"):
    sx = -s if flip else s
    wing = ('<path d="M-4 -6 C 0 -40 20 -54 36 -58 C 28 -40 22 -20 12 -4 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></path>' if wings == "up"
            else '<path d="M-4 -4 C 4 10 20 18 34 20 C 24 8 18 0 12 -4 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></path>')
    lf = '<path d="M40 -6 C 50 -14 60 -12 64 -6 C 56 -2 48 -2 40 -6 Z" fill="#5E8F26" stroke="#0D0D0F" stroke-width="1.4"></path>' if leaf else ""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            '<path d="M-36 -2 L -22 -10 C -8 -16 16 -14 30 -8 C 36 -6 40 -4 42 -2 L 34 0 C 20 6 -8 8 -22 4 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></path>'
            f'{wing}<circle cx="30" cy="-6" r="1.8" fill="#0D0D0F"></circle><path d="M40 -4 L 46 -2 L 40 0 Z" fill="#E8A317"></path>{lf}</g>')

def dove_out(w, h, seed):
    """The dove sent forth over the waters from the side of the ark."""
    y = h * 0.7
    return (sea(w, h, y, seed, color="#2C7DA0", amp=6) + ark_hull(-w * 0.6, y + 40, w * 0.9, h * 0.6, "do", door=False, roof=True)
            + f'<rect x="{f(w * 0.12)}" y="{f(y - h * 0.62)}" width="{f(w * 0.12)}" height="{f(h * 0.12)}" fill="#12090A" stroke="#0D0D0F" stroke-width="2"></rect>'
            + dove(w * 0.6, h * 0.3, 1.3) + f'<path d="M{f(w * 0.26)} {f(h * 0.3)} C {f(w * 0.36)} {f(h * 0.36)} {f(w * 0.44)} {f(h * 0.3)} {f(w * 0.5)} {f(h * 0.3)}" fill="none" stroke="#F3EFE6" stroke-width="2" stroke-dasharray="5 5"></path>')

def hand_dove(w, h, seed):
    """He put forth his hand, and took her: Noah's hand out of the window, the dove coming down onto it."""
    planks = "".join(f'<path d="M-10 {f(y)} L {f(w * 0.36)} {f(y)}" stroke="#4A2A12" stroke-width="2"></path>' for y in range(0, int(h) + 20, 22))
    return (sea(w, h, h * 0.78, seed, color="#2C7DA0", amp=5) + f'<rect x="-10" y="-10" width="{f(w * 0.36 + 10)}" height="{h + 20}" fill="#7A4A26" stroke="#0D0D0F" stroke-width="2.6"></rect>' + planks
            + f'<rect x="{f(w * 0.2)}" y="{f(h * 0.36)}" width="{f(w * 0.16)}" height="{f(h * 0.3)}" fill="#12090A" stroke="#0D0D0F" stroke-width="2"></rect>'
            + f'<path d="M{f(w * 0.3)} {f(h * 0.5)} L {f(w * 0.49)} {f(h * 0.5)}" stroke="#0D0D0F" stroke-width="24" stroke-linecap="round"></path><path d="M{f(w * 0.3)} {f(h * 0.5)} L {f(w * 0.49)} {f(h * 0.5)}" stroke="{NOAH_ROBE}" stroke-width="19" stroke-linecap="round"></path>'
            + f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.5)}" rx="13" ry="10" fill="#C98E66" stroke="#0D0D0F" stroke-width="2"></ellipse>'
            + f'<path d="M{f(w * 0.5 + 4)} {f(h * 0.5 - 8)} l 6 -12 M{f(w * 0.5 + 10)} {f(h * 0.5 - 4)} l 10 -8" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path>'
            + f'<path d="M{f(w * 0.5 + 4)} {f(h * 0.5 - 8)} l 6 -12 M{f(w * 0.5 + 10)} {f(h * 0.5 - 4)} l 10 -8" stroke="#C98E66" stroke-width="4" stroke-linecap="round"></path>'
            + dove(w * 0.5 + 30, h * 0.5 - 26, 1.1, flip=True, wings="up"))

def dove_away(w, h, seed):
    """She returned not again: a speck of white over the waters, toward a green shore."""
    y = h * 0.66
    return (f'<path d="M{f(w * 0.6)} {f(y + 6)} C {f(w * 0.7)} {f(y - 24)} {f(w * 0.9)} {f(y - 30)} {f(w + 10)} {f(y - 20)} L {f(w + 10)} {f(y + 6)} Z" fill="#5E8F26" stroke="#0D0D0F" stroke-width="2"></path>'
            + J.oak(w * 0.86, y - 18, 0.32, seed=3) + sea(w, h, y, seed, color="#2C7DA0", amp=4) + dove(w * 0.7, h * 0.3, 0.45))

def ark_roof(p, w, h, seed):
    """Noah removed the covering of the ark and looked: the face of the ground dried."""
    base = h * 0.7
    o = [V.rays(w * 0.2, h * 0.1, 30, 30, w * 1.2, color="#FFF4C2", op=0.35),
         hills(w, h, h * 0.62, seed, color="#8A9A5A", amp=10, step=80),
         ark_hull(w * 0.3, base + h * 0.3, w * 0.8, h * 0.28, "rf", door=False, light=False, roof=False)]
    o += [f'<path d="M{f(w * 0.3 + i * 40)} {f(base + h * 0.02)} l 30 -30" stroke="#5A3418" stroke-width="6"></path>' for i in range(4)]
    o.append(noah(p, w * 0.78, base + h * 0.02, fit(base, h * 0.36), flip=True, up=[(-22, -158), (-40, -176), (-30, -196)]))
    return "".join(o)

def dry_ground(w, h, seed):
    """The earth dry: cracked mud, the sun high."""
    r = random.Random(seed); base = h * 0.5
    cr = "".join(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-20, 20))} {f(r.uniform(6, 16))} l {f(r.uniform(-14, 14))} {f(r.uniform(6, 14))}" fill="none" stroke="#6A4A3A" stroke-width="1.8"></path>'
                 for x, y in [(r.uniform(0, w), r.uniform(base + 10, h)) for _ in range(30)])
    return (f'<circle cx="{f(w * 0.75)}" cy="{f(h * 0.2)}" r="26" fill="#FFD23F"></circle>' + V.rays(w * 0.75, h * 0.2, 24, 34, w, color="#FFF4C2", op=0.4)
            + ground(w, h, base, "#C8A06A", dy=0) + cr)

def go_forth(p, w, h, seed):
    """Every beast, every creeping thing and every bird going forth out of the ark, down the mountain."""
    base = h * 0.9
    mt = f'<path d="M-10 {f(h * 0.4)} L {f(w * 0.3)} {f(h * 0.3)} L {f(w * 0.7)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.82)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A7A4A" stroke="#0D0D0F" stroke-width="2"></path>'
    return (V.rays(w * 0.9, h * 0.1, 30, 30, w, color="#FFF4C2", op=0.3) + mt + ark_hull(w * 0.02, h * 0.36, w * 0.32, h * 0.12, "gf", door=True, open_=True, light=False)
            + family8(p, w * 0.36, w * 0.62, h * 0.58, round(h / 900, 3), flip=False)
            + G1.camel(w * 0.68, h * 0.72, 0.24) + S.lion(w * 0.78, h * 0.8, 0.26, roar=False) + E.sheep(w * 0.86, h * 0.86, 0.3) + A.cow(w * 0.94, h * 0.9, 0.22)
            + birds(14, w * 0.3, w * 0.98, h * 0.05, h * 0.35, seed))

def noah_altar(p, w, h, seed):
    """Noah builded an altar unto Jehovah, and offered burnt-offerings."""
    base = h * 0.86
    return (V.rays(w * 0.5, base - h * 0.4, 36, 30, w, color="#FFF4C2", op=0.3)
            + ground(w, h, base, "#5E7A3A", dy=0) + A4.altar(w * 0.56, base, round(h / 420, 3), seed=seed)
            + E.kneel(w * 0.3, base + 2, round(h / 330, 3), color=NOAH_ROBE, skin=SKIN)
            + "".join(son(p, w * x, base + 2, round(h / 520, 3), k, flip=True) for x, k in [(0.78, "shem"), (0.86, "ham"), (0.94, "japheth")]))

def seasons(w, h, seed):
    """Seedtime and harvest, cold and heat, summer and winter, day and night: eight narrow bands."""
    r = random.Random(seed)
    bands = [("#5E8F26", "seed"), ("#E8A317", "harvest"), ("#8FD0E2", "cold"), ("#D7261E", "heat"),
             ("#FFD23F", "summer"), ("#C8D0DE", "winter"), ("#FFF4C2", "day"), ("#12113A", "night")]
    bw = w / len(bands); o = []
    for i, (c, k) in enumerate(bands):
        x = i * bw; cx = x + bw / 2
        o.append(f'<rect x="{f(x)}" y="-10" width="{f(bw)}" height="{h + 20}" fill="{c}" stroke="#0D0D0F" stroke-width="2"></rect>')
        if k == "seed": o.append(f'<path d="M{f(cx)} {f(h * 0.7)} L {f(cx)} {f(h * 0.5)} M{f(cx)} {f(h * 0.58)} C {f(cx - 14)} {f(h * 0.52)} {f(cx - 18)} {f(h * 0.5)} {f(cx - 20)} {f(h * 0.48)} M{f(cx)} {f(h * 0.54)} C {f(cx + 14)} {f(h * 0.48)} {f(cx + 18)} {f(h * 0.46)} {f(cx + 20)} {f(h * 0.44)}" fill="none" stroke="#F3EFE6" stroke-width="3"></path>')
        if k == "harvest": o.append(G1.wheat(cx, h * 0.8, 0.8, seed=seed))
        if k == "cold" or k == "winter":
            o += [f'<g transform="translate({f(cx + r.uniform(-20, 20))} {f(r.uniform(h * 0.1, h * 0.9))})" stroke="#F3EFE6" stroke-width="2"><path d="M-6 0 L 6 0 M0 -6 L 0 6 M-4 -4 L 4 4 M-4 4 L 4 -4"></path></g>' for _ in range(5)]
        if k == "heat": o.append(E.blaze(cx, h * 0.8, 30, 60, seed))
        if k == "summer": o.append(f'<circle cx="{f(cx)}" cy="{f(h * 0.4)}" r="18" fill="#FF8A3D" stroke="#0D0D0F" stroke-width="2"></circle>')
        if k == "day": o.append(V.rays(cx, h * 0.4, 12, 10, 40, color="#E8A317", op=0.7) + f'<circle cx="{f(cx)}" cy="{f(h * 0.4)}" r="10" fill="#FFD23F" stroke="#0D0D0F" stroke-width="2"></circle>')
        if k == "night": o.append(mk.stars(12, bw, h, seed).replace("<g ", f'<g transform="translate({f(x)} 0)" ', 1) + f'<circle cx="{f(cx)}" cy="{f(h * 0.4)}" r="10" fill="#E8E2D6"></circle><circle cx="{f(cx - 5)}" cy="{f(h * 0.4 - 3)}" r="9" fill="#12113A"></circle>')
    return "".join(o)

# ---- Genesis 9 ------------------------------------------------------------------------------------------
def dominion(w, h, seed):
    """The fear and the dread of you upon every beast, bird and fish: they flee and scatter."""
    y = h * 0.62
    return (ground(w, h * 0.7, h * 0.4, "#7A9A4A", dy=0)
            + S.lion(w * 0.2, h * 0.58, 0.32, flip=True, roar=False) + N.ass(w * 0.36, h * 0.6, 0.18, flip=True) + E.sheep(w * 0.5, h * 0.6, 0.34, flip=True)
            + birds(12, w * 0.1, w * 0.9, h * 0.05, h * 0.3, seed)
            + sea(w, h, y, seed, color="#2C7DA0", amp=4) + "".join(E2.fish(w * x, h * yy, 0.7, rot=0) for x, yy in [(0.2, 0.8), (0.45, 0.88), (0.7, 0.78), (0.85, 0.9)]))

def green_herb(w, h, seed):
    """As the green herb have I given you all."""
    base = h * 0.8
    return ground(w, h, base, "#5E7A3A", dy=0) + S.grain(-10, w + 10, base + 6, h * 0.36, seed) + J.oak(w * 0.8, base, 0.5, seed=seed)

def blood_drop(w, h):
    """The life thereof, which is the blood thereof."""
    return (V.rays(w * 0.5, h * 0.5, 26, 20, w, color="#D7261E", op=0.25)
            + f'<path d="M{f(w * 0.5)} {f(h * 0.16)} C {f(w * 0.5 + 12)} {f(h * 0.38)} {f(w * 0.5 + 44)} {f(h * 0.52)} {f(w * 0.5 + 44)} {f(h * 0.66)} C {f(w * 0.5 + 44)} {f(h * 0.82)} {f(w * 0.5 - 44)} {f(h * 0.82)} {f(w * 0.5 - 44)} {f(h * 0.66)} C {f(w * 0.5 - 44)} {f(h * 0.52)} {f(w * 0.5 - 12)} {f(h * 0.38)} {f(w * 0.5)} {f(h * 0.16)} Z" fill="#D7261E" stroke="#0D0D0F" stroke-width="3"></path>'
            + f'<path d="M{f(w * 0.5 - 22)} {f(h * 0.62)} C {f(w * 0.5 - 22)} {f(h * 0.54)} {f(w * 0.5 - 14)} {f(h * 0.48)} {f(w * 0.5 - 8)} {f(h * 0.44)}" fill="none" stroke="#FF8A8A" stroke-width="5" stroke-linecap="round"></path>')

def image_of_god(p, w, h):
    """In the image of God made he man: a man standing in light."""
    base = h * 0.9
    return (V.rays(w * 0.5, base - h * 0.4, 40, 30, w * 1.2, color="#FFF4C2", op=0.4) + f'<circle cx="{f(w * 0.5)}" cy="{f(base - h * 0.4)}" r="{f(h * 0.22)}" fill="#FFF4C2" opacity="0.6"></circle>'
            + ground(w, h, base, "#2A1A2E", dy=0) + mk.person(p, round(w * 0.5), round(base), fit(base, h * 0.42), body="#12090A"))

def covenant_sky(w, h, seed, k=1.0):
    """The bow in the cloud: a full arch of six colors standing on a bank of dark cloud."""
    r = random.Random(seed); cx, cy = w * 0.5, h * 0.98; R0 = min(w * 0.46, h * 0.8) * k
    cols = ["#D7261E", "#FF8A3D", "#FFD23F", "#5E8F26", "#1F5FAD", "#7A3BA8"]
    bw = R0 * 0.06
    bow = "".join(f'<path d="M{f(cx - (R0 - i * bw))} {f(cy)} A {f(R0 - i * bw)} {f(R0 - i * bw)} 0 0 1 {f(cx + (R0 - i * bw))} {f(cy)}" fill="none" stroke="{c}" stroke-width="{f(bw)}" opacity="0.95"></path>' for i, c in enumerate(cols))
    clouds = "".join(f'<ellipse cx="{f(r.uniform(-20, w + 20))}" cy="{f(r.uniform(h * 0.86, h * 1.04))}" rx="{f(r.uniform(50, 110))}" ry="{f(r.uniform(18, 34))}" fill="{r.choice(["#3A4A6A", "#4A5A7A", "#2A3A5A"])}" stroke="#0D0D0F" stroke-width="2"></ellipse>' for _ in range(12))
    return bow + clouds

def all_flesh(p, w, h, seed):
    """Every living creature of all flesh, and the ark empty on the mountain behind, under the bow."""
    base = h * 0.86
    return (covenant_sky(w, h * 0.86, seed) + ground(w, h, base - 10, "#5E8F26", dy=0)
            + family8(p, w * 0.08, w * 0.42, base, fit(base, h * 0.66), flip=True)
            + G1.camel(w * 0.52, base - 6, 0.26) + S.lion(w * 0.62, base, 0.28, roar=False) + A.cow(w * 0.72, base + 2, 0.24, color="#8A5A30")
            + E.sheep(w * 0.8, base + 4, 0.3) + N.ass(w * 0.9, base + 4, 0.16) + birds(10, w * 0.4, w * 0.95, h * 0.1, h * 0.4, seed))

def vineyard(p, w, h, seed):
    """Noah a husbandman, planting a vineyard: rows of vines on stakes, grapes."""
    base = h * 0.84; r = random.Random(seed); o = [ground(w, h, base, "#8A6A4A", dy=-4)]
    for row in range(2):
        for i in range(6):
            x = w * (0.08 + i * 0.12) + row * 30; y = base + 8 + row * 26
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 70)}" stroke="#5A3A22" stroke-width="4"></path>'
                     f'<path d="M{f(x - 30)} {f(y - 50)} C {f(x - 10)} {f(y - 70)} {f(x + 10)} {f(y - 40)} {f(x + 30)} {f(y - 60)}" fill="none" stroke="#3F6A2A" stroke-width="5"></path>')
            if r.random() < 0.7: o.append(N.grapes(x + r.uniform(-14, 14), y - 46, 0.32, seed=i + row))
    o.append(noah(p, w * 0.84, base + 6, round(h / 300, 3), flip=True, up=[(-22, -158), (-40, -120), (-58, -90)]))
    return "".join(o)

def tent_night(w, h, seed):
    """His tent at night, its door shut, a lamp low within; a cup upon the ground."""
    base = h * 0.84
    return (mk.stars(80, w, h * 0.6, seed) + f'<circle cx="{f(w * 0.15)}" cy="{f(h * 0.18)}" r="14" fill="#E8E2D6"></circle>'
            + ground(w, h, base, "#1A1430", dy=0) + G1.tent_big(w * 0.55, base, w * 0.5, h * 0.56, color="#3A2214", open_=True, glow="#5A2A12")
            + f'<g transform="translate({f(w * 0.86)} {f(base + 10)}) rotate(80)"><path d="M-10 -16 L 10 -16 L 6 -2 L 2 0 L 2 8 L 8 10 L -8 10 L -2 8 L -2 0 L -6 -2 Z" fill="#C9A86A" stroke="#0D0D0F" stroke-width="1.6"></path></g>'
            + f'<path d="M{f(w * 0.86)} {f(base + 12)} c 10 4 24 2 30 6" fill="none" stroke="#7A1E3A" stroke-width="4" stroke-linecap="round"></path>')

def garment_backward(p, w, h, seed):
    """Shem and Japheth go backward toward the tent with a garment laid upon both their shoulders; Ham stands apart."""
    base = h * 0.88
    tent = G1.tent_big(w * 0.16, base, w * 0.3, h * 0.58, color="#3A2214", open_=True, glow="#2A1408")
    s = fit(base, h * 0.42); ax = w * 0.42; bx = w * 0.56
    top, low = base - 156 * s, base - 70 * s
    cloak = (f'<path d="M{f(ax - 4)} {f(top)} C {f(ax + 30)} {f(top - 6)} {f(bx - 30)} {f(top - 6)} {f(bx + 4)} {f(top)} '
             f'L {f(bx + 8)} {f(low)} C {f(bx - 30)} {f(low + 16)} {f(ax + 30)} {f(low + 16)} {f(ax - 8)} {f(low)} Z" fill="#E2D8C4" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + "".join(f'<path d="M{f(ax + (bx - ax) * t)} {f(top + 4)} L {f(ax + (bx - ax) * t + 4)} {f(low + 10)}" stroke="#B8AE9E" stroke-width="2"></path>' for t in (0.3, 0.5, 0.7)))
    arrows = f'<path d="M{f(ax - 30)} {f(base + 14)} L {f(ax - 80)} {f(base + 14)} M{f(ax - 70)} {f(base + 6)} L {f(ax - 82)} {f(base + 14)} L {f(ax - 70)} {f(base + 22)}" fill="none" stroke="#FFD23F" stroke-width="3"></path>'
    return (mk.stars(60, w, h * 0.5, seed) + ground(w, h, base, "#2A1A2E", dy=0) + tent
            + son(p, ax, base, s, "shem") + son(p, bx, base, s, "japheth") + cloak + arrows
            + son(p, w * 0.9, base, round(s * 0.95, 3), "ham", flip=True))

def cairn_sunset(w, h, seed):
    """All the days of Noah: the vineyard at sunset, a heap of stones."""
    base = h * 0.82
    return (f'<circle cx="{f(w * 0.7)}" cy="{f(base - 10)}" r="{f(h * 0.24)}" fill="#FF8A3D"></circle>' + V.rays(w * 0.7, base - 10, 30, h * 0.26, w, color="#FFD23F", op=0.3)
            + hills(w, h, base, seed, color="#2A1A2E", amp=6) + A4.stone_heap(w * 0.3, base + 6, w * 0.22, h * 0.16)
            + "".join(f'<path d="M{f(w * x)} {f(base + 4)} L {f(w * x)} {f(base - 50)}" stroke="#12090A" stroke-width="4"></path>' for x in (0.55, 0.62, 0.69, 0.76, 0.83, 0.9)))
