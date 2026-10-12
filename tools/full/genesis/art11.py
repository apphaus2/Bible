"""New drawings for Genesis chapter 11 (Genesis 37–38): Joseph and his brethren, Dothan, the pit, Judah and Tamar."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus4 as E4, exodus5 as V, judges1 as G1, samuel2 as A2, samuel4 as A4, ruth1 as R
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art8 as L, art10 as T
from genesis.art2 import fit, ground, hills, city, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg, node, route
def f(v): return f"{v:.1f}"

JOSEPH = F("adam", skin="#E3B08A", shadow="#B97A58", hair="#5A3A22", hl="#8A6A4A", light="#FFE680")
JOSEPH_AFRAID = F("adam", skin="#D9A27A", shadow="#6A4A5A", hair="#5A3A22", hl="#8A6A4A", brow="sorrow", sweat=True, light="#9FB8FF")
ISRAEL = F("adam", skin="#C98E66", shadow="#6A4A5A", hair="#C8C2B6", hl="#8A867E", beard=True, light="#FFE680")
ISRAEL_WEEP = F("adam", skin="#C98E66", shadow="#6A4A5A", hair="#C8C2B6", hl="#8A867E", beard=True, brow="sorrow", tear=True)
REUBEN = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", brow="sorrow", light="#FFC14D")
JUDAH = F("adam", skin="#B9785A", shadow="#5A2A1E", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#E2D8C4", cord=True, light="#FFC14D")
JUDAH_STERN = F("adam", skin="#B9785A", shadow="#4A1A16", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#E2D8C4", cord=True, brow="scowl", light="#FF6A4A")
BROTHER = F("adam", skin="#B98A6E", shadow="#5A2A1E", hair="#1A1210", hl="#4A3A2E", stubble="#2A1A10", brow="scowl", light="#FF6A4A")
TAMAR = F("eve", skin="#D9A27A", shadow="#8A5A4A", hair="#1A1210", scarf="#3A3A4A", light="#FFC14D")
TAMAR_VEIL = F("eve", skin="#D9A27A", shadow="#8A5A4A", hair="#1A1210", scarf="#5A3A8A", light="#FF8A3D")
STRANGER = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#7A6A5A", hl="#8A867E", beard=True, scarf="#E2D8C4", cord=True, light="#FFE680")

BROS = ["#7A3A2A", "#5A3A22", "#3A5A6A", "#8A6A3A", "#5A6A3A", "#6A4A6A"]

def brothers(p, w, h, seed, x0=0.5, x1=0.95, top=0.46, flip=True, n=5):
    b = h * 0.88
    return "".join(man(p, w * (x0 + (x1 - x0) * i / max(1, n - 1)), b, fit(b, h * (top + (i % 2) * 0.03)), BROS[i % 6], flip=flip) for i in range(n))

def flock_field(p, w, h, seed, cast=()):
    return T.stage(p, w, h, seed, "field", cast, props=Z.flock(w * 0.02, w * 0.4, h * 0.86, h * 0.96, 7, seed, cows=0, smin=0.2, smax=0.26))

def wanderer(p, w, h, seed):
    """A certain man found him wandering in the field: two figures on a wide plain."""
    return T.stage(p, w, h, seed, "field", [("joseph", 0.3, 0.46), (("man", "#E2D8C4"), 0.62, 0.44, True, "point")])

def dothan_map(w, h, seed):
    o = [grid_bg(w, h)]
    o.append(route([(w * 0.5, h * 0.84), (w * 0.44, h * 0.5), (w * 0.4, h * 0.24)], color="#FFD23F", sw=3))
    o.append(node(w * 0.5, h * 0.84, "HEBRON", "#FFD23F", r=5, dy=20) + node(w * 0.44, h * 0.5, "SHECHEM", "#C8C2B6", r=5, dy=-12) + node(w * 0.4, h * 0.24, "DOTHAN", "#D7261E", r=6, dy=-12))
    return "".join(o)

def caravan_road(p, w, h, seed):
    """A caravan of Ishmaelites coming from Gilead, camels bearing spicery and balm and myrrh."""
    b = h * 0.84
    return (sun(w * 0.2, h * 0.3, 18, color="#FFC14D", op=0.3) + hills(w, h, b - h * 0.1, seed, color="#8A6A4A", amp=8) + ground(w, h, b, "#C8A06A", dy=0)
            + Z.caravan(p, w * 0.5, w * 0.96, b + 4, 0.6, seed, flip=True)
            + "".join(E.kneel(w * x, b + 2, round(h / 600, 3), color=c, skin=SKIN) for x, c in [(0.08, BROS[0]), (0.16, BROS[1]), (0.24, BROS[2]), (0.32, BROS[3])]))

def rent_clothes(p, w, h, seed):
    """Reuben returned unto the pit, and Joseph was not in the pit; and he rent his clothes."""
    b = h * 0.86
    pit = f'<ellipse cx="{f(w * 0.4)}" cy="{f(b + 4)}" rx="{f(w * 0.14)}" ry="{f(h * 0.06)}" fill="#12090A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
    return (sun(w * 0.8, h * 0.2, 14, op=0.25) + ground(w, h, b, "#B5A06A", dy=0) + pit
            + man(p, w * 0.66, b, fit(b, h * 0.42), "#7A3A2A", flip=True, up=[(-22, -158), (-6, -200), (14, -236)]))

def sackcloth(p, w, h, seed):
    """Jacob rent his garments, and put sackcloth upon his loins, and mourned for his son many days."""
    b = h * 0.88
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A3440"></rect>' + ground(w, h, b, "#2A2430", dy=0)
            + E.kneel(w * 0.5, b + 2, round(h / 360, 3), color="#6A5A4A", skin=SKIN)
            + "".join(mk.person(p, round(w * x), round(b), round(fit(b, h * 0.4), 3), body=SKIN, cloth=c, sw=3, flip=x > 0.5, woman=i % 3 == 2, hair="#1A1210" if i % 3 == 2 else False)
                      for i, (x, c) in enumerate([(0.12, BROS[0]), (0.22, BROS[1]), (0.3, "#C2456A"), (0.72, BROS[2]), (0.82, BROS[3]), (0.9, "#E07A9A")])))

def potiphar_house(p, w, h, seed):
    """Sold into Egypt unto Potiphar, an officer of Pharaoh's, the captain of the guard: a guarded house, a spear-bearer."""
    return T.stage(p, w, h, seed, "egypt", [(("egypt", "#F3EFE6"), 0.3, 0.44, False, "point"), ("joseph", 0.46, 0.5, True)],
                   props=label(w * 0.3, h * 0.96, "POTIPHAR", "#12113A", 9))

# ---- Genesis 38 ----------------------------------------------------------------------------------------
def adullam(p, w, h, seed):
    """Judah went down from his brethren and turned in to a certain Adullamite, Hirah; and took the daughter of Shua."""
    return T.stage(p, w, h, seed, "rock", [(("man", "#B5421E"), 0.3, 0.42), (("man", "#4A6A3A"), 0.46, 0.44, True), (("woman", "#C8902E"), 0.72, 0.46, True)],
                   props=label(w * 0.3, h * 0.96, "JUDAH", "#12113A", 9) + label(w * 0.46, h * 0.96, "HIRAH", "#12113A", 9) + label(w * 0.72, h * 0.96, "SHUA'S DAUGHTER", "#12113A", 9))

def graves_two(w, h, seed):
    """Er and Onan: two small cairns on a hillside under a dark sky."""
    b = h * 0.84
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2440"></rect>' + mk.stars(30, w, h * 0.5, seed) + hills(w, h, b, seed, color="#1A1430", amp=6)
            + A4.stone_heap(w * 0.36, b + 4, w * 0.14, h * 0.12) + A4.stone_heap(w * 0.6, b + 4, w * 0.14, h * 0.12)
            + label(w * 0.36, b + 26, "ER", "#C8C2B6", 10) + label(w * 0.6, b + 26, "ONAN", "#C8C2B6", 10))

def widow_house(p, w, h, seed):
    """Tamar went and dwelt in her father's house: a widow in dark garments at a doorway."""
    b = h * 0.88
    return (sun(w * 0.86, h * 0.2, 12, op=0.2) + city(w * 0.7, b, w * 0.4, h * 0.6, seed, color="#8A6A5A", lit="#FFC14D", wall="#9A7A6A") + ground(w, h, b, "#B59A7A", dy=0)
            + woman(p, w * 0.3, b, fit(b, h * 0.42), "#3A3A4A"))

def gate_enaim(p, w, h, seed):
    """She covered herself with her veil, and sat in the gate of Enaim, by the way to Timnah; Judah coming up the road."""
    b = h * 0.88
    return (sun(w * 0.86, h * 0.2, 14, op=0.25) + A4.gatehouse(w * 0.24, b, w * 0.34, h * 0.6) + ground(w, h, b, "#C8A06A", dy=0)
            + E.kneel(w * 0.46, b + 2, round(h / 520, 3), color="#5A3A8A", skin=SKIN)
            + man(p, w * 0.82, b, fit(b, h * 0.46), "#E2D8C4", flip=True) + label(w * 0.24, b + 18, "ENAIM", "#12113A", 9))

def pledge(w, h, seed):
    """Thy signet and thy cord, and thy staff that is in thy hand."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12113A"></rect>', V.rays(w * 0.5, h * 0.5, 30, 20, w, color="#FFD23F", op=0.15)]
    o.append(f'<path d="M{f(w * 0.12)} {f(h * 0.86)} L {f(w * 0.88)} {f(h * 0.3)}" stroke="#0D0D0F" stroke-width="14" stroke-linecap="round"></path><path d="M{f(w * 0.12)} {f(h * 0.86)} L {f(w * 0.88)} {f(h * 0.3)}" stroke="#8A5A30" stroke-width="9" stroke-linecap="round"></path>')
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.4)} C {f(w * 0.4)} {f(h * 0.6)} {f(w * 0.6)} {f(h * 0.6)} {f(w * 0.66)} {f(h * 0.42)}" fill="none" stroke="#B5421E" stroke-width="4"></path>')
    o.append(f'<circle cx="{f(w * 0.48)}" cy="{f(h * 0.6)}" r="16" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></circle><circle cx="{f(w * 0.48)}" cy="{f(h * 0.6)}" r="7" fill="#B5652E"></circle>')
    o.append(label(w * 0.48, h * 0.76, "SIGNET · CORD · STAFF", "#FFD23F", 10))
    return "".join(o)

def kid_sent(p, w, h, seed):
    """Judah sent the kid of the goats by the hand of his friend the Adullamite: but he found her not."""
    b = h * 0.88
    return (sun(w * 0.86, h * 0.2, 14, op=0.25) + A4.gatehouse(w * 0.76, b, w * 0.3, h * 0.6) + ground(w, h, b, "#C8A06A", dy=0)
            + man(p, w * 0.32, b, fit(b, h * 0.44), "#4A6A3A") + E.sheep(w * 0.44, b + 4, 0.36, wool="#3A2A22", face="#2A1A10")
            + "".join(man(p, w * x, b, fit(b, h * 0.48), c, flip=True) for x, c in [(0.6, "#8A6A5A"), (0.68, "#5A4A3E")]))

def burnt(p, w, h, seed):
    """Bring her forth: Tamar led out, holding up the signet, the cord and the staff."""
    b = h * 0.88
    return (sun(w * 0.86, h * 0.2, 14, color="#FF8A3D", op=0.25) + ground(w, h, b, "#B59A7A", dy=0)
            + woman(p, w * 0.3, b, fit(b, h * 0.42), "#3A3A4A", up=[(-22, -158), (-6, -196), (14, -226)])
            + man(p, w * 0.18, b, fit(b, h * 0.46), "#5A4A3E") + man(p, w * 0.42, b, fit(b, h * 0.46), "#5A4A3E", flip=True)
            + man(p, w * 0.82, b, fit(b, h * 0.44), "#B5421E", flip=True))

def twins(w, h, seed):
    """One put out a hand, and the midwife bound upon his hand a scarlet thread: two swaddled twins, a scarlet thread."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A2E"></rect>', f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.5)}" r="{f(h * 0.6)}" fill="#FFC14D" opacity="0.2"></circle>']
    o.append(R.baby(w * 0.32, h * 0.7, 4.4) + R.baby(w * 0.68, h * 0.74, 4.4))
    o.append(f'<path d="M{f(w * 0.68 + 60)} {f(h * 0.72)} C {f(w * 0.68 + 120)} {f(h * 0.6)} {f(w * 0.68 + 60)} {f(h * 0.56)} {f(w * 0.68 + 140)} {f(h * 0.5)}" fill="none" stroke="#D7261E" stroke-width="7" stroke-linecap="round"></path>')
    o.append(label(w * 0.32, h * 0.88, "PEREZ", "#FFD23F", 14) + label(w * 0.68, h * 0.92, "ZERAH", "#FFD23F", 14))
    return "".join(o)
