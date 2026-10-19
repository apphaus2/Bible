"""Isaiah 56–59 drawings (on top of isa.art15): the house of prayer for all peoples, the dumb watch-dogs asleep, the righteous
at rest, the oaks and the smooth stones of the valley (57:5–8 told in words only over the empty valley and a shut door), the
high and holy place and the contrite, the troubled sea, the trumpet, the fast that I have chosen (bread dealt to the hungry,
the light breaking forth as the morning, a watered garden, the repairer of the breach, the sabbath), the adders' eggs and the
spider's web (a plate), groping for the wall at noonday, truth fallen in the street, the armor of righteousness laid out as a
plate (no one wearing it), and the rushing stream."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art15 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
from genesis.art2 import birds
from exo.art8 import bp, dim, tag, title_bar, box

def house_prayer(p, w, h, seed):
    """Mine house shall be called a house of prayer for all peoples: the house of Jehovah on its mount, the foreigner and the
    eunuch among Israel in the court, people of every colour bringing their offerings, the altar smoking."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FC8E8", "#FFF0C8"), ground(w, h, h * 0.62, "#D8C8A0", dy=0), K1.temple_front(w * 0.5, h * 0.62, min(w * 0.3, h * 0.66), seed),
         horned_altar(w * 0.2, h * 0.8, min(0.6, h / 500), fire=True, seed=seed)]
    s = fit(b, max(h * 0.45, b - 180))
    for i in range(8):
        x = w * (0.3 + i * 0.09) + r.uniform(-6, 6); y = b - (i % 3) * h * 0.03
        o.append((man if i % 2 == 0 else woman)(p, x, y, s * (1 - (i % 3) * 0.08), r.choice(["#7A2A6A", "#E8B830", "#1F5FAD", "#B5121B", "#2E8A5A", "#F3EFE6", "#5A4A3A"]),
                                              flip=True, up=[(-22, -158), (-30, -190), (-24, -222)] if i % 3 == 0 else None))
    return "".join(o)

def dumb_dogs(w, h, seed):
    """His watchmen are blind; they are all dumb dogs, they cannot bark; dreaming, lying down, loving to slumber: watch-dogs asleep
    at the open gate of a sheepfold at night, the flock unguarded, eyes of wild beasts glinting in the dark beyond."""
    o = [bg(w, h, "#0B0B2A", "#2A2A4A"), mk.stars(30, w, h * 0.4, seed), ground(w, h, h * 0.6, "#2A2A30", dy=0)]
    for i in range(9):
        o.append(f'<rect x="{f(w * (0.04 + i * 0.05))}" y="{f(h * 0.62)}" width="{f(w * 0.048)}" height="{f(h * 0.08)}" fill="#5A5A60" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    s = min(0.5, h / 560)
    for i in range(4):
        o.append(E.sheep(w * (0.08 + i * 0.1), h * (0.86 + (i % 2) * 0.04), s * 0.8, wool="#9A9AA8"))
    for i, x in enumerate((0.54, 0.66)):
        cx, cy, k = w * x, h * 0.9, s * 1.4
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy - 14 * k)}" rx="{f(40 * k)}" ry="{f(14 * k)}" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
                 f'<ellipse cx="{f(cx + 40 * k)}" cy="{f(cy - 14 * k)}" rx="{f(14 * k)}" ry="{f(10 * k)}" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
                 f'<path d="M{f(cx + 36 * k)} {f(cy - 22 * k)} l 4 -8 l 4 8" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="1.2"></path>'
                 f'<path d="M{f(cx + 40 * k)} {f(cy - 14 * k)} l 6 0" stroke="#0D0D0F" stroke-width="1.6"></path>')
        o.append(label(cx + 30 * k, cy - 40 * k, "z z", "#8FD0E2", 10))
    for x in (0.8, 0.86, 0.94):
        o.append(f'<circle cx="{f(w * x)}" cy="{f(h * 0.7)}" r="2.6" fill="#FFD23F"></circle><circle cx="{f(w * x + 8)}" cy="{f(h * 0.7)}" r="2.6" fill="#FFD23F"></circle>')
    return "".join(o)

def at_rest(w, h, seed):
    """The righteous perisheth, and no man layeth it to heart; he entereth into peace; they rest in their beds: a quiet burial
    garden at evening, a sealed tomb under an olive-tree, a lamp left burning beside it."""
    from genesis.art4 import clay_lamp
    o = [bg(w, h, "#4A4A7A", "#E8B8A0"), f'<path d="M-10 {f(h * 0.4)} C {f(w * 0.4)} {f(h * 0.3)} {f(w * 0.7)} {f(h * 0.36)} {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = min(1.2, h / 260); cx = w * 0.6
    o.append(f'<path d="M{f(cx - 40 * s)} {f(h * 0.8)} L {f(cx - 40 * s)} {f(h * 0.56)} Q {f(cx)} {f(h * 0.46)} {f(cx + 40 * s)} {f(h * 0.56)} L {f(cx + 40 * s)} {f(h * 0.8)} Z" fill="#2A1E1A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<circle cx="{f(cx + 10 * s)}" cy="{f(h * 0.74)}" r="{f(36 * s)}" fill="#9A8A7A" stroke="#0D0D0F" stroke-width="2.4"></circle>')
    o.append(J.oak(w * 0.24, h * 0.9, min(0.8, h / 380), seed=seed))
    o.append(ground(w, h, h * 0.86, "#6A7A4A", dy=0) + clay_lamp(w * 0.8, h * 0.9, 0.6 * s))
    return "".join(o)

def oaks_valley(w, h, seed):
    """Ye that inflame yourselves among the oaks, under every green tree; among the smooth stones of the valley is thy portion:
    an empty valley at dusk, green trees, smooth stones in the dry stream-bed, the smoke of strange altars in the clefts of the
    rocks (57:5 told in words only: no one drawn)."""
    r = random.Random(seed)
    o = [bg(w, h, "#3A2A3A", "#B87A5A"), f'<path d="M-10 {f(h * 0.3)} L {f(w * 0.3)} {f(h * 0.6)} L {f(w * 0.7)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for x in (0.1, 0.24, 0.78, 0.9):
        o.append(J.oak(w * x, h * (0.56 if x < 0.5 else 0.54), min(0.5, h / 520), seed=int(x * 100)))
    for _ in range(14):
        x = r.uniform(w * 0.3, w * 0.7); y = r.uniform(h * 0.66, h * 0.96)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(r.uniform(10, 22))}" ry="{f(r.uniform(6, 10))}" fill="#B8B0A8" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    o.append(smoke(w * 0.16, h * 0.3, 5, seed, r0=8, color="#3A3036", op=0.5) + smoke(w * 0.84, h * 0.32, 5, seed + 1, r0=8, color="#3A3036", op=0.5))
    return "".join(o)

def shut_door(w, h, seed):
    """Upon a high and lofty mountain hast thou set thy bed; behind the doors and the posts hast thou set up thy memorial: a house
    on a high place with its door shut and a strange token on the post (57:7–8 told in words only)."""
    o = [bg(w, h, "#2A2040", "#8A5A6A"), f'<path d="M-10 {f(h + 10)} L {f(w * 0.5)} {f(h * 0.3)} L {f(w + 10)} {f(h + 10)} Z" fill="#5A4A4A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = min(1.0, h / 300); cx, b = w * 0.5, h * 0.42
    o.append(f'<rect x="{f(cx - 60 * s)}" y="{f(b - 70 * s)}" width="{f(120 * s)}" height="{f(80 * s)}" fill="#A8987A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(cx - 16 * s)}" y="{f(b - 40 * s)}" width="{f(32 * s)}" height="{f(50 * s)}" fill="#4A2E1A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<circle cx="{f(cx + 26 * s)}" cy="{f(b - 30 * s)}" r="{f(6 * s)}" fill="#C8A040" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    return "".join(o)

def high_holy(p, w, h, seed):
    """I dwell in the high and holy place, with him also that is of a contrite and humble spirit: light falling from on high,
    and in it a man kneeling with his head bowed (God is never drawn)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), rect(w, h, "#14123A"), V.rays(w * 0.5, -h * 0.1, 30, 10, max(w, h) * 1.2, color="#FFF4C2", op=0.25),
         f'<path d="M{f(w * 0.4)} -10 L {f(w * 0.6)} -10 L {f(w * 0.72)} {f(b)} L {f(w * 0.28)} {f(b)} Z" fill="#FFF4C2" opacity="0.18"></path>', ground(w, h, b, "#2A2448", dy=0)]
    o.append(E.kneel(w * 0.46, b, fit(b, max(h * 0.5, b - 170)), color="#5A4A6A", skin="#B98A6E"))
    return "".join(o)

def troubled_sea(w, h, seed):
    """But the wicked are like the troubled sea; for it cannot rest, and its waters cast up mire and dirt: a grey sea heaving under
    a low sky, its waves churned brown with mire along the shore."""
    r = random.Random(seed)
    o = [bg(w, h, "#3A3A4A", "#7A7A8A")]
    for k in range(5):
        y = h * (0.4 + k * 0.12)
        d = f"M-10 {f(y)} " + " ".join(f"Q {f(x + 30)} {f(y - 20 + r.uniform(-8, 8))} {f(x + 60)} {f(y)}" for x in range(-10, int(w) + 60, 60))
        o.append(f'<path d="{d} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{["#3A4A5A", "#34424E", "#4A4434", "#5A4A30", "#6A5430"][k]}" stroke="#C8C0A8" stroke-width="1.6"></path>')
    return "".join(o)

def trumpet_cry(p, w, h, seed):
    """Cry aloud, spare not, lift up thy voice like a trumpet, and declare unto my people their transgression: a trumpeter on the
    city wall blowing the ram's horn over the streets."""
    o = [mk.defs(p, *ALL), bg(w, h, "#8A6A8A", "#F3D8B0"), f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.6)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    for i in range(14):
        o.append(f'<rect x="{f(i * w / 13 - 10)}" y="{f(h * 0.46)}" width="{f(w / 26)}" height="{f(h * 0.05)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    s = fit(h * 0.5, h * 0.12)
    o.append(J.trumpeter(p, w * 0.4, h * 0.5, s) + J.blasts(w * 0.4 + 60 * s, h * 0.5 - 150 * s, s * 1.6))
    return "".join(o)

def false_fast(p, w, h, seed):
    """Is such the fast that I have chosen? to bow down his head as a rush, and to spread sackcloth and ashes under him?: a man in
    sackcloth sitting in ashes with his head bowed, while behind him in the street his servants are driven at their work."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8A7A6A", "#E8D0B0"), ground(w, h, h * 0.66, "#A8987A", dy=0)]
    s = fit(b, max(h * 0.5, b - 170))
    o.append(f'<ellipse cx="{f(w * 0.3)}" cy="{f(b)}" rx="{f(w * 0.12)}" ry="{f(h * 0.03)}" fill="#7A7A7A"></ellipse>' + E.kneel(w * 0.3, b, s, color="#6A5A40", skin="#8A5A3A"))
    for i in range(3):
        o.append(man(p, w * (0.62 + i * 0.1), h * 0.74, s * 0.6, "#8A6A4A", up=[(-22, -158), (-6, -176), (6, -190)]))
        o.append(f'<rect x="{f(w * (0.62 + i * 0.1) - 14 * s * 0.6)}" y="{f(h * 0.74 - 210 * s * 0.6)}" width="{f(28 * s * 0.6)}" height="{f(20 * s * 0.6)}" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    return "".join(o)

def true_fast(p, w, h, seed):
    """Is not this the fast that I have chosen: to deal thy bread to the hungry, to bring the poor that are cast out to thy house,
    when thou seest the naked, that thou cover him: a householder at his open door handing bread to a poor man and putting a
    cloak over another."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FB0D8", "#FFE8B8"), f'<rect x="{f(w * 0.04)}" y="{f(h * 0.2)}" width="{f(w * 0.3)}" height="{f(h * 0.7)}" fill="#D8C8A8" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.12)} {f(b)} L {f(w * 0.12)} {f(h * 0.5)} Q {f(w * 0.19)} {f(h * 0.42)} {f(w * 0.26)} {f(h * 0.5)} L {f(w * 0.26)} {f(b)} Z" fill="#FFC14D" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, h * 0.86, "#C8B080", dy=0)]
    s = fit(b, max(h * 0.4, b - 200))
    o.append(man(p, w * 0.38, b, s, "#2E6B8A", up=[(22, -158), (40, -150), (60, -146)]))
    o.append(f'<ellipse cx="{f(w * 0.38 + 66 * s)}" cy="{f(b - 148 * s)}" rx="{f(14 * s)}" ry="{f(8 * s)}" fill="#C8904A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    o.append(man(p, w * 0.54, b, s * 0.94, "#8A8478", flip=True, up=[(-22, -158), (-40, -150), (-56, -150)]))
    o.append(man(p, w * 0.72, b, s * 0.94, "#C8A060", flip=True) + E.kneel(w * 0.86, b, s * 0.8, color="#8A8478", skin="#8A5A3A", flip=True))
    return "".join(o)

def light_morning(w, h, seed):
    """Then shall thy light break forth as the morning; thou shalt be like a watered garden, and like a spring of water, whose
    waters fail not: dawn breaking over a green garden with a spring running through it."""
    r = random.Random(seed)
    o = [bg(w, h, "#6A7ABA", "#FFE0A8"), V.rays(w * 0.5, h * 0.5, 40, 20, max(w, h), color="#FFF4C2", op=0.4), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.5)}" r="{f(h * 0.08)}" fill="#FFF4C2"></circle>',
         hills(w, h, h * 0.54, seed, color="#5E8F3A", amp=10), ground(w, h, h * 0.62, "#7AAA4A", dy=0),
         f'<path d="M{f(w * 0.5)} {f(h * 0.62)} C {f(w * 0.4)} {f(h * 0.72)} {f(w * 0.6)} {f(h * 0.82)} {f(w * 0.46)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="{f(max(6, h * 0.03))}" fill="none"></path>']
    for _ in range(12):
        x = r.uniform(0, w); y = r.uniform(h * 0.66, h * 0.98); s = 0.4 + (y / h) * 0.8
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 26 * s)}" stroke="#5A3A22" stroke-width="{f(3 * s)}"></path><circle cx="{f(x)}" cy="{f(y - 34 * s)}" r="{f(14 * s)}" fill="{r.choice(["#3E8A3A", "#2E6A32", "#5E9F2A"])}" stroke="#0D0D0F" stroke-width="1.2"></circle>')
    return "".join(o)

def repairer(p, w, h, seed):
    """They that shall be of thee shall build the old waste places; thou shalt be called The repairer of the breach, The restorer
    of paths to dwell in: builders setting stones back into a broken city wall, a new path laid to the gate."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FC8E8", "#FFF0C8"), f'<rect x="-10" y="{f(h * 0.3)}" width="{f(w * 0.4)}" height="{f(h * 0.5)}" fill="#C8B898" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.62)}" y="{f(h * 0.3)}" width="{f(w * 0.4)}" height="{f(h * 0.5)}" fill="#C8B898" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.3)} {f(h * 0.8)} L {f(w * 0.3)} {f(h * 0.5)} L {f(w * 0.36)} {f(h * 0.56)} L {f(w * 0.44)} {f(h * 0.6)} L {f(w * 0.52)} {f(h * 0.56)} L {f(w * 0.58)} {f(h * 0.5)} L {f(w * 0.62)} {f(h * 0.5)} L {f(w * 0.62)} {f(h * 0.8)} Z" fill="#E0D4B4" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, h * 0.8, "#C8B080", dy=0)]
    for k in range(3):
        for j in range(5):
            o.append(f'<rect x="{f(w * 0.3 + j * w * 0.064)}" y="{f(h * (0.74 - k * 0.06))}" width="{f(w * 0.06)}" height="{f(h * 0.06)}" fill="#D8C8A8" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    s = fit(b, max(h * 0.5, b - 170))
    o.append(man(p, w * 0.22, b, s, "#8A6A4A", up=[(-22, -158), (-6, -176), (6, -190)]) + f'<rect x="{f(w * 0.22 - 14 * s)}" y="{f(b - 212 * s)}" width="{f(28 * s)}" height="{f(20 * s)}" fill="#D8C8A8" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    o.append(man(p, w * 0.72, b, s, "#5A6A4A", flip=True, up=[(-22, -158), (-40, -150), (-60, -150)]))
    return "".join(o)

def sabbath_rest(p, w, h, seed):
    """If thou call the sabbath a delight, and the holy of Jehovah honorable: then shalt thou delight thyself in Jehovah; and I will
    make thee to ride upon the high places of the earth: a field at rest on the sabbath, the plow left, a family walking up the
    hill to the high place at evening."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#5A6ABA", "#FFD8A0"), sun(w * 0.84, h * 0.3, min(22, h * 0.06), color="#FFF4C2", op=0.4),
         f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.6)} {f(h * 0.3)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8AA05A" stroke="#0D0D0F" stroke-width="2"></path>']
    s = fit(b, max(h * 0.5, b - 170))
    o.append(f'<path d="M{f(w * 0.08)} {f(b)} L {f(w * 0.2)} {f(b - 40 * s)} M{f(w * 0.1)} {f(b - 6)} L {f(w * 0.06)} {f(b + 4)}" stroke="#5A3A22" stroke-width="{f(5 * s)}"></path>')
    for i in range(3):
        t = i / 3; o.append((man if i != 1 else woman)(p, w * (0.36 + t * 0.2), b - t * h * 0.3, s * (1 - t * 0.5), ["#3A4A7A", "#7A3A5A", "#5A6A3A"][i]))
    return "".join(o)

def eggs_web(w, h):
    """They hatch adders' eggs, and weave the spider's web; their webs shall not become garments (a plate: the eggs, one broken
    with a viper breaking out, and the web)."""
    o = [bp(w, h), title_bar(w, "ADDERS' EGGS · THE SPIDER'S WEB")]
    s = min(1.2, h / 220); cy = h * 0.6
    for i in range(4):
        x = w * (0.1 + i * 0.08)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(cy)}" rx="{f(14 * s)}" ry="{f(18 * s)}" fill="#E8E0C8" stroke="#8FD0E2" stroke-width="1.6"></ellipse>')
    o.append(f'<path d="M{f(w * 0.42 - 14 * s)} {f(cy)} l {f(6 * s)} {f(-6 * s)} l {f(6 * s)} {f(6 * s)} l {f(6 * s)} {f(-6 * s)} l {f(6 * s)} {f(6 * s)}" stroke="#8FD0E2" stroke-width="1.6" fill="none"></path>'
             f'<path d="M{f(w * 0.42 - 14 * s)} {f(cy)} C {f(w * 0.42 - 14 * s)} {f(cy + 24 * s)} {f(w * 0.42 + 14 * s)} {f(cy + 24 * s)} {f(w * 0.42 + 14 * s)} {f(cy)}" fill="#E8E0C8" stroke="#8FD0E2" stroke-width="1.6"></path>')
    o.append(SN.snake([(w * 0.42, cy - 4), (w * 0.44, cy - 30 * s), (w * 0.48, cy - 20 * s), (w * 0.5, cy - 40 * s)], 4 * s, "ew1", head_scale=0.4))
    o.append(label(w * 0.26, cy + 50 * s, "ADDERS' EGGS", CYAN, 9))
    wx, wy, R = w * 0.76, h * 0.56, min(w * 0.18, h * 0.32)
    for k in range(8):
        a = k * math.pi / 4
        o.append(f'<path d="M{f(wx)} {f(wy)} L {f(wx + math.cos(a) * R)} {f(wy + math.sin(a) * R)}" stroke="#E8E8F0" stroke-width="1.2"></path>')
    for j in range(1, 5):
        rr = R * j / 4
        o.append(f'<path d="M{" L ".join(f"{f(wx + math.cos(k * math.pi / 4) * rr)} {f(wy + math.sin(k * math.pi / 4) * rr)}" for k in range(9))}" stroke="#E8E8F0" stroke-width="1" fill="none"></path>')
    o.append(label(wx, wy - R - 10, "THE SPIDER'S WEB · NOT A GARMENT", CYAN, 9))
    return "".join(o)

def grope_wall(p, w, h, seed):
    """We grope for the wall like the blind; we stumble at noonday as in the twilight: people feeling their way along a city wall
    in a strange dusk at noon, the sun dim and small."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#4A4A5A", "#8A8070"), f'<circle cx="{f(w * 0.8)}" cy="{f(h * 0.16)}" r="{f(min(18, h * 0.05))}" fill="#C8C0A0" opacity="0.6"></circle>',
         f'<rect x="-10" y="{f(h * 0.2)}" width="{f(w * 0.7)}" height="{f(h * 0.74)}" fill="#8A8070" stroke="#0D0D0F" stroke-width="2"></rect>', ground(w, h, b, "#5A5448", dy=0)]
    s = fit(b, max(h * 0.45, b - 180))
    for i in range(3):
        o.append(man(p, w * (0.74 + i * 0.09), b, s, ["#5A4A6A", "#6A5A3A", "#4A5A5A"][i], flip=True, up=[(-22, -158), (-44, -150), (-64, -148)]))
    return "".join(o)

def truth_fallen(w, h, seed):
    """Truth is fallen in the street, and uprightness cannot enter: a set of scales and a fallen measuring-line lying in the dust of
    an empty street, the gate beyond shut."""
    o = [bg(w, h, "#6A5A6A", "#D8B8A0"), ground(w, h, h * 0.62, "#A8987A", dy=0)]
    o.append(S4.gatehouse(w * 0.76, h * 0.62, min(w * 0.36, h * 0.8), h * 0.44))
    s = min(1.0, h / 280)
    o.append(f'<g transform="rotate(-70 {f(w * 0.3)} {f(h * 0.9)})">{S4.balance(w * 0.3, h * 0.9, 0.5 * s)}</g>'
             f'<path d="M{f(w * 0.4)} {f(h * 0.92)} C {f(w * 0.46)} {f(h * 0.88)} {f(w * 0.52)} {f(h * 0.96)} {f(w * 0.6)} {f(h * 0.9)}" stroke="#E8D8A8" stroke-width="2" fill="none"></path>')
    return "".join(o)

def armor(w, h):
    """He put on righteousness as a breastplate, and a helmet of salvation upon his head; and he put on garments of vengeance for
    clothing, and was clad with zeal as a mantle (a plate of the armor, set out on its own: no one wearing it)."""
    o = [bp(w, h), title_bar(w, "RIGHTEOUSNESS · SALVATION · VENGEANCE · ZEAL")]
    s = min(1.0, h / 220); cw = w / 4; b = h * 0.74
    items = [("A BREASTPLATE · RIGHTEOUSNESS", "breast"), ("A HELMET · SALVATION", "helm"), ("GARMENTS · VENGEANCE", "robe"), ("A MANTLE · ZEAL", "mantle")]
    for i, (nm, k) in enumerate(items):
        cx = cw * (i + 0.5)
        if k == "breast":
            o.append(f'<path d="M{f(cx - 34 * s)} {f(b - 90 * s)} L {f(cx + 34 * s)} {f(b - 90 * s)} L {f(cx + 30 * s)} {f(b - 10 * s)} L {f(cx)} {f(b)} L {f(cx - 30 * s)} {f(b - 10 * s)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
                     + "".join(f'<path d="M{f(cx - 28 * s)} {f(b - (70 - j * 16) * s)} L {f(cx + 28 * s)} {f(b - (70 - j * 16) * s)}" stroke="#B88A20" stroke-width="2"></path>' for j in range(4)))
        elif k == "helm":
            o.append(f'<path d="M{f(cx - 30 * s)} {f(b - 20 * s)} C {f(cx - 34 * s)} {f(b - 90 * s)} {f(cx + 34 * s)} {f(b - 90 * s)} {f(cx + 30 * s)} {f(b - 20 * s)} Z" fill="#C8D0D8" stroke="#0D0D0F" stroke-width="2"></path>'
                     f'<path d="M{f(cx)} {f(b - 86 * s)} L {f(cx)} {f(b - 110 * s)}" stroke="#FFD23F" stroke-width="{f(6 * s)}"></path>')
        elif k == "robe":
            o.append(f'<path d="M{f(cx - 24 * s)} {f(b - 100 * s)} L {f(cx + 24 * s)} {f(b - 100 * s)} L {f(cx + 40 * s)} {f(b)} L {f(cx - 40 * s)} {f(b)} Z" fill="#8A1A2A" stroke="#0D0D0F" stroke-width="2"></path>')
        else:
            o.append(f'<path d="M{f(cx - 20 * s)} {f(b - 100 * s)} C {f(cx - 50 * s)} {f(b - 60 * s)} {f(cx - 46 * s)} {f(b - 20 * s)} {f(cx - 40 * s)} {f(b)} L {f(cx + 40 * s)} {f(b)} C {f(cx + 46 * s)} {f(b - 20 * s)} {f(cx + 50 * s)} {f(b - 60 * s)} {f(cx + 20 * s)} {f(b - 100 * s)} Z" fill="#FF6A2A" stroke="#0D0D0F" stroke-width="2"></path>')
        o.append(label(cx, b + 22 * s, nm, CYAN, 8))
    return "".join(o)

def rushing_stream(w, h, seed):
    """He will come as a rushing stream, which the breath of Jehovah driveth; and a Redeemer will come to Zion: a flood-stream
    pouring down a mountain gorge toward Zion at sunrise, the wind driving it."""
    r = random.Random(seed)
    o = [bg(w, h, "#5A7ABA", "#FFE0A8"), sun(w * 0.86, h * 0.2, min(24, h * 0.06), color="#FFF4C2", op=0.4),
         f'<path d="M-10 {f(h * 0.6)} L {f(w * 0.2)} {f(h * 0.2)} L {f(w * 0.36)} {f(h * 0.5)} L {f(w * 0.5)} {f(h * 0.4)} L {f(w * 0.6)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A6A5A" stroke="#0D0D0F" stroke-width="2"></path>',
         J.city_hill(w * 0.84, h * 0.7, w * 0.16, h * 0.2, seed), ground(w, h, h * 0.72, "#9AA06A", dy=0)]
    pts = [(w * 0.22, h * 0.24), (w * 0.3, h * 0.46), (w * 0.4, h * 0.6), (w * 0.56, h * 0.8), (w * 0.7, h + 10)]
    o.append(f'<path d="M{" L ".join(f"{f(x)} {f(y)}" for x, y in pts)}" stroke="#2C9DB8" stroke-width="{f(max(10, h * 0.06))}" fill="none" stroke-linejoin="round"></path>')
    for x, y in pts[:-1]:
        o.append(f'<path d="M{f(x - 10)} {f(y)} q 10 -8 20 0" stroke="#E8F6FA" stroke-width="2" fill="none"></path>')
    for k in range(5):
        y = h * (0.1 + k * 0.08)
        o.append(f'<path d="M{f(w * 0.02)} {f(y)} C {f(w * 0.2)} {f(y - 10)} {f(w * 0.4)} {f(y + 10)} {f(w * 0.6)} {f(y)}" stroke="#FFF4C2" stroke-width="2" fill="none" opacity="0.6"></path>')
    return "".join(o)
