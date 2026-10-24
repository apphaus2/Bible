"""Drawings for Luke 8–9: the twelve and the women who ministered of their substance on the road through the villages —
Mary Magdalene, Joanna the wife of Chuzas, Susanna; and for Luke 9 the village of the Samaritans that would not receive him,
the hand put to the plough. Built on luk.art4."""
from luk.art4 import *
from luk.art4 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch, \
    jesus_kneel, light_seated, WOMEN3, PURPLE, GOLD, kneel_w, boy_fig, zach_fig, elis_fig, shepherd_fig, swaddled, fish_heap, WIDOW_C, WIDOW_V, SINNER_C, SINNER_V
import random, math

JOANNA = ("#8A5A1A", "#C8902A")      # an amber veil
SUSANNA = ("#5A6A4A", "#7A8A5A")     # a sage veil

def women_follow(p, w, h, seed):
    """Through cities and villages, and with him the twelve, and certain women: the road between the villages of Galilee,
    Jesus walking ahead with the disciples, and behind them Mary Magdalene, Joanna and Susanna and others, carrying bundles
    and jars of their substance."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#8A9A6A", amp=14, step=80),
         hill_town(w * 0.84, h * 0.56, w * 0.26, h * 0.18, seed, hill="#9A8A6A"), ground(w, h, h * 0.62, "#B8A06A", dy=-6),
         f'<path d="M-10 {f(b + 6)} C {f(w * 0.3)} {f(b - h * 0.06)} {f(w * 0.6)} {f(h * 0.7)} {f(w * 0.84)} {f(h * 0.6)}" stroke="#D8C08A" stroke-width="{f(h * 0.07)}" fill="none" opacity="0.8"></path>']
    s = fit(b, max(h * 0.3, b - 220))
    o.append(jesus(p, w * 0.74, b - 14, s * 0.92))
    for i, who in enumerate(("peter", "john", "james", "andrew")):
        o.append(disciple(p, w * (0.64 - 0.07 * i), b - 10 + 2 * i, s * (0.9 - 0.01 * i), who))
    jar = '<path d="M-48 -122 C -56 -112 -54 -98 -46 -96 L -34 -96 C -26 -98 -24 -112 -32 -122 Z" fill="#E8D8A8" stroke="#0D0D0F" stroke-width="1.6"></path>'
    for i, (c, vl) in enumerate(((ROBES["magdalene"], "#C2456A"), JOANNA, SUSANNA)):
        o.append(woman_fig(p, w * (0.3 - 0.09 * i), b - 2 * i, s * (0.9 - 0.02 * i), c, vl, up=[(-22, -158), (-34, -130), (-40, -112)], extra=jar))
    return "".join(o)

def samaritan_village(p, w, h, seed):
    """They received him not, because his face was as though he were going to Jerusalem: a village of Samaria on its hill at
    evening, the gate shut against them; James and John standing with their arms lifted toward the sky, Jesus turned to them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#4A3A6A", "#FFB07A"), hills(w, h, h * 0.44, seed, color="#6A5A5A", amp=14, step=80),
         walls(w * 0.5, w * 1.06, h * 0.66, h * 0.36, seed, towers=2, color="#A8907A"), ground(w, h, h * 0.66, "#8A7A5A", dy=0)]
    gx = w * 0.5 + (w * 0.56) * 0.5 / 2 + (w * 0.56) * 1.5 / 2
    s = fit(b, max(h * 0.3, b - 220))
    o.append(jesus(p, w * 0.18, b, s))
    o.append(disciple(p, w * 0.32, b, s * 0.95, "james", up=UP_HIGH) + disciple(p, w * 0.42, b, s * 0.94, "john", up=UP_HIGH))
    return "".join(o)

def plough(p, w, h, seed):
    """No man, having put his hand to the plough, and looking back, is fit for the kingdom of God: a ploughman at evening
    behind a yoke of oxen, his hand on the plough, the furrow straight before him across the field."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#4A3A6A", "#FFB07A"), sun(w * 0.86, h * 0.46, 16, color="#FFE680", op=0.4),
         hills(w, h, h * 0.52, seed, color="#6A5A5A", amp=12, step=80), ground(w, h, h * 0.62, "#8A6A4A", dy=0)]
    for k in range(6):
        y = h * (0.66 + 0.05 * k)
        o.append(f'<path d="M-10 {f(y)} L {f(w * 0.5)} {f(y + 2)}" stroke="#5A3A22" stroke-width="2"></path>')
    import samuel1 as S1
    k = max(0.3, h / 900)
    o.append(S1.cow(w * 0.62, b - 6, k * 0.96, color="#5A3A22", patch="#5A3A22") + S1.cow(w * 0.7, b, k, color="#8A5A30", patch="#8A5A30"))
    o.append(f'<path d="M{f(w * 0.56)} {f(b - 60 * k)} L {f(w * 0.4)} {f(b - 10)} L {f(w * 0.42)} {f(b + 4)}" stroke="#5A3A1E" stroke-width="5" fill="none"></path>')
    s = fit(b, max(h * 0.3, b - 220))
    o.append(man(p, w * 0.3, b, s, "#6A5A3A", up=[(-22, -158), (-44, -134), (-60, -120)], flip=True))   # flipped: the free arm reaches right, to the plough
    return "".join(o)
