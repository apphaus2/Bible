"""New drawings for Numbers chapter 8 (Numbers 15–17): law pictograms for the drink-offerings, the first of the dough and
sins of error; the man gathering sticks; the fringe with its cord of blue; Korah and his company with their censers; the
ground cleaving under the tents of Korah, Dathan and Abiram; the censers beaten into plates for the altar; Aaron standing
between the dead and the living; and the twelve rods, Aaron's budded with blossoms and ripe almonds.
Restraint: 15:36 is a heap of stones without the camp; 16:31–33 shows the tents going down into the cleft, no bodies;
16:48–49 is told by the dividing smoke of Aaron's censer."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V, numbers1 as N
from faces_ex import F
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man
from exo import art as A, art8 as B8, art9 as Q
from lev.art import GND, priest, offerer, REACH, altar, flour, jar, cakes, goat, door
from lev.art3 import censer, BOTH
from lev.art4 import verdict
from exo.art7 import ban
from num.art import ALL, TRIBE_C, wilderness_camp
from num.art3 import cup, scroll
def f(v): return f"{v:.1f}"
CY = B8.CY

KORAH = F("adam", skin="#C98E66", shadow="#6A3A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#6A2A4A", band=True, brow="scowl", light="#D7261E")
DATHAN = F("adam", skin="#B9785A", shadow="#4A1A16", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#C8202A", cord=True, brow="scowl", light="#FF6A2A")
AARON_CENSER = F("adam", skin="#D9946A", shadow="#7A3A2A", hair="#9A968E", hl="#6A665E", beard=True, scarf="#F3EFE6", band=True, light="#FFD23F")
KORAH_C = "#6A2A4A"

# ---- 15:1–31 pictograms ----------------------------------------------------------------------------------------------
def hin(x, y, frac, color="#C8B040", label_=""):
    """A measuring jar filled to frac."""
    return (f'<rect x="{f(x - 12)}" y="{f(y - 34)}" width="24" height="34" rx="4" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></rect>'
            f'<rect x="{f(x - 11)}" y="{f(y - 33 * frac)}" width="22" height="{f(33 * frac)}" fill="{color}"></rect>'
            + (label(x, y + 10, label_, CY, 6.5) if label_ else ""))
def portion(beast, fl, oil, wine, fl_t, oil_t, wine_t):
    def pg(p):
        return (GND + beast + flour(150, 84, 0.8) + label(150, 96, fl_t, CY, 6.5) + hin(210, 84, oil, "#C8B040", oil_t) + hin(270, 84, wine, "#7A1A3A", wine_t))
    return pg
pg_lamb = portion(E3.lamb(70, 84, 0.36), 0.1, 0.25, 0.25, "1/10 EPHAH", "1/4 HIN OIL", "1/4 HIN WINE")
pg_ram = portion(E.sheep(70, 84, 0.4), 0.2, 0.33, 0.33, "2/10 EPHAH", "1/3 HIN OIL", "1/3 HIN WINE")
pg_bullock = portion('<g transform="translate(70 84) scale(0.28)"><path d="M-110 -120 L 110 -120 L 110 0 L -110 0 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="5"></path></g>', 0.3, 0.5, 0.5, "3/10 EPHAH", "1/2 HIN OIL", "1/2 HIN WINE")
def pg_offering_fire(p): return GND + offerer(p, 60) + E3.lamb(130, 84, 0.34) + altar(230, 84, 1.1) + label(230, 96, "A SWEET SAVOR", CY, 7)
def pg_each(p):        return GND + E3.lamb(50, 84, 0.3) + E.sheep(110, 84, 0.34) + '<g transform="translate(180 84) scale(0.24)"><path d="M-110 -120 L 110 -120 L 110 0 L -110 0 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="5"></path></g>' + label(260, 56, "EACH ACCORDING TO ITS NUMBER", CY, 6.5)
def pg_one_law(p):     return GND + man(p, 100, 86, 0.36, "#5A3A22") + label(160, 50, "=", "#FFD23F", 24) + man(p, 220, 86, 0.36, "#6A6A8A", flip=True) + label(160, 96, "THE HOME-BORN · THE SOJOURNER", CY, 7)
def pg_bread(p):       return GND + cakes(90, 84, 1.2) + label(90, 96, "THE FIRST OF YOUR DOUGH", CY, 7) + priest(p, 220, up=REACH)
def pg_err(p):         return GND + label(100, 50, "UNWITTINGLY", "#FFD23F", 10) + man(p, 220, 86, 0.36, "#5A3A22")
def pg_congregation(p): return GND + '<g transform="translate(70 84) scale(0.28)"><path d="M-110 -120 L 110 -120 L 110 0 L -110 0 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="5"></path></g>' + goat(150, 84, 0.42) + altar(250, 84, 1.0)
def pg_forgiven(p):    return GND + priest(p, 90, up=REACH) + altar(170, 84, 0.9) + verdict(260, 44, True)
def pg_she_goat(p):    return GND + offerer(p, 60) + goat(140, 84, 0.42, color="#8A7A6A") + priest(p, 230, flip=True)
def pg_high_hand(p):   return GND + man(p, 120, 86, 0.38, "#3A2214", up=[(-22, -158), (-14, -196), (-6, -230)]) + ban(220, 50, 30) + label(220, 96, "CUT OFF", CY, 8)

# ---- scenes --------------------------------------------------------------------------------------------------------
def sticks(p, w, h, seed, ward=False):
    """A man gathering sticks upon the sabbath day (ward=True: put in ward, sitting under guard)."""
    r = random.Random(seed); b = h * 0.9
    o = [mk.defs(p, *ALL), sun(w * 0.86, h * 0.16, 14, op=0.25), hills(w, h, h * 0.5, seed, color="#B5652E", amp=12), ground(w, h, h * 0.58, "#D8B878", dy=0)]
    s = fit(b, h * 0.48)
    if not ward:
        o.append(E.kneel(w * 0.5, b, s * 0.95, color="#5A4A3A", skin="#8A5A3E"))
        o.append("".join(f'<path d="M{f(w * 0.56 + i * 9)} {f(b - 4)} L {f(w * 0.6 + i * 9)} {f(b - 24 - i * 3)}" stroke="#5A3A22" stroke-width="3" stroke-linecap="round"></path>' for i in range(5)))
        for i in range(3): o.append(man(p, w * (0.1 + i * 0.08), b, s, r.choice(A.HEBREW)))
    else:
        o.append(A.black_tent(w * 0.5, b - 4, w * 0.3, h * 0.36) + E.kneel(w * 0.5, b, s * 0.7, color="#5A4A3A", skin="#8A5A3E"))
        for x in (0.28, 0.72): o.append(man(p, w * x, b, s, "#6A5A3A", flip=x > 0.5))
    return "".join(o)

def fringe(w, h):
    """The border of a garment with its fringe, and a cord of blue upon the fringe of each border."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#E8E2D6"></rect>',
         f'<path d="M-10 {f(h * 0.1)} L {f(w * 0.7)} {f(h * 0.1)} L {f(w * 0.62)} {f(h * 0.62)} L -10 {f(h * 0.7)} Z" fill="#C8B890" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i in range(14):
        x = w * (0.02 + i * 0.045); y0 = h * 0.7 - i * h * 0.006
        o.append(f'<path d="M{f(x)} {f(y0)} C {f(x - 4)} {f(y0 + h * 0.1)} {f(x + 4)} {f(y0 + h * 0.18)} {f(x)} {f(y0 + h * 0.26)}" fill="none" stroke="#F3EFE6" stroke-width="3"></path>')
    for x0 in (0.08, 0.38):
        x = w * x0; y0 = h * 0.68
        o.append(f'<path d="M{f(x)} {f(y0)} C {f(x - 6)} {f(y0 + h * 0.1)} {f(x + 6)} {f(y0 + h * 0.2)} {f(x)} {f(y0 + h * 0.3)}" fill="none" stroke="#1F5FAD" stroke-width="5" stroke-linecap="round"></path>')
    return "".join(o)

def company(p, w, h, seed, censers=False, against=True):
    """Korah and his company, the two hundred and fifty princes, risen up before Moses and Aaron at the tent (censers=True:
    every man his censer, fire in them and incense)."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), sun(w * 0.88, h * 0.15, 14, op=0.25), ground(w, h, h * 0.56, "#C8B080", dy=0), V.tabernacle(w * 0.22, h * 0.6, w * 0.4, uid=p + "tb")]
    s = fit(b, h * 0.42)
    o.append(A.moses(p, w * 0.08, b, s, flip=False) + A.aaron(p, w * 0.17, b, s * 0.98))
    for k in range(2):
        y = b - k * h * 0.08; n = 8 + k * 3
        for i in range(n):
            x = w * (0.36 + 0.62 * (i + 0.5) / n)
            c = KORAH_C if (k == 0 and i == 0) else r.choice(["#6A5A7A", "#7A4A3A", "#5A4A6A", "#8A6A4A", "#4A3A5A"])
            up = [(-22, -158), (-34, -150), (-48, -140)] if censers else None
            o.append(man(p, x, y, s * (0.95 - 0.12 * k), c, flip=True, up=up))
            if censers and k == 0: o.append(censer(x - 48 * s * 0.95, y - 140 * s * 0.95, s * 1.2))
    return "".join(o)

def cleft(p, w, h, seed, stage=0):
    """The tents of Korah, Dathan and Abiram: (0) the families at their tent doors and the people drawing back; (1) the ground
    clave asunder and the tents go down; (2) the earth closed, the people fleeing at the cry."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{"#8FB0C8" if stage == 0 else "#3A1A1A"}"></rect>', ground(w, h, h * 0.5, "#8A6A4A" if stage == 0 else "#4A2A1A", dy=0)]
    cx = w * 0.55
    if stage == 1:
        o.append(f'<path d="M{f(cx - w * 0.3)} {f(h * 0.62)} L {f(cx - w * 0.1)} {f(h * 0.58)} L {f(cx)} {f(h)} L {f(cx - w * 0.2)} {f(h)} Z" fill="#0D0D0F"></path>'
                 f'<path d="M{f(cx - w * 0.1)} {f(h * 0.58)} L {f(cx + w * 0.25)} {f(h * 0.6)} L {f(cx + w * 0.1)} {f(h)} L {f(cx)} {f(h)} Z" fill="#1A0A0A"></path>')
        for i, x in enumerate((-0.2, -0.04, 0.12)):
            o.append(f'<g transform="rotate({(-18, 10, 24)[i]} {f(cx + w * x)} {f(h * 0.66)})">' + A.black_tent(cx + w * x, h * 0.72, w * 0.14, h * 0.2) + '</g>')
        o.append(V.rays(cx, h * 0.62, 30, 10, w * 0.5, color="#FF6A2A", op=0.2))
    elif stage == 0:
        for i, x in enumerate((-0.2, 0.0, 0.2)):
            o.append(A.black_tent(cx + w * x, h * 0.66, w * 0.16, h * 0.22))
            for j in range(3): o.append(man(p, cx + w * x + (j - 1) * w * 0.03, h * 0.74, fit(h * 0.74, h * 0.6), r.choice(["#5A4A6A", "#6A2A4A", "#7A4A3A"])))
    else:
        o.append(f'<path d="M{f(cx - w * 0.3)} {f(h * 0.62)} L {f(cx + w * 0.25)} {f(h * 0.6)}" stroke="#0D0D0F" stroke-width="4" stroke-dasharray="14 6"></path>')
    s = fit(b, h * 0.6)
    for i in range(6 if stage else 4):
        x = w * (0.04 + i * 0.06) if i % 2 == 0 else w * (0.96 - i * 0.05)
        o.append(man(p, x, b - (i % 2) * 4, s, r.choice(A.HEBREW), flip=x < w / 2, up=[(-22, -158), (-14, -196), (-6, -228)] if stage == 2 else None))
    return "".join(o)

def plates(w, h):
    """The brazen censers beaten into broad plates for a covering of the altar: a memorial."""
    o = [B8.bp(w, h), B8.title_bar(w, "BEATEN PLATES FOR A COVERING OF THE ALTAR · A MEMORIAL")]
    s = min(2.4, h / 120)
    for i in range(5): o.append(censer(w * (0.06 + i * 0.075), h * 0.9 - (i % 2) * 14, s, fire=False))
    o.append(label(w * 0.22, h * 0.97, "250 BRAZEN CENSERS", CY, 9))
    o.append(f'<path d="M{f(w * 0.46)} {f(h * 0.8)} L {f(w * 0.54)} {f(h * 0.8)}" stroke="#FFD23F" stroke-width="3"></path><path d="M{f(w * 0.54)} {f(h * 0.8)} l -10 -6 l 0 12 z" fill="#FFD23F"></path>' + label(w * 0.5, h * 0.76, "BEATEN OUT", "#FFD23F", 9))
    ax, ay = w * 0.76, h * 0.94; aw = min(w * 0.36, h * 1.2)
    o.append(f'<rect x="{f(ax - aw / 2)}" y="{f(ay - aw * 0.55)}" width="{f(aw)}" height="{f(aw * 0.55)}" fill="{B8.BRASS}" stroke="#0D0D0F" stroke-width="2"></rect>')
    for i in range(6): o.append(f'<rect x="{f(ax - aw / 2 + i * aw / 6)}" y="{f(ay - aw * 0.55)}" width="{f(aw / 6)}" height="{f(aw * 0.55)}" fill="none" stroke="#5A3A1A" stroke-width="1.4"></rect>')
    return "".join(o)

def between(p, w, h, seed):
    """Aaron ran into the midst of the assembly with his censer and stood between the dead and the living: the smoke of the
    incense rises between a darkened side and the living who kneel."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w * 0.5)}" height="{f(h)}" fill="#1A1020"></rect>', f'<rect x="{f(w * 0.5)}" y="0" width="{f(w * 0.5)}" height="{f(h)}" fill="#F3D8A0"></rect>',
         ground(w, h, h * 0.62, "#3A2A2A", dy=0)]
    o.append(f'<rect x="{f(w * 0.5)}" y="{f(h * 0.62)}" width="{f(w * 0.5)}" height="{f(h * 0.38)}" fill="#C8A06A"></rect>')
    for i in range(7):
        yy = h * (0.6 - i * 0.09)
        o.append(f'<ellipse cx="{f(w * 0.5 + math.sin(i) * 14)}" cy="{f(yy)}" rx="{f(w * 0.05 + i * 4)}" ry="{f(h * 0.05)}" fill="#E8E2D6" opacity="{0.7 - i * 0.06:.2f}"></ellipse>')
    s = fit(b, h * 0.36)
    o.append(Q.high_priest(p, w * 0.5, b, s, up=[(-22, -158), (2, -150), (24, -140)]) + censer(w * 0.5 + 26 * s, b - 140 * s, s * 1.4))
    for i in range(5): o.append(E.kneel(w * (0.62 + i * 0.08), b, s * 0.8, color=r.choice(A.HEBREW), skin="#8A5A3E", flip=True))
    return "".join(o)

def rods(w, h, budded=False, names=True):
    """The twelve rods, a name on each, laid up before the testimony; Aaron's rod for the house of Levi budded, blossomed,
    and bare ripe almonds."""
    o = [B8.bp(w, h), B8.title_bar(w, "TWELVE RODS BEFORE THE TESTIMONY" if not budded else "THE ROD OF AARON · BUDS · BLOSSOMS · RIPE ALMONDS")]
    tribes = ["REUBEN", "SIMEON", "LEVI", "JUDAH", "ISSACHAR", "ZEBULUN", "EPHRAIM", "MANASSEH", "BENJAMIN", "DAN", "ASHER", "NAPHTALI"]
    n = len(tribes); top, bot = h * 0.16, h * 0.92
    for i, t in enumerate(tribes):
        x = w * (0.05 + 0.9 * (i + 0.5) / n); lev = t == "LEVI"
        o.append(f'<path d="M{f(x)} {f(bot)} L {f(x + 4)} {f(top)}" stroke="{"#C8A06A" if not (lev and budded) else "#8A5A30"}" stroke-width="{f(max(3, w / 160))}" stroke-linecap="round"></path>')
        if names: o.append(f'<g transform="translate({f(x - 6)} {f(bot - 10)}) rotate(-90)">' + label(0, 0, t if not lev else "AARON", "#FFD23F" if lev else CY, 7, "start", ls=0.08) + '</g>')
        if lev and budded:
            for k in range(7):
                yy = top + (bot - top) * (0.05 + k * 0.08); side = 1 if k % 2 else -1
                o.append(f'<path d="M{f(x + 2)} {f(yy)} C {f(x + side * 10)} {f(yy - 6)} {f(x + side * 16)} {f(yy - 2)} {f(x + side * 18)} {f(yy + 4)}" fill="#4A8A3A" stroke="#0D0D0F" stroke-width="1"></path>')
                o.append(f'<circle cx="{f(x + side * 18)}" cy="{f(yy + 4)}" r="5" fill="#F3D8E8" stroke="#0D0D0F" stroke-width="1"></circle>' if k % 3 else
                         f'<ellipse cx="{f(x + side * 16)}" cy="{f(yy + 6)}" rx="4" ry="6" fill="#C8A06A" stroke="#0D0D0F" stroke-width="1"></ellipse>')
            o.append(V.rays(x, (top + bot) / 2, 24, 20, h * 0.5, color="#FFF4C2", op=0.2))
    return "".join(o)
