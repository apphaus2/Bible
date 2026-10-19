"""Drawings for Jeremiah chapter 6 (Jeremiah 16–18), on top of jer.art: the house of mourning and the house of feasting, the
fishers and hunters, the pen of iron, the heath and the tree by the waters, the gates on the sabbath, the potter's house."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2

def two_doors(p, w, h, seed, feast=False):
    """Enter not into the house of mourning (feast=True: neither into the house of feasting): the prophet passing alone in the
    street at night, a door with mourners seated at it (or a lit door with the sound of feasting)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), night(w, h, seed, "#14122A"), ground(w, h, h * 0.8, "#2A2430", dy=0)]
    o.append(f'<rect x="{f(w * 0.46)}" y="{f(h * 0.3)}" width="{f(w * 0.5)}" height="{f(h * 0.5)}" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    dx = w * 0.66
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.5)}" width="{f(w * 0.1)}" height="{f(h * 0.3)}" fill="{"#FFC14D" if feast else "#1A1210"}" stroke="#0D0D0F" stroke-width="2"></rect>')
    if feast: o.append(glow(dx + w * 0.05, h * 0.66, w * 0.16, color="#FFC14D", op=0.4, uid=f"td{seed}") + S3.notes(dx + w * 0.05, h * 0.42, 4, seed))
    else:
        s2 = fit(b, max(h * 0.6, b - 140))
        for i in range(3): o.append(E.kneel(w * (0.8 + i * 0.07), b, s2, color="#1A1418", skin="#6A5A5A", flip=True))
    s = fit(b, max(h * 0.4, b - 230))
    o.append(jer_fig(p, w * 0.2, b, s, age=1))
    return "".join(o)

def boat(x, y, s=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-70 -20 L 70 -20 L 50 6 L -50 6 Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M-60 -20 L -60 -30 M60 -20 L 60 -30" stroke="#0D0D0F" stroke-width="3"></path></g>')

def fishers_hunters(p, w, h, seed):
    """I will send for many fishers, and they shall fish them up; and afterward for many hunters, and they shall hunt them from
    every mountain, and out of the clefts of the rocks: boats with nets on the water; hunters with bows on the crags."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E0B0"), f'<rect x="-10" y="{f(h * 0.6)}" width="{f(w * 0.55)}" height="{f(h * 0.5)}" fill="#1F6F9A"></rect>',
         crag(w * 0.46, w + 10, h * 1.0, h * 0.34)]
    for i in range(2):
        x, y = w * (0.1 + i * 0.22), h * (0.74 + i * 0.08)
        o.append(boat(x, y, min(0.9, h / 360)))
        o.append(f'<path d="M{f(x + 40)} {f(y - 10)} Q {f(x + 60)} {f(y + 30)} {f(x + 90)} {f(y + 20)}" stroke="#E8D8B0" stroke-width="1.6" fill="none" stroke-dasharray="3 3"></path>')
    s = fit(h * 0.5, h * 0.24)
    for i, (x, y) in enumerate(((0.62, 0.52), (0.82, 0.44))):
        o.append(man(p, w * x, h * y, s * (1 - i * 0.1), "#5A4A2A", flip=True, up=[(22, -158), (50, -166), (78, -170)]))
        o.append(f'<path d="M{f(w * x - 78 * s)} {f(h * y - 200 * s)} Q {f(w * x - 96 * s)} {f(h * y - 170 * s)} {f(w * x - 78 * s)} {f(h * y - 140 * s)}" stroke="#4A2A1A" stroke-width="3" fill="none"></path>')
    return "".join(o)

def iron_pen(w, h, seed):
    """The sin of Judah is written with a pen of iron, and with the point of a diamond, graven upon the tablet and upon the
    horns of your altars: a stone tablet with its graven lines, an iron stylus, a horned altar behind."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2228"></rect>', horned_altar(w * 0.78, h * 0.92, min(0.9, h / 260)),
         f'<path d="M{f(w * 0.2)} {f(h * 0.94)} L {f(w * 0.22)} {f(h * 0.3)} Q {f(w * 0.38)} {f(h * 0.18)} {f(w * 0.54)} {f(h * 0.3)} L {f(w * 0.56)} {f(h * 0.94)} Z" fill="#A89A8A" stroke="#0D0D0F" stroke-width="2.6"></path>']
    r = random.Random(seed)
    for k in range(6):
        y = h * (0.4 + k * 0.08); x = w * 0.27
        while x < w * 0.5:
            L = w * r.uniform(0.02, 0.05)
            o.append(f'<path d="M{f(x)} {f(y)} l {f(L)} 0" stroke="#3A3030" stroke-width="2.6"></path>'); x += L + w * 0.012
    o.append(f'<path d="M{f(w * 0.46)} {f(h * 0.62)} L {f(w * 0.66)} {f(h * 0.2)}" stroke="#5A5A62" stroke-width="7" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.46)} {f(h * 0.62)} l -4 12 l 10 -6 Z" fill="#E8F6FA" stroke="#0D0D0F" stroke-width="1.2"></path>')
    return "".join(o)

def heath(w, h, seed):
    """Like the heath in the desert, in the parched places of the wilderness, a salt land and not inhabited."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#E8A060", "#F8E8C0"), sun(w * 0.8, h * 0.24, min(w, h) * 0.06, color="#FFE680", op=0.4), ground(w, h, h * 0.62, "#E8D8B8", dy=0)]
    o.append("".join(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.66, h))}" r="{f(r.uniform(1, 3))}" fill="#F8F6F0"></circle>' for _ in range(60)))
    x, y = w * 0.42, h * 0.86
    for k in range(9):
        a = -math.pi / 2 + (k - 4) * 0.28
        o.append(f'<path d="M{f(x)} {f(y)} l {f(math.cos(a) * h * 0.18)} {f(math.sin(a) * h * 0.18)}" stroke="#6A5A3A" stroke-width="2.4"></path>')
    return "".join(o)

def tree_waters(w, h, seed):
    """A tree planted by the waters, that spreadeth out its roots by the river; its leaf shall be green."""
    o = [K2.sky(w, h, "#8FC0E0", "#F3F0D0"), ground(w, h, h * 0.62, "#7AA84A", dy=0),
         f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.6)} {f(h * 0.92)} {f(w + 10)} {f(h * 0.84)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></path>',
         S4b.great_oak(w * 0.5, h * 0.84, min(1.0, h / 330), seed)]
    for k in range(5):
        o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.84)} q {f((k - 2) * w * 0.04)} {f(h * 0.04)} {f((k - 2) * w * 0.08)} {f(h * 0.08)}" stroke="#4A2A1A" stroke-width="3" fill="none"></path>')
    return "".join(o)

def partridge(w, h, seed):
    """As the partridge that sitteth on eggs which she hath not laid."""
    o = [K2.sky(w, h, "#C8A880", "#F3E0B0"), ground(w, h, h * 0.66, "#B8946A", dy=0), thicket(w * 0.6, w + 10, h * 0.7, h * 0.4, seed, color="#6A7A3A")]
    x, y, s = w * 0.36, h * 0.86, min(1.4, h / 180)
    o.append(f'<ellipse cx="{f(x)}" cy="{f(y + 6 * s)}" rx="{f(46 * s)}" ry="{f(10 * s)}" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
             f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-36 0 Q -40 -30 -6 -34 Q 18 -36 26 -24 L 34 -32 Q 44 -38 46 -28 L 50 -26 L 44 -22 Q 40 -14 30 -10 Q 20 4 -20 4 Z" fill="#9A7A5A" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-30 -14 Q -10 -22 14 -14" stroke="#5A3A2A" stroke-width="2" fill="none"></path><circle cx="40" cy="-28" r="2" fill="#0D0D0F"></circle>'
             + "".join(f'<path d="M{-28 + k * 9} -26 l 4 -2" stroke="#E8D8B0" stroke-width="1.6"></path>' for k in range(5)) + '</g>')
    for k in range(3):
        o.append(f'<ellipse cx="{f(x + (50 + k * 14) * s)}" cy="{f(y + 4 * s)}" rx="{f(6 * s)}" ry="{f(8 * s)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    return "".join(o)

def glorious_throne(w, h, seed):
    """A glorious throne, set on high from the beginning, is the place of our sanctuary: the house on its mount in light."""
    o = [K2.sky(w, h, "#3A3A7A", "#FFE0A0"), V.rays(w * 0.5, h * 0.4, 30, 20, max(w, h), color="#FFF4C2", op=0.3),
         f'<path d="M-10 {f(h + 10)} C {f(w * 0.2)} {f(h * 0.7)} {f(w * 0.8)} {f(h * 0.7)} {f(w + 10)} {f(h + 10)} Z" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         temple_front(w * 0.5, h * 0.8, min(w * 0.4, h * 0.9), seed)]
    return "".join(o)

def sabbath_gate(p, w, h, seed, kings=False, burden=True):
    """The gate of the children of the people, whereby the kings of Judah come in: men bearing burdens through it (kings=True:
    kings and princes riding in by it in chariots)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E0B0"), wall(-10, w + 10, h * 0.3, h * 0.78, seed, towers=4, gate=w * 0.5), ground(w, h, h * 0.78, "#C8A870", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    if kings:
        o.append(E3.chariot(w * 0.3, b, min(0.9, s * 1.0), color="#3A2214", driver="#1F3A7A") + E3.chariot(w * 0.6, b - 4, min(0.8, s * 0.9), color="#5A3A1A", driver="#7A2A3A"))
    else:
        for i in range(4):
            x = w * (0.3 + i * 0.12)
            o.append(man(p, x, b, s * 0.86, ["#6A5A3A", "#5A4A6A", "#6A3A2A", "#4A5A3A"][i], up=[(-22, -158), (-26, -190), (-10, -206)])
                     + R1.sack(x - 6 * s, b - 196 * s, 0.6 * s))
        o.append(jer_fig(p, w * 0.12, b, s, age=1, up=[(22, -158), (40, -186), (52, -220)], flip=True))
    return "".join(o)

def offering_bearers(p, w, h, seed):
    """They shall come from the cities of Judah bringing burnt-offerings and meal-offerings and frankincense unto the house of
    Jehovah: a line of people climbing to the house with lambs, baskets and jars."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#FFC890", "#F8ECD0"), temple_front(w * 0.82, h * 0.62, w * 0.3, seed),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.9)} L {f(w * 0.7)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h + 10)} Z" fill="#C8B080" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i in range(6):
        t = i / 5; x = w * (0.08 + 0.56 * t); y = h * (0.94 - 0.28 * t)
        s = fit(y, y - h * (0.32 - 0.14 * t))
        o.append(man(p, x, y, s, ["#6A5A3A", "#5A4A6A", "#6A3A2A", "#4A5A3A", "#7A5A3A", "#3A4A6A"][i]) if i % 2 == 0 else woman(p, x, y, s, ["#8A5A6A", "#6A5A3A", "#5A3A5A"][i % 3]))
        o.append(E3.lamb(x + 26 * s, y, 0.5 * s) if i % 3 == 0 else E4.basket(x + 26 * s, y, 0.6 * s) if i % 3 == 1 else jar(x + 26 * s, y, 0.4 * s))
    return "".join(o)

def gates_fire(w, h, seed):
    """I will kindle a fire in the gates thereof, and it shall devour the palaces of Jerusalem: the gate burning, no one drawn."""
    o = [K2.sky(w, h, "#2A0A0A", "#8A2A1A"), wall(-10, w + 10, h * 0.3, h * 0.82, seed, towers=4, gate=w * 0.5, color="#8A6A4A"), ground(w, h, h * 0.82, "#2A1410", dy=0)]
    o += [E.blaze(w * (0.3 + i * 0.2), h * 0.82, w * 0.14, h * 0.4, seed + i, n=6) for i in range(3)]
    o.append(smoke(w * 0.5, h * 0.24, 7, seed, w=0.8))
    return "".join(o)

def potter(p, w, h, seed, marred=False, prophet=True):
    """The potter's house: the potter seated at his wheels with a vessel of clay on them (marred=True: the vessel marred in his
    hand, a lump of clay); the prophet watching at the door."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#7A5A3A"></rect>',
         f'<rect x="{f(w * 0.04)}" y="{f(h * 0.14)}" width="{f(w * 0.2)}" height="{f(h * 0.8)}" fill="#F3D8A0" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         ground(w, h, h * 0.84, "#5A3A22", dy=0)]
    for k in range(4):
        o.append(jar(w * (0.66 + k * 0.08), h * 0.5, min(0.5, h / 600), color="#C8804A", stopper=None, handles=k % 2 == 0))
    o.append(f'<rect x="{f(w * 0.62)}" y="{f(h * 0.5)}" width="{f(w * 0.36)}" height="{f(h * 0.02)}" fill="#4A2A1A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    wx, wy, R = w * 0.5, h * 0.8, min(w * 0.12, h * 0.16)
    o.append(f'<ellipse cx="{f(wx)}" cy="{f(b - 6)}" rx="{f(R * 1.2)}" ry="{f(R * 0.22)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<rect x="{f(wx - 5)}" y="{f(wy)}" width="10" height="{f(b - 6 - wy)}" fill="#4A2A1A" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             f'<ellipse cx="{f(wx)}" cy="{f(wy)}" rx="{f(R)}" ry="{f(R * 0.2)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    if marred:
        o.append(f'<path d="M{f(wx - R * 0.5)} {f(wy)} Q {f(wx - R * 0.6)} {f(wy - R * 0.6)} {f(wx - R * 0.1)} {f(wy - R * 0.4)} Q {f(wx + R * 0.3)} {f(wy - R * 0.9)} {f(wx + R * 0.5)} {f(wy)} Z" fill="#B8784A" stroke="#0D0D0F" stroke-width="2"></path>')
    else:
        o.append(jar(wx, wy, R / 80, color="#B8784A", handles=False, stopper=None))
    ps = fit(b, max(h * 0.4, b - 220)); o.append(man(p, wx + R * 1.2, b, ps, "#6A5A3A", flip=True, up=[(22, -158), (46, -128), (70, -112)], extra=A.headcloth("#8A7A5A") + A.BLACK_BEARD))
    if prophet:
        s = fit(b, max(h * 0.3, b - 240))
        o.append(jer_fig(p, w * 0.14, b, s * 0.9, age=1))
    return "".join(o)

def lebanon_snow(w, h, seed):
    """Shall the snow of Lebanon fail from the rock of the field? or the cold waters that flow down from afar be dried up?"""
    o = [K2.sky(w, h, "#6A9AC8", "#E8F0F8"), f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.2)} {f(h * 0.3)} L {f(w * 0.36)} {f(h * 0.5)} L {f(w * 0.56)} {f(h * 0.2)} L {f(w * 0.78)} {f(h * 0.46)} L {f(w + 10)} {f(h * 0.34)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A6A7A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.14)} {f(h * 0.4)} L {f(w * 0.2)} {f(h * 0.3)} L {f(w * 0.27)} {f(h * 0.4)} Z M{f(w * 0.48)} {f(h * 0.32)} L {f(w * 0.56)} {f(h * 0.2)} L {f(w * 0.64)} {f(h * 0.3)} Z M{f(w * 0.92)} {f(h * 0.4)} L {f(w + 10)} {f(h * 0.34)} L {f(w + 10)} {f(h * 0.42)} Z" fill="#F8F8FF" stroke="#0D0D0F" stroke-width="1.6"></path>',
         f'<path d="M{f(w * 0.56)} {f(h * 0.34)} C {f(w * 0.5)} {f(h * 0.6)} {f(w * 0.66)} {f(h * 0.76)} {f(w * 0.5)} {f(h + 10)}" stroke="#8FD0E2" stroke-width="7" fill="none"></path>']
    return "".join(o)

def plotters(p, w, h, seed):
    """Come, and let us devise devices against Jeremiah: a priest, a wise man and a prophet conferring together by a pillar at
    dusk."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A1A3A", "#B8704A"), ground(w, h, h * 0.8, "#3A2E2A", dy=0),
         f'<rect x="{f(w * 0.1)}" y="{f(h * 0.1)}" width="{f(w * 0.06)}" height="{f(h * 0.7)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    s = fit(b, max(h * 0.4, b - 220))
    o.append(priest(p, w * 0.42, b, s) + man(p, w * 0.54, b, s, "#3A3A4A", flip=True, extra=A.headcloth("#3A3A4A") + A.BLACK_BEARD)
             + man(p, w * 0.66, b, s * 0.96, "#6A4A2A", flip=True, extra=A.headcloth("#8A6A2A") + A.BLACK_BEARD))
    return "".join(o)

def pit_snares(w, h, seed):
    """They have digged a pit to take me, and hid snares for my feet: a covered pit in the path, a noose-snare among stones."""
    o = [K2.sky(w, h, "#3A2A3A", "#B8806A"), ground(w, h, h * 0.5, "#8A6A4A", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.4)} {f(h * 0.7)} {f(w * 0.5)} {f(h * 0.6)} {f(w * 0.56)} {f(h * 0.5)}" stroke="#C8A878" stroke-width="{f(w * 0.08)}" fill="none"></path>',
         f'<ellipse cx="{f(w * 0.42)}" cy="{f(h * 0.76)}" rx="{f(w * 0.1)}" ry="{f(h * 0.06)}" fill="#1A1210" stroke="#0D0D0F" stroke-width="2"></ellipse>']
    for k in range(7):
        o.append(f'<path d="M{f(w * (0.33 + k * 0.03))} {f(h * 0.72)} l {f(w * 0.02)} {f(h * 0.06)}" stroke="#6A4A2A" stroke-width="3"></path>')
    o.append(f'<circle cx="{f(w * 0.72)}" cy="{f(h * 0.84)}" r="{f(h * 0.05)}" fill="none" stroke="#C8A878" stroke-width="2.4"></circle>'
             f'<path d="M{f(w * 0.72 + h * 0.05)} {f(h * 0.84)} L {f(w * 0.86)} {f(h * 0.7)}" stroke="#C8A878" stroke-width="2.4"></path>')
    return "".join(o)
