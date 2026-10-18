"""New drawings for Numbers chapter 1 (Numbers 1–2): the camp in the wilderness of Sinai, the standards of the tribes,
the mustering of the men of war, and the plan of the camp round about the tent of meeting (blueprint style, like the
tabernacle pages of Exodus)."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, numbers1 as N
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man
from exo import art as A, art8 as B8, art9 as Q
def f(v): return f"{v:.1f}"
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")

# the twelve tribes as Numbers 2 sets them about the tent of meeting, with a colour for each standard
TRIBE_C = {"REUBEN": "#C8202A", "SIMEON": "#E8C840", "LEVI": "#E04A2A", "JUDAH": "#2E9A4A", "DAN": "#1F5FAD", "NAPHTALI": "#B8C8D8",
           "GAD": "#E87A2A", "ASHER": "#B88A6A", "ISSACHAR": "#8A4AC8", "ZEBULUN": "#5AC8C8", "EPHRAIM": "#3A3A5A", "MANASSEH": "#6A6A8A",
           "BENJAMIN": "#7A9A5A"}
CAMPS = {"E": ("JUDAH", [("JUDAH", "74,600"), ("ISSACHAR", "54,400"), ("ZEBULUN", "57,400")], "186,400"),
         "S": ("REUBEN", [("REUBEN", "46,500"), ("SIMEON", "59,300"), ("GAD", "45,650")], "151,450"),
         "W": ("EPHRAIM", [("EPHRAIM", "40,500"), ("MANASSEH", "32,200"), ("BENJAMIN", "35,400")], "108,100"),
         "N": ("DAN", [("DAN", "62,700"), ("ASHER", "41,500"), ("NAPHTALI", "53,400")], "157,600")}
GOLD = "#E8B830"

def standard(x, y, s=1.0, color="#D7261E", pole=70):
    """A standard: a pole with a square banner and a gold finial; y is the foot of the pole."""
    t = y - pole * s
    return (f'<path d="M{f(x)} {f(y)} L {f(x)} {f(t)}" stroke="#3A2214" stroke-width="{f(3 * s)}"></path>'
            f'<circle cx="{f(x)}" cy="{f(t - 3 * s)}" r="{f(4 * s)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.2"></circle>'
            f'<path d="M{f(x)} {f(t + 2 * s)} L {f(x + 30 * s)} {f(t + 5 * s)} L {f(x + 27 * s)} {f(t + 18 * s)} L {f(x + 30 * s)} {f(t + 31 * s)} L {f(x)} {f(t + 28 * s)} Z" '
            f'fill="{color}" stroke="#0D0D0F" stroke-width="{f(1.6 * s)}" stroke-linejoin="round"></path>'
            f'<path d="M{f(x + 4 * s)} {f(t + 10 * s)} L {f(x + 22 * s)} {f(t + 12 * s)}" stroke="{GOLD}" stroke-width="{f(1.4 * s)}" opacity="0.8"></path>')

def wilderness_camp(p, w, h, seed, cast=(), cloud=True, standards=True, tents=26, base=0.9, sinai=True, dusk=False):
    """The camp in the wilderness of Sinai: the mountain behind, the tabernacle in its court in the midst, the pillar of cloud
    upon it, rows of tents and the standards of the tribes. cast entries: (fn, x, top[, flip[, up]])."""
    r = random.Random(seed); b = h * base
    o = [mk.defs(p, *ALL)]
    if not dusk: o.append(sun(w * 0.88, h * 0.16, 14, op=0.25))
    if sinai: o.append(E4.sinai(w * 0.24, h * 0.48, w * 0.5, h * 0.36, seed, fire=False))
    o.append(ground(w, h, h * 0.46, "#C8A06A" if not dusk else "#7A5A4A", dy=0))
    o.append(N.camp(tents // 2, w * 0.02, w * 0.36, h * 0.5, h * 0.7, seed))
    o.append(N.camp(tents // 2, w * 0.64, w * 0.98, h * 0.5, h * 0.7, seed + 1))
    tx = w * 0.5
    o.append(V.tabernacle(tx, h * 0.6, w * 0.26, uid=p + "tb"))
    if cloud: o.append(E3.pillar_cloud(tx + w * 0.04, h * 0.5, -20, w * 0.045, seed))
    if standards:
        names = ["JUDAH", "REUBEN", "EPHRAIM", "DAN"]
        for i, x in enumerate((0.12, 0.3, 0.7, 0.88)):
            o.append(standard(w * x, h * 0.76, min(1.2, h / 300), TRIBE_C[names[i]], pole=60))
    for c in cast:
        fn, x, top = c[0], c[1], c[2]; flip = c[3] if len(c) > 3 else False; up = c[4] if len(c) > 4 else None
        o.append(fn(p, w * x, b, fit(b, h * top), flip=flip, up=up))
    return "".join(o)

def muster(p, w, h, seed, rows_=4, per=11, scribes=True):
    """The men from twenty years old and upward standing in ranks to be numbered; Moses and Aaron with a scroll at the left."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), sun(w * 0.9, h * 0.14, 14, op=0.25), hills(w, h, h * 0.44, seed, color="#8A6A4A", amp=10), ground(w, h, h * 0.5, "#C8A06A", dy=0)]
    x1 = 0.76 if scribes else 0.98
    for k in range(rows_):                                  # back rank first
        y = h * 0.56 + (b - h * 0.56) * (k + 1) / rows_
        s = fit(y, y - h * (0.16 + 0.1 * k / max(1, rows_ - 1)) * 1.6)
        for i in range(per):
            x = w * (0.03 + (x1 - 0.03) * (i + 0.5 * (k % 2)) / per)
            o.append(man(p, x, y, s, r.choice(A.HEBREW)))
    if scribes:                                             # Moses and Aaron facing the ranks, a scroll in Moses' hand
        s = fit(b, h * 0.42)
        o.append(A.moses(p, w * 0.84, b, s, flip=True, up=[(-22, -158), (-40, -150), (-52, -134)]) + A.aaron(p, w * 0.94, b, s * 0.97, flip=True))
        sx, sy = w * 0.84 + 52 * s, b - 134 * s
        o.append(f'<rect x="{f(sx - 4)}" y="{f(sy - 8 * s)}" width="{f(40 * s)}" height="{f(24 * s)}" rx="3" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    return "".join(o)

def princes(p, w, h, seed, n=12):
    """The twelve princes of the tribes in a line, each with the standard of his tribe beside him."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sun(w * 0.9, h * 0.15, 14, op=0.25), hills(w, h, h * 0.5, seed, color="#8A6A4A", amp=8), ground(w, h, h * 0.56, "#C8A06A", dy=0)]
    names = ["REUBEN", "SIMEON", "JUDAH", "ISSACHAR", "ZEBULUN", "EPHRAIM", "MANASSEH", "BENJAMIN", "DAN", "ASHER", "GAD", "NAPHTALI"][:n]
    s = fit(b, h * 0.5)
    for i, nm in enumerate(names):
        x = w * (0.05 + 0.9 * (i + 0.5) / n)
        o.append(standard(x + 26 * s, b, s * 1.3, TRIBE_C[nm], pole=170))
        o.append(A.elder(TRIBE_C[nm], i)(p, x, b, s))
    return "".join(o)

# ---- the plan of the camp (blueprint) ---------------------------------------------------------------------------------
def camp_plan(w, h, hi=None, title="THE CAMP · EVERY MAN BY HIS OWN STANDARD", totals=True):
    """The camp from above: the tabernacle in its court, the Levites round about it, and the four camps of three tribes
    each — east (Judah), south (Reuben), west (Ephraim), north (Dan). hi = "E" / "S" / "W" / "N" / "L" picks one out."""
    o = [B8.bp(w, h), B8.title_bar(w, title)]
    cx, cy = w * 0.5, h * 0.54
    u = min(w / 15, (h - 40) / 9.5)                           # one unit of the plan
    def blk(x, y, bw, bh, fill, text, sub="", on=True, vertical=False):
        op = "1" if on else "0.35"
        s = (f'<rect x="{f(x)}" y="{f(y)}" width="{f(bw)}" height="{f(bh)}" fill="{fill}" stroke="#0D0D0F" stroke-width="1.6" opacity="{op}"></rect>')
        fs = max(6.5, min(10, u * 0.3))
        light = fill in ("#E8C840", "#B8C8D8", "#5AC8C8", "#B88A6A", "#E87A2A")
        tc, sc = ("#0D0D0F", "#3A1A0A") if light else ("#F3EFE6", "#FFD23F")
        if vertical:
            s += (f'<g transform="translate({f(x + bw / 2)} {f(y + bh / 2)}) rotate(-90)" opacity="{op}">' + label(0, -1, text, tc, fs, ls=0.06)
                  + (label(0, fs + 2, sub, sc, fs * 0.9, ls=0.04) if sub else "") + '</g>')
        else:
            s += f'<g opacity="{op}">' + label(x + bw / 2, y + bh / 2 - 1, text, tc, fs, ls=0.06) + (label(x + bw / 2, y + bh / 2 + fs + 1, sub, sc, fs * 0.9, ls=0.04) if sub else "") + '</g>'
        return s
    # the court and the tent (east is to the right, toward the sunrising)
    o.append(f'<rect x="{f(cx - 2 * u)}" y="{f(cy - u)}" width="{f(4 * u)}" height="{f(2 * u)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             f'<rect x="{f(cx - 1.6 * u)}" y="{f(cy - 0.4 * u)}" width="{f(1.6 * u)}" height="{f(0.8 * u)}" fill="#8A3A2A" stroke="#0D0D0F" stroke-width="1.4"></rect>'
             f'<rect x="{f(cx + 0.6 * u)}" y="{f(cy - 0.22 * u)}" width="{f(0.44 * u)}" height="{f(0.44 * u)}" fill="#B8862A" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    o.append(label(cx, cy + u + 12, "THE TENT OF MEETING", B8.CY, max(6.5, u * 0.26), ls=0.06))
    # the Levites round about
    lv = hi in (None, "L")
    lc = TRIBE_C["LEVI"]
    o.append(f'<rect x="{f(cx - 3.2 * u)}" y="{f(cy - 2.1 * u)}" width="{f(6.4 * u)}" height="{f(4.2 * u)}" fill="none" stroke="{lc}" stroke-width="{f(max(3, u * 0.22))}" stroke-dasharray="{f(u * 0.5)} {f(u * 0.2)}" opacity="{1 if lv else 0.35}"></rect>')
    o.append(label(cx, cy - 1.2 * u, "THE LEVITES", lc, max(6.5, u * 0.26), ls=0.12))
    # the four camps
    for side, (lead, tribes, tot) in CAMPS.items():
        on = hi is None or hi == side
        if side in ("E", "W"):
            x = cx + 3.6 * u if side == "E" else cx - 3.6 * u - 2.6 * u
            for i, (nm, n) in enumerate(tribes):
                y = cy - 3.3 * u + i * 2.2 * u
                o.append(blk(x, y, 2.6 * u, 2.0 * u, TRIBE_C[nm], nm, n, on))
            o.append(label(x + 1.3 * u, cy + 3.5 * u + 12, ("EAST · " if side == "E" else "WEST · ") + tot, "#FFD23F" if on else "#6A7A8A", max(6.5, u * 0.27), ls=0.06))
        else:
            y = cy - 2.5 * u - 2.0 * u if side == "N" else cy + 2.5 * u
            for i, (nm, n) in enumerate(tribes):
                x = cx - 3.3 * u + i * 2.2 * u
                o.append(blk(x, y, 2.0 * u, 2.0 * u, TRIBE_C[nm], nm, n, on))
            ly = y - 6 if side == "N" else y + 2.0 * u + 12
            o.append(label(cx, ly, ("NORTH · " if side == "N" else "SOUTH · ") + tot, "#FFD23F" if on else "#6A7A8A", max(6.5, u * 0.27), ls=0.06))
    # compass: east is toward the sunrising
    o.append(label(min(w - 14, cx + 6.6 * u + 16), cy + 4, "E ▸", "#FFD23F", 10))
    if totals: o.append(label(w * 0.86, h - 10, "603,550", "#FFD23F", 12, ls=0.1))
    return "".join(o)

def levites_round(p, w, h, seed):
    """The Levites encamped round about the tabernacle of the testimony, keeping the charge of it; the people beyond."""
    b = h * 0.9; r = random.Random(seed)
    o = [mk.defs(p, *ALL), sun(w * 0.88, h * 0.15, 14, op=0.25), ground(w, h, h * 0.44, "#C8A06A", dy=0)]
    o.append(N.camp(10, w * 0.0, w * 0.2, h * 0.46, h * 0.56, seed) + N.camp(10, w * 0.8, w * 1.0, h * 0.46, h * 0.56, seed + 1))
    o.append(V.tabernacle(w * 0.5, h * 0.7, w * 0.5, uid=p + "tb"))
    o.append(E3.pillar_cloud(w * 0.56, h * 0.56, -20, w * 0.04, seed))
    for i in range(9):                                       # Levites in white tunics round the court
        x = w * (0.18 + 0.64 * i / 8); y = b - (i % 2) * 4
        o.append(man(p, x, y, fit(y, max(h * 0.56, y - 220)), "#E8E2D6", flip=x > w / 2))
    return "".join(o)
