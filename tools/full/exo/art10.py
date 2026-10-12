"""New drawings for Exodus chapter 10 (Exodus 32–34): the golden rings brought to Aaron, the gate of the camp at dusk,
the people mourning without their ornaments, the tent of meeting pitched without the camp and the pillar of cloud at its
door, Moses hewing the tables and climbing at dawn, the cloud on the mount, Moses bowed, and the veil on his face.
The judgment of 32:27–28 is never shown: an empty gate under a red sky and a count."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4, exodus5 as V
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art10 as T
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import sun, label, man, woman
from exo import art as A
def f(v): return f"{v:.1f}"

AARON_FEAR, MOSES_SHINE = A.tok("AARON_FEAR"), A.tok("MOSES_SHINE")
AARON_PLEAD = F("adam", skin="#C98E66", shadow="#6A4A5A", hair="#9A968E", hl="#6A665E", beard=True, scarf="#4A6A9A", cord=True, brow="sorrow", light="#FF8A3D")
MOSES_VEIL = (F("adam", skin="#C98E66", shadow="#8A5A3E", hair="#2A1A10", hl="#5A4A3E", beard=True, scarf="#E2D8C4", cord=True, light="#FFFFFF")
              + '<path d="M150 150 C 200 136 250 140 268 150 L 262 300 C 230 316 190 314 156 300 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2.4" opacity="0.96"></path>'
              + '<path d="M170 170 L 172 296 M200 166 L 200 306 M230 166 L 228 304" stroke="#C8C2B6" stroke-width="2"></path>')

def rings(p, w, h, seed):
    """All the people brake off the golden rings which were in their ears, and brought them unto Aaron: a heap of gold at his feet."""
    r = random.Random(seed); b = h * 0.9
    o = [sun(w * 0.86, h * 0.2, 14, color="#FF8A3D", op=0.3), E4.sinai(w * 0.86, h * 0.6, w * 0.3, h * 0.46, seed, fire=False), ground(w, h, h * 0.6, "#8A6A4A", dy=0)]
    o.append(A.aaron(p, w * 0.5, b, fit(b, h * 0.38)))
    hx = w * 0.58
    o.append(f'<path d="M{f(hx - 40)} {f(b + 2)} C {f(hx - 30)} {f(b - 26)} {f(hx + 30)} {f(b - 26)} {f(hx + 40)} {f(b + 2)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<circle cx="{f(hx + r.uniform(-30, 30))}" cy="{f(b - r.uniform(2, 18))}" r="4" fill="none" stroke="#FFF4C2" stroke-width="1.6"></circle>' for _ in range(16)))
    for i, x in enumerate((0.12, 0.22, 0.32, 0.72, 0.82, 0.92)):
        o.append((woman if i % 2 else man)(p, w * x, b - (i % 2) * 6, fit(b, h * 0.44), r.choice(A.HEBREW + ["#C2456A", "#5A6E8A"]), flip=x > 0.5, up=T.POSES["reach"]))
    return "".join(o)

def gate(w, h, seed, red=True):
    """The gate of the camp at dusk: two posts, the tents behind; no one is shown slain."""
    b = h * 0.88
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{"#3A0A10" if red else "#1A1430"}"></rect>', sun(w * 0.5, b, 40, color="#D7261E", op=0.3),
         ground(w, h, b, "#1A0A0E", dy=0)]
    o += [A.black_tent(w * x, b, w * 0.1, h * 0.14, color="#0D0D0F", lit="#5A1A1E") for x in (0.08, 0.2, 0.8, 0.92)]
    o.append(f'<rect x="{f(w * 0.36)}" y="{f(b - h * 0.5)}" width="16" height="{f(h * 0.5)}" fill="#0D0D0F"></rect><rect x="{f(w * 0.62)}" y="{f(b - h * 0.5)}" width="16" height="{f(h * 0.5)}" fill="#0D0D0F"></rect>'
             f'<rect x="{f(w * 0.34)}" y="{f(b - h * 0.54)}" width="{f(w * 0.3)}" height="14" fill="#0D0D0F"></rect>')
    return "".join(o)

def mourning(p, w, h, seed):
    """They mourned: and no man did put on him his ornaments: the people in dark robes, heads bowed, the ornaments laid in a heap."""
    r = random.Random(seed); b = h * 0.9
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A3450"></rect>', E4.sinai(w * 0.8, h * 0.56, w * 0.4, h * 0.46, seed, fire=False), ground(w, h, h * 0.56, "#4A4A5A", dy=0)]
    for i in range(10):
        x = w * (0.06 + i * 0.075); y = b - (i % 3) * 8
        o.append(E.kneel(x, y, fit(y, h * 0.5) * 0.9, color=r.choice(["#3A3430", "#4A3A3E", "#2A2A3A", "#5A4A4E"]), skin="#6A4A3A", flip=i % 2 == 1))
    o.append(f'<g transform="translate({f(w * 0.78)} {f(b - h * 0.2)})">' + A.jewels(w * 0.2, h * 0.22, seed) + '</g>')
    return "".join(o)

def tent_without(p, w, h, seed, cloud=False, worship=False):
    """Moses pitched the tent without the camp, afar off; the people stood every man at his tent door and looked after him.
    cloud=True: the pillar of cloud stands at the door of the Tent; worship=True: the people bow at their doors."""
    r = random.Random(seed); b = h * 0.9
    o = [sun(w * 0.9, h * 0.16, 14, op=0.25), E4.sinai(w * 0.5, h * 0.52, w * 0.9, h * 0.44, seed, fire=False), ground(w, h, h * 0.52, "#8A6A4A", dy=0)]
    tx = w * 0.8
    o.append(A.black_tent(tx, h * 0.72, w * 0.22, h * 0.2, color="#8A3A2A", lit="#FFE680") + label(tx, h * 0.78, "THE TENT OF MEETING", "#F3EFE6", 8))
    if cloud: o.append(E3.pillar_cloud(tx - w * 0.06, h * 0.7, -20, w * 0.05, seed))
    else: o.append(A.moses(p, tx - w * 0.12, h * 0.74, fit(h * 0.74, h * 0.6), up=T.HOLD_STAFF))
    for i, x in enumerate((0.06, 0.18, 0.3, 0.42)):
        o.append(A.black_tent(w * x, b - 6, w * 0.1, h * 0.14))
        if worship: o.append(E.kneel(w * x + w * 0.05, b, fit(b, h * 0.62) * 0.9, color=r.choice(A.HEBREW), skin="#8A5A3E", flip=True))
        else: o.append(man(p, w * x + w * 0.05, b, fit(b, h * 0.6), r.choice(A.HEBREW), flip=True))
    return "".join(o)

def hewing(p, w, h, seed):
    """Hew thee two tables of stone like unto the first: Moses with a hammer at a block of grey stone, two slabs cut."""
    b = h * 0.88
    o = [sun(w * 0.86, h * 0.2, 14, op=0.25), E4.sinai(w * 0.7, b, w * 0.6, h * 0.66, seed, fire=False), ground(w, h, b, "#8A6A4A", dy=0)]
    o.append(f'<path d="M{f(w * 0.36)} {f(b)} L {f(w * 0.38)} {f(b - h * 0.24)} L {f(w * 0.56)} {f(b - h * 0.26)} L {f(w * 0.58)} {f(b)} Z" fill="#8A8478" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(V.tables(w * 0.48, b - h * 0.36, min(0.5, h / 520), uid=f"hw{seed}", glow=False))
    o.append(A.moses(p, w * 0.24, b, fit(b, h * 0.42), up=[(-22, -158), (-2, -196), (22, -206)]))
    return "".join(o)

def climbing(p, w, h, seed):
    """Moses rose up early in the morning, and went up unto mount Sinai, and took in his hand two tables of stone: dawn on the slope."""
    b = h * 0.92
    o = [sun(w * 0.18, h * 0.5, 30, color="#FFC14D", op=0.35), E4.sinai(w * 0.55, b, w * 1.0, h * 0.86, seed, fire=False)]
    o.append(f'<path d="M{f(w * 0.2)} {f(b)} C {f(w * 0.35)} {f(h * 0.7)} {f(w * 0.45)} {f(h * 0.5)} {f(w * 0.55)} {f(h * 0.2)}" fill="none" stroke="#C8A06A" stroke-width="3" stroke-dasharray="6 6"></path>')
    s = fit(h * 0.6, h * 0.36)
    o.append(A.moses(p, w * 0.44, h * 0.6, s, up=[(-22, -158), (-6, -150), (14, -150)]) + V.tables(w * 0.44 + 14 * s, h * 0.6 - 150 * s, s * 0.2, uid=f"cl{seed}", glow=False))
    return "".join(o)

def cloud_mount(w, h, seed):
    """Jehovah descended in the cloud, and stood with him there: the summit wrapped in bright cloud; Moses small upon it."""
    b = h * 0.96
    return (V.rays(w * 0.5, h * 0.2, 36, 20, max(w, h) * 1.2, color="#FFF4C2", op=0.3) + E4.sinai(w * 0.5, b, w * 1.0, h * 0.8, seed, fire=False)
            + "".join(f'<circle cx="{f(w * (0.3 + 0.08 * i))}" cy="{f(h * (0.22 + 0.04 * (i % 2)))}" r="{f(h * 0.12)}" fill="#F3EFE6" opacity="0.85" stroke="#C8C2B6" stroke-width="2"></circle>' for i in range(6)))

def bowed(p, w, h, seed):
    """Moses made haste, and bowed his head toward the earth, and worshipped: kneeling on the summit with the two tables beside him."""
    b = h * 0.86
    return (V.rays(w * 0.5, -40, 30, 20, h * 1.4, color="#FFF4C2", op=0.3) + f'<path d="M-10 {f(h + 10)} L {f(w * 0.3)} {f(b)} L {f(w * 0.7)} {f(b - 6)} L {f(w + 10)} {f(h + 10)} Z" fill="#4A3A3E" stroke="#0D0D0F" stroke-width="2.4"></path>'
            + E.kneel(w * 0.46, b, fit(b, h * 0.5) * 0.9, color=A.MOSES_ROBE, skin="#C98E66") + V.tables(w * 0.66, b - h * 0.16, min(0.4, h / 600), uid=f"bw{seed}", glow=True))

def shining(p, w, h, seed):
    """When Moses came down from the mount with the two tables, the skin of his face shone: Aaron and the people draw back."""
    r = random.Random(seed); b = h * 0.9
    o = [E4.sinai(w * 0.2, h * 0.6, w * 0.5, h * 0.5, seed, fire=False), ground(w, h, h * 0.6, "#8A6A4A", dy=0)]
    mx = w * 0.32; s = fit(b, h * 0.36)
    o.append(V.rays(mx, b - 186 * s, 24, 10 * s, 70 * s, color="#FFF4C2", op=0.7))
    o.append(A.moses(p, mx, b, s, up=[(-22, -158), (-6, -150), (14, -150)]) + V.tables(mx + 14 * s, b - 150 * s, s * 0.2, uid=f"sh{seed}", glow=False))
    o.append(A.aaron(p, w * 0.62, b, fit(b, h * 0.4), flip=True, up=T.POSES["reach"]))
    for i, x in enumerate((0.72, 0.8, 0.88, 0.96)):
        o.append(man(p, w * x, b - (i % 2) * 6, fit(b, h * 0.44), r.choice(A.HEBREW), flip=True))
    return "".join(o)
