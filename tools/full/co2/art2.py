"""Drawings for the 2 Corinthians volume, chapter 2 (2 Corinthians 6–9): the day of salvation; the hardships of 6:4–10 over
empty places (a shut prison door, the armour of righteousness on its stand); the unequal yoke; the temple of the living God
(light over the saints gathered); come out from among them; the coming of Titus; the church at Corinth hearing the letter;
the churches of Macedonia giving; the manna and the omers; Titus and the brethren on the road with the bounty; the
collection ready in Achaia; the two sowers; the cheerful giver; the harvest; the gift carried to Jerusalem. The cast and
helpers are co2.art's."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from co2.art import *
import numbers1 as N1, samuel1 as S1, exodus4 as E4x, ruth1 as R1
from ntcast import ROBES

def bag(x, y, s=1.0, color="#8A6A3A", tie="#3A2214"):
    """A money bag tied at the neck, (x, y) its foot."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
            f'<path d="M-8 -30 C -26 -28 -30 -6 -22 0 L 22 0 C 30 -6 26 -28 8 -30 C 14 -36 10 -42 0 -40 C -10 -42 -14 -36 -8 -30 Z" fill="{color}" stroke="{INK}" stroke-width="2"></path>'
            f'<path d="M-9 -30 L 9 -30" stroke="{tie}" stroke-width="3"></path></g>')

def chest_open(x, base, s, coins_=True):
    """A wooden chest with its lid thrown back, full of coins; (x, base) the middle of its foot (about 90 × 70 at s = 1)."""
    o = [f'<g transform="translate({f(x)} {f(base)}) scale({f(s)})">',
         f'<path d="M-46 -60 L -40 -96 L 40 -96 L 46 -60 Z" fill="#6A3A1E" stroke="{INK}" stroke-width="2.4"></path>',
         f'<rect x="-48" y="-60" width="96" height="60" fill="#8A5A30" stroke="{INK}" stroke-width="2.6"></rect>',
         f'<path d="M-48 -40 L 48 -40 M-30 -60 L -30 0 M30 -60 L 30 0" stroke="#5A3418" stroke-width="2.4"></path>']
    if coins_:
        r = random.Random(7)
        for i in range(22):
            cx, cy = r.uniform(-40, 40), -60 - r.uniform(0, 10)
            o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="6" ry="2.6" fill="{r.choice(["#E8B830", "#C8C8D0", "#FFD23F"])}" stroke="{INK}" stroke-width="1"></ellipse>')
    return "".join(o) + "</g>"

# ---- 2 Corinthians 6 ------------------------------------------------------------------------------------------------------
def salvation_day(w, h, seed):
    """Behold, now is the acceptable time; behold, now is the day of salvation: the sun coming up over a walled city on its
    hill, its gates open, the road going up to it in the morning light."""
    return vista(w, h, seed, tone="dawn", horizon=0.62, hills_n=2, glow_at=(0.66, 0.5, 0.7, "#FFF4C2"), sun_at=(0.66, 0.46), city="walls", cx=0.42, cw=0.5, birds_=5)

def prison_night(p, w, h, seed):
    """In stripes, in imprisonments, in tumults … in watchings: a city street at night, the prison's iron-bound door shut
    in its stone wall, a torch burnt low beside it; no one in the street. (The sufferings are told in words only.)"""
    return prison_shut(p, w, h, seed)

def armour(w, h):
    """By the armor of righteousness on the right hand and on the left: a plate — the armour on its stand, the shield on
    the left hand and the sword on the right, the breastplate between, in the light."""
    import exo.art8 as B
    o = [plate_bg(w, h, "2 CORINTHIANS 6:7 · THE ARMOR OF RIGHTEOUSNESS")]
    k = min(w / 520, (h - 40) / 200); cx, b = w * 0.5, h - 24
    o.append(halo(cx, b - 100 * k, 150 * k, "#FFF4C2", 0.35))
    o.append(f'<path d="M{f(cx)} {f(b)} L {f(cx)} {f(b - 150 * k)} M{f(cx - 40 * k)} {f(b)} L {f(cx + 40 * k)} {f(b)}" stroke="#8A6A3A" stroke-width="{f(6 * k)}"></path>'
             f'<path d="M{f(cx - 44 * k)} {f(b - 150 * k)} C {f(cx - 46 * k)} {f(b - 110 * k)} {f(cx - 34 * k)} {f(b - 70 * k)} {f(cx)} {f(b - 60 * k)} C {f(cx + 34 * k)} {f(b - 70 * k)} {f(cx + 46 * k)} {f(b - 110 * k)} {f(cx + 44 * k)} {f(b - 150 * k)} '
             f'C {f(cx + 20 * k)} {f(b - 162 * k)} {f(cx - 20 * k)} {f(b - 162 * k)} {f(cx - 44 * k)} {f(b - 150 * k)} Z" fill="#B8860E" stroke="{INK}" stroke-width="2.6"></path>'
             f'<path d="M{f(cx)} {f(b - 156 * k)} L {f(cx)} {f(b - 64 * k)} M{f(cx - 36 * k)} {f(b - 124 * k)} C {f(cx - 12 * k)} {f(b - 116 * k)} {f(cx + 12 * k)} {f(b - 116 * k)} {f(cx + 36 * k)} {f(b - 124 * k)}" stroke="#7A5208" stroke-width="2" fill="none"></path>')
    sx = cx - 130 * k
    o.append(f'<ellipse cx="{f(sx)}" cy="{f(b - 92 * k)}" rx="{f(46 * k)}" ry="{f(58 * k)}" fill="#7A2A1E" stroke="{INK}" stroke-width="2.8"></ellipse>'
             f'<ellipse cx="{f(sx)}" cy="{f(b - 92 * k)}" rx="{f(36 * k)}" ry="{f(46 * k)}" fill="none" stroke="#E8B830" stroke-width="2.4"></ellipse>'
             f'<circle cx="{f(sx)}" cy="{f(b - 92 * k)}" r="{f(10 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="2"></circle>')
    wx = cx + 130 * k
    o.append(f'<path d="M{f(wx - 5 * k)} {f(b - 40 * k)} L {f(wx - 5 * k)} {f(b - 168 * k)} L {f(wx)} {f(b - 182 * k)} L {f(wx + 5 * k)} {f(b - 168 * k)} L {f(wx + 5 * k)} {f(b - 40 * k)} Z" fill="#D8D8E0" stroke="{INK}" stroke-width="2"></path>'
             f'<rect x="{f(wx - 22 * k)}" y="{f(b - 42 * k)}" width="{f(44 * k)}" height="{f(7 * k)}" fill="#B8860E" stroke="{INK}" stroke-width="1.8"></rect>'
             f'<rect x="{f(wx - 4 * k)}" y="{f(b - 35 * k)}" width="{f(8 * k)}" height="{f(26 * k)}" fill="#5A3A22" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<circle cx="{f(wx)}" cy="{f(b - 7 * k)}" r="{f(6 * k)}" fill="#B8860E" stroke="{INK}" stroke-width="1.6"></circle>')
    o.append(label(sx, b + 14, "ON THE LEFT", CY, 10) + label(wx, b + 14, "ON THE RIGHT HAND", CY, 10))
    return "".join(o)

def ox(x, y, s, color="#8A5A30", patch="#E8D8B8"):
    """An ox: samuel1's cow without the udder."""
    return (S1.cow(x, y, s, color=color, patch=patch)
            .replace('<path d="M-36 -50 C -36 -38 -16 -36 -14 -50 Z" fill="#E89A9A" stroke="#0D0D0F" stroke-width="1.6"></path>', "")
            .replace('<path d="M-30 -42 L -30 -36 M-20 -42 L -20 -36" stroke="#0D0D0F" stroke-width="2"></path>', ""))

def unequal_yoke(w, h, seed):
    """Be not unequally yoked: an ox and an ass under one wooden yoke in a furrowed field at evening, the beam tilted
    between the tall beast and the low one, the plough behind them going crooked."""
    b = h * 0.9
    o = [sky(w, h, "#5A3A6A", "#FFC890"), sun(w * 0.84, h * 0.42, 14, color="#FFE680", op=0.3), hills(w, h, h * 0.46, seed, color="#7A6A5A", amp=10, step=80),
         ground(w, h, h * 0.54, "#8A6A4A", dy=0)]
    for i in range(6):
        y = h * (0.6 + 0.07 * i)
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y + 6)} {f(w * 0.6)} {f(y - 10 + i * 3)} {f(w + 10)} {f(y + 8)}" stroke="#6A4A30" stroke-width="2" fill="none"></path>')
    k = max(0.5, (b - h * 0.3) / 150)
    ox_ = w * 0.46
    o.append(ox(ox_, b - 10, k))
    ka = k * 0.78; ax = ox_ + 6 * k
    o.append(N1.ass(ax, b + 10, ka, color="#9A9488"))
    y1 = (ox_ + 76 * k, b - 10 - 106 * k); y2 = (ax + 50 * ka, b + 10 - 94 * ka)
    for (cx_, cy_), kk in ((y1, k), (y2, ka)):
        o.append(f'<path d="M{f(cx_ - 9 * kk)} {f(cy_)} C {f(cx_ - 12 * kk)} {f(cy_ + 30 * kk)} {f(cx_ + 12 * kk)} {f(cy_ + 30 * kk)} {f(cx_ + 9 * kk)} {f(cy_)}" fill="none" stroke="{INK}" stroke-width="{f(6 * kk)}"></path>'
                 f'<path d="M{f(cx_ - 9 * kk)} {f(cy_)} C {f(cx_ - 12 * kk)} {f(cy_ + 30 * kk)} {f(cx_ + 12 * kk)} {f(cy_ + 30 * kk)} {f(cx_ + 9 * kk)} {f(cy_)}" fill="none" stroke="#C8A060" stroke-width="{f(3 * kk)}"></path>')
    o.append(f'<path d="M{f(y1[0])} {f(y1[1])} L {f(y2[0])} {f(y2[1])}" stroke="{INK}" stroke-width="{f(11 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(y1[0])} {f(y1[1])} L {f(y2[0])} {f(y2[1])}" stroke="#7A4A22" stroke-width="{f(7 * k)}" stroke-linecap="round"></path>')
    mx, my = (y1[0] + y2[0]) / 2, (y1[1] + y2[1]) / 2
    o.append(f'<path d="M{f(mx)} {f(my)} L {f(w * 0.16)} {f(b - 36 * k)} L {f(w * 0.12)} {f(b + 4)} M{f(w * 0.16)} {f(b - 36 * k)} L {f(w * 0.08)} {f(b - 86 * k)}" stroke="#5A3A22" stroke-width="{f(5 * k)}" fill="none"></path>')
    return "".join(o)

def temple_living(p, w, h, seed):
    """We are a temple of the living God; even as God said, I will dwell in them: the saints gathered in a house, standing
    together, and the light coming down upon them from above (light only; no idol and no figure of God)."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#5A4A5A", floor="#3A2E34"),
         f'<path d="M{f(w * 0.36)} 0 L {f(w * 0.64)} 0 L {f(w * 0.86)} {f(b)} L {f(w * 0.14)} {f(b)} Z" fill="#FFF4C2" opacity="0.35"></path>',
         halo(w * 0.5, h * 0.1, max(w, h) * 0.3, "#FFFFFF", 0.7), rays(w * 0.5, -h * 0.05, 18, h * 0.1, h * 0.9, "#FFF4C2", 0.25, 5, a0=60, a1=120)]
    s = fit(b, max(h * 0.24, b - 210))
    for i, x in enumerate((0.16, 0.27, 0.38, 0.5, 0.62, 0.73, 0.84)):
        o.append(brother(p, w * x, b, s * (0.96 + 0.04 * (i % 2)), i, flip=x > 0.5, up=[(-22, -158), (-34, -184), (-36, -214)] if i in (2, 5) else None))
    return "".join(o)

def come_out(p, w, h, seed):
    """Come ye out from among them, and be ye separate: the gate of an idol city at evening, a temple of the idols dark on
    its height within the walls, and a few going out of the gate along the road toward the light."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#2A2A5A", "#FFD8A0"), halo(w * 0.9, h * 0.4, max(w, h) * 0.4, "#FFF4C2", 0.55),
         hills(w, h, h * 0.56, seed, color="#5A4A5A", amp=12, step=80), ground(w, h, h * 0.62, "#8A7058", dy=0)]
    tx, ty, tw = w * 0.22, h * 0.28, w * 0.18
    o.append(f'<path d="M{f(tx - tw * 0.8)} {f(h * 0.5)} L {f(tx - tw * 0.6)} {f(ty + tw * 0.2)} L {f(tx + tw * 0.6)} {f(ty + tw * 0.2)} L {f(tx + tw * 0.8)} {f(h * 0.5)} Z" fill="#4A3A44" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(tx - tw / 2 - 6)} {f(ty)} L {f(tx)} {f(ty - tw * 0.26)} L {f(tx + tw / 2 + 6)} {f(ty)} Z" fill="#5A4A50" stroke="{INK}" stroke-width="1.8"></path>'
             + "".join(f'<rect x="{f(tx - tw / 2 + tw * j / 6 - 3)}" y="{f(ty)}" width="6" height="{f(tw * 0.2)}" fill="#6A5A60" stroke="{INK}" stroke-width="1"></rect>' for j in range(1, 6)))
    o.append(walls(w * -0.02, w * 0.44, h * 0.66, h * 0.32, seed, color="#6A5A5A", gate=True, towers=2))
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.66)} C {f(w * 0.5)} {f(h * 0.7)} {f(w * 0.7)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.78)} L {f(w + 10)} {f(h * 0.9)} C {f(w * 0.7)} {f(h * 0.96)} {f(w * 0.5)} {f(h * 0.82)} {f(w * 0.3)} {f(h * 0.7)} Z" fill="#C8A878" stroke="{INK}" stroke-width="1.6"></path>')
    s = fit(b, max(h * 0.24, b - 190))
    for i, x in enumerate((0.56, 0.68, 0.8)):
        o.append(brother(p, w * x, b - (2 - i) * 6, s * (0.9 + 0.04 * i), [0, 2, 4][i], flip=True))
    return "".join(o)

# ---- 2 Corinthians 7 ------------------------------------------------------------------------------------------------------
def basin_water(w, h, seed):
    """Let us cleanse ourselves from all defilement of flesh and spirit: a basin of clean water and its pitcher on a stone
    ledge, the morning light falling into the water."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#D8C8A8"></rect>',
         f'<path d="M{f(w * 0.56)} -10 L {f(w * 0.8)} -10 L {f(w * 0.62)} {f(h * 0.86)} L {f(w * 0.3)} {f(h * 0.86)} Z" fill="#FFF8DC" opacity="0.6"></path>']
    ly = h * 0.82
    o.append(f'<rect x="-10" y="{f(ly)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></rect>')
    k = min(1.6, h / 220); bx = w * 0.46
    o.append(f'<path d="M{f(bx - 90 * k)} {f(ly - 46 * k)} C {f(bx - 80 * k)} {f(ly)} {f(bx + 80 * k)} {f(ly)} {f(bx + 90 * k)} {f(ly - 46 * k)} Z" fill="#B87A3A" stroke="{INK}" stroke-width="2.6"></path>'
             f'<ellipse cx="{f(bx)}" cy="{f(ly - 46 * k)}" rx="{f(90 * k)}" ry="{f(16 * k)}" fill="#8FD0E2" stroke="{INK}" stroke-width="2.4"></ellipse>'
             f'<ellipse cx="{f(bx + 10 * k)}" cy="{f(ly - 48 * k)}" rx="{f(40 * k)}" ry="{f(6 * k)}" fill="#FFFFFF" opacity="0.7"></ellipse>')
    px = w * 0.74
    o.append(f'<path d="M{f(px - 18 * k)} {f(ly)} C {f(px - 40 * k)} {f(ly - 40 * k)} {f(px - 30 * k)} {f(ly - 80 * k)} {f(px - 12 * k)} {f(ly - 96 * k)} L {f(px - 14 * k)} {f(ly - 112 * k)} '
             f'L {f(px + 14 * k)} {f(ly - 112 * k)} L {f(px + 12 * k)} {f(ly - 96 * k)} C {f(px + 30 * k)} {f(ly - 80 * k)} {f(px + 40 * k)} {f(ly - 40 * k)} {f(px + 18 * k)} {f(ly)} Z" fill="#B5652E" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(px + 24 * k)} {f(ly - 86 * k)} C {f(px + 50 * k)} {f(ly - 84 * k)} {f(px + 46 * k)} {f(ly - 50 * k)} {f(px + 30 * k)} {f(ly - 44 * k)}" fill="none" stroke="{INK}" stroke-width="{f(5 * k)}"></path>')
    return "".join(o)

def fears_within(p, w, h, seed):
    """When we were come into Macedonia our flesh had no relief … without were fightings, within were fears: Paul sitting
    alone by the lamp in a room at night, the storm beating at the window; no fighting is drawn."""
    b = h * 0.95
    o = [room(w, h, b, wall="#3A2E3A", floor="#2A2228"), lamp_glow(w * 0.4, b - h * 0.3, max(w, h) * 0.32, f"{p}lg", op=0.45)]
    wx, ww, wt = w * 0.62, min(w * 0.22, h * 0.5), h * 0.18
    uid = f"{p}wn"
    o.append(f'<defs><clipPath id="{uid}"><rect x="{f(wx)}" y="{f(wt)}" width="{f(ww)}" height="{f(ww * 0.9)}"></rect></clipPath></defs><g clip-path="url(#{uid})">'
             + f'<rect x="{f(wx)}" y="{f(wt)}" width="{f(ww)}" height="{f(ww)}" fill="#14141E"></rect>' + bolt(wx + ww * 0.6, wt, wt + ww * 0.8, seed, color="#C8C8E8", sw=3)
             + f'<g transform="translate({f(wx)} {f(wt)})">' + rain(ww, ww, seed, n=30, color="#8A8AA8", op=0.6) + '</g></g>'
             + f'<rect x="{f(wx)}" y="{f(wt)}" width="{f(ww)}" height="{f(ww * 0.9)}" fill="none" stroke="{INK}" stroke-width="3"></rect>'
             + f'<path d="M{f(wx + ww / 2)} {f(wt)} L {f(wx + ww / 2)} {f(wt + ww * 0.9)}" stroke="#4A3A2A" stroke-width="4"></path>')
    k = min(1.2, h / 280)
    o.append(low_table(w * 0.32, b, 60 * k, k) + clay_lamp(w * 0.32 + 30 * k, b - 31 * k, k * 0.6))
    s = (b - max(h * 0.22, b - 200)) / 135
    o.append(seated(w * 0.2, b, s, ROBES["paul"], head="#5A4A3A", beard="#3A2A1A", bowed=True))
    return "".join(o)

def titus_comes(p, w, h, seed):
    """God … comforted us by the coming of Titus: the door of the house in Macedonia open on the street in the afternoon,
    Titus come in from the road with his staff and his travelling bag, Paul going to meet him with his hands out, Timothy
    behind."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#C8A878", floor="#8A6A4A")]
    s = fit(b, max(h * 0.24, b - 220))
    dx, dw = w * 0.64, min(w * 0.22, 150 * s)
    o.append(doorway(dx, b - 220 * s, dw, b, seed, night=False))
    staff = '<path d="M34 -150 L 46 6" stroke="#5A3A22" stroke-width="5"></path>'
    pack = '<path d="M-26 -156 C -40 -140 -40 -110 -30 -100 L -18 -104 C -26 -120 -24 -140 -16 -152 Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(titus_fig(p, dx + dw * 0.45, b, s, extra=staff + pack))
    o.append(paul_fig(p, w * 0.44, b, s, flip=True, up=[(-22, -158), (-48, -142), (-72, -136)]))
    o.append(timothy_fig(p, w * 0.24, b, s * 0.97, flip=True))
    return "".join(o)

def corinth_reading(p, w, h, seed):
    """What earnest care it wrought in you: the church at Corinth gathered by lamplight, one of the brethren standing and
    reading Paul's letter aloud from the roll, the rest sitting and listening."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#5A4232", floor="#3A2A20"), lamp_glow(w * 0.3, b - h * 0.5, max(w, h) * 0.45, f"{p}lg", op=0.45)]
    s = fit(b, max(h * 0.24, b - 220))
    roll = open_letter(-70, -186, 46, 30, rows=4, seed=seed)
    o.append(brother(p, w * 0.2, b, s, 1, flip=True, up=[(-22, -158), (-44, -170), (-62, -176)], extra=roll))
    o.append(clay_lamp(w * 0.08, h * 0.34, min(1.2, h / 260)) + f'<rect x="{f(w * 0.05)}" y="{f(h * 0.34)}" width="{f(w * 0.06)}" height="6" fill="#6A4A2A" stroke="{INK}" stroke-width="1.4"></rect>')
    for i, x in enumerate((0.4, 0.51, 0.62, 0.73, 0.84, 0.94)):
        o.append(seated(w * x, b, s * 0.8, ["#4A5A6A", "#3A5A4A", "#5A4A5A", "#8A7A5A", "#4A4A6A", "#6A6A5A"][i], head=["#2A3A4A", "#1F3A5A", "#3A3A4A", None, "#2A2A3A", "#F3EFE6"][i],
                        beard=["#2A1A10", None, "#3A2A1A", "#2A1A10", None, "#B8B2A8"][i], flip=True))
    return "".join(o)

# ---- 2 Corinthians 8 ------------------------------------------------------------------------------------------------------
def macedonia_giving(p, w, h, seed):
    """In much proof of affliction … their deep poverty abounded unto the riches of their liberality: the saints of a
    church in Macedonia, poor folk in plain and patched clothes, bringing what they have to the chest set out in the
    courtyard — a purse, a few coins, a woman's bracelet."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.62, seed, hmin=0.2, hmax=0.32, stairs=True),
         pavement(w, h, h * 0.62, color="#C8B898")]
    s = fit(b, max(h * 0.24, b - 210))
    o.append(chest_open(w * 0.5, b, s * 0.9))
    hand = [(-22, -158), (-40, -130), (-58, -118)]
    o.append(brother(p, w * 0.34, b, s, 7, flip=True, up=hand) + brother(p, w * 0.22, b, s * 0.98, 5, flip=True) + brother(p, w * 0.1, b, s, 4, flip=True))
    o.append(brother(p, w * 0.66, b, s, 2, up=hand) + brother(p, w * 0.78, b, s, 3) + brother(p, w * 0.9, b, s * 0.97, 6))
    return "".join(o)

def manna_omers(w, h, seed):
    """He that gathered much had nothing over; and he that gathered little had no lack: a plate — the manna lying white on
    the ground at dawn, and the measures of those who gathered much and little, each an omer, level full."""
    o = [plate_bg(w, h, "2 CORINTHIANS 8:15 · AN OMER A HEAD")]
    gy = h * 0.6
    o.append(f'<rect x="10" y="{f(gy)}" width="{f(w - 20)}" height="{f(h - gy - 10)}" fill="#1E2A3A" stroke="{CY}" stroke-width="1.2"></rect>'
             + E4x.manna(120, 16, w - 16, gy + 6, h - 16, seed))
    k = min(1.2, (gy - 40) / 120)
    for i, (x, t) in enumerate(((0.3, "GATHERED MUCH · NOTHING OVER"), (0.7, "GATHERED LITTLE · NO LACK"))):
        cx, by = w * x, gy - 6; hh = 70 * k; cw = 44 * k
        o.append(f'<path d="M{f(cx - cw)} {f(by - hh)} L {f(cx + cw)} {f(by - hh)} L {f(cx + cw * 0.8)} {f(by)} L {f(cx - cw * 0.8)} {f(by)} Z" fill="#B5652E" stroke="{INK}" stroke-width="2.4"></path>'
                 f'<ellipse cx="{f(cx)}" cy="{f(by - hh)}" rx="{f(cw)}" ry="{f(8 * k)}" fill="#F8F6F0" stroke="{INK}" stroke-width="2"></ellipse>'
                 + label(cx, by - hh - 18 * k, t, GOLD, 10))
    o.append(dim(w * 0.3 + 60 * k, gy - 6 - 70 * k, w * 0.7 - 60 * k, gy - 6 - 70 * k, "EQUALITY", size=9, color=CY))
    return "".join(o)

def titus_road(p, w, h, seed):
    """We have sent together with him the brother whose praise in the gospel is spread through all the churches: Titus and
    the two brethren on the road south from Macedonia, an ass behind them carrying the bags of the bounty."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), vista(w, h, seed, tone="day", horizon=0.56, hills_n=2, far="mount", cx=0.7, cw=0.5, birds_=3, ground_=False),
         ground(w, h, h * 0.6, "#C8A870", dy=0),
         f'<path d="M-10 {f(h * 0.82)} C {f(w * 0.3)} {f(h * 0.78)} {f(w * 0.6)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.64)} L {f(w + 10)} {f(h * 0.74)} C {f(w * 0.6)} {f(h * 0.82)} {f(w * 0.3)} {f(h * 0.98)} -10 {f(h + 10)} Z" fill="#E0C898" stroke="{INK}" stroke-width="1.6"></path>']
    s = fit(b, max(h * 0.24, b - 200))
    staff = '<path d="M34 -150 L 46 6" stroke="#5A3A22" stroke-width="5"></path>'
    o.append(titus_fig(p, w * 0.62, b, s, flip=True, extra=staff))
    o.append(brother(p, w * 0.5, b, s * 0.98, 0, flip=True, extra=staff) + brother(p, w * 0.39, b, s, 3, flip=True, extra=staff))
    ka = s * 0.62
    o.append(N1.ass(w * 0.2, b, ka, flip=False, color="#9A9488"))
    o.append(bag(w * 0.2 - 10 * ka, b - 88 * ka, ka * 0.9, "#8A6A3A") + bag(w * 0.2 + 26 * ka, b - 86 * ka, ka * 0.9, "#6A5A3A"))
    return "".join(o)

# ---- 2 Corinthians 9 ------------------------------------------------------------------------------------------------------
def achaia_ready(p, w, h, seed):
    """Achaia hath been prepared for a year past: in a house at Corinth the chest of the bounty, laid by week by week, the
    money bags tied and stacked beside it, a lamp."""
    b = h * 0.92
    o = [room(w, h, b, wall="#C8A878", floor="#8A6A4A", window=(w * 0.72, min(w * 0.1, h * 0.26)))]
    k = min(1.8, h / 170)
    o.append(chest_open(w * 0.42, b, k))
    for i, (dx, c) in enumerate(((-110, "#8A6A3A"), (-80, "#6A5A3A"), (80, "#7A5A3A"), (106, "#8A6A3A"), (93, "#5A4A3A"))):
        o.append(bag(w * 0.42 + dx * k, b - (30 * k if i == 4 else 0), k * 0.8, c))
    o.append(clay_lamp(w * 0.16, b - 4, k * 0.8))
    return "".join(o)

def two_sowers(p, w, h, seed):
    """He that soweth sparingly shall reap also sparingly; and he that soweth bountifully shall reap also bountifully: two
    fields side by side at harvest — at the left a thin crop, a few ears standing apart; at the right the grain thick and
    tall; a sower in each, one casting a pinch, the other a wide arc."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.36, seed, color="#9AAA7A", amp=12, step=90), ground(w, h, h * 0.44, "#8A6A4A", dy=0)]
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.44)} L {f(w * 0.5)} {f(h + 10)}" stroke="#F3EFE6" stroke-width="2" stroke-dasharray="6 5"></path>')
    r = random.Random(seed)
    for _ in range(9):
        x = r.uniform(w * 0.04, w * 0.46); y = r.uniform(h * 0.56, h * 0.96)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x + 2)} {f(y - 26)}" stroke="#C8A060" stroke-width="2"></path><ellipse cx="{f(x + 2)}" cy="{f(y - 30)}" rx="3" ry="7" fill="#E8C060" stroke="#8A6A3A" stroke-width="1"></ellipse>')
    o.append(grain(w * 0.5, w + 10, h * 0.98, h * 0.4, seed))
    gy = h * 0.86
    s = fit(gy, max(h * 0.12, gy - 210))
    sbag = '<path d="M14 -120 C 30 -116 34 -96 26 -84 C 16 -80 8 -90 10 -104 Z" fill="#C8A060" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(robed(p, w * 0.24, gy, s, "#7A6A5A", head="#3A3A4A", cord="#1A1210", beard="#3A2A1A", flip=True, up=[(-22, -158), (-34, -140), (-44, -132)], extra=sbag))
    o.append(robed(p, w * 0.72, gy, s, "#7A5A30", head="#E8E2D6", cord="#3A2214", beard="#2A1A10", flip=True, up=[(-22, -158), (-50, -170), (-76, -160)], extra=sbag))
    for i in range(14):
        a = math.radians(200 + i * 10); rr = 70 + (i % 3) * 18
        o.append(f'<circle cx="{f(w * 0.72 + math.cos(a) * rr * s * -1)}" cy="{f(gy - 150 * s + math.sin(a) * rr * s * -0.6)}" r="2" fill="#E8D8A0"></circle>')
    o.append(plate_label(w * 0.25, h * 0.08, "SPARINGLY", "#12113A", 11, halo_="#F3EFE6") + plate_label(w * 0.75, h * 0.08, "BOUNTIFULLY", "#12113A", 11, halo_="#F3EFE6"))
    return "".join(o)

def cheerful_giver(p, w, h, seed):
    """Not grudgingly, or of necessity: for God loveth a cheerful giver: in the courtyard where the church meets, a man
    tipping out his purse into the chest with both hands, a woman beside him bringing hers, the morning sun on them."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#FFE6A0", "#FFF8E6"), halo(w * 0.8, h * 0.2, max(w, h) * 0.4, "#FFFFFF", 0.6),
         houses(w, h, h * 0.64, seed, hmin=0.2, hmax=0.3, stairs=True), pavement(w, h, h * 0.64, color="#D8C8A8")]
    s = fit(b, max(h * 0.24, b - 220))
    cx = w * 0.5
    o.append(chest_open(cx, b, s * 0.95))
    purse = bag(-62, -136, 0.7, "#8A6A3A")
    o.append(brother(p, cx - 80 * s, b, s, 7, flip=True, up=[(-22, -158), (-44, -150), (-62, -144)], extra=purse))
    for i in range(6):
        o.append(f'<ellipse cx="{f(cx - 22 * s + i * 7 * s)}" cy="{f(b - 104 * s + i * 4 * s)}" rx="{f(4 * s)}" ry="{f(2 * s)}" fill="#E8B830" stroke="{INK}" stroke-width="0.8"></ellipse>')
    o.append(brother(p, cx + 84 * s, b, s, 2, up=[(-22, -158), (-40, -134), (-56, -124)]))
    o.append(brother(p, w * 0.12, b, s * 0.97, 4, flip=True) + brother(p, w * 0.88, b, s * 0.97, 6))
    return "".join(o)

def harvest_poor(p, w, h, seed):
    """He hath scattered abroad, he hath given to the poor … he that supplieth seed to the sower and bread for food: the
    harvest field in the evening, the sheaves standing, the corners of the field left for the poor, two women gleaning there."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#5A3A6A", "#FFC890"), sun(w * 0.82, h * 0.36, 16, color="#FFE680", op=0.3),
         hills(w, h, h * 0.42, seed, color="#7A6A5A", amp=10, step=80), ground(w, h, h * 0.5, "#C8A060", dy=0), grain(w * 0.56, w + 10, h * 0.7, h * 0.18, seed)]
    for i, x in enumerate((0.12, 0.24, 0.36, 0.48)):
        o.append(R1.sheaf(w * x, h * (0.66 + 0.06 * (i % 2)), min(1.1, h / 280)))
    s = fit(b, max(h * 0.24, b - 190))
    down = [(-22, -158), (-36, -124), (-42, -96)]
    o.append(brother(p, w * 0.66, b, s * 0.9, 2, up=down, extra=R1.sheaf(-48, -84, 0.4)) + brother(p, w * 0.84, b, s * 0.88, 5, flip=True, up=down))
    return "".join(o)

def to_jerusalem_gift(w, h):
    """The ministration of this service … filleth up the measure of the wants of the saints: the bounty of Macedonia and
    Achaia carried to the saints at Jerusalem, on the map."""
    return geo.med_map(w, h, box=(20.6, 36.4, 30.8, 42.0), places=("PHILIPPI", "THESSALONICA", "CORINTH", "CENCHREÆ", "EPHESUS", "JERUSALEM"),
                       routes=[["PHILIPPI", "THESSALONICA", (22.3, 39.6), (22.7, 38.7), "CORINTH"], ["CENCHREÆ", (24.5, 36.4), (29.0, 34.4), (34.0, 32.6), "CÆSAREA", "JERUSALEM"]],
                       hi=("JERUSALEM",), regions=("MACEDONIA", "ACHAIA", "ASIA", "JUDÆA", "THE GREAT SEA"), lit_routes=[1], size=10,
                       title="2 CORINTHIANS 9:12 · THE MINISTERING TO THE SAINTS")
