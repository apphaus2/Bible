"""Generators and faces for Joshua Book One (Jericho): the walls of Jericho and their fall, Rahab's window and the
scarlet line, stalks of flax, the ark of the covenant borne by priests, rams'-horn trumpets, the Jordan standing in
one heap, the prince of Jehovah's host, sun and moon, and new faces (Joshua as leader and in old age, Rahab)."""
import math, random
import mk, exodus as E, exodus4 as Z, numbers1 as N
from faces_ex import F
def f(v): return f"{v:.1f}"

def tokens():
    t = N.tokens()
    t["__FACE_JOSHUA_LEAD__"] = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#2A1A10", hl="#6A5A4E", beard=True, scarf="#B5421E", cord=True, brow="scowl", light="#FFC14D")
    t["__FACE_JOSHUA_AWE__"] = F("adam", skin="#E8A06A", shadow="#7A4A3A", hair="#2A1A10", hl="#6A5A4E", beard=True, scarf="#B5421E", cord=True, brow="sorrow", sweat=True, light="#FFF4C2")
    t["__FACE_JOSHUA_OLD__"] = F("adam", skin="#C98E66", shadow="#7A4A3A", hair="#E8E2D6", hl="#B8B2A6", beard=True, beard_color="#E8E2D6", scarf="#B5421E", cord=True, light="#FFC14D")
    t["__FACE_RAHAB__"] = F("eve", skin="#C98E66", shadow="#8A5A3E", hair="#1A1210", scarf="#D7261E")
    return t

BRICK = "#C8803A"
def jericho(x0, x1, top, base, seed, color=BRICK, towers=4, houses=True, window=None, cord=0):
    """The wall of Jericho from outside: mudbrick courses, battlements and towers, flat-roofed houses behind.
    window=(x, y) puts Rahab's house in the wall with its window; cord = length of the scarlet line hanging from it."""
    r = random.Random(seed); o = []
    if houses:
        x = x0
        while x < x1:
            w = r.uniform(40, 90); h = r.uniform(20, 60)
            o.append(f'<rect x="{f(x)}" y="{f(top - h)}" width="{f(w)}" height="{f(h + 10)}" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></rect>'
                     f'<rect x="{f(x + w*0.4)}" y="{f(top - h + 10)}" width="8" height="12" fill="#3A2214"></rect>')
            x += w + r.uniform(-10, 20)
    o.append(f'<rect x="{f(x0)}" y="{f(top)}" width="{f(x1 - x0)}" height="{f(base - top)}" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    for k, yy in enumerate(range(int(top) + 14, int(base), 14)):
        o.append(f'<path d="M{f(x0)} {yy} L {f(x1)} {yy}" stroke="#8A5A30" stroke-width="1.2" opacity="0.7"></path>')
        xx = x0 + (14 if k % 2 else 0)
        while xx < x1:
            o.append(f'<path d="M{f(xx)} {yy - 14} L {f(xx)} {yy}" stroke="#8A5A30" stroke-width="1" opacity="0.5"></path>'); xx += 28
    xx = x0
    while xx < x1:
        o.append(f'<rect x="{f(xx)}" y="{f(top - 14)}" width="14" height="15" fill="{color}" stroke="#0D0D0F" stroke-width="2"></rect>'); xx += 26
    for i in range(towers):
        tx = x0 + (x1 - x0) * (i + 0.5) / towers - 30
        o.append(f'<rect x="{f(tx)}" y="{f(top - 50)}" width="60" height="{f(base - top + 50)}" fill="#B5652E" stroke="#0D0D0F" stroke-width="2.4"></rect>'
                 + "".join(f'<rect x="{f(tx + j*16)}" y="{f(top - 64)}" width="12" height="15" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></rect>' for j in range(4))
                 + f'<rect x="{f(tx + 24)}" y="{f(top - 30)}" width="12" height="20" fill="#2A140C"></rect>')
    if window:
        wx, wy = window
        o.append(f'<rect x="{f(wx - 46)}" y="{f(wy - 40)}" width="92" height="84" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
                 f'<rect x="{f(wx - 52)}" y="{f(wy - 48)}" width="104" height="10" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(wx - 16)}" y="{f(wy - 18)}" width="32" height="36" fill="#FFC14D" stroke="#0D0D0F" stroke-width="2.4"></rect>')
        if cord:
            o.append(f'<path d="M{f(wx)} {f(wy + 16)} C {f(wx + 4)} {f(wy + cord*0.4)} {f(wx - 4)} {f(wy + cord*0.7)} {f(wx + 2)} {f(wy + cord)}" fill="none" stroke="#0D0D0F" stroke-width="6.5" stroke-linecap="round"></path>'
                     f'<path d="M{f(wx)} {f(wy + 16)} C {f(wx + 4)} {f(wy + cord*0.4)} {f(wx - 4)} {f(wy + cord*0.7)} {f(wx + 2)} {f(wy + cord)}" fill="none" stroke="#E8182A" stroke-width="4" stroke-linecap="round"></path>')
    return "".join(o)

def collapse(x0, x1, base, h, seed, color=BRICK):
    """The wall falling down flat: broken stumps, tumbling blocks and a great cloud of dust."""
    r = random.Random(seed); o = []
    for _ in range(18):
        cx, cy, rr = r.uniform(x0, x1), base - r.uniform(h * 0.2, h * 1.1), r.uniform(30, 80)
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(rr)}" fill="#E8C88A" opacity="0.55"></circle>')
    pts = [(x0, base)]; x = x0
    while x < x1:
        x += r.uniform(20, 50); pts.append((x, base - r.uniform(min(12, h * 0.05), min(60, h * 0.16))))
    pts.append((x1, base))
    o.append('<path d="M' + " L ".join(f"{f(px)} {f(py)}" for px, py in pts) + f' Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for _ in range(34):
        cx, cy = r.uniform(x0, x1), base - r.uniform(0, h); w, hh = r.uniform(16, 44), r.uniform(10, 22); a = r.uniform(-50, 50)
        o.append(f'<rect x="{f(-w/2)}" y="{f(-hh/2)}" width="{f(w)}" height="{f(hh)}" fill="{r.choice([color, "#B5652E", "#E8A35A"])}" stroke="#0D0D0F" stroke-width="2" transform="translate({f(cx)} {f(cy)}) rotate({f(a)})"></rect>')
    for _ in range(40):
        o.append(f'<circle cx="{f(r.uniform(x0, x1))}" cy="{f(base - r.uniform(0, h * 1.2))}" r="{f(r.uniform(2, 5))}" fill="#8A5A30"></circle>')
    return "".join(o)

def flax(x, y, w, seed):
    """Stalks of flax laid in order on a roof."""
    r = random.Random(seed); o = []
    for i in range(int(w / 7)):
        xx = x + i * 7 + r.uniform(-2, 2); hh = r.uniform(26, 38)
        o.append(f'<path d="M{f(xx)} {f(y)} L {f(xx + r.uniform(-8, 8))} {f(y - hh)}" stroke="#C9A86A" stroke-width="3"></path>'
                 f'<circle cx="{f(xx + r.uniform(-8, 8))}" cy="{f(y - hh)}" r="2.6" fill="#8FA0E2"></circle>')
    return f'<path d="M{f(x - 4)} {f(y)} L {f(x + w + 4)} {f(y)}" stroke="#8A6A3A" stroke-width="5"></path>' + "".join(o)

CHERUB = ("M-50 -70 L -28 -70 L -31 -94 C -33 -102 -45 -102 -47 -94 Z", "M-39 -116 A 7 7 0 1 0 -39 -102 A 7 7 0 1 0 -39 -116 Z",
          "M-36 -96 C -24 -132 2 -136 -2 -110 C -12 -114 -24 -106 -34 -88 Z")
def ark(x, y, s, uid="ak", glow=True, pole=150):
    """The ark of the covenant: a gold chest with the mercy-seat and two cherubim, borne on two staves. (x, y) = its feet."""
    g = (f'<defs><linearGradient id="{uid}G" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFF4C2"></stop><stop offset="0.4" stop-color="#FFD23F"></stop>'
         f'<stop offset="1" stop-color="#A8721A"></stop></linearGradient></defs>')
    cher = ""
    for sx in (1, -1):
        body, head, wing = CHERUB
        cher += (f'<g transform="scale({sx} 1)"><path d="{wing}" fill="url(#{uid}G)" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<path d="{body}" fill="url(#{uid}G)" stroke="#0D0D0F" stroke-width="2"></path><path d="{head}" fill="url(#{uid}G)" stroke="#0D0D0F" stroke-width="2"></path></g>')
    halo = '<ellipse cx="0" cy="-60" rx="110" ry="80" fill="#FFF4C2" opacity="0.45"></ellipse>' if glow else ""
    return (g + f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">{halo}'
            '<path d="M-52 0 L -52 -8 M52 0 L 52 -8" stroke="#0D0D0F" stroke-width="8"></path>'
            f'<rect x="-58" y="-64" width="116" height="58" fill="url(#{uid}G)" stroke="#0D0D0F" stroke-width="2.6"></rect>'
            '<path d="M-58 -52 L 58 -52 M-58 -18 L 58 -18" stroke="#A8721A" stroke-width="3"></path>'
            '<path d="M-20 -46 L 20 -46 L 20 -24 L -20 -24 Z" fill="none" stroke="#FFF4C2" stroke-width="2"></path>'
            f'<rect x="-64" y="-72" width="128" height="9" fill="url(#{uid}G)" stroke="#0D0D0F" stroke-width="2.4"></rect>'
            f'{cher}'
            f'<path d="M{f(-pole)} -34 L {f(pole)} -34" stroke="#0D0D0F" stroke-width="10" stroke-linecap="round"></path>'
            f'<path d="M{f(-pole)} -34 L {f(pole)} -34" stroke="#C8962E" stroke-width="6" stroke-linecap="round"></path>'
            '<circle cx="-46" cy="-34" r="7" fill="none" stroke="#0D0D0F" stroke-width="3"></circle><circle cx="46" cy="-34" r="7" fill="none" stroke="#0D0D0F" stroke-width="3"></circle></g>')

PRIEST = dict(body="#2A140C", cloth="#F3EFE6")
def ark_borne(p, x, y, s, uid, gap=0.0, priest_body="#2A140C", glow=True):
    """Two priests bearing the ark on its staves; (x, y) = ground under the ark."""
    gap = gap or 170 * s; sh = y - 150 * s; sa = 0.9 * s
    return (mk.person(p, round(x - gap), y, round(s, 3), body=priest_body, cloth="#F3EFE6", sw=3)
            + ark(x, sh + 34 * sa, sa, uid, glow, pole=(gap + 34 * s) / sa)
            + mk.person(p, round(x + gap), y, round(s, 3), body=priest_body, cloth="#F3EFE6", sw=3))

HORN = ("M0 0 C 20 -2 40 -12 52 -32 C 58 -42 68 -46 74 -38 C 64 -28 58 -12 44 2 C 30 12 12 10 0 7 Z")
def shofar(x, y, s=1.0, rot=0, flip=False):
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(sx)} {f(s)})"><path d="{HORN}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>'
            '<path d="M18 -1 C 20 4 20 8 18 10 M34 -6 C 37 -1 38 4 36 6 M48 -20 C 52 -16 54 -12 52 -8" fill="none" stroke="#8A6A3A" stroke-width="1.8"></path></g>')
TRUMPET_ARM = [(-22, -158), (-4, -176), (6, -186)]
def trumpeter(p, x, y, s, flip=False, body="#2A140C"):
    """A priest blowing a trumpet of ram's horn (horn held up at the mouth, flaring forward)."""
    return mk.person(p, round(x), round(y), round(s, 3), body=body, cloth="#F3EFE6", sw=3, flip=flip, up=TRUMPET_ARM,
                     extra=shofar(8, -188, 0.9, rot=-14))

def blasts(x, y, s, n=4, color="#FFF4C2"):
    return "".join(f'<path d="M{f(x + 30*s*i)} {f(y - 30*s*i)} C {f(x + 30*s*i + 10*s)} {f(y - 30*s*i - 20*s)} {f(x + 30*s*i + 30*s)} {f(y - 30*s*i - 26*s)} {f(x + 30*s*i + 44*s)} {f(y - 30*s*i - 18*s)}" fill="none" stroke="{color}" stroke-width="{f(4*s)}" stroke-linecap="round" opacity="{f(1 - i*0.2)}"></path>' for i in range(n))

def heap(cx, base, w, h, uid="hp"):
    """The waters of Jordan standing up in one heap, upstream."""
    return (f'<defs><linearGradient id="{uid}W" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8FD0E2"></stop><stop offset="0.5" stop-color="#2C9DB8"></stop><stop offset="1" stop-color="#0B2E4A"></stop></linearGradient></defs>'
            f'<path d="M{f(cx - w/2)} {f(base)} C {f(cx - w*0.45)} {f(base - h*0.8)} {f(cx - w*0.2)} {f(base - h)} {f(cx)} {f(base - h)} C {f(cx + w*0.2)} {f(base - h)} {f(cx + w*0.45)} {f(base - h*0.8)} {f(cx + w/2)} {f(base)} Z" fill="url(#{uid}W)" stroke="#0D0D0F" stroke-width="2.4"></path>'
            + "".join(f'<path d="M{f(cx - w*k)} {f(base - h*0.2)} C {f(cx - w*k*0.8)} {f(base - h*0.7)} {f(cx - w*k*0.3)} {f(base - h*0.92)} {f(cx)} {f(base - h*0.95)}" fill="none" stroke="#E8F6FA" stroke-width="2" opacity="0.6"></path>' for k in (0.2, 0.32, 0.44))
            + f'<path d="M{f(cx - w*0.3)} {f(base - h*0.92)} C {f(cx - w*0.15)} {f(base - h*1.04)} {f(cx + w*0.15)} {f(base - h*1.04)} {f(cx + w*0.3)} {f(base - h*0.92)}" fill="none" stroke="#F3F7FA" stroke-width="6" stroke-linecap="round"></path>')

def riverbed(x0, x1, y0, y1, seed):
    r = random.Random(seed)
    return "".join(f'<ellipse cx="{f(r.uniform(x0, x1))}" cy="{f(r.uniform(y0, y1))}" rx="{f(r.uniform(6, 16))}" ry="{f(r.uniform(3, 7))}" fill="{r.choice(["#8A7A6A", "#A89A86", "#6A5A4A"])}" stroke="#0D0D0F" stroke-width="1.2"></ellipse>' for _ in range(40))

def prince(p, x, y, s, flip=False, glow=True):
    """The prince of the host of Jehovah: a man of war in crimson with gold, his sword drawn."""
    halo = f'<ellipse cx="{f(x)}" cy="{f(y - 120*s)}" rx="{f(130*s)}" ry="{f(170*s)}" fill="#FFF4C2" opacity="0.4"></ellipse>' if glow else ""
    plate = '<path d="M-20 -160 L 20 -160 L 18 -110 L 0 -100 L -18 -110 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
    return halo + mk.person(p, round(x), round(y), s, body="#B9785A", cloth="#8A1A1A", hair="#1A1210", stroke="#FFD23F", sw=3, flip=flip,
                            up=N.SWORD_ARM, extra=plate + N.BLADE)

def sun(x, y, r):
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r*1.8)}" fill="#FFF4C2" opacity="0.3"></circle>'
            f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="#FFE680" stroke="#E8A317" stroke-width="3"></circle>'
            f'<circle cx="{f(x - r*0.3)}" cy="{f(y - r*0.3)}" r="{f(r*0.45)}" fill="#FFFFFF" opacity="0.7"></circle>')

def moon(x, y, r):
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r*1.5)}" fill="#E8F0F6" opacity="0.2"></circle>'
            f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="#E8F0F6" stroke="#8FA0B8" stroke-width="2"></circle>'
            + "".join(f'<circle cx="{f(x + dx*r)}" cy="{f(y + dy*r)}" r="{f(rr*r)}" fill="#C8D0DE"></circle>' for dx, dy, rr in [(-0.3, -0.2, 0.18), (0.25, 0.1, 0.24), (-0.1, 0.4, 0.12)]))

def city_hill(cx, base, w, h, seed):
    """A walled city on a hill (Gibeon)."""
    r = random.Random(seed); o = [f'<path d="M{f(cx - w)} {f(base)} C {f(cx - w*0.5)} {f(base - h)} {f(cx + w*0.5)} {f(base - h)} {f(cx + w)} {f(base)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>']
    x = cx - w * 0.4
    while x < cx + w * 0.4:
        bw, bh = r.uniform(14, 30), r.uniform(14, 34)
        o.append(f'<rect x="{f(x)}" y="{f(base - h*0.72 - bh)}" width="{f(bw)}" height="{f(bh + 6)}" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
        x += bw - 2
    return "".join(o)

def oak(x, y, s, seed=1):
    r = random.Random(seed)
    leaves = "".join(f'<circle cx="{f(r.uniform(-70, 70))}" cy="{f(r.uniform(-230, -150))}" r="{f(r.uniform(30, 50))}" fill="{r.choice(["#3F8A44", "#2E6A32", "#5E8F26"])}" stroke="#0D0D0F" stroke-width="2"></circle>' for _ in range(12))
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-14 0 C -10 -60 -16 -110 -30 -150 L -10 -150 C 0 -120 6 -110 14 -150 L 30 -150 C 16 -110 12 -60 16 0 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></path>'
            f'{leaves}</g>')
