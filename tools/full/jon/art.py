"""Drawings for the Jonah volume, on the minor prophets' kit (oba.minor): Joppa and the ship of Tarshish, the tempest, the
wares cast into the sea, the sleeper in the innermost part of the ship, the lots, the sea calmed; the great fish (a great
whale-like fish; Jonah inside only a dark shape), the deep with its weeds and the bars of the earth, the dry land; Nineveh,
that great city of three days' journey, in sackcloth; the king in ashes; the booth east of the city, the gourd, the worm,
the sultry east wind. God is never drawn: the tempest is wind and lightning, his word comes in the Voice box."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from oba.minor import *
from job.art import seated
from kg1.art import bed

JONAH_C = "#1F5A7A"
SACK = "#6A5A48"

def jonah_fig(p, x, y, s, flip=False, up=None):
    """Jonah at a distance: a sea-blue robe and headcloth, brown beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=JONAH_C, sw=3, flip=flip, up=up, extra=A.headcloth(JONAH_C) + BLACK_BEARD.replace("#2A1A10", "#4A2A1A"))

def tossed(x, y, s, rot, sail="#E8E2D6", crew=0, p=None, seed=1):
    """The ship heeling over at angle rot, with a few mariners on deck."""
    o = ship(0, 0, 1, sail=sail)
    if crew and p:
        r = random.Random(seed)
        for i in range(crew):
            o += man(p, -60 + i * 40, -22, 0.22, r.choice(["#6A4A3A", "#3A4A6A", "#7A3A3A", "#5A5A3A"]), flip=i % 2 == 1, up=[(22, -158), (40, -176), (58, -196)] if i % 2 else None)
    return f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(s)})">{o}</g>'

def swell(w, h, y, seed, color="#0F3A52", foam="#CFEFFF", n=5, amp=0.12):
    """Great breaking waves across the panel."""
    r = random.Random(seed); o = []
    for k in range(n):
        yy = y + (h - y) * k / n; a = h * amp * r.uniform(0.6, 1.2)
        d = f"M-20 {f(yy)}"
        x = -20
        while x < w + 40:
            d += f" Q {f(x + 40)} {f(yy - a)} {f(x + 90)} {f(yy - a * 0.2)} Q {f(x + 110)} {f(yy + a * 0.3)} {f(x + 150)} {f(yy)}"; x += 150
        d += f" L {f(w + 20)} {f(h + 20)} L -20 {f(h + 20)} Z"
        o.append(f'<path d="{d}" fill="{color}" stroke="#0D0D0F" stroke-width="2" opacity="{0.9 if k else 0.8}"></path>')
        x = r.uniform(0, 60)
        while x < w:
            o.append(f'<path d="M{f(x + 70)} {f(yy - a * 0.9)} q 14 -4 26 6" stroke="{foam}" stroke-width="3" fill="none"></path>'); x += 150
    return "".join(o)

def joppa(p, w, h, seed):
    """Jonah went down to Joppa and found a ship going to Tarshish: the harbour, the ship at the quay, Jonah at its side."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.42, seed, color="#A8906A", amp=16),
         walls(w * 0.02, w * 0.4, h * 0.5, h * 0.2, seed, towers=2), sea(w, h, h * 0.5, seed),
         f'<path d="M-10 {f(h * 0.74)} L {f(w * 0.46)} {f(h * 0.74)} L {f(w * 0.46)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.2"></path>',
         ship(w * 0.74, h * 0.8, min(1.3, h / 260), sail="#E8E2D6")]
    s = fit(b, h * 0.44)
    o.append(jonah_fig(p, w * 0.36, b, s, flip=False) + man(p, w * 0.2, b, s * 0.96, "#6A4A3A", flip=False, up=[(22, -158), (40, -150), (56, -140)]))
    return "".join(o)

def tempest(p, w, h, seed, crew=3, bolts_=2):
    """A great wind upon the sea and a mighty tempest: the ship like to be broken (God is not drawn: wind and lightning)."""
    o = [mk.defs(p, *ALL), sky(w, h, "#0B0B1A", "#3A3A4E"), clouds(w, h * 0.1, seed, n=7, color="#1A1A28", op=0.9, h=h)]
    for i in range(bolts_): o.append(bolt(w * (0.2 + 0.55 * i), 0, h * 0.5, seed + i))
    o.append(wind_lines(w, h, seed, n=12, color="#CFE0FF", op=0.4, y0=0.05, y1=0.6))
    o.append(swell(w, h, h * 0.62, seed + 3, n=2))
    o.append(tossed(w * 0.5, h * 0.7, min(1.8, h / 170), -18, crew=crew, p=p, seed=seed))
    o.append(swell(w, h, h * 0.8, seed + 5, n=2, color="#0B2E42"))
    return "".join(o)

def wares(p, w, h, seed):
    """The mariners cast forth the wares into the sea: jars and bales falling from the heeling ship."""
    o = [tempest(p, w, h, seed, crew=4, bolts_=1)]
    r = random.Random(seed)
    k = min(1.4, h / 240)
    for i in range(5):
        x, y = w * (0.62 + i * 0.06), h * (0.5 + r.uniform(0, 0.2))
        o.append(f'<g transform="rotate({r.randint(-40, 40)} {f(x)} {f(y)})"><path d="M{f(x - 8 * k)} {f(y)} C {f(x - 12 * k)} {f(y - 20 * k)} {f(x + 12 * k)} {f(y - 20 * k)} {f(x + 8 * k)} {f(y)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></path></g>')
    return "".join(o)

def hold(w, h, seed):
    """Jonah gone down into the innermost parts of the ship, fast asleep: the dark hold, its ribs, a swinging lamp."""
    from genesis.art4 import clay_lamp
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A120C"></rect>']
    for i in range(9):
        x = w * (i + 0.5) / 9
        o.append(f'<path d="M{f(x)} -10 C {f(x - 14)} {f(h * 0.4)} {f(x - 14)} {f(h * 0.7)} {f(x + (x - w / 2) * 0.1)} {f(h + 10)}" stroke="#4A3220" stroke-width="12" fill="none"></path>'
                 f'<path d="M{f(x)} -10 C {f(x - 14)} {f(h * 0.4)} {f(x - 14)} {f(h * 0.7)} {f(x + (x - w / 2) * 0.1)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="1.4" fill="none"></path>')
    o.append(halo(w * 0.3, h * 0.3, h * 0.5, "#FFC14D", 0.35))
    o.append(f'<path d="M{f(w * 0.3)} 0 L {f(w * 0.31)} {f(h * 0.24)}" stroke="#0D0D0F" stroke-width="2"></path>' + clay_lamp(w * 0.31, h * 0.3, min(1.0, h / 300)))
    for i in range(3):
        o.append(f'<path d="M{f(w * (0.68 + i * 0.09))} {f(h * 0.94)} C {f(w * (0.66 + i * 0.09))} {f(h * 0.7)} {f(w * (0.74 + i * 0.09))} {f(h * 0.7)} {f(w * (0.72 + i * 0.09))} {f(h * 0.94)} Z" fill="#8A4A26" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.92)}" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#3A2614" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(bed(w, h, w * 0.12, w * 0.6, h * 0.98, cover=JONAH_C, head="#C98E66", hair="#4A2A1A"))
    o.append(label(w * 0.42, h * 0.62, "Z z z", "#FFE6A0", 14))
    return "".join(o)

def lots(w, h, seed):
    """They cast lots, and the lot fell upon Jonah: the potsherds thrown on the wet deck, one lit."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A1E"></rect>']
    for i in range(12):
        o.append(f'<path d="M-10 {f(h * i / 12)} L {f(w + 10)} {f(h * i / 12)}" stroke="#241810" stroke-width="3"></path>')
    o.append(rain(w, h, seed, n=40, op=0.3))
    k = min(1.4, h / 200)
    for i in range(9):
        x, y = w * r.uniform(0.12, 0.88), h * r.uniform(0.3, 0.85)
        lit = i == 4
        if lit: x, y = w * 0.5, h * 0.56; o.append(halo(x, y, 70 * k, "#FFD23F", 0.6))
        o.append(f'<path d="M{f(x - 16 * k)} {f(y)} L {f(x - 6 * k)} {f(y - 12 * k)} L {f(x + 14 * k)} {f(y - 8 * k)} L {f(x + 12 * k)} {f(y + 8 * k)} L {f(x - 8 * k)} {f(y + 10 * k)} Z" '
                 f'fill="{"#FFD23F" if lit else "#B5652E"}" stroke="#0D0D0F" stroke-width="1.8" transform="rotate({r.randint(-40, 40)} {f(x)} {f(y)})"></path>')
    o.append(label(w * 0.5, h * 0.56 + 40 * k, "THE LOT", "#FFD23F", 11))
    return "".join(o)

def cast_forth(w, h, seed, calm=True):
    """Cast forth into the sea, and the sea ceased from its raging: the ship on a stilled sea, the ring of the splash."""
    o = [sky(w, h, "#5A6A8A", "#E8D8C8") if calm else sky(w, h, "#1A1A2A", "#4A4A5E"), clouds(w, h * 0.16, seed, n=5, color="#8A8AA0", op=0.6, h=h),
         sea(w, h, h * 0.56, seed, rough=not calm), ship(w * 0.62, h * 0.66, min(1.3, h / 260))]
    x, y = w * 0.3, h * 0.78
    for k in (1, 1.8, 2.6):
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(26 * k)}" ry="{f(7 * k)}" fill="none" stroke="#E8F6FA" stroke-width="2.4" opacity="{1.2 - k * 0.35:.2f}"></ellipse>')
    return "".join(o)

def vows(p, w, h, seed):
    """The men feared Jehovah exceedingly, and offered a sacrifice, and made vows: the smoke of the offering rising from the
    ship on the calm sea at evening."""
    o = [sky(w, h, "#2A2A5A", "#FFB07A"), sea(w, h, h * 0.58, seed), ship(w * 0.5, h * 0.72, min(1.5, h / 230)),
         smoke(w * 0.42, h * 0.6, 9, seed, color="#E8E2D6", op=0.5, k=max(0.6, h / 300))]
    return "".join(o)

def fish(x, y, s=1.0, flip=False, mouth=0.0, inside=False):
    """A great fish, whale-like: a long dark body with a pale ridged throat, a small eye, a pectoral fin and broad tail;
    (x, y) = its middle. mouth 0..1 opens the jaw; inside=True shows only a dark shape within, faintly lit."""
    sx = -s if flip else s
    jaw = 30 * mouth
    o = (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
         '<path d="M-260 -10 C -300 -60 -330 -70 -350 -84 C -340 -40 -340 30 -352 70 C -330 50 -300 30 -262 10 Z" fill="#2A3A4E" stroke="#0D0D0F" stroke-width="3"></path>'
         f'<path d="M-270 -10 C -200 -70 -40 -90 120 -74 C 200 -66 250 -40 268 -10 L 268 {f(4 + jaw * 0.3)} C 200 {f(10 + jaw)} 120 {f(40 + jaw)} 40 {f(56 + jaw * 0.6)} C -80 74 -200 50 -270 10 Z" fill="#34495E" stroke="#0D0D0F" stroke-width="3"></path>'
         f'<path d="M260 2 C 180 {f(12 + jaw)} 100 {f(34 + jaw)} 20 {f(48 + jaw * 0.6)} C -60 60 -160 46 -230 14 C -150 70 -40 84 40 {f(70 + jaw * 0.6)} C 120 {f(56 + jaw)} 200 {f(30 + jaw)} 262 {f(10 + jaw * 0.4)} Z" fill="#C8D4DA" stroke="#0D0D0F" stroke-width="2.2"></path>')
    for k in range(6):
        o += f'<path d="M{200 - k * 40} {f(18 + jaw * 0.8 - k * 1)} C {170 - k * 40} {f(36 + jaw * 0.6)} {130 - k * 40} {f(52 + jaw * 0.4)} {90 - k * 40} {f(58 + jaw * 0.3)}" stroke="#7A8A96" stroke-width="2" fill="none"></path>'
    o += ('<path d="M40 30 C 20 60 -10 90 -50 104 C -30 76 -10 50 0 30 Z" fill="#2A3A4E" stroke="#0D0D0F" stroke-width="2.4"></path>'
          '<circle cx="190" cy="-20" r="7" fill="#0D0D0F"></circle><circle cx="192" cy="-22" r="2" fill="#E8F6FA"></circle>'
          '<path d="M-60 -84 C -40 -100 -20 -100 0 -86" stroke="#0D0D0F" stroke-width="2" fill="#2A3A4E"></path>')
    if inside:
        o += ('<ellipse cx="-20" cy="-6" rx="90" ry="36" fill="#FFC14D" opacity="0.18"></ellipse>'
              '<path d="M-40 10 C -46 -6 -36 -24 -20 -26 C -6 -28 2 -18 0 -8 C 8 -4 14 6 12 14 Z" fill="#0D0D0F" opacity="0.85"></path>')
    return o + '</g>'

def deep(w, h, seed, fish_=True, inside=False, weeds=True, mountains=False, light=False):
    """The depth, in the heart of the seas: dark water, shafts of light from far above, weeds, and the great fish."""
    r = random.Random(seed)
    o = [hgrad(f"dp{seed}", [("0", "#1F5A7A"), ("0.5", "#0B2A44"), ("1", "#03101E")], vertical=True),
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#dp{seed})"></rect>']
    for i in range(5):
        x = w * r.uniform(0.1, 0.9)
        o.append(f'<path d="M{f(x)} -10 L {f(x + w * 0.06)} -10 L {f(x + w * 0.16)} {f(h * 0.8)} L {f(x + w * 0.1)} {f(h * 0.8)} Z" fill="#8FD0E2" opacity="0.08"></path>')
    if light: o.append(halo(w * 0.5, -h * 0.05, h * 0.6, "#FFE680", 0.5))
    if mountains:
        o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.62)} L {f(w * 0.16)} {f(h * 0.4)} L {f(w * 0.3)} {f(h * 0.7)} L {f(w * 0.52)} {f(h * 0.34)} L {f(w * 0.7)} {f(h * 0.66)} L {f(w * 0.86)} {f(h * 0.44)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} Z" fill="#06121E" stroke="#1F4A6A" stroke-width="2"></path>')
    for i in range(14):
        x, y = r.uniform(0, w), r.uniform(0, h)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(1.5, 4))}" fill="none" stroke="#8FD0E2" stroke-width="1" opacity="0.5"></circle>')
    if fish_:
        o.append(fish(w * 0.52, h * 0.52, min(w / 760, h / 300) * 1.0, flip=r.random() < 0.5, inside=inside))
    if weeds:
        for i in range(10):
            x = w * (i + 0.5) / 10 + r.uniform(-14, 14); hh = h * r.uniform(0.2, 0.4)
            o.append(f'<path d="M{f(x)} {f(h + 4)} C {f(x - 16)} {f(h - hh * 0.4)} {f(x + 16)} {f(h - hh * 0.7)} {f(x - 6)} {f(h - hh)}" stroke="#2E6B3A" stroke-width="5" fill="none" stroke-linecap="round"></path>')
    return "".join(o)

def bars(w, h, seed):
    """I went down to the bottoms of the mountains; the earth with its bars closed upon me: the roots of the mountains and
    the sea floor barred like a gate."""
    o = [deep(w, h, seed, fish_=False, mountains=True, weeds=False)]
    for i in range(11):
        x = w * (i + 0.5) / 11
        o.append(f'<path d="M{f(x)} {f(h * 0.5)} L {f(x)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="7"></path><path d="M{f(x)} {f(h * 0.5)} L {f(x)} {f(h + 10)}" stroke="#3A4A5A" stroke-width="3"></path>')
    o.append(f'<path d="M-10 {f(h * 0.56)} L {f(w + 10)} {f(h * 0.56)} M-10 {f(h * 0.84)} L {f(w + 10)} {f(h * 0.84)}" stroke="#3A4A5A" stroke-width="5"></path>')
    return "".join(o)

def temple_far(w, h, seed):
    """Yet I will look again toward thy holy temple: from the deep, the light far above, and the house on its hill at the
    top of the panel (seen as through the water)."""
    o = [deep(w, h, seed, fish_=False, weeds=True, light=True),
         f'<g opacity="0.55">{temple_front(w * 0.5, h * 0.3, w * 0.2, seed)}</g>', fish(w * 0.5, h * 0.7, min(w / 760, h / 300) * 0.7, flip=True, inside=True)]
    return "".join(o)

def dry_land(p, w, h, seed):
    """It vomited out Jonah upon the dry land: the great fish turning away in the surf, a dark shape on the sand."""
    o = [sky(w, h, "#FFE6A0", "#F3C890"), sea(w, h, h * 0.48, seed), fish(w * 0.66, h * 0.62, min(w / 1100, h / 520), flip=False, mouth=0.4),
         f'<path d="M-10 {f(h * 0.74)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.5)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.84)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2.2"></path>',
         E.kneel(w * 0.2, h * 0.92, fit(h * 0.92, h * 0.6) * 0.9, color="#0D0D0F")]
    return "".join(o)

def nineveh_great(p, w, h, seed, jonah=True, sack=False, dusk=False):
    """Nineveh, that great city, an exceeding great city of three days' journey: walls and towers to the horizon, a stepped
    temple-tower, the river; Jonah at the gate crying (sack=True: the people in sackcloth on the walls and before the gate)."""
    b = h * 0.96
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A", "#E8803A") if dusk else sky(w, h, "#E8C890", "#F3E8C8")]
    for k in range(3):
        o.append(walls(w * (-0.05 + k * 0.08), w * (1.05 - k * 0.04), h * (0.42 + k * 0.1), h * (0.12 + k * 0.05), seed + k, color=["#B8986A", "#C8A878", "#D8B888"][k], towers=4 + k, gate=k == 2))
        if k == 0:
            for i in range(4):
                x, wd = w * 0.62, w * (0.26 - i * 0.05)
                o.append(f'<rect x="{f(x - wd / 2)}" y="{f(h * (0.3 - i * 0.07))}" width="{f(wd)}" height="{f(h * 0.07)}" fill="{["#A8804A", "#B8905A", "#C8A06A", "#D8B07A"][i]}" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(ground(w, h, h * 0.78, "#C8A878", dy=0))
    o.append(river(w, h * 0.84, h * 0.06, seed=seed))
    s = fit(b, h * 0.5)
    if jonah: o.append(jonah_fig(p, w * 0.22, b, s, up=[(22, -158), (40, -176), (58, -196)]))
    if sack:
        o.append(crowd(p, w * 0.42, w * 0.96, b, h * 0.56, 8, seed, colors=(SACK, "#5A4A3A", "#7A6A58"), flip=None))
    return "".join(o)

def sackcloth(p, w, h, seed):
    """From the greatest of them even to the least of them: the people in sackcloth, kneeling and bowed, in the street."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), sky(w, h, "#6A6A7A", "#C8B8A0"), walls(w * -0.05, w * 1.05, h * 0.5, h * 0.24, seed, color="#A8906A", towers=4, gate=False),
         ground(w, h, h * 0.54, "#8A7A60", dy=0)]
    r = random.Random(seed)
    for i in range(9):
        x = w * (0.06 + i * 0.11); bb = b - (i % 2) * h * 0.06
        if i % 3 == 1: o.append(E.kneel(x, bb, fit(bb, h * 0.62) * 0.9, color=SACK, flip=i % 2 == 0))
        else: o.append(figure(p, x, bb, h * 0.5 + (i % 2) * h * 0.06, r.choice([SACK, "#5A4A3A", "#7A6A58"]), "woman" if i % 4 == 0 else "man", flip=i % 2 == 0))
    return "".join(o)

def king_ashes(p, w, h, seed):
    """The king of Nineveh arose from his throne, laid his robe from him, covered him with sackcloth and sat in ashes: the
    empty throne between the winged bulls, the robe on its step, the king sitting in the ash below."""
    from est.art import lamassu
    b = h * 0.94
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A2A"></rect>',
         f'<rect x="-10" y="{f(h * 0.12)}" width="{f(w + 20)}" height="{f(h * 0.08)}" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="2"></rect>',
         lamassu(w * 0.14, h * 0.82, min(0.9, h / 400)), lamassu(w * 0.86, h * 0.82, min(0.9, h / 400), flip=True),
         f'<rect x="-10" y="{f(h * 0.82)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2"></rect>']
    tx, ty, k = w * 0.62, h * 0.82, min(1.2, h / 300)
    o.append(f'<g transform="translate({f(tx)} {f(ty)}) scale({f(k)})"><rect x="-50" y="-150" width="100" height="18" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             '<rect x="-46" y="-132" width="92" height="70" fill="#C8963E" stroke="#0D0D0F" stroke-width="2.4"></rect><rect x="-60" y="-62" width="120" height="16" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             '<path d="M-50 -46 L -50 0 M50 -46 L 50 0" stroke="#8A5A1E" stroke-width="10"></path>'
             '<path d="M-70 0 C -60 -20 -20 -26 0 -18 C 20 -26 60 -20 74 0 Z" fill="#6A1A5A" stroke="#0D0D0F" stroke-width="2.4"></path></g>')
    o.append(f'<ellipse cx="{f(w * 0.34)}" cy="{f(b)}" rx="{f(w * 0.14)}" ry="{f(h * 0.04)}" fill="#A8A29A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    o.append(seated(w * 0.32, b, min(1.4, h / 220), SACK, head=SACK, beard="#1A1210", bowed=True))
    return "".join(o)

def decree(p, w, h, seed):
    """Let neither man nor beast, herd nor flock, taste anything: a herald with the decree on the wall, the herds and flocks
    standing unfed by empty troughs, the beasts covered with sackcloth."""
    from samuel1 import cow
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#7A7A8A", "#D8C8B0"), walls(w * 0.3, w * 1.05, h * 0.44, h * 0.22, seed, color="#B8986A", towers=3, gate=False),
         ground(w, h, h * 0.48, "#9A8A6A", dy=0)]
    s = fit(h * 0.3, h * 0.08)
    o.append(man(p, w * 0.58, h * 0.3, s * 0.6, "#5A3A6A", up=[(22, -158), (38, -180), (34, -206)]) + scroll(w * 0.62, h * 0.08, w * 0.08, h * 0.06, lines=3))
    k = min(0.8, h / 400)
    for i in range(3):
        x = w * (0.12 + i * 0.16)
        o.append(f'<rect x="{f(x - 40 * k)}" y="{f(b - 18 * k)}" width="{f(80 * k)}" height="{f(18 * k)}" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(cow(w * 0.18, b - 4, k * 0.9) + cow(w * 0.42, b - 10, k * 0.8, flip=True))
    o.append(sheep_row(w * 0.62, w * 0.96, b, 4, seed, s=k * 0.7))
    o.append("".join(f'<path d="M{f(w * x - 30 * k)} {f(b - 70 * k)} l {f(60 * k)} 0 l 6 {f(30 * k)} l {f(-72 * k)} 0 Z" fill="{SACK}" stroke="#0D0D0F" stroke-width="1.4" opacity="0.9"></path>' for x in (0.18, 0.42)))
    return "".join(o)

def booth(p, w, h, seed, stage="booth"):
    """On the east side of the city: Jonah sitting under his booth, watching the city. stage 'booth', 'gourd' (the gourd
    grown over it, green and shading), 'worm' (the gourd withered, the worm on its stem) or 'wind' (the sun beating and the
    sultry east wind, Jonah fainting)."""
    b = h * 0.94
    hot = stage in ("wind",)
    o = [sky(w, h, "#FFE680", "#FFB04A") if hot else sky(w, h, "#8FD0E2", "#F3E8C8")]
    o.append(sun(w * 0.82, h * 0.16, max(14, h * 0.07), color="#FFF4C2" if hot else "#FFE680", op=0.7 if hot else 0.4))
    o.append(walls(w * 0.52, w * 1.02, h * 0.5, h * 0.16, seed, color="#C8A878", towers=3, gate=False))
    o.append(ground(w, h, h * 0.52, "#D8B880", dy=0))
    if hot: o.append(wind_lines(w, h, seed, n=10, color="#FFF4C2", op=0.6, y0=0.3, y1=0.9))
    bx, k = w * 0.26, min(1.3, h / 300)
    o.append(f'<g transform="translate({f(bx)} {f(b)}) scale({f(k)})"><path d="M-90 0 L -84 -120 M90 0 L 84 -120 M-90 -120 L 92 -122" stroke="#6A4A2A" stroke-width="7" fill="none" stroke-linecap="round"></path>'
             + "".join(f'<path d="M{-96 + i * 24} -124 l 12 -8 l 14 8" stroke="#8A6A3A" stroke-width="4" fill="none"></path>' for i in range(8)) + '</g>')
    if stage in ("gourd", "worm", "wind"):
        dead = stage != "gourd"
        leaf, stem = ("#8A7A3A", "#6A5A2A") if dead else ("#3F8A34", "#2E6A2A")
        o.append(f'<path d="M{f(bx - 100 * k)} {f(b)} C {f(bx - 110 * k)} {f(b - 80 * k)} {f(bx - 100 * k)} {f(b - 140 * k)} {f(bx - 40 * k)} {f(b - 150 * k)} C {f(bx + 20 * k)} {f(b - 160 * k)} {f(bx + 80 * k)} {f(b - 150 * k)} {f(bx + 110 * k)} {f(b - 130 * k)}" stroke="{stem}" stroke-width="{f(6 * k)}" fill="none"></path>')
        r = random.Random(seed)
        for i in range(10):
            lx, ly = bx + (-100 + i * 22) * k, b - (130 + r.uniform(0, 34)) * k
            if dead:
                o.append(f'<path d="M{f(lx)} {f(ly)} c {f(-10 * k)} {f(10 * k)} {f(-6 * k)} {f(26 * k)} {f(4 * k)} {f(34 * k)} c {f(8 * k)} {f(-10 * k)} {f(8 * k)} {f(-22 * k)} {f(-4 * k)} {f(-34 * k)} Z" fill="{leaf}" stroke="#0D0D0F" stroke-width="1.4"></path>')
            else:
                o.append(f'<path d="M{f(lx)} {f(ly)} c {f(-26 * k)} {f(-6 * k)} {f(-30 * k)} {f(20 * k)} {f(-10 * k)} {f(26 * k)} c {f(16 * k)} {f(6 * k)} {f(32 * k)} {f(-14 * k)} {f(10 * k)} {f(-26 * k)} Z" fill="{leaf}" stroke="#0D0D0F" stroke-width="1.6"></path>')
        if stage == "worm":
            wx, wy = bx - 104 * k, b - 60 * k
            o.append(f'<path d="M{f(wx - 4 * k)} {f(wy)} c {f(6 * k)} {f(-6 * k)} {f(10 * k)} {f(6 * k)} {f(16 * k)} 0 c {f(6 * k)} {f(-6 * k)} {f(10 * k)} {f(6 * k)} {f(16 * k)} 0" stroke="#E8C8A8" stroke-width="{f(5 * k)}" fill="none" stroke-linecap="round"></path>')
    o.append(seated(bx + 10 * k, b, k * (0.62 if stage != "wind" else 0.6), JONAH_C, head=JONAH_C, beard="#4A2A1A", flip=True, bowed=stage == "wind"))
    return "".join(o)

def worm_close(w, h, seed):
    """When the morning rose the next day, a worm smote the gourd, that it withered: the stem close up at dawn, the worm
    in it, the leaves above already drooping."""
    o = [sky(w, h, "#5A4A7A", "#FFB07A"), sun(w * 0.8, h * 0.8, max(14, h * 0.07), color="#FFC14D", op=0.4)]
    k = min(1.6, h / 220)
    o.append(f'<path d="M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.32)} {f(h * 0.6)} {f(w * 0.28)} {f(h * 0.3)} {f(w * 0.4)} {f(h * 0.06)}" stroke="#4A6A2A" stroke-width="{f(14 * k)}" fill="none"></path>')
    for i in range(4):
        x, y = w * (0.36 + i * 0.12), h * (0.1 + i * 0.05)
        o.append(f'<path d="M{f(x)} {f(y)} c {f(-30 * k)} {f(10 * k)} {f(-24 * k)} {f(50 * k)} {f(6 * k)} {f(60 * k)} c {f(20 * k)} {f(-20 * k)} {f(16 * k)} {f(-50 * k)} {f(-6 * k)} {f(-60 * k)} Z" fill="#8A8A3A" stroke="#0D0D0F" stroke-width="1.8"></path>')
    wx, wy = w * 0.31, h * 0.62
    o.append(f'<ellipse cx="{f(wx)}" cy="{f(wy)}" rx="{f(10 * k)}" ry="{f(5 * k)}" fill="#2A1A10"></ellipse>'
             f'<path d="M{f(wx)} {f(wy)} c {f(10 * k)} {f(-10 * k)} {f(18 * k)} {f(6 * k)} {f(28 * k)} 0 c {f(8 * k)} {f(-8 * k)} {f(14 * k)} {f(6 * k)} {f(22 * k)} {f(-2 * k)}" stroke="#E8C8A8" stroke-width="{f(7 * k)}" fill="none" stroke-linecap="round"></path>'
             f'<circle cx="{f(wx + 50 * k)}" cy="{f(wy - 2 * k)}" r="{f(3.4 * k)}" fill="#3A2A1A"></circle>')
    return "".join(o)

def sixscore(p, w, h, seed):
    """Nineveh, that great city, wherein are more than sixscore thousand persons, and also much cattle: the city at evening,
    its lamps lit, herds on the plain before it."""
    from samuel1 import cow
    o = [nineveh_great(p, w, h, seed, jonah=False, dusk=True)]
    k = min(0.6, h / 500)
    for i in range(5): o.append(cow(w * (0.1 + i * 0.18), h * 0.97, k * (0.9 + (i % 2) * 0.1), flip=i % 2 == 1))
    return "".join(o)
