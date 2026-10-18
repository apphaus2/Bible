"""New drawings for Numbers chapter 5 (Numbers 9–10): the cloud upon the tabernacle by day and the appearance of fire by
night, the times the cloud tarried, the two trumpets of silver and their calls, the order of march out of the wilderness
of Sinai, and the ark going before the people. Hobab the Midianite (a face for 10:29–32)."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, joshua1 as J, numbers1 as N
from faces_ex import F
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man
from exo import art as A, art8 as B8, art9 as Q
from num.art import ALL, TRIBE_C, CAMPS, standard
def f(v): return f"{v:.1f}"
CY, GOLD, SILVER = B8.CY, B8.GOLD, B8.SILVER

HOBAB = F("adam", skin="#B98A6E", shadow="#5A3A3A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E", scarf="#8A3A2A", band=True, light="#FFC14D")
UNCLEAN = F("adam", skin="#B9886A", shadow="#4A3A4A", hair="#2A1A10", hl="#5A4A3E", stubble="#2A1A10", brow="sorrow", light="#9AA8C8")

def cloud_tab(p, w, h, seed, night=False):
    """The tabernacle with the cloud upon it by day, or the appearance of fire upon it by night."""
    b = h * 0.9
    o = []
    if night: o.append(f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#0B0B2A"></rect>' + mk.stars(60, w, h * 0.5, seed))
    else: o.append(sun(w * 0.88, h * 0.15, 14, op=0.25))
    o.append(ground(w, h, h * 0.62, "#2A1E2A" if night else "#C8A06A", dy=0))
    o.append(N.camp(10, 0, w * 0.3, h * 0.64, h * 0.8, seed, color=("#2A1E22", "#3A2A2A") if night else ("#5A3A22", "#6B4A2A", "#3A2214"))
             + N.camp(10, w * 0.7, w, h * 0.64, h * 0.8, seed + 1, color=("#2A1E22", "#3A2A2A") if night else ("#5A3A22", "#6B4A2A", "#3A2214")))
    o.append(V.tabernacle(w * 0.5, h * 0.82, w * 0.44, uid=p + "tb"))
    if night: o.append(E3.pillar_fire(w * 0.56, h * 0.7, h * 0.05, w * 0.06, seed))
    else: o.append(E3.pillar_cloud(w * 0.56, h * 0.7, -20, w * 0.06, seed))
    return "".join(o)

def tarry(w, h):
    """How long the cloud abode: from evening until morning, two days, a month, a year — the camp stays; when it is taken up, they journey."""
    o = [B8.bp(w, h), B8.title_bar(w, "AS LONG AS THE CLOUD ABODE · THEY REMAINED ENCAMPED")]
    spans = [("EVENING · MORNING", 0.08), ("TWO DAYS", 0.16), ("A MONTH", 0.36), ("A YEAR", 0.94)]
    x0 = w * 0.04; L = w * 0.9; y = 50
    for i, (nm, frac) in enumerate(spans):
        yy = y + i * (h - 70) / 4
        o.append(f'<rect x="{f(x0)}" y="{f(yy)}" width="{f(L * frac)}" height="{f((h - 70) / 4 * 0.5)}" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.4" opacity="0.9"></rect>'
                 + label(x0 + L * frac + 8, yy + (h - 70) / 8 * 0.5 + 4, nm + " ▸ THEN THEY JOURNEYED", "#FFD23F", 8.5, "start", ls=0.06))
    return "".join(o)

def trumpet(x, y, s=1.0, rot=0):
    """A trumpet of silver, of beaten work: a long straight tube flaring to a bell; (x, y) the mouthpiece."""
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">'
            f'<path d="M0 -3 L 200 -5 C 230 -6 250 -26 262 -34 L 262 30 C 250 22 230 6 200 5 L 0 3 Z" fill="{SILVER}" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M0 0 L 200 0" stroke="#F3EFE6" stroke-width="1.4" opacity="0.8"></path>'
            '<rect x="-8" y="-5" width="10" height="10" rx="2" fill="#A8A8B0" stroke="#0D0D0F" stroke-width="1.4"></rect>'
            + "".join(f'<rect x="{x0}" y="-6" width="6" height="12" fill="#A8A8B0" stroke="#0D0D0F" stroke-width="1"></rect>' for x0 in (60, 130)) + '</g>')

def trumpets_plate(w, h):
    """Two trumpets of silver, of beaten work, and their calls."""
    o = [B8.bp(w, h), B8.title_bar(w, "TWO TRUMPETS OF SILVER · OF BEATEN WORK")]
    s = min(1.3, w * 0.5 / 270, h / 200)
    o.append(trumpet(w * 0.5, h * 0.42, s, rot=-6) + trumpet(w * 0.5, h * 0.66, s, rot=6))
    calls = [("BOTH", "ALL THE CONGREGATION"), ("ONE", "THE PRINCES"), ("ALARM", "THE EAST SIDE"), ("ALARM ×2", "THE SOUTH SIDE")]
    for i, (a, b_) in enumerate(calls):
        yy = h * 0.86 + 0 * i
    o.append(label(w * 0.74, h * 0.92, "BOTH · CONGREGATION   ONE · PRINCES   ALARM · EAST   ALARM ×2 · SOUTH", CY, 8, ls=0.04))
    return "".join(o)

def blowing(p, w, h, seed, war=False):
    """The sons of Aaron, the priests, blowing the trumpets at the door of the tent of meeting (or before the host, war=True)."""
    r = random.Random(seed); b = h * 0.9
    o = [mk.defs(p, *ALL), sun(w * 0.88, h * 0.15, 14, op=0.25), ground(w, h, h * 0.56, "#C8B080", dy=0)]
    if not war: o.append(V.tabernacle(w * 0.62, h * 0.6, w * 0.5, uid=p + "tb"))
    s = fit(b, h * 0.36)
    for i, x in enumerate((0.14, 0.3)):
        o.append(Q.son_priest(p, w * x, b, s, up=[(-22, -158), (2, -170), (20, -176)]))
        o.append(trumpet(w * x + 22 * s, b - 176 * s, s * 0.6, rot=-14))
    o.append(J.blasts(w * 0.3 + 190 * s, b - 200 * s, s * 0.8) if hasattr(J, "blasts") else "")
    if war:
        for i in range(10): o.append(man(p, w * (0.5 + i * 0.05), b - (i % 2) * 6, s * 0.8, r.choice(A.HEBREW), flip=True))
    return "".join(o)

ORDER = [("JUDAH", "E"), ("GERSHON · MERARI", "T"), ("REUBEN", "S"), ("KOHATH", "K"), ("EPHRAIM", "W"), ("DAN", "N")]
def march_plan(w, h, hi=None, title="THE ORDER OF MARCH · NUMBERS 10"):
    """The order of march, front at the right: Judah's camp, the tabernacle borne by Gershon and Merari, Reuben's camp, the
    Kohathites bearing the sanctuary, Ephraim's camp, Dan's camp the rearward. hi = indexes to light."""
    o = [B8.bp(w, h), B8.title_bar(w, title)]
    n = len(ORDER); gap = 10; bw = (w - 30 - gap * (n - 1)) / n; y = h * 0.34; bh = h * 0.5
    for k, (nm, key) in enumerate(ORDER):
        x = w - 15 - (k + 1) * bw - k * gap                         # the first to set forward is at the right
        on = hi is None or k in hi
        if key in CAMPS:
            lead, tribes, tot = CAMPS[key]
            for j, (t, cnt) in enumerate(tribes):
                o.append(f'<rect x="{f(x)}" y="{f(y + j * bh / 3)}" width="{f(bw)}" height="{f(bh / 3 - 3)}" fill="{TRIBE_C[t]}" stroke="#0D0D0F" stroke-width="1.4" opacity="{1 if on else 0.3}"></rect>'
                         + label(x + bw / 2, y + j * bh / 3 + bh / 6 + 3, t, "#0D0D0F" if TRIBE_C[t] in ("#E8C840", "#B8C8D8", "#5AC8C8", "#B88A6A", "#E87A2A") else "#F3EFE6", max(6, min(9, bw / 11)), ls=0.04))
        else:
            c = "#5AC8C8" if key == "T" else "#E8B830"
            o.append(f'<rect x="{f(x)}" y="{f(y + bh * 0.3)}" width="{f(bw)}" height="{f(bh * 0.4)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.4" opacity="{1 if on else 0.3}" stroke-dasharray="5 3"></rect>')
            o.append(label(x + bw / 2, y + bh * 0.5 + 3, "THE TABERNACLE" if key == "T" else "THE SANCTUARY", "#0D0D0F", max(6, min(8, bw / 13)), ls=0.04))
        o.append(label(x + bw / 2, y - 8, nm, "#FFD23F" if on else "#6A7A8A", max(6.5, min(9, bw / 10)), ls=0.06))
        o.append(label(x + bw / 2, y + bh + 16, ["FIRST", "", "SECOND", "", "THIRD", "REARWARD"][k], CY if on else "#6A7A8A", 8, ls=0.1))
    o.append(label(w - 16, h - 8, "◂ THEY SET FORWARD", "#FFD23F", 9, "end"))
    return "".join(o)

def procession(p, w, h, seed, ark=True, cloud=True, tribes=("JUDAH", "ISSACHAR", "ZEBULUN")):
    """The camps setting forward by their standards through the wilderness; the ark of the covenant borne before them,
    the cloud of Jehovah over them by day."""
    r = random.Random(seed); b = h * 0.9
    o = [mk.defs(p, *ALL), sun(w * 0.88, h * 0.14, 14, op=0.25), hills(w, h, h * 0.5, seed, color="#B5652E", amp=16), ground(w, h, h * 0.56, "#D8B878", dy=0)]
    if cloud: o.append(f'<g opacity="0.95">' + E3.pillar_cloud(w * 0.72, h * 0.34, -40, w * 0.07, seed) + '</g>')
    s = min(fit(b, h * 0.5), w / 800)
    if ark: o.append(J.ark_borne(p, w * 0.8, b, s * 0.9, p + "ak"))
    for k, t in enumerate(tribes):
        x0 = w * (0.52 - k * 0.2)
        o.append(standard(x0 + 30 * s, b - 6, s * 1.8, TRIBE_C[t], pole=150))
        for i in range(5): o.append(man(p, x0 - i * 22 * s, b - (i % 2) * 5, s * (0.92 - 0.02 * i), r.choice(A.HEBREW), flip=False))
    return "".join(o)
