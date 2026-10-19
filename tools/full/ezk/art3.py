"""Drawings for Ezekiel 8–11: the elders in Ezekiel's house, the visions of God in Jerusalem — the image of jealousy at the
north gate, the hole in the wall and the chamber of imagery, the women weeping for Tammuz, the five and twenty men with
their faces toward the east — the six men and the man in linen with the inkhorn, the coals scattered from between the
cherubim, the glory over the threshold and at the east gate, the caldron, the heart of stone and the heart of flesh, and
the glory going up to the mountain east of the city. Restraint: 9:5–7 is words over the empty court; Pelatiah's death is
words only. The man in linen and the six men are figures at a distance; the glory is light, never a figure."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art2 import *
from ezk.art2 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2

LINEN = "#F3EFE6"

def court(p, w, h, seed, sky=("#5A6A8A", "#E8D8B8"), gate=True, temple=True, altar=False, night=False):
    """The courts of the house of Jehovah in the vision: the stone pavement, the inner wall, a gate, the house behind."""
    o = [mk.defs(p, *ALL), bg(f"ct{seed}", w, h, [(0, sky[0]), (1, sky[1])])]
    if night: o.append(mk.stars(30, w, h * 0.4, seed))
    if temple: o.append(K1.temple_front(w * 0.7, h * 0.62, w * 0.36, seed))
    o.append(f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    if gate: o.append(S4.gatehouse(w * 0.2, h * 0.68, w * 0.3, h * 0.36))
    o.append(f'<path d="M-10 {f(h * 0.68)} L {f(w + 10)} {f(h * 0.68)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B8A888" stroke="{INK}" stroke-width="2"></path>')
    for i in range(1, 6):
        y = h * 0.68 + (h * 0.32) * (i / 6) ** 1.4
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#9A8A6A" stroke-width="1.2"></path>')
    if altar: o.append(K1.horned_altar(w * 0.52, h * 0.86, min(0.8, h / 380), fire=True, seed=seed))
    return "".join(o)

def man_linen(p, x, y, s, flip=False, up=None):
    """The man clothed in linen with a writer's inkhorn by his side (at a distance, white, no face detail)."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=LINEN, sw=3, flip=flip, up=up,
                     extra=A.headcloth(LINEN, cord=None) + '<rect x="10" y="-108" width="8" height="18" fill="#3A2A1A" stroke="#0D0D0F" stroke-width="1.4"></rect><path d="M18 -106 L 26 -126" stroke="#8A6A3A" stroke-width="2"></path>')

def elders_house(p, w, h, seed):
    """As I sat in my house, and the elders of Judah sat before me: a lamp-lit room, Ezekiel seated, the elders seated
    before him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bg(f"eh{seed}", w, h, [(0, "#3A2A2A"), (1, "#8A6A4A")]), f'<rect x="-10" y="{f(h * 0.72)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#6A5040" stroke="{INK}" stroke-width="2"></rect>',
         glow(f"el{seed}", w * 0.5, h * 0.4, w * 0.3, h * 0.4, "#FFC14D", 0.5), A.clay_lamp(w * 0.5, h * 0.42, min(1.2, h / 300)) if hasattr(A, "clay_lamp") else ""]
    s = min(fit(b, max(h * 0.44, b - 220)) * 0.7, 1.0)
    o.append(seated(w * 0.18, b, s * 1.05, EZ_C, head="#F3EFE6", beard="#4A4640"))
    for i in range(5):
        o.append(seated(w * (0.42 + i * 0.12), b, s, CAPT[i], head=CAPT[(i + 3) % 7], beard="#C8C2B6" if i % 2 else "#8A847A", flip=True))
    return "".join(o)

def lifted(p, w, h, seed):
    """The Spirit lifted me up between earth and heaven, and brought me in the visions of God to Jerusalem: Ezekiel borne
    high over the land in a rushing wind, the city far off, a likeness of fire and amber light above (no figure)."""
    o = [bg(f"lf{seed}", w, h, [(0, "#1A1A3A"), (0.6, "#6A4A6A"), (1, "#C8A080")]), hills(w, h, h * 0.8, seed, "#5A4A4A", amp=8, step=90),
         J.city_hill(w * 0.82, h * 0.86, w * 0.16, h * 0.14, seed)]
    o.append(glory(f"lg{seed}", w * 0.2, h * 0.7, w * 0.08, h * 0.6, seed))
    o.append(wind_lines(w, h, seed, n=10, color="#E8E0F0", op=0.5, y0=0.2, y1=0.7))
    s = min(1.0, h / 360)
    o.append(f'<g transform="translate({f(w * 0.5)} {f(h * 0.5)}) rotate(-70)">' + mk.person(p, 0, 0, round(s * 0.7, 3), body=SKIN, cloth=EZ_C, sw=3, extra=A.headcloth("#F3EFE6", cord="#1F5FAD") + GB_BEARD) + '</g>')
    return mk.defs(p, *ALL) + "".join(o)

def jealousy(p, w, h, seed):
    """The seat of the image of jealousy in the entry northward of the gate of the altar: a gilded idol on a high seat in
    the gateway; Ezekiel looking; the glory of the God of Israel as light over the court."""
    o = [court(p, w, h, seed, sky=("#4A3A5A", "#E8C8A0"), temple=True)]
    o.append(glory(f"jg{seed}", w * 0.72, h * 0.5, w * 0.12, h * 0.4, seed))
    k = min(1.6, h / 260)
    o.append(f'<rect x="{f(w * 0.2 - 26 * k)}" y="{f(h * 0.68 - 30 * k)}" width="{f(52 * k)}" height="{f(30 * k)}" fill="#6A5A4A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(idol(w * 0.2, h * 0.68 - 30 * k, k * 1.3, color="#E8B830"))
    o.append(ezek_fig(p, w * 0.46, h * 0.96, min(fit(h * 0.96, h * 0.5), 1.0), flip=True))
    return "".join(o)

def hole_wall(p, w, h, seed, door=False):
    """The door of the court, and a hole in the wall; dig now in the wall: Ezekiel digging, and behold, a door."""
    o = [mk.defs(p, *ALL), bg(f"hw{seed}", w, h, [(0, "#2A2A3A"), (1, "#6A5A5A")])]
    o.append(f'<rect x="-10" y="{f(h * 0.08)}" width="{f(w + 20)}" height="{f(h * 0.82)}" fill="#A8946A" stroke="{INK}" stroke-width="2"></rect>')
    r = random.Random(seed)
    for row in range(10):
        y = h * 0.08 + row * h * 0.082
        off = 0 if row % 2 else 30
        for c in range(int(w / 60) + 2):
            o.append(f'<rect x="{f(c * 60 - off)}" y="{f(y)}" width="60" height="{f(h * 0.082)}" fill="none" stroke="#7A6A4A" stroke-width="1.2"></rect>')
    hx, hy = w * 0.6, h * 0.62
    if door:
        o.append(P(f"M{f(hx - w * 0.07)} {f(h * 0.9)} L {f(hx - w * 0.07)} {f(h * 0.46)} L {f(hx + w * 0.07)} {f(h * 0.46)} L {f(hx + w * 0.07)} {f(h * 0.9)} Z", "#1A1010", 2.4))
        o.append(glow(f"hd{seed}", hx, h * 0.7, w * 0.06, h * 0.2, "#FF8A3D", 0.5))
        for i in range(8):
            o.append(f'<path d="M{f(hx + w * 0.1 + r.uniform(-20, 40))} {f(h * 0.9)} l {f(r.uniform(-8, 8))} -6" stroke="#5A4A3A" stroke-width="5" stroke-linecap="round"></path>')
    else:
        o.append(f'<ellipse cx="{f(hx)}" cy="{f(hy)}" rx="{f(w * 0.03)}" ry="{f(h * 0.05)}" fill="#1A1010" stroke="{INK}" stroke-width="2"></ellipse>')
    s = min(fit(h * 0.96, h * 0.42), 1.1)
    o.append(ezek_fig(p, w * 0.3, h * 0.96, s, up=[(-22, -158), (10, -150), (40, -140)] if door else None))
    o.append(f'<path d="M{f(w * 0.3 + 40 * s)} {f(h * 0.96 - 140 * s)} L {f(w * 0.3 + 70 * s)} {f(h * 0.96 - 80 * s)}" stroke="#5A3A1A" stroke-width="4"></path>' if door else "")
    o.append(ground(w, h, h * 0.9, "#6A5A4A", dy=0))
    return "".join(o)

BEASTS = ["M-20 0 C -24 -10 -10 -16 0 -14 C 12 -12 20 -6 24 -10 L 28 -4 L 22 0 Z", "M-24 -2 C -20 -12 20 -12 24 -2 L 30 -8 L 30 4 L 24 0 C 20 6 -20 6 -24 -2 Z",
          "M-18 0 L -14 -14 L 10 -16 L 18 -24 L 20 -10 L 14 0 Z", "M-26 0 C -16 -6 -6 6 4 0 C 12 -6 20 4 26 -2"]
def imagery(p, w, h, seed):
    """The chamber of imagery: every form of creeping things and abominable beasts and idols portrayed upon the wall round
    about; the seventy elders with censers, Jaazaniah in the midst; the cloud of incense going up (in the dark)."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), bg(f"im{seed}", w, h, [(0, "#1A1010"), (1, "#3A2A2A")])]
    o.append(f'<rect x="-10" y="{f(h * 0.04)}" width="{f(w + 20)}" height="{f(h * 0.7)}" fill="#4A3A2A" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(int(w / 70) * 2):
        x = r.uniform(20, w - 20); y = h * r.uniform(0.1, 0.5); d = r.choice(BEASTS); k = r.uniform(1.0, 1.8) * min(1.4, h / 300)
        o.append(f'<path transform="translate({f(x)} {f(y)}) scale({f(k)})" d="{d}" fill="{"none" if d == BEASTS[3] else "#8A3A2A"}" stroke="#D8A060" stroke-width="2"></path>')
    for i in range(3): o.append(idol(w * (0.2 + i * 0.3), h * 0.66, min(1.4, h / 260), color="#C8A040"))
    o.append(glow(f"ig{seed}", w * 0.5, h * 0.6, w * 0.4, h * 0.3, "#FF8A3D", 0.35))
    o.append(f'<rect x="-10" y="{f(h * 0.74)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#2A1E1A" stroke="{INK}" stroke-width="2"></rect>')
    b = h * 0.98; s = min(fit(b, max(h * 0.5, b - 180)), 0.9)
    for i in range(9):
        x = w * (0.06 + i * 0.11)
        o.append(mk.person(p, round(x), round(b - (i % 2) * 6), round(s * (0.9 + 0.1 * (i == 4)), 3), body=SKIN, cloth=CAPT[i % 7], sw=2.6, flip=i > 4,
                           extra=A.headcloth(CAPT[(i + 2) % 7]) + A.WHITE_BEARD.replace("#E8E2D6", "#B8B2A6")))
        o.append(smoke(x + (14 if i <= 4 else -14) * s, b - 120 * s, 5, seed + i, color="#C8B8A8", op=0.35, k=s * 0.6))
    return "".join(o)

def tammuz(p, w, h, seed):
    """The door of the gate of Jehovah's house toward the north, and there sat the women weeping for Tammuz."""
    b = h * 0.95
    o = [court(p, w, h, seed, sky=("#5A4A6A", "#D8B8A0"), temple=False)]
    o.append(S4.gatehouse(w * 0.62, h * 0.7, w * 0.5, h * 0.5))
    s = min(fit(b, max(h * 0.5, b - 200)), 1.0)
    for i in range(6):
        x = w * (0.08 + i * 0.15)
        o.append(f'<g transform="translate({f(x)} {f(b)}) scale({f(s * 0.8)})">' + P("M-36 0 C -40 -40 -26 -80 -6 -94 C 6 -100 18 -94 22 -82 C 30 -60 40 -30 44 0 Z", ["#5A3A5A", "#3A3A5A", "#6A4A3A", "#4A3A4A"][i % 4], 2.4)
                 + f'<circle cx="8" cy="-100" r="14" fill="{SKIN}" stroke="{INK}" stroke-width="2"></circle>' + P("M-10 -98 C -10 -122 24 -124 26 -100 L 30 -60 L 14 -86 L -4 -84 L -16 -50 Z", "#2A1A20", 2) + '</g>')
    return "".join(o)

def sun_worship(p, w, h, seed):
    """At the door of the temple, between the porch and the altar, five and twenty men with their backs toward the temple
    and their faces toward the east, worshipping the sun."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), bg(f"sw{seed}", w, h, [(0, "#3A4A7A"), (0.7, "#F8B060"), (1, "#FFE8A0")]), sun(w * 0.1, h * 0.5, max(14, h * 0.07), color="#FFD23F", op=0.5)]
    o.append(K1.temple_front(w * 0.82, h * 0.7, w * 0.34, seed))
    o.append(f'<path d="M-10 {f(h * 0.7)} L {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B8A888" stroke="{INK}" stroke-width="2"></path>')
    s = min(fit(b, max(h * 0.5, b - 190)), 0.9)
    for i in range(10):
        x = w * (0.3 + (i % 5) * 0.09) + (i // 5) * w * 0.04; y = b - (i // 5) * h * 0.08
        o.append(mk.person(p, round(x), round(y), round(s * (1 - (i // 5) * 0.12), 3), body=SKIN, cloth=CAPT[i % 7], sw=2.6, flip=True,
                           up=[(22, -158), (40, -186), (52, -214)] if i % 3 == 0 else None, extra=A.headcloth(CAPT[(i + 3) % 7])))
    return "".join(o)

def six_men(p, w, h, seed):
    """Six men from the way of the upper gate toward the north, every man with his weapon in his hand, and one man in the
    midst of them clothed in linen with a writer's inkhorn; they stood beside the brazen altar."""
    b = h * 0.95
    o = [court(p, w, h, seed, sky=("#3A3A5A", "#C8A8A0"), temple=True, gate=True)]
    o.append(K1.horned_altar(w * 0.86, h * 0.9, min(0.7, h / 420)))
    s = min(fit(b, max(h * 0.46, b - 210)), 1.0)
    for i in range(7):
        x = w * (0.18 + i * 0.09)
        if i == 3: o.append(man_linen(p, x, b, s))
        else: o.append(warrior(p, x, b - (i % 2) * 4, s * 0.96, ["#3A3A4A", "#4A3A3A", "#3A4A3A"][i % 3]))
    return "".join(o)

def marking(p, w, h, seed):
    """Go through the midst of the city and set a mark upon the foreheads of the men that sigh and that cry: the man in
    linen in a street of Jerusalem, his inkhorn by his side, men bowed with a mark upon their foreheads."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), bg(f"mk{seed}", w, h, [(0, "#4A4A6A"), (1, "#C8B8A0")])]
    r = random.Random(seed)
    for side in (0, 1):
        for i in range(3):
            x = (w * 0.0 + i * w * 0.11) if side == 0 else (w * 0.67 + i * w * 0.11)
            o.append(house(x, h * 0.72, w * 0.11, h * r.uniform(0.3, 0.44), color=r.choice(["#A8946A", "#B8A47A"])))
    o.append(ground(w, h, h * 0.72, "#9A8A7A", dy=0))
    s = min(fit(b, max(h * 0.46, b - 210)), 1.0)
    o.append(man_linen(p, w * 0.4, b, s, up=[(-22, -158), (-40, -176), (-58, -180)]))
    for i, x in enumerate((0.22, 0.56, 0.66)):
        o.append(mk.person(p, round(w * x), round(b - 4), round(s * 0.92, 3), body=SKIN, cloth=CAPT[i + 2], sw=2.6, flip=i == 0, extra=A.headcloth(CAPT[i + 4])))
        o.append(f'<path d="M{f(w * x - 5 * s)} {f(b - 4 - 184 * s)} l {f(10 * s)} {f(10 * s)} M{f(w * x + 5 * s)} {f(b - 4 - 184 * s)} l {f(-10 * s)} {f(10 * s)}" stroke="#1A1A6A" stroke-width="{f(3 * s)}"></path>')
    return "".join(o)

def empty_court(w, h, seed, smoke_=True):
    """The courts and the city after the word went forth (9:5–7): the court empty, the gate open, smoke over the city —
    no one drawn."""
    o = [bg(f"ec{seed}", w, h, [(0, "#2A1A2A"), (1, "#8A5A4A")]), J.city_hill(w * 0.8, h * 0.66, w * 0.3, h * 0.24, seed)]
    if smoke_:
        for i in range(3): o.append(smoke(w * (0.66 + i * 0.1), h * 0.5, 8, seed + i, color="#2A1A1A", op=0.6, k=min(1.2, h / 300)))
    o.append(f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#A89878" stroke="{INK}" stroke-width="2"></rect>')
    o.append(S4.gatehouse(w * 0.3, h * 0.68, w * 0.36, h * 0.4))
    o.append(f'<path d="M-10 {f(h * 0.68)} L {f(w + 10)} {f(h * 0.68)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#9A8A6A" stroke="{INK}" stroke-width="2"></path>')
    o.append(K1.horned_altar(w * 0.62, h * 0.92, min(0.7, h / 420)))
    return "".join(o)

def fallen_court(p, w, h, seed):
    """I was left, and I fell upon my face: Ezekiel alone, fallen on his face in the empty court."""
    o = [empty_court(w, h, seed, smoke_=True)]
    o.append(N.prostrate(w * 0.24, h * 0.94, min(1.1, h / 340), color=EZ_C, skin=SKIN))
    return "".join(o)

def coals(p, w, h, seed):
    """Go in between the whirling wheels, under the cherub, and fill both thy hands with coals of fire: the man in linen
    among the cherubim and the wheels, the cloud filling the inner court."""
    o = [mk.defs(p, *ALL), bg(f"co{seed}", w, h, [(0, "#1A1A2A"), (0.6, "#4A2A2A"), (1, "#8A5A3A")])]
    for i in range(6):
        o.append(f'<ellipse cx="{f(w * (0.1 + i * 0.17))}" cy="{f(h * 0.2)}" rx="{f(w * 0.14)}" ry="{f(h * 0.1)}" fill="#E8E2D6" opacity="0.18"></ellipse>')
    b = h * 0.92; s = min(fit(b, h * 0.36) * 0.7, 0.9)
    for i, x in enumerate((0.14, 0.36, 0.64, 0.86)):
        o.append(wheel(w * x, b - 36 * s, 44 * s, seed + i, tilt=(-8, 6, -6, 8)[i]))
        o.append(creature(p, w * x, b - 40 * s, s, seed + 7 * i, spread="down", fire=i in (1, 2)))
    o.append(E.blaze(w * 0.5, b - 10 * s, w * 0.14, h * 0.2, seed, n=6))
    o.append(man_linen(p, w * 0.5, b + 4, s * 1.1, up=[(-22, -158), (0, -130), (14, -110)]))
    o.append("".join(f'<circle cx="{f(w * 0.5 + 18 * s + i * 5)}" cy="{f(b - 110 * s - (i % 2) * 4)}" r="{f(4 * s)}" fill="#FF6A2A" stroke="#FFD23F" stroke-width="1.2"></circle>' for i in range(4)))
    return "".join(o)

def threshold(p, w, h, seed, east=False):
    """The glory of Jehovah over the threshold of the house, the house filled with the cloud and the court full of the
    brightness; east=True: the cherubim with their wheels standing at the door of the east gate, the glory over them."""
    o = [mk.defs(p, *ALL), bg(f"th{seed}", w, h, [(0, "#2A2A4A"), (1, "#C8B898")])]
    if east:
        o.append(S4.gatehouse(w * 0.5, h * 0.74, w * 0.6, h * 0.5))
        o.append(f'<path d="M-10 {f(h * 0.74)} L {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B8A888" stroke="{INK}" stroke-width="2"></path>')
        s = min(fit(h * 0.96, h * 0.5) * 0.6, 0.7)
        for i, x in enumerate((0.16, 0.34, 0.66, 0.84)):
            o.append(wheel(w * x, h * 0.96 - 30 * s, 36 * s, seed + i))
            o.append(creature(p, w * x, h * 0.96 - 34 * s, s, seed + 3 * i, spread="up", fire=False))
        o.append(glory(f"tg{seed}", w * 0.5, h * 0.4, w * 0.16, h * 0.42, seed))
    else:
        o.append(K1.temple_front(w * 0.5, h * 0.72, w * 0.6, seed))
        o.append(f'<path d="M-10 {f(h * 0.72)} L {f(w + 10)} {f(h * 0.72)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#E8D8B8" stroke="{INK}" stroke-width="2"></path>')
        o.append(glory(f"tg{seed}", w * 0.5, h * 0.76, w * 0.16, h * 0.5, seed))
        for i in range(8):
            o.append(f'<ellipse cx="{f(w * (0.05 + i * 0.13))}" cy="{f(h * (0.5 + 0.06 * (i % 2)))}" rx="{f(w * 0.12)}" ry="{f(h * 0.08)}" fill="#F3EFE6" opacity="0.55"></ellipse>')
    return "".join(o)

def caldron(w, h, seed, city=True):
    """This city is the caldron, and we are the flesh: a great caldron over the fire, the walls of the city behind."""
    o = [bg(f"cl{seed}", w, h, [(0, "#2A1A2A"), (1, "#8A4A2A")])]
    if city: o.append(J.city_hill(w * 0.5, h * 0.62, w * 0.5, h * 0.3, seed))
    cx, cy, R = w * 0.5, h * 0.74, min(w * 0.22, h * 0.24)
    o.append(E.blaze(cx, h * 0.98, R * 2.4, h * 0.22, seed, n=8))
    o.append(P(f"M{f(cx - R)} {f(cy - R * 0.5)} C {f(cx - R * 1.1)} {f(cy + R * 0.6)} {f(cx + R * 1.1)} {f(cy + R * 0.6)} {f(cx + R)} {f(cy - R * 0.5)} Z", "#3A3A44", 2.6))
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy - R * 0.5)}" rx="{f(R)}" ry="{f(R * 0.2)}" fill="#5A5A64" stroke="{INK}" stroke-width="2.4"></ellipse>')
    o.append(smoke(cx - R * 0.3, cy - R * 0.7, 6, seed, color="#E8E2D6", op=0.4, k=R / 120))
    return "".join(o)

def hearts(w, h):
    """I will take the stony heart out of their flesh, and will give them a heart of flesh: a plate, a heart of stone
    cracked and grey, an arrow, a heart of flesh."""
    o = [bp(w, h), title_bar(w, "ONE HEART · A NEW SPIRIT")]
    def heart(cx, cy, R, fill, stone):
        d = f"M{f(cx)} {f(cy + R)} C {f(cx - R * 1.4)} {f(cy)} {f(cx - R * 1.1)} {f(cy - R * 1.1)} {f(cx)} {f(cy - R * 0.45)} C {f(cx + R * 1.1)} {f(cy - R * 1.1)} {f(cx + R * 1.4)} {f(cy)} {f(cx)} {f(cy + R)} Z"
        s = P(d, fill, 2.6)
        if stone: s += f'<path d="M{f(cx - R * 0.4)} {f(cy - R * 0.5)} L {f(cx - R * 0.1)} {f(cy)} L {f(cx - R * 0.3)} {f(cy + R * 0.3)} M{f(cx + R * 0.3)} {f(cy - R * 0.6)} L {f(cx + R * 0.1)} {f(cy - R * 0.1)}" stroke="#0D0D0F" stroke-width="2" fill="none"></path>'
        else: s += f'<path d="M{f(cx - R * 0.5)} {f(cy - R * 0.3)} C {f(cx - R * 0.4)} {f(cy - R * 0.6)} {f(cx - R * 0.1)} {f(cy - R * 0.6)} {f(cx)} {f(cy - R * 0.3)}" stroke="#FFB0A0" stroke-width="3" fill="none"></path>'
        return s
    R = min(w * 0.14, h * 0.3)
    o.append(heart(w * 0.26, h * 0.56, R, "#8A8A90", True))
    o.append(heart(w * 0.74, h * 0.56, R, "#C8202A", False) + glow("hg", w * 0.74, h * 0.56, R * 1.6, R * 1.6, "#FF8A6A", 0.4))
    o.append(route([(w * 0.42, h * 0.56), (w * 0.56, h * 0.56)], color=GOLD, sw=3, dash="8 5"))
    o.append(label(w * 0.26, h * 0.56 + R * 1.5, "THE STONY HEART", CYAN, 10) + label(w * 0.74, h * 0.56 + R * 1.5, "A HEART OF FLESH", GOLD, 10))
    return "".join(o)

def glory_mountain(w, h, seed):
    """The glory of Jehovah went up from the midst of the city, and stood upon the mountain on the east side of the city:
    the city dark below, the light standing over the eastern mountain."""
    o = [bg(f"gm{seed}", w, h, [(0, "#0B0B2A"), (1, "#3A2A4A")]), mk.stars(40, w, h * 0.5, seed)]
    o.append(P(f"M{f(w * 0.5)} {f(h + 10)} L {f(w * 0.56)} {f(h * 0.62)} C {f(w * 0.66)} {f(h * 0.5)} {f(w * 0.82)} {f(h * 0.48)} {f(w + 10)} {f(h * 0.56)} L {f(w + 10)} {f(h + 10)} Z", "#2A2A3A", 2.4))
    o.append(glory(f"gmg{seed}", w * 0.76, h * 0.5, w * 0.1, h * 0.4, seed))
    o.append(J.city_hill(w * 0.26, h * 0.92, w * 0.3, h * 0.32, seed))
    o.append(f'<rect x="-10" y="{f(h * 0.92)}" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#1A1A2A"></rect>')
    return "".join(o)

def speaking_captives(p, w, h, seed):
    """Then I spake unto them of the captivity all the things that Jehovah had showed me: Ezekiel standing by the river,
    the captives seated about him."""
    return chebar(p, w, h, seed, opened=False)
