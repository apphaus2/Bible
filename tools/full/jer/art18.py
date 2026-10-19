"""Drawings for Jeremiah chapter 18 (Jeremiah 51), on top of jer.art: the destroying wind and the winnowers, the golden cup, the
watchmen and the standard on Babylon's walls, the many waters, the battle-axe, the destroying mountain made a burnt mountain,
the kingdoms of Ararat, Minni and Ashkenaz (a map), the posts running, the reeds burned, the threshing-floor, the sea come up
upon Babylon, and Seraiah's book bound to a stone and sunk in the Euphrates."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2
from jer.art10 import babylon
from jer.art8 import cup
from jer.art5 import winnowing
from jer.art17 import archers, bel_shamed, hammer_broken, ostriches, babylon_king
from jer.art4 import heavens_waters

def destroying_wind(w, h, seed):
    """I will raise up against Babylon a destroying wind, and send strangers that shall winnow her: a wind tearing across the
    city, palms bent, dust and chaff driven."""
    r = random.Random(seed)
    o = [babylon(w, h, seed, dusk=True)]
    o.append(speed_lines(w, h, seed, 0.1, 0.8, color="#F3E0C0", n=26))
    o.append("".join(f'<path d="M{f(r.uniform(0, w))} {f(r.uniform(h * 0.1, h * 0.8))} l 14 -4" stroke="#C8A050" stroke-width="2"></path>' for _ in range(40)))
    return "".join(o)

def golden_cup(w, h, seed):
    """Babylon hath been a golden cup in Jehovah's hand, that made all the earth drunken: a golden cup overturned, wine spilled
    across the ground (no hand)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A0E14"></rect>', V.rays(w * 0.5, h * 0.6, 24, 10, max(w, h), color="#E8B830", op=0.12),
         ground(w, h, h * 0.8, "#3A2420", dy=0)]
    cx, cy, s = w * 0.42, h * 0.8, min(1.6, h / 170)
    o.append(f'<g transform="rotate(-78 {f(cx)} {f(cy)})"><path d="M{f(cx - 50 * s)} {f(cy - 100 * s)} L {f(cx + 50 * s)} {f(cy - 100 * s)} Q {f(cx + 44 * s)} {f(cy - 40 * s)} {f(cx + 8 * s)} {f(cy - 32 * s)} L {f(cx + 8 * s)} {f(cy - 10 * s)} L {f(cx + 28 * s)} {f(cy)} L {f(cx - 28 * s)} {f(cy)} L {f(cx - 8 * s)} {f(cy - 10 * s)} L {f(cx - 8 * s)} {f(cy - 32 * s)} Q {f(cx - 44 * s)} {f(cy - 40 * s)} {f(cx - 50 * s)} {f(cy - 100 * s)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.6"></path></g>')
    o.append(f'<path d="M{f(cx + 90 * s)} {f(cy - 8)} C {f(cx + 160 * s)} {f(cy + 4)} {f(cx + 240 * s)} {f(cy - 2)} {f(w * 0.96)} {f(cy + 6)}" stroke="#7A0A1E" stroke-width="{f(10 * s)}" fill="none" stroke-linecap="round"></path>')
    return "".join(o)

def walls_watch(p, w, h, seed):
    """Set up a standard against the walls of Babylon, make the watch strong, set the watchmen: watchmen on the blue towers at
    night, a standard planted before the wall."""
    o = [mk.defs(p, *ALL), night(w, h, seed, "#14122A"), J.moon(w * 0.86, h * 0.14, min(w, h) * 0.04), wall(-10, w + 10, h * 0.42, h * 0.84, seed, towers=4, gate=w * 0.5, color="#2A4A8A"),
         ground(w, h, h * 0.84, "#2A2230", dy=0), banner(w * 0.14, h * 0.96, min(0.9, h / 300))]
    s = fit(h * 0.32, h * 0.18)
    for k in range(4):
        tx = -10 + (w + 20) * (k + 0.5) / 4
        o.append(warrior(p, tx, h * 0.31, s, BABEL_C))
    return "".join(o)

def many_waters(w, h, seed):
    """O thou that dwellest upon many waters, abundant in treasures: Babylon among its canals, the river branching about it."""
    o = [K2.sky(w, h, "#8FB0C8", "#F3E0B0"), ground(w, h, h * 0.4, "#C8B078", dy=0)]
    for k in range(5):
        y = h * (0.46 + k * 0.11)
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 10)} {f(w * 0.6)} {f(y + 12)} {f(w + 10)} {f(y)}" stroke="#2C7A9A" stroke-width="{f(6 + (k % 2) * 4)}" fill="none"></path>')
    zx, zb = w * 0.5, h * 0.42
    o.append(wall(w * 0.2, w * 0.8, h * 0.28, h * 0.42, seed, towers=4, color="#2A5A9A"))
    for k in range(4):
        tw = w * (0.2 - k * 0.04)
        o.append(f'<rect x="{f(zx - tw / 2)}" y="{f(h * 0.28 - h * 0.05 * (k + 1))}" width="{f(tw)}" height="{f(h * 0.05)}" fill="#D8B080" stroke="#0D0D0F" stroke-width="1.8"></rect>')
    return "".join(o)

def canker_worm(w, h, seed):
    """Surely I will fill thee with men, as with the canker-worm: a cloud of locusts over the city."""
    return babylon(w, h, seed) + E2.locusts(60, 0, w, h * 0.04, h * 0.5, seed)

def battle_axe(w, h, seed):
    """Thou art my battle-axe and weapons of war: and with thee will I break in pieces the nations: a great battle-axe standing
    in a field strewn with broken chariot wheels, shields and spears (no hand)."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#3A2A3A", "#C88A6A"), ground(w, h, h * 0.6, "#8A7A5A", dy=0)]
    for _ in range(10):
        x, y = r.uniform(0, w), r.uniform(h * 0.66, h * 0.96)
        if r.random() < 0.4:
            o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(h * 0.05)}" fill="none" stroke="#5A3A1E" stroke-width="3"></circle><path d="M{f(x - h * 0.05)} {f(y)} L {f(x + h * 0.05)} {f(y)}" stroke="#5A3A1E" stroke-width="2"></path>')
        else:
            o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-40, 40))} {f(r.uniform(-6, 6))}" stroke="#3A2A1A" stroke-width="3"></path>')
    ax, ay, s = w * 0.5, h * 0.9, min(1.4, h / 180)
    o.append(f'<path d="M{f(ax)} {f(ay)} L {f(ax + 6 * s)} {f(ay - 150 * s)}" stroke="#6A4A2A" stroke-width="{f(7 * s)}" stroke-linecap="round"></path>'
             f'<path d="M{f(ax + 6 * s)} {f(ay - 150 * s)} C {f(ax + 50 * s)} {f(ay - 170 * s)} {f(ax + 60 * s)} {f(ay - 120 * s)} {f(ax + 5 * s)} {f(ay - 116 * s)} Z" fill="#A8A8B0" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(ax + 4 * s)} {f(ay - 148 * s)} C {f(ax - 30 * s)} {f(ay - 160 * s)} {f(ax - 36 * s)} {f(ay - 126 * s)} {f(ax + 3 * s)} {f(ay - 122 * s)} Z" fill="#A8A8B0" stroke="#0D0D0F" stroke-width="2.4"></path>')
    return "".join(o)

def burnt_mountain(w, h, seed):
    """O destroying mountain, I will roll thee down from the rocks, and make thee a burnt mountain; they shall not take of thee a
    stone for a corner: a blackened mountain, its rocks tumbled, smoke on its top."""
    o = [K2.sky(w, h, "#2A1A1A", "#8A4A2A"), crag(w * 0.1, w * 0.9, h + 10, h * 0.2, color="#2A2220", dark="#140E0C"), smoke(w * 0.5, h * 0.14, 8, seed, w=0.8),
         S4b.stone_heap(w * 0.16, h * 0.96, w * 0.2, h * 0.12, seed), S4b.stone_heap(w * 0.84, h * 0.96, w * 0.18, h * 0.1, seed + 1)]
    return "".join(o)

NORTH_N = ("ARARAT", "MINNI", "ASHKENAZ", "THE MEDES", "BABYLON")
def kingdoms_map(w, h):
    return near_east(w, h, NORTH_N, hi=NORTH_N[:-1], arrows=[(n, "BABYLON") for n in NORTH_N[:-1]], box=(36.0, 52.0, 29.0, 42.4), under=("MINNI",))

def posts(p, w, h, seed):
    """One post shall run to meet another, to show the king of Babylon that his city is taken on every quarter; the reeds they
    have burned with fire: runners along the river, the reed-beds burning behind."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A2A3A", "#C88A5A"), E.reeds(-10, w + 10, h * 0.6, h * 0.24, 30, seed),
         E.blaze(w * 0.3, h * 0.6, w * 0.2, h * 0.3, seed, n=6), E.blaze(w * 0.74, h * 0.6, w * 0.16, h * 0.24, seed + 1, n=5),
         f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 0.08)}" fill="#2C6A8A"></rect>', ground(w, h, h * 0.7, "#B89A6A", dy=0)]
    s = fit(b, max(h * 0.44, b - 200))
    o.append(S4b.runner(p, w * 0.24, b, s, cloth="#E8E2D6") + S4b.runner(p, w * 0.7, b, s * 0.94, cloth="#C8B8A0", flip=True))
    return "".join(o)

def threshing(p, w, h, seed):
    """The daughter of Babylon is like a threshing-floor at the time when it is trodden: oxen treading out the grain on a floor."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E8A060", "#F8E0A8"), ground(w, h, h * 0.6, "#C8A870", dy=0), S4b.threshing_floor(w * 0.5, b, w * 0.7)]
    s = min(1.0, h / 300)
    o.append(S1.cow(w * 0.36, b - 10, s, color="#8A5A30") + S1.cow(w * 0.62, b - 6, s * 0.95, flip=True, color="#C9A27A"))
    o.append(J1.chaff(30, w * 0.2, w * 0.8, h * 0.3, h * 0.7, seed))
    return "".join(o)

def sea_over(w, h, seed):
    """The sea is come up upon Babylon; she is covered with the multitude of the waves thereof: great waves rolling over the
    tops of the blue walls."""
    o = [K2.sky(w, h, "#2A3A5A", "#8AA0B8"), wall(-10, w + 10, h * 0.5, h * 0.9, seed, towers=4, color="#2A4A8A"),
         E3.crash(w, h, seed, color="#1F6F9A", deep="#0B2E4A", foam="#E8F6FA")]
    return "".join(o)

def sunk_book(p, w, h, seed, stage=0):
    """Seraiah at the Euphrates: stage 0, reading the book aloud on the bank; stage 1, the book bound to a stone and cast into the
    midst of the river, rings spreading where it sank."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E8A060", "#F8E0A8"), J1.palm(w * 0.9, h * 0.56, min(0.5, h / 600)),
         f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#2C6A8A"></rect>', ground(w, h, h * 0.8, "#C8A870", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    if stage == 0:
        o.append(man(p, w * 0.3, b, s, "#4A5A7A", up=[(-22, -158), (-40, -150), (-60, -150)], extra=A.headcloth("#4A5A7A") + A.BLACK_BEARD)
                 + f'<rect x="{f(w * 0.3 - 74 * s)}" y="{f(b - 166 * s)}" width="{f(30 * s)}" height="{f(30 * s)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    else:
        o.append(man(p, w * 0.3, b, s, "#4A5A7A", up=[(22, -158), (50, -190), (78, -220)], extra=A.headcloth("#4A5A7A") + A.BLACK_BEARD))
        for k in range(4):
            o.append(f'<ellipse cx="{f(w * 0.62)}" cy="{f(h * 0.64)}" rx="{f(w * (0.03 + k * 0.035))}" ry="{f(h * (0.012 + k * 0.012))}" fill="none" stroke="#E8F6FA" stroke-width="2" opacity="{0.9 - k * 0.18:.2f}"></ellipse>')
    return "".join(o)
