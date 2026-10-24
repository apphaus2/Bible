"""Drawings for the Mark volume. Mark shares most of Matthew's scenes, so this starts from all of Matthew's drawings
(`from mat.art11 import *`, which carries mat.art … mat.art10) and adds Mark's own: the forty days with the wild beasts,
the desert place before day, the house at Capernaum with the roof broken up and the bed let down, and the scenes of the
later chapters below.

Jesus at a distance is only ever ntcast.jesus_fig; the disciples at a distance wear ntcast.ROBES. Angels are figures of
white light with a gold rim and no face (angel); the Spirit a dove of light; God, Satan and demons are never drawn. Every
function takes (p, w, h, seed, ...) — p, a prefix unique to the panel, names the figure defs and gradients."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from mat.art11 import *
from mat.art11 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, torch, jesus_kneel, jesus_risen, roman_fig, pilate_fig
import mk
from ntcast import jesus_fig, ROBES, JESUS_TUNIC, JESUS_MANTLE, JESUS_SKIN, JESUS_HAIR
import judges2 as J2
from job.art import seated
from exo import art as A

def silhouette(svg, color="#0B0610"):
    """A drawing filled flat in one dark colour (beasts on a ridge against the night)."""
    return f'<g fill="{color}" stroke="{color}">' + svg.replace('fill="', 'data-f="').replace('stroke="', 'data-s="') + '</g>'

def lying(p, x, y, s, cloth="#C8B898", flip=False):
    """A man lying on his back on a bed (the LIE figure, needs *LIE in the panel's defs), (x, y) under his middle."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})" fill="{cloth}" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use>'
            f'<use href="#{p}LieA"></use></g>')

def on_bed(p, x, y, wd, cloth="#C8B898", bed="#C8B088", flip=False):
    """A man lying on a bed wd wide, (x, y) the middle of the bed's top: the pallet, and the LIE figure filling it."""
    k = wd / 235
    return bedroll(x, y, wd, max(6, 14 * k)) + lying(p, x + (-85 if flip else 85) * k, y + 1, k, cloth, flip=flip)

def bedroll(x, y, wd, th, color="#C8B088"):
    return f'<rect x="{f(x - wd / 2)}" y="{f(y)}" width="{f(wd)}" height="{f(th)}" rx="{f(th / 3)}" fill="{color}" stroke="{INK}" stroke-width="2"></rect>'

# ---- Mark 1 -------------------------------------------------------------------------------------------------------------
def with_beasts(p, w, h, seed):
    """Forty days in the wilderness with the wild beasts: the night desert, a lion and jackals dark on the ridges, Jesus alone
    standing below, and two angels of white light ministering beside him (the tempter is never drawn)."""
    b = h * 0.92
    o = [wilderness(p, w, h, seed, john=False, tone="night")]
    k = max(0.3, h / 900)
    o.append(silhouette(J2.lion(w * 0.12, h * 0.5, k, roar=False)))
    o.append(silhouette(J2.fox(w * 0.84, h * 0.56, k * 0.8, flip=True, brand=False, seed=seed), "#100A16"))
    o.append(silhouette(J2.fox(w * 0.94, h * 0.6, k * 0.7, flip=True, brand=False, seed=seed + 1), "#100A16"))
    o.append(glow(w * 0.5, b - h * 0.3, h * 0.5, "#FFF4C2", 0.35, f"{p}g"))
    s = fit(b, max(h * 0.28, b - 220))
    o.append(angel(p, w * 0.3, b, s * 0.96, up=UP_BLESS))
    o.append(angel(p, w * 0.7, b, s * 0.96, flip=True, up=UP_BLESS))
    o.append(jesus(p, w * 0.5, b, s))
    return "".join(o)

def before_day(p, w, h, seed, found=False):
    """A great while before day, in a desert place: the hills deep blue, the last stars, Jesus alone with his arms lifted in
    prayer; found=True: Simon and the others coming over the ridge to him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#0B1A3A", "#6A6A9A"), mk.stars(30, w, h * 0.4, seed), hills(w, h, h * 0.52, seed, color="#2A2A4A", amp=24, step=90),
         ground(w, h, h * 0.7, "#3A3A5A", dy=0)]
    s = fit(b, max(h * 0.28, b - 220))
    o.append(jesus(p, w * 0.64, b, s, flip=True, up=UP_HIGH))
    if found:
        sd = s * 0.7
        for i, who in enumerate(("peter", "andrew", "james", "john")):
            o.append(disciple(p, w * (0.08 + 0.08 * i), h * 0.74 + 4 * i, sd, who))
    return "".join(o)

def synagogue_peace(p, w, h, seed):
    """They were all amazed: in the synagogue the man stands quiet and whole before Jesus, in a soft light; the people
    about them turned to one another (the unclean spirit is never drawn)."""
    b = h * 0.94
    o = [synagogue(p, w, h, seed, teaching=False, crowd_n=9)]
    s = fit(b, max(h * 0.2, b - 230))
    o.append(glow(w * 0.6, b - 110 * s, 130 * s, "#FFF4C2", 0.6, f"{p}g"))
    o.append(man(p, w * 0.6, b, s * 0.96, "#7A6A5A", flip=True))
    o.append(jesus(p, w * 0.42, b, s))
    return "".join(o)

def door_crowd(p, w, h, seed):
    """It was noised that he was in the house: a house of Capernaum, its door crowded, the street full, no room even about
    the door."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.62, seed, x0=w * 0.62, hmin=0.24, hmax=0.36)]
    hx0, hx1, top = w * 0.08, w * 0.6, h * 0.22
    o.append(f'<rect x="{f(hx0)}" y="{f(top)}" width="{f(hx1 - hx0)}" height="{f(b - top)}" fill="#E0CFA8" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(hx0 - 6)}" y="{f(top - 8)}" width="{f(hx1 - hx0 + 12)}" height="10" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.26)}" y="{f(b - h * 0.36)}" width="{f(w * 0.14)}" height="{f(h * 0.36)}" fill="#3A2A1E" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(hx1)} {f(b)} L {f(hx1 + h * 0.3)} {f(b)} L {f(hx1)} {f(top + 6)} Z" fill="#B8A07A" stroke="{INK}" stroke-width="2"></path>')
    o.append(pavement(w, h, b - h * 0.02))
    s = fit(b, max(h * 0.2, b - 230))
    o.append(crowd(p, w * 0.04, w * 0.74, b, b - 165 * s, 10, seed))
    return "".join(o)

def roof_opened(p, w, h, seed):
    """They uncovered the roof where he was, and let down the bed: the house of Capernaum drawn open like a doll's house —
    on the flat roof four men at the hole they have broken up, letting the bed down by cords; within, the room full, Jesus
    standing beneath; the crowd outside about the door."""
    b = h * 0.95
    hx0, hx1, top = w * 0.1, w * 0.76, h * 0.34
    gx0, gx1 = w * 0.36, w * 0.54
    o = [mk.defs(p, *ALL, *LIE), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.3, seed, color="#8A9A7A", amp=12, step=90), ground(w, h, b, "#C8B07A", dy=0),
         f'<rect x="{f(hx0)}" y="{f(top)}" width="{f(hx1 - hx0)}" height="{f(b - top)}" fill="#7A5A3A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(hx0 + 10)}" y="{f(top + 12)}" width="{f(hx1 - hx0 - 20)}" height="{f(b - top - 12)}" fill="#C8A878" stroke="{INK}" stroke-width="1.6"></rect>',
         f'<path d="M{f(gx0)} {f(top + 12)} L {f(gx1)} {f(top + 12)} L {f(gx1 + w * 0.06)} {f(b)} L {f(gx0 - w * 0.06)} {f(b)} Z" fill="#FFF4C2" opacity="0.4"></path>',
         f'<rect x="{f(hx0 - 6)}" y="{f(top - 4)}" width="{f(gx0 - hx0 + 6)}" height="16" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="{f(gx1)}" y="{f(top - 4)}" width="{f(hx1 - gx1 + 6)}" height="16" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>',
         f'<path d="M{f(gx0)} {f(top - 4)} l 8 -5 l 10 6 l 9 -4 M{f(gx1)} {f(top - 4)} l -8 -6 l -10 5 l -8 -4" stroke="#6A4A2A" stroke-width="2.4" fill="none"></path>',
         f'<path d="M{f(hx1 + 6)} {f(b)} L {f(hx1 + 6 + (b - top) * 0.45)} {f(b)} L {f(hx1 + 6)} {f(top + 8)} Z" fill="#B8A07A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(top - 4, max(h * 0.02, top - 4 - 130))
    by = top + (b - top) * 0.42; bw = (gx1 - gx0) * 1.1; cx = (gx0 + gx1) / 2
    hands = []
    for i, (x, fl) in enumerate(((gx0 - w * 0.1, True), (gx0 - w * 0.03, True), (gx1 + w * 0.03, False), (gx1 + w * 0.1, False))):
        o.append(man(p, x, top - 4, s, HEB[i + 2], flip=fl, up=[(-22, -158), (-36, -122), (-50, -92)]))
        hands.append((x + (50 if fl else -50) * s, top - 4 - 92 * s))
    ends = [cx - bw / 2 + 4, cx - bw / 2 + 4, cx + bw / 2 - 4, cx + bw / 2 - 4]
    for (hx, hy), ex in zip(hands, ends):
        o.append(f'<path d="M{f(hx)} {f(hy)} L {f(ex)} {f(by)}" stroke="#E8D8B0" stroke-width="2"></path>')
    o.append(on_bed(p, cx, by, bw))
    si = fit(b, max(top + 40, b - 200))
    o.append(jesus(p, hx0 + (gx0 - hx0) * 0.4, b, si, up=UP_BLESS, glow=False))
    r = random.Random(seed)
    for i in range(4):
        x = gx1 + (hx1 - gx1) * (i + 0.6) / 4.4
        o.append(man(p, x, b, si * r.uniform(0.86, 0.96), r.choice(HEB), flip=True))
    o.append(crowd(p, hx1 + 20, w * 1.02, b, b - 150 * si, 3, seed + 5, flip=True))
    return "".join(o)

def let_down(p, w, h, seed):
    """Within the house: the bed let down through the broken roof on its cords, light falling with it, the man of the palsy
    lying on it; Jesus before him; the scribes sitting by the wall."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, *LIE), room(w, h, b, wall="#B89A70", floor="#7A5A3A"),
         f'<path d="M{f(w * 0.4)} {f(h * 0.06)} L {f(w * 0.6)} {f(h * 0.06)} L {f(w * 0.74)} {f(b)} L {f(w * 0.28)} {f(b)} Z" fill="#FFF4C2" opacity="0.35"></path>',
         f'<rect x="{f(w * 0.4)}" y="{f(h * 0.04)}" width="{f(w * 0.2)}" height="{f(h * 0.07)}" fill="#8FD0E2" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.2, b - 230))
    by = b - h * 0.3
    o.append(f'<path d="M{f(w * 0.4)} {f(h * 0.1)} L {f(w * 0.4)} {f(by)} M{f(w * 0.6)} {f(h * 0.1)} L {f(w * 0.6)} {f(by)}" stroke="#E8D8B0" stroke-width="2"></path>')
    o.append(on_bed(p, w * 0.5, by, w * 0.26))
    o.append(jesus(p, w * 0.22, b, s, up=UP_BLESS))
    o.append(seated(w * 0.82, b, s * 0.8, "#3A4A6A", head="#3A4A6A", beard="#2A1A10", flip=True, band=True)
             + seated(w * 0.94, b, s * 0.78, "#E8E2D6", head="#F3EFE6", beard="#6A645E", flip=True, band=True))
    return "".join(o)

def heavens_rent(p, w, h, seed, dove_k=0.7):
    """He saw the heavens rent asunder, and the Spirit as a dove descending upon him: a dark sky torn open along a jagged
    seam, light pouring through it, a small dove of light coming down; Jesus coming up out of the Jordan, John in the water
    beside him (God is never drawn: the light only)."""
    r = random.Random(seed); b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#14123A", "#5A6AA8")]
    pts, x = [], w * 0.12
    while x < w * 0.9:
        pts.append((x, h * (0.12 + r.uniform(-0.04, 0.05)))); x += w * r.uniform(0.05, 0.09)
    up = " L ".join(f"{f(a)} {f(c - h * r.uniform(0.02, 0.06))}" for a, c in pts)
    dn = " L ".join(f"{f(a)} {f(c + h * r.uniform(0.02, 0.07))}" for a, c in reversed(pts))
    o.append(shaft(w * 0.5, w, h, top_w=0.26, bot_w=0.14, color="#FFF4C2", op=0.32))
    o.append(rays(w * 0.5, h * 0.12, 30, w * 0.1, h * 1.1, color="#FFF4C2", op=0.18, a0=10, a1=170))
    o.append(f'<path d="M{f(w * 0.06)} {f(h * 0.12)} L {up} L {f(w * 0.94)} {f(h * 0.12)} L {dn} Z" fill="#FFFDF0" stroke="#FFD23F" stroke-width="2.4"></path>')
    o.append(hills(w, h, h * 0.66, seed, color="#3A5A4A", amp=12, step=80))
    o.append(f'<path d="M-10 {f(h * 0.76)} C {f(w * 0.3)} {f(h * 0.72)} {f(w * 0.6)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.76)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2C6A98" stroke="{INK}" stroke-width="2"></path>')
    s = fit(b, max(h * 0.4, b - 220))
    o.append(jesus(p, w * 0.5, b, s))
    o.append(f'<rect x="{f(w * 0.5 - 50 * s)}" y="{f(b - 30 * s)}" width="{f(100 * s)}" height="{f(40 * s)}" fill="#2C6A98"></rect>'
             f'<path d="M{f(w * 0.5 - 50 * s)} {f(b - 30 * s)} q {f(25 * s)} -6 {f(50 * s)} 0 t {f(50 * s)} 0" stroke="#BFE6F2" stroke-width="3" fill="none"></path>')
    o.append(john_fig(p, w * 0.8, b + 40 * s, s * 0.8, flip=True, up=UP_BLESS))
    o.append(f'<rect x="{f(w * 0.66)}" y="{f(b - 6 * s)}" width="{f(w * 0.3)}" height="{f(h)}" fill="#2C6A98"></rect>')
    o.append(dove_light(w * 0.5, b - 220 * s - h * 0.08, max(0.4, h / 360) * dove_k, f"{p}dv"))
    return "".join(o)
