"""Drawings for the Malachi volume, on the minor prophets' kit (oba.minor), with drawings from Obadiah, Micah, Haggai and
the Kings where they fit. Edom's waste places; the blind, the lame and the sick brought to the altar; the doors shut; incense
from the rising of the sun to the going down of the same; the covenant with Levi; the altar covered with tears and the wife
of thy youth; the messenger preparing the way to the temple; the refiner's fire and the fuller's soap; the storehouse and
the windows of heaven opened; the book of remembrance; the day burning as a furnace; the sun of righteousness with healing in
its wings (a sun, its rays spread as wings — no figure); Horeb and the tables; and Elijah the prophet on the road, fathers
and children turned to one another. God is never drawn."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from oba.minor import *
from oba.art import stubble
from chr2.art import shut_doors
from kg1.art import elijah_fig, priest
from deu.art import horeb
from mic.art import balances
import samuel4 as S4, samuel1 as S1

MAL_C = "#E8E2D6"

def edom_waste(w, h, seed):
    """Esau I hated, and made his mountains a desolation, and gave his heritage to the jackals of the wilderness; they shall
    build, but I will throw down: the red rock with its dwellings broken, jackals among the ruins at dusk."""
    o = [vista(w, h, seed, tone="dusk", far="crag", cx=0.6, cw=0.8, hills_n=1, horizon=0.62), ruin(w * 0.02, w * 0.5, h * 0.92, h * 0.18, seed, color="#A8603A")]
    k = min(0.7, h / 360)
    for i, x in enumerate((0.58, 0.8)):
        o.append(f'<g transform="translate({f(w * x)} {f(h * 0.94)}) scale({f(k * (1 if i else -1))} {f(k)})"><path d="M-50 -20 C -40 -36 20 -40 36 -30 L 52 -48 L 58 -42 L 56 -30 L 68 -24 L 54 -18 L 40 -20 L 36 0 L 30 0 L 26 -14 L -26 -14 L -32 0 L -38 0 L -40 -18 C -50 -14 -60 -10 -66 -4 L -62 -14 Z" fill="#8A5A2A" stroke="#0D0D0F" stroke-width="1.6"></path></g>')
    return "".join(o)

def blemished(p, w, h, seed, shut=False):
    """Ye offer polluted bread upon mine altar; the blind, the lame and the sick for sacrifice: the altar with a meagre fire,
    a limping lamb, a blind one with a white eye and a sick one lying down brought to it, a broken loaf on the table."""
    o = [sky(w, h, "#6A4A3A", "#D8B898"), ground(w, h, h * 0.66, "#A88A6A", dy=0), S4.altar(w * 0.66, h * 0.9, min(1.0, h / 300), seed=seed)]
    k = min(0.7, h / 360)
    o.append(f'<g transform="rotate(-10 {f(w * 0.16)} {f(h * 0.94)})">{E.sheep(w * 0.16, h * 0.94, k)}</g>' + E.sheep(w * 0.32, h * 0.95, k * 0.9, wool="#C8C0B0")
             + f'<circle cx="{f(w * 0.32 + 34 * k * 0.9)}" cy="{f(h * 0.95 - 40 * k * 0.9)}" r="{f(4 * k)}" fill="#F3F3F3" stroke="#0D0D0F" stroke-width="1"></circle>'
             + S1.cow(w * 0.88, h * 0.98, k * 0.5, low=True))
    o.append(f'<rect x="{f(w * 0.38)}" y="{f(h * 0.78)}" width="{f(w * 0.14)}" height="{f(h * 0.03)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             f'<path d="M{f(w * 0.4)} {f(h * 0.78)} C {f(w * 0.42)} {f(h * 0.74)} {f(w * 0.46)} {f(h * 0.74)} {f(w * 0.45)} {f(h * 0.78)} Z M{f(w * 0.46)} {f(h * 0.78)} l 10 -6 l 6 6 Z" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return "".join(o)

def incense_world(w, h, seed):
    """From the rising of the sun even unto the going down of the same my name shall be great among the Gentiles; in every
    place incense shall be offered: a wide land from sunrise on the left to sunset on the right, thin columns of incense
    rising from many places."""
    o = [hgrad(f"iw{seed}", [("0", "#FFD8A0"), ("0.5", "#8FB8D8"), ("1", "#E8803A")]), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#iw{seed})"></rect>',
         sun(w * 0.06, h * 0.5, max(14, h * 0.07), color="#FFE680", op=0.4), sun(w * 0.94, h * 0.52, max(14, h * 0.07), color="#FF8A3D", op=0.4),
         hills(w, h, h * 0.6, seed, color="#6A6A5A", amp=14), ground(w, h, h * 0.66, "#8A7A5A", dy=0)]
    r = random.Random(seed)
    for i in range(9):
        x = w * (0.1 + i * 0.1); y = h * r.uniform(0.68, 0.92)
        o.append(f'<rect x="{f(x - 5)}" y="{f(y - 10)}" width="10" height="10" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></rect>'
                 f'<path d="M{f(x)} {f(y - 10)} C {f(x - 10)} {f(y - 40)} {f(x + 10)} {f(y - 60)} {f(x)} {f(y - 90)}" stroke="#F3EFE6" stroke-width="3" fill="none" opacity="0.7"></path>')
    return "".join(o)

def dim_altar(w, h, seed):
    """I will send the curse upon you, and curse your blessings; I will rebuke your seed: the altar cold under a grey sky,
    ash blown from it, a priest's turban dropped on the step."""
    o = [sky(w, h, "#3A3A4A", "#8A8478"), ground(w, h, h * 0.7, "#5A5248", dy=0), S4.altar(w * 0.5, h * 0.92, min(1.1, h / 280), fire=False, seed=seed),
         wind_lines(w, h, seed, n=8, color="#A8A29A", op=0.5, y0=0.3, y1=0.7)]
    k = min(1.0, h / 300)
    o.append(f'<path d="M{f(w * 0.74 - 16 * k)} {f(h * 0.94)} C {f(w * 0.74 - 18 * k)} {f(h * 0.94 - 24 * k)} {f(w * 0.74 + 18 * k)} {f(h * 0.94 - 24 * k)} {f(w * 0.74 + 16 * k)} {f(h * 0.94)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return "".join(o)

def levi_teach(p, w, h, seed):
    """My covenant was with Levi of life and peace; the law of truth was in his mouth; the priest's lips should keep
    knowledge, and they should seek the law at his mouth: a priest in white reading from a scroll in the court, people
    gathered to hear."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), sky(w, h, "#8FB8D8", "#F3E8C8"), temple_front(w * 0.8, h * 0.62, w * 0.3, seed), ground(w, h, h * 0.62, "#C8B88A", dy=0)]
    s = fit(b, h * 0.3)
    o.append(priest(p, w * 0.5, b, s, up=[(22, -158), (40, -150), (56, -146)]) + scroll(w * 0.5 + 64 * s, b - 150 * s, 50 * s, 30 * s, lines=3))
    o.append(crowd(p, w * 0.04, w * 0.36, b, h * 0.42, 4, seed, flip=False))
    return "".join(o)

def turned_aside(w, h, seed):
    """Ye are turned aside out of the way; ye have caused many to stumble in the law: a straight road and a path turning off
    it into rough ground, a scroll dropped at the fork."""
    o = [sky(w, h, "#6A6A7A", "#D8C8B0"), hills(w, h, h * 0.44, seed, color="#7A7060", amp=14), ground(w, h, h * 0.5, "#9A8A6A", dy=0),
         f'<path d="M{f(w * 0.46)} {f(h * 0.5)} L {f(w * 0.54)} {f(h * 0.5)} L {f(w * 0.7)} {f(h + 10)} L {f(w * 0.3)} {f(h + 10)} Z" fill="#C8B890" stroke="#0D0D0F" stroke-width="1.6"></path>',
         f'<path d="M{f(w * 0.42)} {f(h * 0.76)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.16)} {f(h * 0.74)} {f(w * 0.02)} {f(h * 0.66)}" stroke="#8A7050" stroke-width="{f(h * 0.06)}" fill="none"></path>']
    r = random.Random(seed)
    for i in range(10):
        x, y = r.uniform(0, w * 0.3), r.uniform(h * 0.6, h * 0.9)
        o.append(f'<path d="M{f(x)} {f(y)} l 8 -10 l 8 10 Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="1"></path>')
    o.append(f'<g transform="rotate(-20 {f(w * 0.46)} {f(h * 0.82)})">{scroll(w * 0.46, h * 0.82, w * 0.08, h * 0.05, lines=2)}</g>')
    return "".join(o)

def foreign_god(p, w, h, seed):
    """Have we not all one father? Judah hath married the daughter of a foreign god: a house in Judah, and in its doorway a
    small gilded idol set up, the father's house across the way dark."""
    o = [sky(w, h, "#8A7A8A", "#E8D0B0"), ground(w, h, h * 0.8, "#B8A07A", dy=0)]
    for i, x in enumerate((0.06, 0.56)):
        o.append(f'<rect x="{f(w * x)}" y="{f(h * 0.3)}" width="{f(w * 0.38)}" height="{f(h * 0.5)}" fill="{["#C8B090", "#D8C098"][i]}" stroke="#0D0D0F" stroke-width="2.2"></rect>'
                 f'<rect x="{f(w * x + w * 0.14)}" y="{f(h * 0.5)}" width="{f(w * 0.1)}" height="{f(h * 0.3)}" fill="#2A1A10" stroke="#0D0D0F" stroke-width="2"></rect>')
    k = min(0.8, h / 300); x, y = w * 0.75, h * 0.8
    o.append(halo(x, y - 40 * k, 40 * k, "#FFC14D", 0.5) + f'<path d="M{f(x - 10 * k)} {f(y)} L {f(x - 12 * k)} {f(y - 60 * k)} L {f(x + 12 * k)} {f(y - 60 * k)} L {f(x + 10 * k)} {f(y)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>'
             f'<circle cx="{f(x)}" cy="{f(y - 70 * k)}" r="{f(10 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    return "".join(o)

def tears_altar(p, w, h, seed):
    """Ye cover the altar of Jehovah with tears, with weeping, and with sighing; Jehovah hath been witness between thee and
    the wife of thy youth: the altar wet with drops in the dusk, and a woman alone at her door, her husband's back turned
    on the far road."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A4A", "#A87A6A"), ground(w, h, h * 0.66, "#5A4A40", dy=0), S4.altar(w * 0.3, h * 0.9, min(1.0, h / 300), fire=False, seed=seed)]
    r = random.Random(seed)
    for i in range(14):
        x, y = w * r.uniform(0.18, 0.42), h * r.uniform(0.62, 0.86)
        o.append(f'<path d="M{f(x)} {f(y)} c -3 5 -3 9 0 9 c 3 0 3 -4 0 -9 Z" fill="#8FD0E2" stroke="#0D0D0F" stroke-width="0.8"></path>')
    o.append(f'<rect x="{f(w * 0.6)}" y="{f(h * 0.34)}" width="{f(w * 0.3)}" height="{f(h * 0.62)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.68)}" y="{f(h * 0.56)}" width="{f(w * 0.1)}" height="{f(h * 0.4)}" fill="#1A1210"></rect>')
    o.append(woman(p, w * 0.73, b, fit(b, h * 0.6), "#7A3A5A", flip=True) + man(p, w * 0.96, h * 0.66, fit(h * 0.66, h * 0.56), "#3A3A4A"))
    return "".join(o)

def messenger_way(p, w, h, seed):
    """Behold, I send my messenger, and he shall prepare the way before me; and the Lord, whom ye seek, will suddenly come to
    his temple: a messenger on a straightened road, the temple at its end blazing with light (no one drawn in the light)."""
    from genesis.art3 import STAFF, HOLD_STAFF
    b = h * 0.95
    o = [mk.defs(p, *ALL), sky(w, h, "#2A3A6A", "#FFD8A0"), halo(w * 0.7, h * 0.36, h * 0.5, "#FFF4C2", 0.7), rays(w * 0.7, h * 0.36, 24, h * 0.1, max(w, h), "#FFF4C2", 0.3, 4),
         temple_front(w * 0.7, h * 0.56, w * 0.24, seed), ground(w, h, h * 0.56, "#B8A07A", dy=0),
         f'<path d="M{f(w * 0.66)} {f(h * 0.56)} L {f(w * 0.74)} {f(h * 0.56)} L {f(w * 0.5)} {f(h + 10)} L {f(w * 0.1)} {f(h + 10)} Z" fill="#E8D8A8" stroke="#0D0D0F" stroke-width="1.6"></path>']
    s = fit(b, h * 0.4)
    o.append(mk.person(p, round(w * 0.3), round(b), round(s, 3), body=SKIN, cloth="#E8E2D6", sw=3, flip=True, up=HOLD_STAFF, extra=STAFF + A.headcloth("#E8E2D6")))
    return "".join(o)

def refiner(w, h, seed):
    """He is like a refiner's fire, and like fullers' soap; he will sit as a refiner and purifier of silver, and purify the
    sons of Levi: a refiner's furnace with the crucible and the bright silver, and a fuller's basin with white cloth."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A14"></rect>', halo(w * 0.34, h * 0.6, h * 0.5, "#FF8A3D", 0.4),
         f'<rect x="-10" y="{f(h * 0.9)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#4A3424" stroke="#0D0D0F" stroke-width="2"></rect>']
    k = min(1.4, h / 240); x, y = w * 0.34, h * 0.9
    o.append(f'<path d="M{f(x - 70 * k)} {f(y)} L {f(x - 60 * k)} {f(y - 90 * k)} L {f(x + 60 * k)} {f(y - 90 * k)} L {f(x + 70 * k)} {f(y)} Z" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(x - 30 * k)} {f(y)} L {f(x - 30 * k)} {f(y - 40 * k)} Q {f(x)} {f(y - 60 * k)} {f(x + 30 * k)} {f(y - 40 * k)} L {f(x + 30 * k)} {f(y)} Z" fill="#FF8A3D"></path>'
             + E.blaze(x, y - 86 * k, 90 * k, 50 * k, seed, n=5)
             + f'<path d="M{f(x - 30 * k)} {f(y - 100 * k)} L {f(x + 30 * k)} {f(y - 100 * k)} L {f(x + 20 * k)} {f(y - 70 * k)} L {f(x - 20 * k)} {f(y - 70 * k)} Z" fill="#3A3A44" stroke="#0D0D0F" stroke-width="2"></path>'
             + f'<ellipse cx="{f(x)}" cy="{f(y - 100 * k)}" rx="{f(28 * k)}" ry="{f(6 * k)}" fill="#F3F3FF" stroke="#0D0D0F" stroke-width="1.4"></ellipse>' + halo(x, y - 100 * k, 30 * k, "#FFFFFF", 0.6))
    bx = w * 0.76
    o.append(f'<ellipse cx="{f(bx)}" cy="{f(y - 10 * k)}" rx="{f(70 * k)}" ry="{f(16 * k)}" fill="#6A6A72" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<path d="M{f(bx - 70 * k)} {f(y - 10 * k)} L {f(bx - 60 * k)} {f(y)} L {f(bx + 60 * k)} {f(y)} L {f(bx + 70 * k)} {f(y - 10 * k)}" fill="#5A5A62" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(bx - 40 * k)} {f(y - 14 * k)} C {f(bx - 20 * k)} {f(y - 60 * k)} {f(bx + 30 * k)} {f(y - 70 * k)} {f(bx + 50 * k)} {f(y - 20 * k)}" fill="#FFFFFF" stroke="#0D0D0F" stroke-width="1.6"></path>'
             + "".join(f'<circle cx="{f(bx + dx * k)}" cy="{f(y - (30 + abs(dx) * 0.4) * k)}" r="{f(4 * k)}" fill="#E8F6FA" stroke="#8FD0E2" stroke-width="1"></circle>' for dx in (-50, -20, 10, 40)))
    return "".join(o)

def storehouse(p, w, h, seed, full=False):
    """Will a man rob God? In tithes and offerings (full=False: the store-house bins standing empty); bring ye the whole
    tithe into the store-house, and I will open you the windows of heaven (full=True: the bins heaped, light and rain of
    blessing pouring from opened windows in the sky, the vines heavy)."""
    o = [sky(w, h, "#5A7AB8", "#FFE6A0") if full else sky(w, h, "#6A6A7A", "#C8B8A0")]
    if full:
        for i in range(3):
            x = w * (0.2 + i * 0.3)
            o.append(f'<rect x="{f(x - w * 0.08)}" y="{f(h * 0.04)}" width="{f(w * 0.16)}" height="{f(h * 0.12)}" fill="#FFF4C2" stroke="#E8B830" stroke-width="2"></rect>'
                     f'<path d="M{f(x - w * 0.08)} {f(h * 0.16)} L {f(x - w * 0.12)} {f(h * 0.6)} L {f(x + w * 0.12)} {f(h * 0.6)} L {f(x + w * 0.08)} {f(h * 0.16)} Z" fill="#FFF4C2" opacity="0.35"></path>')
        o.append(rain(w, h * 0.6, seed, n=40, color="#FFF4C2", op=0.6))
    o.append(ground(w, h, h * 0.62, "#B8A07A" if full else "#9A8A6A", dy=0))
    k = min(1.0, h / 300)
    for i in range(4):
        x = w * (0.08 + i * 0.13)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.7)}" width="{f(w * 0.11)}" height="{f(h * 0.24)}" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2"></rect>')
        if full: o.append(f'<path d="M{f(x - 4)} {f(h * 0.7)} C {f(x + w * 0.02)} {f(h * 0.6)} {f(x + w * 0.09)} {f(h * 0.6)} {f(x + w * 0.11 + 4)} {f(h * 0.7)} Z" fill="#E8C060" stroke="#0D0D0F" stroke-width="1.6"></path>')
    if full: o.append(vines(w * 0.64, w * 0.98, h * 0.8, h * 0.94, seed, rows=2))
    else: o.append(f'<path d="M{f(w * 0.7)} {f(h * 0.94)} L {f(w * 0.94)} {f(h * 0.94)}" stroke="#5A4A3A" stroke-width="3"></path>')
    return "".join(o)

def proud(w, h, seed):
    """It is vain to serve God; now we call the proud happy; they that work wickedness are built up: a proud new house with
    banners and lit windows on the hill, and below in the shade the plain house of the mourners."""
    o = [sky(w, h, "#2A1A3A", "#E8A06A"), hills(w, h, h * 0.5, seed, color="#5A3A4A", amp=12),
         walls(w * 0.46, w * 0.96, h * 0.5, h * 0.36, seed, color="#E8C890", lit=True, towers=3), ground(w, h, h * 0.56, "#6A4A3A", dy=0),
         f'<rect x="{f(w * 0.06)}" y="{f(h * 0.72)}" width="{f(w * 0.2)}" height="{f(h * 0.24)}" fill="#7A6A5A" stroke="#0D0D0F" stroke-width="2"></rect>'
         f'<rect x="{f(w * 0.13)}" y="{f(h * 0.82)}" width="{f(w * 0.05)}" height="{f(h * 0.14)}" fill="#2A1A10"></rect>']
    return "".join(o)

def remembrance(p, w, h, seed):
    """Then they that feared Jehovah spake one with another; and a book of remembrance was written before him: two and three
    together in a lamplit room speaking, and above them a glowing open book with its lines being written."""
    from genesis.art4 import clay_lamp
    b = h * 0.95
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1430"></rect>', halo(w * 0.5, h * 0.22, h * 0.3, "#FFE680", 0.6)]
    k = min(1.4, h / 260); x, y = w * 0.5, h * 0.24
    o.append(f'<path d="M{f(x)} {f(y + 40 * k)} L {f(x - 90 * k)} {f(y + 30 * k)} L {f(x - 90 * k)} {f(y - 40 * k)} L {f(x)} {f(y - 30 * k)} L {f(x + 90 * k)} {f(y - 40 * k)} L {f(x + 90 * k)} {f(y + 30 * k)} Z" fill="#F3E8C8" stroke="{"#E8B830"}" stroke-width="2.4"></path>'
             f'<path d="M{f(x)} {f(y - 30 * k)} L {f(x)} {f(y + 40 * k)}" stroke="#C8A878" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(x - 80 * k)} {f(y - 22 * k + j * 12 * k)} L {f(x - 10 * k)} {f(y - 16 * k + j * 12 * k)} M{f(x + 10 * k)} {f(y - 16 * k + j * 12 * k)} L {f(x + (80 - (j == 4) * 40) * k)} {f(y - 22 * k + j * 12 * k)}" stroke="#3A2A1A" stroke-width="2" stroke-dasharray="8 3"></path>' for j in range(5)))
    s = fit(b, h * 0.52)
    for i, (x, c, fl) in enumerate(((0.14, "#3A4A6A", False), (0.3, "#6A4A3A", True), (0.66, "#4A5A3A", False), (0.84, "#5A3A5A", True))):
        o.append((man if i != 3 else woman)(p, w * x, b, s, c, flip=fl, up=[(22, -158), (40, -150), (56, -146)] if i in (0, 2) else None))
    o.append(clay_lamp(w * 0.5, h * 0.9, min(0.9, h / 360)) + halo(w * 0.5, h * 0.84, h * 0.2, "#FFC14D", 0.4))
    return "".join(o)

def sun_wings(w, h, seed):
    """Unto you that fear my name shall the sun of righteousness arise with healing in its wings; ye shall go forth and
    gambol as calves of the stall: the sun rising over the hills, its rays spread wide on either side like wings, calves
    leaping in the field."""
    o = [sky(w, h, "#3A4A8A", "#FFD8A0"), halo(w * 0.5, h * 0.5, h * 0.6, "#FFF4C2", 0.6)]
    cx, cy = w * 0.5, h * 0.5
    for side in (-1, 1):
        for i in range(7):
            a = math.radians(-8 - i * 10); L = w * (0.44 - i * 0.03)
            o.append(f'<path d="M{f(cx + side * 30)} {f(cy)} Q {f(cx + side * L * 0.5 * math.cos(a))} {f(cy + L * 0.5 * math.sin(a) - 30)} {f(cx + side * L * math.cos(a))} {f(cy + L * math.sin(a))}" stroke="#FFE680" stroke-width="{f(10 - i)}" fill="none" stroke-linecap="round" opacity="0.8"></path>')
    o.append(sun(cx, cy, max(18, h * 0.08), color="#FFE680", op=0.4))
    o.append(hills(w, h, h * 0.62, seed, color="#6A8A4A", amp=12) + ground(w, h, h * 0.68, "#9CBB5E", dy=0))
    k = min(0.6, h / 500)
    for i, (x, rot) in enumerate(((0.24, -14), (0.44, 10), (0.7, -18))):
        o.append(f'<g transform="rotate({rot} {f(w * x)} {f(h * 0.92)})">{S1.calf(w * x, h * 0.92, k, flip=i == 1)}</g>')
    return "".join(o)

def horeb_law(w, h, seed):
    """Remember ye the law of Moses my servant, which I commanded unto him in Horeb for all Israel: Horeb in its cloud, and
    the two tables of stone before it."""
    o = [horeb(w, h, seed), V.tables(w * 0.5, h * 0.94, min(0.9, h / 320), uid=f"tb{seed}")]
    return "".join(o)

def elijah_comes(p, w, h, seed):
    """Behold, I will send you Elijah the prophet; he shall turn the heart of the fathers to the children, and the heart of
    the children to their fathers: Elijah in his hairy mantle on the road at dawn, and before a house a father and his son
    turned toward one another (all at the left, clear of the end mark)."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), sky(w, h, "#3A3A6A", "#FFC890"), sun(w * 0.8, h * 0.3, max(14, h * 0.06), color="#FFE680", op=0.4),
         hills(w, h, h * 0.5, seed, color="#6A5A6A", amp=14), ground(w, h, h * 0.54, "#B8986A", dy=0),
         f'<path d="M{f(w + 10)} {f(h * 0.56)} C {f(w * 0.7)} {f(h * 0.6)} {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.08)} {f(h + 10)} L {f(w * 0.24)} {f(h + 10)} C {f(w * 0.4)} {f(h * 0.82)} {f(w * 0.72)} {f(h * 0.62)} {f(w + 10)} {f(h * 0.6)} Z" fill="#D8C090" stroke="#0D0D0F" stroke-width="1.4"></path>',
         f'<rect x="{f(w * 0.14)}" y="{f(h * 0.3)}" width="{f(w * 0.2)}" height="{f(h * 0.5)}" fill="#C8B090" stroke="#0D0D0F" stroke-width="2"></rect>'
         f'<rect x="{f(w * 0.21)}" y="{f(h * 0.54)}" width="{f(w * 0.06)}" height="{f(h * 0.26)}" fill="#2A1A10"></rect>']
    s = fit(b, h * 0.36)
    o.append(elijah_fig(p, w * 0.06, b, s))
    o.append(man(p, w * 0.17, h * 0.84, fit(h * 0.84, h * 0.4), "#3A4A6A", up=[(22, -158), (40, -150), (56, -140)])
             + man(p, w * 0.27, h * 0.84, fit(h * 0.84, h * 0.4) * 0.62, "#B5652E", flip=True, up=[(22, -158), (40, -150), (56, -140)]))
    return "".join(o)
