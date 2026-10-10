"""New drawings for Genesis chapter 3 (Genesis 10–15): the nations, Babel, Terah's house, Abram's journeys,
Egypt, Lot and the Plain, the war of the kings, Melchizedek, the stars and the covenant between the pieces."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4, exodus5 as V, joshua1 as J, judges1 as G1, judges2 as S
import samuel1 as A, samuel2 as A2, samuel3 as A3, samuel4 as A4, numbers1 as N, ruth1 as R, egypt as EG, tower as TW
from faces_ex import F
import faces
from genesis import art2 as Y
from genesis.art2 import fit, ground, hills, birds, city, SKIN, WHITE_BEARD, SONS
def f(v): return f"{v:.1f}"

# ---- faces ----------------------------------------------------------------------------------------------
ABRAM = faces.face("adam", skin="#C98E66", shadow="#8A5A3E", hair="#B8B2A6", hl="#8A867E", beard=True, light="#FFE680")
ABRAM_GRAVE = faces.face("adam", skin="#C98E66", shadow="#6A4A5A", hair="#B8B2A6", hl="#8A867E", beard=True, brow="sorrow")
ABRAM_BOLD = faces.face("adam", skin="#C47A5A", shadow="#5A1A16", hair="#B8B2A6", hl="#8A867E", beard=True, brow="scowl", light="#FF8A3D")
ABRAM_STARS = faces.face("adam", skin="#9A7A8A", shadow="#4A3A6E", hair="#C8C2D6", hl="#8A86A6", beard=True, light="#CFE0FF")
ABRAM_DARK = faces.face("adam", skin="#6A5A7A", shadow="#2A1A3E", hair="#8A86A6", hl="#5A5676", beard=True, brow="sorrow", sweat=True, light="#9A6AFF")
SARAI = F("eve", skin="#DDA684", shadow="#A87050", hair="#2A1A10", scarf="#8A3A5A", light="#FFE680")
SARAI_SAD = F("eve", skin="#C99A84", shadow="#7A5A6A", hair="#2A1A10", scarf="#8A3A5A", tear=True)
LOT = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E", scarf="#7A2A3A", cord=True, light="#FFC14D")
LOT_TAKEN = F("adam", skin="#B98A6E", shadow="#5A3A4A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E", scarf="#7A2A3A", cord=True, brow="sorrow", sweat=True)
TERAH = F("adam", skin="#B98A6E", shadow="#6A4A5A", hair="#F3EFE6", hl="#B8B2A6", beard=True, brow="sorrow", tear=True)
PHARAOH = F("adam", skin="#B9785A", shadow="#5A2A1E", egypt=("#E8B830", "#D7261E"), collar=True, kohl=True, false_beard=True, brow="scowl", light="#FF6A4A")
MELCHIZEDEK = F("adam", skin="#D9A27A", shadow="#9A6A4A", hair="#F3EFE6", hl="#C8C2B6", beard=True, beard_color="#F3EFE6", scarf="#F3EFE6", band=True, light="#FFD23F")
KING_SODOM = F("adam", skin="#B98A6E", shadow="#4A1A26", hair="#1A1210", beard=True, beard_color="#1A1210", scarf="#5A1A4A", band=True, brow="scowl", light="#FF6A4A")
NIMROD = F("adam", skin="#A8704E", shadow="#4A2418", hair="#0D0D0F", beard=True, beard_color="#0D0D0F", band=True, brow="scowl", light="#FF8A3D")

# ---- people ---------------------------------------------------------------------------------------------
ABRAM_ROBE, SARAI_ROBE, LOT_ROBE = "#2C4A7A", "#8A3A5A", "#7A2A3A"
GREY_BEARD = WHITE_BEARD.replace("#E8E2D6", "#B8B2A6")
CROWN = A2.crown(0, -194, 0.42)
HOLD_STAFF = [(-22, -158), (-40, -120), (-48, -92)]
STAFF = '<path d="M-50 -170 L -46 6" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"></path>'

def abram(p, x, y, s, flip=False, up=None, staff=False):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=ABRAM_ROBE, sw=3, flip=flip, up=up, extra=GREY_BEARD + (STAFF if staff else ""))

def sarai(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=SARAI_ROBE, woman=True, hair="#2A1A10", sw=3, flip=flip, up=up)

def lot(p, x, y, s, flip=False, up=None):
    beard = '<path d="M-9 -172 C -8 -162 -3 -154 0 -150 C 3 -154 8 -162 9 -172 C 5 -168 -5 -168 -9 -172 Z" fill="#3A2A1E" stroke="#0D0D0F" stroke-width="1.4"></path>'
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=LOT_ROBE, sw=3, flip=flip, up=up, extra=beard)

def man(p, x, y, s, cloth, flip=False, up=None, extra="", kind="Tunic", body=SKIN):
    return mk.person(p, round(x), round(y), round(s, 3), body=body, cloth=cloth, kind=kind, sw=3, flip=flip, up=up, extra=extra)

def woman(p, x, y, s, cloth, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, woman=True, hair="#1A1210", sw=3, flip=flip, up=up)

def king(p, x, y, s, cloth, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, sw=3, flip=flip, up=up, extra=CROWN)

def sun(x, y, r, color="#FFD23F", glow="#FFF4C2", op=0.35):
    return V.rays(x, y, 30, r * 1.1, r * 9, color=glow, op=op) + f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{color}"></circle>'

def label(x, y, text, color="#F3EFE6", size=11, anchor="middle", weight=600, ls=0.14):
    return (f'<text x="{f(x)}" y="{f(y)}" fill="{color}" font-family="IBM Plex Mono, monospace" font-weight="{weight}" font-size="{size}" '
            f'letter-spacing="{ls}em" text-anchor="{anchor}">{text}</text>')

def grid_bg(w, h, color="#1E3A5A", step=28, bg="#0B1A2E"):
    lines = "".join(f'<path d="M{x} 0 L {x} {f(h)}" stroke="{color}" stroke-width="1"></path>' for x in range(0, int(w) + step, step))
    lines += "".join(f'<path d="M0 {y} L {f(w)} {y}" stroke="{color}" stroke-width="1"></path>' for y in range(0, int(h) + step, step))
    return f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{bg}"></rect>' + lines

def node(x, y, name, color="#FFD23F", r=6, dy=-12, anchor="middle", size=10):
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r + 5)}" fill="none" stroke="{color}" stroke-width="1.6" opacity="0.6"></circle>'
            f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{color}" stroke="#0D0D0F" stroke-width="1.4"></circle>' + label(x, y + dy, name, color, size, anchor))

def route(pts, color="#8FD0E2", sw=2.4, dash="7 6", arrow=True):
    d = "M" + " L ".join(f"{f(x)} {f(y)}" for x, y in pts)
    o = f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-dasharray="{dash}"></path>'
    if arrow and len(pts) > 1:
        (x0, y0), (x1, y1) = pts[-2], pts[-1]; a = math.atan2(y1 - y0, x1 - x0)
        o += f'<path d="M{f(x1)} {f(y1)} L {f(x1 - 12 * math.cos(a - 0.45))} {f(y1 - 12 * math.sin(a - 0.45))} L {f(x1 - 12 * math.cos(a + 0.45))} {f(y1 - 12 * math.sin(a + 0.45))} Z" fill="{color}"></path>'
    return o

def flock(x0, x1, y0, y1, n, seed, cows=0.25, flip=False, smin=0.18, smax=0.36):
    r = random.Random(seed); o = []
    for y, x in sorted((r.uniform(y0, y1), r.uniform(x0, x1)) for _ in range(n)):
        k = (y - y0) / max(1, y1 - y0); s = smin + (smax - smin) * k
        o.append(A.cow(x, y, s * 0.8, color=r.choice(["#8A5A30", "#C9A27A", "#5A3A22"]), flip=flip) if r.random() < cows else E.sheep(x, y, s, flip=flip))
    return "".join(o)

def caravan(p, x0, x1, base, s, seed, flip=False, family=True):
    """Camels with riders and loads, asses, walkers and sheep in a line across the panel."""
    r = random.Random(seed); o = []
    n = 7
    for i in range(n):
        x = x0 + (x1 - x0) * i / (n - 1)
        k = i % 3
        if k == 0: o.append(G1.camel(x, base - 4, 0.36 * s, flip=flip, color=r.choice(["#B5844A", "#C99A5A"]), rider=r.choice(["#2C4A7A", "#7A2A3A", "#C9A86A", "#5A3A22"])))
        elif k == 1: o.append(N.ass(x, base, 0.2 * s, flip=flip))
        else: o.append(man(p, x, base, s * 0.42, r.choice(["#5A3A22", "#8A6A4A", "#3A2214"]), flip=flip, extra=STAFF))
    o.append(flock(x0, x1, base + 4, base + 30 * s, 8, seed + 1, cows=0.2, flip=flip, smin=0.2 * s, smax=0.3 * s))
    return "".join(o)

# ---- Genesis 10 -----------------------------------------------------------------------------------------
def three_sons(p, w, h, seed):
    """Shem, Ham and Japheth on a rise; three lines of their sons going out over a grid map of the earth."""
    base = h * 0.92
    o = [grid_bg(w, h, color="#1E2E4A", bg="#0B1226"), mk.stars(40, w, h * 0.5, seed)]
    ends = {"japheth": (w * 0.95, h * 0.18), "ham": (w * 0.95, h * 0.82), "shem": (w * 0.98, h * 0.5)}
    for k, (ex, ey) in ends.items():
        o.append(route([(w * 0.34, h * 0.56), (w * 0.62, (h * 0.56 + ey) / 2), (ex, ey)], color=SONS[k], sw=3))
    o.append(node(w * 0.84, h * 0.2, "THE ISLES", SONS["japheth"]) + node(w * 0.84, h * 0.84, "THE SOUTH", SONS["ham"], dy=22) + node(w * 0.88, h * 0.5, "THE EAST", SONS["shem"]))
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(base - 16)} C {f(w * 0.1)} {f(base - 34)} {f(w * 0.3)} {f(base - 30)} {f(w * 0.42)} {f(base)} L {f(w * 0.42)} {f(h + 10)} Z" fill="#1A1430" stroke="#0D0D0F" stroke-width="2"></path>')
    for i, k in enumerate(["shem", "ham", "japheth"]):
        o.append(Y.son(p, w * (0.08 + i * 0.1), base - 20 + i * 3, fit(base, h * 0.52), k, flip=True))
    return "".join(o)

def isles(w, h, seed):
    """The isles of the nations: islands with harbours and sails on a blue sea."""
    r = random.Random(seed); y = h * 0.52
    o = [sun(w * 0.8, h * 0.2, 16, op=0.3), Y.sea(w, h, y, seed, color="#1F6F9A", amp=4)]
    for x, iw in [(0.18, 90), (0.55, 70), (0.86, 60)]:
        o.append(f'<path d="M{f(w * x - iw)} {f(y + 18)} C {f(w * x - iw * 0.5)} {f(y - 18)} {f(w * x + iw * 0.5)} {f(y - 22)} {f(w * x + iw)} {f(y + 18)} Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>')
        o.append(f'<g transform="translate({f(w * x)} {f(y - 4)}) scale(0.5)">' + city(0, 0, iw * 1.2, 60, int(x * 100), color="#E8E2D6", lit="#1F5FAD") + '</g>')
    for i in range(4):
        sx, sy = r.uniform(0.05, 0.95) * w, r.uniform(y + 20, h * 0.95)
        o.append(f'<path d="M{f(sx - 18)} {f(sy)} L {f(sx + 18)} {f(sy)} L {f(sx + 12)} {f(sy + 8)} L {f(sx - 12)} {f(sy + 8)} Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 f'<path d="M{f(sx)} {f(sy)} L {f(sx)} {f(sy - 34)} L {f(sx + 16)} {f(sy - 6)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return "".join(o)

def hunter(p, w, h, seed):
    """Nimrod, a mighty hunter before Jehovah: bow drawn on a ridge at sunset, a lion and wild asses below."""
    base = h * 0.84
    s = fit(base, h * 0.4)
    bow = (f'<g transform="translate({f(w * 0.3)} {f(base)}) scale({f(s)})">'
           '<path d="M44 -230 C 74 -200 74 -130 44 -100" fill="none" stroke="#0D0D0F" stroke-width="8" stroke-linecap="round"></path>'
           '<path d="M44 -230 C 74 -200 74 -130 44 -100" fill="none" stroke="#8A5A30" stroke-width="5" stroke-linecap="round"></path>'
           '<path d="M44 -230 L 4 -164 L 44 -100" fill="none" stroke="#F3EFE6" stroke-width="1.4"></path>'
           '<path d="M2 -164 L 110 -168" stroke="#0D0D0F" stroke-width="3"></path><path d="M110 -168 L 98 -174 L 100 -162 Z" fill="#A8B0BA" stroke="#0D0D0F" stroke-width="1.2"></path></g>')
    o = [sun(w * 0.82, base - 30, h * 0.16, color="#FF8A3D", glow="#FFD23F", op=0.3),
         f'<path d="M-10 {f(base)} L {f(w * 0.46)} {f(base - 10)} L {f(w * 0.56)} {f(base + 24)} L {f(w + 10)} {f(base + 30)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A140C" stroke="#0D0D0F" stroke-width="2"></path>',
         man(p, w * 0.3, base, s, "#5A1A16", up=[(-22, -158), (8, -166), (40, -166)],
             extra='<path d="M18 -150 L 4 -164" stroke="#0D0D0F" stroke-width="12" stroke-linecap="round"></path><path d="M18 -150 L 4 -164" stroke="#5A2A16" stroke-width="8" stroke-linecap="round"></path>'
             + '<path d="M-14 -192 C -10 -200 10 -200 14 -192" fill="none" stroke="#E8B830" stroke-width="4"></path>'),
         bow,
         S.lion(w * 0.74, base + 34, 0.42, flip=True, roar=True), N.ass(w * 0.92, base + 36, 0.18), N.ass(w * 0.6, base + 40, 0.16),
         mk.speed(w * 0.74, base, 12, 30, 120, seed, color="#FFD23F", op=0.4)]
    return "".join(o)

def kingdom(w, h, seed, names, color="#E8A35A", great=None):
    """A row of walled cities of the plain, each named; the great city larger."""
    r = random.Random(seed); base = h * 0.82; n = len(names); o = [ground(w, h, base, "#8A6A4A", dy=0)]
    for i, nm in enumerate(names):
        cx = w * (i + 0.5) / n; big = nm == great
        cw, ch = w / n * (0.92 if big else 0.7), h * (0.5 if big else 0.34)
        o.append(city(cx, base, cw, ch, seed + i, color=color if not big else "#B5652E"))
        o.append(f'<rect x="{f(cx - len(nm) * 4.4 - 6)}" y="{f(base + 8)}" width="{f(len(nm) * 8.8 + 12)}" height="18" fill="#12113A"></rect>' + label(cx, base + 21, nm, "#FFD23F", 10.5))
    return "".join(o)

def nineveh(w, h, seed):
    """Out of that land he went forth into Assyria: Nineveh on its river, with Rehoboth-Ir, Calah and Resen."""
    base = h * 0.76
    o = [sun(w * 0.12, h * 0.2, 14, color="#FFE680", op=0.25),
         J.jericho(w * 0.3, w * 0.98, base - h * 0.42, base, seed, towers=5),
         f'<path d="M-10 {f(base)} L {f(w + 10)} {f(base)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M-10 {f(base + 20)} C {f(w * 0.3)} {f(base + 10)} {f(w * 0.6)} {f(base + 34)} {f(w + 10)} {f(base + 22)} L {f(w + 10)} {f(base + 44)} C {f(w * 0.6)} {f(base + 56)} {f(w * 0.3)} {f(base + 30)} -10 {f(base + 42)} Z" fill="#2C7DA0" stroke="#0D0D0F" stroke-width="2"></path>',
         city(w * 0.12, base, w * 0.16, h * 0.24, seed + 9, color="#7A5A4A")]
    return "".join(o)

def canaan_map(w, h, seed):
    """The border of the Canaanite, as a technical map: Sidon in the north, Gerar and Gaza on the coast, the cities of the Plain to the east."""
    o = [grid_bg(w, h)]
    coast = f'M{f(w * 0.24)} -10 C {f(w * 0.22)} {f(h * 0.3)} {f(w * 0.16)} {f(h * 0.6)} {f(w * 0.08)} {f(h + 10)} L -10 {f(h + 10)} L -10 -10 Z'
    o.append(f'<path d="{coast}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>' + label(w * 0.06, h * 0.5, "THE GREAT SEA", "#8FD0E2", 9, "start"))
    o.append(f'<path d="M{f(w * 0.62)} {f(h * 0.06)} C {f(w * 0.6)} {f(h * 0.3)} {f(w * 0.66)} {f(h * 0.5)} {f(w * 0.64)} {f(h * 0.62)}" fill="none" stroke="#2C9DB8" stroke-width="3"></path>')
    o.append(f'<ellipse cx="{f(w * 0.64)}" cy="{f(h * 0.76)}" rx="{f(w * 0.04)}" ry="{f(h * 0.14)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>')
    pts = {"SIDON": (w * 0.3, h * 0.12), "GERAR": (w * 0.2, h * 0.8), "GAZA": (w * 0.16, h * 0.66), "SODOM": (w * 0.58, h * 0.72), "GOMORRAH": (w * 0.7, h * 0.66),
           "ADMAH": (w * 0.74, h * 0.8), "ZEBOIIM": (w * 0.6, h * 0.88), "LASHA": (w * 0.78, h * 0.94)}
    o.append(f'<path d="M{f(pts["SIDON"][0])} {f(pts["SIDON"][1])} L {f(pts["GAZA"][0])} {f(pts["GAZA"][1])} L {f(pts["GERAR"][0])} {f(pts["GERAR"][1])} L {f(pts["ZEBOIIM"][0])} {f(pts["ZEBOIIM"][1])} '
             f'L {f(pts["LASHA"][0])} {f(pts["LASHA"][1])} L {f(w * 0.72)} {f(h * 0.3)} Z" fill="#D7261E" fill-opacity="0.12" stroke="#D7261E" stroke-width="2" stroke-dasharray="8 5"></path>')
    for nm, (x, y) in pts.items():
        o.append(node(x, y, nm, "#FFD23F", r=4, dy=-10, anchor="start" if x < w * 0.5 else "middle", size=9))
    o.append(label(w * 0.94, h * 0.1, "N ↑", "#8FD0E2", 12, "end"))
    return "".join(o)

def divided(p, w, h, seed):
    """In the days of Peleg was the earth divided: a crack of light across the land, the two brothers on either side."""
    r = random.Random(seed); base = h * 0.86
    crack = [(w * 0.5 + r.uniform(-20, 20), y) for y in range(-10, int(h) + 20, 18)]
    d = "M" + " L ".join(f"{f(x)} {f(y)}" for x, y in crack)
    o = [mk.stars(50, w, h * 0.5, seed), hills(w * 0.5, h, base - 20, seed, color="#3A2A2E", amp=10),
         f'<g transform="translate({f(w * 0.52)} 0)">' + hills(w * 0.5, h, base - 10, seed + 1, color="#2A2A3E", amp=10) + '</g>',
         f'<path d="{d}" fill="none" stroke="#FFD23F" stroke-width="7" opacity="0.5"></path><path d="{d}" fill="none" stroke="#FFF4C2" stroke-width="2.4"></path>',
         man(p, w * 0.32, base, fit(base, h * 0.32), "#1F5FAD", flip=True), man(p, w * 0.7, base + 4, fit(base, h * 0.36), "#5E8F26")]
    o.append(label(w * 0.32, base + 22, "PELEG", "#FFD23F", 10) + label(w * 0.7, base + 22, "JOKTAN", "#FFD23F", 10))
    return "".join(o)

def mount_east(w, h, seed):
    """From Mesha toward Sephar, the mountain of the east."""
    base = h * 0.8
    return (sun(w * 0.7, h * 0.36, 18, color="#FFC14D", op=0.3)
            + f'<path d="M-10 {f(base)} L {f(w * 0.4)} {f(h * 0.38)} L {f(w * 0.56)} {f(h * 0.5)} L {f(w * 0.8)} {f(h * 0.3)} L {f(w + 10)} {f(base)} Z" fill="#5A3A4E" stroke="#0D0D0F" stroke-width="2"></path>'
            + ground(w, h, base, "#C8A06A", dy=0) + route([(w * 0.08, base + 16), (w * 0.5, base + 6), (w * 0.82, h * 0.36)], color="#FFD23F", sw=2.4)
            + label(w * 0.1, base + 34, "MESHA", "#12113A", 10, "start") + label(w * 0.86, h * 0.26, "SEPHAR", "#F3EFE6", 10))

def nations_spread(w, h, seed):
    """The nations divided in the earth after the flood: three colored streams of dots spreading from one point across the grid."""
    r = random.Random(seed); cx, cy = w * 0.36, h * 0.56; o = [grid_bg(w, h, color="#1E2E4A", bg="#0B1226")]
    for k, a0 in [("japheth", -0.9), ("shem", 0.0), ("ham", 0.9)]:
        for i in range(70):
            a = a0 + r.uniform(-0.38, 0.38); d = r.uniform(20, w * 0.7)
            x, y = cx + math.cos(a) * d, cy + math.sin(a) * d * 0.7
            o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(1.4, 3.4))}" fill="{SONS[k]}" opacity="{0.5 + r.random() * 0.5:.2f}"></circle>')
        o.append(route([(cx, cy), (cx + math.cos(a0) * w * 0.66, cy + math.sin(a0) * w * 0.46)], color=SONS[k], sw=2))
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="14" fill="none" stroke="#FFD23F" stroke-width="2.4"></circle><circle cx="{f(cx)}" cy="{f(cy)}" r="5" fill="#FFD23F"></circle>')
    o.append(label(cx, cy + 32, "ARARAT", "#FFD23F", 10))
    return "".join(o)

# ---- Genesis 11 -----------------------------------------------------------------------------------------
def babble(w, h, seed, color):
    """A speech balloon full of scribble that no one can read."""
    r = random.Random(seed); cx, cy = w * 0.5, h * 0.56; rx, ry = w * 0.38, h * 0.22
    marks = "".join(f'<path d="M{f(cx - rx * 0.7 + i * rx * 0.2)} {f(cy + r.uniform(-6, 6))} {r.choice(["c 6 -14 12 14 18 0", "l 8 -12 l 8 12", "q 9 -16 18 0 t 0 8", "m 0 -8 l 16 16 m 0 -16 l -16 16"])}" fill="none" stroke="#0D0D0F" stroke-width="3" stroke-linecap="round"></path>' for i in range(8))
    rays = mk.speed(cx, cy, 60, rx * 0.6, w, seed, color="#0D0D0F", sw=1, op=0.35)
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{color}"></rect>' + rays
            + f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="#ffffff" stroke="#0D0D0F" stroke-width="2.5"></ellipse>' + marks)

def scattering(p, w, h, seed):
    """They left off building the city: the unfinished tower, and the builders walking away in every direction."""
    base = h * 0.84; r = random.Random(seed)
    o = [sun(w * 0.5, base - h * 0.1, h * 0.2, color="#FF8A3D", op=0.25), ground(w, h, base, "#C8A06A", dy=0),
         TW.tower(w * 0.5, base, w * 0.3, h * 0.08, 7, 0.88, f"sc{seed}", unfinished=3)]
    for i in range(14):
        x = r.uniform(0.04, 0.96) * w; y = r.uniform(base + 6, h * 1.02); left = x < w * 0.5
        o.append(man(p, x, y, round(0.12 + 0.2 * (y - base) / (h - base + 1), 3), r.choice(["#5A3A22", "#8A3A1E", "#3A2214", "#4A3A6A", "#2C5F9A"]), flip=left))
    return "".join(o)

def ur(w, h, seed):
    """Ur of the Chaldees at night: a stepped temple-tower, the city on the river, the moon."""
    base = h * 0.78
    o = [mk.stars(70, w, h * 0.6, seed), f'<circle cx="{f(w * 0.82)}" cy="{f(h * 0.2)}" r="20" fill="#E8E2D6"></circle><circle cx="{f(w * 0.82 - 8)}" cy="{f(h * 0.2 - 4)}" r="18" fill="#12113A"></circle>',
         TW.tower(w * 0.36, base - 6, w * 0.3, h * 0.1, 3, 0.7, f"ur{seed}", unfinished=0, light="#C8A06A", dark="#5A3A2E", brick="#8A5A3E"),
         city(w * 0.72, base, w * 0.38, h * 0.3, seed, color="#3A2A3E"), city(w * 0.08, base, w * 0.2, h * 0.22, seed + 1, color="#3A2A3E"),
         f'<path d="M-10 {f(base)} L {f(w + 10)} {f(base)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1A2440" stroke="#0D0D0F" stroke-width="2"></path>',
         "".join(f'<path d="M{f(x)} {f(base + 14 + (x % 3) * 8)} c 16 -4 30 4 46 0" fill="none" stroke="#8FB8D8" stroke-width="1.6" opacity="0.5"></path>' for x in range(0, int(w), 70))]
    return "".join(o)

def two_couples(p, w, h, seed):
    """Abram and Sarai; Nahor and Milcah."""
    base = h * 0.86; s = fit(base, h * 0.3)
    return (sun(w * 0.5, base - 10, h * 0.2, color="#FFC14D", op=0.25) + hills(w, h, base, seed, color="#3A2A3E", amp=6)
            + abram(p, w * 0.14, base, s, flip=False) + sarai(p, w * 0.28, base, s * 0.93, flip=True)
            + man(p, w * 0.72, base, s * 0.98, "#4A3A6A", kind="Robe", extra=GREY_BEARD.replace("#B8B2A6", "#3A2A1E")) + woman(p, w * 0.86, base, s * 0.92, "#1F7A8C", flip=True)
            + label(w * 0.21, base + 22, "ABRAM · SARAI", "#FFD23F", 10) + label(w * 0.79, base + 22, "NAHOR · MILCAH", "#FFD23F", 10))

def journey_map(w, h, seed, legs, cur=None, color="#FFD23F", band=(0, 1)):
    """The fertile crescent as a technical map; legs = list of place names in order (the route so far)."""
    P = {"UR": (0.9, 0.84), "HARAN": (0.56, 0.12), "SHECHEM": (0.2, 0.42), "BETH-EL": (0.2, 0.52), "THE SOUTH": (0.16, 0.74), "EGYPT": (0.06, 0.9),
         "DAN": (0.24, 0.28), "HOBAH": (0.34, 0.2), "DAMASCUS": (0.32, 0.26), "MAMRE": (0.18, 0.62), "SODOM": (0.26, 0.66), "SALEM": (0.2, 0.58),
         "EUPHRATES": (0.7, 0.4)}
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.48)} -10 C {f(w * 0.6)} {f(h * 0.3)} {f(w * 0.74)} {f(h * 0.6)} {f(w * 0.98)} {f(h + 10)}" fill="none" stroke="#2C9DB8" stroke-width="4" opacity="0.7"></path>')
    o.append(f'<path d="M{f(w * 0.62)} -10 C {f(w * 0.72)} {f(h * 0.3)} {f(w * 0.84)} {f(h * 0.6)} {f(w * 1.02)} {f(h * 0.9)}" fill="none" stroke="#2C9DB8" stroke-width="3" opacity="0.5"></path>')
    o.append(f'<path d="M{f(w * 0.12)} -10 C {f(w * 0.1)} {f(h * 0.4)} {f(w * 0.08)} {f(h * 0.7)} {f(w * 0.0)} {f(h + 10)} L -10 {f(h + 10)} L -10 -10 Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    P = {k: (x, band[0] + (band[1] - band[0]) * y) for k, (x, y) in P.items()}
    pts = [(P[n][0] * w, P[n][1] * h) for n in legs]
    o.append(route(pts, color=color, sw=3))
    for n in legs:
        x, y = P[n][0] * w, P[n][1] * h
        o.append(node(x, y, n, "#D7261E" if n == cur else color, r=5, dy=-12 if y > h * 0.15 else 22, anchor="middle", size=10))
    return "".join(o)

# ---- Genesis 12 -----------------------------------------------------------------------------------------
def look_up(p, w, h, seed):
    """Abram under the night sky, alone on a hill, looking up into the light."""
    base = h * 0.88
    return (mk.stars(90, w, h, seed) + V.rays(w * 0.7, -30, 30, 30, h * 1.5, color="#FFF4C2", op=0.18)
            + f'<path d="M-10 {f(h + 10)} L -10 {f(base)} C {f(w * 0.3)} {f(base - 30)} {f(w * 0.6)} {f(base - 20)} {f(w + 10)} {f(base + 10)} L {f(w + 10)} {f(h + 10)} Z" fill="#12090A" stroke="#0D0D0F" stroke-width="2"></path>'
            + abram(p, w * 0.24, base - 20, fit(base, h * 0.5), up=[(-22, -158), (-6, -196), (14, -230)]))

def shechem(p, w, h, seed):
    """The oak of Moreh at Shechem; the Canaanite city on the hill beyond; Abram's tents beneath the oak."""
    base = h * 0.86
    return (sun(w * 0.86, h * 0.2, 14, op=0.2) + J.city_hill(w * 0.76, base - h * 0.14, w * 0.24, h * 0.24, seed)
            + ground(w, h, base - h * 0.14, "#7A9A4A", dy=4) + A4.great_oak(w * 0.24, base, round(h / 300, 3), seed=seed)
            + E4.tent(w * 0.52, base, w * 0.12, h * 0.16) + abram(p, w * 0.38, base + 4, fit(base, h * 0.5), staff=True, up=HOLD_STAFF))

def bethel(p, w, h, seed):
    """The mountain east of Beth-el: his tent, an altar with its smoke; Beth-el to the west, Ai to the east."""
    base = h * 0.86
    return (sun(w * 0.5, h * 0.18, 12, op=0.2) + hills(w, h, base - h * 0.2, seed, color="#8A7A5A", amp=10, step=50)
            + city(w * 0.08, base - h * 0.2, w * 0.16, h * 0.16, seed, color="#7A5A4A") + city(w * 0.92, base - h * 0.2, w * 0.14, h * 0.14, seed + 1, color="#7A5A4A")
            + f'<path d="M{f(w * 0.2)} {f(base + 10)} C {f(w * 0.36)} {f(base - h * 0.34)} {f(w * 0.64)} {f(base - h * 0.34)} {f(w * 0.8)} {f(base + 10)} Z" fill="#9A8A5A" stroke="#0D0D0F" stroke-width="2"></path>'
            + E4.tent(w * 0.4, base - h * 0.14, w * 0.14, h * 0.18) + A4.altar(w * 0.6, base - h * 0.16, round(h / 600, 3), seed=seed)
            + label(w * 0.08, base - h * 0.4, "BETH-EL", "#12113A", 9) + label(w * 0.92, base - h * 0.36, "AI", "#12113A", 9))

def southward(p, w, h, seed):
    """Going on still toward the South: a long road into the desert."""
    base = h * 0.6
    return (sun(w * 0.7, base - 10, h * 0.14, color="#FFE680", op=0.3) + ground(w, h, base, "#E8C88A", dy=0)
            + f'<path d="M{f(w * 0.2)} {f(h + 10)} L {f(w * 0.6)} {f(base)} L {f(w * 0.66)} {f(base)} L {f(w * 0.6)} {f(h + 10)} Z" fill="#C8A06A"></path>'
            + caravan(p, w * 0.44, w * 0.66, base + 6, 0.5, seed) + abram(p, w * 0.36, h * 0.92, fit(h * 0.92, h * 0.5), staff=True, up=HOLD_STAFF))

def famine(w, h, seed):
    """A famine in the land: cracked ground, withered stalks, a dead tree, bones of a beast, the white sun."""
    r = random.Random(seed); base = h * 0.62
    cr = "".join(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-24, 24))} {f(r.uniform(6, 16))} l {f(r.uniform(-16, 16))} {f(r.uniform(6, 14))}" fill="none" stroke="#6A4A3A" stroke-width="2"></path>'
                 for x, y in [(r.uniform(0, w), r.uniform(base + 10, h)) for _ in range(40)])
    stalks = "".join(f'<path d="M{f(x)} {f(base + 30)} C {f(x + 2)} {f(base + 10)} {f(x + 10)} {f(base)} {f(x + 18)} {f(base + 4)}" fill="none" stroke="#8A6A3A" stroke-width="2"></path>' for x in range(20, int(w * 0.4), 14))
    tree = (f'<path d="M{f(w * 0.74)} {f(base + 20)} L {f(w * 0.75)} {f(base - h * 0.3)} M{f(w * 0.75)} {f(base - h * 0.16)} L {f(w * 0.68)} {f(base - h * 0.28)} M{f(w * 0.75)} {f(base - h * 0.22)} L {f(w * 0.84)} {f(base - h * 0.34)}" '
            f'fill="none" stroke="#2A1A14" stroke-width="7" stroke-linecap="round"></path>')
    return (f'<circle cx="{f(w * 0.3)}" cy="{f(h * 0.2)}" r="{f(h * 0.12)}" fill="#FFF4C2"></circle>' + V.rays(w * 0.3, h * 0.2, 30, h * 0.14, w, color="#FFF4C2", op=0.4)
            + ground(w, h, base, "#C8885A", dy=0) + cr + stalks + tree + birds(4, w * 0.6, w * 0.95, h * 0.1, h * 0.3, seed, color="#2A1A14"))

def to_egypt(p, w, h, seed):
    """Near to enter into Egypt: the pyramids on the horizon, Abram and Sarai on the road."""
    base = h * 0.88; hz = h * 0.56
    return (sun(w * 0.7, hz - 30, h * 0.12, color="#FFC14D", op=0.3) + EG.pyramid(w * 0.66, hz, w * 0.22, h * 0.24) + EG.pyramid(w * 0.84, hz, w * 0.14, h * 0.15)
            + ground(w, h, hz, "#E8C88A", dy=0) + "".join(G1.palm(w * x, hz + 4, 0.3) for x in (0.4, 0.46, 0.94))
            + abram(p, w * 0.2, base, fit(base, h * 0.22), staff=True, up=HOLD_STAFF) + sarai(p, w * 0.32, base + 2, fit(base, h * 0.26)))

def beheld(p, w, h, seed):
    """The Egyptians beheld the woman: Sarai walking in the street, faces turning."""
    base = h * 0.9; r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{w + 20}" height="{f(h * 0.6)}" fill="#E8C88A"></rect>',
         "".join(f'<rect x="{f(x)}" y="{f(h * 0.06)}" width="{f(w * 0.05)}" height="{f(h * 0.6)}" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></rect>' for x in [w * k for k in (0.06, 0.3, 0.54, 0.78)]),
         ground(w, h, h * 0.66, "#C8A06A", dy=0)]
    for x in (0.08, 0.16, 0.66, 0.76, 0.86, 0.94):
        o.append(man(p, w * x, base - r.uniform(0, 14), fit(base, h * 0.5) * r.uniform(0.9, 1.0), "#F3EFE6", flip=x > 0.5, extra='<path d="M-14 -190 L 14 -190 L 18 -170 L -18 -170 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></path>'))
    o.append(sarai(p, w * 0.42, base + 6, fit(base, h * 0.5)))
    o.append(mk.speed(w * 0.42, base - h * 0.4, 30, h * 0.36, w, seed, color="#FFF4C2", op=0.5))
    return "".join(o)

def throne_room(p, w, h, seed):
    """Pharaoh's house: blue and gold columns, Pharaoh enthroned, his princes bowing, Sarai brought in."""
    base = h * 0.9
    o = [f'<rect x="-10" y="-10" width="{w + 20}" height="{h + 20}" fill="#1F3F7A"></rect>']
    for x in (0.06, 0.22, 0.78, 0.94):
        o.append(f'<rect x="{f(w * x - 16)}" y="-10" width="32" height="{f(base + 10)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></rect>'
                 + "".join(f'<path d="M{f(w * x - 16)} {f(y)} L {f(w * x + 16)} {f(y)}" stroke="#1F5FAD" stroke-width="5"></path>' for y in range(20, int(base), 34)))
    o.append(ground(w, h, base, "#C8A06A", dy=0))
    o.append(A3.throne(w * 0.5, base, round(h / 300, 3)))
    o.append(mk.person(p, round(w * 0.5), round(base - 26 * h / 300), round(fit(base, h * 0.22) * 0.8, 3), body="#8A4A2E", cloth="#F3EFE6", kind="Tunic", sw=3,
                       extra='<path d="M-18 -200 L 18 -200 L 26 -150 L 14 -160 L -14 -160 L -26 -150 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
                       '<path d="M-18 -186 L 18 -186 M-20 -174 L 20 -174 M-22 -162 L 22 -162" stroke="#1F5FAD" stroke-width="4"></path>'))
    o.append(E.kneel(w * 0.3, base + 2, round(h / 600, 3), color="#F3EFE6", skin="#8A4A2E", flip=False))
    o.append(E.kneel(w * 0.7, base + 2, round(h / 600, 3), color="#F3EFE6", skin="#8A4A2E", flip=True))
    o.append(sarai(p, w * 0.14, base, fit(base, h * 0.36)))
    return "".join(o)

def gifts(p, w, h, seed):
    """He had sheep, and oxen, and he-asses, and men-servants, and maid-servants, and she-asses, and camels."""
    base = h * 0.8
    return (ground(w, h, base - 30, "#C8A06A", dy=0) + EG.pyramid(w * 0.86, base - 30, w * 0.24, h * 0.28)
            + G1.camel(w * 0.16, base - 6, 0.34) + G1.camel(w * 0.3, base - 4, 0.3, flip=True)
            + N.ass(w * 0.46, base, 0.18) + N.ass(w * 0.56, base + 4, 0.16, flip=True)
            + man(p, w * 0.66, base, fit(base, h * 0.42), "#F3EFE6") + woman(p, w * 0.74, base, fit(base, h * 0.44), "#E8E2D6", flip=True)
            + flock(w * 0.02, w * 0.98, base + 6, h * 1.0, 10, seed, cows=0.35))

def plagued(w, h, seed):
    """Jehovah plagued Pharaoh and his house: the palace under a red sky, cracks of light, a sickness falling."""
    base = h * 0.84; r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{w + 20}" height="{h + 20}" fill="#3A0A0A"></rect>', V.rays(w * 0.5, -30, 30, 30, h * 1.4, color="#D7261E", op=0.3),
         f'<path d="M{f(w * 0.1)} {f(base)} L {f(w * 0.1)} {f(base - h * 0.4)} L {f(w * 0.9)} {f(base - h * 0.4)} L {f(w * 0.9)} {f(base)} Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    o += [f'<rect x="{f(w * x - 7)}" y="{f(base - h * 0.4)}" width="14" height="{f(h * 0.4)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></rect>' for x in (0.2, 0.35, 0.5, 0.65, 0.8)]
    o.append(f'<path d="M{f(w * 0.06)} {f(base - h * 0.4)} L {f(w * 0.94)} {f(base - h * 0.4)} L {f(w * 0.9)} {f(base - h * 0.48)} L {f(w * 0.1)} {f(base - h * 0.48)} Z" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(ground(w, h, base, "#2A0A0A", dy=0))
    o += [E2.bolt(w * x, -10, h * 0.5, seed + i, w=1.2) for i, x in enumerate((0.3, 0.72))]
    return "".join(o)

# ---- Genesis 13 -----------------------------------------------------------------------------------------
def riches(p, w, h, seed):
    """Up out of Egypt, very rich in cattle, in silver and in gold: the caravan, gold glinting in the packs."""
    base = h * 0.7
    o = [sun(w * 0.2, base - 20, h * 0.16, color="#FFE680", op=0.3), ground(w, h, base, "#E8C88A", dy=0), caravan(p, w * 0.08, w * 0.92, base + 10, 0.9, seed, flip=True)]
    o += [f'<g transform="translate({f(w * x)} {f(h * 0.92)})">' + "".join(f'<ellipse cx="{dx}" cy="{dy}" rx="9" ry="4" fill="{c}" stroke="#0D0D0F" stroke-width="1.2"></ellipse>'
          for dx, dy, c in [(-12, 0, "#E8B830"), (0, -5, "#C8C8D0"), (12, 0, "#E8B830"), (-6, -10, "#E8B830"), (6, -14, "#C8C8D0")]) + '</g>' for x in (0.2, 0.5, 0.8)]
    return "".join(o)

def old_altar(p, w, h, seed):
    """Unto the place of the altar which he had made there at the first: Abram kneeling at the old altar between Beth-el and Ai."""
    base = h * 0.86
    return (V.rays(w * 0.62, base - h * 0.5, 30, 30, w, color="#FFF4C2", op=0.3) + hills(w, h, base - h * 0.16, seed, color="#8A7A5A", amp=8)
            + city(w * 0.08, base - h * 0.16, w * 0.14, h * 0.14, seed, color="#7A5A4A") + city(w * 0.94, base - h * 0.16, w * 0.12, h * 0.12, seed + 1, color="#7A5A4A")
            + ground(w, h, base, "#9A8A5A", dy=0) + A4.altar(w * 0.62, base, round(h / 400, 3), seed=seed)
            + E.kneel(w * 0.4, base + 2, round(h / 380, 3), color=ABRAM_ROBE, skin=SKIN))

def crowded(w, h, seed):
    """The land not able to bear them: flocks and herds packed from edge to edge, two camps of tents."""
    base = h * 0.4
    return (ground(w, h, base, "#9A9A5A", dy=0) + "".join(E4.tent(w * x, base + 4, w * 0.08, h * 0.14) for x in (0.06, 0.14, 0.22, 0.7, 0.8, 0.9))
            + flock(-10, w + 10, base + 10, h * 1.05, 46, seed, cows=0.3, smin=0.14, smax=0.4))

def strife(p, w, h, seed):
    """Strife between the herdsmen: two men with staves raised over a well, the sheep scattering."""
    base = h * 0.88
    s = fit(base, h * 0.44)
    staff_up = '<path d="M14 -236 L 40 -310" stroke="#5A3A22" stroke-width="6" stroke-linecap="round"></path>'
    return (ground(w, h, base - 30, "#B5A06A", dy=0) + f'<ellipse cx="{f(w * 0.5)}" cy="{f(base - 6)}" rx="{f(w * 0.08)}" ry="14" fill="#5A5A6A" stroke="#0D0D0F" stroke-width="2.4"></ellipse><ellipse cx="{f(w * 0.5)}" cy="{f(base - 8)}" rx="{f(w * 0.06)}" ry="8" fill="#1F3F5A"></ellipse>'
            + man(p, w * 0.36, base, s, "#2C4A7A", up=[(-22, -158), (-6, -200), (14, -236)], extra=staff_up)
            + man(p, w * 0.64, base, s, "#7A2A3A", flip=True, up=[(-22, -158), (-6, -200), (14, -236)], extra=staff_up)
            + E.sheep(w * 0.12, base, 0.4, flip=True) + E.sheep(w * 0.2, base + 10, 0.34, flip=True) + E.sheep(w * 0.84, base + 6, 0.4) + E.sheep(w * 0.92, base - 4, 0.32)
            + mk.speed(w * 0.5, base - h * 0.5, 24, h * 0.2, w * 0.6, seed, color="#D7261E", op=0.5))

def plain_jordan(w, h, seed):
    """The Plain of the Jordan, well watered every where, like the garden of Jehovah: green fields, a winding river, cities shining far off."""
    r = random.Random(seed); hz = h * 0.4
    river = f'M{f(w * 0.46)} {f(hz)} C {f(w * 0.3)} {f(h * 0.56)} {f(w * 0.7)} {f(h * 0.7)} {f(w * 0.4)} {f(h + 10)} L {f(w * 0.56)} {f(h + 10)} C {f(w * 0.84)} {f(h * 0.7)} {f(w * 0.38)} {f(h * 0.56)} {f(w * 0.5)} {f(hz)} Z'
    o = [sun(w * 0.8, h * 0.14, 16, color="#FFE680", op=0.3), f'<path d="M-10 {f(hz)} L {f(w + 10)} {f(hz)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5E8F26" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="{river}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></path>']
    o += [f'<g opacity="0.85">' + city(w * x, hz + 4, w * 0.08, h * 0.12, seed + i, color="#E8C88A", lit="#FFD23F") + '</g>' for i, x in enumerate((0.16, 0.28, 0.66, 0.84))]
    o += [G1.palm(r.uniform(0, w), r.uniform(hz + 40, h * 1.0), r.uniform(0.3, 0.5)) for _ in range(8)]
    o += [f'<path d="M{f(x)} {f(y)} l 30 0" stroke="#9CCB5E" stroke-width="3"></path>' for x, y in [(r.uniform(0, w), r.uniform(hz + 10, h)) for _ in range(30)]]
    return "".join(o)

def parting_ways(p, w, h, seed):
    """They separated themselves: Lot's caravan going east to the green plain, Abram's going west into the hills."""
    base = h * 0.8
    return (f'<path d="M{f(w * 0.5)} -10 L {f(w + 10)} -10 L {f(w + 10)} {f(h + 10)} L {f(w * 0.5)} {f(h + 10)} Z" fill="#9CCB5E" opacity="0.4"></path>'
            + hills(w * 0.5, h, base - h * 0.3, seed, color="#8A7A5A", amp=14) + ground(w, h, base, "#C8A06A", dy=0)
            + f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="#F3EFE6" stroke-width="3" stroke-dasharray="10 8"></path>'
            + caravan(p, w * 0.06, w * 0.42, base + 4, 0.7, seed, flip=True) + caravan(p, w * 0.58, w * 0.94, base + 4, 0.7, seed + 2)
            + label(w * 0.25, h * 0.12, "← ABRAM", "#12113A", 12) + label(w * 0.75, h * 0.12, "LOT →", "#12113A", 12))

def sodom_sky(p, w, h, seed):
    """Lot pitched his tent toward Sodom: the city on the plain under a blood-red sky, its towers lit."""
    base = h * 0.82
    return (f'<circle cx="{f(w * 0.62)}" cy="{f(base - 20)}" r="{f(h * 0.3)}" fill="#D7261E" opacity="0.4"></circle>'
            + city(w * 0.64, base, w * 0.5, h * 0.5, seed, color="#2A0A1A", lit="#FF6A2A") + ground(w, h, base, "#3A1A1A", dy=0)
            + E4.tent(w * 0.16, base + 6, w * 0.14, h * 0.22, color="#5A2A22") + lot(p, w * 0.28, base + 8, fit(base, h * 0.4), flip=False)
            + label(w * 0.64, base + 24, "SODOM", "#FFD23F", 12))

def compass(p, w, h, seed):
    """Northward and southward and eastward and westward: Abram on the height, a compass ring around him over the land."""
    base = h * 0.82; cx, cy = w * 0.5, base - h * 0.2
    o = [sun(w * 0.8, h * 0.14, 14, op=0.2), hills(w, h, base - h * 0.06, seed, color="#7A8A5A", amp=10, step=50),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.4)} {f(base - h * 0.1)} {f(w * 0.6)} {f(base - h * 0.1)} {f(w * 0.7)} {f(h + 10)} Z" fill="#5A6A3A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<ellipse cx="{f(cx)}" cy="{f(base - 4)}" rx="{f(w * 0.36)}" ry="{f(h * 0.1)}" fill="none" stroke="#FFD23F" stroke-width="2.4" stroke-dasharray="6 5"></ellipse>']
    for nm, (x, y) in {"NORTH": (cx, base - 4 - h * 0.1), "SOUTH": (cx, base - 4 + h * 0.1), "EAST": (cx + w * 0.36, base - 4), "WEST": (cx - w * 0.36, base - 4)}.items():
        o.append(node(x, y, nm, "#FFD23F", r=4, dy=-10, size=10))
    o.append(abram(p, cx, base - h * 0.08, fit(base - h * 0.08, h * 0.46), staff=True, up=HOLD_STAFF))
    return "".join(o)

def dust(w, h, seed):
    """As the dust of the earth: a handful of dust running through the fingers in the light, every grain a point."""
    r = random.Random(seed)
    o = [V.rays(w * 0.5, h * 0.2, 30, 20, w, color="#FFE680", op=0.3)]
    o += [f'<circle cx="{f(w * 0.5 + r.gauss(0, w * 0.16))}" cy="{f(r.uniform(h * 0.4, h))}" r="{f(r.uniform(0.8, 2.6))}" fill="{r.choice(["#E8C88A", "#FFE680", "#C8A06A", "#FFF4C2"])}"></circle>' for _ in range(420)]
    o.append(E.hand(w * 0.5, h * 0.66, round(h / 520, 3), skin="#C98E66", uid=f"du{seed}").replace("<g ", '<g opacity="1" ', 1))
    return "".join(o)

def walk_land(p, w, h, seed):
    """Walk through the land in the length of it and in the breadth of it: a long road over the hills."""
    base = h * 0.86
    return (sun(w * 0.86, h * 0.2, 14, op=0.25) + hills(w, h, h * 0.5, seed, color="#7A8A5A", amp=14, step=70) + hills(w, h, h * 0.66, seed + 1, color="#5E7A3A", amp=10, step=90)
            + f'<path d="M{f(w * 0.1)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.72)} {f(w * 0.9)} {f(h * 0.5)}" fill="none" stroke="#E8C88A" stroke-width="16" stroke-linecap="round"></path>'
            + abram(p, w * 0.24, base, fit(base, h * 0.28), staff=True, up=HOLD_STAFF))

def mamre(p, w, h, seed):
    """The oaks of Mamre in Hebron: his tent among great oaks, a new altar with smoke."""
    base = h * 0.86
    return (sun(w * 0.5, h * 0.2, 14, color="#FFE680", op=0.25) + ground(w, h, base, "#7A9A4A", dy=0)
            + A4.great_oak(w * 0.08, base, round(h / 300, 3), seed=seed) + A4.great_oak(w * 0.7, base, round(h / 340, 3), seed=seed + 1)
            + G1.tent_big(w * 0.4, base, w * 0.3, h * 0.44, color="#3A2214", open_=True, glow="#5A2A12") + A4.altar(w * 0.78, base, round(h / 560, 3), seed=seed)
            + abram(p, w * 0.62, base + 4, fit(base, h * 0.46)))

# ---- Genesis 14 -----------------------------------------------------------------------------------------
def kings_row(p, w, h, seed, names, colors, flip=False):
    """Kings in a row, crowned, each named below."""
    base = h * 0.8; n = len(names)
    o = [ground(w, h, base, "#3A2A2E", dy=0)]
    for i, (nm, c) in enumerate(zip(names, colors)):
        x = w * (i + 0.5) / n
        o.append(king(p, x, base, fit(base, h * 0.38), c, flip=flip))
        lines = nm.split("|")
        for k, ln in enumerate(lines):
            o.append(label(x, base + 18 + k * 13, ln, "#FFD23F" if k == 0 else "#F3EFE6", 10 if k == 0 else 8.5))
    return "".join(o)

def tally(w, h, seed):
    """Twelve years they served; in the thirteenth year they rebelled: a row of thirteen marks, the last one red and broken."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12113A"></rect>']
    for i in range(14):
        x = w * (0.06 + i * 0.066); c = "#FFD23F" if i < 12 else "#D7261E"
        if i < 12: o.append(f'<rect x="{f(x)}" y="{f(h * 0.56)}" width="{f(w * 0.04)}" height="{f(h * 0.26)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
        elif i == 12: o.append(f'<path d="M{f(x)} {f(h * 0.56)} L {f(x + w * 0.04)} {f(h * 0.56)} L {f(x + w * 0.03)} {f(h * 0.66)} L {f(x + w * 0.05)} {f(h * 0.72)} L {f(x + w * 0.04)} {f(h * 0.82)} L {f(x)} {f(h * 0.82)} L {f(x + w * 0.012)} {f(h * 0.7)} Z" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></path>')
        else: o.append(f'<rect x="{f(x)}" y="{f(h * 0.56)}" width="{f(w * 0.04)}" height="{f(h * 0.26)}" fill="none" stroke="#D7261E" stroke-width="2" stroke-dasharray="4 3"></rect>')
        o.append(label(x + w * 0.02, h * 0.92, f"{i + 1:02d}", c if i < 13 else "#D7261E", 9))
    return "".join(o)

def campaign(w, h, seed):
    """The campaign of Chedorlaomer as a technical map: a red route through the peoples he smote."""
    P = [("ASHTEROTH-KARNAIM", 0.86, 0.1), ("HAM", 0.82, 0.26), ("SHAVEH-KIRIATHAIM", 0.8, 0.42), ("SEIR", 0.74, 0.78), ("EL-PARAN", 0.62, 0.92),
         ("EN-MISHPAT", 0.5, 0.78), ("HAZAZON-TAMAR", 0.6, 0.56)]
    o = [grid_bg(w, h, color="#3A1A1E", bg="#1A0A0E")]
    o.append(f'<ellipse cx="{f(w * 0.7)}" cy="{f(h * 0.6)}" rx="{f(w * 0.025)}" ry="{f(h * 0.16)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="1.6"></ellipse>')
    pts = [(w * x, h * y) for _, x, y in P]
    o.append(route([(w * 0.98, h * 0.02)] + pts, color="#D7261E", sw=3.4, dash="10 6"))
    for i, (nm, x, y) in enumerate(P):
        o.append(node(w * x, h * y, f"{i + 1:02d} {nm}", "#FF8A3D", r=4, dy=4, anchor="end" if x > 0.7 else "start", size=9).replace(f'x="{f(w * x)}" y="{f(h * y + 4)}"', f'x="{f(w * x + (-12 if x > 0.7 else 12))}" y="{f(h * y + 4)}"'))
    return "".join(o)

def battle_array(p, w, h, seed):
    """Four kings against the five in the vale of Siddim: two battle lines with spears and banners."""
    base = h * 0.9
    o = [V.rays(w * 0.5, base, 30, 30, w, color="#FF8A3D", op=0.2), hills(w, h, base - h * 0.36, seed, color="#4A2A2E", amp=8)]
    o.append(E4.warriors(p, 22, w * 0.02, w * 0.4, base - h * 0.3, base, seed, 0.2, 0.42, flip=False, cloth=("#1F5FAD", "#3A2214", "#5A1A4A")))
    o.append(E4.warriors(p, 22, w * 0.6, w * 0.98, base - h * 0.3, base, seed + 1, 0.2, 0.42, flip=True, cloth=("#8A3A1E", "#5A2A16", "#C9A86A")))
    o.append(king(p, w * 0.3, base - h * 0.34, fit(base - h * 0.34, h * 0.42), "#5A1A4A") + king(p, w * 0.7, base - h * 0.34, fit(base - h * 0.34, h * 0.42), "#B5421E", flip=True))
    o.append(label(w * 0.2, h * 0.1, "IV", "#FFD23F", 22) + label(w * 0.8, h * 0.1, "V", "#FFD23F", 22))
    return "".join(o)

def slime_pits(p, w, h, seed):
    """The vale full of slime pits: black pits steaming, kings falling into them, the rest fleeing to the mountain."""
    r = random.Random(seed); base = h * 0.6
    o = [f'<path d="M{f(w * 0.6)} {f(base)} L {f(w * 0.82)} {f(h * 0.08)} L {f(w + 10)} {f(h * 0.2)} L {f(w + 10)} {f(base)} Z" fill="#5A3A3E" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, base, "#8A6A4A", dy=0)]
    for x, y, pw in [(0.14, 0.76, 80), (0.38, 0.9, 110), (0.62, 0.74, 70), (0.3, 0.68, 50)]:
        o.append(f'<ellipse cx="{f(w * x)}" cy="{f(h * y)}" rx="{pw}" ry="{f(pw * 0.22)}" fill="#0D0D0F" stroke="#3A2A1E" stroke-width="3"></ellipse>'
                 + f'<path d="M{f(w * x - 10)} {f(h * y - 6)} c -6 -16 10 -24 4 -40" fill="none" stroke="#6A5A5A" stroke-width="5" opacity="0.5"></path>')
    o.append(king(p, w * 0.38, h * 0.9 + 6, fit(h * 0.9, h * 0.66) * 0.7, "#5A1A4A", up=[(-22, -158), (-40, -196), (-30, -232)]))
    o.append(f'<rect x="{f(w * 0.38 - 60)}" y="{f(h * 0.9 - 2)}" width="120" height="30" fill="#0D0D0F"></rect>')
    for i in range(7):
        x = w * (0.66 + i * 0.045); y = base - i * h * 0.06
        o.append(man(p, x, y, 0.16, r.choice(["#8A3A1E", "#C9A86A", "#5A2A16"])))
    return "".join(o)

def plunder(p, w, h, seed):
    """They took all the goods of Sodom and Gomorrah: a line of soldiers driving laden asses and bound captives away."""
    base = h * 0.84; r = random.Random(seed)
    o = [sun(w * 0.9, base - 20, h * 0.16, color="#FF8A3D", op=0.25), city(w * 0.9, base, w * 0.2, h * 0.36, seed, color="#3A1A1A", lit="#FF6A2A"),
         ground(w, h, base, "#8A6A4A", dy=0)]
    for i in range(6):
        x = w * (0.08 + i * 0.13)
        if i % 2: o.append(N.ass(x, base + 4, 0.2, flip=True) + R.sack(x - 6, base - 34, 0.6))
        else: o.append(man(p, x, base, fit(base, h * 0.36), r.choice(["#1F5FAD", "#5A1A4A"]), flip=True, extra='<path d="M10 -150 L 40 -260" stroke="#3A2214" stroke-width="4"></path><path d="M36 -260 L 44 -276 L 46 -258 Z" fill="#A8B0BA" stroke="#0D0D0F" stroke-width="1.2"></path>'))
    o.append(f'<path d="M{f(w * 0.12)} {f(base - 60)} C {f(w * 0.3)} {f(base - 50)} {f(w * 0.5)} {f(base - 70)} {f(w * 0.7)} {f(base - 56)}" fill="none" stroke="#C9A86A" stroke-width="2.4"></path>')
    return "".join(o)

def messenger(p, w, h, seed):
    """One that had escaped came running to Abram the Hebrew at the oaks of Mamre."""
    base = h * 0.86
    return (sun(w * 0.86, h * 0.24, 14, color="#FF8A3D", op=0.25) + ground(w, h, base, "#7A9A4A", dy=0) + A4.great_oak(w * 0.02, base, round(h / 300, 3), seed=seed)
            + G1.tent_big(w * 0.26, base, w * 0.24, h * 0.4, color="#3A2214") + abram(p, w * 0.44, base, fit(base, h * 0.52), flip=True)
            + A4.runner(p, w * 0.76, base + 2, fit(base, h * 0.52), flip=True, cloth="#C9A86A"))

def count318(p, w, h, seed):
    """He led forth his trained men, three hundred and eighteen: ranks of men with a counter."""
    base = h * 0.96
    o = [V.rays(w * 0.5, h * 0.2, 30, 30, w, color="#FF8A3D", op=0.2),
         E4.warriors(p, 60, w * 0.0, w * 1.0, h * 0.42, base, seed, 0.12, 0.34, flip=True, cloth=("#2C4A7A", "#3A2214", "#5A3A22"))]
    return "".join(o)

def night_raid(p, w, h, seed):
    """He divided himself against them by night: torches in two bands closing on a camp below, Damascus on the hill."""
    base = h * 0.86; r = random.Random(seed)
    o = [mk.stars(70, w, h * 0.5, seed), J.city_hill(w * 0.86, h * 0.5, w * 0.12, h * 0.16, seed), label(w * 0.86, h * 0.26, "DAMASCUS", "#8FB8D8", 9),
         hills(w, h, h * 0.56, seed, color="#12102A", amp=10), ground(w, h, base, "#1A1430", dy=0)]
    o += [E4.tent(w * x, h * 0.74, w * 0.06, h * 0.1, color="#2A1A14") for x in (0.42, 0.5, 0.58)]
    for side in (0, 1):
        for i in range(5):
            x = w * (0.06 + i * 0.06) if side == 0 else w * (0.94 - i * 0.06)
            o.append(G1.torchbearer(p, x, base + r.uniform(-6, 10), round(h / 900, 3), flip=side == 1, seed=seed + i + side * 10))
    return "".join(o)

def brought_back(p, w, h, seed):
    """He brought back all the goods, and Lot, and the women also, and the people: the long column homeward at dawn."""
    base = h * 0.84
    return (sun(w * 0.12, base - 10, h * 0.2, color="#FFC14D", op=0.3) + ground(w, h, base, "#C8A06A", dy=0)
            + abram(p, w * 0.14, base, fit(base, h * 0.5), staff=True, up=HOLD_STAFF) + lot(p, w * 0.24, base, fit(base, h * 0.5))
            + woman(p, w * 0.34, base, fit(base, h * 0.52), "#C2456A") + woman(p, w * 0.42, base, fit(base, h * 0.52), "#7A3BA8")
            + N.ass(w * 0.54, base + 4, 0.2) + R.sack(w * 0.54 - 6, base - 34, 0.6) + G1.camel(w * 0.68, base - 4, 0.32, rider="#2C4A7A")
            + E4.warriors(p, 10, w * 0.76, w * 0.98, base - 10, base + 6, seed, 0.3, 0.36, cloth=("#2C4A7A", "#3A2214")))

def kings_vale(p, w, h, seed):
    """The king of Sodom went out to meet him in the vale of Shaveh, the King's Vale."""
    base = h * 0.86
    return (sun(w * 0.5, base - h * 0.2, h * 0.16, color="#FFE680", op=0.25) + hills(w, h, base - h * 0.2, seed, color="#8A7A5A", amp=8)
            + ground(w, h, base, "#B5A06A", dy=0)
            + abram(p, w * 0.2, base, fit(base, h * 0.5), flip=False) + E4.warriors(p, 8, w * 0.0, w * 0.12, base - 6, base + 6, seed, 0.3, 0.36, cloth=("#2C4A7A", "#3A2214"))
            + king(p, w * 0.74, base, fit(base, h * 0.48), "#5A1A4A", flip=True) + man(p, w * 0.86, base, fit(base, h * 0.52), "#3A1A2A", flip=True) + man(p, w * 0.94, base, fit(base, h * 0.52), "#3A1A2A", flip=True))

def bread_wine(p, w, h, seed):
    """Melchizedek king of Salem brought forth bread and wine: a white-robed priest-king coming down from his city with loaf and cup."""
    base = h * 0.88
    hold = [(-22, -158), (8, -150), (34, -160)]
    gifts_ = ('<ellipse cx="38" cy="-166" rx="16" ry="9" fill="#D9A25A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
              '<path d="M46 -160 L 62 -160 L 58 -142 L 54 -138 L 54 -128 L 60 -124 L 48 -124 L 52 -128 L 52 -138 L 48 -142 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>'
              '<path d="M47 -158 L 61 -158" stroke="#8A0E16" stroke-width="4"></path>')
    return (V.rays(w * 0.62, base - h * 0.5, 36, 30, w, color="#FFF4C2", op=0.4) + J.city_hill(w * 0.82, base - h * 0.2, w * 0.2, h * 0.3, seed)
            + label(w * 0.82, base - h * 0.56, "SALEM", "#12113A", 10) + ground(w, h, base, "#C8A06A", dy=0)
            + mk.person(p, round(w * 0.56), round(base), fit(base, h * 0.22), body="#8A5A3E", cloth="#F3EFE6", sw=3, up=hold,
                        extra=WHITE_BEARD + CROWN.replace("#E8B830", "#FFD23F") + gifts_))

def tithe(w, h, seed):
    """He gave him a tenth of all: the spoil heaped as ten blocks, one of them set apart in gold."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12113A"></rect>']
    bw = w * 0.07
    for i in range(10):
        x = w * 0.08 + i * (bw + w * 0.015); c = "#FFD23F" if i == 9 else "#5A5A7A"
        y = h * (0.3 if i == 9 else 0.4)
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(bw)}" height="{f(h * 0.4)}" fill="{c}" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(label(w * 0.08 + 9 * (bw + w * 0.015) + bw / 2, h * 0.24, "1/10", "#FFD23F", 12))
    return "".join(o)

def thread_shoe(w, h, seed):
    """Not a thread nor a shoe-latchet: a sandal and a loose scarlet thread on the ground."""
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#C8A06A"></rect>'
            + E.sandal(w * 0.6, h * 0.62, round(h / 260, 3), -12)
            + f'<path d="M{f(w * 0.1)} {f(h * 0.8)} C {f(w * 0.2)} {f(h * 0.5)} {f(w * 0.3)} {f(h * 0.9)} {f(w * 0.42)} {f(h * 0.6)} S {f(w * 0.44)} {f(h * 0.3)} {f(w * 0.36)} {f(h * 0.4)}" fill="none" stroke="#0D0D0F" stroke-width="5" stroke-linecap="round"></path>'
            + f'<path d="M{f(w * 0.1)} {f(h * 0.8)} C {f(w * 0.2)} {f(h * 0.5)} {f(w * 0.3)} {f(h * 0.9)} {f(w * 0.42)} {f(h * 0.6)} S {f(w * 0.44)} {f(h * 0.3)} {f(w * 0.36)} {f(h * 0.4)}" fill="none" stroke="#B5121B" stroke-width="2.6" stroke-linecap="round"></path>'
            + f'<path d="M{f(w * 0.06)} {f(h * 0.1)} L {f(w * 0.94)} {f(h * 0.9)} M{f(w * 0.94)} {f(h * 0.1)} L {f(w * 0.06)} {f(h * 0.9)}" stroke="#D7261E" stroke-width="6" opacity="0.6"></path>')

def allies(p, w, h, seed):
    """Aner, Eshcol and Mamre with the young men eating by the fire."""
    base = h * 0.88
    o = [mk.stars(40, w, h * 0.4, seed), ground(w, h, base, "#3A2A1E", dy=0), E.blaze(w * 0.5, base, 40, 60, seed), E4.basket(w * 0.4, base + 6, 1.6), E4.basket(w * 0.6, base + 6, 1.6)]
    for i, (nm, c) in enumerate([("ANER", "#5E8F26"), ("ESHCOL", "#1F7A8C"), ("MAMRE", "#B5421E")]):
        x = w * (0.12 + i * 0.1)
        o.append(man(p, x, base, fit(base, h * 0.3), c, kind="Robe", extra=GREY_BEARD.replace("#B8B2A6", "#3A2A1E")) + label(x, base + 16, nm, "#FFD23F", 9.5))
    o += [E.kneel(w * x, base + 2, round(h / 560, 3), color="#5A3A22", skin=SKIN, flip=True) for x in (0.72, 0.82, 0.92)]
    return "".join(o)

# ---- Genesis 15 -----------------------------------------------------------------------------------------
def star_count(p, w, h, seed):
    """Number the stars: Abram on a hilltop under the galaxy; a counter running at the side."""
    r = random.Random(seed); base = h * 0.88
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0B0B2A"></rect>',
         f'<path d="M-10 {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.3)} {f(w * 0.6)} {f(h * 0.2)} {f(w + 10)} {f(-10)}" fill="none" stroke="#5B2470" stroke-width="{f(h * 0.3)}" opacity="0.45"></path>',
         mk.stars(420, w, h * 0.9, seed), mk.stars(80, w, h * 0.7, seed + 1, color="#FFE680")]
    o += [f'<path d="M{f(x)} {f(y - 9)} L {f(x + 2)} {f(y - 2)} L {f(x + 9)} {f(y)} L {f(x + 2)} {f(y + 2)} L {f(x)} {f(y + 9)} L {f(x - 2)} {f(y + 2)} L {f(x - 9)} {f(y)} L {f(x - 2)} {f(y - 2)} Z" fill="#FFF4C2"></path>' for x, y in [(r.uniform(0, w), r.uniform(0, h * 0.6)) for _ in range(6)]]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(base)} C {f(w * 0.2)} {f(base - 30)} {f(w * 0.5)} {f(base - 26)} {f(w + 10)} {f(base + 10)} L {f(w + 10)} {f(h + 10)} Z" fill="#05050A" stroke="#3A2A6A" stroke-width="2"></path>')
    o.append(mk.person(p, round(w * 0.38), round(base - 22), fit(base - 22, h * 0.42), body="#05050A", stroke="#7A6AE0", sw=2.4, up=[(-22, -158), (0, -200), (22, -246)]))
    for i, (t, c) in enumerate([("STAR COUNT ··· 001,284", "#8F9AFF"), ("STAR COUNT ··· 048,911", "#8F9AFF"), ("STAR COUNT ··· OVERFLOW", "#FFD23F")]):
        o.append(label(16, h * 0.9 + i * 13 - 30, t, c, 9.5, "start"))
    return "".join(o)

def offerings(w, h, seed):
    """A heifer, a she-goat and a ram, each three years old, a turtle-dove and a young pigeon."""
    base = h * 0.84
    goat = lambda x, y, s: E.sheep(x, y, s, wool="#3A2A22", face="#2A1A10")
    ram = (lambda x, y, s: E.sheep(x, y, s) + f'<path d="M{f(x + 26 * s)} {f(y - 54 * s)} c 10 -8 18 4 8 12" fill="none" stroke="#8A6A3A" stroke-width="{f(5 * s)}"></path>')
    o = [V.rays(w * 0.5, -30, 30, 30, h * 1.3, color="#FFF4C2", op=0.3), ground(w, h, base, "#B5A06A", dy=0),
         A.cow(w * 0.16, base + 4, 0.42, color="#B5652E"), goat(w * 0.4, base + 6, 0.5), ram(w * 0.6, base + 6, 0.52),
         Y.dove(w * 0.78, base - 10, 0.7), Y.dove(w * 0.9, base - 6, 0.6, flip=True, wings="down")]
    for nm, x in [("HEIFER", 0.16), ("SHE-GOAT", 0.4), ("RAM", 0.6), ("TURTLE-DOVE", 0.78), ("PIGEON", 0.92)]:
        o.append(label(w * x, base + 20, nm, "#12113A", 9))
    return "".join(o)

def pieces(w, h, seed):
    """Laid each half over against the other: two rows of stones with the offerings upon them, covered, and a path between; the birds whole."""
    base = h * 0.86
    o = [sun(w * 0.86, h * 0.2, 16, color="#FFC14D", op=0.25), ground(w, h, h * 0.4, "#B5A06A", dy=0),
         f'<path d="M{f(w * 0.46)} {f(h * 0.4)} L {f(w * 0.54)} {f(h * 0.4)} L {f(w * 0.7)} {f(h + 10)} L {f(w * 0.3)} {f(h + 10)} Z" fill="#D8C08A" stroke="#0D0D0F" stroke-width="1.6"></path>']
    for side in (-1, 1):
        for i in range(3):
            t = (i + 1) / 3.6; y = h * 0.4 + (base - h * 0.4) * t; x = w * 0.5 + side * w * (0.1 + 0.18 * t)
            sw = 50 + 70 * t
            o.append(f'<rect x="{f(x - sw / 2)}" y="{f(y - 10 * (0.6 + t))}" width="{f(sw)}" height="{f(12 * (0.6 + t))}" rx="4" fill="#8A8478" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                     f'<path d="M{f(x - sw * 0.4)} {f(y - 10 * (0.6 + t))} C {f(x - sw * 0.3)} {f(y - 34 * (0.6 + t))} {f(x + sw * 0.3)} {f(y - 34 * (0.6 + t))} {f(x + sw * 0.4)} {f(y - 10 * (0.6 + t))} Z" fill="#E2D8C4" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append(Y.dove(w * 0.14, h * 0.9, 0.6, wings="down") + Y.dove(w * 0.86, h * 0.92, 0.6, flip=True, wings="down"))
    return "".join(o)

def prey(p, w, h, seed):
    """The birds of prey came down upon the carcasses, and Abram drove them away."""
    r = random.Random(seed); base = h * 0.88
    vult = lambda x, y, s, fl: (f'<g transform="translate({f(x)} {f(y)}) scale({f(-s if fl else s)} {f(s)})">'
                                '<path d="M-60 -10 C -40 -30 -16 -26 0 -10 C 16 -26 40 -30 60 -10 L 50 -6 L 40 -12 L 30 -4 L 20 -10 L 8 0 L -8 0 L -20 -10 L -30 -4 L -40 -12 L -50 -6 Z" fill="#2A1A14" stroke="#0D0D0F" stroke-width="2"></path>'
                                '<path d="M-6 -2 C -6 10 6 10 6 -2 Z" fill="#2A1A14" stroke="#0D0D0F" stroke-width="2"></path><circle cx="0" cy="-12" r="5" fill="#C8888A" stroke="#0D0D0F" stroke-width="1.4"></circle>'
                                '<path d="M4 -12 L 12 -8 L 4 -8 Z" fill="#E8C88A"></path></g>')
    o = [sun(w * 0.8, h * 0.24, 18, color="#FFC14D", op=0.3), ground(w, h, base - h * 0.1, "#B5A06A", dy=0)]
    o += [vult(r.uniform(w * 0.4, w * 0.95), r.uniform(h * 0.08, h * 0.5), r.uniform(0.4, 0.8), r.random() < 0.5) for _ in range(6)]
    raised = '<path d="M10 -240 L 34 -330" stroke="#0D0D0F" stroke-width="8" stroke-linecap="round"></path><path d="M10 -240 L 34 -330" stroke="#8A5A30" stroke-width="5" stroke-linecap="round"></path>'
    o.append(mk.person(p, round(w * 0.26), round(base), fit(base, h * 0.3), body=SKIN, cloth=ABRAM_ROBE, sw=3, up=[(-22, -158), (-8, -200), (10, -240)], extra=GREY_BEARD + raised))
    o.append(mk.speed(w * 0.3, h * 0.3, 18, h * 0.1, h * 0.4, seed, color="#F3EFE6", op=0.5))
    return "".join(o)

def deep_sleep(p, w, h, seed):
    """A deep sleep fell upon Abram; a horror of great darkness: the sun gone down, a black vortex over the sleeper."""
    r = random.Random(seed); base = h * 0.84
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0B0510"></rect>',
         f'<circle cx="{f(w * 0.5)}" cy="{f(base + 6)}" r="{f(h * 0.3)}" fill="#8A1A1A" opacity="0.5"></circle>']
    for i in range(10):
        rr = h * (0.1 + i * 0.09)
        o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.3)}" rx="{f(rr * 2.2)}" ry="{f(rr * 0.7)}" fill="none" stroke="#3A1A5A" stroke-width="{f(2 + i)}" opacity="{0.6 - i * 0.05:.2f}" transform="rotate({r.uniform(-8, 8):.1f} {f(w * 0.5)} {f(h * 0.3)})"></ellipse>')
    o.append(ground(w, h, base, "#12090A", dy=0))
    o.append(f'<g transform="translate({f(w * 0.6)} {f(base + 2)}) scale({f(h / 260)})" fill="#2C4A7A" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use><use href="#{p}LieA"></use></g>')
    return "".join(o)

def bondage(p, w, h, seed):
    """Thy seed shall be sojourners in a land that is not theirs: bowed figures under burdens before a brick wall and a pyramid, in a red light."""
    base = h * 0.86; r = random.Random(seed)
    o = [V.rays(w * 0.8, base - 30, 30, 30, w, color="#FF6A2A", op=0.25), EG.pyramid(w * 0.82, base, w * 0.3, h * 0.5),
         f'<path d="M-10 {f(base)} L {f(w * 0.6)} {f(base)} L {f(w * 0.6)} {f(base - h * 0.34)} L -10 {f(base - h * 0.4)} Z" fill="#9A4A2A" stroke="#0D0D0F" stroke-width="2"></path>']
    o += [f'<path d="M-10 {f(base - h * 0.34 + k * 14)} L {f(w * 0.6)} {f(base - h * 0.3 + k * 14)}" stroke="#5A2A16" stroke-width="1.4"></path>' for k in range(int(h * 0.3 / 14))]
    o.append(ground(w, h, base, "#C8885A", dy=0))
    for i in range(6):
        x = w * (0.08 + i * 0.12)
        o.append(E.kneel(x, base + 4, round(h / 700, 3), color="#5A3A22", skin="#3A1E14") + R.sack(x + 10, base - h * 0.2, 0.5))
    return "".join(o)

def going_out(p, w, h, seed):
    """Afterward shall they come out with great substance: a multitude walking out at dawn with laden beasts."""
    base = h * 0.86
    return (sun(w * 0.86, base - 20, h * 0.24, color="#FFC14D", op=0.35) + ground(w, h, base - h * 0.2, "#C8A06A", dy=0)
            + E4.warriors(p, 40, w * 0.0, w * 0.8, base - h * 0.2, base + 10, seed, 0.12, 0.3, cloth=("#5A3A22", "#8A6A4A", "#C9A86A", "#2C4A7A"))
            + G1.camel(w * 0.7, base - 2, 0.3) + N.ass(w * 0.58, base + 6, 0.18) + R.sack(w * 0.58 - 6, base - 28, 0.5))

def four_generations(w, h, seed):
    """In the fourth generation they shall come hither again: four linked nodes along a path that turns back."""
    o = [mk.stars(60, w, h, seed)]
    pts = [(w * 0.1, h * 0.7), (w * 0.34, h * 0.4), (w * 0.62, h * 0.4), (w * 0.88, h * 0.7)]
    o.append(route(pts, color="#FFD23F", sw=2.6))
    for i, (x, y) in enumerate(pts):
        c = "#D7261E" if i == 3 else "#FFD23F"
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="14" fill="#12113A" stroke="{c}" stroke-width="3"></circle><circle cx="{f(x)}" cy="{f(y)}" r="5" fill="{c}"></circle>'
                 + label(x, y + 34, ["I", "II", "III", "IV"][i], c, 14))
    return "".join(o)

def furnace(w, h, seed):
    """A smoking furnace and a flaming torch that passed between these pieces, in the dark."""
    r = random.Random(seed); base = h * 0.86
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#05050A"></rect>', mk.stars(50, w, h * 0.4, seed),
         f'<path d="M-10 {f(base)} L {f(w + 10)} {f(base)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#12090A"></path>']
    for side in (-1, 1):
        for i in range(3):
            t = (i + 1) / 3.4; y = h * 0.56 + (base - h * 0.56) * t; x = w * 0.5 + side * w * (0.08 + 0.2 * t)
            sw = 40 + 70 * t
            o.append(f'<rect x="{f(x - sw / 2)}" y="{f(y - 8 * (0.6 + t))}" width="{f(sw)}" height="{f(10 * (0.6 + t))}" rx="4" fill="#2A2420" stroke="#5A3A2A" stroke-width="1.4"></rect>'
                     f'<path d="M{f(x - sw * 0.4)} {f(y - 8 * (0.6 + t))} C {f(x - sw * 0.3)} {f(y - 28 * (0.6 + t))} {f(x + sw * 0.3)} {f(y - 28 * (0.6 + t))} {f(x + sw * 0.4)} {f(y - 8 * (0.6 + t))} Z" fill="#3A2A26" stroke="#FF8A3D" stroke-width="1.4"></path>')
    fx, fy = w * 0.46, h * 0.68
    o.append(f'<circle cx="{f(fx)}" cy="{f(fy)}" r="{f(h * 0.3)}" fill="#FF6A2A" opacity="0.18"></circle>')
    o.append(f'<path d="M{f(fx)} {f(fy - 40)} C {f(fx - 60)} {f(fy - 120)} {f(fx + 50)} {f(fy - 180)} {f(fx - 20)} {f(-20)}" fill="none" stroke="#4A3A3E" stroke-width="40" stroke-linecap="round" opacity="0.7"></path>')
    o.append(f'<path d="M{f(fx - 40)} {f(fy + 30)} L {f(fx - 34)} {f(fy - 30)} C {f(fx - 30)} {f(fy - 50)} {f(fx + 30)} {f(fy - 50)} {f(fx + 34)} {f(fy - 30)} L {f(fx + 40)} {f(fy + 30)} Z" fill="#3A2A26" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(fx - 14)} {f(fy + 30)} L {f(fx - 14)} {f(fy + 4)} C {f(fx - 14)} {f(fy - 8)} {f(fx + 14)} {f(fy - 8)} {f(fx + 14)} {f(fy + 4)} L {f(fx + 14)} {f(fy + 30)} Z" fill="#FFD23F"></path>'
             + E.flame(fx, fy + 24, 12, 26, 0))
    tx, ty = w * 0.6, h * 0.56
    o.append(f'<path d="M{f(tx)} {f(ty + 60)} L {f(tx + 6)} {f(ty)}" stroke="#5A3A22" stroke-width="7" stroke-linecap="round"></path>' + E.flame(tx + 6, ty + 4, 22, 70, 6)
             + f'<circle cx="{f(tx + 6)}" cy="{f(ty - 20)}" r="{f(h * 0.16)}" fill="#FFC14D" opacity="0.25"></circle>')
    o += [f'<circle cx="{f(tx + r.uniform(-30, 30))}" cy="{f(ty - r.uniform(30, 120))}" r="{f(r.uniform(1, 2.6))}" fill="#FFD23F"></circle>' for _ in range(20)]
    return "".join(o)

def land_grant(w, h, seed):
    """From the river of Egypt unto the great river, the river Euphrates: the land marked out on a technical map."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.14)} -10 C {f(w * 0.12)} {f(h * 0.4)} {f(w * 0.1)} {f(h * 0.7)} {f(w * 0.02)} {f(h + 10)} L -10 {f(h + 10)} L -10 -10 Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.5)} -10 C {f(w * 0.64)} {f(h * 0.3)} {f(w * 0.8)} {f(h * 0.6)} {f(w * 1.0)} {f(h + 10)}" fill="none" stroke="#2C9DB8" stroke-width="5"></path>')
    o.append(f'<path d="M{f(w * 0.06)} {f(h * 0.92)} C {f(w * 0.1)} {f(h * 0.86)} {f(w * 0.12)} {f(h * 0.8)} {f(w * 0.16)} {f(h * 0.82)}" fill="none" stroke="#2C9DB8" stroke-width="3"></path>')
    o.append(f'<path d="M{f(w * 0.16)} {f(h * 0.84)} L {f(w * 0.14)} {f(h * 0.1)} L {f(w * 0.56)} {f(h * 0.06)} C {f(w * 0.66)} {f(h * 0.3)} {f(w * 0.78)} {f(h * 0.56)} {f(w * 0.84)} {f(h * 0.7)} L {f(w * 0.4)} {f(h * 0.92)} Z" '
             f'fill="#FFD23F" fill-opacity="0.14" stroke="#FFD23F" stroke-width="2.4" stroke-dasharray="9 5"></path>')
    o.append(node(w * 0.14, h * 0.86, "RIVER OF EGYPT", "#8FD0E2", r=5, dy=22, anchor="start", size=9.5) + node(w * 0.88, h * 0.82, "EUPHRATES", "#8FD0E2", r=5, dy=-12, anchor="end", size=9.5))
    return "".join(o)

def panorama(w, h, seed):
    """All the land which thou seest: hills and valleys rolling away to the edge of the sky."""
    o = [sun(w * 0.5, h * 0.3, 16, color="#FFE680", op=0.3)]
    for i, (c, y) in enumerate([("#9AAA7A", 0.42), ("#7A9A5A", 0.54), ("#5E7A3A", 0.68), ("#3F5A2A", 0.84)]):
        o.append(hills(w, h, h * y, seed + i, color=c, amp=10 + i * 4, step=60 + i * 20))
    return "".join(o)

def peoples(p, w, h, seed):
    """The Kenite, the Kenizzite, the Kadmonite, the Hittite, the Perizzite, the Rephaim, the Amorite, the Canaanite, the Girgashite and the Jebusite: ten peoples on the land under the stars."""
    r = random.Random(seed); base = h * 0.9
    o = [mk.stars(60, w, h * 0.6, seed), ground(w, h, base, "#1A1430", dy=0)]
    for i in range(10):
        x = w * (0.05 + i * 0.1)
        o.append(man(p, x, base, fit(base, h * 0.6) * (1.3 if i == 5 else 1.0), r.choice(["#5A3A22", "#3A2214", "#4A3A6A", "#5A1A16", "#2C5F9A"]), flip=i % 2 == 1, kind="Robe", body="#12090A"))
    return "".join(o)
