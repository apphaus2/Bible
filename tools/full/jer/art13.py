"""Drawings for Jeremiah chapter 13 (Jeremiah 37–39), on top of jer.art: the Chaldeans breaking up for fear of Pharaoh, the
arrest in the gate of Benjamin, the dungeon-house, the daily loaf, the dungeon of Malchijah with its cords (no one drawn in it),
Ebed-melech and the thirty men drawing up the prophet, the third entry, the breach, the princes of Babylon in the middle gate,
the flight by night between the two walls, and the poor left with vineyards."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2
from jer.art11 import court_guard

EBED_C = "#F3EFE6"
def ebed_fig(p, x, y, s, flip=False, up=None):
    """Ebed-melech the Ethiopian at a distance: dark skin, white robe, a gold headcloth."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#3A2014", cloth=EBED_C, kind="Robe", sw=3, flip=flip, up=up, extra=A.headcloth("#F3EFE6", cord="#E8B830"))

def pharaoh_relief(w, h):
    """Pharaoh's army come forth out of Egypt, and the Chaldeans breaking up from Jerusalem (a map)."""
    return near_east(w, h, ("JERUSALEM", "EGYPT", "MIGDOL", "BABYLON"), hi=("EGYPT",), arrows=[("EGYPT", "MIGDOL"), ("JERUSALEM", "BABYLON")], lit="#FF8A6A", box=(29.0, 41.0, 26.5, 35.0))

def gate_arrest(p, w, h, seed, age=3):
    """In the gate of Benjamin, Irijah the captain of the ward laid hold on Jeremiah the prophet."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E0B0"), wall(-10, w + 10, h * 0.24, h * 0.74, seed, towers=3, gate=w * 0.5, color="#C8B088"), ground(w, h, h * 0.74, "#C8B080", dy=0)]
    s = fit(b, max(h * 0.4, b - 230))
    o.append(jer_fig(p, w * 0.42, b, s, age=age))
    o.append(man(p, w * 0.56, b, s, "#6A2A3A", flip=True, up=[(22, -158), (50, -150), (76, -140)], extra=A.headcloth("#6A2A3A") + A.BLACK_BEARD))
    return "".join(o)

def cells(w, h, seed):
    """The dungeon-house, the cells in the house of Jonathan the scribe: a dark vault, a barred cell door, a patch of light."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1E1A1E"></rect>']
    for i in range(3):
        x = w * (0.08 + i * 0.32)
        o.append(f'<path d="M{f(x)} {f(h * 0.9)} L {f(x)} {f(h * 0.36)} Q {f(x + w * 0.12)} {f(h * 0.2)} {f(x + w * 0.24)} {f(h * 0.36)} L {f(x + w * 0.24)} {f(h * 0.9)} Z" fill="#0D0B0E" stroke="#4A4048" stroke-width="3"></path>'
                 + "".join(f'<path d="M{f(x + w * 0.24 * k / 6)} {f(h * 0.4)} L {f(x + w * 0.24 * k / 6)} {f(h * 0.9)}" stroke="#5A5058" stroke-width="3"></path>' for k in range(1, 6)))
    o.append(f'<path d="M{f(w * 0.46)} -10 L {f(w * 0.54)} -10 L {f(w * 0.62)} {f(h * 0.9)} L {f(w * 0.4)} {f(h * 0.9)} Z" fill="#C8B8A0" opacity="0.18"></path>')
    o.append(ground(w, h, h * 0.9, "#2A2428", dy=0))
    return "".join(o)

def loaf(w, h, seed):
    """They gave him daily a loaf of bread out of the bakers' street, until all the bread in the city was spent."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A4A3A"></rect>', glow(w * 0.5, h * 0.6, min(w, h) * 0.5, color="#FFE680", op=0.2, uid=f"lf{seed}"),
         ground(w, h, h * 0.8, "#3A2E24", dy=0)]
    s = min(1.6, h / 160)
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.78)}" rx="{f(44 * s)}" ry="{f(18 * s)}" fill="#C8904A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
             f'<path d="M{f(w * 0.5 - 24 * s)} {f(h * 0.76)} q {f(10 * s)} {f(-8 * s)} {f(20 * s)} 0 M{f(w * 0.5 + 4 * s)} {f(h * 0.76)} q {f(10 * s)} {f(-8 * s)} {f(20 * s)} 0" stroke="#8A5A2A" stroke-width="2" fill="none"></path>')
    return "".join(o)

def dungeon(p, w, h, seed, stage=0):
    """The dungeon of Malchijah in the court of the guard: a cistern's round mouth in the paving, cords let down into the dark,
    no water but mire (nothing drawn within). stage 1: Ebed-melech and the men at the mouth letting down rags and worn-out
    garments by cords; stage 2: drawing up with the cords."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#6A5A6A", "#D8B090"), f'<rect x="-10" y="{f(h * 0.18)}" width="{f(w + 20)}" height="{f(h * 0.24)}" fill="#C8B088" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         ground(w, h, h * 0.42, "#A89070", dy=0)]
    cx, cy, rx, ry = w * 0.5, h * 0.74, w * 0.16, h * 0.1
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx * 1.18)}" ry="{f(ry * 1.3)}" fill="#8A8478" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="#0D0B08" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy + ry * 0.4)}" rx="{f(rx * 0.6)}" ry="{f(ry * 0.3)}" fill="#3A2A18" opacity="0.8"></ellipse>')
    s = fit(b, max(h * 0.4, b - 220)) if stage else fit(h * 0.6, h * 0.36)
    if stage == 0:
        for dx in (-0.06, 0.06):
            o.append(f'<path d="M{f(cx + w * dx)} {f(h * 0.5)} L {f(cx + w * dx * 0.6)} {f(cy + ry * 0.2)}" stroke="#C8A878" stroke-width="3"></path>')
            o.append(f'<rect x="{f(cx + w * dx - 6)}" y="{f(h * 0.48)}" width="12" height="8" fill="#6A4A2A"></rect>')
    else:
        for i, x in enumerate((0.22, 0.32, 0.68, 0.78)):
            pull = stage == 2
            o.append(man(p, w * x, b, s * 0.9, ["#6A5A3A", "#5A4A3A", "#4A4A5A", "#6A4A3A"][i], flip=x > 0.5,
                         up=[(22, -158), (40, -120), (56, -96)] if x > 0.5 else [(-22, -158), (-40, -120), (-56, -96)]))
            o.append(f'<path d="M{f(w * x + (-56 if x < 0.5 else 56) * s * 0.9)} {f(b - 96 * s * 0.9)} L {f(cx + (x - 0.5) * w * 0.12)} {f(cy)}" stroke="#C8A878" stroke-width="2.6"></path>')
        o.append(ebed_fig(p, w * 0.5, h * 0.6, fit(h * 0.6, h * 0.36), up=[(-22, -158), (-10, -126), (0, -100)]))
        if stage == 1:
            o.append(f'<path d="M{f(cx - 12)} {f(cy - ry * 0.4)} q 6 -10 14 -4 q 8 -10 12 2 l -4 12 q -12 4 -22 -2 Z" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return "".join(o)

def third_entry(p, w, h, seed, age=3):
    """The third entry that is in the house of Jehovah: the king and the prophet alone between the pillars, at dusk."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A2A4A", "#C88A6A"), f'<rect x="-10" y="{f(h * 0.1)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    for k in range(5):
        o.append(f'<rect x="{f(w * (0.04 + k * 0.22))}" y="{f(h * 0.16)}" width="{f(w * 0.05)}" height="{f(h * 0.78)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.2"></rect>')
    o.append(ground(w, h, h * 0.94, "#6A5A4A", dy=0))
    s = fit(b, max(h * 0.4, b - 230))
    o.append(jer_fig(p, w * 0.36, b, s, age=age))
    o.append(king_fig(p, w * 0.62, b, s, flip=True, cloth="#1F3A7A"))
    return "".join(o)

def women_brought(p, w, h, seed):
    """All the women that are left in the king of Judah's house shall be brought forth to the king of Babylon's princes: women
    led out of the palace gate between soldiers."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A4A5A", "#C8A080"), f'<rect x="{f(w * 0.56)}" y="{f(h * 0.3)}" width="{f(w * 0.44)}" height="{f(h * 0.46)}" fill="#D8C8A0" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.7)}" y="{f(h * 0.5)}" width="{f(w * 0.1)}" height="{f(h * 0.26)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></rect>', ground(w, h, h * 0.76, "#B8A07A", dy=0)]
    s = fit(b, max(h * 0.44, b - 210))
    for i in range(4): o.append(woman(p, w * (0.24 + i * 0.1), b, s * 0.92, ["#7A3A5A", "#5A4A7A", "#8A5A3A", "#3A5A6A"][i], flip=True))
    o.append(warrior(p, w * 0.1, b, s, BABEL_C, flip=True) + warrior(p, w * 0.64, b, s, BABEL_C, flip=True))
    return "".join(o)

def princes_gate(p, w, h, seed):
    """All the princes of the king of Babylon came in, and sat in the middle gate."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#4A3A4A", "#C8906A"), S4b.gatehouse(w * 0.5, h * 0.8, w * 0.8, h * 0.7), ground(w, h, h * 0.8, "#7A6A50", dy=0), smoke(w * 0.14, h * 0.2, 6, seed, w=0.6)]
    s = fit(b, max(h * 0.5, b - 180))
    for i in range(6): o.append(E.kneel(w * (0.16 + i * 0.14), b, s * 0.8, color=[BABEL_C, "#5A3A6A", "#2A5A5A", BABEL_C, "#6A3A2A", "#3A3A6A"][i], skin="#9A6A4A", flip=i >= 3))
    return "".join(o)

def flight(p, w, h, seed):
    """Zedekiah and all the men of war fled by night, by the way of the king's garden, through the gate betwixt the two walls,
    toward the Arabah: dark figures slipping out between two walls under the stars."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), night(w, h, seed, "#0E0C1E"), J.moon(w * 0.86, h * 0.14, min(w, h) * 0.04),
         wall(-10, w * 0.4, h * 0.3, h * 0.8, seed, towers=2, color="#4A4448"), wall(w * 0.6, w + 10, h * 0.3, h * 0.8, seed + 1, towers=2, color="#4A4448"),
         ground(w, h, h * 0.8, "#1A1820", dy=0)]
    s = fit(b, max(h * 0.44, b - 200))
    for i in range(5):
        o.append(mk.person(p, round(w * (0.42 + i * 0.05)), round(b - i * h * 0.03), round(s * (1 - i * 0.12), 3), body="#0D0B10", cloth="#1A1622", kind="Tunic", sw=2))
    return "".join(o)

def riblah(w, h, seed):
    """Riblah in the land of Hamath: the empty plain by the river at evening, the king of Babylon's tents far off (39:5–7 told
    in words only)."""
    o = [K2.sky(w, h, "#2A1A2A", "#A84A2A"), hills(w, h, h * 0.56, seed, "#3A2A2A", amp=10, step=90), ground(w, h, h * 0.62, "#5A4A3A", dy=0),
         f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.74)} {f(w * 0.6)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.78)}" stroke="#3A5A6A" stroke-width="6" fill="none"></path>',
         N.camp(6, w * 0.6, w + 10, h * 0.6, h * 0.68, seed, color=(BABEL_C, "#3A3A5A", "#2A3A4A"))]
    return "".join(o)

def poor_vineyards(p, w, h, seed):
    """Nebuzaradan left of the poor of the people, that had nothing, in the land of Judah, and gave them vineyards and fields."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), vine(w, h, seed)]
    s = fit(b, max(h * 0.5, b - 180))
    for i in range(3): o.append(man(p, w * (0.2 + i * 0.3), b, s * 0.9, ["#8A7A5A", "#7A6A5A", "#9A8A6A"][i]))
    return "".join(o)

def released(p, w, h, seed, age=3):
    """They took Jeremiah out of the court of the guard and committed him unto Gedaliah the son of Ahikam: the prophet led out of
    the court by a Babylonian officer to Gedaliah waiting at the gate."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8A8A9A", "#E8C8A0"), f'<rect x="-10" y="{f(h * 0.34)}" width="{f(w * 0.5)}" height="{f(h * 0.4)}" fill="#C8B088" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.3)}" y="{f(h * 0.46)}" width="{f(w * 0.1)}" height="{f(h * 0.28)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></rect>', ground(w, h, h * 0.74, "#B8A07A", dy=0)]
    s = fit(b, max(h * 0.4, b - 230))
    o.append(jer_fig(p, w * 0.5, b, s, age=age))
    o.append(man(p, w * 0.36, b, s, BABEL_C, extra=A.headcloth(BABEL_C, cord="#E8B830") + A.BLACK_BEARD))
    o.append(man(p, w * 0.72, b, s, "#5A4A3A", flip=True, up=[(22, -158), (44, -150), (66, -140)], extra=A.headcloth("#5A4A3A") + A.BLACK_BEARD))
    return "".join(o)
