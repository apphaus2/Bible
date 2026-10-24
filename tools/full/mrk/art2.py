"""Drawings for Mark 3–4: the multitude coming from every country (a plan of the land), the twelve on the mountain in
Mark's order, the four grounds close up, and the seed growing secretly from night to day. Built on mrk.art (which carries
all of Matthew's drawings)."""
from mrk.art import *
from mrk.art import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette
import random, math

def whence(w, h, seed=1):
    """A great multitude from Galilee, Judæa, Jerusalem, Idumæa, beyond the Jordan, Tyre and Sidon: a plan of the land on the
    blueprint grid, the sea of Galilee and the Jordan running down to the Salt Sea, and from each country a dashed road
    coming in to the sea's shore."""
    o = [grid_bg(w, h)]
    sx, sy_ = w * 0.56, h * 0.3
    o.append(f'<path d="M{f(sx - 22)} {f(sy_ - 30)} C {f(sx - 40)} {f(sy_)} {f(sx - 30)} {f(sy_ + 40)} {f(sx)} {f(sy_ + 44)} C {f(sx + 26)} {f(sy_ + 30)} {f(sx + 24)} {f(sy_ - 20)} {f(sx + 6)} {f(sy_ - 34)} Z" '
             f'fill="#1F6F9A" stroke="#8FD0E2" stroke-width="2"></path>')
    dx, dy = w * 0.58, h * 0.8
    o.append(f'<path d="M{f(sx)} {f(sy_ + 44)} C {f(sx + 10)} {f(h * 0.5)} {f(sx - 8)} {f(h * 0.62)} {f(dx)} {f(dy - 34)}" stroke="#8FD0E2" stroke-width="2.4" fill="none"></path>'
             f'<path d="M{f(dx - 12)} {f(dy - 36)} C {f(dx - 18)} {f(dy)} {f(dx - 8)} {f(dy + 34)} {f(dx + 2)} {f(dy + 40)} C {f(dx + 14)} {f(dy + 20)} {f(dx + 14)} {f(dy - 20)} {f(dx + 8)} {f(dy - 36)} Z" fill="#1F6F9A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(label(sx + 34, sy_ + 6, "SEA OF GALILEE", "#8FD0E2", 9, anchor="start") + label(dx + 20, dy + 6, "SALT SEA", "#8FD0E2", 9, anchor="start")
             + label(sx + 18, h * 0.55, "JORDAN", "#8FD0E2", 8, anchor="start"))
    places = [("SIDON", 0.3, 0.08, "#F3EFE6"), ("TYRE", 0.22, 0.2, "#F3EFE6"), ("GALILEE", 0.34, 0.36, "#FFD23F"), ("BEYOND THE JORDAN", 0.84, 0.52, "#F3EFE6"),
              ("JERUSALEM", 0.4, 0.7, "#FFD23F"), ("JUDÆA", 0.24, 0.8, "#F3EFE6"), ("IDUMÆA", 0.34, 0.95, "#F3EFE6")]
    for nm, x, y, c in places:
        px, py = w * x, h * y
        tx, ty = sx + (px - sx) * 0.16, sy_ + 10 + (py - sy_) * 0.16
        o.append(route([(px, py), (tx, ty)], color="#E8B830", sw=1.8, dash="5 5", arrow=True))
        o.append(node(px, py, nm, c, r=5, dy=-11, size=9.5))
    return "".join(o)

def twelve_mark(p, w, h, seed):
    """He appointed twelve: the twelve standing in a row on the mountain-side, each in his colour, his name beneath, in
    Mark's order — Simon Peter, James and John the sons of thunder, Andrew … Judas Iscariot."""
    b = h * 0.72
    order = [("SIMON PETER", ROBES["peter"]), ("JAMES", ROBES["james"]), ("JOHN", ROBES["john"]), ("ANDREW", ROBES["andrew"]), ("PHILIP", "#4A6A4A"),
             ("BARTHOLOMEW", "#7A5A2A"), ("MATTHEW", ROBES["matthew"]), ("THOMAS", ROBES["thomas"]), ("JAMES", "#5A5A7A"), ("THADDÆUS", "#6A3A3A"),
             ("SIMON", "#3A5A5A"), ("JUDAS ISCARIOT", ROBES["judas"])]
    o = [mk.defs(p, *ALL), grid_bg(w, h)]
    s = min(fit(b, max(h * 0.12, b - 230)) * 0.9, w * 0.84 / 12 / 80)
    for i, (nm, c) in enumerate(order):
        x = w * (0.07 + 0.84 * i / 11)
        o.append(mk.person(p, round(x), round(b), round(s, 3), body="#B98A6E", cloth=c, kind="Robe", sw=3))
        o.append(f'<path d="M{f(x)} {f(b + 4)} L {f(x)} {f(b + 10 + (i % 2) * 14)}" stroke="#4A7A9A" stroke-width="1.4"></path>')
        o.append(label(x, b + 20 + (i % 2) * 14, nm, "#FFD23F" if i < 3 else "#8FD0E2", 8.5))
    o.append(label(w * 0.03, b + 58, "JAMES AND JOHN · BOANERGES", "#FFD23F", 8.5, anchor="start"))
    return "".join(o)

def ground_close(p, w, h, seed, kind):
    """One of the four grounds close up: 'way' the beaten path, the seed lying on it and the birds at it; 'rocky' grey
    rocks, thin earth, the shoots scorched under a hard sun; 'thorns' the thorns grown up over the young grain; 'good' the
    grain standing tall and full in the ear."""
    r = random.Random(seed)
    if kind == "rocky":
        o = [sky(w, h, "#FFD89A", "#FFF4C2"), sun(w * 0.8, h * 0.18, max(14, h * 0.08), color="#FFC14D", op=0.5), ground(w, h, h * 0.5, "#B8946A", dy=0)]
        for _ in range(9):
            x = r.uniform(0, w); y = r.uniform(h * 0.6, h * 0.98); rr = r.uniform(0.05, 0.1) * h
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rr * 1.6)}" ry="{f(rr)}" fill="#9A9488" stroke="{INK}" stroke-width="1.8"></ellipse>')
        for _ in range(16):
            x = r.uniform(0, w); y = r.uniform(h * 0.58, h * 0.98)
            o.append(f'<path d="M{f(x)} {f(y)} C {f(x)} {f(y - h * 0.1)} {f(x + 6)} {f(y - h * 0.13)} {f(x + h * 0.06)} {f(y - h * 0.08)}" stroke="#A8903A" stroke-width="2.4" fill="none"></path>')
        return "".join(o)
    if kind == "thorns":
        o = [sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.46, "#6A5A3A", dy=0), grain(-10, w + 10, h * 0.98, h * 0.26, seed, color="#9AAA5A")]
        for _ in range(16):
            x = r.uniform(0, w); y = r.uniform(h * 0.6, h * 1.0); k = h / 200
            o.append(f'<path d="M{f(x)} {f(y)} l {f(-16 * k)} {f(-40 * k)} M{f(x)} {f(y)} l {f(3 * k)} {f(-52 * k)} M{f(x)} {f(y)} l {f(18 * k)} {f(-38 * k)}" stroke="#2A3A1E" stroke-width="3"></path>'
                     f'<path d="M{f(x - 8 * k)} {f(y - 22 * k)} l -6 -3 M{f(x + 8 * k)} {f(y - 20 * k)} l 6 -4 M{f(x + 2 * k)} {f(y - 36 * k)} l 5 -3" stroke="#2A3A1E" stroke-width="2"></path>')
        return "".join(o)
    if kind == "good":
        o = [sky(w, h, "#8FD0E2", "#FFF4C2"), sun(w * 0.86, h * 0.16, 14, color="#FFE680", op=0.3), hills(w, h, h * 0.4, seed, color="#9AAA7A", amp=10, step=80),
             ground(w, h, h * 0.5, "#8A6A4A", dy=0), grain(-10, w + 10, h * 0.72, h * 0.22, seed), grain(-10, w + 10, h * 1.0, h * 0.34, seed + 1)]
        for i, t in enumerate(("THIRTYFOLD", "SIXTYFOLD", "A HUNDREDFOLD")):
            o.append(label(w * (0.2 + 0.3 * i), h * 0.3, t, "#0D0D0F", 10))
        return "".join(o)
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.44, "#9AAA6A", dy=0),
         f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.56)} {f(w * 0.6)} {f(h * 0.66)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8A878" stroke="{INK}" stroke-width="2"></path>']
    for _ in range(26):
        o.append(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.66, h * 0.98))}" r="2.4" fill="#F3E8C0" stroke="#8A6A3A" stroke-width="0.8"></circle>')
    o.append("".join(bird(r.uniform(w * 0.1, w * 0.9), r.uniform(h * 0.7, h * 0.94), max(1.2, h / 120), "#2A1A10") for _ in range(5)))
    o.append(birds(3, w * 0.5, w * 0.9, h * 0.1, h * 0.3, seed))
    return "".join(o)

def seed_secretly(p, w, h, seed):
    """So is the kingdom of God, as if a man should cast seed upon the earth, and should sleep and rise night and day: one
    strip of field from night (the moon) to day (the sun), the grain growing along it — first the blade, then the ear, then
    the full grain in the ear — and at the end the sickle laid ready, for the harvest is come."""
    o = [f'<defs><linearGradient id="{p}nd" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0B0B2A"></stop><stop offset="0.5" stop-color="#5A4A8A"></stop>'
         f'<stop offset="1" stop-color="#FFE6A0"></stop></linearGradient></defs><rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{p}nd)"></rect>',
         mk.stars(14, w * 0.3, h * 0.4, seed), moon(w * 0.08, h * 0.16, max(8, h * 0.05)), sun(w * 0.92, h * 0.16, max(10, h * 0.05), color="#FFE680", op=0.4),
         ground(w, h, h * 0.72, "#6A4A30", dy=0)]
    k = h / 260
    stages = [(0.14, "THE SEED", 0), (0.36, "THE BLADE", 1), (0.58, "THE EAR", 2), (0.8, "THE FULL GRAIN", 3)]
    for x, t, st in stages:
        cx = w * x; base = h * 0.84
        if st == 0:
            o.append("".join(f'<circle cx="{f(cx + dx * k)}" cy="{f(base - 4)}" r="{f(3 * k)}" fill="#E8D8A0" stroke="{INK}" stroke-width="1"></circle>' for dx in (-14, -2, 10)))
        else:
            ht = [0, 40, 80, 110][st] * k
            for dx in (-14, 0, 14):
                o.append(f'<path d="M{f(cx + dx * k)} {f(base)} C {f(cx + dx * k - 4)} {f(base - ht * 0.5)} {f(cx + dx * k + 4)} {f(base - ht * 0.8)} {f(cx + dx * k)} {f(base - ht)}" stroke="#5A8A3A" stroke-width="{f(2.6 * k)}" fill="none"></path>'
                         f'<path d="M{f(cx + dx * k)} {f(base - ht * 0.4)} q {f(-14 * k)} {f(-8 * k)} {f(-18 * k)} {f(-22 * k)}" stroke="#6A9A3A" stroke-width="{f(2 * k)}" fill="none"></path>')
                if st >= 2:
                    col = "#9AAA5A" if st == 2 else "#E8C060"
                    o.append(f'<ellipse cx="{f(cx + dx * k)}" cy="{f(base - ht - 10 * k)}" rx="{f(4 * k)}" ry="{f((8 if st == 2 else 14) * k)}" fill="{col}" stroke="#7A5A1A" stroke-width="1.2"></ellipse>')
        o.append(label(cx, h * 0.95, t, "#F3EFE6", 9))
    sk = w * 0.94
    o.append(f'<path d="M{f(sk)} {f(h * 0.86)} L {f(sk)} {f(h * 0.7)}" stroke="#6A4A2A" stroke-width="{f(4 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(sk)} {f(h * 0.7)} C {f(sk - 30 * k)} {f(h * 0.66)} {f(sk - 40 * k)} {f(h * 0.56)} {f(sk - 20 * k)} {f(h * 0.5)} C {f(sk - 28 * k)} {f(h * 0.58)} {f(sk - 18 * k)} {f(h * 0.66)} {f(sk)} {f(h * 0.68)} Z" fill="#B8B8C0" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)
