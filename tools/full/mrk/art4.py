"""Drawings for Mark 6:30–7:37: the companies on the green grass, in ranks by hundreds and by fifties, seen from the hill;
the cups and pots and brasen vessels of the washings; the woman's house, the child lying quiet on her bed; the deaf man
taken aside, Jesus looking up to heaven. Built on mrk.art3."""
from mrk.art3 import *
from mrk.art3 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, gerasene_fig
import random, math

def companies(p, w, h, seed):
    """He commanded them that all should sit down by companies upon the green grass, in ranks, by hundreds and by fifties:
    the wide green slope above the lake seen from the hill, the people seated in squared companies like garden beds, Jesus
    and the twelve standing small at the head."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), sky(w, h, "#5A7AB0", "#FFD8A0"), hills(w, h, h * 0.22, seed, color="#6A7A8A", amp=10, step=90), lake(w, h, h * 0.26, seed, n=6, op=0.5),
         f'<path d="M-10 {f(h * 0.36)} C {f(w * 0.3)} {f(h * 0.32)} {f(w * 0.7)} {f(h * 0.34)} {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A9A3A" stroke="{INK}" stroke-width="2"></path>']
    cols = ["#6A4A3A", "#3A4A6A", "#5A6A3A", "#7A3A3A", "#4A3A5A", "#8A6A3A", "#C8B898"]
    rows_ = [(0.42, 5, 0.55), (0.56, 5, 0.75), (0.74, 4, 1.0)]
    for y, n, k in rows_:
        bw = w / n * 0.78
        for i in range(n):
            cx = w * (i + 0.5) / n; yy = h * y
            o.append(f'<rect x="{f(cx - bw / 2)}" y="{f(yy - 6 * k)}" width="{f(bw)}" height="{f(h * 0.12 * k)}" fill="#7AAA4A" opacity="0.6"></rect>')
            m = int(7 * k) + 2
            for jy in range(3):
                for jx in range(m):
                    x = cx - bw / 2 + bw * (jx + 0.5) / m + (bw / m / 2 if jy % 2 else 0) * 0.5; y2 = yy + jy * h * 0.032 * k
                    hr = max(2.2, 5.0 * k * h / 300)
                    o.append(f'<path d="M{f(x - hr * 1.4)} {f(y2 + hr * 2.6)} C {f(x - hr * 1.4)} {f(y2)} {f(x + hr * 1.4)} {f(y2)} {f(x + hr * 1.4)} {f(y2 + hr * 2.6)} Z" fill="{r.choice(cols)}"></path>'
                             f'<circle cx="{f(x)}" cy="{f(y2 - hr * 0.4)}" r="{f(hr)}" fill="#B98A6E"></circle>')
    s = fit(h * 0.4, h * 0.3)
    o.append(jesus(p, w * 0.5, h * 0.38, s, up=UP_HIGH))
    return "".join(o)

def cups_pots(p, w, h, seed):
    """The washings of cups, and pots, and brasen vessels: on a stone ledge by the door, the water-jars of stone, the cups
    and pitchers and brass pots set out in a row, a basin and a towel."""
    b = h * 0.8
    o = [bgr(w, h, "#C8B490"), f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A7A5A" stroke="{INK}" stroke-width="2"></rect>']
    k = h / 240
    x = w * 0.06
    items = ["jar", "cup", "pitcher", "brass", "cup", "jar", "brass", "basin", "pitcher"]
    for it in items:
        if it == "jar":
            o.append(f'<path d="M{f(x)} {f(b)} C {f(x - 24 * k)} {f(b - 30 * k)} {f(x - 26 * k)} {f(b - 80 * k)} {f(x - 12 * k)} {f(b - 96 * k)} L {f(x + 12 * k)} {f(b - 96 * k)} C {f(x + 26 * k)} {f(b - 80 * k)} {f(x + 24 * k)} {f(b - 30 * k)} {f(x)} {f(b)} Z" fill="#D8C8A8" stroke="{INK}" stroke-width="2"></path>'
                     f'<rect x="{f(x - 14 * k)}" y="{f(b - 104 * k)}" width="{f(28 * k)}" height="{f(10 * k)}" fill="#C8B898" stroke="{INK}" stroke-width="1.6"></rect>'); x += 64 * k
        elif it == "cup":
            o.append(cup(x, b, 0.36 * k, color="#C8A070")); x += 40 * k
        elif it == "pitcher":
            o.append(f'<path d="M{f(x - 14 * k)} {f(b)} C {f(x - 22 * k)} {f(b - 30 * k)} {f(x - 16 * k)} {f(b - 50 * k)} {f(x - 8 * k)} {f(b - 60 * k)} L {f(x + 10 * k)} {f(b - 60 * k)} L {f(x + 18 * k)} {f(b - 66 * k)} '
                     f'L {f(x + 14 * k)} {f(b - 54 * k)} C {f(x + 22 * k)} {f(b - 40 * k)} {f(x + 20 * k)} {f(b - 16 * k)} {f(x + 14 * k)} {f(b)} Z" fill="#B5652E" stroke="{INK}" stroke-width="2"></path>'); x += 50 * k
        elif it == "brass":
            o.append(f'<path d="M{f(x - 26 * k)} {f(b - 40 * k)} L {f(x + 26 * k)} {f(b - 40 * k)} C {f(x + 28 * k)} {f(b - 10 * k)} {f(x + 16 * k)} {f(b)} {f(x)} {f(b)} C {f(x - 16 * k)} {f(b)} {f(x - 28 * k)} {f(b - 10 * k)} {f(x - 26 * k)} {f(b - 40 * k)} Z" fill="#E8B830" stroke="{INK}" stroke-width="2"></path>'
                     f'<ellipse cx="{f(x)}" cy="{f(b - 40 * k)}" rx="{f(26 * k)}" ry="{f(5 * k)}" fill="#C8963E" stroke="{INK}" stroke-width="1.6"></ellipse>'); x += 64 * k
        else:
            o.append(f'<path d="M{f(x - 34 * k)} {f(b - 20 * k)} L {f(x + 34 * k)} {f(b - 20 * k)} C {f(x + 28 * k)} {f(b)} {f(x - 28 * k)} {f(b)} {f(x - 34 * k)} {f(b - 20 * k)} Z" fill="#B8B0A0" stroke="{INK}" stroke-width="2"></path>'
                     f'<path d="M{f(x + 30 * k)} {f(b - 20 * k)} l {f(8 * k)} {f(20 * k)} l {f(14 * k)} 0 l {f(-8 * k)} {f(-22 * k)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="1.4"></path>'); x += 84 * k
        if x > w * 0.96: break
    return "".join(o)

def child_bed(p, w, h, seed):
    """She went away unto her house, and found the child laid upon the bed: a small room at Tyre in the evening, the
    little girl lying quiet on her bed, her mother in her orange headcloth come in at the door."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, *LIE), room(w, h, b, wall="#C8A08A", window=(w * 0.72, w * 0.08)), glow(w * 0.42, b - h * 0.2, h * 0.4, "#FFF4C2", 0.5, f"{p}g")]
    s = fit(b, max(h * 0.2, b - 240))
    o.append(f'<rect x="{f(w * 0.24)}" y="{f(b - 30 * s)}" width="{f(w * 0.36)}" height="{f(30 * s)}" fill="#8A5A30" stroke="{INK}" stroke-width="2"></rect>')
    o.append(on_bed(p, w * 0.42, b - 36 * s, w * 0.3, cloth="#F3EFE6"))
    o.append(woman_fig(p, w * 0.82, b, s, "#9A4A2A", "#E8903A", flip=True, up=UP_BLESS))
    return "".join(o)

def ephphatha(p, w, h, seed):
    """He took him aside from the multitude privately; and looking up to heaven, he sighed, and saith unto him, Ephphatha:
    apart from the crowd under an olive tree, Jesus with his face lifted, his hand at the deaf man's ear; the multitude far
    off along the shore."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.36, seed, color="#9AAA7A", amp=12, step=90), lake(w, h, h * 0.42, seed, n=6),
         ground(w, h, h * 0.56, "#C8B07A", dy=0), olive(w * 0.86, b, max(0.6, h / 300), seed=seed)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(crowd(p, w * 0.02, w * 0.3, h * 0.62, h * 0.62 - 150 * s * 0.5, 6, seed))
    o.append(jesus(p, w * 0.5, b, s, flip=True, up=[(-22, -158), (-36, -170), (-50, -178)]))
    hood = A.headcloth("#C8B080", cord="#5A3A22") + A.BLACK_BEARD
    o.append(man(p, w * 0.64, b, s * 0.96, "#7A6A4A", kind="Robe", extra=hood))
    return "".join(o)

def house_tyre(p, w, h, seed):
    """He entered into a house at the borders of Tyre and Sidon, and would have no man know it: a white house by the great
    sea at evening, its door shut, a lamp lit in the window."""
    b = h * 0.94
    o = [sky(w, h, "#4A3A6A", "#FFB07A"), lake(w, h, h * 0.5, seed, color="#2A6A9A", deep="#1A3A5A", n=8),
         f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.3)} {f(h * 0.56)} {f(w * 0.6)} {f(h * 0.62)} {f(w + 10)} {f(h * 0.58)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8A878" stroke="{INK}" stroke-width="2"></path>',
         f'<rect x="{f(w * 0.3)}" y="{f(h * 0.36)}" width="{f(w * 0.36)}" height="{f(b - h * 0.36)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.29)}" y="{f(h * 0.33)}" width="{f(w * 0.38)}" height="{f(h * 0.04)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.42)}" y="{f(b - h * 0.28)}" width="{f(w * 0.08)}" height="{f(h * 0.28)}" fill="#5A3A22" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.56)}" y="{f(h * 0.46)}" width="{f(w * 0.05)}" height="{f(h * 0.08)}" fill="#FFC14D" stroke="{INK}" stroke-width="1.6"></rect>']
    return "".join(o)
