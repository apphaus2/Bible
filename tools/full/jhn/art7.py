"""Drawings for John 13–14. The upper room at night under the lamps: the twelve reclining at the low table with Jesus; he
rising from supper and laying aside his garments, the towel girded about him, the water poured into the basin; Jesus
kneeling with the basin and the towel at Peter's feet (warm lamplight, restrained); the basin and towel alone on the floor;
the beloved disciple leaning on his breast, the sop given to Judas across the table (13:27 "then entered Satan into him" is
words only); the door standing open on the night as Judas goes out — and it was night; the cock on the wall at grey dawn.
John 14: many mansions — a great house of many lit rooms on a height in the morning light; the way — a road going up
over the hills into the light; the Comforter — a soft light come down into the room among the eleven (no dove here: the
Spirit is not yet given); Arise, let us go hence — the eleven rising from the table. Built on jhn.art6."""
from jhn.art6 import *
from jhn.art6 import f, INK, HEB, TWELVE, P, LIE, on_bed, lying, bedroll, _loaf
import random, math

PETER_C, JUDAS_C, JOHN_C = ROBES["peter"], ROBES["judas"], ROBES["john"]

def upper(w, h, b, seed, light=0.6):
    """The upper room by night: dark plaster walls, a small window of stars, two lamps burning, the low table."""
    o = [room(w, h, b, wall="#4A3438", floor="#3A2A2A", window=(w * 0.06, w * 0.08), night_=True, seed=seed)]
    for x in (0.34, 0.7): o.append(glow(w * x, h * 0.24, h * 0.24, "#FFC14D", light, f"up{seed}{int(x * 10)}") + A.lamp(w * x, h * 0.24, min(1.2, max(0.6, h / 360))))
    return "".join(o)

def basin(x, y, s, water=True):
    """A wide brass basin on the floor, water in it."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-40 -18 C -38 4 38 4 40 -18 Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="2.4"></path>'
            f'<ellipse cx="0" cy="-18" rx="40" ry="8" fill="{"#5AA8C8" if water else "#8A6A2A"}" stroke="#0D0D0F" stroke-width="2"></ellipse></g>')

def towel_on(x, y, s):
    return (f'<path d="M{f(x - 30 * s)} {f(y)} C {f(x - 20 * s)} {f(y - 8 * s)} {f(x + 20 * s)} {f(y - 6 * s)} {f(x + 34 * s)} {f(y)} L {f(x + 30 * s)} {f(y + 4 * s)} L {f(x - 26 * s)} {f(y + 4 * s)} Z" '
            f'fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></path>')

GIRDED = '<path d="M-24 -100 L 24 -100 L 26 -82 C 10 -78 -10 -78 -26 -82 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.8"></path><path d="M14 -82 L 20 -50 L 10 -50 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></path>'

def washing(p, w, h, seed, stage="supper"):
    """The upper room. supper: the twelve reclining at the low table with Jesus in the midst. rise: Jesus risen from the
    table, his outer garment laid aside on the bench, a towel girded about him, pouring water from the pitcher into the
    basin. wash: Jesus kneeling on the floor with the basin and the towel at the feet of Peter, who sits on the bench with
    his hand raised; the others watching. sop: John leaning back on Jesus' breast, Jesus holding out the sop across the
    table to Judas. door: the door standing open on the night, Judas going out through it, the others at the table.
    rising: the eleven getting up from the table with Jesus — Arise, let us go hence."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), upper(w, h, b, seed)]
    s = fit(b, max(h * 0.26, b - 220))
    table = f'<rect x="{f(w * 0.2)}" y="{f(b - 32 * s)}" width="{f(w * 0.72)}" height="{f(12 * s)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>'
    bread = "".join(_loaf(w * (0.28 + 0.12 * i), b - 36 * s, s * 0.5) + cup(w * (0.34 + 0.12 * i), b - 32 * s, s * 0.11, color="#B5652E") for i in range(5))
    if stage in ("supper", "eleven"):                       # eleven: after Judas has gone out (no one in his colour)
        o.append(table + bread)
        for i in range(5):
            o.append(disciple_seated(w * (0.26 + 0.07 * i), b, s * 0.66, i))
            o.append(disciple_seated(w * (0.94 - 0.06 * i), b, s * 0.66, i + (7 if stage == "eleven" else 6), flip=True))
        o.append(jesus_seated(w * 0.62, b, s * 0.82))
    elif stage == "rise":
        o.append(table + bread)
        for i in range(4): o.append(disciple_seated(w * (0.6 + 0.09 * i), b, s * 0.66, i + 2, flip=True))
        o.append(f'<path d="M{f(w * 0.06)} {f(b - 30 * s)} L {f(w * 0.2)} {f(b - 30 * s)} L {f(w * 0.2)} {f(b)} L {f(w * 0.06)} {f(b)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></path>'
                 f'<path d="M{f(w * 0.07)} {f(b - 30 * s)} C {f(w * 0.1)} {f(b - 44 * s)} {f(w * 0.16)} {f(b - 44 * s)} {f(w * 0.19)} {f(b - 30 * s)} L {f(w * 0.18)} {f(b - 10 * s)} L {f(w * 0.08)} {f(b - 10 * s)} Z" fill="{JESUS_MANTLE}" stroke="{INK}" stroke-width="1.6"></path>')
        o.append(jesus(p, w * 0.34, b, s, flip=True, up=[(-22, -158), (-44, -140), (-56, -126)]).replace("</g>", GIRDED + "</g>", 1))
        o.append(basin(w * 0.34 + 70 * s, b, s * 0.8) + pitcher_carry(w * 0.34 + 62 * s, b - 112 * s, s * 0.8))
        o.append(f'<path d="M{f(w * 0.34 + 70 * s)} {f(b - 80 * s)} C {f(w * 0.34 + 74 * s)} {f(b - 60 * s)} {f(w * 0.34 + 70 * s)} {f(b - 40 * s)} {f(w * 0.34 + 72 * s)} {f(b - 18 * s)}" stroke="#5AA8C8" stroke-width="{f(4 * s)}" fill="none"></path>')
    elif stage == "wash":
        o.append(f'<rect x="{f(w * 0.5)}" y="{f(b - 40 * s)}" width="{f(w * 0.46)}" height="{f(40 * s)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>')
        o.append(seated(w * 0.56, b - 40 * s, s * 0.8, PETER_C, head=None, beard="#4A4440", flip=True))
        for i in range(3): o.append(disciple_seated(w * (0.72 + 0.1 * i), b - 40 * s, s * 0.62, i + 2, flip=True))
        o.append(f'<path d="M{f(w * 0.5)} {f(b - 4)} l {f(-14 * s)} 0" stroke="#B98A6E" stroke-width="{f(8 * s)}" stroke-linecap="round"></path>')
        o.append(glow(w * 0.38, b - 50 * s, 120 * s, "#FFC14D", 0.5, f"{p}w"))
        o.append(jesus_stoop(w * 0.3, b, s * 0.92))
        o.append(basin(w * 0.44, b, s * 0.7) + towel_on(w * 0.18, b - 2, s))
    elif stage == "sop":
        o.append(table + bread)
        o.append(jesus_seated(w * 0.4, b, s * 0.82))
        o.append(seated(w * 0.5, b, s * 0.74, JOHN_C, head=None, beard=None, flip=True, bowed=True))
        o.append(seated(w * 0.82, b, s * 0.78, JUDAS_C, head="#6A2A1A", beard="#1A1210", flip=True))
        for i in range(3): o.append(disciple_seated(w * (0.6 + 0.08 * i), b, s * 0.62, i + 7, flip=True))
        o.append(disciple_seated(w * 0.24, b, s * 0.64, 0) + disciple_seated(w * 0.14, b, s * 0.62, 3))
        o.append(f'<path d="M{f(w * 0.4 + 30 * s)} {f(b - 70 * s)} L {f(w * 0.72)} {f(b - 70 * s)}" stroke="#B9825E" stroke-width="{f(7 * s)}" stroke-linecap="round"></path>'
                 f'<ellipse cx="{f(w * 0.73)}" cy="{f(b - 72 * s)}" rx="{f(9 * s)}" ry="{f(6 * s)}" fill="#C8904A" stroke="{INK}" stroke-width="1.4"></ellipse>')
    elif stage == "door":
        o.append(f'<rect x="{f(w * 0.8)}" y="{f(h * 0.18)}" width="{f(w * 0.14)}" height="{f(b - h * 0.18)}" fill="#05051A" stroke="{INK}" stroke-width="2.4"></rect>'
                 f'<g transform="translate({f(w * 0.8)} {f(h * 0.18)})">{mk.stars(8, w * 0.14, (b - h * 0.18) * 0.6, seed)}</g>'
                 f'<path d="M{f(w * 0.8)} {f(h * 0.18)} L {f(w * 0.72)} {f(h * 0.22)} L {f(w * 0.72)} {f(b + 6)} L {f(w * 0.8)} {f(b)} Z" fill="#5A3A22" stroke="{INK}" stroke-width="2"></path>')
        o.append(mk.person(p, round(w * 0.87), round(b), round(s * 0.9, 3), body="#B98A6E", cloth=JUDAS_C, kind="Robe", sw=3, extra=A.headcloth("#6A2A1A", cord="#2A1A10") + A.BLACK_BEARD))
        o.append(f'<rect x="{f(w * 0.08)}" y="{f(b - 32 * s)}" width="{f(w * 0.56)}" height="{f(12 * s)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>')
        o.append(jesus_seated(w * 0.3, b, s * 0.82))
        for i in range(4): o.append(disciple_seated(w * (0.42 + 0.06 * i), b, s * 0.64, i, flip=True))
        o.append(disciple_seated(w * 0.14, b, s * 0.64, 5))
    elif stage == "rising":
        o.append(table)
        o.append(jesus(p, w * 0.24, b, s, flip=True, up=UP_CALL))
        for i, who in enumerate(("peter", "john", "andrew", "james", "thomas", "matthew")):
            o.append(disciple(p, w * (0.38 + 0.1 * i), b - 4 * (i % 2), s * (0.94 - 0.02 * i), who, flip=True))
    return "".join(o)

def basin_still(p, w, h, seed):
    """I have given you an example: the brass basin of water on the floor of the upper room, the pitcher beside it and the
    towel laid over its rim, in the warm light of the lamp."""
    b = h * 0.84
    o = [bgr(w, h, "#3A2A2A"), glow(w * 0.5, b - h * 0.2, h * 0.7, "#FFC14D", 0.7, f"{p}g"),
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#5A4030" stroke="{INK}" stroke-width="2"></rect>']
    k = min(4.0, max(1.2, h / 130))
    o.append(basin(w * 0.46, b + 6 * k, k) + pitcher_carry(w * 0.7, b + 4 * k, k * 1.2) + towel_on(w * 0.46 - 20 * k, b - 14 * k, k * 0.9))
    o.append(clay_lamp(w * 0.2, b - 4, k * 0.6))
    return "".join(o)

def mansions(p, w, h, seed):
    """In my Father's house are many mansions: on a height in the morning a great house of many rooms, its windows full of
    light, its doors open, a path going up to it (no one drawn in it)."""
    o = [sky(w, h, "#5A6A9A", "#FFF4C2"), rays(w * 0.5, h * 0.3, 36, 20, w, color="#FFFFFF", op=0.25), glow(w * 0.5, h * 0.36, h * 0.6, "#FFFFFF", 0.8, f"{p}g"),
         hills(w, h, h * 0.64, seed, color="#9AA87A", amp=12, step=90)]
    r = random.Random(seed)
    cx, base = w * 0.5, h * 0.66
    for row in range(3):
        n = 7 - row * 2; y = base - row * h * 0.12; ww = w * (0.6 - row * 0.14)
        o.append(f'<rect x="{f(cx - ww / 2)}" y="{f(y - h * 0.12)}" width="{f(ww)}" height="{f(h * 0.12)}" fill="#F3EAD0" stroke="{INK}" stroke-width="2"></rect>')
        for k in range(n):
            x = cx - ww / 2 + ww * (k + 0.5) / n
            o.append(f'<path d="M{f(x - 7)} {f(y - 2)} L {f(x - 7)} {f(y - h * 0.07)} Q {f(x)} {f(y - h * 0.09)} {f(x + 7)} {f(y - h * 0.07)} L {f(x + 7)} {f(y - 2)} Z" fill="#FFD23F" stroke="{INK}" stroke-width="1.4"></path>')
    o.append(f'<rect x="{f(cx - w * 0.36)}" y="{f(base)}" width="{f(w * 0.72)}" height="6" fill="#C8B898" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(ground(w, h, base + 6, "#B8B07A", dy=0))
    o.append(f'<path d="M{f(cx)} {f(base + 6)} C {f(cx - w * 0.04)} {f(h * 0.8)} {f(cx - w * 0.16)} {f(h * 0.9)} {f(cx - w * 0.2)} {f(h + 10)} L {f(cx - w * 0.1)} {f(h + 10)} C {f(cx - w * 0.06)} {f(h * 0.9)} {f(cx + w * 0.02)} {f(h * 0.8)} {f(cx + w * 0.02)} {f(base + 6)} Z" fill="#E8DCB0" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def the_way(p, w, h, seed):
    """I am the way, and the truth, and the life: a road going up and up over the hills into a dawn of white light, and
    Jesus standing at its foot."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#3A4A8A", "#FFF4C2"), glow(w * 0.62, h * 0.24, h * 0.5, "#FFFFFF", 0.95, f"{p}g"),
         rays(w * 0.62, h * 0.24, 36, 20, w, color="#FFFFFF", op=0.3),
         hills(w, h, h * 0.4, seed, color="#8A8AA0", amp=12, step=90), hills(w, h, h * 0.56, seed + 1, color="#7A8A6A", amp=12, step=80),
         ground(w, h, h * 0.7, "#9AAA6A", dy=0),
         f'<path d="M{f(w * 0.2)} {f(h + 10)} C {f(w * 0.4)} {f(h * 0.8)} {f(w * 0.5)} {f(h * 0.6)} {f(w * 0.6)} {f(h * 0.42)} L {f(w * 0.64)} {f(h * 0.42)} C {f(w * 0.6)} {f(h * 0.6)} {f(w * 0.58)} {f(h * 0.8)} {f(w * 0.5)} {f(h + 10)} Z" fill="#F3EAD0" stroke="{INK}" stroke-width="1.6"></path>']
    s = fit(b, max(h * 0.3, b - 220))
    o.append(jesus(p, w * 0.24, b, s, flip=True, up=UP_BLESS))
    return "".join(o)

def comforter(p, w, h, seed):
    """Another Comforter, even the Spirit of truth: the upper room at night, the eleven at the table, and a soft light
    falling into the room upon them from above (the Spirit is promised, not yet given: light only)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), upper(w, h, b, seed, light=0.4), shaft(w * 0.5, w, h, top_w=0.12, bot_w=0.4, color="#FFF4C2", op=0.3),
         glow(w * 0.5, 0, h * 0.6, "#FFFFFF", 0.6, f"{p}g")]
    s = fit(b, max(h * 0.26, b - 220))
    o.append(f'<rect x="{f(w * 0.06)}" y="{f(b - 32 * s)}" width="{f(w * 0.88)}" height="{f(12 * s)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(5):
        o.append(disciple_seated(w * (0.1 + 0.07 * i), b, s * 0.64, i))
        o.append(disciple_seated(w * (0.9 - 0.07 * i), b, s * 0.64, i + 6, flip=True))
    o.append(jesus_seated(w * 0.5, b, s * 0.8))
    return "".join(o)
