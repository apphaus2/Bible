"""Generators and faces for 2 Samuel Book One: David as king (crowned, dancing in a linen ephod), musicians with
timbrels, cymbals and harps, a palace window, a house of cedar, the king's table, a sealed letter, the palace roof
at eventide, Nathan's parable of the ewe lamb, and new faces (David as king, Nathan, Michal, Mephibosheth)."""
import random, math
import mk, exodus4 as Z, samuel2 as B
from faces_ex import F
def f(v): return f"{v:.1f}"

def tokens():
    t = B.tokens()
    k = dict(skin="#D99A72", shadow="#8A4A2E", hair="#8A3A1E", hl="#C8703A", beard=True, beard_color="#7A3218", band=True)
    t["__FACE_DAVID_KING__"] = F("adam", scarf="#4A2A7A", light="#FFE680", **k)
    t["__FACE_DAVID_KING_JOY__"] = F("adam", scarf="#F3EFE6", laugh=True, light="#FFE680", **k)
    t["__FACE_DAVID_KING_WRATH__"] = F("adam", scarf="#4A2A7A", brow="scowl", light="#FF6A4A", **k)
    t["__FACE_DAVID_KING_GRIEF__"] = F("adam", scarf="#4A2A7A", brow="sorrow", tear=True, **k)
    t["__FACE_DAVID_MOURN__"] = F("adam", skin="#C89A7E", shadow="#5A3A4A", hair="#8A3A1E", hl="#9A502A", stubble="#7A3218", brow="sorrow", tear=True)
    t["__FACE_NATHAN__"] = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#6A665E", hl="#9A968E", beard=True, beard_color="#7A766E", scarf="#5E7A4A", cord=True)
    t["__FACE_NATHAN_STERN__"] = F("adam", skin="#C98E66", shadow="#5A2A2A", hair="#6A665E", hl="#9A968E", beard=True, beard_color="#7A766E", scarf="#5E7A4A", cord=True, brow="scowl", light="#FFD23F")
    t["__FACE_MICHAL__"] = F("eve", skin="#D9A27A", shadow="#6A3A4A", hair="#1A1210", scarf="#8A1E2E", band=True, brow="scowl")
    t["__FACE_MEPHIBOSHETH__"] = F("adam", skin="#D9A27A", shadow="#6A4A5A", hair="#2A1A10", hl="#5A4A3E", stubble="#2A1A10", scarf="#1F5FAD", brow="sorrow")
    return t

KING = B.crown(0, -194, 0.42)
DAVID_K = dict(body="#5A2A16", cloth="#4A2A7A", kind="Tunic", sw=4)
NATHAN = dict(body="#3A1E14", cloth="#5E7A4A", kind="Tunic", sw=4)

def dancer(x, y, s, uid, left, right, cloth="#F3EFE6", body="#5A2A16", crown=True):
    """David dancing in a linen ephod, both arms up (left/right = arm points from each shoulder)."""
    return (f'<defs><path id="{uid}B" d="{Z.MAN_BOTH}"></path><path id="{uid}T" d="{mk.TUNIC}"></path></defs>'
            f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})" fill="{body}"><use href="#{uid}B"></use>'
            f'<use href="#{uid}T" fill="{cloth}" stroke="#0D0D0F" stroke-width="3"></use>'
            '<path d="M-20 -150 L 20 -150 M-24 -120 L 24 -120" stroke="#C9A86A" stroke-width="2"></path>'
            + mk.arm(left, body, 10) + mk.arm(right, body, 10) + (KING if crown else "") + '</g>')

def timbrel(x, y, s=1.0):
    jingles = "".join(f'<circle cx="{f(15 * math.cos(a))}" cy="{f(15 * math.sin(a))}" r="2.6" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></circle>' for a in [i * 1.047 for i in range(6)])
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><circle cx="0" cy="0" r="17" fill="#F3E0B8" stroke="#0D0D0F" stroke-width="2"></circle>'
            f'<circle cx="0" cy="0" r="17" fill="none" stroke="#8A5A30" stroke-width="4"></circle>{jingles}</g>')

def cymbals(x, y, s=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
            '<ellipse cx="-12" cy="0" rx="5" ry="16" fill="#E8B830" stroke="#0D0D0F" stroke-width="2" transform="rotate(-20 -12 0)"></ellipse>'
            '<ellipse cx="12" cy="0" rx="5" ry="16" fill="#E8B830" stroke="#0D0D0F" stroke-width="2" transform="rotate(20 12 0)"></ellipse>'
            '<path d="M-2 -18 L 2 -26 M-6 18 L -10 24 M6 18 L 10 24" stroke="#FFF4C2" stroke-width="2"></path></g>')

def musician(p, x, y, s, kind="timbrel", cloth="#C2456A", woman=True, seed=0):
    """A man or woman playing a timbrel or cymbals held up, or a harp at the chest."""
    if kind == "harp":
        return mk.person(p, round(x), round(y), round(s, 3), body="#3A1E14", cloth=cloth, woman=woman, hair=woman, sw=4,
                         up=[(-22, -158), (-30, -128), (-6, -118)], extra=B.harp(2, -96, 0.6))
    inst = timbrel(-34, -246, 1.1) if kind == "timbrel" else cymbals(-34, -246, 1.0)
    return mk.person(p, round(x), round(y), round(s, 3), body="#3A1E14", cloth=cloth, woman=woman, hair=woman, sw=4,
                     up=[(-22, -158), (-40, -200), (-34, -236)], extra=inst)

def notes(x, y, n, seed, color="#FFD23F"):
    r = random.Random(seed); o = []
    for _ in range(n):
        nx, ny = x + r.uniform(-60, 60), y + r.uniform(-40, 40)
        o.append(f'<ellipse cx="{f(nx)}" cy="{f(ny)}" rx="5" ry="4" fill="{color}" stroke="#0D0D0F" stroke-width="1.2" transform="rotate(-20 {f(nx)} {f(ny)})"></ellipse>'
                 f'<path d="M{f(nx + 4)} {f(ny)} L {f(nx + 4)} {f(ny - 18)} L {f(nx + 12)} {f(ny - 14)}" fill="none" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return "".join(o)

def window(x, y, w, h, inner="#12090A"):
    """An arched palace window in a stone wall (draw the face inside it afterwards)."""
    return (f'<path d="M{f(x - w/2 - 14)} {f(y + h + 14)} L {f(x - w/2 - 14)} {f(y - 14)} C {f(x - w/2 - 14)} {f(y - w*0.6 - 14)} {f(x + w/2 + 14)} {f(y - w*0.6 - 14)} {f(x + w/2 + 14)} {f(y - 14)} L {f(x + w/2 + 14)} {f(y + h + 14)} Z" fill="#C8B89A" stroke="#0D0D0F" stroke-width="2.4"></path>'
            f'<path d="M{f(x - w/2)} {f(y + h)} L {f(x - w/2)} {f(y)} C {f(x - w/2)} {f(y - w*0.55)} {f(x + w/2)} {f(y - w*0.55)} {f(x + w/2)} {f(y)} L {f(x + w/2)} {f(y + h)} Z" fill="{inner}" stroke="#0D0D0F" stroke-width="2.4"></path>'
            f'<rect x="{f(x - w/2 - 20)}" y="{f(y + h)}" width="{f(w + 40)}" height="14" fill="#A89A7E" stroke="#0D0D0F" stroke-width="2"></rect>')

def cedar(W, H, floor):
    """Cedar-panelled walls of David's house."""
    planks = "".join(f'<rect x="{x}" y="-10" width="40" height="{floor + 10}" fill="{c}" stroke="#3A1E10" stroke-width="1.4"></rect>'
                     for x, c in zip(range(-10, W + 10, 40), ["#8A4A26", "#9A5A30", "#7A3E20"] * 40))
    grain = "".join(f'<path d="M{x + 8} {y} c 6 10 -4 20 4 30" fill="none" stroke="#5A2A14" stroke-width="1" opacity="0.6"></path>' for x in range(-10, W, 40) for y in range(10, int(floor), 70))
    return (planks + grain + f'<rect x="-10" y="{f(floor - 16)}" width="{W + 20}" height="16" fill="#5A2A14"></rect>'
            + f'<path d="M-10 {f(floor)} L {W + 10} {f(floor)} L {W + 10} {H + 10} L -10 {H + 10} Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></path>')

def throne(x, y, s=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
            '<path d="M-40 0 L -40 -70 L -46 -170 L 46 -170 L 40 -70 L 40 0 Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M-34 -160 L 34 -160 L 30 -80 L -30 -80 Z" fill="#4A2A7A" stroke="#0D0D0F" stroke-width="2"></path>'
            '<rect x="-48" y="-78" width="96" height="14" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></rect>'
            '<circle cx="-46" cy="-170" r="7" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></circle><circle cx="46" cy="-170" r="7" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></circle></g>')

def table(x, y, w, s=1.0):
    """The king's table, set with loaves and cups."""
    loaves = "".join(f'<ellipse cx="{f(x - w/2 + 30 + i * (w - 60) / 4)}" cy="{f(y - 72*s)}" rx="{f(14*s)}" ry="{f(8*s)}" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>' for i in range(5))
    cups = "".join(f'<path d="M{f(x - w/2 + 50 + i * (w - 100) / 2)} {f(y - 68*s)} l {f(-6*s)} {f(-16*s)} l {f(12*s)} 0 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>' for i in range(3))
    return (f'<rect x="{f(x - w/2)}" y="{f(y - 66*s)}" width="{f(w)}" height="{f(12*s)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
            f'<path d="M{f(x - w/2 + 10)} {f(y - 54*s)} L {f(x - w/2 + 16)} {f(y)} M{f(x + w/2 - 10)} {f(y - 54*s)} L {f(x + w/2 - 16)} {f(y)}" stroke="#5A3A22" stroke-width="{f(6*s)}"></path>'
            f'<path d="M{f(x - w/2 + 4)} {f(y - 54*s)} L {f(x + w/2 - 4)} {f(y - 54*s)} L {f(x + w/2 - 14)} {f(y - 30*s)} L {f(x - w/2 + 14)} {f(y - 30*s)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path>'
            + loaves + cups)

def letter(x, y, s=1.0, rot=0, text=True):
    """A sealed letter: a rolled scroll with a clay seal."""
    lines = "".join(f'<path d="M-40 {-14 + i * 8} L 30 {-14 + i * 8}" stroke="#5A3A22" stroke-width="1.6" opacity="0.7"></path>' for i in range(4)) if text else ""
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">'
            '<rect x="-50" y="-24" width="100" height="44" fill="#F3E0B8" stroke="#0D0D0F" stroke-width="2"></rect>'
            '<ellipse cx="-50" cy="-2" rx="8" ry="24" fill="#E8D0A0" stroke="#0D0D0F" stroke-width="2"></ellipse>'
            '<ellipse cx="50" cy="-2" rx="8" ry="24" fill="#E8D0A0" stroke="#0D0D0F" stroke-width="2"></ellipse>'
            f'{lines}<circle cx="38" cy="12" r="9" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.6"></circle></g>')

def roof(W, H, top, seed=1):
    """The flat roof of the king's house with its parapet, and Jerusalem's rooftops below at eventide."""
    r = random.Random(seed); o = []
    for i in range(14):
        hx = i * W / 13 + r.uniform(-12, 12); hw = r.uniform(40, 70); hh = r.uniform(20, 50)
        o.append(f'<rect x="{f(hx - hw/2)}" y="{f(top + 40 - hh)}" width="{f(hw)}" height="{f(hh + 200)}" fill="{r.choice(["#5A3A4A", "#4A2E3E", "#6A4A5A"])}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
        if r.random() < 0.5:
            o.append(f'<rect x="{f(hx - 5)}" y="{f(top + 40 - hh + 10)}" width="10" height="12" fill="#FFC14D"></rect>')
    return ("".join(o)
            + f'<rect x="-10" y="{f(top + 60)}" width="{W + 20}" height="{H}" fill="#7A5A4A" stroke="#0D0D0F" stroke-width="2"></rect>'
            + "".join(f'<rect x="{x}" y="{f(top + 44)}" width="22" height="18" fill="#9A7A5A" stroke="#0D0D0F" stroke-width="1.6"></rect>' for x in range(-6, W, 40)))

def lamb_held(x, y, s=1.0):
    """A little ewe lamb held at the chest."""
    puffs = "".join(f'<circle cx="{px}" cy="{py}" r="{pr}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.2"></circle>' for px, py, pr in [(-8, 0, 8), (2, -4, 9), (12, 0, 8), (4, 6, 8)])
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">{puffs}<ellipse cx="22" cy="-6" rx="6" ry="5" fill="#2A1A10"></ellipse>'
            '<path d="M18 -10 L 14 -14" stroke="#2A1A10" stroke-width="2"></path></g>')

HOLD_LAMB = [(-22, -158), (-10, -128), (14, -124)]
