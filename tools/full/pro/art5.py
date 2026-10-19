"""Drawings for Proverbs 30–31 (chapter 11 of the volume): Agur's numbered sayings as numbered roundels on the blueprint
grid, the ravens over the valley (nothing more drawn), king Lemuel and his mother, and the worthy woman's household — wool
and flax, the merchant-ships, the lamp by night, the field and the vineyard, the distaff and the spindle, the household in
scarlet in the snow, her husband among the elders at the gate, her children rising up to call her blessed."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from pro.art4 import *
from pro.art4 import f, K2, K1, EM, INK, SON_C, glow, son_fig, emb_art, numbered, SEVEN_SIGNS, runner_fig
import judges2 as J2, exodus2 as E2, numbers1 as N, samuel1 as S1
from chr2.art import judges_gate
from genesis.art2 import bird
import samuel3 as S3

WORTHY_C, HUSBAND_C = "#2C6A7A", "#F3EFE6"

def worthy_fig(p, x, y, s, flip=False, up=None, cloth=WORTHY_C):
    """The worthy woman at a distance: a teal robe and headscarf."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind="Robe", woman=True, hair="#2A1A10", sw=3, flip=flip, up=up,
                     extra=A.headcloth(cloth, cord=None))

def husband_fig(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#3A4A6A", kind="Robe", sw=3, flip=flip, up=up, extra=A.headcloth(HUSBAND_C) + A.BLACK_BEARD)

# ---- signs for the numbered sayings (in a 60 x 60 box centred on 0, 0) ------------------------------------------------------
def _ico(svg_fn, k=0.19):
    """An emblem (320 x 120) shrunk into a roundel."""
    return f'<g transform="scale({k}) translate(-160 -70)"><clipPath id="{svg_fn[1]}c"><circle cx="160" cy="70" r="150"></circle></clipPath><g clip-path="url(#{svg_fn[1]}c)">{EM.EMB[svg_fn[0]](svg_fn[1])}</g></g>'

S = {
    "eye": SEVEN_SIGNS[0], "hands": SEVEN_SIGNS[2], "pair": SEVEN_SIGNS[6],
    "teeth": '<path d="M-22 -6 C -14 -18 14 -18 22 -6 L 22 2 C 14 14 -14 14 -22 2 Z" fill="#5A1A2A" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<path d="M{x} -10 L {x + 2} 0 L {x + 4} -10 Z" fill="#E8ECF8" stroke="#0D0D0F" stroke-width="0.8"></path>' for x in range(-16, 16, 6))
             + '<path d="M-24 18 L 22 -24" stroke="#C8C8D0" stroke-width="3"></path>',
    "grave": '<path d="M-24 14 C -24 -16 24 -16 24 14 Z" fill="#05050A" stroke="#8A8478" stroke-width="3"></path><path d="M-28 16 L 28 16" stroke="#5A4A3A" stroke-width="4"></path>',
    "cradle": '<path d="M-22 -2 C -20 16 20 16 22 -2 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path><path d="M-24 18 C -10 24 10 24 24 18" fill="none" stroke="#5A3A22" stroke-width="3"></path>',
    "earth": '<path d="M-26 6 L 26 6 L 26 18 L -26 18 Z" fill="#B8864A" stroke="#0D0D0F" stroke-width="2"></path><path d="M-14 6 l 4 6 l -3 6 M8 6 l -3 5 l 4 7" fill="none" stroke="#5A3A22" stroke-width="1.6"></path><path d="M0 -20 c 4 7 4 11 0 13 c -4 -2 -4 -6 0 -13 Z" fill="#8FD0E2" stroke="#2C7DA0" stroke-width="1.2"></path>',
    "fire": '<path d="M-14 14 C -22 0 -8 -6 -6 -22 C 2 -12 4 -18 8 -26 C 14 -10 24 -2 14 14 Z" fill="#FF6A2A" stroke="#0D0D0F" stroke-width="2"></path><path d="M-6 12 C -10 4 -2 0 0 -8 C 4 0 10 4 6 12 Z" fill="#FFE680"></path>',
    "crown_servant": '<path d="M-14 -14 L -14 -24 L -7 -18 L 0 -28 L 7 -18 L 14 -24 L 14 -14 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path><circle cx="0" cy="-4" r="8" fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.6"></circle><path d="M-14 22 C -14 4 14 4 14 22 Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.6"></path>',
    "bowl": '<path d="M-24 -4 C -22 18 22 18 24 -4 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path><path d="M-20 -6 C -10 -16 10 -16 20 -6 Z" fill="#C8862E" stroke="#0D0D0F" stroke-width="1.4"></path>',
    "ring": '<circle cx="0" cy="2" r="14" fill="none" stroke="#0D0D0F" stroke-width="7"></circle><circle cx="0" cy="2" r="14" fill="none" stroke="#E8B830" stroke-width="4"></circle><path d="M-6 -16 L 0 -24 L 6 -16 Z" fill="#B5121B" stroke="#0D0D0F" stroke-width="1"></path>',
    "key": '<circle cx="-12" cy="0" r="9" fill="none" stroke="#0D0D0F" stroke-width="6"></circle><circle cx="-12" cy="0" r="9" fill="none" stroke="#C8962E" stroke-width="3.4"></circle><path d="M-3 0 L 24 0 M16 0 L 16 8 M22 0 L 22 6" stroke="#C8962E" stroke-width="4"></path>',
    "eagle": '<path d="M0 0 C -10 -6 -24 -14 -28 -8 C -22 -6 -18 -2 -16 2 C -8 2 -4 4 0 6 C 4 4 8 2 16 2 C 18 -2 22 -6 28 -8 C 24 -14 10 -6 0 0 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.6"></path><circle cx="0" cy="-4" r="4" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1"></circle>',
    "serpent": '<path d="M-26 14 L 26 14 L 18 4 L -18 4 Z" fill="#8A6A5A" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M-20 2 C -12 -10 -4 8 4 -4 C 10 -14 16 -8 20 -14" fill="none" stroke="#0D0D0F" stroke-width="6" stroke-linecap="round"></path><path d="M-20 2 C -12 -10 -4 8 4 -4 C 10 -14 16 -8 20 -14" fill="none" stroke="#6A8A3A" stroke-width="3.6" stroke-linecap="round"></path>',
    "ship": '<path d="M-22 6 C -14 16 14 16 24 4 L -24 4 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M0 4 L 0 -24" stroke="#3A2214" stroke-width="2.4"></path><path d="M-12 -22 L 12 -22 L 10 -4 L -10 -4 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.4"></path><path d="M-28 18 q 7 -4 14 0 q 7 4 14 0 q 7 -4 14 0 q 7 4 14 0" fill="none" stroke="#8FD0E2" stroke-width="2"></path>',
    "maiden": '<circle cx="-9" cy="-14" r="6" fill="#C98E66" stroke="#0D0D0F" stroke-width="1.4"></circle><path d="M-17 20 L -17 -4 C -17 -9 -1 -9 -1 -4 L -1 20 Z" fill="#3A4A6A" stroke="#0D0D0F" stroke-width="1.4"></path><circle cx="9" cy="-12" r="5.6" fill="#C98E66" stroke="#0D0D0F" stroke-width="1.4"></circle><path d="M1 20 L 3 -2 C 3 -7 15 -7 15 -2 L 17 20 Z" fill="#C2456A" stroke="#0D0D0F" stroke-width="1.4"></path>',
    "ant": '<g transform="scale(0.9) translate(4 6)"><ellipse cx="-16" cy="-4" rx="10" ry="7" fill="#3A1A10" stroke="#0D0D0F" stroke-width="1.4"></ellipse><ellipse cx="0" cy="-4" rx="6" ry="4" fill="#3A1A10" stroke="#0D0D0F" stroke-width="1.4"></ellipse><circle cx="12" cy="-6" r="6" fill="#3A1A10" stroke="#0D0D0F" stroke-width="1.4"></circle><path d="M-10 0 L -18 10 M0 0 L 0 10 M8 0 L 16 10 M16 -12 C 20 -20 26 -20 28 -16" fill="none" stroke="#0D0D0F" stroke-width="1.8"></path><ellipse cx="22" cy="0" rx="5" ry="3" fill="#E8C060" stroke="#0D0D0F" stroke-width="1"></ellipse></g>',
    "coney": '<path d="M-26 18 L -12 -2 L 4 -6 L 26 18 Z" fill="#8A6A5A" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M-10 -2 C -14 -14 -2 -20 10 -18 C 18 -16 22 -10 20 -2 Z" fill="#9A7A5A" stroke="#0D0D0F" stroke-width="1.6"></path><circle cx="14" cy="-12" r="1.8" fill="#0D0D0F"></circle>',
    "locust": '<g transform="translate(-4 4)"><path d="M-18 0 C -10 -6 10 -6 20 -2 C 10 4 -10 4 -18 0 Z" fill="#8A7A2A" stroke="#0D0D0F" stroke-width="1.4"></path><path d="M-8 -2 C 0 -16 14 -16 22 -10 C 12 -6 2 -4 -8 -2 Z" fill="#C8B870" stroke="#0D0D0F" stroke-width="1.2"></path><path d="M14 2 L 22 12 L 26 10 M6 2 L 0 12" fill="none" stroke="#0D0D0F" stroke-width="1.6"></path><circle cx="18" cy="-2" r="1.6" fill="#0D0D0F"></circle></g>',
    "lizard": '<g transform="rotate(-30)"><path d="M-26 0 C -16 -3 -6 -3 4 -4 C 14 -5 20 -4 24 -2 C 26 0 24 2 20 2 C 14 4 4 4 -6 3 C -14 3 -20 2 -26 0 Z" fill="#6A7A4A" stroke="#0D0D0F" stroke-width="1.4"></path><path d="M-4 -3 L -8 -12 M-4 3 L -8 12 M12 -4 L 16 -12 M12 3 L 16 12" stroke="#0D0D0F" stroke-width="2"></path></g>',
    "lion": '<circle cx="4" cy="-6" r="16" fill="#8A4A16" stroke="#0D0D0F" stroke-width="1.6"></circle><circle cx="6" cy="-6" r="10" fill="#D9964A" stroke="#0D0D0F" stroke-width="1.6"></circle><circle cx="10" cy="-9" r="1.6" fill="#0D0D0F"></circle><path d="M-12 4 L -26 18 L 24 18 L 12 6 Z" fill="#C8862E" stroke="#0D0D0F" stroke-width="1.6"></path>',
    "greyhound": '<path d="M-24 4 C -16 -4 10 -4 16 -2 L 22 -14 L 28 -10 L 26 -4 L 20 2 L 18 18 L 14 18 L 12 4 C 0 6 -10 6 -16 4 L -18 18 L -22 18 Z" fill="#B8A89A" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M-24 4 C -28 0 -30 -6 -26 -10" fill="none" stroke="#0D0D0F" stroke-width="1.6"></path>',
    "goat": '<path d="M-20 0 C -18 -10 8 -10 12 -6 L 16 -16 C 20 -20 26 -18 24 -12 L 20 -2 L 16 18 L 12 18 L 10 2 L -12 2 L -14 18 L -18 18 Z" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M18 -16 C 14 -26 6 -28 2 -24" fill="none" stroke="#C8B890" stroke-width="3"></path><path d="M22 -10 L 24 -2" stroke="#0D0D0F" stroke-width="2"></path>',
    "king": '<path d="M-12 -12 L -12 -22 L -6 -16 L 0 -26 L 6 -16 L 12 -22 L 12 -12 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path><circle cx="0" cy="-2" r="8" fill="#C98E66" stroke="#0D0D0F" stroke-width="1.4"></circle><path d="M-16 22 C -16 6 16 6 16 22 Z" fill="#7A2A4A" stroke="#0D0D0F" stroke-width="1.6"></path>',
}

def signs(*names): return [S[n] for n in names]

def generations(w, h, seed):
    """There is a generation ...: four signs — them that curse their father, the unwashed, the lofty eyes, the teeth as swords."""
    return numbered(w, h, signs("pair", "hands", "eye", "teeth"), red_last=False)

def never_satisfied(w, h, seed):
    """Four that say not, Enough: Sheol, the barren womb, the earth not satisfied with water, the fire."""
    return numbered(w, h, signs("grave", "cradle", "earth", "fire"))

def wonderful(w, h, seed):
    """Four too wonderful: the way of an eagle in the air, a serpent upon a rock, a ship in the sea, a man with a maiden."""
    return numbered(w, h, signs("eagle", "serpent", "ship", "maiden"), bg="#0B1A2E", line="#1E3A5A")

def trembles(w, h, seed):
    """For four the earth cannot bear: a servant when he is king, a fool filled with food, an odious woman married, a handmaid
    heir to her mistress."""
    return numbered(w, h, signs("crown_servant", "bowl", "ring", "key"))

def little_wise(w, h, seed):
    """Four things little upon the earth, but exceeding wise: the ants, the conies, the locusts, the lizard."""
    return numbered(w, h, signs("ant", "coney", "locust", "lizard"), red_last=False, bg="#1A2A1A", line="#2A4A2A")

def stately(w, h, seed):
    """Four stately in going: the lion, the greyhound, the he-goat, and the king."""
    return numbered(w, h, signs("lion", "greyhound", "goat", "king"))

def ravens(w, h, seed):
    """The ravens of the valley: dark birds circling over a deep valley at dusk (nothing more is drawn)."""
    r = random.Random(seed)
    o = [sky(w, h, "#2A1A2A", "#C8603A"), f'<path d="M-10 {f(h * 0.3)} L {f(w * 0.36)} {f(h * 0.6)} L {f(w * 0.5)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A2A2A" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w + 10)} {f(h * 0.26)} L {f(w * 0.64)} {f(h * 0.6)} L {f(w * 0.5)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} Z" fill="#2A1E22" stroke="{INK}" stroke-width="2"></path>']
    for i in range(7):
        a = i * 2 * math.pi / 7
        o.append(bird(w * 0.5 + math.cos(a) * w * 0.16, h * 0.36 + math.sin(a) * h * 0.12, min(2.6, h / 120) * r.uniform(0.8, 1.2)))
    return "".join(o)

def lemuel(p, w, h, seed):
    """The words of king Lemuel, the oracle which his mother taught him: the young king seated, his mother standing over him."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A1A2A"></rect>',
         "".join(f'<rect x="{f(x)}" y="-10" width="{f(w / 14 - 4)}" height="{f(h + 20)}" fill="#4A2234"></rect>' for x in [i * w / 14 for i in range(15)]),
         ground(w, h, b, "#2A1018", dy=0), glow(w * 0.5, b - h * 0.3, h * 0.5, "#FFC14D", 0.25)]
    s = min(fit(b, h * 0.24), 1.2)
    o.append(S3.throne(w * 0.38, b, s * 0.9))
    o.append(K1.king_fig(p, w * 0.38, b - 30 * s, s * 0.82, cloth="#3A1A4A"))
    o.append(mk.person(p, round(w * 0.6), round(b), round(s, 3), body=SKIN, cloth="#5A2470", kind="Robe", woman=True, hair="#8A847A", sw=3, flip=True,
                       up=[(-22, -158), (-44, -150), (-64, -164)], extra=A.headcloth("#5A2470", cord="#E8B830")))
    return "".join(o)

def worthy_home(p, w, h, seed):
    """A worthy woman who can find? Her husband trusteth in her: the house with its door open and lamp lit, the woman and her
    husband before it."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFE3B8"), hills(w, h, h * 0.5, seed, "#8A9A6A", amp=8, step=80), ground(w, h, h * 0.6, "#C8A06A", dy=0)]
    s = min(fit(b, h * 0.3), 1.1)
    o.append(EM.house(w * 0.68, b, min(w * 0.44, 300 * s), min(h * 0.56, 200 * s), lit=True))
    o.append(husband_fig(p, w * 0.3, b, s, up=[(-22, -158), (2, -140), (26, -146)]) + worthy_fig(p, w * 0.42, b, s * 0.92, flip=True))
    return "".join(o)

def wool_ships(p, w, h, seed):
    """She seeketh wool and flax; she is like the merchant-ships; she riseth while it is yet night: the woman with a basket of
    wool by the flax, the ships on the sea beyond, the morning star."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#1E1650", "#C8603A"), mk.stars(20, w, h * 0.3, seed), f'<rect x="-10" y="{f(h * 0.46)}" width="{f(w + 20)}" height="{f(h)}" fill="#1F4A6A"></rect>',
         K1.ship(w * 0.66, h * 0.5, min(0.7, h / 500)), K1.ship(w * 0.86, h * 0.5, min(0.5, h / 700)),
         f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.56)} {f(w * 0.5)} {f(h * 0.6)} {f(w * 0.56)} {f(h * 0.7)} L {f(w * 0.6)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B89A6A" stroke="{INK}" stroke-width="2"></path>']
    s = min(fit(b, h * 0.34), 1.0)
    for i in range(8):
        x = w * (0.04 + i * 0.03)
        o.append(f'<path d="M{f(x)} {f(b)} L {f(x + 2)} {f(b - 70 * s)}" stroke="#7A8A4A" stroke-width="2"></path><circle cx="{f(x + 2)}" cy="{f(b - 72 * s)}" r="{f(4 * s)}" fill="#6A8AC8"></circle>')
    o.append(worthy_fig(p, w * 0.36, b, s, up=[(-22, -158), (-40, -126), (-58, -118)]))
    o.append(f'<path d="M{f(w * 0.36 - 76 * s)} {f(b - 120 * s)} C {f(w * 0.36 - 80 * s)} {f(b - 96 * s)} {f(w * 0.36 - 40 * s)} {f(b - 96 * s)} {f(w * 0.36 - 44 * s)} {f(b - 120 * s)} Z" fill="#8A6A3A" stroke="{INK}" stroke-width="1.6"></path>'
             + "".join(f'<circle cx="{f(w * 0.36 - (70 - i * 8) * s)}" cy="{f(b - 124 * s)}" r="{f(6 * s)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1"></circle>' for i in range(4)))
    return "".join(o)

def vineyard_plant(p, w, h, seed):
    """She considereth a field, and buyeth it; with the fruit of her hands she planteth a vineyard: young vines in rows on a
    hillside, the woman planting, a field beyond."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#E8F6FA"), hills(w, h, h * 0.42, seed, "#6A9A4A", amp=10, step=80), R.field(-10, w + 10, h * 0.5, h * 0.1, seed, rows=2),
         ground(w, h, h * 0.58, "#8A6A4A", dy=0)]
    s = min(fit(b, h * 0.34), 1.0)
    for row in range(2):
        for i in range(7):
            x = w * (0.4 + i * 0.09) - row * 20; y = h * (0.7 + row * 0.12)
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 40 * s)} M{f(x - 14 * s)} {f(y - 30 * s)} L {f(x + 14 * s)} {f(y - 30 * s)}" stroke="#5A3A22" stroke-width="3"></path>'
                     f'<path d="M{f(x - 14 * s)} {f(y - 30 * s)} C {f(x - 4 * s)} {f(y - 40 * s)} {f(x + 4 * s)} {f(y - 22 * s)} {f(x + 14 * s)} {f(y - 30 * s)}" fill="none" stroke="#2E6B3A" stroke-width="4"></path>')
    o.append(E.kneel(w * 0.22, b, s * 0.9, color=WORTHY_C))
    return "".join(o)

def lamp_distaff(p, w, h, seed):
    """Her lamp goeth not out by night; she layeth her hands to the distaff: the woman at her spinning by the lamp, the
    night at the window."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A14"></rect>',
         f'<rect x="{f(w * 0.66)}" y="{f(h * 0.14)}" width="{f(min(w * 0.24, h * 0.5))}" height="{f(h * 0.36)}" fill="#0B0B2A" stroke="{INK}" stroke-width="3"></rect>',
         f'<g transform="translate({f(w * 0.66)} {f(h * 0.14)})">{mk.stars(10, min(w * 0.24, h * 0.5), h * 0.36, seed)}</g>', ground(w, h, b, "#1A100C", dy=0)]
    s = min(fit(b, h * 0.3), 1.0)
    o.append(glow(w * 0.4, b - 100 * s, 200 * s, "#FFC14D", 0.35))
    o.append(E.kneel(w * 0.3, b, s, color=WORTHY_C))
    x = w * 0.3 + 60 * s
    o.append(f'<path d="M{f(x)} {f(b)} L {f(x)} {f(b - 150 * s)}" stroke="#C8862E" stroke-width="{f(5 * s)}"></path><ellipse cx="{f(x)}" cy="{f(b - 150 * s)}" rx="{f(14 * s)}" ry="{f(12 * s)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></ellipse>'
             f'<path d="M{f(x + 10 * s)} {f(b - 144 * s)} C {f(x + 40 * s)} {f(b - 120 * s)} {f(x + 50 * s)} {f(b - 100 * s)} {f(x + 54 * s)} {f(b - 70 * s)}" fill="none" stroke="#F3EFE6" stroke-width="1.6"></path>'
             f'<path d="M{f(x + 54 * s)} {f(b - 80 * s)} L {f(x + 54 * s)} {f(b - 30 * s)}" stroke="#8A5A30" stroke-width="3"></path><ellipse cx="{f(x + 54 * s)}" cy="{f(b - 36 * s)}" rx="{f(10 * s)}" ry="{f(4 * s)}" fill="#5A3A22" stroke="{INK}" stroke-width="1.2"></ellipse>')
    o.append(EM.lamp_shape(w * 0.56, b - 4, 0.6 * s))
    return "".join(o)

def snow_scarlet(p, w, h, seed):
    """She is not afraid of the snow for her household; for all her household are clothed with scarlet: snow falling on the
    house, her children in scarlet at the door; she stretcheth out her hand to the poor."""
    b = h * 0.9
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), sky(w, h, "#8A9AB8", "#C8D6E8"), ground(w, h, h * 0.66, "#E8ECF8", dy=0)]
    s = min(fit(b, h * 0.3), 1.0)
    o.append(EM.house(w * 0.66, b, min(w * 0.4, 280 * s), min(h * 0.5, 190 * s), lit=True))
    for i, x in enumerate((0.44, 0.5, 0.56)):
        o.append(man(p, w * x, b, s * (0.6 - i * 0.06), "#B5121B"))
    o.append(worthy_fig(p, w * 0.32, b, s, flip=True, up=[(-22, -158), (-46, -136), (-70, -132)]))
    o.append(E.kneel(w * 0.14, b, s * 0.8, color="#6A6058"))
    o.append("".join(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(0, b))}" r="{f(r.uniform(1.6, 3.4))}" fill="#F3EFE6"></circle>' for _ in range(90)))
    return "".join(o)

def gate_husband(p, w, h, seed):
    """Her husband is known in the gates, when he sitteth among the elders of the land; she delivereth girdles unto the
    merchant: the elders at the gate, a merchant with his laden ass."""
    b = h * 0.92
    o = [judges_gate(p, w, h, seed)]
    s = fit(b, max(h * 0.44, b - 220))
    o.append(E.kneel(w * 0.42, b, s * 0.7, color="#3A4A6A"))
    o.append(N.ass(w * 0.1, b, s * 0.7) + man(p, w * 0.2, b, s * 0.9, "#7A5A3A"))
    return "".join(o)

def blessed(p, w, h, seed):
    """Her children rise up, and call her blessed; her husband also: the family before the house at evening, the woman in the
    middle, light about them."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A6A", "#FFC14D"), sun(w * 0.8, h * 0.5, min(40, h * 0.1), color="#FFE680", op=0.4), hills(w, h, h * 0.58, seed, "#6A5A4A", amp=8, step=80),
         ground(w, h, h * 0.66, "#B89A6A", dy=0)]
    s = min(fit(b, h * 0.3), 0.9)
    o.append(EM.house(w * 0.82, b, min(w * 0.3, 220 * s), min(h * 0.44, 160 * s), lit=True))
    o.append(glow(w * 0.42, b - 110 * s, 150 * s, "#FFE680", 0.35))
    o.append(husband_fig(p, w * 0.26, b, s, up=[(-22, -158), (2, -140), (26, -150)]))
    o.append(worthy_fig(p, w * 0.42, b, s * 0.94))
    for i, (x, c) in enumerate(((0.54, "#B5121B"), (0.6, "#B5121B"), (0.66, "#B5121B"))):
        o.append((man if i != 1 else woman)(p, w * x, b, s * (0.72 - i * 0.06), c, flip=True))
    return "".join(o)
