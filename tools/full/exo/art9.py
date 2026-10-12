"""Blueprints for Exodus chapter 9 (Exodus 28–31): the holy garments (ephod, onyx stones, breastplate of twelve stones,
robe of blue with bells and pomegranates, the plate HOLY TO JEHOVAH), the consecration (no carcasses: the beasts are
shown whole, the offerings as fire on the altar), the altar of incense, the half shekel, the laver, the anointing oil and
the incense as charts, Bezalel and Oholiab, the sabbath.

Each function f(w, h) draws a whole panel, using art8's blueprint kit (bp, dim, box, tag). The drawing keeps to the
right-hand part of the panel (from w * 0.5 rightward) where the panel's words sit at the left."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V, samuel1 as S1, samuel4 as A4
from genesis.art3 import label
from exo import art as A
from exo.art8 import bp, dim, box, tag, title_bar, INK, CY, GOLD, SILVER, BRASS, BLUE, PURPLE, SCARLET, LINEN, cherub
def f(v): return f"{v:.1f}"

ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")
SKIN = "#A8704E"
TRIBES = ["REUBEN", "SIMEON", "LEVI", "JUDAH", "DAN", "NAPHTALI", "GAD", "ASHER", "ISSACHAR", "ZEBULUN", "JOSEPH", "BENJAMIN"]
STONES = [("SARDIUS", "#C8202A"), ("TOPAZ", "#E8C840"), ("CARBUNCLE", "#E04A2A"), ("EMERALD", "#2E9A4A"), ("SAPPHIRE", "#1F5FAD"), ("DIAMOND", "#E8F6FA"),
          ("JACINTH", "#E87A2A"), ("AGATE", "#B88A6A"), ("AMETHYST", "#8A4AC8"), ("BERYL", "#5AC8C8"), ("ONYX", "#2A2A3A"), ("JASPER", "#7A9A5A")]

# ---- the high priest's figure (local units: feet at 0, head at -188) ---------------------------------------------
def high_priest(p, x, y, s, flip=False, up=None):
    """Aaron in the holy garments: the robe of blue with bells and pomegranates at the hem, the ephod of gold, blue, purple
    and scarlet with its woven band, the breastplate of twelve stones, the linen mitre with the gold plate."""
    hem = "".join(f'<circle cx="{-26 + i * 6.5}" cy="-4" r="2.6" fill="{GOLD if i % 2 else SCARLET}" stroke="#0D0D0F" stroke-width="0.8"></circle>' for i in range(9))
    ephod = ('<path d="M-18 -160 L 18 -160 L 20 -104 L -20 -104 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.8"></path>'
             + "".join(f'<path d="M-19 {-150 + k * 11} L 19 {-150 + k * 11}" stroke="{c}" stroke-width="3"></path>' for k, c in enumerate((BLUE, PURPLE, SCARLET, BLUE)))
             + '<path d="M-21 -112 L 21 -112" stroke="#E8B830" stroke-width="6"></path><path d="M-21 -112 L 21 -112" stroke="#0D0D0F" stroke-width="0.8" stroke-dasharray="2 2"></path>')
    plate = ('<rect x="-11" y="-158" width="22" height="22" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></rect>'
             + "".join(f'<circle cx="{-6 + (i % 3) * 6}" cy="{-153 + (i // 3) * 5}" r="2" fill="{STONES[i][1]}"></circle>' for i in range(12)))
    mitre = ('<path d="M-14 -192 C -16 -212 16 -212 14 -192 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path>'
             '<path d="M-12 -198 L 12 -198" stroke="#0D0D0F" stroke-width="0.8" opacity="0.5"></path><rect x="-6" y="-200" width="12" height="5" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></rect>')
    beard = A.GREY_BEARD
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=BLUE, sw=3, flip=flip, up=up, extra=hem + ephod + plate + beard + mitre)

def son_priest(p, x, y, s, flip=False, up=None):
    """A son of Aaron: the white linen coat, girdle and head-tire."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#F3EFE6", sw=3, flip=flip, up=up,
                     extra='<path d="M-20 -110 L 20 -110" stroke="#1F5FAD" stroke-width="5"></path><path d="M-13 -192 C -14 -208 14 -208 13 -192 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path>')

def stage(p, w, h, cast, x0=0.52, x1=0.96):
    """A blueprint floor with figures standing on it, spread from x0 to x1 of the width."""
    b = h * 0.9; n = len(cast)
    o = [bp(w, h), f'<path d="M{f(w * x0 - 20)} {f(b)} L {f(w * x1 + 10)} {f(b)}" stroke="{CY}" stroke-width="1.6"></path>', mk.defs(p, *ALL)]
    for i, (fn, top) in enumerate(cast):
        x = w * (x0 + (x1 - x0) * (i + 0.5) / n)
        o.append(fn(p, x, b, max(0.2, min((b - h * top) / 205, w * (x1 - x0) / n / 62, 1.25))))     # never wider than its share of the floor
    return "".join(o)

# ---- Exodus 28 ----
def priests(w, h):
    return stage("q1", w, h, [(high_priest, 0.12)] + [(son_priest, 0.24)] * 4) + title_bar(w, "AARON · NADAB · ABIHU · ELEAZAR · ITHAMAR")

def garments(w, h):
    """The six garments of 28:4 as an exploded parts list."""
    o = [bp(w, h), title_bar(w, "THE HOLY GARMENTS · PARTS")]
    x0 = w * 0.6; cw = (w * 0.38) / 3; ch = (h - 40) / 2
    parts = [("BREASTPLATE", lambda x, y, s: f'<rect x="{f(x - 18 * s)}" y="{f(y - 18 * s)}" width="{f(36 * s)}" height="{f(36 * s)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2"></rect>' + "".join(f'<circle cx="{f(x + (-10 + (i % 3) * 10) * s)}" cy="{f(y + (-12 + (i // 3) * 8) * s)}" r="{f(3 * s)}" fill="{STONES[i][1]}"></circle>' for i in range(12))),
             ("EPHOD", lambda x, y, s: f'<path d="M{f(x - 22 * s)} {f(y - 24 * s)} L {f(x + 22 * s)} {f(y - 24 * s)} L {f(x + 24 * s)} {f(y + 24 * s)} L {f(x - 24 * s)} {f(y + 24 * s)} Z" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2"></path>' + "".join(f'<path d="M{f(x - 22 * s)} {f(y + (-14 + k * 10) * s)} L {f(x + 22 * s)} {f(y + (-14 + k * 10) * s)}" stroke="{c}" stroke-width="{f(3 * s)}"></path>' for k, c in enumerate((BLUE, PURPLE, SCARLET)))),
             ("ROBE", lambda x, y, s: f'<path d="M{f(x - 14 * s)} {f(y - 28 * s)} L {f(x + 14 * s)} {f(y - 28 * s)} L {f(x + 26 * s)} {f(y + 28 * s)} L {f(x - 26 * s)} {f(y + 28 * s)} Z" fill="{BLUE}" stroke="#0D0D0F" stroke-width="2"></path>' + "".join(f'<circle cx="{f(x + (-22 + i * 7.3) * s)}" cy="{f(y + 26 * s)}" r="{f(2.6 * s)}" fill="{GOLD if i % 2 else SCARLET}"></circle>' for i in range(7))),
             ("COAT · CHECKER WORK", lambda x, y, s: f'<path d="M{f(x - 14 * s)} {f(y - 28 * s)} L {f(x + 14 * s)} {f(y - 28 * s)} L {f(x + 22 * s)} {f(y + 28 * s)} L {f(x - 22 * s)} {f(y + 28 * s)} Z" fill="{LINEN}" stroke="#0D0D0F" stroke-width="2"></path>' + "".join(f'<rect x="{f(x + (-12 + (i % 4) * 6) * s)}" y="{f(y + (-20 + (i // 4) * 8) * s)}" width="{f(3 * s)}" height="{f(3 * s)}" fill="#C8C2B6"></rect>' for i in range(24))),
             ("MITRE", lambda x, y, s: f'<path d="M{f(x - 22 * s)} {f(y + 10 * s)} C {f(x - 26 * s)} {f(y - 26 * s)} {f(x + 26 * s)} {f(y - 26 * s)} {f(x + 22 * s)} {f(y + 10 * s)} Z" fill="{LINEN}" stroke="#0D0D0F" stroke-width="2"></path><rect x="{f(x - 9 * s)}" y="{f(y - 2 * s)}" width="{f(18 * s)}" height="{f(7 * s)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1"></rect>'),
             ("GIRDLE", lambda x, y, s: f'<path d="M{f(x - 28 * s)} {f(y)} C {f(x - 10 * s)} {f(y - 8 * s)} {f(x + 10 * s)} {f(y + 8 * s)} {f(x + 28 * s)} {f(y)}" fill="none" stroke="{BLUE}" stroke-width="{f(7 * s)}"></path><path d="M{f(x + 20 * s)} {f(y)} L {f(x + 24 * s)} {f(y + 24 * s)} M{f(x + 26 * s)} {f(y)} L {f(x + 32 * s)} {f(y + 22 * s)}" stroke="{SCARLET}" stroke-width="{f(3 * s)}"></path>')]
    for i, (nm, fn) in enumerate(parts):
        x = x0 + (i % 3) * cw + cw / 2; y = 34 + (i // 3) * ch + ch * 0.42; s = min(cw, ch) / 80
        o.append(f'<rect x="{f(x - cw / 2 + 4)}" y="{f(y - ch * 0.4)}" width="{f(cw - 8)}" height="{f(ch * 0.86)}" fill="none" stroke="#2C9DB8" stroke-width="1"></rect>' + fn(x, y, s) + label(x, y + ch * 0.4, nm, CY, 7.5, ls=0.04))
    return "".join(o)

def ephod(w, h, stones=False, chains=False):
    """The ephod: gold, blue, purple, scarlet and fine twined linen; two shoulder-pieces, the skilfully woven band; with the onyx stones in settings of gold."""
    o = [bp(w, h), title_bar(w, "THE EPHOD · FRONT")]
    cx, top = w * 0.74, h * 0.2; ew, eh = min(w * 0.22, h * 0.5), min(h * 0.62, w * 0.3)
    o.append(f'<path d="M{f(cx - ew / 2)} {f(top + eh * 0.2)} L {f(cx - ew * 0.3)} {f(top)} L {f(cx - ew * 0.12)} {f(top)} L {f(cx - ew * 0.12)} {f(top + eh * 0.2)} L {f(cx + ew * 0.12)} {f(top + eh * 0.2)} L {f(cx + ew * 0.12)} {f(top)} L {f(cx + ew * 0.3)} {f(top)} L {f(cx + ew / 2)} {f(top + eh * 0.2)} L {f(cx + ew / 2)} {f(top + eh)} L {f(cx - ew / 2)} {f(top + eh)} Z" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for k, c in enumerate((BLUE, PURPLE, SCARLET, LINEN)):
        yy = top + eh * (0.3 + k * 0.14)
        o.append(f'<path d="M{f(cx - ew / 2)} {f(yy)} L {f(cx + ew / 2)} {f(yy)}" stroke="{c}" stroke-width="{f(eh * 0.06)}"></path>')
    by = top + eh * 0.86
    o.append(f'<path d="M{f(cx - ew * 0.9)} {f(by)} L {f(cx + ew * 0.9)} {f(by)}" stroke="#0D0D0F" stroke-width="{f(eh * 0.1 + 3)}"></path><path d="M{f(cx - ew * 0.9)} {f(by)} L {f(cx + ew * 0.9)} {f(by)}" stroke="{GOLD}" stroke-width="{f(eh * 0.1)}"></path>')
    o.append(tag(cx - ew * 0.21, top + 4, "TWO SHOULDER-PIECES", w * 0.52, top - 6) + tag(cx + ew * 0.8, by, "THE SKILFULLY WOVEN BAND", w * 0.6, by + 22))
    if stones:
        for dx in (-ew * 0.21, ew * 0.21):
            o.append(f'<ellipse cx="{f(cx + dx)}" cy="{f(top + 6)}" rx="{f(ew * 0.1)}" ry="{f(ew * 0.07)}" fill="#2A2A3A" stroke="{GOLD}" stroke-width="3"></ellipse>')
        o.append(tag(cx + ew * 0.21, top + 6, "ONYX · SETTINGS OF GOLD", w * 0.98, top - 10))
    if chains:
        o.append("".join(f'<path d="M{f(cx + d)} {f(top + 10)} C {f(cx + d * 0.6)} {f(top + eh * 0.3)} {f(cx + d * 0.4)} {f(top + eh * 0.36)} {f(cx + d * 0.4)} {f(top + eh * 0.44)}" fill="none" stroke="#FFD23F" stroke-width="3" stroke-dasharray="3 2"></path>' for d in (-ew * 0.21, ew * 0.21)))
    return "".join(o)

def onyx(w, h):
    """Two onyx stones graven like a signet with the names of the children of Israel, six on each, according to their birth."""
    o = [bp(w, h), title_bar(w, "TWO ONYX STONES · STONES OF MEMORIAL")]
    for k in range(2):
        cx = w * (0.63 + k * 0.24); cy = h * 0.55; rx, ry = min(w * 0.11, h * 0.3), min(h * 0.36, w * 0.15)
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx + 6)}" ry="{f(ry + 6)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2"></ellipse>'
                 f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="#2A2A3A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
        for i in range(6):
            o.append(label(cx, cy - ry * 0.62 + i * ry * 0.26, TRIBES[k * 6 + i], "#E8E2D6", min(9, rx / 6), ls=0.06))
    return "".join(o)

def chains(w, h):
    """Settings of gold, and two chains of pure gold, like cords, of wreathen work."""
    o = [bp(w, h), title_bar(w, "SETTINGS · WREATHEN CHAINS OF PURE GOLD")]
    for k in range(2):
        cx = w * (0.62 + k * 0.24); cy = h * 0.34
        o.append("".join(f'<circle cx="{f(cx + 18 * math.cos(a))}" cy="{f(cy + 18 * math.sin(a))}" r="7" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.4"></circle>' for a in [i * math.pi / 4 for i in range(8)])
                 + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="12" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.6"></circle>')
        o.append("".join(f'<ellipse cx="{f(cx)}" cy="{f(cy + 30 + i * 12)}" rx="5" ry="7" fill="none" stroke="#FFD23F" stroke-width="2.4" transform="rotate({30 if i % 2 else -30} {f(cx)} {f(cy + 30 + i * 12)})"></ellipse>' for i in range(int(h * 0.5 / 12))))
    return "".join(o)

def breastplate(w, h, names=True, rings=False):
    """The breastplate of judgment: foursquare and double, a span each way; four rows of stones inclosed in gold, each graven with a name."""
    o = [bp(w, h), title_bar(w, "THE BREASTPLATE OF JUDGMENT · A SPAN SQUARE")]
    sz = min(w * 0.4, h * 0.74); x0, y0 = w * 0.96 - sz, h * 0.16
    o.append(f'<rect x="{f(x0 + 6)}" y="{f(y0 + 6)}" width="{f(sz)}" height="{f(sz)}" fill="#8A6A1E" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(sz)}" height="{f(sz)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    cw = sz / 3; rh = sz / 4
    for i, (nm, c) in enumerate(STONES):
        cx = x0 + cw * (i % 3 + 0.5); cy = y0 + rh * (i // 3 + 0.46)
        o.append(f'<rect x="{f(cx - cw * 0.3)}" y="{f(cy - rh * 0.3)}" width="{f(cw * 0.6)}" height="{f(rh * 0.5)}" rx="4" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<rect x="{f(cx - cw * 0.34)}" y="{f(cy - rh * 0.34)}" width="{f(cw * 0.68)}" height="{f(rh * 0.58)}" rx="5" fill="none" stroke="#FFF4C2" stroke-width="1.4"></rect>')
        if names: o.append(label(cx, cy + rh * 0.38, nm, "#0D0D0F", min(7.5, cw / 9), weight=700, ls=0.02))
    if rings:
        for cx, cy in ((x0, y0), (x0 + sz, y0), (x0, y0 + sz), (x0 + sz, y0 + sz)):
            o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="7" fill="none" stroke="#0D0D0F" stroke-width="5"></circle><circle cx="{f(cx)}" cy="{f(cy)}" r="7" fill="none" stroke="#FFD23F" stroke-width="2.6"></circle>')
        o.append(f'<path d="M{f(x0)} {f(y0 + sz)} L {f(x0 - 20)} {f(y0 + sz + 26)} M{f(x0 + sz)} {f(y0 + sz)} L {f(x0 + sz + 4)} {f(y0 + sz + 26)}" stroke="{BLUE}" stroke-width="4"></path>'
                 + tag(x0 - 14, y0 + sz + 18, "A LACE OF BLUE", w * 0.52, y0 + sz + 6))
        o.append(f'<path d="M{f(x0)} {f(y0)} C {f(x0 - 10)} {f(y0 - 30)} {f(x0 + 10)} {f(y0 - 40)} {f(x0 + 20)} {f(y0 - 60)} M{f(x0 + sz)} {f(y0)} C {f(x0 + sz + 6)} {f(y0 - 30)} {f(x0 + sz - 10)} {f(y0 - 40)} {f(x0 + sz - 20)} {f(y0 - 60)}" fill="none" stroke="#FFD23F" stroke-width="3" stroke-dasharray="3 2"></path>')
    o.append(dim(x0, y0 + sz + 14, x0 + sz, y0 + sz + 14, "A SPAN", size=8) if not rings else "")
    return "".join(o)

def tribes_grid(w, h):
    """The twelve stones according to the names of the children of Israel: each stone with its tribe."""
    o = [bp(w, h), title_bar(w, "TWELVE STONES · TWELVE NAMES")]
    x0 = w * 0.6; cw = (w * 0.38) / 4; ch = (h - 40) / 3
    for i in range(12):
        nm, c = STONES[i]; cx = x0 + cw * (i % 4 + 0.5); cy = 34 + ch * (i // 4 + 0.42)
        o.append(f'<rect x="{f(cx - cw * 0.26)}" y="{f(cy - ch * 0.26)}" width="{f(cw * 0.52)}" height="{f(ch * 0.36)}" rx="4" fill="{c}" stroke="{GOLD}" stroke-width="3"></rect>'
                 + label(cx, cy + ch * 0.26, TRIBES[i], "#FFD23F", 8, ls=0.04) + label(cx, cy + ch * 0.44, nm, CY, 7, ls=0.04))
    return "".join(o)

def urim(w, h):
    """The breastplate upon Aaron's heart, with the Urim and the Thummim, when he goeth in before Jehovah."""
    o = [bp(w, h), title_bar(w, "UPON HIS HEART · URIM AND THUMMIM")]
    o.append(stage("q2", w, h, [(high_priest, 0.08)], x0=0.6, x1=0.84)[len(bp(w, h)):])
    o.append(V.rays(w * 0.72, h * 0.4, 20, 10, h * 0.5, color="#FFF4C2", op=0.25))
    o.append(tag(w * 0.72, h * 0.32, "URIM · THUMMIM", w * 0.96, h * 0.2, color="#FFD23F"))
    return "".join(o)

def robe(w, h, zoom=False):
    """The robe of the ephod, all of blue, the hole for the head bound like a coat of mail; a golden bell and a pomegranate round the skirts."""
    o = [bp(w, h), title_bar(w, "THE ROBE OF THE EPHOD · ALL OF BLUE")]
    if zoom:
        y = h * 0.6
        o.append(f'<path d="M{f(w * 0.5)} {f(y - 40)} L {f(w * 0.98)} {f(y - 40)} L {f(w * 0.98)} {f(y)} L {f(w * 0.5)} {f(y)} Z" fill="{BLUE}" stroke="#0D0D0F" stroke-width="2"></path>')
        for i in range(8):
            x = w * 0.53 + i * w * 0.058
            if i % 2:
                o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y + 8)}" stroke="#0D0D0F" stroke-width="1.4"></path><path d="M{f(x - 9)} {f(y + 30)} C {f(x - 9)} {f(y + 10)} {f(x + 9)} {f(y + 10)} {f(x + 9)} {f(y + 30)} Z" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.6"></path><circle cx="{f(x)}" cy="{f(y + 32)}" r="3" fill="#8A6A1E"></circle>')
            else:
                o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y + 8)}" stroke="#0D0D0F" stroke-width="1.4"></path><circle cx="{f(x)}" cy="{f(y + 22)}" r="12" fill="{[BLUE, PURPLE, SCARLET][(i // 2) % 3]}" stroke="#0D0D0F" stroke-width="1.6"></circle><path d="M{f(x - 4)} {f(y + 10)} L {f(x)} {f(y + 6)} L {f(x + 4)} {f(y + 10)}" fill="{[BLUE, PURPLE, SCARLET][(i // 2) % 3]}" stroke="#0D0D0F" stroke-width="1.2"></path>')
        o.append(label(w * 0.74, y + 62, "A GOLDEN BELL AND A POMEGRANATE", CY, 9))
        return "".join(o)
    cx, top = w * 0.74, h * 0.14; rw, rh = min(w * 0.3, h * 0.7), h * 0.72
    o.append(f'<path d="M{f(cx - rw * 0.25)} {f(top)} L {f(cx + rw * 0.25)} {f(top)} L {f(cx + rw / 2)} {f(top + rh)} L {f(cx - rw / 2)} {f(top + rh)} Z" fill="{BLUE}" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(top + 6)}" rx="{f(rw * 0.1)}" ry="6" fill="{INK}" stroke="#FFD23F" stroke-width="2.4"></ellipse>')
    for i in range(14):
        x = cx - rw / 2 + 6 + i * (rw - 12) / 13
        o.append(f'<circle cx="{f(x)}" cy="{f(top + rh + 6)}" r="4" fill="{GOLD if i % 2 else SCARLET}" stroke="#0D0D0F" stroke-width="1"></circle>')
    o.append(tag(cx, top + 6, "A HOLE FOR THE HEAD", w * 0.52, top + 2) + tag(cx + rw / 2 - 6, top + rh + 6, "BELLS · POMEGRANATES", w * 0.98, top + rh - 20))
    return "".join(o)

def plate(w, h):
    """A plate of pure gold, graven like a signet, HOLY TO JEHOVAH, on a lace of blue upon the forefront of the mitre."""
    o = [bp(w, h), title_bar(w, "THE PLATE OF PURE GOLD · THE MITRE")]
    cx, cy = w * 0.74, h * 0.6; mw = min(w * 0.4, h * 1.1)
    o.append(f'<path d="M{f(cx - mw / 2)} {f(cy + mw * 0.12)} C {f(cx - mw * 0.56)} {f(cy - mw * 0.5)} {f(cx + mw * 0.56)} {f(cy - mw * 0.5)} {f(cx + mw / 2)} {f(cy + mw * 0.12)} Z" fill="{LINEN}" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + "".join(f'<path d="M{f(cx - mw * 0.46)} {f(cy - mw * k)} C {f(cx - mw * 0.2)} {f(cy - mw * k - 6)} {f(cx + mw * 0.2)} {f(cy - mw * k - 6)} {f(cx + mw * 0.46)} {f(cy - mw * k)}" fill="none" stroke="#C8C2B6" stroke-width="2"></path>' for k in (0.05, 0.15, 0.25)))
    o.append(f'<path d="M{f(cx - mw * 0.5)} {f(cy)} L {f(cx + mw * 0.5)} {f(cy)}" stroke="{BLUE}" stroke-width="5"></path>'
             f'<rect x="{f(cx - mw * 0.3)}" y="{f(cy - mw * 0.08)}" width="{f(mw * 0.6)}" height="{f(mw * 0.16)}" rx="4" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2"></rect>'
             + label(cx, cy + mw * 0.025, "HOLY TO JEHOVAH", "#5A3A0A", min(13, mw * 0.05), weight=700, ls=0.08))
    o.append(tag(cx + mw * 0.45, cy, "A LACE OF BLUE", w * 0.98, cy + mw * 0.24))
    return "".join(o)

def sons_garments(w, h):
    """Coats, girdles and head-tires for Aaron's sons, for glory and for beauty; and linen breeches."""
    return stage("q3", w, h, [(son_priest, 0.2)] * 4, x0=0.52, x1=0.98) + title_bar(w, "COATS · GIRDLES · HEAD-TIRES · LINEN BREECHES")

# ---- Exodus 29 ----
def bullock_rams(w, h, basket=True):
    """One young bullock and two rams without blemish, and the basket of unleavened bread, cakes and wafers."""
    b = h * 0.86
    o = [bp(w, h), f'<path d="M{f(w * 0.5)} {f(b)} L {f(w)} {f(b)}" stroke="{CY}" stroke-width="1.6"></path>', S1.cow(w * 0.62, b, min(0.7, h / 300), color="#5A3A22", patch="#3A2214"),
         E.sheep(w * 0.8, b, min(0.7, h / 280)), E.sheep(w * 0.92, b, min(0.6, h / 300))]
    if basket:
        o.append(f'<g transform="translate({f(w * 0.54)} {f(b)}) scale({f(min(2.2, h / 110))})"><path d="M-16 -14 L 16 -14 L 12 0 L -12 0 Z" fill="#C9A86A" stroke="#0D0D0F" stroke-width="1.2"></path>'
                 '<ellipse cx="-6" cy="-15" rx="7" ry="2.6" fill="#E8C88A" stroke="#0D0D0F" stroke-width="0.8"></ellipse><ellipse cx="6" cy="-17" rx="7" ry="2.6" fill="#F3E8D0" stroke="#0D0D0F" stroke-width="0.8"></ellipse></g>')
    return "".join(o) + title_bar(w, "A BULLOCK · TWO RAMS · A BASKET OF UNLEAVENED BREAD")

def washing(w, h):
    """Aaron and his sons washed with water at the door of the tent of meeting: the laver, the priests in white."""
    o = [stage("q4", w, h, [(son_priest, 0.24)] * 3, x0=0.62, x1=0.98)]
    b = h * 0.9
    o.append(laver_shape(w * 0.55, b, min(1.0, h / 260)))
    return "".join(o) + title_bar(w, "AT THE DOOR OF THE TENT OF MEETING")

def laver_shape(x, y, s=1.0):
    """The laver of brass on its base of brass."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-26 0 L 26 0 L 14 -16 L 8 -60 L -8 -60 L -14 -16 Z" fill="{BRASS}" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="M-50 -60 C -50 -90 50 -90 50 -60 Z" fill="{BRASS}" stroke="#0D0D0F" stroke-width="2.4"></path><ellipse cx="0" cy="-60" rx="50" ry="8" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></ellipse></g>')

def dressing(w, h, oil=False):
    """The garments put upon Aaron, the mitre and the holy crown; with oil=True, Moses pours the anointing oil upon his head."""
    o = [stage("q5", w, h, [(high_priest, 0.2)], x0=0.66, x1=0.82)]
    b = h * 0.9; s = (b - h * 0.2) / 205
    if oil:
        hx, hy = w * 0.74, b - 205 * s
        o.append(A.moses("q5", w * 0.9, b, s * 0.98, flip=True, up=[(-22, -158), (-6, -200), (10, -220)]))
        o.append(S1.vial(hx + 12, hy - 22, 0.8, rot=-120, pour=26) + S1.drops(hx, hy + 30, 6, 7, spread=20))
    return "".join(o) + title_bar(w, "THE ANOINTING" if oil else "THE HOLY CROWN UPON THE MITRE")

def offering_fire(w, h, beast="bullock", hands=True, without=False):
    """An offering: the beast whole before the altar, hands laid upon its head; then only fire on the altar (no carcass is drawn).
    without=True: the fire without the camp."""
    b = h * 0.88; o = [bp(w, h)]
    if without:
        o.append(E.blaze(w * 0.76, b, w * 0.16, h * 0.4, 9, n=7) + label(w * 0.76, h * 0.96, "WITHOUT THE CAMP", CY, 9))
        return "".join(o)
    o.append(A4.altar(w * 0.86, b, min(1.0, h / 300), seed=3))
    if beast == "bullock": o.append(S1.cow(w * 0.62, b, min(0.6, h / 330), color="#5A3A22", patch="#3A2214"))
    elif beast == "ram": o.append(E.sheep(w * 0.64, b, min(0.7, h / 280)))
    if hands:
        o.append(mk.defs("q6", *ALL) + son_priest("q6", w * 0.66, b, min(1.0, (b - h * 0.34) / 205), up=[(-22, -158), (4, -140), (26, -130)]))
    return "".join(o)

def marks(w, h):
    """The tip of the right ear, the thumb of the right hand, the great toe of the right foot: a figure outline with three marks."""
    o = [bp(w, h), title_bar(w, "THE RIGHT EAR · THE RIGHT THUMB · THE RIGHT GREAT TOE")]
    o.append(stage("q7", w, h, [(son_priest, 0.12)], x0=0.66, x1=0.86)[len(bp(w, h)):])
    b = h * 0.9; s = min(1.25, (b - h * 0.12) / 205); x = w * 0.76
    for (dx, dy), t, ty in (((10, -190), "EAR", 0.2), ((30, -96), "THUMB", 0.5), ((12, -2), "GREAT TOE", 0.86)):
        o.append(f'<circle cx="{f(x + dx * s)}" cy="{f(b + dy * s)}" r="5" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.2"></circle>' + tag(x + dx * s, b + dy * s, t, w * 0.96, h * ty, color="#FFD23F"))
    return "".join(o)

def wave(w, h):
    """The wave-offering and the heave-offering: a priest's hands lifting the portion, arrows for waving and heaving."""
    o = [stage("q8", w, h, [(son_priest, 0.24)], x0=0.66, x1=0.86)]
    b = h * 0.9; s = min(1.25, (b - h * 0.24) / 205); x = w * 0.76
    o[0] = stage("q8", w, h, [(lambda p, x_, y_, s_, flip=False, up=None: son_priest(p, x_, y_, s_, up=[(-22, -158), (-10, -190), (10, -210)]), 0.24)], x0=0.66, x1=0.86)
    hx, hy = x + 10 * s, b - 214 * s
    o.append(f'<ellipse cx="{f(hx)}" cy="{f(hy)}" rx="{f(22 * s)}" ry="{f(8 * s)}" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    o.append(f'<path d="M{f(hx - 60)} {f(hy - 20)} L {f(hx + 60)} {f(hy - 20)}" stroke="#FFD23F" stroke-width="2.4"></path><path d="M{f(hx + 60)} {f(hy - 20)} l -8 -5 l 0 10 Z M{f(hx - 60)} {f(hy - 20)} l 8 -5 l 0 10 Z" fill="#FFD23F"></path>'
             f'<path d="M{f(hx + 76)} {f(hy + 40)} L {f(hx + 76)} {f(hy - 60)}" stroke="{CY}" stroke-width="2.4"></path><path d="M{f(hx + 76)} {f(hy - 60)} l -5 8 l 10 0 Z" fill="{CY}"></path>'
             + label(hx, hy - 30, "WAVED", "#FFD23F", 9) + label(hx + 82, hy + 50, "HEAVED UP", CY, 9, "start"))
    return "".join(o)

def days7(w, h, title="SEVEN DAYS"):
    o = [bp(w, h), title_bar(w, title)]
    cw = (w * 0.38) / 7
    for d in range(7):
        x = w * 0.6 + d * cw
        o.append(f'<rect x="{f(x + 2)}" y="{f(h * 0.4)}" width="{f(cw - 4)}" height="{f(min(cw, h * 0.3))}" fill="#FFD23F" fill-opacity="0.85" stroke="#2C9DB8" stroke-width="1.4"></rect>' + label(x + cw / 2, h * 0.4 + min(cw, h * 0.3) / 2 + 5, str(d + 1), "#0D0D0F", 13))
    return "".join(o)

def boil(w, h):
    """Boil its flesh in a holy place; eat it at the door of the tent of meeting, and burn what remaineth until morning."""
    b = h * 0.88
    o = [bp(w, h), title_bar(w, "IN A HOLY PLACE · AT THE DOOR OF THE TENT"), E.blaze(w * 0.66, b, w * 0.12, h * 0.2, 4, n=5),
         f'<path d="M{f(w * 0.58)} {f(b - h * 0.22)} C {f(w * 0.58)} {f(b - h * 0.06)} {f(w * 0.74)} {f(b - h * 0.06)} {f(w * 0.74)} {f(b - h * 0.22)} Z" fill="{BRASS}" stroke="#0D0D0F" stroke-width="2"></path>']
    o.append(f'<g transform="translate({f(w * 0.88)} {f(b)}) scale({f(min(2.4, h / 100))})"><path d="M-16 -14 L 16 -14 L 12 0 L -12 0 Z" fill="#C9A86A" stroke="#0D0D0F" stroke-width="1.2"></path></g>')
    return "".join(o)

def lambs_day(w, h):
    """Two lambs a year old day by day: one in the morning, the other at even; the measures of flour, oil and wine."""
    o = [bp(w, h), title_bar(w, "THE CONTINUAL BURNT-OFFERING")]
    b = h * 0.62
    o.append(f'<circle cx="{f(w * 0.68)}" cy="{f(b - 40)}" r="14" fill="#FFE680"></circle>' + label(w * 0.68, b + 30, "MORNING", "#FFE680", 9) + E3.lamb(w * 0.68, b, min(0.5, h / 400)))
    o.append(f'<circle cx="{f(w * 0.86)}" cy="{f(b - 40)}" r="14" fill="#FF8A3D"></circle>' + label(w * 0.86, b + 30, "EVEN", "#FF8A3D", 9) + E3.lamb(w * 0.86, b, min(0.5, h / 400)))
    meas = [("1/10 EPHAH FLOUR", "#F3EFE6"), ("1/4 HIN OIL", "#C8B040"), ("1/4 HIN WINE", "#8A1E3A")]
    for i, (t, c) in enumerate(meas):
        x = w * (0.66 + i * 0.12); y = h * 0.92
        o.append(f'<rect x="{f(x - 14)}" y="{f(y - 22)}" width="28" height="22" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></rect>' + label(x, y - 28, t, CY, 7.5, ls=0.02))
    return "".join(o)

def glory_tent(w, h):
    """The Tent shall be sanctified by my glory: the tabernacle under a blaze of light (God himself is not drawn)."""
    return bp(w, h) + V.rays(w * 0.74, h * 0.3, 30, 20, max(w, h), color="#FFF4C2", op=0.3) + V.tabernacle(w * 0.74, h * 0.86, min(w * 0.46, h * 1.2), uid="q9")

# ---- Exodus 30–31 ----
def incense_altar(w, h, smoke=False):
    """The altar of incense: a cubit by a cubit, foursquare, two cubits high, overlaid with pure gold, horns, a crown, two rings, staves."""
    u = min(w / 9.0, h / 3.8, 70)
    L, B, H_ = u, u, 2 * u
    x, y = w * 0.74 - L * 0.6, h * 0.9; dx, dy = B * 0.5, -B * 0.35
    o = [bp(w, h), title_bar(w, "THE ALTAR OF INCENSE · PURE GOLD")]
    if smoke:
        o.append("".join(f'<path d="M{f(x + L * 0.6 + d)} {f(y - H_)} c 14 -20 -14 -40 0 -60 c 14 -20 -10 -40 4 -60" fill="none" stroke="#E8E2D6" stroke-width="5" opacity="0.6"></path>' for d in (-6, 8)))
    o.append(box(x, y, L, B, H_, fill=GOLD, top="#FFD23F", side="#C8981E"))
    for hx, hy in ((x, y - H_), (x + L, y - H_), (x + dx, y - H_ + dy), (x + L + dx, y - H_ + dy)):
        o.append(f'<path d="M{f(hx - 5)} {f(hy)} C {f(hx - 5)} {f(hy - 10)} {f(hx + 2)} {f(hy - 16)} {f(hx + 6)} {f(hy - 18)} C {f(hx + 3)} {f(hy - 10)} {f(hx + 5)} {f(hy - 4)} {f(hx + 5)} {f(hy)} Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.4"></path>')
    sy = y - H_ * 0.78
    o.append(f'<path d="M{f(x - u * 0.8)} {f(sy)} L {f(x + L + u * 0.8)} {f(sy)}" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path><path d="M{f(x - u * 0.8)} {f(sy)} L {f(x + L + u * 0.8)} {f(sy)}" stroke="{GOLD}" stroke-width="4" stroke-linecap="round"></path>')
    o.append(dim(x, y + 10, x + L, y + 10, "1", size=8) + dim(x - 12, y, x - 12, y - H_, "2 CUBITS", size=8))
    return "".join(o)

def half_shekel(w, h):
    """Half a shekel after the shekel of the sanctuary (the shekel is twenty gerahs): the rich shall not give more, the poor not less."""
    o = [bp(w, h), title_bar(w, "THE ATONEMENT MONEY · HALF A SHEKEL")]
    cx, cy = w * 0.66, h * 0.5; r = min(h * 0.24, w * 0.05)
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{SILVER}" stroke="#0D0D0F" stroke-width="2"></circle><path d="M{f(cx)} {f(cy - r)} L {f(cx)} {f(cy + r)}" stroke="#D7261E" stroke-width="2.4" stroke-dasharray="4 3"></path>'
             + label(cx, cy + r + 18, "1 SHEKEL = 20 GERAHS", CY, 9))
    bx = w * 0.86; by = h * 0.6
    o.append(f'<path d="M{f(bx)} {f(by - 60)} L {f(bx)} {f(by + 30)} M{f(bx - 60)} {f(by - 50)} L {f(bx + 60)} {f(by - 50)}" stroke="#E8B830" stroke-width="3"></path>'
             + "".join(f'<path d="M{f(bx + d - 20)} {f(by - 10)} C {f(bx + d - 20)} {f(by + 4)} {f(bx + d + 20)} {f(by + 4)} {f(bx + d + 20)} {f(by - 10)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>'
                       f'<path d="M{f(bx + d)} {f(by - 50)} L {f(bx + d - 18)} {f(by - 10)} M{f(bx + d)} {f(by - 50)} L {f(bx + d + 18)} {f(by - 10)}" stroke="#E8B830" stroke-width="1.2"></path>'
                       f'<path d="M{f(bx + d - 6)} {f(by - 14)} A 6 6 0 0 1 {f(bx + d + 6)} {f(by - 14)} Z" fill="{SILVER}" stroke="#0D0D0F" stroke-width="1"></path>' for d in (-60, 60))
             + label(bx - 60, by + 22, "THE RICH", CY, 8) + label(bx + 60, by + 22, "THE POOR", CY, 8))
    return "".join(o)

def laver(w, h):
    """The laver of brass and its base between the tent of meeting and the altar, with water therein."""
    o = [bp(w, h), title_bar(w, "THE LAVER OF BRASS · BETWEEN THE TENT AND THE ALTAR")]
    b = h * 0.9
    o.append(f'<rect x="{f(w * 0.6)}" y="{f(b - min(h * 0.4, 120))}" width="{f(w * 0.08)}" height="{f(min(h * 0.4, 120))}" fill="{GOLD}" opacity="0.5" stroke="#0D0D0F" stroke-width="1.4"></rect>' + label(w * 0.64, b + 12, "TENT", CY, 8))
    o.append(laver_shape(w * 0.78, b, min(1.0, h / 260)))
    o.append(box(w * 0.88, b, w * 0.08, w * 0.08, w * 0.05, fill=BRASS, top="#D8935A", side="#8A5222") + label(w * 0.92, b + 12, "ALTAR", CY, 8))
    return "".join(o)

def chart(w, h, rows_, title, unit=""):
    """A horizontal bar chart: rows_ = [(name, value, colour)]."""
    o = [bp(w, h), title_bar(w, title)]
    mx = max(v for _, v, _ in rows_); x0 = w * 0.76; bw = w * 0.17; rh = min(60, (h - 50) / len(rows_))
    for i, (nm, val, c) in enumerate(rows_):
        y = 36 + i * rh
        o.append(label(x0 - 8, y + rh * 0.6, nm, CY, 9, "end") + f'<rect x="{f(x0)}" y="{f(y + rh * 0.2)}" width="{f(bw * val / mx)}" height="{f(rh * 0.6)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></rect>'
                 + label(x0 + bw * val / mx + 6, y + rh * 0.6, f"{val}{unit}" if val else "", "#FFD23F", 9, "start"))
    return "".join(o)

def spices(w, h):
    return chart(w, h, [("FLOWING MYRRH", 500, "#8A3A1E"), ("SWEET CINNAMON", 250, "#B5652E"), ("SWEET CALAMUS", 250, "#9A9A3A"), ("CASSIA", 500, "#6A4A2A")],
                 "THE HOLY ANOINTING OIL · SHEKELS", "") + label(w * 0.98, 36 + 4 * min(60, (h - 50) / 4) + 14, "AND OF OLIVE OIL A HIN", "#C8B040", 9, "end")

def incense_mix(w, h):
    """Stacte, onycha, galbanum and pure frankincense, of each a like weight, seasoned with salt."""
    o = [bp(w, h), title_bar(w, "THE INCENSE · OF EACH A LIKE WEIGHT")]
    cx, cy, r = w * 0.74, h * 0.56, min(h * 0.34, w * 0.14)
    cols = [("STACTE", "#B5652E"), ("ONYCHA", "#8A6A5A"), ("GALBANUM", "#9A9A3A"), ("FRANKINCENSE", "#E8E2D6")]
    for i, (nm, c) in enumerate(cols):
        a0, a1 = i * math.pi / 2 - math.pi / 2, (i + 1) * math.pi / 2 - math.pi / 2
        o.append(f'<path d="M{f(cx)} {f(cy)} L {f(cx + r * math.cos(a0))} {f(cy + r * math.sin(a0))} A {f(r)} {f(r)} 0 0 1 {f(cx + r * math.cos(a1))} {f(cy + r * math.sin(a1))} Z" fill="{c}" stroke="#0D0D0F" stroke-width="2"></path>')
        am = (a0 + a1) / 2
        o.append(tag(cx + r * 0.7 * math.cos(am), cy + r * 0.7 * math.sin(am), nm, cx + (r + 30) * math.cos(am), cy + (r + 20) * math.sin(am)))
    o.append(label(cx, cy + r + 34, "SEASONED WITH SALT", CY, 9))
    return "".join(o)

def anointed(w, h):
    """Thou shalt anoint therewith the tent of meeting and all its furniture: the plan with every piece lit gold."""
    o = [bp(w, h), title_bar(w, "ANOINTED · MOST HOLY")]
    x0, x1, y0, y1 = w * 0.6, w * 0.98, h * 0.2, min(h * 0.86, h * 0.2 + w * 0.3)
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(x1 - x0)}" height="{f(y1 - y0)}" fill="none" stroke="#F3EFE6" stroke-width="2"></rect>')
    items = [("ARK", 0.12, 0.5), ("TABLE", 0.36, 0.3), ("CANDLESTICK", 0.36, 0.72), ("INCENSE", 0.46, 0.5), ("ALTAR", 0.76, 0.5), ("LAVER", 0.62, 0.5)]
    for nm, fx_, fy in items:
        x, y = x0 + (x1 - x0) * fx_, y0 + (y1 - y0) * fy
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="16" fill="#FFF4C2" opacity="0.3"></circle><circle cx="{f(x)}" cy="{f(y)}" r="6" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.2"></circle>' + label(x, y + 22, nm, CY, 7.5, ls=0.04))
    return "".join(o)

def craftsmen(p, w, h):
    """Bezalel of Judah and Oholiab of Dan, filled with wisdom: two craftsmen at a bench with gold, a chisel and a carving."""
    b = h * 0.9
    o = [bp(w, h), mk.defs(p, *ALL), f'<path d="M{f(w * 0.5)} {f(b)} L {f(w)} {f(b)}" stroke="{CY}" stroke-width="1.6"></path>']
    s = (b - h * 0.24) / 205
    o.append(A.son("#6A7AD8", 3)(p, w * 0.62, b, s) + A.son("#1F7A8C", 1)(p, w * 0.9, b, s, flip=True))
    o.append(box(w * 0.7, b, w * 0.12, w * 0.06, h * 0.18, fill="#8A5A3E", top="#B5793A", side="#6A3A1E")
             + f'<path d="M{f(w * 0.72)} {f(b - h * 0.24)} L {f(w * 0.76)} {f(b - h * 0.2)} L {f(w * 0.8)} {f(b - h * 0.24)} L {f(w * 0.78)} {f(b - h * 0.18)} Z" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.4"></path>')
    o.append(label(w * 0.62, h * 0.12, "BEZALEL · JUDAH", "#FFD23F", 9) + label(w * 0.9, h * 0.12, "OHOLIAB · DAN", "#FFD23F", 9))
    return "".join(o)

def works(w, h):
    """All that I have commanded thee: the works of 31:7–11 as a checklist."""
    o = [bp(w, h), title_bar(w, "THE WORKS")]
    items = ["THE TENT OF MEETING", "THE ARK · THE MERCY-SEAT", "THE TABLE · THE CANDLESTICK", "THE ALTAR OF INCENSE", "THE ALTAR OF BURNT-OFFERING", "THE LAVER AND ITS BASE", "THE HOLY GARMENTS", "THE ANOINTING OIL · THE INCENSE"]
    rh = min(34, (h - 40) / len(items))
    for i, t in enumerate(items):
        y = 34 + i * rh + rh * 0.6
        o.append(f'<rect x="{f(w * 0.6)}" y="{f(y - 10)}" width="12" height="12" fill="none" stroke="#FFD23F" stroke-width="1.6"></rect><path d="M{f(w * 0.6 + 2)} {f(y - 4)} l 4 4 l 8 -10" stroke="#FFD23F" stroke-width="2" fill="none"></path>'
                 + label(w * 0.6 + 22, y, t, CY, 9, "start"))
    return "".join(o)
