"""Drawings for the proverbs of Solomon, Proverbs 10–29 (chapters 4–10 of the volume): the scenes on chapter title pages and
the drawn cells among the sayings, on top of pro.art3 (everything there is re-exported here)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from pro.art3 import *
from pro.art3 import f, K2, K1, EM, INK, SON_C, WIS_C, STRANGE_C, glow, son_fig, wisdom_fig, veiled, emb_art, deer, stone_well, street_row
import judges2 as J2

def father_son(p, w, h, seed, gate=False):
    """A wise son maketh a glad father: Solomon in the court of his house with his son, an open scroll between them."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFE3B8"), ground(w, h, b, "#E8C88A", dy=0)]
    if gate: o.append(S4.gatehouse(w * 0.82, b, min(w * 0.36, h * 0.9), h * 0.66))
    else:
        o.append(f'<rect x="-10" y="{f(h * 0.2)}" width="{f(w + 20)}" height="{f(b - h * 0.2)}" fill="#D8C8A0" stroke="{INK}" stroke-width="2"></rect>'
                 + "".join(f'<rect x="{f(x)}" y="{f(h * 0.2)}" width="{f(w * 0.05)}" height="{f(b - h * 0.2)}" fill="#C8B890" stroke="{INK}" stroke-width="1.6"></rect>' for x in [w * (0.08 + i * 0.22) for i in range(5)]))
    s = min(fit(b, h * 0.3), 1.3)
    o.append(glow(w * 0.48, b - 110 * s, 150 * s, "#FFE680", 0.35))
    o.append(K1.sol_fig(p, w * 0.36, b, s, flip=True, up=[(-22, -158), (-44, -136), (-62, -128)]))
    o.append(son_fig(p, w * 0.6, b, s * 0.86, up=[(-22, -158), (-44, -136), (-62, -128)]))
    o.append(f'<rect x="{f(w * 0.48 - 40 * s)}" y="{f(b - 132 * s)}" width="{f(80 * s)}" height="{f(30 * s)}" fill="#F3E8C8" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<rect x="{f(w * 0.48 - 46 * s)}" y="{f(b - 136 * s)}" width="{f(8 * s)}" height="{f(38 * s)}" rx="3" fill="#8A5A30" stroke="{INK}" stroke-width="1.4"></rect>'
             f'<rect x="{f(w * 0.48 + 38 * s)}" y="{f(b - 136 * s)}" width="{f(8 * s)}" height="{f(38 * s)}" rx="3" fill="#8A5A30" stroke="{INK}" stroke-width="1.4"></rect>')
    return "".join(o)

def watercourses(p, w, h, seed):
    """The king's heart is in the hand of Jehovah as the watercourses: channels of water turned across a green garden, the
    king standing among them, light from above (God is never drawn)."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#5A8FC8", "#E8F6FA"), EM.rays(w * 0.5, -h * 0.1, 11, 30, max(w, h), "#FFE680", 0.35, 5, 40, 140),
         hills(w, h, h * 0.42, seed, "#6A9A4A", amp=10, step=80), ground(w, h, h * 0.5, "#7AAA4A", dy=0)]
    k = max(w, h)
    for x0, x1 in ((0.5, 0.1), (0.5, 0.36), (0.5, 0.64), (0.5, 0.9)):
        d = f'M{f(w * x0)} {f(h * 0.5)} C {f(w * x0)} {f(h * 0.7)} {f(w * x1)} {f(h * 0.7)} {f(w * x1)} {f(h + 10)}'
        o.append(f'<path d="{d}" fill="none" stroke="#0D0D0F" stroke-width="{f(k * 0.024)}"></path><path d="{d}" fill="none" stroke="#2C9DB8" stroke-width="{f(k * 0.018)}"></path>')
    s = min(fit(b, h * 0.4), 1.1)
    o.append(K1.sol_fig(p, w * 0.24, b, s))
    for x in (0.74, 0.82):
        o.append(EM.tree(w * x, h * 0.62, s * 0.7))
    return "".join(o)

def wise_gate(p, w, h, seed):
    """Incline thine ear, and hear the words of the wise: elders seated at the city gate, a youth standing to hear them."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE3B8", "#E8C88A"), ground(w, h, b, "#C8A06A", dy=0), S4.gatehouse(w * 0.66, b, min(w * 0.5, h * 1.0), h * 0.74)]
    s = min(fit(b, h * 0.36), 1.0)
    for x, c in ((0.36, "#5A4A3A"), (0.46, "#3A4A6A"), (0.84, "#6A4A3A"), (0.94, "#4A5A3A")):
        o.append(E.kneel(w * x, b, s * 0.85, color=c, flip=x > 0.6))
    o.append(son_fig(p, w * 0.16, b, s))
    return "".join(o)

def wine_mast(p, w, h, seed):
    """Look not thou upon the wine when it is red: a red cup and a jar on the table in a dark room, an adder coiled by the
    jar; through the window, a lone mast rocking on the sea at night (no drunkard drawn)."""
    import snake
    b = h * 0.9
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1018"></rect>']
    wx, wy, ww, wh = w * 0.56, h * 0.12, min(w * 0.36, h * 1.0), h * 0.5
    o.append(f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}" fill="#0B0B2A" stroke="{INK}" stroke-width="3"></rect>'
             + f'<g transform="translate({f(wx)} {f(wy)})">{mk.stars(14, ww, wh * 0.5, seed)}</g>'
             f'<rect x="{f(wx)}" y="{f(wy + wh * 0.62)}" width="{f(ww)}" height="{f(wh * 0.38)}" fill="#0F3A5A"></rect>'
             f'<path d="M{f(wx + ww * 0.5)} {f(wy + wh * 0.66)} L {f(wx + ww * 0.56)} {f(wy + wh * 0.12)}" stroke="#8A5A30" stroke-width="4"></path>'
             f'<path d="M{f(wx + ww * 0.36)} {f(wy + wh * 0.66)} C {f(wx + ww * 0.4)} {f(wy + wh * 0.74)} {f(wx + ww * 0.62)} {f(wy + wh * 0.74)} {f(wx + ww * 0.68)} {f(wy + wh * 0.64)} Z" fill="#5A3A22" stroke="{INK}" stroke-width="1.6"></path>')
    ty = b - h * 0.18
    o.append(f'<rect x="{f(w * 0.04)}" y="{f(ty)}" width="{f(w * 0.52)}" height="{f(h * 0.04)}" fill="#5A3A22" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="-10" y="{f(ty + h * 0.04)}" width="{f(w + 20)}" height="{f(h)}" fill="#1A0A10"></rect>')
    k = min(1.6, h / 140)
    cx = w * 0.18
    o.append(glow(cx, ty - 30 * k, 60 * k, "#B5121B", 0.4))
    o.append(f'<path d="M{f(cx - 26 * k)} {f(ty - 56 * k)} L {f(cx + 26 * k)} {f(ty - 56 * k)} C {f(cx + 24 * k)} {f(ty - 30 * k)} {f(cx + 10 * k)} {f(ty - 26 * k)} {f(cx)} {f(ty - 26 * k)} C {f(cx - 10 * k)} {f(ty - 26 * k)} {f(cx - 24 * k)} {f(ty - 30 * k)} {f(cx - 26 * k)} {f(ty - 56 * k)} Z" fill="#C8C8D0" stroke="{INK}" stroke-width="2"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(ty - 55 * k)}" rx="{f(24 * k)}" ry="{f(4 * k)}" fill="#8A0E16"></ellipse><path d="M{f(cx)} {f(ty - 26 * k)} L {f(cx)} {f(ty - 4 * k)} M{f(cx - 12 * k)} {f(ty - 2 * k)} L {f(cx + 12 * k)} {f(ty - 2 * k)}" stroke="#C8C8D0" stroke-width="{f(4 * k)}"></path>')
    jx = w * 0.38
    o.append(f'<path d="M{f(jx - 22 * k)} {f(ty)} C {f(jx - 40 * k)} {f(ty - 20 * k)} {f(jx - 36 * k)} {f(ty - 60 * k)} {f(jx - 12 * k)} {f(ty - 70 * k)} L {f(jx - 12 * k)} {f(ty - 84 * k)} L {f(jx + 12 * k)} {f(ty - 84 * k)} L {f(jx + 12 * k)} {f(ty - 70 * k)} C {f(jx + 36 * k)} {f(ty - 60 * k)} {f(jx + 40 * k)} {f(ty - 20 * k)} {f(jx + 22 * k)} {f(ty)} Z" fill="#8A3A2A" stroke="{INK}" stroke-width="2"></path>')
    P = [(jx + 30 * k, ty - 2), (jx + 60 * k, ty - 10 * k), (jx + 80 * k, ty - 2), (jx + 96 * k, ty - 20 * k), (jx + 92 * k, ty - 40 * k)]
    o.append(snake.snake(P, 7 * k, p + "sn", 0.7 * k))
    return "".join(o)

def sluggard_field(p, w, h, seed):
    """I went by the field of the sluggard: the vineyard grown over with thorns and nettles, its stone wall broken down, the
    man that passed by standing to consider it."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#E8D8C0"), hills(w, h, h * 0.3, seed, "#9A8A6A", amp=8, step=80), ground(w, h, h * 0.36, "#9A8A6A", dy=0)]
    r = random.Random(seed)
    for i in range(40):
        x = r.uniform(w * 0.3, w + 10); y = r.uniform(h * 0.42, b + 6); hh = r.uniform(h * 0.06, h * 0.16)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x - 8)} {f(y - hh * 0.5)} {f(x + 10)} {f(y - hh * 0.7)} {f(x + 2)} {f(y - hh)} M{f(x)} {f(y - hh * 0.4)} L {f(x + 12)} {f(y - hh * 0.55)} M{f(x + 2)} {f(y - hh * 0.6)} L {f(x - 10)} {f(y - hh * 0.75)}" fill="none" stroke="#4A3A22" stroke-width="2.4"></path>')
    for i in range(5):
        x = w * (0.36 + i * 0.13)
        o.append(f'<path d="M{f(x)} {f(h * 0.74)} L {f(x + 4)} {f(h * 0.6)} L {f(x - 8)} {f(h * 0.56)}" stroke="#5A3A22" stroke-width="4" fill="none"></path>')
    bw = 22
    for i, (x, y) in enumerate([(0.3, 0.7), (0.34, 0.7), (0.32, 0.66), (0.5, 0.72), (0.66, 0.68), (0.7, 0.68), (0.68, 0.64), (0.86, 0.7)]):
        o.append(f'<rect x="{f(w * x)}" y="{f(h * y)}" width="{bw}" height="12" transform="rotate({(i % 3 - 1) * 12} {f(w * x)} {f(h * y)})" fill="#A89E92" stroke="{INK}" stroke-width="1.4"></rect>')
    s = min(fit(b, h * 0.36), 1.0)
    o.append(son_fig(p, w * 0.14, b, s, flip=True, up=[(-22, -158), (-40, -136), (-60, -140)]))
    return "".join(o)

def scribes(p, w, h, seed):
    """These also are proverbs of Solomon, which the men of Hezekiah king of Judah copied out: scribes seated cross-legged
    with scrolls on their knees, an old scroll open on a stand before them, lamps lit, shelves of scrolls behind."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A2A18"></rect>',
         "".join(f'<rect x="{f(x)}" y="-10" width="{f(w / 14 - 4)}" height="{f(h + 20)}" fill="#5A341E"></rect>' for x in [i * w / 14 for i in range(15)]),
         shelf(w * 0.04, h * 0.3, w * 0.4, 9, seed), shelf(w * 0.56, h * 0.3, w * 0.4, 9, seed + 1), ground(w, h, b, "#2A1A10", dy=0)]
    s = min(fit(b, h * 0.42), 1.0)
    o.append(glow(w * 0.5, b - 60 * s, 160 * s, "#FFC14D", 0.3))
    o.append(f'<path d="M{f(w * 0.5)} {f(b)} L {f(w * 0.5)} {f(b - 70 * s)}" stroke="#5A3A22" stroke-width="{f(8 * s)}"></path>'
             f'<rect x="{f(w * 0.5 - 50 * s)}" y="{f(b - 92 * s)}" width="{f(100 * s)}" height="{f(24 * s)}" fill="#E8D8A8" stroke="{INK}" stroke-width="1.6" transform="rotate(-8 {f(w * 0.5)} {f(b - 80 * s)})"></rect>')
    for x, c, fl in ((0.2, "#5A4A6A", False), (0.32, "#3A5A4A", False), (0.68, "#6A4A3A", True), (0.8, "#4A4A6A", True)):
        o.append(E.kneel(w * x, b, s * 0.9, color=c, flip=fl))
        o.append(f'<rect x="{f(w * x + (-1 if fl else 1) * 18 * s - 16 * s)}" y="{f(b - 52 * s)}" width="{f(32 * s)}" height="{f(10 * s)}" fill="#F3E8C8" stroke="{INK}" stroke-width="1.2"></rect>')
    o.append(EM.lamp_shape(w * 0.1, b - 4, 0.4 * s) + EM.lamp_shape(w * 0.92, b - 4, 0.4 * s))
    return "".join(o)

def flocks(p, w, h, seed):
    """Be thou diligent to know the state of thy flocks: the hay carried, the tender grass, the herbs of the mountains; the
    lambs and the goats, a shepherd with them, and a woman of his household with a pitcher of milk."""
    from lev.art import goat
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#E8F6FA"), hills(w, h, h * 0.3, seed, "#6A9A4A", amp=14, step=70), ground(w, h, h * 0.4, "#9CCB5E", dy=0)]
    for i in range(3):
        x = w * (0.62 + i * 0.12)
        o.append(f'<path d="M{f(x - 30)} {f(h * 0.48)} C {f(x - 24)} {f(h * 0.34)} {f(x + 24)} {f(h * 0.34)} {f(x + 30)} {f(h * 0.48)} Z" fill="#C8B070" stroke="{INK}" stroke-width="2"></path>')
    k = min(1.6, h / 200)
    for x, y in ((0.2, 0.74), (0.32, 0.8), (0.46, 0.76), (0.4, 0.9), (0.58, 0.86)):
        o.append(E.sheep(w * x, h * y, k * 0.7))
    for x, y in ((0.7, 0.82), (0.82, 0.9)):
        o.append(goat(w * x, h * y, k * 0.7))
    s = min(fit(b, h * 0.4), 0.9)
    o.append(man(p, w * 0.12, b, s, "#8A6A4A") + f'<path d="M{f(w * 0.12 + 26 * s)} {f(b - 200 * s)} L {f(w * 0.12 + 30 * s)} {f(b)}" stroke="#5A3A22" stroke-width="{f(5 * s)}"></path>')
    o.append(woman(p, w * 0.9, b, s * 0.92, "#C2456A", flip=True))
    return "".join(o)

def bold_lion(p, w, h, seed):
    """The wicked flee when no man pursueth; but the righteous are bold as a lion: a lion standing on the rock against the
    sunset, a man in white standing firm below; far off, a figure fleeing over the hill."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8A3A2A", "#FFC14D"), sun(w * 0.7, h * 0.46, min(50, h * 0.1), color="#FFE680", op=0.4),
         hills(w, h, h * 0.62, seed, "#5A3A3A", amp=10, step=80), ground(w, h, h * 0.7, "#8A6A4A", dy=0),
         EM.E4rock(w * 0.66, h * 0.72, w * 0.5, h * 0.24)]
    o.append(J2.lion(w * 0.62, h * 0.52, min(1.6, h / 280), roar=True))
    s = min(fit(b, h * 0.4), 0.85)
    o.append(man(p, w * 0.2, b, s, "#F3EFE6"))
    o.append(runner_fig(w * 0.92, h * 0.64, s * 0.3, cloth="#3A2A3A", skin="#2A1A1A", hood=False))
    return "".join(o)

def casting_lot(p, w, h, seed):
    """The lot is cast into the lap: men kneeling about a red cloth on the ground, white and black stones fallen on it, light
    from above (the whole disposing thereof is of Jehovah; God is never drawn)."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#12113A", "#3A2A5A"), EM.rays(w * 0.5, -h * 0.1, 13, 30, max(w, h), "#FFE680", 0.3, 5, 40, 140),
         ground(w, h, h * 0.7, "#3A2A3A", dy=0)]
    k = min(1.8, h / 160)
    cx, cy = w * 0.5, b - 20 * k
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(130 * k)}" ry="{f(30 * k)}" fill="#B5402A" stroke="{INK}" stroke-width="2.4"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(110 * k)}" ry="{f(22 * k)}" fill="none" stroke="#E8B830" stroke-width="2"></ellipse>')
    r = random.Random(seed)
    for i in range(7):
        o.append(f'<ellipse cx="{f(cx + r.uniform(-80, 80) * k)}" cy="{f(cy + r.uniform(-12, 12) * k)}" rx="{f(9 * k)}" ry="{f(6 * k)}" fill="{"#F3EFE6" if i % 2 else "#2A2420"}" stroke="{INK}" stroke-width="1.6"></ellipse>')
    o.append(glow(cx, cy, 120 * k, "#FFE680", 0.25))
    s = min(fit(b, h * 0.42), 1.0)
    for x, c, fl in ((0.16, "#5A4A3A", False), (0.28, "#3A4A6A", False), (0.72, "#6A3A3A", True), (0.84, "#4A5A3A", True)):
        o.append(E.kneel(w * x, b, s * 0.9, color=c, flip=fl))
    return "".join(o)
