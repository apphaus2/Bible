"""Drawings for Luke 18–19: the unrighteous judge on his seat in the gate and the widow's continual coming; the Pharisee
and the publican in the temple — the one standing forward with his hands lifted, the other afar off by a pillar with his
eyes down, smiting his breast; Zacchæus — little of stature, run on before and up into the sycomore over the crowd, Jesus
looking up, his house and his standing to restore fourfold; the pounds — the nobleman going into a far country, the
napkin; Jesus on the descent of the mount of Olives weeping over the city; teaching daily in the temple. Built on
luk.art10."""
from luk.art10 import *
from luk.art10 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch, \
    jesus_kneel, light_seated, WOMEN3, PURPLE, GOLD, kneel_w, boy_fig, zach_fig, elis_fig, shepherd_fig, swaddled, fish_heap, WIDOW_C, WIDOW_V, SINNER_C, SINNER_V, \
    JOANNA, SUSANNA, SAMARITAN_C, samaritan_fig, priest_fig, levite_fig, RICH_C, rich_fig, barn, son_fig, father_fig, elder_fig, farm, LAZ_C, LEPER_C
import random, math

ZAC_C = "#7A2A22"
def zacchaeus_fig(p, x, y, s, flip=False, up=None):
    """Zacchæus: little of stature, a crimson-brown robe, a teal headcloth with a cord, black beard."""
    return mk.person(p, round(x), round(y), round(s * 0.8, 3), body="#C98E66", cloth=ZAC_C, kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth("#1F5A6A", cord="#E8B830") + A.BLACK_BEARD)

def judge_widow(p, w, h, seed, avenged=False):
    """There was in a city a judge, who feared not God, and regarded not man: the judge on his seat under the arch of the city
    gate in a black robe with a gold band; the widow in grey with her black veil before him, her hands lifted, coming oft;
    avenged=True: the judge's hand thrown up, done with her, the widow going away satisfied."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), walls(w * 0.0, w * 1.0, h * 0.7, h * 0.5, seed, towers=2, houses=False), ground(w, h, h * 0.7, "#B8A06A", dy=0),
         f'<path d="M{f(w * 0.06)} {f(b)} L {f(w * 0.06)} {f(h * 0.24)} Q {f(w * 0.2)} {f(h * 0.1)} {f(w * 0.34)} {f(h * 0.24)} L {f(w * 0.34)} {f(b)} Z" fill="#5A4A3A" stroke="{INK}" stroke-width="2.4"></path>']
    s = fit(b, max(h * 0.2, b - 230))
    o.append(f'<rect x="{f(w * 0.12)}" y="{f(b - 90 * s)}" width="{f(90 * s)}" height="{f(90 * s)}" fill="#8A6A3A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(seated(w * 0.16, b - 40 * s, s * 0.86, "#1A1A22", head="#2A2A32", beard="#6A645E", band=True))
    if avenged:
        o.append(widow_fig(p, w * 0.72, b, s * 0.9))
    else:
        o.append(widow_fig(p, w * 0.48, b, s * 0.9, up=[(-22, -158), (-44, -170), (-56, -188)]))
    return "".join(o)

def pharisee_publican(p, w, h, seed):
    """Two men went up into the temple to pray: in the court, the Pharisee in white standing forward, his hands lifted,
    looking about him; far behind by a pillar the publican in a dark tunic, his head bowed, his hand upon his breast."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), temple(w * 0.5, h * 0.52, w * 0.58), pavement(w, h, h * 0.52),
         f'<rect x="{f(w * 0.86 - 16)}" y="{f(h * 0.1)}" width="32" height="{f(h * 0.62)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.2, b - 240))
    o.append(scribe_fig(p, w * 0.36, b, s, white=True, up=UP_HIGH))
    o.append(mk.person(p, round(w * 0.82), round(h * 0.74), round(s * 0.62, 3), body="#B98A6E", cloth="#3A3440", kind="Tunic", sw=3, flip=True,
                       up=[(-22, -158), (-12, -140), (4, -146)], extra=A.headcloth("#3A3440")))
    return "".join(o)

def sycomore(p, w, h, seed, stage="climb"):
    """Zacchæus in Jericho: stage='climb' the street under the palms thronged with the crowd, a great sycomore by the way and
    a little man in crimson-brown up among its branches; 'call' Jesus come to the place, looking up, his hand lifted to him;
    'house' Zacchæus' fine house with its door open, Jesus going in with him, the crowd murmuring behind; 'stood' Zacchæus
    standing before Jesus with his hands spread, a bag of money held out."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.66, seed, hmin=0.26, hmax=0.4), pavement(w, h, h * 0.66)]
    for x in (0.06, 0.94):
        o.append(f'<g transform="translate({f(w * x)} {f(h * 0.7)}) scale({f(max(0.4, h / 600))})">' + J1.palm(0, 0, 1) + '</g>')
    s = fit(b, max(h * 0.24, b - 230))
    if stage in ("climb", "call"):
        tx = w * 0.66
        k = max(0.6, h / 360)
        o.append(f'<path d="M{f(tx)} {f(b)} C {f(tx - 10 * k)} {f(b - 80 * k)} {f(tx + 6 * k)} {f(b - 120 * k)} {f(tx)} {f(b - 150 * k)} M{f(tx)} {f(b - 120 * k)} L {f(tx - 70 * k)} {f(b - 170 * k)} '
                 f'M{f(tx)} {f(b - 130 * k)} L {f(tx + 76 * k)} {f(b - 176 * k)}" stroke="#6A5040" stroke-width="{f(14 * k)}" fill="none" stroke-linecap="round"></path>')
        rr = random.Random(seed)
        for _ in range(16):
            lx, ly = tx + rr.uniform(-110, 110) * k, b - rr.uniform(150, 230) * k
            o.append(f'<ellipse cx="{f(lx)}" cy="{f(ly)}" rx="{f(26 * k)}" ry="{f(14 * k)}" fill="{rr.choice(["#3F7A34", "#4A8A3A", "#2E6A2A"])}" stroke="{INK}" stroke-width="1.4"></ellipse>')
        o.append(zacchaeus_fig(p, tx + 30 * k, b - 150 * k, s * 0.7, flip=True, up=[(-22, -158), (-40, -176), (-50, -196)]))
        if stage == "climb":
            o.append(crowd(p, w * 0.02, w * 0.56, b, b - 190 * s, 9, seed, flip=None))
        else:
            o.append(jesus(p, tx - 60 * k - 40 * s, b, s, flip=True, up=[(-22, -158), (-40, -190), (-50, -222)]))
            o.append(crowd(p, w * 0.02, w * 0.36, b, b - 190 * s, 5, seed, flip=True))
    elif stage == "house":
        o.append(f'<rect x="{f(w * 0.54)}" y="{f(h * 0.16)}" width="{f(w * 0.44)}" height="{f(b - h * 0.16)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2.4"></rect>'
                 f'<rect x="{f(w * 0.52)}" y="{f(h * 0.12)}" width="{f(w * 0.48)}" height="10" fill="{GOLD}" stroke="{INK}" stroke-width="2"></rect>'
                 f'<path d="M{f(w * 0.68)} {f(b)} L {f(w * 0.68)} {f(b - h * 0.42)} Q {f(w * 0.76)} {f(b - h * 0.52)} {f(w * 0.84)} {f(b - h * 0.42)} L {f(w * 0.84)} {f(b)} Z" fill="#FFC14D" stroke="{INK}" stroke-width="2"></path>')
        o.append(zacchaeus_fig(p, w * 0.7, b, s, flip=False, up=UP_BLESS) + jesus(p, w * 0.58, b, s, flip=True))
        o.append(crowd(p, w * 0.02, w * 0.42, b, b - 190 * s, 6, seed, flip=True))
    else:
        o.append(glow(w * 0.5, b - 110 * s, 150 * s, "#FFF4C2", 0.6, f"{p}g"))
        o.append(jesus(p, w * 0.34, b, s, flip=True))
        o.append(zacchaeus_fig(p, w * 0.56, b, s, up=[(-22, -158), (-46, -150), (-62, -144)])
                 + f'<path d="M{f(w * 0.56 - 50 * s * 0.8)} {f(b - 118 * s * 0.8)} C {f(w * 0.56 - 60 * s * 0.8)} {f(b - 96 * s * 0.8)} {f(w * 0.56 - 34 * s * 0.8)} {f(b - 96 * s * 0.8)} {f(w * 0.56 - 40 * s * 0.8)} {f(b - 118 * s * 0.8)} Z" fill="#8A6A3A" stroke="{INK}" stroke-width="1.6"></path>')
        o.append(disciple(p, w * 0.16, b, s * 0.94, "peter") + disciple(p, w * 0.8, b, s * 0.92, "john", flip=True))
    return "".join(o)

def nobleman(p, w, h, seed, stage="go"):
    """A certain nobleman went into a far country, to receive for himself a kingdom: stage='go' at the door of his house the
    nobleman, robed and ready for the journey, giving a pound to each of his ten servants; 'napkin' the third servant before
    the throne holding out one pound folded in a napkin."""
    b = h * 0.92
    s = fit(b, max(h * 0.2, b - 230))
    if stage == "go":
        o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#8A9A6A", amp=12, step=80),
             f'<rect x="{f(w * 0.02)}" y="{f(h * 0.2)}" width="{f(w * 0.3)}" height="{f(b - h * 0.2)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2.4"></rect>', ground(w, h, b, "#B8A06A", dy=0)]
        o.append(rich_fig(p, w * 0.24, b, s, flip=True, up=UP_BLESS) + N.ass(w * 0.08, b, s * 0.7))
        for i in range(10):
            o.append(man(p, w * (0.38 + 0.06 * i), b - (i % 2) * 6, s * (0.86 - 0.01 * i), HEB[i % len(HEB)]))
    else:
        o = [king_hall(p, w, h, seed, kneel=False)]
        o.append(man(p, w * 0.6, b, s * 0.94, "#5A4A3A", up=[(-22, -158), (-44, -146), (-62, -140)])
                 + f'<rect x="{f(w * 0.6 - 74 * s)}" y="{f(b - 150 * s)}" width="{f(26 * s)}" height="{f(16 * s)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>')
    return "".join(o)

def wept_city(p, w, h, seed):
    """When he drew nigh, he saw the city and wept over it: on the descent of the mount of Olives, Jesus seen from behind on
    the colt, still, the city and the temple bright across the Kidron valley, the disciples standing quiet about him."""
    b = h * 0.96
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A9A", "#FFD8A0")]
    o.append(hills(w, h, h * 0.5, seed, color="#8A8A7A", amp=10, step=80))
    o.append(walls(w * 0.14, w * 0.9, h * 0.58, h * 0.22, seed, towers=4) + temple(w * 0.56, h * 0.4, w * 0.3))
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.72)} C {f(w * 0.3)} {f(h * 0.68)} {f(w * 0.7)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.76)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A9A5A" stroke="{INK}" stroke-width="2.4"></path>')
    s = fit(b, max(h * 0.3, b - 230))
    o.append(jesus_riding(p, w * 0.46, b, s))
    o.append(disciple(p, w * 0.22, b, s * 0.94, "peter") + disciple(p, w * 0.72, b, s * 0.92, "john", flip=True) + disciple(p, w * 0.84, b, s * 0.9, "james", flip=True))
    return "".join(o)

def temple_teaching(p, w, h, seed, watchers=True):
    """He was teaching daily in the temple: under Solomon's porch, Jesus seated teaching, the people sitting and standing close
    about him hanging upon his words; watchers=True: chief priests and scribes standing apart at the side, watching."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bgr(w, h, "#C8B490"), f'<rect x="-10" y="{f(h * 0.06)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>']
    for x in (0.04, 0.24, 0.44, 0.64, 0.84):
        o.append(f'<rect x="{f(w * x - 12)}" y="{f(h * 0.12)}" width="24" height="{f(b - h * 0.12)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(w * x - 18)}" y="{f(h * 0.12)}" width="36" height="9" fill="{GOLD}" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(f'<rect x="-10" y="{f(b - h * 0.05)}" width="{f(w + 20)}" height="{f(h)}" fill="#B8A07A" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.2, b - 230))
    o.append(glow(w * 0.3, b - 80 * s, 120 * s, "#FFF4C2", 0.5, f"{p}g") + jesus_seated(w * 0.3, b, s * 0.86))
    r = random.Random(seed)
    for i, x in enumerate((0.1, 0.48, 0.58)):
        c = r.choice(HEB)
        o.append(seated(w * x, b, s * 0.76, c, head=r.choice([c, "#E8E2D6", None]), beard=r.choice(["#2A1A10", "#6A645E", None]), flip=x > 0.3))
    o.append(crowd(p, w * 0.42, w * 0.68, b - 4, b - 4 - 190 * s, 3, seed, flip=True))
    if watchers:
        o.append(scribe_fig(p, w * 0.82, b, s, white=True, flip=True) + scribe_fig(p, w * 0.92, b, s * 0.98, flip=True))
    return "".join(o)
