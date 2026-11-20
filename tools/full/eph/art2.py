"""Drawings for the Ephesians volume, chapter 2 (Ephesians 4–6), on eph.art (which carries Galatians', Acts' and the epistle
kit's drawings). The whole armor of God (6:13–17) is the volume's set piece: the Roman soldier at full height on a
technical plate, each piece labelled, the fiery darts striking the shield and going out (no archer). Every function takes
(p, w, h, seed, ...) or (w, h, ...); the kit clips every drawing to its panel."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from eph.art import *
from eph.art import _person_mark
from act.art import f, INK
from genesis.art2 import dove
from luk.art import incense_altar
from mat.art3 import waves
from epistle import GUARD
from ntcast import PAUL as PAUL_FACE

def _defs(p): return mk.defs(p, *ALL, "ManUp", "WomanUp", "LieB", "LieA")

# ---- Ephesians 4 ----------------------------------------------------------------------------------------------------------
def _anchor(x, y, s, c):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round">'
            '<circle cx="0" cy="-26" r="5"></circle><path d="M0 -21 L 0 24 M-12 -12 L 12 -12 M-22 10 C -18 24 -8 26 0 24 C 8 26 18 24 22 10"></path></g>')

def _crown(x, y, s, c):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-22 12 L -22 -10 L -11 2 L 0 -16 L 11 2 L 22 -10 L 22 12 Z" fill="none" stroke="{c}" stroke-width="3" stroke-linejoin="round"></path>'
            f'<path d="M-22 18 L 22 18" stroke="{c}" stroke-width="3"></path></g>')

def _shield_icon(x, y, s, c):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-18 -22 L 18 -22 L 18 4 C 18 16 8 24 0 28 C -8 24 -18 16 -18 4 Z" fill="none" stroke="{c}" stroke-width="3"></path>'
            f'<path d="M0 -22 L 0 28 M-18 -2 L 18 -2" stroke="{c}" stroke-width="2"></path></g>')

def _water(x, y, s, c):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round">'
            + "".join(f'<path d="M-24 {dy} C -16 {dy - 7} -8 {dy - 7} 0 {dy} C 8 {dy + 7} 16 {dy + 7} 24 {dy}"></path>' for dy in (-8, 4, 16))
            + '<path d="M0 -26 L 0 -16 M-6 -22 L 0 -16 L 6 -22"></path></g>')

def seven_ones(w, h):
    """There is one body, and one Spirit … one Lord, one faith, one baptism, one God and Father of all: an emblem plate —
    at the centre a medallion of light (no figure) for the one God and Father of all, about it six medallions joined to it,
    each with its emblem: a body (a figure in outline), the Spirit (a dove of light), hope (an anchor), the Lord (a crown),
    faith (a shield), baptism (water)."""
    o = [plate_bg(w, h, "EPHESIANS 4:4–6 · ONE"), mk.defs("so", *ALL)]
    top = 34; H = h - top
    cx, cy = w * 0.5, top + H * 0.46                                          # raised, so the lowest names clear the last line
    R0 = min(H * 0.17, w * 0.1); r = min(H * 0.11, w * 0.07)
    rx, ry = min(w * 0.36, w * 0.5 - r - 40), H * 0.3
    items = [("ONE BODY", "body"), ("ONE SPIRIT", "dove"), ("ONE HOPE", "anchor"), ("ONE LORD", "crown"), ("ONE FAITH", "shield"), ("ONE BAPTISM", "water")]
    pts = []
    for i in range(6):
        a = math.radians(-90 + 60 * i + 30)
        pts.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    for x, y in pts:
        o.append(f'<path d="M{f(cx)} {f(cy)} L {f(x)} {f(y)}" stroke="{GOLD}" stroke-width="1.4" stroke-dasharray="4 4"></path>')
    o.append(halo(cx, cy, R0 * 2.4, "#FFE680", 0.45) + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R0)}" fill="#FFF4C2" stroke="{GOLD}" stroke-width="3"></circle>'
             + halo(cx, cy, R0 * 0.8, "#FFFFFF", 0.95)
             + lab(cx, cy - 6, "ONE GOD AND", "#12113A", 9.5, halo_="#FFF4C2") + lab(cx, cy + 8, "FATHER OF ALL", "#12113A", 9.5, halo_="#FFF4C2"))
    k = r / 34
    for (nm, em), (x, y) in zip(items, pts):
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="#163A56" stroke="{CY}" stroke-width="2.4"></circle>'
                 f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r - 5)}" fill="none" stroke="{GOLD}" stroke-width="1"></circle>')
        if em == "body": o.append(mk.person("so", round(x), round(y + 22 * k), round(k * 0.22, 3), body="#1E4A6A", cloth="#24506E", kind="Tunic", stroke=CY, sw=6))
        elif em == "dove": o.append(halo(x, y, r * 0.7, "#FFF4C2", 0.4) + dove(x - 12 * k, y + 10 * k, 0.55 * k))
        elif em == "anchor": o.append(_anchor(x, y, k * 0.8, CY))
        elif em == "crown": o.append(_crown(x, y, k * 0.8, GOLD))
        elif em == "shield": o.append(_shield_icon(x, y, k * 0.8, CY))
        else: o.append(_water(x, y, k * 0.8, CY))
        o.append(lab(x, y + r + 16, nm, GOLD, 10))
    o.append(lab(w * 0.5, h - 10, "WHO IS OVER ALL, AND THROUGH ALL, AND IN ALL", CY, 9))
    return "".join(o)

def _fetter(x, y, s, rot=0):
    """A broken fetter lying on the road: two iron cuffs and the chain snapped between them."""
    o = [f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(s)})">']
    for cx_ in (-26, 26):
        o.append(f'<ellipse cx="{cx_}" cy="0" rx="11" ry="6" fill="none" stroke="{INK}" stroke-width="6"></ellipse><ellipse cx="{cx_}" cy="0" rx="11" ry="6" fill="none" stroke="#8A8A94" stroke-width="3"></ellipse>')
    for k, cx_ in enumerate((-12, -4, 8, 15)):
        o.append(f'<ellipse cx="{cx_}" cy="{(k % 2) * 2}" rx="4.5" ry="2.4" fill="none" stroke="#8A8A94" stroke-width="2"></ellipse>')
    o.append('<path d="M1 -4 L 4 4" stroke="#FFE680" stroke-width="2"></path></g>')
    return "".join(o)

def captivity(p, w, h, seed):
    """When he ascended on high, he led captivity captive, and gave gifts unto men: a triumph of light — a road of light
    climbing from the earth up through the clouds into the light above (no figure on it), the fetters lying broken along
    its foot, and at the right the people below, their hands lifted, the gifts falling to them like sparks of light."""
    b = h * 0.95
    o = [_defs(p), sky(w, h, "#2A1E5A", "#5A3A6A"), starfield(w, h, seed, 40, 0.5)]
    o.append(halo(w * 0.42, -h * 0.05, max(w, h) * 0.7, "#FFE680", 0.55) + rays(w * 0.42, -h * 0.05, 30, h * 0.1, max(w, h) * 1.2, "#FFF4C2", 0.2, 5))
    o.append(hills(w, h, h * 0.66, seed, color="#3A2A4A", amp=14, step=90) + ground(w, h, h * 0.78, "#4A3A4A", dy=0))
    road = (f'M{f(w * 0.06)} {f(h + 10)} C {f(w * 0.2)} {f(h * 0.7)} {f(w * 0.3)} {f(h * 0.4)} {f(w * 0.4)} {f(-10)} '
            f'L {f(w * 0.45)} {f(-10)} C {f(w * 0.4)} {f(h * 0.4)} {f(w * 0.36)} {f(h * 0.7)} {f(w * 0.34)} {f(h + 10)} Z')
    o.append(f'<defs><linearGradient id="{p}rd" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#FFC14D" stop-opacity="0.5"></stop><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.95"></stop></linearGradient></defs>'
             f'<path d="{road}" fill="url(#{p}rd)" stroke="#FFE680" stroke-width="2"></path>')
    r = random.Random(seed)
    for i in range(5):
        y = h * (0.12 + 0.12 * i)
        o.append(f'<ellipse cx="{f(w * r.uniform(0.1, 0.9))}" cy="{f(y)}" rx="{f(w * 0.16)}" ry="{f(h * 0.03)}" fill="#FFF4D8" opacity="0.3"></ellipse>')
    for (fx, fy, rot) in ((0.12, 0.9, -10), (0.26, 0.94, 14), (0.4, 0.88, -4)):
        o.append(_fetter(w * fx, h * fy, max(0.8, h / 300), rot))
    s = fit(b, max(h * 0.5, b - 140))
    for i in range(5):
        x = w * (0.62 + 0.08 * i)
        o.append(robed(p, x, b, s * (0.96 - 0.02 * i), ("#6A4A3A", "#3A4A6A", "#5A6A3A", "#4A3A5A", "#6A5A4A")[i], woman=i == 2,
                       veil="#2A3A5A" if i == 2 else None, head=None if i == 2 else ("#E8E2D6", "#2A3A4A", None, "#3A3A4A", None)[i],
                       hair="#2A1A10" if i in (2, 4) else None, flip=True, up=[(-22, -158), (-30, -182), (-28, -208)]))
    for _ in range(26):
        x = r.uniform(w * 0.5, w * 0.98); y = r.uniform(h * 0.1, h * 0.6)
        o.append(f'<path d="M{f(x)} {f(y - 6)} L {f(x + 2)} {f(y - 1)} L {f(x + 7)} {f(y)} L {f(x + 2)} {f(y + 1)} L {f(x)} {f(y + 6)} L {f(x - 2)} {f(y + 1)} L {f(x - 7)} {f(y)} L {f(x - 2)} {f(y - 1)} Z" fill="#FFF4C2" opacity="{r.uniform(0.5, 1):.2f}"></path>')
    return "".join(o)

def gifts(w, h):
    """He gave some to be apostles; and some, prophets; and some, evangelists; and some, pastors and teachers: a plate — the
    four gifts as figures in outline, each with its sign (the apostle's staff for the road, the prophet's scroll, the
    evangelist's hand lifted, the pastor's crook and the teacher's tablet), their lines running to one bar, the building up
    of the body; at the right a measuring rod from a child to a fullgrown man."""
    o = [plate_bg(w, h, "EPHESIANS 4:11–13 · THE GIFTS · THE BUILDING UP OF THE BODY"), mk.defs("gf", *ALL)]
    top = 34; H = h - top
    base = top + H * 0.72; s = (H * 0.5) / 205
    names = [("APOSTLES",), ("PROPHETS",), ("EVANGELISTS",), ("PASTORS AND", "TEACHERS")]
    xs = [w * (0.1 + 0.155 * i) for i in range(4)]
    staff = '<path d="M30 -2 L 34 -190" stroke="#8FD0E2" stroke-width="3"></path>'
    scroll_ = '<rect x="-62" y="-196" width="14" height="40" fill="#163A56" stroke="#8FD0E2" stroke-width="2.4"></rect>'
    crook = '<path d="M32 -2 L 32 -170 C 32 -196 54 -196 54 -176" fill="none" stroke="#8FD0E2" stroke-width="3"></path>'
    for i, x in enumerate(xs):
        up = [(-22, -158), (-40, -170), (-54, -186)] if i in (1, 2) else None
        ex = (staff, scroll_, "", crook)[i]
        o.append(mk.person("gf", round(x), round(base), round(s, 3), body="#1E4A6A", cloth="#24506E", kind="Tunic", stroke=CY, sw=2.4, up=up,
                           extra=ex + (A_head(i))))
        for j, ln in enumerate(names[i]):
            o.append(lab(x, base + 18 + j * 13, ln, CY, 9))
    by = top + 22
    o.append(f'<rect x="{f(w * 0.04)}" y="{f(by - 13)}" width="{f(w * 0.6)}" height="20" fill="{GOLD}" opacity="0.9"></rect>'
             + lab(w * 0.34, by + 1, "FOR THE PERFECTING OF THE SAINTS · THE BUILDING UP OF THE BODY", "#12113A", 8.5, halo_=GOLD))
    for x in xs:
        o.append(f'<path d="M{f(x)} {f(base - 215 * s)} L {f(x)} {f(by + 9)}" stroke="{GOLD}" stroke-width="1.2" stroke-dasharray="4 4"></path>')
    # the measuring rod
    rx = w * 0.8
    o.append(f'<rect x="{f(rx - 5)}" y="{f(base - 220 * s)}" width="10" height="{f(220 * s)}" fill="#163A56" stroke="{GOLD}" stroke-width="1.6"></rect>'
             + "".join(f'<path d="M{f(rx - 5)} {f(base - k * 22 * s)} l {f(-8 if k % 5 == 0 else -4)} 0" stroke="{GOLD}" stroke-width="1.2"></path>' for k in range(11)))
    o.append(mk.person("gf", round(rx - 40), round(base), round(s * 0.55, 3), body="#1E4A6A", cloth="#24506E", kind="Tunic", stroke=CY, sw=2.4, flip=True)
             + mk.person("gf", round(rx + 36), round(base), round(s, 3), body="#1E4A6A", cloth="#24506E", kind="Tunic", stroke=GOLD, sw=2.4))
    o.append(lab(rx, base + 18, "UNTO A FULLGROWN MAN", GOLD, 9) + lab(rx, base + 31, "THE MEASURE OF THE STATURE", CY, 8)
             + lab(rx, base + 43, "OF THE FULNESS OF CHRIST", CY, 8)
             + lab(rx, top + 22, "TILL WE ALL ATTAIN", GOLD, 9))
    return "".join(o)

def A_head(i):
    """The gift-bearers' headcloths, in outline (the evangelist bareheaded)."""
    if i == 2: return ""
    return headcloth("#163A56", cord=None).replace('stroke="#0D0D0F"', f'stroke="{CY}"')

def tossed(w, h, seed):
    """No longer children, tossed to and fro and carried about with every wind of doctrine: a little boat heeled over on a
    grey storm sea, its sail torn and flogging, the wind driving the spray, the clouds low (no one drawn in the storm)."""
    o = [sky(w, h, "#2A3040", "#6A7480")]
    r = random.Random(seed)
    for i in range(5):
        y = h * (0.05 + 0.1 * i)
        for _ in range(4):
            cx = r.uniform(-0.2, 1.2) * w; rw = w * r.uniform(0.2, 0.4)
            o.append(f'<path d="M{f(cx - rw)} {f(y + 12)} C {f(cx - rw * 0.5)} {f(y - 16)} {f(cx + rw * 0.3)} {f(y - 22)} {f(cx + rw)} {f(y + 10)} Z" fill="{r.choice(("#3A4050", "#4A5060", "#30363F"))}" opacity="0.9"></path>')
    for _ in range(14):
        y = r.uniform(0.1, 0.7) * h; x = r.uniform(-0.1, 0.9) * w
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x + 40)} {f(y - 4)} {f(x + 90)} {f(y + 6)} {f(x + 160)} {f(y + 2)}" fill="none" stroke="#C8D0D8" stroke-width="1.6" opacity="0.55"></path>')
    sy = h * 0.6
    bx, by = w * 0.5, sy - h * 0.03
    k = min(w / 702, h / 300) * 1.1
    o.append(f'<g transform="translate({f(bx)} {f(by)}) rotate(-18) scale({f(k)})">'
             '<path d="M-90 -10 L 90 -10 C 84 14 60 26 0 26 C -60 26 -84 14 -90 -10 Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="3"></path>'
             '<path d="M-86 -2 L 86 -2" stroke="#4A3018" stroke-width="2"></path>'
             '<path d="M0 -10 L 0 -150" stroke="#0D0D0F" stroke-width="6"></path><path d="M0 -10 L 0 -150" stroke="#8A6A3A" stroke-width="3"></path>'
             '<path d="M4 -144 C 40 -130 60 -110 70 -84 L 46 -70 L 60 -52 L 4 -40 Z" fill="#D8CDB8" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<path d="M70 -84 C 86 -90 100 -86 112 -96 M60 -52 C 80 -50 96 -60 110 -56" fill="none" stroke="#D8CDB8" stroke-width="3"></path></g>')
    o.append(waves(w, h, sy, seed, amp=h * 0.08))
    for _ in range(20):
        x = r.uniform(0.2, 0.9) * w; y = r.uniform(0.4, 0.62) * h
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(1.4, 3.2))}" fill="#E8F6FA" opacity="0.8"></circle>')
    return "".join(o)

def body_plate(w, h):
    """From whom all the body fitly framed and knit together through that which every joint supplieth: a plate — a body
    drawn in outline, its joints marked (shoulders, elbows, wrists, hips, knees, ankles) and the bands between them drawn
    in, under a disc of light marked "the head, even Christ" (no face, no figure of Christ)."""
    o = [plate_bg(w, h, "EPHESIANS 4:15–16 · THE BODY FITLY FRAMED AND KNIT TOGETHER"), mk.defs("bd", *ALL)]
    top = 34; H = h - top
    base = h - 18; s = (H - 70) / 205
    cx = w * 0.5
    X = lambda u: cx + u * s; Y = lambda v: base + v * s
    o.append(mk.person("bd", round(cx), round(base), round(s, 3), body="#163A56", cloth=None, stroke=CY, sw=2.0 / max(s, 0.5) * 1.2))
    o.append(halo(X(0), Y(-188), 46 * s, "#FFE680", 0.6) + f'<circle cx="{f(X(0))}" cy="{f(Y(-188))}" r="{f(16 * s)}" fill="#FFF4C2" stroke="{GOLD}" stroke-width="2.4"></circle>')
    joints = [(-24, -160), (24, -160), (-30, -124), (30, -124), (-29, -96), (29, -96), (-11, -96), (11, -96), (-10, -52), (10, -52), (-10, -12), (10, -12), (0, -168)]
    bands = [(0, 1), (0, 2), (2, 4), (1, 3), (3, 5), (6, 7), (6, 8), (8, 10), (7, 9), (9, 11), (0, 6), (1, 7), (12, 0), (12, 1)]
    for a, b_ in bands:
        o.append(f'<path d="M{f(X(joints[a][0]))} {f(Y(joints[a][1]))} L {f(X(joints[b_][0]))} {f(Y(joints[b_][1]))}" stroke="{CY}" stroke-width="1.6" stroke-dasharray="5 3"></path>')
    for u, v in joints:
        o.append(f'<circle cx="{f(X(u))}" cy="{f(Y(v))}" r="{f(max(3.5, 4 * s))}" fill="{GOLD}" stroke="{INK}" stroke-width="1.2"></circle>')
    lx, rx = w * 0.05, w * 0.95
    o.append(f'<path d="M{f(X(14))} {f(Y(-190))} L {f(rx - 150)} {f(Y(-190))}" stroke="{GOLD}" stroke-width="1.2"></path>'
             + lab(rx, Y(-194), "THE HEAD · EVEN CHRIST", GOLD, 10, "end") + lab(rx, Y(-180), "FROM WHOM ALL THE BODY", CY, 8, "end"))
    o.append(callout(X(-30), Y(-124), lx, Y(-140), [("EVERY JOINT SUPPLIETH", GOLD, 9)])
             + callout(X(-10), Y(-75), lx, Y(-80), [("KNIT TOGETHER", CY, 9)])
             + callout(X(24), Y(-142), rx, Y(-130), [("EACH SEVERAL PART", CY, 9)])
             + callout(X(10), Y(-32), rx, Y(-56), [("MAKETH THE INCREASE", CY, 9), ("UNTO THE BUILDING UP", CY, 8), ("OF ITSELF IN LOVE", CY, 8)]))
    return "".join(o)

def ephesus_night(w, h, seed):
    """Walk not as the Gentiles walk, in the vanity of their mind: a street of Ephesus by night, every door shut and every
    window dark, and far off on the plain the temple of Diana lit red by its torches — no one in the street."""
    o = [sky(w, h, "#05050E", "#2A1428"), mk.stars(20, w, h * 0.3, seed)]
    o.append(diana_temple(w * 0.5, h * 0.6, w * 0.34).replace("#F8F4EC", "#7A5058").replace("#F3EFE6", "#6A4048").replace("#D8D0C0", "#5A3840").replace("#E8E0D0", "#604048"))
    o.append(halo(w * 0.5, h * 0.52, h * 0.25, "#D7261E", 0.3))
    for tx in (w * 0.35, w * 0.65):
        o.append(f'<circle cx="{f(tx)}" cy="{f(h * 0.5)}" r="4" fill="#FF8A3A"></circle>' + halo(tx, h * 0.5, 16, "#FF8A3A", 0.5))
    o.append(houses(w, h, h * 0.8, seed, x1=w * 0.32, hmin=0.3, hmax=0.44, shut=True, color=("#4A4250", "#3E3848", "#544C5A"))
             + houses(w, h, h * 0.8, seed + 3, x0=w * 0.7, hmin=0.3, hmax=0.44, shut=True, color=("#4A4250", "#3E3848", "#544C5A"))
             + pavement(w, h, h * 0.8, color="#2E2834", line="#3E3644"))
    return "".join(o)

def _garment(x, y, s, fill, line, torn=False):
    """A plain robe laid out flat (a T-shaped tunic with long sleeves), (x, y) the middle of its neck."""
    d = "M-14 0 L -60 10 L -96 50 L -84 66 L -50 42 L -46 180 L 46 180 L 50 42 L 84 66 L 96 50 L 60 10 L 14 0 C 8 10 -8 10 -14 0 Z"
    if torn: d = "M-14 0 L -60 10 L -96 50 L -84 66 L -50 42 L -48 120 L -40 132 L -46 150 L -34 180 L 10 172 L 22 182 L 46 180 L 44 140 L 52 128 L 50 42 L 84 66 L 92 56 L 80 44 L 60 10 L 14 0 C 8 10 -8 10 -14 0 Z"
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="{d}" fill="{fill}" stroke="{line}" stroke-width="3"></path>'
         f'<path d="M0 10 L 0 176 M-46 150 L 46 150" stroke="{line}" stroke-width="1.4" opacity="0.5" fill="none"></path>']
    if torn:
        o += [f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#2A2420" opacity="0.6"></ellipse>' for cx, cy, rx, ry in ((-20, 70, 14, 9), (24, 110, 10, 7), (-30, 150, 9, 6))]
    return "".join(o) + "</g>"

def garments(w, h):
    """Put away … the old man, that waxeth corrupt … and put on the new man: a plate of two garments laid out — at the left
    the old robe, worn and torn and stained, dark; at the right the new robe, white, edged in gold light; an arrow between
    them, renewed in the spirit of your mind."""
    o = [plate_bg(w, h, "EPHESIANS 4:22–24 · PUT AWAY · PUT ON")]
    top = 34; H = h - top
    s = (H - 86) / 190
    o.append(lab(w * 0.26, top + 22, "THE OLD MAN · PUT AWAY", "#A8A8B0", 10) + lab(w * 0.74, top + 22, "THE NEW MAN · PUT ON", GOLD, 10))
    o.append(_garment(w * 0.26, top + 40, s, "#4A4440", "#8A847A", torn=True))
    o.append(halo(w * 0.74, top + 40 + 90 * s, 120 * s, "#FFE680", 0.4) + _garment(w * 0.74, top + 40, s, "#F8F4EA", GOLD))
    o.append(f'<path d="M{f(w * 0.43)} {f(top + H * 0.55)} L {f(w * 0.57)} {f(top + H * 0.55)}" stroke="{CY}" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.57)} {f(top + H * 0.55)} l -12 -7 l 0 14 Z" fill="{CY}"></path>'
             + lab(w * 0.5, top + H * 0.55 - 12, "RENEWED", CY, 9) + lab(w * 0.5, top + H * 0.55 + 20, "IN THE SPIRIT", CY, 8) + lab(w * 0.5, top + H * 0.55 + 32, "OF YOUR MIND", CY, 8))
    o.append(lab(w * 0.26, h - 30, "WAXETH CORRUPT · THE LUSTS OF DECEIT", "#A8A8B0", 8) + lab(w * 0.74, h - 30, "RIGHTEOUSNESS AND HOLINESS OF TRUTH", GOLD, 8))
    return "".join(o)

def sundown(w, h, seed):
    """Let not the sun go down upon your wrath: the sun going down into the sea beyond the harbour of Ephesus, the hills
    dark against it, the roofs below, a ship at anchor."""
    o = [sky(w, h, "#2A1E4A", "#FF9A4A")]
    sy = h * 0.66
    o.append(halo(w * 0.6, sy, h * 0.6, "#FFD08A", 0.5) + f'<circle cx="{f(w * 0.6)}" cy="{f(sy)}" r="{f(h * 0.12)}" fill="#FFE6A0"></circle>')
    o.append(sea(w, h, sy, seed, color="#6A4A6A", deep="#3A2A4A"))
    r = random.Random(seed)
    for i in range(8):
        y = sy + 8 + i * (h - sy) / 9
        o.append(f'<path d="M{f(w * 0.6 - h * 0.1 + i * 4)} {f(y)} L {f(w * 0.6 + h * 0.1 - i * 4)} {f(y)}" stroke="#FFE6A0" stroke-width="3" opacity="{0.8 - i * 0.08:.2f}"></path>')
    o.append(f'<path d="M-10 {f(sy + 4)} L -10 {f(h * 0.4)} C {f(w * 0.1)} {f(h * 0.36)} {f(w * 0.24)} {f(h * 0.44)} {f(w * 0.34)} {f(sy + 4)} Z" fill="#2A1A2E" stroke="{INK}" stroke-width="2"></path>'
             + houses(w, h, h * 0.94, seed, x1=w * 0.36, hmin=0.14, hmax=0.24, lit=True, color=("#3A2A3A", "#443040", "#2E2234"))
             + ship(w * 0.84, sy + h * 0.04, max(0.35, h / 700)))
    return "".join(o)

def ship(x, y, s):
    from kg1.art import ship as _ship
    return _ship(x, y, s)

# ---- Ephesians 5 ----------------------------------------------------------------------------------------------------------
def sweet_smell(w, h, seed):
    """An offering and a sacrifice to God for an odor of a sweet smell: the golden altar of incense in the dark of the house,
    its cloud rising in a column into the light that falls from above (no figure)."""
    b = h * 0.92
    o = [sky(w, h, "#1A1028", "#3A2418"), halo(w * 0.5, -h * 0.1, h * 0.9, "#FFE680", 0.45), rays(w * 0.5, -h * 0.1, 20, h * 0.1, h * 1.1, "#FFF4C2", 0.18, 6, 50, 130)]
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h - b + 10)}" fill="#2A1A12" stroke="{INK}" stroke-width="2"></rect>')
    k = (b - h * 0.12) / 300
    r = random.Random(seed)
    for i in range(12):
        y = b - 120 * k - i * (b - 140 * k) / 12
        o.append(f'<ellipse cx="{f(w * 0.5 + r.uniform(-20, 20) * k + math.sin(i) * 14 * k)}" cy="{f(y)}" rx="{f((24 + i * 6) * k)}" ry="{f((14 + i * 3) * k)}" fill="#F3ECF8" opacity="{max(0.08, 0.5 - i * 0.035):.2f}"></ellipse>')
    o.append(incense_altar(w * 0.5, b, k * 1.4, seed, smoke_=False))
    return "".join(o)

def children_light(p, w, h, seed):
    """Walk as children of light: a road through the fields at sunrise, a man, a woman and a boy walking along it toward the
    sun, their long shadows behind them."""
    b = h * 0.9
    o = [_defs(p), sky(w, h, "#8FD0E2", "#FFE6A0"), halo(w * 0.86, h * 0.5, h * 0.7, "#FFF4C2", 0.6),
         f'<circle cx="{f(w * 0.86)}" cy="{f(h * 0.5)}" r="{f(h * 0.08)}" fill="#FFFFFF"></circle>', rays(w * 0.86, h * 0.5, 24, h * 0.1, w, "#FFF4C2", 0.25, 4),
         hills(w, h, h * 0.56, seed, color="#9AAA7A", amp=10, step=90), ground(w, h, h * 0.62, "#C8C07A", dy=0),
         f'<path d="M-10 {f(b + 14)} C {f(w * 0.3)} {f(b)} {f(w * 0.6)} {f(h * 0.7)} {f(w * 0.9)} {f(h * 0.62)} L {f(w * 0.96)} {f(h * 0.62)} C {f(w * 0.7)} {f(h * 0.74)} {f(w * 0.4)} {f(h + 10)} {f(w * 0.1)} {f(h + 10)} Z" fill="#E8D8A8" stroke="{INK}" stroke-width="1.6"></path>']
    s = fit(b, max(h * 0.4, b - 190))
    people = [(0.3, lambda x, k: robed(p, x, b, k, "#3A5A7A", head="#E8E2D6", cord="#5A4A3A", beard="#4A3A2A", mantle="#2A4A6A", flip=True, pose="walk")),
              (0.43, lambda x, k: robed(p, x, b, k * 0.94, "#6A5A7A", woman=True, veil="#2A3A5A", flip=True, pose="walk")),
              (0.54, lambda x, k: robed(p, x, b, k * 0.66, "#C8A060", hair="#2A1A10", belt="#6A4A2A", flip=True, pose="walk"))]
    for fx, fn in people:
        x = w * fx
        o.append(f'<ellipse cx="{f(x - 70 * s)}" cy="{f(b)}" rx="{f(80 * s)}" ry="{f(6 * s)}" fill="#6A5A3A" opacity="0.35"></ellipse>' + fn(x, s))
    return "".join(o)

def awake(p, w, h, seed):
    """Awake, thou that sleepest, and arise from the dead, and Christ shall shine upon thee: a dark room, a sleeper lying
    on his mat under his cloak, and the door flung open on the dawn, a shaft of light falling across the floor onto him."""
    b = h * 0.78
    o = [_defs(p), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#14101E"></rect>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h - b + 10)}" fill="#1E1824" stroke="{INK}" stroke-width="2"></rect>']
    dx, dw, dt = w * 0.74, w * 0.14, h * 0.18
    o.append(f'<defs><linearGradient id="{p}dw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFB07A"></stop><stop offset="1" stop-color="#FFF4C2"></stop></linearGradient>'
             f'<linearGradient id="{p}sh" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#FFF4C2" stop-opacity="0.85"></stop><stop offset="1" stop-color="#FFE6A0" stop-opacity="0.15"></stop></linearGradient></defs>'
             f'<rect x="{f(dx)}" y="{f(dt)}" width="{f(dw)}" height="{f(b - dt)}" fill="url(#{p}dw)" stroke="{INK}" stroke-width="3"></rect>'
             f'<circle cx="{f(dx + dw * 0.5)}" cy="{f(b - (b - dt) * 0.3)}" r="{f(dw * 0.22)}" fill="#FFFFFF"></circle>'
             f'<path d="M{f(dx)} {f(dt)} L {f(dx - dw * 0.9)} {f(dt + (b - dt) * 0.2)} L {f(dx - dw * 0.9)} {f(b + (b - dt) * 0.08)} L {f(dx)} {f(b)} Z" fill="#3A2A20" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(dx)} {f(b)} L {f(dx + dw)} {f(b)} L {f(w * 0.02)} {f(h + 10)} L {f(w * 0.02)} {f(b + 2)} Z" fill="url(#{p}sh)"></path>'
             f'<path d="M{f(dx + dw)} {f(dt)} L {f(w * 0.18)} {f(b)} L {f(dx)} {f(b)} Z" fill="#FFF4C2" opacity="0.18"></path>')
    s = min(w * 0.42 / 215, h * 0.9 / 205); ly = h * 0.9
    mx = w * 0.12
    o.append(floor_mat(mx, ly + 2, 225 * s, s, color="#5A4A3A"))
    o.append(f'<g transform="translate({f(mx + 200 * s)} {f(ly - 4)}) scale({f(s)})" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB" fill="#5A5A6A"></use>'
             f'<use href="#{p}LieA" fill="#5A5A6A"></use>'
             f'<path d="M-96 -6 C -60 -20 -10 -20 22 -10 L 22 8 L -96 8 Z" fill="#3A4A6A" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<circle cx="-180" cy="-14" r="12.5" fill="{SKIN}"></circle><path d="M-192 -18 C -192 -30 -176 -32 -170 -24 C -178 -22 -184 -18 -190 -10 Z" fill="#2A1A10"></path></g>')
    return "".join(o)

def _lyre(x, y, s):
    """A lyre: the sound box below, two curved arms, the crossbar, seven strings; (x, y) the foot of the sound box."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-20 0 C -24 -14 -22 -26 -16 -30 L 16 -30 C 22 -26 24 -14 20 0 Z" fill="#8A5A2A" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M-14 -30 C -26 -50 -30 -70 -18 -86 M14 -30 C 26 -50 30 -70 18 -86" fill="none" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path>'
            '<path d="M-14 -30 C -26 -50 -30 -70 -18 -86 M14 -30 C 26 -50 30 -70 18 -86" fill="none" stroke="#C8963E" stroke-width="4" stroke-linecap="round"></path>'
            '<path d="M-24 -80 L 24 -80" stroke="#0D0D0F" stroke-width="5" stroke-linecap="round"></path><path d="M-24 -80 L 24 -80" stroke="#C8963E" stroke-width="2.6"></path>'
            + "".join(f'<path d="M{-9 + i * 3} -80 L {-9 + i * 3} -12" stroke="#F3EFE6" stroke-width="0.9"></path>' for i in range(7)) + '</g>')

def hymns(p, w, h, seed):
    """Speaking one to another in psalms and hymns and spiritual songs: brethren gathered in a room by lamplight, one sitting
    on a stool with a lyre on his knee, the others standing about him singing, the roll of the psalms open on the table."""
    b = h * 0.95
    s = (h * 0.68) / 205
    o = [_defs(p), room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * 0.5, b - 90 * s, max(w, h) * 0.6, f"{p}g", op=0.5)]
    o.append(low_table(w * 0.46, b, 60 * s, s) + clay_lamp(w * 0.46 + 14 * s, b - 31 * s, s * 0.5)
             + f'<rect x="{f(w * 0.46 + 26 * s)}" y="{f(b - 36 * s)}" width="{f(30 * s)}" height="{f(6 * s)}" fill="#EADBB4" stroke="{INK}" stroke-width="1.4"></rect>')
    sx = w * 0.3
    o.append(robed(p, sx, b, s, "#3A5A5A", head="#E8E2D6", cord="#5A4A3A", beard="#3A2A1A", flip=True, pose="sit", up=[(-22, -158), (-40, -134), (-50, -120)]))
    o.append(_lyre(sx + 52 * s, b - 52 * s, s * 0.9))
    looks = [(0.1, dict(cloth="#4A5A6A", head="#2A3A4A", beard="#2A1A10")), (0.6, dict(cloth="#6A5A7A", woman=True, veil="#2A3A5A")),
             (0.72, dict(cloth="#5A4A3A", hair="#1A1210", beard="#1A1210")), (0.86, dict(cloth="#3A4A3A", head="#F3EFE6", beard="#B8B2A8"))]
    for fx, lk in looks:
        lk = dict(lk); wm = lk.pop("woman", False)
        o.append(robed(p, w * fx, b, s * (0.94 if wm else 1), lk.pop("cloth"), woman=wm, flip=fx > 0.4, **lk))
    r = random.Random(seed)
    for _ in range(5):
        x = w * r.uniform(0.35, 0.65); y = b - r.uniform(120, 190) * s
        o.append(f'<path d="M{f(x)} {f(y)} l 0 {f(-14 * s)} l {f(8 * s)} {f(-3 * s)}" stroke="#FFE6A0" stroke-width="{f(2 * s)}" fill="none" opacity="0.7"></path>'
                 f'<ellipse cx="{f(x - 3 * s)}" cy="{f(y)}" rx="{f(3.4 * s)}" ry="{f(2.6 * s)}" fill="#FFE6A0" opacity="0.7"></ellipse>')
    return "".join(o)

def household(p, w, h, seed):
    """Wives … husbands: a plain household by day — the door of a house in its court, the husband come in from the field with
    his mattock on his shoulder, the wife standing at the door with the water jar; an olive tree, the bread oven."""
    b = h * 0.93
    o = [_defs(p), sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.86, h * 0.14, 14, op=0.3)]
    o.append(f'<rect x="{f(w * 0.48)}" y="{f(h * 0.2)}" width="{f(w * 0.5)}" height="{f(b - h * 0.2)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.46)}" y="{f(h * 0.16)}" width="{f(w * 0.54)}" height="{f(h * 0.05)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>')
    dx, dw = w * 0.62, w * 0.12
    o.append(f'<path d="M{f(dx)} {f(b)} L {f(dx)} {f(b - h * 0.42)} C {f(dx)} {f(b - h * 0.5)} {f(dx + dw)} {f(b - h * 0.5)} {f(dx + dw)} {f(b - h * 0.42)} L {f(dx + dw)} {f(b)} Z" fill="#3A2A1E" stroke="{INK}" stroke-width="2"></path>'
             f'<rect x="{f(w * 0.86)}" y="{f(h * 0.34)}" width="{f(w * 0.06)}" height="{f(h * 0.1)}" fill="#3A2A1E" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(ground(w, h, b, "#C8B07A", dy=0) + olive(w * 0.14, b, min(1.2, h / 260), seed))
    o.append(f'<path d="M{f(w * 0.3)} {f(b)} C {f(w * 0.3)} {f(b - 40)} {f(w * 0.4)} {f(b - 40)} {f(w * 0.4)} {f(b)} Z" fill="#B8784A" stroke="{INK}" stroke-width="2"></path>')
    s = min(h * 0.58, 330) / 205
    jar = '<path d="M-46 -172 C -58 -172 -60 -150 -50 -142 L -40 -142 C -30 -150 -32 -172 -46 -172 Z" fill="#B8683A" stroke="#0D0D0F" stroke-width="2"></path>'
    basket = '<path d="M-52 -196 L -14 -196 L -20 -176 L -46 -176 Z" fill="#B8904A" stroke="#0D0D0F" stroke-width="2"></path><path d="M-50 -188 L -16 -188" stroke="#7A5A2A" stroke-width="1.4"></path>'
    o.append(robed(p, w * 0.46, b, s, "#5A6A4A", head="#E8E2D6", cord="#6A5A3A", beard="#3A2A1A", belt="#3A2A1A", flip=True,
                   up=[(-22, -158), (-36, -168), (-32, -178)], extra=basket))
    o.append(robed(p, w * 0.8, b, s * 0.94, "#6A4A6A", woman=True, veil="#2A3A5A", up=[(-22, -158), (-38, -164), (-44, -150)], extra=jar))
    return "".join(o)

def bridal(w, h, seed):
    """This mystery is great: but I speak in regard of Christ and of the church — an emblem on gold: a bride's veil of white
    lace hanging empty from a wreath, and beside it a clay lamp burning on its stand (no bride's figure)."""
    o = [f'<defs><radialGradient id="br{seed}" cx="0.5" cy="0.45" r="0.7"><stop offset="0" stop-color="#FFF4D8"></stop><stop offset="0.6" stop-color="#E8C878"></stop>'
         f'<stop offset="1" stop-color="#8A5A2A"></stop></radialGradient></defs><rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#br{seed})"></rect>',
         f'<rect x="12" y="12" width="{f(w - 24)}" height="{f(h - 24)}" fill="none" stroke="#7A4A2A" stroke-width="2"></rect>'
         f'<rect x="20" y="20" width="{f(w - 40)}" height="{f(h - 40)}" fill="none" stroke="#C8963E" stroke-width="1.2"></rect>']
    k = (h - 60) / 260
    vx, vy = w * 0.4, 40
    leaves = "".join(f'<ellipse cx="{f(vx + math.cos(math.radians(a)) * 40 * k)}" cy="{f(vy + 20 * k + math.sin(math.radians(a)) * 12 * k)}" rx="{f(9 * k)}" ry="{f(4 * k)}" '
                     f'transform="rotate({a + 90} {f(vx + math.cos(math.radians(a)) * 40 * k)} {f(vy + 20 * k + math.sin(math.radians(a)) * 12 * k)})" fill="#4E7A3A" stroke="#1E3A1E" stroke-width="1"></ellipse>' for a in range(0, 360, 24))
    veil = (f'<path d="M{f(vx - 40 * k)} {f(vy + 22 * k)} C {f(vx - 70 * k)} {f(vy + 100 * k)} {f(vx - 96 * k)} {f(vy + 170 * k)} {f(vx - 104 * k)} {f(vy + 230 * k)} '
            f'C {f(vx - 50 * k)} {f(vy + 240 * k)} {f(vx + 50 * k)} {f(vy + 240 * k)} {f(vx + 104 * k)} {f(vy + 230 * k)} C {f(vx + 96 * k)} {f(vy + 170 * k)} {f(vx + 70 * k)} {f(vy + 100 * k)} {f(vx + 40 * k)} {f(vy + 22 * k)} Z" '
            f'fill="#FFFFFF" opacity="0.85" stroke="#C8963E" stroke-width="2"></path>'
            + "".join(f'<path d="M{f(vx + dx * k)} {f(vy + 26 * k)} C {f(vx + dx * 1.6 * k)} {f(vy + 120 * k)} {f(vx + dx * 2.2 * k)} {f(vy + 180 * k)} {f(vx + dx * 2.5 * k)} {f(vy + 234 * k)}" fill="none" stroke="#E8DCC0" stroke-width="1.4"></path>' for dx in (-30, -12, 6, 24))
            + f'<path d="M{f(vx - 104 * k)} {f(vy + 230 * k)} C {f(vx - 50 * k)} {f(vy + 240 * k)} {f(vx + 50 * k)} {f(vy + 240 * k)} {f(vx + 104 * k)} {f(vy + 230 * k)}" fill="none" stroke="#E8B830" stroke-width="3"></path>')
    o.append(halo(vx, vy + 120 * k, 130 * k, "#FFFFFF", 0.35) + veil + leaves)
    lx, ly = w * 0.72, h - 40
    o.append(f'<path d="M{f(lx)} {f(ly)} L {f(lx)} {f(ly - 110 * k)}" stroke="#0D0D0F" stroke-width="{f(9 * k)}"></path><path d="M{f(lx)} {f(ly)} L {f(lx)} {f(ly - 110 * k)}" stroke="#8A5A2A" stroke-width="{f(5 * k)}"></path>'
             f'<path d="M{f(lx - 30 * k)} {f(ly)} L {f(lx + 30 * k)} {f(ly)} L {f(lx + 20 * k)} {f(ly - 10 * k)} L {f(lx - 20 * k)} {f(ly - 10 * k)} Z" fill="#6A3A1E" stroke="#0D0D0F" stroke-width="2"></path>'
             + halo(lx, ly - 140 * k, 80 * k, "#FFE680", 0.6) + clay_lamp(lx, ly - 112 * k, 1.6 * k))
    o.append(plate_label(w * 0.5, h - 26, "THE TWO SHALL BECOME ONE FLESH · CHRIST AND THE CHURCH", "#3A2010", 9, halo_="#F3E2B0"))
    return "".join(o)

# ---- Ephesians 6 ----------------------------------------------------------------------------------------------------------
def father_son(p, w, h, seed):
    """Children, obey your parents … ye fathers … nurture them in the chastening and admonition of the Lord: the court of a
    house by day, the father sitting on a stool with the roll open on his knee, his son standing before him listening, the
    mother and the little daughter at the door."""
    b = h * 0.93
    o = [_defs(p), sky(w, h, "#8FD0E2", "#F3E8C8"),
         f'<rect x="{f(w * 0.5)}" y="{f(h * 0.18)}" width="{f(w * 0.52)}" height="{f(b - h * 0.18)}" fill="#E0CFA8" stroke="{INK}" stroke-width="2.4"></rect>'
         f'<rect x="{f(w * 0.48)}" y="{f(h * 0.14)}" width="{f(w * 0.54)}" height="{f(h * 0.05)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>',
         ground(w, h, b, "#C8B07A", dy=0)]
    dx, dw = w * 0.72, w * 0.13
    o.append(f'<path d="M{f(dx)} {f(b)} L {f(dx)} {f(b - h * 0.44)} C {f(dx)} {f(b - h * 0.52)} {f(dx + dw)} {f(b - h * 0.52)} {f(dx + dw)} {f(b - h * 0.44)} L {f(dx + dw)} {f(b)} Z" fill="#3A2A1E" stroke="{INK}" stroke-width="2"></path>')
    s = min(h * 0.58, 330) / 205
    roll = f'<rect x="-66" y="-150" width="30" height="10" fill="#EADBB4" stroke="#0D0D0F" stroke-width="1.6"></rect>'
    o.append(robed(p, w * 0.22, b, s, "#3A4A6A", head="#2A3A4A", cord="#0D1430", beard="#3A2A1A", mantle="#2A3450", flip=True, pose="sit",
                   up=[(-22, -158), (-46, -150), (-58, -144)], extra=roll))
    o.append(robed(p, w * 0.44, b, s * 0.66, "#C8A060", hair="#2A1A10", belt="#6A4A2A"))
    o.append(robed(p, w * 0.66, b, s * 0.94, "#6A5A7A", woman=True, veil="#2A3A5A") + robed(p, w * 0.6, b, s * 0.56, "#8A6A8A", woman=True, veil="#E8E2D6"))
    return "".join(o)

def servant_master(p, w, h, seed):
    """Servants, be obedient … and, ye masters, do the same things unto them, and forbear threatening: the court of a house by
    day, a servant walking in with the water jar on his shoulder, his master at the door pointing the way to the cistern —
    a plain household, no rod, no blow."""
    b = h * 0.93
    o = [_defs(p), sky(w, h, "#8FD0E2", "#F3E8C8"),
         f'<rect x="{f(w * 0.56)}" y="{f(h * 0.16)}" width="{f(w * 0.46)}" height="{f(b - h * 0.16)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2.4"></rect>'
         f'<rect x="{f(w * 0.54)}" y="{f(h * 0.12)}" width="{f(w * 0.48)}" height="{f(h * 0.05)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>',
         ground(w, h, b, "#C8B07A", dy=0)]
    dx, dw = w * 0.76, w * 0.12
    o.append(f'<path d="M{f(dx)} {f(b)} L {f(dx)} {f(b - h * 0.44)} C {f(dx)} {f(b - h * 0.52)} {f(dx + dw)} {f(b - h * 0.52)} {f(dx + dw)} {f(b - h * 0.44)} L {f(dx + dw)} {f(b)} Z" fill="#3A2A1E" stroke="{INK}" stroke-width="2"></path>')
    cx_ = w * 0.44
    o.append(f'<ellipse cx="{f(cx_)}" cy="{f(b - 4)}" rx="{f(w * 0.06)}" ry="{f(h * 0.03)}" fill="#8A8A90" stroke="{INK}" stroke-width="2"></ellipse>'
             f'<ellipse cx="{f(cx_)}" cy="{f(b - 6)}" rx="{f(w * 0.045)}" ry="{f(h * 0.018)}" fill="#1F4A6A"></ellipse>')
    s = min(h * 0.58, 330) / 205
    jar = '<path d="M-40 -220 C -56 -220 -60 -196 -48 -186 L -34 -186 C -24 -196 -26 -220 -40 -220 Z" fill="#B8683A" stroke="#0D0D0F" stroke-width="2"></path>'
    o.append(robed(p, w * 0.2, b, s, "#8A7A5A", hair="#1A1210", beard="#2A1A10", belt="#5A3A1E", flip=True, pose="walk",
                   up=[(-22, -158), (-30, -186), (-38, -200)], extra=jar))
    o.append(robed(p, w * 0.68, b, s, "#5A2A4A", head="#F3EFE6", cord="#C8963E", beard="#5A4A3A", mantle="#2A3A5A", belt="#C8963E",
                   up=[(-22, -158), (-52, -152), (-80, -148)]))
    return "".join(o)

def two_faces(w, h, seed):
    """Finally, be strong in the Lord … put on the whole armor of God: Paul's face at the left, turned to the soldier he is
    chained to; the soldier's face at the right, in his helmet and red cloak, turned to Paul; between them, low in the
    panel, the chain (their wrists below the frame), the lamplight on the wall behind."""
    o = [f'<defs><radialGradient id="tf{seed}" cx="0.5" cy="0.4" r="0.8"><stop offset="0" stop-color="#FFC877"></stop><stop offset="0.5" stop-color="#A8603A"></stop>'
         f'<stop offset="1" stop-color="#3A2018"></stop></radialGradient></defs><rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#tf{seed})"></rect>']
    s = min(h / 390, w / 760)
    o.append(mk.face(PAUL_FACE, f(-30 * s), f(h - 380 * s + 4), round(s, 3)))
    o.append(mk.face(GUARD, f(w + 30 * s), f(h - 380 * s + 4), round(s, 3), flip=True))
    o.append(chain(w * 0.3, h - 20, w * 0.7, h - 20, s=max(1.2, s * 2.2), sag=0.12))
    return "".join(o)

def hosts_dark(w, h, seed):
    """Our wrestling is not against flesh and blood, but … against the spiritual hosts of wickedness in the heavenly places:
    darkness only — a night sky heaped with black cloud, rank behind rank of it, a cold glimmer at its edges, the roofs of
    the city far below with every light gone out (nothing drawn in the dark)."""
    o = [sky(w, h, "#020206", "#1A1222")]
    r = random.Random(seed)
    for i in range(8):
        y = h * (0.04 + 0.09 * i)
        for _ in range(6):
            cx = r.uniform(-0.2, 1.2) * w; rw = w * r.uniform(0.18, 0.36)
            o.append(f'<path d="M{f(cx - rw)} {f(y + 16)} C {f(cx - rw * 0.6)} {f(y - 20)} {f(cx + rw * 0.2)} {f(y - 28)} {f(cx + rw)} {f(y + 12)} Z" fill="{r.choice(("#0A0810", "#120E1A", "#1A1422", "#08060C"))}" '
                     f'stroke="#3A3448" stroke-width="1" opacity="0.95"></path>')
    o.append(houses(w, h, h * 1.0, seed, hmin=0.08, hmax=0.14, shut=True, stairs=False, color=("#0E0C14", "#121018", "#0A0810")))
    return "".join(o)

def _dart(x, y, ang, L, out=True):
    """A fiery dart: the shaft and its flight, the head struck into the shield; out=True the flame gone out (smoke)."""
    a = math.radians(ang); tx, ty = x + math.cos(a) * L, y + math.sin(a) * L
    o = [f'<path d="M{f(x)} {f(y)} L {f(tx)} {f(ty)}" stroke="#0D0D0F" stroke-width="4"></path><path d="M{f(x)} {f(y)} L {f(tx)} {f(ty)}" stroke="#C8A060" stroke-width="2"></path>',
         f'<path d="M{f(tx)} {f(ty)} l {f(math.cos(a + 0.5) * 12)} {f(math.sin(a + 0.5) * 12)} M{f(tx)} {f(ty)} l {f(math.cos(a - 0.5) * 12)} {f(math.sin(a - 0.5) * 12)}" stroke="#E8E2D6" stroke-width="3"></path>']
    if out: o.append("".join(f'<circle cx="{f(x + k * 5)}" cy="{f(y - k * 9)}" r="{f(3 + k * 2)}" fill="#C8C0C8" opacity="{0.55 - k * 0.12:.2f}"></circle>' for k in range(4)))
    else: o.append(f'<path d="M{f(x)} {f(y)} C {f(x - 6)} {f(y - 10)} {f(x + 2)} {f(y - 18)} {f(x + 4)} {f(y - 24)} C {f(x + 8)} {f(y - 14)} {f(x + 10)} {f(y - 6)} {f(x)} {f(y)} Z" fill="#FF8A2A" stroke="#D7261E" stroke-width="1.2"></path>')
    return "".join(o)

def armour_plate(p, w, h):
    """THE WHOLE ARMOR OF GOD (6:13–17): a technical plate — the Roman soldier at full height on the kit silhouette (as the
    guard Paul is chained to), his sword lifted in his hand and his shield before him, each piece called out to the margin
    with the words it is given: the loins girded with truth, the breastplate of righteousness, the feet shod with the
    preparation of the gospel of peace, the shield of faith, the helmet of salvation, the sword of the Spirit. Fiery darts
    come in from beyond the right edge (no archer) and stand struck in the shield, their fire gone out in smoke."""
    o = [plate_bg(w, h, "EPHESIANS 6:13–17 · THE WHOLE ARMOR OF GOD"), mk.defs(p, *ALL)]
    top = 34; H = h - top
    base = h - 30; s = min((H - 70) / 265, w * 0.5 / 165)
    cx = w * 0.5
    X = lambda u: cx + u * s; Y = lambda v: base + v * s
    o.append(halo(cx, Y(-120), 170 * s, "#FFE680", 0.3))
    sword = ('<path d="M-58 -176 L -61 -248 L -55 -262 L -51 -248 L -54 -176 Z" fill="#D8D8E0" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-70 -176 L -42 -178" stroke="#0D0D0F" stroke-width="6" stroke-linecap="round"></path><path d="M-70 -176 L -42 -178" stroke="#C8963E" stroke-width="3.4" stroke-linecap="round"></path>'
             '<path d="M-56 -176 L -56 -162" stroke="#5A3A1E" stroke-width="6"></path>')
    shield = ('<path d="M4 -176 C 30 -184 58 -180 74 -170 L 74 -40 C 58 -30 30 -26 4 -34 Z" fill="#A8281E" stroke="#FFE680" stroke-width="3"></path>'
              '<path d="M10 -168 C 32 -174 54 -172 68 -164 M10 -42 C 32 -36 54 -38 68 -46" fill="none" stroke="#E8B830" stroke-width="2.4"></path>'
              '<circle cx="39" cy="-104" r="11" fill="#C8963E" stroke="#0D0D0F" stroke-width="2"></circle><path d="M39 -168 L 39 -116 M39 -92 L 39 -40" stroke="#E8B830" stroke-width="2"></path>')
    o.append(roman_guard(p, cx, base, s, spear=False, up=[(-22, -158), (-46, -150), (-56, -176)], extra=sword + shield))
    for (u, v, ang) in ((62, -150, -14), (54, -120, -6), (68, -80, -18), (50, -58, -2)):   # darts struck in the shield, from the right
        o.append(_dart(X(u), Y(v), ang, w - X(u) + 40, out=True))
    o.append(_dart(w - 60, Y(-104), -8, 90, out=False))                                  # one more coming in, still alight
    L, R = w * 0.03, w * 0.97
    def stack(u, v, side, ty, lines):
        x0, y0 = X(u), Y(v)
        ex = L + 160 if side == "l" else R - 160
        anchor = "start" if side == "l" else "end"; lx = L if side == "l" else R
        out = [f'<circle cx="{f(x0)}" cy="{f(y0)}" r="3.4" fill="{GOLD}"></circle><path d="M{f(x0)} {f(y0)} L {f(ex)} {f(ty)} L {f(lx + (4 if side == "l" else -4))} {f(ty)}" stroke="{GOLD}" stroke-width="1.2" fill="none"></path>']
        for j, (t, c, sz) in enumerate(lines):
            out.append(lab(lx, ty - 6 if j == 0 else ty + 8 + (j - 1) * 12, t, c, sz, anchor))
        return "".join(out)
    o.append(stack(0, -200, "l", top + H * 0.12, [("THE HELMET OF SALVATION", GOLD, 10), ("6:17", CY, 8)])
             + stack(-56, -250, "r", top + H * 0.1, [("THE SWORD OF THE SPIRIT", GOLD, 10), ("WHICH IS THE WORD OF GOD · 6:17", CY, 8)])
             + stack(-8, -140, "l", top + H * 0.36, [("THE BREASTPLATE", GOLD, 10), ("OF RIGHTEOUSNESS · 6:14", CY, 8)])
             + stack(66, -168, "r", top + H * 0.37, [("THE SHIELD OF FAITH · 6:16", GOLD, 10), ("TO QUENCH ALL THE FIERY DARTS", CY, 8), ("OF THE EVIL ONE", CY, 8)])
             + stack(-16, -104, "l", top + H * 0.58, [("THE LOINS GIRDED", GOLD, 10), ("WITH TRUTH · 6:14", CY, 8)])
             + stack(-10, -6, "l", top + H * 0.84, [("THE FEET SHOD WITH", GOLD, 10), ("THE PREPARATION OF THE", CY, 8), ("GOSPEL OF PEACE · 6:15", CY, 8)]))
    o.append(lab(R, top + H * 0.24, "HAVING DONE ALL, TO STAND · 6:13", CY, 8, "end"))
    return "".join(o)
