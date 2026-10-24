"""Drawings for Mark 8:1–9:29: the Pharisees asking a sign on the shore of Dalmanutha; the blind man of Bethsaida led out
of the village by the hand, and what he first saw — men as trees, walking; the way down the mountain; the great multitude
at the mountain's foot, and the same multitude standing in a ring with its back to us, the middle hidden (the boy's fits
are never drawn). Built on mrk.art4."""
from mrk.art4 import *
from mrk.art4 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, gerasene_fig
import random, math

BETH_HEAD = A.headcloth("#5A6A3A", cord="#3A2214")          # the blind man of Bethsaida's olive headcloth

def sign_asked(p, w, h, seed):
    """The Pharisees came forth, seeking of him a sign from heaven: on the shore of Dalmanutha, the boat drawn up, three
    Pharisees in white before Jesus, one pointing up at the empty sky."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.34, seed, color="#8A9A7A", amp=12, step=90), lake(w, h, h * 0.42, seed, n=6),
         shore(w, h, h * 0.66)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(boat(p, w * 0.12, h * 0.64, s * 0.6, mast=True))
    o.append(jesus(p, w * 0.3, b, s))
    o.append(scribe_fig(p, w * 0.56, b, s * 0.98, white=True, flip=True, up=[(-22, -158), (-30, -196), (-34, -232)])
             + scribe_fig(p, w * 0.7, b, s * 0.96, white=True, flip=True) + scribe_fig(p, w * 0.84, b, s * 0.96, flip=True))
    return "".join(o)

def bethsaida(p, w, h, seed):
    """He took hold of the blind man by the hand, and brought him out of the village: the road out of Bethsaida by the
    lake, Jesus leading the man by the hand, the man in his olive headcloth feeling his way, the village gate behind."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), lake(w, h, h * 0.4, seed, n=6), walls(w * 0.62, w + 10, h * 0.66, h * 0.36, seed, towers=2),
         ground(w, h, h * 0.66, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(jesus(p, w * 0.32, b, s, up=[(-22, -158), (-14, -128), (4, -112)]))
    o.append(man(p, w * 0.46, b, s * 0.96, "#8A7A5A", kind="Robe", up=[(-22, -158), (-36, -132), (-50, -118)], extra=BETH_HEAD + A.BLACK_BEARD))
    return "".join(o)

def men_as_trees(p, w, h, seed):
    """I see men; for I behold them as trees, walking: the world as the man first saw it — blurred, green and brown shapes
    tall as trees, moving along a pale road under a pale sky."""
    r = random.Random(seed); b = h * 0.92
    o = [f'<defs><filter id="{p}bl" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="{f(max(3, h / 60))}"></feGaussianBlur></filter></defs>',
         sky(w, h, "#C8D8E0", "#F3EFE6"), f'<g filter="url(#{p}bl)">', ground(w, h, h * 0.62, "#D8C8A0", dy=0)]
    for i in range(6):
        x = w * (0.1 + 0.16 * i) + r.uniform(-12, 12); hh = h * r.uniform(0.46, 0.6); k = hh / 300
        o.append(f'<path d="M{f(x - 10 * k)} {f(b)} L {f(x - 8 * k)} {f(b - hh * 0.55)} L {f(x + 8 * k)} {f(b - hh * 0.55)} L {f(x + 10 * k)} {f(b)} Z" fill="#6A4A30"></path>'
                 f'<ellipse cx="{f(x)}" cy="{f(b - hh * 0.72)}" rx="{f(46 * k)}" ry="{f(hh * 0.28)}" fill="{r.choice(["#5A8A4A", "#6A7A3A", "#4A6A5A"])}"></ellipse>'
                 f'<path d="M{f(x - 14 * k)} {f(b)} l {f(-10 * k)} {f(-30 * k)} M{f(x + 14 * k)} {f(b)} l {f(10 * k)} {f(-30 * k)}" stroke="#6A4A30" stroke-width="{f(8 * k)}"></path>')
    o.append('</g>')
    return "".join(o)

def coming_down(p, w, h, seed):
    """As they were coming down from the mountain: the steep path at evening, Jesus going before, Peter, James and John
    behind him, the plain and the lake far below."""
    o = [mk.defs(p, *ALL), sky(w, h, "#3A2A5A", "#FFB07A"), lake(w, h, h * 0.7, seed, color="#4A6A9A", n=6, op=0.4),
         f'<path d="M-10 {f(h * 0.2)} L {f(w * 0.5)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.9)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A4A5A" stroke="{INK}" stroke-width="2.4"></path>']
    for i, (x, who) in enumerate(((0.62, None), (0.44, "peter"), (0.32, "james"), (0.2, "john"))):
        y = h * (0.2 + 0.7 * (x * w + 10) / (w + 20)) + h * 0.04
        s = fit(y, y - h * 0.3)
        o.append(jesus(p, w * x, y, s, flip=True) if who is None else disciple(p, w * x, y, s * 0.96, who, flip=True))
    return "".join(o)

def foot_mountain(p, w, h, seed):
    """They saw a great multitude about them, and scribes questioning with them: at the mountain's foot the nine disciples
    hemmed in by the crowd, two scribes arguing with them; Jesus and the three coming down the slope behind."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"),
         f'<path d="M-10 {f(h * 0.2)} C {f(w * 0.1)} {f(h * 0.2)} {f(w * 0.3)} {f(h * 0.5)} {f(w * 0.42)} {f(h * 0.7)} L -10 {f(h * 0.7)} Z" fill="#7A7A8A" stroke="{INK}" stroke-width="2.2"></path>',
         ground(w, h, h * 0.66, "#B8A86A", dy=0)]
    s = fit(b, max(h * 0.24, b - 230))
    sm = fit(h * 0.6, h * 0.45)
    o.append(jesus(p, w * 0.22, h * 0.56, sm, flip=True) + disciple(p, w * 0.14, h * 0.48, sm * 0.9, "peter", flip=True))
    o.append(crowd(p, w * 0.42, w * 0.98, b - 30 * s, b - 30 * s - 150 * s, 9, seed, flip=None))
    o.append(disciple(p, w * 0.52, b, s, "andrew") + disciple(p, w * 0.62, b, s * 0.98, "thomas") + scribe_fig(p, w * 0.74, b, s, flip=True, up=UP_BLESS)
             + scribe_fig(p, w * 0.86, b, s * 0.98, flip=True))
    return "".join(o)

def crowd_ring(p, w, h, seed, tone="day"):
    """The multitude standing close in a ring, seen from behind, every back turned to us and the middle hidden by them;
    the bare hills beyond — what befell the boy is told in words only."""
    b = h * 0.96
    top, bot = {"day": ("#8FD0E2", "#F3E8C8"), "grey": ("#6A6A7A", "#C8C0B8")}[tone]
    o = [mk.defs(p, *ALL), sky(w, h, top, bot), hills(w, h, h * 0.4, seed, color="#8A8A7A", amp=14, step=90), ground(w, h, h * 0.5, "#B8A86A", dy=0)]
    r = random.Random(seed)
    for row, (y, k, n) in enumerate(((0.66, 0.9, 14), (0.8, 1.2, 11), (0.97, 1.6, 9))):
        for i in range(n):
            x = w * (i + 0.5 + (0.5 if row % 2 else 0)) / (n + 0.5) + r.uniform(-8, 8)
            kind = "woman" if r.random() < 0.3 else "man"
            o.append(figure(p, x, h * y, h * y - min(h * 0.36 * k, h * y - h * 0.02), r.choice(HEB), kind, flip=r.random() < 0.5))
    return "".join(o)
