"""Drawings for the Amos volume, on top of Joel's and Hosea's (jol.art carries hos.art: Israel's land, olive trees, the
locusts, the maps). Amos at a distance: a brown herdsman's robe and headcloth, black beard, a staff (amos_fig); Amaziah the
priest: white robe and headcloth with a gold band, grey beard (amaziah_fig). The nations round Israel as a technical map,
each lit in turn with fire on its wall (nations); the plumb-line as a blueprint (plumb)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jol.art import *
from jol.art import f, K2
from hos.art2 import calf_broken, eagle, heifer, israel_map, PL, FIELD, oaks, altars, whirlwind_field
from hos.art3 import heaps, vanish
from kg1.art import bethel_altar, samaria_hill, calves, horned_altar, ivory_throne
from exo.art8 import bp, dim, tag, title_bar
import joshua1 as J1x, samuel1 as S1x, judges2 as JG, numbers1 as N1, exodus3 as E3
from genesis.art3 import flock, STAFF
from job.art3 import constellations

AMOS_C = "#7A5A3A"

def amos_fig(p, x, y, s, flip=False, up=None, staff=True):
    """Amos at a distance: a brown herdsman's robe and headcloth, a black beard, his staff."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=AMOS_C, sw=3, flip=flip, up=up,
                     extra=A.headcloth("#6A4A2A", cord="#2A1A10") + A.BLACK_BEARD + (STAFF if staff and not up else ""))

def amaziah_fig(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#E8E2D6", sw=3, flip=flip, up=up, extra=A.headcloth("#F3EFE6", cord="#E8B830") + GREY_BEARD)

from est.art import GREY_BEARD

# ---- Amos 1–4 -------------------------------------------------------------------------------------------------------------------
def tekoa(p, w, h, seed):
    """Among the herdsmen of Tekoa: Amos with his staff on the bare hills south of Jerusalem, his flock about him."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#9AB8D8", "#F3E0B0"), hills(w, h, h * 0.46, seed, "#B8A070", amp=16, step=120),
         hills(w, h, h * 0.58, seed + 1, "#A88A5A", amp=12, step=90), ground(w, h, h * 0.7, "#C8A878", dy=0)]
    o.append(flock(w * 0.4, w * 0.96, h * 0.72, b, 12, seed))
    o.append(amos_fig(p, w * 0.22, b, fit(b, b - h * 0.52)))
    return "".join(o)

def carmel(w, h, seed):
    """Jehovah will roar from Zion: the pastures of the shepherds mourn and the top of Carmel withers — the ridge above the sea
    browned and dry, rings of sound rolling over it."""
    o = [K2.sky(w, h, "#C8A880", "#F0D8B0"), f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w * 0.4)}" height="{f(h * 0.4)}" fill="#3A6A8A" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.1)} {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.3)} {f(w * 0.6)} {f(h * 0.3)} {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.1)} {f(h + 10)} Z" fill="#A88A5A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    r = random.Random(seed)
    for i in range(30):
        x = r.uniform(w * 0.2, w); y = r.uniform(h * 0.42, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-3, 3))} {f(-r.uniform(6, 14))}" stroke="#7A5A3A" stroke-width="1.6"></path>')
    for i in range(4):
        o.append(f'<path d="M{f(w * 0.96 - i * w * 0.08)} {f(h * 0.1)} A {f(w * 0.2 + i * w * 0.08)} {f(h * 0.3 + i * h * 0.08)} 0 0 0 {f(w * 0.96 - i * w * 0.08)} {f(h * 0.7)}" fill="none" stroke="#FFD23F" stroke-width="1.6" opacity="{0.6 - i * 0.12}"></path>')
    o.append(label(w * 0.5, h * 0.26, "THE TOP OF CARMEL", "#3A2A1A", max(8, min(11, h / 22))))
    return "".join(o)

NAT = {"DAMASCUS": (0.78, 0.16), "GAZA": (0.18, 0.86), "TYRE": (0.34, 0.12), "EDOM": (0.62, 0.86), "AMMON": (0.84, 0.5), "MOAB": (0.76, 0.74),
       "JUDAH": (0.42, 0.74), "ISRAEL": (0.5, 0.38), "ASHDOD": (0.2, 0.66), "ASHKELON": (0.16, 0.76), "EKRON": (0.26, 0.6), "TEMAN": (0.46, 0.92),
       "BOZRAH": (0.78, 0.9), "RABBAH": (0.86, 0.56), "KERIOTH": (0.74, 0.8), "JERUSALEM": (0.54, 0.62), "KIR": (0.96, 0.06), "SAMARIA": (0.48, 0.42),
       "BETH-EL": (0.52, 0.56), "GILGAL": (0.62, 0.58), "BEER-SHEBA": (0.4, 0.88), "DAN": (0.6, 0.12), "CALNEH": (0.98, 0.24), "HAMATH": (0.74, 0.02),
       "GATH": (0.24, 0.72), "ARABAH": (0.66, 0.84)}
ORDER = ["DAMASCUS", "GAZA", "TYRE", "EDOM", "AMMON", "MOAB", "JUDAH", "ISRAEL"]
def nations(w, h, lit=None, fire=(), extra=(), moves=(), title=""):
    """The nations round Israel as a technical map: the great sea on the west, the Jordan and the Dead Sea; the eight of
    1:3–2:16 marked, the one `lit` red with a ring; fire = places drawn burning; extra = other places named; moves = arrows."""
    o = [grid_bg(w, h),
         f'<path d="M-10 -10 L {f(w * 0.24)} -10 C {f(w * 0.3)} {f(h * 0.3)} {f(w * 0.18)} {f(h * 0.6)} {f(w * 0.1)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.64)} {f(h * 0.1)} C {f(w * 0.62)} {f(h * 0.3)} {f(w * 0.66)} {f(h * 0.45)} {f(w * 0.62)} {f(h * 0.58)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>'
         f'<ellipse cx="{f(w * 0.62)}" cy="{f(h * 0.7)}" rx="{f(w * 0.025)}" ry="{f(h * 0.1)}" fill="#2C9DB8"></ellipse>']
    for nm in list(dict.fromkeys(ORDER + list(extra))):
        if nm not in ORDER and nm not in extra: continue
        x, y = NAT[nm]
        on = nm == lit
        big = nm in ORDER
        o.append(node(w * x, h * y, nm, "#FF8A6A" if on else ("#FFD23F" if big else CYAN), r=7 if big else 4, dy=-12 if y > 0.08 else 16, size=10 if on else 8))
        if on: o.append(f'<circle cx="{f(w * x)}" cy="{f(h * y)}" r="{f(min(w, h) * 0.06)}" fill="none" stroke="#FF8A6A" stroke-width="2" stroke-dasharray="4 3"></circle>')
    for nm in fire:
        x, y = NAT[nm]
        o.append(E.flame(w * x + min(w, h) * 0.07, h * y + 8, min(w, h) * 0.025, min(w, h) * 0.06, 1))
    for a, b2 in moves:
        (x0, y0), (x1, y1) = NAT[a], NAT[b2]
        o.append(route([(w * x0, h * y0), (w * x1, h * y1)], color="#FF8A6A"))
    if title: o.append(label(w * 0.98, h * 0.04 + 8, title, "#F3EFE6", 9, anchor="end"))
    return "".join(o)

def tally(w, h, n=8, lit=0):
    """For three transgressions, yea, for four: three marks and a fourth in red, as a plate (n nations' marks along the foot)."""
    o = [grid_bg(w, h)]
    k = min(1.6, h / 120)
    for i in range(4):
        x = w * (0.2 + i * 0.12)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.2)}" width="{f(w * 0.05)}" height="{f(h * 0.5)}" fill="{"#D7261E" if i == 3 else "#FFD23F"}" fill-opacity="0.4" stroke="{"#D7261E" if i == 3 else "#FFD23F"}" stroke-width="2"></rect>')
    o.append(label(w * 0.38, h * 0.86, "THREE TRANSGRESSIONS · YEA, FOR FOUR", "#FFD23F", max(8, min(10, 7 * k))))
    return "".join(o)

def burning_wall(w, h, seed, city="palace"):
    """A fire sent on the wall of a city, devouring its palaces (no one drawn)."""
    o = [K2.sky(w, h, "#2A0A0A", "#8A2A1A"), J.jericho(w * 0.06, w * 0.94, h * 0.36, h * 0.86, seed, towers=4, houses=True), ground(w, h, h * 0.86, "#2A1A1A", dy=0)]
    for i in range(4):
        o.append(E.blaze(w * (0.16 + i * 0.22), h * 0.5, w * 0.12, h * 0.24, seed + i, n=5))
    o.append(smoke(w * 0.5, h * 0.26, 6, seed, color="#3A2A2A", op=0.6, k=min(1.6, h / 260)))
    return "".join(o)

def sold(w, h):
    """They have sold the righteous for silver, and the needy for a pair of shoes: a balance with a pair of sandals in one pan."""
    o = [grid_bg(w, h)]
    k = min(1.6, h / 140)
    cx, cy = w * 0.5, h * 0.3
    o.append(f'<path d="M{f(cx)} {f(cy)} L {f(cx)} {f(h * 0.86)} M{f(cx - 30 * k)} {f(h * 0.86)} L {f(cx + 30 * k)} {f(h * 0.86)}" stroke="#FFD23F" stroke-width="2.4"></path>'
             f'<path d="M{f(cx - 120 * k)} {f(cy + 10 * k)} L {f(cx + 120 * k)} {f(cy - 10 * k)}" stroke="#FFD23F" stroke-width="2.4"></path>')
    for sx, dy, t in ((-1, 10, "THE NEEDY"), (1, -10, "A PAIR OF SHOES")):
        x0 = cx + sx * 120 * k; y0 = cy + dy * k
        o.append(f'<path d="M{f(x0)} {f(y0)} L {f(x0 - 30 * k)} {f(y0 + 50 * k)} M{f(x0)} {f(y0)} L {f(x0 + 30 * k)} {f(y0 + 50 * k)}" stroke="#FFD23F" stroke-width="1.2"></path>'
                 f'<path d="M{f(x0 - 36 * k)} {f(y0 + 50 * k)} C {f(x0 - 30 * k)} {f(y0 + 66 * k)} {f(x0 + 30 * k)} {f(y0 + 66 * k)} {f(x0 + 36 * k)} {f(y0 + 50 * k)} Z" fill="#FFD23F" fill-opacity="0.25" stroke="#FFD23F" stroke-width="2"></path>'
                 + label(x0, y0 + 84 * k, t, CYAN, max(8, min(10, 6 * k))))
    o.append(E.sandal(cx + 108 * k, cy + 52 * k, 0.4 * k, -80) + E.sandal(cx + 132 * k, cy + 52 * k, 0.4 * k, -100))
    return "".join(o)

def amorite(w, h, seed):
    """Yet destroyed I the Amorite, whose height was like the height of the cedars: a great cedar cut down, its fruit fallen
    and its roots torn up."""
    o = [land(w, h, seed, tone="day", olives=0, horizon=0.44)]
    k = min(1.6, h / 260)
    cx, by = w * 0.3, h * 0.88
    o.append(f'<path d="M{f(cx - 16 * k)} {f(by)} L {f(cx - 12 * k)} {f(by - 40 * k)} L {f(cx + 12 * k)} {f(by - 36 * k)} L {f(cx + 16 * k)} {f(by)} Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(cx)} {f(by)} l {f(math.cos(math.radians(a)) * 40 * k)} {f(math.sin(math.radians(a)) * 12 * k)}" stroke="#5A3A22" stroke-width="{f(4 * k)}" stroke-linecap="round"></path>' for a in (10, 40, 140, 170)))
    tx, ty = w * 0.36, h * 0.84
    o.append(f'<g transform="rotate(-8 {f(tx)} {f(ty)})"><rect x="{f(tx)}" y="{f(ty - 12 * k)}" width="{f(w * 0.5)}" height="{f(16 * k)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(tx + w * (0.1 + i * 0.08))} {f(ty - 12 * k)} l {f(-20 * k)} {f(-30 * k)} m {f(20 * k)} {f(30 * k)} l {f(24 * k)} {f(-28 * k)}" stroke="#2E5A3A" stroke-width="{f(6 * k)}" stroke-linecap="round"></path>' for i in range(5)) + '</g>')
    return "".join(o)

def nazirite(p, w, h, seed):
    """Ye gave the Nazirites wine to drink, and commanded the prophets, saying, Prophesy not: a cup held out to a man with long
    unshorn hair; a man with his hand raised over a prophet's mouth."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), land(w, h, seed, tone="dusk", olives=1)]
    s = fit(b, b - h * 0.5)
    locks = '<path d="M-14 -186 C -22 -170 -24 -150 -20 -130 M14 -186 C 22 -170 24 -150 20 -130" stroke="#1A1210" stroke-width="6" fill="none" stroke-linecap="round"></path>'
    o.append(mk.person(p, round(w * 0.18), round(b), round(s, 3), body=SKIN, cloth="#E8E2D6", sw=3, extra=locks + A.BLACK_BEARD))
    o.append(man(p, w * 0.34, b, s, "#7A1A2A", flip=True, up=[(-22, -158), (-46, -150), (-70, -152)]) + cup(w * 0.34 - 74 * s, b - 150 * s, s * 0.6, fill="#7A1A2A"))
    o.append(amos_fig(p, w * 0.68, b, s, staff=False) + man(p, w * 0.84, b, s, "#3A3A5A", flip=True, up=[(-22, -158), (-46, -170), (-70, -172)]))
    return "".join(o)

def cart_sheaves(w, h, seed):
    """I will press you in your place, as a cart presseth that is full of sheaves: a cart heaped high with sheaves, its
    wheels pressed deep into the ground."""
    import ruth1 as R1x
    o = [land(w, h, seed, tone="day", olives=1, horizon=0.44)]
    k = min(2.4, h / 130)
    cx, by = w * 0.5, h * 0.94
    o.append(f'<path d="M{f(cx - 90 * k)} {f(by - 40 * k)} L {f(cx + 90 * k)} {f(by - 40 * k)} L {f(cx + 80 * k)} {f(by - 20 * k)} L {f(cx - 80 * k)} {f(by - 20 * k)} Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>')
    for i in range(9):
        o.append(R1x.sheaf(cx - 70 * k + (i % 5) * 34 * k, by - 40 * k - (i // 5) * 26 * k, 0.5 * k))
    for dx in (-60, 60):
        o.append(f'<circle cx="{f(cx + dx * k)}" cy="{f(by - 10 * k)}" r="{f(22 * k)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.4"></circle><circle cx="{f(cx + dx * k)}" cy="{f(by - 10 * k)}" r="{f(5 * k)}" fill="#3A2A1A"></circle>')
    o.append(f'<path d="M{f(cx - 100 * k)} {f(by + 6 * k)} C {f(cx - 60 * k)} {f(by + 16 * k)} {f(cx + 60 * k)} {f(by + 16 * k)} {f(cx + 100 * k)} {f(by + 6 * k)}" stroke="#5A3A22" stroke-width="3" fill="none"></path>')
    return "".join(o)

def mighty_flee(p, w, h, seed):
    """Flight shall perish from the swift: the swift, the bowman and the horseman scattered in flight across the plain."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A3A3A", "#C88A5A"), hills(w, h, h * 0.5, seed, "#6A4A3A", amp=12, step=100), ground(w, h, h * 0.62, "#8A6A4A", dy=0)]
    s = fit(b, b - h * 0.4)
    for i in range(5):
        x = w * (0.1 + i * 0.18); y = b - (i % 2) * h * 0.08
        o.append(man(p, x, y, s * (1 - (i % 2) * 0.15), ("#5A4A3A", "#6A3A2A", "#4A4A3A", "#7A5A3A", "#3A3A4A")[i], flip=True, up=[(-22, -158), (-40, -140), (-56, -150)]))
    o.append(f'<path d="M{f(w * 0.7)} {f(b)} C {f(w * 0.72)} {f(b - 40)} {f(w * 0.74)} {f(b - 50)} {f(w * 0.78)} {f(b - 54)}" fill="none" stroke="#6A3A1A" stroke-width="4"></path>')
    return "".join(o)

def two_walk(w, h):
    """Shall two walk together, except they have agreed? a lion and its prey, a bird and the snare, a trumpet and the city —
    cause and effect, as a plate of linked pairs."""
    o = [grid_bg(w, h)]
    pairs = [("TWO WALK", "AGREED"), ("A LION ROARS", "PREY"), ("A BIRD FALLS", "A GIN SET"), ("A TRUMPET", "AFRAID"), ("EVIL", "JEHOVAH HATH DONE IT")]
    for i, (a, b2) in enumerate(pairs):
        y = h * (0.14 + i * 0.18)
        o.append(node(w * 0.2, y, a, "#FFD23F", r=5, dy=-10, size=9) + route([(w * 0.24, y), (w * 0.72, y)], color="#8FD0E2") + node(w * 0.78, y, b2, "#FF8A6A", r=5, dy=-10, size=9))
    return "".join(o)

def lion_roar(w, h, seed):
    """The lion hath roared; who will not fear?: a lion roaring in the thicket at dusk."""
    o = [K2.sky(w, h, "#5A3A3A", "#E8A06A"), hills(w, h, h * 0.56, seed, "#6A5A3A", amp=12, step=100), ground(w, h, h * 0.7, "#8A7A4A", dy=0)]
    k = min(h / 300, w / 600)
    o.append(JG.lion(w * 0.24, h * 0.98, k * 1.1, roar=True))
    for i in range(4):
        o.append(f'<path d="M{f(w * 0.62 + i * 26)} {f(h * 0.3)} A {f(30 + i * 30)} {f(50 + i * 30)} 0 0 1 {f(w * 0.62 + i * 26)} {f(h * 0.7)}" fill="none" stroke="#FFD23F" stroke-width="2" opacity="{0.7 - i * 0.15}"></path>')
    o.append(tree(w * 0.9, h * 0.78, min(1.2, h / 260), color="#3A5A2A", kind="round", seed=seed))
    return "".join(o)

def samaria_mount(w, h, seed, palaces=True):
    """The mountains of Samaria, the city on its hill with its palaces, the nations bidden to assemble round it."""
    o = [K2.sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, "#7A8A6A", amp=14, step=100),
         J.city_hill(w * 0.5, h * 0.86, w * 0.36, h * 0.42, seed), ground(w, h, h * 0.86, "#A89A6A", dy=0)]
    return "".join(o)

def lion_mouth(w, h, seed):
    """As the shepherd rescueth out of the mouth of the lion two legs, or a piece of an ear: a shepherd's staff and a scrap of
    ear held up beside the lion's track in the dust — nothing more."""
    o = [land(w, h, seed, tone="grey", olives=0, horizon=0.44)]
    k = min(1.6, h / 220)
    cx, by = w * 0.4, h * 0.9
    o.append(f'<path d="M{f(cx)} {f(by)} L {f(cx + 10 * k)} {f(by - 120 * k)} C {f(cx + 12 * k)} {f(by - 140 * k)} {f(cx + 30 * k)} {f(by - 140 * k)} {f(cx + 28 * k)} {f(by - 124 * k)}" fill="none" stroke="#5A3A22" stroke-width="{f(5 * k)}" stroke-linecap="round"></path>')
    for i in range(5):
        o.append(f'<g transform="translate({f(w * (0.56 + i * 0.08))} {f(by - (i % 2) * 8)}) scale({f(k * 0.5)})"><ellipse cx="0" cy="0" rx="10" ry="8" fill="#5A4A3A"></ellipse>'
                 + "".join(f'<circle cx="{dx}" cy="-12" r="3.6" fill="#5A4A3A"></circle>' for dx in (-8, -3, 3, 8)) + '</g>')
    return "".join(o)

def couch(w, h, seed):
    """Them that sit in Samaria in the corner of a couch, and on the silken cushions of a bed: an empty couch with silk cushions
    in a palace room."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A3A3A"></rect>', bab_floor(w, h, h * 0.74, color="#8A6A4A")]
    k = min(1.6, h / 220)
    cx, by = w * 0.5, h * 0.86
    o.append(f'<rect x="{f(cx - 120 * k)}" y="{f(by - 40 * k)}" width="{f(240 * k)}" height="{f(30 * k)}" fill="#E8DCC8" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<path d="M{f(cx - 120 * k)} {f(by - 40 * k)} L {f(cx - 130 * k)} {f(by - 90 * k)} L {f(cx - 104 * k)} {f(by - 90 * k)} L {f(cx - 100 * k)} {f(by - 40 * k)} Z" fill="#E8DCC8" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + "".join(f'<rect x="{f(cx + d * k)}" y="{f(by - 10 * k)}" width="{f(8 * k)}" height="{f(14 * k)}" fill="#C8962E" stroke="#0D0D0F" stroke-width="1.4"></rect>' for d in (-116, 108))
             + "".join(f'<ellipse cx="{f(cx + d * k)}" cy="{f(by - 48 * k)}" rx="{f(30 * k)}" ry="{f(12 * k)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></ellipse>' for d, c in ((-70, "#7A2A6A"), (-10, "#2A6A8A"), (50, "#C8962E"))))
    return "".join(o)

def horns_cut(w, h, seed):
    """The horns of the altar of Beth-el cut off and fallen to the ground; the winter-house and the summer-house, the houses
    of ivory, broken."""
    o = [K2.sky(w, h, "#5A3A5A", "#C88A6A"), ground(w, h, h * 0.8, "#6A5A4A", dy=0)]
    k = min(1.6, h / 220)
    o.append(horned_altar(w * 0.3, h * 0.84, k * 0.8).replace('<path d="M-66 -98 L -58 -122 L -50 -98 Z"', '<path d="M-66 -98 L -66 -98 Z"'))
    o.append(f'<path d="M{f(w * 0.12)} {f(h * 0.84)} l {f(14 * k)} {f(-8 * k)} l {f(4 * k)} {f(10 * k)} Z M{f(w * 0.44)} {f(h * 0.86)} l {f(12 * k)} {f(-10 * k)} l {f(6 * k)} {f(10 * k)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append(J1x.collapse(w * 0.56, w * 0.98, h * 0.8, h * 0.36, seed, color="#E8DCC8"))
    return "".join(o)

def kine(w, h, seed):
    """Ye kine of Bashan, that are in the mountain of Samaria: fat cattle at ease on the green hill, Samaria above them."""
    o = [K2.sky(w, h, "#8FD0E2", "#F3E8C8"), J.city_hill(w * 0.72, h * 0.5, w * 0.24, h * 0.22, seed), hills(w, h, h * 0.52, seed, "#7A9A4A", amp=10, step=100),
         ground(w, h, h * 0.62, "#9CCB5E", dy=0)]
    k = min(1.0, h / 320)
    for i in range(4):
        o.append(S1x.cow(w * (0.14 + i * 0.22), h * (0.88 + (i % 2) * 0.05), k * (0.9 + (i % 2) * 0.1), color=("#C9A27A", "#8A5A30", "#E8D8C0", "#6A4A3A")[i], flip=i % 2 == 1))
    return "".join(o)

def hooks(w, h, seed):
    """They shall take you away with hooks, and your residue with fish-hooks; ye shall go out at the breaches: a breach in
    the wall, hooks hanging on cords."""
    o = [K2.sky(w, h, "#5A4A5A", "#C8A080"), J1x.collapse(-10, w + 10, h * 0.86, h * 0.5, seed, color="#A89880"), ground(w, h, h * 0.86, "#6A5A4A", dy=0)]
    k = min(1.4, h / 220)
    for i in range(5):
        x = w * (0.2 + i * 0.15)
        o.append(f'<path d="M{f(x)} -10 L {f(x)} {f(h * 0.3 + (i % 2) * 20)}" stroke="#C8B898" stroke-width="1.6"></path>'
                 f'<path d="M{f(x)} {f(h * 0.3 + (i % 2) * 20)} l 0 {f(14 * k)} c 0 {f(10 * k)} {f(-12 * k)} {f(10 * k)} {f(-12 * k)} 0" fill="none" stroke="#8A9AA8" stroke-width="{f(3 * k)}" stroke-linecap="round"></path>')
    return "".join(o)

def bethel_gilgal(w, h, seed):
    """Come to Beth-el, and transgress; to Gilgal, and multiply transgression: the calf on its high place at Beth-el, altars
    smoking, sacrifices every morning."""
    o = [K2.sky(w, h, "#5A3A5A", "#E8A06A"), hills(w, h, h * 0.5, seed, "#6A5A4A", amp=14, step=100), ground(w, h, h * 0.62, "#8A7A5A", dy=0)]
    k = min(1.2, h / 300)
    o.append(V.calf(w * 0.3, h * 0.66, k * 0.6, uid=f"bg{seed}"))
    for i in range(4):
        x = w * (0.56 + i * 0.12); y = h * (0.8 + (i % 2) * 0.06)
        o.append(f'<path d="M{f(x - 14 * k)} {f(y)} L {f(x - 10 * k)} {f(y - 22 * k)} L {f(x + 10 * k)} {f(y - 22 * k)} L {f(x + 14 * k)} {f(y)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></path>'
                 + E.flame(x, y - 22 * k, 6 * k, 14 * k, 1) + smoke(x, y - 36 * k, 3, seed + i, color="#C8B8C8", op=0.45, k=k * 0.5))
    o.append(label(w * 0.3, h * 0.96, "BETH-EL", "#F3EFE6", 9) + label(w * 0.74, h * 0.98, "GILGAL", "#F3EFE6", 9))
    return "".join(o)

def empty_bowls(w, h, seed):
    """Cleanness of teeth in all your cities, and want of bread: empty bowls and an empty bread basket on a bare table."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A3A30"></rect>', f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h * 0.32)}" fill="#6A4A30" stroke="#0D0D0F" stroke-width="2"></rect>']
    k = min(1.6, h / 200)
    for i in range(4): o.append(bowl(w * (0.2 + i * 0.2), h * 0.74, k, fill="#3A2A20", color="#B5652E"))
    return "".join(o)

def rain_one_city(w, h, seed):
    """I caused it to rain upon one city, and caused it not to rain upon another: rain falling on one walled city, the next
    one dry under the sun, people walking between them to drink."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#C8B898", "#F0E0B0"), sun(w * 0.8, h * 0.18, max(10, h * 0.05), color="#FFC14D", op=0.3),
         f'<path d="M-10 -10 L {f(w * 0.46)} -10 L {f(w * 0.46)} {f(h * 0.3)} C {f(w * 0.3)} {f(h * 0.36)} {f(w * 0.1)} {f(h * 0.3)} -10 {f(h * 0.34)} Z" fill="#6A7A8A"></path>',
         ground(w, h, h * 0.7, "#B89A6A", dy=0), f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w * 0.48)}" height="{f(h * 0.32)}" fill="#7A9A4A"></rect>',
         J.city_hill(w * 0.22, h * 0.74, w * 0.18, h * 0.2, seed), J.city_hill(w * 0.78, h * 0.74, w * 0.18, h * 0.2, seed + 1)]
    o.append("".join(f'<path d="M{f(r.uniform(0, w * 0.44))} {f(r.uniform(h * 0.3, h * 0.66))} l -4 12" stroke="#C8E8F0" stroke-width="1.4"></path>' for _ in range(50)))
    o.append(route([(w * 0.7, h * 0.86), (w * 0.34, h * 0.86)], color="#5A3A22"))
    return "".join(o)

def blasted(w, h, seed):
    """Blasting and mildew: gardens, vineyards, fig-trees and olive-trees grey and spotted, the palmer-worm in them."""
    o = [K2.sky(w, h, "#9A9A8A", "#D8D0B0"), hills(w, h, h * 0.5, seed, "#9A9A7A", amp=10, step=100), ground(w, h, h * 0.6, "#A89A7A", dy=0),
         vine_rows(w, h, h * 0.64, h * 0.98, seed, rows=4)]
    r = random.Random(seed)
    o.append("".join(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.6, h))}" r="{f(r.uniform(2, 5))}" fill="#8A8A6A" opacity="0.7"></circle>' for _ in range(60)))
    o.append("".join(worm(r.uniform(0, w), r.uniform(h * 0.7, h), 0.3, "#7A8A3A") for _ in range(6)))
    return "".join(o)

def brand(w, h, seed):
    """As when God overthrew Sodom and Gomorrah, and ye were as a brand plucked out of the burning: smoking ruins on the plain,
    one charred brand lying apart."""
    o = [K2.sky(w, h, "#3A1A1A", "#A85A3A"), J1x.collapse(-10, w * 0.6, h * 0.84, h * 0.3, seed, color="#5A4A3A"), ground(w, h, h * 0.84, "#3A2A22", dy=0)]
    o.append(smoke(w * 0.3, h * 0.5, 6, seed, color="#4A3A3A", op=0.6, k=min(1.6, h / 260)))
    k = min(1.6, h / 220)
    o.append(f'<g transform="rotate(-14 {f(w * 0.8)} {f(h * 0.86)})"><rect x="{f(w * 0.7)}" y="{f(h * 0.86 - 8 * k)}" width="{f(w * 0.2)}" height="{f(14 * k)}" rx="{f(6 * k)}" fill="#2A1A10" stroke="#0D0D0F" stroke-width="2"></rect></g>'
             + E.flame(w * 0.89, h * 0.82, 6 * k, 14 * k, 1))
    return "".join(o)

def he_formeth(w, h, seed):
    """He that formeth the mountains, and createth the wind, that maketh the morning darkness, and treadeth upon the high
    places of the earth: mountains under a dark dawn, the wind driving over them."""
    o = [K2.sky(w, h, "#1A1A3A", "#8A5A6A"), sun(w * 0.5, h * 0.5, max(10, h * 0.05), color="#3A2A3A", op=0.3)]
    for i, (x, ht, c) in enumerate(((0.2, 0.5, "#3A3040"), (0.5, 0.66, "#2A2030"), (0.82, 0.46, "#3A3040"))):
        o.append(f'<path d="M{f(w * x - w * 0.28)} {f(h)} L {f(w * x)} {f(h * (1 - ht))} L {f(w * x + w * 0.28)} {f(h)} Z" fill="{c}" stroke="#0D0D0F" stroke-width="2"></path>')
    for i in range(6):
        y = h * (0.12 + i * 0.07)
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 14)} {f(w * 0.6)} {f(y + 14)} {f(w + 10)} {f(y)}" fill="none" stroke="#C8C0D8" stroke-width="1.6" opacity="0.5" stroke-dasharray="14 10"></path>')
    return "".join(o)
