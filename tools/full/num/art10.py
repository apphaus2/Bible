"""New drawings for Numbers chapter 10 (Numbers 20–21): Miriam's grave at Kadesh, the messengers before the king of Edom
and Edom coming out with a strong hand, mount Hor (Aaron, Eleazar and Moses going up; Eleazar coming down in Aaron's
garments; the mourning thirty days), the journeys from mount Hor to Pisgah as a map, the well at Beer dug with sceptres and
staves, and the wars with Sihon and Og as distant hosts. Aaron's death (20:28) is told in a caption over the empty summit."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, ruth1 as R, numbers1 as N
from faces_ex import F
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man, woman, king, grid_bg, node, route
from exo import art as A, art8 as B8, art9 as Q
from num.art import ALL, wilderness_camp, standard, TRIBE_C
def f(v): return f"{v:.1f}"

EDOM_KING = F("adam", skin="#B9785A", shadow="#5A2A1A", hair="#8A3A1A", hl="#B85A2A", beard=True, beard_color="#8A3A1A", scarf="#8A2A1A", band=True, brow="scowl", light="#FF6A2A")
ELEAZAR = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E", scarf="#F3EFE6", band=True, light="#FFD23F")

def miriam_grave(p, w, h, seed):
    """Kadesh in the wilderness of Zin: a new grave of heaped stones, women mourning beside it."""
    r = random.Random(seed); b = h * 0.9
    o = [mk.defs(p, *ALL), sun(w * 0.86, h * 0.18, 16, color="#FF8A3D", op=0.3), hills(w, h, h * 0.46, seed, color="#A8542A", amp=14), ground(w, h, h * 0.56, "#C8946A", dy=0)]
    o.append(R.graves(w * 0.5, b - 6, 1, min(2.6, h / 120)))
    s = fit(b, h * 0.5)
    for i, x in enumerate((0.16, 0.26, 0.74, 0.84)):
        o.append(woman(p, w * x, b, s, ["#C2456A", "#6A3A5A", "#4A3A6A", "#8A5A3A"][i], flip=x > 0.5))
    return "".join(o)

def edom(p, w, h, seed, army=False):
    """The king of Edom upon his walls above the king's highway (army=True: Edom come out against Israel with much people)."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), sun(w * 0.84, h * 0.16, 14, color="#FF8A3D", op=0.3)]
    o.append(f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.3)} {f(h * 0.2)} L {f(w * 0.5)} {f(h * 0.34)} L {f(w * 0.75)} {f(h * 0.14)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h)} L -10 {f(h)} Z" fill="#B5442A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(f'<path d="M{f(w * 0.08)} {f(h)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.5)} {f(h * 0.64)} {f(w * 0.62)} {f(h * 0.46)}" fill="none" stroke="#E8C88A" stroke-width="{f(h * 0.06)}" opacity="0.8"></path>')
    o.append(label(w * 0.34, h * 0.78, "THE KING'S HIGHWAY", "#3A1A0A", 9))
    wx = w * 0.62
    o.append(f'<rect x="{f(wx)}" y="{f(h * 0.28)}" width="{f(w * 0.3)}" height="{f(h * 0.18)}" fill="#8A4A3A" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(wx + i * w * 0.03)}" y="{f(h * 0.25)}" width="{f(w * 0.018)}" height="{f(h * 0.03)}" fill="#8A4A3A" stroke="#0D0D0F" stroke-width="1.4"></rect>' for i in range(10)))
    o.append(king(p, wx + w * 0.08, h * 0.28, fit(h * 0.28, h * 0.12), "#8A2A1A"))
    if army:
        for i in range(16):
            x = w * (0.5 + (i % 8) * 0.06); y = h * (0.62 + (i // 8) * 0.14)
            o.append(man(p, x, y, fit(y, y - h * 0.18), "#5A1A1A", flip=True, up=[(-22, -158), (-28, -196), (-30, -240)]))
            o.append(f'<path d="M{f(x - 28 * fit(y, y - h * 0.18))} {f(y - 240 * fit(y, y - h * 0.18))} L {f(x - 30 * fit(y, y - h * 0.18))} {f(y - 330 * fit(y, y - h * 0.18))}" stroke="#3A2214" stroke-width="2"></path>')
    else:
        for i in range(3): o.append(man(p, w * (0.14 + i * 0.07), b, fit(b, h * 0.5), "#7A6A4A"))
    return "".join(o)

def hor(p, w, h, seed, stage=0):
    """Mount Hor by the border of Edom: (0) Moses, Aaron and Eleazar going up in the sight of all the congregation;
    (1) the summit, empty under the sky; (2) Moses and Eleazar coming down, Eleazar in the high priest's garments."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{"#E8B880" if stage != 1 else "#5B2470"}"></rect>']
    if stage == 1: o.append(mk.stars(40, w, h * 0.5, seed) + V.rays(w * 0.5, h * 0.2, 30, 20, w, color="#FFF4C2", op=0.25))
    o.append(f'<path d="M-10 {f(h)} L {f(w * 0.5)} {f(h * 0.16)} L {f(w * 0.62)} {f(h * 0.2)} L {f(w + 10)} {f(h)} Z" fill="#8A4A3A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    s = fit(h * 0.5, h * 0.32)
    if stage == 0:
        for i, fn in enumerate((A.moses, A.aaron, Q.son_priest)):
            t = 0.4 + i * 0.08; x = w * (0.18 + 0.32 * t); y = h * (0.92 - 0.76 * t)
            o.append(fn(p, x, y, fit(y, y - h * 0.26)))
        for i in range(10): o.append(man(p, w * (0.6 + i * 0.04), h * 0.98, fit(h * 0.98, h * 0.86), r.choice(A.HEBREW), flip=True))
    elif stage == 2:
        for i, fn in enumerate((A.moses, Q.high_priest)):
            t = 0.5 - i * 0.1; x = w * (0.5 + 0.4 * (1 - t)); y = h * (0.92 - 0.6 * t)
            o.append(fn(p, x, y, fit(y, y - h * 0.34), flip=True))
    return "".join(o)

def mourning(p, w, h, seed):
    """All the house of Israel weeping for Aaron thirty days: the camp under a darkening sky, people bowed at their tents."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#3A2A4A"></rect>', ground(w, h, h * 0.56, "#4A3A4A", dy=0)]
    for i in range(7):
        x = w * (0.06 + i * 0.14)
        o.append(A.black_tent(x + w * 0.04, b - 8, w * 0.12, h * 0.26) + E.kneel(x, b, fit(b, h * 0.6) * 0.8, color=r.choice(A.HEBREW), skin="#8A5A3E"))
    o.append(label(w * 0.94, h * 0.5, "三十日 · THIRTY DAYS", "#FFD23F", 12, "end"))
    return "".join(o)

def journeys(w, h, hi=None):
    """From mount Hor round Edom by the way to the Red Sea, then Oboth, Iye-abarim, the valley of Zered, beyond the Arnon,
    Beer, Mattanah, Nahaliel, Bamoth, the top of Pisgah; Heshbon and Jazer; Edrei in Bashan."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.3)} -10 C {f(w * 0.28)} {f(h * 0.3)} {f(w * 0.32)} {f(h * 0.5)} {f(w * 0.3)} {f(h * 0.62)}" fill="none" stroke="#8FD0E2" stroke-width="3"></path>'
             f'<ellipse cx="{f(w * 0.3)}" cy="{f(h * 0.7)}" rx="{f(w * 0.03)}" ry="{f(h * 0.1)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>' + label(w * 0.26, h * 0.3, "JORDAN", "#8FD0E2", 8, "end"))
    o.append(f'<path d="M{f(w * 0.36)} {f(h * 0.62)} L {f(w * 0.92)} {f(h * 0.6)}" stroke="#E8C88A" stroke-width="1.4" stroke-dasharray="3 4"></path>' + label(w * 0.9, h * 0.58, "THE ARNON", "#E8C88A", 8, "end"))
    pts = [("MOUNT HOR", 0.2, 0.96), ("OBOTH", 0.52, 0.9), ("IYE-ABARIM", 0.62, 0.8), ("ZERED", 0.66, 0.72), ("ARNON", 0.6, 0.62), ("BEER", 0.56, 0.5),
           ("MATTANAH", 0.53, 0.43), ("NAHALIEL", 0.49, 0.36), ("BAMOTH", 0.44, 0.3), ("PISGAH", 0.37, 0.24)]
    P = [(w * x, h * y) for _, x, y in pts]
    o.append(route(P, color="#FFD23F"))
    for i, (nm, x, y) in enumerate(pts):
        o.append(node(w * x, h * y, nm, "#FFD23F" if hi is None or nm in hi else "#6A7A8A", r=4, dy=-8 if i % 2 else 14, size=8))
    for nm, x, y in (("HESHBON", 0.36, 0.44), ("JAZER", 0.46, 0.16), ("EDREI · BASHAN", 0.56, 0.06)):
        o.append(node(w * x, h * y, nm, "#D7261E" if hi is None or nm in hi else "#6A3A3A", r=4, dy=-8, size=8))
    return "".join(o)

def well(p, w, h, seed):
    """The well at Beer, which the princes digged with the sceptre and with their staves, the people singing about it."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), sun(w * 0.86, h * 0.14, 14, op=0.25), ground(w, h, h * 0.5, "#C8A06A", dy=0)]
    cx = w * 0.5
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(h * 0.74)}" rx="{f(w * 0.12)}" ry="{f(h * 0.06)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(h * 0.72)}" rx="{f(w * 0.08)}" ry="{f(h * 0.03)}" fill="#8FD0E2"></ellipse>')
    o.append("".join(f'<path d="M{f(cx + (i - 2) * 10)} {f(h * 0.7)} C {f(cx + (i - 2) * 16)} {f(h * 0.5)} {f(cx + (i - 2) * 22)} {f(h * 0.46)} {f(cx + (i - 2) * 30)} {f(h * 0.6)}" fill="none" stroke="#8FD0E2" stroke-width="3" stroke-linecap="round"></path>' for i in range(5)))
    s = fit(b, h * 0.5)
    for i, x in enumerate((0.22, 0.32, 0.68, 0.78)):
        o.append(A.elder(r.choice(A.CLOTHS), i)(p, w * x, b, s, flip=x > 0.5, up=[(-22, -158), (-6, -130), (10, -100)]))
        o.append(f'<path d="M{f(w * x + (8 if x < 0.5 else -8) * s)} {f(b - 110 * s)} L {f(w * x + (40 if x < 0.5 else -40) * s)} {f(b - 4)}" stroke="#5A3A22" stroke-width="{f(5 * s)}" stroke-linecap="round"></path>')
    return "".join(o)

def host(p, w, h, seed, foe="#5A3A2A", city=True, giant=False):
    """Israel against a king of the Amorites (Sihon at Jahaz, Og at Edrei): two hosts at a distance, a city on its hill."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), sun(w * 0.5, h * 0.3, 30, color="#FF8A3D", op=0.3), hills(w, h, h * 0.44, seed, color="#6A4A3A", amp=16), ground(w, h, h * 0.56, "#8A6A4A", dy=0)]
    if city:
        cx = w * 0.82
        o.append(f'<path d="M{f(cx - w * 0.14)} {f(h * 0.5)} L {f(cx - w * 0.08)} {f(h * 0.3)} L {f(cx + w * 0.08)} {f(h * 0.3)} L {f(cx + w * 0.14)} {f(h * 0.5)} Z" fill="#7A5A3A" stroke="#0D0D0F" stroke-width="2"></path>'
                 + "".join(f'<rect x="{f(cx - w * 0.07 + i * w * 0.035)}" y="{f(h * 0.22)}" width="{f(w * 0.03)}" height="{f(h * 0.08)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="1.4"></rect>' for i in range(4)))
    for side in (0, 1):
        for i in range(9):
            x = w * (0.06 + i * 0.045) if side == 0 else w * (0.58 + i * 0.045); y = b - (i % 3) * h * 0.04
            sc = fit(y, y - h * 0.22) * (1.5 if (giant and side == 1 and i == 4) else 1)
            o.append(man(p, x, y, sc, r.choice(A.HEBREW) if side == 0 else foe, flip=side == 1, up=[(-22, -158), (-26, -200), (-28, -236)]))
            o.append(f'<path d="M{f(x - 28 * sc * (1 if side == 0 else -1))} {f(y - 236 * sc)} L {f(x - 30 * sc * (1 if side == 0 else -1))} {f(y - 330 * sc)}" stroke="#3A2214" stroke-width="2"></path>')
    if not giant: o.append(standard(w * 0.42, b, fit(b, h * 0.4) * 1.6, TRIBE_C["JUDAH"], pole=140))
    return "".join(o)
