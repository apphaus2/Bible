"""Drawings for Luke 23–24. The passion: Herod the tetrarch on his seat with Jesus standing silent before him; then Herod's
hall empty, the throne left, and the gorgeous apparel thrown down on the floor (the setting at nought and the mocking told
in words only); the daughters of Jerusalem bewailing him by the road out of the gate; the women preparing spices and
ointments at lamplight. The resurrection: the two men in dazzling apparel at the empty tomb — figures of white light, no
face; Peter stooping at the tomb, the linen cloths by themselves; the road to Emmaus — Jesus risen in white light walking
with the two, their eyes holden; the table at Emmaus, the bread broken, the place empty; the eleven and Jesus in the midst;
the broiled fish; the ascension at Bethany, Jesus in white light with his hands lifted up, parted from them into a cloud of
light (God never drawn); the disciples continually in the temple. Built on luk.art12."""
from luk.art12 import *
from luk.art12 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch, \
    jesus_kneel, light_seated, WOMEN3, PURPLE, GOLD, kneel_w, boy_fig, zach_fig, elis_fig, shepherd_fig, swaddled, fish_heap, WIDOW_C, WIDOW_V, SINNER_C, SINNER_V, \
    JOANNA, SUSANNA, SAMARITAN_C, samaritan_fig, priest_fig, levite_fig, RICH_C, rich_fig, barn, son_fig, father_fig, elder_fig, farm, LAZ_C, LEPER_C, ZAC_C, \
    zacchaeus_fig
import random, math
from oba.minor import cup

def antipas_fig(p, x, y, s, flip=False, up=None):
    """Herod the tetrarch at a distance (ntcast's Herod): a deep-purple robe and headcloth with a gold band, a black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#C98E66", cloth="#5A1A4A", kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth("#5A1A4A", cord="#E8B830") + A.BLACK_BEARD)

GORGEOUS = "#F3E2B0"
def antipas_hall(p, w, h, seed, stage="before"):
    """Herod's hall at Jerusalem: gold columns and purple hangings; stage='before' Herod on his seat leaning forward, Jesus
    standing before him silent, the chief priests and scribes at the side accusing; 'robe' the hall empty, the seat left,
    and on the floor a gorgeous robe of shining white and gold thrown down (the soldiers' mocking told in words only)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bgr(w, h, "#3A1A3A")]
    for x in (0.06, 0.34, 0.66, 0.94):
        o.append(f'<rect x="{f(w * x - 14)}" y="-10" width="28" height="{f(b + 10)}" fill="#E8B830" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<path d="M-10 -10 L {f(w + 10)} -10 L {f(w + 10)} {f(h * 0.14)} C {f(w * 0.7)} {f(h * 0.26)} {f(w * 0.3)} {f(h * 0.26)} -10 {f(h * 0.14)} Z" fill="#5A1A4A" stroke="{INK}" stroke-width="2"></path>'
             f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#6A4A3A" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.24, b - 240))
    o.append(f'<path d="M{f(w * 0.12)} {f(b)} L {f(w * 0.12)} {f(b - 150 * s)} L {f(w * 0.12 + 100 * s)} {f(b - 150 * s)} L {f(w * 0.12 + 100 * s)} {f(b)} Z" fill="#E8B830" stroke="{INK}" stroke-width="2.4"></path>')
    if stage == "before":
        o.append(antipas_fig(p, w * 0.12 + 50 * s, b, s, flip=True, up=UP_BLESS))
        o.append(jesus(p, w * 0.48, b, s, glow=False))
        o.append(scribe_fig(p, w * 0.72, b, s * 0.96, white=True, flip=True, up=UP_BLESS) + scribe_fig(p, w * 0.84, b, s * 0.94, flip=True))
    else:
        k = max(0.6, h / 260); cx = w * 0.5
        o.append(f'<path d="M{f(cx - 100 * k)} {f(b)} C {f(cx - 80 * k)} {f(b - 44 * k)} {f(cx - 10 * k)} {f(b - 56 * k)} {f(cx + 30 * k)} {f(b - 34 * k)} C {f(cx + 64 * k)} {f(b - 44 * k)} {f(cx + 96 * k)} {f(b - 20 * k)} {f(cx + 104 * k)} {f(b)} Z" fill="{GORGEOUS}" stroke="{INK}" stroke-width="2.4"></path>'
                 f'<path d="M{f(cx - 70 * k)} {f(b - 10 * k)} C {f(cx - 30 * k)} {f(b - 30 * k)} {f(cx + 30 * k)} {f(b - 20 * k)} {f(cx + 80 * k)} {f(b - 8 * k)}" stroke="{GOLD}" stroke-width="{f(4 * k)}" fill="none"></path>'
                 + glow(cx, b - 20 * k, 120 * k, "#FFE680", 0.4, f"{p}g"))
    return "".join(o)

def daughters(p, w, h, seed):
    """Daughters of Jerusalem, weep not for me: the road out of the city gate, the women standing at the roadside bewailing
    him, their hands to their faces; Jesus turned toward them between the soldiers; behind, Simon of Cyrene bearing the cross."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8A8A9A", "#E8C8A0"), walls(w * 0.64, w + 10, h * 0.62, h * 0.4, seed, towers=2), ground(w, h, h * 0.62, "#B8A07A", dy=0)]
    s = fit(b, max(h * 0.26, b - 220))
    cols = [("#3A4A6A", "#2A3A5A"), ("#6A3A4A", "#4A2A3A"), ("#5A5A4A", "#3A3A2A"), ("#7A5A3A", "#5A3A22")]
    for i, (c, vl) in enumerate(cols):
        o.append(woman_fig(p, w * (0.06 + 0.09 * i), b - 2 * (i % 2), s * (0.92 - 0.02 * i), c, vl, flip=True, up=[(-22, -158), (-16, -176), (-4, -186)]))
    o.append(jesus(p, w * 0.48, b, s, glow=False, up=UP_BLESS))
    o.append(roman_fig(p, w * 0.6, b, s * 0.96))
    beam = '<path d="M-90 -170 L 60 -150" stroke="#6A4A2A" stroke-width="12" stroke-linecap="round"></path>'
    o.append(man(p, w * 0.78, h * 0.78, s * 0.7, "#2A6A5A", up=[(-22, -158), (-30, -170), (-20, -176)], extra=beam))
    return "".join(o)

def spices_prepare(p, w, h, seed):
    """They returned, and prepared spices and ointments: a room at lamplight on the evening of the Preparation, the women of
    Galilee at a low table with jars, a mortar and bundles of myrrh and aloes; then the sabbath stillness."""
    b = min(h * 0.92, h - 76)
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#5A4048", floor="#4A3A30", window=(w * 0.84, w * 0.08), night_=True, seed=seed),
         glow(w * 0.4, b - h * 0.2, h * 0.5, "#FFE680", 0.45, f"{p}g"), A.lamp(w * 0.4, h * 0.3, max(0.6, h / 320))]
    s = fit(b, max(h * 0.2, b - 230))
    o.append(f'<rect x="{f(w * 0.24)}" y="{f(b - 36 * s)}" width="{f(w * 0.34)}" height="{f(12 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
    for i, c in enumerate(("#E8D8A8", "#C8A878", "#F3EFE6")):
        x = w * (0.3 + 0.09 * i)
        o.append(f'<path d="M{f(x - 8 * s)} {f(b - 36 * s)} C {f(x - 12 * s)} {f(b - 56 * s)} {f(x - 6 * s)} {f(b - 66 * s)} {f(x)} {f(b - 66 * s)} C {f(x + 6 * s)} {f(b - 66 * s)} {f(x + 12 * s)} {f(b - 56 * s)} {f(x + 8 * s)} {f(b - 36 * s)} Z" fill="{c}" stroke="{INK}" stroke-width="1.6"></path>')
    for i, (c, vl) in enumerate(WOMEN3):
        x = (0.14, 0.66, 0.78)[i]
        o.append(seated(w * x, b, s * 0.78, c, head=vl, beard=None, flip=x > 0.4))
    return "".join(o)
