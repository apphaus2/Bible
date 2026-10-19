"""Drawings for the Haggai volume, on the minor prophets' kit (oba.minor), with Ezra's drawings of the house rebuilt
(ezr.art.altar_ruins, work_ceased): the ceiled houses beside the house lying waste, the bag with holes, wood brought down
from the mountain, the drought, the work begun again, the former glory as a ghost blueprint over the new walls, the
shaking of the nations, the measures that came to half, the foundation laid and the trees budding, the thrones
overthrown, and Zerubbabel's signet."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from oba.minor import *
from ezr.art import altar_ruins, work_ceased
from est.art import signet as ring
import samuel3 as S3

def ceiled_waste(w, h, seed):
    """Is it a time for you to dwell in your ceiled houses, while this house lieth waste? — on the left a room panelled in
    cedar, lamp-lit; on the right the temple mount, its stones scattered and grown over."""
    from genesis.art4 import clay_lamp
    o = [f'<svg x="0" y="0" width="{f(w * 0.48)}" height="{f(h)}" overflow="hidden">{S3.cedar(int(w * 0.48), h, h * 0.8)}'
         f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w * 0.5)}" height="{f(h * 0.3)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>'
         f'{clay_lamp(w * 0.24, h * 0.8, min(1.0, h / 300))}{halo(w * 0.24, h * 0.7, h * 0.3, "#FFC14D", 0.4)}</svg>',
         f'<g transform="translate({f(w * 0.48)} 0)">{sky(w * 0.52, h, "#8A8A9A", "#E8D8C0")}{ruin(w * 0.04, w * 0.5, h * 0.8, h * 0.3, seed, color="#C8BDA8")}'
         f'{ground(w * 0.52, h, h * 0.8, "#A89A80", dy=0)}{grain(0, w * 0.52, h * 0.98, h * 0.1, seed, color="#8A9A5A")}</g>',
         f'<path d="M{f(w * 0.48)} -10 L {f(w * 0.48)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="3"></path>']
    return "".join(o)

def bag_holes(w, h, seed):
    """Ye have sown much, and bring in little; he that earneth wages earneth wages to put it into a bag with holes: a purse
    with its coins falling through the bottom, a thin harvest sheaf beside an empty bowl."""
    o = [sky(w, h, "#C8A880", "#F3E8D0"), ground(w, h, h * 0.72, "#B8986A", dy=0), grain(-10, w * 0.4, h * 0.98, h * 0.12, seed, color="#A89A6A", n=10)]
    k = min(1.4, h / 240); x, y = w * 0.58, h * 0.5
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})"><path d="M-40 -40 C -60 -10 -50 40 0 44 C 50 40 60 -10 40 -40 Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<path d="M-40 -40 C -20 -50 20 -50 40 -40 L 30 -54 L -30 -54 Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></path>'
             '<circle cx="-10" cy="36" r="5" fill="#1A0E08"></circle><circle cx="14" cy="30" r="4" fill="#1A0E08"></circle></g>')
    r = random.Random(seed)
    for i in range(6):
        cx, cy = x + r.uniform(-20, 20) * k, y + (50 + i * 16) * k
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(6 * k)}" ry="{f(3 * k)}" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    o.append(f'<path d="M{f(w * 0.8)} {f(h * 0.9)} C {f(w * 0.8)} {f(h * 0.96)} {f(w * 0.94)} {f(h * 0.96)} {f(w * 0.94)} {f(h * 0.9)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def bring_wood(p, w, h, seed):
    """Go up to the mountain, and bring wood, and build the house: men carrying beams down a wooded mountain path."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.5)} {f(h * 0.08)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A7A4A" stroke="#0D0D0F" stroke-width="2.2"></path>']
    r = random.Random(seed)
    for i in range(10):
        o.append(tree(w * r.uniform(0.2, 0.9), h * r.uniform(0.3, 0.7), min(0.5, h / 600), color="#2E5A2E", kind="tall", seed=seed + i))
    o.append(route([(w * 0.62, h * 0.24), (w * 0.4, h * 0.56), (w * 0.2, h * 0.96)], color="#E8D8A8", dash="10 6", arrow=False))
    b = h * 0.96
    for i, (x, y) in enumerate(((0.26, 0.96), (0.38, 0.8))):
        yy = h * y; s = fit(yy, yy - h * 0.34)
        o.append(man(p, w * x, yy, s, ["#6A4A3A", "#3A4A6A"][i], up=[(22, -158), (30, -178), (24, -196)]))
        o.append(f'<path d="M{f(w * x - 70 * s)} {f(yy - 196 * s)} L {f(w * x + 70 * s)} {f(yy - 206 * s)}" stroke="#8A5A30" stroke-width="{f(14 * s)}" stroke-linecap="round"></path>')
    return "".join(o)

def drought(w, h, seed):
    """I called for a drought upon the land, upon the grain, the new wine and the oil: cracked earth under a white sun,
    withered stalks, a dry winepress, an empty oil jar."""
    r = random.Random(seed)
    o = [sky(w, h, "#F3E8C8", "#E8C890"), sun(w * 0.7, h * 0.18, max(16, h * 0.08), color="#FFF4C2", op=0.7), hills(w, h, h * 0.5, seed, color="#C8A070", amp=12),
         ground(w, h, h * 0.56, "#D8B07A", dy=0)]
    for i in range(30):
        x, y = r.uniform(0, w), r.uniform(h * 0.6, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-20, 20))} {f(r.uniform(4, 12))} l {f(r.uniform(-14, 14))} {f(r.uniform(4, 10))}" stroke="#8A6A3A" stroke-width="1.6" fill="none"></path>')
    o.append(grain(w * 0.04, w * 0.36, h * 0.9, h * 0.14, seed, color="#A89A6A", n=12))
    k = min(1.0, h / 300)
    o.append(f'<path d="M{f(w * 0.74 - 20 * k)} {f(h * 0.92)} C {f(w * 0.74 - 34 * k)} {f(h * 0.92 - 50 * k)} {f(w * 0.74 - 14 * k)} {f(h * 0.92 - 80 * k)} {f(w * 0.74)} {f(h * 0.92 - 84 * k)} C {f(w * 0.74 + 14 * k)} {f(h * 0.92 - 80 * k)} {f(w * 0.74 + 34 * k)} {f(h * 0.92 - 50 * k)} {f(w * 0.74 + 20 * k)} {f(h * 0.92)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2" transform="rotate(80 {f(w * 0.74)} {f(h * 0.92)})"></path>')
    return "".join(o)

def rebuild(p, w, h, seed):
    """They came and did work on the house of Jehovah of hosts: the walls of the house rising in courses, a scaffold, men
    setting stones and hauling on ropes."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.72, "#C8B88A", dy=0)]
    for row in range(6):
        for k in range(10 - row):
            x = w * (0.22 + k * 0.055) + row * w * 0.0275; y = h * (0.82 - row * 0.06)
            o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.053)}" height="{f(h * 0.058)}" fill="#D8CDB8" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    o.append(f'<path d="M{f(w * 0.2)} {f(h * 0.88)} L {f(w * 0.2)} {f(h * 0.3)} M{f(w * 0.82)} {f(h * 0.88)} L {f(w * 0.82)} {f(h * 0.3)} M{f(w * 0.18)} {f(h * 0.4)} L {f(w * 0.84)} {f(h * 0.4)} M{f(w * 0.18)} {f(h * 0.58)} L {f(w * 0.84)} {f(h * 0.58)}" stroke="#6A4A2A" stroke-width="4"></path>')
    s = fit(b, h * 0.5)
    o.append(man(p, w * 0.1, b, s, "#6A4A3A", up=[(22, -158), (40, -176), (58, -196)]) + man(p, w * 0.9, b, s, "#3A4A6A", flip=True)
             + man(p, w * 0.5, h * 0.4, fit(h * 0.4, h * 0.2), "#5A6A3A", up=[(22, -158), (40, -150), (56, -140)]))
    return "".join(o)

def former_glory(w, h, seed):
    """Who is left among you that saw this house in its former glory? is it not in your eyes as nothing? — the low new
    walls on the mount, and over them the outline of Solomon's house in a dashed gold line, as in a blueprint."""
    o = [sky(w, h, "#3A3A6A", "#D8B898"), ground(w, h, h * 0.8, "#A89A80", dy=0)]
    for row in range(2):
        for k in range(10):
            x = w * (0.22 + k * 0.056); y = h * (0.74 - row * 0.06)
            o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.054)}" height="{f(h * 0.058)}" fill="#D8CDB8" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    x0, x1, top = w * 0.2, w * 0.8, h * 0.08
    d = f"M{f(x0)} {f(h * 0.8)} L {f(x0)} {f(top + h * 0.2)} L {f(x0 + w * 0.12)} {f(top + h * 0.2)} L {f(x0 + w * 0.12)} {f(top)} L {f(x1 - w * 0.12)} {f(top)} L {f(x1 - w * 0.12)} {f(top + h * 0.2)} L {f(x1)} {f(top + h * 0.2)} L {f(x1)} {f(h * 0.8)}"
    o.append(f'<path d="{d}" stroke="#FFD23F" stroke-width="2.4" stroke-dasharray="10 6" fill="none" opacity="0.9"></path>'
             + "".join(f'<path d="M{f(x)} {f(top + h * 0.26)} L {f(x)} {f(h * 0.62)}" stroke="#FFD23F" stroke-width="2" stroke-dasharray="6 6" opacity="0.7"></path>' for x in (w * 0.44, w * 0.56))
             + label(w * 0.5, top - 6, "THE FORMER GLORY", "#FFD23F", 10) + label(w * 0.5, h * 0.94, "THIS HOUSE · NOW", "#F3EFE6", 10))
    return "".join(o)

def shaking(w, h, seed):
    """I will shake the heavens, and the earth, and the sea, and the dry land; the precious things of all nations shall
    come; I will fill this house with glory: lightning across the heavens, the sea heaving, and roads of gold flowing to the
    lit house on its mount."""
    o = [sky(w, h, "#14143A", "#5A4A7A"), bolt(w * 0.14, 0, h * 0.4, seed), bolt(w * 0.86, 0, h * 0.34, seed + 1),
         sea(w * 0.3, h, h * 0.62, seed, rough=True), halo(w * 0.6, h * 0.42, h * 0.4, "#FFE680", 0.6),
         mount_zion(w * 0.6, h * 0.86, w * 0.26, h * 0.5, seed, color="#6A5A6A", lit=True), ground(w, h, h * 0.86, "#3A2A3A", dy=0)]
    for side in (-1, 1):
        o.append(route([(w * 0.6 + side * w * 0.5, h * 0.98), (w * 0.6 + side * w * 0.2, h * 0.9), (w * 0.6 + side * w * 0.08, h * 0.84)], color="#FFD23F", sw=4, dash="4 6"))
    o.append(mk.speed(w * 0.6, h * 0.42, 26, h * 0.3, max(w, h) * 0.6, seed, color="#FFF4C2", op=0.25))
    return "".join(o)

def skirt_bread(w, h, seed):
    """If one bear holy flesh in the skirt of his garment, and with his skirt do touch bread, or pottage, or wine, or oil:
    the fold of a white garment just touching a loaf, a pot of pottage, a cup of wine and a jar of oil on a table."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A22"></rect>', halo(w * 0.5, h * 0.4, h * 0.6, "#FFC14D", 0.3),
         f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h * 0.08)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>']
    k = min(1.2, h / 260)
    o.append(f'<ellipse cx="{f(w * 0.3)}" cy="{f(h * 0.66)}" rx="{f(40 * k)}" ry="{f(16 * k)}" fill="#C8904A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<path d="M{f(w * 0.46 - 30 * k)} {f(h * 0.7)} C {f(w * 0.46 - 34 * k)} {f(h * 0.7 - 40 * k)} {f(w * 0.46 + 34 * k)} {f(h * 0.7 - 40 * k)} {f(w * 0.46 + 30 * k)} {f(h * 0.7)} Z" fill="#6A6A72" stroke="#0D0D0F" stroke-width="2"></path>'
             + cup(w * 0.62, h * 0.7, k * 0.5, color="#C8C8D0")
             + f'<path d="M{f(w * 0.76 - 12 * k)} {f(h * 0.7)} C {f(w * 0.76 - 22 * k)} {f(h * 0.7 - 40 * k)} {f(w * 0.76 - 6 * k)} {f(h * 0.7 - 60 * k)} {f(w * 0.76)} {f(h * 0.7 - 62 * k)} C {f(w * 0.76 + 6 * k)} {f(h * 0.7 - 60 * k)} {f(w * 0.76 + 22 * k)} {f(h * 0.7 - 40 * k)} {f(w * 0.76 + 12 * k)} {f(h * 0.7)} Z" fill="#C8A040" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.02)} {f(h * 0.1)} C {f(w * 0.2)} {f(h * 0.3)} {f(w * 0.24)} {f(h * 0.5)} {f(w * 0.28)} {f(h * 0.6)} C {f(w * 0.2)} {f(h * 0.62)} {f(w * 0.08)} {f(h * 0.5)} {f(w * -0.02)} {f(h * 0.44)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2.2"></path>')
    return "".join(o)

def measures(w, h, seed):
    """When one came to a heap of twenty measures, there were but ten; to the winevat for fifty vessels, but twenty; blasting,
    mildew and hail: a grain heap and a winevat with their tallies, hail falling."""
    import exodus2 as E2
    o = [sky(w, h, "#5A5A6A", "#C8B8A0"), ground(w, h, h * 0.64, "#A8906A", dy=0), E2.hail(30, 0, w, 0, h * 0.6, seed)]
    k = min(1.2, h / 260)
    o.append(f'<path d="M{f(w * 0.12)} {f(h * 0.92)} C {f(w * 0.16)} {f(h * 0.92 - 60 * k)} {f(w * 0.34)} {f(h * 0.92 - 60 * k)} {f(w * 0.38)} {f(h * 0.92)} Z" fill="#E8C060" stroke="#0D0D0F" stroke-width="2"></path>'
             + label(w * 0.25, h * 0.92 - 80 * k, "20 → 10", "#F3EFE6", 12))
    o.append(f'<rect x="{f(w * 0.56)}" y="{f(h * 0.92 - 50 * k)}" width="{f(w * 0.3)}" height="{f(50 * k)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.58)}" y="{f(h * 0.92 - 20 * k)}" width="{f(w * 0.26)}" height="{f(16 * k)}" fill="#5A1A3A"></rect>'
             + label(w * 0.71, h * 0.92 - 70 * k, "50 → 20", "#F3EFE6", 12))
    return "".join(o)

def foundation_bless(w, h, seed):
    """Since the day that the foundation of Jehovah's temple was laid — the vine, the fig-tree, the pomegranate and the
    olive-tree; from this day will I bless you: the foundation stone in the morning light, the trees about it in fresh leaf."""
    o = [sky(w, h, "#5A7AB8", "#FFE6A0"), sun(w * 0.5, h * 0.4, max(16, h * 0.06), color="#FFE680", op=0.5), hills(w, h, h * 0.58, seed, color="#7A9A5A", amp=12),
         ground(w, h, h * 0.66, "#B8B07A", dy=0), vines(w * 0.04, w * 0.3, h * 0.84, h * 0.9, seed, rows=2),
         fig_tree(w * 0.38, h * 0.96, min(0.8, h / 360), seed=seed), olive(w * 0.88, h * 0.96, min(0.8, h / 360), seed + 1)]
    r = random.Random(seed); k = min(1.0, h / 300)
    o.append(tree(w * 0.72, h * 0.96, k * 0.7, color="#3F7A34", seed=seed + 2)
             + "".join(f'<circle cx="{f(w * 0.72 + r.uniform(-30, 30) * k)}" cy="{f(h * 0.96 - r.uniform(70, 110) * k)}" r="{f(5 * k)}" fill="#C8202A" stroke="#0D0D0F" stroke-width="1"></circle>' for _ in range(5)))
    o.append(f'<rect x="{f(w * 0.46)}" y="{f(h * 0.8)}" width="{f(w * 0.16)}" height="{f(h * 0.12)}" fill="#E8DCC8" stroke="#0D0D0F" stroke-width="2.2"></rect>'
             + halo(w * 0.54, h * 0.86, h * 0.16, "#FFF4C2", 0.5))
    return "".join(o)

def overthrow(w, h, seed):
    """I will overthrow the throne of kingdoms; I will overthrow the chariots, and those that ride in them: a throne thrown
    down on its side, a chariot's broken wheel, under a storm — the heavens and the earth shaken."""
    o = [sky(w, h, "#14141E", "#5A4A5A"), bolt(w * 0.5, 0, h * 0.5, seed), ground(w, h, h * 0.7, "#3A3030", dy=0)]
    k = min(1.0, h / 300)
    o.append(f'<g transform="rotate(-80 {f(w * 0.3)} {f(h * 0.92)})">{S3.throne(w * 0.3, h * 0.92, k * 0.8)}</g>')
    cx, cy, rr = w * 0.7, h * 0.84, 40 * k
    o.append(f'<g transform="rotate(30 {f(cx)} {f(cy)})"><circle cx="{f(cx)}" cy="{f(cy)}" r="{f(rr)}" fill="none" stroke="#6A4A2A" stroke-width="{f(7 * k)}"></circle>'
             + "".join(f'<path d="M{f(cx)} {f(cy)} L {f(cx + rr * math.cos(a))} {f(cy + rr * math.sin(a))}" stroke="#6A4A2A" stroke-width="{f(4 * k)}"></path>' for a in (0.3, 1.5, 2.6, 3.8)) + '</g>')
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.96)} L {f(w * 0.9)} {f(h * 0.9)}" stroke="#6A4A2A" stroke-width="{f(8 * k)}" stroke-linecap="round"></path>')
    return "".join(o)

def signet_plate(w, h, seed):
    """I will take thee, O Zerubbabel, my servant, and will make thee as a signet; for I have chosen thee: the gold signet
    ring glowing on a dark field, its seal pressed in clay beside it."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12113A"></rect>', halo(w * 0.42, h * 0.56, h * 0.5, "#FFD23F", 0.5),
         rays(w * 0.42, h * 0.56, 24, h * 0.24, h * 0.6, "#FFE680", 0.3, 3)]
    k = min(2.2, h / 130)
    o.append(ring(w * 0.42, h * 0.62, k))
    o.append(f'<ellipse cx="{f(w * 0.76)}" cy="{f(h * 0.74)}" rx="{f(44 * k)}" ry="{f(30 * k)}" fill="#A8603A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<path d="M{f(w * 0.76 - 14 * k)} {f(h * 0.74 - 8 * k)} L {f(w * 0.76)} {f(h * 0.74 + 4 * k)} L {f(w * 0.76 + 14 * k)} {f(h * 0.74 - 8 * k)} M{f(w * 0.76 - 10 * k)} {f(h * 0.74 + 10 * k)} L {f(w * 0.76 + 10 * k)} {f(h * 0.74 + 10 * k)}" stroke="#5A2A12" stroke-width="{f(3 * k)}" fill="none"></path>')
    return "".join(o)
