"""Drawings for Mark 13:1–14:42: the porter at the door of the house through the four watches of the night — at even, at
midnight, at cockcrowing, in the morning; the man bearing a pitcher of water in the street, two disciples following him.
Built on mrk.art7."""
from mrk.art7 import *
from mrk.art7 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, gerasene_fig
import random, math

def four_watches(p, w, h, seed):
    """Watch therefore: for ye know not when the lord of the house cometh, whether at even, or at midnight, or at
    cockcrowing, or in the morning: four narrow skies across the top, from the sunset to the dawn, each named; below
    them the house with its door, and the porter standing at it with his lamp, awake."""
    b = h * 0.94
    skies = [("AT EVEN", "#4A2A5A", "#FF9A4A"), ("AT MIDNIGHT", "#05051A", "#1E1650"), ("AT COCKCROWING", "#1A1A4A", "#5A5A8A"), ("IN THE MORNING", "#8FD0E2", "#FFE6A0")]
    o = [mk.defs(p, *ALL), bgr(w, h, "#2A2230")]
    sh = h * 0.36; cw = w / 4
    for i, (t, a, c) in enumerate(skies):
        x0 = cw * i
        o.append(f'<defs><linearGradient id="{p}s{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{a}"></stop><stop offset="1" stop-color="{c}"></stop></linearGradient></defs>'
                 f'<rect x="{f(x0)}" y="0" width="{f(cw)}" height="{f(sh)}" fill="url(#{p}s{i})" stroke="{INK}" stroke-width="2"></rect>')
        if i == 0: o.append(f'<circle cx="{f(x0 + cw * 0.5)}" cy="{f(sh * 0.86)}" r="{f(sh * 0.12)}" fill="#FFB04A"></circle>')
        if i == 1: o.append(f'<g transform="translate({f(x0)} 0)">' + mk.stars(10, cw, sh * 0.8, seed) + '</g>' + moon(x0 + cw * 0.7, sh * 0.3, sh * 0.08))
        if i == 2: o.append(f'<g transform="translate({f(x0)} 0)">' + mk.stars(5, cw, sh * 0.5, seed + 1) + '</g>')
        if i == 3: o.append(f'<circle cx="{f(x0 + cw * 0.5)}" cy="{f(sh * 0.9)}" r="{f(sh * 0.14)}" fill="#FFE680"></circle>')
        o.append(label(x0 + cw / 2, sh - 8, t, "#F3EFE6", 9))
    o.append(f'<rect x="{f(w * 0.2)}" y="{f(sh + h * 0.06)}" width="{f(w * 0.6)}" height="{f(b - sh - h * 0.06)}" fill="#C8A878" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.44)}" y="{f(b - h * 0.4)}" width="{f(w * 0.12)}" height="{f(h * 0.4)}" fill="#5A3A22" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#4A3A30"></rect>')
    s = fit(b, max(sh + h * 0.08, b - 200))
    o.append(man(p, w * 0.64, b, s, "#6A5A3A", flip=True, up=[(-22, -158), (-36, -136), (-48, -126)]))
    o.append(clay_lamp(w * 0.64 - 50 * s, b - 126 * s, max(0.5, s * 0.7)))
    return "".join(o)

def pitcher(p, w, h, seed):
    """There shall meet you a man bearing a pitcher of water: follow him: a street of the city, a man going ahead with a
    water-jar on his shoulder, two of the disciples following him at a distance."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.8, seed, hmin=0.34, hmax=0.52), pavement(w, h, h * 0.8)]
    s = fit(b, max(h * 0.24, b - 230))
    jar = ('<path d="M10 -196 C -4 -206 -6 -232 6 -244 L 24 -244 C 36 -232 34 -206 20 -196 Z" fill="#C8784A" stroke="#0D0D0F" stroke-width="2"></path>'
           '<rect x="8" y="-252" width="14" height="10" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(man(p, w * 0.72, b, s, "#7A6A4A", flip=True, up=[(22, -158), (30, -186), (20, -204)], extra=jar))
    o.append(disciple(p, w * 0.3, b, s * 0.96, "peter", flip=True) + disciple(p, w * 0.18, b, s * 0.94, "john", flip=True))
    return "".join(o)
