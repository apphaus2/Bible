"""Drawings and faces for the Deuteronomy volume.

Moses in Deuteronomy is a hundred and twenty years old: white hair and beard under the off-white headcloth with its dark
cord, a brown robe at a distance (deu.art.moses_old). Moods: calm (gold light), stern (red), grieved (cold blue), shining
(white rim). Joshua as Moses' successor: exo.art5.JOSHUA. The signature scene is Moses on a rise in the plains of Moab
speaking to all Israel, Jericho and the Jordan behind them (address)."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, numbers1 as N, joshua1 as J
from faces_ex import F
from genesis.art2 import fit, ground, hills, SKIN, WHITE_BEARD
from genesis.art3 import sun, label, man, woman, grid_bg, node, route
from exo import art as A
from num.art import ALL, TRIBE_C, standard, wilderness_camp
def f(v): return f"{v:.1f}"

def _moses(brow=None, light="#FFC14D", sweat=False):
    return F("adam", skin="#C98E66", shadow="#8A5A3E", hair="#ECE8E0", hl="#B8B2A6", beard=True, beard_color="#ECE8E0", scarf="#E2D8C4", cord=True,
             brow=brow, sweat=sweat, light=light)
MOSES = _moses()
MOSES_CALM = _moses(light="#FFD23F")
MOSES_STERN = _moses(brow="scowl", light="#D7261E")
MOSES_GRIEF = _moses(brow="sorrow", light="#9AA8C8")
MOSES_FIRE = _moses(light="#FF8A3D")

def moses_old(p, x, y, s, flip=False, up=None):
    """Moses at a hundred and twenty: brown robe, off-white headcloth with a dark cord, white beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#7A5A3A", sw=3, flip=flip, up=up, extra=A.headcloth("#E2D8C4") + WHITE_BEARD)

RAISE = [(-22, -158), (-6, -196), (8, -228)]

def address(p, w, h, seed, raise_hand=False, dusk=False):
    """The plains of Moab: Moses on a low rise at the left, all Israel before him in ranks with their standards, the Jordan
    and Jericho's walls far off at the right."""
    r = random.Random(seed); b = h * 0.92
    sky = "#2A1A3A" if dusk else "#F3D8A0"
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{sky}"></rect>', sun(w * 0.84, h * 0.16, 16, color="#FF8A3D", op=0.3)]
    o.append(hills(w, h, h * 0.4, seed, color="#7A5A6A" if dusk else "#9A8A6A", amp=12))
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.46)} C {f(w * 0.62)} {f(h * 0.44)} {f(w * 0.8)} {f(h * 0.48)} {f(w + 10)} {f(h * 0.46)}" fill="none" stroke="#2C9DB8" stroke-width="5"></path>')
    jx = w * 0.82
    o.append(f'<rect x="{f(jx - w * 0.07)}" y="{f(h * 0.33)}" width="{f(w * 0.14)}" height="{f(h * 0.08)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             + "".join(f'<rect x="{f(jx - w * 0.07 + i * w * 0.02)}" y="{f(h * 0.31)}" width="{f(w * 0.012)}" height="{f(h * 0.02)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="1"></rect>' for i in range(7)))
    o.append(ground(w, h, h * 0.5, "#B89A6A" if not dusk else "#5A4A4A", dy=0))
    o.append(f'<path d="M-10 {f(h)} L -10 {f(h * 0.6)} C {f(w * 0.12)} {f(h * 0.56)} {f(w * 0.22)} {f(h * 0.6)} {f(w * 0.3)} {f(h)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    s = fit(h * 0.62, h * 0.24)
    o.append(moses_old(p, w * 0.12, h * 0.62, s, up=RAISE if raise_hand else None))
    for k in range(4):
        y = h * (0.62 + k * 0.1)
        for i in range(14):
            x = w * (0.3 + 0.7 * (i + 0.5 * (k % 2)) / 14)
            o.append(man(p, x, y, fit(y, y - h * (0.12 + 0.04 * k)), r.choice(A.HEBREW), flip=True) if (i + k) % 4 else woman(p, x, y, fit(y, y - h * (0.11 + 0.04 * k)), r.choice(["#6A3A5A", "#4A3A6A", "#8A5A3A"]), flip=True))
    for i, t in enumerate(("JUDAH", "REUBEN", "EPHRAIM", "DAN")):
        o.append(standard(w * (0.38 + i * 0.16), h * 0.64, min(1.2, h / 330), TRIBE_C[t], pole=58))
    return "".join(o)

def horeb(w, h, seed, fire=False):
    """Horeb, the mount of God, its peak in cloud (fire=True: burning with fire unto the heart of heaven)."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{"#2A0A0A" if fire else "#5A6E8A"}"></rect>',
         E4.sinai(w * 0.5, h * 0.94, w * 0.9, h * 0.8, seed, fire=fire), ground(w, h, h * 0.92, "#5A4A3A", dy=0)]
    return "".join(o)

def map_moab(w, h, hi=None):
    """The way round: from Kadesh-barnea, compassing mount Seir, by Elath and Ezion-geber, past Moab and Ar, over the brook
    Zered and the Arnon, to Heshbon; Ammon and the Jabbok to the east."""
    o = [grid_bg(w, h)]
    o.append(f'<ellipse cx="{f(w * 0.34)}" cy="{f(h * 0.3)}" rx="{f(w * 0.03)}" ry="{f(h * 0.1)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>' + label(w * 0.3, h * 0.3, "THE SALT SEA", "#8FD0E2", 8, "end"))
    o.append(f'<path d="M{f(w * 0.34)} 0 L {f(w * 0.34)} {f(h * 0.2)}" stroke="#8FD0E2" stroke-width="3"></path>' + label(w * 0.32, h * 0.08, "JORDAN", "#8FD0E2", 8, "end"))
    regions = [("SEIR · EDOM", 0.3, 0.6, 0.62, 0.92, "#B5442A"), ("MOAB", 0.4, 0.34, 0.66, 0.52, "#C8A030"), ("AMMON", 0.7, 0.1, 0.94, 0.34, "#5A8A4A"), ("SIHON · HESHBON", 0.38, 0.1, 0.66, 0.32, "#6A4A3A")]
    for nm, x0, y0, x1, y1, c in regions:
        on = hi is None or any(k in nm for k in hi)
        o.append(f'<rect x="{f(w * x0)}" y="{f(h * y0)}" width="{f(w * (x1 - x0))}" height="{f(h * (y1 - y0))}" fill="{c}" opacity="{0.55 if on else 0.15}" stroke="{c}" stroke-width="2"></rect>' + label(w * x0 + 8, h * y0 + 14, nm, "#F3EFE6", 9, "start", ls=0.1))
    pts = [("KADESH-BARNEA", 0.12, 0.7), ("EZION-GEBER", 0.44, 0.98), ("ZERED", 0.64, 0.56), ("ARNON", 0.6, 0.34), ("HESHBON", 0.5, 0.18)]
    o.append(route([(w * x, h * y) for _, x, y in pts], color="#FFD23F"))
    for nm, x, y in pts: o.append(node(w * x, h * y, nm, "#FFD23F", r=4, dy=-8, size=8))
    o.append(label(w * 0.82, h * 0.32, "JABBOK", "#8FD0E2", 8))
    return "".join(o)

def giants(w, h, seed):
    """Emim, Anakim, Zamzummim: the tall peoples of old, as great dark silhouettes over the hills (an aside of Moses)."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#3A2A3A"></rect>', hills(w, h, h * 0.7, seed, color="#2A1A2A", amp=14)]
    o.append(mk.defs("gi", *ALL))
    for i, x in enumerate((0.2, 0.42, 0.66, 0.86)):
        o.append(man("gi", w * x, h * 0.9, fit(h * 0.9, h * 0.1) * (1 - 0.1 * (i % 2)), "#1A0E1A"))
    return "".join(o)

def gerizim_ebal(w, h, seed):
    """Mount Gerizim (the blessing, green and lit) and mount Ebal (the curse, bare and dark), the valley between."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#F3D8A0"></rect>', sun(w * 0.24, h * 0.18, 18, color="#FFE680", op=0.35)]
    o.append(f'<path d="M-10 {f(h)} L {f(w * 0.24)} {f(h * 0.22)} L {f(w * 0.5)} {f(h)} Z" fill="#5A8A4A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(f'<path d="M{f(w * 0.5)} {f(h)} L {f(w * 0.76)} {f(h * 0.2)} L {f(w + 10)} {f(h)} Z" fill="#6A5A5A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(label(w * 0.24, h * 0.82, "GERIZIM · THE BLESSING", "#F3EFE6", 10) + label(w * 0.76, h * 0.82, "EBAL · THE CURSE", "#F3EFE6", 10))
    return "".join(o)

def rain(w, h, seed, shut=False):
    """The rain of your land in its season (shut=True: the heavens shut up, the land cracked and bare)."""
    r = random.Random(seed)
    if shut:
        o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#E8B880"></rect>', sun(w * 0.5, h * 0.2, 30, color="#FF8A3D", op=0.4), ground(w, h, h * 0.62, "#B8946A", dy=0)]
        o.append("".join(f'<path d="M{f(r.uniform(0, w))} {f(r.uniform(h * 0.66, h))} l {f(r.uniform(-30, 30))} {f(r.uniform(6, 18))} l {f(r.uniform(-20, 20))} {f(r.uniform(6, 14))}" fill="none" stroke="#7A5A3A" stroke-width="2"></path>' for _ in range(24)))
    else:
        o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#5A6E8A"></rect>', ground(w, h, h * 0.62, "#6A9A4A", dy=0)]
        o.append("".join(f'<path d="M{f(x)} {f(y)} l -6 18" stroke="#CFE6FF" stroke-width="2" opacity="0.8"></path>' for x, y in ((r.uniform(0, w), r.uniform(0, h * 0.6)) for _ in range(90))))
        o.append("".join(f'<path d="M{x} {f(h * 0.62)} L {x} {f(h * 0.52)}" stroke="#C8A030" stroke-width="2"></path>' for x in range(10, int(w), 12)))
    return "".join(o)

def stones_written(w, h, seed):
    """Great stones plastered with plaster and written with all the words of this law, and an altar of unhewn stones
    with its fire, on mount Ebal."""
    import samuel4 as S4
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#E8C8A0"></rect>', sun(w * 0.86, h * 0.16, 16, op=0.3)]
    o.append(f'<path d="M-10 {f(h)} L -10 {f(h * 0.5)} L {f(w * 0.4)} {f(h * 0.3)} L {f(w + 10)} {f(h * 0.56)} L {f(w + 10)} {f(h)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    s = min(1.0, h / 300)
    for i in range(3):
        x = w * (0.1 + i * 0.13); y0 = h * 0.4; sw, sh = w * 0.1, h * 0.46
        o.append(f'<rect x="{f(x)}" y="{f(y0)}" width="{f(sw)}" height="{f(sh)}" rx="6" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></rect>'
                 + "".join(f'<path d="M{f(x + 8)} {f(y0 + 12 + k * 9)} L {f(x + sw - 8)} {f(y0 + 12 + k * 9)}" stroke="#5A4A3A" stroke-width="1.6"></path>' for k in range(int((sh - 20) / 9))))
    o.append(S4.altar(w * 0.74, h * 0.9, s * 1.4, fire=True, seed=seed))
    return "".join(o)

def city_siege(w, h, seed):
    """A city besieged: high walls under a red sky, the camp of the enemy round about it (nothing within is shown)."""
    from genesis.art2 import city
    r = random.Random(seed)
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#3A1A1A"></rect>', V.rays(w * 0.5, h * 0.4, 30, 20, w, color="#FF6A2A", op=0.15)]
    o.append(city(w * 0.5, h * 0.7, w * 0.5, h * 0.4, seed, color="#2A1A1E", lit="#FF6A2A", wall="#3A2A2A"))
    o.append(ground(w, h, h * 0.7, "#2A1A1A", dy=0) + N.camp(16, 0, w, h * 0.74, h * 0.96, seed, color=("#1A0E0E", "#2A1A16")))
    return "".join(o)
