"""New drawings for Genesis chapters 12–13 (Genesis 39–41): Potiphar's house, the prison, the butler and the baker,
Pharaoh's court, the second chariot, the storehouses."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, judges1 as G1, samuel2 as A2, samuel3 as A3, numbers1 as N, egypt as EG, ruth1 as R
from faces_ex import F
import faces
from genesis import art2 as Y, art3 as Z, art10 as T, art11 as U
from genesis.art2 import fit, ground, hills, city, birds, SKIN
from genesis.art3 import sun, label, man, woman
def f(v): return f"{v:.1f}"

JOSEPH, JOSEPH_AFRAID = U.JOSEPH, U.JOSEPH_AFRAID
JOSEPH_FIRM = F("adam", skin="#E3B08A", shadow="#8A5A4A", hair="#5A3A22", hl="#8A6A4A", brow="scowl", light="#FFE680")
JOSEPH_PRISON = F("adam", skin="#C9A28A", shadow="#5A4A5A", hair="#5A3A22", hl="#8A6A4A", stubble="#5A3A22", brow="sorrow", light="#FFF4C2")
JOSEPH_EG = faces.face("adam", skin="#D9A27A", shadow="#9A6A4A", hair="#3A2214", hl="#6A5A4E", collar=True, kohl=True, light="#FFE680")
JOSEPH_EG_STERN = faces.face("adam", skin="#C98E66", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", collar=True, kohl=True, brow="scowl", light="#FF8A3D")
JOSEPH_EG_WEEP = faces.face("adam", skin="#D9A27A", shadow="#8A5A5A", hair="#3A2214", hl="#6A5A4E", collar=True, kohl=True, brow="sorrow", tear=True)
PHARAOH = faces.face("adam", skin="#C98E66", shadow="#8A5A3E", egypt=("#E8B830", "#1F5FAD"), collar=True, kohl=True, false_beard=True, light="#FFE680")
PHARAOH_TROUBLED = faces.face("adam", skin="#B98A7E", shadow="#4A3A5A", egypt=("#E8B830", "#1F5FAD"), collar=True, kohl=True, false_beard=True, brow="sorrow", light="#9A8AFF")
POTIPHAR = faces.face("adam", skin="#B9785A", shadow="#5A2A1E", egypt=("#F3EFE6", "#1F5FAD"), collar=True, kohl=True, light="#FFC14D")
POTIPHAR_WROTH = faces.face("adam", skin="#B9684A", shadow="#4A1A16", egypt=("#F3EFE6", "#1F5FAD"), collar=True, kohl=True, brow="scowl", light="#FF6A4A")
WIFE = F("eve", skin="#D9A27A", shadow="#8A5A4A", hair="#0D0D0F", collar=True, kohl=True, band=True, light="#FFC14D")
WIFE_SCHEME = F("eve", skin="#C98E66", shadow="#5A2A1E", hair="#0D0D0F", collar=True, kohl=True, band=True, brow="scowl", light="#FF6A4A")
BUTLER = faces.face("adam", skin="#C98E66", shadow="#6A4A3A", egypt=("#F3EFE6", "#D7261E"), kohl=True, light="#FFE680")
BUTLER_SAD = faces.face("adam", skin="#B98A7E", shadow="#4A3A5A", egypt=("#F3EFE6", "#D7261E"), kohl=True, brow="sorrow", light="#9FB8FF")
BAKER = faces.face("adam", skin="#B9785A", shadow="#5A3A2A", egypt=("#E8D8B0", "#8A6A3A"), kohl=True, brow="sorrow", light="#FFC14D")

EGYPT_BG = "linear-gradient(180deg, #FFE3B8 0%, #E8C88A 100%)"
HALL = "linear-gradient(180deg, #3A2214 0%, #8A5A30 100%)"
JAIL = "linear-gradient(180deg, #12090A 0%, #3A2A26 100%)"

def egyptian(p, x, y, s, cloth="#F3EFE6", flip=False, up=None, extra=""):
    return man(p, x, y, s, cloth, flip=flip, up=up, extra='<path d="M-14 -190 L 14 -190 L 18 -170 L -18 -170 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></path>' + extra)

def house_of_potiphar(p, w, h, seed, joseph_top=0.46):
    """The Egyptian's house: columns and a courtyard; Joseph the overseer with servants bringing in the harvest."""
    b = h * 0.88
    cols = "".join(f'<rect x="{f(w * x - 12)}" y="{f(h * 0.16)}" width="24" height="{f(b - h * 0.16)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2"></rect>'
                   f'<rect x="{f(w * x - 20)}" y="{f(h * 0.12)}" width="40" height="14" fill="#5E8F26" stroke="#0D0D0F" stroke-width="2"></rect>' for x in (0.08, 0.92))
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#1F5FAD"></rect>' + cols + ground(w, h, b, "#D8B878", dy=0)
            + T.figure(p, "joseph_plain", w * 0.32, b, fit(b, h * joseph_top), pose="point")
            + egyptian(p, w * 0.54, b, fit(b, h * 0.5), "#F3EFE6", flip=True).replace("</g>", R.sack(0, -150, 0.8).replace("translate(0 -150)", "translate(0 -150)") + "</g>", 1)
            + egyptian(p, w * 0.68, b, fit(b, h * 0.5), "#E8E2D6", flip=True) + R.sack(w * 0.8, b + 4, 1.2) + R.sack(w * 0.86, b + 6, 1.1))

def garment(p, w, h, seed):
    """He left his garment in her hand, and fled: the empty doorway, the cloth hanging from her hand."""
    b = h * 0.9
    door = f'<rect x="{f(w * 0.56)}" y="{f(h * 0.08)}" width="{f(w * 0.26)}" height="{f(b - h * 0.08)}" fill="#FFF4C2" stroke="#0D0D0F" stroke-width="3"></rect>'
    cloth = (f'<path d="M{f(w * 0.36)} {f(h * 0.42)} C {f(w * 0.4)} {f(h * 0.5)} {f(w * 0.38)} {f(h * 0.7)} {f(w * 0.42)} {f(h * 0.82)} L {f(w * 0.3)} {f(h * 0.84)} C {f(w * 0.28)} {f(h * 0.7)} {f(w * 0.32)} {f(h * 0.54)} {f(w * 0.3)} {f(h * 0.44)} Z" '
             f'fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2.4"></path>')
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A3A22"></rect>' + door + ground(w, h, b, "#3A2214", dy=0)
            + woman(p, w * 0.22, b, fit(b, h * 0.3), "#E8E2D6", up=[(-22, -158), (4, -150), (30, -150)]) + cloth
            + mk.person(p, round(w * 0.7), round(b), round(fit(b, h * 0.4) * 0.8, 3), body="#12090A", up=T.POSES["run"])
            + mk.speed(w * 0.78, h * 0.5, 14, 20, w * 0.2, seed, color="#F3EFE6", op=0.6))

def cried_out(p, w, h, seed):
    """She called unto the men of her house: the wife holding up the garment, the servants gathering."""
    b = h * 0.88
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A3A22"></rect>' + ground(w, h, b, "#3A2214", dy=0)
            + woman(p, w * 0.3, b, fit(b, h * 0.4), "#E8E2D6", up=[(-22, -158), (4, -150), (30, -150)])
            + f'<path d="M{f(w * 0.3 + 30 * fit(b, h * 0.4))} {f(b - 152 * fit(b, h * 0.4))} C {f(w * 0.3 + 46 * fit(b, h * 0.4))} {f(b - 110 * fit(b, h * 0.4))} {f(w * 0.3 + 38 * fit(b, h * 0.4))} {f(b - 70 * fit(b, h * 0.4))} {f(w * 0.3 + 52 * fit(b, h * 0.4))} {f(b - 40 * fit(b, h * 0.4))} L {f(w * 0.3 + 20 * fit(b, h * 0.4))} {f(b - 36 * fit(b, h * 0.4))} C {f(w * 0.3 + 14 * fit(b, h * 0.4))} {f(b - 80 * fit(b, h * 0.4))} {f(w * 0.3 + 22 * fit(b, h * 0.4))} {f(b - 120 * fit(b, h * 0.4))} {f(w * 0.3 + 18 * fit(b, h * 0.4))} {f(b - 150 * fit(b, h * 0.4))} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2.4"></path>'
            + "".join(egyptian(p, w * x, b, fit(b, h * 0.46), c, flip=True) for x, c in [(0.6, "#F3EFE6"), (0.72, "#E8D8B0"), (0.84, "#F3EFE6")]))

def prison(p, w, h, seed, figures=()):
    """The king's prison: stone walls, a barred window high up, a shaft of light."""
    b = h * 0.9
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2420"></rect>']
    o += [f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#1A1410" stroke-width="2"></path>' for y in range(0, int(h), 40)]
    o.append(f'<rect x="{f(w * 0.6)}" y="{f(h * 0.1)}" width="{f(w * 0.12)}" height="{f(h * 0.12)}" fill="#8FD0E2"></rect>'
             + "".join(f'<path d="M{f(w * 0.6 + i * w * 0.03)} {f(h * 0.1)} L {f(w * 0.6 + i * w * 0.03)} {f(h * 0.22)}" stroke="#2A2420" stroke-width="4"></path>' for i in range(1, 4))
             + f'<path d="M{f(w * 0.6)} {f(h * 0.22)} L {f(w * 0.72)} {f(h * 0.22)} L {f(w * 0.5)} {f(b)} L {f(w * 0.2)} {f(b)} Z" fill="#FFF4C2" opacity="0.2"></path>')
    o.append(ground(w, h, b, "#1A1410", dy=0))
    for who, x, top, flip in figures:
        o.append(T.figure(p, who, w * x, b, fit(b, h * top), flip=flip) if isinstance(who, str) or who[0] != "eg" else egyptian(p, w * x, b, fit(b, h * top), who[1], flip=flip))
    return "".join(o)

def vine(w, h, seed):
    """A vine with three branches, budding and blossoming, the clusters ripe; Pharaoh's cup."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A5E"></rect>', mk.stars(40, w, h, seed)]
    o.append(f'<path d="M{f(w * 0.3)} {f(h)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.36)} {f(h * 0.5)} {f(w * 0.3)} {f(h * 0.3)}" fill="none" stroke="#5A3A22" stroke-width="10"></path>')
    for i, (x, y) in enumerate([(0.14, 0.32), (0.46, 0.36), (0.36, 0.14)]):
        o.append(f'<path d="M{f(w * 0.32)} {f(h * (0.5 - i * 0.08))} Q {f(w * (x + 0.04))} {f(h * (y + 0.1))} {f(w * x)} {f(h * y)}" fill="none" stroke="#5A3A22" stroke-width="6"></path>'
                 + N.grapes(w * x, h * y + 10, 0.5, seed=i))
    o.append(f'<path d="M{f(w * 0.66)} {f(h * 0.5)} L {f(w * 0.84)} {f(h * 0.5)} L {f(w * 0.8)} {f(h * 0.66)} L {f(w * 0.76)} {f(h * 0.68)} L {f(w * 0.76)} {f(h * 0.8)} L {f(w * 0.82)} {f(h * 0.82)} L {f(w * 0.68)} {f(h * 0.82)} L {f(w * 0.74)} {f(h * 0.8)} L {f(w * 0.74)} {f(h * 0.68)} L {f(w * 0.7)} {f(h * 0.66)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
             + f'<path d="M{f(w * 0.67)} {f(h * 0.52)} L {f(w * 0.83)} {f(h * 0.52)}" stroke="#7A1E3A" stroke-width="6"></path>')
    return "".join(o)

def baskets(w, h, seed):
    """Three baskets of white bread on my head, and the birds did eat them out of the uppermost basket."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A1A1A"></rect>']
    for i in range(3):
        y = h * (0.82 - i * 0.18); bw = w * (0.4 - i * 0.04)
        o.append(f'<path d="M{f(w * 0.5 - bw / 2)} {f(y - h * 0.12)} L {f(w * 0.5 + bw / 2)} {f(y - h * 0.12)} L {f(w * 0.5 + bw / 2 - 12)} {f(y)} L {f(w * 0.5 - bw / 2 + 12)} {f(y)} Z" fill="#C9A86A" stroke="#0D0D0F" stroke-width="2"></path>'
                 + "".join(f'<ellipse cx="{f(w * 0.5 - bw / 2 + 20 + k * (bw - 40) / 4)}" cy="{f(y - h * 0.12)}" rx="14" ry="7" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></ellipse>' for k in range(5)))
    o.append(birds(7, w * 0.2, w * 0.8, h * 0.06, h * 0.26, seed, smin=1.2, smax=2.2, color="#0D0D0F"))
    return "".join(o)

def birthday(p, w, h, seed):
    """Pharaoh's birthday feast: the butler restored, giving the cup into Pharaoh's hand."""
    b = h * 0.9
    return (T.stage(p, w, h, seed, "palace", [("pharaoh", 0.62, 0.36, True), (("egypt", "#F3EFE6"), 0.42, 0.42, False, "point")],
                    props=f'<path d="M{f(w * 0.5)} {f(b - h * 0.4)} l 10 0 l -2 14 l -6 0 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>'))

def magicians(p, w, h, seed):
    """Pharaoh called for all the magicians of Egypt, and all the wise men: a row of them, none could interpret."""
    b = h * 0.9; r = random.Random(seed)
    return T.stage(p, w, h, seed, "palace", [("pharaoh", 0.14, 0.34)] + [(("egypt", r.choice(["#F3EFE6", "#E8D8B0", "#C8C2D6"])), 0.36 + i * 0.1, 0.42, True) for i in range(6)])

def shaved(p, w, h, seed):
    """He shaved himself, and changed his raiment: the prison garment on the floor, fine linen held out."""
    b = h * 0.88
    return (prison(p, w, h, seed, figures=[("joseph_plain", 0.4, 0.4, False)])
            + egyptian(p, w * 0.7, b, fit(b, h * 0.44), "#F3EFE6", flip=True, up=[(-22, -158), (-40, -126), (-58, -110)])
            + f'<path d="M{f(w * 0.5)} {f(b - h * 0.34)} L {f(w * 0.6)} {f(b - h * 0.34)} L {f(w * 0.62)} {f(b - h * 0.12)} L {f(w * 0.48)} {f(b - h * 0.12)} Z" fill="#FFFDF0" stroke="#0D0D0F" stroke-width="2"></path>')

def chariot_ride(p, w, h, seed):
    """He made him to ride in the second chariot; and they cried before him, Bow the knee."""
    b = h * 0.86
    return (sun(w * 0.86, h * 0.2, 16, color="#FFE680", op=0.3) + EG.pyramid(w * 0.86, b, w * 0.24, h * 0.36) + ground(w, h, b, "#D8B878", dy=0)
            + E3.chariot(w * 0.36, b + 4, 0.8, color="#E8B830", driver="#1F5FAD")
            + "".join(E.kneel(w * x, b + 4, round(h / 600, 3), color=c, skin="#8A4A2E", flip=True) for x, c in [(0.62, "#F3EFE6"), (0.7, "#E8D8B0"), (0.78, "#F3EFE6"), (0.88, "#E8D8B0")]))

def signet(w, h, seed):
    """Pharaoh's signet ring on Joseph's hand, a gold chain about his neck, vestures of fine linen."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1F5FAD"></rect>', V.rays(w * 0.5, h * 0.5, 36, 20, w, color="#FFD23F", op=0.2)]
    o.append(f'<path d="M{f(w * 0.1)} {f(h * 0.3)} C {f(w * 0.3)} {f(h * 0.9)} {f(w * 0.7)} {f(h * 0.9)} {f(w * 0.9)} {f(h * 0.3)}" fill="none" stroke="#0D0D0F" stroke-width="16"></path>'
             f'<path d="M{f(w * 0.1)} {f(h * 0.3)} C {f(w * 0.3)} {f(h * 0.9)} {f(w * 0.7)} {f(h * 0.9)} {f(w * 0.9)} {f(h * 0.3)}" fill="none" stroke="#FFD23F" stroke-width="10" stroke-dasharray="14 6"></path>')
    o.append(f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.5)}" r="{f(h * 0.12)}" fill="none" stroke="#0D0D0F" stroke-width="14"></circle><circle cx="{f(w * 0.5)}" cy="{f(h * 0.5)}" r="{f(h * 0.12)}" fill="none" stroke="#E8B830" stroke-width="9"></circle>'
             + f'<rect x="{f(w * 0.5 - 16)}" y="{f(h * 0.38 - 16)}" width="32" height="24" rx="4" fill="#1F7A8C" stroke="#0D0D0F" stroke-width="2"></rect>')
    return "".join(o)

def handfuls(p, w, h, seed):
    """In the seven plenteous years the earth brought forth by handfuls: tall grain along the river."""
    b = h * 0.84
    return (sun(w * 0.8, h * 0.2, 18, color="#FFE680", op=0.35) + ground(w, h, b, "#C8A06A", dy=0) + Z.S.grain(-10, w + 10, b + 6, h * 0.46, seed)
            + f'<rect x="-10" y="{f(h * 0.94)}" width="{f(w + 20)}" height="{f(h * 0.08)}" fill="#2C9DB8"></rect>')

def bread_lines(p, w, h, seed):
    """All countries came into Egypt to Joseph to buy grain: crowds with sacks before the storehouses."""
    b = h * 0.9; r = random.Random(seed)
    o = [sun(w * 0.86, h * 0.18, 16, color="#FFF4C2", op=0.4), EG.granaries(w * 0.04, h * 0.62, 6, w * 0.16, h * 0.3), ground(w, h, h * 0.62, "#C8885A", dy=0)]
    for i in range(16):
        x = r.uniform(0.04, 0.96) * w; y = r.uniform(h * 0.7, b); s = 0.14 + 0.2 * (y - h * 0.7) / (b - h * 0.7)
        o.append(man(p, x, y, s, r.choice(["#5A3A22", "#8A6A3A", "#3A5A6A", "#7A3A2A", "#F3EFE6"]), flip=r.random() < 0.5) + R.sack(x + 14 * s, y - 10, s * 2))
    return "".join(o)
