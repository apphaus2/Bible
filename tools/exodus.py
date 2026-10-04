"""Generators for the Exodus books: reeds, ark of bulrushes, burning bush, sheep, hands, sandals."""
import math, random
def f(v): return f"{v:.1f}"

def reeds(x0, x1, by, h, n, seed, color="#4E7A3A", dark="#2E4A22", heads=0.35, lean=0.0):
    r = random.Random(seed); out = []
    for i in range(n):
        x = r.uniform(x0, x1); hh = h * r.uniform(0.55, 1.05); w = r.uniform(2.5, 5.5)
        bend = r.uniform(-0.25, 0.25) * hh + lean * hh
        tx, ty = x + bend, by - hh
        cx, cy = x + bend * 0.2, by - hh * 0.55
        col = r.choice([color, color, dark])
        out.append(f'<path d="M{f(x-w)} {f(by)} Q {f(cx-w*0.6)} {f(cy)} {f(tx)} {f(ty)} Q {f(cx+w*0.6)} {f(cy)} {f(x+w)} {f(by)} Z" fill="{col}" stroke="#0D0D0F" stroke-width="1"></path>')
        if r.random() < heads:
            # cattail head just below tip on a thin stalk
            t = 0.82; hx = x + (cx - x) * 2 * t * (1 - t) + (tx - x) * t * t; hy = by + (cy - by) * 2 * t * (1 - t) + (ty - by) * t * t
            ang = math.degrees(math.atan2(tx - hx, -(ty - hy)))
            out.append(f'<rect x="{f(hx-3.5)}" y="{f(hy-16)}" width="7" height="22" rx="3.5" fill="#6B3A10" stroke="#0D0D0F" stroke-width="1" transform="rotate({f(ang)} {f(hx)} {f(hy)})"></rect>')
    return "\n".join(out)

def basket(cx, cy, w, h, uid, lid=True):
    """Ark of bulrushes: woven oval basket, daubed with pitch, seen 3/4 from the side."""
    x0, x1 = cx - w / 2, cx + w / 2; top = cy - h * 0.15; bot = cy + h / 2
    o = [f'<defs><pattern id="{uid}Weave" width="10" height="8" patternUnits="userSpaceOnUse"><rect width="10" height="8" fill="#C9A86A"></rect><path d="M0 2 C 3 0 7 0 10 2 M0 6 C 3 4 7 4 10 6" stroke="#8A6A3A" stroke-width="1.6" fill="none"></path><path d="M5 0 L 5 8" stroke="#6B4A22" stroke-width="0.8" opacity="0.6"></path></pattern></defs>']
    o.append(f'<path d="M{f(x0)} {f(top)} C {f(x0)} {f(bot+h*0.1)} {f(x1)} {f(bot+h*0.1)} {f(x1)} {f(top)} Z" fill="url(#{uid}Weave)" stroke="#0D0D0F" stroke-width="2.2"></path>')
    # pitch at the waterline
    o.append(f'<path d="M{f(x0+w*0.02)} {f(cy+h*0.22)} C {f(x0+w*0.1)} {f(bot+h*0.06)} {f(x1-w*0.1)} {f(bot+h*0.06)} {f(x1-w*0.02)} {f(cy+h*0.22)} C {f(x1-w*0.2)} {f(cy+h*0.32)} {f(x0+w*0.2)} {f(cy+h*0.32)} {f(x0+w*0.02)} {f(cy+h*0.22)} Z" fill="#2A1A10" opacity="0.85"></path>')
    # rim
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(top)}" rx="{f(w/2)}" ry="{f(h*0.16)}" fill="#3A2412" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(top)}" rx="{f(w/2-5)}" ry="{f(h*0.16-4)}" fill="none" stroke="#E8C88A" stroke-width="3"></ellipse>')
    if lid:
        o.append(f'<path d="M{f(x0+4)} {f(top)} C {f(x0+w*0.1)} {f(top-h*0.5)} {f(cx+w*0.05)} {f(top-h*0.55)} {f(cx+w*0.12)} {f(top-h*0.02)} Z" fill="url(#{uid}Weave)" stroke="#0D0D0F" stroke-width="2"></path>')
    return "\n".join(o)

def flame(x, y, w, h, lean, layers=(("#D7261E", 1.0), ("#FF8A3D", 0.78), ("#FFD23F", 0.55), ("#FFF4C2", 0.3))):
    o = []
    for col, k in layers:
        ww, hh = w * k, h * k; tx = x + lean * k; ty = y - hh
        o.append(f'<path d="M{f(x-ww)} {f(y)} C {f(x-ww*1.1)} {f(y-hh*0.45)} {f(tx-ww*0.6)} {f(y-hh*0.7)} {f(tx)} {f(ty)} C {f(tx+ww*0.1)} {f(y-hh*0.55)} {f(x+ww*1.2)} {f(y-hh*0.4)} {f(x+ww)} {f(y)} C {f(x+ww*0.5)} {f(y+ww*0.5)} {f(x-ww*0.5)} {f(y+ww*0.5)} {f(x-ww)} {f(y)} Z" fill="{col}"' + (' stroke="#0D0D0F" stroke-width="1.6"' if k == 1.0 else '') + '></path>')
    return "\n".join(o)

def blaze_path(cx, by, w, h, seed, n=9):
    """One outline for a whole fire: a rounded base and a crown of curling tongues."""
    r = random.Random(seed)
    xs = [cx - w / 2 + w * (i + 0.5) / n for i in range(n)]
    pts = []
    for i, x in enumerate(xs):
        mid = 1 - abs((i + 0.5) / n - 0.5) * 1.5
        th = h * (0.45 + 0.55 * mid) * r.uniform(0.8, 1.05)
        pts.append((x + r.uniform(-w * 0.02, w * 0.02), by - th, r.uniform(-w * 0.05, w * 0.05)))
    d = f"M{f(cx - w/2)} {f(by - h*0.08)}"
    prev_x = cx - w / 2
    for i, (x, y, lean) in enumerate(pts):
        valley_y = by - h * 0.22 - h * 0.25 * (1 - abs((i + 0.5) / n - 0.5) * 2) * r.uniform(0.6, 1.0)
        vx = (prev_x + x) / 2 if i else cx - w / 2 + w * 0.02
        d += f" Q {f(vx)} {f(valley_y)} {f(x + lean*0.3 - w*0.03)} {f(y + (by-y)*0.35)} Q {f(x + lean - w*0.02)} {f(y + (by-y)*0.12)} {f(x + lean)} {f(y)}"
        d += f" Q {f(x + w*0.01)} {f(y + (by-y)*0.3)} {f(x + w*0.035)} {f(y + (by-y)*0.5)}"
        prev_x = x
    d += f" Q {f(cx + w/2)} {f(by - h*0.2)} {f(cx + w/2)} {f(by - h*0.08)} C {f(cx + w*0.45)} {f(by + h*0.06)} {f(cx - w*0.45)} {f(by + h*0.06)} {f(cx - w/2)} {f(by - h*0.08)} Z"
    return d

def tongue(x, y, ww, hh, lean):
    tx, ty = x + lean, y - hh
    return (f"M{f(x-ww)} {f(y)} C {f(x-ww*1.25)} {f(y-hh*0.45)} {f(tx-ww*0.9)} {f(y-hh*0.62)} {f(tx)} {f(ty)} "
            f"C {f(tx+ww*0.05)} {f(y-hh*0.68)} {f(x+ww*1.25)} {f(y-hh*0.42)} {f(x+ww)} {f(y)} "
            f"C {f(x+ww*0.6)} {f(y+ww*0.7)} {f(x-ww*0.6)} {f(y+ww*0.7)} {f(x-ww)} {f(y)} Z")

def blaze(cx, by, w, h, seed, n=9):
    """A single burning mass: overlapping S-curved tongues merged under one outline, then hotter cores."""
    r = random.Random(seed); T = []
    for i in range(n):
        u = (i + 0.5) / n - 0.5                      # -0.5 .. 0.5
        x = cx + u * w * 0.82 + r.uniform(-w * 0.02, w * 0.02)
        hh = h * (1 - (abs(u) * 1.45) ** 1.4) * r.uniform(0.82, 1.0)
        ww = w * r.uniform(0.11, 0.15)
        T.append((x, by - h * 0.12, ww, max(hh, h * 0.28), u * w * 0.35 + r.uniform(-w * 0.04, w * 0.04)))
    T.sort(key=lambda t: t[3])
    o = []
    base = f'<ellipse cx="{f(cx)}" cy="{f(by - h*0.1)}" rx="{f(w*0.47)}" ry="{f(h*0.14)}"'
    o.append(base + ' fill="#0D0D0F" stroke="#0D0D0F" stroke-width="5"></ellipse>')
    o += [f'<path d="{tongue(*t)}" fill="#0D0D0F" stroke="#0D0D0F" stroke-width="5" stroke-linejoin="round"></path>' for t in T]
    for col, kw, kh in (("#D7261E", 1.0, 1.0), ("#FF8A3D", 0.74, 0.8), ("#FFD23F", 0.52, 0.6), ("#FFF4C2", 0.3, 0.38)):
        if kw == 1.0:
            o.append(base + f' fill="{col}"></ellipse>')
        else:
            o.append(f'<ellipse cx="{f(cx)}" cy="{f(by - h*0.1)}" rx="{f(w*0.47*kw)}" ry="{f(h*0.14*kw)}" fill="{col}"></ellipse>')
        for (x, y, ww, hh, ln) in T:
            o.append(f'<path d="{tongue(cx + (x-cx)*kw, y, ww*kw, hh*kh, ln*kh)}" fill="{col}"></path>')
    return "\n".join(o)

def bush(cx, by, w, h, seed, flames=True, leaves=True):
    """A thorny desert bush. With flames=True it burns but is not consumed: green leaves stay among the fire."""
    r = random.Random(seed); branches = []; tips = []; nodes = []
    def grow(x, y, ang, ln, wd, depth):
        x2 = x + math.sin(ang) * ln; y2 = y - math.cos(ang) * ln
        mx = (x + x2) / 2 + r.uniform(-ln * 0.15, ln * 0.15); my = (y + y2) / 2
        branches.append((f'M{f(x)} {f(y)} Q {f(mx)} {f(my)} {f(x2)} {f(y2)}', wd))
        nodes.append((x2, y2))
        if depth == 0 or ln < 14:
            tips.append((x2, y2)); return
        for d in (-1, 1) if r.random() < 0.8 else (-1, 0, 1):
            grow(x2, y2, ang * 0.85 + d * r.uniform(0.2, 0.45), ln * r.uniform(0.62, 0.78), wd * 0.66, depth - 1)
    for a in (-0.75, -0.38, 0, 0.38, 0.75):
        grow(cx + a * w * 0.06, by, a * 0.55 + r.uniform(-0.06, 0.06), h * r.uniform(0.22, 0.27), 9, 4)
    out = []
    if flames:
        out.append(blaze(cx, by, w * 1.0, h * 1.1, seed + 11, n=9))
    for d, wd in branches:
        out.append(f'<path d="{d}" fill="none" stroke="#0D0D0F" stroke-width="{f(wd+3)}" stroke-linecap="round"></path>')
    for d, wd in branches:
        out.append(f'<path d="{d}" fill="none" stroke="#3A2214" stroke-width="{f(wd)}" stroke-linecap="round"></path>')
    # thorns
    for (x, y) in r.sample(nodes, min(len(nodes), 26)):
        a = r.uniform(0, 6.28)
        out.append(f'<path d="M{f(x)} {f(y)} L {f(x+math.cos(a)*9)} {f(y+math.sin(a)*9)}" stroke="#3A2214" stroke-width="2" stroke-linecap="round"></path>')
    if leaves:
        for (x, y) in r.sample(tips, len(tips) // 2) + r.sample(nodes, min(len(nodes), 8)):
            a = r.uniform(-60, 60)
            out.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="4.5" ry="9" fill="#3F8A44" stroke="#0D0D0F" stroke-width="1.2" transform="rotate({f(a)} {f(x)} {f(y)})"></ellipse>')
    if flames:
        # front flames licking the branches, smaller
        for (x, y) in r.sample(tips, min(len(tips), 0)):
            out.append(flame(x + r.uniform(-6, 6), y + r.uniform(0, 14), r.uniform(w * 0.025, w * 0.04), r.uniform(h * 0.1, h * 0.18), r.uniform(-8, 8)))
        for _ in range(26):
            x = r.uniform(cx - w * 0.5, cx + w * 0.5); y = by - r.uniform(h * 0.4, h * 1.1); s = r.uniform(1.5, 3.5)
            out.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(s)}" fill="#FFE680"></circle>')
    return "\n".join(out)

def sheep(x, y, s=1.0, flip=False, wool="#E8E2D6", face="#2A1A10"):
    sx = -s if flip else s
    puffs = "".join(f'<circle cx="{px}" cy="{py}" r="{pr}"></circle>' for px, py, pr in [(-22,-34,13),(-8,-40,14),(8,-40,14),(22,-34,13),(-26,-22,12),(26,-22,12),(-10,-20,14),(10,-20,14)])
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            f'<g stroke="#0D0D0F" stroke-width="3.5" stroke-linecap="round"><path d="M-18 -14 L -19 0"></path><path d="M-8 -12 L -8 0"></path><path d="M10 -12 L 11 0"></path><path d="M20 -14 L 21 0"></path></g>'
            f'<g fill="{wool}" stroke="#0D0D0F" stroke-width="2">{puffs}</g><g fill="{wool}">{puffs.replace(" r=", " data-r=").replace("data-r=", "r=")}</g>'
            f'<path d="M30 -40 C 42 -46 52 -40 52 -30 C 52 -22 46 -20 40 -22 C 34 -24 30 -30 30 -40 Z" fill="{face}" stroke="#0D0D0F" stroke-width="1.6"></path>'
            f'<path d="M34 -40 C 30 -44 26 -42 26 -38" fill="{face}" stroke="#0D0D0F" stroke-width="1.4"></path>'
            '</g>')

def hand(cx, cy, s, skin="#D9A27A", line="#0D0D0F", uid="h", spots=False):
    """An open right hand, palm facing the viewer, fingers up. Local units: palm about 80 wide."""
    fingers = [(-30, -40, -34, -108), (-10, -46, -10, -126), (10, -46, 12, -122), (28, -40, 34, -100)]
    o = [f'<g transform="translate({f(cx)} {f(cy)}) scale({f(s)})">']
    def limb(d, w):
        return (f'<path d="{d}" fill="none" stroke="{line}" stroke-width="{w+5}" stroke-linecap="round"></path>',
                f'<path d="{d}" fill="none" stroke="{skin}" stroke-width="{w}" stroke-linecap="round"></path>')
    outer, inner = [], []
    for (x0, y0, x1, y1) in fingers:
        a, b = limb(f'M{x0} {y0} L {x1} {y1}', 18); outer.append(a); inner.append(b)
    a, b = limb('M-36 0 C -52 -12 -62 -30 -68 -52', 20); outer.append(a); inner.append(b)
    a, b = limb('M0 10 L 0 70', 46); outer.append(a); inner.append(b)
    o += outer
    o.append(f'<path d="M-46 -46 C -52 -10 -44 22 -24 38 C -6 48 16 48 30 36 C 48 18 52 -12 46 -46 C 22 -58 -22 -58 -46 -46 Z" fill="{skin}" stroke="{line}" stroke-width="2.5"></path>')
    o += inner
    o.append(f'<g fill="none" stroke="{line}" stroke-width="1.4" opacity="0.5"><path d="M-30 -14 C -10 -20 14 -18 32 -26"></path><path d="M-36 6 C -16 -2 4 2 24 -6"></path><path d="M-20 30 C -24 10 -30 -4 -42 -12"></path></g>')
    if spots:
        r = random.Random(7)
        for _ in range(18):
            x = r.uniform(-36, 36); y = r.uniform(-110, 60)
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(r.uniform(3,7))}" ry="{f(r.uniform(2,5))}" fill="#F3EFE6" stroke="#C8C2D6" stroke-width="0.8" opacity="0.9"></ellipse>')
    o.append('</g>')
    return "\n".join(o)

SANDAL = "M-14 0 C -16 -20 -12 -46 0 -50 C 12 -46 16 -20 14 0 C 12 10 -12 10 -14 0 Z"
ROD = "M0 0 L 0 -210 C 0 -232 22 -236 26 -220"

KNEEL = "M-58 0 L 40 0 C 46 -8 42 -18 30 -22 C 10 -30 4 -50 8 -78 C 10 -96 6 -106 -2 -110 C -16 -116 -32 -110 -38 -96 C -48 -76 -54 -50 -56 -34 C -62 -22 -64 -10 -58 0 Z"
KNEEL_HEAD = "M4 -120 A 13 13 0 1 0 30 -120 A 13 13 0 1 0 4 -120 Z"
KNEEL_ARM = "M-6 -100 L 30 -84 L 32 -120"
def kneel(x, y, s, color="#3A2214", rim="#0D0D0F", flip=False, skin=None):
    """A kneeling figure in profile (facing right), one arm raised across the face."""
    sx = -s if flip else s
    sk = skin or color
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            f'<path d="{KNEEL}" fill="{color}" stroke="{rim}" stroke-width="2"></path>'
            f'<path d="{KNEEL_HEAD}" fill="{sk}" stroke="{rim}" stroke-width="2"></path>'
            f'<path d="{KNEEL_ARM}" fill="none" stroke="{rim}" stroke-width="13.5" stroke-linecap="round" stroke-linejoin="round"></path>'
            f'<path d="{KNEEL_ARM}" fill="none" stroke="{color}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"></path>'
            f'<circle cx="32" cy="-121" r="5.5" fill="{sk}" stroke="{rim}" stroke-width="1.6"></circle>'
            '<path d="M-44 -40 C -30 -30 -6 -24 24 -20 M-40 -80 C -30 -60 -20 -40 -4 -30" fill="none" stroke="#12090A" stroke-width="1.4" opacity="0.6"></path></g>')

def sandal(x, y, s, rot, sole="#C9A86A", strap="#5A3A22"):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">'
            f'<path d="{SANDAL}" fill="{sole}" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="M-11 -6 C -6 -2 6 -2 11 -6" fill="none" stroke="#8A6A3A" stroke-width="1.4"></path>'
            f'<path d="M-13 -28 C -6 -20 6 -20 13 -28 M0 -40 L 0 -22" fill="none" stroke="{strap}" stroke-width="4" stroke-linecap="round"></path>'
            f'<path d="M-14 -16 C -22 -14 -26 -8 -24 -2 M14 -16 C 22 -14 26 -8 24 -2" fill="none" stroke="{strap}" stroke-width="2.4" stroke-linecap="round"></path></g>')
