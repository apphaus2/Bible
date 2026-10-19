"""Isaiah 6–9 drawings (on top of isa.art): the nations map used through the whole book, the felled stock, the conduit of the
upper pool, the two firebrands, Immanuel, the fly and the bee, the great tablet, the River's flood, the great light, the
broken yoke, the throne of David."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower

# ---- the nations: one technical map for the whole book ---------------------------------------------------------------------
PLACES = {"TYRE": (0.215, 0.30), "SIDON": (0.225, 0.235), "DAMASCUS": (0.33, 0.27), "SAMARIA": (0.215, 0.39), "JERUSALEM": (0.225, 0.47),
          "PHILISTIA": (0.14, 0.50), "MOAB": (0.3, 0.53), "EDOM": (0.28, 0.65), "EGYPT": (0.08, 0.74), "ETHIOPIA": (0.12, 0.95),
          "KEDAR": (0.42, 0.6), "DUMAH": (0.48, 0.46), "TEMA": (0.44, 0.74), "HAMATH": (0.33, 0.14), "ARPAD": (0.4, 0.07),
          "CARCHEMISH": (0.48, 0.05), "NINEVEH": (0.7, 0.11), "BABYLON": (0.77, 0.5), "ELAM": (0.93, 0.52), "MEDIA": (0.9, 0.2),
          "TARSHISH": (0.04, 0.2), "KITTIM": (0.1, 0.26), "SEBA": (0.3, 0.97)}
def nations_map(w, h, hi=(), arrows=(), show=None, lit="#D7261E", note=None):
    """The lands of Isaiah's burdens as one technical map: the great sea on the left, the Nile, the Euphrates and the
    Tigris; hi = places lit red, arrows = (from, to) pairs; show = the places named (default all)."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.2)} -10 C {f(w * 0.19)} {f(h * 0.2)} {f(w * 0.2)} {f(h * 0.4)} {f(w * 0.19)} {f(h * 0.52)} C {f(w * 0.16)} {f(h * 0.6)} {f(w * 0.1)} {f(h * 0.64)} {f(w * 0.02)} {f(h * 0.64)} L -10 {f(h * 0.64)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.07)} {f(h * 0.64)} C {f(w * 0.09)} {f(h * 0.76)} {f(w * 0.08)} {f(h * 0.88)} {f(w * 0.11)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>'
             f'<path d="M{f(w * 0.2)} {f(h * 0.7)} L {f(w * 0.26)} {f(h * 0.78)} L {f(w * 0.3)} {f(h + 10)} L {f(w * 0.24)} {f(h + 10)} L {f(w * 0.18)} {f(h * 0.76)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="1.6"></path>')
    o.append(f'<path d="M{f(w * 0.46)} -10 C {f(w * 0.5)} {f(h * 0.2)} {f(w * 0.7)} {f(h * 0.4)} {f(w * 0.84)} {f(h * 0.66)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>'
             f'<path d="M{f(w * 0.66)} -10 C {f(w * 0.7)} {f(h * 0.2)} {f(w * 0.8)} {f(h * 0.4)} {f(w * 0.86)} {f(h * 0.64)}" stroke="#2C9DB8" stroke-width="2.4" fill="none"></path>'
             f'<path d="M{f(w * 0.8)} {f(h * 0.66)} C {f(w * 0.86)} {f(h * 0.7)} {f(w * 0.96)} {f(h * 0.76)} {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.86)} {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="1.6"></path>'
             + label(w * 0.58, h * 0.3, "EUPHRATES", "#4A8AAA", 8) + label(w * 0.03, h * 0.56, "THE GREAT SEA", "#4A8AAA", 8, "start"))
    pos = {n: (w * x, h * y) for n, (x, y) in PLACES.items()}
    for a, b in arrows: o.append(route([pos[a], pos[b]], color=lit))
    names = show or list(PLACES)
    size = max(8, min(10, w / 70))
    for nm in names:
        x, y = pos[nm]
        o.append(node(x, y, nm, lit if nm in hi else ("#FFD23F" if nm == "JERUSALEM" else "#8FD0E2"), r=6 if nm in hi else 4, dy=-11, size=size + (1 if nm in hi else 0)))
    if note: o.append(label(w * 0.97, h * 0.08, note, "#FF8A6A", 10, "end"))
    return "".join(o)

# ---- Isaiah 6–9 ----------------------------------------------------------------------------------------------------------
def stump(w, h, seed, shoot=False, waste=True):
    """As a terebinth, and as an oak, whose stock remaineth, when they are felled: a great stump in a wasted land, empty houses
    beyond (shoot=True: a green shoot springing out of the stock)."""
    r = random.Random(seed)
    o = [bg(w, h, "#7A7A8A" if waste else "#8FD0E2", "#D8C8A8" if waste else "#F3E8C8"), hills(w, h, h * 0.56, seed, color="#8A7A6A" if waste else "#7A9A5A", amp=10)]
    if waste:
        for i in range(5):
            x = w * (0.08 + i * 0.2) + r.uniform(-20, 20); y = h * 0.58
            o.append(f'<path d="M{f(x - 18)} {f(y)} L {f(x - 18)} {f(y - 16)} L {f(x - 4)} {f(y - 10)} L {f(x + 4)} {f(y - 20)} L {f(x + 18)} {f(y - 12)} L {f(x + 18)} {f(y)} Z" fill="#5A4A4A" stroke="#0D0D0F" stroke-width="1.4"></path>')
    o.append(ground(w, h, h * 0.7, "#A89068" if waste else "#8AA05A", dy=0))
    s = min(2.2, h / 230); cx, b = w * 0.5, h * 0.9
    o.append(f'<path d="M{f(cx - 80 * s)} {f(b)} C {f(cx - 60 * s)} {f(b - 10 * s)} {f(cx - 50 * s)} {f(b - 40 * s)} {f(cx - 46 * s)} {f(b - 70 * s)} L {f(cx + 46 * s)} {f(b - 70 * s)} C {f(cx + 50 * s)} {f(b - 40 * s)} {f(cx + 60 * s)} {f(b - 10 * s)} {f(cx + 84 * s)} {f(b)} Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.6"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(b - 70 * s)}" rx="{f(46 * s)}" ry="{f(12 * s)}" fill="#C8A070" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
             + "".join(f'<ellipse cx="{f(cx)}" cy="{f(b - 70 * s)}" rx="{f(46 * s * k / 5)}" ry="{f(12 * s * k / 5)}" fill="none" stroke="#8A6A3A" stroke-width="1.2"></ellipse>' for k in range(1, 5)))
    o.append(f'<path d="M{f(cx + 90 * s)} {f(b + 4)} L {f(w * 0.98)} {f(b - 20 * s)}" stroke="#5A3A22" stroke-width="{f(18 * s)}" stroke-linecap="round"></path>')
    if shoot:
        o.append(f'<path d="M{f(cx + 10 * s)} {f(b - 72 * s)} C {f(cx + 4 * s)} {f(b - 100 * s)} {f(cx + 20 * s)} {f(b - 120 * s)} {f(cx + 12 * s)} {f(b - 150 * s)}" stroke="#3E7A2A" stroke-width="{f(5 * s)}" fill="none"></path>'
                 + "".join(f'<path d="M{f(cx + 12 * s + (14 if k % 2 else -14) * s)} {f(b - (100 + k * 14) * s)} C {f(cx + 12 * s)} {f(b - (104 + k * 14) * s)} {f(cx + 12 * s)} {f(b - (98 + k * 14) * s)} {f(cx + 14 * s)} {f(b - (96 + k * 14) * s)} Z" fill="#7AC04A" stroke="#0D0D0F" stroke-width="1.4"></path>' for k in range(4))
                 + V.rays(cx + 12 * s, b - 150 * s, 20, 10, 80 * s, color="#FFF4C2", op=0.4))
    return "".join(o)

def fullers_field(p, w, h, seed):
    """At the end of the conduit of the upper pool, in the highway of the fuller's field: the conduit and the pool below the
    wall, Ahaz with his servants, Isaiah and Shear-jashub his son coming to meet him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FD0E2", "#F3E8C8"),
         f'<rect x="-10" y="{f(h * 0.2)}" width="{f(w * 0.5)}" height="{f(h * 0.4)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    for i in range(7):
        o.append(f'<rect x="{f(i * w * 0.07)}" y="{f(h * 0.16)}" width="{f(w * 0.04)}" height="{f(h * 0.05)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.8"></rect>')
    o.append(ground(w, h, h * 0.6, "#C8B88A", dy=0))
    o.append(f'<path d="M-10 {f(h * 0.64)} L {f(w * 0.36)} {f(h * 0.7)}" stroke="#8A7A6A" stroke-width="{f(h * 0.03)}"></path><path d="M-10 {f(h * 0.64)} L {f(w * 0.36)} {f(h * 0.7)}" stroke="#2C9DB8" stroke-width="{f(h * 0.012)}"></path>'
             f'<ellipse cx="{f(w * 0.42)}" cy="{f(h * 0.74)}" rx="{f(w * 0.1)}" ry="{f(h * 0.05)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    for i in range(4):
        o.append(f'<path d="M{f(w * (0.56 + i * 0.03))} {f(h * 0.66)} l {f(w * 0.02)} {f(h * 0.08)}" stroke="#E8E2D6" stroke-width="5"></path>')
    s = fit(b, max(h * 0.45, b - 200))
    o.append(king_fig(p, w * 0.24, b, s, cloth="#1F3A7A") + man(p, w * 0.16, b, s * 0.94, "#5A4A3A") + man(p, w * 0.09, b, s * 0.94, "#4A5A6A"))
    o.append(K1.prophet_fig(p, w * 0.78, b, s, "#4A3A6A", flip=True) + man(p, w * 0.88, b, s * 0.72, "#C8B88A", flip=True))
    return "".join(o)

def firebrands(w, h, seed):
    """These two tails of smoking firebrands: two charred sticks, nearly burned out, a thin smoke from each (a plate)."""
    o = [grid_bg(w, h)]
    s = min(1.2, h / 200)
    for i, (x, nm) in enumerate(((0.28, "REZIN · SYRIA"), (0.72, "THE SON OF REMALIAH · EPHRAIM"))):
        cx, cy = w * x, h * 0.7
        o.append(f'<path d="M{f(cx - 70 * s)} {f(cy + 8 * s)} L {f(cx + 60 * s)} {f(cy - 8 * s)}" stroke="#3A2A1E" stroke-width="{f(12 * s)}" stroke-linecap="round"></path>'
                 f'<path d="M{f(cx + 40 * s)} {f(cy - 5 * s)} L {f(cx + 62 * s)} {f(cy - 8 * s)}" stroke="#D7261E" stroke-width="{f(10 * s)}" stroke-linecap="round"></path>'
                 f'<circle cx="{f(cx + 64 * s)}" cy="{f(cy - 8 * s)}" r="{f(4 * s)}" fill="#FFD23F"></circle>')
        o.append(smoke(cx + 64 * s, cy - 18 * s, 6, seed + i, r0=6 * s, spread=6 * s, color="#8A8AA0", op=0.5))
        o.append(label(cx, cy + 30 * s, nm, "#FF8A6A", 9))
    return "".join(o)

def immanuel(p, w, h, seed):
    """Behold, a virgin shall conceive, and bear a son, and shall call his name Immanuel; butter and honey shall he eat: a
    young mother at the door of a house at dawn with the child in her arms, a jar of honey and a bowl of butter by her."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#5A6ABA", "#FFE0A0"), V.rays(w * 0.8, h * 0.7, 30, 20, max(w, h), color="#FFF4C2", op=0.3),
         hills(w, h, h * 0.66, seed, color="#8A9A6A", amp=8), ground(w, h, h * 0.76, "#C8B080", dy=0)]
    o.append(f'<rect x="{f(w * 0.14)}" y="{f(h * 0.24)}" width="{f(w * 0.3)}" height="{f(b - h * 0.24)}" fill="#E0D0B0" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<path d="M{f(w * 0.24)} {f(b)} L {f(w * 0.24)} {f(h * 0.5)} Q {f(w * 0.29)} {f(h * 0.42)} {f(w * 0.34)} {f(h * 0.5)} L {f(w * 0.34)} {f(b)} Z" fill="#3A2A1E"></path>')
    s = fit(b, max(h * 0.4, b - 210))
    o.append(mk.person(p, round(w * 0.5), round(b), s, body="#3A1E14", cloth="#2A5A9A", woman=True, hair="#1A1210", sw=3, up=R1.HOLD_BABY, extra=R1.baby(10, -130, 0.8)))
    o.append(f'<path d="M{f(w * 0.62)} {f(b)} C {f(w * 0.6)} {f(b - 30 * s)} {f(w * 0.61)} {f(b - 50 * s)} {f(w * 0.63)} {f(b - 56 * s)} L {f(w * 0.67)} {f(b - 56 * s)} C {f(w * 0.69)} {f(b - 50 * s)} {f(w * 0.7)} {f(b - 30 * s)} {f(w * 0.68)} {f(b)} Z" fill="#C8862E" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.72)} {f(b - 22 * s)} L {f(w * 0.8)} {f(b - 22 * s)} C {f(w * 0.79)} {f(b)} {f(w * 0.73)} {f(b)} {f(w * 0.72)} {f(b - 22 * s)} Z" fill="#E8D8A8" stroke="#0D0D0F" stroke-width="2"></path>'
             + label(w * 0.65, b - 64 * s, "HONEY", "#3A2A1A", 9) + label(w * 0.76, b - 30 * s, "BUTTER", "#3A2A1A", 9))
    return "".join(o)

def bees(w, h, seed):
    """Jehovah will hiss for the fly that is in the uttermost part of the rivers of Egypt, and for the bee that is in the land of
    Assyria: two swarms on the map, settling upon the land between."""
    o = [nations_map(w, h, hi=("EGYPT", "NINEVEH"), arrows=(("EGYPT", "JERUSALEM"), ("NINEVEH", "JERUSALEM")),
                     show=["EGYPT", "NINEVEH", "JERUSALEM", "DAMASCUS", "SAMARIA", "BABYLON"])]
    o.append(E2.swarm(30, w * 0.1, h * 0.7, w * 0.05, h * 0.06, seed, smin=0.3, smax=0.6) + E2.swarm(30, w * 0.7, h * 0.16, w * 0.06, h * 0.06, seed + 1, smin=0.3, smax=0.6)
             + E2.swarm(24, w * 0.24, h * 0.46, w * 0.06, h * 0.08, seed + 2, smin=0.3, smax=0.5))
    return "".join(o)

def cow_sheep(p, w, h, seed):
    """A man shall keep alive a young cow, and two sheep; butter and honey shall every one eat that is left: a lone man in a
    land gone to briers and thorns, his cow and two sheep."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#A8A08A", "#E8D8B0"), hills(w, h, h * 0.56, seed, color="#9A8A6A", amp=8), ground(w, h, h * 0.66, "#A89A6A", dy=0)]
    o.append(thorns(0, w, h * 0.74, seed, n=int(w / 30), s=min(1.0, h / 300)))
    s = min(0.8, h / 330)
    o.append(S1.cow(w * 0.38, b, s * 0.9, color="#B8865A", patch="#E8D8B0", low=True) + E.sheep(w * 0.62, b, s * 0.7) + E.sheep(w * 0.72, b - 6, s * 0.6, flip=True))
    o.append(man(p, w * 0.18, b, fit(b, max(h * 0.45, b - 190)), "#6A5A3A"))
    return "".join(o)

def great_tablet(w, h, seed):
    """Take thee a great tablet, and write upon it with the pen of a man: a great tablet, the name written large, a reed pen
    beside it; the two witnesses' seals at the foot."""
    o = [rect(w, h, "#3A2A2A"), V.rays(w * 0.5, h * 0.5, 20, 10, max(w, h), color="#FFE8B0", op=0.1)]
    tw, th = min(w * 0.7, h * 1.8), min(h * 0.7, w * 0.3)
    x0, y0 = w * 0.5 - tw / 2, h * 0.5 - th / 2
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(tw)}" height="{f(th)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="3"></rect>'
             f'<rect x="{f(x0 + 8)}" y="{f(y0 + 8)}" width="{f(tw - 16)}" height="{f(th - 16)}" fill="none" stroke="#8A6A3A" stroke-width="1.6"></rect>')
    o.append(f'<text x="{f(w * 0.5)}" y="{f(h * 0.5 + th * 0.08)}" text-anchor="middle" font-family="Anton, sans-serif" font-size="{f(min(th * 0.28, tw / 13))}" fill="#3A2A1A" letter-spacing="0.06em">MAHER-SHALAL-HASH-BAZ</text>')
    o.append(f'<path d="M{f(x0 + tw + 20)} {f(y0 + th)} L {f(x0 + tw + 60)} {f(y0 + th * 0.2)}" stroke="#8A6A3A" stroke-width="4" stroke-linecap="round"></path>')
    for i in range(2):
        o.append(f'<circle cx="{f(x0 + tw * (0.3 + i * 0.4))}" cy="{f(y0 + th - 18)}" r="9" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    return "".join(o)

def river_flood(w, h, seed):
    """The waters of the River, strong and many, sweeping onward into Judah, reaching even to the neck; the stretching out of
    its wings filling the breadth of the land: the hills drowning under a flood, a storm shaped like two great wings over it."""
    r = random.Random(seed)
    o = [bg(w, h, "#2A2A4A", "#6A7A9A")]
    for side in (-1, 1):
        o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.22)} C {f(w * 0.5 + side * w * 0.2)} {f(-h * 0.1)} {f(w * 0.5 + side * w * 0.45)} {f(h * 0.0)} {f(w * 0.5 + side * w * 0.56)} {f(h * 0.18)} '
                 f'C {f(w * 0.5 + side * w * 0.4)} {f(h * 0.2)} {f(w * 0.5 + side * w * 0.2)} {f(h * 0.3)} {f(w * 0.5)} {f(h * 0.3)} Z" fill="#14142A" opacity="0.8"></path>')
    o.append(J.city_hill(w * 0.5, h * 0.62, w * 0.18, h * 0.22, seed))
    o.append(hills(w, h, h * 0.6, seed, color="#6A6A5A", amp=14, step=50))
    for k in range(4):
        y = h * (0.62 + k * 0.1)
        d = f"M-10 {f(y)} " + " ".join(f"Q {f(x + 25)} {f(y - 10 + r.uniform(-4, 4))} {f(x + 50)} {f(y)}" for x in range(-10, int(w) + 50, 50))
        o.append(f'<path d="{d} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{["#1F4A6A", "#1A3A5A", "#16304A", "#122840"][k]}" stroke="#8FD0E2" stroke-width="1.6"></path>')
    return "".join(o)

def snare(w, h, seed):
    """For a stone of stumbling and for a rock of offence, for a gin and for a snare: a plate of the stone and the snare."""
    o = [grid_bg(w, h)]
    s = min(1.3, h / 200); b = h * 0.8
    o.append(f'<path d="M{f(w * 0.18)} {f(b)} C {f(w * 0.16)} {f(b - 50 * s)} {f(w * 0.24)} {f(b - 70 * s)} {f(w * 0.32)} {f(b - 66 * s)} C {f(w * 0.4)} {f(b - 60 * s)} {f(w * 0.42)} {f(b - 20 * s)} {f(w * 0.4)} {f(b)} Z" fill="#8A8A9A" stroke="#8FD0E2" stroke-width="2"></path>'
             + label(w * 0.29, b + 18, "A STONE OF STUMBLING · A ROCK OF OFFENCE", CYAN, 9))
    cx = w * 0.72
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(b - 6)}" rx="{f(60 * s)}" ry="{f(12 * s)}" fill="none" stroke="#FFD23F" stroke-width="2"></ellipse>'
             f'<path d="M{f(cx - 60 * s)} {f(b - 6)} C {f(cx - 40 * s)} {f(b - 70 * s)} {f(cx + 40 * s)} {f(b - 70 * s)} {f(cx + 60 * s)} {f(b - 6)}" stroke="#FFD23F" stroke-width="2" fill="none" stroke-dasharray="5 4"></path>'
             f'<path d="M{f(cx)} {f(b - 6)} L {f(cx)} {f(b - 60 * s)} L {f(cx + 30 * s)} {f(b - 80 * s)}" stroke="#B87333" stroke-width="3" fill="none"></path>'
             + label(cx, b + 18, "A GIN · A SNARE", GOLD, 9))
    return "".join(o)

def bound_scroll(w, h, seed):
    """Bind thou up the testimony, seal the law among my disciples: a scroll rolled and bound with a cord, sealed."""
    o = [rect(w, h, "#2A1E2A"), V.rays(w * 0.5, h * 0.5, 20, 10, max(w, h), color="#E8C88A", op=0.1)]
    s = min(1.4, h / 180); cx, cy = w * 0.5, h * 0.56
    o.append(f'<rect x="{f(cx - 120 * s)}" y="{f(cy - 26 * s)}" width="{f(240 * s)}" height="{f(52 * s)}" rx="{f(26 * s)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.6"></rect>'
             f'<ellipse cx="{f(cx - 120 * s)}" cy="{f(cy)}" rx="{f(12 * s)}" ry="{f(26 * s)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
             f'<path d="M{f(cx - 30 * s)} {f(cy - 26 * s)} L {f(cx - 30 * s)} {f(cy + 26 * s)} M{f(cx + 30 * s)} {f(cy - 26 * s)} L {f(cx + 30 * s)} {f(cy + 26 * s)}" stroke="#8A3A1E" stroke-width="{f(4 * s)}"></path>'
             f'<circle cx="{f(cx)}" cy="{f(cy + 26 * s)}" r="{f(12 * s)}" fill="#B5121B" stroke="#0D0D0F" stroke-width="2"></circle>')
    return "".join(o)

def dark_road(p, w, h, seed):
    """They shall look unto the earth, and, behold, distress and darkness: a lone hungry figure on a dark road under a starless
    sky, his face turned upward; far off, the glow of a fire among the tombs."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#05050A", "#2A1A2A"), hills(w, h, h * 0.66, seed, color="#14101A", amp=12), ground(w, h, h * 0.78, "#2A2026", dy=0)]
    o.append(f'<circle cx="{f(w * 0.84)}" cy="{f(h * 0.76)}" r="{f(h * 0.06)}" fill="#8A2A1A" opacity="0.5"></circle>' + E.blaze(w * 0.84, h * 0.8, w * 0.03, h * 0.08, seed, n=4))
    o.append(man(p, w * 0.36, b, fit(b, max(h * 0.45, b - 200)), "#3A3440", up=[(-22, -158), (-30, -190), (-24, -222)]))
    return "".join(o)

def great_light(w, h, seed):
    """The people that walked in darkness have seen a great light: Galilee of the nations, by the way of the sea — the hills
    about the lake in darkness, and the light rising over them."""
    o = [rect(w, h, "#0B0B2A"), V.rays(w * 0.5, h * 0.48, 40, 20, max(w, h) * 1.2, color="#FFE680", op=0.35),
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.48)}" r="{f(h * 0.14)}" fill="#FFF4C2"></circle>',
         hills(w, h, h * 0.52, seed, color="#2A2448", amp=14, step=60),
         f'<path d="M-10 {f(h * 0.66)} C {f(w * 0.3)} {f(h * 0.6)} {f(w * 0.7)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.66)} L {f(w + 10)} {f(h * 0.8)} C {f(w * 0.7)} {f(h * 0.86)} {f(w * 0.3)} {f(h * 0.86)} -10 {f(h * 0.8)} Z" fill="#3A5A8A" stroke="#FFE680" stroke-width="1.6"></path>',
         ground(w, h, h * 0.84, "#1A1630", dy=0)]
    o.append(f'<path d="M{f(w * 0.46)} {f(h * 0.66)} L {f(w * 0.54)} {f(h * 0.66)} L {f(w * 0.58)} {f(h * 0.8)} L {f(w * 0.42)} {f(h * 0.8)} Z" fill="#FFE680" opacity="0.5"></path>')
    o.append(label(w * 0.5, h * 0.95, "GALILEE OF THE NATIONS", "#FFE680", 10))
    return "".join(o)

def broken_yoke(w, h, seed):
    """The yoke of his burden, the staff of his shoulder, the rod of his oppressor broken; the armor of the armed man for
    burning, for fuel of fire."""
    o = [bg(w, h, "#3A1A1A", "#C86A2A"), ground(w, h, h * 0.76, "#6A4A3A", dy=0)]
    s = min(1.2, h / 220); b = h * 0.86
    o.append(f'<path d="M{f(w * 0.08)} {f(b - 30 * s)} C {f(w * 0.14)} {f(b - 60 * s)} {f(w * 0.2)} {f(b - 60 * s)} {f(w * 0.24)} {f(b - 40 * s)}" stroke="#8A5A2A" stroke-width="{f(12 * s)}" fill="none" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.28)} {f(b - 34 * s)} C {f(w * 0.32)} {f(b - 54 * s)} {f(w * 0.38)} {f(b - 56 * s)} {f(w * 0.42)} {f(b - 30 * s)}" stroke="#8A5A2A" stroke-width="{f(12 * s)}" fill="none" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.24)} {f(b - 44 * s)} l {f(8 * s)} {f(6 * s)} l {f(-6 * s)} {f(4 * s)} l {f(10 * s)} {f(4 * s)}" stroke="#FFD23F" stroke-width="2" fill="none"></path>')
    o.append(f'<path d="M{f(w * 0.12)} {f(b)} L {f(w * 0.26)} {f(b - 6 * s)}" stroke="#5A3A22" stroke-width="{f(7 * s)}"></path><path d="M{f(w * 0.3)} {f(b - 4 * s)} L {f(w * 0.44)} {f(b - 2 * s)}" stroke="#5A3A22" stroke-width="{f(7 * s)}"></path>')
    o.append(E.blaze(w * 0.72, b, w * 0.24, h * 0.5, seed, n=8))
    o.append(S2.helmet_alone(w * 0.66, b - 6, 0.5 * s) + f'<path d="M{f(w * 0.62)} {f(b)} L {f(w * 0.86)} {f(b - 40 * s)}" stroke="#5A5A6A" stroke-width="{f(5 * s)}"></path>')
    return "".join(o)

def davids_throne(w, h, seed):
    """Upon the throne of David, and upon his kingdom, to establish it for ever: the throne of David, empty, in rising light,
    lamps burning before it (no one drawn)."""
    from genesis.art4 import clay_lamp
    o = [rect(w, h, "#1A1438"), V.rays(w * 0.5, h * 0.3, 40, 20, max(w, h) * 1.2, color="#FFD23F", op=0.25)]
    s = min(1.6, h / 200)
    for k in range(3):
        dw = w * (0.12 + k * 0.05)
        o.append(f'<rect x="{f(w * 0.5 - dw)}" y="{f(h * (0.78 + k * 0.06))}" width="{f(dw * 2)}" height="{f(h * 0.06)}" fill="#C8A040" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(S3.throne(w * 0.5, h * 0.78, s * 0.7) + S2.crown(w * 0.5, h * 0.24, 0.6 * s))
    o.append(clay_lamp(w * 0.28, h * 0.84, 0.6 * s) + clay_lamp(w * 0.72, h * 0.84, 0.6 * s))
    o.append(label(w * 0.5, h * 0.98, "THE THRONE OF DAVID", "#FFD23F", 10))
    return "".join(o)

def bricks_cedars(w, h, seed):
    """The bricks are fallen, but we will build with hewn stone; the sycomores are cut down, but we will put cedars in their
    place: fallen mud-brick on the left, new hewn stones and cedar beams stacked on the right."""
    r = random.Random(seed)
    o = [bg(w, h, "#8A7A6A", "#E8D0A8"), ground(w, h, h * 0.8, "#A88A5A", dy=0)]
    s = min(1.1, h / 220); b = h * 0.86
    for _ in range(18):
        x = r.uniform(w * 0.04, w * 0.4); y = b - r.uniform(0, 30 * s)
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(24 * s)}" height="{f(12 * s)}" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.4" transform="rotate({r.randint(-30, 30)} {f(x)} {f(y)})"></rect>')
    for k in range(3):
        for j in range(4 - k):
            o.append(f'<rect x="{f(w * 0.5 + j * 46 * s + k * 23 * s)}" y="{f(b - (k + 1) * 26 * s)}" width="{f(44 * s)}" height="{f(26 * s)}" fill="#D8CCB0" stroke="#0D0D0F" stroke-width="1.8"></rect>')
    for k in range(4):
        o.append(f'<rect x="{f(w * 0.76)}" y="{f(b - (k + 1) * 14 * s)}" width="{f(w * 0.2)}" height="{f(13 * s)}" rx="{f(6 * s)}" fill="#B5793A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)

def forest_fire(w, h, seed):
    """Wickedness burneth as the fire; it devoureth the briers and thorns; it kindleth in the thickets of the forest, and
    they roll upward in a column of smoke."""
    o = [bg(w, h, "#2A1A1A", "#8A3A1A")]
    o.append(smoke(w * 0.5, h * 0.6, 10, seed, r0=h * 0.06, spread=w * 0.08, color="#2A2026", op=0.8, rise=0.8))
    for i in range(12):
        x = w * (0.02 + i * 0.085); y = h * 0.86
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - h * 0.3)}" stroke="#1A1010" stroke-width="5"></path>'
                 f'<path d="M{f(x - 20)} {f(y - h * 0.16)} L {f(x)} {f(y - h * 0.36)} L {f(x + 20)} {f(y - h * 0.16)} Z" fill="#1A1A14" stroke="#0D0D0F" stroke-width="1.4"></path>')
    for i in range(6):
        o.append(E.blaze(w * (0.08 + i * 0.17), h * 0.92, w * 0.15, h * 0.42, seed + i, n=6))
    o.append(ground(w, h, h * 0.9, "#2A1A14", dy=0))
    return "".join(o)
