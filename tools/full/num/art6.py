"""New drawings for Numbers chapter 6 (Numbers 11–12): the fire of Jehovah at Taberah, the food remembered from Egypt,
the people weeping at their tent doors, the seventy elders about the Tent, the quails, the graves at Kibroth-hattaavah,
and Miriam shut up without the camp seven days. Faces: old Miriam (grey hair, pink headscarf), Miriam leprous (white as
snow, cold light), Aaron pleading, Joshua, the young man that ran."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, ruth1 as R, numbers1 as N
from faces_ex import F
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man, woman
from exo import art as A, art8 as B8
from num.art import ALL, wilderness_camp
from lev.art4 import days
def f(v): return f"{v:.1f}"

MIRIAM_OLD = A.tok("MIRIAM_OLD")
MIRIAM_SCOWL = F("eve", skin="#D9A27A", shadow="#9A6A4A", hair="#B8B2A6", scarf="#C2456A", brow="scowl", light="#FF8A3D")
MIRIAM_LEPROUS = F("eve", skin="#F3F1EC", shadow="#B8BCC8", hair="#B8B2A6", scarf="#C2456A", brow="sorrow", light="#CFE6FF")
YOUNG_MAN = F("adam", skin="#C98E66", shadow="#8A5A3E", hair="#2A1A10", hl="#5A4A3E", sweat=True, light="#FFC14D")
MIRIAM_C = "#C2456A"

def taberah(p, w, h, seed, abated=False):
    """The fire of Jehovah burning in the uttermost part of the camp; the people crying unto Moses (or the fire abated)."""
    r = random.Random(seed); b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{"#3A1408" if not abated else "#4A3A3A"}"></rect>',
         ground(w, h, h * 0.56, "#5A3A2A", dy=0), N.camp(14, w * 0.0, w * 0.6, h * 0.58, h * 0.74, seed, color=("#3A2214", "#4A3022", "#2A1A10"))]
    if not abated:
        for i in range(4):
            o.append(E.blaze(w * (0.68 + i * 0.09), h * 0.74, w * 0.12, h * (0.5 - (i % 2) * 0.1), seed + i))
    else:
        o.append("".join(f'<path d="M{f(w * (0.66 + i * 0.09))} {f(h * 0.72)} C {f(w * (0.66 + i * 0.09) - 20)} {f(h * 0.5)} {f(w * (0.66 + i * 0.09) + 20)} {f(h * 0.4)} {f(w * (0.66 + i * 0.09))} {f(h * 0.2)}" fill="none" stroke="#8A8478" stroke-width="10" opacity="0.5" stroke-linecap="round"></path>' for i in range(4)))
    s = fit(b, h * 0.48)
    o.append(A.moses(p, w * 0.12, b, s, up=[(-22, -158), (-6, -200), (8, -232)]))
    for i in range(5): o.append(E.kneel(w * (0.24 + i * 0.07), b, s * 0.9, color=r.choice(A.HEBREW), skin="#8A5A3E", flip=True))
    return "".join(o)

def egypt_food(w, h):
    """We remember the fish, which we did eat in Egypt for nought; the cucumbers, the melons, the leeks, the onions, the garlic."""
    b = h * 0.86; s = min(1.4, h / 140)
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#E8B830" opacity="0.25"></rect>', f'<path d="M0 {f(b)} L {f(w)} {f(b)}" stroke="#0D0D0F" stroke-width="2"></path>']
    items = []
    x = w * 0.08; step = w * 0.15
    # fish
    o.append(f'<g transform="translate({f(x)} {f(b - 14 * s)}) scale({f(s)})"><path d="M-30 0 C -14 -16 14 -16 26 0 C 14 16 -14 16 -30 0 Z" fill="#8FB8C8" stroke="#0D0D0F" stroke-width="2"></path><path d="M26 0 L 40 -12 L 40 12 Z" fill="#8FB8C8" stroke="#0D0D0F" stroke-width="2"></path><circle cx="-18" cy="-3" r="2.5" fill="#0D0D0F"></circle></g>')
    x += step
    o.append(f'<g transform="translate({f(x)} {f(b - 10 * s)}) scale({f(s)}) rotate(-12)"><rect x="-30" y="-9" width="60" height="18" rx="9" fill="#4A8A3A" stroke="#0D0D0F" stroke-width="2"></rect>' + "".join(f'<circle cx="{dx}" cy="-2" r="1.6" fill="#9CCB5E"></circle>' for dx in (-18, -6, 6, 18)) + '</g>')
    x += step
    o.append(f'<g transform="translate({f(x)} {f(b - 22 * s)}) scale({f(s)})"><ellipse cx="0" cy="0" rx="28" ry="22" fill="#5A9A4A" stroke="#0D0D0F" stroke-width="2"></ellipse>' + "".join(f'<path d="M{dx} -20 C {dx + 4} -6 {dx + 4} 6 {dx} 20" fill="none" stroke="#2E6B3A" stroke-width="2"></path>' for dx in (-14, 0, 14)) + '</g>')
    x += step
    o.append(f'<g transform="translate({f(x)} {f(b)}) scale({f(s)})"><rect x="-6" y="-26" width="12" height="26" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></rect><path d="M-6 -26 L -16 -60 M0 -26 L 0 -64 M6 -26 L 16 -60" stroke="#4A8A3A" stroke-width="5" stroke-linecap="round"></path></g>')
    x += step
    o.append(f'<g transform="translate({f(x)} {f(b - 18 * s)}) scale({f(s)})"><path d="M0 -20 C 22 -14 24 14 0 18 C -24 14 -22 -14 0 -20 Z" fill="#C8784A" stroke="#0D0D0F" stroke-width="2"></path><path d="M0 -20 L 0 -30" stroke="#4A8A3A" stroke-width="3"></path></g>')
    x += step
    o.append(f'<g transform="translate({f(x)} {f(b - 14 * s)}) scale({f(s)})">' + "".join(f'<path d="M{dx} 12 C {dx - 10} 6 {dx - 8} -8 {dx} -14 C {dx + 8} -8 {dx + 10} 6 {dx} 12 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path>' for dx in (-10, 0, 10)) + '</g>')
    names = ["FISH", "CUCUMBERS", "MELONS", "LEEKS", "ONIONS", "GARLIC"]
    for i, nm in enumerate(names): o.append(label(w * 0.08 + step * i, b + 14, nm, "#3A2A1A", 8, ls=0.08))
    return "".join(o)

def weeping(p, w, h, seed):
    """Every man at the door of his tent, weeping throughout their families."""
    r = random.Random(seed); b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#2A2A4A"></rect>', ground(w, h, h * 0.6, "#5A4A4A", dy=0)]
    for i, x in enumerate((0.1, 0.32, 0.54, 0.76)):
        o.append(A.black_tent(w * x + w * 0.04, b - 8, w * 0.16, h * 0.32))
        o.append(E.kneel(w * x, b, fit(b, h * 0.6) * 0.9, color=r.choice(A.HEBREW), skin="#8A5A3E"))
        o.append(woman(p, w * x + w * 0.1, b, fit(b, h * 0.5), r.choice(["#6A3A5A", "#4A3A6A", "#5A4A3A"]), flip=True))
    return "".join(o)

def elders_round(p, w, h, seed, spirit=False):
    """The seventy elders set round about the Tent; Jehovah came down in the cloud (spirit=True: light upon them)."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), ground(w, h, h * 0.5, "#C8B080", dy=0), V.tabernacle(w * 0.5, h * 0.62, w * 0.42, uid=p + "tb")]
    o.append(E3.pillar_cloud(w * 0.54, h * 0.52, -40, w * 0.07, seed))
    if spirit: o.append(V.rays(w * 0.54, h * 0.2, 40, 20, max(w, h), color="#FFF4C2", op=0.35))
    for k in range(2):
        y = h * (0.74 + k * 0.18); n = 14 + k * 4
        for i in range(n):
            x = w * (0.02 + 0.96 * (i + 0.5) / n)
            if abs(x - w * 0.5) < w * 0.2 and k == 0: continue
            o.append(A.elder(r.choice(A.CLOTHS), i)(p, x, y, fit(y, y - h * (0.18 + 0.06 * k)), flip=x > w / 2))
    return "".join(o)

def quails_fall(p, w, h, seed, gathering=False):
    """A wind from Jehovah brought quails from the sea and let them fall by the camp, two cubits above the face of the earth;
    gathering=True: the people gathering them all that day and all the night."""
    r = random.Random(seed); b = h * 0.9
    o = [mk.defs(p, *ALL), sun(w * 0.86, h * 0.14, 14, op=0.25), ground(w, h, h * 0.56, "#C8A06A", dy=0), N.camp(14, w * 0.2, w * 0.8, h * 0.58, h * 0.7, seed)]
    o.append("".join(f'<path d="M{f(-20 + i * 70)} {f(h * (0.1 + (i % 3) * 0.06))} C {f(80 + i * 70)} {f(h * (0.06 + (i % 3) * 0.06))} {f(160 + i * 70)} {f(h * (0.14 + (i % 3) * 0.06))} {f(240 + i * 70)} {f(h * (0.1 + (i % 3) * 0.06))}" fill="none" stroke="#F3EFE6" stroke-width="2" opacity="0.5"></path>' for i in range(int(w / 70))))
    o.append(E4.quails(70, 0, w, h * 0.08, h * 0.5, seed, smin=0.3, smax=0.8))
    o.append(E4.quails(60, 0, w, h * 0.72, h * 0.86, seed + 1, smin=0.3, smax=0.6, flying=False))
    if gathering:
        for i in range(6):
            x = w * (0.08 + i * 0.16)
            o.append(E.kneel(x, b, fit(b, h * 0.6) * 0.8, color=r.choice(A.HEBREW), skin="#8A5A3E", flip=i % 2 == 1))
    return "".join(o)

def graves_lust(w, h, seed):
    """Kibroth-hattaavah: the graves of them that lusted, stone heaps across the wilderness at dusk."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#2A1A2E"></rect>', V.rays(w * 0.8, h * 0.5, 30, 20, w, color="#FF8A3D", op=0.15),
         hills(w, h, h * 0.5, seed, color="#3A2430", amp=14), ground(w, h, h * 0.62, "#4A3030", dy=0)]
    o.append(R.graves(w * 0.1, h * 0.8, 9, min(1.2, h / 260)) + R.graves(w * 0.5, h * 0.9, 7, min(1.4, h / 220)))
    return "".join(o)

def miriam_without(p, w, h, seed, k=0):
    """Miriam shut up without the camp seven days; the camp waiting, the tents struck not; k days marked."""
    b = h * 0.9
    o = [wilderness_camp(p, w, h, seed, standards=False, sinai=False)]
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.5)} L {f(w * 0.2)} {f(h)}" stroke="#FFD23F" stroke-width="3" stroke-dasharray="10 7"></path>')
    o.append(woman(p, w * 0.1, b, fit(b, h * 0.56), MIRIAM_C))
    o.append(f'<g transform="translate({f(w * 0.04)} {f(h * 0.08)}) scale({f(min(1.6, h / 200))})">' + days(40, 10, 7, lit=k or 7, w=11) + '</g>')
    return "".join(o)

def door_cloud(p, w, h, seed, three=True, leprous=False):
    """Jehovah came down in a pillar of cloud and stood at the door of the Tent: Moses, Aaron and Miriam before it."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sun(w * 0.88, h * 0.15, 14, op=0.25), ground(w, h, h * 0.58, "#C8B080", dy=0), V.tabernacle(w * 0.62, h * 0.66, w * 0.56, uid=p + "tb"),
         E3.pillar_cloud(w * 0.56, h * 0.64, -40, w * 0.08, seed)]
    s = fit(b, h * 0.42)
    o.append(A.moses(p, w * 0.1, b, s) + A.aaron(p, w * 0.22, b, s))
    o.append(woman(p, w * 0.34, b, s * 0.94, "#F3F1EC" if leprous else MIRIAM_C))
    return "".join(o)
