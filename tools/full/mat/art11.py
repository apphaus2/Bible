"""Drawings for Matthew 27–28, drawn with the restraint the volume keeps for the passion: Jesus led bound at dawn; the
silver scattered on the sanctuary floor; the potter's field at dusk (Judas's death in words only); Pilate's judgment-seat on
the Pavement and the crowd; the basin of water; the empty court of the Praetorium with the scarlet robe and the reed laid
aside (the scourging, the thorns and the mocking in words only); Simon of Cyrene bearing the cross out of the gate; Golgotha
— the three crosses on the hill against a darkened sky, seen only from far off, no figure on them in any detail; the lots
cast at the foot of the hill; the darkness over all the land; the veil of the temple rent, the rocks rent and the tombs
open; the women beholding from afar; the new tomb hewn in the rock and its great stone; the seal and the guard; the angel
of the Lord (white light, no face) on the stone rolled away, the guards fallen; the place where the Lord lay, the linen
folded; Jesus risen in white light, the women at his feet; the money given to the soldiers; the mountain in Galilee.
Built on mat.art10."""
from mat.art10 import *
from mat.art10 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, torch, jesus_kneel
from ntcast import JESUS_SKIN, JESUS_HAIR, JESUS_TUNIC, JESUS_MANTLE, ROBES
import random, math
from job.art import seated, smoke
import exodus as E

def jesus_risen(p, x, y, s, flip=False, up=None):
    """Jesus risen: his figure in white light, a bright glow about him."""
    return (glow(x, y - 110 * s, 170 * s, "#FFFFFF", 0.95, f"{p}rz{int(x)}") + rays(x, y - 110 * s, 24, 60 * s, 220 * s, color="#FFFDF0", op=0.3)
            + jesus_fig(p, x, y, s, flip=flip, up=up, glow=False).replace(JESUS_TUNIC, "#FFFFFF").replace(JESUS_MANTLE, "#E8ECF8"))

def roman_fig(p, x, y, s, flip=False, up=None):
    return soldier_fig(p, x, y, s, flip=flip, up=up)

def pilate_fig(p, x, y, s, flip=False, up=None):
    """Pilate the governor: a white toga with a broad purple border, bareheaded, clean-shaven."""
    border = '<path d="M-24 -160 C -10 -150 6 -120 14 -40 L 22 -40 C 14 -120 0 -156 -14 -164 Z" fill="#6A1A5A" stroke="#0D0D0F" stroke-width="1.4"></path>'
    hair = '<path d="M-13 -192 C -12 -204 12 -204 13 -192 C 8 -196 -8 -196 -13 -192 Z" fill="#4A3A2A"></path>'
    return mk.person(p, round(x), round(y), round(s, 3), body="#E3B08A", cloth="#F3EFE6", kind="Robe", sw=3, flip=flip, up=up, extra=border + hair)

def bound_dawn(p, w, h, seed):
    """When morning was come, they bound him, and led him away to Pilate: the street at grey dawn, Jesus with his hands bound
    walking between two officers of the temple, a priest in white going before."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A4A", "#C8906A"), houses(w, h, h * 0.8, seed, hmin=0.36, hmax=0.52, stairs=False), pavement(w, h, h * 0.8, color="#8A7A6A", line="#6A5A4A")]
    s = fit(b, max(h * 0.26, b - 220))
    o.append(scribe_fig(p, w * 0.82, b, s, white=True))
    o.append(man(p, w * 0.62, b, s * 0.96, "#3A3A4A", extra='<path d="M30 -150 L 44 -230" stroke="#5A3A22" stroke-width="5"></path>'))
    o.append(jesus(p, w * 0.46, b, s, glow=False) + f'<path d="M{f(w * 0.46 - 20 * s)} {f(b - 100 * s)} L {f(w * 0.46 + 20 * s)} {f(b - 96 * s)}" stroke="#8A6A3A" stroke-width="{f(4 * s)}"></path>')
    o.append(man(p, w * 0.3, b, s * 0.96, "#3A3A4A"))
    return "".join(o)

def silver_floor(p, w, h, seed):
    """He cast down the pieces of silver into the sanctuary: the silver coins scattered across the stone floor before the
    sanctuary doors — no one drawn."""
    r = random.Random(seed)
    o = [bgr(w, h, "#3A2A2A"), f'<rect x="{f(w * 0.3)}" y="{f(h * 0.06)}" width="{f(w * 0.4)}" height="{f(h * 0.5)}" fill="#E8B830" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.38)}" y="{f(h * 0.14)}" width="{f(w * 0.24)}" height="{f(h * 0.42)}" fill="#7A2A3A" stroke="{INK}" stroke-width="2"></rect>',
         pavement(w, h, h * 0.56, color="#B8A888", line="#98886A")]
    for _ in range(30):
        x = r.uniform(w * 0.1, w * 0.9); y = r.uniform(h * 0.62, h * 0.98); k = 0.5 + (y - h * 0.6) / h
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(9 * k)}" ry="{f(4 * k)}" fill="#D8D8E0" stroke="{INK}" stroke-width="1"></ellipse>')
    return "".join(o)

def potters_field(p, w, h, seed):
    """The potter's field, the field of blood, to bury strangers in: a bare clay field at dusk, broken potsherds, a few
    rough heaps of stones for graves — no one drawn."""
    r = random.Random(seed)
    o = [sky(w, h, "#2A1A2A", "#A84A2A"), hills(w, h, h * 0.5, seed, color="#3A2A2A", amp=12, step=80), ground(w, h, h * 0.58, "#8A4A30", dy=0)]
    for i in range(5):
        x = w * (0.12 + 0.18 * i); y = h * (0.74 + 0.04 * (i % 2)); k = max(0.5, h / 300)
        o.append(f'<path d="M{f(x - 34 * k)} {f(y)} C {f(x - 24 * k)} {f(y - 26 * k)} {f(x + 24 * k)} {f(y - 26 * k)} {f(x + 34 * k)} {f(y)} Z" fill="#7A6A5A" stroke="{INK}" stroke-width="1.8"></path>')
    for _ in range(16):
        x = r.uniform(0, w); y = r.uniform(h * 0.84, h * 0.98)
        o.append(f'<path d="M{f(x)} {f(y)} l 10 -6 l 6 8 Z" fill="#B5652E" stroke="{INK}" stroke-width="1"></path>')
    return "".join(o)

def judgment_seat(p, w, h, seed, crowd_=True, wash=False):
    """Jesus before the governor: Pilate on his judgment-seat on the raised Pavement before the Praetorium's columns, Jesus
    standing before him; crowd_=True the multitude below; wash=True a servant holding a basin of water before Pilate."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8")]
    for x in (0.08, 0.24, 0.4):
        o.append(f'<rect x="{f(w * x - 14)}" y="{f(h * 0.1)}" width="28" height="{f(h * 0.6)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.04)}" width="{f(w * 0.5)}" height="{f(h * 0.06)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w * 0.56)}" height="{f(h * 0.06)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    o.append(pavement(w, h, h * 0.76))
    s = fit(h * 0.7, max(h * 0.16, h * 0.7 - 220))
    o.append(f'<rect x="{f(w * 0.08)}" y="{f(h * 0.7 - 70 * s)}" width="{f(70 * s)}" height="{f(70 * s)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(pilate_fig(p, w * 0.1 + 35 * s, h * 0.7, s, up=UP_BLESS if wash else None))
    if wash:
        o.append(f'<ellipse cx="{f(w * 0.1 + 35 * s - 70 * s)}" cy="{f(h * 0.7 - 110 * s)}" rx="{f(24 * s)}" ry="{f(8 * s)}" fill="#C8963E" stroke="{INK}" stroke-width="1.6"></ellipse>')
    o.append(jesus(p, w * 0.42, h * 0.7, s * 0.98, flip=True, glow=False))
    if crowd_:
        bb = b
        o.append(crowd(p, w * 0.56, w * 0.98, bb, bb - 160 * s * 1.1, 9, seed, flip=True, up=UP_HIGH if wash else None))
        o.append(scribe_fig(p, w * 0.6, bb, s * 1.04, white=True, flip=True))
    return "".join(o)

def robe_laid(p, w, h, seed):
    """The Praetorium court empty: the scarlet robe thrown down on the pavement by a pillar, a reed beside it — the scourging,
    the crown of thorns and the mocking are told in words only."""
    b = h * 0.92
    o = [bgr(w, h, "#5A4A44")]
    for x in (0.16, 0.84):
        o.append(f'<rect x="{f(w * x - 22)}" y="-10" width="44" height="{f(b + 10)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    o.append(pavement(w, h, b - h * 0.16, color="#8A7A6A", line="#6A5A4A"))
    k = max(0.6, h / 260)
    cx = w * 0.46
    o.append(f'<path d="M{f(cx - 90 * k)} {f(b)} C {f(cx - 70 * k)} {f(b - 40 * k)} {f(cx - 10 * k)} {f(b - 50 * k)} {f(cx + 30 * k)} {f(b - 30 * k)} C {f(cx + 60 * k)} {f(b - 40 * k)} {f(cx + 90 * k)} {f(b - 20 * k)} {f(cx + 96 * k)} {f(b)} Z" fill="#A8181E" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(cx - 40 * k)} {f(b - 30 * k)} C {f(cx - 20 * k)} {f(b - 10 * k)} {f(cx + 20 * k)} {f(b - 16 * k)} {f(cx + 50 * k)} {f(b - 6 * k)}" stroke="#6A0A10" stroke-width="2" fill="none"></path>'
             f'<path d="M{f(cx + 110 * k)} {f(b - 4)} L {f(cx + 240 * k)} {f(b - 30 * k)}" stroke="#A8A05A" stroke-width="{f(4 * k)}"></path>')
    return "".join(o)

def cyrene(p, w, h, seed):
    """As they came out, they found a man of Cyrene, Simon: the road out of the city gate, Simon bearing the cross-beam on his
    shoulder, Jesus walking before him between the soldiers."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8A8A9A", "#E8C8A0"), walls(w * 0.6, w + 10, h * 0.66, h * 0.4, seed, towers=2), ground(w, h, h * 0.66, "#B8A07A", dy=0)]
    s = fit(b, max(h * 0.26, b - 220))
    beam = '<path d="M-90 -170 L 60 -150" stroke="#6A4A2A" stroke-width="12" stroke-linecap="round"></path>'
    o.append(man(p, w * 0.56, b, s, "#2A6A5A", up=[(-22, -158), (-30, -170), (-20, -176)], extra=beam))
    o.append(roman_fig(p, w * 0.42, b, s * 0.96) + roman_fig(p, w * 0.78, b, s * 0.96))
    o.append(jesus(p, w * 0.24, b, s, glow=False))
    o.append(roman_fig(p, w * 0.1, b, s * 0.94))
    return "".join(o)

def golgotha(p, w, h, seed, dark=False, lots=False, passers=False):
    """Golgotha seen from far off: a bare hill against the sky, on its top three crosses standing against the light, small and
    dark (no wounds, nothing in detail); dark=True: the darkness over all the land, the sky black, a dull red rim; lots=True:
    soldiers at the foot of the hill, near, crouched over their lots and the garments; passers=True: people on the road
    below, wagging their heads."""
    b = h * 0.94
    top, bot = ("#05050E", "#3A1A1A") if dark else ("#4A3A5A", "#C8805A")
    o = [mk.defs(p, *ALL), sky(w, h, top, bot)]
    if not dark: o.append(clouds(w, h * 0.16, seed, n=5, color="#3A2A3A", op=0.8, h=h))
    hx = w * 0.56
    o.append(f'<path d="M{f(hx - w * 0.5)} {f(h * 0.78)} C {f(hx - w * 0.24)} {f(h * 0.4)} {f(hx + w * 0.2)} {f(h * 0.38)} {f(hx + w * 0.5)} {f(h * 0.78)} Z" fill="{"#1A1418" if dark else "#5A4A44"}" stroke="{INK}" stroke-width="2"></path>')
    k = max(0.3, h / 900)
    for dx, tall in ((-0.12, 0.9), (0, 1.0), (0.12, 0.9)):
        x = hx + dx * w; base = h * 0.44 + abs(dx) * h * 0.1; ch = 120 * k * tall
        col = "#0D0D0F"
        o.append(f'<path d="M{f(x)} {f(base)} L {f(x)} {f(base - ch)} M{f(x - 30 * k)} {f(base - ch * 0.78)} L {f(x + 30 * k)} {f(base - ch * 0.78)}" stroke="{col}" stroke-width="{f(5 * k + 1)}"></path>')
        o.append(f'<circle cx="{f(x)}" cy="{f(base - ch * 0.84)}" r="{f(5 * k + 1)}" fill="{col}"></circle><path d="M{f(x)} {f(base - ch * 0.78)} L {f(x)} {f(base - ch * 0.46)}" stroke="{col}" stroke-width="{f(7 * k + 1)}"></path>')
    o.append(ground(w, h, h * 0.8, "#2A2228" if dark else "#7A6A5A", dy=0))
    s = fit(b, max(h * 0.3, b - 220))
    if lots:
        for i, x in enumerate((0.2, 0.36, 0.64, 0.8)):
            o.append(seated(w * x, b, s * 0.8, "#A8281E", head="#C8963E", beard="", flip=x > 0.5))
        o.append(f'<path d="M{f(w * 0.44)} {f(b)} L {f(w * 0.56)} {f(b - 6)} L {f(w * 0.58)} {f(b)} Z" fill="{JESUS_TUNIC}" stroke="{INK}" stroke-width="1.6"></path>'
                 f'<rect x="{f(w * 0.48)}" y="{f(b - 14)}" width="8" height="8" fill="#F3EFE6" stroke="{INK}" stroke-width="1"></rect><rect x="{f(w * 0.51)}" y="{f(b - 12)}" width="8" height="8" fill="#F3EFE6" stroke="{INK}" stroke-width="1"></rect>')
    if passers:
        o.append(crowd(p, w * 0.04, w * 0.6, b, b - 150 * s, 6, seed))
        o.append(scribe_fig(p, w * 0.76, b, s, white=True, flip=True) + scribe_fig(p, w * 0.88, b, s * 0.98, flip=True))
    return "".join(o)

def veil_rent(p, w, h, seed):
    """The veil of the temple rent in two from the top to the bottom: the great curtain before the holy place torn down its
    length, light beyond it; the floor cracked by the earthquake."""
    o = [bgr(w, h, "#1A1018"), f'<rect x="{f(w * 0.18)}" y="{f(h * 0.04)}" width="{f(w * 0.64)}" height="{f(h * 0.82)}" fill="#E8B830" stroke="{INK}" stroke-width="2.4"></rect>',
         glow(w * 0.5, h * 0.4, h * 0.4, "#FFFFFF", 0.9, f"{p}g")]
    L = (f'M{f(w * 0.22)} {f(h * 0.08)} L {f(w * 0.49)} {f(h * 0.08)} L {f(w * 0.47)} {f(h * 0.3)} L {f(w * 0.5)} {f(h * 0.5)} L {f(w * 0.46)} {f(h * 0.7)} L {f(w * 0.48)} {f(h * 0.86)} L {f(w * 0.22)} {f(h * 0.86)} Z')
    R = (f'M{f(w * 0.78)} {f(h * 0.08)} L {f(w * 0.51)} {f(h * 0.08)} L {f(w * 0.55)} {f(h * 0.3)} L {f(w * 0.53)} {f(h * 0.5)} L {f(w * 0.57)} {f(h * 0.7)} L {f(w * 0.56)} {f(h * 0.86)} L {f(w * 0.78)} {f(h * 0.86)} Z')
    for d in (L, R):
        o.append(f'<path d="{d}" fill="#6A1A3A" stroke="{INK}" stroke-width="2.4"></path>')
    for k in range(5):
        x = w * (0.26 + 0.12 * k)
        o.append(f'<path d="M{f(x)} {f(h * 0.1)} L {f(x + (4 if x < w / 2 else -4))} {f(h * 0.84)}" stroke="#4A0A2A" stroke-width="2" opacity="0.6"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.86)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.1)} {f(h + 10)} L {f(w * 0.3)} {f(h * 0.9)} L {f(w * 0.5)} {f(h * 0.96)} L {f(w * 0.7)} {f(h * 0.88)}" stroke="#1A0A08" stroke-width="4" fill="none"></path>')
    return "".join(o)

def tombs_open(p, w, h, seed):
    """The earth did quake, the rocks were rent, and the tombs were opened: a rocky hillside split, the round stones rolled
    from the tomb doors, light within — no one drawn."""
    o = [sky(w, h, "#1A1A2A", "#5A4A5A"), f'<path d="M-10 {f(h * 0.3)} C {f(w * 0.3)} {f(h * 0.2)} {f(w * 0.7)} {f(h * 0.26)} {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A5A54" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.3)} {f(h * 0.26)} L {f(w * 0.36)} {f(h * 0.5)} L {f(w * 0.3)} {f(h * 0.7)} L {f(w * 0.38)} {f(h + 10)}" stroke="#1A0A08" stroke-width="5" fill="none"></path>']
    for i in range(4):
        x = w * (0.14 + 0.24 * i); y = h * (0.66 + 0.04 * (i % 2)); rr = min(w * 0.06, h * 0.12)
        o.append(f'<path d="M{f(x - rr)} {f(y + rr)} L {f(x - rr)} {f(y - rr * 0.4)} Q {f(x)} {f(y - rr * 1.4)} {f(x + rr)} {f(y - rr * 0.4)} L {f(x + rr)} {f(y + rr)} Z" fill="#FFF4C2" stroke="{INK}" stroke-width="1.6"></path>'
                 f'<circle cx="{f(x + rr * 1.9)}" cy="{f(y + rr * 0.3)}" r="{f(rr * 0.9)}" fill="#A89A8A" stroke="{INK}" stroke-width="1.8"></circle>')
    return "".join(o)

def women_afar(p, w, h, seed):
    """Many women beholding from afar: the women standing together on a slope in the foreground under the darkened sky, the
    hill of the crosses far off."""
    b = h * 0.94
    o = [golgotha(p, w, h, seed, dark=True)]
    s = fit(b, max(h * 0.3, b - 220))
    cols = [(ROBES["magdalene"], "#C2456A"), ("#6A4A2A", "#8A6A4A"), ("#8A5A3A", "#A87A5A"), ("#3A4A6A", "#5A6A8A")]
    for i, (c, sc) in enumerate(cols):
        o.append(woman_fig(p, w * (0.1 + 0.1 * i), b, s * (0.96 - 0.02 * i), c, sc))
    return "".join(o)

def new_tomb(p, w, h, seed, stone=True, women=False, sealed=False, guard=False):
    """Joseph's new tomb hewn out in the rock, in a garden at evening: the low doorway; stone=True the great round stone rolled
    to the door; women=True Mary Magdalene and the other Mary sitting over against it; sealed=True a cord and a seal across the
    stone; guard=True soldiers standing watch."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A4A", "#C8906A"),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.34)} {f(h * 0.3)} C {f(w * 0.5)} {f(h * 0.2)} {f(w * 0.8)} {f(h * 0.22)} {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.5)} {f(b - h * 0.04)} L {f(w * 0.5)} {f(h * 0.54)} Q {f(w * 0.58)} {f(h * 0.44)} {f(w * 0.66)} {f(h * 0.54)} L {f(w * 0.66)} {f(b - h * 0.04)} Z" fill="#1A1210" stroke="{INK}" stroke-width="2"></path>',
         ground(w, h, b - h * 0.04, "#5A6A3A", dy=0), olive(w * 0.1, b, h / 360, seed=seed)]
    if stone:
        cx, cy, r = w * 0.6, b - h * 0.04 - h * 0.17, h * 0.17
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="#A89A8A" stroke="{INK}" stroke-width="2.6"></circle><circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r * 0.7)}" fill="none" stroke="#8A7A6A" stroke-width="2"></circle>')
        if sealed:
            o.append(f'<path d="M{f(w * 0.46)} {f(cy)} L {f(w * 0.74)} {f(cy)}" stroke="#C8A878" stroke-width="3"></path><circle cx="{f(w * 0.6)}" cy="{f(cy)}" r="{f(r * 0.16)}" fill="#B5121B" stroke="{INK}" stroke-width="1.6"></circle>')
    s = fit(b, max(h * 0.3, b - 220))
    if women:
        o.append(woman_fig(p, w * 0.14, b, s * 0.9, ROBES["magdalene"], "#C2456A") + woman_fig(p, w * 0.24, b, s * 0.88, "#6A4A2A", "#8A6A4A"))
    if guard:
        o.append(roman_fig(p, w * 0.4, b, s * 0.96) + roman_fig(p, w * 0.8, b, s * 0.96, flip=True))
    return "".join(o)

def stone_rolled(p, w, h, seed, guards=True, women=False):
    """At dawn: the stone rolled away from the door, and sitting upon it an angel of the Lord, a figure of white light with
    a gold rim and no face, his raiment white as snow; guards=True the watchers fallen on the ground as dead men; women=True
    the two Marys standing before him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL, *LIE), sky(w, h, "#3A3A7A", "#FFC890"), sun(w * 0.9, h * 0.5, 16, color="#FFE680", op=0.4),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.34)} {f(h * 0.3)} C {f(w * 0.5)} {f(h * 0.2)} {f(w * 0.8)} {f(h * 0.22)} {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.5)} {f(b - h * 0.04)} L {f(w * 0.5)} {f(h * 0.54)} Q {f(w * 0.58)} {f(h * 0.44)} {f(w * 0.66)} {f(h * 0.54)} L {f(w * 0.66)} {f(b - h * 0.04)} Z" fill="#1A1210" stroke="{INK}" stroke-width="2"></path>',
         ground(w, h, b - h * 0.04, "#5A6A3A", dy=0)]
    cx, cy, r = w * 0.82, b - h * 0.04 - h * 0.14, h * 0.14
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="#A89A8A" stroke="{INK}" stroke-width="2.6"></circle>')
    s = fit(b, max(h * 0.3, b - 220))
    o.append(glow(cx, cy - r - 60 * s, 140 * s, "#FFFFFF", 0.95, f"{p}ag") + angel(p, cx, cy - r * 0.6, s * 0.9, flip=True, up=UP_BLESS))
    if guards:
        for x in (0.14, 0.34):
            o.append(f'<g transform="translate({f(w * x + 90 * s * 0.6)} {f(b - 2)}) scale({f(s * 0.6)})" fill="#A8281E" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use><use href="#{p}LieA"></use></g>')
    if women:
        o.append(woman_fig(p, w * 0.2, b, s * 0.9, ROBES["magdalene"], "#C2456A", up=UP_BLESS) + woman_fig(p, w * 0.32, b, s * 0.88, "#6A4A2A", "#8A6A4A"))
    return "".join(o)

def linen(p, w, h, seed):
    """Come, see the place where the Lord lay: inside the tomb, the stone shelf empty, the linen cloth lying folded on it,
    morning light falling through the open door."""
    o = [bgr(w, h, "#2A2220"), f'<path d="M{f(w * 0.06)} {f(h * 0.2)} L {f(w * 0.06)} {f(h * 0.9)} L {f(w * 0.3)} {f(h * 0.9)} L {f(w * 0.3)} {f(h * 0.3)} Q {f(w * 0.18)} {f(h * 0.12)} {f(w * 0.06)} {f(h * 0.2)} Z" fill="#FFE6A0" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.3)} {f(h * 0.9)} L {f(w * 0.06)} {f(h * 0.9)} L {f(w * 0.5)} {f(h + 10)} L {f(w * 0.9)} {f(h + 10)} Z" fill="#FFE680" opacity="0.3"></path>',
         f'<rect x="{f(w * 0.38)}" y="{f(h * 0.6)}" width="{f(w * 0.58)}" height="{f(h * 0.14)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.38)}" y="{f(h * 0.74)}" width="{f(w * 0.58)}" height="{f(h * 0.26)}" fill="#6A5A54" stroke="{INK}" stroke-width="2"></rect>']
    k = max(0.6, h / 260)
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.6)} L {f(w * 0.52)} {f(h * 0.6 - 16 * k)} L {f(w * 0.74)} {f(h * 0.6 - 16 * k)} L {f(w * 0.76)} {f(h * 0.6)} Z" fill="#F8F4EC" stroke="{INK}" stroke-width="1.8"></path>'
             f'<path d="M{f(w * 0.53)} {f(h * 0.6 - 8 * k)} L {f(w * 0.75)} {f(h * 0.6 - 8 * k)}" stroke="#C8C0B0" stroke-width="1.4"></path>'
             f'<path d="M{f(w * 0.82)} {f(h * 0.6)} L {f(w * 0.83)} {f(h * 0.6 - 10 * k)} L {f(w * 0.9)} {f(h * 0.6 - 10 * k)} L {f(w * 0.91)} {f(h * 0.6)} Z" fill="#F8F4EC" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def met_them(p, w, h, seed):
    """Jesus met them, saying, All hail: Jesus risen in white light on the garden path at sunrise, the two Marys fallen at
    his feet holding them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A9A", "#FFE6A0"), sun(w * 0.8, h * 0.5, 20, color="#FFF4C2", op=0.5), hills(w, h, h * 0.56, seed, color="#7A8A5A", amp=10, step=80),
         ground(w, h, h * 0.66, "#8AA84A", dy=0), olive(w * 0.92, b, h / 340, seed=seed)]
    s = fit(b, max(h * 0.3, b - 220))
    o.append(jesus_risen(p, w * 0.36, b, s, up=UP_BLESS))
    o.append(E.kneel(w * 0.54, b, s * 0.8, color=ROBES["magdalene"], flip=True, skin=SKIN) + E.kneel(w * 0.68, b, s * 0.78, color="#6A4A2A", flip=True, skin=SKIN))
    return "".join(o)

def bribe(p, w, h, seed):
    """They gave much money unto the soldiers: in a dim room, chief priests pressing bags of money into the hands of the
    soldiers of the guard."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#4A3A3A", floor="#3A2A2A"), A.lamp(w * 0.5, h * 0.26, max(0.6, h / 300))]
    s = fit(b, max(h * 0.26, b - 220))
    o.append(scribe_fig(p, w * 0.3, b, s, white=True, flip=True, up=[(-22, -158), (-40, -136), (-56, -120)]))
    o.append(scribe_fig(p, w * 0.16, b, s * 0.96, flip=True))
    o.append(roman_fig(p, w * 0.56, b, s * 0.96, up=[(22, -158), (40, -136), (56, -120)]) + roman_fig(p, w * 0.7, b, s * 0.94) + roman_fig(p, w * 0.84, b, s * 0.94))
    o.append(f'<path d="M{f(w * 0.43 - 8)} {f(b - 128 * s)} C {f(w * 0.43 - 18)} {f(b - 116 * s)} {f(w * 0.43 - 12)} {f(b - 100 * s)} {f(w * 0.43)} {f(b - 100 * s)} C {f(w * 0.43 + 12)} {f(b - 100 * s)} {f(w * 0.43 + 18)} {f(b - 116 * s)} {f(w * 0.43 + 8)} {f(b - 128 * s)} Z" fill="#C8963E" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def galilee_mount(p, w, h, seed):
    """The mountain in Galilee where Jesus had appointed them: Jesus risen in white light on the hill-top, the eleven before
    him, some kneeling, the lake far below in the morning."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), lake(w, h, h * 0.5, seed, n=8),
         f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.2)} {f(h * 0.4)} {f(w * 0.5)} {f(h * 0.44)} {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8AB84A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.3, b - 220))
    o.append(jesus_risen(p, w * 0.26, h * 0.62, s * 0.9, up=UP_HIGH))
    for i in range(11):
        x = w * (0.42 + 0.052 * i); y = h * (0.78 + 0.1 * (i % 3) / 2)
        c = TWELVE[i] if i < 6 else TWELVE[i + 1] if i + 1 < 12 else TWELVE[0]
        if i % 3 == 0: o.append(E.kneel(x, y, s * 0.6, color=c, flip=True, skin="#B98A6E"))
        else: o.append(mk.person(p, round(x), round(y), round(s * 0.7, 3), body="#B98A6E", cloth=c, kind="Robe", sw=3, flip=True))
    return "".join(o)
