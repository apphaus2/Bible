"""Drawings for Matthew 13–14: the parables drawn as their own scenes (Jesus in the boat off the beach; the sower and the four
grounds; the field at night where the tares were sown, no one drawn; wheat and tares together; the reapers binding the tares
for the fire and the wheat carried to the barn; the mustard tree; the leaven; the treasure in the field; the pearl of great
price; the net drawn up on the beach); Nazareth's synagogue; Herod's birthday feast (no dancer drawn: the lamps and the
empty floor), the prison door and the tomb (John's death in words only); the desert place, the five loaves and two fishes
and the twelve baskets; the mountain at evening; the walking on the sea and Peter caught by the hand; Gennesaret.
Built on mat.art4."""
from mat.art4 import *
from mat.art4 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE
from ntcast import JESUS_SKIN, JESUS_HAIR, JESUS_TUNIC, JESUS_MANTLE, ROBES
import random, math
from job.art import seated, smoke
from ecc.art import loaf
from lev.art3 import creature
import exodus as E

def boat_preach(p, w, h, seed):
    """He entered into a boat and sat, and all the multitude stood on the beach: the boat a little off shore with Jesus
    seated in it, the crowd thick along the beach, the hills behind."""
    b = h * 0.96
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.3, seed, color="#8A9A7A", amp=12, step=90), lake(w, h, h * 0.36, seed, n=10),
         shore(w, h, h * 0.66, x0=w * 0.36, x1=w + 10)]
    s = fit(b, max(h * 0.3, b - 220))
    bx, by = w * 0.18, h * 0.66
    o.append(jesus_seated(bx + 10 * s, by - 14 * s, s * 0.5) + boat(p, bx, by, s * 0.8, mast=True))
    o.append(crowd(p, w * 0.44, w * 0.98, h * 0.78, h * 0.78 - 110 * s, 9, seed, flip=True))
    o.append(crowd(p, w * 0.4, w * 0.96, b, b - 160 * s, 7, seed + 1, flip=True))
    return "".join(o)

def sower(p, w, h, seed, ground_="all"):
    """The sower went forth to sow: a man with a seed-bag casting seed in a wide arc over the field; ground_='all' shows the
    four grounds in a row — the beaten way-side with the birds, the rocky places with the scorched shoots, the thorns, and
    the good ground standing tall."""
    r = random.Random(seed); b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), sun(w * 0.86, h * 0.14, 14, color="#FFE680", op=0.3), hills(w, h, h * 0.36, seed, color="#9AAA7A", amp=12, step=90),
         ground(w, h, h * 0.46, "#8A6A4A", dy=0)]
    z = [w * k / 4 for k in range(5)]
    # 1 way-side: a beaten path, birds
    o.append(f'<rect x="{f(z[0] - 10)}" y="{f(h * 0.6)}" width="{f(z[1] - z[0] + 10)}" height="{f(h * 0.4)}" fill="#B89A70"></rect>')
    o.append("".join(bird(r.uniform(z[0] + 20, z[1] - 20), r.uniform(h * 0.66, h * 0.9), 1.2, "#2A1A10") for _ in range(4)))
    for _ in range(10): o.append(f'<circle cx="{f(r.uniform(z[0] + 10, z[1] - 10))}" cy="{f(r.uniform(h * 0.66, h * 0.96))}" r="2" fill="#E8D8A0"></circle>')
    # 2 rocky places: grey rocks, shoots wilted
    for _ in range(6):
        x = r.uniform(z[1] + 10, z[2] - 20); y = r.uniform(h * 0.66, h * 0.96)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(h * 0.06)}" ry="{f(h * 0.035)}" fill="#9A9488" stroke="{INK}" stroke-width="1.6"></ellipse>')
    for _ in range(8):
        x = r.uniform(z[1] + 10, z[2] - 10); y = r.uniform(h * 0.64, h * 0.96)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x)} {f(y - 14)} {f(x + 6)} {f(y - 18)} {f(x + 10)} {f(y - 12)}" stroke="#A8903A" stroke-width="2" fill="none"></path>')
    # 3 thorns
    for _ in range(9):
        x = r.uniform(z[2] + 10, z[3] - 10); y = r.uniform(h * 0.66, h * 0.98)
        o.append(f'<path d="M{f(x)} {f(y)} l -10 -26 M{f(x)} {f(y)} l 2 -32 M{f(x)} {f(y)} l 12 -24" stroke="#3A4A2A" stroke-width="2.4"></path>'
                 f'<path d="M{f(x - 6)} {f(y - 14)} l -5 -2 M{f(x + 6)} {f(y - 12)} l 5 -3" stroke="#3A4A2A" stroke-width="1.6"></path>')
    # 4 good ground
    o.append(grain(z[3], z[4] + 10, h * 0.98, h * 0.34, seed))
    for k in range(1, 4):
        o.append(f'<path d="M{f(z[k])} {f(h * 0.5)} L {f(z[k])} {f(h + 10)}" stroke="#F3EFE6" stroke-width="1.4" stroke-dasharray="5 5" opacity="0.6"></path>')
    s = fit(h * 0.62, max(h * 0.1, h * 0.62 - 200))
    bag = '<path d="M14 -120 C 30 -116 34 -96 26 -84 C 16 -80 8 -90 10 -104 Z" fill="#C8A060" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(man(p, w * 0.5, h * 0.62, s * 0.7, "#7A5A30", up=[(-22, -158), (-48, -168), (-72, -160)], extra=bag))
    for _ in range(18):
        a = r.uniform(-2.8, -0.4); d = r.uniform(20, 90) * s
        o.append(f'<circle cx="{f(w * 0.5 - 50 * s * 0.7 + math.cos(a) * d)}" cy="{f(h * 0.62 - 120 * s * 0.7 - math.sin(a) * d * 0.4)}" r="1.8" fill="#E8D8A0"></circle>')
    for i, t in enumerate(("THE WAY SIDE", "THE ROCKY PLACES", "THE THORNS", "THE GOOD GROUND")):
        o.append(label(z[i] + w / 8, h * 0.56, t, "#F3EFE6", 9))
    return "".join(o)

def eyes_ears(p, w, h, seed):
    """Seeing they see not, and hearing they hear not: the people on the beach at dusk, shut doors behind them; and in the
    light near the boat, the twelve listening."""
    return boat_preach(p, w, h, seed)

def tares_night(p, w, h, seed):
    """While men slept, his enemy came and sowed tares among the wheat, and went away: the sown field at night under the
    moon, the house dark, a line of footprints across the furrows and away — no one drawn."""
    r = random.Random(seed)
    o = [night(w, h, seed, n=60, top="#05051A", bot="#1E1838"), moon(w * 0.18, h * 0.2, max(8, h * 0.04)), hills(w, h, h * 0.46, seed, color="#1A1630", amp=10, step=90),
         ground(w, h, h * 0.54, "#2A2230", dy=0)]
    for k in range(7):
        y = h * (0.58 + 0.06 * k)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y + 4)}" stroke="#3A3040" stroke-width="2"></path>')
    from job.art import house
    o.append(house(w * 0.82, h * 0.56, w * 0.12, h * 0.16, color="#4A4048"))
    for k in range(12):
        x = w * (0.1 + 0.07 * k); y = h * (0.94 - 0.03 * k) + (8 if k % 2 else -8)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="6" ry="3" fill="#14101A"></ellipse>')
    for _ in range(30):
        o.append(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.6, h))}" r="1.4" fill="#5A5468"></circle>')
    return "".join(o)

def tares_field(p, w, h, seed, servants=True):
    """The blade sprang up and the tares appeared also: the wheat with the dark darnel among it; the householder at the
    field's edge and his servants come to ask him."""
    r = random.Random(seed); b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, color="#9AAA7A", amp=10, step=90), ground(w, h, h * 0.44, "#7A6A3A", dy=0),
         grain(-10, w * 0.7, h * 0.8, h * 0.2, seed, color="#C8B060")]
    for _ in range(26):
        x = r.uniform(0, w * 0.7); y = r.uniform(h * 0.62, h * 0.82)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x + r.uniform(-4, 4))} {f(y - h * 0.16)}" stroke="#3A4A2A" stroke-width="1.6"></path>'
                 f'<ellipse cx="{f(x)}" cy="{f(y - h * 0.16)}" rx="2.4" ry="{f(h * 0.03)}" fill="#3A3A2A"></ellipse>')
    if servants:
        s = fit(b, max(h * 0.3, b - 220))
        o.append(man(p, w * 0.78, b, s, "#5A2A4A", kind="Robe", extra=A.headcloth("#F3EFE6", cord="#E8B830") + GREY_BEARD))
        o.append(man(p, w * 0.62, b, s * 0.94, "#6A5A3A", flip=True, up=UP_BLESS) + man(p, w * 0.54, b, s * 0.92, "#5A4A3A", flip=True))
    o.append(grain(-10, w * 0.46, h * 1.02, h * 0.18, seed + 1, color="#C8B060"))
    return "".join(o)

def reapers(p, w, h, seed):
    """In the time of the harvest: the reapers binding the tares in bundles and throwing them on the fire; the sheaves of
    wheat carried into the barn."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A6A", "#FFC890"), hills(w, h, h * 0.42, seed, color="#8A7A5A", amp=10, step=90), ground(w, h, h * 0.5, "#C8A060", dy=0),
         grain(w * 0.4, w + 10, h * 0.76, h * 0.12, seed, color="#D8B050")]
    from job.art import house
    o.append(house(w * 0.82, h * 0.6, w * 0.16, h * 0.2, color="#B89A6A"))
    o.append(E.blaze(w * 0.16, b, w * 0.2, h * 0.36, seed, n=6))
    s = fit(b, max(h * 0.3, b - 220))
    bundle = '<path d="M-60 -150 L -30 -170 L -20 -150 L -50 -134 Z" fill="#3A3A2A" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(man(p, w * 0.32, b, s, "#6A5A3A", flip=True, up=[(-22, -158), (-40, -166), (-54, -156)], extra=bundle))
    sheaf = '<path d="M10 -230 L 40 -230 L 34 -150 L 16 -150 Z" fill="#E8C060" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(man(p, w * 0.62, b, s * 0.96, "#5A4A3A", up=[(22, -158), (26, -196), (24, -214)], extra=sheaf))
    return "".join(o)

def mustard(p, w, h, seed):
    """The least of all seeds become a tree, so that the birds of the heaven lodge in its branches: a great spreading
    mustard tree in a field, birds among its branches and coming in to it; the tiny seed shown in a hand-span circle."""
    b = h * 0.92
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#9AAA7A", amp=10, step=90), ground(w, h, h * 0.62, "#9AAA5A", dy=0)]
    k = max(0.6, (b - h * 0.08) / 220)
    tx = w * 0.56
    o.append(f'<path d="M{f(tx)} {f(b)} C {f(tx - 6 * k)} {f(b - 60 * k)} {f(tx + 8 * k)} {f(b - 90 * k)} {f(tx)} {f(b - 120 * k)} M{f(tx)} {f(b - 90 * k)} L {f(tx - 60 * k)} {f(b - 150 * k)} M{f(tx)} {f(b - 100 * k)} L {f(tx + 70 * k)} {f(b - 160 * k)}" stroke="#6A5040" stroke-width="{f(12 * k)}" fill="none" stroke-linecap="round"></path>')
    r = random.Random(seed)
    for _ in range(16):
        o.append(f'<circle cx="{f(tx + r.uniform(-110, 110) * k)}" cy="{f(b - r.uniform(130, 210) * k)}" r="{f(r.uniform(22, 36) * k)}" fill="{r.choice(["#5A8A3A", "#6A9A3A", "#4A7A2A"])}" stroke="{INK}" stroke-width="1.6"></circle>')
    for _ in range(6):
        o.append(f'<circle cx="{f(tx + r.uniform(-80, 80) * k)}" cy="{f(b - r.uniform(140, 200) * k)}" r="{f(3 * k)}" fill="#E8C030"></circle>')
    o.append(birds(7, w * 0.3, w * 0.9, h * 0.06, h * 0.3, seed))
    cx, cy, cr = w * 0.14, h * 0.3, min(w, h) * 0.12
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(cr)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></circle><circle cx="{f(cx)}" cy="{f(cy)}" r="2.4" fill="#5A3A1A"></circle>'
             + label(cx, cy + cr + 14, "A GRAIN OF MUSTARD SEED", "#0D0D0F", 9))
    return "".join(o)

def leaven(p, w, h, seed):
    """Leaven, which a woman took, and hid in three measures of meal: a woman kneeling at the kneading-trough, the dough
    risen high and rounded, three sacks of meal beside her."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#C8A878", window=(w * 0.8, w * 0.1)), A.lamp(w * 0.12, h * 0.34, max(0.6, h / 300))]
    s = fit(b, max(h * 0.2, b - 230))
    tx = w * 0.5
    o.append(f'<path d="M{f(tx - 110 * s)} {f(b - 60 * s)} L {f(tx + 110 * s)} {f(b - 60 * s)} L {f(tx + 90 * s)} {f(b)} L {f(tx - 90 * s)} {f(b)} Z" fill="#8A5A30" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(tx - 100 * s)} {f(b - 60 * s)} C {f(tx - 90 * s)} {f(b - 120 * s)} {f(tx + 90 * s)} {f(b - 120 * s)} {f(tx + 100 * s)} {f(b - 60 * s)} Z" fill="#F3E8C8" stroke="{INK}" stroke-width="2"></path>')
    o.append(E.kneel(tx - 160 * s, b, s * 0.9, color="#7A3A5A", skin=SKIN))
    for i in range(3):
        x = w * (0.72 + 0.08 * i)
        o.append(f'<path d="M{f(x - 22 * s)} {f(b)} C {f(x - 30 * s)} {f(b - 40 * s)} {f(x - 20 * s)} {f(b - 70 * s)} {f(x)} {f(b - 72 * s)} C {f(x + 20 * s)} {f(b - 70 * s)} {f(x + 30 * s)} {f(b - 40 * s)} {f(x + 22 * s)} {f(b)} Z" fill="#E8D8B0" stroke="{INK}" stroke-width="2"></path>')
    return "".join(o)

def treasure_field(p, w, h, seed, joy=False):
    """A treasure hidden in the field: a man with a mattock in a field, the earth thrown up, the lid of a buried chest and
    the gold showing; joy=True: the man going off with his arms raised."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#9AAA7A", amp=10, step=90), ground(w, h, h * 0.5, "#9A7A4A", dy=0)]
    s = fit(b, max(h * 0.24, b - 220))
    cx = w * 0.5
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(b - 6)}" rx="{f(80 * s)}" ry="{f(22 * s)}" fill="#5A3A22" stroke="{INK}" stroke-width="2"></ellipse>'
             f'<rect x="{f(cx - 40 * s)}" y="{f(b - 30 * s)}" width="{f(80 * s)}" height="{f(30 * s)}" fill="#7A5A30" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<circle cx="{f(cx - 30 * s + i * 12 * s)}" cy="{f(b - 32 * s)}" r="{f(6 * s)}" fill="#E8B830" stroke="{INK}" stroke-width="1"></circle>' for i in range(6))
             + glow(cx, b - 30 * s, 60 * s, "#FFE680", 0.8, f"{p}g"))
    if joy:
        o.append(man(p, w * 0.78, b, s, "#6A5A3A", up=UP_HIGH))
    else:
        mattock = '<path d="M-30 -160 L -60 -40 M-70 -46 L -48 -36" stroke="#5A3A22" stroke-width="6"></path>'
        o.append(man(p, cx - 120 * s, b, s, "#6A5A3A", extra=mattock))
    return "".join(o)

def pearl(p, w, h, seed):
    """A merchant seeking goodly pearls, and one pearl of great price: the merchant in his fine robe holding up a single
    great pearl to the light, his trays of lesser pearls before him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#3A2A5A", "#E8A86A"), houses(w, h, h * 0.8, seed, hmin=0.3, hmax=0.46, stairs=False), pavement(w, h, h * 0.8)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(man(p, w * 0.4, b, s, "#1F5A6A", kind="Robe", up=UP_HIGH, extra=A.headcloth("#E8B830", cord="#5A1A4A") + A.BLACK_BEARD))
    px, py = w * 0.4 + 46 * s, b - 226 * s
    o.append(glow(px, py, 50 * s, "#FFFDF0", 1.0, f"{p}g") + f'<circle cx="{f(px)}" cy="{f(py)}" r="{f(10 * s)}" fill="#F8F4EC" stroke="{INK}" stroke-width="1.6"></circle>')
    o.append(f'<rect x="{f(w * 0.58)}" y="{f(b - 50 * s)}" width="{f(w * 0.3)}" height="{f(50 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
    r = random.Random(seed)
    for _ in range(20):
        o.append(f'<circle cx="{f(w * 0.6 + r.uniform(0, w * 0.26))}" cy="{f(b - 54 * s + r.uniform(-4, 2))}" r="{f(3 * s)}" fill="#E8E2D6" stroke="{INK}" stroke-width="0.8"></circle>')
    return "".join(o)

def dragnet(p, w, h, seed):
    """A net cast into the sea, gathered of every kind, drawn up on the beach: the fishermen seated on the sand sorting the
    catch into vessels, the bad thrown aside; the boat pulled up beside them."""
    r = random.Random(seed); b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.3, seed, color="#8A9A7A", amp=10, step=90), lake(w, h, h * 0.36, seed, n=8),
         shore(w, h, h * 0.62)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(boat(p, w * 0.86, h * 0.66, s * 0.8, mast=True))
    o.append(f'<path d="M{f(w * 0.3)} {f(b - 10)} C {f(w * 0.36)} {f(b - 60 * s)} {f(w * 0.6)} {f(b - 60 * s)} {f(w * 0.66)} {f(b - 10)} Z" fill="#C8B888" opacity="0.5" stroke="#8A7A5A" stroke-width="1.4"></path>')
    for _ in range(14):
        o.append(creature("fish", w * r.uniform(0.34, 0.62), b - r.uniform(14, 44) * s, s * 0.5, color=r.choice(["#8FB8C8", "#C8B888", "#B8C8A8"])))
    for x in (0.18, 0.74):
        o.append(seated(w * x, b, s * 0.85, r.choice(TWELVE), head=None, beard="#2A1A10", flip=x > 0.5))
    o.append(f'<path d="M{f(w * 0.08)} {f(b)} C {f(w * 0.06)} {f(b - 30 * s)} {f(w * 0.14)} {f(b - 40 * s)} {f(w * 0.14)} {f(b - 40 * s)} L {f(w * 0.06)} {f(b - 40 * s)} Z" fill="#B5652E" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def furnace(p, w, h, seed):
    """The furnace of fire: only fire, filling the dark — no one drawn in it."""
    o = [bgr(w, h, "#1A0A08")]
    for i in range(6):
        o.append(E.blaze(w * (0.08 + 0.17 * i), h, w * 0.24, h * random.Random(seed + i).uniform(0.6, 0.95), seed + i, n=7))
    return "".join(o)

def sun_field(p, w, h, seed):
    """The righteous shine forth as the sun in the kingdom of their Father: the sun risen in full over a field of grain."""
    o = [sky(w, h, "#FFE680", "#FFF4C2"), sun(w * 0.5, h * 0.42, max(20, h * 0.12), color="#FFF4C2", glow="#FFFFFF", op=0.5),
         hills(w, h, h * 0.66, seed, color="#C8A060", amp=8, step=90), ground(w, h, h * 0.72, "#D8B860", dy=0), grain(-10, w + 10, h * 1.0, h * 0.2, seed)]
    return "".join(o)

def feast_hall(p, w, h, seed):
    """Herod's birthday: the banqueting hall at night, the lamps hung between the columns, the guests reclining at the
    tables along the walls, the floor in the midst left empty (the dance is told in words only)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bgr(w, h, "#2A1A2A")]
    for x in (0.08, 0.3, 0.7, 0.92):
        o.append(f'<rect x="{f(w * x - 14)}" y="-10" width="28" height="{f(b + 10)}" fill="#C8963E" stroke="{INK}" stroke-width="2"></rect>')
    for x in (0.19, 0.5, 0.81):
        o.append(f'<path d="M{f(w * x)} -10 L {f(w * x)} {f(h * 0.2)}" stroke="#8A6A3A" stroke-width="2"></path>' + glow(w * x, h * 0.24, h * 0.16, "#FFC14D", 0.7, f"{p}l{int(x * 100)}") + A.lamp(w * x, h * 0.24, max(0.6, h / 360)))
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#5A3A3A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(b + h * 0.04)}" rx="{f(w * 0.16)}" ry="{f(h * 0.03)}" fill="#7A4A4A"></ellipse>')
    s = fit(b, max(h * 0.24, b - 220))
    r = random.Random(seed)
    for x in (0.04, 0.14, 0.24, 0.76, 0.86, 0.96):
        o.append(seated(w * x, b, s * 0.8, r.choice(["#5A1A4A", "#7A2A3A", "#3A4A6A", "#6A5A3A"]), head=r.choice(["#E8B830", "#5A1A4A", None]), beard="#2A1A10", flip=x > 0.5))
    return "".join(o)

def tomb(p, w, h, seed, sealed=False):
    """A tomb cut in the rock at dusk, its round stone rolled to the door (John's burial)."""
    b = h * 0.92
    o = [sky(w, h, "#3A2A4A", "#C8906A"), hills(w, h, h * 0.5, seed, color="#5A4A44", amp=12, step=80),
         f'<path d="M{f(w * 0.2)} {f(b)} C {f(w * 0.24)} {f(h * 0.3)} {f(w * 0.8)} {f(h * 0.26)} {f(w * 0.86)} {f(b)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.44)} {f(b)} L {f(w * 0.44)} {f(h * 0.6)} Q {f(w * 0.5)} {f(h * 0.5)} {f(w * 0.56)} {f(h * 0.6)} L {f(w * 0.56)} {f(b)} Z" fill="#1A1210" stroke="{INK}" stroke-width="2"></path>',
         f'<circle cx="{f(w * 0.52)}" cy="{f(b - h * 0.16)}" r="{f(h * 0.16)}" fill="#A89A8A" stroke="{INK}" stroke-width="2.4"></circle>',
         ground(w, h, b, "#6A5A4A", dy=0)]
    return "".join(o)

def desert_place(p, w, h, seed):
    """He withdrew in a boat to a desert place apart, and the multitudes followed him on foot: the boat on the lake, the
    long line of people along the shore road toward the bare hills."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.3, seed, color="#C8A06A", amp=16, step=80), lake(w, h, h * 0.4, seed, n=8),
         shore(w, h, h * 0.76)]
    s = fit(h * 0.66, h * 0.5)
    o.append(boat(p, w * 0.3, h * 0.6, s * 1.4, crew=[(-40, ROBES["peter"]), (0, "jesus"), (40, ROBES["john"])], mast=True))
    for i in range(14):
        x = w * (0.4 + 0.04 * i); y = h * (0.9 - 0.006 * i)
        o.append(figure(p, x, y, y - h * 0.12, random.Random(seed + i).choice(HEB), "man" if i % 3 else "woman", flip=True))
    return "".join(o)

def five_loaves(p, w, h, seed):
    """Five loaves, and two fishes: Jesus standing on the green grass at evening, his face lifted to heaven, the five
    loaves and two fishes in a basket held up before him, the disciples beside, the multitude seated row on row."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A6A", "#FFC890"), sun(w * 0.86, h * 0.32, 16, color="#FFE680", op=0.3), hills(w, h, h * 0.34, seed, color="#7A7A6A", amp=12, step=90),
         ground(w, h, h * 0.42, "#8AB84A", dy=0)]
    r = random.Random(seed)
    s = fit(b, max(h * 0.3, b - 220))
    for row in range(4):
        y = h * (0.5 + 0.08 * row); k = s * (0.3 + 0.12 * row)
        for i in range(10):
            x = w * (0.42 + 0.06 * i) + r.uniform(-8, 8) - row * 10
            c = r.choice(HEB)
            o.append(seated(x, y, k, c, head=r.choice([c, "#E8E2D6", None]), beard=r.choice(["#2A1A10", ""]), flip=True))
    basket = ('<path d="M-70 -170 L -30 -170 L -36 -150 L -64 -150 Z" fill="#C8A060" stroke="#0D0D0F" stroke-width="1.6"></path>'
              '<ellipse cx="-58" cy="-174" rx="6" ry="3" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1"></ellipse><ellipse cx="-44" cy="-175" rx="6" ry="3" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    o.append(jesus(p, w * 0.2, b, s, up=[(-22, -158), (-44, -168), (-60, -176)]))
    o.append(f'<g transform="translate({f(w * 0.2)} {f(b)}) scale({f(s)})">{basket}</g>')
    o.append(disciple(p, w * 0.34, b, s * 0.96, "#4A6A4A", flip=True) + disciple(p, w * 0.06, b, s * 0.94, "andrew"))
    return "".join(o)

def baskets(p, w, h, seed):
    """They took up that which remained over of the broken pieces, twelve baskets full: the twelve baskets set in a row on
    the grass, heaped with broken bread, the multitude rising in the dusk behind."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#3A2A5A", "#E8A86A"), hills(w, h, h * 0.4, seed, color="#5A5A5A", amp=12, step=90), ground(w, h, h * 0.5, "#7AA84A", dy=0)]
    o.append(crowd(p, w * 0.04, w * 0.96, h * 0.6, h * 0.6 - h * 0.12, 16, seed))
    k = min(w / 14 / 50, (b - h * 0.6) / 60)
    for i in range(12):
        x = w * (0.06 + 0.08 * i)
        o.append(f'<path d="M{f(x - 22 * k)} {f(b - 40 * k)} L {f(x + 22 * k)} {f(b - 40 * k)} L {f(x + 16 * k)} {f(b)} L {f(x - 16 * k)} {f(b)} Z" fill="#C8A060" stroke="{INK}" stroke-width="1.8"></path>'
                 f'<path d="M{f(x - 22 * k)} {f(b - 40 * k)} C {f(x - 16 * k)} {f(b - 56 * k)} {f(x + 16 * k)} {f(b - 56 * k)} {f(x + 22 * k)} {f(b - 40 * k)} Z" fill="#D9A25A" stroke="{INK}" stroke-width="1.6"></path>'
                 f'<path d="M{f(x - 20 * k)} {f(b - 26 * k)} L {f(x + 20 * k)} {f(b - 26 * k)} M{f(x - 18 * k)} {f(b - 12 * k)} L {f(x + 18 * k)} {f(b - 12 * k)}" stroke="#8A6A3A" stroke-width="1.4"></path>')
    return "".join(o)

def mount_alone(p, w, h, seed):
    """He went up into the mountain apart to pray, and when even was come he was there alone: the mountain-top at nightfall,
    Jesus a small figure standing alone, the lake and a tiny boat far below."""
    o = [mk.defs(p, *ALL), night(w, h, seed, n=50, top="#0B0B2A", bot="#5A3A6A"), lake(w, h, h * 0.66, seed, color="#2A3A5A", deep="#14243A", n=6, op=0.4),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.5)} L {f(w * 0.2)} {f(h * 0.4)} L {f(w * 0.34)} {f(h * 0.46)} L {f(w * 0.56)} {f(h + 10)} Z" fill="#2A2238" stroke="{INK}" stroke-width="2.4"></path>']
    o.append(boat(p, w * 0.78, h * 0.76, max(0.15, h / 1400), mast=True))
    s = fit(h * 0.42, h * 0.3)
    o.append(jesus(p, w * 0.2, h * 0.41, s, up=[(-22, -158), (-34, -186), (-30, -214)]))
    return "".join(o)

def on_the_sea(p, w, h, seed, peter=False, calm=False):
    """In the fourth watch of the night he came unto them, walking upon the sea: the boat tossed in the dark, the waves
    high, and Jesus standing upon the water in his soft light; peter=True: Peter out on the water sinking to his waist, Jesus'
    hand holding him; calm=True: the wind ceased, the men in the boat bowed."""
    b = h * 0.86
    o = [mk.defs(p, *ALL), sky(w, h, "#0B0B2A", "#2A2A5A") if not calm else sky(w, h, "#2A2A6A", "#C8906A")]
    if not calm: o.append(rain(w, h, seed, n=30, op=0.3))
    s = min(1.0, (b - h * 0.2) / 160)
    if calm:
        o.append(lake(w, h, h * 0.6, seed, color="#3A4A7A", deep="#1A2A4A", n=8, op=0.5))
        o.append(boat(p, w * 0.5, h * 0.8, s, crew=[(-70, ROBES["peter"]), (-30, ROBES["andrew"]), (20, "jesus"), (66, ROBES["john"])], mast=True))
        return "".join(o)
    o.append(boat(p, w * 0.28, b - h * 0.04, s * 0.9, crew=[(-60, ("up", ROBES["andrew"])), (-20, ROBES["james"]), (30, ("up", ROBES["john"]))], mast=True, tilt=-8))
    jx = w * 0.72
    o.append(glow(jx, b - 100 * s, 120 * s, "#FFE680", 0.6, f"{p}g"))
    if peter:
        o.append(jesus(p, jx, b, s, flip=True, up=[(-22, -158), (-40, -140), (-60, -126)]))
        o.append(mk.person(p, round(jx - 70 * s), round(b + 80 * s), round(s * 0.96, 3), body="#B98A6E", cloth=ROBES["peter"], kind="Robe", sw=3,
                           up=[(-22, -158), (-6, -190), (12, -206)]))
    else:
        o.append(jesus(p, jx, b, s, flip=True))
    o.append(waves(w, h, b - h * 0.02, seed, amp=max(6, h * 0.04)))
    return "".join(o)

def gennesaret(p, w, h, seed):
    """At Gennesaret they brought unto him all that were sick, to touch the border of his garment: the beach crowded, the
    sick laid on their pallets along the shore, hands reaching to his hem."""
    b = h * 0.94
    o = [mk.defs(p, *ALL, *LIE), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.3, seed, color="#8A9A7A", amp=12, step=90), lake(w, h, h * 0.36, seed, n=8),
         shore(w, h, h * 0.56)]
    s = fit(b, max(h * 0.3, b - 220))
    o.append(boat(p, w * 0.12, h * 0.6, s * 0.7, mast=True))
    o.append(jesus(p, w * 0.36, b, s))
    o.append(crowd(p, w * 0.5, w * 0.98, b - 40 * s, b - 40 * s - 150 * s, 8, seed, flip=True))
    for x in (0.52, 0.76):
        o.append(f'<rect x="{f(w * x - 10)}" y="{f(b - 6)}" width="{f(170 * s * 0.6)}" height="{f(8 * s)}" fill="#C8B088" stroke="{INK}" stroke-width="1.4"></rect>'
                 f'<g transform="translate({f(w * x + 120 * s * 0.6)} {f(b - 4)}) scale({f(s * 0.55)})" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use><use href="#{p}LieA"></use></g>')
    o.append(E.kneel(w * 0.46, b, s * 0.8, color="#6A5A7A", flip=True, skin=SKIN))
    return "".join(o)
