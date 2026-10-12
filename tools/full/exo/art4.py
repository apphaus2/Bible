"""New drawings for Exodus chapter 4 (Exodus 13–15): the sign upon the hand, the firstling of an ass, the way of the
wilderness, the camp by the sea, the pillar between the camps, the morning watch, the sea returning, the nations
trembling, the mountain of inheritance, Marah and Elim."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4, exodus5 as V, judges1 as G1, numbers1 as N, egypt as EG
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art10 as T
from genesis.art2 import fit, ground, hills, city, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg, node, route
from exo import art as A
def f(v): return f"{v:.1f}"

def hand_sign(w, h, seed, cx=0.5):
    """A sign upon thy hand, and a memorial between thine eyes: an open hand with a cord bound about the wrist."""
    s = min(1.2, h / 300); x = w * cx; y = h * 0.5
    return (V.rays(x, y, 24, 60, max(w, h), color="#FFF4C2", op=0.15) + E.hand(x, y, s, uid=f"hs{seed}")
            + f'<path d="M{f(x - 40 * s)} {f(y + 92 * s)} C {f(x)} {f(y + 104 * s)} {f(x + 40 * s)} {f(y + 92 * s)} {f(x + 50 * s)} {f(y + 80 * s)}" fill="none" stroke="#D7261E" stroke-width="7"></path>')

def ass_lamb(w, h, seed):
    """Every firstling of an ass thou shalt redeem with a lamb: the young ass and the lamb side by side."""
    b = h * 0.86
    return sun(w * 0.86, h * 0.2, 14, op=0.25) + ground(w, h, b, "#9CBB5E", dy=0) + N.ass(w * 0.32, b, min(0.9, h / 300)) + E3.lamb(w * 0.62, b, min(1.1, h / 200))

def armed(p, w, h, seed):
    """The children of Israel went up armed out of the land of Egypt: ranks of men with spears, the wilderness ahead."""
    b = h * 0.9
    return (sun(w * 0.86, h * 0.18, 14, op=0.25) + hills(w, h, h * 0.5, seed, color="#C8682E", amp=14) + ground(w, h, h * 0.5, "#C8A06A", dy=0)
            + E4.warriors(p, 26, -10, w + 10, h * 0.56, b, seed, 0.2, 0.42, flip=True, body=SKIN, cloth=tuple(A.HEBREW[:4])))

def sea_map(w, h, legs=(), cur=None):
    """The camp by the sea as a technical map: Succoth, Etham in the edge of the wilderness, Migdol, Pi-hahiroth and
    Baal-zephon by the sea; the way of the land of the Philistines along the coast."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 {f(h * 0.12)} C {f(w * 0.3)} {f(h * 0.06)} {f(w * 0.6)} {f(h * 0.1)} {f(w + 10)} {f(h * 0.02)} L {f(w + 10)} -10 L -10 -10 Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             + label(w * 0.2, h * 0.06, "THE GREAT SEA", "#8FD0E2", 9))
    o.append(f'<path d="M{f(w * 0.52)} {f(h * 0.5)} C {f(w * 0.56)} {f(h * 0.66)} {f(w * 0.62)} {f(h * 0.82)} {f(w * 0.7)} {f(h + 10)} L {f(w * 0.9)} {f(h + 10)} C {f(w * 0.78)} {f(h * 0.8)} {f(w * 0.66)} {f(h * 0.62)} {f(w * 0.6)} {f(h * 0.46)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             + label(w * 0.8, h * 0.96, "THE RED SEA", "#8FD0E2", 9))
    P = {"SUCCOTH": (0.2, 0.42), "ETHAM": (0.4, 0.34), "MIGDOL": (0.44, 0.62), "PI-HAHIROTH": (0.5, 0.74), "BAAL-ZEPHON": (0.66, 0.4), "PHILISTIA": (0.74, 0.16)}
    o.append(f'<path d="M{f(w * 0.2)} {f(h * 0.42)} C {f(w * 0.4)} {f(h * 0.2)} {f(w * 0.6)} {f(h * 0.16)} {f(w * 0.74)} {f(h * 0.16)}" fill="none" stroke="#D7261E" stroke-width="2" stroke-dasharray="4 6"></path>'
             + label(w * 0.48, h * 0.18, "THE WAY OF THE LAND OF THE PHILISTINES", "#D7261E", 8))
    pts = [(P[n][0] * w, P[n][1] * h) for n in legs]
    if len(pts) > 1: o.append(route(pts, color="#FFD23F", sw=3))
    for n, (x, y) in P.items():
        o.append(node(w * x, h * y, n, "#D7261E" if n == cur else ("#FFD23F" if n in legs else "#8FD0E2"), r=5, dy=-12, size=10))
    return "".join(o)

def cloud_between(p, w, h, seed):
    """The pillar of cloud came between the camp of Egypt and the camp of Israel: dark on the chariots, light on the tents."""
    b = h * 0.86; mid = w * 0.5
    o = [f'<rect x="-10" y="-10" width="{f(mid + 10)}" height="{f(h + 20)}" fill="#0B0B1A"></rect>', f'<rect x="{f(mid)}" y="-10" width="{f(w - mid + 10)}" height="{f(h + 20)}" fill="#2A3A6A"></rect>',
         mk.stars(30, w, h * 0.4, seed).replace("<g", f'<g transform="translate({f(mid)} 0)"', 1), ground(w, h, b, "#2A2A3A", dy=0)]
    o += [E3.chariot(w * x, b, 0.42, color="#1A1210", driver="#2A1A16") for x in (0.08, 0.22, 0.34)]
    o += [A.black_tent(w * x, b, w * 0.12, h * 0.16) for x in (0.66, 0.8, 0.94)]
    o.append(f'<ellipse cx="{f(w * 0.8)}" cy="{f(b - 20)}" rx="{f(w * 0.24)}" ry="{f(h * 0.3)}" fill="#FFF4C2" opacity="0.18"></ellipse>')
    o.append(E3.pillar_cloud(mid, b, -20, w * 0.09, seed))
    return "".join(o)

def morning_watch(w, h, seed):
    """In the morning watch Jehovah looked forth through the pillar of fire and of cloud: the chariots in the sea-bed, fire above."""
    o = [E3.sea_corridor(w, h, (w * 0.5, h * 0.3), w * 0.16, w * 0.84, seed, uid=f"mw{seed}")]
    o.append(E3.pillar_fire(w * 0.5, h * 0.3, -20, w * 0.08, seed))
    o += [E3.chariot(w * x, h * (0.66 + 0.1 * i), 0.3 + 0.08 * i, flip=x > 0.5) for i, x in enumerate((0.42, 0.58, 0.46))]
    return "".join(o)

def dry_walk(p, w, h, seed):
    """The children of Israel walked upon dry land in the midst of the sea: a file of people between the walls of water."""
    o = [E3.sea_corridor(w, h, (w * 0.5, h * 0.24), w * 0.18, w * 0.82, seed, uid=f"dw{seed}")]
    r = random.Random(seed)
    for i in range(16):
        y = h * (0.34 + 0.6 * i / 15); s = 0.06 + 0.32 * i / 15; x = w * 0.5 + r.uniform(-1, 1) * (y - h * 0.24) * 0.5
        o.append((man if i % 2 else woman)(p, x, y, s, r.choice(A.HEBREW + ["#C2456A", "#5A6E8A"]), flip=r.random() < 0.5))
    return "".join(o)

def sunk(w, h, seed):
    """They went down into the depths like a stone: a wheel and a chariot sinking through blue water, light far above."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0B2E4A"></rect>', V.rays(w * 0.5, -40, 20, 20, h * 1.2, color="#8FD0E2", op=0.12)]
    o += [f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(0, h))}" r="{f(r.uniform(2, 6))}" fill="none" stroke="#8FD0E2" stroke-width="1.4" opacity="0.7"></circle>' for _ in range(30)]
    o.append(f'<g transform="rotate(-20 {f(w * 0.36)} {f(h * 0.6)})">{E3.chariot(w * 0.36, h * 0.7, min(0.8, h / 300), color="#1A1A2A", driver="#2A2A3A")}</g>')
    o.append(f'<g transform="translate({f(w * 0.76)} {f(h * 0.4)}) rotate(30)"><circle r="{f(h * 0.12)}" fill="none" stroke="#3A2214" stroke-width="6"></circle>'
             + "".join(f'<path d="M0 0 L {f(h * 0.12 * math.cos(a))} {f(h * 0.12 * math.sin(a))}" stroke="#3A2214" stroke-width="4"></path>' for a in [i * math.pi / 3 for i in range(6)]) + '</g>')
    return "".join(o)

def nations(w, h, seed):
    """The peoples have heard, they tremble: Philistia, Edom, Moab and Canaan as a technical map, red pulses on each."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.16)} -10 C {f(w * 0.14)} {f(h * 0.4)} {f(w * 0.1)} {f(h * 0.7)} {f(w * 0.04)} {f(h + 10)} L -10 {f(h + 10)} L -10 -10 Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<ellipse cx="{f(w * 0.76)}" cy="{f(h * 0.5)}" rx="{f(w * 0.025)}" ry="{f(h * 0.16)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>')
    for nm, x, y in (("PHILISTIA", 0.52, 0.68), ("CANAAN", 0.64, 0.26), ("MOAB", 0.9, 0.44), ("EDOM", 0.8, 0.84)):
        o.append("".join(f'<circle cx="{f(w * x)}" cy="{f(h * y)}" r="{rr}" fill="none" stroke="#D7261E" stroke-width="2" opacity="{op}"></circle>' for rr, op in ((14, 0.8), (26, 0.5), (40, 0.25)))
                 + node(w * x, h * y, nm, "#FFD23F", r=5, dy=-14, size=11))
    return "".join(o)

def inheritance(w, h, seed):
    """Thou wilt plant them in the mountain of thine inheritance: a green mountain under rays of light, the people below."""
    b = h * 0.9
    return (V.rays(w * 0.6, h * 0.1, 30, 20, max(w, h) * 1.2, color="#FFF4C2", op=0.3) + sun(w * 0.6, h * 0.1, 18, color="#FFF4C2", op=0.3)
            + f'<path d="M-10 {f(b)} L {f(w * 0.3)} {f(h * 0.5)} L {f(w * 0.46)} {f(h * 0.36)} L {f(w * 0.6)} {f(h * 0.22)} L {f(w * 0.74)} {f(h * 0.38)} L {f(w * 0.9)} {f(h * 0.5)} L {f(w + 10)} {f(b)} Z" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="2.4"></path>'
            + f'<path d="M{f(w * 0.6)} {f(h * 0.22)} L {f(w * 0.74)} {f(h * 0.38)} L {f(w * 0.9)} {f(h * 0.5)} L {f(w * 0.7)} {f(b)} Z" fill="#9CCB5E" opacity="0.6"></path>'
            + ground(w, h, b, "#9CCB5E", dy=0))

def wilderness(p, w, h, seed, cast=()):
    """The wilderness of Shur: bare sand and rock under a white sun, the long file of the people."""
    b = h * 0.86
    o = [sun(w * 0.8, h * 0.2, 18, color="#FFF4C2", op=0.4), hills(w, h, h * 0.56, seed, color="#C8682E", amp=12), ground(w, h, h * 0.56, "#E8C88A", dy=0)]
    o.append(Z.caravan(p, w * 0.06, w * 0.94, h * 0.7, 0.24, seed, flip=True))
    o += [T.figure(p, c[0], w * c[1], b, fit(b, h * c[2]), flip=c[3] if len(c) > 3 else False, pose=c[4] if len(c) > 4 else None) for c in cast]
    return "".join(o)

def marah(p, w, h, seed, sweet=False):
    """The waters of Marah: a brackish pool; Moses casts the tree into it and the waters are made sweet."""
    b = h * 0.86; py = h * 0.74
    o = [sun(w * 0.84, h * 0.2, 16, color="#FFF4C2", op=0.35), hills(w, h, h * 0.5, seed, color="#C8682E", amp=10), ground(w, h, h * 0.5, "#E8C88A", dy=0),
         f'<ellipse cx="{f(w * 0.56)}" cy="{f(py)}" rx="{f(w * 0.3)}" ry="{f(h * 0.1)}" fill="{"#2C9DB8" if sweet else "#6A7A4A"}" stroke="#0D0D0F" stroke-width="2.4"></ellipse>']
    if sweet:
        o.append(f'<g transform="translate({f(w * 0.56)} {f(py - 4)}) rotate(-12)"><path d="M-60 0 L 60 0" stroke="#5A3A22" stroke-width="7" stroke-linecap="round"></path>'
                 '<path d="M-20 0 L -34 -18 M10 0 L 22 -20 M36 0 L 48 -14" stroke="#5A3A22" stroke-width="4"></path></g>'
                 + "".join(f'<path d="M{f(w * 0.56 + d)} {f(py)} m -20 0 a 20 6 0 1 0 40 0 a 20 6 0 1 0 -40 0" fill="none" stroke="#E8F6FA" stroke-width="2"></path>' for d in (-80, 70)))
    o.append(A.moses(p, w * 0.2, b, fit(b, h * 0.36), up=[(-22, -158), (4, -150), (30, -140)] if sweet else T.POSES["raise"]))
    return "".join(o)

def elim(p, w, h, seed):
    """Elim, where were twelve springs of water, and threescore and ten palm-trees: the camp pitched by the waters."""
    r = random.Random(seed); b = h * 0.9
    o = [sun(w * 0.86, h * 0.16, 16, op=0.3), ground(w, h, h * 0.52, "#E8C88A", dy=0)]
    for i in range(12):
        x = w * (0.06 + (i % 6) * 0.17) + (i // 6) * w * 0.08; y = h * (0.66 + (i // 6) * 0.16)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.05)}" ry="{f(h * 0.03)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    palms = sorted((r.uniform(h * 0.5, h * 0.64), r.uniform(0, w)) for _ in range(70))
    for y, x in palms:
        o.append(G1.palm(x, y, 0.18 + 0.4 * (y - h * 0.5) / (h * 0.14)))
    o += [A.black_tent(w * x, b, w * 0.1, h * 0.12) for x in (0.2, 0.5, 0.8)]
    return "".join(o)

def wheels_off(p, w, h, seed):
    """He took off their chariot wheels, and they drove them heavily: a chariot down on its axle in the sea-bed, a wheel rolled
    away, the horse rearing, the walls of water standing over them."""
    o = [E3.sea_corridor(w, h, (w * 0.5, h * 0.2), w * 0.1, w * 0.9, seed, uid=f"wo{seed}")]
    b = h * 0.9; s = min(1.0, h / 300)
    o.append(f'<g transform="rotate(14 {f(w * 0.42)} {f(b)})">{E3.chariot(w * 0.42, b, s, color="#3A2214", driver="#5A2A16")}</g>')
    wx, wy, rr = w * 0.78, b - 30 * s, 34 * s
    o.append(f'<g transform="translate({f(wx)} {f(wy)}) rotate(20)"><circle r="{f(rr)}" fill="none" stroke="#0D0D0F" stroke-width="9"></circle><circle r="{f(rr)}" fill="none" stroke="#E8B830" stroke-width="5"></circle>'
             + "".join(f'<path d="M0 0 L {f(rr * math.cos(a))} {f(rr * math.sin(a))}" stroke="#E8B830" stroke-width="4"></path>' for a in [i * math.pi / 3 for i in range(6)]) + '</g>')
    o.append(E3.chariot(w * 0.62, h * 0.56, 0.36 * s, flip=True))
    return "".join(o)
