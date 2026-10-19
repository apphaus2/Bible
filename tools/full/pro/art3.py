"""Drawings for Proverbs 7–9 (chapter 3 of the volume), on top of pro.art2 (everything there is re-exported here).
Proverbs 7 is drawn with restraint: the father at his lattice, the street at twilight, the far veiled figure at the corner,
the shut house with its lamp, the full moon on the road, the ox led on its rope and the bird to the snare, the stair going
down into the dark — her words are in song boxes, and no one is drawn near."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from pro.art2 import *
from pro.art2 import f, K2, K1, EM, INK, SON_C, WIS_C, STRANGE_C, glow, son_fig, wisdom_fig, veiled, emb_art, deer, stone_well

def wisdom_son(p, w, h, seed):
    """Say unto wisdom, Thou art my sister: Wisdom in white and gold light, the son beside her on the road."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.6, seed, "#6A9A4A", amp=8, step=80), ground(w, h, h * 0.68, "#9CCB5E", dy=0)]
    s = min(fit(b, h * 0.3), 1.1)
    o.append(wisdom_fig(p, w * 0.42, b, s))
    o.append(son_fig(p, w * 0.56, b, s * 0.96, flip=True))
    return "".join(o)

def street_row(w, h, base, seed, lit=False, color="#3A2A3A"):
    """A row of flat-roofed houses along a street."""
    r = random.Random(seed); o = []; x = -20
    while x < w + 20:
        hw = r.uniform(70, 130); hh = r.uniform(h * 0.22, h * 0.4)
        o.append(f'<rect x="{f(x)}" y="{f(base - hh)}" width="{f(hw)}" height="{f(hh)}" fill="{color}" stroke="{INK}" stroke-width="2"></rect>')
        if r.random() < 0.6:
            o.append(f'<rect x="{f(x + hw * 0.3)}" y="{f(base - hh * 0.7)}" width="10" height="12" fill="{"#FFC14D" if lit and r.random() < 0.5 else "#12090A"}"></rect>')
        x += hw
    return "".join(o)

def lattice_window(p, w, h, seed):
    """For at the window of my house I looked forth through my lattice: the father at his lattice above the street at
    twilight, a young man passing below near the corner."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A4A", "#C8603A"), street_row(w * 0.6, h, h * 0.7, seed, lit=True), ground(w, h, h * 0.7, "#3A2A2A", dy=0)]
    lx, lw = w * 0.62, w * 0.38
    o.append(f'<rect x="{f(lx)}" y="-10" width="{f(lw + 10)}" height="{f(h + 20)}" fill="#5A3A2A" stroke="{INK}" stroke-width="2.4"></rect>')
    wx, ww, wy, wh = lx + lw * 0.12, lw * 0.6, h * 0.14, h * 0.46
    o.append(f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}" fill="#FFC14D" stroke="{INK}" stroke-width="2"></rect>')
    s = min(wh / 230, 1.2)
    o.append(K1.sol_fig(p, wx + ww * 0.5, wy + wh + 10 * s, s, flip=True))
    for i in range(7):
        o.append(f'<path d="M{f(wx + (i + 1) * ww / 8)} {f(wy)} L {f(wx + (i + 1) * ww / 8)} {f(wy + wh)}" stroke="#5A3A22" stroke-width="3"></path>')
    for j in range(1, 6):
        o.append(f'<path d="M{f(wx)} {f(wy + j * wh / 6)} L {f(wx + ww)} {f(wy + j * wh / 6)}" stroke="#5A3A22" stroke-width="3"></path>')
    s2 = min(fit(b, h * 0.6), 0.6)
    o.append(man(p, w * 0.24, b, s2, "#7A3A5A"))
    return "".join(o)

def corner_dusk(p, w, h, seed, figure=True):
    """In the twilight, in the evening of the day: the corner of the street at dusk, a far veiled figure waiting there."""
    b = h * 0.88
    o = [mk.defs(p, *ALL), sky(w, h, "#1A0A2A", "#8A2A3A"), street_row(w, h, h * 0.74, seed, lit=True, color="#2A1A2A"), ground(w, h, h * 0.74, "#2A1A20", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.46)} {f(h * 0.74)} L {f(w * 0.54)} {f(h * 0.74)} L {f(w * 0.7)} {f(h + 10)} Z" fill="#4A3A3A" stroke="{INK}" stroke-width="2"></path>']
    if figure:
        o.append(veiled(p, w * 0.78, h * 0.78, min(fit(h * 0.78, h * 0.5), 0.5), flip=True))
    return "".join(o)

def shut_house(p, w, h, seed, moon=False):
    """A shut house in the night, a lamp in its window (no one drawn)."""
    b = h * 0.9
    o = [sky(w, h, "#05050A", "#1E1650"), mk.stars(40, w, h * 0.5, seed), ground(w, h, b, "#14141E", dy=0)]
    if moon:
        o.append(f'<circle cx="{f(w * 0.8)}" cy="{f(h * 0.24)}" r="{f(min(34, h * 0.1))}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></circle>' + glow(w * 0.8, h * 0.24, min(80, h * 0.25), "#F3EFE6", 0.25))
    hw, hh = min(w * 0.4, h * 1.0), h * 0.6
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(b - hh)}" width="{f(hw)}" height="{f(hh)}" fill="#2A2030" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.3 + hw * 0.6)}" y="{f(b - hh * 0.75)}" width="{f(hw * 0.16)}" height="{f(hh * 0.2)}" fill="#FFC14D" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<rect x="{f(w * 0.3 + hw * 0.16)}" y="{f(b - hh * 0.55)}" width="{f(hw * 0.22)}" height="{f(hh * 0.55)}" fill="#12090A" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o)

def moon_road(w, h, seed):
    """He will come home at the full moon: an empty road into the hills under the full moon."""
    o = [sky(w, h, "#05050A", "#1E1650"), mk.stars(50, w, h * 0.6, seed), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.3)}" r="{f(min(40, h * 0.12))}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></circle>',
         glow(w * 0.5, h * 0.3, min(110, h * 0.35), "#F3EFE6", 0.2), hills(w, h, h * 0.6, seed, "#14141E", amp=12, step=80), ground(w, h, h * 0.66, "#2A2430", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.44)} {f(h * 0.8)} {f(w * 0.5)} {f(h * 0.7)} {f(w * 0.52)} {f(h * 0.66)} L {f(w * 0.55)} {f(h * 0.66)} C {f(w * 0.56)} {f(h * 0.74)} {f(w * 0.6)} {f(h * 0.86)} {f(w * 0.66)} {f(h + 10)} Z" fill="#5A5060" stroke="{INK}" stroke-width="2"></path>']
    return "".join(o)

def ox_snare(p, w, h, seed):
    """As an ox goeth to the slaughter, as a bird hasteth to the snare: an ox led along on its rope, a bird flying down to a
    net spread on the ground (nothing slain is drawn)."""
    b = h * 0.9
    k = min(1.3, h / 170)
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#E8D8C0"), ground(w, h, b, "#9A8A6A", dy=0)]
    o.append(S1.cow(w * 0.3, b, k * 0.8, color="#8A5A30", patch="#E8E2D6"))
    o.append(f'<path d="M{f(w * 0.3 + 104 * k * 0.8)} {f(b - 70 * k * 0.8)} C {f(w * 0.46)} {f(b - 40 * k)} {f(w * 0.5)} {f(b - 80 * k)} {f(w * 0.52)} {f(b - 96 * k)}" fill="none" stroke="#5A3A22" stroke-width="2.4"></path>')
    o.append(man(p, w * 0.54, b, min(fit(b, h * 0.3), 0.9), "#3A3A3A", up=[(-22, -158), (-30, -120), (-40, -100)]))
    nw = 140 * k
    for i in range(8):
        x = w * 0.72 + i * nw / 7
        o.append(f'<path d="M{f(x)} {f(b)} L {f(x + nw / 7)} {f(b - 30 * k)} M{f(x + nw / 7)} {f(b)} L {f(x)} {f(b - 30 * k)}" stroke="#5A4A3A" stroke-width="1.4"></path>')
    o.append(EM.E4quail(w * 0.8, b - 100 * k).replace("scale(0.8", f"scale({f(k * 0.9)}"))
    return "".join(o)

def stair_down(w, h, seed):
    """Her house is the way to Sheol, going down to the chambers of death: a stair cut in the rock going down into the dark."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#05050A"></rect>']
    n = 9
    for i in range(n):
        t = i / n
        x0, x1 = w * (0.18 + t * 0.22), w * (0.82 - t * 0.22)
        y = h * (0.2 + t * 0.8)
        c = int(90 - t * 80)
        o.append(f'<path d="M{f(x0)} {f(y)} L {f(x1)} {f(y)} L {f(x1 - w * 0.02)} {f(y + h * 0.09)} L {f(x0 + w * 0.02)} {f(y + h * 0.09)} Z" fill="rgb({c},{c - 10 if c > 10 else 0},{c})" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(f'<path d="M-10 -10 L {f(w * 0.18)} {f(h * 0.2)} L {f(w * 0.4)} {f(h + 10)} L -10 {f(h + 10)} Z M{f(w + 10)} -10 L {f(w * 0.82)} {f(h * 0.2)} L {f(w * 0.6)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} Z" fill="#2A2420" stroke="{INK}" stroke-width="2"></path>')
    return "".join(o)

def before_earth(w, h, seed):
    """Before the mountains were settled, when there were no depths: a dark deep, a faint light upon it (God never drawn)."""
    o = [sky(w, h, "#05050A", "#12113A"), mk.stars(20, w, h * 0.5, seed), EM.rays(w * 0.5, -h * 0.2, 26, 40, max(w, h) * 1.2, "#FFF4C2", 0.15, 5, 30, 150),
         f'<rect x="-10" y="{f(h * 0.6)}" width="{f(w + 20)}" height="{f(h)}" fill="#0B1A2E"></rect>']
    for i in range(6):
        y = h * (0.64 + i * 0.06)
        o.append(f'<path d="M-10 {f(y)} ' + " ".join(f"Q {f(x + 30)} {f(y - 5)} {f(x + 60)} {f(y)}" for x in range(-10, int(w) + 60, 60)) + '" fill="none" stroke="#1F4A6A" stroke-width="2"></path>')
    return "".join(o)

def circle_deep(w, h, seed):
    """When he set a circle upon the face of the deep, and gave to the sea its bound: the curve of the sea's edge under the
    firmament, the shore holding it, the stars above."""
    o = [sky(w, h, "#05050A", "#1E1650"), mk.stars(60, w, h * 0.55, seed),
         f'<path d="M-10 {f(h * 0.62)} Q {f(w * 0.5)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1F6F9A" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M-10 {f(h * 0.62)} Q {f(w * 0.5)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.62)}" fill="none" stroke="#FFD23F" stroke-width="2" stroke-dasharray="8 6"></path>',
         f'<path d="M-10 {f(h * 0.9)} C {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.6)} {f(h * 0.86)} {f(w + 10)} {f(h * 0.78)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8A06A" stroke="{INK}" stroke-width="2"></path>']
    for i in range(5):
        y = h * (0.66 + i * 0.045)
        o.append("".join(f'<path d="M{f(x)} {f(y)} q 12 -5 24 0" fill="none" stroke="#E8F6FA" stroke-width="1.6"></path>' for x in range(int(20 + i * 17), int(w), 90)))
    return "".join(o)

def habitable_earth(p, w, h, seed):
    """Rejoicing in his habitable earth, and my delight was with the sons of men: green hills, a town and its fields, people
    at work, Wisdom in the light."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.52, seed, "#6A9A4A", amp=10, step=80), J.city_hill(w * 0.8, h * 0.6, w * 0.3, h * 0.2, seed),
         ground(w, h, h * 0.62, "#9CCB5E", dy=0), R.field(w * 0.36, w * 0.66, h * 0.72, h * 0.12, seed, rows=2)]
    s = min(fit(b, h * 0.36), 1.0)
    o.append(wisdom_fig(p, w * 0.18, b, s))
    o.append(R.reaper(p, w * 0.46, b, s * 0.7) + man(p, w * 0.58, b, s * 0.72, "#5A3A22") + woman(p, w * 0.64, b, s * 0.68, "#7A3A6A") + man(p, w * 0.69, b, s * 0.46, "#C8A06A"))
    return "".join(o)

def seven_pillars(p, w, h, seed, maidens=True):
    """Wisdom hath builded her house; she hath hewn out her seven pillars; her table furnished, her maidens sent forth."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFE3B8"), ground(w, h, b, "#E8C88A", dy=0)]
    hx0, hx1 = w * 0.14, w * 0.86
    top = h * 0.2
    o.append(f'<path d="M{f(hx0 - 20)} {f(top)} L {f((hx0 + hx1) / 2)} {f(top - h * 0.12)} L {f(hx1 + 20)} {f(top)} Z" fill="#E8D8B0" stroke="{INK}" stroke-width="2.4"></path>'
             f'<rect x="{f(hx0 - 20)}" y="{f(top)}" width="{f(hx1 - hx0 + 40)}" height="{f(h * 0.06)}" fill="#E8B830" stroke="{INK}" stroke-width="2.2"></rect>'
             f'<rect x="{f(hx0 - 30)}" y="{f(b - h * 0.04)}" width="{f(hx1 - hx0 + 60)}" height="{f(h * 0.04)}" fill="#D8C8A0" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(hx0)}" y="{f(top + h * 0.06)}" width="{f(hx1 - hx0)}" height="{f(b - h * 0.04 - top - h * 0.06)}" fill="#5A3A2A"></rect>')
    pw = (hx1 - hx0) / 7 * 0.36
    for i in range(7):
        x = hx0 + (i + 0.5) * (hx1 - hx0) / 7
        o.append(f'<rect x="{f(x - pw / 2)}" y="{f(top + h * 0.06)}" width="{f(pw)}" height="{f(b - h * 0.04 - top - h * 0.06)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(x - pw * 0.7)}" y="{f(top + h * 0.06)}" width="{f(pw * 1.4)}" height="{f(h * 0.03)}" fill="#E8D8B0" stroke="{INK}" stroke-width="1.6"></rect>')
    ty = b - h * 0.16
    o.append(glow(w * 0.5, ty - h * 0.1, h * 0.3, "#FFC14D", 0.3))
    o.append(f'<rect x="{f(w * 0.36)}" y="{f(ty)}" width="{f(w * 0.28)}" height="{f(h * 0.03)}" fill="#8A5A30" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.38)} {f(ty)} L {f(w * 0.38)} {f(b - h * 0.04)} M{f(w * 0.62)} {f(ty)} L {f(w * 0.62)} {f(b - h * 0.04)}" stroke="#5A3A22" stroke-width="4"></path>')
    for i, x in enumerate((0.42, 0.5, 0.58)):
        o.append(EM.lamp_shape(w * x, ty, 0.3, lit=True) if i == 1 else f'<ellipse cx="{f(w * x)}" cy="{f(ty - 4)}" rx="{f(w * 0.025)}" ry="{f(h * 0.012)}" fill="#C8862E" stroke="{INK}" stroke-width="1.4"></ellipse>')
    s = min(fit(b, h * 0.42), 1.0)
    o.append(wisdom_fig(p, w * 0.5, b - h * 0.04, s * 0.9, light=False))
    if maidens:
        for i, x in enumerate((0.06, 0.94)):
            o.append(woman(p, w * x, b + 2, s * 0.82, "#E8D8B0", flip=x > 0.5))
    return "".join(o)

def folly_door(p, w, h, seed):
    """The foolish woman sitteth at the door of her house, on a seat in the high places of the city: a dark house at the top of
    the street at dusk, a far figure at its door calling to them that pass by."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A", "#C8603A"), J.city_hill(w * 0.5, h * 0.56, w * 0.7, h * 0.26, seed), ground(w, h, h * 0.62, "#5A4A4A", dy=0)]
    hw, hh = min(w * 0.22, h * 0.6), h * 0.3
    hx = w * 0.62
    o.append(f'<rect x="{f(hx)}" y="{f(h * 0.62 - hh)}" width="{f(hw)}" height="{f(hh)}" fill="#3A2A3A" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(hx + hw * 0.36)}" y="{f(h * 0.62 - hh * 0.6)}" width="{f(hw * 0.28)}" height="{f(hh * 0.6)}" fill="#D7261E" opacity="0.7" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(veiled(p, hx - 14, h * 0.62, min(hh / 200, 0.5), flip=True))
    s = min(fit(b, h * 0.5), 0.7)
    for i in range(3):
        o.append(man(p, w * (0.12 + i * 0.1), b - i * 4, s * (1 - i * 0.08), ("#5A4A3A", "#3A4A5A", "#4A5A3A")[i]))
    return "".join(o)
