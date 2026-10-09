"""Generators and faces for 2 Samuel Book Two (Absalom): Absalom with his heavy hair, the balance that weighed it,
the great oak of the forest of Ephraim with Absalom caught in its boughs, the city gate with the chamber over it
and the watchman on its roof, a runner, a heap of stones, Araunah's threshing-floor and David's altar, and new faces
(Absalom, David grown old, the Cushite, Gad)."""
import random, math
import mk, exodus4 as Z, samuel3 as C
from faces_ex import F
def f(v): return f"{v:.1f}"

def tokens():
    t = C.tokens()
    t["__FACE_ABSALOM__"] = F("adam", skin="#E3B08A", shadow="#A8705A", hair="#1A1210", hl="#4A3A2E", stubble="#2A1A10", band=True, light="#FFE680")
    t["__FACE_ABSALOM_SLY__"] = F("adam", skin="#E3B08A", shadow="#8A4A3A", hair="#1A1210", hl="#4A3A2E", stubble="#2A1A10", band=True, laugh=True, light="#FF8A3D")
    old = dict(skin="#C98E66", hair="#9A6A5A", hl="#C8B8AA", beard=True, beard_color="#B8A89A", band=True)
    t["__FACE_DAVID_OLD__"] = F("adam", shadow="#7A4A3A", scarf="#4A2A7A", **old)
    t["__FACE_DAVID_OLD_ALARM__"] = F("adam", shadow="#5A2A3A", scarf="#4A2A7A", brow="sorrow", sweat=True, light="#FF8A3D", **old)
    t["__FACE_DAVID_OLD_WEEP__"] = F("adam", shadow="#4A3A5A", scarf="#4A2A7A", brow="sorrow", tear=True, light="#8FD0E2", **old)
    t["__FACE_CUSHITE__"] = F("adam", skin="#6A3A22", shadow="#2A140C", hair="#0D0D0F", hl="#2A2220", stubble="#0D0D0F", scarf="#F3EFE6", sweat=True)
    t["__FACE_GAD__"] = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#2A2220", hl="#5A5650", beard=True, beard_color="#3A3230", scarf="#8A6A4A", cord=True)
    return t

DAVID_OLD = dict(body="#5A2A16", cloth="#4A2A7A", kind="Tunic", sw=4)
ABSALOM = dict(body="#4A2416", cloth="#B5121B", kind="Tunic", sw=4)
HAIR_BACK = ('<path d="M-14 -196 C -26 -192 -30 -176 -28 -160 C -26 -140 -22 -128 -16 -118 L 16 -118 C 22 -128 26 -140 28 -160 '
             'C 30 -176 26 -192 14 -196 C 6 -200 -6 -200 -14 -196 Z" fill="#1A1210" stroke="#0D0D0F" stroke-width="2"></path>')
SASH = '<path d="M-26 -110 L 26 -110" stroke="#E8B830" stroke-width="5"></path>'

def absalom(p, x, y, s, flip=False, up=None, extra=""):
    """Absalom: scarlet tunic with a gold sash, a gold band, and his heavy black hair falling to his shoulders."""
    return mk.person(p, round(x), round(y), round(s, 3), **ABSALOM, flip=flip, up=up, pre=HAIR_BACK,
                     extra=SASH + '<path d="M-12 -190 L 12 -190" stroke="#E8B830" stroke-width="3"></path>' + extra)

def hanging(x, y, s, uid):
    """Absalom caught by the head in the oak: (x, y) = where his head meets the boughs; arms up, feet dangling."""
    left = [(-22, -158), (-36, -196), (-30, -232)]; right = [(22, -158), (40, -194), (34, -230)]
    return (f'<defs><path id="{uid}B" d="{Z.MAN_BOTH}"></path><path id="{uid}T" d="{mk.TUNIC}"></path></defs>'
            f'<g transform="translate({f(x)} {f(y + 186 * s)}) rotate(6) scale({f(s)})" fill="#4A2416">{HAIR_BACK}<use href="#{uid}B"></use>'
            f'<use href="#{uid}T" fill="#B5121B" stroke="#0D0D0F" stroke-width="3"></use>{SASH}'
            + mk.arm(left, "#4A2416", 10) + mk.arm(right, "#4A2416", 10) + '</g>')

def great_oak(x, y, s=1.0, seed=1, dark=False):
    """A great oak with a thick trunk and long low boughs reaching to the right; (x, y) = foot of the trunk."""
    r = random.Random(seed)
    trunk = "#2A1A14" if dark else "#5A3A22"
    leaf = ["#1A2A1A", "#22301E", "#1A241A"] if dark else ["#3F8A44", "#2E6A32", "#5E8F26"]
    boughs = ('<path d="M-30 0 C -24 -80 -40 -150 -60 -200 L -20 -210 C -10 -170 0 -150 10 -190 L 40 -186 C 28 -140 24 -80 34 0 Z" fill="' + trunk + '" stroke="#0D0D0F" stroke-width="2.6"></path>'
              f'<path d="M10 -170 C 80 -190 160 -180 260 -150 L 262 -136 C 160 -160 90 -168 20 -150 Z" fill="{trunk}" stroke="#0D0D0F" stroke-width="2.4"></path>'
              f'<path d="M-40 -190 C -100 -220 -160 -220 -220 -200 L -222 -188 C -160 -204 -100 -204 -44 -176 Z" fill="{trunk}" stroke="#0D0D0F" stroke-width="2.4"></path>')
    clumps = "".join(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(rr)}" fill="{r.choice(leaf)}" stroke="#0D0D0F" stroke-width="2"></circle>'
                     for cx, cy, rr in [(r.uniform(-240, 280), r.uniform(-330, -190), r.uniform(36, 60)) for _ in range(26)])
    return f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">{boughs}{clumps}</g>'

def bough_over(x, y, s=1.0, seed=2, dark=False):
    """A few leafy clumps and twigs drawn over Absalom's head where it is caught."""
    r = random.Random(seed)
    leaf = ["#1A2A1A", "#22301E"] if dark else ["#3F8A44", "#2E6A32", "#5E8F26"]
    twigs = "".join(f'<path d="M{f(x + r.uniform(-30, 30))} {f(y - 30 * s)} L {f(x + r.uniform(-24, 24))} {f(y + 10 * s)}" stroke="#2A1A14" stroke-width="{f(3 * s)}"></path>' for _ in range(5))
    clumps = "".join(f'<circle cx="{f(x + r.uniform(-50, 50) * s)}" cy="{f(y - r.uniform(10, 50) * s)}" r="{f(r.uniform(18, 28) * s)}" fill="{r.choice(leaf)}" stroke="#0D0D0F" stroke-width="2"></circle>' for _ in range(6))
    return twigs + clumps

def balance(x, y, s=1.0):
    """A merchant's balance: a beam on a post, the hair heaped in one pan, the weights in the other."""
    pan = lambda px, py: f'<path d="M{px - 40} {py} C {px - 30} {py + 18} {px + 30} {py + 18} {px + 40} {py} Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2"></path>'
    cords = lambda px, py: f'<path d="M{px} -150 L {px - 38} {py} M{px} -150 L {px + 38} {py}" stroke="#5A3A22" stroke-width="1.6"></path>'
    hair = '<path d="M-150 -70 C -150 -100 -110 -110 -96 -86 C -90 -100 -60 -100 -60 -74 L -60 -68 L -150 -68 Z" fill="#1A1210" stroke="#0D0D0F" stroke-width="2"></path>' + "".join(f'<path d="M{-146 + i * 10} -70 C {-140 + i * 10} -84 {-136 + i * 10} -92 {-130 + i * 10} -96" fill="none" stroke="#4A3A2E" stroke-width="1.4"></path>' for i in range(8))
    weights = "".join(f'<rect x="{60 + i * 22}" y="{-78 - (i % 2) * 6}" width="18" height="{10 + (i % 2) * 6}" fill="#8A8A9A" stroke="#0D0D0F" stroke-width="1.6"></rect>' for i in range(4))
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
            '<path d="M-40 0 L 40 0 L 10 -10 L 10 -150 L -10 -150 L -10 -10 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M-108 -150 L 108 -150" stroke="#0D0D0F" stroke-width="8" stroke-linecap="round"></path><path d="M-108 -150 L 108 -150" stroke="#E8B830" stroke-width="4" stroke-linecap="round"></path>'
            + cords(-105, -66) + cords(105, -66) + hair + pan(-105, -68) + weights + pan(105, -68) + '</g>')

def gatehouse(x, base, w, h, lit=False, watchman=None):
    """A city gate: two towers, an arched gateway, the chamber over the gate with its window, and the roof above."""
    win = "#FFC14D" if lit else "#12090A"
    o = (f'<rect x="{f(x - w/2)}" y="{f(base - h)}" width="{f(w)}" height="{f(h)}" fill="#B59A7A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
         + "".join(f'<rect x="{f(x - w/2 + i * w / 8)}" y="{f(base - h - 16)}" width="{f(w / 16)}" height="16" fill="#B59A7A" stroke="#0D0D0F" stroke-width="2"></rect>' for i in range(8))
         + f'<path d="M{f(x - w*0.18)} {f(base)} L {f(x - w*0.18)} {f(base - h*0.4)} C {f(x - w*0.18)} {f(base - h*0.62)} {f(x + w*0.18)} {f(base - h*0.62)} {f(x + w*0.18)} {f(base - h*0.4)} L {f(x + w*0.18)} {f(base)} Z" fill="#2A1A14" stroke="#0D0D0F" stroke-width="2.4"></path>'
         + f'<rect x="{f(x - w*0.1)}" y="{f(base - h*0.86)}" width="{f(w*0.2)}" height="{f(h*0.16)}" fill="{win}" stroke="#0D0D0F" stroke-width="2"></rect>'
         + f'<path d="M{f(x)} {f(base - h*0.86)} L {f(x)} {f(base - h*0.7)}" stroke="#0D0D0F" stroke-width="2"></path>'
         + "".join(f'<path d="M{f(x - w/2)} {f(base - h + k * h / 6)} L {f(x + w/2)} {f(base - h + k * h / 6)}" stroke="#9A7E5E" stroke-width="1.4"></path>' for k in range(1, 6)))
    if lit:
        o += f'<rect x="{f(x - w*0.1)}" y="{f(base - h*0.86)}" width="{f(w*0.2)}" height="{f(h*0.16)}" fill="#FFF4C2" opacity="0.4"></rect>'
    return o

def runner(p, x, y, s, flip=False, cloth="#F3EFE6", body="#3A1E14"):
    return (mk.person(p, round(x), round(y), round(s, 3), body=body, cloth=cloth, kind="Tunic", sw=4, flip=flip, up=[(-22, -158), (-46, -140), (-60, -160)])
            + mk.speed(x - (60 if not flip else -60) * s, y - 90 * s, 10, 20 * s, 120 * s, int(x), color="#F3EFE6", op=0.6))

def stone_heap(cx, base, w, h, seed=1):
    r = random.Random(seed); o = []
    rows = 6
    for k in range(rows):
        rw = w * (1 - k / rows); yy = base - k * h / rows
        for i in range(max(1, int(rw / 26))):
            sx = cx - rw / 2 + 13 + i * 26 + r.uniform(-4, 4)
            o.append(f'<ellipse cx="{f(sx)}" cy="{f(yy - 8)}" rx="{f(r.uniform(12, 16))}" ry="{f(r.uniform(8, 11))}" fill="{r.choice(["#8A8478", "#A89E92", "#7A746A"])}" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    return "".join(o)

def threshing_floor(cx, base, w):
    return (f'<ellipse cx="{f(cx)}" cy="{f(base)}" rx="{f(w/2)}" ry="{f(w*0.12)}" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
            f'<ellipse cx="{f(cx)}" cy="{f(base)}" rx="{f(w*0.4)}" ry="{f(w*0.09)}" fill="none" stroke="#C9A86A" stroke-width="2" stroke-dasharray="8 6"></ellipse>')

def altar(x, y, s=1.0, fire=True, seed=1):
    """An altar of unhewn stones with the fire of the burnt-offering and its smoke."""
    r = random.Random(seed)
    stones = "".join(f'<rect x="{f(-60 + i * 30 + (k % 2) * 15)}" y="{f(-24 - k * 22)}" width="28" height="20" rx="5" fill="{r.choice(["#A89E92", "#8A8478", "#B8AE9E"])}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                     for k in range(5) for i in range(4 - (1 if k % 2 else 0)))
    fl = ""
    if fire:
        fl = ('<path d="M-46 -112 C -50 -150 -20 -160 -24 -200 C 0 -170 10 -190 6 -230 C 34 -190 50 -170 40 -112 Z" fill="#FF8A3D" stroke="#0D0D0F" stroke-width="2"></path>'
              '<path d="M-26 -112 C -28 -140 -8 -146 -10 -172 C 6 -150 20 -156 18 -112 Z" fill="#FFD23F"></path>'
              '<path d="M0 -230 C -30 -280 30 -320 0 -380 C -30 -430 20 -470 0 -520" fill="none" stroke="#D8D2C6" stroke-width="18" opacity="0.5" stroke-linecap="round"></path>')
    return f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><rect x="-64" y="-112" width="128" height="10" fill="#7A746A"></rect>{stones}{fl}</g>'
