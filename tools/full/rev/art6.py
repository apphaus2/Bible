"""Drawings for Revelation 19–22 (chapter 6 of the volume): the hallelujahs and the marriage supper of the Lamb, the Word of
God on the white horse, the thousand years, the great white throne, and the new heaven and the new earth with the holy
city, new Jerusalem — the volume's last great plates. God is never drawn: the great white throne is empty, in light; the
dragon bound is a sealed pit; the lake of fire is fire with no one in it; the birds' supper and the slain are words over
the empty sky. The bride is the holy city and the fine linen, never a woman's body.

    marriage_supper(p, w, h, seed)      the marriage supper of the Lamb: a long table in light, the guests in white, the
                                        fine linen bright and pure hung over it, the Lamb at its head
    angel_john(p, w, h, seed, fallen=)  the angel and John (fallen= John fallen before his feet: see thou do it not)
    white_horse(p, w, h, seed, armies=) heaven opened, he that sat on the white horse — a figure of light, many diadems; the
                                        armies in fine linen on white horses behind (armies=True)
    sun_angel(p, w, h, seed)            an angel standing in the sun, the birds in mid heaven
    lake_fire(w, h, seed)               the lake of fire that burneth with brimstone, nothing in it
    abyss_sealed(p, w, h, seed)         the angel with the key of the abyss and a great chain, the pit shut and sealed
    thrones_souls(p, w, h, seed)        thrones, and they sat upon them; the souls as figures of white light reigning
    beloved_city(w, h, seed)            the camp of the saints and the beloved city compassed about, fire out of heaven
    white_throne(w, h, seed)            a great white throne, empty, in light; the books opened; no earth, no heaven
    sea_light(w, h, seed)               the sea under the light from above, empty
    new_earth(p, w, h, seed, stage=)    a new heaven and a new earth, no sea; "descend" (the holy city coming down out of
                                        heaven, made ready as a bride adorned), "dwell" (men in white on the new earth before
                                        its light), "mountain" (John and the angel on a mountain great and high), "nations"
                                        (the nations walking into its open gates), "dawn" (the last morning, the morning star)
    city_plan(w, h)                     the city foursquare in plan: twelve gates of pearl named for the tribes, an angel at
                                        each, the wall on its twelve foundations (a plate)
    city_measure(w, h)                  twelve thousand furlongs, length, breadth and height; the wall 144 cubits (a plate)
    foundations(w, h)                   the twelve foundations, each stone named and coloured (a plate)
    street_gold(p, w, h, seed)          within: the street of pure gold as transparent glass, a gate of one pearl, no temple
    river_life(p, w, h, seed)           the river of water of life out of the throne, the tree of life on either side
    servants(p, w, h, seed)             his servants in white before the throne in light
    open_book(w, h, seed)               the book of this prophecy, open, not sealed
    water_life(p, w, h, seed)           whosoever will, let him take the water of life freely: the river flowing out to all"""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from rev.art5 import *
from rev.art import f, INK, GOLD, GOLD_L, WHITE, GIRDLE
from ntcast import JESUS_SKIN, JESUS_HAIR, _HAIR_FIG, _BEARD_FIG

SKINS = ["#5A3A2A", "#8A5A3A", "#C98E66", "#D9A27A", "#E3B896", "#A8704E", "#6A4430"]
HAIRS = ["#1A1210", "#2A1A10", "#3A2214", "#0D0D0F", "#5A3A22"]

def white_fig(p, x, b, s, r, flip=False, up=None, pose="stand", extra="", woman=None):
    """One of the saints in white: a person of any nation in a white robe."""
    return robed(p, x, b, s, "#FFFFFF", skin=r.choice(SKINS), hair=r.choice(HAIRS), woman=r.random() < 0.4 if woman is None else woman, flip=flip, up=up,
                 pose=pose, seat=None, line="#3A3A4A", extra=extra)

def marriage_supper(p, w, h, seed):
    """The marriage supper of the Lamb (19:7–9): a long table spread with white linen in light, the bidden seated at it in
    white, cups and bread upon it, the Lamb in light at its head; the fine linen, bright and pure, hung above (the bride is
    the city and the linen — no woman is drawn)."""
    r = random.Random(seed)
    o = [defs(p), sky(w, h, "#2A2A6A", "#FFE6B0"), halo(w * 0.86, h * 0.36, w * 0.4, WHITE, 0.9), rays(w * 0.86, h * 0.36, 30, h * 0.08, w, "#FFFDF0", 0.35, 4)]
    for k in range(5):
        x0 = w * (0.02 + 0.18 * k)
        o.append(f'<path d="M{f(x0)} -10 C {f(x0 + w * 0.06)} {f(h * 0.12)} {f(x0 + w * 0.12)} {f(h * 0.12)} {f(x0 + w * 0.18)} -10" fill="#FFFFFF" stroke="#E8D8B0" stroke-width="2" opacity="0.95"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.84)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
    ty = h * 0.72
    s = h * 0.42 / 157
    for i in range(7):                                         # the far side of the table
        x = w * (0.08 + 0.1 * i)
        o.append(white_fig(p, x, ty + h * 0.02, s * 0.9, r, pose="sit", flip=True))
    o.append(f'<path d="M-10 {f(ty)} L {f(w * 0.8)} {f(ty)} L {f(w * 0.82)} {f(ty + h * 0.12)} L -10 {f(ty + h * 0.12)} Z" fill="#FFFFFF" stroke="#C8B890" stroke-width="2.4"></path>')
    for i in range(9):
        x = w * (0.05 + 0.09 * i)
        o.append(cup(x, ty - 1, h / 900, color="#E8B830") + f'<ellipse cx="{f(x + w * 0.035)}" cy="{f(ty - 4)}" rx="{f(h * 0.025)}" ry="{f(h * 0.012)}" fill="#D8A860" stroke="{INK}" stroke-width="1"></ellipse>')
    o.append(lamb(w * 0.86 - 30 * h / 400, ty + h * 0.02, h * 0.18 / 90))
    return "".join(o)

def angel_john(p, w, h, seed, fallen=True):
    """The angel that showed John these things and John (19:10; 22:8–9): the angel of white light, his hand raised — see thou
    do it not — and John fallen before his feet (fallen=False: John standing before him, listening)."""
    o = [defs(p), sky(w, h, "#2A2A6A", "#E8C8A0"), halo(w * 0.62, h * 0.4, w * 0.4, "#FFF4C2", 0.7)]
    b = h * 0.95
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(b)}" rx="{f(w * 0.48)}" ry="{f(h * 0.06)}" fill="#FFF4C2" opacity="0.4"></ellipse>')
    s = min(h * 0.84, w * 0.5) / 205                          # a tall panel: the figures kept to the width, standing on its floor
    o.append(angel(p, w * 0.64, b, s, up=[(-22, -158), (-40, -176), (-44, -200)], flip=False))
    if fallen: o.append(john_fallen(max(w * 0.36, 126 * s * 0.95 + 12), b, s * 0.95))
    else: o.append(john_fig(p, w * 0.3, b, s * 0.94, flip=True))
    return "".join(o)

DIADEMS = "".join(f'<path d="M{-14 + 7 * i} {-198 - 6 * (i % 2)} l -1 -10 l 4 4 l 3 -7 l 3 7 l 4 -4 l -1 10 Z" fill="#FFD23F" stroke="#C8962E" stroke-width="1"></path>' for i in range(5))

def rider_light(x, b, s, glow=True):
    """He that sat upon the white horse, called Faithful and True (19:11–16): a figure of light on a white horse — ntcast's
    Jesus, his hair and beard, in white, many diadems upon his head; his eyes, the name written, the garment sprinkled with
    blood and the sword of his mouth are in the words only."""
    o = (halo(x, b - 120 * s, 170 * s, WHITE, 0.85) + rays(x, b - 120 * s, 24, 80 * s, 240 * s, "#FFFDF0", 0.4, max(2, 3 * s))) if glow else ""
    o += E3.horse(x, b, s, color="#FFFFFF", rim="#C8962E")
    hx, hy = x + 2 * s, b - 122 * s
    o += (f'<g transform="translate({f(x)} {f(b)}) scale({f(s)})">'
          '<path d="M-14 -70 C -16 -56 -14 -44 -8 -34 L 10 -34 C 12 -48 10 -60 6 -70 Z" fill="#FFFFFF" stroke="#C8962E" stroke-width="2"></path>'
          '<path d="M-13 -68 C -15 -92 -10 -110 0 -116 C 11 -112 15 -92 13 -68 Z" fill="#FFFFFF" stroke="#C8962E" stroke-width="2"></path>'
          '<path d="M-12 -110 C -6 -100 -2 -86 -6 -68" fill="none" stroke="#C8D2E6" stroke-width="6"></path>'
          f'<path d="M-9 -128 C -10 -138 10 -138 9 -128 L 10 -110 C 6 -112 4 -112 3 -114 L 3 -126 C 0 -130 -3 -130 -4 -126 L -4 -112 C -6 -110 -9 -110 -10 -112 Z" fill="{JESUS_HAIR}"></path>'
          f'<circle cx="2" cy="-123" r="8.5" fill="{JESUS_SKIN}" stroke="#C8962E" stroke-width="1.6"></circle>'
          f'<path d="M-3 -120 C -2 -112 6 -110 10 -116 L 9 -120 Z" fill="{JESUS_HAIR}"></path>'
          '<path d="M5 -102 C 16 -98 26 -94 34 -90" fill="none" stroke="#C8962E" stroke-width="7" stroke-linecap="round"></path>'
          '<path d="M5 -102 C 16 -98 26 -94 34 -90" fill="none" stroke="#FFFFFF" stroke-width="4.5" stroke-linecap="round"></path>'
          + "".join(f'<path d="M{-9 + 4.5 * i} {-131 - 3 * (i % 2)} l -1 -7 l 3 3 l 2 -5 l 2 5 l 3 -3 l -1 7 Z" fill="#FFD23F" stroke="#C8962E" stroke-width="0.8"></path>' for i in range(5))
          + '</g>')
    return o

def white_horse(p, w, h, seed, armies=False):
    """I saw the heaven opened; and behold, a white horse (19:11–16): the clouds parted on light, the rider of light;
    armies= the armies of heaven following upon white horses, clothed in fine linen, white and pure, small behind him."""
    o = [sky(w, h, "#1A1440", "#5A4A8A")]
    o.append(halo(w * 0.5, h * 0.4, w * 0.6, "#FFF4C2", 0.8) + rays(w * 0.5, h * 0.4, 40, h * 0.1, w, "#FFFDF0", 0.35, 5))
    for k in range(6):
        x = w * (0.05 + 0.18 * k)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(h * (0.12 if k % 2 else 0.2))}" rx="{f(w * 0.12)}" ry="{f(h * 0.06)}" fill="#C8C0D8" stroke="#8A80A8" stroke-width="1.6" opacity="0.9"></ellipse>')
    if armies:
        r = random.Random(seed)
        for row in range(3):
            for i in range(9):
                x = w * (0.06 + 0.1 * i + 0.03 * row) + r.uniform(-6, 6); b = h * (0.46 + 0.1 * row); s = h * (0.08 + 0.02 * row) / 110
                o.append(horse_rider(x, b, s, "#FFFFFF", "#F3EFE6"))
        o.append(rider_light(w * 0.5, h * 0.98, h * 0.5 / 140))
    else:
        o.append(rider_light(w * 0.48, h * 0.96, h * 0.66 / 140))
    return "".join(o)

def sun_angel(p, w, h, seed):
    """An angel standing in the sun, crying to all the birds that fly in mid heaven (19:17–18): the sun's great disc with a
    figure of white light standing in it, and the birds wheeling in the empty sky (nothing on the earth is drawn)."""
    o = [defs(p), sky(w, h, "#C8601A", "#F3D8A0")]
    cx, cy, R = w * 0.5, h * 0.44, h * 0.34
    o.append(halo(cx, cy, R * 1.8, "#FFF4C2", 0.8) + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R)}" fill="#FFE680" stroke="#FF8A2E" stroke-width="3"></circle>' + rays(cx, cy, 30, R * 1.05, R * 1.7, "#FFE680", 0.6, 3))
    o.append(angel(p, cx, cy + R * 0.85, R * 1.5 / 205, up=[(-22, -158), (-46, -176), (-70, -186)], glow=False))
    o.append(birds(22, w * 0.02, w * 0.98, h * 0.06, h * 0.9, seed, 0.6, 1.4, color="#2A1A14"))
    o.append(hills(w, h, h * 0.94, seed, color="#5A3A2A", amp=8, step=90))
    return "".join(o)

def lake_fire(w, h, seed):
    """The lake of fire that burneth with brimstone (19:20; 20:10, 14–15): a lake of fire under a dark sky between black
    shores, its smoke going up — no one drawn in it."""
    o = [sky(w, h, "#0A0406", "#4A1A10")]
    hz = h * 0.52
    o.append(f'<path d="M-10 {f(hz)} L {f(w * 0.2)} {f(hz - h * 0.08)} L {f(w * 0.36)} {f(hz - h * 0.02)} L {f(w * 0.6)} {f(hz - h * 0.1)} L {f(w * 0.8)} {f(hz - h * 0.03)} L {f(w + 10)} {f(hz - h * 0.08)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1A0E0C" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.74)}" rx="{f(w * 0.48)}" ry="{f(h * 0.2)}" fill="#C8401A" stroke="#3A0A06" stroke-width="3"></ellipse>'
             f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.74)}" rx="{f(w * 0.36)}" ry="{f(h * 0.13)}" fill="#FF8A2E" opacity="0.8"></ellipse>'
             f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.74)}" rx="{f(w * 0.2)}" ry="{f(h * 0.06)}" fill="#FFD23F" opacity="0.7"></ellipse>')
    o.append(fires(w * 0.08, w * 0.92, h * 0.76, h * 0.22, seed, n=7))
    o.append(smokes([w * 0.24, w * 0.5, w * 0.76], h * 0.56, seed, k=h / 300, color="#2A1A1A", op=0.6, n=8))
    return "".join(o)

def abyss_sealed(p, w, h, seed):
    """An angel coming down out of heaven, having the key of the abyss and a great chain (20:1–3): the pit shut, its stone
    lid bound about with the chain and sealed; the dragon himself never drawn — what is bound is in the words."""
    o = [defs(p), sky(w, h, "#0B0B2A", "#2A2A4A"), starfield(w, h, seed, 50, 0.5), halo(w * 0.3, h * 0.2, w * 0.3, "#FFF4C2", 0.7)]
    hz = h * 0.6
    o.append(ground(w, h, hz, "#2A2A2A", dy=0))
    cx, cy, R = w * 0.62, h * 0.8, min(w * 0.22, h * 0.32)
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy + R * 0.12)}" rx="{f(R * 1.15)}" ry="{f(R * 0.4)}" fill="#0A0606" stroke="{INK}" stroke-width="2"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(R)}" ry="{f(R * 0.34)}" fill="#6A645C" stroke="{INK}" stroke-width="3"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(R * 0.7)}" ry="{f(R * 0.22)}" fill="none" stroke="#4A443E" stroke-width="2"></ellipse>')
    for a in (-0.6, 0.2, 0.9):                                 # the great chain about it
        o.append("".join(f'<ellipse cx="{f(cx + R * (k / 6 - 0.5) * 2 * math.cos(a))}" cy="{f(cy + R * 0.34 * (k / 6 - 0.5) * 2 * math.sin(a))}" rx="{f(R * 0.07)}" ry="{f(R * 0.04)}" '
                         f'transform="rotate({f(math.degrees(a))} {f(cx + R * (k / 6 - 0.5) * 2 * math.cos(a))} {f(cy + R * 0.34 * (k / 6 - 0.5) * 2 * math.sin(a))})" fill="none" stroke="#A8A8B0" stroke-width="3"></ellipse>' for k in range(7)))
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R * 0.1)}" fill="#B5121B" stroke="{INK}" stroke-width="2"></circle>')
    s = h * 0.62 / 205
    key = ('<g transform="translate(-58 -150) rotate(-60)"><circle cx="0" cy="0" r="8" fill="none" stroke="#E8B830" stroke-width="4"></circle>'
           '<path d="M8 0 L 36 0 M26 0 L 26 8 M32 0 L 32 6" stroke="#E8B830" stroke-width="4"></path></g>')
    o.append(angel(p, w * 0.24, h * 0.86, s, up=[(-22, -158), (-46, -152), (-58, -150)], flip=True, extra=key))
    return "".join(o)

def thrones_souls(p, w, h, seed):
    """I saw thrones, and they sat upon them … and the souls … and they lived, and reigned with Christ a thousand years
    (20:4–6): thrones in a row in light, and on them figures of white light, faceless."""
    o = [defs(p), sky(w, h, "#2A2A6A", "#FFE6B0"), halo(w * 0.5, h * 0.2, w * 0.6, WHITE, 0.85), rays(w * 0.5, h * 0.2, 34, h * 0.06, w, "#FFFDF0", 0.35, 4)]
    o.append(f'<rect x="-10" y="{f(h * 0.88)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
    s = h * 0.62 / 157
    for i in range(6):
        x = w * (0.09 + 0.164 * i)
        o.append(elder_throne(x, h * 0.92, s * 0.9, color="#F3E8C0") + halo(x, h * 0.92 - 90 * s, 70 * s, "#FFF4C2", 0.6)
                 + robed(p, x, h * 0.92, s * 0.9, WHITE, skin="#FFF6DA", line="#E8B830", pose="sit", seat=None, flip=i >= 3))
    return "".join(o)

def beloved_city(w, h, seed):
    """They compassed the camp of the saints about, and the beloved city: and fire came down out of heaven (20:8–9): the city
    and the camp in light on a plain, a dark host as the sand of the sea all about the horizon, fire falling upon the far host
    (no one drawn in it)."""
    r = random.Random(seed)
    o = [sky(w, h, "#1A1028", "#8A4A3A")]
    hz = h * 0.62
    o.append(ground(w, h, hz, "#5A4A3A", dy=0))
    for k in range(320):
        x = r.uniform(-10, w + 10)
        if abs(x - w * 0.5) < w * 0.26: continue
        y = hz + r.uniform(-h * 0.01, h * 0.06)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - h * 0.03)}" stroke="#1A0E0C" stroke-width="1.2"></path>')
    o.append(halo(w * 0.5, hz, h * 0.4, "#FFF4C2", 0.7) + walls(w * 0.36, w * 0.64, hz + h * 0.06, h * 0.2, seed, lit=True, towers=3, color="#E8D8B0"))
    for i in range(7):
        x = w * (0.3 + 0.07 * i); y = hz + h * 0.16
        o.append(f'<path d="M{f(x - 14)} {f(y)} L {f(x)} {f(y - 20)} L {f(x + 14)} {f(y)} Z" fill="#E8DCC0" stroke="{INK}" stroke-width="1.2"></path>')
    for x in (0.06, 0.16, 0.84, 0.94):
        o.append(f'<path d="M{f(w * x + 30)} 0 L {f(w * x)} {f(hz)}" stroke="#FF8A2E" stroke-width="8" opacity="0.7"></path>' + E.blaze(w * x, hz + h * 0.04, 50, h * 0.16, seed + int(x * 100), n=5))
    return "".join(o)

def open_books(cx, y, s, n=5):
    o = []
    for i in range(n):
        x = cx + (i - (n - 1) / 2) * 70 * s
        o.append(f'<path d="M{f(x - 30 * s)} {f(y)} L {f(x)} {f(y + 6 * s)} L {f(x + 30 * s)} {f(y)} L {f(x + 30 * s)} {f(y - 20 * s)} L {f(x)} {f(y - 14 * s)} L {f(x - 30 * s)} {f(y - 20 * s)} Z" '
                 f'fill="{"#FFF8DC" if i != n // 2 else "#FFE680"}" stroke="#C8962E" stroke-width="{f(max(1, 1.6 * s))}"></path>'
                 + "".join(f'<path d="M{f(x - 26 * s)} {f(y - 15 * s + k * 4 * s)} L {f(x - 4 * s)} {f(y - 11 * s + k * 4 * s)} M{f(x + 26 * s)} {f(y - 15 * s + k * 4 * s)} L {f(x + 4 * s)} {f(y - 11 * s + k * 4 * s)}" stroke="#8A7A5A" stroke-width="0.8"></path>' for k in range(3)))
    return "".join(o)

def white_throne(w, h, seed):
    """A great white throne, and him that sat upon it, from whose face the earth and the heaven fled away (20:11–12): the
    throne white and empty in a blaze of light, nothing about it — no earth, no sky, no stars; the books opened before it,
    the book of life among them. God is never drawn."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0A0A12"></rect>', halo(w * 0.5, h * 0.42, max(w, h) * 0.6, WHITE, 0.95),
         rays(w * 0.5, h * 0.42, 48, h * 0.1, max(w, h), "#FFFFFF", 0.35, 5)]
    o.append(empty_throne(w * 0.5, h * 0.78, h * 0.5 / 180).replace("#FFF8DC", "#FFFFFF").replace("#FFE680", "#F3F3F8").replace("#C8962E", "#B8B8C8"))
    o.append(open_books(w * 0.5, h * 0.94, min(1.4, h / 260)))
    return "".join(o)

def sea_light(w, h, seed):
    """The sea gave up the dead that were in it (20:13): the sea under a light from above, empty, still."""
    o = [sky(w, h, "#1A1A3A", "#8A8AB0"), halo(w * 0.5, 0, w * 0.5, WHITE, 0.85), rays(w * 0.5, -10, 24, h * 0.05, h * 1.2, "#FFFDF0", 0.35, 4)]
    o.append(sea(w, h, h * 0.5, seed, color="#2A4A6A", deep="#14243A"))
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.62)}" rx="{f(w * 0.2)}" ry="{f(h * 0.05)}" fill="#E8F0F8" opacity="0.5"></ellipse>')
    return "".join(o)

def new_earth(p, w, h, seed, stage="descend"):
    """A new heaven and a new earth, and the sea is no more (21–22). "descend": the holy city, new Jerusalem, coming down out
    of heaven from God, made ready as a bride adorned — the city in light high over the green new earth; "dwell": men and
    women of every nation in white on the new earth before its light; "mountain": John and the angel on a mountain great and
    high, the city coming down before them; "nations": the nations walking into its open gates of pearl, the kings bringing
    their glory; "dawn": the last morning over the new earth, the city shining, the morning star."""
    r = random.Random(seed)
    o = [defs(p), sky(w, h, "#3A5AA8", "#FFF4D8") if stage != "dawn" else sky(w, h, "#1A1A5A", "#FFC890")]
    hz = h * 0.7
    if stage == "descend":
        o.append(halo(w * 0.5, h * 0.36, w * 0.6, WHITE, 0.85) + rays(w * 0.5, h * 0.36, 40, h * 0.1, w, "#FFFDF0", 0.35, 5))
        for k in range(5):
            o.append(f'<ellipse cx="{f(w * (0.1 + 0.2 * k))}" cy="{f(h * 0.08)}" rx="{f(w * 0.12)}" ry="{f(h * 0.05)}" fill="#FFFFFF" stroke="#D8D0E8" stroke-width="1.6" opacity="0.9"></ellipse>')
        o.append(holy_city(w * 0.5, h * 0.52, w * 0.5, h * 0.26, seed))
        o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.54)}" rx="{f(w * 0.3)}" ry="{f(h * 0.03)}" fill="#FFFFFF" opacity="0.7"></ellipse>')
        o.append(hills(w, h, h * 0.8, seed, color="#6AA85A", amp=12, step=90) + ground(w, h, h * 0.86, "#8AC86A", dy=0))
        for x in (0.08, 0.2, 0.82, 0.94): o.append(olive(w * x, h * 0.98, h / 460, seed=int(x * 100)))
        return "".join(o)
    if stage == "mountain":
        o.append(halo(w * 0.66, h * 0.4, w * 0.5, WHITE, 0.85) + rays(w * 0.66, h * 0.4, 30, h * 0.1, w, "#FFFDF0", 0.3, 4))
        o.append(holy_city(w * 0.68, h * 0.62, w * 0.44, h * 0.3, seed))
        o.append(hills(w, h, h * 0.84, seed, color="#6AA85A", amp=10, step=90))
        o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.6)} L {f(w * 0.12)} {f(h * 0.5)} L {f(w * 0.26)} {f(h * 0.56)} L {f(w * 0.4)} {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>')
        s = h * 0.3 / 205
        o.append(angel(p, w * 0.11, h * 0.52, s, up=[(-22, -158), (-46, -164), (-68, -170)], flip=True) + john_fig(p, w * 0.22, h * 0.56, s * 0.94, flip=True))
        return "".join(o)
    o.append(halo(w * 0.62, h * 0.3, w * 0.5, WHITE, 0.85))
    o.append(holy_city(w * 0.62, hz, w * (0.6 if stage == "nations" else 0.5), h * (0.4 if stage == "nations" else 0.32), seed))
    o.append(ground(w, h, hz, "#8AC86A", dy=0))
    if stage == "dawn":
        o.append(star(w * 0.16, h * 0.18, h * 0.05, "#FFFFFF", 1, "#C8962E") + halo(w * 0.16, h * 0.18, h * 0.14, "#FFF4C2", 0.6))
        for x in (0.06, 0.94): o.append(olive(w * x, h * 0.98, h / 420, seed=int(x * 100)))
        return "".join(o)
    s = h * 0.32 / 205
    if stage == "dwell":
        for i in range(10):
            x = w * (0.04 + 0.1 * i); b = h * (0.92 + 0.03 * (i % 2))
            o.append(white_fig(p, x, b, s, r, flip=True, up=[(-22, -158), (-34, -178), (-40, -198)] if i % 3 == 0 else None))
    if stage == "nations":
        for i in range(8):
            x = w * (0.04 + 0.06 * i); b = h * (0.9 + 0.03 * (i % 2))
            king = i % 3 == 0
            crown = '<path d="M-12 -196 L -13 -208 L -6 -201 L 0 -211 L 6 -201 L 13 -208 L 12 -196 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>'
            gift = '<rect x="-56" y="-120" width="20" height="16" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></rect>'
            o.append(robed(p, x, b, s, r.choice(["#7A1A2A", "#3A2A6A", "#1F4A6A", "#5A6A3A", "#8A5A2A", "#4A3A5A"]), skin=r.choice(SKINS), hair=r.choice(HAIRS), beard="#2A1A10" if king else None,
                           mantle="#E8B830" if king else None, flip=True, pose="walk", up=[(-22, -158), (-40, -136), (-50, -118)] if king else None, extra=(crown + gift) if king else ""))
    return "".join(o)

GATES = {"N": ["REUBEN", "JUDAH", "LEVI"], "E": ["JOSEPH", "BENJAMIN", "DAN"], "S": ["SIMEON", "ISSACHAR", "ZEBULUN"], "W": ["GAD", "ASHER", "NAPHTALI"]}
STONES = [("JASPER", "#4F9A6A"), ("SAPPHIRE", "#2A4AB0"), ("CHALCEDONY", "#8AB0C0"), ("EMERALD", "#1F8A4A"), ("SARDONYX", "#C8603A"), ("SARDIUS", "#B5281E"),
          ("CHRYSOLITE", "#C8C840"), ("BERYL", "#5AC8C0"), ("TOPAZ", "#E8B040"), ("CHRYSOPRASE", "#7AC86A"), ("JACINTH", "#5A3AA8"), ("AMETHYST", "#8A4AB0")]

def city_plan(w, h):
    """The holy city in plan (21:12–14, 21:21): the wall great and high, foursquare; three gates of pearl on each side — on the
    east, the north, the south and the west — an angel at each (a point of light) and a tribe's name on each (the tribes'
    gates as Ezekiel's city names them, Ezek 48:31–34); the twelve foundations under the wall, the street of gold within."""
    import exo.art8 as B
    from epistle import plate_bg
    o = [plate_bg(w, h, "THE HOLY CITY JERUSALEM · TWELVE GATES · TWELVE FOUNDATIONS")]
    B._W[0] = w
    S = min(h - 150, w * 0.4)
    x0, y0 = w * 0.32 - S / 2 + 20, 70 + (h - 120 - S) / 2
    for k in range(12):                                         # the foundations, ring on ring under the wall
        d = 4 + k * 2.2
        o.append(f'<rect x="{f(x0 - d)}" y="{f(y0 - d)}" width="{f(S + 2 * d)}" height="{f(S + 2 * d)}" fill="none" stroke="{STONES[11 - k][1]}" stroke-width="2.2"></rect>')
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(S)}" height="{f(S)}" fill="#3A3410" stroke="#CFE8C8" stroke-width="4"></rect>')
    o.append(halo(x0 + S / 2, y0 + S / 2, S * 0.4, "#FFE680", 0.6))
    o.append(f'<path d="M{f(x0 + S / 2)} {f(y0)} L {f(x0 + S / 2)} {f(y0 + S)} M{f(x0)} {f(y0 + S / 2)} L {f(x0 + S)} {f(y0 + S / 2)}" stroke="#FFD23F" stroke-width="5" opacity="0.8"></path>')
    def gate(gx, gy, nm, side, i=1):
        o.append(f'<circle cx="{f(gx)}" cy="{f(gy)}" r="{f(S * 0.035)}" fill="#F8F6F2" stroke="#C8B8C8" stroke-width="2"></circle>'
                 f'<circle cx="{f(gx)}" cy="{f(gy)}" r="{f(S * 0.012)}" fill="#FFF4C2"></circle>')
        dx, dy, an = {"N": (0, -34, "middle"), "S": (0, 44, "middle"), "E": (34, 4, "start"), "W": (-34, 4, "end")}[side]
        if side in "NS" and i != 1:                     # the outer names of a wall run outward, clear of the middle one
            dx, an = (-6, "end") if i == 0 else (6, "start")
        o.append(geo.label(gx + dx, gy + dy, nm, "#FFD23F", max(7, min(9, S / 40)), anchor=an))
    for i, nm in enumerate(GATES["N"]): gate(x0 + S * (i + 1) / 4, y0, nm, "N", i)
    for i, nm in enumerate(GATES["S"]): gate(x0 + S * (i + 1) / 4, y0 + S, nm, "S", i)
    for i, nm in enumerate(GATES["E"]): gate(x0 + S, y0 + S * (i + 1) / 4, nm, "E")
    for i, nm in enumerate(GATES["W"]): gate(x0, y0 + S * (i + 1) / 4, nm, "W")
    sz = max(8, min(10, S / 34))
    o.append(label(x0 + S / 2, y0 - 50, "NORTH", "#8FD0E2", sz) + label(x0 + S / 2, y0 + S + 60, "SOUTH", "#8FD0E2", sz)
             + label(x0 + S + 34, y0 + S * 0.92, "EAST", "#8FD0E2", sz, anchor="start") + label(x0 - 34, y0 + S * 0.92, "WEST", "#8FD0E2", sz, anchor="end"))
    tx = w * 0.72
    o.append(tag(x0 + S * 0.25, y0, "TWELVE GATES · TWELVE PEARLS", tx, h * 0.2))
    o.append(tag(x0 + S / 2 + 6, y0 + S * 0.3, "THE STREET OF PURE GOLD", tx, h * 0.34))
    o.append(tag(x0 + S + 10, y0 + S * 0.86, "TWELVE FOUNDATIONS", tx, h * 0.5))
    o.append(label(tx, h * 0.6, "TWELVE NAMES OF THE TWELVE", "#8FD0E2", 8, anchor="start") + label(tx, h * 0.6 + 12, "APOSTLES OF THE LAMB", "#8FD0E2", 8, anchor="start"))
    o.append(tag(x0 + S * 0.75, y0 + S, "AT THE GATES TWELVE ANGELS", tx, h * 0.76))
    o.append(label(tx, h * 0.84, "GATES AS IN EZEKIEL 48", "#B8C4D0", 7, anchor="start"))   # the text names no tribe's gate
    return "".join(o)

def city_measure(w, h):
    """He measured the city with the reed, twelve thousand furlongs: the length and the breadth and the height thereof are
    equal; the wall a hundred and forty and four cubits (21:15–17): the city as a cube of light with its three dimensions,
    the wall and its measure, and the golden reed."""
    import exo.art8 as B
    from epistle import plate_bg
    o = [plate_bg(w, h, "THE CITY LIETH FOURSQUARE · MEASURED WITH A GOLDEN REED")]
    B._W[0] = w
    S = min(h * 0.44, w * 0.28)
    cx, cy = w * 0.36, max(h * 0.62, 50 + S * 1.3)
    dxs, dys = S * 0.5, S * 0.3
    front = f'M{f(cx - S / 2)} {f(cy)} L {f(cx + S / 2)} {f(cy)} L {f(cx + S / 2)} {f(cy - S)} L {f(cx - S / 2)} {f(cy - S)} Z'
    top = f'M{f(cx - S / 2)} {f(cy - S)} L {f(cx + S / 2)} {f(cy - S)} L {f(cx + S / 2 + dxs)} {f(cy - S - dys)} L {f(cx - S / 2 + dxs)} {f(cy - S - dys)} Z'
    side = f'M{f(cx + S / 2)} {f(cy)} L {f(cx + S / 2 + dxs)} {f(cy - dys)} L {f(cx + S / 2 + dxs)} {f(cy - S - dys)} L {f(cx + S / 2)} {f(cy - S)} Z'
    o.append(halo(cx + dxs / 2, cy - S / 2, S * 1.1, "#FFE680", 0.5))
    o.append(f'<path d="{side}" fill="#C8A040" opacity="0.85" stroke="#FFD23F" stroke-width="2"></path><path d="{front}" fill="#E8C860" opacity="0.85" stroke="#FFD23F" stroke-width="2"></path>'
             f'<path d="{top}" fill="#FFF0A0" opacity="0.9" stroke="#FFD23F" stroke-width="2"></path>')
    o.append(f'<rect x="{f(cx - S / 2 - 8)}" y="{f(cy - S * 0.12)}" width="{f(S + 16)}" height="{f(S * 0.12)}" fill="#CFE8C8" stroke="#4F9A6A" stroke-width="2"></rect>')
    o.append(dim(cx - S / 2, cy + 18, cx + S / 2, cy + 18, "12,000 FURLONGS", size=8))
    o.append(dim(cx - S / 2 - 22, cy, cx - S / 2 - 22, cy - S, "12,000 FURLONGS", size=8))
    o.append(dim(cx - S / 2, cy - S, cx - S / 2 + dxs, cy - S - dys, "12,000 FURLONGS", off=-12, size=7))   # the length, on the top's
                                                                              # far edge: clear of the wall's leader, and a label
    tx = w * 0.7
    o.append(tag(cx + S * 0.3, cy - S * 0.06, "THE WALL · 144 CUBITS · JASPER", tx, h * 0.74))
    o.append(tag(cx, cy - S * 0.5, "PURE GOLD, LIKE UNTO PURE GLASS", tx - w * 0.04, h * 0.3))
    o.append(f'<path d="M{f(w * 0.68)} {f(h * 0.52)} L {f(w * 0.94)} {f(h * 0.4)}" stroke="#E8B830" stroke-width="6" stroke-linecap="round"></path>' + label(w * 0.81, h * 0.56, "A GOLDEN REED", "#FFD23F", 9))
    return "".join(o)

def foundations(w, h):
    """The foundations of the wall of the city adorned with all manner of precious stones (21:19–20): the twelve, from the
    first at the bottom, each coloured as its stone and named, ordinal and stone."""
    from epistle import plate_bg
    import exo.art8 as B
    o = [plate_bg(w, h, "THE TWELVE FOUNDATIONS OF THE WALL")]
    B._W[0] = w
    ords = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH", "SEVENTH", "EIGHTH", "NINTH", "TENTH", "ELEVENTH", "TWELFTH"]
    top, bot = 36, h - 40
    ch = (bot - top) / 12
    x0, x1 = w * 0.06, w * 0.6
    o.append(f'<rect x="{f(x0 + 10)}" y="{f(top - ch * 1.2)}" width="{f(x1 - x0 - 20)}" height="{f(ch * 1.2)}" fill="#CFE8C8" stroke="#4F9A6A" stroke-width="1.6" opacity="0.9"></rect>'
             if top - ch * 1.2 > 26 else "")
    for i, (nm, c) in enumerate(STONES):                       # the first at the bottom, the twelfth at the top, each a course of the wall
        y = bot - (i + 1) * ch
        o.append(f'<rect x="{f(x0)}" y="{f(y)}" width="{f(x1 - x0)}" height="{f(ch)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></rect>'
                 f'<rect x="{f(x0)}" y="{f(y + 1)}" width="{f(x1 - x0)}" height="{f(ch * 0.28)}" fill="#FFFFFF" opacity="0.22"></rect>'
                 + geo.label((x0 + x1) / 2, y + ch * 0.5 + max(3, ch * 0.18), f"{ords[i]} · {nm}", "#F3EFE6", max(7, min(11, ch * 0.5))))
    o.append(tag(x1, bot - ch * 6, "ALL MANNER OF PRECIOUS STONES", w * 0.66, h * 0.3))
    o.append(label(w * 0.66, bot - 2, "THE FIRST AT THE FOOT OF THE WALL", "#8FD0E2", 8, anchor="start"))
    return "".join(o)

def street_gold(p, w, h, seed):
    """Within the city (21:21–23): the street of pure gold, as it were transparent glass, running to a gate of one pearl; no
    temple therein, no sun, no moon — the whole lit from within by the glory, the Lamb its lamp."""
    o = [defs(p), sky(w, h, "#FFF8DC", "#FFE6A0"), halo(w * 0.5, h * 0.3, w * 0.6, WHITE, 0.95)]
    hz = h * 0.48
    o.append(houses(-10, w * 0.32, hz + h * 0.02, h * 0.3, seed, colors=("#FFF4C2", "#F8E8B0", "#FFFDF0")) + houses(w * 0.68, w + 10, hz + h * 0.02, h * 0.3, seed + 1, colors=("#FFF4C2", "#F8E8B0", "#FFFDF0")))
    o.append(f'<path d="M{f(w * 0.44)} {f(hz)} L {f(w * 0.56)} {f(hz)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#F0C850" stroke="#C8962E" stroke-width="2" opacity="0.92"></path>')
    for k in range(1, 7):
        y = hz + (h - hz) * (k / 7) ** 1.4
        o.append(f'<path d="M{f(w * 0.44 - (w * 0.44) * (k / 7) ** 1.4)} {f(y)} L {f(w * 0.56 + (w * 0.44) * (k / 7) ** 1.4)} {f(y)}" stroke="#FFF4C2" stroke-width="1.6" opacity="0.8"></path>')
    o.append(f'<path d="M{f(w * 0.46)} {f(h * 0.7)} L {f(w * 0.5)} {f(h * 0.98)} M{f(w * 0.56)} {f(h * 0.6)} L {f(w * 0.64)} {f(h * 0.94)}" stroke="#FFFFFF" stroke-width="5" opacity="0.6"></path>')
    gw, gh = w * 0.1, h * 0.2
    o.append(f'<path d="M{f(w * 0.5 - gw)} {f(hz)} L {f(w * 0.5 - gw)} {f(hz - gh * 0.6)} A {f(gw)} {f(gw)} 0 0 1 {f(w * 0.5 + gw)} {f(hz - gh * 0.6)} L {f(w * 0.5 + gw)} {f(hz)} Z" fill="#F8F6F2" stroke="#C8B8C8" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.5 - gw * 0.55)} {f(hz)} L {f(w * 0.5 - gw * 0.55)} {f(hz - gh * 0.55)} A {f(gw * 0.55)} {f(gw * 0.55)} 0 0 1 {f(w * 0.5 + gw * 0.55)} {f(hz - gh * 0.55)} L {f(w * 0.5 + gw * 0.55)} {f(hz)} Z" fill="#FFFFFF"></path>')
    o.append(lamb(w * 0.5 - 18 * h / 600, hz - h * 0.02, h * 0.07 / 90))
    return "".join(o)

def river_life(p, w, h, seed):
    """A river of water of life, bright as crystal, proceeding out of the throne of God and of the Lamb, in the midst of the
    street; on this side of the river and on that the tree of life, bearing twelve manner of fruits (22:1–2): the throne in
    light at the head of the street (empty — God is never drawn — the Lamb before it), the river running down toward us,
    a tree of life on either bank, its leaves for the healing of the nations."""
    o = [defs(p), sky(w, h, "#FFF8DC", "#FFE6A0"), halo(w * 0.5, h * 0.16, w * 0.5, WHITE, 0.95), rays(w * 0.5, h * 0.16, 34, h * 0.05, w, "#FFFDF0", 0.4, 4)]
    hz = h * 0.36
    o.append(f'<rect x="-10" y="{f(hz)}" width="{f(w + 20)}" height="{f(h)}" fill="#F0C850"></rect>')
    o.append(empty_throne(w * 0.5, hz + 4, h * 0.2 / 180))
    o.append(lamb(w * 0.56, hz + h * 0.06, h * 0.08 / 90))
    o.append(f'<path d="M{f(w * 0.47)} {f(hz + 4)} L {f(w * 0.53)} {f(hz + 4)} C {f(w * 0.6)} {f(h * 0.6)} {f(w * 0.74)} {f(h * 0.8)} {f(w * 0.78)} {f(h + 10)} L {f(w * 0.22)} {f(h + 10)} C {f(w * 0.26)} {f(h * 0.8)} {f(w * 0.4)} {f(h * 0.6)} {f(w * 0.47)} {f(hz + 4)} Z" '
             f'fill="#C8F0FF" stroke="#5AB0D8" stroke-width="2.4"></path>')
    for k in range(6):
        y = h * (0.5 + 0.08 * k)
        o.append(f'<path d="M{f(w * (0.44 - 0.03 * k))} {f(y)} q 12 -4 24 0 q 12 4 24 0" fill="none" stroke="#FFFFFF" stroke-width="2.4" opacity="0.8"></path>')
    o.append(tree_life(w * 0.13, h * 0.98, h * 0.7 / 270, seed) + tree_life(w * 0.87, h * 0.98, h * 0.7 / 270, seed + 1))
    return "".join(o)

def servants(p, w, h, seed):
    """His servants shall serve him; and they shall see his face (22:3–5): the servants in white, of every nation, before the
    throne in light, their faces lifted to it — no night, no lamp, no sun: only the light."""
    r = random.Random(seed)
    o = [defs(p), sky(w, h, "#FFF8DC", "#FFE6A0"), halo(w * 0.5, h * 0.2, w * 0.7, WHITE, 0.95), rays(w * 0.5, h * 0.18, 40, h * 0.05, w, "#FFFDF0", 0.4, 4)]
    o.append(empty_throne(w * 0.5, h * 0.42, h * 0.26 / 180))
    for row in range(2):
        n = 10 + row * 2; s = h * (0.32 + row * 0.12) / 205; b = h * (0.8 + row * 0.17)
        for i in range(n):
            x = w * (i + 0.5) / n + r.uniform(-6, 6)
            o.append(white_fig(p, x, b, s, r, flip=x > w * 0.5, up=[(-22, -158), (-34, -178), (-40, -198)] if r.random() < 0.4 else None))
    return "".join(o)

def open_book(w, h, seed):
    """Seal not up the words of the prophecy of this book (22:10): the book open in the light, its seals broken, its words
    open to all (lines of writing, no words)."""
    o = [sky(w, h, "#1A1440", "#5A4A8A"), radiance(w, h, seed, cy=0.6)]
    s = min(w / 300, h / 160)
    cx, cy = w * 0.5, h * 0.62
    o.append(f'<path d="M{f(cx - 120 * s)} {f(cy - 40 * s)} L {f(cx)} {f(cy - 26 * s)} L {f(cx + 120 * s)} {f(cy - 40 * s)} L {f(cx + 120 * s)} {f(cy + 30 * s)} L {f(cx)} {f(cy + 44 * s)} L {f(cx - 120 * s)} {f(cy + 30 * s)} Z" '
             f'fill="#FFF8DC" stroke="#C8962E" stroke-width="3"></path><path d="M{f(cx)} {f(cy - 26 * s)} L {f(cx)} {f(cy + 44 * s)}" stroke="#C8962E" stroke-width="2"></path>')
    for k in range(6):
        y = cy - 22 * s + k * 10 * s
        o.append(f'<path d="M{f(cx - 108 * s)} {f(y - 2 * s)} L {f(cx - 12 * s)} {f(y + 10 * s)} M{f(cx + 108 * s)} {f(y - 2 * s)} L {f(cx + 12 * s)} {f(y + 10 * s)}" stroke="#8A7A5A" stroke-width="1.4" stroke-dasharray="8 3 14 3"></path>')
    for i in range(7):
        x = cx - 90 * s + i * 30 * s
        o.append(f'<path d="M{f(x - 5 * s)} {f(cy + 52 * s)} L {f(x)} {f(cy + 46 * s)} L {f(x + 3 * s)} {f(cy + 54 * s)} Z M{f(x + 4 * s)} {f(cy + 48 * s)} L {f(x + 9 * s)} {f(cy + 54 * s)} L {f(x + 4 * s)} {f(cy + 57 * s)} Z" fill="#8A2A2A" stroke="{INK}" stroke-width="1"></path>')
    return "".join(o)

def water_life(p, w, h, seed):
    """The Spirit and the bride say, Come … he that will, let him take the water of life freely (22:17): the river of water of
    life flowing out of the holy city in light across the new earth, and people of every nation coming to it, kneeling to
    drink, a cup lifted."""
    r = random.Random(seed)
    o = [defs(p), sky(w, h, "#3A5AA8", "#FFF4D8"), halo(w * 0.7, h * 0.3, w * 0.5, WHITE, 0.85)]
    hz = h * 0.56
    o.append(holy_city(w * 0.72, hz, w * 0.44, h * 0.28, seed))
    o.append(ground(w, h, hz, "#8AC86A", dy=0))
    o.append(f'<path d="M{f(w * 0.7)} {f(hz)} L {f(w * 0.76)} {f(hz)} C {f(w * 0.7)} {f(h * 0.7)} {f(w * 0.5)} {f(h * 0.8)} {f(w * 0.3)} {f(h + 10)} L {f(w * 0.1)} {f(h + 10)} C {f(w * 0.36)} {f(h * 0.8)} {f(w * 0.6)} {f(h * 0.7)} {f(w * 0.7)} {f(hz)} Z" '
             f'fill="#C8F0FF" stroke="#5AB0D8" stroke-width="2.4"></path>')
    s = h * 0.34 / 205
    for i, (x, b, fl) in enumerate(((0.06, 0.82, True), (0.42, 0.98, False), (0.54, 0.84, False), (0.62, 0.96, False))):
        o.append(white_fig(p, w * x, h * b, s, r, flip=fl, up=[(-22, -158), (-40, -168), (-52, -176)] if i % 2 == 0 else None,
                           extra='<path d="M-60 -182 C -58 -172 -44 -172 -42 -182 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>' if i == 2 else ""))
    return "".join(o)
