"""Drawings for Job 29–31 (the months of old, the derision of the young, and Job's oath of clearing), and the desert
creatures: ostrich() and jackal()."""
from job.art8 import *
from job.art8 import f, K2, K3, sea, label, SHIELD
import samuel2 as S2

def ostrich(x, y, s=1.0, flip=False, run=False):
    """An ostrich standing (or running), facing right; (x, y) = the ground under it; about 200 units tall at s=1."""
    sx = -s if flip else s
    legs = ('<path d="M-6 -86 L -20 -40 L -10 0 M8 -86 L 26 -44 L 34 -2" stroke="#C88A6A" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"></path>' if run else
            '<path d="M-6 -86 L -10 -44 L -6 0 M8 -86 L 12 -44 L 16 0" stroke="#C88A6A" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"></path>')
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">' + legs
            + '<path d="M-6 0 l -12 2 M16 0 l 12 2 M-6 0 l 8 2" stroke="#C88A6A" stroke-width="4" stroke-linecap="round"></path>'
            + P("M-56 -112 C -60 -140 -30 -150 0 -146 C 30 -144 44 -130 40 -110 C 34 -90 0 -82 -30 -88 C -46 -92 -54 -100 -56 -112 Z", "#1A1614", 2.2)
            + P("M-56 -112 C -74 -116 -80 -100 -70 -92 C -64 -100 -60 -104 -50 -100 Z", "#F3EFE6", 1.6)
            + '<path d="M-40 -130 C -30 -136 -10 -138 6 -132" stroke="#4A4440" stroke-width="2" fill="none"></path>'
            + '<path d="M30 -136 C 36 -160 30 -190 40 -206" stroke="#0D0D0F" stroke-width="10" fill="none" stroke-linecap="round"></path><path d="M30 -136 C 36 -160 30 -190 40 -206" stroke="#D8A08A" stroke-width="7" fill="none" stroke-linecap="round"></path>'
            + P("M34 -214 C 40 -222 52 -220 56 -212 L 66 -208 L 54 -204 C 48 -200 38 -202 34 -208 Z", "#C8A08A", 1.6)
            + '<circle cx="46" cy="-212" r="2" fill="#0D0D0F"></circle></g>')

def jackal(x, y, s=1.0, flip=False, howl=False):
    """A jackal standing (howl=True: head raised), facing right; about 70 units tall at s=1."""
    sx = -s if flip else s
    head = ("M36 -50 L 44 -74 L 50 -60 L 56 -76 L 60 -56 L 70 -48 L 52 -40 Z" if howl else "M36 -46 L 42 -64 L 48 -54 L 54 -66 L 56 -48 L 76 -40 L 54 -32 Z")
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            + '<path d="M-30 -30 L -34 0 M-20 -28 L -18 0 M24 -28 L 22 0 M32 -30 L 36 0" stroke="#0D0D0F" stroke-width="5" stroke-linecap="round"></path>'
            + P("M-40 -40 C -40 -52 -20 -54 0 -52 C 20 -50 34 -50 40 -44 L 44 -36 C 40 -28 20 -26 -10 -26 C -30 -26 -40 -30 -40 -40 Z", "#B8905A", 2)
            + P("M-40 -40 C -56 -36 -64 -24 -60 -14 C -54 -24 -48 -30 -40 -34 Z", "#8A6A3A", 1.6) + P(head, "#B8905A", 2) + '</g>')

def past_tent(p, w, h, seed):
    """Oh that I were as in the months of old, when his lamp shined upon my head, and my children were about me: Job in white
    at his tent door in the evening of his prosperity, a lamp lit over the door, his sons and daughters about him."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A3A6A", "#F3B87A"), hills(w, h, h * 0.78, seed, "#6A5A5A", amp=8, step=90), ground(w, h, h * 0.84, "#B8A06A", dy=0),
         A.black_tent(w * 0.06, h * 0.94, w * 0.34, h * 0.18, color="#3A2A22")]
    o.append(f'<circle cx="{f(w * 0.24)}" cy="{f(h * 0.8)}" r="{f(h * 0.06)}" fill="#FFE680" opacity="0.35"></circle>' + E.flame(w * 0.24, h * 0.8, 6, 14, 0.1))
    s = fit(h * 0.97, h * 0.74)
    o.append(mk.person(p, round(w * 0.46), round(h * 0.97), s, body=SKIN, cloth=JOB_C, sw=3, extra=A.headcloth("#F3EFE6", cord=None) + BAND + GREY_BEARD))
    cl = ["#7A2A3A", "#2C4A7A", "#C8506A", "#5A6A2A", "#D8A040", "#3A5A6A", "#8A5AB8", "#6A3A5A", "#7A5A2A", "#4A3A2A"]
    for i in range(10):
        x = w * (0.56 + (i % 5) * 0.085) + (i // 5) * 20; y = h * (0.94 + (i // 5) * 0.03); k = s * (0.82 + (i // 5) * 0.08)
        o.append(woman(p, x, y, k * 0.95, cl[i]) if i in (2, 4, 6) else man(p, x, y, k, cl[i]))
    return "".join(o)

def gate_seat(p, w, h, seed):
    """When I went forth to the gate unto the city and prepared my seat in the street, the aged rose up and stood, the
    princes laid their hand on their mouth: the gate of the city, Job in white seated in the street before it, the elders
    standing about him."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB8D8", "#F3E0B0"), S4.gatehouse(w * 0.5, h * 0.86, w * 0.5, h * 0.4), ground(w, h, h * 0.86, "#C8A87A", dy=0)]
    k = min(1.0, (h * 0.22) / 135)
    o.append(f'<rect x="{f(w * 0.43)}" y="{f(h * 0.93)}" width="{f(w * 0.14)}" height="{f(h * 0.04)}" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(seated(w * 0.48, h * 0.94, k, JOB_C, head="#F3EFE6", band=True))
    s = fit(h * 0.97, h * 0.74)
    for i, x in enumerate((0.12, 0.22, 0.32, 0.68, 0.78, 0.88)):
        o.append(mk.person(p, round(w * x), round(h * 0.97), s, body=SKIN, cloth=["#5A4A6A", "#6A5A3A", "#3A5A5A", "#7A3A2A", "#4A4A6A", "#5A6A4A"][i], sw=3, flip=x > 0.5,
                           extra=A.headcloth(["#5A4A6A", "#6A5A3A", "#3A5A5A", "#7A3A2A", "#4A4A6A", "#5A6A4A"][i]) + A.WHITE_BEARD))
    return "".join(o)

def helper(p, w, h, seed):
    """I was eyes to the blind, and feet was I to the lame; I caused the widow's heart to sing for joy: Job in white leading a
    blind man by the hand, a lame man leaning on his staff beside them, a widow with her child holding bread."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.84, "#C8B07A", dy=0)]
    s = fit(h * 0.97, h * 0.74)
    o.append(mk.person(p, round(w * 0.38), round(h * 0.97), s, body=SKIN, cloth=JOB_C, sw=3, up=[(22, -158), (40, -130), (62, -126)], extra=A.headcloth("#F3EFE6", cord=None) + BAND + GREY_BEARD))
    o.append(man(p, w * 0.5, h * 0.97, s * 0.95, "#6A5A4A", extra='<path d="M-14 -176 L 14 -176" stroke="#E8E2D6" stroke-width="5"></path>'))
    o.append(man(p, w * 0.22, h * 0.97, s * 0.9, "#5A4A3A", extra='<path d="M-50 -150 L -46 6" stroke="#5A3A22" stroke-width="5"></path>'))
    o.append(mk.person(p, round(w * 0.74), round(h * 0.97), s * 0.94, body=SKIN, cloth="#2A2A30", woman=True, hair="#1A1210", sw=3, flip=True)
             + mk.person(p, round(w * 0.82), round(h * 0.97), round(s * 0.55, 3), body=SKIN, cloth="#7A5A3A", kind="Tunic", sw=3, flip=True)
             + f'<ellipse cx="{f(w * 0.7)}" cy="{f(h * 0.97 - 110 * s)}" rx="{f(12 * s * 2)}" ry="{f(5 * s * 2)}" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    return "".join(o)

def dew_tree(w, h, seed):
    """My root is spread out to the waters, and the dew lieth all night upon my branch; my bow is renewed in my hand: a green
    tree by a stream at dawn, dew shining on its leaves, a bow hung on its branch."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#5A6A9A", "#F3D8B0"), ground(w, h, h * 0.86, "#7A9A4A", dy=0),
         f'<path d="M-10 {f(h * 0.97)} C {f(w * 0.3)} {f(h * 0.93)} {f(w * 0.6)} {f(h * 0.99)} {f(w + 10)} {f(h * 0.95)}" stroke="#8FD0E2" stroke-width="12" fill="none"></path>']
    tx = w * 0.5
    o.append(f'<path d="M{f(tx)} {f(h * 0.94)} L {f(tx)} {f(h * 0.82)}" stroke="#5A3A1E" stroke-width="14"></path>'
             f'<ellipse cx="{f(tx)}" cy="{f(h * 0.8)}" rx="{f(w * 0.18)}" ry="{f(h * 0.07)}" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
             f'<path d="M{f(tx - 20)} {f(h * 0.94)} C {f(tx - 60)} {f(h * 0.97)} {f(tx - 90)} {f(h * 0.96)} {f(tx - 120)} {f(h * 0.97)} M{f(tx + 20)} {f(h * 0.94)} C {f(tx + 60)} {f(h * 0.97)} {f(tx + 80)} {f(h * 0.96)} {f(tx + 110)} {f(h * 0.98)}" stroke="#5A3A1E" stroke-width="4" fill="none"></path>')
    for i in range(20):
        o.append(f'<circle cx="{f(tx + r.uniform(-0.16, 0.16) * w)}" cy="{f(h * r.uniform(0.75, 0.85))}" r="2" fill="#E8F6FA"></circle>')
    o.append(f'<path d="M{f(tx + w * 0.1)} {f(h * 0.82)} C {f(tx + w * 0.14)} {f(h * 0.86)} {f(tx + w * 0.14)} {f(h * 0.9)} {f(tx + w * 0.1)} {f(h * 0.94)}" stroke="#8A5A30" stroke-width="4" fill="none"></path>'
             f'<path d="M{f(tx + w * 0.1)} {f(h * 0.82)} L {f(tx + w * 0.1)} {f(h * 0.94)}" stroke="#E8E2D6" stroke-width="1.2"></path>')
    return "".join(o)

def outcasts(p, w, h, seed):
    """They dwell in frightful valleys, in holes of the earth and of the rocks; among the bushes they bray: a stony ravine with
    caves in its walls, gaunt figures gathered under the bushes, one gnawing a root."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A4A4A", "#C8A080"),
         P(f"M-10 {f(h + 10)} L -10 {f(h * 0.66)} L {f(w * 0.3)} {f(h * 0.72)} L {f(w * 0.36)} {f(h + 10)} Z", "#6A5444"),
         P(f"M{f(w + 10)} {f(h + 10)} L {f(w + 10)} {f(h * 0.64)} L {f(w * 0.68)} {f(h * 0.7)} L {f(w * 0.62)} {f(h + 10)} Z", "#5A4434"),
         ground(w, h, h * 0.94, "#8A7458", dy=0)]
    for x, y in ((0.1, 0.82), (0.22, 0.9), (0.84, 0.8)):
        o.append(f'<ellipse cx="{f(w * x)}" cy="{f(h * y)}" rx="{f(w * 0.04)}" ry="{f(h * 0.04)}" fill="#120A08" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    o.append(E.bush(w * 0.5, h * 0.96, w * 0.14, h * 0.12, seed, flames=False))
    k = min(0.9, h / 420)
    for i, x in enumerate((0.42, 0.5, 0.58)):
        o.append(E.kneel(w * x, h * 0.97, k * 0.28, color=["#5A4A3A", "#4A4038", "#6A5A4A"][i], skin="#3A1E14", flip=i == 2))
    return "".join(o)

def jackals_ostriches(w, h, seed):
    """I am a brother to jackals, and a companion to ostriches: the waste at dusk, two jackals howling on a rock, ostriches
    stalking over the sand."""
    o = [K2.sky(w, h, "#2A2A4A", "#E8906A"), mk.stars(20, w, h * 0.4, seed), ground(w, h, h * 0.88, "#C8A06A", dy=0),
         P(f"M{f(w * 0.06)} {f(h * 0.92)} L {f(w * 0.1)} {f(h * 0.84)} L {f(w * 0.3)} {f(h * 0.83)} L {f(w * 0.34)} {f(h * 0.92)} Z", "#7A6A5A")]
    k = min(1.0, h / 330)
    o.append(jackal(w * 0.12, h * 0.84, k * 0.7, howl=True) + jackal(w * 0.4, h * 0.95, k * 0.6, flip=True))
    o.append(ostrich(w * 0.62, h * 0.97, k * 0.5) + ostrich(w * 0.8, h * 0.96, k * 0.44, flip=True) + ostrich(w * 0.94, h * 0.95, k * 0.36))
    return "".join(o)

def harp_mourning(w, h, seed):
    """My harp is turned to mourning, and my pipe into the voice of them that weep: a harp with broken strings and a pipe
    lying on sackcloth in the ashes."""
    o = [rect(w, h, "#2A2430"), ground(w, h, h * 0.86, "#4A4440", dy=0), ash_mound(w * 0.5, h * 0.99, w * 0.7, h * 0.08, seed),
         P(f"M{f(w * 0.24)} {f(h * 0.96)} L {f(w * 0.74)} {f(h * 0.94)} L {f(w * 0.76)} {f(h * 0.98)} L {f(w * 0.22)} {f(h * 1.0)} Z", SACK)]
    o.append(S2.harp(w * 0.42, h * 0.94, min(1.0, h / 300), rot=-70))
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.95)} L {f(w * 0.72)} {f(h * 0.92)}" stroke="#8A6A3A" stroke-width="6" stroke-linecap="round"></path>'
             + "".join(f'<circle cx="{f(w * (0.6 + i * 0.03))}" cy="{f(h * (0.94 - i * 0.006))}" r="1.6" fill="#2A1A10"></circle>' for i in range(4)))
    return "".join(o)

def hand_mill(w, h, seed):
    """Then let my wife grind unto another: a hand-mill of two round stones in a doorway, the grain beside it, the door
    standing open on the dark (no one is drawn)."""
    o = [rect(w, h, "#5A4A3A"), P(f"M{f(w * 0.56)} {f(h * 0.5)} L {f(w * 0.8)} {f(h * 0.5)} L {f(w * 0.8)} {f(h * 0.9)} L {f(w * 0.56)} {f(h * 0.9)} Z", "#120A08"), ground(w, h, h * 0.9, "#3A2A20", dy=0)]
    k = min(1.4, h / 260); x, y = w * 0.3, h * 0.96
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})">' + P("M-60 0 L -60 -16 C -60 -26 60 -26 60 -16 L 60 0 Z", "#7A7068") + '<ellipse cx="0" cy="-20" rx="60" ry="10" fill="#8A8078" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             + P("M-48 -24 L -48 -40 C -48 -48 48 -48 48 -40 L 48 -24 Z", "#9A9088") + '<ellipse cx="0" cy="-42" rx="48" ry="8" fill="#A8A098" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             + '<circle cx="0" cy="-42" r="6" fill="#3A3028"></circle><path d="M30 -42 L 34 -70" stroke="#5A3A1E" stroke-width="5"></path></g>')
    o.append(P(f"M{f(w * 0.08)} {f(h * 0.96)} C {f(w * 0.1)} {f(h * 0.9)} {f(w * 0.16)} {f(h * 0.9)} {f(w * 0.18)} {f(h * 0.96)} Z", "#E8C070"))
    return "".join(o)

def sharing(p, w, h, seed):
    """If I have eaten my morsel alone, and the fatherless hath not eaten thereof; if he hath not been warmed with the fleece of
    my sheep: Job in white giving bread to a fatherless child, a poor man wrapped in a fleece beside them."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E8A06A", "#F3D8A0"), ground(w, h, h * 0.84, "#B8A06A", dy=0), house(w * 0.72, h * 0.9, w * 0.2, h * 0.14, lit=True)]
    s = fit(h * 0.97, h * 0.74)
    o.append(mk.person(p, round(w * 0.34), round(h * 0.97), s, body=SKIN, cloth=JOB_C, sw=3, up=[(22, -158), (44, -128), (66, -124)], extra=A.headcloth("#F3EFE6", cord=None) + BAND + GREY_BEARD)
             + f'<ellipse cx="{f(w * 0.34 + 70 * s)}" cy="{f(h * 0.97 - 124 * s)}" rx="{f(14 * s)}" ry="{f(6 * s)}" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    o.append(mk.person(p, round(w * 0.46), round(h * 0.97), round(s * 0.55, 3), body=SKIN, cloth="#7A5A3A", kind="Tunic", sw=3, flip=True, up=[(22, -158), (-10, -190), (-26, -214)]))
    o.append(man(p, w * 0.58, h * 0.97, s * 0.95, "#E8E2D6", flip=True, extra='<path d="M-30 -150 C -36 -100 -30 -40 -26 -10 L 30 -10 C 34 -60 34 -120 26 -150 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></path>'))
    return "".join(o)

def sun_moon(w, h, seed):
    """If I have beheld the sun when it shined, or the moon walking in brightness, and my heart hath been secretly enticed:
    the sun going down in the west and the full moon rising in the east over the same hills."""
    o = [f'<defs><linearGradient id="sm{seed}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#F3B87A"></stop><stop offset="1" stop-color="#2A2A5A"></stop></linearGradient></defs>'
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#sm{seed})"></rect>', sun(w * 0.16, h * 0.82, min(30, h * 0.08), color="#FF8A3D", op=0.35),
         J.moon(w * 0.84, h * 0.72, min(24, h * 0.07)), mk.stars(30, w * 0.4, h * 0.7, seed).replace("<g ", f'<g transform="translate({f(w * 0.6)} 0)" '),
         hills(w, h, h * 0.86, seed, "#3A2A3A", amp=10, step=80)]
    return "".join(o)

def open_door(p, w, h, seed):
    """The sojourner hath not lodged in the street; but I have opened my doors to the traveller: a house at night with its door
    wide and lamplight pouring out, a traveller with his staff coming up to it."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#0B0B2A", "#2A2A4A"), mk.stars(50, w, h * 0.6, seed), ground(w, h, h * 0.86, "#3A3028", dy=0)]
    hx, hw, hh = w * 0.18, w * 0.34, h * 0.24
    o.append(P(f"M{f(hx)} {f(h * 0.94)} L {f(hx)} {f(h * 0.94 - hh)} L {f(hx + hw)} {f(h * 0.94 - hh)} L {f(hx + hw)} {f(h * 0.94)} Z", "#8A7058")
             + P(f"M{f(hx + hw * 0.6)} {f(h * 0.94)} L {f(hx + hw * 0.6)} {f(h * 0.94 - hh * 0.62)} L {f(hx + hw * 0.84)} {f(h * 0.94 - hh * 0.62)} L {f(hx + hw * 0.84)} {f(h * 0.94)} Z", "#FFC14D")
             + f'<path d="M{f(hx + hw * 0.84)} {f(h * 0.94)} L {f(w * 0.84)} {f(h * 1.0)} L {f(w * 0.6)} {f(h * 1.0)} Z" fill="#FFC14D" opacity="0.3"></path>')
    s = fit(h * 0.97, h * 0.74)
    o.append(man(p, w * 0.7, h * 0.97, s, "#5A4A6A", flip=True, extra='<path d="M-50 -170 L -46 6" stroke="#5A3A22" stroke-width="5"></path>'))
    return "".join(o)

def signature(w, h, seed):
    """Lo, here is my signature, let the Almighty answer me; I would bind it unto me as a crown: Job's written cause, a scroll
    tied with a cord, its end marked with his sign, a cross-stroke cut deep."""
    o = [rect(w, h, "#3A2A2A"), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.86)}" r="{f(h * 0.3)}" fill="#FFC14D" opacity="0.12"></circle>']
    x0, x1, y0, y1 = w * 0.16, w * 0.84, h * 0.72, h * 0.94
    o.append(P(f"M{f(x0)} {f(y0)} L {f(x1)} {f(y0)} L {f(x1)} {f(y1)} L {f(x0)} {f(y1)} Z", "#E8D8B0"))
    for k in range(4): o.append(f'<path d="M{f(x0 + 20)} {f(y0 + 14 + k * 14)} L {f(x0 + (x1 - x0) * 0.62)} {f(y0 + 14 + k * 14)}" stroke="#8A6A4A" stroke-width="2"></path>')
    cx, cy = x0 + (x1 - x0) * 0.8, (y0 + y1) / 2
    o.append(f'<path d="M{f(cx - 16)} {f(cy - 16)} L {f(cx + 16)} {f(cy + 16)} M{f(cx + 16)} {f(cy - 16)} L {f(cx - 16)} {f(cy + 16)}" stroke="#B5121B" stroke-width="6" stroke-linecap="round"></path>'
             f'<ellipse cx="{f(x0)}" cy="{f(cy)}" rx="10" ry="{f((y1 - y0) / 2 + 4)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<path d="M{f(x0 - 10)} {f(cy)} C {f(x0 - 40)} {f(cy + 10)} {f(x0 - 30)} {f(cy + 30)} {f(x0 - 50)} {f(cy + 34)}" stroke="#5A3A1E" stroke-width="3" fill="none"></path>')
    return "".join(o)

def thistles(w, h, seed):
    """If my land crieth out against me: let thistles grow instead of wheat, and cockle instead of barley: a field gone to
    thistles and cockle, a few stalks of wheat among them, the furrows dark as with weeping."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#7A7A8A", "#D8C8A0"), ground(w, h, h * 0.8, "#6A5A3A", dy=0)]
    for i in range(6): o.append(f'<path d="M-10 {f(h * (0.84 + i * 0.03))} L {f(w + 10)} {f(h * (0.82 + i * 0.03))}" stroke="#3A2A1A" stroke-width="2"></path>')
    for i in range(30):
        x = r.uniform(0, w); y = h * r.uniform(0.84, 1.0); s = r.uniform(0.6, 1.1) * min(1.3, h / 300)
        if i % 5 == 0:
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 40 * s)}" stroke="#B89A3A" stroke-width="2"></path><ellipse cx="{f(x)}" cy="{f(y - 44 * s)}" rx="3" ry="8" fill="#E8C050"></ellipse>')
        else:
            o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M0 0 L -4 -30 M0 0 L 2 -36 M0 0 L 8 -26" stroke="#3A4A22" stroke-width="2.4" fill="none"></path>'
                     f'<circle cx="2" cy="-38" r="5" fill="{["#8A4A8A", "#C85A8A"][i % 2]}" stroke="#0D0D0F" stroke-width="1.2"></circle></g>')
    return "".join(o)

def breach(w, h, seed):
    """As through a wide breach they come; in the midst of the ruin they roll themselves upon me: a town wall broken down in
    the middle, its stones fallen in a heap, dust rising."""
    return "".join([K2.sky(w, h, "#5A4A5A", "#C8A080"), J.jericho(-10, w * 0.3, h * 0.56, h * 0.9, seed, towers=1, houses=True),
                    J.collapse(w * 0.3, w * 0.74, h * 0.9, h * 0.3, seed, color="#B5652E"), J.jericho(w * 0.74, w + 10, h * 0.56, h * 0.9, seed + 1, towers=1, houses=True),
                    ground(w, h, h * 0.9, "#4A3A30", dy=0)])
