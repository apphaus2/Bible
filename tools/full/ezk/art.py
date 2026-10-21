"""Drawings for the Ezekiel volume (chapter by chapter; later chapters in art2.py ...), on top of everything in job.art (which
carries chr2.art, chr1.art, kg2.art, kg1.art and 2 Samuel's drawings as K2).

Ezekiel at a distance: a blue-grey robe, a white headcloth with a blue cord, a grey-black beard (ezek_fig). The vision:
creature() is one living creature — a bronze figure in fire with four wings, two stretched out and two covering the body;
wheel() a wheel within a wheel, beryl, the rims full of eyes; firmament() the terrible crystal; throne() the throne of
sapphire with only fire and amber light above it and the bow round about (never a figure). God is never drawn, not even
a hand (roll() is the roll alone in the light)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from job.art import *
from job.art import f, K2, K3, P, rect, seated, clouds, smoke, house, tents
import kg1.art as K1
from genesis.art2 import fit, ground, hills, SKIN, city as gcity
from genesis.art3 import man, woman, sun, grid_bg, node, route, label
from exo import art as A
from exo.art8 import bp, dim, tag, title_bar, box
from ecc.art import tree, wind_lines
import joshua1 as J, numbers1 as N, exodus as E, exodus2 as E2, exodus5 as V

INK = "#0D0D0F"
EZ_C = "#4A5A7A"
GB_BEARD = A.WHITE_BEARD.replace("#E8E2D6", "#4A4640")
BERYL, BERYL_D = "#8FD8B8", "#2E7A6A"
BRONZE, BRONZE_L = "#B87333", "#F0C070"
CAPT = ["#5A4A3A", "#6A5A4A", "#3A4A5A", "#5A3A3A", "#4A5A4A", "#6A4A5A", "#7A6A4A"]

def ezek_fig(p, x, y, s, flip=False, up=None):
    """Ezekiel at a distance: blue-grey robe, white headcloth with a blue cord, grey-black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=EZ_C, sw=3, flip=flip, up=up, extra=A.headcloth("#F3EFE6", cord="#1F5FAD") + GB_BEARD)

def captive_fig(p, x, y, s, i=0, flip=False, up=None):
    """One of the captives: an earth-toned robe and headcloth, black beard."""
    c = CAPT[i % len(CAPT)]
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=c, sw=3, flip=flip, up=up, extra=A.headcloth(c) + A.BLACK_BEARD)

def rgrad(uid, stops, cx=0.5, cy=0.5, r=0.5):
    return (f'<defs><radialGradient id="{uid}" cx="{cx}" cy="{cy}" r="{r}">' + "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{a}"></stop>' for o, c, a in stops)
            + '</radialGradient></defs>')

def glow(uid, cx, cy, rx, ry, color="#FFC14D", op=0.9, core="#FFF4C2"):
    """A soft radial glow."""
    return rgrad(uid, [(0, core, op), (0.45, color, op * 0.6), (1, color, 0)]) + f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="url(#{uid})"></ellipse>'

def vgrad(uid, stops):
    return (f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="0" y2="1">' + "".join(f'<stop offset="{o}" stop-color="{c}"></stop>' for o, c in stops)
            + '</linearGradient></defs>')

def bg(uid, w, h, stops):
    """A sky from top to bottom of the drawing; the top colour carries on above it (the drawing may be set under words)."""
    return (f'<defs><linearGradient id="{uid}" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="{f(h)}">'
            + "".join(f'<stop offset="{o}" stop-color="{c}"></stop>' for o, c in stops) + '</linearGradient></defs>'
            + f'<rect x="-10" y="-1500" width="{f(w + 20)}" height="{f(h + 1510)}" fill="url(#{uid})"></rect>')

# ---- the vision ---------------------------------------------------------------------------------------------------------
def wing(x0, y0, x1, y1, bulge=0.3, n=6, fill="#F0D8A0", op=1.0, sw=2.2):
    """A feathered wing from its root (x0, y0) to its tip (x1, y1): a curved leading edge on the side of the bulge's sign,
    a broad scalloped trailing edge on the other side, feather lines between."""
    dx, dy = x1 - x0, y1 - y0; L = math.hypot(dx, dy) or 1; nx, ny = -dy / L, dx / L
    sg = 1 if bulge >= 0 else -1; b = abs(bulge)
    cx, cy = (x0 + x1) / 2 + nx * b * L * sg, (y0 + y1) / 2 + ny * b * L * sg
    d = f"M{f(x0)} {f(y0)} Q {f(cx)} {f(cy)} {f(x1)} {f(y1)}"
    pts = []
    for i in range(n + 1):
        t = 1 - i / n
        k = -sg * L * 0.2 * math.sin(math.pi * min(1, t * 1.15)) ** 0.7
        pts.append((x0 + dx * t + nx * k, y0 + dy * t + ny * k))
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        mx, my = (ax + bx) / 2 - nx * sg * L * 0.06, (ay + by) / 2 - ny * sg * L * 0.06
        d += f" Q {f(mx)} {f(my)} {f(bx)} {f(by)}"
    o = f'<path d="{d} Z" fill="{fill}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round" opacity="{op}"></path>'
    for i, (ax, ay) in enumerate(pts[1:-1]):
        t = 1 - (i + 1) / n
        lx, ly = x0 + dx * t + nx * sg * b * L * 0.5 * 4 * t * (1 - t), y0 + dy * t + ny * sg * b * L * 0.5 * 4 * t * (1 - t)
        o += f'<path d="M{f(ax)} {f(ay)} L {f(lx)} {f(ly)}" stroke="#8A6A3A" stroke-width="1.3" opacity="{op * 0.75:.2f}"></path>'
    return o

def creature(p, x, base, s, seed=1, spread="up", fire=True):
    """One living creature: a figure of burnished brass in fire, four wings — two stretched out (spread="up": raised;
    "level": straight out under the firmament; "down": let down) and two covering the body."""
    r = random.Random(seed)
    o = [glow(f"{p}cg{seed}", x, base - 100 * s, 150 * s, 150 * s, "#FF8A3D", 0.75)]
    sh = base - 160 * s
    tips = {"up": (118, -250), "level": (150, -170), "down": (110, -70)}[spread]
    for sx in (-1, 1):
        o.append(wing(x + sx * 12 * s, sh, x + sx * tips[0] * s, base + tips[1] * s, bulge=0.28 * sx * (-1 if spread == "down" else 1), fill="#F3D890"))
    o.append(mk.person(p, round(x), round(base), round(s, 3), body=BRONZE, cloth="#E8B830", kind="Tunic", sw=2.6))
    o.append(f'<circle cx="{f(x)}" cy="{f(base - 186 * s)}" r="{f(22 * s)}" fill="none" stroke="#FFF4C2" stroke-width="{f(3 * s)}" opacity="0.8"></circle>')
    for sx in (-1, 1):
        o.append(wing(x + sx * 14 * s, base - 150 * s, x + sx * 26 * s, base - 30 * s, bulge=-0.22 * sx, n=5, fill="#E8C878", op=0.95))
    if fire:
        for i in range(3):
            fx = x + r.uniform(-60, 60) * s; fy = base - r.uniform(10, 120) * s
            o.append(E.flame(fx, fy, 14 * s, 30 * s, r.uniform(-4, 4) * s))
    return "".join(o)

def eye(x, y, k, ang=0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(ang)})"><path d="M{f(-k)} 0 Q 0 {f(-k * 0.7)} {f(k)} 0 Q 0 {f(k * 0.7)} {f(-k)} 0 Z" fill="#F3EFE6" stroke="{INK}" stroke-width="1.2"></path>'
            f'<circle cx="0" cy="0" r="{f(k * 0.36)}" fill="#1A2A4A"></circle></g>')

def wheel(x, y, r, seed=1, tilt=0, lit=True):
    """A wheel within a wheel, the colour of beryl, the rims full of eyes; (x, y) its centre."""
    o = []
    if lit: o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r * 1.25)}" fill="#FFF4C2" opacity="0.18"></circle>')
    t = max(4, r * 0.14)
    for rx, rot in ((r, tilt), (r * 0.34, tilt)):
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rx)}" ry="{f(r)}" transform="rotate({f(rot)} {f(x)} {f(y)})" fill="none" stroke="{INK}" stroke-width="{f(t + 4)}"></ellipse>'
                 f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rx)}" ry="{f(r)}" transform="rotate({f(rot)} {f(x)} {f(y)})" fill="none" stroke="{BERYL}" stroke-width="{f(t)}"></ellipse>'
                 f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rx)}" ry="{f(r)}" transform="rotate({f(rot)} {f(x)} {f(y)})" fill="none" stroke="#E8FFF4" stroke-width="{f(t * 0.25)}" opacity="0.7"></ellipse>')
    n = max(8, int(r / 6))
    a0 = math.radians(tilt)
    for rx, m in ((r, n), (r * 0.34, max(5, n // 2))):
        for i in range(m):
            th = 2 * math.pi * (i + 0.5) / m
            px, py = rx * math.cos(th), r * math.sin(th)
            ex, ey = x + px * math.cos(a0) - py * math.sin(a0), y + px * math.sin(a0) + py * math.cos(a0)
            ang = math.degrees(math.atan2(r * math.cos(th), -rx * math.sin(th))) + tilt
            o.append(eye(ex, ey, t * 0.42, ang))
    o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(t * 0.6)}" fill="#FFE680" stroke="{INK}" stroke-width="1.6"></circle>')
    return "".join(o)

def bolts(w, h, seed, n=3, y0=0.1, y1=0.5):
    r = random.Random(seed)
    return "".join(E2.bolt(r.uniform(w * 0.1, w * 0.9), h * y0, h * (y1 - y0), seed + i, w=0.6) for i in range(n))

def storm(w, h, seed):
    """A stormy wind out of the north, a great cloud with a fire infolding itself, a brightness round about it, and in the
    midst as it were glowing metal."""
    r = random.Random(seed)
    cx, cy = w * 0.5, h * 0.56
    o = [bg(f"st{seed}", w, h, [(0, "#0B0B1A"), (0.6, "#2A1A2E"), (1, "#5A3A2A")])]
    o.append(glow(f"sb{seed}", cx, cy, w * 0.5, h * 0.5, "#FFB04A", 0.5))
    for _ in range(30):
        a = r.uniform(0, 2 * math.pi); d = r.uniform(0.35, 0.9)
        o.append(f'<ellipse cx="{f(cx + math.cos(a) * w * d * 0.55)}" cy="{f(cy + math.sin(a) * h * d * 0.42)}" rx="{f(w * r.uniform(0.08, 0.16))}" ry="{f(h * r.uniform(0.05, 0.09))}" '
                 f'fill="{r.choice(["#1A1426", "#2A2036", "#3A2A3A", "#4A3040"])}" stroke="#0D0D0F" stroke-width="1.2" opacity="0.95"></ellipse>')
    o.append(f'<g opacity="0.95">' + E.blaze(cx, cy + h * 0.2, w * 0.34, h * 0.5, seed, n=9) + '</g>')
    o.append(glow(f"sm{seed}", cx, cy - h * 0.02, w * 0.09, h * 0.11, "#FFE680", 1.0, core="#FFFFFF"))
    o.append(V.rays(cx, cy, 30, h * 0.2, h * 0.6, color="#FFE680", op=0.14))
    o.append(bolts(w, h, seed, 2, 0.02, 0.36))
    o.append(wind_lines(w, h, seed, n=8, color="#C8C0D8", op=0.35, y0=0.4, y1=0.98))
    return "".join(o)

def chebar(p, w, h, seed, opened=True, ezek=True):
    """Among the captives by the river Chebar: the flat land of the Chaldeans, a ziggurat far off, poplars on the bank,
    the captives sitting; opened=True: the heavens opened, light pouring out of a rift in the clouds."""
    r = random.Random(seed)
    b = h * 0.95
    o = [mk.defs(p, *ALL), bg(f"cb{seed}", w, h, [(0, "#2A2A5A"), (0.5, "#C88A6A"), (1, "#F3D8A0")])]
    if opened:
        o.append(V.rays(w * 0.62, h * 0.08, 24, 30, h * 1.1, color="#FFF4C2", op=0.3))
        o.append(f'<ellipse cx="{f(w * 0.62)}" cy="{f(h * 0.1)}" rx="{f(w * 0.16)}" ry="{f(h * 0.06)}" fill="#FFF4C2"></ellipse>')
        o.append(clouds(w, h * 0.12, seed, n=7, color="#3A3A6A", op=0.85, ry=0.05))
    o.append(f'<path d="M{f(w * 0.08)} {f(h * 0.6)} L {f(w * 0.1)} {f(h * 0.54)} L {f(w * 0.14)} {f(h * 0.54)} L {f(w * 0.15)} {f(h * 0.5)} L {f(w * 0.19)} {f(h * 0.5)} L {f(w * 0.2)} {f(h * 0.54)} L {f(w * 0.24)} {f(h * 0.54)} L {f(w * 0.26)} {f(h * 0.6)} Z" fill="#8A5A4A" stroke="{INK}" stroke-width="1.6" opacity="0.8"></path>')
    o.append(ground(w, h, h * 0.6, "#C8A878", dy=0))
    o.append(f'<path d="M-10 {f(h * 0.66)} C {f(w * 0.3)} {f(h * 0.64)} {f(w * 0.6)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.67)} L {f(w + 10)} {f(h * 0.76)} C {f(w * 0.6)} {f(h * 0.79)} {f(w * 0.3)} {f(h * 0.73)} -10 {f(h * 0.76)} Z" fill="#3A7A9A" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.1)} {f(h * 0.7)} L {f(w * 0.3)} {f(h * 0.7)} M{f(w * 0.5)} {f(h * 0.73)} L {f(w * 0.75)} {f(h * 0.73)}" stroke="#A8D8E8" stroke-width="2" opacity="0.7"></path>')
    for i in range(6):
        tx = w * (0.32 + i * 0.12) + r.uniform(-10, 10)
        o.append(tree(tx, h * 0.66, h * 0.0024 * r.uniform(0.8, 1.1), color="#4A6A3A", kind="tall", seed=seed + i))
    o.append(E.reeds(-10, w * 0.4, h * 0.78, h * 0.08, 14, seed))
    s = fit(b, max(h * 0.45, b - 210)) * 0.62
    for i in range(5):
        o.append(seated(w * (0.42 + i * 0.11), b, s, CAPT[i], head=CAPT[(i + 2) % 7], beard="#2A1A10", flip=i % 2 == 1, bowed=True))
    if ezek:
        se = s * 1.02
        o.append(ezek_fig(p, w * 0.3, b, se, up=[(-22, -158), (-46, -192), (-58, -228)] if opened else None))
    return "".join(o)

def vision(p, w, h, seed, stage="creatures"):
    """The four living creatures in the fire. stage: "creatures" (lightning among them), "wheels" (a wheel upon the earth
    beside each), "lifted" (lifted up from the earth with the wheels), "firmament" (the crystal stretched over their heads,
    their wings straight)."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), bg(f"vs{seed}", w, h, [(0, "#0B0B1A"), (0.55, "#3A1A2A"), (1, "#7A3A1A")])]
    o.append(glow(f"vg{seed}", w * 0.5, h * 0.6, w * 0.55, h * 0.55, "#FF6A2A", 0.6))
    lifted = stage == "lifted"
    gy = h * (0.98 if not lifted else 1.3)
    if not lifted: o.append(f'<path d="M-10 {f(h * 0.92)} L {f(w + 10)} {f(h * 0.92)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A2A22" stroke="{INK}" stroke-width="2"></path>')
    else: o.append(f'<path d="M-10 {f(h * 0.96)} L {f(w + 10)} {f(h * 0.96)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A1E1A" stroke="{INK}" stroke-width="2"></path>')
    top = h * (0.18 if stage == "firmament" else 0.08)
    b0 = h * (0.86 if not lifted else 0.72)
    s = fit(b0, top + (b0 - top) * 0.2) * (0.78 if stage == "firmament" else 0.85)
    s = min(s, w / 702 * 1.0)
    pos = [(0.3, 0.88, 0.8), (0.7, 0.88, 0.8), (0.16, 1.0, 1.0), (0.84, 1.0, 1.0)]
    if stage == "firmament":
        o.append(firmament_band(w, h, top - h * 0.05, h * 0.09, seed))
    for i, (fx, fb, k) in enumerate(pos):
        bb = b0 * fb if fb < 1 else b0
        if stage in ("wheels", "lifted"):
            o.append(wheel(w * fx, bb - 34 * s * k, 46 * s * k, seed + i, tilt=r.uniform(-12, 12)))
        o.append(creature(p, w * fx, bb - (40 * s * k if stage in ("wheels", "lifted") else 0), s * k, seed + i * 7, spread="level" if stage == "firmament" else "up"))
    if stage == "creatures":
        o.append(bolts(w, h, seed, 3, 0.15, 0.7))
        o.append(mk.speed(w * 0.5, h * 0.5, 30, w * 0.3, w * 0.9, seed, color="#FFE680", op=0.3))
    if lifted:
        o.append(mk.speed(w * 0.5, h * 1.2, 24, h * 0.4, h * 1.4, seed, color="#FFF4C2", op=0.25))
    return "".join(o)

def firmament_band(w, h, y, t, seed):
    """The likeness of a firmament like the terrible crystal: a shining plane seen from below, stretched over the panel."""
    r = random.Random(seed)
    o = [vgrad(f"fm{seed}{int(y)}", [(0, "#FFFFFF"), (0.4, "#CFF4FF"), (1, "#7FC8E8")]),
         f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)} L {f(w * 0.94)} {f(y + t)} L {f(w * 0.06)} {f(y + t)} Z" fill="url(#fm{seed}{int(y)})" stroke="{INK}" stroke-width="2.4"></path>']
    for _ in range(14):
        x = r.uniform(0.05, 0.95) * w
        o.append(f'<path d="M{f(x)} {f(y + 3)} L {f(x + r.uniform(-30, 30))} {f(y + t - 3)}" stroke="#FFFFFF" stroke-width="1.4" opacity="0.8"></path>')
    for _ in range(6):
        x = r.uniform(0.1, 0.9) * w; yy = y + r.uniform(0.2, 0.8) * t
        o.append(f'<path d="M{f(x - 8)} {f(yy)} L {f(x + 8)} {f(yy)} M{f(x)} {f(yy - 8)} L {f(x)} {f(yy + 8)}" stroke="#FFFFFF" stroke-width="2"></path>')
    return "".join(o)

def throne(w, h, seed, fall=False, p="th"):
    """Above the firmament the likeness of a throne as a sapphire stone, and upon it only glowing metal and fire — from
    the loins upward amber light, downward fire — and the brightness round about like the bow in the cloud. No figure is
    drawn. fall=True: Ezekiel fallen upon his face below."""
    o = [bg(f"tb{seed}", w, h, [(0, "#05051A"), (0.6, "#12113A"), (1, "#2A1A5E")]), mk.stars(50, w, h * 0.6, seed)]
    cx = w * 0.5; fy = h * 0.74
    R = min(w * 0.42, h * 0.62)
    o.append(V.rays(cx, fy - R * 0.55, 32, R * 0.3, R * 1.5, color="#FFE680", op=0.1))
    for i, c in enumerate(["#D7261E", "#FF8A3D", "#FFD23F", "#5ECB5E", "#2C9DE8", "#7A3BA8"]):
        o.append(f'<path d="M{f(cx - R + i * 7)} {f(fy)} A {f(R - i * 7)} {f(R - i * 7)} 0 0 1 {f(cx + R - i * 7)} {f(fy)}" fill="none" stroke="{c}" stroke-width="7" opacity="0.6"></path>')
    o.append(glow(f"tg{seed}", cx, fy - R * 0.5, R * 0.8, R * 0.7, "#FFB04A", 0.85))
    sw_, sh = R * 0.62, R * 0.2
    o.append(vgrad(f"sap{seed}", [(0, "#8AC8FF"), (0.5, "#1F4FBF"), (1, "#0A1A6A")]))
    sap = f"url(#sap{seed})"
    o.append(P(f"M{f(cx - sw_ * 0.36)} {f(fy - sh)} L {f(cx - sw_ * 0.36)} {f(fy - R * 0.78)} L {f(cx - sw_ * 0.18)} {f(fy - R * 0.86)} L {f(cx + sw_ * 0.18)} {f(fy - R * 0.86)} L {f(cx + sw_ * 0.36)} {f(fy - R * 0.78)} L {f(cx + sw_ * 0.36)} {f(fy - sh)} Z", sap, 2.6))
    o.append(P(f"M{f(cx - sw_ / 2)} {f(fy)} L {f(cx - sw_ / 2)} {f(fy - sh)} L {f(cx + sw_ / 2)} {f(fy - sh)} L {f(cx + sw_ / 2)} {f(fy)} Z", sap, 2.6))
    for sx in (-1, 1):
        o.append(P(f"M{f(cx + sx * sw_ / 2)} {f(fy - sh)} L {f(cx + sx * sw_ / 2)} {f(fy - sh - R * 0.2)} L {f(cx + sx * sw_ * 0.36)} {f(fy - sh - R * 0.2)} L {f(cx + sx * sw_ * 0.36)} {f(fy - sh)} Z", sap, 2.2))
    o.append(f'<path d="M{f(cx - sw_ * 0.3)} {f(fy - R * 0.8)} L {f(cx)} {f(fy - sh)} L {f(cx + sw_ * 0.3)} {f(fy - R * 0.8)}" stroke="#AEE0FF" stroke-width="1.6" fill="none" opacity="0.7"></path>')
    o.append(f'<g opacity="0.85">' + E.blaze(cx, fy - sh, sw_ * 0.62, R * 0.42, seed, n=6) + '</g>')
    o.append(glow(f"tn{seed}", cx, fy - R * 0.72, R * 0.42, R * 0.52, "#FFC14D", 0.6))
    o.append(glow(f"tm{seed}", cx, fy - R * 0.7, R * 0.2, R * 0.36, "#FFE680", 1.0, core="#FFFFFF"))
    o.append(firmament_band(w, h, fy, h * 0.08, seed))
    if fall:
        o.append(N.prostrate(w * 0.4, h * 0.98, min(1.0, h / 520), color=EZ_C, skin=SKIN))
    return "".join(o)

def creature_plan(w, h):
    """A plate of the living creatures: four about one centre, each with four faces — a man before, a lion on the right,
    an ox on the left, an eagle — the wings of each joined to the next, the wheel beside each."""
    o = [bp(w, h), title_bar(w, "THE LIVING CREATURES · THEIR FACES AND THEIR WINGS")]
    cx, cy = w * 0.5, h * 0.56; d = min(w * 0.22, h * 0.28)
    pts = [(cx, cy - d), (cx + d, cy), (cx, cy + d), (cx - d, cy)]
    o.append(f'<path d="M{" L ".join(f"{f(x)} {f(y)}" for x, y in pts)} Z" fill="none" stroke="#FFD23F" stroke-width="2.4" stroke-dasharray="8 5"></path>')
    k = d * 0.3
    for i, (x, y) in enumerate(pts):
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(k)}" fill="#3A2A1A" stroke="#FFD23F" stroke-width="2"></circle>')
        for j, (nm, col) in enumerate((("MAN", "#F3EFE6"), ("LION", "#FFC14D"), ("EAGLE", "#8FD0E2"), ("OX", "#C8A06A"))):
            a = math.atan2(y - cy, x - cx) + j * math.pi / 2
            fx, fy = x + math.cos(a) * k, y + math.sin(a) * k
            o.append(f'<circle cx="{f(fx)}" cy="{f(fy)}" r="{f(k * 0.3)}" fill="{col}" stroke="#0D0D0F" stroke-width="1.4"></circle>')
            if i == 1: o.append(label(fx + math.cos(a) * k * 0.9, fy + math.sin(a) * k * 0.9 + 3, nm, col, 8))
        o.append(wheel(x + (x - cx) * 0.55, y + (y - cy) * 0.55, k * 0.6, 3 + i, lit=False))
    o.append(tag(pts[0][0] + k, pts[0][1], "TWO WINGS JOINED ONE TO ANOTHER", w * 0.72, h * 0.16))
    o.append(label(14, 36, "THEY TURNED NOT WHEN THEY WENT · EVERY ONE STRAIGHT FORWARD", "#8FD0E2", 8, "start"))
    o.append(tag(pts[2][0] + k * 0.5, pts[2][1] + k * 0.6, "A WHEEL UPON THE EARTH BESIDE EACH", w * 0.62, h * 0.86))
    o.append(label(w * 0.03, h * 0.95, "FACE OF A MAN · A LION ON THE RIGHT · AN OX ON THE LEFT · AN EAGLE", "#8FD0E2", 8, "start"))
    return "".join(o)

def roll(w, h, seed):
    """The roll of a book spread out in a light, written within and without (no hand is drawn)."""
    r = random.Random(seed)
    o = [bg(f"rl{seed}", w, h, [(0, "#1A1030"), (1, "#5A3A6A")]), glow(f"rg{seed}", w * 0.5, h * 0.5, w * 0.5, h * 0.55, "#FFE680", 0.8, core="#FFFFFF")]
    x0, x1, y0, y1 = w * 0.18, w * 0.82, h * 0.3, h * 0.78
    o.append(f'<path d="M{f(x0)} {f(y0)} L {f(x1)} {f(y0 + 8)} L {f(x1)} {f(y1 + 8)} L {f(x0)} {f(y1)} Z" fill="#F0E2B8" stroke="{INK}" stroke-width="2.4"></path>')
    for i in range(10):
        y = y0 + (y1 - y0) * (i + 0.8) / 11
        o.append(f'<path d="M{f(x0 + 24)} {f(y + 1)} L {f(x1 - 24)} {f(y + 8)}" stroke="#3A2A1A" stroke-width="2.2" stroke-dasharray="{r.randint(6, 14)} {r.randint(3, 6)} {r.randint(10, 30)} 4" opacity="0.8"></path>')
    for x, yy in ((x0, y0), (x1, y0 + 8)):
        o.append(f'<rect x="{f(x - 14)}" y="{f(yy - 16)}" width="28" height="{f(y1 - y0 + 32)}" rx="12" fill="#D8C08A" stroke="{INK}" stroke-width="2.4"></rect>'
                 f'<rect x="{f(x - 4)}" y="{f(yy - 30)}" width="8" height="{f(y1 - y0 + 60)}" fill="#6A3A1A" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<path d="M{f(x1 - 40)} {f(y1 + 8)} Q {f(x1 - 10)} {f(y1 - 30)} {f(x1 + 4)} {f(y1 - 60)} L {f(x1 + 4)} {f(y1 + 8)} Z" fill="#E0CC98" stroke="{INK}" stroke-width="1.6"></path>'
             f'<path d="M{f(x1 - 28)} {f(y1 - 2)} L {f(x1 - 6)} {f(y1 - 34)}" stroke="#3A2A1A" stroke-width="1.6" stroke-dasharray="6 3"></path>')
    o.append(V.rays(w * 0.5, h * 0.54, 20, w * 0.36, w * 0.8, color="#FFF4C2", op=0.25))
    return "".join(o)

def scorpion(x, y, s, flip=False):
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            '<path d="M-20 0 C -18 -10 10 -12 20 -4 C 26 -2 26 4 20 6 C 8 10 -14 10 -20 0 Z" fill="#3A2A1A" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M-18 0 C -36 -6 -44 -26 -34 -40 C -28 -48 -18 -44 -22 -36" fill="none" stroke="#0D0D0F" stroke-width="6" stroke-linecap="round"></path>'
            '<path d="M-18 0 C -36 -6 -44 -26 -34 -40 C -28 -48 -18 -44 -22 -36" fill="none" stroke="#5A3A1A" stroke-width="3.6" stroke-linecap="round"></path>'
            '<path d="M18 -2 L 30 -10 L 38 -6 M18 4 L 30 10 L 38 6 M-6 6 L -10 14 M2 6 L 0 14 M10 6 L 12 14" fill="none" stroke="#0D0D0F" stroke-width="2.4" stroke-linecap="round"></path></g>')

def briers(w, h, seed):
    """Briers and thorns and the scorpions among the stones (2:6)."""
    r = random.Random(seed)
    o = [bg(f"br{seed}", w, h, [(0, "#C88A5A"), (1, "#F3D8A0")]), hills(w, h, h * 0.5, seed, "#9A6A4A", amp=12, step=80), ground(w, h, h * 0.62, "#B8946A", dy=0)]
    for i in range(7):
        x = r.uniform(0, w); y = h * r.uniform(0.66, 0.96)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(r.uniform(20, 46))}" ry="{f(r.uniform(10, 20))}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></ellipse>')
    for i in range(9):
        x = r.uniform(0, w); y = h * r.uniform(0.66, 1.0); L = r.uniform(60, 120)
        d = f"M{f(x)} {f(y)} C {f(x + L * 0.3)} {f(y - L * 0.6)} {f(x + L * 0.8)} {f(y - L * 0.5)} {f(x + L)} {f(y - L * 0.9)}"
        o.append(f'<path d="{d}" fill="none" stroke="#3A2A1A" stroke-width="3.4"></path>')
        for k in range(6):
            t = (k + 1) / 7; px = x + L * t; py = y - L * 0.7 * t
            o.append(f'<path d="M{f(px)} {f(py)} l {f(r.choice([-1, 1]) * 9)} {f(-6)}" stroke="#3A2A1A" stroke-width="2"></path>')
    for i in range(3):
        o.append(scorpion(w * (0.2 + i * 0.3), h * (0.84 + 0.05 * (i % 2)), min(1.6, h / 260), flip=i % 2 == 0))
    return "".join(o)

def tel_abib(p, w, h, seed, ezek_seated=True):
    """Tel-abib by the river Chebar: houses of mud brick among the palms, the captives; Ezekiel sitting overwhelmed among
    them seven days."""
    r = random.Random(seed); b = h * 0.95
    o = [mk.defs(p, *ALL), bg(f"ta{seed}", w, h, [(0, "#4A3A6A"), (0.6, "#E8A070"), (1, "#F3D8A0")])]
    o.append(f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.4)} {f(h * 0.6)} {f(w * 0.7)} {f(h * 0.64)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.66)} L -10 {f(h * 0.68)} Z" fill="#3A7A9A" stroke="{INK}" stroke-width="2"></path>')
    for i in range(5):
        x = w * (0.04 + i * 0.2) + r.uniform(-10, 10); hh = h * r.uniform(0.16, 0.22)
        o.append(house(x, h * 0.72, w * 0.13, hh, lit=i % 2 == 0, color=r.choice(["#B8946A", "#C8A47A", "#A8845A"])))
    for i in range(3): o.append(S1.palm(w * (0.17 + i * 0.3), h * 0.72, h / 520))
    o.append(ground(w, h, h * 0.72, "#C8A878", dy=0))
    s = fit(b, max(h * 0.48, b - 200)) * 0.62
    for i in range(6):
        o.append(seated(w * (0.08 + i * 0.16), b, s, CAPT[i], head=CAPT[(i + 3) % 7], beard="#2A1A10", flip=i >= 3, bowed=True))
    if ezek_seated:
        o.append(seated(w * 0.5, b, s * 1.08, EZ_C, head="#F3EFE6", beard="#4A4640", bowed=True))
    return "".join(o)

def watchman(p, w, h, seed, city=True, dusk=True):
    """A watchman upon the wall: a tower over the city at dusk, the watchman (Ezekiel) blowing the trumpet."""
    o = [mk.defs(p, *ALL), bg(f"wm{seed}", w, h, [(0, "#1A1A3A") if dusk else (0, "#5A8AB0"), (0.6, "#C8603A") if dusk else (0.6, "#C8D8E0"), (1, "#F3B870") if dusk else (1, "#F3E8C8")])]
    if city:
        o.append(gcity(w * 0.66, h * 0.76, w * 0.66, h * 0.2, seed, color="#3A2A3E", lit="#FFC14D"))
    tx, tw = w * 0.2, max(70, w * 0.14)
    top = h * 0.66
    o.append(f'<path d="M-10 {f(h * 0.76)} L {f(w + 10)} {f(h * 0.76)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="2.4"></path>')
    for i in range(int(w / 40) + 1):
        o.append(f'<rect x="{f(i * 40)}" y="{f(h * 0.74)}" width="22" height="12" fill="#8A6A4A" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="{f(tx - tw / 2)}" y="{f(top)}" width="{f(tw)}" height="{f(h - top + 10)}" fill="#9A7A5A" stroke="{INK}" stroke-width="2.6"></rect>')
    for i in range(4):
        o.append(f'<rect x="{f(tx - tw / 2 + i * tw / 4 + 2)}" y="{f(top - 12)}" width="{f(tw / 4 - 8)}" height="14" fill="#9A7A5A" stroke="{INK}" stroke-width="1.8"></rect>')
    s = min(fit(top - 12, h * 0.36), 1.0)
    o.append(mk.person(p, round(tx), round(top - 12), round(s, 3), body=SKIN, cloth=EZ_C, sw=3, up=J.TRUMPET_ARM,
                       extra=A.headcloth("#F3EFE6", cord="#1F5FAD") + GB_BEARD + J.shofar(8, -188, 0.9, rot=-14)))
    o.append(mk.speed(tx + 60 * s, top - 190 * s, 10, 30 * s, 140 * s, seed, color="#FFF4C2", op=0.4))
    return "".join(o)

def plain_glory(p, w, h, seed, fallen=True):
    """The plain: the glory of Jehovah standing there as a pillar of amber light, and Ezekiel fallen on his face."""
    o = [mk.defs(p, *ALL), bg(f"pg{seed}", w, h, [(0, "#2A2A4A"), (0.6, "#8A6A6A"), (1, "#C8A878")]), hills(w, h, h * 0.62, seed, "#5A4A4A", amp=6, step=90),
         ground(w, h, h * 0.7, "#A8906A", dy=0)]
    o.append(glory(f"pl{seed}", w * 0.66, h * 0.8, w * 0.12, h * 0.5, seed))
    s = min(1.1, h / 360)
    if fallen: o.append(N.prostrate(w * 0.24, h * 0.9, s, color=EZ_C, skin=SKIN))
    else: o.append(ezek_fig(p, w * 0.26, h * 0.94, fit(h * 0.94, h * 0.5)))
    return "".join(o)

def shut_house(p, w, h, seed):
    """Go, shut thyself within thy house: a house of mud brick at evening, the door shut, cords laid on the threshold."""
    o = [mk.defs(p, *ALL), bg(f"sh{seed}", w, h, [(0, "#1A1A3A"), (1, "#8A5A5A")]), ground(w, h, h * 0.84, "#7A6A5A", dy=0)]
    x0, x1, top = w * 0.24, w * 0.76, h * 0.22
    o.append(P(f"M{f(x0)} {f(h * 0.84)} L {f(x0)} {f(top)} L {f(x1)} {f(top)} L {f(x1)} {f(h * 0.84)} Z", "#A8845A", 2.6))
    for i in range(1, 9):
        y = top + (h * 0.84 - top) * i / 9
        o.append(f'<path d="M{f(x0)} {f(y)} L {f(x1)} {f(y)}" stroke="#7A5A3A" stroke-width="1.2"></path>')
    dx = w * 0.5
    o.append(P(f"M{f(dx - w * 0.07)} {f(h * 0.84)} L {f(dx - w * 0.07)} {f(h * 0.5)} Q {f(dx)} {f(h * 0.44)} {f(dx + w * 0.07)} {f(h * 0.5)} L {f(dx + w * 0.07)} {f(h * 0.84)} Z", "#4A2A1A", 2.4))
    o.append(f'<path d="M{f(dx - w * 0.07)} {f(h * 0.66)} L {f(dx + w * 0.07)} {f(h * 0.66)}" stroke="#2A1A10" stroke-width="5"></path>')
    for i in range(4):
        o.append(f'<ellipse cx="{f(dx - w * 0.12 + i * 10)}" cy="{f(h * 0.88)}" rx="{f(w * 0.05)}" ry="{f(h * 0.018)}" fill="none" stroke="#C8A878" stroke-width="3"></ellipse>')
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(h * 0.32)}" width="{f(w * 0.06)}" height="{f(h * 0.08)}" fill="#FFC14D" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o)

def glory(uid, cx, base, wd, ht, seed=1):
    """The glory of Jehovah as a standing pillar of amber light in a ring of brightness (no figure)."""
    return (glow(uid + "a", cx, base - ht * 0.5, wd * 1.4, ht * 0.7, "#FFC14D", 0.8)
            + V.rays(cx, base - ht * 0.55, 26, wd * 0.4, ht * 1.1, color="#FFE680", op=0.14)
            + f'<ellipse cx="{f(cx)}" cy="{f(base - ht * 0.55)}" rx="{f(wd * 0.75)}" ry="{f(ht * 0.55)}" fill="none" stroke="#FFF4C2" stroke-width="3" opacity="0.6"></ellipse>'
            + glow(uid + "b", cx, base - ht * 0.5, wd * 0.4, ht * 0.5, "#FFE680", 1.0, core="#FFFFFF"))
