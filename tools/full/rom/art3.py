"""Drawings for Romans chapter 3 (Romans 8), on top of rom.art2. The cell standing open in the morning, the chains on the
floor (no condemnation); the plate of the two minds (a lamp gone out, a lamp burning); new grain springing from the dark
furrows at dawn (life to your mortal bodies); the plate of bondage and adoption (an iron collar broken, the signet and the
sealed testament of the heirs); the whole creation groaning — a stormy horizon at dawn, bent trees, the light breaking low;
a man kneeling in prayer by night, wordless, a faint light at the window; the golden chain of 8:29–30; the judgment-seat
with no accuser and the empty throne in light (God never drawn); the ring of the love of Christ that tribulation, anguish,
persecution, famine, nakedness, peril and sword cannot cross; the empty pasture at dusk (8:36: words only, no sheep slain);
and the technical diagram of 8:38–39, neither height nor depth."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from rom.art2 import *
from rom.art2 import f, INK, GOLD, CY, plate_label, _heart, _milky, abraham
from epistle import paul_fig, robed

def open_cell(w, h, seed):
    """There is therefore now no condemnation: a prison cell in the morning, its iron door standing open on the light, the
    chains lying loose on the straw (no one)."""
    b = h * 0.9
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A3238"></rect>']
    for k in range(9):
        y = h * k / 8
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#2A2228" stroke-width="2"></path>')
    dx, dw = w * 0.5, min(w * 0.22, h * 0.5)
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.12)}" width="{f(dw)}" height="{f(b - h * 0.12)}" fill="#FFF4C2" stroke="{INK}" stroke-width="3"></rect>'
             + halo(dx + dw / 2, h * 0.5, max(w, h) * 0.45, "#FFFFFF", 0.55)
             + f'<path d="M{f(dx)} {f(b)} L {f(dx + dw)} {f(b)} L {f(dx + dw + w * 0.16)} {f(h + 10)} L {f(dx - w * 0.22)} {f(h + 10)} Z" fill="#FFE680" opacity="0.5"></path>')
    o.append(f'<path d="M{f(dx)} {f(h * 0.12)} L {f(dx - dw * 0.55)} {f(h * 0.2)} L {f(dx - dw * 0.55)} {f(b + h * 0.05)} L {f(dx)} {f(b)} Z" fill="#4A4A54" stroke="{INK}" stroke-width="2.6"></path>'
             + "".join(f'<path d="M{f(dx - dw * 0.55 * t)} {f(h * 0.12 + h * 0.08 * t)} L {f(dx - dw * 0.55 * t)} {f(b + h * 0.05 * t)}" stroke="#2A2A30" stroke-width="3"></path>' for t in (0.3, 0.6, 0.85)))
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#5A4A3A" stroke="{INK}" stroke-width="2"></rect>')
    k = min(1.2, h / 260)
    for i in range(7):
        x, y = w * 0.14 + i * 18 * k, b + h * 0.04 + math.sin(i) * 4
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(10 * k)}" ry="{f(6 * k)}" transform="rotate({0 if i % 2 else 90} {f(x)} {f(y)})" fill="none" stroke="#0D0D0F" stroke-width="{f(5 * k)}"></ellipse>'
                 f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(10 * k)}" ry="{f(6 * k)}" transform="rotate({0 if i % 2 else 90} {f(x)} {f(y)})" fill="none" stroke="#8A8A94" stroke-width="{f(3 * k)}"></ellipse>')
    return "".join(o)

def two_minds(w, h):
    """The mind of the flesh is death; but the mind of the Spirit is life and peace: a plate — a lamp gone out, its smoke
    rising, at the left; a lamp burning with a steady light at the right."""
    o = [plate_bg(w, h, "ROMANS 8:5–6 · THE MIND OF THE FLESH · THE MIND OF THE SPIRIT")]
    k = min(2.0, h / 150); y = h * 0.7
    o.append(f'<g transform="translate({f(w * 0.27)} {f(y)}) scale({f(k)})"><path d="M-30 0 L 30 0 L 26 6 L -26 6 Z" fill="#3A3A44" stroke="{CY}" stroke-width="1.4"></path>'
             '<path d="M-20 0 C -22 -12 6 -16 18 -8 L 30 -10 L 24 -2 L 16 0 Z" fill="#4A4A54" stroke="#8FD0E2" stroke-width="1.4"></path></g>'
             + smoke(w * 0.27 + 27 * k, y - 12 * k, 5, 85, color="#5A6A7A", op=0.45, k=k * 0.4))
    o.append(halo(w * 0.73 + 27 * k, y - 16 * k, 70 * k, "#FFE680", 0.6) + clay_lamp(w * 0.73, y, k))
    o.append(label(w * 0.27, min(h - 12, y + 30 * k), "THE MIND OF THE FLESH · DEATH", "#C8C8E8", 10) + label(w * 0.73, min(h - 12, y + 30 * k), "THE MIND OF THE SPIRIT · LIFE AND PEACE", GOLD, 10))
    o.append(f'<path d="M{f(w * 0.5)} 34 L {f(w * 0.5)} {f(h - 8)}" stroke="#2C5A7A" stroke-width="1.4" stroke-dasharray="5 5"></path>')
    return "".join(o)

def new_grain(w, h, seed):
    """Shall give life also to your mortal bodies: green blades springing from the dark furrows of a ploughed field at dawn."""
    o = [sky(w, h, "#3A3A7A", "#FFD8A0"), halo(w * 0.7, h * 0.46, max(w, h) * 0.4, "#FFF4C2", 0.6), hills(w, h, h * 0.44, seed, color="#6A6A5A", amp=12, step=90),
         f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A2418"></rect>']
    r = random.Random(seed)
    for j in range(6):
        y = h * (0.54 + j * 0.08)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#2A1A10" stroke-width="{f(3 + j)}"></path>')
        for i in range(int(w / (40 - j * 4))):
            x = i * (40 - j * 4) + r.uniform(-6, 6); hh = h * (0.02 + j * 0.012)
            o.append(f'<path d="M{f(x)} {f(y)} C {f(x - 2)} {f(y - hh * 0.6)} {f(x - 6)} {f(y - hh)} {f(x - 8)} {f(y - hh * 1.1)} M{f(x)} {f(y)} C {f(x + 2)} {f(y - hh * 0.6)} {f(x + 6)} {f(y - hh * 0.9)} {f(x + 9)} {f(y - hh)}" '
                     f'stroke="#7AB84A" stroke-width="{f(1.4 + j * 0.4)}" fill="none"></path>')
    return "".join(o)

def adoption(w, h):
    """Not the spirit of bondage again unto fear, but the spirit of adoption: a plate — an iron slave-collar broken open at
    the left; at the right a signet ring and a testament sealed for the heirs, HEIRS OF GOD · JOINT-HEIRS WITH CHRIST."""
    o = [plate_bg(w, h, "ROMANS 8:15–17 · BONDAGE · ADOPTION")]
    k = min(w / 700, h / 220); cy = h * 0.56
    cx = w * 0.26
    o.append(f'<path d="M{f(cx - 50 * k)} {f(cy)} A {f(50 * k)} {f(36 * k)} 0 0 1 {f(cx + 40 * k)} {f(cy - 22 * k)}" fill="none" stroke="#0D0D0F" stroke-width="{f(16 * k)}"></path>'
             f'<path d="M{f(cx - 50 * k)} {f(cy)} A {f(50 * k)} {f(36 * k)} 0 0 1 {f(cx + 40 * k)} {f(cy - 22 * k)}" fill="none" stroke="#6A6A74" stroke-width="{f(11 * k)}"></path>'
             f'<path d="M{f(cx - 44 * k)} {f(cy + 18 * k)} A {f(50 * k)} {f(36 * k)} 0 0 0 {f(cx + 48 * k)} {f(cy + 8 * k)}" fill="none" stroke="#0D0D0F" stroke-width="{f(16 * k)}"></path>'
             f'<path d="M{f(cx - 44 * k)} {f(cy + 18 * k)} A {f(50 * k)} {f(36 * k)} 0 0 0 {f(cx + 48 * k)} {f(cy + 8 * k)}" fill="none" stroke="#6A6A74" stroke-width="{f(11 * k)}"></path>')
    o.append(label(cx, min(h - 12, cy + 70 * k), "THE SPIRIT OF BONDAGE · FEAR", "#C8C8E8", 10))
    gx = w * 0.74
    o.append(halo(gx, cy, 90 * k, "#FFE680", 0.4) + open_letter(gx - 70 * k, cy - 50 * k, 110 * k, 80 * k, rows=5, seed=815, color="#E8D8B0")
             + f'<circle cx="{f(gx + 30 * k)}" cy="{f(cy + 30 * k)}" r="{f(12 * k)}" fill="#B5121B" stroke="{INK}" stroke-width="1.6"></circle>'
             f'<circle cx="{f(gx + 64 * k)}" cy="{f(cy + 6 * k)}" r="{f(16 * k)}" fill="none" stroke="#0D0D0F" stroke-width="{f(8 * k)}"></circle>'
             f'<circle cx="{f(gx + 64 * k)}" cy="{f(cy + 6 * k)}" r="{f(16 * k)}" fill="none" stroke="#E8B830" stroke-width="{f(5 * k)}"></circle>'
             f'<rect x="{f(gx + 56 * k)}" y="{f(cy - 22 * k)}" width="{f(16 * k)}" height="{f(13 * k)}" rx="2" fill="#2C4A8A" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(label(gx, min(h - 26, cy + 70 * k), "THE SPIRIT OF ADOPTION", GOLD, 10) + label(gx, min(h - 12, cy + 84 * k), "HEIRS OF GOD · JOINT-HEIRS WITH CHRIST", GOLD, 9))
    o.append(f'<path d="M{f(w * 0.5)} 34 L {f(w * 0.5)} {f(h - 8)}" stroke="#2C5A7A" stroke-width="1.4" stroke-dasharray="5 5"></path>')
    return "".join(o)

def groaning(w, h, seed, dawn=0.4):
    """The whole creation groaneth and travaileth in pain together: a stormy horizon at dawn — low torn clouds, trees bent
    by the wind, a dark sea, and the red light breaking under the cloud at the edge of the world (no one)."""
    o = [sky(w, h, "#1A1A2E", "#5A3A4A"), halo(w * 0.6, h * 0.62, max(w, h) * dawn, "#FF8A3D", 0.6),
         f'<rect x="-10" y="{f(h * 0.58)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#FFB04A" opacity="0.6"></rect>',
         clouds(w, h * 0.2, seed, n=7, color="#2A2A3E", op=0.95, h=h), clouds(w, h * 0.42, seed + 1, n=6, color="#3A3048", op=0.9, h=h),
         sea_(w, h, h * 0.62, seed, color="#1A3A4A", deep="#0A1A24", rough=True)]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.8)} C {f(w * 0.2)} {f(h * 0.74)} {f(w * 0.36)} {f(h * 0.78)} {f(w * 0.46)} {f(h + 10)} Z" fill="#1A1418" stroke="{INK}" stroke-width="2"></path>')
    for i, x in enumerate((0.06, 0.16, 0.28)):
        bx, by = w * x, h * (0.8 + i * 0.02)
        o.append(f'<path d="M{f(bx)} {f(by)} C {f(bx + 6)} {f(by - h * 0.1)} {f(bx + 24)} {f(by - h * 0.18)} {f(bx + 44)} {f(by - h * 0.22)}" stroke="#1A1418" stroke-width="5" fill="none"></path>'
                 + "".join(f'<path d="M{f(bx + 10 + j * 10)} {f(by - h * (0.08 + j * 0.04))} l {f(26)} {f(-6)}" stroke="#1A1418" stroke-width="2.4"></path>' for j in range(4)))
    o.append(rain(w, h * 0.6, seed, n=30, color="#8A8AA8", op=0.35))
    return "".join(o)

def kneeling_prayer(p, w, h, seed):
    """The Spirit himself maketh intercession for us with groanings which cannot be uttered: a man kneeling by night in a bare
    room, his head bowed, a faint light at the window (the Spirit is not drawn)."""
    b = h * 0.92
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1E1A2A"></rect>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#1A1420" stroke="{INK}" stroke-width="2"></rect>']
    wx, ww = w * 0.62, min(w * 0.16, h * 0.4)
    o.append(f'<rect x="{f(wx)}" y="{f(h * 0.16)}" width="{f(ww)}" height="{f(ww * 1.3)}" fill="#3A3A6A" stroke="{INK}" stroke-width="2.4"></rect>'
             + halo(wx + ww / 2, h * 0.16 + ww * 0.65, max(w, h) * 0.35, "#FFF4C2", 0.35)
             + f'<path d="M{f(wx)} {f(h * 0.16 + ww * 1.3)} L {f(wx + ww)} {f(h * 0.16 + ww * 1.3)} L {f(wx + ww * 0.6)} {f(b)} L {f(wx - ww * 1.2)} {f(b)} Z" fill="#FFF4C2" opacity="0.18"></path>')
    k = (h * 0.6) / 140
    o.append(E.kneel(w * 0.4, b, k * 0.9, color="#5A4A3A", skin=SKIN, flip=False))
    return "".join(o)

def golden_chain(w, h):
    """Whom he foreknew, he also foreordained … called … justified … glorified: a plate — five gold links rising step by
    step from the left to the light at the right."""
    o = [plate_bg(w, h, "ROMANS 8:29–30 · FOREKNEW · FOREORDAINED · CALLED · JUSTIFIED · GLORIFIED")]
    names = ["FOREKNEW", "FOREORDAINED", "CALLED", "JUSTIFIED", "GLORIFIED"]
    k = min(w / 760, h / 240)
    pts = [(w * (0.12 + i * 0.19), h * (0.78 - i * 0.12)) for i in range(5)]
    o.append(halo(pts[-1][0], pts[-1][1], 80 * k, "#FFE680", 0.6))
    for i, (x, y) in enumerate(pts):
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(38 * k)}" ry="{f(22 * k)}" transform="rotate({-18 if i % 2 else 18} {f(x)} {f(y)})" fill="none" stroke="#0D0D0F" stroke-width="{f(14 * k)}"></ellipse>'
                 f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(38 * k)}" ry="{f(22 * k)}" transform="rotate({-18 if i % 2 else 18} {f(x)} {f(y)})" fill="none" stroke="#E8B830" stroke-width="{f(9 * k)}"></ellipse>')
        o.append(label(x, y - 34 * k, names[i], GOLD, 10))
    return "".join(o)

def no_accuser(p, w, h, seed):
    """Who is he that condemneth? the judgment-seat in the forum with no accuser and no judge before it, and above it, in the
    sky, an empty throne in light (the right hand of God — God never drawn)."""
    o = [judgment_bema(p, w, h, seed, gallio_=False, accusers=False, paul_=False)]
    tx, ty = w * 0.5, h * 0.2
    k = min(1.0, h / 400)
    o.append(halo(tx, ty, max(w, h) * 0.25, "#FFFFFF", 0.8) + rays(tx, ty, 24, 30 * k, max(w, h) * 0.4, "#FFF4C2", 0.35, 3)
             + f'<g transform="translate({f(tx)} {f(ty)}) scale({f(k)})"><path d="M-40 40 L -40 -30 C -40 -60 40 -60 40 -30 L 40 40 Z" fill="#FFE680" stroke="#C8962E" stroke-width="3"></path>'
             '<rect x="-56" y="30" width="112" height="16" fill="#FFD23F" stroke="#C8962E" stroke-width="3"></rect>'
             '<rect x="-30" y="0" width="60" height="30" fill="#FFF4C2" stroke="#C8962E" stroke-width="2"></rect></g>')
    return "".join(o)

def love_ring(w, h):
    """Who shall separate us from the love of Christ? a plate — the heart within a ring of light, and round it, outside the
    ring and unable to cross it, the seven: tribulation, anguish, persecution, famine, nakedness, peril, sword."""
    o = [plate_bg(w, h, "ROMANS 8:35 · WHO SHALL SEPARATE US?")]
    cx, cy = w * 0.5, h * 0.55; R = min(w * 0.18, h * 0.3)
    o.append(halo(cx, cy, R * 1.2, "#FFE680", 0.5) + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R)}" fill="none" stroke="{GOLD}" stroke-width="4"></circle>'
             + _heart(cx, cy, R * 0.5, writing=False) + label(cx, cy + R * 0.82, "THE LOVE OF CHRIST", GOLD, 10))
    names = ["TRIBULATION", "ANGUISH", "PERSECUTION", "FAMINE", "NAKEDNESS", "PERIL", "SWORD"]
    for i, t in enumerate(names):
        a = math.radians(-90 + i * 360 / 7)
        x, y = cx + math.cos(a) * R * 1.75, cy + math.sin(a) * R * 1.25
        ex, ey = cx + math.cos(a) * R * 1.12, cy + math.sin(a) * R * 1.12
        o.append(f'<path d="M{f(x)} {f(y)} L {f(ex)} {f(ey)}" stroke="#FF6A4A" stroke-width="1.6" stroke-dasharray="4 4"></path>'
                 f'<path d="M{f(ex - 6)} {f(ey)} L {f(ex + 6)} {f(ey)}" stroke="#FF6A4A" stroke-width="3"></path>'
                 + plate_label(x, y + 4, t, "#FF8A6A", 9.5))
    return "".join(o)

def empty_pasture(w, h, seed):
    """We were accounted as sheep for the slaughter: an empty sheepfold on a hillside at dusk, its gate open, no sheep (words
    only)."""
    b = h * 0.92
    o = [sky(w, h, "#2A1A3A", "#C8704A"), hills(w, h, h * 0.5, seed, color="#4A3A3A", amp=14, step=90), ground(w, h, h * 0.6, "#5A5A3A", dy=0)]
    fx, fw, fy = w * 0.36, w * 0.4, h * 0.66
    r = random.Random(seed)
    for i in range(int(fw / 18)):
        x = fx + i * 18
        if fw * 0.42 < i * 18 < fw * 0.56: continue
        o.append(f'<rect x="{f(x)}" y="{f(fy - r.uniform(14, 20))}" width="16" height="{f(22)}" fill="#8A8070" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(f'<path d="M{f(fx + fw * 0.42)} {f(fy)} L {f(fx + fw * 0.3)} {f(fy + 18)}" stroke="#5A3A22" stroke-width="5"></path>')
    o.append(tree(w * 0.12, b, min(1.2, h / 300), color="#3A3A2A", seed=seed))
    return "".join(o)

def height_depth(w, h):
    """Neither death, nor life, nor angels, nor principalities, nor things present, nor things to come, nor powers, nor height,
    nor depth, nor any other creature: a technical section through all things — the heights above (the stars), the depths
    below (the deep of the sea), things present and things to come along the line of time — and in the middle the circle of
    the love of God in Christ Jesus our Lord, every arrow stopped at its rim. Angels are only named."""
    o = [plate_bg(w, h, "ROMANS 8:38–39 · NEITHER HEIGHT NOR DEPTH")]
    cx, cy = w * 0.5, h * 0.54; R = min(w * 0.14, h * 0.22)
    top, bot = 34, h - 8
    o.append(f'<rect x="0" y="{f(top)}" width="{f(w)}" height="{f(h * 0.16)}" fill="#14204A" opacity="0.8"></rect>' + mk.stars(30, w, h * 0.12, 839).replace('<g fill="#F3EFE6">', f'<g fill="#F3EFE6" transform="translate(0 {f(top + 4)})">', 1))
    o.append(f'<rect x="0" y="{f(h * 0.84)}" width="{f(w)}" height="{f(h * 0.16)}" fill="#05203A" opacity="0.9"></rect>'
             + "".join(f'<path d="M0 {f(h * (0.87 + 0.04 * j))} ' + "".join(f"Q {f(x + 20)} {f(h * (0.86 + 0.04 * j))} {f(x + 40)} {f(h * (0.87 + 0.04 * j))} " for x in range(0, int(w), 40)) + f'" stroke="#2C7DA8" stroke-width="1.4" fill="none"></path>' for j in range(3)))
    o.append(label(w * 0.5, top + h * 0.1, "HEIGHT", "#C8D8FF", 10) + label(w * 0.5, h * 0.95, "DEPTH", "#8FD0E2", 10))
    o.append(f'<path d="M{f(w * 0.04)} {f(cy)} L {f(w * 0.96)} {f(cy)}" stroke="{CY}" stroke-width="1.4" stroke-dasharray="6 4"></path>'
             + label(w * 0.1, cy - 8, "THINGS PRESENT", CY, 9) + label(w * 0.9, cy - 8, "THINGS TO COME", CY, 9))
    o.append(halo(cx, cy, R * 1.6, "#FFE680", 0.6) + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R)}" fill="#1A1A3A" stroke="{GOLD}" stroke-width="4"></circle>'
             + _heart(cx, cy - R * 0.15, R * 0.42, writing=False, glow_=False)
             + label(cx, cy + R * 0.48, "THE LOVE OF GOD", GOLD, 9) + label(cx, cy + R * 0.66, "IN CHRIST JESUS OUR LORD", GOLD, 7.5))
    names = [("DEATH", 0.18, 0.34), ("LIFE", 0.82, 0.34), ("ANGELS", 0.22, 0.74), ("PRINCIPALITIES", 0.8, 0.74), ("POWERS", 0.34, 0.24),
             ("ANY OTHER CREATURE", 0.68, 0.24)]
    for t, x, y in names:
        X, Y = w * x, h * y
        a = math.atan2(cy - Y, cx - X); ex, ey = cx - math.cos(a) * (R + 8), cy - math.sin(a) * (R + 8)
        o.append(f'<path d="M{f(X)} {f(Y)} L {f(ex)} {f(ey)}" stroke="#FF6A4A" stroke-width="1.4" stroke-dasharray="4 4"></path>'
                 f'<path d="M{f(ex - 7 * math.sin(a))} {f(ey + 7 * math.cos(a))} L {f(ex + 7 * math.sin(a))} {f(ey - 7 * math.cos(a))}" stroke="#FF6A4A" stroke-width="3"></path>'
                 + plate_label(X, Y - 6, t, "#FF8A6A", 9.5))
    return "".join(o)
