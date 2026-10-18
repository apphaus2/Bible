"""New drawings for Numbers chapter 4 (Numbers 7–8): the six covered wagons and twelve oxen, the wagons given to Gershon
and Merari (a chart), the oblation of each prince as a strip of icons, the totals of the dedication, the Voice from above
the mercy-seat, the seven lamps, and the cleansing and waving of the Levites."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V, samuel1 as S1
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man
from exo import art as A, art8 as B8, art9 as Q
from lev.art import goat, flour, incense, altar
from lev.art3 import BOTH
from lev.art5 import water
from num.art import ALL, TRIBE_C, standard
def f(v): return f"{v:.1f}"
CY, GOLD, SILVER = B8.CY, B8.GOLD, B8.SILVER

def wagon(x, y, s=1.0, cover="#C8B890", ox=True, ox_c="#8A5A30"):
    """A covered wagon (a two-wheeled cart with a hooped cover) and its ox, heading right; (x, y) = ground under the wheel."""
    load = ('<path d="M-86 -82 L -86 -118 C -60 -150 30 -150 56 -118 L 56 -82 Z" fill="' + cover + '" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M-60 -82 L -60 -138 M-16 -82 L -16 -146 M28 -82 L 28 -138" stroke="#8A7A5A" stroke-width="1.6"></path>')
    o = ""
    if ox: o += S1.cow(x + 280 * s, y, 0.92 * s, color=ox_c, patch="#E8E2D6") + S1.yoke(x + 330 * s, y - 104 * s, s)
    return S1.cart(x, y, s, load=load) + o

def wagons(p, w, h, seed):
    """Six covered wagons and twelve oxen presented before the tabernacle."""
    b = h * 0.92; r = random.Random(seed)
    o = [mk.defs(p, *ALL), sun(w * 0.88, h * 0.15, 14, op=0.25), ground(w, h, h * 0.44, "#C8B080", dy=0), V.tabernacle(w * 0.5, h * 0.5, w * 0.4, uid=p + "tb")]
    s = min(h / 640, w / 1900)
    for i in range(6):
        row, col = divmod(i, 3)
        x = w * (0.04 + col * 0.32) + (row * w * 0.06); y = h * (0.66 + row * 0.24)
        o.append(wagon(x, y, s * (0.85 + row * 0.15), ox_c=r.choice(["#8A5A30", "#5A3A22", "#C9A27A"])))
        o.append(S1.cow(x + 200 * s, y + 6, 0.7 * s * (0.85 + row * 0.15), color=r.choice(["#8A5A30", "#5A3A22", "#6A4A2A"]), patch="#E8E2D6"))
    return "".join(o)

def wagons_chart(w, h):
    """Two wagons and four oxen to Gershon, four wagons and eight oxen to Merari, none to Kohath: upon their shoulders."""
    o = [B8.bp(w, h), B8.title_bar(w, "THE WAGONS AND THE OXEN · TO EVERY MAN ACCORDING TO HIS SERVICE")]
    rows_ = [("GERSHON", 2, 4, "#5AC8C8"), ("MERARI", 4, 8, "#8A6A4A"), ("KOHATH", 0, 0, "#E8B830")]
    rh = (h - 40) / 3
    for k, (nm, wg, ox, c) in enumerate(rows_):
        y = 40 + rh * (k + 0.72)
        o.append(label(w * 0.58, y - rh * 0.25, nm, c, 12, "start", ls=0.12))
        if wg:
            for i in range(wg):
                o.append(f'<g transform="translate({f(w * 0.58 + i * 54)} {f(y)}) scale(0.22)">' + wagon(0, 0, 1.0, ox=False) + '</g>')
            o.append(label(w * 0.98, y - 4, f"{wg} WAGONS · {ox} OXEN", "#FFD23F", 9, "end"))
        else:
            o.append(label(w * 0.98, y - 4, "NONE · UPON THEIR SHOULDERS", "#FFD23F", 9, "end"))
    return "".join(o)

# ---- the oblation of a prince ----------------------------------------------------------------------------------------
def platter(x, y, s=1.0): return f'<ellipse cx="{f(x)}" cy="{f(y - 6 * s)}" rx="{f(26 * s)}" ry="{f(7 * s)}" fill="{SILVER}" stroke="#0D0D0F" stroke-width="1.6"></ellipse><ellipse cx="{f(x)}" cy="{f(y - 9 * s)}" rx="{f(16 * s)}" ry="{f(4 * s)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1"></ellipse>'
def bowl(x, y, s=1.0): return f'<path d="M{f(x - 18 * s)} {f(y - 18 * s)} C {f(x - 16 * s)} {f(y)} {f(x + 16 * s)} {f(y)} {f(x + 18 * s)} {f(y - 18 * s)} Z" fill="{SILVER}" stroke="#0D0D0F" stroke-width="1.6"></path><ellipse cx="{f(x)}" cy="{f(y - 18 * s)}" rx="{f(18 * s)}" ry="{f(4 * s)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1"></ellipse>'
def spoon(x, y, s=1.0): return f'<path d="M{f(x - 22 * s)} {f(y - 4 * s)} L {f(x)} {f(y - 10 * s)}" stroke="{GOLD}" stroke-width="{f(4 * s)}" stroke-linecap="round"></path><ellipse cx="{f(x + 8 * s)}" cy="{f(y - 11 * s)}" rx="{f(10 * s)}" ry="{f(6 * s)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.4"></ellipse><circle cx="{f(x + 8 * s)}" cy="{f(y - 15 * s)}" r="{f(3 * s)}" fill="#F3EFE6" opacity="0.8"></circle>'

def oblation(w, h, tribe=None, days_=1):
    """The oblation of one prince (or of all twelve when days_=12): the vessels, the burnt-offering, the sin-offering and the
    peace-offerings, each icon with its count, standing on a ground line."""
    b = h - 20; s = min(1.0, h / 120, w / 760)
    o = [f'<path d="M0 {f(b)} L {f(w)} {f(b)}" stroke="#0D0D0F" stroke-width="2"></path>']
    items = [(platter, "SILVER PLATTER", 130), (bowl, "SILVER BOWL", 70), (spoon, "GOLDEN SPOON", 10)]
    x = w * 0.04
    for fn, nm, wt in items:                          # each vessel: its weight in shekels above it, and ×12 for the twelve
        o.append(fn(x + 26 * s, b, s) + label(x + 26 * s, b + 12, nm, "#0D0D0F", 6.5, ls=0.04)
                 + label(x + 26 * s, b - 34 * s, f"{wt} SHEKELS", "#3A2A1A", 6.5, ls=0.04)
                 + (label(x + 26 * s, b - 44 * s - 4, f"×{days_}", "#D7261E", 11, ls=0.04) if days_ > 1 else ""))
        x += 72 * s
    beasts = [("BULLOCK", 1, lambda X: S1.cow(X, b, 0.26 * s, color="#8A5A30", patch="#E8E2D6")), ("RAM", 1, lambda X: E.sheep(X, b, 0.32 * s)),
              ("HE-LAMB", 1, lambda X: E3.lamb(X, b, 0.26 * s)), ("HE-GOAT", 1, lambda X: goat(X, b, 0.34 * s)),
              ("OXEN", 2, lambda X: S1.cow(X, b, 0.26 * s, color="#5A3A22", patch="#E8E2D6")), ("RAMS", 5, lambda X: E.sheep(X, b, 0.32 * s)),
              ("HE-GOATS", 5, lambda X: goat(X, b, 0.34 * s)), ("HE-LAMBS", 5, lambda X: E3.lamb(X, b, 0.26 * s))]
    gw = (w * 0.98 - x) / len(beasts)
    for i, (nm, n, draw) in enumerate(beasts):
        cx = x + gw * (i + 0.5)
        if i == 4: o.append(f'<path d="M{f(cx - gw * 0.5)} {f(b - 50 * s)} L {f(cx - gw * 0.5)} {f(b)}" stroke="#0D0D0F" stroke-width="1.4" stroke-dasharray="3 3"></path>')
        o.append(draw(cx) + label(cx, b + 12, nm, "#0D0D0F", 6.5, ls=0.04) + label(cx, b - 44 * s, f"×{n * days_}", "#D7261E", 11, ls=0.04))
    o.append(label(x + gw * 2, 12, "BURNT-OFFERING · SIN-OFFERING", "#3A2A1A", 6.5, ls=0.08) + label(x + gw * 6, 12, "PEACE-OFFERINGS", "#3A2A1A", 6.5, ls=0.08))
    return "".join(o)

def voice(p, w, h, seed):
    """Moses in the tent of meeting before the veil-hidden ark: the Voice from above the mercy-seat, between the cherubim."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#1A0E12"></rect>', V.rays(w * 0.66, h * 0.4, 36, 30, max(w, h), color="#FFF4C2", op=0.25)]
    o.append(f'<g transform="translate({f(w * 0.36)} {f(h * 0.02)})">' + B8.mercy_seat(w * 0.62, h * 0.86, grid=False) + '</g>')
    o.append(mk.defs(p, *ALL) + A.moses(p, w * 0.16, h * 0.96, fit(h * 0.96, h * 0.36), flip=False))
    return "".join(o)

def lamps(p, w, h, seed):
    """Aaron lighting the seven lamps so that they give light in front of the candlestick."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#1A0E12"></rect>', V.rays(w * 0.62, h * 0.3, 30, 20, max(w, h), color="#FFC14D", op=0.18)]
    o.append(f'<g transform="translate({f(w * 0.36)} 0)">' + B8.lampstand(w * 0.6, h, lit=True) + '</g>')
    o.append(mk.defs(p, *ALL) + Q.high_priest(p, w * 0.2, h * 0.98, fit(h * 0.98, h * 0.32), up=[(-22, -158), (2, -170), (26, -180)]))
    return "".join(o)

def cleansing(p, w, h, seed, stage="sprinkle"):
    """The cleansing of the Levites: sprinkled with the water of expiation, shaven, washing their clothes (stage
    "sprinkle"); the children of Israel laying their hands upon them ("hands"); Aaron waving them before Jehovah ("wave")."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), sun(w * 0.88, h * 0.15, 14, op=0.25), ground(w, h, h * 0.5, "#C8B080", dy=0), V.tabernacle(w * 0.72, h * 0.56, w * 0.4, uid=p + "tb")]
    s = fit(b, h * 0.42)
    if stage == "sprinkle":
        o.append(A.moses(p, w * 0.12, b, s, up=[(-22, -158), (4, -150), (30, -150)]))
        o.append("".join(f'<circle cx="{f(w * 0.2 + i * 9)}" cy="{f(b - 150 * s + (i % 3) * 8)}" r="2.6" fill="#8FD0E2"></circle>' for i in range(8)))
        for i in range(5): o.append(man(p, w * (0.3 + i * 0.1), b - (i % 2) * 4, s * 0.96, "#E8E2D6", flip=True))
        o.append(water(w * 0.86, b - 10, 80) + E3.basin(w * 0.86, b - 14, 34))
    elif stage == "hands":
        for i in range(5): o.append(man(p, w * (0.36 + i * 0.1), b, s * 0.96, "#E8E2D6"))
        for i in range(4): o.append(man(p, w * (0.06 + i * 0.07), b, s, r.choice(A.HEBREW), up=[(-22, -158), (10, -170), (34, -176)]))
    else:
        o.append(V.rays(w * 0.5, h * 0.3, 30, 20, max(w, h), color="#FFF4C2", op=0.25))
        o.append(Q.high_priest(p, w * 0.14, b, s, up=BOTH))
        for i in range(6): o.append(man(p, w * (0.32 + i * 0.1), b - (i % 2) * 4, s * 0.96, "#E8E2D6", flip=True, up=BOTH))
    return "".join(o)

def ages(w, h):
    """From twenty and five years old the Levites go in to the service; from fifty they cease, and minister with their brethren."""
    o = [B8.bp(w, h), B8.title_bar(w, "THE SERVICE OF THE LEVITES")]
    x0, x1 = w * 0.08, w * 0.94; y = h * 0.6; X = lambda a: x0 + (x1 - x0) * (a - 20) / 50
    o.append(f'<path d="M{f(x0)} {f(y)} L {f(x1)} {f(y)}" stroke="{CY}" stroke-width="2"></path>')
    o.append(f'<rect x="{f(X(25))}" y="{f(y - 22)}" width="{f(X(50) - X(25))}" height="22" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.4"></rect>'
             + label((X(25) + X(50)) / 2, y - 7, "THE SERVICE · THE WORK OF THE TENT", "#0D0D0F", 8.5))
    o.append(f'<rect x="{f(X(50))}" y="{f(y - 22)}" width="{f(X(70) - X(50))}" height="22" fill="#5A6E8A" stroke="#0D0D0F" stroke-width="1.4"></rect>'
             + label((X(50) + X(70)) / 2, y - 7, "KEEP THE CHARGE", "#F3EFE6", 8.5))
    for a in (20, 25, 30, 40, 50, 60, 70):
        o.append(f'<path d="M{f(X(a))} {f(y)} L {f(X(a))} {f(y + 6)}" stroke="{CY}" stroke-width="1.4"></path>' + label(X(a), y + 18, str(a), CY, 9))
    return "".join(o)
