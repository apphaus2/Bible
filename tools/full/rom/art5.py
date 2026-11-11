"""Drawings for Romans chapter 5 (Romans 12–16), on top of rom.art4. A man standing before the altar with his hands open,
presenting himself (12:1: no beast slain); the plate of one body and many members; the plate of the gifts; the believers at
table (Acts' breaking of bread) for hospitality; bread, a water jar and a pan of coals on a doorstep (12:20); a Roman on the
judgment-seat (Gallio, as Acts draws him) and the plate of tribute — the coins, the sword sheathed; the tables of the law
summed up in one heart; the armour of light by a window at dawn (13:12); two at table, herbs and meat (14:2); the plate of
the days; the throne in light and every knee bowed far below (14:10–11, God never drawn); the table of meat and wine; the
root of Jesse, a green shoot from the stump (15:12); the nations with hands lifted; the map from Jerusalem round about
unto Illyricum and the map of the road to Spain (15:19, 15:24–28, Acts' projection); Phoebe come to Rome with the letter;
the brethren with Paul at Corinth (16:21–23)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from rom.art4 import *
from rom.art4 import f, INK, GOLD, CY, plate_label, _heart, _tablets, _jar
from rom.art import _bird_idol
from epistle import paul_fig, robed, TERTIUS_LOOK, PHOEBE_LOOK, scribe_seated, pigeonholes, low_table, doorway, mat
from act.art import breaking_bread
from act.art16 import rome
from act.art10 import judgment_bema, timothy
from act import geo
from exo.art8 import box

def living_sacrifice(p, w, h, seed):
    """Present your bodies a living sacrifice: a man standing before the altar of burnt-offering in the morning, his hands
    open and lifted, the fire on the altar and its smoke going up (no beast slain)."""
    b = h * 0.93
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#5A7AA8", "#FFE6B0"), halo(w * 0.66, h * 0.3, max(w, h) * 0.4, "#FFF4C2", 0.5),
         ground(w, h, h * 0.78, "#C8B08A", dy=0)]
    k = min(1.6, h / 250)
    ax = w * 0.64
    o.append(box(ax - 60 * k, b, 120 * k, 50 * k, 70 * k, fill="#B87333", top="#D88A4A", side="#8A5022"))
    for i in range(4):
        o.append(f'<path d="M{f(ax - 60 * k + i * 30 * k + 8)} {f(b - 70 * k)} L {f(ax - 60 * k + i * 30 * k + 8)} {f(b - 10)}" stroke="#7A4A1E" stroke-width="1.6"></path>')
    o.append(E.blaze(ax - 6 * k, b - 72 * k, 70 * k, 50 * k, seed, n=6) + smoke(ax - 6 * k, b - 120 * k, 6, seed, color="#8A8A9A", op=0.45, k=k * 0.5))
    s = (h * 0.68) / 205
    o.append(robed(p, w * 0.3, b, s, "#6A5A4A", head="#3A4A5A", cord="#1A2A3A", beard="#3A2A1A", flip=True, up=[(-22, -158), (-40, -186), (-50, -214)]))
    return "".join(o)

def one_body(w, h):
    """As we have many members in one body: a plate — a man's silhouette, its members named (the eye, the ear, the hand, the
    foot), every line running out to the many figures round it, all one body."""
    o = [plate_bg(w, h, "ROMANS 12:4–5 · MANY MEMBERS · ONE BODY"), mk.defs("ob124", *ALL)]
    cx, by = w * 0.5, h - 14; s = (by - 50) / 205
    o.append(halo(cx, by - 110 * s, 90 * s, "#FFE680", 0.35) + mk.person("ob124", round(cx), round(by), round(s, 3), body="#2A5A7A", cloth="#1E4A6A", kind="Tunic", stroke=GOLD, sw=2.4))
    parts = [("THE EYE", (6, -190)), ("THE EAR", (-12, -186)), ("THE HAND", (-29, -88)), ("THE FOOT", (10, -4))]
    for i, (t, (dx, dy)) in enumerate(parts):
        x, y = cx + dx * s, by + dy * s
        side = 1 if i % 2 == 0 else -1
        o.append(tag(x, y, t, cx + side * w * 0.22, y - 10, color=CY))
    for i in range(10):
        a = math.radians(200 + i * 14) if i < 5 else math.radians(-20 - (i - 5) * 14)
        fx = cx + math.cos(a) * w * 0.4 * (1 if i >= 5 else 1); fy = by - 10
        fx = w * (0.06 + 0.04 * i) if i < 5 else w * (0.94 - 0.04 * (i - 5))
        o.append(mk.person("ob124", round(fx), round(by), round(s * 0.42, 3), body="#1E4A6A", cloth="#163A56", kind="Tunic", woman=i % 2 == 1, stroke=CY, sw=2.2, flip=i >= 5)
                 + f'<path d="M{f(fx)} {f(by - 90 * s * 0.42)} L {f(cx)} {f(by - 110 * s)}" stroke="{GOLD}" stroke-width="1" opacity="0.5"></path>')
    return "".join(o)

def gifts_plate(w, h):
    """Gifts differing: a plate of seven emblems — prophecy (a scroll and a light), ministry (a basin and a towel), teaching
    (a tablet), exhorting (an open hand), giving (coins), ruling (a staff), showing mercy (bread and a cup)."""
    o = [plate_bg(w, h, "ROMANS 12:6–8 · GIFTS DIFFERING")]
    names = ["PROPHECY", "MINISTRY", "TEACHING", "EXHORTING", "GIVING", "RULING", "MERCY"]
    n = len(names); R = min(w / (n * 2.4), h * 0.24); cy = h * 0.52
    for i, t in enumerate(names):
        cx = w * (i + 0.5) / n; k = R / 40
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R)}" fill="#12304A" stroke="{GOLD}" stroke-width="2"></circle>')
        if i == 0: o.append(halo(cx, cy - 10 * k, 20 * k, "#FFF4C2", 0.8) + f'<rect x="{f(cx - 16 * k)}" y="{f(cy)}" width="{f(32 * k)}" height="{f(10 * k)}" rx="3" fill="#EADBB4"></rect>')
        elif i == 1: o.append(f'<path d="M{f(cx - 18 * k)} {f(cy)} L {f(cx + 18 * k)} {f(cy)} L {f(cx + 12 * k)} {f(cy + 12 * k)} L {f(cx - 12 * k)} {f(cy + 12 * k)} Z" fill="#B87333"></path><path d="M{f(cx - 10 * k)} {f(cy - 16 * k)} L {f(cx + 10 * k)} {f(cy - 16 * k)} L {f(cx + 8 * k)} {f(cy - 2 * k)} L {f(cx - 8 * k)} {f(cy - 2 * k)} Z" fill="#E8E2D6"></path>')
        elif i == 2: o.append(f'<rect x="{f(cx - 14 * k)}" y="{f(cy - 18 * k)}" width="{f(28 * k)}" height="{f(34 * k)}" fill="#C8B888"></rect>' + "".join(f'<path d="M{f(cx - 9 * k)} {f(cy - 10 * k + j * 7 * k)} l {f(18 * k)} 0" stroke="#4A3020" stroke-width="1.4"></path>' for j in range(4)))
        elif i == 3: o.append(f'<path d="M{f(cx - 10 * k)} {f(cy + 16 * k)} L {f(cx - 10 * k)} {f(cy - 4 * k)} L {f(cx - 14 * k)} {f(cy - 16 * k)} M{f(cx - 4 * k)} {f(cy - 4 * k)} L {f(cx - 4 * k)} {f(cy - 20 * k)} M{f(cx + 2 * k)} {f(cy - 4 * k)} L {f(cx + 2 * k)} {f(cy - 20 * k)} M{f(cx + 8 * k)} {f(cy - 2 * k)} L {f(cx + 8 * k)} {f(cy - 16 * k)} M{f(cx + 12 * k)} {f(cy + 4 * k)} L {f(cx + 18 * k)} {f(cy - 6 * k)}" stroke="#D9A27A" stroke-width="{f(4 * k)}" stroke-linecap="round" fill="none"></path>')
        elif i == 4: o.append("".join(f'<ellipse cx="{f(cx + (j % 3 - 1) * 10 * k)}" cy="{f(cy + 8 * k - (j // 3) * 6 * k)}" rx="{f(7 * k)}" ry="{f(3 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="0.8"></ellipse>' for j in range(6)))
        elif i == 5: o.append(f'<path d="M{f(cx - 8 * k)} {f(cy + 20 * k)} L {f(cx + 6 * k)} {f(cy - 18 * k)} C {f(cx + 10 * k)} {f(cy - 26 * k)} {f(cx + 18 * k)} {f(cy - 22 * k)} {f(cx + 14 * k)} {f(cy - 14 * k)}" stroke="#C8A060" stroke-width="{f(4 * k)}" fill="none"></path>')
        else: o.append(f'<ellipse cx="{f(cx - 8 * k)}" cy="{f(cy + 6 * k)}" rx="{f(10 * k)}" ry="{f(6 * k)}" fill="#C8904A"></ellipse>' + cup(cx + 10 * k, cy + 14 * k, 0.24 * k))
        o.append(label(cx, cy + R + 16, t, GOLD, max(7, min(9.5, R / 4.2))))
    return "".join(o)

def table_guests(p, w, h, seed):
    """Given to hospitality: the believers at a low table under the lamp, sharing bread (Acts' drawing)."""
    return breaking_bread(p, w, h, seed)

def coals(w, h, seed):
    """If thine enemy hunger, feed him; if he thirst, give him to drink: a loaf and a jar of water set on a doorstep by a
    door at dusk, and beside them a pan of glowing coals (12:20)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A2A"></rect>']
    dx, dw = w * 0.56, min(w * 0.22, h * 0.5)
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.08)}" width="{f(dw)}" height="{f(h * 0.7)}" fill="#5A3A1E" stroke="{INK}" stroke-width="3"></rect>'
             f'<path d="M{f(dx + dw / 2)} {f(h * 0.08)} L {f(dx + dw / 2)} {f(h * 0.78)}" stroke="{INK}" stroke-width="2"></path>'
             f'<rect x="-10" y="{f(h * 0.78)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></rect>')
    k = min(1.6, h / 220); y = h * 0.86
    from ecc.art import loaf
    o.append(loaf(w * 0.2, y, k * 0.9) if True else "")
    o.append(_jar(w * 0.32, y + 6, k * 0.55, "#B8784A"))
    px = w * 0.44
    o.append(halo(px, y - 10 * k, 50 * k, "#FF8A3D", 0.6)
             + f'<path d="M{f(px - 30 * k)} {f(y - 10 * k)} L {f(px + 30 * k)} {f(y - 10 * k)} L {f(px + 22 * k)} {f(y + 4 * k)} L {f(px - 22 * k)} {f(y + 4 * k)} Z" fill="#4A4A4A" stroke="{INK}" stroke-width="2"></path>')
    r = random.Random(seed)
    o.append("".join(f'<circle cx="{f(px + r.uniform(-24, 24) * k)}" cy="{f(y - 12 * k - r.uniform(0, 6) * k)}" r="{f(r.uniform(3, 6) * k)}" fill="{r.choice(["#FF6A2A", "#FFC14D", "#D7261E"])}" stroke="#2A0A0A" stroke-width="1"></circle>' for _ in range(14)))
    return "".join(o)

def ruler_seat(p, w, h, seed):
    """The higher powers: a Roman magistrate on the judgment-seat in the forum (Gallio, as Acts draws him), no one before him."""
    return judgment_bema(p, w, h, seed, gallio_=True, accusers=False, paul_=False)

def tribute(w, h):
    """Render to all their dues: a plate — tribute coins stacked, the sword in its sheath laid down, and the four dues:
    TRIBUTE · CUSTOM · FEAR · HONOR."""
    o = [plate_bg(w, h, "ROMANS 13:4–7 · RENDER TO ALL THEIR DUES")]
    k = min(w / 700, h / 220); y = h * 0.6
    for i in range(4):
        for j in range(5 - i):
            x = w * 0.16 + i * 34 * k
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y - j * 7 * k)}" rx="{f(15 * k)}" ry="{f(5 * k)}" fill="#C8C8D0" stroke="{INK}" stroke-width="1.2"></ellipse>')
    cx = w * 0.3
    o.append(f'<circle cx="{f(cx)}" cy="{f(y - 60 * k)}" r="{f(26 * k)}" fill="#C8C8D0" stroke="{INK}" stroke-width="2"></circle>'
             f'<path d="M{f(cx - 10 * k)} {f(y - 44 * k)} C {f(cx - 14 * k)} {f(y - 60 * k)} {f(cx - 6 * k)} {f(y - 76 * k)} {f(cx + 6 * k)} {f(y - 76 * k)} C {f(cx + 12 * k)} {f(y - 70 * k)} {f(cx + 10 * k)} {f(y - 62 * k)} {f(cx + 14 * k)} {f(y - 58 * k)} L {f(cx + 8 * k)} {f(y - 54 * k)} L {f(cx + 8 * k)} {f(y - 44 * k)} Z" fill="#9A9AA4" stroke="{INK}" stroke-width="1.2"></path>')
    sx = w * 0.62
    o.append(f'<g transform="rotate(-12 {f(sx)} {f(y)})"><rect x="{f(sx - 110 * k)}" y="{f(y - 8 * k)}" width="{f(180 * k)}" height="{f(16 * k)}" rx="{f(6 * k)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(sx + 70 * k)}" y="{f(y - 18 * k)}" width="{f(8 * k)}" height="{f(36 * k)}" fill="#C8963E" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<rect x="{f(sx + 78 * k)}" y="{f(y - 5 * k)}" width="{f(34 * k)}" height="{f(10 * k)}" fill="#8A5A30" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<circle cx="{f(sx + 116 * k)}" cy="{f(y)}" r="{f(7 * k)}" fill="#C8963E" stroke="{INK}" stroke-width="1.6"></circle></g>')
    o.append(tag(sx, y - 20 * k, "THE SWORD · NOT IN VAIN", sx + 40 * k, y - 70 * k, color=CY))
    for i, t in enumerate(["TRIBUTE", "CUSTOM", "FEAR", "HONOR"]):
        o.append(label(w * (0.14 + i * 0.24), h - 18, t, GOLD, 10))
    return "".join(o)

def law_love(w, h):
    """Love therefore is the fulfilment of the law: a plate — the two tables of stone, the commandments' rows running into one
    heart: THOU SHALT LOVE THY NEIGHBOR AS THYSELF."""
    o = [plate_bg(w, h, "ROMANS 13:8–10 · SUMMED UP IN THIS WORD")]
    k = min(w / 520, (h - 40) / 230); cy = h * 0.55
    o.append(_tablets(w * 0.26, cy, k))
    for i in range(5):
        y = cy - 34 * k + i * 18 * k
        o.append(f'<path d="M{f(w * 0.26 + 70 * k)} {f(y)} C {f(w * 0.5)} {f(y)} {f(w * 0.56)} {f(cy)} {f(w * 0.66)} {f(cy)}" stroke="{GOLD}" stroke-width="1.6" fill="none" opacity="0.7"></path>')
    o.append(_heart(w * 0.76, cy, 56 * k, writing=False) + label(w * 0.76, min(h - 12, cy + 80 * k), "LOVE · THE FULFILMENT OF THE LAW", GOLD, 10))
    return "".join(o)

def armor_light(w, h, seed):
    """The night is far spent, and the day is at hand; put on the armor of light: a window at the end of night, the dawn
    breaking over the roofs, and before it on its stand a soldier's armour — helmet, breastplate, shield — made of light."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1E1828"></rect>']
    wx, ww, wy, wh = w * 0.46, w * 0.46, h * 0.1, h * 0.62
    o.append(f'<defs><linearGradient id="al{seed}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1A1A4A"></stop><stop offset="0.6" stop-color="#8A5A7A"></stop><stop offset="1" stop-color="#FFC890"></stop></linearGradient></defs>'
             f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}" fill="url(#al{seed})" stroke="{INK}" stroke-width="3"></rect>'
             + f'<g transform="translate({f(wx)} {f(wy)})">' + mk.stars(14, ww, wh * 0.3, seed) + houses(ww, wh, wh * 0.86, seed, hmin=0.12, hmax=0.24) + '</g>'
             + halo(wx + ww * 0.6, wy + wh * 0.86, wh * 0.4, "#FFE680", 0.6)
             + f'<path d="M{f(wx + ww / 2)} {f(wy)} L {f(wx + ww / 2)} {f(wy + wh)}" stroke="#4A3424" stroke-width="5"></path>'
             f'<rect x="-10" y="{f(h * 0.86)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2028" stroke="{INK}" stroke-width="2"></rect>')
    cx, k = w * 0.24, min(1.6, h / 260)
    o.append(halo(cx, h * 0.5, 120 * k, "#FFF4C2", 0.65))
    o.append(f'<path d="M{f(cx)} {f(h * 0.86)} L {f(cx)} {f(h * 0.3)}" stroke="#5A3A22" stroke-width="{f(5 * k)}"></path>'
             f'<path d="M{f(cx - 32 * k)} {f(h * 0.36)} C {f(cx - 40 * k)} {f(h * 0.5)} {f(cx - 30 * k)} {f(h * 0.62)} {f(cx)} {f(h * 0.66)} C {f(cx + 30 * k)} {f(h * 0.62)} {f(cx + 40 * k)} {f(h * 0.5)} {f(cx + 32 * k)} {f(h * 0.36)} Z" fill="#FFF4C2" stroke="#E8B830" stroke-width="3"></path>'
             f'<path d="M{f(cx - 18 * k)} {f(h * 0.3)} C {f(cx - 20 * k)} {f(h * 0.2)} {f(cx + 20 * k)} {f(h * 0.2)} {f(cx + 18 * k)} {f(h * 0.3)} Z" fill="#FFFDF0" stroke="#E8B830" stroke-width="3"></path>'
             f'<path d="M{f(cx - 24 * k)} {f(h * 0.2)} L {f(cx + 24 * k)} {f(h * 0.2)}" stroke="#E8B830" stroke-width="{f(5 * k)}"></path>'
             f'<ellipse cx="{f(cx + 60 * k)}" cy="{f(h * 0.62)}" rx="{f(30 * k)}" ry="{f(42 * k)}" fill="#FFF8DC" stroke="#E8B830" stroke-width="3"></ellipse>'
             + plate_label(cx, h * 0.17, "HELMET", "#12113A", 9).replace('stroke="#0B1A2E"', 'stroke="#FFF4C2"') + plate_label(cx - 50 * k, h * 0.5, "BREASTPLATE", "#12113A", 9, "end").replace('stroke="#0B1A2E"', 'stroke="#FFF4C2"')
             + plate_label(cx + 60 * k, h * 0.62 + 56 * k, "SHIELD", "#12113A", 9).replace('stroke="#0B1A2E"', 'stroke="#FFF4C2"'))
    return "".join(o)

def two_diners(p, w, h, seed):
    """One man hath faith to eat all things: but he that is weak eateth herbs: two men at one table, a dish of herbs before
    the one, a dish of meat before the other, neither despising (both standing at the long table)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#C8A878", floor="#8A6A4A")]
    s = (h * 0.7) / 205
    ty = b - 80 * s
    o.append(robed(p, w * 0.22, b, s, "#5A6A3A", head="#3A4A3A", cord="#1A2A1A", beard="#2A1A10", flip=True))
    o.append(robed(p, w * 0.78, b, s, "#6A4A5A", hair="#2A1A10", beard="#3A2A1A"))
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(ty)}" width="{f(w * 0.4)}" height="{f(10 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(x)}" y="{f(ty + 10 * s)}" width="{f(8 * s)}" height="{f(b - ty - 10 * s)}" fill="#5A2E16" stroke="{INK}" stroke-width="1.6"></rect>' for x in (w * 0.32, w * 0.66)))
    hx, mx = w * 0.4, w * 0.6
    o.append(f'<ellipse cx="{f(hx)}" cy="{f(ty - 2)}" rx="{f(26 * s)}" ry="{f(7 * s)}" fill="#C8B898" stroke="{INK}" stroke-width="1.6"></ellipse>'
             + "".join(f'<path d="M{f(hx + d * s)} {f(ty - 4)} C {f(hx + d * s - 4)} {f(ty - 16 * s)} {f(hx + d * s + 4)} {f(ty - 20 * s)} {f(hx + d * s)} {f(ty - 26 * s)}" stroke="#4A8A3A" stroke-width="{f(3 * s)}" fill="none"></path>' for d in (-14, -6, 2, 10, 16))
             + f'<ellipse cx="{f(mx)}" cy="{f(ty - 2)}" rx="{f(26 * s)}" ry="{f(7 * s)}" fill="#C8B898" stroke="{INK}" stroke-width="1.6"></ellipse>'
             f'<ellipse cx="{f(mx)}" cy="{f(ty - 10 * s)}" rx="{f(18 * s)}" ry="{f(9 * s)}" fill="#8A3A1E" stroke="{INK}" stroke-width="1.6"></ellipse>')
    o.append(label(hx, ty + 28 * s, "HERBS", "#12113A", 9) + label(mx, ty + 28 * s, "MEAT", "#12113A", 9))
    return "".join(o)

def days_plate(w, h):
    """One man esteemeth one day above another: another esteemeth every day alike: a plate — a row of seven days, one lit
    above the rest; below, the same seven all alike."""
    o = [plate_bg(w, h, "ROMANS 14:5–6 · ONE DAY ABOVE ANOTHER · EVERY DAY ALIKE")]
    cw = min(w * 0.1, 70); x0 = w * 0.5 - 3.5 * cw
    for row, y in enumerate((h * 0.32, h * 0.62)):
        for i in range(7):
            lit = row == 0 and i == 6
            o.append((halo(x0 + (i + 0.5) * cw, y + cw * 0.4, cw, "#FFE680", 0.6) if lit else "")
                     + f'<rect x="{f(x0 + i * cw + 4)}" y="{f(y)}" width="{f(cw - 8)}" height="{f(cw * 0.8)}" fill="{GOLD if lit else "#12304A"}" stroke="{CY}" stroke-width="1.6"></rect>'
                     + label(x0 + (i + 0.5) * cw, y + cw * 0.5, str(i + 1), "#0B1A2E" if lit else CY, 11))
    return "".join(o)

def knees_bow(p, w, h, seed):
    """We shall all stand before the judgment-seat of God; to me every knee shall bow: an empty throne in light high above, and
    far below on the plain a great company kneeling (God never drawn)."""
    b = h * 0.94
    o = [sky(w, h, "#2A3A7A", "#FFF4C2"), halo(w * 0.5, h * 0.2, max(w, h) * 0.4, "#FFFFFF", 0.85), rays(w * 0.5, h * 0.2, 30, 30, max(w, h), "#FFFDF0", 0.3, 3),
         clouds(w, h * 0.34, seed, n=6, color="#FFFDF0", op=0.8, h=h), ground(w, h, h * 0.7, "#8A8A6A", dy=0)]
    k = min(1.0, h / 400)
    o.append(f'<g transform="translate({f(w * 0.5)} {f(h * 0.2)}) scale({f(k)})"><path d="M-40 40 L -40 -30 C -40 -60 40 -60 40 -30 L 40 40 Z" fill="#FFE680" stroke="#C8962E" stroke-width="3"></path>'
             '<rect x="-56" y="30" width="112" height="16" fill="#FFD23F" stroke="#C8962E" stroke-width="3"></rect></g>')
    r = random.Random(seed)
    for row in range(3):
        y = h * (0.78 + row * 0.07); ks = (h * 0.12 + row * h * 0.03) / 140
        for i in range(9 + row * 2):
            x = w * (0.04 + (i + 0.5) / (9 + row * 2) * 0.92) + r.uniform(-6, 6)
            o.append(E.kneel(x, y, ks, color=r.choice(["#6A4A3A", "#3A4A6A", "#5A6A3A", "#7A3A3A", "#4A3A5A", "#E8E2D6"]), skin=SKIN, flip=x > w * 0.5))
    return "".join(o)

def meat_wine(w, h, seed):
    """It is good not to eat flesh, nor to drink wine, nor to do anything whereby thy brother stumbleth: a table with meat and
    a cup of wine on it, set aside, and bread (no one)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A3424"></rect>', lamp_glow(w * 0.5, h * 0.3, max(w, h) * 0.5, f"mw{seed}", op=0.4)]
    ty = h * 0.68; k = min(1.6, h / 220)
    o.append(f'<rect x="-10" y="{f(ty)}" width="{f(w + 20)}" height="{f(h)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2.4"></rect>')
    from ecc.art import loaf
    o.append(f'<ellipse cx="{f(w * 0.3)}" cy="{f(ty + 10 * k)}" rx="{f(46 * k)}" ry="{f(12 * k)}" fill="#C8B898" stroke="{INK}" stroke-width="1.6"></ellipse>'
             f'<ellipse cx="{f(w * 0.3)}" cy="{f(ty)}" rx="{f(30 * k)}" ry="{f(14 * k)}" fill="#8A3A1E" stroke="{INK}" stroke-width="1.6"></ellipse>'
             + cup(w * 0.56, ty + 14 * k, 0.5 * k) + loaf(w * 0.76, ty + 14 * k, k * 0.8))
    return "".join(o)

def jesse_root(w, h, seed):
    """There shall be the root of Jesse: the stump of a felled tree in the field, and out of it a green shoot rising into the
    light."""
    o = [sky(w, h, "#5A7AA8", "#FFE6B0"), halo(w * 0.5, h * 0.3, max(w, h) * 0.4, "#FFF4C2", 0.6), hills(w, h, h * 0.62, seed, color="#8A9A6A", amp=10, step=90),
         ground(w, h, h * 0.72, "#9AAA6A", dy=0)]
    cx, b = w * 0.5, h * 0.9; k = min(1.6, h / 240)
    o.append(f'<path d="M{f(cx - 60 * k)} {f(b)} C {f(cx - 50 * k)} {f(b - 20 * k)} {f(cx - 46 * k)} {f(b - 50 * k)} {f(cx - 44 * k)} {f(b - 60 * k)} L {f(cx + 44 * k)} {f(b - 60 * k)} C {f(cx + 46 * k)} {f(b - 50 * k)} {f(cx + 50 * k)} {f(b - 20 * k)} {f(cx + 60 * k)} {f(b)} Z" fill="#6A5040" stroke="{INK}" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(b - 60 * k)}" rx="{f(44 * k)}" ry="{f(10 * k)}" fill="#C8A878" stroke="{INK}" stroke-width="2"></ellipse>'
             + "".join(f'<ellipse cx="{f(cx)}" cy="{f(b - 60 * k)}" rx="{f(44 * k * t)}" ry="{f(10 * k * t)}" fill="none" stroke="#8A6A4A" stroke-width="1.2"></ellipse>' for t in (0.3, 0.55, 0.8)))
    o.append(f'<path d="M{f(cx + 10 * k)} {f(b - 60 * k)} C {f(cx + 14 * k)} {f(b - 100 * k)} {f(cx + 4 * k)} {f(b - 130 * k)} {f(cx + 12 * k)} {f(b - 160 * k)}" stroke="#4A8A3A" stroke-width="{f(4 * k)}" fill="none"></path>'
             + "".join(f'<ellipse cx="{f(cx + 12 * k + (8 if j % 2 else -8) * k)}" cy="{f(b - 90 * k - j * 18 * k)}" rx="{f(9 * k)}" ry="{f(4 * k)}" transform="rotate({-30 if j % 2 else 30} {f(cx + 12 * k)} {f(b - 90 * k - j * 18 * k)})" fill="#7AB84A" stroke="{INK}" stroke-width="1"></ellipse>' for j in range(5)))
    return "".join(o)

def nations_praise(p, w, h, seed):
    """Praise the Lord, all ye Gentiles: a company of many nations on a hill at sunrise, their hands lifted."""
    return scene(p, w, h, seed, "road", [(0.06, "crowd", {"n": 12, "x1": 0.94, "women": 0.45, "up": [(-22, -158), (-30, -196), (-40, -230)]})], tone="dusk")

def illyricum(w, h):
    """From Jerusalem, and round about even unto Illyricum: the map — Paul's road from Jerusalem through Syria, Asia,
    Macedonia and Achaia, bending round to the coast of Illyricum."""
    rt = ["JERUSALEM", "ANTIOCH", "TARSUS", "ICONIUM", "EPHESUS", "TROAS", "PHILIPPI", "THESSALONICA", "BERŒA", (20.4, 41.6), (19.6, 42.2)]
    return geo.med_map(w, h, box=(16.0, 38.5, 30.5, 44.4), places=("JERUSALEM", "ANTIOCH", "EPHESUS", "PHILIPPI", "THESSALONICA", "CORINTH"), routes=[rt], red=True,
                       hi=("JERUSALEM",), regions=("SYRIA", "ASIA", "MACEDONIA", "ACHAIA", "GALATIA", ("ILLYRICUM", 18.6, 43.3)), title="ROMANS 15:19 · ROUND ABOUT EVEN UNTO ILLYRICUM")

def to_spain(w, h):
    """I go unto Jerusalem, ministering unto the saints … I will go on by you unto Spain: the map — from Corinth to Jerusalem
    with the contribution of Macedonia and Achaia, then by Rome unto Spain (the way hoped for, dotted)."""
    o = geo.med_map(w, h, box=(-9.5, 37.0, 30.0, 44.0), places=("CORINTH", "JERUSALEM", "ROME"), routes=[["CORINTH", (27.0, 36.6), (31.0, 34.6), "JERUSALEM"]], red=True,
                    hi=("JERUSALEM", "ROME"), regions=("MACEDONIA", "ACHAIA", "ITALY", ("SPAIN", -4.0, 40.2), "THE GREAT SEA"), title="ROMANS 15:24–28 · BY YOU UNTO SPAIN", size=8)
    P = geo.Proj(w, h, (-9.5, 37.0, 30.0, 44.0))
    pts = [P(35.23, 31.78), P(25, 36.0), P(15.5, 38.2), P(12.5, 41.9), P(6.0, 40.2), P(-0.4, 39.47)]
    d = "M" + " L ".join(f"{f(x)} {f(y)}" for x, y in pts)
    sx, sy = pts[-1]
    o = o[:-4] + (f'<path d="{d}" fill="none" stroke="#FFD23F" stroke-width="2" stroke-dasharray="3 6"></path>'
                  f'<circle cx="{f(sx)}" cy="{f(sy)}" r="4" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.2"></circle>') + o[-4:]
    return o

def phoebe_rome(p, w, h, seed):
    """I commend unto you Phoebe: Phoebe come to Rome, the sealed letter in her hand, received at a house door by two of the
    saints, the city behind."""
    b = h * 0.94
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), f'<g>{rome("pr" + p, w, h * 0.8, seed)}</g>', ground(w, h, h * 0.8, "#B8A87A", dy=0)]
    o.append(f'<rect x="{f(w * 0.66)}" y="{f(h * 0.36)}" width="{f(w * 0.3)}" height="{f(b - h * 0.36)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2.4"></rect>'
             + doorway(w * 0.72, h * 0.5, w * 0.12, b, seed, night=False))
    s = (h * 0.66) / 205
    scroll_ = sealed_scroll(-70, -150, 0.3, rot=12)
    o.append(robed(p, w * 0.42, b, s * 0.94, PHOEBE_LOOK["cloth"], woman=True, veil=PHOEBE_LOOK["veil"], mantle=PHOEBE_LOOK["mantle"], flip=True,
                   up=[(-22, -158), (-42, -146), (-62, -146)], extra=scroll_))
    o.append(robed(p, w * 0.62, b, s, "#6A4A3A", head="#C8B080", cord="#6A4A2A", beard="#3A2214", up=[(-22, -158), (-42, -146), (-62, -146)]))
    o.append(robed(p, w * 0.74, b, s * 0.94, "#5A6A8A", woman=True, veil="#3A6A8A"))
    return "".join(o)

def brethren(p, w, h, seed, stage="timothy"):
    """The brethren with Paul at Corinth, in the room where the letter is written: stage "timothy" Timothy (young, beardless,
    in his grey-blue tunic) with Lucius, Jason and Sosipater standing by Paul, Tertius at his roll; "gaius" Gaius the host,
    Erastus the treasurer of the city (a toga) and Quartus."""
    b = h * 0.95
    k = (h * 0.72) / 205
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * 0.5, b - 80 * k, max(w, h) * 0.55, f"{p}bl", op=0.45),
         pigeonholes(w * 0.04, b - 205 * k, min(w * 0.18, 120 * k), min(h * 0.3, 76 * k), seed)]
    o.append(paul_fig(p, w * 0.16, b, k, flip=True))
    o.append(scribe_seated(w * 0.3, b - 4 * k, k, **{kk: vv for kk, vv in TERTIUS_LOOK.items() if kk in ("cloth", "head", "cord")}, stage="write"))
    if stage == "timothy":
        o.append(robed(p, w * 0.52, b, k * 0.98, "#7A8A9A", hair="#3A2214", flip=True))
        for i, (c, hd, bd) in enumerate((("#5A4A6A", "#2A2A4A", "#2A1A10"), ("#4A5A3A", "#E8E2D6", "#3A2A1A"), ("#6A5A3A", "#3A4A5A", "#6A645E"))):
            o.append(robed(p, w * (0.66 + i * 0.12), b, k * (0.97 + 0.02 * (i % 2)), c, head=hd, cord="#1A1210", beard=bd, flip=True))
    else:
        o.append(robed(p, w * 0.54, b, k, "#6A4A3A", head="#E8E2D6", cord="#3A2A1A", beard="#9A948A", flip=True))
        o.append(toga_fig(p, w * 0.7, b, k, hr="#4A3A2A", border="#2A4A6A", flip=True))
        o.append(robed(p, w * 0.84, b, k * 0.98, "#3A5A6A", hair="#2A1A10", beard="#2A1A10", flip=True))
    return "".join(o)
