"""Generators and faces for Exodus Book Three (the passover and the Red Sea): blood-marked doors, hyssop,
the lamb, horses and chariots, pillars of cloud and fire, walls of water, the timbrel, and new faces."""
import math, random
import exodus as E, exodus2 as X
from faces_ex import F
def f(v): return f"{v:.1f}"

def tokens():
    t = X.tokens()
    t["__FACE_PHARAOH_WEEP__"] = F("adam", skin="#B9785A", shadow="#4A2A3A", egypt=("#0D0D0F", "#E8B830"), collar=True, kohl=True, false_beard=True, brow="sorrow", tear=True)
    t["__FACE_MIRIAM_OLD__"] = F("eve", skin="#D9A27A", shadow="#9A6A4A", hair="#B8B2A6", scarf="#C2456A", laugh=True)
    t["__FACE_HEBREW_FEAR__"] = F("adam", skin="#B98A6E", shadow="#5E3A4A", hair="#1A1210", hl="#4A3A2E", brow="sorrow", sweat=True, stubble="#2A1A10")
    t["__FACE_MOSES_CALM__"] = F("adam", skin="#C98E66", shadow="#8A5A3E", hair="#2A1A10", hl="#5A4A3E", beard=True, scarf="#E2D8C4", cord=True, light="#FFE680")
    return t

# ── the passover ──
def door(x, y, w, h, blood=True, light="#FFC14D"):
    """A house door seen from outside, with the blood struck on the lintel and both side-posts."""
    o = [f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{light}" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(x-12)}" y="{f(y-14)}" width="{f(w+24)}" height="16" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.2"></rect>',
         f'<rect x="{f(x-12)}" y="{f(y)}" width="12" height="{f(h)}" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.2"></rect>',
         f'<rect x="{f(x+w)}" y="{f(y)}" width="12" height="{f(h)}" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.2"></rect>']
    if blood:
        r = random.Random(int(x * 7 + y))
        o.append(f'<path d="M{f(x-8)} {f(y-6)} C {f(x+w*0.3)} {f(y-12)} {f(x+w*0.7)} {f(y-2)} {f(x+w+8)} {f(y-8)}" fill="none" stroke="#B5121B" stroke-width="7" stroke-linecap="round"></path>')
        for px in (x - 6, x + w + 6):
            o.append(f'<path d="M{f(px)} {f(y+h*0.12)} C {f(px+2)} {f(y+h*0.3)} {f(px-2)} {f(y+h*0.45)} {f(px)} {f(y+h*0.62)}" fill="none" stroke="#B5121B" stroke-width="6" stroke-linecap="round"></path>')
            for _ in range(2):
                dy = r.uniform(0.2, 0.6)
                o.append(f'<path d="M{f(px)} {f(y+h*dy)} L {f(px)} {f(y+h*dy+r.uniform(8,18))}" stroke="#B5121B" stroke-width="2.4" stroke-linecap="round"></path>')
    return "".join(o)

def hyssop(x, y, s=1.0, rot=0, dipped=True):
    r = random.Random(3)
    leaves = "".join(f'<ellipse cx="{f(r.uniform(-6,6))}" cy="{f(-60 - i*7)}" rx="4" ry="7" fill="#6FA35A" stroke="#0D0D0F" stroke-width="1" transform="rotate({r.choice([-40,40])} 0 {f(-60-i*7)})"></ellipse>' for i in range(8))
    tip = '<g fill="#B5121B">' + "".join(f'<circle cx="{f(r.uniform(-7,7))}" cy="{f(-110 + r.uniform(-8,8))}" r="{f(r.uniform(2,4))}"></circle>' for _ in range(8)) + '</g>' if dipped else ""
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">'
            f'<path d="M0 0 L 0 -112" stroke="#5A6A2A" stroke-width="3"></path>{leaves}{tip}</g>')

def basin(x, y, w):
    return (f'<path d="M{f(x-w/2)} {f(y)} C {f(x-w/2)} {f(y+w*0.35)} {f(x+w/2)} {f(y+w*0.35)} {f(x+w/2)} {f(y)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2.2"></path>'
            f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w/2)}" ry="{f(w*0.1)}" fill="#8A0E16" stroke="#0D0D0F" stroke-width="2"></ellipse>')

def lamb(x, y, s=1.0, flip=False):
    return E.sheep(x, y, s, flip=flip, wool="#F8F6F0", face="#F3E8DA")

# ── horses and chariots ──
HORSE = ("M-58 -62 C -50 -70 -30 -72 0 -70 C 20 -70 34 -74 42 -84 L 56 -104 C 60 -110 68 -110 72 -104 L 88 -82 C 92 -76 88 -70 82 -72 "
         "L 66 -80 C 60 -70 56 -60 52 -50 C 50 -42 52 -36 58 -28 L 72 -10 L 66 -6 L 48 -26 C 42 -34 38 -36 34 -34 L 32 0 L 25 0 L 24 -32 "
         "C 0 -30 -20 -30 -34 -34 L -36 -14 L -24 -2 L -30 2 L -44 -12 C -50 -20 -54 -28 -56 -36 L -70 -4 L -77 -4 L -66 -42 C -66 -52 -64 -58 -58 -62 Z")
TAIL = "M-58 -62 C -74 -62 -86 -50 -94 -26 C -84 -36 -74 -46 -62 -52 Z"
MANE = "M40 -84 C 46 -96 52 -104 58 -108 C 54 -98 50 -88 46 -78 Z"
def horse(x, y, s=1.0, color="#3A2214", flip=False, rim="#0D0D0F"):
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            f'<path d="{TAIL}" fill="#12090A" stroke="{rim}" stroke-width="{f(2/s)}"></path>'
            f'<path d="{HORSE}" fill="{color}" stroke="{rim}" stroke-width="{f(2/s)}" stroke-linejoin="round"></path>'
            f'<path d="{MANE}" fill="#12090A"></path><circle cx="72" cy="-96" r="2.6" fill="#F3EFE6"></circle>'
            f'<path d="M58 -96 L 86 -78 M44 -76 L 58 -70" stroke="#E8B830" stroke-width="{f(2.4/s)}"></path>'
            f'<path d="M-10 -68 C 0 -40 4 -34 6 -30" fill="none" stroke="#E8B830" stroke-width="{f(3/s)}"></path></g>')

def chariot(x, y, s=1.0, flip=False, color="#3A2214", driver="#5A2A16"):
    """A horse pulling a two-wheeled war chariot with a driver; faces right unless flip."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            + horse(0, 0, 1.0, color)
            + f'<path d="M-40 -46 L -100 -54" stroke="#8A5A30" stroke-width="5"></path>'
            f'<g transform="translate(-150 0)">'
            f'<path d="M-4 -34 L -16 -110 L -2 -112 C 6 -96 14 -84 20 -78 L 4 -78 Z" fill="{driver}" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<circle cx="-10" cy="-120" r="10" fill="{driver}" stroke="#0D0D0F" stroke-width="2"></circle>'
            f'<path d="M-22 -126 C -14 -136 0 -134 2 -124 L -6 -116 L -22 -116 Z" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="1.6"></path>'
            f'<path d="M-6 -100 L 30 -150" stroke="#0D0D0F" stroke-width="3"></path><path d="M26 -156 L 34 -146 L 36 -160 Z" fill="#C8C2D6" stroke="#0D0D0F" stroke-width="1.4"></path>'
            f'<path d="M-30 -30 L -30 -78 L 40 -78 C 54 -66 56 -46 50 -30 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></path>'
            f'<path d="M-24 -70 L 40 -70 M-24 -46 L 48 -46" stroke="#B5421E" stroke-width="3"></path>'
            f'<circle cx="0" cy="-26" r="26" fill="none" stroke="#0D0D0F" stroke-width="7"></circle><circle cx="0" cy="-26" r="26" fill="none" stroke="#8A5A30" stroke-width="4"></circle>'
            + "".join(f'<path d="M0 -26 L {f(26*math.cos(a))} {f(-26+26*math.sin(a))}" stroke="#5A3A22" stroke-width="3"></path>' for a in [i * math.pi / 3 for i in range(6)])
            + '<circle cx="0" cy="-26" r="5" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></circle></g></g>')

# ── pillars ──
def pillar_cloud(cx, bottom, top, w, seed):
    r = random.Random(seed); o = []
    y = bottom
    while y > top:
        k = (y - top) / max(1, bottom - top)
        ww = w * (0.7 + 0.3 * (1 - k))
        for _ in range(3):
            o.append((r.uniform(cx - ww / 2, cx + ww / 2), y + r.uniform(-10, 10), r.uniform(ww * 0.22, ww * 0.38)))
        y -= w * 0.18
    outl = "".join(f'<circle cx="{f(a)}" cy="{f(b)}" r="{f(c)}"></circle>' for a, b, c in o)
    shade = "".join(f'<circle cx="{f(a + c*0.25)}" cy="{f(b + c*0.25)}" r="{f(c*0.7)}"></circle>' for a, b, c in o[::2])
    return (f'<g fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2.4">{outl}</g><g fill="#F3EFE6">{outl}</g>'
            f'<g fill="#C8C2D6" opacity="0.55">{shade}</g>')

def pillar_fire(cx, bottom, top, w, seed):
    o = [f'<ellipse cx="{f(cx)}" cy="{f((top+bottom)/2)}" rx="{f(w*1.4)}" ry="{f((bottom-top)*0.62)}" fill="#FFC14D" opacity="0.25"></ellipse>']
    h = bottom - top; n = 4
    for i in range(n):
        yb = bottom - h * i / n
        o.append(E.blaze(cx, yb, w * (1.1 - i * 0.12), h / n * 1.9, seed + i, n=7))
    return "".join(o)

# ── the sea ──
def water_wall(pts_top, base_y, x_edge, seed, side="left", color="#0F4C68", mid="#2C9DB8", foam="#E8F6FA"):
    """A standing wall of sea: pts_top is the crest line from the panel edge to the vanishing end."""
    r = random.Random(seed)
    top = " L ".join(f"{f(x)} {f(y)}" for x, y in pts_top)
    x0, x1 = pts_top[0][0], pts_top[-1][0]
    d = f"M{f(x_edge)} {f(base_y)} L {top} L {f(x1)} {f(base_y)} Z"
    o = [f'<path d="{d}" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>']
    # inner bands
    for k in (0.25, 0.5, 0.75):
        band = " L ".join(f"{f(x)} {f(y + (base_y - y) * k)}" for x, y in pts_top)
        o.append(f'<path d="M{band}" fill="none" stroke="{mid}" stroke-width="{f(6 - k*4)}" opacity="0.7"></path>')
    # the face of the wall (towards the dry path)
    xa, ya = pts_top[-1]
    o.append(f'<path d="M{f(xa)} {f(ya)} L {f(xa)} {f(base_y)}" stroke="{foam}" stroke-width="5"></path>')
    # crest foam curls
    for (x, y) in pts_top[::2]:
        rr = r.uniform(10, 22)
        sgn = 1 if side == "left" else -1
        o.append(f'<path d="M{f(x - rr*sgn)} {f(y+4)} C {f(x - rr*sgn)} {f(y - rr)} {f(x + rr*sgn)} {f(y - rr)} {f(x + rr*sgn*0.6)} {f(y - 2)}" fill="none" stroke="{foam}" stroke-width="3.5" stroke-linecap="round"></path>')
    # fish in the wall
    for _ in range(4):
        fx = r.uniform(min(x0, x1) + 20, max(x0, x1) - 20); fy = r.uniform(min(y for _, y in pts_top) + 60, base_y - 30)
        o.append(f'<g transform="translate({f(fx)} {f(fy)}) scale({f(r.uniform(0.25,0.45))})" opacity="0.6"><path d="M-30 0 C -16 -14 14 -14 26 0 C 14 14 -16 14 -30 0 Z M-30 0 L -44 -12 L -42 0 L -44 12 Z" fill="#8FD0E2"></path></g>')
    return "".join(o)

def timbrel(x, y, s=1.0, rot=0):
    jing = "".join(f'<ellipse cx="{f(28*math.cos(a))}" cy="{f(28*math.sin(a))}" rx="5" ry="3" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2" transform="rotate({f(math.degrees(a)+90)} {f(28*math.cos(a))} {f(28*math.sin(a))})"></ellipse>' for a in [i * math.pi / 4 for i in range(8)])
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">'
            f'<circle r="28" fill="#F3E8DA" stroke="#0D0D0F" stroke-width="2.4"></circle><circle r="22" fill="none" stroke="#C9A86A" stroke-width="2"></circle>{jing}'
            '<path d="M-14 -6 C -6 -12 6 -12 14 -6" fill="none" stroke="#C2456A" stroke-width="3"></path></g>')

def pillar_fire(cx, bottom, top, w, seed):
    h = bottom - top
    return (f'<ellipse cx="{f(cx)}" cy="{f(top + h*0.55)}" rx="{f(w*1.6)}" ry="{f(h*0.6)}" fill="#FFC14D" opacity="0.25"></ellipse>'
            + E.blaze(cx, bottom, w, h, seed, n=7))

def sea_corridor(W, H, vp, l_near, r_near, seed, deep="#0B2E4A", face="#1F6F9A", foam="#E8F6FA", floor="#C8A06A", uid="sc"):
    """The Red Sea parted, in one-point perspective: two walls of water whose inner faces run from the
    near edges (x = l_near, r_near) to the vanishing point vp = (x, y), with dry ground between."""
    r = random.Random(seed); vx, vy = vp
    o = [f'<defs><linearGradient id="{uid}G" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8FD0E2" stop-opacity="0.35"></stop><stop offset="0.5" stop-color="#2C9DB8" stop-opacity="0"></stop><stop offset="1" stop-color="#05121E" stop-opacity="0.55"></stop></linearGradient></defs>']
    o.append(f'<path d="M{f(l_near)} {f(H+10)} L {f(vx-6)} {f(vy+30)} L {f(vx+6)} {f(vy+30)} L {f(r_near)} {f(H+10)} Z" fill="{floor}" stroke="#0D0D0F" stroke-width="2"></path>')
    for k in range(1, 6):
        t = k / 6; yy = vy + 30 + (H - vy - 30) * t ** 1.6
        xl = vx - 6 + (l_near - vx + 6) * t ** 1.6; xr = vx + 6 + (r_near - vx - 6) * t ** 1.6
        o.append(f'<path d="M{f(xl)} {f(yy)} C {f(xl + (xr-xl)*0.3)} {f(yy-4)} {f(xl + (xr-xl)*0.7)} {f(yy+4)} {f(xr)} {f(yy)}" fill="none" stroke="#8A6A3A" stroke-width="1.4" opacity="0.6"></path>')
    for side, xn in (("l", l_near), ("r", r_near)):
        sg = -1 if side == "l" else 1
        xv = vx + sg * 6
        edge = -10 if side == "l" else W + 10
        o.append(f'<path d="M{f(edge)} -10 L {f(xn)} -10 L {f(xv)} {f(vy-24)} L {f(xv)} {f(vy+30)} L {f(xn)} {f(H+10)} L {f(edge)} {f(H+10)} Z" fill="{deep}"></path>')
        o.append(f'<path d="M{f(xn)} -10 L {f(xv)} {f(vy-24)} L {f(xv)} {f(vy+30)} L {f(xn)} {f(H+10)} Z" fill="{face}" stroke="#0D0D0F" stroke-width="2.4"></path>')
        o.append(f'<path d="M{f(xn)} -10 L {f(xv)} {f(vy-24)} L {f(xv)} {f(vy+30)} L {f(xn)} {f(H+10)} Z" fill="url(#{uid}G)"></path>')
        for k in range(1, 9):
            t = k / 9
            y0 = -10 + (H + 20) * t
            o.append(f'<path d="M{f(xn)} {f(y0)} L {f(xv)} {f(vy - 24 + 54 * t)}" stroke="#8FD0E2" stroke-width="{f(3 - t*1.5)}" opacity="0.55"></path>')
        for _ in range(5):
            t = r.uniform(0.15, 0.8); fx = xn + (xv - xn) * t * 0.6; fy = r.uniform(40, H - 60)
            o.append(f'<g transform="translate({f(fx)} {f(fy)}) scale({f(-sg*0.4)} 0.4)" opacity="0.5"><path d="M-30 0 C -16 -14 14 -14 26 0 C 14 14 -16 14 -30 0 Z M-30 0 L -44 -12 L -42 0 L -44 12 Z" fill="#8FD0E2"></path></g>')
        # spray and curls along the crest
        for k in range(0, 9):
            t = k / 8; cx = xn + (xv - xn) * t; cy = -10 + (vy - 24 + 10) * t; rr = 22 * (1 - t) + 5
            o.append(f'<path d="M{f(cx - rr*sg)} {f(cy + 6)} C {f(cx - rr*sg)} {f(cy - rr)} {f(cx + rr*sg)} {f(cy - rr)} {f(cx + rr*sg*0.5)} {f(cy)}" fill="none" stroke="{foam}" stroke-width="{f(2 + 3*(1-t))}" stroke-linecap="round"></path>')
            o.append(f'<circle cx="{f(cx + r.uniform(-10,10))}" cy="{f(cy - rr - r.uniform(2, 14))}" r="{f(r.uniform(1.5, 4)*(1.2-t))}" fill="{foam}"></circle>')
        o.append(f'<path d="M{f(xv)} {f(vy-24)} L {f(xv)} {f(vy+30)}" stroke="{foam}" stroke-width="3"></path>')
        o.append(f'<path d="M{f(xn)} {f(H+10)} L {f(xv)} {f(vy+30)}" stroke="{foam}" stroke-width="4" opacity="0.8"></path>')
    return "".join(o)

def crash(W, H, seed, color="#1F6F9A", deep="#0B2E4A", foam="#E8F6FA"):
    """A great wave breaking from the right over the whole panel."""
    r = random.Random(seed)
    o = [f'<path d="M{W+10} {H+10} L {W+10} -10 C {W*0.6} -20 {W*0.25} 20 {W*0.18} {H*0.28} C {W*0.14} {H*0.4} {W*0.22} {H*0.52} {W*0.32} {H*0.46} '
         f'C {W*0.26} {H*0.6} {W*0.1} {H*0.7} -10 {H*0.72} L -10 {H+10} Z" fill="{color}" stroke="#0D0D0F" stroke-width="3"></path>',
         f'<path d="M{W+10} {H*0.2} C {W*0.7} {H*0.1} {W*0.4} {H*0.16} {W*0.3} {H*0.34} C {W*0.4} {H*0.3} {W*0.7} {H*0.4} {W+10} {H*0.5} Z" fill="{deep}" opacity="0.6"></path>']
    for k, op in ((1, 0.6), (2, 0.45), (3, 0.3)):
        dx, dy = W * 0.06 * k, H * 0.08 * k
        o.append(f'<path d="M{W+10} {f(-6+dy)} C {f(W*0.6+dx)} {f(-14+dy)} {f(W*0.25+dx)} {f(24+dy)} {f(W*0.18+dx)} {f(H*0.28+dy)} C {f(W*0.15+dx)} {f(H*0.38+dy)} {f(W*0.2+dx)} {f(H*0.46+dy)} {f(W*0.28+dx)} {f(H*0.44+dy)}" fill="none" stroke="#8FD0E2" stroke-width="3" opacity="{op}"></path>')
    o.append(f'<path d="M{W+10} -6 C {W*0.6} -14 {W*0.25} 24 {W*0.18} {H*0.28} C {W*0.14} {H*0.4} {W*0.22} {H*0.52} {W*0.32} {H*0.46}" fill="none" stroke="{foam}" stroke-width="10" stroke-linecap="round"></path>')
    for _ in range(40):
        t = r.uniform(0, 1)
        o.append(f'<circle cx="{f(W*0.14 + t*W*0.5 + r.uniform(-30, 30))}" cy="{f(H*0.05 + r.uniform(0, H*0.45))}" r="{f(r.uniform(2, 7))}" fill="{foam}"></circle>')
    return "".join(o)
