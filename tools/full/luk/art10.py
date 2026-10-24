"""Drawings for Luke 16–17: the unrighteous steward called to account, and the debtors rewriting their bonds; the rich man
and Lazarus — the rich man's gate with the feast lit within, Lazarus laid at the gate in a torn tunic with the dogs (no
sores drawn); carried away by the angels (figures of white light, no faces); the rich man's shut tomb; Hades only as
darkness and smoke, the great gulf fixed, and far across it Abraham's bosom as light (no one drawn in torment, no figure in
the light); the sycamine tree rooted up and planted in the sea; the servant come in from the plow, serving at the table; the
ten lepers standing afar off, going, and the one Samaritan turned back at his feet. Built on luk.art9."""
from luk.art9 import *
from luk.art9 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch, \
    jesus_kneel, light_seated, WOMEN3, PURPLE, GOLD, kneel_w, boy_fig, zach_fig, elis_fig, shepherd_fig, swaddled, fish_heap, WIDOW_C, WIDOW_V, SINNER_C, SINNER_V, \
    JOANNA, SUSANNA, SAMARITAN_C, samaritan_fig, priest_fig, levite_fig, RICH_C, rich_fig, barn, son_fig, father_fig, elder_fig, farm
import random, math
from oba.minor import smokes

LAZ_C = "#7A7A7E"

def steward_bonds(p, w, h, seed, stage="called"):
    """The rich man and his steward: stage='called' the lord seated in his hall, the steward standing before him holding the
    account-roll; 'bonds' the steward at a table with the debtors, a jar of oil and a sack of wheat by them, each writing
    on his bond."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#A88A6A", window=(w * 0.84, w * 0.08)), A.lamp(w * 0.5, h * 0.24, max(0.6, h / 300))]
    s = fit(b, max(h * 0.2, b - 230))
    if stage == "called":
        o.append(f'<rect x="{f(w * 0.08)}" y="{f(b - 120 * s)}" width="{f(80 * s)}" height="{f(120 * s)}" fill="#8A5A2A" stroke="{INK}" stroke-width="2"></rect>')
        o.append(seated(w * 0.12, b - 40 * s, s * 0.84, RICH_C, head="#6A2A6A", beard="#2A1A10", band=True))
        o.append(man(p, w * 0.46, b, s, "#6A5A3A", flip=False, up=[(-22, -158), (-40, -140), (-54, -136)], extra=A.headcloth("#5A4A3A")))
        o.append(f'<rect x="{f(w * 0.46 - 60 * s)}" y="{f(b - 150 * s)}" width="{f(12 * s)}" height="{f(30 * s)}" rx="4" fill="#E8D8B0" stroke="{INK}" stroke-width="1.6"></rect>')
    else:
        o.append(f'<rect x="{f(w * 0.24)}" y="{f(b - 40 * s)}" width="{f(w * 0.4)}" height="{f(14 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
        for i in range(2):
            o.append(f'<rect x="{f(w * (0.32 + 0.16 * i))}" y="{f(b - 48 * s)}" width="{f(30 * s)}" height="{f(8 * s)}" fill="#E8D8B0" stroke="{INK}" stroke-width="1.2"></rect>')
        o.append(seated(w * 0.24, b, s * 0.8, "#6A5A3A", head="#5A4A3A", beard="#2A1A10"))
        o.append(seated(w * 0.66, b, s * 0.78, HEB[2], head=HEB[2], beard="#2A1A10", flip=True) + seated(w * 0.8, b, s * 0.78, HEB[4], head=HEB[4], beard="#6A645E", flip=True))
        o.append(f'<path d="M{f(w * 0.9)} {f(b)} C {f(w * 0.88)} {f(b - 40 * s)} {f(w * 0.9)} {f(b - 70 * s)} {f(w * 0.92)} {f(b - 72 * s)} C {f(w * 0.94)} {f(b - 70 * s)} {f(w * 0.96)} {f(b - 40 * s)} {f(w * 0.94)} {f(b)} Z" fill="#C8783A" stroke="{INK}" stroke-width="2"></path>'
                 f'<path d="M{f(w * 0.02)} {f(b)} C {f(w * 0.0)} {f(b - 50 * s)} {f(w * 0.12)} {f(b - 60 * s)} {f(w * 0.12)} {f(b)} Z" fill="#C8A878" stroke="{INK}" stroke-width="2"></path>')
    return "".join(o)

def rich_gate(p, w, h, seed, stage="gate"):
    """A certain rich man clothed in purple and fine linen, and a beggar named Lazarus laid at his gate: stage='gate' the
    great house lit within, the feast glimpsed through its door, the rich man at the table in purple; at the gate Lazarus
    sitting in a torn grey tunic, the dogs come to him (the sores told in words only); 'carried' the gate empty at night and
    above it two angels of white light bearing Lazarus up, wrapped in white, toward a light far off; 'buried' the same house
    at evening and beside it the rich man's tomb, its stone rolled to the door."""
    b = h * 0.92
    night_ = stage == "carried"
    o = [mk.defs(p, *ALL), night(w, h, seed, n=60) if night_ else sky(w, h, "#5A4A7A", "#FFB07A") if stage == "buried" else sky(w, h, "#8FD0E2", "#F3E8C8")]
    hx0, hx1, top = w * 0.36, w * 1.02, h * 0.18
    o.append(f'<rect x="{f(hx0)}" y="{f(top)}" width="{f(hx1 - hx0)}" height="{f(b - top)}" fill="{"#4A4058" if night_ else "#E8DCC0"}" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(hx0 - 6)}" y="{f(top - 10)}" width="{f(hx1 - hx0 + 12)}" height="12" fill="{GOLD}" stroke="{INK}" stroke-width="2"></rect>')
    for x in (0.42, 0.98):
        o.append(f'<rect x="{f(w * x - 10)}" y="{f(top)}" width="20" height="{f(b - top)}" fill="{"#5A5068" if night_ else "#F3EFE6"}" stroke="{INK}" stroke-width="1.8"></rect>')
    dx0, dx1 = w * 0.54, w * 0.86
    o.append(f'<rect x="{f(dx0)}" y="{f(b - h * 0.5)}" width="{f(dx1 - dx0)}" height="{f(h * 0.5)}" fill="{"#2A2030" if stage != "gate" else "#FFC14D"}" stroke="{INK}" stroke-width="2"></rect>')
    o.append(ground(w, h, b, "#2A2438" if night_ else "#B8A06A", dy=0))
    s = fit(b, max(h * 0.2, b - 230))
    if stage == "gate":
        o.append(f'<rect x="{f(dx0 + 10)}" y="{f(b - 40 * s)}" width="{f(dx1 - dx0 - 20)}" height="{f(10 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="1.6"></rect>'
                 + seated(w * 0.7, b - 4, s * 0.7, RICH_C, head="#6A2A6A", beard="#2A1A10", band=True)
                 + seated(w * 0.8, b - 4, s * 0.66, "#E8E2D6", head="#F3EFE6", beard="#6A645E", flip=True))
        o.append(seated(w * 0.2, b, s * 0.82, LAZ_C, head=None, beard="#3A2A1A", bowed=True))
        for i, x in enumerate((0.06, 0.32)):
            o.append(f'<g transform="translate({f(w * x)} {f(b)}) scale({f(s * 0.5 * (1 if i else -1))} {f(s * 0.5)})">'
                     '<path d="M-50 0 L -46 -36 C -40 -52 20 -54 34 -40 L 52 -58 L 62 -54 L 56 -34 L 48 -26 L 46 0 L 38 0 L 36 -20 L -30 -20 L -36 0 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>'
                     '<path d="M-46 -30 C -60 -36 -66 -52 -60 -60" stroke="#8A6A4A" stroke-width="6" fill="none"></path></g>')
    elif stage == "carried":
        o.append(glow(w * 0.24, h * 0.1, h * 0.3, "#FFF4C2", 0.8, f"{p}g"))
        sa = max(0.22, h / 1100)
        o.append(angel(p, w * 0.14, h * 0.6, sa, up=[(-22, -158), (-46, -150), (-62, -140)], flip=True) + angel(p, w * 0.32, h * 0.58, sa, up=[(-22, -158), (-46, -150), (-62, -140)]))
        o.append(f'<path d="M{f(w * 0.17)} {f(h * 0.6 - 140 * sa)} C {f(w * 0.2)} {f(h * 0.6 - 170 * sa)} {f(w * 0.27)} {f(h * 0.6 - 170 * sa)} {f(w * 0.29)} {f(h * 0.6 - 140 * sa)} Z" fill="#FFFDF0" stroke="#E8B830" stroke-width="2"></path>')
    else:
        tx = w * 0.16
        o.append(f'<path d="M{f(tx - w * 0.14)} {f(b)} L {f(tx - w * 0.14)} {f(b - h * 0.32)} C {f(tx - w * 0.1)} {f(b - h * 0.42)} {f(tx + w * 0.1)} {f(b - h * 0.42)} {f(tx + w * 0.14)} {f(b - h * 0.32)} L {f(tx + w * 0.14)} {f(b)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>'
                 f'<circle cx="{f(tx)}" cy="{f(b - h * 0.13)}" r="{f(h * 0.13)}" fill="#A89A8A" stroke="{INK}" stroke-width="2.4"></circle>')
    return "".join(o)

def gulf(p, w, h, seed):
    """Hades and Abraham's bosom, and between them a great gulf fixed: on the near side darkness and drifting smoke with a
    dull red glow far down (no one drawn in torment); a chasm of black plunging between; far across, on the height, a field
    of warm light (no figure drawn in it)."""
    r = random.Random(seed)
    o = [bgr(w, h, "#0A0608"), glow(w * 0.8, h * 0.28, h * 0.5, "#FFF4C2", 0.85, f"{p}l"), glow(w * 0.78, h * 0.26, h * 0.22, "#FFFFFF", 0.7, f"{p}l2"),
         f'<path d="M{f(w * 0.6)} {f(h + 10)} L {f(w * 0.62)} {f(h * 0.5)} C {f(w * 0.7)} {f(h * 0.44)} {f(w * 0.9)} {f(h * 0.42)} {f(w + 10)} {f(h * 0.44)} L {f(w + 10)} {f(h + 10)} Z" fill="#C8A86A" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.56)} C {f(w * 0.14)} {f(h * 0.52)} {f(w * 0.32)} {f(h * 0.54)} {f(w * 0.4)} {f(h * 0.58)} L {f(w * 0.44)} {f(h + 10)} Z" fill="#2A1A1A" stroke="{INK}" stroke-width="2"></path>',
         glow(w * 0.18, h * 0.96, h * 0.3, "#8A1A10", 0.6, f"{p}d")]
    o.append(smokes([w * r.uniform(0.02, 0.36) for _ in range(5)], h * 0.6, seed, k=max(0.6, h / 300), color="#3A2A2E", op=0.6))
    for k in range(5):
        x = w * (0.46 + 0.03 * k)
        o.append(f'<path d="M{f(x)} {f(h * 0.6)} L {f(x + 4)} {f(h + 10)}" stroke="#050304" stroke-width="10"></path>')
    return "".join(o)

def sycamine(p, w, h, seed, uprooted=False):
    """Ye would say unto this sycamine tree, Be thou rooted up, and be thou planted in the sea: a great broad sycamine tree on
    the shore of the sea; uprooted=True: the tree lifted with its roots out of the earth, standing in the sea."""
    b = h * 0.92
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), lake(w, h, h * 0.56, seed), shore(w, h, h * 0.78, x0=-10, x1=w * 0.5)]
    k = max(0.5, h / 300)
    tx, ty = (w * 0.72, h * 0.66) if uprooted else (w * 0.26, h * 0.86)
    o.append(tree(tx, ty, k, color="#3F7A34", kind="round", seed=seed))
    if uprooted:
        o.append("".join(f'<path d="M{f(tx)} {f(ty)} C {f(tx + dx * 0.4 * k)} {f(ty + 10 * k)} {f(tx + dx * k)} {f(ty + 18 * k)} {f(tx + dx * 1.2 * k)} {f(ty + 30 * k)}" stroke="#6A4A2A" stroke-width="{f(4 * k)}" fill="none"></path>' for dx in (-30, -12, 10, 28)))
        o.append(f'<path d="M{f(tx - 50 * k)} {f(ty + 20 * k)} q {f(25 * k)} -6 {f(50 * k)} 0 t {f(50 * k)} 0" stroke="#E8F6FA" stroke-width="3" fill="none"></path>')
    return "".join(o)

def plowman_serves(p, w, h, seed):
    """Make ready wherewith I may sup, and gird thyself, and serve me: the house at evening, the master seated at the table,
    the servant girded, come in from the field, setting the dish before him; the plow leaning by the door."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#A88A6A"), A.lamp(w * 0.5, h * 0.24, max(0.6, h / 300)),
         f'<path d="M{f(w * 0.9)} {f(b)} L {f(w * 0.84)} {f(b - h * 0.4)}" stroke="#5A3A1E" stroke-width="5"></path><path d="M{f(w * 0.9)} {f(b)} L {f(w * 0.96)} {f(b - h * 0.06)}" stroke="#5A3A1E" stroke-width="5"></path>']
    s = fit(b, max(h * 0.2, b - 230))
    o.append(f'<rect x="{f(w * 0.14)}" y="{f(b - 40 * s)}" width="{f(w * 0.3)}" height="{f(14 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>' + loaf(w * 0.22, b - 44 * s, s * 0.6))
    o.append(seated(w * 0.14, b, s * 0.82, "#5A3A5A", head="#5A3A5A", beard="#2A1A10", band=True))
    dish = '<ellipse cx="-62" cy="-140" rx="18" ry="5" fill="#C8A060" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
    o.append(man(p, w * 0.56, b, s, "#6A5A3A", up=[(-22, -158), (-44, -146), (-62, -142)], extra=dish + '<path d="M-24 -104 L 24 -104" stroke="#3A2214" stroke-width="5"></path>'))
    return "".join(o)

LEPER_C = ["#8A8A86", "#9A9690", "#7A7A78", "#A8A49C"]
def ten_lepers(p, w, h, seed, stage="afar"):
    """Ten men that were lepers, who stood afar off: stage='afar' at the edge of a village on the border of Samaria and
    Galilee, ten men in grey and ash standing together far off on the hillside, crying; Jesus and the disciples on the road
    below; 'go' the ten going away up the road toward the priests; 'back' one of them, the Samaritan in a rust cloak, fallen
    on his face at Jesus' feet, the nine small and far off on the road, not turning."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#8A9A6A", amp=14, step=80),
         hill_town(w * 0.84, h * 0.52, w * 0.28, h * 0.18, seed, hill="#9A8A6A"), ground(w, h, h * 0.58, "#B8A06A", dy=-6),
         f'<path d="M-10 {f(b + 6)} C {f(w * 0.3)} {f(b - h * 0.06)} {f(w * 0.6)} {f(h * 0.68)} {f(w * 0.84)} {f(h * 0.56)}" stroke="#D8C08A" stroke-width="{f(h * 0.06)}" fill="none" opacity="0.8"></path>']
    s = fit(b, max(h * 0.24, b - 230))
    if stage == "afar":
        sf = s * 0.5
        for i in range(10):
            o.append(man(p, w * (0.5 + 0.04 * i), h * 0.66 - (i % 2) * 4, sf, LEPER_C[i % 4] if i != 6 else "#8A4A2A", flip=True, up=UP_HIGH if i % 3 == 0 else None,
                         extra=A.headcloth("#B8B2A6", cord=None)))
        o.append(jesus(p, w * 0.2, b, s) + disciple(p, w * 0.08, b, s * 0.94, "peter") + disciple(p, w * 0.32, b - 4, s * 0.9, "john"))
    elif stage == "go":
        sf = s * 0.42
        for i in range(10):
            o.append(man(p, w * (0.56 + 0.026 * i), h * 0.62 - i * 3, sf * (1 - 0.02 * i), LEPER_C[i % 4] if i != 6 else "#8A4A2A", extra=A.headcloth("#B8B2A6", cord=None)))
        o.append(jesus(p, w * 0.2, b, s, up=UP_BLESS, flip=True))
    else:
        for i in range(9):
            o.append(man(p, w * (0.66 + 0.02 * i), h * 0.58 - i * 2, s * 0.3, LEPER_C[i % 4]))
        o.append(jesus(p, w * 0.28, b, s, flip=True))
        o.append(E.kneel(w * 0.46, b, s * 0.86, color="#8A4A2A", flip=True, skin="#C98E66"))
    return "".join(o)
