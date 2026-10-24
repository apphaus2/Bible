"""Drawings for John 15–17. The true vine: an old vine on its stone terrace at first light, its branches spread heavy with
clusters (the husbandman is the Father, and is never drawn: the vine only); the withered branches cast on a fire by the
vineyard wall; Jesus and the eleven walking by night along the road past the vineyards under the moon; the synagogue door
shut; the mother at dawn with her new-born child in her arms, her sorrow turned into joy (nothing of the travail drawn);
the eleven scattered along the dark roads every man to his own, Jesus standing alone, a light upon him; I have overcome
the world. The prayer: Jesus on the hillside at night, his eyes and hands lifted up to heaven, the eleven sitting about him,
the city and the temple across the dark valley; that they may be one — the eleven drawn close together in the light about
him. Built on jhn.art7."""
from jhn.art7 import *
from jhn.art7 import f, INK, HEB, TWELVE, P, _loaf
import random, math
import ruth1 as R1

def vine_plant(x, b, s, seed, fruit=True, wither=False):
    """An old vine: a thick twisted stock and branches trained along a low wall, leaves and purple clusters."""
    r = random.Random(seed)
    o = [f'<path d="M{f(x)} {f(b)} C {f(x - 10 * s)} {f(b - 60 * s)} {f(x + 14 * s)} {f(b - 100 * s)} {f(x)} {f(b - 150 * s)}" stroke="#4A2A18" stroke-width="{f(16 * s)}" fill="none" stroke-linecap="round"></path>']
    for k, (dx, dy) in enumerate(((-1, -0.1), (1, -0.2), (-1, -0.5), (1, -0.6), (-0.6, -0.9), (0.7, -1.0))):
        ex, ey = x + dx * 200 * s, b - 150 * s + dy * 60 * s
        o.append(f'<path d="M{f(x)} {f(b - 140 * s + k * 4 * s)} C {f(x + dx * 60 * s)} {f(b - 170 * s)} {f(x + dx * 140 * s)} {f(ey - 20 * s)} {f(ex)} {f(ey)}" stroke="#5A3A22" stroke-width="{f(6 * s)}" fill="none" stroke-linecap="round"></path>')
        for t in (0.22, 0.36, 0.5, 0.64, 0.78, 0.92):
            lx = x + dx * 200 * s * t; ly = b - 150 * s + (ey - (b - 150 * s)) * t - 20 * s * math.sin(math.pi * t)
            col = "#8A7A3A" if wither else r.choice(["#3F7A34", "#5E8F26", "#4A6A2A"])
            lk = s * r.uniform(1.1, 1.5); lr = r.choice((1, -1))
            o.append(f'<path d="M{f(lx)} {f(ly)} c {f(-16 * lk * lr)} {f(-4 * lk)} {f(-20 * lk * lr)} {f(-22 * lk)} {f(-4 * lk * lr)} {f(-28 * lk)} c {f(6 * lk * lr)} {f(10 * lk)} {f(18 * lk * lr)} {f(8 * lk)} {f(20 * lk * lr)} {f(22 * lk)} c {f(-4 * lk * lr)} {f(6 * lk)} {f(-10 * lk * lr)} {f(8 * lk)} {f(-16 * lk * lr)} {f(6 * lk)} Z" fill="{col}" stroke="{INK}" stroke-width="1.4"></path>')
            if fruit and not wither and r.random() < 0.5:
                for g in range(6):
                    o.append(f'<circle cx="{f(lx + (g % 3 - 1) * 5 * s)}" cy="{f(ly + 10 * s + (g // 3) * 7 * s + (g % 2) * 2 * s)}" r="{f(4 * s)}" fill="#5A1A5A" stroke="{INK}" stroke-width="0.8"></circle>')
    return "".join(o)

def true_vine(p, w, h, seed, stage="vine"):
    """vine: the true vine on its terrace at first light, branches spread and heavy with clusters, a pruned branch or two
    lying on the stones beneath (the husbandman is never drawn). fire: the withered branches gathered and burning on a fire
    by the vineyard wall at dusk — no one drawn."""
    b = h * 0.9
    if stage == "fire":
        o = [sky(w, h, "#2A1A2A", "#C8603A"), hills(w, h, h * 0.5, seed, color="#3A2A2A", amp=12, step=80), ground(w, h, h * 0.62, "#4A3A2A", dy=0),
             f'<path d="M-10 {f(h * 0.7)} L {f(w + 10)} {f(h * 0.66)}" stroke="#6A5A4A" stroke-width="{f(h * 0.06)}"></path>']
        o.append(E.blaze(w * 0.5, b, w * 0.3, h * 0.4, seed, n=7))
        r = random.Random(seed)
        for _ in range(8):
            x = w * r.uniform(0.3, 0.7); y = b - r.uniform(0, h * 0.06)
            o.append(f'<path d="M{f(x - 30)} {f(y)} L {f(x + 30)} {f(y - 10)} M{f(x)} {f(y - 4)} l 10 -14" stroke="#3A2214" stroke-width="3"></path>')
        o.append(vine_plant(w * 0.12, b, max(0.4, h / 600), seed, wither=True))
        return "".join(o)
    o = [sky(w, h, "#5A6A9A", "#FFE6A0"), sun(w * 0.86, h * 0.3, max(12, h * 0.04), color="#FFF4C2", op=0.4), hills(w, h, h * 0.5, seed, color="#7A8A5A", amp=12, step=90),
         ground(w, h, h * 0.62, "#8A7A4A", dy=0),
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#A89A8A" stroke="{INK}" stroke-width="2"></rect>']
    k = min(1.6, max(0.6, (b - h * 0.1) / 260))
    o.append(vine_plant(w * 0.5, b, k, seed))
    o.append(f'<path d="M{f(w * 0.2)} {f(b + 10)} l 50 -6 M{f(w * 0.24)} {f(b + 16)} l 40 2" stroke="#6A5A3A" stroke-width="3"></path>')
    return "".join(o)

def night_walk(p, w, h, seed):
    """Arise, let us go hence: the road out of the city by night under the full moon, past the walled vineyards, Jesus and
    the eleven walking together toward the brook Kidron."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1E1650"), mk.stars(50, w, h * 0.4, seed), moon(w * 0.82, h * 0.14, max(10, h * 0.04)),
         walls(w * 0.0, w * 0.4, h * 0.5, h * 0.24, seed, lit=True, towers=2), hills(w, h, h * 0.56, seed, color="#1E1E3A", amp=10, step=80),
         ground(w, h, h * 0.6, "#2A2A44", dy=0), vines(w * 0.5, w * 0.98, h * 0.66, h * 0.72, seed, rows=2)]
    s = fit(b, max(h * 0.3, b - 220))
    o.append(jesus(p, w * 0.62, b, s, flip=True))
    for i, who in enumerate(("peter", "john", "james", "andrew", "thomas")):
        o.append(disciple(p, w * (0.5 - 0.1 * i), b - 4 * (i % 2), s * (0.96 - 0.02 * i), who, flip=True))
    return "".join(o)

def newborn(p, w, h, seed):
    """When she is delivered of the child, she remembereth no more the anguish: a mother at dawn sitting in her doorway
    with her new-born child in swaddling bands in her arms, the morning light on them (nothing of the travail drawn)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#C8A878", floor="#8A6A4A"),
         f'<rect x="{f(w * 0.56)}" y="{f(h * 0.16)}" width="{f(w * 0.3)}" height="{f(b - h * 0.16)}" fill="#FFE6A0" stroke="{INK}" stroke-width="2"></rect>',
         glow(w * 0.6, h * 0.5, h * 0.6, "#FFF4C2", 0.8, f"{p}g")]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(seated(w * 0.48, b, s * 1.0, "#6A4A6A", head="#3A2A4A", beard=None, flip=False))
    o.append(R1.baby(w * 0.48 + 20 * s, b - 66 * s, s * 0.8))
    o.append(man(p, w * 0.8, b, s * 0.96, "#5A6A4A", flip=True, up=UP_HIGH))
    return "".join(o)

def scattered(p, w, h, seed):
    """Ye shall be scattered, every man to his own, and shall leave me alone: the dark hillside at night, the roads going
    away every way, small figures fleeing down them, and Jesus standing alone in the midst with a soft light upon him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1E1650"), mk.stars(40, w, h * 0.3, seed), hills(w, h, h * 0.4, seed, color="#1E1E3A", amp=12, step=80),
         ground(w, h, h * 0.46, "#2A2A44", dy=0)]
    for ex, ey in ((0.04, 0.5), (0.3, 0.46), (0.7, 0.46), (0.96, 0.5)):
        o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.9)} C {f(w * 0.5)} {f(h * 0.7)} {f(w * ex)} {f(h * 0.6)} {f(w * ex)} {f(h * ey)}" stroke="#4A4A66" stroke-width="{f(max(5, h * 0.03))}" fill="none"></path>')
    for i, (x, y) in enumerate(((0.12, 0.56), (0.32, 0.54), (0.68, 0.54), (0.88, 0.56), (0.22, 0.64), (0.78, 0.64))):
        yy = h * y
        o.append(disciple(p, w * x, yy, fit(yy, yy - h * 0.12), TWELVE[i], flip=x < 0.5))
    s = fit(b, max(h * 0.3, b - 220))
    o.append(glow(w * 0.5, b - 110 * s, 150 * s, "#FFF4C2", 0.6, f"{p}g") + jesus(p, w * 0.5, b, s))
    return "".join(o)

def prayer(p, w, h, seed, one=False):
    """Jesus lifting up his eyes to heaven: on the hillside at night, the city and the temple lit across the dark valley,
    Jesus standing with his hands lifted, the eleven sitting on the ground about him; one=True the eleven drawn close
    together in the light about him, that they may be one."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), jerusalem_far(w, h, seed, tone="night", lit=True), mk.stars(50, w, h * 0.3, seed), moon(w * 0.86, h * 0.12, max(8, h * 0.035)),
         f'<path d="M-10 {f(h * 0.78)} C {f(w * 0.3)} {f(h * 0.72)} {f(w * 0.7)} {f(h * 0.74)} {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A2A3A" stroke="{INK}" stroke-width="2"></path>',
         olive(w * 0.06, h * 0.98, h / 360, seed=seed), olive(w * 0.96, h * 0.98, h / 380, seed=seed + 1)]
    s = fit(b, max(h * 0.3, b - 220))
    jx = w * (0.5 if one else 0.3)
    o.append(glow(jx, b - 120 * s, 160 * s, "#FFF4C2", 0.6, f"{p}g"))
    o.append(jesus(p, jx, b, s, up=[(-22, -158), (-34, -190), (-38, -222)]))
    if one:
        for i in range(5):
            o.append(disciple_seated(w * (0.18 + 0.05 * i), b, s * 0.62, i))
            o.append(disciple_seated(w * (0.82 - 0.05 * i), b, s * 0.62, i + 7, flip=True))
    else:
        for i in range(6):
            o.append(disciple_seated(w * (0.46 + 0.08 * i), b - (i % 2) * 6, s * 0.62, i + (1 if i >= 6 else 0), flip=True))
    return "".join(o)
