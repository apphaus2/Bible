"""Drawings for Mark 9:30–10:52: the valley of the unquenchable fire with no one in it; the rich man kneeling on the road;
blind Bartimæus by the way side outside Jericho, his grey garment, and the garment cast away on the road as he springs
up. Built on mrk.art5."""
from mrk.art5 import *
from mrk.art5 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, gerasene_fig
import random, math

RICH_C, RICH_HEAD = "#7A2A6A", A.headcloth("#7A2A6A", cord="#E8B830")    # Matthew's rich young man: plum, a gold band
BART_CLOAK, BART_C = "#8A8A90", "#6A4A30"                                 # Bartimæus: the grey garment over a brown robe

def gehenna(p, w, h, seed):
    """Into hell, into the unquenchable fire, where their worm dieth not: a deep valley under the city wall at dusk, the
    fire smouldering along its floor and the smoke rising — no one drawn."""
    o = [sky(w, h, "#2A0A10", "#8A2A1A"), walls(w * 0.5, w + 10, h * 0.34, h * 0.22, seed, color="#6A4A44", towers=2),
         f'<path d="M-10 {f(h * 0.3)} C {f(w * 0.2)} {f(h * 0.34)} {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.5)} {f(h * 0.76)} C {f(w * 0.7)} {f(h * 0.7)} {f(w * 0.8)} {f(h * 0.4)} {f(w + 10)} {f(h * 0.36)} '
         f'L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A1A18" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.12)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.7)} {f(h * 0.8)} {f(w * 0.88)} {f(h + 10)} Z" fill="#1E0A08"></path>']
    o.append(smoke(w * 0.3, h * 0.8, 7, seed, color="#4A3A3A", op=0.6, k=max(0.6, h / 300)) + smoke(w * 0.62, h * 0.82, 7, seed + 1, color="#4A3A3A", op=0.6, k=max(0.6, h / 300)))
    for i in range(5):
        o.append(E.blaze(w * (0.22 + 0.14 * i), h * 0.96, w * 0.14, h * 0.2, seed + i, n=5))
    return "".join(o)

def rich_kneels(p, w, h, seed):
    """There ran one to him, and kneeled to him: on the road out of the village, a young man in a fine plum robe with a
    gold band on his headcloth, kneeling before Jesus; the disciples behind."""
    b = h * 0.94
    o = [road_scene(p, w, h, seed)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(jesus(p, w * 0.34, b, s, flip=True))
    o.append(E.kneel(w * 0.52, b, s * 0.9, color=RICH_C, flip=True, skin="#D9A27A"))
    o.append(disciple(p, w * 0.18, b, s * 0.96, "peter", flip=True) + disciple(p, w * 0.08, b, s * 0.94, "andrew", flip=True))
    return "".join(o)

def bartimaeus_way(p, w, h, seed, sprang=False):
    """Bartimæus, a blind beggar, was sitting by the way side: outside Jericho's gate under the palms, the beggar in his
    grey garment sitting at the road's edge, his hand out, as the great multitude comes along the road with Jesus;
    sprang=True: the grey garment flung down on the road, the man standing before Jesus with his arms out."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), walls(w * 0.6, w + 10, h * 0.58, h * 0.32, seed, towers=2), ground(w, h, h * 0.58, "#D8B880", dy=0)]
    for x in (0.08, 0.2, 0.52):
        o.append(f'<g transform="translate({f(w * x)} {f(h * 0.6)}) scale({f(h * 0.3 / 210)})">' + J1.palm(0, 0, 1) + '</g>')
    o.append(f'<path d="M-10 {f(h * 0.82)} C {f(w * 0.3)} {f(h * 0.76)} {f(w * 0.6)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.72)} C {f(w * 0.6)} {f(h * 0.82)} {f(w * 0.3)} {f(h * 0.9)} -10 {f(h * 0.94)} Z" fill="#E8D8B0"></path>')
    s = fit(b, max(h * 0.24, b - 230))
    if sprang:
        o.append(f'<path d="M{f(w * 0.68)} {f(b)} C {f(w * 0.7)} {f(b - 14 * s)} {f(w * 0.8)} {f(b - 20 * s)} {f(w * 0.86)} {f(b - 6 * s)} L {f(w * 0.88)} {f(b)} Z" fill="{BART_CLOAK}" stroke="{INK}" stroke-width="2"></path>')
        o.append(jesus(p, w * 0.34, b, s, flip=True, up=UP_TOUCH))
        o.append(man(p, w * 0.5, b, s * 0.96, BART_C, kind="Robe", up=[(-22, -158), (-40, -168), (-58, -170)], extra=A.BLACK_BEARD))
        o.append(crowd(p, -10, w * 0.2, b, b - 160 * s, 3, seed))
    else:
        o.append(crowd(p, w * 0.02, w * 0.42, b - 20 * s, b - 20 * s - 160 * s, 7, seed, flip=True))
        o.append(jesus(p, w * 0.3, b, s, flip=True))
        o.append(seated(w * 0.74, b, s * 0.8, BART_CLOAK, head=BART_CLOAK, beard="#3A2A1E", flip=True))
    return "".join(o)
