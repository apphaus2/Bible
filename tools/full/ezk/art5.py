"""Drawings for Ezekiel 15–16: the vine-wood cast into the fire; Jerusalem the foundling told only in words over things and
places — an empty field at dawn, the garments and ornaments laid out, the high places decked with colours, the lofty place at
the head of every way, the lovers as a map, the city burned (no one drawn), the three sisters Samaria, Jerusalem and Sodom as
a map, and the everlasting covenant as dawn over the city."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art4 import *
from ezk.art4 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2, JJ2

def vine_branch(x0, y0, x1, y1, seed, burnt=0.0, sw=10):
    """A gnarled vine branch from (x0, y0) to (x1, y1); burnt: the share of each end charred."""
    r = random.Random(seed)
    pts = [(x0 + (x1 - x0) * t + r.uniform(-8, 8), y0 + (y1 - y0) * t + r.uniform(-10, 10)) for t in [i / 8 for i in range(9)]]
    d = "M" + " L ".join(f"{f(a)} {f(b)}" for a, b in pts)
    o = f'<path d="{d}" stroke="#0D0D0F" stroke-width="{sw + 4}" fill="none" stroke-linecap="round" stroke-linejoin="round"></path><path d="{d}" stroke="#6A4A2A" stroke-width="{sw}" fill="none" stroke-linecap="round" stroke-linejoin="round"></path>'
    if burnt:
        n = max(1, int(8 * burnt))
        for seg_ in (pts[:n + 1], pts[-n - 1:]):
            dd = "M" + " L ".join(f"{f(a)} {f(b)}" for a, b in seg_)
            o += f'<path d="{dd}" stroke="#1A1210" stroke-width="{sw}" fill="none" stroke-linecap="round"></path>'
    return o

def vine_fire(w, h, seed):
    """The vine-tree among the trees of the forest given to the fire for fuel: both the ends devoured, the midst burned."""
    o = [bg(f"vf{seed}", w, h, [(0, "#1A0A0A"), (1, "#5A2A1A")]), ground(w, h, h * 0.86, "#2A1A1A", dy=0)]
    o.append(E.blaze(w * 0.5, h * 0.9, w * 0.5, h * 0.4, seed, n=9))
    o.append(vine_branch(w * 0.18, h * 0.62, w * 0.82, h * 0.7, seed, burnt=0.3))
    o.append(vine_branch(w * 0.3, h * 0.8, w * 0.7, h * 0.56, seed + 1, burnt=0.25, sw=7))
    o.append(f'<g opacity="0.7">' + E.blaze(w * 0.5, h * 0.82, w * 0.3, h * 0.22, seed + 2, n=6) + '</g>')
    return "".join(o)

def open_field(w, h, seed):
    """Cast out in the open field in the day that thou wast born — an empty field at dawn (no one is drawn)."""
    o = [bg(f"of{seed}", w, h, [(0, "#3A3A6A"), (0.7, "#E8A080"), (1, "#F3D8A0")]), sun(w * 0.8, h * 0.64, max(10, h * 0.05), color="#FFD23F", op=0.3)]
    o.append(hills(w, h, h * 0.62, seed, "#7A6A5A", amp=8, step=90) + ground(w, h, h * 0.7, "#A8946A", dy=0))
    r = random.Random(seed)
    o.append("".join(f'<path d="M{f(x)} {f(h * 0.7 + (x % 40))} l {f(r.uniform(-4, 4))} -10" stroke="#6A7A3A" stroke-width="1.6"></path>' for x in range(0, int(w), 9)))
    return "".join(o)

def ornaments(w, h, seed):
    """I clothed thee with broidered work and decked thee with ornaments: broidered linen and silk laid out, bracelets, a
    chain, a ring, ear-rings and a beautiful crown — the things alone."""
    o = [bg(f"or{seed}", w, h, [(0, "#2A1A3A"), (1, "#5A3A4A")])]
    o.append(P(f"M{f(w * 0.06)} {f(h * 0.4)} L {f(w * 0.94)} {f(h * 0.36)} L {f(w * 0.98)} {f(h * 0.96)} L {f(w * 0.02)} {f(h * 0.98)} Z", "#E8E2D6", 2.4))
    for i in range(8):
        o.append(f'<path d="M{f(w * 0.06 + i * w * 0.11)} {f(h * 0.42)} l {f(w * 0.02)} {f(h * 0.54)}" stroke="#7A3BA8" stroke-width="3" stroke-dasharray="6 4" opacity="0.8"></path>')
    k = min(1.6, h / 220)
    o.append(f'<g transform="translate({f(w * 0.5)} {f(h * 0.62)}) scale({f(k)})"><path d="M-30 0 L -30 -22 L -15 -10 L 0 -30 L 15 -10 L 30 -22 L 30 0 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
             '<circle cx="0" cy="-30" r="4" fill="#D7261E" stroke="#0D0D0F" stroke-width="1.2"></circle></g>')
    for i, x in enumerate((0.2, 0.3)):
        o.append(f'<ellipse cx="{f(w * x)}" cy="{f(h * 0.78)}" rx="{f(16 * k)}" ry="{f(8 * k)}" fill="none" stroke="#0D0D0F" stroke-width="{f(6 * k)}"></ellipse><ellipse cx="{f(w * x)}" cy="{f(h * 0.78)}" rx="{f(16 * k)}" ry="{f(8 * k)}" fill="none" stroke="#E8B830" stroke-width="{f(3.6 * k)}"></ellipse>')
    o.append("".join(f'<circle cx="{f(w * 0.66 + i * 9 * k)}" cy="{f(h * 0.82 + math.sin(i * 0.7) * 8 * k)}" r="{f(3.6 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></circle>' for i in range(12)))
    o.append(f'<circle cx="{f(w * 0.8)}" cy="{f(h * 0.6)}" r="{f(7 * k)}" fill="none" stroke="#C8C8D0" stroke-width="{f(3 * k)}"></circle>')
    o.append(f'<path d="M{f(w * 0.88)} {f(h * 0.62)} l 0 {f(14 * k)} M{f(w * 0.92)} {f(h * 0.62)} l 0 {f(14 * k)}" stroke="#E8B830" stroke-width="{f(3 * k)}"></path>')
    return "".join(o)

def awning(x, base, wd, ht, color, seed):
    """A tent-shrine of the high places decked with divers colours."""
    return (P(f"M{f(x - wd / 2)} {f(base)} L {f(x)} {f(base - ht)} L {f(x + wd / 2)} {f(base)} Z", color, 2)
            + f'<path d="M{f(x - wd * 0.25)} {f(base - ht * 0.5)} L {f(x + wd * 0.25)} {f(base - ht * 0.5)}" stroke="#E8B830" stroke-width="2.4"></path>'
            + f'<path d="M{f(x)} {f(base - ht)} L {f(x)} {f(base - ht - 12)}" stroke="#0D0D0F" stroke-width="2"></path>')

def high_places(w, h, seed, lofty=False):
    """High places decked with divers colours upon the hills; lofty=True: a vaulted place built at the head of every way —
    shrines where the roads part."""
    r = random.Random(seed)
    o = [bg(f"hp{seed}", w, h, [(0, "#4A3A6A"), (1, "#E8B080")])]
    svg, pk = ridge(w, h, h * 0.66, 4, seed, h * 0.2, "#8A7A5A")
    o.append(svg)
    if lofty:
        o.append(ground(w, h, h * 0.8, "#B8A07A", dy=0))
        for a, b in (((w * 0.5, h * 0.8), (w * 0.1, h + 10)), ((w * 0.5, h * 0.8), (w * 0.9, h + 10)), ((w * 0.5, h * 0.8), (w * 0.5, h + 10))):
            o.append(f'<path d="M{f(a[0])} {f(a[1])} L {f(b[0])} {f(b[1])}" stroke="#D8C8A0" stroke-width="{f(w * 0.04)}"></path>')
        k = min(1.4, h / 260)
        o.append(P(f"M{f(w * 0.5 - 40 * k)} {f(h * 0.82)} L {f(w * 0.5 - 40 * k)} {f(h * 0.82 - 50 * k)} Q {f(w * 0.5)} {f(h * 0.82 - 90 * k)} {f(w * 0.5 + 40 * k)} {f(h * 0.82 - 50 * k)} L {f(w * 0.5 + 40 * k)} {f(h * 0.82)} Z", "#C8A878", 2.4))
        o.append(idol(w * 0.5, h * 0.82, k * 0.9, color="#E8B830"))
    for i, (px, py) in enumerate(pk):
        o.append(awning(px, py + 8, min(70, w * 0.1), min(60, h * 0.16), ["#C8202A", "#1F5FAD", "#7A3BA8", "#2E8A3A"][i % 4], seed + i))
    return "".join(o)

def lovers_map(w, h, hi=("EGYPT", "ASSYRIA", "CHALDEA")):
    """The nations Jerusalem went after, as a map: Egypt, Assyria, Chaldea, the land of traffic; the Philistines."""
    o = [grid_bg(w, h)]
    J0 = (w * 0.36, h * 0.56)
    pts = {"EGYPT": (w * 0.12, h * 0.86), "ASSYRIA": (w * 0.72, h * 0.18), "CHALDEA": (w * 0.88, h * 0.62), "THE PHILISTINES": (w * 0.16, h * 0.46)}
    for nm, pt in pts.items():
        o.append(route([J0, pt], color="#FF8A6A" if nm in hi else "#4A7A9A", sw=2, dash="6 5") + node(*pt, nm, "#FFD23F" if nm in hi else "#8FD0E2", r=5, dy=-11, size=9))
    o.append(node(*J0, "JERUSALEM", "#D7261E", r=7, dy=-14, size=10))
    return "".join(o)

def sisters_map(w, h):
    """Thine elder sister is Samaria, that dwelleth at thy left hand; thy younger sister, that dwelleth at thy right hand,
    is Sodom: the three cities as a map, Sodom under the waters of the Salt Sea."""
    o = [grid_bg(w, h)]
    o.append(f'<ellipse cx="{f(w * 0.62)}" cy="{f(h * 0.72)}" rx="{f(w * 0.05)}" ry="{f(h * 0.2)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>')
    o.append(f'<path d="M{f(w * 0.64)} {f(h * 0.1)} C {f(w * 0.62)} {f(h * 0.3)} {f(w * 0.66)} {f(h * 0.4)} {f(w * 0.62)} {f(h * 0.52)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>')
    o.append(node(w * 0.44, h * 0.24, "SAMARIA · THE ELDER", "#FF8A6A", r=6, dy=-12, size=9))
    o.append(node(w * 0.46, h * 0.56, "JERUSALEM", "#FFD23F", r=7, dy=-14, size=10))
    o.append(node(w * 0.62, h * 0.8, "SODOM · THE YOUNGER", "#FF8A6A", r=6, dy=-12, size=9))
    o.append(label(w * 0.14, h * 0.92, "THE GREAT SEA", "#4A7A9A", 9))
    return "".join(o)

def covenant_dawn(w, h, seed):
    """I will establish unto thee an everlasting covenant: the sun rising over the city on its hill."""
    o = [jerusalem("cd", w, h, seed, mode="day")]
    o.append(V.rays(w * 0.82, h * 0.3, 24, h * 0.06, h * 0.9, color="#FFF4C2", op=0.22) + sun(w * 0.82, h * 0.3, max(12, h * 0.06), color="#FFD23F", op=0.4))
    return "".join(o)
