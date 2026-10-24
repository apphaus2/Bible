"""Drawings for Acts 5–6. Ananias and Sapphira are told in words only: the empty floor before the apostles, the purse
lying where it was laid down, the open door and the bright street beyond it, and later the door shut. The sick laid in the
streets on beds and couches as Peter came by, his shadow long before him in the morning sun; the multitudes from the
cities bringing their sick. The public ward; the prison doors opened by night by an angel of the Lord (white light, a gold
rim, no face); the prison-house found shut in all safety, the keepers at the doors and no man within. The beating of the
apostles (5:40) is told in words only over the council's shut door. The daily ministration and the widows; the seven set
before the apostles and the hands laid on them; Stephen disputing in the synagogue of the Libertines; Stephen seized and
brought into the council. Built on act.art2."""
from act.art2 import *
from act.art2 import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue
import random, math
from ecc.art import loaf

def empty_floor(p, w, h, seed, purse=True, door="open"):
    """Where Ananias stood: the stone floor of the porch empty before the apostles' feet, the purse lying on it, and beyond
    the columns a doorway — door="open" the bright street, "shut" the door closed. No one is drawn."""
    b = h * 0.94
    o = [bgr(w, h, "#5A4A44"), f'<rect x="-10" y="{f(h * 0.06)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#3A2A22" stroke="{INK}" stroke-width="2"></rect>']
    for x in (0.08, 0.92):
        o.append(f'<rect x="{f(w * x - 20)}" y="{f(h * 0.12)}" width="40" height="{f(b - h * 0.12)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    dx, dw = w * 0.42, w * 0.18
    if door == "open":
        o.append(f'<rect x="{f(dx)}" y="{f(h * 0.2)}" width="{f(dw)}" height="{f(h * 0.5)}" fill="#FFE6A0" stroke="{INK}" stroke-width="2.4"></rect>'
                 f'<path d="M{f(dx)} {f(h * 0.2)} L {f(dx - dw * 0.4)} {f(h * 0.24)} L {f(dx - dw * 0.4)} {f(h * 0.74)} L {f(dx)} {f(h * 0.7)} Z" fill="#5A3A22" stroke="{INK}" stroke-width="2"></path>'
                 f'<path d="M{f(dx)} {f(h * 0.7)} L {f(dx + dw)} {f(h * 0.7)} L {f(dx + dw * 1.6)} {f(b)} L {f(dx - dw * 0.6)} {f(b)} Z" fill="#FFE680" opacity="0.25"></path>')
    else:
        o.append(f'<rect x="{f(dx)}" y="{f(h * 0.2)}" width="{f(dw)}" height="{f(h * 0.5)}" fill="#5A3A22" stroke="{INK}" stroke-width="2.4"></rect>'
                 f'<path d="M{f(dx + dw / 2)} {f(h * 0.2)} L {f(dx + dw / 2)} {f(h * 0.7)}" stroke="#2A1A10" stroke-width="2"></path>'
                 f'<rect x="{f(dx)}" y="{f(h * 0.7 - 3)}" width="{f(dw)}" height="4" fill="#FFC14D"></rect>')
    o.append(pavement(w, h, h * 0.7, color="#8A7A6A", line="#6A5A4A"))
    if purse:
        k = max(0.6, h / 300)
        cx, cy = w * 0.3, b - 10 * k
        o.append(f'<path d="M{f(cx - 20 * k)} {f(cy)} C {f(cx - 26 * k)} {f(cy - 26 * k)} {f(cx - 4 * k)} {f(cy - 30 * k)} {f(cx)} {f(cy - 36 * k)} L {f(cx + 6 * k)} {f(cy - 36 * k)} C {f(cx + 8 * k)} {f(cy - 30 * k)} {f(cx + 30 * k)} {f(cy - 26 * k)} {f(cx + 22 * k)} {f(cy)} Z" fill="#8A5A2A" stroke="{INK}" stroke-width="2"></path>')
        for j in range(4):
            o.append(f'<ellipse cx="{f(cx + (30 + 12 * j) * k)}" cy="{f(cy + 4 * k)}" rx="{f(6 * k)}" ry="{f(3 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="1"></ellipse>')
    return "".join(o)

def shadow_street(p, w, h, seed):
    """They carried out the sick into the streets on beds and couches, that as Peter came by at the least his shadow might
    overshadow some one of them: the street in the low morning sun, the beds along it, Peter walking with John, his long
    shadow falling across the first of them."""
    bg, b = _street(w, h, seed, "dawn")
    o = [mk.defs(p, *ALL, *LIE), bg, sun(w * 0.06, h * 0.36, 18, color="#FFE680", op=0.5)]
    s = fit(b, max(h * 0.28, b - 210))
    px = w * 0.24
    o.append(f'<path d="M{f(px)} {f(b)} L {f(px + 30 * s)} {f(b)} L {f(w * 0.74)} {f(b - 12 * s)} L {f(w * 0.7)} {f(b - 26 * s)} Z" fill="#2A2A3A" opacity="0.45"></path>')
    for i, x in enumerate((0.44, 0.66, 0.88)):
        o.append(on_bed(p, w * x, b - 22 * s - i * 2, 170 * s * 0.9, cloth=["#C8B898", "#8A9AAA", "#B89A7A"][i], flip=i % 2 == 1))
    o.append(peter(p, px, b, s) + john_ap(p, px - 80 * s, b, s * 0.96))
    o.append(woman_fig(p, w * 0.56, b - 70 * s, s * 0.7, "#6A4A5A", "#3A3A5A", flip=True) + man_fig(p, w * 0.8, b - 70 * s, s * 0.7, "#5A6A3A", head="#6A5A3A", bd="#2A1A10", flip=True))
    return "".join(o)

def bringing_sick(p, w, h, seed):
    """The multitude from the cities round about Jerusalem, bringing sick folk: the road from the hill-towns, men carrying a
    sick man on a litter, a lame man on a staff, a mother with her child, all coming toward the city."""
    o = [mk.defs(p, *ALL, *LIE), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.42, seed, color="#9A9A7A", amp=14, step=90)]
    for i, x in enumerate((0.16, 0.5, 0.84)):
        o.append(hill_town(w * x, h * 0.5, w * 0.12, h * 0.1, seed + i, hill="#A8A87A"))
    o.append(ground(w, h, h * 0.52, "#C8B07A", dy=0))
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.52)} C {f(w * 0.46)} {f(h * 0.7)} {f(w * 0.3)} {f(h * 0.86)} {f(w * 0.1)} {f(h + 10)}" stroke="#E0D0A8" stroke-width="{f(max(10, h * 0.08))}" fill="none"></path>')
    b = h * 0.94
    s = fit(b, max(h * 0.3, b - 210))
    x0 = w * 0.42
    o.append(man_fig(p, x0 - 60 * s, b, s, "#6A4A3A", head="#E8E2D6", bd="#2A1A10", kind="Tunic", flip=True) + man_fig(p, x0 + 120 * s, b, s, "#3A4A6A", head="#6A5A3A", bd="#3A2A1A", kind="Tunic"))
    o.append(bedroll(x0 + 30 * s, b - 110 * s, 230 * s, 12 * s) + lying(p, x0 + 60 * s, b - 108 * s, s * 0.9, cloth="#C8B898"))
    o.append(man_fig(p, w * 0.72, b, s * 0.94, "#7A7A80", hr="#6A645E", bd="#6A645E", flip=True, extra='<path d="M-30 -150 L -40 0" stroke="#5A3A22" stroke-width="5"></path>'))
    o.append(woman_fig(p, w * 0.86, b, s * 0.9, "#5A6A4A", "#2A4A5A", flip=True))
    return "".join(o)

def hill_town(x, base, wd, ht, seed, hill="#7A6A4A"):
    from mat.art import hill_town as _ht
    return _ht(x, base, wd, ht, seed, hill=hill)

def prison_opened(p, w, h, seed):
    """An angel of the Lord by night opened the prison doors and brought them out: the prison wall at night, the iron-bound
    door standing open, a figure of white light with a gold rim in the doorway (no face), the apostles coming out after."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1E1650"), mk.stars(40, w, h * 0.3, seed),
         f'<rect x="-10" y="{f(h * 0.16)}" width="{f(w + 20)}" height="{f(b - h * 0.16)}" fill="#4A4248" stroke="{INK}" stroke-width="2"></rect>']
    for k in range(8):
        y = h * 0.16 + (b - h * 0.16) * k / 8
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#3A3238" stroke-width="2"></path>')
    dx, dw = w * 0.36, w * 0.2
    o.append(glow(dx + dw / 2, b - h * 0.2, h * 0.5, "#FFF4C2", 0.8, f"{p}g"))
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.3)}" width="{f(dw)}" height="{f(b - h * 0.3)}" fill="#FFF4C2" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(dx)} {f(h * 0.3)} L {f(dx - dw * 0.5)} {f(h * 0.34)} L {f(dx - dw * 0.5)} {f(b + 4)} L {f(dx)} {f(b)} Z" fill="#3A3A44" stroke="{INK}" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(dx - dw * 0.5)} {f(h * 0.3 + (b - h * 0.3) * k / 4)} L {f(dx)} {f(h * 0.3 + (b - h * 0.3) * k / 4 - 4)}" stroke="#1A1A20" stroke-width="3"></path>' for k in (1, 2, 3)))
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2228" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.28, b - 210))
    o.append(angel(p, dx + dw / 2, b, s, flip=True, up=UP_BLESS))
    for i in range(4):
        o.append(apostle(p, w * (0.66 + 0.09 * i), b, s * (0.98 - 0.02 * i), i))
    return "".join(o)

def prison_found(p, w, h, seed):
    """The prison-house we found shut in all safety, and the keepers standing at the doors: but when we had opened, we found
    no man within — the open cell empty, the straw and the loosed chains; the keepers standing either side of the door."""
    bg, b = _prison(w, h, seed)
    o = [mk.defs(p, *ALL), bg, f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#FFE6A0" opacity="0.08"></rect>']
    s = fit(b, max(h * 0.28, b - 210))
    k = s
    for x in (0.4, 0.56):
        o.append(f'<path d="M{f(w * x)} {f(b - 4)} C {f(w * x + 10 * k)} {f(b - 30 * k)} {f(w * x + 30 * k)} {f(b - 30 * k)} {f(w * x + 40 * k)} {f(b - 4)}" stroke="#8A8A90" stroke-width="{f(4 * k)}" fill="none" stroke-dasharray="{f(6 * k)} {f(3 * k)}"></path>')
    o.append(f'<path d="M{f(w * 0.3)} {f(b)} L {f(w * 0.7)} {f(b)} L {f(w * 0.66)} {f(b - 8 * k)} L {f(w * 0.34)} {f(b - 8 * k)} Z" fill="#C8A860" opacity="0.7"></path>')
    o.append(officer(p, w * 0.12, b, s, flip=True) + officer(p, w * 0.88, b, s))
    return "".join(o)

def council_door(p, w, h, seed):
    """The door of the council-chamber shut — what was done within (the apostles beaten) is told in words only: the great
    door barred, lamplight under it, the stone wall of the court."""
    o = [bgr(w, h, "#3A3038")]
    for k in range(9):
        y = h * k / 8
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#2A2228" stroke-width="2"></path>')
    b = h * 0.94
    o.append(f'<path d="M{f(w * 0.3)} {f(b)} L {f(w * 0.3)} {f(h * 0.26)} Q {f(w * 0.5)} {f(h * 0.06)} {f(w * 0.7)} {f(h * 0.26)} L {f(w * 0.7)} {f(b)} Z" fill="#5A3A22" stroke="{INK}" stroke-width="3"></path>'
             f'<path d="M{f(w * 0.5)} {f(h * 0.16)} L {f(w * 0.5)} {f(b)}" stroke="#2A1A10" stroke-width="3"></path>'
             f'<path d="M{f(w * 0.26)} {f(h * 0.56)} L {f(w * 0.74)} {f(h * 0.56)}" stroke="#2A1A10" stroke-width="12"></path>'
             f'<rect x="{f(w * 0.3)}" y="{f(b - 4)}" width="{f(w * 0.4)}" height="6" fill="#FFC14D"></rect>'
             f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#1E1A20"></rect>')
    o.append(A.lamp(w * 0.16, h * 0.4, max(0.6, h / 360)) + A.lamp(w * 0.84, h * 0.4, max(0.6, h / 360)))
    return "".join(o)

def ministration(p, w, h, seed):
    """The daily ministration: a table of loaves in the court, widows of the Hebrews receiving their portion at it, the
    Grecian widows standing aside, passed over, and the Grecian Jews murmuring."""
    bg, b = _porch(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.34, b - 200))
    ty = b - 60 * s
    o.append(f'<rect x="{f(w * 0.04)}" y="{f(ty)}" width="{f(w * 0.26)}" height="{f(14 * s)}" fill="#7A4A2A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.06)} {f(ty + 14 * s)} L {f(w * 0.06)} {f(b)} M{f(w * 0.28)} {f(ty + 14 * s)} L {f(w * 0.28)} {f(b)}" stroke="#5A3A1E" stroke-width="{f(6 * s)}"></path>')
    for x in (0.08, 0.14, 0.2, 0.26):
        o.append(loaf(w * x, ty - 1, s * 0.6))
    for i, x in enumerate((0.36, 0.46)):
        o.append(woman_fig(p, w * x, b, s * 0.92, ["#4A4A5A", "#5A4A3A"][i], ["#2A2A3A", "#3A3030"][i], up=UP_TOUCH if i == 0 else None))
    for i, x in enumerate((0.6, 0.68)):
        o.append(woman_fig(p, w * x, b, s * 0.9, ["#6A6A7A", "#5A5A6A"][i], ["#8A8A9A", "#7A7A8A"][i], flip=True))
    o.append(man_fig(p, w * 0.8, b, s, "#1F5A6A", head="#F3EFE6", cord="#1F5FAD", hr="#2A1A10", bd="#2A1A10", up=UP_BLESS)
             + man_fig(p, w * 0.9, b, s * 0.98, "#8A6A2A", head="#E8E2D6", bd="#6A645E", flip=True))
    return "".join(o)

SEVEN = ["#2A6A5A", "#2A6A6A", "#6A5A7A", "#8A6A4A", "#4A6A8A", "#7A4A3A", "#5A6A3A"]
def seven(p, w, h, seed, hands=False):
    """The seven set before the apostles — Stephen (sea-green, bareheaded) first and Philip (teal headcloth) — standing in a
    row; hands=True the apostles laying their hands upon them as they kneel."""
    bg, b = _porch(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.28, b - 210))
    if not hands:
        for i in range(7):
            x = w * (0.08 + 0.12 * i)
            if i == 0: o.append(stephen(p, x, b, s))
            elif i == 1: o.append(philip_ev(p, x, b, s))
            else: o.append(man_fig(p, x, b, s * (0.97 + 0.03 * (i % 2)), SEVEN[i], head=SEVEN[i] if i % 2 else None, hr="#2A1A10", bd=["#2A1A10", "#4A3A2A", "#1A1210"][i % 3]))
    else:
        for i in range(4):
            x = w * (0.18 + 0.2 * i)
            o.append(E.kneel(x, b, s * 0.82, color=SEVEN[i], skin=SKIN))
            o.append(apostle(p, x + 70 * s, b, s, i, up=[(-22, -158), (-44, -150), (-60, -134)]))
    return "".join(o)

def disputing(p, w, h, seed):
    """The synagogue of the Libertines: Stephen standing among the benches, his hand lifted, the men of Cyrene, Alexandria,
    Cilicia and Asia standing against him, disputing."""
    bg, b = _synagogue(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.28, b - 210))
    o.append(stephen(p, w * 0.24, b, s, flip=True, up=UP_BLESS))
    o.append(seated(w * 0.08, b, s * 0.8, "#6A5A3A", head="#E8E2D6", beard="#6A645E"))
    for i, (x, c, hd) in enumerate(((0.5, "#1F5A6A", "#F3EFE6"), (0.6, "#8A6A2A", "#E8E2D6"), (0.7, "#5A2A4A", "#2A2A3A"), (0.8, "#2A4A2A", "#C8B080"), (0.9, "#6A2A2A", "#3A4A6A"))):
        o.append(man_fig(p, w * x, b, s * (1 - 0.02 * (i % 2)), c, head=hd, bd=["#2A1A10", "#6A645E"][i % 2], up=UP_BLESS if i in (0, 3) else None))
    return "".join(o)

def seized(p, w, h, seed):
    """They came upon him and brought him into the council: the street before the council-house, Stephen walking in the
    midst of the elders and scribes, the officers on either side — no blow drawn."""
    bg, b = _street(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.28, b - 210))
    o.append(officer(p, w * 0.12, b, s) + elder(p, w * 0.24, b, s) + stephen(p, w * 0.4, b, s) + officer(p, w * 0.52, b, s))
    o.append(scribe(p, w * 0.66, b, s * 0.98) + priest(p, w * 0.76, b, s * 0.98))
    o.append(crowd(p, w * 0.84, w * 0.98, b, b - 180 * s, 2, seed, flip=True))
    return "".join(o)
