"""Drawings for Mark 11–12: the bush that burned and was not consumed, in the wilderness at night (the place concerning
the Bush — God is never drawn: the fire only); the treasury of the temple, the rich casting in much and the poor widow in
her black veil casting in two mites, Jesus seated over against it. Built on mrk.art6."""
from mrk.art6 import *
from mrk.art6 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, gerasene_fig
import random, math

WIDOW_C, WIDOW_VEIL = "#6A6A72", "#3E3E4E"

def the_bush(p, w, h, seed):
    """In the place concerning the Bush: a thorn-bush on the mount at night, burning with fire and not consumed; the
    mountain dark behind it — no one drawn, God never drawn."""
    o = [sky(w, h, "#0B0B2A", "#3A2A5A"), mk.stars(30, w, h * 0.4, seed),
         f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.3)} {f(h * 0.3)} L {f(w * 0.46)} {f(h * 0.4)} L {f(w * 0.7)} {f(h * 0.2)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A2232" stroke="{INK}" stroke-width="2"></path>',
         ground(w, h, h * 0.8, "#3A2E2A", dy=0), glow(w * 0.5, h * 0.6, h * 0.5, "#FFC14D", 0.6, f"{p}g")]
    o.append(E.bush(w * 0.5, h * 0.88, min(w * 0.4, h * 0.7), h * 0.5, seed))
    return "".join(o)

def widow_fig(p, x, y, s, flip=False, up=None):
    """The poor widow: a grey robe, a black veil."""
    return woman_fig(p, x, y, s, WIDOW_C, WIDOW_VEIL, flip=flip, up=up)

def treasury(p, w, h, seed, widow=True, rich=True):
    """Over against the treasury: in the court of the temple, the brass chests with their trumpet mouths along the wall;
    the rich in fine robes casting in much (rich=True); the poor widow in her grey robe and black veil dropping in two
    small coins (widow=True); Jesus seated on the step across the court, the disciples beside him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bgr(w, h, "#D8C8A8")]
    for x in (0.06, 0.34, 0.66, 0.94):
        o.append(f'<rect x="{f(w * x - 14)}" y="-10" width="28" height="{f(b * 0.7 + 10)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(b * 0.7)}" width="{f(w + 20)}" height="{f(h)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    o.append(pavement(w, h, b * 0.7))
    s = fit(b, max(h * 0.24, b - 230))
    for x in (0.46, 0.6, 0.74):
        cx, cy = w * x, b - 4
        o.append(f'<rect x="{f(cx - 22 * s)}" y="{f(cy - 70 * s)}" width="{f(44 * s)}" height="{f(70 * s)}" fill="#C8963E" stroke="{INK}" stroke-width="2"></rect>'
                 f'<path d="M{f(cx - 6 * s)} {f(cy - 70 * s)} C {f(cx - 8 * s)} {f(cy - 100 * s)} {f(cx - 26 * s)} {f(cy - 116 * s)} {f(cx - 30 * s)} {f(cy - 124 * s)} L {f(cx + 30 * s)} {f(cy - 124 * s)} '
                 f'C {f(cx + 26 * s)} {f(cy - 116 * s)} {f(cx + 8 * s)} {f(cy - 100 * s)} {f(cx + 6 * s)} {f(cy - 70 * s)} Z" fill="#E8B830" stroke="{INK}" stroke-width="2"></path>')
    if rich:
        from genesis.art3 import man as _man
        o.append(_man(p, w * 0.84, b, s, "#7A2A6A", flip=True, kind="Robe", extra=A.headcloth("#7A2A6A", cord="#E8B830"))
                 + _man(p, w * 0.95, b, s * 0.98, "#2A4A7A", flip=True, kind="Robe", extra=A.headcloth("#E8E2D6", cord="#E8B830")))
    if widow:
        o.append(widow_fig(p, w * 0.53, b, s * 0.9, flip=True, up=[(-22, -158), (-34, -150), (-46, -152)]))
        o.append(f'<circle cx="{f(w * 0.53 + 46 * s * 0.9 + 2)}" cy="{f(b - 152 * s * 0.9 + 6)}" r="{f(3 * s + 1)}" fill="#B5652E" stroke="{INK}" stroke-width="1"></circle>'
                 f'<circle cx="{f(w * 0.53 + 46 * s * 0.9 - 4)}" cy="{f(b - 152 * s * 0.9 + 14)}" r="{f(3 * s + 1)}" fill="#B5652E" stroke="{INK}" stroke-width="1"></circle>')
    o.append(jesus_seated(w * 0.18, b, s * 0.82))
    o.append(disciple(p, w * 0.06, b, s * 0.94, "peter") + disciple(p, w * 0.3, b, s * 0.92, "john", flip=True))
    return "".join(o)
