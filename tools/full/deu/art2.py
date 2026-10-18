"""Drawings for Deuteronomy chapter 2 (Deuteronomy 3–4): Og's bedstead of iron (a blueprint, nine cubits by four, beside a
man for scale), the likenesses forbidden (4:16–19: man, beast, bird, creeping thing, fish, and the host of heaven, each
struck through), and the people scattered among the nations."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V
from genesis.art2 import fit, ground, hills
from genesis.art3 import label, man, sun
from exo import art8 as B8
from exo.art7 import ban
from lev.art3 import raptor
from num.art import ALL
def f(v): return f"{v:.1f}"
CY = B8.CY

def bedstead(w, h):
    """Nine cubits the length thereof, and four cubits the breadth of it, after the cubit of a man."""
    o = [B8.bp(w, h), B8.title_bar(w, "THE BEDSTEAD OF OG · IRON · 9 × 4 CUBITS")]
    u = min(w * 0.6 / 9, (h - 70) / 5.2)
    x0, y0 = w * 0.36, h * 0.5
    o.append(B8.box(x0, y0 + 2 * u, 9 * u, 4 * u, 0.9 * u, fill="#6A6A72", k=0.5))
    for i in range(5): o.append(f'<path d="M{f(x0 + i * 2.2 * u)} {f(y0 + 2 * u)} L {f(x0 + i * 2.2 * u)} {f(y0 + 2.9 * u)}" stroke="#3A3A42" stroke-width="2"></path>')
    o.append(B8.dim(x0, y0 + 3.4 * u, x0 + 9 * u, y0 + 3.4 * u, "9 CUBITS", size=9))
    o.append(mk.defs("bd", *ALL) + man("bd", x0 - 0.9 * u, y0 + 2.9 * u, (3.5 * u) / 200, "#C8A06A"))
    o.append(label(x0 - 0.9 * u, y0 + 3.4 * u + 12, "A MAN", CY, 8))
    return "".join(o)

def likenesses(w, h, heaven=False):
    """No manner of form: the likeness of male or female, of beast, of winged bird, of creeping thing, of fish (heaven=True:
    the sun, the moon and the stars), each struck through."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#2A2458"></rect>', mk.defs("lk", *ALL)]
    b = h * 0.78; s = min(1.4, h / 180)
    if heaven:
        items = [lambda x: sun(x, b - 40 * s, 26 * s, color="#FFC14D", op=0.5),
                 lambda x: f'<path d="M{f(x - 20 * s)} {f(b - 60 * s)} A {f(24 * s)} {f(24 * s)} 0 1 0 {f(x + 4 * s)} {f(b - 18 * s)} A {f(18 * s)} {f(18 * s)} 0 1 1 {f(x - 20 * s)} {f(b - 60 * s)} Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></path>',
                 lambda x: "".join(f'<circle cx="{f(x + dx * s)}" cy="{f(b - dy * s)}" r="{f(3 * s)}" fill="#FFF4C2"></circle>' for dx, dy in ((-20, 60), (0, 30), (16, 70), (24, 20), (-10, 10)))]
    else:
        items = [lambda x: man("lk", x, b, fit(b, b - 100 * s), "#8A6A4A"), lambda x: E.sheep(x, b, s * 0.5),
                 lambda x: raptor(x, b - 30 * s, s * 0.6), lambda x: f'<path d="M{f(x - 30 * s)} {f(b - 4)} C {f(x - 10 * s)} {f(b - 18 * s)} {f(x + 10 * s)} {f(b + 6)} {f(x + 30 * s)} {f(b - 6)}" fill="none" stroke="#6A8A4A" stroke-width="{f(6 * s)}" stroke-linecap="round"></path>',
                 lambda x: f'<path d="M{f(x - 26 * s)} {f(b - 12 * s)} C {f(x - 10 * s)} {f(b - 28 * s)} {f(x + 14 * s)} {f(b - 28 * s)} {f(x + 22 * s)} {f(b - 12 * s)} C {f(x + 14 * s)} {f(b + 4 * s)} {f(x - 10 * s)} {f(b + 4 * s)} {f(x - 26 * s)} {f(b - 12 * s)} Z M{f(x + 22 * s)} {f(b - 12 * s)} L {f(x + 34 * s)} {f(b - 22 * s)} L {f(x + 34 * s)} {f(b - 2 * s)} Z" fill="#8FB8C8" stroke="#0D0D0F" stroke-width="1.6"></path>']
    n = len(items)
    for i, fn in enumerate(items):
        x = w * (i + 0.5) / n
        o.append(fn(x) + ban(x, b - 40 * s, 44 * s))
    return "".join(o)

def scattered(w, h, seed):
    """Scattered among the peoples: small groups of people far apart across a dark land, each beside a strange idol."""
    r = random.Random(seed)
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#2A2A3A"></rect>', hills(w, h, h * 0.5, seed, color="#1A1A2A", amp=14), ground(w, h, h * 0.62, "#3A3A4A", dy=0), mk.defs("sc", *ALL)]
    for k in range(5):
        x = w * (0.1 + k * 0.2); y = h * (0.72 + (k % 2) * 0.12)
        o.append(f'<path d="M{f(x + 20)} {f(y)} L {f(x + 22)} {f(y - 40)} L {f(x + 30)} {f(y - 46)} L {f(x + 38)} {f(y - 40)} L {f(x + 40)} {f(y)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.4"></path>')
        for j in range(2): o.append(man("sc", x - j * 14, y, fit(y, y - h * 0.18), r.choice(["#5A4A3A", "#4A3A5A", "#3A4A3A"])))
    return "".join(o)
