"""Drawings for Luke 10: the seventy sent two and two and returning with joy; serpents and scorpions trodden; the parable
of the good Samaritan — the steep road from Jerusalem down to Jericho through the bare hills, the robbers going off over the
ridge and the man's garments thrown down (the man himself told in words: he is never drawn stripped or wounded — lying
hidden below the road's edge), the priest and the Levite passing by on the other side, the Samaritan kneeling with his oil
and wine, the man wrapped in the Samaritan's cloak set on his own beast, the inn and the two shillings; Martha and Mary in
the house, Mary sitting at the Lord's feet. Built on luk.art5."""
from luk.art5 import *
from luk.art5 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch, \
    jesus_kneel, light_seated, WOMEN3, PURPLE, GOLD, kneel_w, boy_fig, zach_fig, elis_fig, shepherd_fig, swaddled, fish_heap, WIDOW_C, WIDOW_V, SINNER_C, SINNER_V, \
    JOANNA, SUSANNA
import random, math
from snake import snake

SAMARITAN_C = "#8A1A22"
STRIPES = ''.join(f'<path d="M{x} -150 L {x + 4} -6" stroke="#E8D8B0" stroke-width="3" opacity="0.8"></path>' for x in (-14, -2, 10))
def samaritan_fig(p, x, y, s, flip=False, up=None):
    """The Samaritan: a deep-red striped cloak, a white headcloth, a black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#B98A6E", cloth=SAMARITAN_C, kind="Robe", sw=3, flip=flip, up=up,
                     extra=STRIPES + A.headcloth("#F3EFE6", cord="#8A1A22") + A.BLACK_BEARD)

def priest_fig(p, x, y, s, flip=False):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#F3EFE6", kind="Robe", sw=3, flip=flip,
                     extra=A.headcloth("#F3EFE6", cord="#E8B830") + A.WHITE_BEARD.replace("#E8E2D6", "#9A948A"))

def levite_fig(p, x, y, s, flip=False):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#5A6A8A", kind="Robe", sw=3, flip=flip, extra=A.headcloth("#8A9AB0") + A.BLACK_BEARD)

def seventy(p, w, h, seed, back=False):
    """He sent them two and two before his face into every city and place: from the hill the roads going out to the towns of
    the land, pairs of small figures walking out on each; back=True: the seventy coming back up the road with joy, their
    arms lifted, Jesus waiting on the hill."""
    b = h * 0.94
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, color="#8A9A7A", amp=14, step=90)]
    towns = [(0.1, 0.42), (0.34, 0.38), (0.62, 0.4), (0.88, 0.44)]
    for x, y in towns: o.append(hill_town(w * x, h * y, w * 0.16, h * 0.1, seed + int(x * 100), hill="#9A8A6A"))
    o.append(ground(w, h, h * 0.5, "#B8A86A", dy=0))
    for x, y in towns:
        o.append(f'<path d="M{f(w * 0.5)} {f(b)} C {f(w * 0.5)} {f(h * 0.7)} {f(w * x)} {f(h * 0.6)} {f(w * x)} {f(h * y + 4)}" stroke="#D8C08A" stroke-width="7" fill="none" opacity="0.9"></path>')
    for i, (x, y) in enumerate(towns):
        for k in range(2):
            t = 0.4 + 0.12 * k + r.uniform(-0.04, 0.04)
            px = w * (0.5 + (x - 0.5) * t); py = b - (b - h * y) * t
            o.append(man(p, px + k * 6, py, max(0.12, h / 2600) * (1.6 - t), TWELVE[(i * 2 + k) % 12], up=UP_HIGH if back else None))
    s = fit(b, max(h * 0.4, b - 180))
    o.append(jesus(p, w * 0.5, b, s * 0.9))
    return "".join(o)

def tread(p, w, h, seed):
    """Authority to tread upon serpents and scorpions: on the stony ground a serpent and a scorpion, and a sandalled foot set
    down beside them, unhurt."""
    b = h * 0.9
    r = random.Random(seed)
    o = [sky(w, h, "#C8A878", "#F3E8C8"), ground(w, h, h * 0.4, "#C8A878", dy=0)]
    for _ in range(12):
        x, y = r.uniform(0, w), r.uniform(h * 0.5, h); rr = r.uniform(6, 16) * h / 300
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rr * 1.4)}" ry="{f(rr)}" fill="#A88A6A" stroke="{INK}" stroke-width="1.4"></ellipse>')
    k = max(1.0, h / 160)
    o.append(snake([(w * 0.12, b - 4 * k), (w * 0.22, b - 14 * k), (w * 0.3, b - 2 * k), (w * 0.4, b - 12 * k)], 4.5 * k, f"{p}sn", 0.8))
    sx, sy = w * 0.74, b - 6 * k                          # a scorpion
    o.append(f'<g transform="translate({f(sx)} {f(sy)}) scale({f(k)})"><ellipse cx="0" cy="0" rx="14" ry="7" fill="#3A2A1A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
             '<path d="M12 0 C 26 -2 34 -14 30 -26 C 28 -32 22 -32 22 -26" stroke="#3A2A1A" stroke-width="4" fill="none"></path><path d="M20 -26 L 26 -30 L 24 -22 Z" fill="#8A1A1A"></path>'
             '<path d="M-12 -2 C -20 -10 -28 -8 -30 -2 M-12 2 C -20 10 -28 8 -30 2 M-6 6 L -10 14 M0 6 L 0 15 M6 6 L 10 14 M-6 -6 L -10 -14 M0 -6 L 0 -15 M6 -6 L 10 -14" '
             'stroke="#3A2A1A" stroke-width="2" fill="none"></path></g>')
    fx = w * 0.54                                          # the foot
    o.append(f'<g transform="translate({f(fx)} {f(b)}) scale({f(k * 1.4)})"><path d="M-30 0 C -30 -10 -20 -14 -6 -14 L 20 -14 C 30 -14 34 -6 32 0 Z" fill="{SKIN}" stroke="#0D0D0F" stroke-width="1.6"></path>'
             '<path d="M-34 2 L 36 2" stroke="#8A5A2A" stroke-width="4"></path><path d="M-4 -14 L -2 -40 L 10 -40 L 12 -14" fill="#7A5A3A" stroke="#0D0D0F" stroke-width="1.4"></path>'
             '<path d="M-10 -10 C 0 -4 12 -4 20 -10" stroke="#5A3A22" stroke-width="2.4" fill="none"></path></g>')
    return "".join(o)

def jericho_road(p, w, h, seed, stage="robbers"):
    """The road down from Jerusalem to Jericho: a pale road winding down through bare tawny hills toward the green of
    Jericho far below; stage='robbers' the robbers going away over the ridge, a torn cloak and an emptied bag thrown down
    at the road's edge (the man lies below the edge, unseen); 'priest' a priest in white passing by on the other side;
    'levite' a Levite in blue-grey passing by on the other side; 'mercy' the Samaritan's beast standing in the road and the
    Samaritan kneeling at the edge with his flasks of oil and wine; 'beast' the Samaritan leading his beast down toward the
    inn, the man set on it wrapped whole in the Samaritan's red cloak."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFE6B0"), hills(w, h, h * 0.36, seed, color="#C8985A", amp=24, step=70),
         f'<path d="M{f(w * 0.7)} {f(h * 0.46)} C {f(w * 0.8)} {f(h * 0.42)} {f(w * 0.94)} {f(h * 0.44)} {f(w + 10)} {f(h * 0.46)} L {f(w + 10)} {f(h * 0.52)} L {f(w * 0.7)} {f(h * 0.52)} Z" fill="#5A8A3A" stroke="{INK}" stroke-width="1.6"></path>',
         hills(w, h, h * 0.52, seed + 1, color="#B8885A", amp=16, step=80), ground(w, h, h * 0.66, "#C8A070", dy=0),
         f'<path d="M-10 {f(h * 0.82)} C {f(w * 0.3)} {f(h * 0.76)} {f(w * 0.6)} {f(h * 0.72)} {f(w * 0.86)} {f(h * 0.58)}" stroke="#E8D0A0" stroke-width="{f(h * 0.1)}" fill="none"></path>',
         f'<path d="M-10 {f(h * 0.92)} C {f(w * 0.3)} {f(h * 0.88)} {f(w * 0.6)} {f(h * 0.86)} {f(w + 10)} {f(h * 0.86)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#A8805A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(h * 0.8, max(h * 0.4, h * 0.8 - 190))
    ex, ey = w * 0.26, h * 0.9                           # the near edge of the road, where he lies unseen below
    if stage in ("robbers", "priest", "levite"):
        o.append(f'<path d="M{f(ex - 40 * s)} {f(ey - 4)} C {f(ex - 20 * s)} {f(ey - 20 * s)} {f(ex + 20 * s)} {f(ey - 24 * s)} {f(ex + 50 * s)} {f(ey - 6)} Z" fill="#5A6A8A" stroke="{INK}" stroke-width="2"></path>'
                 f'<path d="M{f(ex + 64 * s)} {f(ey - 4)} C {f(ex + 66 * s)} {f(ey - 18 * s)} {f(ex + 86 * s)} {f(ey - 18 * s)} {f(ex + 88 * s)} {f(ey - 4)} Z" fill="#8A6A3A" stroke="{INK}" stroke-width="1.6"></path>')
    if stage == "robbers":
        for i in range(3):
            o.append(silhouette(man(p, w * (0.56 + 0.05 * i), h * 0.5, max(0.14, h / 2200), "#000"), "#2A1A14"))
    if stage == "priest":
        o.append(priest_fig(p, w * 0.7, h * 0.7, s * 0.8, flip=True))
    if stage == "levite":
        o.append(levite_fig(p, w * 0.66, h * 0.72, s * 0.8, flip=True))
    if stage == "mercy":
        o.append(N.ass(w * 0.46, h * 0.84, s * 0.8, color="#8A8478"))
        o.append(E.kneel(ex + 30 * s, ey + 2, s * 0.9, color=SAMARITAN_C, skin="#B98A6E"))
        for k, c in enumerate(("#C8A040", "#7A1A2A")):
            o.append(f'<path d="M{f(ex + (96 + 16 * k) * s)} {f(ey)} C {f(ex + (90 + 16 * k) * s)} {f(ey - 18 * s)} {f(ex + (104 + 16 * k) * s)} {f(ey - 22 * s)} {f(ex + (100 + 16 * k) * s)} {f(ey - 30 * s)} '
                     f'L {f(ex + (108 + 16 * k) * s)} {f(ey - 30 * s)} C {f(ex + (106 + 16 * k) * s)} {f(ey - 20 * s)} {f(ex + (118 + 16 * k) * s)} {f(ey - 16 * s)} {f(ex + (112 + 16 * k) * s)} {f(ey)} Z" fill="{c}" stroke="{INK}" stroke-width="1.4"></path>')
    if stage == "beast":
        bx, by = w * 0.5, h * 0.82
        o.append(N.ass(bx, by, s * 0.9, color="#8A8478"))
        o.append(f'<g transform="translate({f(bx - 8 * s)} {f(by - 70 * s)})"><path d="M-34 0 C -36 -30 -16 -60 4 -64 C 20 -66 28 -50 26 -30 L 30 0 Z" fill="{SAMARITAN_C}" stroke="{INK}" stroke-width="2"></path>'
                 f'<circle cx="8" cy="-70" r="11" fill="#B98A6E" stroke="{INK}" stroke-width="1.8"></circle>'
                 f'<path d="M-4 -74 C -2 -86 18 -86 20 -72 L 20 -60 L -2 -62 Z" fill="#F3EFE6" stroke="{INK}" stroke-width="1.4"></path>{STRIPES.replace("-150", "-60").replace("-6", "-2")}</g>')
        o.append(samaritan_fig(p, bx + 110 * s, h * 0.84, s * 0.94, flip=False, up=[(-22, -158), (-50, -140), (-74, -122)]))
    return "".join(o)

def inn(p, w, h, seed):
    """He brought him to an inn: on the morrow, the inn's courtyard at sunrise, the host at the door, the Samaritan putting
    two shillings into his hand, the beast saddled to go; in the window the lamp still burning where the man lies within."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A9A", "#FFC890"), hills(w, h, h * 0.4, seed, color="#B8885A", amp=14, step=80)]
    hx0, hx1, top = w * 0.04, w * 0.6, h * 0.22
    o.append(f'<rect x="{f(hx0)}" y="{f(top)}" width="{f(hx1 - hx0)}" height="{f(b - top)}" fill="#D8C090" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(hx0 - 6)}" y="{f(top - 8)}" width="{f(hx1 - hx0 + 12)}" height="10" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.36)} {f(b)} L {f(w * 0.36)} {f(b - h * 0.36)} Q {f(w * 0.44)} {f(b - h * 0.46)} {f(w * 0.52)} {f(b - h * 0.36)} L {f(w * 0.52)} {f(b)} Z" fill="#3A2A1E" stroke="{INK}" stroke-width="2"></path>'
             f'<rect x="{f(w * 0.12)}" y="{f(top + h * 0.12)}" width="{f(w * 0.08)}" height="{f(h * 0.1)}" fill="#FFC14D" stroke="{INK}" stroke-width="1.8"></rect>')
    o.append(ground(w, h, b, "#B8A06A", dy=0))
    s = fit(b, max(h * 0.2, b - 230))
    o.append(man(p, w * 0.46, b, s, "#6A5A3A", flip=False))
    o.append(samaritan_fig(p, w * 0.62, b, s, flip=False, up=UP_BLESS))
    o.append(f'<circle cx="{f(w * 0.62 - 66 * s)}" cy="{f(b - 156 * s)}" r="{f(5 * s)}" fill="#C8C2B6" stroke="{INK}" stroke-width="1"></circle>'
             f'<circle cx="{f(w * 0.62 - 58 * s)}" cy="{f(b - 152 * s)}" r="{f(5 * s)}" fill="#C8C2B6" stroke="{INK}" stroke-width="1"></circle>')
    o.append(N.ass(w * 0.86, b, s * 0.8, color="#8A8478"))
    return "".join(o)

def martha_house(p, w, h, seed, stage="feet"):
    """Martha received him into her house: the room at Bethany, Jesus seated, Mary her sister sitting at his feet listening;
    stage='feet' Martha at the hearth behind with her jars and loaves; 'cumbered' Martha come up to him with a dish in her
    hands, her other hand out toward Mary."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#B8987A", window=(w * 0.84, w * 0.08)), A.lamp(w * 0.5, h * 0.24, max(0.6, h / 300))]
    s = fit(b, max(h * 0.2, b - 230))
    o.append(jesus_seated(w * 0.3, b, s * 0.84))
    o.append(glow(w * 0.3, b - 80 * s, 120 * s, "#FFF4C2", 0.4, f"{p}g"))
    o.append(seated(w * 0.5, b, s * 0.7, "#7A4A5A", head="#7A4A5A", beard=None, flip=True))
    if stage == "feet":
        o.append(f'<rect x="{f(w * 0.68)}" y="{f(b - 50 * s)}" width="{f(w * 0.24)}" height="{f(50 * s)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>'
                 + loaf(w * 0.74, b - 54 * s, s * 0.6) + loaf(w * 0.82, b - 54 * s, s * 0.6))
        o.append(woman_fig(p, w * 0.9, b, s * 0.92, "#6A5A2A", "#8A6A2A", flip=False, up=[(-22, -158), (-40, -136), (-56, -128)]))
    else:
        dish = '<ellipse cx="-62" cy="-140" rx="18" ry="5" fill="#C8A060" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
        o.append(woman_fig(p, w * 0.66, b, s * 0.92, "#6A5A2A", "#8A6A2A", flip=False, up=[(-22, -158), (-44, -146), (-62, -142)], extra=dish))
    return "".join(o)
