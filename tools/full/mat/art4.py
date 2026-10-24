"""Drawings for Matthew 11–12: John in the prison and his messengers; a reed shaken with the wind; the children in the
marketplace; the cities of the lake under a heavy sky; the yoke; the grainfields on the sabbath; the withered hand
stretched forth in the synagogue; the sheep in the pit; the Pharisees taking counsel; the bruised reed and the smoking
flax; the strong man's house; the sign of Jonah (jon.art) and the queen of the south (kg1.art); the house empty, swept
and garnished (no spirit drawn); his mother and his brethren at the door. Built on mat.art3."""
from mat.art3 import *
from mat.art3 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, centurion_fig, road_scene, LIE
from ntcast import JESUS_SKIN, JESUS_HAIR, JESUS_TUNIC, JESUS_MANTLE, ROBES
import random, math
from job.art import seated, smoke
from samuel1 import cow
import exodus as E

def prison(p, w, h, seed):
    """John in the prison: the dark stone keep of a fortress on its hill, one barred window lit; two of his disciples on
    the road below, setting out."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A4A", "#C8906A"), hills(w, h, h * 0.56, seed, color="#4A3A3A", amp=14, step=80),
         f'<path d="M{f(w * 0.5)} {f(h * 0.7)} C {f(w * 0.56)} {f(h * 0.36)} {f(w * 0.86)} {f(h * 0.36)} {f(w * 0.96)} {f(h * 0.7)} Z" fill="#5A4A44" stroke="{INK}" stroke-width="2"></path>',
         f'<rect x="{f(w * 0.62)}" y="{f(h * 0.12)}" width="{f(w * 0.22)}" height="{f(h * 0.36)}" fill="#6A5A54" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.71)}" y="{f(h * 0.24)}" width="{f(w * 0.04)}" height="{f(h * 0.08)}" fill="#FFC14D" stroke="{INK}" stroke-width="1.6"></rect>'
         + "".join(f'<path d="M{f(w * (0.715 + 0.01 * k))} {f(h * 0.24)} L {f(w * (0.715 + 0.01 * k))} {f(h * 0.32)}" stroke="{INK}" stroke-width="2"></path>' for k in range(3)),
         ground(w, h, h * 0.74, "#6A5040", dy=0)]
    for k in range(5):
        x = w * (0.62 + 0.044 * k)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.1)}" width="{f(w * 0.026)}" height="{f(h * 0.03)}" fill="#6A5A54" stroke="{INK}" stroke-width="1.6"></rect>')
    s = fit(b, max(h * 0.3, b - 220))
    o.append(man(p, w * 0.22, b, s * 0.9, ROBES["baptist"], flip=True) + man(p, w * 0.32, b, s * 0.88, "#6A5A3A", flip=True))
    return "".join(o)

def reed(p, w, h, seed):
    """A reed shaken with the wind: the reeds of the Jordan bending in a hard wind under a wide sky, the wilderness behind."""
    from ecc.art import wind_lines
    r = random.Random(seed)
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#C8A06A", amp=18, step=80),
         f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.58)} {f(w * 0.6)} {f(h * 0.66)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.76)} L -10 {f(h * 0.78)} Z" fill="#2C7DA8" stroke="{INK}" stroke-width="2"></path>',
         ground(w, h, h * 0.76, "#7A9A4A", dy=0), wind_lines(w, h, seed, n=10, color="#F3EFE6", op=0.6, y0=0.1, y1=0.7)]
    for i in range(26):
        x = r.uniform(0, w); hh = r.uniform(0.25, 0.6) * h; bend = r.uniform(0.25, 0.45) * hh
        o.append(f'<path d="M{f(x)} {f(h + 4)} C {f(x + bend * 0.2)} {f(h - hh * 0.5)} {f(x + bend * 0.7)} {f(h - hh * 0.8)} {f(x + bend)} {f(h - hh)}" stroke="#5A7A2A" stroke-width="3" fill="none"></path>'
                 f'<ellipse cx="{f(x + bend)}" cy="{f(h - hh)}" rx="{f(10)}" ry="4" fill="#8A6A3A" transform="rotate(-30 {f(x + bend)} {f(h - hh)})"></ellipse>')
    return "".join(o)

def market_children(p, w, h, seed):
    """Children sitting in the marketplaces, calling to their fellows: a market square with its stalls and awnings, a child
    piping on a flute, others sitting with their backs turned."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.76, seed, hmin=0.34, hmax=0.5, stairs=False), pavement(w, h, h * 0.76)]
    for i, (x, c) in enumerate(((0.12, "#B5121B"), (0.78, "#1F5FAD"))):
        o.append(f'<path d="M{f(w * x - 60)} {f(h * 0.5)} L {f(w * x + 60)} {f(h * 0.5)} L {f(w * x + 70)} {f(h * 0.58)} L {f(w * x - 70)} {f(h * 0.58)} Z" fill="{c}" stroke="{INK}" stroke-width="2"></path>'
                 f'<path d="M{f(w * x - 56)} {f(h * 0.58)} L {f(w * x - 56)} {f(h * 0.8)} M{f(w * x + 56)} {f(h * 0.58)} L {f(w * x + 56)} {f(h * 0.8)}" stroke="#5A3A22" stroke-width="4"></path>')
    s = fit(b, max(h * 0.3, b - 220)) * 0.55
    pipe = '<path d="M16 -168 L 50 -150" stroke="#C8963E" stroke-width="5"></path>'
    o.append(mk.person(p, round(w * 0.4), round(b), round(s, 3), body=SKIN, cloth="#C8783A", kind="Tunic", sw=3, up=[(22, -158), (30, -156), (36, -154)], extra=pipe))
    r = random.Random(seed)
    for x in (0.52, 0.6, 0.68, 0.3):
        o.append(seated(w * x, b, s * 1.3, r.choice(HEB), head=None, beard="", flip=x < 0.4))
    return "".join(o)

def woe(p, w, h, seed):
    """Woe unto thee, Chorazin! woe unto thee, Bethsaida!: the towns along the lake under a heavy, storm-dark sky, a single
    shaft of evening light on the water."""
    o = [sky(w, h, "#1A1A2E", "#6A4A5A"), clouds(w, h * 0.2, seed, n=6, color="#3A3A4E", op=0.9, h=h),
         hills(w, h, h * 0.42, seed, color="#3A3A4A", amp=14, step=90), lake(w, h, h * 0.5, seed, color="#2A4A6A", deep="#14243A", n=8, op=0.4)]
    for x in (0.14, 0.46, 0.8):
        o.append(hill_town(w * x, h * 0.52, w * 0.16, h * 0.12, seed + int(x * 10), hill="#4A4048", color=("#8A7A6A", "#7A6A5A", "#9A8A7A")))
    o.append(shaft(w * 0.62, w, h, top_w=0.02, bot_w=0.08, color="#FFC14D", op=0.25))
    return "".join(o)

def yoke(p, w, h, seed):
    """Take my yoke upon you: two oxen under one wooden yoke, ploughing a furrow in the evening light, the plough behind."""
    b = h * 0.86
    o = [sky(w, h, "#5A3A6A", "#FFC890"), sun(w * 0.84, h * 0.46, 16, color="#FFE680", op=0.3), hills(w, h, h * 0.5, seed, color="#7A6A5A", amp=10, step=80),
         ground(w, h, h * 0.58, "#8A6A4A", dy=0)]
    for k in range(6):
        y = h * (0.62 + 0.06 * k)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y + 4)}" stroke="#6A4A30" stroke-width="2"></path>')
    k = max(0.5, (b - h * 0.4) / 150)
    o.append(cow(w * 0.44, b, k, color="#C8A07A", patch="#F3EFE6") + cow(w * 0.5, b + 8, k, color="#8A5A30", patch="#E8D8B8"))
    o.append(f'<path d="M{f(w * 0.44 + 50 * k)} {f(b - 100 * k)} L {f(w * 0.5 + 60 * k)} {f(b - 92 * k)}" stroke="#5A3A22" stroke-width="{f(8 * k)}" stroke-linecap="round"></path>')
    o.append(f'<path d="M{f(w * 0.44 - 60 * k)} {f(b - 50 * k)} L {f(w * 0.2)} {f(b - 40 * k)} L {f(w * 0.16)} {f(b + 6)} M{f(w * 0.2)} {f(b - 40 * k)} L {f(w * 0.14)} {f(b - 90 * k)}" stroke="#5A3A22" stroke-width="{f(5 * k)}" fill="none"></path>')
    return "".join(o)

def grainfield(p, w, h, seed, pharisees=True):
    """Through the grainfields on the sabbath: Jesus on the path between the tall ripe grain, the disciples plucking the
    ears; at the field's edge two Pharisees in white watching."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.36, seed, color="#9AAA7A", amp=12, step=90), ground(w, h, h * 0.44, "#D8B860", dy=0),
         grain(-10, w + 10, h * 0.62, h * 0.16, seed)]
    s = fit(b, max(h * 0.3, b - 220))
    o.append(jesus(p, w * 0.3, b, s))
    for i, (x, who) in enumerate(((0.44, "peter"), (0.54, "andrew"), (0.14, "john"))):
        o.append(disciple(p, w * x, b, s * 0.96, who, flip=x > 0.4, up=[(-22, -158), (-40, -150), (-58, -144)] if i < 2 else None))
    if pharisees:
        o.append(scribe_fig(p, w * 0.82, b, s * 0.96, white=True, flip=True) + scribe_fig(p, w * 0.92, b, s * 0.94, white=True, flip=True))
    o.append(grain(-10, w + 10, h * 1.02, h * 0.2, seed + 1))
    return "".join(o)

def withered(p, w, h, seed, restored=False):
    """In their synagogue, a man having a withered hand: the man standing out in the midst, his hand drawn in (restored:
    stretched forth), Jesus facing him, the Pharisees seated along the wall watching."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bgr(w, h, "#C8B490"), f'<rect x="-10" y="{f(h * 0.08)}" width="{f(w + 20)}" height="{f(h * 0.05)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>']
    for x in (0.06, 0.94):
        o.append(f'<rect x="{f(w * x - 14)}" y="{f(h * 0.13)}" width="28" height="{f(b - h * 0.13)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(b - h * 0.06)}" width="{f(w + 20)}" height="{f(h)}" fill="#A8906A" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.2, b - 230))
    for x in (0.66, 0.76, 0.86):
        o.append(seated(w * x, b, s * 0.8, "#E8E2D6", head="#F3EFE6", beard="#6A645E", band=True, flip=True))
    o.append(jesus(p, w * 0.22, b, s))
    arm = [(-22, -158), (-46, -152), (-70, -150)] if restored else [(-22, -158), (-26, -130), (-14, -118)]
    o.append(man(p, w * 0.44, b, s * 0.96, "#6A5A3A", flip=True, up=arm))
    if restored: o.append(glow(w * 0.44 - 70 * s, b - 150 * s, 40 * s, "#FFF4C2", 0.8, f"{p}g"))
    return "".join(o)

def sheep_pit(p, w, h, seed):
    """One sheep fallen into a pit: a man kneeling at the edge of a pit in the field, reaching down and lifting the sheep
    out by its fleece."""
    b = h * 0.8
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#9AAA7A", amp=10, step=80), ground(w, h, h * 0.5, "#9AAA5A", dy=0),
         f'<ellipse cx="{f(w * 0.56)}" cy="{f(b)}" rx="{f(w * 0.16)}" ry="{f(h * 0.08)}" fill="#3A2A1A" stroke="{INK}" stroke-width="2.4"></ellipse>']
    k = max(0.4, h / 400)
    o.append(E.sheep(w * 0.58, b + h * 0.02, k * 0.6))
    o.append(f'<ellipse cx="{f(w * 0.56)}" cy="{f(b + h * 0.06)}" rx="{f(w * 0.16)}" ry="{f(h * 0.04)}" fill="#9AAA5A"></ellipse>')
    o.append(E.kneel(w * 0.4, b - h * 0.02, fit(b, h * 0.4) * 0.8, color="#6A5A3A", skin=SKIN))
    o.append(sheep_row(w * 0.74, w * 0.96, h * 0.6, 3, seed, s=k * 0.5))
    return "".join(o)

def counsel(p, w, h, seed):
    """The Pharisees went out and took counsel against him: under a dark colonnade at dusk, a knot of men in white robes
    and headcloths, their heads together."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A2A", "#8A3A2A")]
    for x in (0.08, 0.3, 0.52, 0.74, 0.96):
        o.append(f'<rect x="{f(w * x - 16)}" y="{f(h * 0.1)}" width="32" height="{f(b - h * 0.1)}" fill="#5A4A44" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.02)}" width="{f(w + 20)}" height="{f(h * 0.08)}" fill="#4A3A34" stroke="{INK}" stroke-width="2"></rect>' + pavement(w, h, b - h * 0.04, color="#5A4A44", line="#4A3A34"))
    s = fit(b, max(h * 0.26, b - 220))
    for i, x in enumerate((0.34, 0.42, 0.5, 0.58, 0.66)):
        o.append(scribe_fig(p, w * x, b, s * (0.96 + 0.02 * (i % 2)), white=i % 2 == 0, flip=i > 2))
    return "".join(o)

def reed_flax(p, w, h, seed):
    """A bruised reed shall he not break, and smoking flax shall he not quench: a bent reed by still water, held upright by
    its stake; a lamp whose flax-wick only smokes, kept and not snuffed out — in a quiet dawn light."""
    o = [sky(w, h, "#3A3A6A", "#FFC890"), glow(w * 0.5, h * 0.6, h * 0.6, "#FFF4C2", 0.4, f"{p}g"),
         f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h)}" fill="#4A6A8A" stroke="{INK}" stroke-width="2"></rect>']
    rx = w * 0.3
    o.append(f'<path d="M{f(rx)} {f(h + 4)} L {f(rx)} {f(h * 0.4)} L {f(rx + w * 0.08)} {f(h * 0.5)}" stroke="#7A8A3A" stroke-width="5" fill="none"></path>'
             f'<path d="M{f(rx - 10)} {f(h + 4)} L {f(rx - 10)} {f(h * 0.34)}" stroke="#5A3A22" stroke-width="3"></path>'
             f'<path d="M{f(rx - 12)} {f(h * 0.46)} L {f(rx + 2)} {f(h * 0.46)}" stroke="#C8A878" stroke-width="3"></path>')
    k = max(0.8, h / 160)
    o.append(A.lamp(w * 0.68, h * 0.66, k).replace(E.flame(26, -4, 8, 22, 0.1), ""))
    o.append(f'<path d="M{f(w * 0.68 + 26 * k)} {f(h * 0.66 - 6 * k)} C {f(w * 0.68 + 18 * k)} {f(h * 0.5)} {f(w * 0.68 + 34 * k)} {f(h * 0.4)} {f(w * 0.68 + 24 * k)} {f(h * 0.26)}" stroke="#8A8498" stroke-width="3" fill="none"></path>'
             f'<circle cx="{f(w * 0.68 + 26 * k)}" cy="{f(h * 0.66 - 6 * k)}" r="{f(2.4 * k)}" fill="#FF8A3D"></circle>')
    return "".join(o)

def strong_house(p, w, h, seed):
    """The house of the strong man: a fortified house with a heavy door, its bar drawn back and the door open, the goods
    within carried out; ropes lying on the step."""
    b = h * 0.9
    o = [sky(w, h, "#3A3A5A", "#C8906A"), ground(w, h, b, "#6A5040", dy=0),
         f'<rect x="{f(w * 0.24)}" y="{f(h * 0.2)}" width="{f(w * 0.5)}" height="{f(b - h * 0.2)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.42)}" y="{f(h * 0.46)}" width="{f(w * 0.14)}" height="{f(b - h * 0.46)}" fill="#1A1210" stroke="{INK}" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.42)} {f(h * 0.46)} L {f(w * 0.36)} {f(h * 0.42)} L {f(w * 0.36)} {f(b + 4)} L {f(w * 0.42)} {f(b)} Z" fill="#5A3A22" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.3)} {f(h * 0.62)} L {f(w * 0.4)} {f(h * 0.6)}" stroke="#2A1A10" stroke-width="6"></path>']
    for k in range(4):
        x = w * (0.62 + 0.08 * k)
        o.append(f'<rect x="{f(x)}" y="{f(b - h * 0.08)}" width="{f(w * 0.05)}" height="{f(h * 0.08)}" fill="{["#E8B830", "#8A5A30", "#C8C0B0", "#7A2A5A"][k]}" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<path d="M{f(w * 0.3)} {f(b + 6)} c 20 -10 40 10 60 0 c 20 -10 30 6 50 0" stroke="#C8A878" stroke-width="4" fill="none"></path>')
    return "".join(o)

def jonah_sign(p, w, h, seed):
    """The sign of Jonah the prophet: three days and three nights in the belly of the great fish (jon.art.swallow)."""
    from jon import art as JA
    return JA.swallow(p, w, h, seed)

def nineveh(p, w, h, seed):
    """The men of Nineveh repented at the preaching of Jonah: Nineveh in sackcloth (jon.art)."""
    from jon import art as JA
    return JA.nineveh_great(p, w, h, seed, jonah=False, sack=True)

def queen_south(p, w, h, seed):
    """The queen of the south came from the ends of the earth to hear the wisdom of Solomon (kg1.art.sheba_train)."""
    from kg1 import art as KA
    return KA.sheba_train(p, w, h, seed)

def swept(p, w, h, seed):
    """He findeth it empty, swept, and garnished: an empty room swept clean, a garland hung over the door, the door standing
    open on the night — no one and nothing else drawn."""
    b = h * 0.9
    o = [bgr(w, h, "#C8B8A0"), f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#D8C8A8" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.6)}" y="{f(h * 0.24)}" width="{f(w * 0.18)}" height="{f(b - h * 0.24)}" fill="#0B0B1A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<g transform="translate({f(w * 0.6)} {f(h * 0.24)})">' + mk.stars(5, w * 0.18, h * 0.3, seed) + '</g>',
         f'<path d="M{f(w * 0.58)} {f(h * 0.22)} C {f(w * 0.62)} {f(h * 0.3)} {f(w * 0.76)} {f(h * 0.3)} {f(w * 0.8)} {f(h * 0.22)}" stroke="#3A7A2A" stroke-width="7" fill="none"></path>']
    for k in range(6):
        x = w * (0.6 + k * 0.04)
        o.append(f'<circle cx="{f(x)}" cy="{f(h * 0.26 + (1 - abs(k - 2.5) / 2.5) * h * 0.04)}" r="4" fill="#D7261E"></circle>')
    for k in range(7):
        o.append(f'<path d="M{f(w * (0.06 + k * 0.07))} {f(b + h * 0.03)} q {f(w * 0.02)} -4 {f(w * 0.04)} 0" stroke="#B8A888" stroke-width="2" fill="none"></path>')
    o.append(f'<path d="M{f(w * 0.12)} {f(b)} L {f(w * 0.2)} {f(h * 0.5)}" stroke="#8A6A3A" stroke-width="4"></path><path d="M{f(w * 0.08)} {f(b)} L {f(w * 0.16)} {f(b)} L {f(w * 0.12)} {f(b - h * 0.08)} Z" fill="#C8A060" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def waterless(p, w, h, seed):
    """Waterless places, seeking rest, and findeth it not: a dry wadi under the moon, cracked earth, dead thorns — empty."""
    r = random.Random(seed)
    o = [night(w, h, seed, n=40, top="#0B0B1A", bot="#3A2A3A"), moon(w * 0.8, h * 0.2, max(8, h * 0.04), color="#E8D8C8"),
         hills(w, h, h * 0.5, seed, color="#3A2A2A", amp=20, step=90), ground(w, h, h * 0.62, "#6A5040", dy=0)]
    for _ in range(14):
        x, y = r.uniform(0, w), r.uniform(h * 0.66, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-30, 30))} {f(r.uniform(-6, 6))} l {f(r.uniform(-20, 20))} {f(r.uniform(-6, 6))}" stroke="#3A2A1A" stroke-width="1.6" fill="none"></path>')
    return "".join(o)

def kindred(p, w, h, seed):
    """His mother and his brethren stood without: Jesus within the house among the disciples, his hand stretched toward
    them; at the open door outside, Mary and his brethren waiting."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#B8987A"),
         f'<rect x="{f(w * 0.74)}" y="{f(h * 0.2)}" width="{f(w * 0.26 + 10)}" height="{f(b - h * 0.2)}" fill="#8FD0E2" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.74)}" y="{f(b - h * 0.06)}" width="{f(w * 0.26 + 10)}" height="{f(h * 0.06)}" fill="#C8B07A"></rect>']
    s = fit(b, max(h * 0.2, b - 230))
    o.append(jesus(p, w * 0.34, b, s, up=UP_BLESS))
    for i, x in enumerate((0.12, 0.2, 0.48, 0.58)):
        o.append(disciple_seated(w * x, b, s * 0.7, i, flip=x > 0.4))
    o.append(mary_fig(p, w * 0.8, b, s * 0.9, flip=True))
    o.append(man(p, w * 0.88, b, s * 0.92, "#6A5A3A", flip=True) + man(p, w * 0.95, b, s * 0.9, "#5A4A6A", flip=True))
    return "".join(o)
