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

# ---- Luke 24 ------------------------------------------------------------------------------------------------------------
WOMEN_TOMB = [(ROBES["magdalene"], "#C2456A"), JOANNA, ("#6A4A2A", "#5A3A22")]      # Mary Magdalene, Joanna, Mary the mother of James

def two_men(p, w, h, seed):
    """Two men stood by them in dazzling apparel: within the open tomb, the stone shelf empty and the linen lying, two figures
    of white light with a gold rim standing (no faces), and the women bowed down with their faces to the earth."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bgr(w, h, "#2A2220"),
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#4A3A34" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.5)}" y="{f(b - h * 0.16)}" width="{f(w * 0.46)}" height="{f(h * 0.16)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.62)} {f(b - h * 0.16)} L {f(w * 0.64)} {f(b - h * 0.2)} L {f(w * 0.84)} {f(b - h * 0.2)} L {f(w * 0.86)} {f(b - h * 0.16)} Z" fill="#F8F4EC" stroke="{INK}" stroke-width="1.6"></path>',
         glow(w * 0.6, b - h * 0.3, h * 0.6, "#FFFFFF", 0.7, f"{p}g")]
    s = fit(b, max(h * 0.12, b - 250))
    o.append(angel(p, w * 0.5, b, s, up=UP_BLESS) + angel(p, w * 0.72, b, s, flip=False, up=UP_BLESS))
    for i, (c, vl) in enumerate(WOMEN_TOMB):
        o.append(kneel_w(w * (0.1 + 0.1 * i), b, s * 0.7, c, vl))
    return "".join(o)

def peter_stoops(p, w, h, seed):
    """Peter arose, and ran unto the tomb; and stooping and looking in: the rock tomb in the garden at morning, the stone
    rolled back, Peter bent at the low doorway looking in, the linen cloths lying by themselves within."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A9A", "#FFE6A0"),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.34)} {f(h * 0.26)} C {f(w * 0.5)} {f(h * 0.16)} {f(w * 0.8)} {f(h * 0.18)} {f(w + 10)} {f(h * 0.26)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.46)} {f(b - h * 0.04)} L {f(w * 0.46)} {f(h * 0.52)} Q {f(w * 0.54)} {f(h * 0.42)} {f(w * 0.62)} {f(h * 0.52)} L {f(w * 0.62)} {f(b - h * 0.04)} Z" fill="#1A1210" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.5)} {f(b - h * 0.08)} L {f(w * 0.51)} {f(b - h * 0.12)} L {f(w * 0.59)} {f(b - h * 0.12)} L {f(w * 0.6)} {f(b - h * 0.08)} Z" fill="#F8F4EC" stroke="{INK}" stroke-width="1.4"></path>',
         ground(w, h, b - h * 0.04, "#6A8A3A", dy=0)]
    cx, cy, r = w * 0.82, b - h * 0.04 - h * 0.19, h * 0.19
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="#A89A8A" stroke="{INK}" stroke-width="2.6"></circle>')
    s = fit(b, max(h * 0.3, b - 220))
    o.append(f'<g transform="translate({f(w * 0.4)} {f(b)}) rotate(22) translate({f(-w * 0.4)} {f(-b)})">' + disciple(p, w * 0.4, b, s * 0.9, "peter", flip=True) + '</g>')
    return "".join(o)

def emmaus(p, w, h, seed, stage="walk"):
    """The road to Emmaus, threescore furlongs from Jerusalem: stage='walk' the two going along the road in the afternoon among
    the hills, talking, Jerusalem behind them; 'joined' Jesus risen in white light walking with them — their eyes holden;
    'village' at evening at the gate of the village, the two constraining him, his hand lifted as though he would go further;
    'table' within, at the low table under the lamp, Jesus risen in white light breaking the bread, the two seated; 'gone' the
    same table with the broken bread, his place empty, the two risen up amazed; 'back' the road at night, the two hurrying
    back toward Jerusalem's lights."""
    b = h * 0.94
    s = fit(b, max(h * 0.24, b - 230))
    C1, C2 = "#6A4A2A", "#5A6A7A"                      # Cleopas, and his companion
    if stage in ("walk", "joined", "village", "back"):
        top, bot = {"walk": ("#8FD0E2", "#FFE6B0"), "joined": ("#8FD0E2", "#FFE6B0"), "village": ("#4A3A6A", "#FFB07A"), "back": ("#05051A", "#2A2050")}[stage]
        o = [mk.defs(p, *ALL), sky(w, h, top, bot)]
        if stage == "back": o.append(mk.stars(50, w, h * 0.4, seed))
        o += [hills(w, h, h * 0.46, seed, color="#8A8A6A" if stage != "back" else "#1E1838", amp=14, step=80)]
        if stage in ("walk", "back"):
            o.append(walls(w * 0.74, w * 1.02, h * 0.5, h * 0.14, seed, lit=stage == "back", towers=2))
        o += [ground(w, h, h * 0.58, "#B8A06A" if stage != "back" else "#2A2438", dy=-4),
              f'<path d="M-10 {f(b + 6)} C {f(w * 0.3)} {f(b - h * 0.06)} {f(w * 0.6)} {f(h * 0.68)} {f(w * 0.84)} {f(h * 0.58)}" stroke="{"#D8C08A" if stage != "back" else "#4A4458"}" stroke-width="{f(h * 0.07)}" fill="none" opacity="0.8"></path>']
        if stage == "walk":
            o.append(man(p, w * 0.36, b, s, C1, extra=A.headcloth("#6A4A2A")) + man(p, w * 0.48, b, s * 0.96, C2, flip=True))
        elif stage == "joined":
            o.append(man(p, w * 0.3, b, s, C1, extra=A.headcloth("#6A4A2A")) + man(p, w * 0.42, b, s * 0.96, C2))
            o.append(jesus_risen(p, w * 0.6, b, s, flip=True))
        elif stage == "village":
            o.append(houses(w, h, h * 0.86, seed, x0=w * 0.56, x1=w + 10, hmin=0.3, hmax=0.42, lit=True))
            o.append(jesus_risen(p, w * 0.74, b, s, flip=True, up=UP_CALL))
            o.append(man(p, w * 0.4, b, s, C1, flip=True, up=UP_BLESS, extra=A.headcloth("#6A4A2A")) + man(p, w * 0.52, b, s * 0.96, C2, flip=True, up=UP_BLESS))
        else:
            o.append(man(p, w * 0.5, b, s, C1, up=[(-22, -158), (-40, -136), (-56, -124)], extra=A.headcloth("#6A4A2A")) + man(p, w * 0.62, b, s * 0.96, C2))
    else:
        o = [mk.defs(p, *ALL), room(w, h, b - h * 0.02, wall="#5A4A48", floor="#4A3A30", window=(w * 0.84, w * 0.08), night_=True, seed=seed),
             A.lamp(w * 0.5, h * 0.26, max(0.6, h / 300)), glow(w * 0.5, h * 0.4, h * 0.6, "#FFE680", 0.4, f"{p}g")]
        bb = b - h * 0.02
        o.append(f'<rect x="{f(w * 0.3)}" y="{f(bb - 40 * s)}" width="{f(w * 0.4)}" height="{f(14 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
                 + loaf(w * 0.44, bb - 44 * s, s * 0.6) + loaf(w * 0.54, bb - 44 * s, s * 0.5))
        if stage == "table":
            o.append(seated(w * 0.22, bb, s * 0.8, C1, head="#6A4A2A", beard="#6A5A4E") + seated(w * 0.78, bb, s * 0.78, C2, beard=None, flip=True))
            o.append(jesus_risen(p, w * 0.5, bb - 6, s * 0.9, up=[(-22, -158), (-40, -140), (-50, -130)]))
        else:
            o.append(glow(w * 0.5, bb - 100 * s, 90 * s, "#FFFFFF", 0.4, f"{p}e"))
            o.append(man(p, w * 0.22, bb, s, C1, up=UP_HIGH, extra=A.headcloth("#6A4A2A")) + man(p, w * 0.78, bb, s * 0.96, C2, flip=True, up=UP_HIGH))
    return "".join(o)

def bethany_bless(p, w, h, seed):
    """He led them out until they were over against Bethany: and he lifted up his hands, and blessed them: the slope of the
    mount over against Bethany at morning, Jesus risen in white light with both hands lifted, the eleven kneeling and
    standing about him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A8AC8", "#FFE6B0"), hill_town(w * 0.84, h * 0.6, w * 0.24, h * 0.16, seed, hill="#8A9A6A"),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.5)} {f(w * 0.6)} {f(h * 0.56)} {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h + 10)} Z" fill="#7A9A4A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.24, b - 230))
    o.append(jesus_risen(p, w * 0.46, b - 10, s, up=UP_HIGH))
    for i, x in enumerate((0.12, 0.22, 0.32, 0.6, 0.7, 0.8, 0.9)):
        if i in (2, 3): o.append(E.kneel(w * x, b, s * 0.8, color=TWELVE[i], flip=x > 0.46, skin="#B98A6E"))
        else: o.append(disciple(p, w * x, b - 2 * (i % 2), s * 0.9, TWELVE[i], flip=x > 0.46))
    return "".join(o)

def temple_joy(p, w, h, seed):
    """They returned to Jerusalem with great joy, and were continually in the temple, blessing God: the court of the temple
    at morning, the disciples standing together with their hands lifted (the floor clear below them for the end mark)."""
    b = min(h * 0.94, h - 76)
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), temple(w * 0.62, h * 0.56, w * 0.6), pavement(w, h, h * 0.56)]
    s = fit(b, max(h * 0.56, b - 150))
    for i in range(9):
        o.append(disciple(p, w * (0.06 + 0.07 * i), b - 2 * (i % 2), s * (0.94 - 0.01 * i), TWELVE[i], up=UP_HIGH if i % 2 == 0 else None))
    return "".join(o)
