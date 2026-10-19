"""Drawings for Ezekiel 12–14: the stuff for removing carried out by day and through the wall in the dark; the prince's net
and the way to Babylon; the bread eaten with quaking; the sealed vision; the foxes in the waste places and the gaps in the
wall; the wall daubed with untempered mortar, the shower, the hailstones and the stormy wind; the pillows and the
kerchiefs (objects only); the elders sitting before the prophet; Noah, Daniel and Job and the four sore judgments (a plate)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art3 import *
from ezk.art3 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2
import judges2 as JJ2
from neh.art import rubble

def bundle(x, y, s=1.0):
    """A bundle of stuff for removing, tied with cord."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">' + P("M-30 0 C -36 -24 -20 -40 0 -40 C 20 -40 36 -24 30 0 Z", "#B8946A", 2.2)
            + '<path d="M-26 -20 C -10 -14 10 -14 26 -20 M0 -40 L 0 0" stroke="#5A3A1A" stroke-width="2.4" fill="none"></path></g>')

def removing(p, w, h, seed, night=False):
    """Prepare thee stuff for removing: by day, Ezekiel bringing out his stuff before the onlookers; night=True: in the
    dark, digging through the wall and bearing it upon his shoulder, his face covered."""
    b = h * 0.95
    sky_ = ("#05051A", "#2A2A4A") if night else ("#6AB0D8", "#F3E0B0")
    o = [mk.defs(p, *ALL), bg(f"rm{seed}{night}", w, h, [(0, sky_[0]), (1, sky_[1])])]
    if night: o.append(mk.stars(40, w, h * 0.5, seed))
    o.append(f'<rect x="{f(w * 0.46)}" y="{f(h * 0.22)}" width="{f(w * 0.56)}" height="{f(h * 0.74)}" fill="{"#5A4A3A" if night else "#B8946A"}" stroke="{INK}" stroke-width="2.4"></rect>')
    for row in range(8):
        y = h * 0.22 + row * h * 0.092
        o.append(f'<path d="M{f(w * 0.46)} {f(y)} L {f(w + 10)} {f(y)}" stroke="{"#3A2A1A" if night else "#8A6A4A"}" stroke-width="1.2"></path>')
    o.append(ground(w, h, h * 0.95, "#3A3A3A" if night else "#A8906A", dy=0))
    s = min(fit(b, max(h * 0.42, b - 220)), 1.1)
    if night:
        o.append(P(f"M{f(w * 0.56)} {f(b)} L {f(w * 0.56)} {f(b - 120 * s)} Q {f(w * 0.62)} {f(b - 150 * s)} {f(w * 0.68)} {f(b - 120 * s)} L {f(w * 0.68)} {f(b)} Z", "#0B0B14", 2))
        o.append(mk.person(p, round(w * 0.36), round(b), round(s, 3), body=SKIN, cloth=EZ_C, sw=3, up=[(-22, -158), (-16, -190), (6, -200)],
                           extra=A.headcloth("#F3EFE6", cord="#1F5FAD") + P("M-16 -196 C -4 -204 10 -200 16 -190 L 16 -170 L -16 -170 Z", "#3A4A6A", 1.6)))
        o.append(bundle(w * 0.36 + 16 * s, b - 150 * s, s * 0.9))
    else:
        o.append(ezek_fig(p, w * 0.3, b, s, up=[(-22, -158), (-16, -190), (6, -200)]))
        o.append(bundle(w * 0.3 + 16 * s, b - 150 * s, s * 0.9))
        o.append(bundle(w * 0.16, b, s * 0.8) + bundle(w * 0.2, b - 2, s * 0.7))
        for i in range(4):
            o.append(captive_fig(p, w * (0.6 + i * 0.1), b - (i % 2) * 6, s * 0.86, i, flip=True))
    return "".join(o)

def snare(w, h):
    """My net also will I spread upon him: the way from Jerusalem to Babylon as a map, a net spread across it, the land of
    the Chaldeans that he shall not see."""
    o = [grid_bg(w, h)]
    J0, B = (w * 0.14, h * 0.5), (w * 0.86, h * 0.6)
    o.append(route([J0, (w * 0.4, h * 0.3), (w * 0.62, h * 0.32), B], color="#FF8A6A", sw=2.6))
    o.append(node(*J0, "JERUSALEM", "#D7261E", r=6, dy=-14, size=10) + node(*B, "BABYLON", "#FFD23F", r=6, dy=-14, size=10))
    cx, cy, R = w * 0.4, h * 0.36, min(w, h) * 0.18
    for k in range(-4, 5):
        o.append(f'<path d="M{f(cx - R + k * R / 4)} {f(cy - R)} L {f(cx + R + k * R / 4)} {f(cy + R)}" stroke="#C8C8D0" stroke-width="1.4" opacity="0.8"></path>'
                 f'<path d="M{f(cx + R + k * R / 4)} {f(cy - R)} L {f(cx - R + k * R / 4)} {f(cy + R)}" stroke="#C8C8D0" stroke-width="1.4" opacity="0.8"></path>')
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R * 1.05)}" fill="none" stroke="#C8C8D0" stroke-width="2.4"></circle>')
    o.append(label(w * 0.86, h * 0.76, "THE LAND OF THE CHALDEANS", "#FFD23F", 9))
    return "".join(o)

def quaking(p, w, h, seed):
    """Eat thy bread with quaking, and drink thy water with trembling: a low table, a loaf and a cup, trembling lines."""
    o = [bg(f"qk{seed}", w, h, [(0, "#2A2A3A"), (1, "#7A5A4A")]), f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#5A4030"></rect>']
    k = min(1.6, h / 220)
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(h * 0.7)}" width="{f(w * 0.4)}" height="{f(14 * k)}" fill="#8A5A30" stroke="{INK}" stroke-width="2.2"></rect>')
    o.append(f'<ellipse cx="{f(w * 0.42)}" cy="{f(h * 0.7 - 10 * k)}" rx="{f(28 * k)}" ry="{f(11 * k)}" fill="#C8A060" stroke="{INK}" stroke-width="2"></ellipse>')
    o.append(P(f"M{f(w * 0.56)} {f(h * 0.7)} L {f(w * 0.55)} {f(h * 0.7 - 30 * k)} L {f(w * 0.61)} {f(h * 0.7 - 30 * k)} L {f(w * 0.6)} {f(h * 0.7)} Z", "#8A6A5A", 2))
    for i in range(3):
        o.append(f'<path d="M{f(w * 0.38 - 10 * i)} {f(h * 0.7 - 30 * k - i * 8)} q 4 -6 8 0 t 8 0" stroke="#F3EFE6" stroke-width="2" fill="none"></path>'
                 f'<path d="M{f(w * 0.62 + 10 * i)} {f(h * 0.7 - 40 * k - i * 8)} q 4 -6 8 0 t 8 0" stroke="#F3EFE6" stroke-width="2" fill="none"></path>')
    return "".join(o)

def sealed_vision(w, h, seed):
    """The days are prolonged, and every vision faileth: a roll of a vision lying sealed and dusty — but the word shall be
    performed: light breaking upon it."""
    o = [bg(f"sv{seed}", w, h, [(0, "#1A1A2A"), (1, "#5A4A4A")]), glow(f"svg{seed}", w * 0.5, h * 0.6, w * 0.4, h * 0.4, "#FFE680", 0.45)]
    cx, cy = w * 0.5, h * 0.72; L = min(w * 0.5, h * 1.4)
    o.append(f'<rect x="{f(cx - L / 2)}" y="{f(cy - 22)}" width="{f(L)}" height="44" rx="22" fill="#D8C08A" stroke="{INK}" stroke-width="2.4"></rect>')
    for dx in (-L * 0.2, L * 0.2):
        o.append(f'<rect x="{f(cx + dx - 4)}" y="{f(cy - 24)}" width="8" height="48" fill="#8A2A2A" stroke="{INK}" stroke-width="1.4"></rect><circle cx="{f(cx + dx)}" cy="{f(cy + 24)}" r="9" fill="#B5121B" stroke="{INK}" stroke-width="1.6"></circle>')
    o.append(V.rays(cx, cy, 18, L * 0.3, L, color="#FFE680", op=0.18))
    return "".join(o)

def foxes(w, h, seed):
    """Thy prophets have been like foxes in the waste places; ye have not gone up into the gaps: a broken wall with its
    gaps open, foxes running among the ruins."""
    o = [bg(f"fx{seed}", w, h, [(0, "#5A4A6A"), (1, "#D8B080")]), hills(w, h, h * 0.5, seed, "#8A7A6A", amp=8, step=80)]
    o.append(J.jericho(-10, w * 0.3, h * 0.34, h * 0.78, seed, color="#A88A6A", towers=1, houses=False))
    o.append(J.jericho(w * 0.48, w * 0.72, h * 0.4, h * 0.78, seed + 1, color="#A88A6A", towers=0, houses=False))
    o.append(rubble(w * 0.3, w * 0.48, h * 0.8, h * 0.18, seed) + rubble(w * 0.72, w + 10, h * 0.8, h * 0.14, seed + 1))
    o.append(ground(w, h, h * 0.8, "#9A7A5A", dy=0))
    k = min(1.0, h / 300)
    o.append(JJ2.fox(w * 0.36, h * 0.92, k, brand=False) + JJ2.fox(w * 0.66, h * 0.96, k * 0.9, flip=True, brand=False))
    return "".join(o)

def daubed(w, h, seed, stage=0):
    """A wall daubed with untempered mortar: stage 0 the wall built and whitewashed; 1 the overflowing shower, the great
    hailstones and the stormy wind; 2 the wall fallen, its foundation laid bare."""
    o = [bg(f"db{seed}{stage}", w, h, [(0, "#1A1A2A" if stage else "#8FB0C8"), (1, "#6A6A7A" if stage else "#F3E8C8")])]
    if stage: o.append(clouds(w, h * 0.06, seed, n=8, color="#2A2A3A", op=0.95, ry=0.08))
    x0, x1, top, base = w * 0.12, w * 0.88, h * 0.4, h * 0.84
    if stage < 2:
        o.append(J.jericho(x0, x1, top, base, seed, color="#E8E2D6", towers=0, houses=False))
        if stage == 1:
            o.append(E2.hail(40, 0, w, h * 0.1, h * 0.9, seed))
            o.append("".join(f'<path d="M{f(x)} {f(h * 0.1)} L {f(x - 30)} {f(h * 0.9)}" stroke="#A8C8E8" stroke-width="1.6" opacity="0.6"></path>' for x in range(0, int(w) + 60, 26)))
            o.append(wind_lines(w, h, seed, n=7, color="#E8E2F0", op=0.6, y0=0.2, y1=0.6))
            o.append(f'<path d="M{f(w * 0.4)} {f(top + 6)} L {f(w * 0.43)} {f(base - 30)} L {f(w * 0.41)} {f(base)}" stroke="{INK}" stroke-width="2.4" fill="none"></path>')
    else:
        o.append(J.collapse(x0, x1, base, h * 0.36, seed, color="#E8E2D6"))
        o.append(f'<rect x="{f(x0)}" y="{f(base - 8)}" width="{f(x1 - x0)}" height="14" fill="#7A6A5A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(ground(w, h, base, "#6A5A4A", dy=0))
    return "".join(o)

def pillows(w, h, seed):
    """The pillows sewn upon all elbows and the kerchiefs for the head of persons of every stature, handfuls of barley and
    pieces of bread: the things alone, laid out on a dark floor."""
    r = random.Random(seed)
    o = [bg(f"pw{seed}", w, h, [(0, "#1A1020"), (1, "#4A2A3A")]), f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#3A2028" stroke="{INK}" stroke-width="2"></rect>']
    k = min(1.4, h / 240)
    for i in range(4):
        x = w * (0.1 + i * 0.12); y = h * (0.8 + (i % 2) * 0.06)
        o.append(f'<rect x="{f(x - 24 * k)}" y="{f(y - 12 * k)}" width="{f(48 * k)}" height="{f(24 * k)}" rx="{f(10 * k)}" fill="{["#8A2A6A", "#6A3A8A", "#B04A4A", "#8A6A2A"][i]}" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(3):
        x = w * (0.62 + i * 0.12); y = h * 0.66
        o.append(P(f"M{f(x - 20 * k)} {f(y)} L {f(x + 20 * k)} {f(y)} L {f(x + 26 * k)} {f(y + 56 * k)} L {f(x - 26 * k)} {f(y + 56 * k)} Z", ["#D8C8E8", "#E8D8A8", "#C8E0D8"][i], 1.8, ' opacity="0.9"'))
    o.append("".join(f'<ellipse cx="{f(w * 0.5 + r.uniform(-30, 30))}" cy="{f(h * 0.9 + r.uniform(-6, 6))}" rx="3" ry="1.6" fill="#E8C870"></ellipse>' for _ in range(30)))
    return "".join(o)

def three_men(p, w, h):
    """Though these three men, Noah, Daniel and Job, were in it: a plate of the four sore judgments — the sword, the
    famine, the evil beast, the pestilence — and the three men who should deliver but their own souls."""
    o = [mk.defs(p, *ALL), bp(w, h), title_bar(w, "MY FOUR SORE JUDGMENTS")]
    cw = w / 4
    icons = [("THE SWORD", lambda x, y, k: f'<path d="M{f(x)} {f(y + 30 * k)} L {f(x)} {f(y - 40 * k)} L {f(x + 6 * k)} {f(y - 30 * k)} L {f(x + 6 * k)} {f(y + 30 * k)} Z" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1.6"></path><rect x="{f(x - 12 * k)}" y="{f(y + 22 * k)}" width="{f(30 * k)}" height="{f(6 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></rect>'),
             ("FAMINE", lambda x, y, k: f'<path d="M{f(x - 26 * k)} {f(y)} L {f(x + 26 * k)} {f(y)} L {f(x + 18 * k)} {f(y + 26 * k)} L {f(x - 18 * k)} {f(y + 26 * k)} Z" fill="#B8946A" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M{f(x - 22 * k)} {f(y + 8 * k)} L {f(x + 22 * k)} {f(y + 8 * k)}" stroke="#7A5A3A" stroke-width="1.4"></path>'),
             ("EVIL BEASTS", lambda x, y, k: JJ2.lion(x - 30 * k, y + 30 * k, 0.5 * k, roar=True)),
             ("PESTILENCE", lambda x, y, k: f'<g opacity="0.85">' + "".join(f'<circle cx="{f(x + dx * k)}" cy="{f(y + dy * k)}" r="{f(rr * k)}" fill="#5A6A3A"></circle>' for dx, dy, rr in ((-14, 0, 16), (8, -6, 18), (20, 10, 12), (-4, 14, 14))) + '</g>')]
    k = min(1.4, h / 300)
    for i, (nm, fn) in enumerate(icons):
        x = cw * (i + 0.5)
        o.append(f'<rect x="{f(cw * i + 8)}" y="{f(h * 0.14)}" width="{f(cw - 16)}" height="{f(h * 0.4)}" fill="none" stroke="#8FD0E2" stroke-width="1.4"></rect>')
        o.append(fn(x, h * 0.32, k) + label(x, h * 0.5, nm, "#FFD23F", 9))
    s = min(fit(h * 0.95, h * 0.6), 0.8)
    for i, (nm, cl) in enumerate((("NOAH", "#3A5A8A"), ("DANIEL", "#7A2A5A"), ("JOB", "#ECE6D8"))):
        x = w * (0.3 + i * 0.2)
        o.append(mk.person(p, round(x), round(h * 0.9), round(s, 3), body=SKIN, cloth=cl, sw=2.6, extra=A.headcloth(cl if i != 2 else "#ECE6D8") + (A.WHITE_BEARD if i != 1 else "")))
        o.append(label(x, h * 0.97, nm, "#8FD0E2", 9))
    return "".join(o)
