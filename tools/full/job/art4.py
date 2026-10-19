"""Drawings for Job 11–14 (Zophar's first speech and Job's answer)."""
from job.art3 import *
from job.art3 import f, K2, K3, sea, label
from genesis.art3 import route

def measures(w, h, seed):
    """High as heaven, deeper than Sheol, longer than the earth and broader than the sea: a technical section of the world —
    the sky above, the land and the sea, the deep below — with dimension lines that run off every edge."""
    o = [K2.sky(w, h, "#1E2A5A", "#0B1A2E")]
    gy = h * 0.74
    o.append(f'<rect x="-10" y="{f(gy)}" width="{f(w * 0.55)}" height="{f(h)}" fill="#5A4A3A"></rect><rect x="{f(w * 0.54)}" y="{f(gy + 6)}" width="{f(w * 0.5)}" height="{f(h)}" fill="#1F4A6A"></rect>'
             f'<path d="M-10 {f(gy)} L {f(w * 0.54)} {f(gy)} L {f(w * 0.56)} {f(gy + 6)} L {f(w + 10)} {f(gy + 6)}" stroke="#8FD0E2" stroke-width="2" fill="none"></path>'
             f'<rect x="-10" y="{f(h * 0.9)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#0B0B12" opacity="0.8"></rect>')
    o.append(f'<g stroke="#2A4A7A" stroke-width="1">' + "".join(f'<path d="M{f(x)} 0 L {f(x)} {f(h)}"></path>' for x in range(0, int(w), 40)) + '</g>')
    def dim(x0, y0, x1, y1, text, lx, ly):
        return (f'<path d="M{f(x0)} {f(y0)} L {f(x1)} {f(y1)}" stroke="#FFD23F" stroke-width="2" stroke-dasharray="6 5"></path>'
                f'<path d="M{f(x1)} {f(y1)} l -6 {f(10 if y1 > y0 else -10 if y1 < y0 else 0)}" stroke="#FFD23F" stroke-width="2"></path>' + label(lx, ly, text, "#FFD23F", 10))
    o.append(dim(w * 0.12, gy - 6, w * 0.12, -10, "HIGH AS HEAVEN ↑", w * 0.12 + 70, gy - 16))
    o.append(dim(w * 0.3, gy + 4, w * 0.3, h + 10, "DEEPER THAN SHEOL ↓", w * 0.3 + 76, h * 0.86))
    o.append(f'<path d="M-10 {f(gy - 30)} L {f(w * 0.53)} {f(gy - 30)}" stroke="#8FD0E2" stroke-width="2" stroke-dasharray="6 5"></path>' + label(w * 0.42, gy - 38, "← LONGER THAN THE EARTH", "#8FD0E2", 10))
    o.append(f'<path d="M{f(w * 0.56)} {f(gy - 30)} L {f(w + 10)} {f(gy - 30)}" stroke="#8FD0E2" stroke-width="2" stroke-dasharray="6 5"></path>' + label(w * 0.78, gy - 38, "BROADER THAN THE SEA →", "#8FD0E2", 10))
    return "".join(o)

def morning(p, w, h, seed):
    """Thy life shall be clearer than the noonday; though there be darkness, it shall be as the morning; thou shalt lie down,
    and none shall make thee afraid: dawn breaking over the hills, a tent at peace with its flock."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A2A5A", "#FFC890"), sun(w * 0.7, h * 0.82, min(30, h * 0.08), color="#FFD23F", op=0.4),
         hills(w, h, h * 0.8, seed, "#5A4A5A", amp=10, step=90), ground(w, h, h * 0.86, "#8A9A5A", dy=0),
         A.black_tent(w * 0.18, h * 0.88, w * 0.18, h * 0.1, color="#3A2A22"), flock(w * 0.4, w * 0.6, h * 0.88, h * 0.96, 8, seed, cows=0, smin=0.14, smax=0.2)]
    return "".join(o)

def robber_tents(p, w, h, seed):
    """The tents of robbers prosper: dark tents at evening heaped with plunder, camels laden, their fire bright."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A1A3A", "#C8704A"), hills(w, h, h * 0.78, seed, "#3A2A2A", amp=10, step=90), ground(w, h, h * 0.84, "#6A4A3A", dy=0)]
    for i in range(3): o.append(A.black_tent(w * (0.06 + i * 0.22), h * (0.88 - (i % 2) * 0.02), w * 0.2, h * 0.12, color="#1A1214", lit="#FF8A3D"))
    for i in range(6):
        x = w * (0.1 + i * 0.07)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.9)}" width="{f(w * 0.04)}" height="{f(h * 0.05)}" fill="{["#E8B830", "#B5121B", "#1F5FAD"][i % 3]}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(J1.camel(w * 0.8, h * 0.94, min(0.4, h / 800), color="#8A6A4A") + E.blaze(w * 0.66, h * 0.96, w * 0.06, h * 0.1, seed, n=4))
    return "".join(o)

def creatures(w, h, seed):
    """Ask now the beasts, and the birds of the heavens; speak to the earth, and the fishes of the sea shall declare: a lion on
    a rock, birds over the shore, fish beneath the water."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8FD0E2", "#E8F0D8"), P(f"M-10 {f(h * 0.82)} L {f(w * 0.46)} {f(h * 0.8)} L {f(w * 0.52)} {f(h + 10)} L -10 {f(h + 10)} Z", "#B89A6A"),
         f'<rect x="{f(w * 0.5)}" y="{f(h * 0.82)}" width="{f(w * 0.55)}" height="{f(h * 0.3)}" fill="#2C7DA0"></rect>',
         P(f"M{f(w * 0.06)} {f(h * 0.9)} L {f(w * 0.1)} {f(h * 0.84)} L {f(w * 0.3)} {f(h * 0.83)} L {f(w * 0.34)} {f(h * 0.9)} Z", "#8A7A6A")]
    o.append(J2.lion(w * 0.12, h * 0.84, min(0.4, h / 800), roar=False))
    for i in range(7):
        x = w * r.uniform(0.3, 0.95); y = h * r.uniform(0.6, 0.76); s = r.uniform(0.8, 1.6)
        o.append(f'<path d="M{f(x - 10 * s)} {f(y)} q {f(5 * s)} {f(-7 * s)} {f(10 * s)} 0 q {f(5 * s)} {f(-7 * s)} {f(10 * s)} 0" fill="none" stroke="#0D0D0F" stroke-width="2.2"></path>')
    for i in range(5):
        x = w * r.uniform(0.56, 0.95); y = h * r.uniform(0.88, 0.98); s = r.uniform(0.7, 1.2)
        o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">' + P("M-16 0 C -8 -8 8 -8 14 0 C 8 8 -8 8 -16 0 Z", "#C8D8E0", 1.4) + P("M14 0 L 22 -7 L 22 7 Z", "#C8D8E0", 1.4) + '</g>')
    return "".join(o)

def flood(w, h, seed):
    """He sendeth out the waters, and they overturn the earth; he breaketh down, and it cannot be built again: a flood
    bursting through a broken wall and running over the fields."""
    o = [K2.sky(w, h, "#4A5A6A", "#A8B8C0"), ground(w, h, h * 0.8, "#6A7A4A", dy=0),
         P(f"M-10 {f(h * 0.62)} L {f(w * 0.36)} {f(h * 0.62)} L {f(w * 0.4)} {f(h * 0.7)} L {f(w * 0.36)} {f(h * 0.86)} L -10 {f(h * 0.86)} Z", "#A8987A"),
         P(f"M{f(w * 0.56)} {f(h * 0.66)} L {f(w * 0.62)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.86)} L {f(w * 0.6)} {f(h * 0.86)} Z", "#A8987A")]
    o.append(f'<path d="M{f(w * 0.38)} {f(h * 0.62)} C {f(w * 0.44)} {f(h * 0.7)} {f(w * 0.46)} {f(h * 0.8)} {f(w * 0.3)} {f(h + 10)} L {f(w * 0.9)} {f(h + 10)} C {f(w * 0.66)} {f(h * 0.86)} {f(w * 0.6)} {f(h * 0.74)} {f(w * 0.58)} {f(h * 0.62)} Z" fill="#3A7A9A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    r = random.Random(seed)
    for i in range(14):
        x = w * r.uniform(0.38, 0.75); y = h * r.uniform(0.66, 0.98)
        o.append(f'<path d="M{f(x)} {f(y)} q 10 -8 20 0" stroke="#E8F6FA" stroke-width="2.4" fill="none"></path>')
    for i in range(6):
        o.append(f'<rect x="{f(w * r.uniform(0.4, 0.7))}" y="{f(h * r.uniform(0.7, 0.95))}" width="14" height="10" fill="#A8987A" stroke="#0D0D0F" stroke-width="1.4" transform="rotate({r.randint(-40, 40)})"></rect>')
    return "".join(o)

def lost_way(p, w, h, seed):
    """He causeth them to wander in a wilderness where there is no way; they grope in the dark without light: three figures at
    night among the dunes, arms out, no path anywhere."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#05050F", "#1A1A2E"), mk.stars(20, w, h * 0.5, seed, color="#5A5A7A")]
    r = random.Random(seed)
    for i in range(4):
        y = h * (0.76 + i * 0.06)
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 20)} {f(w * 0.6)} {f(y + 20)} {f(w + 10)} {f(y - 10)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{["#2A2420", "#221E1A", "#1A1614", "#121010"][i]}" stroke="#0D0D0F" stroke-width="1.6"></path>')
    s = fit(h * 0.96, h * 0.74)
    for i, x in enumerate((0.24, 0.5, 0.76)):
        o.append(man(p, w * x, h * (0.92 + (i % 2) * 0.04), s * (0.9 + 0.1 * (i % 2)), "#3A3440", flip=i == 1, up=[(-22, -158), (-50, -140), (-74, -130)]))
    return "".join(o)

def crumbling(w, h, seed):
    """Your memorable sayings are proverbs of ashes, your defences are defences of clay: a rampart of unbaked clay slumping
    and cracking in the rain, grey ash blowing off its top."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#6A6A7A", "#B8B0A0"), ground(w, h, h * 0.9, "#7A6A52", dy=0)]
    x0, x1, top = w * 0.08, w * 0.92, h * 0.68
    pts = [(x0, h * 0.92)] + [(x0 + (x1 - x0) * i / 10, top + r.uniform(-10, 18) + (30 if i in (6, 7) else 0)) for i in range(11)] + [(x1, h * 0.92)]
    o.append(P("M" + " L ".join(f"{f(x)} {f(y)}" for x, y in pts) + " Z", "#A8805A"))
    for i in range(9):
        x = x0 + r.uniform(0, 1) * (x1 - x0)
        o.append(f'<path d="M{f(x)} {f(top + 14)} l {f(r.uniform(-8, 8))} 18 l {f(r.uniform(-8, 8))} 16" stroke="#5A3A1E" stroke-width="1.8" fill="none"></path>')
    for i in range(40):
        x = r.uniform(x0, x1) + r.uniform(0, 60); y = top - r.uniform(0, h * 0.14)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(1, 3))}" fill="#C8C4BC" opacity="0.7"></circle>')
    o.append(f'<path d="M{f(w * 0.6)} {f(h * 0.92)} C {f(w * 0.62)} {f(h * 0.86)} {f(w * 0.74)} {f(h * 0.86)} {f(w * 0.8)} {f(h * 0.94)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def cause_scroll(w, h, seed):
    """Behold now, I have set my cause in order: a scroll unrolled on a low table, its columns written, the reed pen and
    the ink beside it."""
    o = [rect(w, h, "#3A2A2A"), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.86)}" r="{f(h * 0.3)}" fill="#FFC14D" opacity="0.12"></circle>',
         P(f"M{f(w * 0.06)} {f(h * 0.9)} L {f(w * 0.94)} {f(h * 0.9)} L {f(w * 0.94)} {f(h * 0.94)} L {f(w * 0.06)} {f(h * 0.94)} Z", "#6A4A2A")]
    x0, x1, y0, y1 = w * 0.18, w * 0.82, h * 0.72, h * 0.89
    o.append(P(f"M{f(x0)} {f(y1)} L {f(x0 + 20)} {f(y0)} L {f(x1 - 20)} {f(y0)} L {f(x1)} {f(y1)} Z", "#E8D8B0"))
    for c in range(4):
        cx = x0 + 30 + c * (x1 - x0 - 60) / 4
        for k in range(4):
            y = y0 + 8 + k * (y1 - y0 - 12) / 4
            o.append(f'<path d="M{f(cx + 4)} {f(y)} L {f(cx + (x1 - x0 - 60) / 4 - 10)} {f(y)}" stroke="#5A3A2A" stroke-width="1.6"></path>')
    o.append(f'<ellipse cx="{f(x0 + 6)}" cy="{f((y0 + y1) / 2)}" rx="10" ry="{f((y1 - y0) / 2 + 4)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<ellipse cx="{f(x1 - 6)}" cy="{f((y0 + y1) / 2)}" rx="10" ry="{f((y1 - y0) / 2 + 4)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<path d="M{f(w * 0.86)} {f(h * 0.88)} L {f(w * 0.94)} {f(h * 0.76)}" stroke="#8A6A3A" stroke-width="3"></path>'
             f'<rect x="{f(w * 0.08)}" y="{f(h * 0.82)}" width="{f(w * 0.05)}" height="{f(h * 0.08)}" fill="#1A1A2A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)

def driven_leaf(w, h, seed):
    """Wilt thou harass a driven leaf? and wilt thou pursue the dry stubble?: a reaped field of stubble in a gale, dry leaves
    and straws flying before the wind."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8A8A9A", "#E8D8B0"), ground(w, h, h * 0.8, "#C8A86A", dy=0)]
    for i in range(80):
        x = r.uniform(0, w); y = r.uniform(h * 0.82, h)
        o.append(f'<path d="M{f(x)} {f(y)} l 3 -12" stroke="#8A6A3A" stroke-width="1.6"></path>')
    for i in range(16):
        x = r.uniform(0, w); y = r.uniform(h * 0.5, h * 0.84); a = r.uniform(0, 360)
        o.append(f'<g transform="translate({f(x)} {f(y)}) rotate({a:.0f})">' + P("M0 0 C 6 -8 16 -8 22 0 C 16 8 6 8 0 0 Z", r.choice(["#C8902A", "#8A5A2A", "#B8A040"]), 1.2) + '</g>')
    for i in range(8):
        y = h * (0.5 + i * 0.05)
        o.append(f'<path d="M{f(w * 0.0)} {f(y)} C {f(w * 0.3)} {f(y - 10)} {f(w * 0.6)} {f(y + 10)} {f(w)} {f(y)}" stroke="#FFFFFF" stroke-width="1.6" opacity="0.4" fill="none"></path>')
    return "".join(o)

def stocks(w, h, seed):
    """Thou puttest my feet also in the stocks; like a garment that is moth-eaten: a pair of wooden stocks in a bare yard,
    and a robe hung on a peg beside it, eaten through with holes."""
    r = random.Random(seed)
    o = [rect(w, h, "#5A5048"), P(f"M-10 {f(h * 0.4)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h * 0.86)} L -10 {f(h * 0.86)} Z", "#7A6A5A"), ground(w, h, h * 0.86, "#4A4038", dy=0)]
    k = min(1.4, h / 280); x, y = w * 0.32, h * 0.98
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})">' + P("M-90 0 L -90 -40 L 90 -40 L 90 0 Z", "#8A5A30") + '<path d="M-90 -20 L 90 -20" stroke="#0D0D0F" stroke-width="2"></path>'
             + '<circle cx="-40" cy="-20" r="9" fill="#2A1A10"></circle><circle cx="40" cy="-20" r="9" fill="#2A1A10"></circle>'
             + P("M-100 0 L -100 -56 L -90 -56 L -90 0 Z", "#6A4A2A") + P("M90 0 L 90 -56 L 100 -56 L 100 0 Z", "#6A4A2A") + '</g>')
    gx, gy = w * 0.74, h * 0.6
    o.append(f'<circle cx="{f(gx)}" cy="{f(gy)}" r="5" fill="#3A2214"></circle>'
             + P(f"M{f(gx)} {f(gy)} L {f(gx - w * 0.08)} {f(gy + h * 0.08)} L {f(gx - w * 0.07)} {f(h * 0.94)} L {f(gx + w * 0.07)} {f(h * 0.94)} L {f(gx + w * 0.08)} {f(gy + h * 0.08)} Z", "#8A7A9A"))
    for i in range(12):
        o.append(f'<ellipse cx="{f(gx + r.uniform(-0.06, 0.06) * w)}" cy="{f(r.uniform(gy + h * 0.1, h * 0.92))}" rx="{f(r.uniform(3, 7))}" ry="{f(r.uniform(2, 5))}" fill="#5A5048"></ellipse>')
    return "".join(o)

def flower_cut(w, h, seed):
    """He cometh forth like a flower, and is cut down; he fleeth also as a shadow: wild flowers in the grass, one stalk cut
    and fallen, the long shadow of evening across them."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#6A5A8A", "#F3C89A"), ground(w, h, h * 0.8, "#7A9A4A", dy=0),
         f'<path d="M-10 {f(h * 0.9)} L {f(w + 10)} {f(h * 0.84)} L {f(w + 10)} {f(h * 0.92)} L -10 {f(h * 0.98)} Z" fill="#3A4A2A" opacity="0.5"></path>']
    for i in range(14):
        x = w * (0.06 + i * 0.066) + r.uniform(-10, 10); top = h * r.uniform(0.66, 0.76)
        o.append(f'<path d="M{f(x)} {f(h * 0.96)} Q {f(x + 6)} {f((top + h) / 2)} {f(x)} {f(top)}" stroke="#2E6B3A" stroke-width="2.4" fill="none"></path>'
                 + "".join(f'<ellipse cx="{f(x + math.cos(a) * 7)}" cy="{f(top + math.sin(a) * 7)}" rx="5" ry="3" transform="rotate({math.degrees(a):.0f} {f(x + math.cos(a) * 7)} {f(top + math.sin(a) * 7)})" fill="{["#E85A8A", "#F3EFE6", "#FFD23F"][i % 3]}" stroke="#0D0D0F" stroke-width="0.8"></ellipse>' for a in [k * 1.2566 for k in range(5)])
                 + f'<circle cx="{f(x)}" cy="{f(top)}" r="3" fill="#E8B830"></circle>')
    x = w * 0.5
    o.append(f'<path d="M{f(x)} {f(h * 0.96)} L {f(x + w * 0.12)} {f(h * 0.94)}" stroke="#6A8A3A" stroke-width="2.4"></path><circle cx="{f(x + w * 0.12)}" cy="{f(h * 0.94)}" r="6" fill="#C85A7A" stroke="#0D0D0F" stroke-width="1"></circle>')
    return "".join(o)

def stump(w, h, seed, sprout=True):
    """There is hope of a tree, if it be cut down, that it will sprout again; through the scent of water it will bud: an old
    stump by a trickle of water with a tender green shoot rising from it."""
    o = [K2.sky(w, h, "#8FD0E2", "#F0F0D8"), ground(w, h, h * 0.84, "#8A7A4A", dy=0),
         f'<path d="M-10 {f(h * 0.96)} C {f(w * 0.3)} {f(h * 0.92)} {f(w * 0.5)} {f(h * 0.98)} {f(w + 10)} {f(h * 0.94)}" stroke="#8FD0E2" stroke-width="8" fill="none"></path>']
    k = min(1.4, h / 300); x, y = w * 0.44, h * 0.92
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})">' + P("M-50 0 C -40 -10 -36 -50 -40 -70 L 40 -70 C 36 -50 40 -10 50 0 Z", "#6A4A2A")
             + '<ellipse cx="0" cy="-70" rx="40" ry="10" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             + '<g fill="none" stroke="#8A6A3A" stroke-width="1.4"><ellipse cx="0" cy="-70" rx="26" ry="6"></ellipse><ellipse cx="0" cy="-70" rx="12" ry="3"></ellipse></g>'
             + '<path d="M-50 0 C -70 4 -80 -2 -90 6 M50 0 C 70 2 76 -4 90 4" stroke="#6A4A2A" stroke-width="6" fill="none"></path>'
             + ('<path d="M22 -72 C 26 -100 40 -116 50 -130" stroke="#3A8A3A" stroke-width="4" fill="none"></path>'
                '<ellipse cx="38" cy="-108" rx="10" ry="5" fill="#7ACB5E" stroke="#0D0D0F" stroke-width="1.2" transform="rotate(-30 38 -108)"></ellipse>'
                '<ellipse cx="52" cy="-126" rx="9" ry="5" fill="#7ACB5E" stroke="#0D0D0F" stroke-width="1.2" transform="rotate(20 52 -126)"></ellipse>' if sprout else "") + '</g>')
    return "".join(o)

def sealed_bag(w, h, seed):
    """My transgression is sealed up in a bag: a leather bag tied at the neck and sealed with clay, on a stone shelf."""
    o = [rect(w, h, "#3A3038"), P(f"M-10 {f(h * 0.9)} L {f(w + 10)} {f(h * 0.9)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z", "#6A6058")]
    k = min(1.4, h / 260); x, y = w * 0.5, h * 0.9
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})">' + P("M-50 0 C -64 -40 -40 -80 -12 -86 L -16 -100 L 16 -100 L 12 -86 C 40 -80 64 -40 50 0 Z", "#8A5A30")
             + '<path d="M-14 -90 L 14 -90" stroke="#3A2214" stroke-width="5"></path><path d="M14 -90 C 30 -86 34 -70 26 -60" stroke="#3A2214" stroke-width="3" fill="none"></path>'
             + '<circle cx="26" cy="-56" r="10" fill="#B5121B" stroke="#0D0D0F" stroke-width="2"></circle><path d="M20 -56 L 32 -56 M26 -62 L 26 -50" stroke="#5A0A0A" stroke-width="2"></path></g>')
    return "".join(o)

def worn_stones(w, h, seed):
    """The mountain falling cometh to nought; the waters wear the stones: a torrent pouring down a fallen crag, round
    worn stones in its bed and the dust washed away."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#6A7A8A", "#C8D0D0"), P(f"M{f(w * 0.1)} {f(h + 10)} L {f(w * 0.2)} {f(h * 0.6)} L {f(w * 0.34)} {f(h * 0.66)} L {f(w * 0.4)} {f(h + 10)} Z", "#7A6A5A"),
         P(f"M{f(w * 0.6)} {f(h + 10)} L {f(w * 0.66)} {f(h * 0.62)} L {f(w * 0.84)} {f(h * 0.58)} L {f(w * 0.94)} {f(h + 10)} Z", "#6A5A4A"),
         f'<path d="M{f(w * 0.4)} {f(h * 0.62)} C {f(w * 0.46)} {f(h * 0.7)} {f(w * 0.44)} {f(h * 0.86)} {f(w * 0.38)} {f(h + 10)} L {f(w * 0.64)} {f(h + 10)} C {f(w * 0.58)} {f(h * 0.86)} {f(w * 0.58)} {f(h * 0.7)} {f(w * 0.64)} {f(h * 0.62)} Z" fill="#5AA8C8" stroke="#0D0D0F" stroke-width="2"></path>']
    for i in range(12):
        o.append(f'<ellipse cx="{f(w * r.uniform(0.42, 0.6))}" cy="{f(h * r.uniform(0.74, 0.98))}" rx="{f(r.uniform(8, 16))}" ry="{f(r.uniform(5, 9))}" fill="#A8A098" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    for i in range(10):
        x = w * r.uniform(0.44, 0.58); y = h * r.uniform(0.66, 0.96)
        o.append(f'<path d="M{f(x)} {f(y)} l 0 14" stroke="#E8F6FA" stroke-width="2"></path>')
    return "".join(o)

def wild_ass_run(w, h, seed):
    """Man is born as a wild ass's colt: a wild ass running alone over the open plain."""
    from genesis.art4 import wild_ass
    return K2.sky(w, h, "#E8C890", "#F3E8C8") + wild_ass(w, h, seed)
