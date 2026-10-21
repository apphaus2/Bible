"""Drawings for Ezekiel 20–21: the way out of Egypt into the wilderness (exo.art.exodus_map), the tables of the statutes and
the sabbaths, the camp in the wilderness, passing under the rod, the forest of the South set on fire, the sword sharpened
and furbished, the king of Babylon at the parting of the way (a map with his divination: the arrows, the teraphim, the
liver), the mitre and the crown taken off, and Rabbah of the children of Ammon."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art6 import *
from ezk.art6 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2, JJ2
from exo.art import exodus_map
from deu.art3 import tables

def wilderness_camp(w, h, seed):
    """The wilderness: the tents of the camp under the cloud, the mountains of the desert round about."""
    o = [bg(f"wc{seed}", w, h, [(0, "#C8803A"), (1, "#F3D8A0")]), hills(w, h, h * 0.52, seed, "#A86A4A", amp=14, step=70), ground(w, h, h * 0.62, "#D8B07A", dy=0)]
    o.append(N.camp(14, w * 0.05, w * 0.95, h * 0.66, h * 0.96, seed))
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.3)}" rx="{f(w * 0.12)}" ry="{f(h * 0.08)}" fill="#F3EFE6" opacity="0.8"></ellipse>')
    return "".join(o)

def under_rod(w, h, seed):
    """I will cause you to pass under the rod: a shepherd's rod held across a narrow gateway, the flock passing under it
    one by one into the fold."""
    o = [bg(f"ur{seed}", w, h, [(0, "#6A8AB0"), (1, "#E8D8B0")]), ground(w, h, h * 0.72, "#A8946A", dy=0)]
    o.append(f'<rect x="{f(w * 0.46)}" y="{f(h * 0.4)}" width="{f(w * 0.04)}" height="{f(h * 0.4)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.58)}" y="{f(h * 0.4)}" width="{f(w * 0.04)}" height="{f(h * 0.4)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(w * 0.4)} {f(h * 0.5)} L {f(w * 0.68)} {f(h * 0.54)} q 10 0 8 -12" stroke="#0D0D0F" stroke-width="7" fill="none" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.4)} {f(h * 0.5)} L {f(w * 0.68)} {f(h * 0.54)} q 10 0 8 -12" stroke="#8A5A30" stroke-width="4" fill="none" stroke-linecap="round"></path>')
    k = min(1.0, h / 300)
    for i in range(5):
        o.append(E.sheep(w * (0.12 + i * 0.07) + (w * 0.42 if i == 4 else 0), h * 0.86, 0.7 * k, wool="#F3EFE6"))
    for i in range(3):
        o.append(E.sheep(w * (0.72 + i * 0.09), h * 0.84 - i * 4, 0.6 * k))
    return "".join(o)

def forest_fire(w, h, seed):
    """I will kindle a fire in thee, and it shall devour every green tree in thee, and every dry tree: the forest of the
    South burning from the south to the north."""
    r = random.Random(seed)
    o = [bg(f"ff{seed}", w, h, [(0, "#1A0A0A"), (0.6, "#8A2A1A"), (1, "#E8803A")]), ground(w, h, h * 0.86, "#2A1A10", dy=0)]
    for i in range(10):
        x = w * (0.04 + i * 0.1) + r.uniform(-10, 10)
        o.append(tree(x, h * 0.88, h * 0.0034 * r.uniform(0.8, 1.2), color="#2E5A2A" if i % 3 else "#6A5A3A", kind="round" if i % 2 else "tall", seed=seed + i))
    for i in range(6):
        o.append(f'<g opacity="0.92">' + E.blaze(w * (0.08 + i * 0.17), h * 0.9, w * 0.14, h * 0.4, seed + 10 + i, n=6) + '</g>')
    o.append(smoke(w * 0.3, h * 0.3, 6, seed, color="#2A1A1A", op=0.6, k=h / 300) + smoke(w * 0.7, h * 0.3, 6, seed + 1, color="#2A1A1A", op=0.6, k=h / 300))
    return "".join(o)

def sword(w, h, seed, sheath=False):
    """A sword, a sword, sharpened and furbished, that it may be as lightning: one great blade glittering against the dark,
    speed lines and lightning about it (sheath=True: returned into its sheath)."""
    o = [bg(f"sd{seed}{sheath}", w, h, [(0, "#0B0B1A"), (1, "#3A1A2A")])]
    cx, cy = w * 0.5, h * 0.55; L = min(w * 0.9, h * 2.2)
    if not sheath:
        o.append(mk.speed(cx, cy, 40, L * 0.2, L * 0.9, seed, color="#C8D8F0", op=0.35))
        o.append(bolts(w, h, seed, 2, 0.0, 0.5))
    a = -0.18
    ca, sa = math.cos(a), math.sin(a)
    def pt(u, v_): return (cx + u * ca - v_ * sa, cy + u * sa + v_ * ca)
    blade = [pt(-L * 0.3, -L * 0.022), pt(L * 0.4, -L * 0.018), pt(L * 0.46, 0), pt(L * 0.4, L * 0.018), pt(-L * 0.3, L * 0.022)]
    if sheath:
        sh = [pt(-L * 0.3, -L * 0.034), pt(L * 0.42, -L * 0.03), pt(L * 0.46, 0), pt(L * 0.42, L * 0.03), pt(-L * 0.3, L * 0.034)]
        o.append(P("M" + " L ".join(f"{f(x)} {f(y)}" for x, y in sh) + " Z", "#5A3A2A", 2.6))
    else:
        o.append(P("M" + " L ".join(f"{f(x)} {f(y)}" for x, y in blade) + " Z", "#D8E0F0", 2.6))
        x0, y0 = pt(-L * 0.28, 0); x1, y1 = pt(L * 0.42, 0)
        o.append(f'<path d="M{f(x0)} {f(y0)} L {f(x1)} {f(y1)}" stroke="#8A9AB8" stroke-width="2"></path>')
        o.append(glow(f"sg{seed}", *pt(L * 0.3, 0), L * 0.08, L * 0.05, "#FFFFFF", 0.9, core="#FFFFFF"))
    g = [pt(-L * 0.31, -L * 0.07), pt(-L * 0.29, -L * 0.07), pt(-L * 0.29, L * 0.07), pt(-L * 0.31, L * 0.07)]
    o.append(P("M" + " L ".join(f"{f(x)} {f(y)}" for x, y in g) + " Z", "#E8B830", 2.2))
    hd = [pt(-L * 0.42, -L * 0.014), pt(-L * 0.31, -L * 0.014), pt(-L * 0.31, L * 0.014), pt(-L * 0.42, L * 0.014)]
    o.append(P("M" + " L ".join(f"{f(x)} {f(y)}" for x, y in hd) + " Z", "#6A3A1A", 2.2))
    return "".join(o)

def parting(w, h):
    """Appoint thee two ways: the king of Babylon standing at the parting of the way, at the head of the two ways — to
    Rabbah of the children of Ammon, and to Judah in Jerusalem the fortified — and his divination: the arrows shaken, the
    teraphim, the liver."""
    o = [grid_bg(w, h)]
    B, X = (w * 0.9, h * 0.3), (w * 0.62, h * 0.42)
    R, J0 = (w * 0.34, h * 0.78), (w * 0.14, h * 0.4)
    o.append(route([B, X], color="#FFD23F", sw=3, arrow=False) + route([X, (w * 0.4, h * 0.42), J0], color="#D7261E", sw=3) + route([X, (w * 0.5, h * 0.66), R], color="#8FD0E2", sw=2.4, dash="5 6"))
    o.append(node(*B, "FROM BABYLON", "#FFD23F", r=5, dy=-12, size=9) + node(*J0, "JERUSALEM", "#D7261E", r=7, dy=-14, size=10) + node(*R, "RABBAH", "#8FD0E2", r=6, dy=-12, size=10))
    o.append(f'<circle cx="{f(X[0])}" cy="{f(X[1])}" r="12" fill="none" stroke="#FFD23F" stroke-width="2.4"></circle>' + label(X[0] + 16, X[1] + 26, "THE PARTING OF THE WAY", "#FFD23F", 9, "start"))
    ix, iy = w * 0.72, h * 0.78
    for i in range(3):
        o.append(f'<path d="M{f(ix + i * 10)} {f(iy)} L {f(ix + 6 + i * 10)} {f(iy - 40)}" stroke="#E8D8B0" stroke-width="2.4"></path><path d="M{f(ix + 6 + i * 10)} {f(iy - 40)} l -4 6 l 7 0 Z" fill="#C8C8D0"></path>')
    o.append(label(ix + 14, iy + 16, "ARROWS", "#8FD0E2", 8))
    o.append(idol(w * 0.84, iy, 0.6, color="#C8A040") + label(w * 0.84, iy + 16, "TERAPHIM", "#8FD0E2", 8))
    o.append(f'<path d="M{f(w * 0.93)} {f(iy - 8)} c -10 -16 20 -24 24 -8 c 2 10 -16 16 -24 8 Z" fill="#8A2A2A" stroke="#0D0D0F" stroke-width="1.4"></path>' + label(w * 0.95, iy + 16, "LIVER", "#8FD0E2", 8))
    return "".join(o)

def mitre_crown(w, h, seed):
    """Remove the mitre, and take off the crown: the mitre and the crown laid down on the steps of an empty throne; overturn,
    overturn, overturn it."""
    o = [bg(f"mc{seed}", w, h, [(0, "#1A1A2A"), (1, "#5A3A4A")])]
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(h * 0.36)}" width="{f(w * 0.4)}" height="{f(h * 0.5)}" fill="#3A2A3A" stroke="{INK}" stroke-width="2.4"></rect>')
    k = min(1.5, h / 260)
    o.append(S3.throne(w * 0.5, h * 0.86, k * 0.8) if hasattr(S3, "throne") else "")
    o.append(f'<rect x="-10" y="{f(h * 0.86)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#2A1A2A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<g transform="translate({f(w * 0.24)} {f(h * 0.93)}) rotate(160) scale({f(k)})"><path d="M-24 0 L -24 -18 L -12 -8 L 0 -24 L 12 -8 L 24 -18 L 24 0 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path></g>')
    o.append(f'<g transform="translate({f(w * 0.78)} {f(h * 0.92)}) rotate(-12) scale({f(k)})"><path d="M-20 0 C -22 -20 -12 -32 0 -34 C 12 -32 22 -20 20 0 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-20 -8 L 20 -8" stroke="#1F5FAD" stroke-width="4"></path><rect x="-10" y="-12" width="20" height="6" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></rect></g>')
    return "".join(o)

def rabbah(w, h, seed, fire=True):
    """Rabbah of the children of Ammon on its hill (fire=True: burning, smoke over it; no one drawn)."""
    o = [bg(f"rb{seed}", w, h, [(0, "#2A0A0A" if fire else "#6A9AC8"), (1, "#C84A1A" if fire else "#F3E0B0")]), hills(w, h, h * 0.6, seed, "#6A4A3A", amp=10, step=80)]
    o.append(J.city_hill(w * 0.5, h * 0.92, w * 0.42, h * 0.4, seed))
    if fire:
        for i in range(4): o.append(f'<g opacity="0.9">' + E.blaze(w * (0.32 + i * 0.12), h * 0.7, w * 0.1, h * 0.2, seed + i, n=5) + '</g>')
        o.append(smoke(w * 0.46, h * 0.5, 8, seed, color="#2A1A1A", op=0.6, k=h / 300))
    o.append(ground(w, h, h * 0.92, "#2A1A10" if fire else "#9A7A5A", dy=0))
    return "".join(o)
