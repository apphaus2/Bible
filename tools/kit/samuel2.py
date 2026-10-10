"""Generators and faces for 1 Samuel Book Two: David the shepherd (sling, staff, five smooth stones, harp),
Goliath in brass helmet and coat of mail (standing and fallen), Saul's spear in the wall, the cave of the
wild goats, Saul's crown on Gilboa, and new faces (David, Goliath, Jonathan, Saul as king, Jesse, Eliab)."""
import random, math
import mk, numbers1 as N, samuel1 as A
from faces_ex import F
def f(v): return f"{v:.1f}"

def tokens():
    t = A.tokens()
    t["__FACE_DAVID__"] = F("adam", skin="#E0A27A", shadow="#A8603E", hair="#8A3A1E", hl="#C8703A", light="#FFE680")
    t["__FACE_DAVID_BOLD__"] = F("adam", skin="#E0A27A", shadow="#8A3A2A", hair="#8A3A1E", hl="#C8703A", brow="scowl", light="#FF8A3D")
    t["__FACE_DAVID_GRIEVED__"] = F("adam", skin="#C89A7E", shadow="#5A3A4A", hair="#6A2A16", hl="#9A502A", brow="sorrow", light="#8FD0E2")
    t["__FACE_GOLIATH__"] = F("adam", skin="#B9785A", shadow="#5A2A1E", hair="#1A1210", hl="#3A2A1E", beard=True, beard_color="#1A1210", scarf="#C8962E", band=True, brow="scowl", light="#FF6A4A")
    t["__FACE_JONATHAN__"] = F("adam", skin="#D9A27A", shadow="#8A5A3E", hair="#2A1A10", hl="#5A4A3E", stubble="#2A1A10", scarf="#1F5FAD", cord=True, light="#FFE680")
    t["__FACE_SAUL_KING__"] = F("adam", skin="#C98E66", shadow="#6A3A3A", hair="#1A1210", hl="#6A665E", beard=True, beard_color="#2A2220", scarf="#8A1E2E", band=True, brow="sorrow")
    t["__FACE_SAUL_MAD__"] = F("adam", skin="#B98A6E", shadow="#4A2A4A", hair="#1A1210", hl="#6A665E", beard=True, beard_color="#2A2220", scarf="#8A1E2E", band=True, brow="scowl", sweat=True, light="#9A5AC8")
    t["__FACE_SAUL_WEEP__"] = F("adam", skin="#C98E66", shadow="#5A3A4A", hair="#1A1210", hl="#6A665E", beard=True, beard_color="#2A2220", scarf="#8A1E2E", band=True, brow="sorrow", tear=True)
    t["__FACE_JESSE__"] = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#B8B2A6", hl="#8A8478", beard=True, beard_color="#B8B2A6", scarf="#8A6A4A", cord=True)
    return t

DAVID = dict(body="#5A2A16", cloth="#C9A86A", kind="Tunic", sw=4)
SLING_ARM = [(-22, -158), (-40, -200), (-36, -238)]

def sling(x, y, s=1.0, whirl=True):
    """The sling: two cords from the hand to a leather pouch; whirling = a blurred orbit over the hand."""
    if whirl:
        return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
                '<ellipse cx="0" cy="-22" rx="34" ry="11" fill="none" stroke="#F3EFE6" stroke-width="3" stroke-dasharray="10 6" opacity="0.9"></ellipse>'
                '<path d="M0 0 L 26 -26" stroke="#5A3A22" stroke-width="2"></path>'
                '<ellipse cx="30" cy="-28" rx="7" ry="4" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></ellipse></g>')
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M0 0 C 4 20 2 40 -2 52 M0 0 C -4 20 -6 40 -2 52" fill="none" stroke="#5A3A22" stroke-width="2"></path>'
            '<ellipse cx="-2" cy="54" rx="6" ry="4" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></ellipse></g>')

STAFF_R = '<path d="M28 -100 L 34 4" stroke="#0D0D0F" stroke-width="8" stroke-linecap="round"></path><path d="M28 -100 L 34 4" stroke="#8A5A30" stroke-width="5" stroke-linecap="round"></path>'
BAG = '<path d="M14 -110 C 22 -100 24 -84 16 -76 C 8 -76 4 -86 6 -100 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M-18 -158 L 12 -108" stroke="#5A3A22" stroke-width="2.4"></path>'

def david(p, x, y, s, flip=False, whirl=False, staff=True, bag=True, up=None, extra=""):
    """David the shepherd boy: short tunic, staff, shepherd's bag; whirl = sling spinning over his raised hand."""
    ex = (STAFF_R if staff else "") + (BAG if bag else "") + extra
    if whirl:
        up = SLING_ARM; ex += sling(-36, -238, 1.0)
    return mk.person(p, round(x), round(y), round(s, 3), **DAVID, flip=flip, up=up, extra=ex)

HELMET = ('<g transform="translate(0 4)"><path d="M-15 -184 C -17 -214 17 -214 15 -184 Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2"></path>'
          '<path d="M-18 -184 L 18 -184" stroke="#0D0D0F" stroke-width="4"></path><path d="M-18 -184 L 18 -184" stroke="#E8B830" stroke-width="2"></path>'
          '<path d="M0 -210 C 6 -220 14 -224 22 -222 C 14 -214 8 -208 2 -206 Z" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.4"></path></g>')
MAIL = "".join(f'<path d="M{x - 4} {y} A 4 4 0 0 0 {x + 4} {y}" fill="none" stroke="#5A4A1A" stroke-width="1.1"></path>'
               for y in range(-156, -66, 7) for x in range(-20 + (4 if (y // 7) % 2 else 0), 22, 8))
GREAVES = ('<path d="M-15 -48 L -5 -48 L -5 -10 L -13 -10 Z M5 -48 L 15 -48 L 13 -10 L 5 -10 Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="1.6"></path>')
GIANT_SPEAR = ('<path d="M30 6 L 36 -330" stroke="#0D0D0F" stroke-width="11" stroke-linecap="round"></path><path d="M30 6 L 36 -330" stroke="#6B4A2A" stroke-width="7" stroke-linecap="round"></path>'
               '<path d="M36 -330 L 28 -366 L 36 -390 L 44 -366 Z" fill="#8A8A9A" stroke="#0D0D0F" stroke-width="2"></path>')
SHIELD = '<ellipse cx="-34" cy="-110" rx="12" ry="30" fill="#8A6A2A" stroke="#0D0D0F" stroke-width="2"></ellipse><circle cx="-34" cy="-110" r="5" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></circle>'

def goliath(p, x, y, s, flip=False, up=None, spear=True, shield=True):
    """Goliath of Gath: brass helmet, coat of mail of brass scales, brass greaves, the great spear."""
    ex = GREAVES + MAIL + HELMET + (GIANT_SPEAR if spear else "") + (SHIELD if shield and not up else "")
    return mk.person(p, round(x), round(y), round(s, 3), body="#6A3A22", cloth="#B08A3A", kind="Tunic", sw=3, flip=flip, up=up, extra=ex)

def helmet_alone(x, y, s=1.0, rot=0):
    return f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)}) translate(0 182)">{HELMET}</g>'

def goliath_fallen(x, y, s=1.0, flip=False):
    """Goliath fallen upon his face: a prone giant in brass mail, his helmet rolled away, his spear down."""
    return (f'<g transform="translate({f(x)} {f(y)})">'
            f'<path d="M{f(-140*s)} 0 L {f(180*s)} {f(-26*s)}" stroke="#0D0D0F" stroke-width="{f(9*s)}" stroke-linecap="round"></path><path d="M{f(-140*s)} 0 L {f(180*s)} {f(-26*s)}" stroke="#6B4A2A" stroke-width="{f(6*s)}" stroke-linecap="round"></path>'
            + N.prostrate(0, 0, s * 1.4, color="#B08A3A", flip=flip, skin="#6A3A22")
            + helmet_alone((-150 if flip else 150) * s, 0, s * 1.4, 70) + '</g>')

def stones(x, y, n=5, s=1.0, seed=1):
    r = random.Random(seed)
    return "".join(f'<ellipse cx="{f(x + i * 22 * s + r.uniform(-4, 4))}" cy="{f(y + r.uniform(-4, 4))}" rx="{f(10 * s)}" ry="{f(7 * s)}" fill="{r.choice(["#C8C2B6", "#A89E92", "#D8D2C6"])}" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
                   f'<path d="M{f(x + i * 22 * s - 5 * s)} {f(y - 3 * s)} C {f(x + i * 22 * s - 2 * s)} {f(y - 5 * s)} {f(x + i * 22 * s + 2 * s)} {f(y - 5 * s)} {f(x + i * 22 * s + 4 * s)} {f(y - 3 * s)}" fill="none" stroke="#F3EFE6" stroke-width="1.4"></path>' for i in range(n))

def brook(x0, x1, y, h, seed=1):
    r = random.Random(seed)
    ripples = "".join(f'<path d="M{f(r.uniform(x0, x1))} {f(y + r.uniform(4, h - 4))} l 24 0" stroke="#F3EFE6" stroke-width="2" opacity="0.7"></path>' for _ in range(18))
    peb = "".join(f'<ellipse cx="{f(r.uniform(x0, x1))}" cy="{f(y + h + r.uniform(2, 14))}" rx="{f(r.uniform(4, 9))}" ry="{f(r.uniform(3, 5))}" fill="#A89E92" stroke="#0D0D0F" stroke-width="1"></ellipse>' for _ in range(24))
    return (f'<path d="M{f(x0)} {f(y)} C {f(x0 + (x1 - x0) * 0.3)} {f(y - 6)} {f(x0 + (x1 - x0) * 0.7)} {f(y + 6)} {f(x1)} {f(y)} L {f(x1)} {f(y + h)} L {f(x0)} {f(y + h)} Z" fill="#4A9ABA" stroke="#0D0D0F" stroke-width="2"></path>' + ripples + peb)

def flying_stone(x, y, s=1.0, dx=-1):
    """A stone in flight with speed streaks behind it (streaks trail toward dx)."""
    streaks = "".join(f'<path d="M{f(x + dx * 16 * s)} {f(y + o * s)} l {f(dx * L * s)} 0" stroke="#F3EFE6" stroke-width="{f(2.4 * s)}" opacity="0.8"></path>' for o, L in [(-6, 60), (0, 110), (6, 70)])
    return streaks + f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(11 * s)}" ry="{f(8 * s)}" fill="#C8C2B6" stroke="#0D0D0F" stroke-width="{f(2 * s)}"></ellipse>'

def harp(x, y, s=1.0, rot=0):
    """A kinnor (lyre): sound-box, two unequal arms and a slanted yoke, five strings."""
    strings = "".join(f'<path d="M{-14 + i * 7} -26 L {-18 + i * 9} {-88 + i * 3}" stroke="#F3EFE6" stroke-width="1.2"></path>' for i in range(5))
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">'
            '<path d="M-26 0 L 26 0 L 22 -28 L -22 -28 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M-20 -28 L -28 -94 M20 -28 L 22 -80" stroke="#0D0D0F" stroke-width="8" stroke-linecap="round"></path>'
            '<path d="M-20 -28 L -28 -94 M20 -28 L 22 -80" stroke="#B5652E" stroke-width="5" stroke-linecap="round"></path>'
            '<path d="M-32 -96 L 26 -78" stroke="#0D0D0F" stroke-width="8" stroke-linecap="round"></path><path d="M-32 -96 L 26 -78" stroke="#C9A86A" stroke-width="5" stroke-linecap="round"></path>'
            f'{strings}</g>')

def spear_in_wall(x, y, s=1.0, rot=-12):
    """Saul's spear stuck quivering in the wall: (x, y) = the point in the wall."""
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">'
            '<path d="M-6 -4 L 6 4" stroke="#0D0D0F" stroke-width="3"></path>'
            '<path d="M-260 0 L -30 0" stroke="#0D0D0F" stroke-width="10" stroke-linecap="round"></path><path d="M-260 0 L -30 0" stroke="#6B4A2A" stroke-width="6" stroke-linecap="round"></path>'
            '<path d="M-34 -7 L 0 0 L -34 7 Z" fill="#8A8A9A" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M-270 -16 C -276 -8 -276 8 -270 16 M-286 -24 C -294 -10 -294 10 -286 24" fill="none" stroke="#F3EFE6" stroke-width="2.4"></path>'
            '<path d="M8 -14 L 22 -26 M10 0 L 28 0 M8 14 L 22 26" stroke="#0D0D0F" stroke-width="2"></path></g>')

def crown(x, y, s=1.0, rot=0):
    pts = "M-30 0 L -30 -22 L -18 -10 L -8 -30 L 0 -12 L 8 -30 L 18 -10 L 30 -22 L 30 0 Z"
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})"><path d="{pts}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>'
            '<path d="M-30 -6 L 30 -6" stroke="#A8721A" stroke-width="2"></path><circle cx="0" cy="-4" r="3.4" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.2"></circle>'
            '<circle cx="-18" cy="-4" r="2.6" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="1"></circle><circle cx="18" cy="-4" r="2.6" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="1"></circle></g>')

def cave(W, H, mouth_x, mouth_w, floor, seed=1):
    """Inside the cave: dark rock all round, a bright ragged mouth (x, width) opening to daylight."""
    r = random.Random(seed)
    top = floor - (floor * 0.7)
    pts = [(mouth_x, floor)]
    for i in range(1, 8):
        a = math.pi * i / 8
        pts.append((mouth_x + mouth_w / 2 - math.cos(a) * mouth_w / 2 + r.uniform(-8, 8), floor - math.sin(a) * (floor - top) + r.uniform(-10, 10)))
    pts.append((mouth_x + mouth_w, floor))
    d = "M" + " L ".join(f"{f(px)} {f(py)}" for px, py in pts) + " Z"
    rocks = "".join(f'<path d="M{f(r.uniform(0, W))} {f(r.uniform(0, floor))} l {f(r.uniform(20, 60))} {f(r.uniform(-10, 10))}" stroke="#2A2220" stroke-width="2"></path>' for _ in range(30))
    return (f'<rect x="-10" y="-10" width="{W + 20}" height="{H + 20}" fill="#1A1412"></rect>'
            f'<path d="{d}" fill="#FFF4C2" stroke="#0D0D0F" stroke-width="3"></path>'
            f'<path d="{d}" fill="#FFC14D" opacity="0.35" transform="translate(0 4)"></path>'
            + rocks
            + f'<path d="M-10 {f(floor)} L {W + 10} {f(floor)} L {W + 10} {H + 10} L -10 {H + 10} Z" fill="#2A2220" stroke="#0D0D0F" stroke-width="2"></path>')

def skirt_piece(x, y, s=1.0, color="#8A1E2E"):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M0 0 L 22 -4 L 26 8 L 18 14 L 10 10 L 2 14 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M2 12 L 4 16 M10 10 L 12 15 M18 13 L 20 17" stroke="#E8B830" stroke-width="1.4"></path></g>')

def knife(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})"><path d="M0 0 L 30 -4 L 34 0 L 30 4 Z" fill="#C8C2D6" stroke="#0D0D0F" stroke-width="1.4"></path>'
            '<rect x="-12" y="-3" width="12" height="6" fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.2"></rect></g>')

def gilboa(W, base, h, seed=1, color="#2A1A2E"):
    r = random.Random(seed); pts = [(-10, base)]
    for i in range(9):
        pts.append((i * W / 8, base - h * (0.4 + 0.6 * math.sin(math.pi * i / 8)) + r.uniform(-12, 12)))
    pts.append((W + 10, base))
    return f'<path d="M-10 {base + 400} L ' + " L ".join(f"{f(px)} {f(py)}" for px, py in pts) + f' L {W + 10} {base + 400} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'

def spears_down(xs, base, seed=1, color="#0D0D0F"):
    r = random.Random(seed)
    return "".join(f'<path d="M{f(x)} {f(base)} L {f(x + r.uniform(-30, 30))} {f(base - r.uniform(60, 110))}" stroke="{color}" stroke-width="3"></path>' for x in xs)
