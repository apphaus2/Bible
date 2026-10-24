"""Drawings for Mark 14:43–16:20. The garden left dark and empty after the arrest (the young man who fled is told in words
only); the Prætorium court empty with the purple robe laid aside and the reed (the scourging, the crown of thorns and the
mocking in words only); the three women on the garden path at sunrise with their spices; the great stone rolled back
from the door, no one on it; within the tomb, the young man in a white robe sitting on the right side — a figure of white
light with a gold rim and no face — and the empty shelf; the women fleeing from the tomb; then Jesus risen in white light:
the disciples mourning when Mary Magdalene comes in; two walking into the country with him; the eleven at meat; received
up into heaven in a cloud of light above the mount (God never drawn: the light only); and the roads going out
everywhere. Built on mrk.art8 (which carries Matthew's passion drawings: mat.art10, mat.art11)."""
from mrk.art8 import *
from mrk.art8 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, gerasene_fig, jesus_risen, roman_fig, torch
import random, math

PURPLE = "#5A1A6A"
WOMEN3 = [(ROBES["magdalene"], "#C2456A"), ("#6A4A2A", "#5A3A22"), ("#5A6A3A", "#4A5A2A")]   # Mary Magdalene, Mary the mother of James, Salome

def purple_laid(p, w, h, seed):
    """The Prætorium court empty: the purple robe taken off and thrown down on the pavement by a pillar, the reed beside it —
    the scourging, the crown of thorns, the blows and the mocking are told in words only."""
    b = h * 0.92
    o = [bgr(w, h, "#5A4A44")]
    for x in (0.16, 0.84):
        o.append(f'<rect x="{f(w * x - 22)}" y="-10" width="44" height="{f(b + 10)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    o.append(pavement(w, h, b - h * 0.16, color="#8A7A6A", line="#6A5A4A"))
    k = max(0.6, h / 260)
    cx = w * 0.46
    o.append(f'<path d="M{f(cx - 90 * k)} {f(b)} C {f(cx - 70 * k)} {f(b - 40 * k)} {f(cx - 10 * k)} {f(b - 50 * k)} {f(cx + 30 * k)} {f(b - 30 * k)} C {f(cx + 60 * k)} {f(b - 40 * k)} {f(cx + 90 * k)} {f(b - 20 * k)} {f(cx + 96 * k)} {f(b)} Z" fill="{PURPLE}" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(cx - 40 * k)} {f(b - 30 * k)} C {f(cx - 20 * k)} {f(b - 10 * k)} {f(cx + 20 * k)} {f(b - 16 * k)} {f(cx + 50 * k)} {f(b - 6 * k)}" stroke="#2A0A3A" stroke-width="2" fill="none"></path>'
             f'<path d="M{f(cx + 110 * k)} {f(b - 4)} L {f(cx + 240 * k)} {f(b - 30 * k)}" stroke="#A8A05A" stroke-width="{f(4 * k)}"></path>')
    return "".join(o)

def dark_garden(p, w, h, seed):
    """They all left him, and fled — and a certain young man followed: the garden of olives at night, empty, the torches
    going away small between the trees toward the city (what befell the young man is told in words only)."""
    o = [sky(w, h, "#05051A", "#1E1650"), mk.stars(40, w, h * 0.4, seed), moon(w * 0.82, h * 0.14, max(8, h * 0.04)),
         hills(w, h, h * 0.56, seed, color="#14142E", amp=10, step=80), ground(w, h, h * 0.66, "#1A1830", dy=0)]
    for i, x in enumerate((0.08, 0.3, 0.58, 0.92)):
        o.append(f'<g opacity="0.95">{olive(w * x, h * (0.98 - 0.04 * (i % 2)), max(0.5, h / 300) * (1.0 - 0.1 * (i % 2)), seed=seed + i)}</g>')
    for i in range(4):
        x, y = w * (0.4 + 0.05 * i), h * (0.6 - 0.01 * i)
        o.append(glow(x, y, 14, "#FFC14D", 0.9, f"{p}t{i}") + f'<circle cx="{f(x)}" cy="{f(y)}" r="2.6" fill="#FFE680"></circle>')
    return "".join(o)

def spices_dawn(p, w, h, seed):
    """Very early on the first day of the week, when the sun was risen: the garden path to the rock tomb at sunrise, the three
    women walking with their jars of spices — Mary Magdalene, Mary the mother of James, and Salome."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#3A3A7A", "#FFC890"), sun(w * 0.86, h * 0.44, 18, color="#FFE680", op=0.5), hills(w, h, h * 0.5, seed, color="#6A6A7A", amp=12, step=80),
         f'<path d="M{f(w * 0.56)} {f(h + 10)} L {f(w * 0.6)} {f(h * 0.36)} C {f(w * 0.7)} {f(h * 0.3)} {f(w * 0.9)} {f(h * 0.3)} {f(w + 10)} {f(h * 0.34)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>',
         ground(w, h, h * 0.66, "#5A6A3A", dy=0), olive(w * 0.1, b, h / 360, seed=seed)]
    s = fit(b, max(h * 0.3, b - 220))
    jar = '<path d="M-48 -122 C -56 -112 -54 -98 -46 -96 L -34 -96 C -26 -98 -24 -112 -32 -122 Z" fill="#E8D8A8" stroke="#0D0D0F" stroke-width="1.6"></path>'
    for i, (c, veil_) in enumerate(WOMEN3):
        o.append(woman_fig(p, w * (0.22 + 0.11 * i), b - 4 * i, s * (0.92 - 0.02 * i), c, veil_, flip=True, up=[(-22, -158), (-34, -130), (-40, -112)], extra=jar))
    return "".join(o)

def stone_back(p, w, h, seed, women=True, fled=False):
    """They see that the stone is rolled back: for it was exceeding great: the tomb's doorway open and dark, the great round
    stone rolled back beside it, no one on it; women=True the three standing on the path looking up at it; fled=True the
    three running away down the path, the tomb behind them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A9A", "#FFE6A0"),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.34)} {f(h * 0.26)} C {f(w * 0.5)} {f(h * 0.16)} {f(w * 0.8)} {f(h * 0.18)} {f(w + 10)} {f(h * 0.26)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.46)} {f(b - h * 0.04)} L {f(w * 0.46)} {f(h * 0.52)} Q {f(w * 0.54)} {f(h * 0.42)} {f(w * 0.62)} {f(h * 0.52)} L {f(w * 0.62)} {f(b - h * 0.04)} Z" fill="#1A1210" stroke="{INK}" stroke-width="2"></path>',
         ground(w, h, b - h * 0.04, "#6A8A3A", dy=0)]
    cx, cy, r = w * 0.8, b - h * 0.04 - h * 0.19, h * 0.19
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="#A89A8A" stroke="{INK}" stroke-width="2.6"></circle><circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r * 0.7)}" fill="none" stroke="#8A7A6A" stroke-width="2"></circle>')
    s = fit(b, max(h * 0.3, b - 220))
    if women or fled:
        for i, (c, veil_) in enumerate(WOMEN3):
            if fled:
                o.append(woman_fig(p, w * (0.06 + 0.1 * i), b - 2 * i, s * 0.88, c, veil_, up=[(-22, -158), (-40, -176), (-56, -190)]))
            else:
                o.append(woman_fig(p, w * (0.12 + 0.1 * i), b - 2 * i, s * (0.92 - 0.02 * i), c, veil_, flip=True, up=UP_BLESS if i == 0 else None))
    return "".join(o)

def light_seated(x, y, s, flip=False):
    """A figure of white light sitting (the young man at the tomb, 16:5): the sitting shape in white with a gold rim, the
    head a plain circle of light — no face."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            '<path d="M-48 0 C -52 -34 -44 -72 -30 -94 C -22 -104 -2 -104 6 -96 C 14 -84 16 -72 22 -62 L 44 -60 C 54 -56 56 -42 56 -26 L 60 0 Z" fill="#FFFFFF" stroke="#E8B830" stroke-width="3"></path>'
            '<path d="M-8 -90 L 10 -66 L 38 -62" fill="none" stroke="#E8B830" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"></path>'
            '<path d="M-8 -90 L 10 -66 L 38 -62" fill="none" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"></path>'
            '<circle cx="-4" cy="-112" r="16" fill="#FFFDF0" stroke="#E8B830" stroke-width="3"></circle></g>')

def young_man(p, w, h, seed):
    """Entering into the tomb, they saw a young man sitting on the right side, arrayed in a white robe: within the rock tomb
    the empty shelf, and on the right a figure of white light with a gold rim sitting, no face drawn; the morning light in
    the doorway, the three women in it."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bgr(w, h, "#2A2220"),
         f'<path d="M{f(w * 0.04)} {f(h * 0.2)} L {f(w * 0.04)} {f(b)} L {f(w * 0.36)} {f(b)} L {f(w * 0.36)} {f(h * 0.3)} Q {f(w * 0.2)} {f(h * 0.1)} {f(w * 0.04)} {f(h * 0.2)} Z" fill="#FFE6A0" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.36)} {f(b)} L {f(w * 0.04)} {f(b)} L {f(w * 0.5)} {f(h + 10)} L {f(w * 0.9)} {f(h + 10)} Z" fill="#FFE680" opacity="0.25"></path>',
         f'<rect x="{f(w * 0.42)}" y="{f(b - h * 0.2)}" width="{f(w * 0.3)}" height="{f(h * 0.12)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#4A3E38"></rect>']
    s = fit(b, max(h * 0.24, b - 230))
    o.append(glow(w * 0.76, b - 70 * s, 150 * s, "#FFFFFF", 0.9, f"{p}g") + light_seated(w * 0.76, b, s, flip=True))
    for i, (c, veil_) in enumerate(WOMEN3):
        o.append(woman_fig(p, w * (0.1 + 0.09 * i), b, s * (0.92 - 0.03 * i), c, veil_, flip=True))
    return "".join(o)

def mourners(p, w, h, seed):
    """She went and told them that had been with him, as they mourned and wept: a dim room, the disciples sitting with their
    heads bowed; Mary Magdalene come in at the bright doorway, her arm raised as she tells them."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#5A4A4A", floor="#3A2E2A"),
         f'<rect x="{f(w * 0.06)}" y="{f(h * 0.24)}" width="{f(w * 0.16)}" height="{f(b - h * 0.24)}" fill="#FFE6A0" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.24, b - 230))
    o.append(woman_fig(p, w * 0.14, b, s, ROBES["magdalene"], "#C2456A", flip=True, up=UP_HIGH))
    for i, x in enumerate((0.36, 0.5, 0.64, 0.78, 0.92)):
        o.append(seated(w * x, b, s * 0.78, TWELVE[i], head=TWELVE[i] if i % 2 else None, beard="#2A1A10", flip=True, bowed=True))
    return "".join(o)

def two_country(p, w, h, seed):
    """He was manifested in another form unto two of them, as they walked, on their way into the country: the road among
    the fields at evening, two disciples walking, and with them a figure in white light."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A6A", "#FFC890"), sun(w * 0.84, h * 0.44, 16, color="#FFE680", op=0.4), hills(w, h, h * 0.46, seed, color="#8A7A5A", amp=12, step=80),
         ground(w, h, h * 0.56, "#B8A06A", dy=0), grain(-10, w * 0.3, h * 0.8, h * 0.14, seed),
         f'<path d="M{f(w * 0.36)} {f(h + 10)} C {f(w * 0.44)} {f(h * 0.8)} {f(w * 0.6)} {f(h * 0.66)} {f(w * 0.7)} {f(h * 0.56)}" stroke="#E0D0A8" stroke-width="{f(max(8, h * 0.06))}" fill="none"></path>']
    s = fit(b, max(h * 0.24, b - 230))
    o.append(disciple(p, w * 0.42, b, s * 0.96, "#6A5A3A", flip=True) + disciple(p, w * 0.54, b, s * 0.94, "#4A5A6A", flip=True))
    o.append(jesus_risen(p, w * 0.68, b, s, flip=True))
    return "".join(o)

def eleven_meat(p, w, h, seed):
    """He was manifested unto the eleven themselves as they sat at meat: the low table under the lamp, the eleven sitting
    about it, and Jesus risen standing among them in white light."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#6A5A4A", floor="#4A3A30"), A.lamp(w * 0.72, h * 0.24, max(0.6, h / 300))]
    s = fit(b, max(h * 0.2, b - 230))
    o.append(f'<rect x="{f(w * 0.28)}" y="{f(b - 40 * s)}" width="{f(w * 0.66)}" height="{f(16 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
    for i, x in enumerate((0.32, 0.44, 0.56, 0.68, 0.8, 0.92)):
        c = TWELVE[i]
        o.append(seated(w * x, b, s * 0.76, c, head=c if i % 2 else None, beard="#2A1A10", flip=x > 0.6))
    o.append(jesus_risen(p, w * 0.16, b, s, up=UP_BLESS))
    return "".join(o)

def received_up(p, w, h, seed):
    """He was received up into heaven, and sat down at the right hand of God: above the mount, Jesus risen in white light
    going up into a great cloud of light; the eleven below on the hill looking up (God is never drawn: the light only)."""
    b = h * 0.96
    o = [mk.defs(p, *ALL), sky(w, h, "#2A3A7A", "#FFE6A0"), rays(w * 0.5, h * 0.14, 32, 30, max(w, h), color="#FFFDF0", op=0.25),
         glow(w * 0.5, h * 0.16, h * 0.4, "#FFFFFF", 0.95, f"{p}g"), clouds(w, h * 0.16, seed, n=6, color="#FFFDF0", op=0.85, h=h),
         f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.7)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A8A4A" stroke="{INK}" stroke-width="2"></path>']
    sj = fit(h * 0.5, h * 0.24)
    o.append(jesus_risen(p, w * 0.5, h * 0.5, sj, up=UP_HIGH))
    for i in range(11):
        x = w * (0.08 + 0.084 * i); y = h * 0.86 + (i % 2) * 6
        if 4 <= i <= 6: x += w * 0.0
        s = fit(y, y - h * 0.16)
        o.append(mk.person(p, round(x), round(y), round(s, 3), body="#B98A6E", cloth=TWELVE[i if i < 6 else i + 1], kind="Robe", sw=3, flip=i > 5,
                           up=[(-22, -158), (-30, -190), (-34, -222)] if i % 3 == 0 else None))
    return "".join(o)

def everywhere(p, w, h, seed):
    """They went forth, and preached everywhere, the Lord working with them: from the hill the roads going out to the towns
    in every direction under the morning sky, the disciples two by two upon them, a soft light over all."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), glow(w * 0.5, 0, h * 0.6, "#FFFFFF", 0.6, f"{p}g"), hills(w, h, h * 0.34, seed, color="#8A9A7A", amp=14, step=90)]
    for i, x in enumerate((0.1, 0.34, 0.66, 0.92)):
        o.append(hill_town(w * x, h * 0.42, w * 0.12, h * 0.1, seed + i, hill="#9AAA7A"))
    o.append(ground(w, h, h * 0.44, "#B8B07A", dy=0))
    for ex in (0.1, 0.34, 0.66, 0.92):
        o.append(f'<path d="M{f(w * 0.5)} {f(h + 10)} C {f(w * 0.5)} {f(h * 0.7)} {f(w * ex)} {f(h * 0.56)} {f(w * ex)} {f(h * 0.44)}" stroke="#D8C8A0" stroke-width="{f(max(5, h * 0.03))}" fill="none"></path>')
    for i, (x, y) in enumerate(((0.16, 0.6), (0.38, 0.64), (0.6, 0.64), (0.82, 0.6), (0.26, 0.86), (0.7, 0.86))):
        for j in range(2):
            yy = h * y; ss = fit(yy, yy - h * 0.14 * (1 + (y - 0.6) * 2.4))
            c = TWELVE[(i * 2 + j) % 12]
            head = A.headcloth(["#E8E2D6", "#6A5A3A", "#3A4A6A", "#8A847A"][(i + j) % 4], cord="#3A2214") + (A.BLACK_BEARD if (i + j) % 3 else "")
            o.append(mk.person(p, round(w * x + (j - 0.5) * 84 * ss), round(yy), round(ss, 3), body="#B98A6E", cloth=c, kind="Tunic", sw=3, flip=x > 0.5, extra=head))
    return "".join(o)
