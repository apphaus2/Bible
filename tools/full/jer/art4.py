"""Drawings for Jeremiah chapter 4 (Jeremiah 10–12), on top of jer.art."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2
from ezr.art import letter_scroll

def idol(x, y, s=1.0, decked=True):
    """A graven image of turned work like a palm-tree, plated with silver and gold, nailed fast to its base so that it move not."""
    gold, silver = ("#E8B830", "#C8C8D0") if decked else ("#8A6A3A", "#7A5A30")
    o = (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
         f'<rect x="-34" y="-14" width="68" height="14" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
         f'<path d="M-16 -14 L -12 -150 Q 0 -168 12 -150 L 16 -14 Z" fill="{gold}" stroke="#0D0D0F" stroke-width="2.4"></path>'
         + "".join(f'<path d="M-15 {-30 - k * 26} L 15 {-30 - k * 26}" stroke="{silver}" stroke-width="5"></path>' for k in range(5))
         + f'<circle cx="0" cy="-160" r="14" fill="{gold}" stroke="#0D0D0F" stroke-width="2.4"></circle>'
         + "".join(f'<circle cx="{dx}" cy="-8" r="2.6" fill="#3A3A3A"></circle>' for dx in (-26, -10, 10, 26))
         + (f'<path d="M-30 -120 Q 0 -100 30 -120 L 26 -70 Q 0 -54 -26 -70 Z" fill="#3A3A8A" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="M-26 -70 Q 0 -54 26 -70 L 22 -50 Q 0 -36 -22 -50 Z" fill="#7A2A7A" stroke="#0D0D0F" stroke-width="2"></path>' if decked else "")
         + '</g>')
    return o

def idol_maker(p, w, h, seed, decked=False):
    """One cutteth a tree out of the forest with the axe; they deck it with silver and gold and fasten it with nails: the felled
    tree, the workman with his axe, the image standing finished (decked=True: clothed in blue and purple, borne by two men)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E0B0"), thicket(-10, w * 0.3, h * 0.6, h * 0.5, seed), ground(w, h, h * 0.6, "#B89A6A", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    if not decked:
        o.append(f'<path d="M{f(w * 0.12)} {f(b - 6)} L {f(w * 0.42)} {f(b - 22)}" stroke="#6A4A2A" stroke-width="{f(14 * s)}" stroke-linecap="round"></path>')
        o.append(man(p, w * 0.32, b, s, "#6A4A2A", up=[(-22, -158), (-40, -196), (-30, -230)]) +
                 f'<path d="M{f(w * 0.32 - 30 * s)} {f(b - 230 * s)} l {f(-18 * s)} {f(-6 * s)} l {f(4 * s)} {f(16 * s)} Z" fill="#8A8A90" stroke="#0D0D0F" stroke-width="1.6"></path>')
        o.append(idol(w * 0.7, b, s * 1.1, decked=True))
    else:
        o.append(idol(w * 0.5, b - 120 * s * 0.0, s * 1.2, decked=True))
        for x in (0.32, 0.68): o.append(man(p, w * x, b, s * 0.9, "#5A4A3A", flip=x > 0.5, up=[(-22, -158), (-6, -120), (14, -110)]))
    return "".join(o)

def heavens_waters(w, h, seed):
    """He stretched out the heavens; when he uttereth his voice there is a tumult of waters in the heavens, vapours from the
    ends of the earth, lightnings for the rain, the wind out of his treasuries."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#1A1A3A", "#5A6A8A")]
    for i in range(6):
        o.append(f'<ellipse cx="{f(w * (0.08 + i * 0.18))}" cy="{f(h * (0.24 + (i % 2) * 0.08))}" rx="{f(w * 0.16)}" ry="{f(h * 0.12)}" fill="#3A3A5A" opacity="0.9"></ellipse>')
    o.append(E2.bolt(w * 0.3, h * 0.28, h * 0.5, seed) + E2.bolt(w * 0.72, h * 0.3, h * 0.44, seed + 1))
    o.append("".join(f'<path d="M{f(r.uniform(0, w))} {f(r.uniform(h * 0.3, h * 0.8))} l -8 22" stroke="#C8D8E8" stroke-width="1.6" opacity="0.7"></path>' for _ in range(50)))
    o.append(f'<rect x="-10" y="{f(h * 0.82)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#1F4A6A"></rect>'
             f'<path d="M-10 {f(h * 0.84)} ' + " ".join(f"q {f(w / 20)} -10 {f(w / 10)} 0" for _ in range(11)) + '" fill="none" stroke="#E8F6FA" stroke-width="2"></path>')
    return "".join(o)

def bundle(w, h, seed):
    """Gather up thy wares out of the land, O thou that abidest in the siege: a bundle tied up and a staff by the shut gate."""
    o = [K2.sky(w, h, "#5A4A5A", "#C8A080"), wall(-10, w + 10, h * 0.3, h * 0.78, seed, towers=3, gate=w * 0.5), ground(w, h, h * 0.78, "#8A7A5A", dy=0)]
    bx, by, s = w * 0.3, h * 0.96, min(1.2, h / 220)
    o.append(f'<path d="M{f(bx - 40 * s)} {f(by)} Q {f(bx - 46 * s)} {f(by - 50 * s)} {f(bx)} {f(by - 56 * s)} Q {f(bx + 46 * s)} {f(by - 50 * s)} {f(bx + 40 * s)} {f(by)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.2"></path>'
             f'<path d="M{f(bx - 8 * s)} {f(by - 56 * s)} l -6 -14 l 14 6 l 14 -6 l -6 14" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.8"></path>'
             f'<path d="M{f(bx + 60 * s)} {f(by)} L {f(bx + 90 * s)} {f(by - 120 * s)}" stroke="#5A3A1E" stroke-width="{f(5 * s)}" stroke-linecap="round"></path>')
    return "".join(o)

def tent_broken(w, h, seed):
    """My tent is destroyed, and all my cords are broken; there is none to spread my tent any more: a fallen tent, its poles down
    and its cords snapped."""
    o = [K2.sky(w, h, "#4A3A4A", "#D8A880"), hills(w, h, h * 0.56, seed, "#7A5A4A", amp=10, step=80), ground(w, h, h * 0.66, "#B89A6A", dy=0)]
    x0, x1, b = w * 0.24, w * 0.76, h * 0.92
    o.append(f'<path d="M{f(x0)} {f(b)} Q {f(w * 0.4)} {f(h * 0.7)} {f(w * 0.52)} {f(h * 0.78)} Q {f(w * 0.64)} {f(h * 0.72)} {f(x1)} {f(b)} Z" fill="#3A2A1E" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.3)} {f(h * 0.86)} L {f(w * 0.7)} {f(h * 0.82)}" stroke="#8A6A4A" stroke-width="2" stroke-dasharray="10 6"></path>'
             f'<path d="M{f(w * 0.44)} {f(b)} L {f(w * 0.36)} {f(h * 0.66)}" stroke="#6A4A2A" stroke-width="6"></path>')
    for x, d in ((0.12, -1), (0.88, 1)):
        o.append(f'<path d="M{f(w * x)} {f(b)} L {f(w * x)} {f(b - 14)}" stroke="#5A3A1E" stroke-width="5"></path>'
                 f'<path d="M{f(w * x)} {f(b - 12)} q {f(-d * 20)} -10 {f(-d * 50)} -4" stroke="#C8A878" stroke-width="2" fill="none"></path>')
    return "".join(o)

def covenant_scroll(w, h, seed):
    """Hear ye the words of this covenant, which I commanded your fathers when I brought them out of the iron furnace."""
    return letter_scroll(w, h, seed, seal="#B5121B", text_lines=7)

def altars_streets(w, h, seed):
    """According to the number of the streets of Jerusalem have ye set up altars to burn incense unto Baal: a street of shut
    houses with a small smoking altar before every door."""
    o = [empty_city(w, h, seed)]
    r = random.Random(seed)
    for i in range(6):
        x = w * (0.08 + i * 0.17); y = h * 0.86
        o.append(f'<rect x="{f(x - 10)}" y="{f(y - 16)}" width="20" height="16" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 + smoke(x, y - 26, 5, seed + i, r0=0.015, w=0.4, color="#E8E2D6", op=0.5))
    return "".join(o)

def olive_fire(w, h, seed):
    """A green olive-tree, fair with goodly fruit: with the noise of a great tumult he hath kindled fire upon it, and the branches
    of it are broken."""
    o = [K2.sky(w, h, "#3A1A1A", "#C8703A"), hills(w, h, h * 0.6, seed, "#4A3A2A", amp=8, step=90), ground(w, h, h * 0.72, "#5A4A2A", dy=0),
         JG2.olive(w * 0.5, h * 0.94, min(1.8, h / 150), burning=True, seed=seed)]
    for k in range(3):
        o.append(f'<path d="M{f(w * (0.3 + k * 0.2))} {f(h * 0.96)} l {f(w * 0.06)} -12" stroke="#4A2A1A" stroke-width="5"></path>')
    return "".join(o)

def anathoth_plot(p, w, h, seed):
    """I was like a gentle lamb that is led to the slaughter, and I knew not that they had devised devices against me: the
    village of Anathoth at dusk, men whispering together at its gate; a lamb on the road."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A1A3A", "#C8805A"), J.city_hill(w * 0.68, h * 0.62, w * 0.26, h * 0.24, seed), ground(w, h, h * 0.62, "#6A5A4A", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    for i in range(3):
        o.append(man(p, w * (0.62 + i * 0.08), b, s * 0.9, "#2A2028", flip=i == 2, extra=A.headcloth("#2A2028")))
    o.append(E3.lamb(w * 0.22, b, min(1.0, s * 1.2)))
    return "".join(o)

def footmen_horses(p, w, h, seed):
    """If thou hast run with the footmen, and they have wearied thee, how canst thou contend with horses? and how wilt thou do in
    the pride of the Jordan?: a runner on the road, horses beyond, the thickets of the Jordan."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E0B0"), thicket(w * 0.55, w + 10, h * 0.62, h * 0.4, seed),
         f'<path d="M{f(w * 0.5)} {f(h * 0.66)} C {f(w * 0.7)} {f(h * 0.62)} {f(w * 0.8)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.66)}" stroke="#2C9DB8" stroke-width="5" fill="none"></path>',
         ground(w, h, h * 0.7, "#C8A870", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    o.append(S4b.runner(p, w * 0.2, b, s, cloth=JER_C))
    for i in range(2): o.append(E3.horse(w * (0.5 + i * 0.18), b - (i % 2) * 6, min(0.8, s * 0.9), color=["#3A2214", "#6A4A2A"][i]))
    return "".join(o)

def speckled_bird(w, h, seed):
    """Is my heritage unto me as a speckled bird of prey? are the birds of prey against her round about?"""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#5A4A5A", "#E8B880"), hills(w, h, h * 0.8, seed, "#5A4A3A", amp=10, step=80)]
    cx, cy, s = w * 0.5, h * 0.56, min(w, h) * 0.006
    o.append(f'<g transform="translate({f(cx)} {f(cy)}) scale({f(s)})"><path d="M-60 0 Q -30 -30 0 -6 Q 30 -30 60 0 Q 30 -8 10 6 L 0 26 L -10 6 Q -30 -8 -60 0 Z" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<circle cx="{dx}" cy="{dy}" r="3" fill="#5A3A1E"></circle>' for dx, dy in ((-40, -6), (-26, -12), (-14, -4), (14, -4), (26, -12), (40, -6), (0, 10)))
             + '<circle cx="0" cy="-10" r="6" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.6"></circle></g>')
    for i in range(7):
        a = i * 2 * math.pi / 7
        o.append(bird(cx + math.cos(a) * w * 0.32, cy + math.sin(a) * h * 0.3, 1.6))
    return "".join(o)

def trodden_vineyard(w, h, seed):
    """Many shepherds have destroyed my vineyard, they have trodden my portion under foot: broken stakes and trampled vines in
    a bare field, a flock's tracks across it."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8A8A9A", "#E8D0A0"), hills(w, h, h * 0.5, seed, "#8A7A5A", amp=10, step=90), ground(w, h, h * 0.6, "#9A7A4A", dy=0)]
    for k in range(7):
        x = w * (0.08 + k * 0.14)
        o.append(f'<path d="M{f(x)} {f(h * 0.9)} l {f(r.uniform(-30, 30))} {f(-h * r.uniform(0.06, 0.2))}" stroke="#5A3A1E" stroke-width="4"></path>'
                 f'<path d="M{f(x - 30)} {f(h * 0.92)} q 20 -10 50 -2" stroke="#4A3A1A" stroke-width="3" fill="none"></path>')
    o.append("".join(f'<ellipse cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.64, h))}" rx="3" ry="2" fill="#5A4A2A"></ellipse>' for _ in range(60)))
    return "".join(o)

def wheat_thorns(w, h, seed):
    """They have sown wheat, and have reaped thorns: a field of thorns where the wheat was sown, a sickle lying idle."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#C8A070", "#F3E0B0"), ground(w, h, h * 0.5, "#8A6A3A", dy=0)]
    for _ in range(40):
        x, y = r.uniform(0, w), r.uniform(h * 0.56, h)
        o.append(f'<path d="M{f(x)} {f(y)} l -8 -22 M{f(x)} {f(y)} l 4 -26 M{f(x)} {f(y)} l 12 -18 M{f(x - 4)} {f(y - 12)} l -5 -2 M{f(x + 2)} {f(y - 16)} l 5 -3" stroke="#3A2A1A" stroke-width="2" fill="none"></path>')
    return "".join(o)
