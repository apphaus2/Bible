"""Isaiah 31–35 drawings (on top of isa.art8): Egypt's horses and chariots, the lion over Zion and the birds hovering, the
shade of a great rock in a weary land, the palace forsaken, the wilderness made a fruitful field, sowing beside all waters,
the highways waste, the munitions of rocks, Zion a tent that shall not be removed, the heavens rolled together as a scroll,
Edom's mountains, its streams of pitch and its beasts, and the desert blossoming as the rose with the way of holiness."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art8 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
from genesis.art2 import birds

def egypt_chariots(w, h, seed):
    """Woe to them that go down to Egypt for help, and rely on horses, and trust in chariots because they are many: Pharaoh's
    chariots drawn up in ranks on the plain before the pyramids, gold and blue."""
    r = random.Random(seed)
    o = [bg(w, h, "#E8A050", "#F8E0A0"), EG.pyramid(w * 0.8, h * 0.56, w * 0.2, h * 0.24), EG.pyramid(w * 0.94, h * 0.56, w * 0.12, h * 0.14), ground(w, h, h * 0.56, "#D8B070", dy=0)]
    k = min(0.5, h / 600)
    for row in range(2):
        for i in range(5):
            x = w * (0.08 + i * 0.16 + row * 0.08); y = h * (0.74 + row * 0.16)
            o.append(E3.chariot(x, y, k * (0.8 + row * 0.25), color="#E8B830", driver="#1F5FAD"))
    return "".join(o)

def lion_zion(w, h, seed):
    """As the lion growling, not dismayed at the shepherds' voice, so will Jehovah of hosts come down upon mount Zion; as birds
    hovering, so will he protect Jerusalem: a lion standing on a rock below the city, shepherds shouting far off, birds
    hovering in a ring over Jerusalem."""
    o = [bg(w, h, "#8FB0D8", "#F3E0B0"), J.city_hill(w * 0.66, h * 0.56, w * 0.26, h * 0.3, seed), K1.temple_front(w * 0.66, h * 0.34, min(w * 0.1, h * 0.24), seed),
         ground(w, h, h * 0.62, "#B8A070", dy=0)]
    for k in range(12):
        a = k * math.pi * 2 / 12
        o.append(birds(1, w * 0.66 + math.cos(a) * w * 0.2, w * 0.66 + math.cos(a) * w * 0.2 + 1, h * 0.14 + math.sin(a) * h * 0.08, h * 0.14 + math.sin(a) * h * 0.08 + 1, seed + k))
    o.append(f'<path d="M{f(w * 0.04)} {f(h + 10)} L {f(w * 0.08)} {f(h * 0.76)} L {f(w * 0.3)} {f(h * 0.72)} L {f(w * 0.36)} {f(h + 10)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(J2.lion(w * 0.2, h * 0.74, min(0.6, h / 420), roar=True))
    for i in range(3):
        o.append(mk.person(f"lz{seed}", round(w * (0.42 + i * 0.05)), round(h * 0.94), round(min(0.24, h / 900), 3), body="#3A2014", cloth="#8A6A4A", kind="Tunic"))
    return mk.defs(f"lz{seed}", *ALL) + "".join(o)

def rock_shade(p, w, h, seed):
    """As a hiding-place from the wind, a covert from the tempest, as streams of water in a dry place, as the shade of a great
    rock in a weary land: a great red rock in the desert, a traveller resting in its shade, a stream running at its foot."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#E8A050", "#FFE8A8"), sun(w * 0.86, h * 0.14, min(26, h * 0.08), color="#FFF4C2", op=0.4), ground(w, h, h * 0.66, "#E0B070", dy=0)]
    o.append(f'<path d="M{f(w * 0.2)} {f(b)} L {f(w * 0.24)} {f(h * 0.3)} C {f(w * 0.3)} {f(h * 0.18)} {f(w * 0.46)} {f(h * 0.2)} {f(w * 0.52)} {f(h * 0.34)} L {f(w * 0.58)} {f(b)} Z" fill="#B85A3A" stroke="#0D0D0F" stroke-width="2.6"></path>'
             f'<path d="M{f(w * 0.58)} {f(b)} L {f(w * 0.56)} {f(h * 0.6)} L {f(w * 0.86)} {f(b)} Z" fill="#8A6A4A" opacity="0.4"></path>'
             f'<path d="M{f(w * 0.3)} {f(b + 4)} C {f(w * 0.5)} {f(b - 10)} {f(w * 0.7)} {f(b + 6)} {f(w + 10)} {f(b - 6)}" stroke="#2C9DB8" stroke-width="6" fill="none"></path>')
    o.append(E.kneel(w * 0.66, b - 6, fit(b, max(h * 0.55, b - 130)) * 0.9, color="#4A5A7A", skin="#B98A6E"))
    return "".join(o)

def forsaken_palace(w, h, seed):
    """The palace shall be forsaken; the populous city deserted; the hill and the watch-tower shall be for dens for ever, a joy
    of wild asses, a pasture of flocks: an empty palace and tower on a hill, thorns at the gate, wild asses grazing."""
    o = [bg(w, h, "#8A8AA0", "#E8D8B8"), hills(w, h, h * 0.6, seed, color="#9A9A6A", amp=8)]
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(h * 0.26)}" width="{f(w * 0.36)}" height="{f(h * 0.4)}" fill="#C8B898" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             + "".join(f'<rect x="{f(w * (0.33 + i * 0.07))}" y="{f(h * 0.34)}" width="{f(w * 0.03)}" height="{f(h * 0.1)}" fill="#2A1E1A"></rect>' for i in range(5)))
    o.append(tower(w * 0.76, h * 0.66, w * 0.08, h * 0.44, color="#A89878"))
    o.append(ground(w, h, h * 0.66, "#A8986A", dy=0) + thorns(w * 0.3, w * 0.66, h * 0.7, seed, n=10, s=min(0.9, h / 300)))
    k = min(0.45, h / 600)
    o.append(N.ass(w * 0.14, h * 0.9, k, color="#9A8A78") + N.ass(w * 0.86, h * 0.94, k * 0.9, flip=True, color="#8A7A68") + E.sheep(w * 0.5, h * 0.92, k * 0.8))
    return "".join(o)

def fruitful(w, h, seed):
    """Until the Spirit be poured upon us from on high, and the wilderness become a fruitful field: light pouring down on a
    wilderness that turns green from the middle outward, a plowed and sown field where the sand was."""
    r = random.Random(seed)
    o = [bg(w, h, "#5A7ABA", "#FFE8B0"), V.rays(w * 0.5, -h * 0.1, 30, 20, max(w, h) * 1.2, color="#FFF4C2", op=0.4), ground(w, h, h * 0.5, "#D8B070", dy=0),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.78)}" rx="{f(w * 0.36)}" ry="{f(h * 0.2)}" fill="#7AA040" stroke="#0D0D0F" stroke-width="2"></ellipse>']
    for k in range(5):
        o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.78)}" rx="{f(w * (0.34 - k * 0.06))}" ry="{f(h * (0.18 - k * 0.03))}" fill="none" stroke="#4E7A2A" stroke-width="2"></ellipse>')
    o.append(R1.field(w * 0.3, w * 0.7, h * 0.86, h * 0.12, seed, rows=2))
    return "".join(o)

def sow_waters(p, w, h, seed):
    """Blessed are ye that sow beside all waters, that send forth the feet of the ox and the ass: a sower by a stream, an ox and
    an ass loosed to graze beside him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FC8E8", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#7A9A4A", amp=8), ground(w, h, h * 0.6, "#9CBB5E", dy=0),
         f'<path d="M-10 {f(h * 0.72)} C {f(w * 0.3)} {f(h * 0.66)} {f(w * 0.6)} {f(h * 0.78)} {f(w + 10)} {f(h * 0.7)}" stroke="#2C9DB8" stroke-width="{f(max(6, h * 0.03))}" fill="none"></path>']
    s = fit(b, max(h * 0.55, b - 140))
    o.append(man(p, w * 0.3, b, s, "#8A6A3A", up=[(-22, -158), (-46, -150), (-70, -160)]))
    k = min(0.5, h / 560)
    o.append(S1.cow(w * 0.6, b, k, color="#8A5A30", low=True) + N.ass(w * 0.84, b, k, flip=True))
    return "".join(o)

def waste_highway(w, h, seed):
    """The highways lie waste, the wayfaring man ceaseth; Lebanon is confounded and withereth away; Sharon is like a desert:
    an empty road running into the distance between withered trees and bare fields."""
    r = random.Random(seed)
    o = [bg(w, h, "#9A8A7A", "#E8D0A8"), hills(w, h, h * 0.46, seed, color="#8A7A5A", amp=10), ground(w, h, h * 0.5, "#B8986A", dy=0),
         f'<path d="M{f(w * 0.46)} {f(h * 0.5)} L {f(w * 0.54)} {f(h * 0.5)} L {f(w * 0.8)} {f(h + 10)} L {f(w * 0.2)} {f(h + 10)} Z" fill="#D8C098" stroke="#0D0D0F" stroke-width="1.6"></path>']
    for i in range(6):
        x = w * (0.06 + i * 0.18) if i < 3 else w * (0.62 + (i - 3) * 0.14); y = h * (0.62 + (i % 3) * 0.1)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - h * 0.14)} M{f(x)} {f(y - h * 0.08)} l -12 -10 M{f(x)} {f(y - h * 0.1)} l 10 -12" stroke="#5A4A3A" stroke-width="3" fill="none"></path>')
    return "".join(o)

def munitions(w, h, seed):
    """He shall dwell on high; his place of defence shall be the munitions of rocks; his bread shall be given him; his waters
    shall be sure: a stronghold built into a high crag, a spring running out of the rock below it."""
    o = [bg(w, h, "#8FB8E0", "#F0E8D0"), f'<path d="M{f(w * 0.2)} {f(h + 10)} L {f(w * 0.3)} {f(h * 0.3)} L {f(w * 0.42)} {f(h * 0.16)} L {f(w * 0.6)} {f(h * 0.2)} L {f(w * 0.72)} {f(h * 0.42)} L {f(w * 0.82)} {f(h + 10)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    o.append(f'<rect x="{f(w * 0.4)}" y="{f(h * 0.1)}" width="{f(w * 0.18)}" height="{f(h * 0.16)}" fill="#C8B898" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(w * (0.4 + i * 0.045))}" y="{f(h * 0.07)}" width="{f(w * 0.025)}" height="{f(h * 0.04)}" fill="#C8B898" stroke="#0D0D0F" stroke-width="1.4"></rect>' for i in range(4)))
    o.append(E4.gush(w * 0.62, h * 0.7, seed, scale=min(1.0, h / 300)) + f'<path d="M{f(w * 0.62)} {f(h * 0.76)} C {f(w * 0.7)} {f(h * 0.86)} {f(w * 0.84)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.92)}" stroke="#2C9DB8" stroke-width="5" fill="none"></path>')
    return "".join(o)

def zion_tent(w, h, seed):
    """Look upon Zion: a quiet habitation, a tent that shall not be removed, the stakes whereof shall never be plucked up; a
    place of broad rivers wherein shall go no galley with oars: a great tent on the hill of Zion, its cords pegged fast, broad
    rivers round it and no ship upon them."""
    o = [bg(w, h, "#8FC8E8", "#FFF0C8"), hills(w, h, h * 0.5, seed, color="#8AA06A", amp=8),
         f'<path d="M-10 {f(h * 0.78)} C {f(w * 0.3)} {f(h * 0.72)} {f(w * 0.7)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.76)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2C7DA8" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, h * 0.62, "#B8A070", dy=0) if False else ""]
    cx, b = w * 0.5, h * 0.62; tw, th = min(w * 0.5, h * 1.0), h * 0.4
    o.append(f'<path d="M{f(cx - tw / 2)} {f(b)} L {f(cx)} {f(b - th)} L {f(cx + tw / 2)} {f(b)} Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.6"></path>'
             f'<path d="M{f(cx - tw * 0.12)} {f(b)} L {f(cx)} {f(b - th * 0.5)} L {f(cx + tw * 0.12)} {f(b)} Z" fill="#5A3A22"></path>')
    for side in (-1, 1):
        for k in range(3):
            x0 = cx + side * tw * (0.1 + k * 0.14); y0 = b - th * (0.8 - k * 0.26)
            x1 = cx + side * (tw / 2 + 40 + k * 30); y1 = b + 6
            o.append(f'<path d="M{f(x0)} {f(y0)} L {f(x1)} {f(y1)}" stroke="#5A3A22" stroke-width="2"></path><path d="M{f(x1)} {f(y1 - 8)} L {f(x1)} {f(y1 + 10)}" stroke="#3A2414" stroke-width="5"></path>')
    return "".join(o)

def heavens_scroll(w, h, seed):
    """All the host of heaven shall be dissolved, and the heavens shall be rolled together as a scroll; and all their host
    shall fade away, as the leaf fadeth from off the vine: the night sky curling up at its edges like a scroll, stars falling
    like leaves."""
    r = random.Random(seed)
    o = [rect(w, h, "#05050A"), f'<path d="M{f(w * 0.08)} {f(h * 0.08)} L {f(w * 0.92)} {f(h * 0.08)} L {f(w * 0.92)} {f(h * 0.7)} L {f(w * 0.08)} {f(h * 0.7)} Z" fill="#12113A"></path>',
         f'<g transform="translate({f(w * 0.08)} {f(h * 0.08)})">{mk.stars(40, w * 0.84, h * 0.62, seed)}</g>']
    for x, side in ((w * 0.08, -1), (w * 0.92, 1)):
        o.append(f'<ellipse cx="{f(x)}" cy="{f(h * 0.39)}" rx="{f(w * 0.04)}" ry="{f(h * 0.33)}" fill="#2A2458" stroke="#8A7AC8" stroke-width="2"></ellipse>'
                 f'<ellipse cx="{f(x)}" cy="{f(h * 0.39)}" rx="{f(w * 0.02)}" ry="{f(h * 0.3)}" fill="none" stroke="#5A4A98" stroke-width="1.6"></ellipse>')
    for _ in range(14):
        x = r.uniform(w * 0.1, w * 0.9); y = r.uniform(h * 0.72, h * 0.96)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x - 8)} {f(y - 6)} {f(x - 6)} {f(y - 16)} {f(x)} {f(y - 18)} C {f(x + 6)} {f(y - 16)} {f(x + 8)} {f(y - 6)} {f(x)} {f(y)} Z" fill="#C8A040" opacity="0.7" transform="rotate({r.randint(-60, 60)} {f(x)} {f(y)})"></path>')
    return "".join(o)

def edom_red(w, h, seed):
    """Upon Edom, upon the people of my curse: the red mountains of Edom and the rock-city of Bozrah under a blood-red evening
    sky (the slaughter told in words only)."""
    o = [bg(w, h, "#3A0A0A", "#C84A2A"), f'<path d="M-10 {f(h * 0.6)} L {f(w * 0.16)} {f(h * 0.3)} L {f(w * 0.3)} {f(h * 0.5)} L {f(w * 0.5)} {f(h * 0.2)} L {f(w * 0.7)} {f(h * 0.46)} L {f(w * 0.86)} {f(h * 0.26)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A2A1A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M-10 {f(h * 0.8)} L {f(w * 0.4)} {f(h * 0.6)} L {f(w * 0.7)} {f(h * 0.72)} L {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A1A14" stroke="#0D0D0F" stroke-width="2"></path>']
    for i in range(4):
        o.append(f'<rect x="{f(w * (0.44 + i * 0.03))}" y="{f(h * 0.6 - (i % 2) * 8)}" width="{f(w * 0.025)}" height="{f(h * 0.06)}" fill="#3A1010" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    return "".join(o)

def edom_pitch(w, h, seed):
    """The streams of Edom shall be turned into pitch, and the dust thereof into brimstone; it shall not be quenched night nor
    day; the smoke thereof shall go up for ever: black streams burning in a red valley, smoke rising in columns."""
    o = [bg(w, h, "#1A0A0A", "#6A2A1A"), ground(w, h, h * 0.5, "#4A2A1A", dy=0)]
    for k in range(3):
        x = w * (0.2 + k * 0.3)
        o.append(f'<path d="M{f(x - 30)} {f(h * 0.5)} C {f(x - 10)} {f(h * 0.7)} {f(x + 20)} {f(h * 0.8)} {f(x + 10)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="{f(max(8, h * 0.05))}" fill="none"></path>')
        o.append(E.blaze(x, h * 0.62 + k * 10, w * 0.12, h * 0.2, seed + k, n=5) + smoke(x, h * 0.44, 9, seed + k, r0=h * 0.04, spread=10, color="#2A1A1A", op=0.75))
    return "".join(o)

def edom_beasts(w, h, seed):
    """The pelican and the porcupine shall possess it; the owl and the raven shall dwell therein; thorns in its palaces; a
    habitation of jackals, a court for ostriches; there shall the kites be gathered: Edom's palace in ruins at dusk, thorns in
    its courts, an owl on the broken lintel, ravens and kites wheeling, a jackal and an ostrich among the stones."""
    r = random.Random(seed)
    o = [bg(w, h, "#3A2A3A", "#B87A5A"), ground(w, h, h * 0.76, "#7A5A4A", dy=0)]
    for i in range(5):
        x = w * (0.1 + i * 0.2); hh = h * r.uniform(0.2, 0.46)
        o.append(f'<rect x="{f(x - 12)}" y="{f(h * 0.76 - hh)}" width="24" height="{f(hh)}" fill="#A88A6A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(f'<rect x="{f(w * 0.08)}" y="{f(h * 0.3)}" width="{f(w * 0.26)}" height="14" fill="#A88A6A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    ox, oy = w * 0.2, h * 0.3
    o.append(f'<ellipse cx="{f(ox)}" cy="{f(oy - 16)}" rx="11" ry="15" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="1.6"></ellipse><circle cx="{f(ox - 4)}" cy="{f(oy - 22)}" r="3.4" fill="#FFD23F"></circle><circle cx="{f(ox + 4)}" cy="{f(oy - 22)}" r="3.4" fill="#FFD23F"></circle>')
    o.append(thorns(0, w, h * 0.8, seed, n=int(w / 40), s=min(0.9, h / 320)))
    o.append(birds(7, w * 0.4, w * 0.95, h * 0.06, h * 0.3, seed, smin=0.8, smax=1.4))
    k = min(0.45, h / 600)
    o.append(beast(w * 0.56, h * 0.9, k * 0.8, "wolf") + f'<ellipse cx="{f(w * 0.36)}" cy="{f(h * 0.94)}" rx="{f(18 * k * 2)}" ry="{f(10 * k * 2)}" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
             + "".join(f'<path d="M{f(w * 0.36 + (j - 4) * 4 * k * 2)} {f(h * 0.94 - 8 * k * 2)} l {f((j - 4) * 1.6 * k * 2)} {f(-14 * k * 2)}" stroke="#E8E2D6" stroke-width="1.4"></path>' for j in range(9)))
    ox, oy, kk = w * 0.82, h * 0.94, k * 2
    o.append(f'<ellipse cx="{f(ox)}" cy="{f(oy - 40 * kk)}" rx="{f(24 * kk)}" ry="{f(16 * kk)}" fill="#1A1414" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
             f'<path d="M{f(ox + 16 * kk)} {f(oy - 48 * kk)} C {f(ox + 22 * kk)} {f(oy - 70 * kk)} {f(ox + 18 * kk)} {f(oy - 86 * kk)} {f(ox + 26 * kk)} {f(oy - 92 * kk)}" stroke="#D8B8A0" stroke-width="{f(4 * kk)}" fill="none"></path>'
             f'<path d="M{f(ox - 6 * kk)} {f(oy - 26 * kk)} L {f(ox - 8 * kk)} {f(oy)} M{f(ox + 6 * kk)} {f(oy - 26 * kk)} L {f(ox + 8 * kk)} {f(oy)}" stroke="#D8B8A0" stroke-width="{f(3 * kk)}"></path>')
    return "".join(o)

def desert_blossom(w, h, seed):
    """The wilderness and the dry land shall be glad; and the desert shall rejoice, and blossom as the rose; the glory of
    Lebanon, the excellency of Carmel and Sharon: a desert of dunes covered in blossom, red and gold, under a clear morning."""
    r = random.Random(seed)
    o = [bg(w, h, "#7AB8E8", "#FFF0C8"), sun(w * 0.82, h * 0.16, min(24, h * 0.07), color="#FFF4C2", op=0.4),
         f'<path d="M-10 {f(h * 0.56)} C {f(w * 0.2)} {f(h * 0.46)} {f(w * 0.4)} {f(h * 0.58)} {f(w * 0.6)} {f(h * 0.5)} C {f(w * 0.8)} {f(h * 0.42)} {f(w * 0.9)} {f(h * 0.54)} {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#E0C080" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M-10 {f(h * 0.72)} C {f(w * 0.3)} {f(h * 0.62)} {f(w * 0.6)} {f(h * 0.76)} {f(w + 10)} {f(h * 0.66)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8A868" stroke="#0D0D0F" stroke-width="2"></path>']
    n = int(w * h / 2400)
    for _ in range(min(140, n)):
        x = r.uniform(0, w); y = r.uniform(h * 0.56, h * 0.98); sc = 0.6 + (y / h - 0.5) * 1.4
        col = r.choice(["#D7261E", "#E8406A", "#FFD23F", "#FF8A3D", "#F3EFE6"])
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 10 * sc)}" stroke="#3E7A2A" stroke-width="1.4"></path>'
                 + "".join(f'<circle cx="{f(x + math.cos(a) * 3.4 * sc)}" cy="{f(y - 12 * sc + math.sin(a) * 3.4 * sc)}" r="{f(2.6 * sc)}" fill="{col}"></circle>' for a in [k * math.pi * 2 / 5 for k in range(5)])
                 + f'<circle cx="{f(x)}" cy="{f(y - 12 * sc)}" r="{f(1.6 * sc)}" fill="#FFF4C2"></circle>')
    return "".join(o)

def streams_desert(w, h, seed):
    """In the wilderness shall waters break out, and streams in the desert; the glowing sand shall become a pool, and in the
    habitation of jackals grass with reeds and rushes: a spring bursting out of the dry rock, a new pool among reeds."""
    o = [bg(w, h, "#8FC8E8", "#FFE8B0"), ground(w, h, h * 0.5, "#E0B878", dy=0),
         f'<path d="M{f(w * 0.06)} {f(h * 0.7)} L {f(w * 0.12)} {f(h * 0.4)} L {f(w * 0.3)} {f(h * 0.36)} L {f(w * 0.36)} {f(h * 0.7)} Z" fill="#B87A4A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    o.append(E4.gush(w * 0.3, h * 0.56, seed, scale=min(1.0, h / 300)))
    o.append(f'<ellipse cx="{f(w * 0.6)}" cy="{f(h * 0.84)}" rx="{f(w * 0.28)}" ry="{f(h * 0.1)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<path d="M{f(w * 0.32)} {f(h * 0.66)} C {f(w * 0.36)} {f(h * 0.76)} {f(w * 0.4)} {f(h * 0.82)} {f(w * 0.46)} {f(h * 0.84)}" stroke="#2C9DB8" stroke-width="7" fill="none"></path>')
    o.append(E.reeds(w * 0.38, w * 0.52, h * 0.82, h * 0.2, 8, seed) + E.reeds(w * 0.78, w * 0.92, h * 0.84, h * 0.2, 8, seed + 1))
    return "".join(o)

def way_holiness(p, w, h, seed):
    """A highway shall be there, and a way, and it shall be called The way of holiness: the ransomed of Jehovah shall return,
    and come with singing unto Zion: a raised road across the blossoming desert, the redeemed walking it with timbrels toward
    Zion shining far off; no lion there."""
    r = random.Random(seed); b = h * 0.94
    o = [mk.defs(p, *ALL), desert_blossom(w, h, seed), J.city_hill(w * 0.84, h * 0.5, w * 0.12, h * 0.14, seed), V.rays(w * 0.84, h * 0.4, 20, 10, w * 0.3, color="#FFF4C2", op=0.4)]
    o.append(f'<path d="M{f(w * 0.06)} {f(h + 10)} L {f(w * 0.8)} {f(h * 0.5)} L {f(w * 0.86)} {f(h * 0.5)} L {f(w * 0.36)} {f(h + 10)} Z" fill="#F3E8C8" stroke="#0D0D0F" stroke-width="2"></path>')
    for i in range(6):
        t = i / 6; x = w * (0.2 + t * 0.52); y = b - t * (b - h * 0.56)
        s = fit(b, b - 120) * (1 - t * 0.7)
        o.append((man if i % 2 else woman)(p, x, y, s, r.choice(["#5A3A6A", "#2A5A7A", "#8A3A2A", "#3A6A3A", "#C2456A", "#E8B830"]), up=[(-22, -158), (-30, -190), (-24, -222)] if i % 3 == 0 else None))
    return "".join(o)
