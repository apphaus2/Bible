"""Drawings for the Nahum volume, on the minor prophets' kit (oba.minor), with Jonah's Nineveh (jon.art.nineveh_great).
The fall of Nineveh is words over the city and its river gates: the whirlwind and the storm, the over-running flood, the
chariots raging in the streets by torchlight, the gates of the rivers opened, the spoil carried out, the empty den of
the lions, the chariots burning in the smoke; No-amon among the rivers; the fortresses like fig-trees; the brickkiln; the
locusts in the hedges; the people scattered on the mountains. No one slain is drawn."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from oba.minor import *
from jon.art import nineveh_great
from job.art import whirl
import exodus2 as E2

def nineveh_wall(w, h, seed, color="#B8986A", lit=False, burning=False, gates=False, base=0.7, water=None):
    """Nineveh's great wall seen close: towers, battlements, the city's roofs behind; gates=True puts the river gates in it
    (arched sluices over the channel), water=True floods them."""
    o = [walls(-10, w + 10, h * base, h * 0.44, seed, color=color, lit=lit, gate=not gates, towers=5)]
    if gates:
        for i in range(3):
            x = w * (0.2 + i * 0.3); gw = w * 0.07
            o.append(f'<path d="M{f(x - gw)} {f(h * base)} L {f(x - gw)} {f(h * (base - 0.12))} Q {f(x)} {f(h * (base - 0.2))} {f(x + gw)} {f(h * (base - 0.12))} L {f(x + gw)} {f(h * base)} Z" fill="#0B1A2A" stroke="#0D0D0F" stroke-width="2.4"></path>'
                     + "".join(f'<path d="M{f(x - gw + k * gw / 3)} {f(h * (base - 0.15))} L {f(x - gw + k * gw / 3)} {f(h * base)}" stroke="#3A3A44" stroke-width="3"></path>' for k in range(1, 6) if not water))
    if burning: o.append(fires(0, w, h * (base - 0.2), h * 0.3, seed, n=6) + smokes([w * 0.2, w * 0.5, w * 0.8], h * 0.2, seed, k=max(0.6, h / 360), color="#2A1A1E"))
    return "".join(o)

def whirlwind(w, h, seed):
    """Jehovah hath his way in the whirlwind and in the storm, and the clouds are the dust of his feet; he rebuketh the sea
    and maketh it dry; the mountains quake (God is not drawn)."""
    o = [sky(w, h, "#0B0B1A", "#4A3A5A"), clouds(w, h * 0.1, seed, n=8, color="#2A2238", op=0.95, h=h),
         whirl(w * 0.66, h * 0.06, h * 0.8, w * 0.36, w * 0.04, seed, color="#C8C0D8", op=0.45),
         bolt(w * 0.22, 0, h * 0.42, seed), hills(w, h, h * 0.66, seed, color="#2A2232", amp=30, step=90),
         ground(w, h, h * 0.78, "#5A4A3A", dy=0)]
    r = random.Random(seed)
    for i in range(6):
        x = r.uniform(0, w)
        o.append(f'<path d="M{f(x)} {f(h * 0.8)} l {f(r.uniform(-30, 30))} {f(h * 0.08)} l {f(r.uniform(-20, 20))} {f(h * 0.1)}" stroke="#2A1A10" stroke-width="2.4" fill="none"></path>')
    return "".join(o)

def flood(w, h, seed):
    """Jehovah is a stronghold in the day of trouble; but with an over-running flood he will make a full end of her place: a
    rock fortress standing high and lit, the flood breaking over the city walls below."""
    o = [sky(w, h, "#2A3A5A", "#8AA8C8"), f'<path d="M{f(w * 0.02)} {f(h * 0.7)} L {f(w * 0.08)} {f(h * 0.18)} L {f(w * 0.3)} {f(h * 0.14)} L {f(w * 0.36)} {f(h * 0.7)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.2"></path>',
         walls(w * 0.06, w * 0.32, h * 0.18, h * 0.12, seed, lit=True, towers=2, gate=False), halo(w * 0.19, h * 0.14, h * 0.3, "#FFE680", 0.4),
         walls(w * 0.44, w * 1.04, h * 0.66, h * 0.24, seed + 1, color="#9A8A6A", towers=3)]
    from jon.art import swell
    o.append(swell(w, h, h * 0.58, seed, color="#3A5A6A", foam="#E8F6FA", n=4, amp=0.1))
    return "".join(o)

def thorns_fire(w, h, seed):
    """Entangled like thorns, drunken as with their drink, consumed utterly as dry stubble: a tangle of thorns and an
    overturned cup, the stubble burning."""
    r = random.Random(seed)
    o = [sky(w, h, "#2A0A0A", "#8A3A1A"), ground(w, h, h * 0.62, "#3A1E14", dy=0), grain(-10, w + 10, h * 0.98, h * 0.12, seed, color="#C8A060"),
         fires(w * 0.4, w + 10, h * 0.98, h * 0.4, seed, n=5)]
    for i in range(30):
        x, y = r.uniform(0, w * 0.4), h * r.uniform(0.66, 0.98)
        o.append(f'<path d="M{f(x)} {f(y)} c {f(r.uniform(-20, 20))} {f(-r.uniform(10, 30))} {f(r.uniform(-20, 20))} {f(-r.uniform(10, 30))} {f(r.uniform(-30, 30))} {f(-r.uniform(5, 20))}" stroke="#1A0E08" stroke-width="2.6" fill="none"></path>')
    o.append(f'<g transform="rotate(-80 {f(w * 0.28)} {f(h * 0.94)})">{cup(w * 0.28, h * 0.94, min(0.7, h / 360), spill=True)}</g>')
    return "".join(o)

def broken_yoke(w, h, seed):
    """I will break his yoke from off thee, and will burst thy bonds in sunder: the yoke snapped in two, the cords burst,
    light breaking in."""
    o = [sky(w, h, "#3A3A6A", "#FFD8A0"), rays(w * 0.5, h * 0.3, 24, h * 0.1, max(w, h), "#FFF4C2", 0.25, 4), ground(w, h, h * 0.66, "#8A7A5A", dy=0)]
    k = min(1.5, h / 220); x, y = w * 0.5, h * 0.62
    for side, rot in ((-1, -14), (1, 16)):
        o.append(f'<g transform="translate({f(x + side * 40 * k)} {f(y)}) rotate({rot}) scale({f(k)})"><path d="M{0 if side > 0 else -110} -10 C {-40 if side < 0 else 40} -20 {-20 if side < 0 else 20} -20 {side * 4} -14 L {side * 4} 2 L {0 if side > 0 else -110} 6 Z" '
                 f'fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.4" transform="scale({1 if side < 0 else 1} 1) translate({0 if side < 0 else 0} 0)"></path>'
                 f'<path d="M{side * 4} -14 l {side * 8} 4 l {-side * 6} 6 l {side * 8} 4" stroke="#0D0D0F" stroke-width="2" fill="none"></path></g>')
    for side in (-1, 1):
        o.append(f'<path d="M{f(x + side * 160 * k)} {f(y + 30 * k)} C {f(x + side * 120 * k)} {f(y + 10 * k)} {f(x + side * 100 * k)} {f(y + 40 * k)} {f(x + side * 70 * k)} {f(y + 20 * k)}" stroke="#C8A060" stroke-width="{f(4 * k)}" fill="none"></path>')
    o.append(mk.speed(x, y - 10 * k, 18, 20 * k, 90 * k, seed, color="#FFF4C2", op=0.7))
    return "".join(o)

def tidings(p, w, h, seed):
    """Behold, upon the mountains the feet of him that bringeth good tidings, that publisheth peace: a runner on the
    mountain ridge at dawn, his arm raised."""
    o = [sky(w, h, "#2A2A5A", "#FFC890"), sun(w * 0.7, h * 0.56, max(14, h * 0.06), color="#FFE680", op=0.5), hills(w, h, h * 0.62, seed, color="#5A3A5A", amp=20),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.8)} L {f(w * 0.3)} {f(h * 0.56)} L {f(w * 0.5)} {f(h * 0.62)} L {f(w * 0.8)} {f(h * 0.82)} L {f(w + 10)} {f(h * 0.9)} L {f(w + 10)} {f(h + 10)} Z" fill="#3A2A3A" stroke="#0D0D0F" stroke-width="2.2"></path>',
         mk.defs(p, *ALL)]
    b = h * 0.58
    o.append(man(p, w * 0.32, b, fit(b, h * 0.22), "#E8E2D6", up=[(22, -158), (40, -176), (58, -196)]))
    return "".join(o)

def chariots_streets(p, w, h, seed, night_=False):
    """The chariots rage in the streets, they rush to and fro in the broad ways, like torches, like the lightnings; the
    shields made red, the valiant men in scarlet: the chariots racing before the walls, each with a red shield hung on its
    side and its driver in scarlet."""
    o = [sky(w, h, "#2A0A1A", "#C8502A") if night_ else sky(w, h, "#8A5A3A", "#E8B880"), nineveh_wall(w, h, seed, base=0.56, lit=night_)]
    o.append(ground(w, h, h * 0.56, "#6A4A3A", dy=0))
    k = min(0.9, h / 320)
    for i, (x, fl) in enumerate(((0.24, False), (0.62, True), (0.86, False))):
        y = h * (0.86 + (i % 2) * 0.08); s = k * (0.8 + 0.1 * (i % 2)); sx = -1 if fl else 1
        o.append(E3.chariot(w * x, y, s, flip=fl, color="#3A1A10", driver="#B5121B") + mk.speed(w * x + (60 if not fl else -60) * k, y - 50 * k, 8, 10 * k, 80 * k, seed + i, color="#FFC14D", op=0.6))
        o.append(f'<circle cx="{f(w * x + sx * -160 * s)}" cy="{f(y - 120 * s)}" r="{f(9 * s)}" fill="{SKIN}" stroke="#0D0D0F" stroke-width="1.6"></circle>'
                 f'<path d="M{f(w * x + sx * -172 * s)} {f(y - 124 * s)} C {f(w * x + sx * -164 * s)} {f(y - 136 * s)} {f(w * x + sx * -150 * s)} {f(y - 134 * s)} {f(w * x + sx * -148 * s)} {f(y - 124 * s)} Z" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="1.4"></path>'
                 f'<circle cx="{f(w * x + sx * -128 * s)}" cy="{f(y - 56 * s)}" r="{f(17 * s)}" fill="#B5121B" stroke="#0D0D0F" stroke-width="2"></circle>'
                 f'<circle cx="{f(w * x + sx * -128 * s)}" cy="{f(y - 56 * s)}" r="{f(5 * s)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></circle>')
    return "".join(o)

def river_gates(w, h, seed, open_=True):
    """The gates of the rivers are opened, and the palace is dissolved: the wall's river gates burst, the flood pouring
    through into the city."""
    o = [sky(w, h, "#3A4A6A", "#B8A890"), nineveh_wall(w, h, seed, base=0.62, gates=True, water=open_)]
    if open_:
        for i in range(3):
            x = w * (0.2 + i * 0.3)
            o.append(f'<path d="M{f(x - w * 0.07)} {f(h * 0.62)} C {f(x - w * 0.1)} {f(h * 0.75)} {f(x - w * 0.16)} {f(h * 0.85)} {f(x - w * 0.2)} {f(h + 10)} L {f(x + w * 0.2)} {f(h + 10)} C {f(x + w * 0.16)} {f(h * 0.85)} {f(x + w * 0.1)} {f(h * 0.75)} {f(x + w * 0.07)} {f(h * 0.62)} Z" fill="#2C7DA8" stroke="#0D0D0F" stroke-width="2"></path>'
                     + "".join(f'<path d="M{f(x + dx * w * 0.03)} {f(h * 0.66)} C {f(x + dx * w * 0.05)} {f(h * 0.8)} {f(x + dx * w * 0.08)} {f(h * 0.9)} {f(x + dx * w * 0.1)} {f(h)}" stroke="#CFEFFF" stroke-width="2.4" fill="none"></path>' for dx in (-1, 0, 1)))
        o.append(f'<rect x="-10" y="{f(h * 0.94)}" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#2C7DA8"></rect>')
    else:
        o.append(river(w, h * 0.8, h * 0.1, seed=seed))
    return "".join(o)

def spoil(w, h, seed):
    """Take ye the spoil of silver, take the spoil of gold: the treasure-house emptied, gold and silver vessels heaped at
    its open door; she is empty, and void, and waste."""
    from est.art import vessel
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A14"></rect>',
         f'<rect x="{f(w * 0.06)}" y="{f(h * 0.1)}" width="{f(w * 0.4)}" height="{f(h * 0.8)}" fill="#4A3424" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.16)}" y="{f(h * 0.34)}" width="{f(w * 0.2)}" height="{f(h * 0.56)}" fill="#0D0806" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(h * 0.88)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2"></rect>']
    r = random.Random(seed); k = min(0.9, h / 300)
    for i in range(9):
        x = w * (0.5 + (i % 5) * 0.1); y = h * (0.9 - (i // 5) * 0.12)
        o.append(vessel(x, y, k * 0.8, r.choice(["cup", "amphora", "bowl", "ewer"]), color=r.choice(["#E8B830", "#C8C8D0"])))
    return "".join(o)

def lions_den(w, h, seed):
    """Where is the den of the lions, the feeding-place of the young lions? an empty den in the rocks, and on the broken
    palace wall a carved lion fallen."""
    o = [sky(w, h, "#5A4A4A", "#C8A080"), f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.3)} C {f(w * 0.2)} {f(h * 0.1)} {f(w * 0.5)} {f(h * 0.2)} {f(w * 0.6)} {f(h * 0.5)} L {f(w * 0.66)} {f(h + 10)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.14)} {f(h * 0.94)} C {f(w * 0.12)} {f(h * 0.56)} {f(w * 0.44)} {f(h * 0.5)} {f(w * 0.46)} {f(h * 0.94)} Z" fill="#1A0E08" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.92, "#6A5A40", dy=0), ruin(w * 0.66, w + 10, h * 0.94, h * 0.3, seed)]
    from ecc.art import lion_lying
    o.append(f'<g transform="rotate(-8 {f(w * 0.8)} {f(h * 0.9)})">{lion_lying(w * 0.8, h * 0.92, min(0.8, h / 300), color="#B8A07A")}</g>')
    return "".join(o)

def wreck(x, y, s, flip=False, rot=-12):
    """A war chariot overturned and burnt black: its body tipped, one wheel broken off (no horse, no driver)."""
    sx = -s if flip else s
    o = (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)}) rotate({rot})">'
         '<path d="M-30 -30 L -30 -78 L 40 -78 C 54 -66 56 -46 50 -30 Z" fill="#1A1210" stroke="#0D0D0F" stroke-width="2.4"></path>'
         '<path d="M-24 -70 L 40 -70 M-24 -46 L 48 -46" stroke="#4A2A1A" stroke-width="3"></path>'
         '<path d="M50 -40 L 120 -20" stroke="#2A1A10" stroke-width="6"></path>'
         '<circle cx="0" cy="-26" r="26" fill="none" stroke="#0D0D0F" stroke-width="7"></circle><circle cx="0" cy="-26" r="26" fill="none" stroke="#3A2414" stroke-width="4"></circle>'
         + "".join(f'<path d="M0 -26 L {f(26 * math.cos(a))} {f(-26 + 26 * math.sin(a))}" stroke="#2A1A10" stroke-width="3"></path>' for a in [i * math.pi / 3 for i in range(6)])
         + '</g>')
    return o + (f'<g transform="translate({f(x + (70 if not flip else -70) * s)} {f(y)}) scale({f(s)})"><ellipse cx="0" cy="-6" rx="26" ry="8" fill="none" stroke="#0D0D0F" stroke-width="6"></ellipse>'
                '<ellipse cx="0" cy="-6" rx="26" ry="8" fill="none" stroke="#3A2414" stroke-width="3"></ellipse></g>')

def burnt_chariots(w, h, seed):
    """I will burn her chariots in the smoke: the chariots overturned and burning before the walls, a great smoke going up
    (no horse or man drawn in the fire)."""
    o = [sky(w, h, "#1A0A0A", "#6A2A1A"), nineveh_wall(w, h, seed, color="#6A5A4A", base=0.6), ground(w, h, h * 0.6, "#2A1810", dy=0),
         smokes([w * 0.15, w * 0.4, w * 0.65, w * 0.9], h * 0.8, seed, k=max(0.8, h / 260), color="#2A2024", op=0.7)]
    k = min(1.1, h / 280)
    for i, x in enumerate((0.18, 0.5, 0.8)):
        o.append(E.blaze(w * x, h * 0.92, w * 0.14, h * 0.26, seed + i, n=5) + wreck(w * x, h * 0.95, k * 0.9, flip=i % 2 == 1))
    return "".join(o)

def bloody_city(w, h, seed):
    """Woe to the bloody city: the noise of the whip and the rattling of wheels, prancing horses, the flashing sword and the
    glittering spear — the walls by night under red light, flashes along them (no one slain is drawn)."""
    o = [sky(w, h, "#0A0508", "#5A0A10"), nineveh_wall(w, h, seed, color="#4A3030", lit=True, base=0.66), ground(w, h, h * 0.66, "#1A0A0C", dy=0)]
    r = random.Random(seed)
    for i in range(10):
        x, y = r.uniform(0, w), r.uniform(h * 0.7, h * 0.96)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.choice([-1, 1]) * 30)} {f(-r.uniform(10, 30))}" stroke="#F3EFE6" stroke-width="2.4"></path>'
                 f'<circle cx="{f(x)}" cy="{f(y)}" r="3" fill="#FFF4C2"></circle>')
    o.append(mk.speed(w * 0.5, h * 0.84, 24, 20, w * 0.5, seed, color="#FF6A2A", op=0.35))
    return "".join(o)

def gazing(p, w, h, seed):
    """Nineveh is laid waste: who will bemoan her? — the city a ruin under smoke, travellers on the far road looking and
    turning away."""
    o = [mk.defs(p, *ALL), sky(w, h, "#5A5A6A", "#C8B8A8"), ruin(w * 0.3, w + 10, h * 0.6, h * 0.3, seed, color="#A8906A"),
         smokes([w * 0.5, w * 0.8], h * 0.4, seed, k=0.6, color="#4A4448"), ground(w, h, h * 0.62, "#9A8A6A", dy=0)]
    b = h * 0.94
    for i, x in enumerate((0.08, 0.16, 0.24)):
        o.append(man(p, w * x, b - i * 4, fit(b, h * 0.6), ["#5A3A6A", "#3A5A4A", "#6A4A2A"][i], flip=True))
    return "".join(o)

def no_amon(w, h, seed):
    """Art thou better than No-amon, situate among the rivers, whose rampart was the sea? — the temple pylons of the city
    of Egypt with the Nile about her, empty under the sun."""
    from egypt import pyramid
    o = [sky(w, h, "#E8C890", "#F3E8C8"), sun(w * 0.84, h * 0.16, max(12, h * 0.05), color="#FFE680", op=0.5), ground(w, h, h * 0.5, "#D8B880", dy=0)]
    for i, x in enumerate((0.3, 0.6)):
        x0 = w * x
        o.append(f'<path d="M{f(x0 - w * 0.12)} {f(h * 0.62)} L {f(x0 - w * 0.1)} {f(h * 0.26)} L {f(x0 - w * 0.02)} {f(h * 0.26)} L {f(x0 - w * 0.02)} {f(h * 0.62)} Z" fill="#E8C890" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<path d="M{f(x0 + w * 0.02)} {f(h * 0.62)} L {f(x0 + w * 0.02)} {f(h * 0.26)} L {f(x0 + w * 0.1)} {f(h * 0.26)} L {f(x0 + w * 0.12)} {f(h * 0.62)} Z" fill="#E8C890" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<rect x="{f(x0 - w * 0.02)}" y="{f(h * 0.4)}" width="{f(w * 0.04)}" height="{f(h * 0.22)}" fill="#3A2214"></rect>')
    o.append(river(w, h * 0.68, h * 0.12, color="#1F6F9A", seed=seed) + river(w, h * 0.88, h * 0.08, color="#1F6F9A", seed=seed + 1))
    return "".join(o)

def fig_fortress(w, h, seed):
    """Thy fortresses like fig-trees with the first-ripe figs: if they be shaken, they fall into the mouth of the eater;
    the gates set wide open, the fire hath devoured thy bars."""
    o = [sky(w, h, "#6A3A2A", "#E8A070"), nineveh_wall(w, h, seed, base=0.6, burning=False), ground(w, h, h * 0.6, "#8A6A4A", dy=0)]
    k = min(1.0, h / 300)
    o.append(fig_tree(w * 0.24, h * 0.98, k, seed=seed))
    r = random.Random(seed)
    for i in range(6):
        x, y = w * r.uniform(0.12, 0.36), h * r.uniform(0.8, 0.95)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(5 * k)}" fill="#6A3A6A" stroke="#0D0D0F" stroke-width="1"></circle>')
    o.append(E.blaze(w * 0.7, h * 0.62, w * 0.1, h * 0.16, seed, n=5))
    return "".join(o)

def brickkiln(p, w, h, seed):
    """Draw thee water for the siege; go into the clay, and tread the mortar; make strong the brickkiln: men treading clay,
    bricks drying in rows, the kiln smoking."""
    from exodus import kneel
    import mk as M
    o = [mk.defs(p, *ALL), sky(w, h, "#8A6A4A", "#E8C890"), nineveh_wall(w, h, seed, base=0.5), ground(w, h, h * 0.5, "#A8805A", dy=0)]
    for row in range(3):
        for i in range(8):
            x = w * (0.04 + i * 0.05); y = h * (0.64 + row * 0.08)
            o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.04)}" height="{f(h * 0.04)}" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    kx = w * 0.82
    o.append(f'<path d="M{f(kx - w * 0.1)} {f(h * 0.94)} L {f(kx - w * 0.08)} {f(h * 0.6)} L {f(kx + w * 0.08)} {f(h * 0.6)} L {f(kx + w * 0.1)} {f(h * 0.94)} Z" fill="#8A5A3A" stroke="#0D0D0F" stroke-width="2.2"></path>'
             f'<path d="M{f(kx - w * 0.03)} {f(h * 0.94)} L {f(kx - w * 0.03)} {f(h * 0.82)} Q {f(kx)} {f(h * 0.78)} {f(kx + w * 0.03)} {f(h * 0.82)} L {f(kx + w * 0.03)} {f(h * 0.94)} Z" fill="#FF8A3D"></path>'
             + smoke(kx, h * 0.56, 7, seed, color="#4A4448", op=0.5, k=max(0.5, h / 400)))
    b = h * 0.96
    o.append(man(p, w * 0.56, b, fit(b, h * 0.56), "#6A5A4A") + man(p, w * 0.66, b, fit(b, h * 0.58), "#5A4A3A", flip=True))
    o.append(f'<ellipse cx="{f(w * 0.61)}" cy="{f(b)}" rx="{f(w * 0.1)}" ry="{f(h * 0.03)}" fill="#7A5A3A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    return "".join(o)

def locust_hedges(w, h, seed):
    """Thy princes are as the locusts, which encamp in the hedges in the cold day, but when the sun ariseth they flee away:
    the hedges at dawn, the swarm rising toward the sun."""
    o = [sky(w, h, "#5A6A8A", "#FFD8A0"), sun(w * 0.8, h * 0.66, max(14, h * 0.07), color="#FFE680", op=0.5), ground(w, h, h * 0.72, "#7A6A4A", dy=0)]
    r = random.Random(seed)
    for i in range(7):
        x = w * (0.02 + i * 0.14)
        o.append("".join(f'<circle cx="{f(x + r.uniform(0, w * 0.12))}" cy="{f(h * r.uniform(0.74, 0.84))}" r="{f(h * 0.05)}" fill="#3A5A2A" stroke="#0D0D0F" stroke-width="1.4"></circle>' for _ in range(4)))
    o.append(E2.locusts(40, w * 0.1, w * 0.9, h * 0.1, h * 0.6, seed, smin=0.15, smax=min(0.5, h / 600)))
    return "".join(o)

def scattered(p, w, h, seed):
    """Thy shepherds slumber, O king of Assyria; thy people are scattered upon the mountains, and there is none to gather
    them: lone figures far apart on the mountains at dusk, the ruin-mound of the city below."""
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A", "#E8803A"), hills(w, h, h * 0.4, seed, color="#4A2A3A", amp=40, step=110),
         hills(w, h, h * 0.58, seed + 1, color="#3A1E2A", amp=30, step=90), ruin(w * 0.3, w * 0.8, h * 0.9, h * 0.12, seed, color="#6A4A3A"),
         ground(w, h, h * 0.9, "#2A1418", dy=0)]
    r = random.Random(seed)
    for i in range(6):
        x, y = w * (0.08 + i * 0.16), h * r.uniform(0.44, 0.62)
        o.append(mk.person(p, round(x), round(y), round(fit(y, y - h * 0.08), 3), body="#0D0D0F", cloth="#1A0E10", sw=1.6, flip=r.random() < 0.5))
    return "".join(o)
