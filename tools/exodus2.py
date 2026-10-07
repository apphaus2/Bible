"""Generators and faces for Exodus Book Two (the plagues): frogs, flies, lice, locusts, dead fish, hail, lightning,
columns, recolored serpents, and new faces (Aaron, the magicians, Pharaoh afraid)."""
import math, random
import faces_ex, snake as SN
from faces_ex import F
def f(v): return f"{v:.1f}"

# ── faces ──
BOILS = '\n<g fill="#D7261E" stroke="#5A0E16" stroke-width="1.2">' + "".join(
    f'<circle cx="{x}" cy="{y}" r="{r}"></circle>' for x, y, r in [(196, 210, 6), (214, 236, 4.5), (182, 262, 5.5), (226, 200, 3.5), (170, 228, 4), (204, 290, 5), (186, 304, 3.5), (232, 274, 4)]) + \
    '</g><g fill="#FFC98A">' + "".join(f'<circle cx="{x-1.5}" cy="{y-1.5}" r="{r*0.35:.1f}"></circle>' for x, y, r in [(196, 210, 6), (182, 262, 5.5), (204, 290, 5)]) + '</g>'
def tokens():
    t = faces_ex.tokens()
    t["__FACE_AARON__"] = F("adam", skin="#C98E66", shadow="#8A5A3E", hair="#9A968E", hl="#6A665E", beard=True, scarf="#4A6A9A", cord=True)
    t["__FACE_AARON_FIRE__"] = F("adam", skin="#D9946A", shadow="#7A3A2A", hair="#9A968E", hl="#6A665E", beard=True, scarf="#4A6A9A", cord=True, light="#FFD23F")
    t["__FACE_MAGICIAN__"] = F("adam", skin="#B9785A", shadow="#4A2A3A", egypt=("#0D0D0F", "#E8E2D6"), kohl=True, collar=True, light="#B07AE8")
    t["__FACE_MAGICIAN_FEAR__"] = F("adam", skin="#B9785A", shadow="#4A2A3A", egypt=("#0D0D0F", "#E8E2D6"), kohl=True, collar=True, brow="sorrow", sweat=True)
    t["__FACE_MAGICIAN_BOILS__"] = F("adam", skin="#B9785A", shadow="#4A2A3A", egypt=("#0D0D0F", "#E8E2D6"), kohl=True, collar=True, brow="sorrow", sweat=True) + BOILS
    t["__FACE_PHARAOH_FEAR__"] = F("adam", skin="#B9785A", shadow="#4A2A3A", egypt=("#0D0D0F", "#E8B830"), collar=True, kohl=True, false_beard=True, brow="sorrow", sweat=True)
    t["__FACE_MOSES_STERN__"] = F("adam", skin="#C47A5A", shadow="#5A1A16", hair="#2A1A10", hl="#5A4A3E", beard=True, scarf="#E2D8C4", cord=True, brow="scowl", light="#FF6A4A")
    return t

# ── creatures ──
def frog(x, y, s=1.0, flip=False, body="#5E8F26", dark="#2E4A12"):
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            f'<path d="M-16 -2 C -26 -6 -28 -16 -18 -18 C -8 -18 -2 -8 0 0 Z" fill="{body}" stroke="#0D0D0F" stroke-width="1.6"></path>'
            f'<path d="M-14 -4 C -16 -16 -4 -26 10 -24 C 22 -22 28 -14 26 -6 C 24 0 14 2 0 0 C -8 0 -12 -2 -14 -4 Z" fill="{body}" stroke="#0D0D0F" stroke-width="1.8"></path>'
            f'<path d="M-6 -2 C 4 0 16 0 24 -4" fill="none" stroke="#C9E265" stroke-width="2"></path>'
            f'<g fill="{dark}"><circle cx="-4" cy="-16" r="2.6"></circle><circle cx="4" cy="-20" r="2"></circle><circle cx="-10" cy="-10" r="2"></circle></g>'
            f'<path d="M16 -4 L 22 2" stroke="#0D0D0F" stroke-width="3.6" stroke-linecap="round"></path><path d="M16 -4 L 22 2" stroke="{body}" stroke-width="2" stroke-linecap="round"></path>'
            f'<circle cx="17" cy="-22" r="5" fill="#E8D040" stroke="#0D0D0F" stroke-width="1.5"></circle><ellipse cx="18" cy="-22" rx="2.6" ry="1.4" fill="#0D0D0F"></ellipse>'
            '</g>')

def frogs(n, x0, x1, y0, y1, seed, smin=0.6, smax=1.3):
    r = random.Random(seed); items = []
    for _ in range(n):
        items.append((r.uniform(y0, y1), r.uniform(x0, x1), r.random() < 0.5))
    items.sort()
    return "".join(frog(x, y, smin + (smax - smin) * (y - y0) / max(1, y1 - y0), flip=fl, body=r.choice(["#5E8F26", "#4E7A22", "#6FA35A"])) for y, x, fl in items)

def fly(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">'
            f'<ellipse cx="-2" cy="-4" rx="5" ry="3" fill="#C8D6E0" opacity="0.75" transform="rotate(-25 -2 -4)"></ellipse>'
            f'<ellipse cx="2" cy="-4" rx="5" ry="3" fill="#E8F0F6" opacity="0.75" transform="rotate(25 2 -4)"></ellipse>'
            f'<ellipse cx="0" cy="0" rx="2.6" ry="4" fill="#12090A"></ellipse><circle cx="0" cy="-4.2" r="2" fill="#5A0E16"></circle></g>')

def swarm(n, cx, cy, rx, ry, seed, smin=0.5, smax=1.4):
    r = random.Random(seed); o = []
    for _ in range(n):
        a = r.uniform(0, 6.283); d = r.random() ** 0.6
        o.append(fly(cx + math.cos(a) * rx * d, cy + math.sin(a) * ry * d, r.uniform(smin, smax), r.uniform(-60, 60)))
    return "".join(o)

def lice(n, x0, x1, y0, y1, seed, color="#2A1A10"):
    r = random.Random(seed)
    return f'<g fill="{color}">' + "".join(f'<ellipse cx="{f(r.uniform(x0, x1))}" cy="{f(r.uniform(y0, y1))}" rx="{f(r.uniform(1, 2.4))}" ry="{f(r.uniform(0.8, 1.6))}"></ellipse>' for _ in range(n)) + "</g>"

def locust(x, y, s=1.0, rot=0, flip=False, body="#8A7A2A", wing="#C8B870"):
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(sx)} {f(s)})">'
            f'<path d="M-4 0 L -18 -20 L -34 6" fill="none" stroke="#0D0D0F" stroke-width="4.5" stroke-linejoin="round"></path>'
            f'<path d="M-4 0 L -18 -20 L -34 6" fill="none" stroke="{body}" stroke-width="2.6" stroke-linejoin="round"></path>'
            f'<path d="M-30 -2 C -28 -8 -10 -10 10 -10 C 22 -10 30 -6 32 0 C 30 4 22 6 10 6 C -10 6 -28 4 -30 -2 Z" fill="{body}" stroke="#0D0D0F" stroke-width="1.8"></path>'
            f'<g stroke="#0D0D0F" stroke-width="0.9" opacity="0.6"><path d="M-20 -6 L -20 4 M-12 -8 L -12 5 M-4 -9 L -4 6"></path></g>'
            f'<path d="M-34 -8 C -16 -20 12 -18 22 -10 C 6 -9 -14 -6 -34 -8 Z" fill="{wing}" stroke="#0D0D0F" stroke-width="1.4" opacity="0.92"></path>'
            f'<circle cx="31" cy="-3" r="7.5" fill="{body}" stroke="#0D0D0F" stroke-width="1.8"></circle><circle cx="33" cy="-5" r="2.4" fill="#0D0D0F"></circle>'
            f'<path d="M34 -10 C 42 -24 52 -28 60 -26 M30 -10 C 34 -26 42 -32 50 -34" fill="none" stroke="#0D0D0F" stroke-width="1.4"></path>'
            f'<path d="M14 4 L 18 14 M22 4 L 28 12" stroke="#0D0D0F" stroke-width="2"></path></g>')

def locusts(n, x0, x1, y0, y1, seed, smin=0.25, smax=0.9):
    r = random.Random(seed); items = sorted((r.uniform(smin, smax), r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(-25, 25)) for _ in range(n))
    return "".join(locust(x, y, s, rot) for s, x, y, rot in items)

def fish(x, y, s=1.0, rot=180, color="#C8C2D6"):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">'
            f'<path d="M-30 0 C -16 -14 14 -14 26 0 C 14 14 -16 14 -30 0 Z M-30 0 L -44 -12 L -42 0 L -44 12 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.8"></path>'
            f'<path d="M-10 -9 C -6 -4 -6 4 -10 9" fill="none" stroke="#0D0D0F" stroke-width="1.2"></path>'
            f'<path d="M12 -5 L 18 1 M18 -5 L 12 1" stroke="#0D0D0F" stroke-width="1.8" stroke-linecap="round"></path></g>')

def hail(n, x0, x1, y0, y1, seed):
    r = random.Random(seed); o = []
    for _ in range(n):
        x, y, rr = r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(2.5, 7)
        o.append(f'<path d="M{f(x+rr*2.2)} {f(y-rr*6)} L {f(x)} {f(y)}" stroke="#E8F0F6" stroke-width="{f(rr*0.5)}" opacity="0.45" stroke-linecap="round"></path>'
                 f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rr)}" fill="#F3F7FA" stroke="#5A7A9A" stroke-width="1"></circle>')
    return "".join(o)

def bolt(x, y, h, seed, w=1.0):
    r = random.Random(seed); pts = [(x, y)]; cx = x
    n = 7
    for i in range(1, n + 1):
        cx += r.uniform(-30, 30) * w; pts.append((cx, y + h * i / n))
    left = [(px - (6 - i * 0.7) * w, py) for i, (px, py) in enumerate(pts)]
    right = [(px + (6 - i * 0.7) * w + 8 * w * (i % 2), py) for i, (px, py) in enumerate(pts)]
    d = "M" + " L ".join(f"{f(a)} {f(b)}" for a, b in left) + " L " + " L ".join(f"{f(a)} {f(b)}" for a, b in reversed(right)) + " Z"
    return f'<path d="{d}" fill="#FFF4C2" stroke="#FFD23F" stroke-width="3" stroke-linejoin="round"></path><path d="{d}" fill="#FFFFFF"></path>'

def columns(xs, top, bottom, w, color="#5A1A16", band="#E8B830"):
    o = []
    for x in xs:
        o.append(f'<rect x="{f(x)}" y="{f(top)}" width="{f(w)}" height="{f(bottom-top)}" fill="{color}" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<path d="M{f(x)} {f(top+40)} L {f(x+w)} {f(top+40)} M{f(x)} {f(top+48)} L {f(x+w)} {f(top+48)}" stroke="{band}" stroke-width="3"></path>'
                 f'<path d="M{f(x-8)} {f(bottom)} L {f(x+w+8)} {f(bottom)} L {f(x+w+4)} {f(bottom-14)} L {f(x-4)} {f(bottom-14)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

BROWN = {"#5E8F26": "#8A5A30", "#22401A": "#3A2214", "#1B3A12": "#2A140C", "#C9E265": "#E8B070", "#D8F08A": "#E8C88A", "#E4DE9A": "#D8C08A"}
def serpent(P, wmax, uid, head_scale=1.0, brown=False):
    s = SN.snake(P, wmax, uid, head_scale)
    if brown:
        for a, b in BROWN.items(): s = s.replace(a, b)
    return s

def kine_dead(x, y, s, color="#8A7A6A", flip=False):
    """A dead ox lying on its side: legs stiff and straight out, head down on the ground."""
    sx = -s if flip else s
    legs = "".join(f'<path d="M{a} -14 L {b} 14" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path><path d="M{a} -14 L {b} 14" stroke="{color}" stroke-width="4" stroke-linecap="round"></path>' for a, b in [(-30, -40), (-18, -24), (18, 26), (30, 44)])
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">' + legs +
            f'<path d="M-44 -22 C -44 -40 -20 -46 10 -44 C 36 -42 46 -34 46 -20 C 46 -8 30 -4 0 -4 C -30 -4 -44 -8 -44 -22 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="M-30 -36 C -10 -40 20 -40 36 -34" fill="none" stroke="#F3EFE6" stroke-width="2" opacity="0.5"></path>'
            f'<path d="M-44 -24 C -50 -40 -62 -44 -70 -30 C -76 -18 -68 -6 -56 -6 C -48 -6 -44 -14 -44 -24 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="M-62 -34 C -66 -46 -60 -52 -54 -50" fill="none" stroke="#E8E2D6" stroke-width="3" stroke-linecap="round"></path>'
            f'<path d="M-64 -24 L -58 -18 M-58 -24 L -64 -18" stroke="#0D0D0F" stroke-width="1.6"></path>'
            f'<path d="M44 -26 C 54 -26 58 -18 62 -10" fill="none" stroke="#0D0D0F" stroke-width="2"></path></g>')
