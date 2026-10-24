"""Drawings for Luke 7: the elders and the centurion's friends on the road at Capernaum; the gate of Nain — the bier carried
out at a distance, the widow in black among much people; Jesus touching the bier and the bearers standing still; the young
man sitting up on it, then given to his mother (no body ever drawn close: the bier is a covered shape far off); the two
messengers of John on the road; in the Pharisee's house, the woman that was a sinner kneeling veiled at his feet with the
alabaster cruse; the lender and his two debtors; go in peace. Built on luk.art3."""
from luk.art3 import *
from luk.art3 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch, \
    jesus_kneel, light_seated, WOMEN3, PURPLE, GOLD, kneel_w, boy_fig, zach_fig, elis_fig, shepherd_fig, swaddled, fish_heap
import random, math

WIDOW_C, WIDOW_V = "#3A3A42", "#1E1E26"
SINNER_C, SINNER_V = "#3A2A4A", "#2A2A4A"

def elders_ask(p, w, h, seed, friends=False):
    """Elders of the Jews beseeching him earnestly in the street of Capernaum, the synagogue that the centurion built behind
    them; friends=True: near the house, the centurion's friends come out to meet him on the road, the house with its Roman
    door beyond."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.84, seed, hmin=0.3, hmax=0.46), pavement(w, h, h * 0.84)]
    if not friends:
        sx = w * 0.7
        o.append(f'<rect x="{f(sx - w * 0.16)}" y="{f(h * 0.3)}" width="{f(w * 0.32)}" height="{f(h * 0.54)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2.4"></rect>'
                 f'<path d="M{f(sx - w * 0.18)} {f(h * 0.3)} L {f(sx)} {f(h * 0.2)} L {f(sx + w * 0.18)} {f(h * 0.3)} Z" fill="#C8B490" stroke="{INK}" stroke-width="2.2"></path>'
                 + "".join(f'<rect x="{f(sx + w * dx - 8)}" y="{f(h * 0.34)}" width="16" height="{f(h * 0.5)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>' for dx in (-0.12, -0.04, 0.04, 0.12)))
    else:
        o.append(f'<rect x="{f(w * 0.72)}" y="{f(h * 0.3)}" width="{f(w * 0.3)}" height="{f(h * 0.54)}" fill="#E8D8C8" stroke="{INK}" stroke-width="2.4"></rect>'
                 f'<rect x="{f(w * 0.8)}" y="{f(h * 0.52)}" width="{f(w * 0.1)}" height="{f(h * 0.32)}" fill="#8A2A1A" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.24, b - 240))
    o.append(jesus(p, w * 0.24, b, s) + disciple(p, w * 0.1, b, s * 0.95, "peter"))
    if friends:
        for i in range(3): o.append(man(p, w * (0.44 + 0.1 * i), b - i * 2, s * (0.96 - 0.02 * i), ["#5A6A7A", "#7A5A3A", "#4A5A4A"][i], flip=False, up=UP_BLESS if i == 0 else None))
    else:
        o.append(scribe_fig(p, w * 0.42, b, s * 0.96, flip=False, up=UP_BLESS) + scribe_fig(p, w * 0.53, b, s * 0.94, white=True, flip=True))
    return "".join(o)

def bier(x, b, s, up=False):
    """The bier carried out: a wooden litter on two poles, the one on it covered with a white linen cloth (no body shown);
    up=True: the young man sitting up on it, alive, in a sand tunic."""
    o = [f'<rect x="{f(x - 70 * s)}" y="{f(b - 10 * s)}" width="{f(140 * s)}" height="{f(8 * s)}" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>',
         f'<path d="M{f(x - 96 * s)} {f(b - 4 * s)} L {f(x + 96 * s)} {f(b - 4 * s)}" stroke="#4A2A1A" stroke-width="{f(4 * s)}"></path>']
    if up:
        o.append(f'<path d="M{f(x - 64 * s)} {f(b - 10 * s)} C {f(x - 60 * s)} {f(b - 26 * s)} {f(x - 10 * s)} {f(b - 26 * s)} {f(x)} {f(b - 12 * s)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></path>'
                 + seated(x + 10 * s, b - 10 * s, s * 0.5, "#C8A878", beard=None, flip=True))
    else:
        o.append(f'<path d="M{f(x - 64 * s)} {f(b - 10 * s)} C {f(x - 60 * s)} {f(b - 30 * s)} {f(x + 50 * s)} {f(b - 32 * s)} {f(x + 64 * s)} {f(b - 10 * s)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def nain(p, w, h, seed, stage="out"):
    """The gate of the city of Nain: stage='out' the bier carried out of the gate by four bearers, far off, the widow in black
    walking behind it with much people; Jesus and his disciples coming up the road toward it; 'touch' Jesus come nigh with his
    hand on the bier, the bearers standing still; 'risen' the young man sitting up on the bier; 'given' the young man
    standing with his mother, the people with hands lifted."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#8A9A6A", amp=14, step=80),
         walls(w * 0.48, w * 1.06, h * 0.62, h * 0.4, seed, towers=2), ground(w, h, h * 0.62, "#B8A06A", dy=0),
         f'<path d="M{f(w * 0.56)} {f(h * 0.62)} L {f(w * 0.68)} {f(h * 0.62)} L {f(w * 0.5)} {f(h + 10)} L {f(w * 0.2)} {f(h + 10)} Z" fill="#D8C08A" opacity="0.8"></path>']
    far = stage == "out"
    s = fit(b, max(h * 0.3, b - 220))
    sf = s * (0.55 if far else 0.9)
    bx, by = (w * 0.66, h * 0.76) if far else (w * 0.56, b)
    if stage in ("out", "touch", "risen"):
        for i, dx in enumerate((-90, -40, 40, 90)):
            o.append(man(p, bx + dx * sf, by, sf, ["#5A4A3A", "#4A4A4A", "#5A5A4A", "#3A3A3A"][i], flip=True))
        o.append(bier(bx, by - 120 * sf, sf * 1.1, up=stage == "risen"))
        o.append(woman_fig(p, bx + 150 * sf, by, sf * 0.94, WIDOW_C, WIDOW_V, flip=True, up=[(-22, -158), (-16, -176), (-6, -186)] if stage != "risen" else UP_HIGH))
        o.append(crowd(p, bx + 190 * sf, bx + 330 * sf, by, by - 180 * sf, 4, seed, flip=True))
    if stage == "out":
        o.append(jesus(p, w * 0.22, b, s) + disciple(p, w * 0.1, b, s * 0.95, "peter") + disciple(p, w * 0.34, b - 4, s * 0.9, "john"))
    elif stage in ("touch", "risen"):
        o.append(jesus(p, bx - 150 * sf, by, sf * 1.02, flip=True, up=[(-22, -158), (-46, -150), (-64, -140)] if stage == "touch" else UP_BLESS))
    else:
        o.append(jesus(p, w * 0.3, b, s))
        o.append(glow(w * 0.56, b - 120 * s, 150 * s, "#FFF4C2", 0.6, f"{p}g"))
        o.append(man(p, w * 0.5, b, s * 0.92, "#C8A878", flip=True) + woman_fig(p, w * 0.6, b, s * 0.9, WIDOW_C, WIDOW_V, flip=False, up=[(-22, -158), (-44, -150), (-60, -152)]))
        o.append(crowd(p, w * 0.7, w * 0.98, b, b - 180 * s, 4, seed, flip=True, up=UP_HIGH))
    return "".join(o)

def at_his_feet(p, w, h, seed, stage="anoint"):
    """In the Pharisee's house, at meat: Jesus reclining at the low table, Simon the Pharisee across from him in white; behind
    at his feet the woman that was a sinner kneeling, veiled, the alabaster cruse beside her (her weeping told in words);
    stage='anoint' the cruse open in her hands; 'turn' Jesus turned toward her, his hand stretched out over her."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#B8987A", window=(w * 0.08, w * 0.08)), A.lamp(w * 0.5, h * 0.24, max(0.6, h / 300))]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(f'<rect x="{f(w * 0.2)}" y="{f(b - 36 * s)}" width="{f(w * 0.2)}" height="{f(12 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(3): o.append(loaf(w * (0.24 + 0.06 * i), b - 40 * s, s * 0.6))
    o.append(seated(w * 0.1, b, s * 0.82, "#E8E2D6", head="#F3EFE6", beard="#6A645E", band=True))
    jx = w * 0.68
    o.append(glow(jx - 60 * s, b - 50 * s, 130 * s, "#FFF4C2", 0.45, f"{p}g"))
    o.append(jesus_seated(jx, b, s * 0.82, flip=True, glow_=stage == "turn"))
    kx = jx - 130 * s                                # kneeling at his feet, facing them
    o.append(kneel_w(kx, b, s * 0.74, SINNER_C, SINNER_V))
    if stage == "anoint":
        o.append(f'<path d="M{f(kx - 36 * s)} {f(b - 2)} C {f(kx - 44 * s)} {f(b - 16 * s)} {f(kx - 38 * s)} {f(b - 28 * s)} {f(kx - 30 * s)} {f(b - 28 * s)} '
                 f'C {f(kx - 22 * s)} {f(b - 28 * s)} {f(kx - 18 * s)} {f(b - 16 * s)} {f(kx - 24 * s)} {f(b - 2)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></path>')
    for i, x in enumerate((0.86, 0.95)):
        o.append(seated(w * x, b, s * 0.76, HEB[i + 2], head=HEB[i + 2], beard="#2A1A10", flip=True))
    return "".join(o)

def debtors(p, w, h, seed):
    """A certain lender had two debtors: the one owed five hundred shillings, the other fifty: the lender's table with his
    scales and two tallies of coins — a great heap and a little one — and his hand lifted over both, forgiving."""
    b = h * 0.9
    r = random.Random(seed)
    o = [bgr(w, h, "#5A3A2A"), glow(w * 0.5, h * 0.4, h * 0.7, "#FFE680", 0.4, f"{p}g"),
         f'<rect x="{f(w * 0.06)}" y="{f(h * 0.62)}" width="{f(w * 0.88)}" height="{f(h * 0.06)}" fill="#8A5A2A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.12)} {f(h * 0.68)} L {f(w * 0.12)} {f(b)} M{f(w * 0.88)} {f(h * 0.68)} L {f(w * 0.88)} {f(b)}" stroke="#5A3A1E" stroke-width="8"></path>']
    k = max(0.5, h / 380)
    for cx, n, rr in ((w * 0.32, 60, 70), (w * 0.7, 8, 22)):
        for i in range(n):
            x = cx + r.uniform(-rr, rr) * k * (1 - i / (n * 1.4)); y = h * 0.62 - 3 - (i / n) * rr * 0.8 * k
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(7 * k)}" ry="{f(3 * k)}" fill="#C8C2B6" stroke="{INK}" stroke-width="1"></ellipse>')
    o.append(label(w * 0.32, h * 0.76, "500", "#FFD23F", 18) + label(w * 0.7, h * 0.76, "50", "#FFD23F", 18))
    return "".join(o)

def go_in_peace(p, w, h, seed):
    """Thy faith hath saved thee; go in peace: the door of the Pharisee's house open on the evening street, the woman going out
    through it veiled into a soft light; Jesus within, seated, looking after her; the guests murmuring."""
    b = min(h * 0.92, h - 76)
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#B8987A"),
         f'<path d="M{f(w * 0.08)} {f(b)} L {f(w * 0.08)} {f(h * 0.24)} Q {f(w * 0.18)} {f(h * 0.14)} {f(w * 0.28)} {f(h * 0.24)} L {f(w * 0.28)} {f(b)} Z" fill="#FFE6B0" stroke="{INK}" stroke-width="2.4"></path>',
         glow(w * 0.18, b - h * 0.3, h * 0.5, "#FFF4C2", 0.6, f"{p}g")]
    s = fit(b, max(h * 0.2, b - 230))
    o.append(woman_fig(p, w * 0.2, b, s * 0.9, SINNER_C, SINNER_V))
    o.append(jesus_seated(w * 0.46, b, s * 0.82, flip=True))
    o.append(seated(w * 0.64, b, s * 0.78, "#E8E2D6", head="#F3EFE6", beard="#6A645E", band=True, flip=True) + seated(w * 0.76, b, s * 0.76, HEB[3], head=HEB[3], beard="#2A1A10", flip=True))
    return "".join(o)
