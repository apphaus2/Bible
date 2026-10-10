"""New drawings for the Genesis volume (anything the digest art does not already cover)."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus5 as V, joshua1 as J, judges1 as G1, judges2 as S, samuel1 as A, numbers1 as N, snake as SN
import faces
def f(v): return f"{v:.1f}"

ADAM = faces.face("adam")
ADAM_AFRAID = faces.face("adam", brow="sorrow", sweat=True, light="#8FD0E2")
ADAM_GRIEF = faces.face("adam", brow="sorrow", tear=True)
EVE = faces.face("eve")
EVE_AFRAID = faces.face("eve", brow="sorrow", light="#8FD0E2")
EVE_SORROW = faces.face("eve", brow="sorrow", tear=True)
SKIN = "#1A1210"   # Adam and Eve before the coats of skins are drawn as silhouettes

def starfield(w, h, seed, n=140):
    return mk.stars(n, w, h, seed)

def evening(w, h, seed=1, sun="#FF8A3D"):
    """Evening and morning: a low horizon, the sun half under it, the first stars."""
    r = random.Random(seed)
    hills = "M-10 " + str(h + 10) + " L " + " L ".join(f"{f(x)} {f(h * 0.62 + r.uniform(-12, 12))}" for x in range(-10, w + 60, 60)) + f" L {w + 10} {h + 10} Z"
    return (mk.stars(40, w, h * 0.5, seed, color="#F3EFE6")
            + f'<circle cx="{f(w * 0.72)}" cy="{f(h * 0.64)}" r="{f(h * 0.2)}" fill="{sun}"></circle>'
            + f'<path d="{hills}" fill="#1A1430" stroke="#0D0D0F" stroke-width="2"></path>')

def fish_swarm(w, h, seed, n=40):
    r = random.Random(seed); o = []
    for _ in range(n):
        x, y, s = r.uniform(0, w), r.uniform(h * 0.15, h), r.uniform(0.5, 1.3)
        c = r.choice(["#FFD23F", "#FF8A3D", "#8FD0E2", "#F3EFE6", "#C2456A"])
        fl = r.random() < 0.5; sx = -s if fl else s
        o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})"><path d="M-16 0 C -8 -9 8 -9 14 0 C 8 9 -8 9 -16 0 Z" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></path>'
                 '<path d="M-16 0 L -26 -8 L -24 0 L -26 8 Z" fill="#0D0D0F"></path><circle cx="8" cy="-2" r="1.6" fill="#0D0D0F"></circle></g>')
    bub = "".join(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(0, h))}" r="{f(r.uniform(1.5, 4))}" fill="none" stroke="#F3EFE6" stroke-width="1.2" opacity="0.7"></circle>' for _ in range(30))
    return "".join(o) + bub

def beasts(w, h, seed):
    """Every kind of beast on the new earth."""
    r = random.Random(seed); base = h * 0.82
    o = [f'<path d="M-10 {f(base - 20)} C {w * 0.3} {f(base - 34)} {w * 0.6} {f(base - 10)} {w + 10} {f(base - 26)} L {w + 10} {h + 10} L -10 {h + 10} Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>']
    o.append(J.oak(w * 0.12, base - 10, 0.55, seed=seed))
    o.append(G1.palm(w * 0.9, base - 12, 0.7))
    o.append(G1.camel(w * 0.78, base, 0.42, flip=True))
    o.append(A.cow(w * 0.55, base + 4, 0.5, color="#8A5A30"))
    o.append(S.lion(w * 0.28, base, 0.55))
    o += [E.sheep(w * x, base + 8 + r.uniform(-4, 4), 0.5, flip=r.random() < 0.5) for x in (0.4, 0.45, 0.66)]
    o.append(N.ass(w * 0.94, base + 6, 0.3, flip=True))
    o.append(SN.snake([(w * 0.6, base + 30), (w * 0.64, base + 22), (w * 0.69, base + 30), (w * 0.73, base + 24)], 4, f"bz{seed}"))
    return "".join(o)

def couple(p, x, y, s, gap=40, hands=True):
    """The man and the woman side by side, as silhouettes, hands joined."""
    up = [(-22, -158), (-34, -120), (-44, -96)] if hands else None
    return (mk.person(p, round(x - gap * s / 2), y, round(s, 3), body=SKIN, flip=True, up=up)
            + mk.person(p, round(x + gap * s / 2), y, round(s * 0.94, 3), body=SKIN, woman=True, hair=True, up=up))

def harvest(w, h, seed):
    """Herbs yielding seed and trees with fruit: food for man and beast."""
    o = [f'<path d="M-10 {f(h * 0.7)} L {w + 10} {f(h * 0.66)} L {w + 10} {h + 10} L -10 {h + 10} Z" fill="#8A9A3A" stroke="#0D0D0F" stroke-width="2"></path>']
    o.append(S.grain(-10, w * 0.55, h * 0.78, 40, seed))
    o.append(S.grain(-10, w * 0.55, h * 0.95, 50, seed + 1))
    r = random.Random(seed)
    for x in (w * 0.68, w * 0.86):
        o.append(J.oak(x, h * 0.86, 0.7, seed=int(x)))
        o += [f'<circle cx="{f(x + r.uniform(-40, 40))}" cy="{f(h * 0.86 - r.uniform(110, 160))}" r="5" fill="#D7261E" stroke="#0D0D0F" stroke-width="1.2"></circle>' for _ in range(7)]
    return "".join(o)

def mist(w, h, seed):
    r = random.Random(seed)
    ground = f'<path d="M-10 {f(h * 0.62)} C {w * 0.3} {f(h * 0.58)} {w * 0.7} {f(h * 0.66)} {w + 10} {f(h * 0.6)} L {w + 10} {h + 10} L -10 {h + 10} Z" fill="#B5866A" stroke="#0D0D0F" stroke-width="2"></path>'
    cracks = "".join(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-20, 20))} {f(r.uniform(6, 16))} l {f(r.uniform(-14, 14))} {f(r.uniform(6, 14))}" fill="none" stroke="#6A4A3A" stroke-width="1.6"></path>'
                     for x, y in [(r.uniform(0, w), r.uniform(h * 0.66, h * 0.95)) for _ in range(16)])
    bands = "".join(f'<path d="M{f(-20 + k * 30)} {f(h * 0.6 - k * 22)} C {f(w * 0.25)} {f(h * 0.5 - k * 22)} {f(w * 0.55)} {f(h * 0.66 - k * 22)} {f(w + 20)} {f(h * 0.54 - k * 22)}" fill="none" stroke="#F3EFE6" stroke-width="{14 - k * 2}" stroke-linecap="round" opacity="{0.55 - k * 0.08}"></path>' for k in range(5))
    return ground + cracks + bands

def gems(w, h):
    """The gold of Havilah, bdellium and the onyx stone."""
    gold = "".join(f'<path d="M{x - 26} {y} L {x - 14} {y - 22} L {x + 12} {y - 26} L {x + 28} {y - 6} L {x + 16} {y + 8} L {x - 18} {y + 8} Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="2"></path>'
                   f'<path d="M{x - 10} {y - 16} L {x + 6} {y - 18}" stroke="#FFF4C2" stroke-width="3"></path>' for x, y in [(w * 0.28, h * 0.62), (w * 0.4, h * 0.7), (w * 0.22, h * 0.76)])
    onyx = "".join(f'<ellipse cx="{x}" cy="{y}" rx="26" ry="18" fill="#1A1A22" stroke="#0D0D0F" stroke-width="2"></ellipse><path d="M{x - 18} {y} C {x - 8} {y - 8} {x + 8} {y + 8} {x + 18} {y}" fill="none" stroke="#F3EFE6" stroke-width="2"></path>'
                   for x, y in [(w * 0.66, h * 0.66), (w * 0.78, h * 0.74)])
    bdel = f'<path d="M{w * 0.52} {h * 0.78} C {w * 0.5} {h * 0.66} {w * 0.6} {h * 0.62} {w * 0.6} {h * 0.76} Z" fill="#E8B060" stroke="#0D0D0F" stroke-width="2" opacity="0.9"></path>'
    ground = f'<path d="M-10 {h * 0.8} L {w + 10} {h * 0.78} L {w + 10} {h + 10} L -10 {h + 10} Z" fill="#6A4A3A"></path>'
    return ground + gold + bdel + onyx

def four_rivers(w, h):
    """One river out of Eden parting into four heads, seen from above."""
    cx, cy = w * 0.5, h * 0.22
    ends = [(w * 0.08, h), (w * 0.36, h), (w * 0.64, h), (w * 0.92, h)]
    paths = "".join(f'<path d="M{cx} {cy} C {cx} {cy + 60} {ex} {ey - 120} {ex} {ey}" fill="none" stroke="#0D0D0F" stroke-width="22"></path>'
                    f'<path d="M{cx} {cy} C {cx} {cy + 60} {ex} {ey - 120} {ex} {ey}" fill="none" stroke="#4A9ABA" stroke-width="16"></path>' for ex, ey in ends)
    return (f'<rect x="-10" y="-10" width="{w + 20}" height="{h + 20}" fill="#7A9A4A"></rect>' + paths
            + f'<path d="M{cx} -10 L {cx} {cy}" stroke="#0D0D0F" stroke-width="26"></path><path d="M{cx} -10 L {cx} {cy}" stroke="#4A9ABA" stroke-width="20"></path>'
            + f'<circle cx="{cx}" cy="{cy}" r="16" fill="#4A9ABA" stroke="#0D0D0F" stroke-width="2"></circle>')

def naming(p, w, h, seed):
    """The man naming the beasts and the birds brought to him."""
    base = h * 0.86
    o = [f'<path d="M-10 {base} L {w + 10} {base - 6} L {w + 10} {h + 10} L -10 {h + 10} Z" fill="#7A9A4A" stroke="#0D0D0F" stroke-width="2"></path>']
    o.append(mk.person(p, round(w * 0.2), round(base + 2), 0.9, body=SKIN, up=[(-22, -158), (-48, -168), (-76, -176)], flip=True))
    o.append(S.lion(w * 0.48, base, 0.5, flip=True, roar=False))
    o.append(A.cow(w * 0.7, base + 2, 0.45, flip=True))
    o.append(E.sheep(w * 0.88, base + 4, 0.5, flip=True))
    o.append(G1.camel(w * 0.98, base - 6, 0.3, flip=True))
    r = random.Random(seed)
    o += [f'<path d="M{f(x)} {f(y)} q 8 -8 16 0 q 8 -8 16 0" fill="none" stroke="#0D0D0F" stroke-width="3"></path>' for x, y in [(w * r.uniform(0.35, 0.95), h * r.uniform(0.1, 0.4)) for _ in range(9)]]
    return "".join(o)

def dawn_couple(p, w, h):
    base = h * 0.84
    return (V.rays(w * 0.5, base, 36, 30, 900, color="#FFF4C2", op=0.35)
            + f'<circle cx="{w * 0.5}" cy="{base}" r="70" fill="#FFD23F"></circle>'
            + f'<path d="M-10 {base} L {w + 10} {base} L {w + 10} {h + 10} L -10 {h + 10} Z" fill="#2A3A1E" stroke="#0D0D0F" stroke-width="2"></path>'
            + couple(p, w * 0.5, round(base), 0.95, gap=46))

def fig_leaves(w, h, seed):
    """Fig-leaves sewn together: big lobed leaves and a running stitch."""
    r = random.Random(seed); o = []
    LEAF = "M0 0 C -10 -20 -40 -26 -46 -54 C -30 -50 -26 -70 -10 -76 C -8 -60 4 -60 6 -80 C 20 -70 22 -54 40 -56 C 36 -34 14 -24 0 0 Z"
    for i in range(5):
        x, y, rot = w * (0.12 + i * 0.19), h * 0.78, r.uniform(-20, 20)
        o.append(f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale(1.7)"><path d="{LEAF}" fill="{r.choice(["#3F8A44", "#2E6A32", "#5E8F26"])}" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 '<path d="M0 0 L 0 -70 M0 -30 L -24 -46 M0 -40 L 20 -54" fill="none" stroke="#1A3A1A" stroke-width="1.2"></path></g>')
    o.append(f'<path d="M{w * 0.05} {h * 0.62} L {w * 0.95} {h * 0.62}" fill="none" stroke="#F3EFE6" stroke-width="3" stroke-dasharray="10 8"></path>')
    return "".join(o)

def walking_voice(w, h, seed):
    """The cool of the day: trees bending in the wind and a light moving among them."""
    r = random.Random(seed)
    o = [f'<ellipse cx="{w * 0.5}" cy="{h * 0.5}" rx="{w * 0.18}" ry="{h * 0.4}" fill="#FFF4C2" opacity="0.5"></ellipse>']
    for i in range(7):
        x = w * (0.05 + i * 0.15) + r.uniform(-10, 10)
        o.append(f'<g transform="skewX({f(r.uniform(-8, -3))})">' + J.oak(x, h + 10, r.uniform(0.9, 1.3), seed=seed + i) + '</g>')
    o += [f'<path d="M{f(r.uniform(0, w))} {f(r.uniform(0, h))} c 20 -6 40 6 60 0" fill="none" stroke="#F3EFE6" stroke-width="2" opacity="0.7"></path>' for _ in range(14)]
    return "".join(o)

def serpent_dust(w, h, seed):
    r = random.Random(seed); base = h * 0.7
    ground = f'<path d="M-10 {base} L {w + 10} {base - 10} L {w + 10} {h + 10} L -10 {h + 10} Z" fill="#B5866A" stroke="#0D0D0F" stroke-width="2"></path>'
    dust = "".join(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(base - 30, h))}" r="{f(r.uniform(1, 3))}" fill="#E8C88A" opacity="0.8"></circle>' for _ in range(80))
    pts = [(w * 0.08, base + 40), (w * 0.25, base + 20), (w * 0.4, base + 50), (w * 0.58, base + 26), (w * 0.74, base + 44), (w * 0.9, base + 30)]
    return ground + SN.snake(pts, 14, f"sd{seed}", head_scale=1.4) + dust

def thorns(w, h, seed):
    r = random.Random(seed); base = h * 0.55
    o = [f'<path d="M-10 {base} L {w + 10} {base + 6} L {w + 10} {h + 10} L -10 {h + 10} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>']
    for _ in range(18):
        x, y, s = r.uniform(0, w), r.uniform(base + 10, h), r.uniform(0.6, 1.3)
        stems = "".join(f'<path d="M0 0 C {f(r.uniform(-30, 30))} -30 {f(r.uniform(-40, 40))} -50 {f(r.uniform(-40, 40))} -70" fill="none" stroke="#3A2A1A" stroke-width="3"></path>' for _ in range(4))
        spikes = "".join(f'<path d="M{f(r.uniform(-30, 30))} {f(r.uniform(-60, -10))} l -6 -4 l 8 0 Z" fill="#3A2A1A"></path>' for _ in range(10))
        head = f'<circle cx="{f(r.uniform(-20, 20))}" cy="-70" r="8" fill="#7A3BA8" stroke="#0D0D0F" stroke-width="1.4"></circle>' if r.random() < 0.5 else ""
        o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">{stems}{spikes}{head}</g>')
    return "".join(o)

def toil(p, w, h, seed):
    base = h * 0.8
    o = [f'<circle cx="{w * 0.82}" cy="{h * 0.2}" r="40" fill="#FFD23F"></circle>',
         V.rays(w * 0.82, h * 0.2, 30, 44, 700, color="#FFF4C2", op=0.3),
         f'<path d="M-10 {base} L {w + 10} {base - 8} L {w + 10} {h + 10} L -10 {h + 10} Z" fill="#9A6A4A" stroke="#0D0D0F" stroke-width="2"></path>',
         "".join(f'<path d="M{x} {base + 20} l 40 -4" stroke="#5A3A22" stroke-width="3"></path>' for x in range(0, int(w), 70)),
         E.kneel(w * 0.4, base + 4, 0.9, color="#8A5A30", skin="#4A2A1A"),
         f'<path d="M{w * 0.4 + 30} {base - 100} L {w * 0.4 + 80} {base + 6}" stroke="#5A3A22" stroke-width="6"></path>',
         "".join(f'<path d="M{f(w * 0.4 + dx)} {f(base - 118 + dy)} c 2 4 2 6 0 8 c -2 -2 -2 -4 0 -8 Z" fill="#8FD0E2" stroke="#0D0D0F" stroke-width="1"></path>' for dx, dy in [(16, 0), (34, -6), (24, 14)])]
    return "".join(o)

def skins(p, w, h):
    """The man and his wife clothed in the coats of skins."""
    base = h * 0.86
    fur = "".join(f'<path d="M{x} -150 l -4 10 M{x + 6} -120 l -4 10 M{x - 4} -90 l -4 10 M{x + 2} -60 l -4 10" stroke="#5A3A22" stroke-width="2"></path>' for x in (-20, -6, 8, 20))
    return (f'<path d="M-10 {base} L {w + 10} {base} L {w + 10} {h + 10} L -10 {h + 10} Z" fill="#5A6A3A" stroke="#0D0D0F" stroke-width="2"></path>'
            + mk.person(p, round(w * 0.4), round(base), 0.95, body="#5A2A16", cloth="#8A5A30", sw=3, flip=True, extra=fur)
            + mk.person(p, round(w * 0.6), round(base), 0.9, body="#5A2A16", cloth="#A8743A", woman=True, hair=True, sw=3, extra=fur))

def cosmic(w, h, cx=None, cy=-40):
    cx = w / 2 if cx is None else cx
    return V.rays(cx, cy, 40, 40, max(w, h) * 1.6, color="#FFF4C2", op=0.18) + mk.stars(60, w, h, int(w + h))
