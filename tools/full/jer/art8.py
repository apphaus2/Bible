"""Drawings for Jeremiah chapter 8 (Jeremiah 23–25), on top of jer.art: the scattered flock and the folds, the righteous
Branch, the whirling tempest, the dreamer, the hammer and the rock, the two baskets of figs, the cup of the wine of wrath and
the nations that drink it (a map)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2

def flock(w, h, seed, fold=False):
    """The sheep of my pasture scattered over the hills with no shepherd (fold=True: brought again to their folds, a shepherd
    standing by the stone fold)."""
    r = random.Random(seed)
    p = f"fk{seed}"
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8" if fold else "#8A7A8A", "#F3E8C8" if fold else "#D8B898"), hills(w, h, h * 0.44, seed, "#7A8A5A", amp=14, step=70),
         ground(w, h, h * 0.56, "#9AAA6A" if fold else "#A89A6A", dy=0)]
    s = min(0.7, h / 360)
    if fold:
        o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.94)} L {f(w * 0.3)} {f(h * 0.7)} L {f(w * 0.86)} {f(h * 0.7)} L {f(w * 0.86)} {f(h * 0.94)}" fill="none" stroke="#8A8478" stroke-width="{f(h * 0.04)}"></path>')
        for i in range(10): o.append(E.sheep(w * (0.36 + (i % 5) * 0.1), h * (0.8 + (i // 5) * 0.1), s))
        o.append(man(p, w * 0.16, h * 0.96, fit(h * 0.96, h * 0.56), "#6A5A3A", extra=A.headcloth("#6A5A3A") + A.BLACK_BEARD))
    else:
        for _ in range(12):
            o.append(E.sheep(w * r.uniform(0.04, 0.96), h * r.uniform(0.6, 0.96), s * r.uniform(0.6, 1.0), flip=r.random() < 0.5))
    return "".join(o)

def branch(w, h, seed):
    """I will raise unto David a righteous Branch: a green shoot rising from the stump of a felled tree at dawn, a small gold
    crown resting on the stump."""
    o = [K2.sky(w, h, "#3A3A7A", "#FFD890"), sun(w * 0.5, h * 0.72, min(w, h) * 0.08, color="#FFE680", op=0.35), ground(w, h, h * 0.78, "#5A6A3A", dy=0)]
    sx, sy, sw = w * 0.5, h * 0.82, min(w * 0.18, h * 0.3)
    o.append(f'<path d="M{f(sx - sw / 2)} {f(sy + 8)} L {f(sx - sw * 0.4)} {f(sy - sw * 0.5)} L {f(sx + sw * 0.4)} {f(sy - sw * 0.5)} L {f(sx + sw / 2)} {f(sy + 8)} Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(sx)}" cy="{f(sy - sw * 0.5)}" rx="{f(sw * 0.4)}" ry="{f(sw * 0.1)}" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    o.append(f'<path d="M{f(sx + sw * 0.1)} {f(sy - sw * 0.5)} C {f(sx + sw * 0.2)} {f(sy - sw * 1.1)} {f(sx - sw * 0.1)} {f(sy - sw * 1.4)} {f(sx + sw * 0.05)} {f(sy - sw * 1.9)}" stroke="#3E7A3A" stroke-width="5" fill="none"></path>')
    for k in range(5):
        t = 0.3 + k * 0.15; y = sy - sw * (0.5 + t * 1.4); x = sx + sw * (0.1 - k * 0.02)
        d = 1 if k % 2 else -1
        o.append(f'<path d="M{f(x)} {f(y)} q {f(d * sw * 0.2)} {f(-sw * 0.1)} {f(d * sw * 0.3)} {f(sw * 0.05)} q {f(-d * sw * 0.1)} {f(sw * 0.1)} {f(-d * sw * 0.3)} {f(-sw * 0.05)} Z" fill="#6AAA4A" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append(S2.crown(sx - sw * 0.2, sy - sw * 0.56, min(0.8, sw / 120)))
    return "".join(o)

def tempest(w, h, seed):
    """Behold, the tempest of Jehovah, even his wrath, is gone forth, a whirling tempest: a dark funnel of cloud over the land,
    lightning."""
    o = [K2.sky(w, h, "#1A1A2A", "#5A5A6A")]
    for i in range(8):
        o.append(f'<ellipse cx="{f(w * 0.5 + (i % 2 - 0.5) * w * 0.04)}" cy="{f(h * (0.12 + i * 0.09))}" rx="{f(w * (0.36 - i * 0.04))}" ry="{f(h * 0.05)}" fill="none" stroke="#8A8A9A" stroke-width="{f(6 - i * 0.5)}" opacity="0.8"></ellipse>')
    o.append(E2.bolt(w * 0.2, h * 0.1, h * 0.6, seed) + E2.bolt(w * 0.82, h * 0.16, h * 0.5, seed + 1))
    o.append(hills(w, h, h * 0.84, seed, "#2A2A30", amp=8, step=80))
    return "".join(o)

def dreamer(w, h, seed):
    """The prophets that say, I have dreamed, I have dreamed: a man asleep under a rug at night, empty dream-shapes above him."""
    o = [night(w, h, seed, "#1A1430"), f'<rect x="-10" y="{f(h * 0.78)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#3A2A2A"></rect>',
         J1.rug_sleeper(w * 0.4, h * 0.86, min(1.2, h / 200), color="#6A4A2A")]
    for i, (x, y, r_) in enumerate(((0.56, 0.58, 0.04), (0.64, 0.42, 0.06), (0.76, 0.24, 0.1))):
        o.append(f'<ellipse cx="{f(w * x)}" cy="{f(h * y)}" rx="{f(w * r_)}" ry="{f(w * r_ * 0.6)}" fill="none" stroke="#C8B8E8" stroke-width="2" stroke-dasharray="6 5"></ellipse>')
    return "".join(o)

def hammer_rock(w, h, seed):
    """Is not my word like fire? and like a hammer that breaketh the rock in pieces?: a great hammer striking a rock in a burst
    of sparks (no hand drawn)."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1012"></rect>', V.rays(w * 0.5, h * 0.66, 30, 10, max(w, h), color="#FF8A2A", op=0.14),
         crag(w * 0.3, w * 0.7, h * 0.98, h * 0.62, color="#7A6A6A", dark="#4A3A3A")]
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.62)} l -12 30 l 18 20 l -10 30" stroke="#FFC14D" stroke-width="3" fill="none"></path>')
    hx, hy = w * 0.56, h * 0.36
    o.append(f'<g transform="rotate(-28 {f(hx)} {f(hy)})"><rect x="{f(hx - w * 0.08)}" y="{f(hy - h * 0.08)}" width="{f(w * 0.16)}" height="{f(h * 0.14)}" fill="#5A5A62" stroke="#0D0D0F" stroke-width="2.6"></rect>'
             f'<rect x="{f(hx - 6)}" y="{f(hy - h * 0.5)}" width="12" height="{f(h * 0.42)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect></g>')
    for _ in range(18):
        a = r.uniform(-math.pi, 0); L = r.uniform(20, 60)
        o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.62)} l {f(math.cos(a) * L)} {f(math.sin(a) * L)}" stroke="#FFE680" stroke-width="2"></path>')
    return "".join(o)

def figs(w, h, seed, bad=None):
    """Two baskets of figs set before the temple of Jehovah: one of very good figs, like the first-ripe, the other of very bad
    figs, which could not be eaten (bad=True: the bad basket alone; False: the good alone)."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8FB0C8", "#F3E0B0"), temple_front(w * 0.5, h * 0.62, w * 0.5, seed), ground(w, h, h * 0.62, "#D8C8A0", dy=0)]
    baskets = [(0.3, True), (0.7, False)] if bad is None else [(0.5, not bad)]
    s = min(1.6, h / 170)
    for x, good in baskets:
        bx, by = w * x, h * 0.94
        o.append(f'<path d="M{f(bx - 50 * s)} {f(by - 40 * s)} L {f(bx + 50 * s)} {f(by - 40 * s)} L {f(bx + 40 * s)} {f(by)} L {f(bx - 40 * s)} {f(by)} Z" fill="#C8A060" stroke="#0D0D0F" stroke-width="2.2"></path>'
                 + "".join(f'<path d="M{f(bx - 46 * s + k * 9 * s)} {f(by - 40 * s)} L {f(bx - 36 * s + k * 8 * s)} {f(by)}" stroke="#8A6A3A" stroke-width="1.4"></path>' for k in range(11)))
        for k in range(9):
            fx, fy = bx + r.uniform(-38, 38) * s, by - 44 * s - r.uniform(0, 14) * s
            c = r.choice(["#6A2A5A", "#7A3A6A", "#5A2A4A"]) if good else r.choice(["#5A5A3A", "#4A4030", "#6A5A40"])
            o.append(f'<ellipse cx="{f(fx)}" cy="{f(fy)}" rx="{f(9 * s)}" ry="{f(11 * s)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
                     + (f'<circle cx="{f(fx + 3 * s)}" cy="{f(fy - 2 * s)}" r="{f(2 * s)}" fill="#2A2418"></circle>' if not good else ""))
    return "".join(o)

def millstones_lamp(w, h, seed):
    """I will take from them the sound of the millstones, and the light of the lamp: a hand-mill standing idle, a clay lamp gone
    out, a thread of smoke."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2220"></rect>', ground(w, h, h * 0.8, "#3A3028", dy=0), JG2.mill(w * 0.34, h * 0.86, min(1.3, h / 200)),
         f'<path d="M{f(w * 0.62)} {f(h * 0.84)} Q {f(w * 0.68)} {f(h * 0.74)} {f(w * 0.76)} {f(h * 0.8)} L {f(w * 0.8)} {f(h * 0.78)} L {f(w * 0.78)} {f(h * 0.84)} Z" fill="#B8783A" stroke="#0D0D0F" stroke-width="2"></path>',
         smoke(w * 0.79, h * 0.7, 5, seed, r0=0.012, w=0.4, color="#8A8A8A", op=0.5)]
    return "".join(o)

def seventy(w, h, seed):
    """These nations shall serve the king of Babylon seventy years: seventy marks on a board, counted off."""
    o = [grid_bg(w, h, color="#3A2A5A", bg="#1A1430")]
    cols, rows = 14, 5
    for i in range(70):
        c, r_ = i % cols, i // cols
        x = w * (0.08 + 0.84 * c / (cols - 1)); y = h * (0.3 + 0.44 * r_ / (rows - 1))
        o.append(f'<rect x="{f(x - 6)}" y="{f(y - 9)}" width="12" height="18" fill="#FFD23F" fill-opacity="0.25" stroke="#FFD23F" stroke-width="1.4"></rect>')
    o.append(label(w * 0.5, h * 0.9, "SEVENTY YEARS · THE KING OF BABYLON", "#FFD23F", 11))
    return "".join(o)

def cup(w, h, seed):
    """Take this cup of the wine of wrath at my hand: a great cup brimming with dark wine on a stone (no hand drawn)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A0E14"></rect>', V.rays(w * 0.5, h * 0.6, 24, 10, max(w, h), color="#B5121B", op=0.14)]
    cx, cy, s = w * 0.5, h * 0.94, min(2.0, h / 150)
    o.append(f'<path d="M{f(cx - 50 * s)} {f(cy - 100 * s)} L {f(cx + 50 * s)} {f(cy - 100 * s)} Q {f(cx + 44 * s)} {f(cy - 40 * s)} {f(cx + 8 * s)} {f(cy - 32 * s)} L {f(cx + 8 * s)} {f(cy - 10 * s)} L {f(cx + 28 * s)} {f(cy)} L {f(cx - 28 * s)} {f(cy)} L {f(cx - 8 * s)} {f(cy - 10 * s)} L {f(cx - 8 * s)} {f(cy - 32 * s)} Q {f(cx - 44 * s)} {f(cy - 40 * s)} {f(cx - 50 * s)} {f(cy - 100 * s)} Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="2.6"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy - 100 * s)}" rx="{f(50 * s)}" ry="{f(9 * s)}" fill="#5A0A1A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<path d="M{f(cx + 40 * s)} {f(cy - 98 * s)} q {f(6 * s)} {f(20 * s)} 0 {f(36 * s)}" stroke="#8A0E16" stroke-width="{f(4 * s)}" fill="none" stroke-linecap="round"></path>')
    return "".join(o)

def grape_tread(w, h, seed):
    """He will give a shout, as they that tread the grapes: the winepress cut in the rock, full of red, under a dark sky."""
    o = [K2.sky(w, h, "#2A0A1A", "#8A2A3A"), ground(w, h, h * 0.6, "#5A3A3A", dy=0), J1.winepress(w * 0.5, h * 0.8, w * 0.5, h * 0.24),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.82)}" rx="{f(w * 0.22)}" ry="{f(h * 0.08)}" fill="#7A0A2A"></ellipse>']
    for i in range(6): o.append(N.grapes(w * (0.12 + i * 0.16), h * 0.62, min(0.4, h / 900), seed + i))
    return "".join(o)

def shepherds_wail(p, w, h, seed):
    """Wail, ye shepherds, and wallow in ashes, ye principal of the flock: shepherds bowed in the ashes before an empty fold."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A3A4A", "#A89A9A"), hills(w, h, h * 0.5, seed, "#5A5A4A", amp=12, step=80), ground(w, h, h * 0.62, "#7A7268", dy=0),
         f'<path d="M{f(w * 0.56)} {f(h * 0.9)} L {f(w * 0.56)} {f(h * 0.7)} L {f(w * 0.96)} {f(h * 0.7)} L {f(w * 0.96)} {f(h * 0.9)}" fill="none" stroke="#8A8478" stroke-width="{f(h * 0.04)}"></path>']
    s = fit(b, h * 0.36)
    for i in range(3): o.append(E.kneel(w * (0.12 + i * 0.14), b, s, color=["#5A4A3A", "#4A4A4A", "#6A5A3A"][i], skin="#8A6A5A"))
    return "".join(o)
