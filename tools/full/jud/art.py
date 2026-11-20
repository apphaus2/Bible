"""Drawings for the Jude volume. Jude starts from all of 2 Peter's drawings (`from pe2.art import *`, which carries 1 Peter's,
James', Galatians', Acts', Mark's and Matthew's drawings, the epistle kit and the writers' figures) and adds its own.

The people at a distance: Jude only ever jas.art.jude_fig; Michael the archangel jas.art.angel_r (white light, a gold rim,
no face); Enoch an old man in a white robe and grey beard; Balaam in his purple headcloth (2 Peter's). The devil is never
drawn; God is never drawn. Every function takes (p, w, h, seed, ...) or (w, h, ...)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from pe2.art import *
from jas.art import art, plate_label, _street, _road
from gal.art import night_window
import numbers1 as N1

JSCRIBE2 = dict(cloth="#4A5A4A", hair="#2A1A10")                      # a young scribe, bareheaded

def _night_win(x, y, ww, hh, night, seed): return night_window(x, y, ww, hh, seed)

def study_jude(p, w, h, seed, stage="dictate", fig_h=None):
    """Jude writing by lamplight in a house of Judæa (epistle.study), standing, his hand out, a young scribe on his mat, the
    hills under the stars through the window."""
    return study(p, w, h, seed, stage=stage, scribe=JSCRIBE2, writer=jude_fig, window=_night_win, fig_h=fig_h)

def through_sea(p, w, h, seed):
    """The Lord, having saved a people out of the land of Egypt: the sea divided, its waters a wall on the right hand and on
    the left, the children of Israel walking through on dry ground at night, the pillar of fire behind them."""
    r = random.Random(seed)
    b = h * 0.94
    o = [D_(p), sky(w, h, "#0B0B2A", "#2A2050"), mk.stars(30, w, h * 0.3, seed)]
    vx, vy = w * 0.5, h * 0.36                                          # the vanishing point: the far shore
    o.append(f'<path d="M-10 {f(h + 10)} L {f(vx - w * 0.06)} {f(vy)} L {f(vx + w * 0.06)} {f(vy)} L {f(w + 10)} {f(h + 10)} Z" fill="#C8A878" stroke="{INK}" stroke-width="2"></path>')
    for side in (-1, 1):                                                # the two walls of water
        xo = vx + side * w * 0.06
        o.append(f'<path d="M{f(xo)} {f(vy)} L {f(xo + side * w * 0.04)} {f(h * 0.08)} L {f(w * 0.5 + side * w * 0.62)} {f(-10)} L {f(w * 0.5 + side * w * 0.62)} {f(h + 10)} L {f(w * 0.5 + side * w * 0.36)} {f(h + 10)} Z" '
                 f'fill="#1F6F9A" stroke="{INK}" stroke-width="2.4"></path>')
        for k in range(8):
            t = k / 8
            x0 = xo + side * (w * 0.04 + w * 0.3 * t); y0 = h * 0.1 + (h * 0.8) * t
            o.append(f'<path d="M{f(x0)} {f(y0)} C {f(x0 + side * 20)} {f(y0 - 6)} {f(x0 + side * 40)} {f(y0 + 6)} {f(x0 + side * 60)} {f(y0)}" stroke="#8FD0E2" stroke-width="2" fill="none" opacity="0.7"></path>')
        o.append(f'<path d="M{f(xo)} {f(vy)} L {f(xo + side * w * 0.04)} {f(h * 0.08)}" stroke="#E8F6FA" stroke-width="3"></path>')
    s0 = fit(b, max(h * 0.3, b - 170))
    for i in range(7):                                                  # the people walking away into the sea, smaller as they go
        t = i / 7
        x = vx + (w * 0.08) * math.sin(i * 1.7) * (1 - t); y = b - (b - vy) * t * 0.92
        ss = s0 * (1 - t * 0.85)
        o.append((woman_r if i % 3 == 1 else man_r)(p, x, y, ss, i, flip=i % 2 == 0, pose="walk"))
    fx, fy = w * 0.12, b                                                # the pillar of fire behind them, at the left
    o.append(halo(fx, fy - h * 0.4, h * 0.4, "#FF8A3D", 0.5)
             + f'<path d="M{f(fx - 24)} {f(fy)} C {f(fx - 30)} {f(fy - h * 0.4)} {f(fx - 14)} {f(fy - h * 0.7)} {f(fx)} {f(-10)} C {f(fx + 16)} {f(fy - h * 0.7)} {f(fx + 30)} {f(fy - h * 0.4)} {f(fx + 24)} {f(fy)} Z" fill="#FF8A3D" opacity="0.85"></path>'
             + f'<path d="M{f(fx - 10)} {f(fy)} C {f(fx - 14)} {f(fy - h * 0.4)} {f(fx - 6)} {f(fy - h * 0.7)} {f(fx)} {f(-10)} C {f(fx + 6)} {f(fy - h * 0.7)} {f(fx + 14)} {f(fy - h * 0.4)} {f(fx + 10)} {f(fy)} Z" fill="#FFE680"></path>')
    o.append(plate_label(w * 0.5, h * 0.06, "SAVED OUT OF THE LAND OF EGYPT", "#E8F6FA", 10, halo_="#0B0B2A"))
    return "".join(o)

def sodom_smoke(w, h, seed):
    """Sodom and Gomorrah, and the cities about them, … set forth as an example: the plain empty and black where the cities
    stood, the smoke going up as the smoke of a furnace into a red sky, the dark mountains beyond. No one in it."""
    r = random.Random(seed)
    o = [sky(w, h, "#1A0A0A", "#8A2A1A"), halo(w * 0.5, h * 0.62, h * 0.6, "#FF6A2A", 0.45), hills(w, h, h * 0.5, seed, color="#2A1414", amp=18, step=100),
         ground(w, h, h * 0.62, "#1E1414", dy=0)]
    for i in range(10):
        x = w * r.uniform(0.05, 0.95); y = h * r.uniform(0.66, 0.92)
        o.append(f'<path d="M{f(x - 34)} {f(y)} C {f(x - 20)} {f(y - 16)} {f(x + 12)} {f(y - 18)} {f(x + 34)} {f(y)} Z" fill="#2A2020" stroke="{INK}" stroke-width="1.4"></path>')
        if i % 3 == 0: o.append(f'<circle cx="{f(x)}" cy="{f(y - 6)}" r="3" fill="#FF8A3D" opacity="0.8"></circle>')
    for x in (0.26, 0.5, 0.74):
        o.append(smoke(w * x, h * 0.54, 8, seed + int(x * 10), color="#3A2A2A", op=0.7, k=max(0.8, h / 220)))
    o.append(plate_label(w * 0.5, h * 0.08, "SODOM AND GOMORRAH · AN EXAMPLE", "#FFE0C0", 10, halo_="#1A0A0A"))
    return "".join(o)

def michael_nebo(p, w, h, seed):
    """Michael the archangel, when contending with the devil he disputed about the body of Moses: mount Nebo in the land of
    Moab at evening, the top of Pisgah over the valley, the valley below empty and no grave to be seen; on the slope Michael,
    a figure of white light with a gold rim and no face, his hand lifted — and no one before him (the devil is never drawn)."""
    b = h * 0.92
    o = [D_(p), sky(w, h, "#2A1A4A", "#E8A06A"), halo(w * 0.86, h * 0.56, h * 0.4, "#FFE0A0", 0.5),
         f'<path d="M{f(w * 0.5)} {f(h * 0.62)} C {f(w * 0.7)} {f(h * 0.58)} {f(w * 0.9)} {f(h * 0.62)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.5)} {f(h + 10)} Z" fill="#6A5A4A" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.5)} L {f(w * 0.14)} {f(h * 0.2)} L {f(w * 0.26)} {f(h * 0.24)} L {f(w * 0.46)} {f(h * 0.56)} L {f(w * 0.64)} {f(h + 10)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.2)} {f(h * 0.3)} L {f(w * 0.34)} {f(h * 0.5)} M{f(w * 0.1)} {f(h * 0.42)} L {f(w * 0.3)} {f(h * 0.72)}" stroke="#6A4A2A" stroke-width="2" fill="none"></path>']
    o.append(f'<path d="M{f(w * 0.52)} {f(h * 0.8)} C {f(w * 0.66)} {f(h * 0.76)} {f(w * 0.8)} {f(h * 0.82)} {f(w * 0.96)} {f(h * 0.78)}" stroke="#7A6A54" stroke-width="3" fill="none"></path>')
    s = fit(b, max(h * 0.3, b - 180))
    o.append(angel_r(p, w * 0.34, b - h * 0.12, s, flip=True, up=[(-22, -158), (-34, -196), (-40, -232)]))
    o.append(plate_label(w * 0.2, h * 0.12, "MOUNT NEBO", "#3A1A2A", 10, halo_="#F0C8A0") + plate_label(w * 0.76, h * 0.7, "THE VALLEY IN THE LAND OF MOAB", "#E8E2D6", 9, halo_="#4A3A2A"))
    return "".join(o)

def three_ways(p, w, h, seed):
    """Woe unto them! for they went in the way of Cain, and ran riotously in the error of Balaam for hire, and perished in the
    gainsaying of Korah: a plate of three — two altars, the smoke of one going up straight and of the other beaten down to the
    ground (Cain); Balaam in his purple headcloth on the grey ass, the bag of hire at his side; the earth rent open and the
    censers lying scattered at its edge, no one there (Korah)."""
    o = [D_(p), plate_bg(w, h, "JUDE 11 · THE WAY OF CAIN · THE ERROR OF BALAAM · THE GAINSAYING OF KORAH")]
    cw = w / 3; base = h * 0.8; k = min(cw / 234, h / 300)
    for i, name in enumerate(("THE WAY OF CAIN", "THE ERROR OF BALAAM", "THE GAINSAYING OF KORAH")):
        x0 = cw * i; cx = x0 + cw / 2
        o.append(f'<rect x="{f(x0 + 8)}" y="{f(h * 0.14)}" width="{f(cw - 16)}" height="{f(h * 0.74)}" fill="#0F2238" stroke="{CY}" stroke-width="1.2"></rect>'
                 f'<path d="M{f(x0 + 8)} {f(base)} L {f(x0 + cw - 8)} {f(base)}" stroke="#6A5A3A" stroke-width="3"></path>')
        if i == 0:
            for j, (dx, up) in enumerate(((-46, True), (46, False))):
                o.append(stone_altar(cx + dx * k, base, 0.5 * k, wood=True))
                if up: o.append(smoke(cx + dx * k, base - 70 * k, 4, seed + j, color="#C8C8D0", op=0.7, k=0.6 * k))
                else: o.append(f'<path d="M{f(cx + dx * k)} {f(base - 44 * k)} C {f(cx + (dx + 20) * k)} {f(base - 56 * k)} {f(cx + (dx + 40) * k)} {f(base - 20 * k)} {f(cx + (dx + 70) * k)} {f(base - 10 * k)}" stroke="#6A6A70" stroke-width="{f(10 * k)}" fill="none" opacity="0.7" stroke-linecap="round"></path>')
        elif i == 1:
            o.append(N1.ass(cx - 10 * k, base, 0.62 * k, flip=False, color="#8A8478"))
            bag = '<path d="M22 -96 C 34 -100 38 -84 30 -78 C 22 -74 16 -86 22 -96 Z" fill="#C8A040" stroke="#0D0D0F" stroke-width="2"></path>'
            o.append(robed(p, cx - 14 * k, base - 0.62 * k * 33, 0.62 * k * 0.9, "#4A2A5A", head="#5A1A6A", cord="#E8B830", beard="#3A2A1A", flip=True, pose="sit", seat=None, extra=bag))
        else:
            o.append(f'<path d="M{f(cx - 70 * k)} {f(base)} L {f(cx - 40 * k)} {f(base - 6 * k)} L {f(cx - 20 * k)} {f(base + 4 * k)} L {f(cx + 10 * k)} {f(base - 8 * k)} L {f(cx + 40 * k)} {f(base + 2 * k)} L {f(cx + 70 * k)} {f(base)} '
                     f'L {f(cx + 30 * k)} {f(base + 0.06 * h)} L {f(cx - 30 * k)} {f(base + 0.06 * h)} Z" fill="#05050E" stroke="#FF6A4A" stroke-width="1.6"></path>')
            for j, dx in enumerate((-60, 52, 72)):
                o.append(f'<g transform="rotate({(-1) ** j * 40} {f(cx + dx * k)} {f(base - 8 * k)})"><path d="M{f(cx + dx * k - 10 * k)} {f(base - 16 * k)} L {f(cx + dx * k + 10 * k)} {f(base - 16 * k)} L {f(cx + dx * k + 6 * k)} {f(base - 4 * k)} L {f(cx + dx * k - 6 * k)} {f(base - 4 * k)} Z" fill="#C8963E" stroke="{INK}" stroke-width="1.4"></path>'
                         f'<path d="M{f(cx + dx * k)} {f(base - 16 * k)} l 0 -14" stroke="#8A6A3A" stroke-width="2"></path></g>')
        o.append(label(cx, h * 0.2, name, CY, 8))
    return "".join(o)

def five_plate(w, h, seed):
    """Hidden rocks in your love-feasts, clouds without water carried along by winds, autumn trees without fruit twice dead
    plucked up by the roots, wild waves of the sea foaming out their own shame, wandering stars: a plate of five cells."""
    r = random.Random(seed)
    o = [plate_bg(w, h, "JUDE 12–13")]
    cw = w / 5; base = h * 0.8; k = min(cw / 140, h / 300)
    names = ("HIDDEN ROCKS", "CLOUDS WITHOUT WATER", "TREES TWICE DEAD", "WILD WAVES", "WANDERING STARS")
    for i, name in enumerate(names):
        x0 = cw * i; cx = x0 + cw / 2
        o.append(f'<rect x="{f(x0 + 6)}" y="{f(h * 0.14)}" width="{f(cw - 12)}" height="{f(h * 0.74)}" fill="#0F2238" stroke="{CY}" stroke-width="1.2"></rect>')
        if i == 0:
            o.append(f'<path d="M{f(x0 + 6)} {f(base - 30 * k)} C {f(cx - 20 * k)} {f(base - 36 * k)} {f(cx + 20 * k)} {f(base - 26 * k)} {f(x0 + cw - 6)} {f(base - 32 * k)} L {f(x0 + cw - 6)} {f(h * 0.88)} L {f(x0 + 6)} {f(h * 0.88)} Z" fill="#14304A"></path>'
                     f'<path d="M{f(cx - 34 * k)} {f(base + 6 * k)} L {f(cx - 20 * k)} {f(base - 26 * k)} L {f(cx + 4 * k)} {f(base - 40 * k)} L {f(cx + 30 * k)} {f(base - 22 * k)} L {f(cx + 40 * k)} {f(base + 6 * k)} Z" fill="#4A4A54" stroke="{INK}" stroke-width="1.6"></path>'
                     f'<path d="M{f(x0 + 6)} {f(base - 30 * k)} C {f(cx - 20 * k)} {f(base - 36 * k)} {f(cx + 20 * k)} {f(base - 26 * k)} {f(x0 + cw - 6)} {f(base - 32 * k)}" stroke="#8FD0E2" stroke-width="2" fill="none"></path>')
        elif i == 1:
            o.append(clouds(cw - 20, h * 0.32, seed, n=3, color="#8A8A9A", op=0.95, ry=0.08, h=h).replace('<ellipse cx="', f'<ellipse transform="translate({f(x0 + 10)} 0)" cx="')
                     + "".join(f'<path d="M{f(cx + (j - 2) * 14 * k)} {f(h * 0.5)} l {f(26 * k)} -6" stroke="{CY}" stroke-width="1.6" opacity="0.7"></path>' for j in range(4))
                     + f'<path d="M{f(x0 + 6)} {f(base)} L {f(x0 + cw - 6)} {f(base)}" stroke="#8A6A3A" stroke-width="3"></path>'
                     + "".join(f'<path d="M{f(cx + (j - 2) * 12 * k)} {f(base)} l {f(6 * k)} -4 l {f(6 * k)} 4" stroke="#6A4A2A" stroke-width="1.4" fill="none"></path>' for j in range(5)))
        elif i == 2:
            o.append(f'<path d="M{f(x0 + 6)} {f(base)} L {f(x0 + cw - 6)} {f(base)}" stroke="#8A6A3A" stroke-width="3"></path>'
                     f'<g transform="rotate(-70 {f(cx)} {f(base)})"><path d="M{f(cx)} {f(base)} L {f(cx)} {f(base - 70 * k)} M{f(cx)} {f(base - 40 * k)} L {f(cx - 18 * k)} {f(base - 60 * k)} M{f(cx)} {f(base - 54 * k)} L {f(cx + 16 * k)} {f(base - 76 * k)} M{f(cx)} {f(base - 70 * k)} L {f(cx - 8 * k)} {f(base - 88 * k)}" stroke="#5A4A3A" stroke-width="{f(4 * k)}" fill="none" stroke-linecap="round"></path></g>'
                     + "".join(f'<path d="M{f(cx)} {f(base)} l {f(dx * k)} {f(dy * k)}" stroke="#6A4A2A" stroke-width="2"></path>' for dx, dy in ((-12, 10), (-4, 14), (6, 12), (12, 6))))
        elif i == 3:
            for j in range(3):
                y = base - j * 26 * k
                o.append(f'<path d="M{f(x0 + 6)} {f(y)} C {f(cx - 24 * k)} {f(y - 30 * k)} {f(cx - 8 * k)} {f(y - 34 * k)} {f(cx)} {f(y - 18 * k)} C {f(cx + 12 * k)} {f(y - 34 * k)} {f(cx + 30 * k)} {f(y - 28 * k)} {f(x0 + cw - 6)} {f(y - 4 * k)} L {f(x0 + cw - 6)} {f(h * 0.88)} L {f(x0 + 6)} {f(h * 0.88)} Z" fill="{["#0F4C68", "#1F6F9A", "#1F5A80"][j]}" stroke="{INK}" stroke-width="1.4"></path>'
                         + "".join(f'<circle cx="{f(cx + r.uniform(-20, 20) * k)}" cy="{f(y - r.uniform(20, 36) * k)}" r="{f(r.uniform(1.4, 3) * k)}" fill="#E8F6FA"></circle>' for _ in range(4)))
        else:
            for j in range(5):
                sx_, sy_ = cx + r.uniform(-40, 40) * k, h * r.uniform(0.3, 0.7)
                o.append(f'<path d="M{f(sx_)} {f(sy_)} C {f(sx_ - 20 * k)} {f(sy_ + 10 * k)} {f(sx_ - 34 * k)} {f(sy_ + 30 * k)} {f(sx_ - 30 * k)} {f(sy_ + 50 * k)}" stroke="#E8E2D6" stroke-width="1" stroke-dasharray="2 3" fill="none" opacity="0.7"></path>'
                         f'<circle cx="{f(sx_)}" cy="{f(sy_)}" r="{f(2.6 * k)}" fill="#FFF4C2"></circle>')
        o.append(label(cx, h * 0.84, name if len(name) < 14 else name.split(" W")[0], CY, 7) + (label(cx, h * 0.84 + 10, "WITHOUT WATER", CY, 7) if i == 1 else ""))
    return "".join(o)

def enoch_lights(p, w, h, seed):
    """Enoch, the seventh from Adam, prophesied, saying, Behold, the Lord came with ten thousands of his holy ones: an old man
    in white on a hilltop at night, his arm lifted to the sky, and the sky full of lights beyond counting, coming (the holy ones
    are points of light; nothing else is drawn)."""
    r = random.Random(seed)
    b = h * 0.92
    o = [D_(p), sky(w, h, "#05051A", "#2A2A5A"), halo(w * 0.7, h * 0.2, h * 0.6, "#FFF4C2", 0.35)]
    for i in range(160):
        x = w * r.uniform(0.25, 1.0); y = h * r.uniform(0.02, 0.6)
        d = math.hypot(x - w * 0.7, y - h * 0.2) / w
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(max(0.8, 3.2 - d * 5))}" fill="#FFF8E0" opacity="{max(0.3, 1 - d):.2f}"></circle>')
    o.append(hills(w, h, h * 0.7, seed, color="#1A1A30", amp=10, step=90)
             + f'<path d="M-10 {f(h + 10)} L -10 {f(b - h * 0.06)} C {f(w * 0.2)} {f(b - h * 0.14)} {f(w * 0.4)} {f(b - h * 0.1)} {f(w * 0.56)} {f(h + 10)} Z" fill="#3A3448" stroke="{INK}" stroke-width="2"></path>')
    s = fit(b, max(h * 0.3, b - 190))
    o.append(robed(p, w * 0.2, b - h * 0.08, s, "#E8E2D6", hair="#C8C2B6", beard="#D8D2C6", mantle="#9A9AB0", belt="#5A5A7A", flip=True, up=[(-22, -158), (-46, -188), (-60, -212)]))
    o.append(plate_label(w * 0.2, h * 0.1, "ENOCH, THE SEVENTH FROM ADAM", "#FFF4C2", 9, halo_="#05051A"))
    return "".join(o)

def brand_fire(w, h, seed):
    """And some save, snatching them out of the fire: a fire burning on the hearth at night, and a hand reaching in and drawing
    out a brand, its end still alight."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#140A08"></rect>', halo(w * 0.42, h * 0.74, h * 0.7, "#FF6A2A", 0.55)]
    k = h / 300
    b = h * 0.9
    o.append(f'<path d="M{f(w * 0.2)} {f(b)} C {f(w * 0.24)} {f(b - 20 * k)} {f(w * 0.6)} {f(b - 20 * k)} {f(w * 0.64)} {f(b)} Z" fill="#3A2A22" stroke="{INK}" stroke-width="2"></path>')
    for i in range(7):
        o.append(flame(w * (0.26 + i * 0.05), b - 6 * k, k * r.uniform(0.8, 1.3), seed + i))
    bx0, by0, bx1, by1 = w * 0.44, b - 30 * k, w * 0.74, h * 0.34          # the brand drawn out, its end aflame
    o.append(f'<path d="M{f(bx0)} {f(by0)} L {f(bx1)} {f(by1)}" stroke="#3A2214" stroke-width="{f(12 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(bx0)} {f(by0)} L {f(bx0 + (bx1 - bx0) * 0.2)} {f(by0 + (by1 - by0) * 0.2)}" stroke="#FF6A2A" stroke-width="{f(12 * k)}" stroke-linecap="round"></path>'
             + flame(bx0, by0, k * 0.7, seed + 9))
    hx, hy = bx1 + 6 * k, by1 - 4 * k                                     # the hand and the sleeve
    o.append(f'<path d="M{f(hx)} {f(hy)} L {f(w + 10)} {f(hy - 60 * k)} L {f(w + 10)} {f(hy - 10 * k)} L {f(hx + 10 * k)} {f(hy + 24 * k)} Z" fill="#4A5A6A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(hx - 18 * k)} {f(hy + 10 * k)} C {f(hx - 24 * k)} {f(hy - 6 * k)} {f(hx - 10 * k)} {f(hy - 18 * k)} {f(hx + 6 * k)} {f(hy - 14 * k)} L {f(hx + 16 * k)} {f(hy + 12 * k)} C {f(hx + 4 * k)} {f(hy + 22 * k)} {f(hx - 10 * k)} {f(hy + 22 * k)} {f(hx - 18 * k)} {f(hy + 10 * k)} Z" fill="{SKIN}" stroke="{INK}" stroke-width="2"></path>')
    o.append(plate_label(w * 0.36, h * 0.1, "SNATCHING THEM OUT OF THE FIRE", "#FFE6A0", 10, halo_="#140A08"))
    return "".join(o)
