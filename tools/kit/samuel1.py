"""Generators and faces for 1 Samuel Book One: the tabernacle at Shiloh with the lamp of God, Eli's seat, the idol Dagon
(standing, fallen, broken on the threshold), the new cart drawn by two milch kine, the vial of oil, and new faces
(Hannah, Eli, the child Samuel, Samuel grown and old, Saul)."""
import random, math
import mk, joshua1 as J, judges2 as S, ruth1 as R
from faces_ex import F
def f(v): return f"{v:.1f}"

def tokens():
    t = R.tokens()
    t["__FACE_HANNAH__"] = F("eve", skin="#D9A27A", shadow="#6A3A4A", hair="#2A1A10", scarf="#1F7A8C", brow="sorrow", tear=True)
    t["__FACE_HANNAH_JOY__"] = F("eve", skin="#E3B08A", shadow="#9A6A4A", hair="#2A1A10", scarf="#1F7A8C", laugh=True, light="#FFE680")
    t["__FACE_ELI__"] = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#E8E2D6", hl="#B8B2A6", beard=True, beard_color="#E8E2D6", scarf="#2C5F9A", band=True)
    t["__FACE_ELI_AWE__"] = F("adam", skin="#D9A27A", shadow="#6A4A5A", hair="#E8E2D6", hl="#B8B2A6", beard=True, beard_color="#E8E2D6", scarf="#2C5F9A", band=True, brow="sorrow", light="#FFE680")
    t["__FACE_SAMUEL_CHILD__"] = F("adam", skin="#E3B08A", shadow="#B97A58", hair="#2A1A10", hl="#5A4A3E", light="#FFE680")
    t["__FACE_SAMUEL_NIGHT__"] = F("adam", skin="#C8A08A", shadow="#4A4A6A", hair="#1A1210", hl="#3A3A5E", light="#8FD0E2")
    t["__FACE_SAMUEL_OLD__"] = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#9A968E", hl="#6A665E", beard=True, beard_color="#9A968E", scarf="#12113A", cord=True)
    t["__FACE_SAMUEL_GRIEVED__"] = F("adam", skin="#B98A6E", shadow="#5A3A4A", hair="#9A968E", hl="#6A665E", beard=True, beard_color="#9A968E", scarf="#12113A", cord=True, brow="sorrow")
    t["__FACE_SAUL__"] = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", scarf="#8A1E2E", cord=True)
    t["__FACE_SAUL_ANOINTED__"] = F("adam", skin="#D9A27A", shadow="#8A5A3E", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", brow="sorrow", light="#FFD23F")
    return t

# ── the sanctuary at Shiloh ──
def lamp(x, y, s=1.0, lit=True):
    """The lamp of God: a seven-branched golden lampstand. (x, y) = its foot."""
    arms = "".join(f'<path d="M{-d} -120 A {d} {d} 0 0 0 {d} -120" fill="none" stroke="#0D0D0F" stroke-width="9"></path>'
                   f'<path d="M{-d} -120 A {d} {d} 0 0 0 {d} -120" fill="none" stroke="#E8B830" stroke-width="5"></path>' for d in (22, 44, 66))
    cups = "".join(f'<path d="M{dx - 7} -128 L {dx + 7} -128 L {dx + 4} -118 L {dx - 4} -118 Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.6"></path>' for dx in (-66, -44, -22, 0, 22, 44, 66))
    if lit:
        fl = "".join(f'<ellipse cx="{dx}" cy="-140" rx="16" ry="20" fill="#FFF4C2" opacity="0.35"></ellipse>'
                     f'<path d="M{dx} -152 C {dx + 6} -142 {dx + 6} -132 {dx} -130 C {dx - 6} -132 {dx - 6} -142 {dx} -152 Z" fill="#FFB020" stroke="#0D0D0F" stroke-width="1.2"></path>'
                     f'<path d="M{dx} -144 C {dx + 2} -138 {dx + 2} -134 {dx} -133 C {dx - 2} -134 {dx - 2} -138 {dx} -144 Z" fill="#FFF4C2"></path>' for dx in (-66, -44, -22, 0, 22, 44, 66))
    else:
        fl = "".join(f'<path d="M{dx} -130 C {dx + 8} -150 {dx - 8} -164 {dx + 4} -186" fill="none" stroke="#8A8478" stroke-width="2" opacity="0.6"></path>' for dx in (-44, 0, 44))
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
            '<path d="M-30 0 L 30 0 L 14 -14 L -14 -14 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M0 -14 L 0 -122" stroke="#0D0D0F" stroke-width="10"></path><path d="M0 -14 L 0 -122" stroke="#E8B830" stroke-width="6"></path>'
            '<path d="M-5 -60 L 5 -60 M-5 -90 L 5 -90" stroke="#FFF4C2" stroke-width="2"></path>'
            f'{arms}{cups}{fl}</g>')

def sanctuary(W, H, floor, seed=1, glow=True):
    """Inside the tabernacle: the veil of blue, purple and scarlet behind gold-capped acacia pillars, and a dark floor."""
    r = random.Random(seed)
    stripes = "".join(f'<rect x="{x}" y="-10" width="24" height="{f(floor + 10)}" fill="{c}"></rect>'
                      for x, c in zip(range(-10, W + 10, 24), (["#1F3F8A", "#4A1D55", "#8A1E2E"] * 60)))
    folds = "".join(f'<path d="M{x} -10 L {x} {f(floor)}" stroke="#0D0D0F" stroke-width="1" opacity="0.35"></path>' for x in range(2, W, 24))
    cher = "".join(f'<path d="M{x - 20} {f(floor * 0.35)} C {x - 10} {f(floor * 0.25)} {x + 10} {f(floor * 0.25)} {x + 20} {f(floor * 0.35)} L {x} {f(floor * 0.45)} Z" fill="#E8B830" opacity="0.5"></path>'
                   for x in range(40, W, 120))
    pil = "".join(f'<rect x="{x - 9}" y="-10" width="18" height="{f(floor + 10)}" fill="#6B4A2A" stroke="#0D0D0F" stroke-width="2"></rect>'
                  f'<rect x="{x - 13}" y="{f(floor - 14)}" width="26" height="14" fill="#C8C2D6" stroke="#0D0D0F" stroke-width="2"></rect>'
                  f'<rect x="{x - 12}" y="-10" width="24" height="22" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></rect>' for x in range(30, W, 180))
    halo = f'<ellipse cx="{W/2}" cy="{f(floor * 0.6)}" rx="{f(W * 0.5)}" ry="{f(floor * 0.6)}" fill="#FFE680" opacity="0.18"></ellipse>' if glow else ""
    return (stripes + folds + cher + halo + pil
            + f'<path d="M-10 {f(floor)} L {W + 10} {f(floor)} L {W + 10} {H + 10} L -10 {H + 10} Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></path>'
            + f'<path d="M-10 {f(floor + 2)} L {W + 10} {f(floor + 2)}" stroke="#8A6A4A" stroke-width="2"></path>')

def mat_sleeper(x, y, s, color="#F3EFE6", head="#2A140C", flip=False):
    """A child asleep on a mat under a blanket: the head shows."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            '<path d="M-100 0 L 100 0 L 96 -10 L -96 -10 Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<circle cx="74" cy="-26" r="15" fill="{head}" stroke="#0D0D0F" stroke-width="2"></circle>'
            '<path d="M60 -30 C 66 -44 86 -46 90 -30 C 82 -38 70 -38 60 -30 Z" fill="#1A1210"></path>'
            f'<path d="M-90 -10 C -92 -34 -60 -42 -4 -42 C 34 -42 56 -36 60 -12 L 60 -10 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M-76 -18 L 50 -18 M-66 -30 L 40 -32" stroke="#C9A86A" stroke-width="2.4" opacity="0.8"></path></g>')

def seat(x, y, s=1.0, fallen=False):
    """Eli's seat: a high-backed wooden chair. Fallen = lying on its back."""
    rot = -80 if fallen else 0
    dy = -36 * s if fallen else 0
    return (f'<g transform="translate({f(x)} {f(y + dy)}) rotate({rot}) scale({f(s)})">'
            '<path d="M-30 0 L -30 -60 M 26 0 L 26 -60" stroke="#0D0D0F" stroke-width="9" stroke-linecap="round"></path>'
            '<path d="M-30 0 L -30 -60 M 26 0 L 26 -60" stroke="#8A5A30" stroke-width="5" stroke-linecap="round"></path>'
            '<rect x="-36" y="-66" width="68" height="10" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></rect>'
            '<path d="M-34 -66 L -40 -150 L -28 -150 L -22 -66 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M-40 -150 L -28 -150 L -28 -100 L -38 -100 Z M-38 -140 L -30 -140" fill="none" stroke="#5A3A22" stroke-width="1.6"></path></g>')

# ── Dagon ──
DG_PLINTH = '<rect x="-64" y="-26" width="128" height="26" fill="#7A746A" stroke="#0D0D0F" stroke-width="2.4"></rect><path d="M-64 -12 L 64 -12" stroke="#5A564E" stroke-width="2"></path>'
DG_TAIL = ('<path d="M-36 -176 C -44 -126 -32 -76 -12 -48 L -50 -28 C -30 -30 -14 -36 0 -40 C 14 -36 30 -30 50 -28 L 12 -48 C 32 -76 44 -126 36 -176 Z" fill="#4A7A6A" stroke="#0D0D0F" stroke-width="2.6" stroke-linejoin="round"></path>'
           + "".join(f'<path d="M{x - 8} {y} A 8 8 0 0 0 {x + 8} {y}" fill="none" stroke="#2A4A3E" stroke-width="1.6"></path>'
                     for y, xs in [(-160, (-24, -8, 8, 24)), (-140, (-28, -12, 4, 20)), (-120, (-24, -8, 8, 24)), (-100, (-18, -2, 14)), (-80, (-12, 4)), (-62, (-4,))] for x in xs))
DG_TORSO = ('<path d="M-36 -176 L -42 -244 C -30 -258 30 -258 42 -244 L 36 -176 Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2.6"></path>'
            '<path d="M-40 -180 L 40 -180" stroke="#8A5A1A" stroke-width="5"></path><path d="M-14 -236 C -8 -226 8 -226 14 -236" fill="none" stroke="#8A5A1A" stroke-width="2"></path>')
def _arm(sx):
    return (f'<path d="M{42*sx} -242 L {58*sx} -206 L {48*sx} -190" fill="none" stroke="#0D0D0F" stroke-width="17" stroke-linecap="round" stroke-linejoin="round"></path>'
            f'<path d="M{42*sx} -242 L {58*sx} -206 L {48*sx} -190" fill="none" stroke="#C8962E" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"></path>')
def palm(x, y, s=1.0, rot=0):
    """One palm of Dagon's hand, broken off at the wrist."""
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">'
            '<path d="M-8 0 L -10 -14 L -12 -30 L -8 -31 L -5 -18 L -4 -34 L 0 -35 L 1 -18 L 4 -33 L 8 -32 L 6 -16 L 11 -26 L 14 -24 L 8 -6 L 8 0 Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2" stroke-linejoin="round"></path>'
            '<path d="M-8 0 L -6 3 L -2 -1 L 2 3 L 6 -1 L 8 0" fill="none" stroke="#5A3A12" stroke-width="1.6"></path></g>')
DG_HEAD = ('<path d="M-22 -258 L -24 -296 C -20 -322 20 -322 24 -296 L 22 -258 Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2.6"></path>'
           '<path d="M-22 -280 L -22 -246 C -10 -236 10 -236 22 -246 L 22 -280 C 12 -272 -12 -272 -22 -280 Z" fill="#6A4A1A" stroke="#0D0D0F" stroke-width="2"></path>'
           + "".join(f'<path d="M{x} -276 L {x} -244" stroke="#3A2A0A" stroke-width="1.4"></path>' for x in (-14, -7, 0, 7, 14))
           + '<path d="M-14 -292 L -6 -290 M6 -290 L 14 -292" stroke="#0D0D0F" stroke-width="3" stroke-linecap="round"></path>'
           '<path d="M-26 -300 L -30 -336 C -24 -350 -8 -360 0 -364 C 8 -360 24 -350 30 -336 L 26 -300 C 14 -308 -14 -308 -26 -300 Z" fill="#4A7A6A" stroke="#0D0D0F" stroke-width="2.6"></path>'
           '<circle cx="10" cy="-340" r="4" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></circle><path d="M-6 -362 L 6 -362 L 0 -374 Z" fill="#4A7A6A" stroke="#0D0D0F" stroke-width="2"></path>')
def head_alone(x, y, s=1.0, rot=0):
    return f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)}) translate(0 300)">{DG_HEAD}</g>'

def dagon(x, y, s=1.0, state=0):
    """state 0: standing on his plinth. 1: fallen upon his face (plinth empty). 2: only the stump lying (head and palms placed separately)."""
    body = DG_TAIL + DG_TORSO
    if state == 0:
        return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">{DG_PLINTH}<g transform="translate(0 -26)">{_arm(1)}{_arm(-1)}{body}{DG_HEAD}'
                f'{palm(48, -190, 1, 180)}{palm(-48, -190, 1, 180)}</g></g>')
    full = (_arm(1) + _arm(-1) + body + DG_HEAD + palm(48, -190, 1, 180) + palm(-48, -190, 1, 180)) if state == 1 else body
    # lying along the ground, head toward +x
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><g transform="translate(-200 -46) rotate(90)">{full}</g></g>')

def threshold(x0, x1, y, h=16):
    return (f'<rect x="{f(x0)}" y="{f(y - h)}" width="{f(x1 - x0)}" height="{f(h)}" fill="#A89A86" stroke="#0D0D0F" stroke-width="2.2"></rect>'
            f'<path d="M{f(x0)} {f(y - h/2)} L {f(x1)} {f(y - h/2)}" stroke="#7A6E5E" stroke-width="1.4"></path>')

# ── the cart and the kine ──
def cow(x, y, s=1.0, flip=False, color="#C9A27A", patch="#F3EFE6", low=False):
    """A milch cow walking, facing right; (x, y) = ground under her middle."""
    sx = -s if flip else s
    mouth = '<path d="M124 -62 L 134 -56" stroke="#0D0D0F" stroke-width="2"></path>' if low else ""
    leg = lambda d, c: f'<path d="{d}" fill="{c}" stroke="#0D0D0F" stroke-width="2" stroke-linejoin="round"></path>'
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            + leg("M-66 -56 L -62 -28 L -68 -4 L -66 0 L -56 0 L -54 -26 L -50 -56 Z", color)
            + leg("M46 -54 L 42 -4 L 44 0 L 54 0 L 54 -4 L 58 -54 Z", color)
            + '<path d="M-82 -88 C -90 -74 -90 -56 -86 -40" fill="none" stroke="#0D0D0F" stroke-width="4"></path><path d="M-86 -42 C -92 -36 -90 -28 -84 -30 C -80 -34 -82 -40 -86 -42 Z" fill="#3A2214"></path>'
            + f'<path d="M-82 -66 C -86 -98 -66 -110 -24 -108 L 40 -112 C 62 -112 72 -104 76 -92 L 80 -70 C 78 -56 68 -50 56 -50 L -60 -48 C -76 -48 -82 -54 -82 -66 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.6"></path>'
            + f'<path d="M-40 -104 C -24 -96 -20 -78 -34 -66 C -46 -74 -50 -92 -40 -104 Z M20 -108 C 30 -98 26 -84 14 -80 C 8 -90 10 -102 20 -108 Z" fill="{patch}" opacity="0.9"></path>'
            + '<path d="M-36 -50 C -36 -38 -16 -36 -14 -50 Z" fill="#E89A9A" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M-30 -42 L -30 -36 M-20 -42 L -20 -36" stroke="#0D0D0F" stroke-width="2"></path>'
            + leg("M-56 -54 L -52 -28 L -58 -4 L -56 0 L -46 0 L -44 -26 L -40 -54 Z", color)
            + leg("M60 -54 L 56 -4 L 58 0 L 68 0 L 68 -4 L 72 -54 Z", color)
            + f'<path d="M68 -108 C 86 -114 102 -106 110 -94 L 128 -72 C 132 -62 126 -54 116 -56 L 104 -60 C 94 -68 82 -76 70 -82 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.6"></path>'
            + '<ellipse cx="122" cy="-62" rx="10" ry="8" fill="#E8B0A0" stroke="#0D0D0F" stroke-width="1.8"></ellipse><circle cx="124" cy="-64" r="1.6" fill="#0D0D0F"></circle>'
            + '<circle cx="104" cy="-92" r="3" fill="#0D0D0F"></circle>'
            + f'<path d="M94 -104 C 84 -112 74 -110 70 -104 C 78 -100 86 -100 94 -104 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></path>'
            + '<path d="M98 -108 C 98 -118 104 -124 110 -124" fill="none" stroke="#0D0D0F" stroke-width="5" stroke-linecap="round"></path><path d="M98 -108 C 98 -118 104 -124 110 -124" fill="none" stroke="#E8E2D6" stroke-width="2.6" stroke-linecap="round"></path>'
            + mouth + '</g>')

def calf(x, y, s=1.0, flip=False, color="#C9A27A"):
    return cow(x, y, s * 0.55, flip, color)

def cart(x, y, s=1.0, load=""):
    """A new cart of fresh wood on two wheels; (x, y) = ground under the wheel. The pole runs forward (+x) to the yoke at x+210."""
    spokes = "".join(f'<path d="M0 -40 L {f(34 * math.cos(a * 0.785))} {f(-40 + 34 * math.sin(a * 0.785))}" stroke="#5A3A22" stroke-width="3"></path>' for a in range(8))
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
            '<path d="M40 -66 L 214 -96" stroke="#0D0D0F" stroke-width="9" stroke-linecap="round"></path><path d="M40 -66 L 214 -96" stroke="#E8C88A" stroke-width="5" stroke-linecap="round"></path>'
            '<rect x="-90" y="-82" width="150" height="20" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
            '<path d="M-90 -72 L 60 -72" stroke="#B5652E" stroke-width="1.6"></path>'
            '<path d="M-90 -82 L -90 -104 M60 -82 L 60 -104" stroke="#0D0D0F" stroke-width="6"></path><path d="M-90 -82 L -90 -104 M60 -82 L 60 -104" stroke="#E8C88A" stroke-width="3"></path>'
            f'{load}'
            '<circle cx="0" cy="-40" r="40" fill="none" stroke="#0D0D0F" stroke-width="10"></circle><circle cx="0" cy="-40" r="40" fill="none" stroke="#C9A86A" stroke-width="6"></circle>'
            f'{spokes}<circle cx="0" cy="-40" r="8" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></circle></g>')

def yoke(x, y, s=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-12 -2 L 16 -10" stroke="#0D0D0F" stroke-width="12" stroke-linecap="round"></path>'
            '<path d="M-12 -2 L 16 -10" stroke="#C9A86A" stroke-width="8" stroke-linecap="round"></path></g>')

def team(x, y, s=1.0, low=False, colors=("#C9A27A", "#8A5A30")):
    """Two milch kine yoked to the cart with the ark upon it, heading right. (x, y) = ground under the cart wheel."""
    k = s
    return (cow(x + 330 * k, y - 26 * k, 0.84 * k, color=colors[1], patch="#E8E2D6", low=low)
            + cart(x, y, k, load=J.ark(-15, -82, 0.62, uid=f"ct{int(x)}", glow=True, pole=72))
            + cow(x + 280 * k, y, 0.92 * k, color=colors[0], low=low)
            + yoke(x + 360 * k, y - 104 * k, k))

# ── people and props ──
HOLD_BABY = R.HOLD_BABY
def hannah_with_child(p, x, y, s, flip=False):
    return mk.person(p, round(x), round(y), round(s, 3), body="#3A1E14", cloth="#1F7A8C", woman=True, hair="#2A1A10", sw=4, flip=flip,
                     up=HOLD_BABY, extra=R.baby(10, -130, 0.8))

def vial(x, y, s=1.0, rot=0, pour=0):
    """A horn-shaped vial of oil; pour = length of the golden stream falling from it."""
    stream = (f'<path d="M-4 6 C -2 {f(pour * 0.4)} 2 {f(pour * 0.7)} 0 {f(pour)}" fill="none" stroke="#FFD23F" stroke-width="5" stroke-linecap="round"></path>'
              f'<path d="M-4 6 C -2 {f(pour * 0.4)} 2 {f(pour * 0.7)} 0 {f(pour)}" fill="none" stroke="#FFF4C2" stroke-width="1.6"></path>') if pour else ""
    return (f'<g transform="translate({f(x)} {f(y)})">{stream}<g transform="rotate({f(rot)}) scale({f(s)})">'
            '<path d="M-6 0 C -10 -16 -14 -30 -10 -44 C -6 -56 6 -60 16 -54 C 24 -48 22 -36 14 -26 C 6 -16 4 -8 6 0 Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.2"></path>'
            '<path d="M-7 0 L 7 0 L 6 6 L -6 6 Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M-6 -40 C 0 -46 8 -46 12 -42" fill="none" stroke="#8A6A3A" stroke-width="1.6"></path></g></g>')

def drops(x, y, n, seed, spread=40):
    r = random.Random(seed)
    return "".join(f'<path d="M{f(dx)} {f(dy - 8)} C {f(dx + 4)} {f(dy - 2)} {f(dx + 4)} {f(dy + 3)} {f(dx)} {f(dy + 3)} C {f(dx - 4)} {f(dy + 3)} {f(dx - 4)} {f(dy - 2)} {f(dx)} {f(dy - 8)} Z" fill="#FFD23F" stroke="#8A5A1A" stroke-width="1"></path>'
                   for dx, dy in ((x + r.uniform(-spread, spread), y + r.uniform(0, spread * 1.4)) for _ in range(n)))

def boy(p, x, y, s, flip=False, up=None, extra=""):
    """The child Samuel in his little linen tunic."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#3A1E14", cloth="#F3EFE6", kind="Tunic", sw=4, flip=flip, up=up, extra=extra)

def eli(p, x, y, s, flip=False, up=None, extra=""):
    """Eli the old priest: blue robe, white head."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#3A1E14", cloth="#2C5F9A", sw=4, flip=flip, up=up, extra=extra)

def eli_seated(p, x, y, s, flip=False):
    """Eli seated on his chair, seen from the side (chair drawn under a kneeling-style body)."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">' + seat(0, 0, 1.0)
            + '<path d="M-30 -66 L -34 -140 C -30 -160 -10 -168 6 -160 L 14 -120 L 12 -72 L 46 -70 L 50 -6 L 38 -6 L 34 -56 L -22 -56 Z" fill="#2C5F9A" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>'
            + '<circle cx="-4" cy="-176" r="15" fill="#C98E66" stroke="#0D0D0F" stroke-width="2"></circle>'
            + '<path d="M-19 -178 C -20 -196 4 -198 10 -186 C 0 -188 -8 -184 -12 -170 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></path>'
            + '<path d="M-20 -182 C -14 -192 6 -194 12 -186" fill="none" stroke="#E8B830" stroke-width="2.4"></path>'
            + '<path d="M2 -168 C 12 -162 12 -146 2 -138 C -4 -146 -6 -158 -4 -166 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></path>'
            + '<circle cx="5" cy="-178" r="1.6" fill="#0D0D0F"></circle>'
            + '<path d="M0 -140 L 22 -112 L 30 -100" fill="none" stroke="#0D0D0F" stroke-width="12" stroke-linecap="round"></path><path d="M0 -140 L 22 -112 L 30 -100" fill="none" stroke="#2C5F9A" stroke-width="8" stroke-linecap="round"></path>'
            + '</g>')

def shiloh(cx, base, w, h):
    """The tabernacle at Shiloh: the long dark tent of meeting rising behind the white linen hangings of its court."""
    tw, tb, tt = w * 0.6, base - h * 0.3, base - h
    sag = "".join(f" Q {f(cx - tw/2 + (i + 0.5) * tw/4)} {f(tt + 10)} {f(cx - tw/2 + (i + 1) * tw/4)} {f(tt)}" for i in range(4))
    return (f'<path d="M{f(cx - tw/2 - 12)} {f(tb)} L {f(cx - tw/2)} {f(tt)}{sag} L {f(cx + tw/2 + 12)} {f(tb)} Z" fill="#4A2E26" stroke="#0D0D0F" stroke-width="2.4"></path>'
            + "".join(f'<path d="M{f(cx - tw/2 + i * tw/4)} {f(tt)} L {f(cx - tw/2 + i * tw/4 + (i - 2) * 3)} {f(tb)}" stroke="#2A1A14" stroke-width="1.6"></path>' for i in range(1, 4))
            + f'<path d="M{f(cx - tw/2 - 6)} {f(tt + 18)} L {f(cx + tw/2 + 6)} {f(tt + 18)}" stroke="#8A1E2E" stroke-width="4"></path>'
            + f'<path d="M{f(cx - w*0.08)} {f(tb)} L {f(cx - w*0.08)} {f(tt + 24)} L {f(cx + w*0.08)} {f(tt + 24)} L {f(cx + w*0.08)} {f(tb)} Z" fill="#1F3F8A" stroke="#0D0D0F" stroke-width="2"></path>'
            + f'<path d="M{f(cx - w*0.04)} {f(tt + 24)} L {f(cx - w*0.04)} {f(tb)} M{f(cx + w*0.04)} {f(tt + 24)} L {f(cx + w*0.04)} {f(tb)}" stroke="#8A1E2E" stroke-width="3"></path>'
            + f'<path d="M{f(cx - w/2)} {f(base)} L {f(cx - w/2)} {f(base - h*0.35)} L {f(cx + w/2)} {f(base - h*0.35)} L {f(cx + w/2)} {f(base)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></path>'
            + "".join(f'<path d="M{f(cx - w/2 + i * w/10)} {f(base)} L {f(cx - w/2 + i * w/10)} {f(base - h*0.38)}" stroke="#8A6A4A" stroke-width="2.4"></path>' for i in range(11)))
