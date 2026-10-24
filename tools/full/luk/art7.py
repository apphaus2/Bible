"""Drawings for Luke 11: the friend at midnight knocking at the shut door for three loaves, the traveller waiting behind
him; the tombs which appear not, walked over unknowing; the key of knowledge taken away and the door shut. Built on
luk.art6."""
from luk.art6 import *
from luk.art6 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch, \
    jesus_kneel, light_seated, WOMEN3, PURPLE, GOLD, kneel_w, boy_fig, zach_fig, elis_fig, shepherd_fig, swaddled, fish_heap, WIDOW_C, WIDOW_V, SINNER_C, SINNER_V, \
    JOANNA, SUSANNA, SAMARITAN_C, samaritan_fig, priest_fig, levite_fig
import random, math

def midnight(p, w, h, seed, opened=False):
    """A friend at midnight: a village street under the stars, a man knocking at a shut door, his friend from the journey
    waiting behind him with his staff; a little light under the door; opened=True the door open, the householder handing
    out the loaves."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), night(w, h, seed, n=60, top="#05051A", bot="#2A2050"), moon(w * 0.86, h * 0.14, max(8, h * 0.04)),
         houses(w, h, b, seed, x0=w * 0.7, x1=w + 10, hmin=0.3, hmax=0.44, shut=True, color=("#5A5A6A", "#4A4A5A"), stairs=False)]
    hx0, hx1, top = w * 0.06, w * 0.5, h * 0.24
    o.append(f'<rect x="{f(hx0)}" y="{f(top)}" width="{f(hx1 - hx0)}" height="{f(b - top)}" fill="#6A6070" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(hx0 - 6)}" y="{f(top - 8)}" width="{f(hx1 - hx0 + 12)}" height="10" fill="#4A3A3A" stroke="{INK}" stroke-width="2"></rect>')
    dx0, dx1 = w * 0.3, w * 0.42
    if opened:
        o.append(f'<path d="M{f(dx0)} {f(b)} L {f(dx0)} {f(b - h * 0.4)} L {f(dx1)} {f(b - h * 0.4)} L {f(dx1)} {f(b)} Z" fill="#FFC14D" stroke="{INK}" stroke-width="2"></path>'
                 + glow((dx0 + dx1) / 2, b - h * 0.2, h * 0.4, "#FFE680", 0.6, f"{p}g"))
    else:
        o.append(f'<path d="M{f(dx0)} {f(b)} L {f(dx0)} {f(b - h * 0.4)} L {f(dx1)} {f(b - h * 0.4)} L {f(dx1)} {f(b)} Z" fill="#4A3020" stroke="{INK}" stroke-width="2"></path>'
                 f'<path d="M{f(dx0)} {f(b - h * 0.2)} L {f(dx1)} {f(b - h * 0.2)}" stroke="#2A1A10" stroke-width="3"></path>'
                 f'<rect x="{f(dx0)}" y="{f(b - 3)}" width="{f(dx1 - dx0)}" height="3" fill="#FFC14D"></rect>')
    o.append(ground(w, h, b, "#2A2438", dy=0))
    s = fit(b, max(h * 0.2, b - 230))
    o.append(man(p, w * 0.52, b, s, "#5A4A3A", flip=False, up=[(-22, -158), (-44, -170), (-56, -176)]))
    o.append(shepherd_fig(p, w * 0.66, b, s * 0.96, 2))
    if opened:
        o.append(man(p, w * 0.36, b, s * 0.96, "#4A4A5A", flip=True, up=[(-22, -158), (-46, -150), (-62, -146)])
                 + "".join(loaf(w * 0.36 + (66 + 12 * k) * s, b - 150 * s - 6 * k * s, s * 0.6) for k in range(3)))
    return "".join(o)

def hidden_tombs(p, w, h, seed):
    """Ye are as the tombs which appear not, and the men that walk over them know it not: a level field at evening, men
    walking across it; under the ground, seen as in a cut-away, the dark shapes of graves beneath their feet."""
    b = h * 0.62
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), sky(w, h, "#5A4A6A", "#E8A870"), hills(w, h, h * 0.44, seed, color="#6A5A5A", amp=8, step=90),
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#6A5038" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h * 0.04)}" fill="#7A8A4A"></rect>']
    for i in range(4):
        x = w * (0.12 + 0.24 * i)
        o.append(f'<rect x="{f(x - w * 0.08)}" y="{f(b + h * 0.12)}" width="{f(w * 0.16)}" height="{f(h * 0.14)}" rx="10" fill="#2A1E16" stroke="#1A120C" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.1, b - 150))
    for i in range(3):
        o.append(man(p, w * (0.2 + 0.28 * i), b + 2, s * r.uniform(0.9, 1.0), r.choice(HEB), flip=i % 2 == 1))
    return "".join(o)

def key_knowledge(p, w, h, seed):
    """Ye took away the key of knowledge: the door of the house of learning shut and barred, the great key gone from its
    lock; outside, men standing at the door who cannot enter."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8A9AB0", "#E8D8B8"), f'<rect x="{f(w * 0.2)}" y="{f(h * 0.12)}" width="{f(w * 0.6)}" height="{f(b - h * 0.12)}" fill="#C8B490" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.4)} {f(b)} L {f(w * 0.4)} {f(h * 0.4)} Q {f(w * 0.5)} {f(h * 0.3)} {f(w * 0.6)} {f(h * 0.4)} L {f(w * 0.6)} {f(b)} Z" fill="#5A3A22" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.4)} {f(h * 0.62)} L {f(w * 0.6)} {f(h * 0.62)}" stroke="#2A1A10" stroke-width="6"></path>',
         f'<circle cx="{f(w * 0.56)}" cy="{f(h * 0.56)}" r="6" fill="#0D0D0F"></circle><rect x="{f(w * 0.56 - 2)}" y="{f(h * 0.56)}" width="4" height="10" fill="#0D0D0F"></rect>',
         ground(w, h, b, "#A8946A", dy=0)]
    s = fit(b, max(h * 0.24, b - 220))
    o.append(man(p, w * 0.12, b, s, "#6A5A3A") + woman_fig(p, w * 0.86, b, s * 0.92, "#4A5A6A", "#3A4A5A", flip=True))
    return "".join(o)
