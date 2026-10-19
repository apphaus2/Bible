"""Drawings for the Proverbs volume (chapter by chapter, added below), on top of 2 Chronicles' (chr2.art, which carries chr1,
kg2, kg1 and 2 Samuel's drawings). The emblems over the saying cells are in pro.emblems.

At a distance: the father is Solomon (kg1's sol_fig, deep blue with the gold crown); the son a youth in a pale-blue tunic and
headcloth (son_fig); Wisdom a woman in white with a gold band, standing in gold light (wisdom_fig) — never a goddess, never
enthroned. The strange woman is never drawn near: a far veiled figure at dusk, a shut door, an empty street."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from chr2.art import *
from chr2.art import f, K2, K3
import kg1.art as K1
from kg1.art import SOL_C
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import man, woman
from pro import emblems as EM
import joshua1 as J, judges1 as J1, ruth1 as R, exodus as E, exodus4 as E4, exodus5 as V, samuel1 as S1, samuel3 as S3, samuel4 as S4, egypt as EG

INK = "#0D0D0F"
SON_C, WIS_C, STRANGE_C = "#8FB8D8", "#F3EFE6", "#5A1A3A"
BAND = '<path d="M-13 -196 C -6 -199 6 -199 13 -196" fill="none" stroke="#E8B830" stroke-width="4" stroke-linecap="round"></path>'

def glow(x, y, r, color="#FFE680", op=0.35): return EM.glow(x, y, r, color, op)

def son_fig(p, x, y, s, flip=False, up=None):
    """The son at a distance: a pale-blue tunic and headcloth, beardless."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=SON_C, kind="Tunic", sw=3, flip=flip, up=up, extra=A.headcloth(SON_C))

def wisdom_fig(p, x, y, s, flip=False, up=None, light=True):
    """Wisdom at a distance: a woman in white with a gold band about her head, standing in gold light."""
    g = (glow(x, y - 110 * s, 150 * s, "#FFE680", 0.45) + EM.rays(x, y - 110 * s, 18, 60 * s, 260 * s, "#FFF4C2", 0.35, 6)) if light else ""
    sash = '<path d="M-36 -112 C -12 -106 12 -106 36 -112" fill="none" stroke="#0D0D0F" stroke-width="7"></path><path d="M-36 -112 C -12 -106 12 -106 36 -112" fill="none" stroke="#E8B830" stroke-width="4"></path>'
    fig = mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=WIS_C, kind="Robe", woman=True, hair="#1A1210", sw=3, flip=flip, up=up, extra=sash + A.headcloth(WIS_C, cord="#E8B830"))
    return g + fig

def veiled(p, x, y, s, flip=False):
    """A far veiled woman at dusk, all in dark wine-red (the strange woman, never drawn near)."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#2A1018", cloth=STRANGE_C, kind="Robe", woman=True, hair=STRANGE_C, sw=3, flip=flip)

def shelf(x, y, w, n=6, seed=1):
    r = random.Random(seed)
    o = [f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="8" fill="#5A3A22" stroke="{INK}" stroke-width="1.6"></rect>']
    for i in range(n):
        cx = x + 12 + i * (w - 24) / max(1, n - 1)
        o.append(f'<rect x="{f(cx - 7)}" y="{f(y - 30)}" width="14" height="30" rx="5" fill="{r.choice(["#E8D8B0", "#D8C090", "#F3E8C8"])}" stroke="{INK}" stroke-width="1.4"></rect>'
                 f'<rect x="{f(cx - 7)}" y="{f(y - 18)}" width="14" height="4" fill="#B5402A"></rect>')
    return "".join(o)

# ---- Proverbs 1–3 ----------------------------------------------------------------------------------------------------------
def writing(p, w, h, seed):
    """Solomon in his chamber at a table with an open scroll, the lamp lit, shelves of scrolls behind: the proverbs of Solomon."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2214"></rect>',
         "".join(f'<rect x="{f(x)}" y="-10" width="{f(w / 14 - 4)}" height="{f(h + 20)}" fill="#4A2A18"></rect>' for x in [i * w / 14 for i in range(15)]),
         f'<rect x="{f(w * 0.06)}" y="{f(h * 0.12)}" width="{f(w * 0.14)}" height="{f(h * 0.36)}" fill="#1A1A3A" stroke="{INK}" stroke-width="2.4"></rect>'
         + mk.stars(10, w * 0.14, h * 0.36, seed).replace("<g fill", f'<g transform="translate({f(w * 0.06)} {f(h * 0.12)})" fill'),
         shelf(w * 0.62, h * 0.32, w * 0.32, 7, seed), shelf(w * 0.62, h * 0.56, w * 0.32, 7, seed + 1),
         ground(w, h, b, "#2A1A10", dy=0)]
    s = fit(b, h * 0.3)
    o.append(glow(w * 0.48, b - 120 * s, 110 * s, "#FFC14D", 0.35))
    o.append(K1.sol_fig(p, w * 0.32, b, s, flip=True, up=[(-22, -158), (-40, -120), (-62, -112)]))
    tx = w * 0.46
    o.append(f'<rect x="{f(tx - 70 * s)}" y="{f(b - 92 * s)}" width="{f(150 * s)}" height="{f(10 * s)}" fill="#8A5A30" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(tx - 60 * s)} {f(b - 82 * s)} L {f(tx - 60 * s)} {f(b)} M{f(tx + 70 * s)} {f(b - 82 * s)} L {f(tx + 70 * s)} {f(b)}" stroke="#5A3A22" stroke-width="{f(8 * s)}"></path>'
             f'<rect x="{f(tx - 40 * s)}" y="{f(b - 102 * s)}" width="{f(80 * s)}" height="{f(10 * s)}" fill="#F3E8C8" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(EM.lamp_shape(tx + 50 * s, b - 92 * s, 0.5 * s))
    return "".join(o)

def ambush(p, w, h, seed):
    """Sinners lying in wait by the road at dusk, crouched behind the rocks: the way of them that are greedy of gain."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A", "#C8603A"), sun(w * 0.8, h * 0.5, 20, color="#FF8A3D", op=0.3), hills(w, h, h * 0.52, seed, "#3A2A3A", amp=10, step=70),
         ground(w, h, h * 0.6, "#4A3A3A", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.4)} {f(h * 0.8)} {f(w * 0.6)} {f(h * 0.66)} {f(w * 0.7)} {f(h * 0.6)} L {f(w * 0.74)} {f(h * 0.6)} C {f(w * 0.68)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.86)} {f(w * 0.56)} {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, h * 0.36)
    for x, k in ((0.1, 1.0), (0.2, 0.9), (0.84, 0.95)):
        o.append(E.kneel(w * x, b - 4, s * k * 0.9, color="#12090A", flip=x > 0.5))
    o.append(E4.rock(w * 0.16, b + 6, w * 0.24, h * 0.22, color="#5A4A4A", dark="#2A2A2A") + E4.rock(w * 0.88, b + 6, w * 0.18, h * 0.18, color="#5A4A4A", dark="#2A2A2A"))
    return "".join(o)

def net_road(p, w, h, seed):
    """In vain is the net spread in the sight of any bird: a fowler's net on the open ground, a bird above it, the road beyond."""
    b = h * 0.88
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.55, seed, "#8A9A6A", amp=8, step=80), ground(w, h, h * 0.62, "#B8A070", dy=0)]
    cx, nw = w * 0.5, min(w * 0.5, 360)
    o.append(f'<path d="M{f(cx - nw / 2)} {f(b)} C {f(cx - nw / 4)} {f(b - h * 0.2)} {f(cx + nw / 4)} {f(b - h * 0.2)} {f(cx + nw / 2)} {f(b)}" fill="none" stroke="#5A4A3A" stroke-width="3"></path>')
    for i in range(12):
        x = cx - nw / 2 + i * nw / 11
        o.append(f'<path d="M{f(x)} {f(b)} L {f(x + nw / 10)} {f(b - h * 0.15)} M{f(x + nw / 10)} {f(b)} L {f(x)} {f(b - h * 0.15)}" stroke="#5A4A3A" stroke-width="1.4"></path>')
    o.append(f'<path d="M{f(cx + nw / 2 + 20)} {f(b)} L {f(cx + nw / 2 + 60)} {f(b - h * 0.3)}" stroke="#5A3A22" stroke-width="4"></path>')
    o.append(EM.E4quail(cx - 30, h * 0.3).replace("scale(0.8", f"scale({f(min(1.6, h / 200))}"))
    return "".join(o)

def wisdom_gate(p, w, h, seed, crowd=True, dusk=False):
    """Wisdom crieth aloud in the street, at the entrance of the gates: she stands before the city gate in white and gold
    light, her arm raised, the people in the broad place."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A5E" if dusk else "#8FD0E2", "#FFC14D" if dusk else "#FFE3B8"), ground(w, h, h * 0.8, "#C8A06A", dy=0)]
    gw = min(w * 0.6, h * 1.0)
    o.append(S4.gatehouse(w * 0.62, h * 0.8, gw, h * 0.62, lit=dusk))
    s = min(fit(b, h * 0.46), 1.0)
    if crowd:
        o.append(crowd_at(p, w, h, seed, w * 0.5, w * 0.98, h * 0.82, h * 0.88, 12, s * 0.42, s * 0.6, flip=True))
    o.append(f'<path d="M{f(w * 0.12)} {f(b)} L {f(w * 0.14)} {f(b - 16 * s)} L {f(w * 0.42)} {f(b - 16 * s)} L {f(w * 0.44)} {f(b)} Z" fill="#B8A88A" stroke="{INK}" stroke-width="2"></path>')
    o.append(wisdom_fig(p, w * 0.28, b - 16 * s, s, up=[(-22, -158), (-34, -200), (-40, -238)]))
    if crowd:
        for i in range(4): o.append(man(p, w * (0.56 + i * 0.1), b + 2 - (i % 2) * 4, s * (0.86 - (i % 2) * 0.08), ("#5A4A3A", "#3A4A5A", "#6A4A3A", "#4A5A3A")[i], flip=True))
    return "".join(o)

def high_place(p, w, h, seed):
    """On the top of high places by the way, where the paths meet: Wisdom on the height above the crossroads, the city behind."""
    b = h * 0.62
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFE3B8"), J.city_hill(w * 0.82, h * 0.5, w * 0.3, h * 0.22, seed),
         f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.2)} {f(h * 0.62)} L {f(w * 0.46)} {f(h * 0.6)} L {f(w * 0.6)} {f(h * 0.7)} L {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B89A6A" stroke="{INK}" stroke-width="2"></path>']
    for x0, x1 in ((-0.05, 0.5), (1.05, 0.5), (0.2, 0.5), (0.8, 0.5)):
        o.append(f'<path d="M{f(w * x0)} {f(h + 10)} L {f(w * x1)} {f(h * 0.66)}" stroke="#E8C88A" stroke-width="{f(max(8, w * 0.03))}" stroke-linecap="round"></path>')
    s = fit(b, h * 0.22)
    o.append(wisdom_fig(p, w * 0.33, b, s, up=[(-22, -158), (-34, -200), (-40, -238)]))
    return "".join(o)

def treasure(p, w, h, seed):
    """If thou seek her as silver, and search for her as for hid treasures: a man digging in a field, a jar of silver in the earth."""
    b = h * 0.86
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.56, seed, "#8A9A6A", amp=8, step=80), ground(w, h, h * 0.62, "#9A7A4A", dy=0)]
    s = fit(b, h * 0.3)
    o.append(f'<ellipse cx="{f(w * 0.55)}" cy="{f(b + 4)}" rx="{f(80 * s)}" ry="{f(18 * s)}" fill="#3A2A1A" stroke="{INK}" stroke-width="2"></ellipse>')
    o.append(glow(w * 0.55, b - 10 * s, 70 * s, "#FFF4C2", 0.5))
    o.append(f'<path d="M{f(w * 0.55 - 26 * s)} {f(b + 6)} C {f(w * 0.55 - 34 * s)} {f(b - 30 * s)} {f(w * 0.55 + 34 * s)} {f(b - 30 * s)} {f(w * 0.55 + 26 * s)} {f(b + 6)} Z" fill="#B5652E" stroke="{INK}" stroke-width="2"></path>')
    o.append(EM.coin_pile(w * 0.55, b - 22 * s, 8, "#C8C8D0", seed).replace('rx="9" ry="3.6"', f'rx="{f(9 * s * 1.4)}" ry="{f(3.6 * s * 1.4)}"'))
    o.append(son_fig(p, w * 0.36, b, s, flip=True, up=[(-22, -158), (-46, -120), (-70, -96)]))
    o.append(f'<path d="M{f(w * 0.36 + 60 * s)} {f(b - 100 * s)} L {f(w * 0.36 + 90 * s)} {f(b)}" stroke="#5A3A22" stroke-width="{f(6 * s)}"></path>')
    o.append(R.heap(w * 0.75, b + 4, 120 * s, 30 * s, "#8A6A3A"))
    return "".join(o)

def two_ways(w, h, seed):
    """The paths of uprightness and the ways of darkness: one road into the morning, one down into the dark."""
    o = [f'<rect x="-10" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#FFE3B8"></rect><rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#14141E"></rect>',
         EM.rays(w * 0.16, h * 0.3, 18, 20, max(w, h) * 0.6, "#FFC14D", 0.35, 6), sun(w * 0.16, h * 0.3, min(30, h * 0.08), color="#FFE680", op=0.3),
         mk.stars(30, w * 0.5, h * 0.5, seed).replace("<g fill", f'<g transform="translate({f(w * 0.5)} 0)" fill'),
         f'<rect x="-10" y="{f(h * 0.55)}" width="{f(w * 0.5 + 10)}" height="{f(h)}" fill="#9CCB5E"></rect><rect x="{f(w * 0.5)}" y="{f(h * 0.55)}" width="{f(w * 0.5 + 10)}" height="{f(h)}" fill="#2A2420"></rect>',
         f'<path d="M-10 {f(h * 0.55)} L {f(w + 10)} {f(h * 0.55)}" stroke="{INK}" stroke-width="2"></path>']
    cx = w * 0.5
    o.append(f'<path d="M{f(cx - w * 0.08)} {f(h + 10)} L {f(cx - w * 0.02)} {f(h * 0.78)} L {f(w * 0.18)} {f(h * 0.55)} L {f(w * 0.24)} {f(h * 0.55)} L {f(cx)} {f(h * 0.72)} '
             f'L {f(w * 0.76)} {f(h * 0.55)} L {f(w * 0.82)} {f(h * 0.55)} L {f(cx + w * 0.02)} {f(h * 0.78)} L {f(cx + w * 0.08)} {f(h + 10)} Z" fill="#E8C88A" stroke="{INK}" stroke-width="2" stroke-linejoin="round"></path>')
    o.append(f'<path d="M{f(cx)} {f(h * 0.72)} L {f(w * 0.76)} {f(h * 0.55)} L {f(w * 0.82)} {f(h * 0.55)} L {f(cx + w * 0.02)} {f(h * 0.78)} Z" fill="#4A4038"></path>')
    return "".join(o)

def strange_house(w, h, seed):
    """Her house inclineth unto death: a house at the edge of a slope at dusk, its door dark, the path from it going down
    into the shadow. No one is drawn."""
    o = [sky(w, h, "#1A0A1A", "#8A2A3A"), sun(w * 0.86, h * 0.62, 18, color="#D7261E", op=0.25),
         f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.46)} {f(h * 0.5)} C {f(w * 0.6)} {f(h * 0.56)} {f(w * 0.7)} {f(h * 0.8)} {f(w * 0.78)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A2A2A" stroke="{INK}" stroke-width="2.2"></path>',
         f'<path d="M{f(w * 0.78)} {f(h + 10)} C {f(w * 0.7)} {f(h * 0.8)} {f(w * 0.6)} {f(h * 0.56)} {f(w * 0.46)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} Z" fill="#05050A"></path>']
    hx, hw, hh = w * 0.26, min(w * 0.3, h * 0.5), h * 0.28
    o.append(EM.house(hx, h * 0.5, hw, hh, color="#5A3A3A"))
    o.append(f'<path d="M{f(hx + 10)} {f(h * 0.5)} C {f(w * 0.46)} {f(h * 0.54)} {f(w * 0.6)} {f(h * 0.66)} {f(w * 0.7)} {f(h * 0.9)}" fill="none" stroke="#8A6A6A" stroke-width="5" stroke-dasharray="10 8"></path>')
    return "".join(o)

def dwell_land(p, w, h, seed):
    """The upright shall dwell in the land: green fields, houses and a vine, a family at the door."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#E8F6FA"), hills(w, h, h * 0.5, seed, "#6A9A4A", amp=10, step=90), ground(w, h, h * 0.62, "#9CCB5E", dy=0),
         R.field(w * 0.5, w + 10, h * 0.7, h * 0.12, seed, rows=2)]
    s = fit(b, h * 0.42)
    o.append(EM.house(w * 0.22, b - 10, 180 * s, 110 * s, lit=False))
    o.append(EM.tree(w * 0.42, b - 6, s * 1.4))
    o.append(man(p, w * 0.58, b, s, "#1F3A7A") + woman(p, w * 0.64, b, s * 0.92, "#7A3A6A") + son_fig(p, w * 0.7, b, s * 0.7, flip=True))
    return "".join(o)

def straight_path(w, h, seed):
    """He will direct thy paths: a straight road across the land toward the sunrise."""
    o = [sky(w, h, "#5A8FC8", "#FFE3B8"), EM.rays(w * 0.5, h * 0.42, 24, 20, max(w, h), "#FFF4C2", 0.4, 5, 180, 360),
         sun(w * 0.5, h * 0.42, min(30, h * 0.07), color="#FFE680", op=0.3), hills(w, h, h * 0.44, seed, "#6A8A5A", amp=8, step=80), ground(w, h, h * 0.48, "#9CCB5E", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.49)} {f(h * 0.48)} L {f(w * 0.51)} {f(h * 0.48)} L {f(w * 0.7)} {f(h + 10)} Z" fill="#E8C88A" stroke="{INK}" stroke-width="2"></path>']
    return "".join(o)

def barns(w, h, seed):
    """Thy barns filled with plenty, and thy vats overflowing with new wine."""
    b = h * 0.9
    o = [sky(w, h, "#8FD0E2", "#FFF4C2"), ground(w, h, b, "#C8A06A", dy=0),
         EG.granaries(w * 0.06, b, 3, min(w * 0.12, h * 0.3), min(h * 0.36, w * 0.14), shrink=0.9),
         R.heap(w * 0.44, b, w * 0.16, h * 0.14), R.sheaf(w * 0.5, b, min(1.6, h / 160)), R.sheaf(w * 0.4, b, min(1.6, h / 160))]
    vx, vw, vh = w * 0.78, min(w * 0.26, h * 0.6), h * 0.26
    o.append(f'<rect x="{f(vx - vw / 2)}" y="{f(b - vh)}" width="{f(vw)}" height="{f(vh)}" fill="#8A6A5A" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(vx - vw / 2 + 6)}" y="{f(b - vh + 4)}" width="{f(vw - 12)}" height="{f(vh * 0.3)}" fill="#6A0E2A"></rect>'
             f'<path d="M{f(vx - vw / 2)} {f(b - vh + 2)} C {f(vx - vw / 2 - 14)} {f(b - vh * 0.5)} {f(vx - vw / 2 - 6)} {f(b - 10)} {f(vx - vw / 2 - 20)} {f(b)}" fill="none" stroke="#8A0E2A" stroke-width="7" stroke-linecap="round"></path>'
             f'<path d="M{f(vx + vw / 2)} {f(b - vh + 2)} C {f(vx + vw / 2 + 14)} {f(b - vh * 0.5)} {f(vx + vw / 2 + 6)} {f(b - 10)} {f(vx + vw / 2 + 20)} {f(b)}" fill="none" stroke="#8A0E2A" stroke-width="7" stroke-linecap="round"></path>')
    o.append(N.grapes(vx - vw * 0.2, b - vh - 6, min(0.6, h / 300), seed) + N.grapes(vx + vw * 0.15, b - vh - 4, min(0.6, h / 300), seed + 1))
    return "".join(o)

def tree_of_life(p, w, h, seed):
    """She is a tree of life to them that lay hold upon her: Wisdom beside a great tree laden with fruit, in gold light."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.62, seed, "#6A9A4A", amp=8, step=80), ground(w, h, h * 0.7, "#9CCB5E", dy=0)]
    s = min(fit(b, h * 0.46), 1.3)
    o.append(EM.tree(w * 0.58, b, min(2.6, (b - h * 0.08) / 112)))
    o.append(wisdom_fig(p, w * 0.32, b, s))
    o.append(son_fig(p, w * 0.82, b, s * 0.9, flip=True, up=[(-22, -158), (-44, -176), (-64, -200)]))
    return "".join(o)

def founded(w, h, seed):
    """Jehovah by wisdom founded the earth; by understanding he established the heavens; the depths broken up, the skies
    dropping down the dew (God is never drawn)."""
    r = random.Random(seed)
    o = [sky(w, h, "#0B0B2A", "#5B2470"), mk.stars(60, w, h * 0.5, seed), EM.rays(w * 0.5, -h * 0.1, 30, 30, max(w, h) * 1.2, "#FFF4C2", 0.25, 5, 20, 160),
         hills(w, h, h * 0.62, seed, "#2E6B3A", amp=14, step=70), f'<rect x="-10" y="{f(h * 0.72)}" width="{f(w + 20)}" height="{f(h)}" fill="#1F6F9A"></rect>',
         "".join(f'<path d="M{f(x)} {f(h * 0.72 + 10 + (i % 3) * 14)} q 14 -6 28 0" fill="none" stroke="#E8F6FA" stroke-width="2"></path>' for i, x in enumerate(range(10, int(w), 60)))]
    for _ in range(40):
        x, y = r.uniform(0, w), r.uniform(h * 0.1, h * 0.6)
        o.append(f'<path d="M{f(x)} {f(y)} c 2 4 2 6 0 7 c -2 -1 -2 -3 0 -7 Z" fill="#CFEFFF" opacity="0.8"></path>')
    return "".join(o)

def sleep_secure(p, w, h, seed):
    """When thou liest down, thou shalt not be afraid: the son asleep on his mat at the tent door under the stars."""
    b = h * 0.88
    o = [sky(w, h, "#05050A", "#1E1650"), mk.stars(50, w, h * 0.6, seed), f'<circle cx="{f(w * 0.8)}" cy="{f(h * 0.22)}" r="{f(min(26, h * 0.07))}" fill="#F3EFE6"></circle>',
         hills(w, h, h * 0.62, seed, "#14141E", amp=8, step=80), ground(w, h, h * 0.7, "#2A2430", dy=0)]
    s = min(1.6, h / 220)
    o.append(J1.tent_big(w * 0.3, b, 220 * s, 130 * s, color="#3A2A2A", stripe="#5A4A3A", open_=True, glow="#FFC14D"))
    o.append(S1.mat_sleeper(w * 0.56, b, s, color=SON_C, head="#2A1A10"))
    return "".join(o)

def neighbor_door(p, w, h, seed):
    """Say not unto thy neighbor, Go, and come again: a man at the door asking, the householder within with bread by him."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE3B8", "#E8C88A"), ground(w, h, b, "#C8A06A", dy=0)]
    hw, hh = min(w * 0.5, h * 1.0), h * 0.7
    o.append(f'<rect x="{f(w * 0.5)}" y="{f(b - hh)}" width="{f(hw)}" height="{f(hh)}" fill="#D8C8A0" stroke="{INK}" stroke-width="2.4"></rect>')
    dx, dw = w * 0.5 + hw * 0.18, hw * 0.34
    o.append(f'<rect x="{f(dx)}" y="{f(b - hh * 0.8)}" width="{f(dw)}" height="{f(hh * 0.8)}" fill="#3A2214" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, b - hh * 0.72)
    o.append(man(p, dx + dw / 2, b, s, "#7A5A3A", flip=True))
    o.append("".join(f'<ellipse cx="{f(dx + dw + 40 * s + i * 30 * s)}" cy="{f(b - 6 * s)}" rx="{f(14 * s)}" ry="{f(7 * s)}" fill="#C8862E" stroke="{INK}" stroke-width="1.6"></ellipse>' for i in range(2)))
    o.append(man(p, w * 0.3, b, s, "#5A6A3A", up=[(-22, -158), (2, -140), (26, -146)], flip=True))
    return "".join(o)
