"""Drawings for the Joshua volume (chapters 1–2 first; later chapters add theirs below).

Joshua at a distance: a rust-red robe and headcloth (joshua_fig). The two spies: plain tunics, bareheaded. Rahab at a
distance: a scarlet headscarf and robe. Jericho: joshua1.jericho (mud-brick wall, towers, Rahab's window in the wall)."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus4 as E4, exodus5 as V, numbers1 as N, joshua1 as J
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import sun, label, man, woman
from exo import art as A
from num.art import ALL, TRIBE_C, standard

def f(v): return f"{v:.1f}"
WAR = ("#8A3A1E", "#5A2A16", "#3A2214", "#5A6E8A")
JOSHUA_C = "#B5421E"
SPY_C = ("#7A6A4A", "#5A6A7A")

def joshua_fig(p, x, y, s, flip=False, up=None):
    """Joshua at a distance: rust-red robe and headcloth, black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=JOSHUA_C, sw=3, flip=flip, up=up,
                     extra=A.headcloth(JOSHUA_C) + A.BLACK_BEARD)

def warrior(p, x, y, s, cloth, flip=False):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind="Tunic", sw=3, flip=flip, extra=E4.SPEAR)

def rahab_fig(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#B5121B", woman=True, hair="#1A1210", sw=3, flip=flip, up=up,
                     extra=A.headcloth("#D7261E"))

def night(w, h, seed, color="#0B0B2A"):
    return f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{color}"></rect>' + mk.stars(40, w, h * 0.5, seed)

# ---- Joshua 1–2 ---------------------------------------------------------------------------------------------------------
def armed(p, w, h, seed, tribes=("REUBEN", "GAD", "MANASSEH")):
    """The mighty men of valor of Reuben, Gad and the half-tribe of Manasseh, armed, in ranks before the Jordan."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.84, h * 0.16, 16, color="#FF8A3D", op=0.3),
         hills(w, h, h * 0.36, seed, color="#9A8A6A", amp=12),
         f'<path d="M-10 {f(h * 0.42)} C {f(w * 0.3)} {f(h * 0.4)} {f(w * 0.6)} {f(h * 0.46)} {f(w + 10)} {f(h * 0.42)}" fill="none" stroke="#2C9DB8" stroke-width="6"></path>',
         ground(w, h, h * 0.46, "#B89A6A", dy=0)]
    for i, t in enumerate(tribes):
        o.append(standard(w * (0.2 + i * 0.3), h * 0.6, min(1.2, h / 330), TRIBE_C[t], pole=58))
    for k in range(3):
        y = h * (0.66 + k * 0.12)
        for i in range(16):
            x = w * ((i + 0.5 * (k % 2)) / 15)
            o.append(warrior(p, x, y, fit(y, y - h * (0.14 + 0.05 * k)), r.choice(WAR)))
    return "".join(o)

def jericho_night(p, w, h, seed, men=True, window_lit=True):
    """Jericho by night: the wall and its gate, Rahab's house in the wall; the king's men with torches at the door."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), night(w, h, seed)]
    o.append(J.jericho(-10, w + 10, h * 0.3, b, seed, color="#7A4A2A", towers=3, window=(w * 0.62, h * 0.52) if window_lit else None))
    o.append(f'<path d="M{f(w * 0.2)} {f(b)} L {f(w * 0.2)} {f(h * 0.62)} C {f(w * 0.2)} {f(h * 0.54)} {f(w * 0.34)} {f(h * 0.54)} {f(w * 0.34)} {f(h * 0.62)} L {f(w * 0.34)} {f(b)} Z" fill="#12090A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(ground(w, h, b, "#2A1A14", dy=0))
    if men:
        for i in range(4):
            x = w * (0.42 + i * 0.07)
            o.append(mk.person(p, round(x), round(b), round(fit(b, h * 0.6), 3), body="#12090A", cloth="#2A1A14", sw=3, flip=True, up=[(-22, -158), (-14, -186), (-6, -206)])
                     + f'<circle cx="{f(x + 6 * fit(b, h * 0.6) * (-1))}" cy="{f(b - 212 * fit(b, h * 0.6))}" r="{f(10 * fit(b, h * 0.6) + 4)}" fill="#FFC14D" opacity="0.9"></circle>')
    return "".join(o)

def scarlet(w, h, seed, cord=None):
    """Rahab's window in the wall by day, the line of scarlet thread bound in it."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8FD0E2"></rect>', sun(w * 0.86, h * 0.14, 16, op=0.25)]
    o.append(J.jericho(-10, w + 10, h * 0.24, h + 10, seed, towers=2, window=(w * 0.5, h * 0.46), cord=cord or h * 0.4))
    return "".join(o)

def mountain_hide(p, w, h, seed):
    """The mountain: the two men hidden in a cleft of the rock by night, the pursuers' torches far below on the way."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), night(w, h, seed, "#14123A"), hills(w, h, h * 0.62, seed, color="#2A2440", amp=20)]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.3)} C {f(w * 0.2)} {f(h * 0.2)} {f(w * 0.4)} {f(h * 0.3)} {f(w * 0.56)} {f(h + 10)} Z" fill="#3A3048" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(f'<path d="M{f(w * 0.12)} {f(h * 0.62)} C {f(w * 0.14)} {f(h * 0.46)} {f(w * 0.3)} {f(h * 0.46)} {f(w * 0.32)} {f(h * 0.62)} Z" fill="#0B0814" stroke="#0D0D0F" stroke-width="2"></path>')
    s = fit(h * 0.62, h * 0.5) * 0.9
    o.append(mk.person(p, round(w * 0.19), round(h * 0.62), round(s, 3), body="#2A2430", cloth="#4A4458", kind="Tunic", sw=2) + mk.person(p, round(w * 0.25), round(h * 0.62), round(s, 3), body="#2A2430", cloth="#3A3448", kind="Tunic", sw=2, flip=True))
    o.append(f'<path d="M{f(w * 0.6)} {f(h * 0.94)} C {f(w * 0.7)} {f(h * 0.82)} {f(w * 0.86)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.76)}" fill="none" stroke="#5A4A3A" stroke-width="4" stroke-dasharray="10 6"></path>')
    for i in range(4):
        x = w * (0.66 + i * 0.08); y = h * (0.88 - i * 0.03)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="5" fill="#FFC14D"></circle><circle cx="{f(x)}" cy="{f(y)}" r="11" fill="#FFC14D" opacity="0.3"></circle>')
    return "".join(o)

def report(p, w, h, seed):
    """The two men come again to Joshua in the camp at Shittim."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.2, h * 0.16, 16, color="#FF8A3D", op=0.3),
         hills(w, h, h * 0.4, seed, color="#9A8A6A", amp=12), ground(w, h, h * 0.5, "#B89A6A", dy=0)]
    o.append("".join(E4.tent(w * x, h * 0.56, w * 0.08, h * 0.1, color=c) for x, c in ((0.08, "#5A3A22"), (0.9, "#6B4A2A"), (0.78, "#3A2214"))))
    s = fit(b, h * 0.36)
    o.append(joshua_fig(p, w * 0.66, b, s, flip=True))
    o.append(man(p, w * 0.36, b, s * 0.96, SPY_C[0], up=[(-22, -158), (4, -150), (30, -150)]) + man(p, w * 0.46, b, s * 0.94, SPY_C[1]))
    return "".join(o)

# ---- Joshua 3–5 ---------------------------------------------------------------------------------------------------------
def crowd_at(p, w, h, seed, x0, x1, y0, y1, n, smin, smax, flip=False):
    """People of Israel at a distance, scaled by depth (nearer = lower = larger)."""
    r = random.Random(seed); items = sorted((r.uniform(y0, y1), r.uniform(x0, x1)) for _ in range(n)); o = []
    for y, x in items:
        k = (y - y0) / max(1, y1 - y0); s = smin + (smax - smin) * k
        o.append((man if r.random() < 0.6 else woman)(p, x, y, s, r.choice(A.HEBREW + ["#C2456A", "#5A6E8A"]), flip=flip))
    return "".join(o)

def ark_ahead(p, w, h, seed):
    """The ark goes before toward the Jordan; the people follow with a space of about two thousand cubits between."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.86, h * 0.16, 16, color="#FF8A3D", op=0.3),
         hills(w, h, h * 0.4, seed, color="#9A8A6A", amp=12), f'<path d="M-10 {f(h * 0.46)} C {f(w * 0.3)} {f(h * 0.44)} {f(w * 0.6)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.46)}" fill="none" stroke="#2C9DB8" stroke-width="7"></path>',
         ground(w, h, h * 0.5, "#B89A6A", dy=0)]
    o.append(J.ark_borne(p, w * 0.78, h * 0.72, fit(h * 0.72, h * 0.5) * 0.9, f"aa{seed}", glow=True))
    o.append(crowd_at(p, w, h, seed, -10, w * 0.32, h * 0.66, b, 26, fit(h * 0.66, h * 0.5) * 0.8, fit(b, h * 0.6)))
    y = h * 0.6
    o.append(f'<path d="M{f(w * 0.34)} {f(y)} L {f(w * 0.66)} {f(y)}" stroke="#D7261E" stroke-width="2.4" stroke-dasharray="8 6"></path>'
             f'<path d="M{f(w * 0.34)} {f(y - 8)} L {f(w * 0.34)} {f(y + 8)} M{f(w * 0.66)} {f(y - 8)} L {f(w * 0.66)} {f(y + 8)}" stroke="#D7261E" stroke-width="2.4"></path>'
             + label(w * 0.5, y - 10, "≈ 2000 CUBITS", "#D7261E", 11))
    return "".join(o)

def stones_carried(p, w, h, seed):
    """Twelve men, a man of every tribe, each with a stone upon his shoulder, coming up out of the dry bed of the Jordan."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8FD0E2"></rect>',
         J.heap(w * 0.12, h * 0.62, w * 0.3, h * 0.5, f"sc{seed}"), ground(w, h, h * 0.6, "#8A7A6A", dy=0), J.riverbed(0, w, h * 0.62, h, seed)]
    names = list(TRIBE_C)[:13]; names.remove("LEVI")
    s = fit(b, h * 0.42)
    for i, t in enumerate(names):
        x = w * (0.2 + i * 0.065); y = b - (i % 2) * h * 0.05
        o.append(man(p, x, y, s * (0.92 if i % 2 else 1), TRIBE_C[t], up=[(-22, -158), (-30, -186), (-14, -204)])
                 + f'<ellipse cx="{f(x - 16 * s)}" cy="{f(y - 214 * s)}" rx="{f(22 * s)}" ry="{f(15 * s)}" fill="#A89A86" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    return "".join(o)

def waters_return(p, w, h, seed):
    """The priests come up out of the Jordan with the ark, and the waters return and go over all its banks."""
    b = h * 0.62
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8FD0E2"></rect>', hills(w, h, h * 0.36, seed, color="#5A8A4A", amp=14),
         f'<path d="M-10 {f(h * 0.44)} C {f(w * 0.3)} {f(h * 0.4)} {f(w * 0.6)} {f(h * 0.52)} {f(w + 10)} {f(h * 0.44)} L {f(w + 10)} {f(h * 0.7)} C {f(w * 0.6)} {f(h * 0.76)} {f(w * 0.3)} {f(h * 0.66)} -10 {f(h * 0.72)} Z" fill="#1F6F9A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i in range(7):
        y = h * (0.48 + i * 0.03)
        o.append(f'<path d="M{f(w * 0.05 + i * 30)} {f(y)} C {f(w * 0.3)} {f(y - 8)} {f(w * 0.6)} {f(y + 8)} {f(w * 0.95 - i * 20)} {f(y)}" fill="none" stroke="#E8F6FA" stroke-width="2" opacity="0.6"></path>')
    o.append(ground(w, h, h * 0.74, "#B89A6A", dy=0))
    o.append(J.ark_borne(p, w * 0.5, h * 0.95, fit(h * 0.95, h * 0.62) * 0.85, f"wr{seed}", glow=True))
    return "".join(o)

def gilgal(p, w, h, seed, people=True):
    """Gilgal on the east border of Jericho: the twelve stones out of the Jordan set up, the camp beyond, Jericho far off."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.14, h * 0.16, 16, color="#FF8A3D", op=0.3),
         hills(w, h, h * 0.38, seed, color="#9A8A6A", amp=12), J.jericho(w * 0.66, w * 0.96, h * 0.34, h * 0.42, seed, towers=1, houses=False), ground(w, h, h * 0.42, "#B89A6A", dy=0),
         N.camp(18, w * 0.02, w * 0.6, h * 0.44, h * 0.56, seed)]
    for i in range(12):
        col, row = i % 6, i // 6
        x = w * (0.32 + col * 0.07 + row * 0.035); y = h * (0.68 + row * 0.08); rw = w * 0.026; rh = h * (0.08 + 0.02 * ((i * 7) % 3))
        o.append(f'<path d="M{f(x - rw)} {f(y)} L {f(x - rw * 0.8)} {f(y - rh)} L {f(x + rw * 0.7)} {f(y - rh * 1.06)} L {f(x + rw)} {f(y)} Z" fill="#A89A86" stroke="#0D0D0F" stroke-width="2.2"></path>')
    if people:
        o.append(joshua_fig(p, w * 0.86, b, fit(b, h * 0.48), flip=True))
        o.append(crowd_at(p, w, h, seed + 1, w * 0.02, w * 0.24, h * 0.7, b, 9, fit(h * 0.7, h * 0.52) * 0.8, fit(b, h * 0.6)))
    return "".join(o)

def kings_afar(p, w, h, seed):
    """The kings of the Amorites and of the Canaanites on a ridge at evening, looking toward the Jordan."""
    b = h * 0.62
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A1A2E"></rect>', sun(w * 0.8, h * 0.5, 30, color="#FF6A2A", op=0.4),
         f'<path d="M-10 {f(h + 10)} L -10 {f(b)} C {f(w * 0.3)} {f(b - h * 0.06)} {f(w * 0.6)} {f(b - h * 0.04)} {f(w + 10)} {f(b + h * 0.06)} L {f(w + 10)} {f(h + 10)} Z" fill="#1A0A14" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = fit(b, h * 0.22)
    for i in range(7):
        x = w * (0.08 + i * 0.12); y = b - h * 0.04 + abs(i - 3) * h * 0.005
        o.append(mk.person(p, round(x), round(y), round(s, 3), body="#12090A", cloth="#12090A", sw=3, flip=True,
                           extra='<path d="M-14 -200 L -14 -214 L -7 -206 L 0 -218 L 7 -206 L 14 -214 L 14 -200 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>'))
    return "".join(o)

def flint(w, h, seed):
    """Knives of flint laid on a stone at Gilgal (Joshua 5:2–3); the camp abiding in its place beyond."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8C88A"></rect>', hills(w, h, h * 0.4, seed, color="#9A8A6A", amp=12),
         ground(w, h, h * 0.46, "#B89A6A", dy=0), N.camp(22, -10, w + 10, h * 0.48, h * 0.62, seed)]
    o.append(f'<path d="M{f(w * 0.2)} {f(h * 0.96)} C {f(w * 0.22)} {f(h * 0.74)} {f(w * 0.78)} {f(h * 0.72)} {f(w * 0.8)} {f(h * 0.96)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for i in range(3):
        cx = w * (0.34 + i * 0.16); cy = h * 0.82
        o.append(f'<path d="M{f(cx - 50)} {f(cy)} L {f(cx + 40)} {f(cy - 14)} L {f(cx + 52)} {f(cy - 4)} L {f(cx - 40)} {f(cy + 10)} Z" fill="#4A4A5A" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<path d="M{f(cx - 30)} {f(cy + 2)} L {f(cx + 34)} {f(cy - 9)}" stroke="#8A8AA0" stroke-width="1.6"></path>')
    return "".join(o)

# ---- Joshua 6–7 ---------------------------------------------------------------------------------------------------------
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "digest"))
from genesis.art3 import node, route, grid_bg

def procession(p, w, h, seed, dawn=False):
    """Round the wall of Jericho: the armed men, seven priests blowing rams' horns, the ark, the rearward."""
    import joshua_book1 as JB
    b = h * 0.92
    sky = "#FF8A3D" if dawn else "#8FD0E2"
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{sky}"></rect>']
    if dawn: o.append(sun(w * 0.12, h * 0.4, 30, color="#FFE680", op=0.5))
    o.append(J.jericho(-10, w + 10, h * 0.22, h * 0.76, seed, towers=3))
    o.append(ground(w, h, h * 0.76, "#8A6A4A", dy=0))
    s = fit(b, h * 0.5) * 0.9
    o.append(JB.procession(p, -w * 0.02, w, round(b), s, seed))
    return "".join(o)

def rahab_out(p, w, h, seed):
    """The two young men bring out Rahab and her father's household, the scarlet line still in the window above."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8A35A"></rect>',
         J.jericho(-10, w * 0.6, h * 0.14, h * 0.7, seed, towers=1, window=(w * 0.32, h * 0.32), cord=h * 0.3),
         J.collapse(w * 0.6, w + 10, h * 0.7, h * 0.4, seed), ground(w, h, h * 0.7, "#8A6A4A", dy=0)]
    s = fit(b, h * 0.44)
    o.append(man(p, w * 0.86, b, s, SPY_C[0], flip=True, up=[(-22, -158), (4, -150), (30, -150)]))
    o.append(rahab_fig(p, w * 0.72, b, s * 0.96, flip=True))
    fam = [("man", "#5A6E8A"), ("woman", "#8A5A3A"), ("man", "#6A5A3A"), ("woman", "#4A3A6A"), ("man", "#7A4A2E")]
    for i, (k, c) in enumerate(fam):
        x = w * (0.6 - i * 0.08); ss = s * (0.94 - 0.02 * i)
        o.append((man if k == "man" else woman)(p, x, b - i * 3, ss, c, flip=True))
    o.append(man(p, w * 0.14, b, s, SPY_C[1], flip=True))
    return "".join(o)

def burning(w, h, seed, city="jericho"):
    """The city burnt with fire, seen from afar: flames along the broken wall and a column of smoke."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A0A0A"></rect>']
    for i in range(9):
        cx = w * (0.3 + r.uniform(0, 0.4)); cy = h * (0.1 + i * 0.05); rr = w * r.uniform(0.08, 0.16)
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(rr)}" fill="#3A2A2E" opacity="0.8"></circle>')
    if city == "jericho": o.append(J.collapse(-10, w + 10, h * 0.82, h * 0.3, seed, color="#5A3A2A"))
    else: o.append(J.city_hill(w * 0.5, h * 0.86, w * 0.5, h * 0.5, seed))
    o += [E.blaze(w * (0.1 + i * 0.16), h * 0.8, w * 0.14, h * 0.32, seed + i, n=7) for i in range(6)]
    o.append(ground(w, h, h * 0.84, "#1A0A0A", dy=0))
    return "".join(o)

def devoted(w, h, seed):
    """Inside a tent: the goodly Babylonish mantle, the wedge of gold, the shekels of silver, hid in the earth."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1408"></rect>',
         f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.5)} -10 L {f(w + 10)} {f(h * 0.7)} Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.7, "#4A2A18", dy=0)]
    cx, cy = w * 0.5, h * 0.84
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(w * 0.3)}" ry="{f(h * 0.1)}" fill="#1A0A04" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    o.append(f'<path d="M{f(cx - w * 0.22)} {f(cy - 6)} C {f(cx - w * 0.1)} {f(cy - h * 0.12)} {f(cx + w * 0.02)} {f(cy - h * 0.04)} {f(cx + w * 0.06)} {f(cy - 2)} Z" fill="#6A2A7A" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(cx - w * 0.2)} {f(cy - 10)} L {f(cx + w * 0.04)} {f(cy - 6)}" stroke="#E8B830" stroke-width="3" stroke-dasharray="6 4"></path>')
    o.append(f'<path d="M{f(cx + w * 0.08)} {f(cy)} L {f(cx + w * 0.2)} {f(cy - 6)} L {f(cx + w * 0.22)} {f(cy + 4)} L {f(cx + w * 0.1)} {f(cy + 10)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>')
    for i in range(9):
        o.append(f'<ellipse cx="{f(cx - w * 0.06 + (i % 5) * 12)}" cy="{f(cy + 18 + (i // 5) * 8)}" rx="7" ry="3.5" fill="#D8D8E0" stroke="#0D0D0F" stroke-width="1.2"></ellipse>')
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(w * 0.24)}" fill="#FFE680" opacity="0.12"></circle>')
    return "".join(o)

def ai(p, w, h, seed, rout=False):
    """Ai beside Beth-aven on its hill; rout=True: the three thousand flee down the descent, the men of Ai at the gate."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.86, h * 0.14, 14, op=0.3),
         J.city_hill(w * 0.7, h * 0.66, w * 0.34, h * 0.42, seed), ground(w, h, h * 0.66, "#B89A6A", dy=0)]
    if rout:
        for i in range(10):
            x = w * (0.08 + i * 0.05 + r.uniform(-0.01, 0.01)); y = h * (0.7 + (i % 3) * 0.08)
            o.append(man(p, x, y, fit(y, y - h * 0.18), r.choice(WAR), flip=True, up=[(-22, -158), (-46, -140), (-60, -160)]))
        for i in range(5):
            x = w * (0.62 + i * 0.05); y = h * 0.66
            o.append(mk.person(p, round(x), round(y), round(fit(y, y - h * 0.14), 3), body="#12090A", cloth="#3A2A2A", kind="Tunic", sw=2, flip=True, extra=E4.SPEAR))
    else:
        for i in range(3):
            x = w * (0.12 + i * 0.07); o.append(man(p, x, b, fit(b, h * 0.5), SPY_C[i % 2]))
    return "".join(o)

ELDER_C = ("#5A4A3A", "#4A3A3A", "#6A5A4A", "#3A3430")
def fallen(p, w, h, seed):
    """Joshua and the elders fallen on their faces before the ark until the evening, dust upon their heads."""
    b = h * 0.86
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A1A2E"></rect>', sun(w * 0.86, h * 0.5, 30, color="#FF6A2A", op=0.4),
         ground(w, h, h * 0.6, "#4A2A2E", dy=0), J.ark(w * 0.8, h * 0.62, min(1.2, h / 300), f"fa{seed}", glow=True, pole=110)]
    s = min(1.1, h / 320)
    o.append(N.prostrate(w * 0.42, b, s, color=JOSHUA_C, skin="#8A5A3A"))
    for i in range(4):
        o.append(N.prostrate(w * (0.06 + i * 0.09), b - h * 0.04 - (i % 2) * h * 0.04, s * 0.8, color=ELDER_C[i], skin="#7A4A3A"))
    return "".join(o)

def lot(w, h, steps=(("TRIBE", "JUDAH"), ("FAMILY", "THE ZERAHITES"), ("HOUSEHOLD", "ZABDI"), ("MAN", "ACHAN"))):
    """The lot taken step by step, as a technical readout: tribe, family, household, man."""
    o = [grid_bg(w, h)]
    n = len(steps); y = h * 0.62
    pts = [(w * (0.12 + 0.76 * i / (n - 1)), y) for i in range(n)]
    o.append(route(pts, color="#FFD23F"))
    for i, ((k, name), (x, yy)) in enumerate(zip(steps, pts)):
        last = i == n - 1
        o.append(node(x, yy, name, "#D7261E" if last else "#FFD23F", r=8 if last else 6, dy=-20, size=11 if last else 10) + label(x, yy + 30, k, "#8FD0E2", 8))
    return "".join(o)

def achor(w, h, seed):
    """The valley of Achor at evening and the great heap of stones raised in it, unto this day."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A2A3A"></rect>', sun(w * 0.8, h * 0.36, 24, color="#FF8A3D", op=0.35),
         hills(w, h, h * 0.44, seed, color="#3A2030", amp=24, step=90)]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.7)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} Z" fill="#2A1A24" stroke="#0D0D0F" stroke-width="2.4"></path>')
    cx, base = w * 0.5, h * 0.9
    for row in range(5):
        for i in range(8 - row):
            x = cx + (i - (7 - row) / 2) * w * 0.045; y = base - row * h * 0.05
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.026)}" ry="{f(h * 0.028)}" fill="{r.choice(["#8A7A6A", "#6A5A4A", "#A89A86"])}" stroke="#0D0D0F" stroke-width="1.8"></ellipse>')
    return "".join(o)

# ---- Joshua 8–9 ---------------------------------------------------------------------------------------------------------
def ai_plan(w, h, stage=0):
    """The taking of Ai as a technical map: Ai and Beth-el, the ambush on the west, the host on the north beyond the
    valley, the way of the wilderness. stage=1 adds the feigned flight and the ambush entering the city."""
    o = [grid_bg(w, h)]
    ax, ay = w * 0.6, h * 0.5
    o.append(f'<rect x="{f(ax - 34)}" y="{f(ay - 22)}" width="68" height="44" fill="#B5652E" opacity="0.7" stroke="#FFD23F" stroke-width="2"></rect>' + label(ax, ay + 5, "AI", "#F3EFE6", 12))
    o.append(node(w * 0.16, h * 0.42, "BETH-EL", "#8FD0E2", r=5, dy=-12, size=9))
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.2)} C {f(w * 0.45)} {f(h * 0.3)} {f(w * 0.7)} {f(h * 0.28)} {f(w * 0.92)} {f(h * 0.22)}" fill="none" stroke="#3A5A7A" stroke-width="10" opacity="0.6"></path>'
             + label(w * 0.62, h * 0.24, "THE VALLEY", "#8FD0E2", 8))
    o.append(f'<rect x="{f(w * 0.5)}" y="{f(h * 0.04)}" width="{f(w * 0.24)}" height="{f(h * 0.12)}" fill="#2E9A4A" opacity="0.4" stroke="#5AD87A" stroke-width="2"></rect>'
             + label(w * 0.62, h * 0.11, "THE HOST · NORTH", "#5AD87A", 9))
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(h * 0.44)}" width="{f(w * 0.14)}" height="{f(h * 0.14)}" fill="#D7261E" opacity="0.35" stroke="#D7261E" stroke-width="2" stroke-dasharray="5 4"></rect>'
             + label(w * 0.37, h * 0.63, "AMBUSH · WEST", "#FF6A5A", 9))
    o.append(label(w * 0.86, h * 0.9, "THE WILDERNESS", "#C8A06A", 9))
    if stage:
        o.append(route([(w * 0.62, h * 0.18), (w * 0.72, h * 0.6), (w * 0.84, h * 0.84)], color="#5AD87A"))
        o.append(route([(ax + 30, ay + 10), (w * 0.76, h * 0.7)], color="#FFB04A", arrow=True))
        o.append(route([(w * 0.44, h * 0.5), (ax - 36, ay)], color="#FF6A5A"))
    return "".join(o)

def javelin(p, w, h, seed):
    """Joshua stretches out the javelin that is in his hand toward Ai, far off on its hill."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3B86A"></rect>', sun(w * 0.86, h * 0.2, 18, color="#FF8A3D", op=0.4),
         J.city_hill(w * 0.82, h * 0.6, w * 0.22, h * 0.3, seed), ground(w, h, h * 0.6, "#B89A6A", dy=0)]
    s = fit(b, h * 0.3)
    spear = '<path d="M30 -150 L 150 -196" stroke="#3E2416" stroke-width="5"></path><path d="M150 -196 L 174 -205 L 156 -186 Z" fill="#C8C2D6" stroke="#0D0D0F" stroke-width="2"></path>'
    o.append(mk.person(p, round(w * 0.24), round(b), round(s, 3), body=SKIN, cloth=JOSHUA_C, sw=3, up=[(-22, -158), (4, -150), (30, -150)],
                       extra=A.headcloth(JOSHUA_C) + A.BLACK_BEARD + spear))
    return "".join(o)

def ruin_heap(w, h, seed):
    """Ai a heap for ever, at the going down of the sun, and a great heap of stones at the entrance of the gate."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A2A3A"></rect>', sun(w * 0.2, h * 0.5, 30, color="#FF6A2A", op=0.45),
         J.collapse(w * 0.3, w + 10, h * 0.7, h * 0.3, seed, color="#5A3A2A"), ground(w, h, h * 0.7, "#2A1A1A", dy=0)]
    cx, base = w * 0.2, h * 0.92
    for row in range(4):
        for i in range(6 - row):
            x = cx + (i - (5 - row) / 2) * w * 0.04; y = base - row * h * 0.045
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.022)}" ry="{f(h * 0.025)}" fill="{r.choice(["#8A7A6A", "#6A5A4A", "#A89A86"])}" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    return "".join(o)

def gibeonites(p, w, h, seed):
    """The men of Gibeon as from a far country: old sacks upon their asses, rent wine-skins bound up, patched garments."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8C88A"></rect>', sun(w * 0.84, h * 0.16, 16, op=0.3),
         hills(w, h, h * 0.5, seed, color="#C8A06A", amp=10), ground(w, h, h * 0.56, "#C8A06A", dy=0)]
    s = fit(b, h * 0.42)
    patch = '<rect x="-12" y="-120" width="12" height="14" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="1.2"></rect><rect x="4" y="-80" width="10" height="12" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="1.2"></rect>'
    for i, x in enumerate((0.18, 0.5)):
        sa = s * 0.5
        o.append(N.ass(w * (x + 0.14), b, sa, flip=True)
                 + f'<rect x="{f(w * (x + 0.14) - 30 * sa)}" y="{f(b - 120 * sa)}" width="{f(60 * sa)}" height="{f(34 * sa)}" rx="6" fill="#A8946A" stroke="#0D0D0F" stroke-width="2"></rect>')
        o.append(man(p, w * x, b, s, "#7A6A5A", flip=True, extra=patch))
        o.append(f'<ellipse cx="{f(w * x + 14 * s)}" cy="{f(b - 100 * s)}" rx="{f(14 * s)}" ry="{f(20 * s)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></ellipse>'
                 f'<path d="M{f(w * x + 4 * s)} {f(b - 104 * s)} L {f(w * x + 24 * s)} {f(b - 94 * s)}" stroke="#C8A06A" stroke-width="2"></path>')
    o.append(man(p, w * 0.86, b, s, "#6A5A4A", flip=True, extra=patch))
    return "".join(o)

def provision(w, h, seed):
    """Their provision: the bread dry and become mouldy, the wine-skins rent and bound up, the shoes old and patched."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A1E"></rect>', ground(w, h, h * 0.6, "#5A4A3A", dy=0)]
    for i in range(3):
        x = w * (0.16 + i * 0.12); y = h * 0.72
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.05)}" ry="{f(h * 0.06)}" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
                 + "".join(f'<circle cx="{f(x + r.uniform(-1, 1) * w * 0.035)}" cy="{f(y + r.uniform(-1, 1) * h * 0.04)}" r="{f(r.uniform(2, 5))}" fill="#6A8A5A"></circle>' for _ in range(7)))
    sx = w * 0.66
    o.append(f'<path d="M{f(sx - w * 0.1)} {f(h * 0.82)} C {f(sx - w * 0.12)} {f(h * 0.5)} {f(sx + w * 0.12)} {f(h * 0.5)} {f(sx + w * 0.1)} {f(h * 0.82)} Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(sx - w * 0.04)} {f(h * 0.6)} L {f(sx + w * 0.02)} {f(h * 0.7)} M{f(sx + w * 0.04)} {f(h * 0.58)} L {f(sx - w * 0.01)} {f(h * 0.66)}" stroke="#C8A06A" stroke-width="3"></path>')
    o.append(f'<path d="M{f(w * 0.82)} {f(h * 0.86)} L {f(w * 0.96)} {f(h * 0.86)} L {f(w * 0.96)} {f(h * 0.8)} L {f(w * 0.86)} {f(h * 0.78)} Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<rect x="{f(w * 0.88)}" y="{f(h * 0.8)}" width="{f(w * 0.03)}" height="{f(h * 0.03)}" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="1"></rect>')
    return "".join(o)

def four_cities(w, h):
    """The cities of the Gibeonites: Gibeon, Chephirah, Beeroth and Kiriath-jearim, three days from Gilgal."""
    o = [grid_bg(w, h)]
    pts = [("GILGAL", 0.86, 0.6, "#8FD0E2"), ("GIBEON", 0.42, 0.42, "#FFD23F"), ("CHEPHIRAH", 0.24, 0.5, "#FFD23F"), ("BEEROTH", 0.5, 0.3, "#FFD23F"), ("KIRIATH-JEARIM", 0.2, 0.68, "#FFD23F")]
    o.append(route([(w * 0.86, h * 0.6), (w * 0.62, h * 0.5), (w * 0.44, h * 0.44)], color="#8FD0E2"))
    for nm, x, y, c in pts: o.append(node(w * x, h * y, nm, c, r=5, dy=-12, size=9))
    o.append(label(w * 0.7, h * 0.46, "THREE DAYS", "#8FD0E2", 8))
    return "".join(o)

def hewers(p, w, h, seed):
    """Hewers of wood and drawers of water for the congregation and for the altar of Jehovah."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.84, h * 0.16, 16, op=0.3),
         ground(w, h, h * 0.62, "#B89A6A", dy=0)]
    ax = w * 0.84
    o.append(f'<rect x="{f(ax - w * 0.07)}" y="{f(h * 0.62)}" width="{f(w * 0.14)}" height="{f(h * 0.16)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></rect>' + E.blaze(ax, h * 0.62, w * 0.1, h * 0.18, seed, n=6))
    s = fit(b, h * 0.44)
    wood = '<path d="M-30 -186 L 22 -200 M-30 -180 L 24 -192 M-28 -174 L 26 -186" stroke="#6A4A2A" stroke-width="7" stroke-linecap="round"></path>'
    jar = '<path d="M-14 -190 C -22 -214 -4 -232 0 -232 C 4 -232 22 -214 14 -190 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>'
    for i in range(5):
        x = w * (0.08 + i * 0.13)
        o.append(man(p, x, b - (i % 2) * 6, s * (0.96 if i % 2 else 1), "#7A6A5A", up=[(-22, -158), (-28, -180), (-16, -196)], extra=wood if i % 2 == 0 else jar))
    return "".join(o)

def below(fn, k=0.42):
    """A drawing f(w, h) set in the lower part of a panel, so a column of words at the top leaves it clear."""
    return lambda w, h: f'<g transform="translate(0 {h * k:.1f})">' + fn(w, h * (1 - k)) + '</g>'

# ---- Joshua 10–11 -------------------------------------------------------------------------------------------------------
import exodus2 as E2, exodus3 as E3
CROWN = '<path d="M-14 -200 L -14 -214 L -7 -206 L 0 -218 L 7 -206 L 14 -214 L 14 -200 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>'
KING_C = ("#5A1A4A", "#1F4A7A", "#7A3A1A", "#3A5A2A", "#6A2A2A")

def five_kings(p, w, h, seed):
    """The five kings of the Amorites with their hosts, encamped against Gibeon on its hill."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8B880"></rect>', sun(w * 0.14, h * 0.16, 16, color="#FF8A3D", op=0.3),
         J.city_hill(w * 0.8, h * 0.6, w * 0.24, h * 0.34, seed), ground(w, h, h * 0.6, "#B89A6A", dy=0)]
    for i in range(18):
        x = w * (0.04 + (i % 9) * 0.07); y = h * (0.7 + (i // 9) * 0.06)
        o.append(mk.person(p, round(x), round(y), round(fit(y, y - h * 0.16), 3), body="#2A1A14", cloth=r.choice(("#3A2A2A", "#4A3A2A", "#2A2A3A")), kind="Tunic", sw=2, extra=E4.SPEAR))
    s = fit(b, h * 0.5)
    for i in range(5):
        o.append(mk.person(p, round(w * (0.1 + i * 0.12)), round(b), round(s, 3), body=SKIN, cloth=KING_C[i], sw=3, flip=False, extra=CROWN))
    return "".join(o)

def night_march(p, w, h, seed):
    """Joshua went up from Gilgal all the night: the men of war climbing in file under the stars."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), night(w, h, seed, "#0F0E2A")]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.9)} L {f(w * 0.7)} {f(h * 0.34)} L {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h + 10)} Z" fill="#1E1A3A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for i in range(12):
        t = i / 11; x = w * (0.04 + 0.66 * t); y = h * (0.9 - 0.56 * t)
        o.append(mk.person(p, round(x), round(y), round(fit(y, y - h * (0.2 - 0.12 * t)), 3), body="#0B0814", cloth="#2A2440", kind="Tunic", sw=2, extra=E4.SPEAR))
    return "".join(o)

def hailstones(w, h, seed):
    """Great stones from heaven upon them at the descent of Beth-horon, unto Azekah."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2E4A"></rect>', V.rays(w * 0.5, -h * 0.2, 30, 20, max(w, h) * 1.4, color="#E8F0F6", op=0.12)]
    o.append(f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.4)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.94)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#4A4A5A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(E2.hail(70, 0, w, 0, h * 0.9, seed))
    o.append(label(w * 0.1, h * 0.46, "BETH-HORON", "#E8F0F6", 9, "start") + label(w * 0.9, h * 0.88, "AZEKAH", "#E8F0F6", 9, "end"))
    return "".join(o)

def cave(w, h, seed, sealed=False, dusk=False):
    """The cave at Makkedah; sealed=True: great stones rolled unto its mouth (dusk: at the going down of the sun)."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{"#4A2A3A" if dusk else "#C8A06A"}"></rect>']
    if dusk: o.append(sun(w * 0.86, h * 0.4, 24, color="#FF6A2A", op=0.45))
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.16)} C {f(w * 0.3)} {f(h * 0.06)} {f(w * 0.6)} {f(h * 0.18)} {f(w * 0.74)} {f(h + 10)} Z" fill="{"#3A2430" if dusk else "#8A6A4A"}" stroke="#0D0D0F" stroke-width="2.4"></path>')
    cx, cy = w * 0.36, h * 0.74
    o.append(f'<path d="M{f(cx - w * 0.14)} {f(h * 0.92)} C {f(cx - w * 0.14)} {f(h * 0.5)} {f(cx + w * 0.14)} {f(h * 0.5)} {f(cx + w * 0.14)} {f(h * 0.92)} Z" fill="#0B0608" stroke="#0D0D0F" stroke-width="2.4"></path>')
    if sealed:
        for row in range(3):
            for i in range(4 - row):
                x = cx + (i - (3 - row) / 2) * w * 0.07; y = h * (0.86 - row * 0.1)
                o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.04)}" ry="{f(h * 0.06)}" fill="{r.choice(["#8A7A6A", "#6A5A4A", "#A89A86"])}" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    o.append(ground(w, h, h * 0.92, "#5A4A3A" if not dusk else "#2A1A24", dy=0))
    return "".join(o)

CAMPAIGN = [("GILGAL", 0.86, 0.36), ("GIBEON", 0.6, 0.3), ("BETH-HORON", 0.46, 0.26), ("AZEKAH", 0.34, 0.46), ("MAKKEDAH", 0.3, 0.54), ("LIBNAH", 0.24, 0.6),
            ("LACHISH", 0.2, 0.7), ("EGLON", 0.12, 0.78), ("HEBRON", 0.5, 0.72), ("DEBIR", 0.4, 0.86)]
def campaign(w, h, upto=None, hi=()):
    """The southern campaign as a technical map: from Gilgal to Gibeon, down by Beth-horon to Makkedah, then city by city.
    upto: draw the route through that city; hi: cities to mark red."""
    o = [grid_bg(w, h)]
    o.append(node(w * 0.26, h * 0.32, "GEZER", "#8FD0E2", r=4, dy=-10, size=8))
    names = [c[0] for c in CAMPAIGN]
    n = names.index(upto) + 1 if upto else len(CAMPAIGN)
    o.append(route([(w * x, h * y) for _, x, y in CAMPAIGN[:n]], color="#FFD23F"))
    for nm, x, y in CAMPAIGN:
        o.append(node(w * x, h * y, nm, "#D7261E" if nm in hi else "#FFD23F", r=6 if nm in hi else 4, dy=-10, size=9 if nm in hi else 8))
    o.append(label(w * 0.92, h * 0.94, "THE SOUTH", "#C8A06A", 9, "end"))
    return "".join(o)

def chariots(p, w, h, seed, burning=False):
    """The hosts of the kings of the north at the waters of Merom, with horses and chariots very many; burning=True: the
    chariots burnt with fire."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{"#2A0A0A" if burning else "#8FD0E2"}"></rect>',
         hills(w, h, h * 0.36, seed, color="#5A6A4A" if not burning else "#2A1A1A", amp=16),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.44)}" rx="{f(w * 0.3)}" ry="{f(h * 0.05)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></ellipse>',
         ground(w, h, h * 0.52, "#B89A6A" if not burning else "#3A2A1A", dy=0)]
    for k in range(3):
        y = h * (0.66 + k * 0.12); s = 0.22 + k * 0.08
        for i in range(5):
            x = w * (0.08 + i * 0.2 + (k % 2) * 0.1)
            o.append(E3.chariot(x, y, s, flip=False, color="#3A2214"))
            if burning: o.append(E.blaze(x, y, w * 0.08, h * 0.16, seed + k * 10 + i, n=5))
    return "".join(o)

LAND = [("THE HILL-COUNTRY", 0.36, 0.3, 0.6, 0.62, "#9A6A3A"), ("THE LOWLAND", 0.16, 0.36, 0.34, 0.74, "#C8A030"), ("THE SOUTH", 0.2, 0.76, 0.64, 0.94, "#C8682E"),
        ("GOSHEN", 0.42, 0.66, 0.6, 0.76, "#9CCB5E"), ("THE ARABAH", 0.62, 0.3, 0.74, 0.8, "#2C9DB8"), ("LEBANON", 0.36, 0.04, 0.7, 0.18, "#2E6B3A")]
def land_taken(w, h):
    """So Joshua took all that land: the regions named in Joshua 11:16–17, from mount Halak unto Baal-gad under Hermon."""
    o = [grid_bg(w, h)]
    for nm, x0, y0, x1, y1, c in LAND:
        o.append(f'<rect x="{f(w * x0)}" y="{f(h * y0)}" width="{f(w * (x1 - x0))}" height="{f(h * (y1 - y0))}" fill="{c}" opacity="0.45" stroke="{c}" stroke-width="2"></rect>'
                 + label(w * x0 + 6, h * y0 + 14, nm, "#F3EFE6", 8, "start", ls=0.08))
    o.append(node(w * 0.74, h * 0.04, "MOUNT HERMON", "#FFD23F", r=4, dy=16, size=8) + node(w * 0.6, h * 0.2, "BAAL-GAD", "#FFD23F", r=4, dy=-8, size=8)
             + node(w * 0.7, h * 0.94, "MOUNT HALAK", "#FFD23F", r=4, dy=-8, size=8))
    return "".join(o)

# ---- Joshua 12–14 -------------------------------------------------------------------------------------------------------
def _sea(cx, cy, rx, ry, name=None, side="end"):
    o = f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>'
    return o + (label(cx - rx - 6 if side == "end" else cx + rx + 6, cy + 3, name, "#8FD0E2", 8, side) if name else "")

def _jordan(w, h, x=0.5):
    return (_sea(w * x, h * 0.18, w * 0.02, h * 0.05, "CHINNEROTH") + _sea(w * x, h * 0.74, w * 0.03, h * 0.11, "THE SALT SEA")
            + f'<path d="M{f(w * x)} {f(h * 0.23)} C {f(w * (x - 0.02))} {f(h * 0.4)} {f(w * (x + 0.02))} {f(h * 0.5)} {f(w * x)} {f(h * 0.63)}" fill="none" stroke="#8FD0E2" stroke-width="3"></path>')

def east_map(w, h):
    """Beyond the Jordan toward the sunrising: Sihon's kingdom from the Arnon to the Jabbok, Og's Bashan unto Hermon."""
    o = [grid_bg(w, h), _jordan(w, h, 0.36)]
    regions = [("SIHON · HESHBON", 0.42, 0.44, 0.78, 0.7, "#6A4A3A"), ("GILEAD", 0.42, 0.28, 0.82, 0.44, "#E87A2A"), ("OG · BASHAN", 0.42, 0.06, 0.86, 0.28, "#6A6A8A")]
    for nm, x0, y0, x1, y1, c in regions:
        o.append(f'<rect x="{f(w * x0)}" y="{f(h * y0)}" width="{f(w * (x1 - x0))}" height="{f(h * (y1 - y0))}" fill="{c}" opacity="0.45" stroke="{c}" stroke-width="2"></rect>'
                 + label(w * x0 + 6, h * y0 + 14, nm, "#F3EFE6", 9, "start", ls=0.08))
    o.append(f'<path d="M{f(w * 0.38)} {f(h * 0.72)} L {f(w * 0.8)} {f(h * 0.72)}" stroke="#8FD0E2" stroke-width="2.4"></path>' + label(w * 0.8, h * 0.76, "ARNON", "#8FD0E2", 8, "end"))
    o.append(f'<path d="M{f(w * 0.37)} {f(h * 0.44)} L {f(w * 0.74)} {f(h * 0.46)}" stroke="#8FD0E2" stroke-width="2.4"></path>' + label(w * 0.74, h * 0.5, "JABBOK", "#8FD0E2", 8, "end"))
    o.append(node(w * 0.8, h * 0.05, "MOUNT HERMON", "#FFD23F", r=4, dy=18, size=8))
    o.append(label(w * 0.12, h * 0.5, "CANAAN", "#8A9AB0", 10))
    return "".join(o)

def remaineth_map(w, h):
    """The land that yet remaineth: the five lords of the Philistines by the sea, the Sidonians, Lebanon unto Hamath."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.14)} -10 C {f(w * 0.12)} {f(h * 0.3)} {f(w * 0.08)} {f(h * 0.7)} {f(w * 0.04)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    phil = [("GAZA", 0.12, 0.9), ("ASHKELON", 0.15, 0.78), ("ASHDOD", 0.18, 0.68), ("GATH", 0.3, 0.74), ("EKRON", 0.28, 0.6)]
    o.append(f'<rect x="{f(w * 0.08)}" y="{f(h * 0.54)}" width="{f(w * 0.3)}" height="{f(h * 0.42)}" fill="#D7261E" opacity="0.25" stroke="#D7261E" stroke-width="2" stroke-dasharray="6 4"></rect>'
             + label(w * 0.24, h * 0.53, "THE FIVE LORDS OF THE PHILISTINES", "#FF6A5A", 8))
    for nm, x, y in phil: o.append(node(w * x, h * y, nm, "#FFD23F", r=4, dy=-8, size=8))
    o.append(f'<rect x="{f(w * 0.2)}" y="{f(h * 0.04)}" width="{f(w * 0.6)}" height="{f(h * 0.2)}" fill="#2E6B3A" opacity="0.4" stroke="#5AD87A" stroke-width="2" stroke-dasharray="6 4"></rect>'
             + label(w * 0.5, h * 0.15, "LEBANON · THE SIDONIANS · UNTO HAMATH", "#5AD87A", 8))
    o.append(node(w * 0.6, h * 0.5, "ISRAEL'S CAMPS", "#8FD0E2", r=5, dy=-10, size=8))
    return "".join(o)

CALEB_C = "#2E6B3A"
def hebron(p, w, h, seed):
    """Caleb, fourscore and five years old and as strong as in the day Moses sent him, before Hebron on its hill."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.2, h * 0.16, 16, color="#FF8A3D", op=0.3),
         J.city_hill(w * 0.66, h * 0.66, w * 0.32, h * 0.44, seed), ground(w, h, h * 0.66, "#B89A6A", dy=0)]
    s = fit(b, h * 0.32)
    o.append(mk.person(p, round(w * 0.22), round(b), round(s, 3), body=SKIN, cloth=CALEB_C, sw=3, up=[(-22, -158), (-6, -196), (8, -228)],
                       extra=A.headcloth(CALEB_C) + A.WHITE_BEARD))
    return "".join(o)

# ---- Joshua 15–17 -------------------------------------------------------------------------------------------------------
def springs(p, w, h, seed):
    """Achsah alighted from off her ass in the land of the South; the upper springs and the nether springs."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.86, h * 0.14, 16, color="#FF8A3D", op=0.3),
         hills(w, h, h * 0.42, seed, color="#C8A06A", amp=16), ground(w, h, h * 0.5, "#D8B878", dy=0)]
    for x, y in ((0.7, 0.56), (0.84, 0.74)):
        o.append(f'<ellipse cx="{f(w * x)}" cy="{f(h * y)}" rx="{f(w * 0.08)}" ry="{f(h * 0.035)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></ellipse>'
                 f'<path d="M{f(w * x - 10)} {f(h * y - 6)} C {f(w * x - 4)} {f(h * y - 30)} {f(w * x + 4)} {f(h * y - 30)} {f(w * x + 10)} {f(h * y - 6)}" fill="none" stroke="#E8F6FA" stroke-width="3"></path>'
                 + "".join(f'<circle cx="{f(w * x + dx)}" cy="{f(h * y - 4)}" r="6" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.2"></circle>' for dx in (-w * 0.09, w * 0.09)))
    s = fit(b, h * 0.42)
    o.append(N.ass(w * 0.44, b, s * 0.55, flip=True))
    o.append(woman(p, w * 0.3, b, s, "#C8A030", flip=False))
    o.append(mk.person(p, round(w * 0.14), round(b), round(s, 3), body=SKIN, cloth=CALEB_C, sw=3, extra=A.headcloth(CALEB_C) + A.WHITE_BEARD))
    return "".join(o)

def daughters(p, w, h, seed):
    """Mahlah, Noah, Hoglah, Milcah and Tirzah before Eleazar the priest, Joshua and the princes."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8C8A0"></rect>', sun(w * 0.5, h * 0.16, 18, op=0.3),
         ground(w, h, h * 0.6, "#B89A6A", dy=0)]
    s = fit(b, h * 0.4)
    for i, c in enumerate(("#8A3A5A", "#5A6E8A", "#C8A030", "#6A3A7A", "#3A7A6A")):
        o.append(woman(p, w * (0.08 + i * 0.09), b - (i % 2) * 4, s * (0.94 + 0.02 * (i % 2)), c))
    from exo.art9 import high_priest
    o.append(high_priest(p, w * 0.72, b, s, flip=True) + joshua_fig(p, w * 0.86, b, s, flip=True))
    for i in range(2): o.append(man(p, w * (0.6 - i * 0.06), b - 6, s * 0.92, ("#5A4A3A", "#6A5A4A")[i], flip=True))
    return "".join(o)

def forest(p, w, h, seed):
    """The forest of the hill-country to be cut down, and in the valley the Canaanites' chariots of iron."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8FD0E2"></rect>', hills(w, h, h * 0.3, seed, color="#3F6A3A", amp=20)]
    for i in range(16):
        x = w * (0.02 + i * 0.065); y = h * (0.46 + (i % 3) * 0.04)
        o.append(f'<path d="M{f(x)} {f(y - h * 0.2)} L {f(x - w * 0.035)} {f(y)} L {f(x + w * 0.035)} {f(y)} Z" fill="{r.choice(["#2E6B3A", "#1F4A34", "#3F7A3A"])}" stroke="#0D0D0F" stroke-width="1.8"></path>'
                 f'<rect x="{f(x - 3)}" y="{f(y)}" width="6" height="{f(h * 0.04)}" fill="#5A3A22"></rect>')
    o.append(ground(w, h, h * 0.66, "#9CCB5E", dy=0))
    for i in range(4):
        o.append(E3.chariot(w * (0.16 + i * 0.22), h * 0.9, 0.36, flip=i % 2 == 1, color="#4A4A5A", driver="#3A3A4A"))
    return "".join(o)

# ---- Joshua 18–19 -------------------------------------------------------------------------------------------------------
import samuel1 as S1, samuel3 as S3
def shiloh(p, w, h, seed, lots=False, people=True):
    """Shiloh: the tent of meeting set up in its linen court on the hill; lots=True: Joshua casting lots before it, the
    three men of each tribe with the book of the land described by cities into seven portions."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8D8B0"></rect>', sun(w * 0.86, h * 0.14, 16, op=0.3),
         hills(w, h, h * 0.42, seed, color="#9AAA6A", amp=14), S1.shiloh(w * 0.62, h * 0.6, w * 0.5, h * 0.36), ground(w, h, h * 0.6, "#B8A878", dy=0)]
    s = fit(b, h * 0.42)
    if lots:
        o.append(joshua_fig(p, w * 0.5, b, s, up=[(-22, -158), (4, -150), (30, -150)]))
        o.append(f'<circle cx="{f(w * 0.5 + 34 * s)}" cy="{f(b - 150 * s)}" r="{f(7 * s)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></circle>')
        for i in range(6):
            x = w * (0.06 + i * 0.06)
            o.append(man(p, x, b - (i % 2) * 4, s * 0.92, r.choice(list(TRIBE_C.values()))))
        o.append(S3.letter(w * 0.24, b - 110 * s, 0.7 * s * 2))
    elif people:
        o.append(crowd_at(p, w, h, seed, 0, w * 0.36, h * 0.68, b, 14, fit(h * 0.68, h * 0.5) * 0.8, s))
    return "".join(o)

def surveyors(p, w, h, seed):
    """Three men of each tribe walk through the land and describe it by cities into seven portions in a book."""
    o = [grid_bg(w, h)]
    regions = [(0.1, 0.1, 0.4, 0.32), (0.42, 0.1, 0.9, 0.3), (0.1, 0.34, 0.5, 0.56), (0.52, 0.32, 0.9, 0.56), (0.1, 0.58, 0.46, 0.8), (0.48, 0.58, 0.9, 0.8), (0.2, 0.82, 0.8, 0.94)]
    for i, (x0, y0, x1, y1) in enumerate(regions):
        o.append(f'<rect x="{f(w * x0)}" y="{f(h * y0)}" width="{f(w * (x1 - x0))}" height="{f(h * (y1 - y0))}" fill="none" stroke="#FFD23F" stroke-width="1.6" stroke-dasharray="6 4"></rect>'
                 + label(w * x0 + 8, h * y0 + 16, f"PORTION {i + 1}", "#FFD23F", 8, "start"))
    return "".join(o)

def timnath(p, w, h, seed, figure=True):
    """Timnath-serah in the hill-country of Ephraim: Joshua built the city, and dwelt therein."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.2, h * 0.2, 18, color="#FF8A3D", op=0.35),
         hills(w, h, h * 0.4, seed, color="#7A9A5A", amp=18), J.city_hill(w * 0.62, h * 0.7, w * 0.3, h * 0.34, seed), ground(w, h, h * 0.7, "#B89A6A", dy=0)]
    if figure: o.append(joshua_fig(p, w * 0.2, b, fit(b, h * 0.4)))
    return "".join(o)

# ---- Joshua 20–22 -------------------------------------------------------------------------------------------------------
def refuge_gate(p, w, h, seed):
    """The manslayer stands at the entrance of the gate of the city of refuge and declares his cause to the elders; the
    avenger of blood far off on the road."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8C88A"></rect>', sun(w * 0.14, h * 0.16, 14, op=0.3)]
    o.append(J.jericho(w * 0.42, w + 10, h * 0.24, b, seed, towers=2, houses=True, color="#B5824A"))
    o.append(f'<path d="M{f(w * 0.56)} {f(b)} L {f(w * 0.56)} {f(h * 0.56)} C {f(w * 0.56)} {f(h * 0.46)} {f(w * 0.74)} {f(h * 0.46)} {f(w * 0.74)} {f(h * 0.56)} L {f(w * 0.74)} {f(b)} Z" fill="#2A140C" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(ground(w, h, b, "#B89A6A", dy=0))
    s = fit(b, h * 0.42)
    o.append(man(p, w * 0.46, b, s, "#6A5A7A", up=[(-22, -158), (4, -150), (30, -150)]))
    for i in range(3): o.append(mk.person(p, round(w * (0.62 + i * 0.06)), round(b), round(s * 0.96, 3), body=SKIN, cloth=("#5A4A3A", "#6A5A4A", "#4A3A3A")[i], sw=3, flip=True, extra=A.WHITE_BEARD))
    o.append(man(p, w * 0.08, b - h * 0.3, s * 0.4, "#3A1A1A"))
    return "".join(o)

def refuge_map(w, h):
    """The six cities of refuge: Kedesh, Shechem and Hebron on this side of the Jordan; Bezer, Ramoth and Golan beyond."""
    o = [grid_bg(w, h), _jordan(w, h, 0.5)]
    for nm, x, y in (("KEDESH", 0.38, 0.12), ("SHECHEM", 0.34, 0.42), ("HEBRON", 0.32, 0.8), ("GOLAN", 0.68, 0.16), ("RAMOTH", 0.7, 0.42), ("BEZER", 0.66, 0.74)):
        o.append(f'<rect x="{f(w * x - 9)}" y="{f(h * y - 9)}" width="18" height="18" fill="#D7261E" stroke="#FFD23F" stroke-width="2"></rect>' + label(w * x, h * y - 16, nm, "#FFD23F", 9))
    o.append(label(w * 0.24, h * 0.96, "THIS SIDE JORDAN", "#8FD0E2", 8) + label(w * 0.78, h * 0.96, "BEYOND THE JORDAN", "#8FD0E2", 8))
    return "".join(o)

def altar_ed(p, w, h, seed, people=True):
    """The great altar to see to, built by the Jordan on the side that pertaineth to the children of Israel."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3B86A"></rect>', sun(w * 0.84, h * 0.18, 20, color="#FF8A3D", op=0.35),
         hills(w, h, h * 0.4, seed, color="#9A8A6A", amp=14),
         f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.48)} {f(w * 0.6)} {f(h * 0.54)} {f(w + 10)} {f(h * 0.5)}" fill="none" stroke="#2C9DB8" stroke-width="8"></path>',
         ground(w, h, h * 0.54, "#B89A6A", dy=0)]
    ax, aw, ah = w * 0.56, w * 0.3, h * 0.34
    r = random.Random(seed)
    for row in range(6):
        for i in range(7 - row // 2):
            x = ax - aw / 2 + (i + (row % 2) * 0.5) * aw / 7; y = b - (row + 1) * ah / 6
            if x > ax + aw / 2 - aw / 14: continue
            o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(aw / 7 - 2)}" height="{f(ah / 6 - 2)}" rx="4" fill="{r.choice(["#8A7A6A", "#A89A86", "#7A6A5A"])}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    if people:
        o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.3, h * 0.66, b, 10, fit(h * 0.66, h * 0.5) * 0.8, fit(b, h * 0.56)))
    return "".join(o)

# ---- Joshua 23–24 -------------------------------------------------------------------------------------------------------
JOSHUA_OLD_C = "#B5421E"
def joshua_old_fig(p, x, y, s, flip=False, up=None):
    """Joshua at a hundred and ten: white hair and beard under the rust-red headcloth."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=JOSHUA_OLD_C, sw=3, flip=flip, up=up, extra=A.headcloth(JOSHUA_OLD_C) + A.WHITE_BEARD)

def shechem(p, w, h, seed, stone=True, people=True, joshua=True):
    """Shechem: the oak by the sanctuary of Jehovah, the great stone set up under it, all the tribes gathered."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.86, h * 0.16, 18, color="#FF8A3D", op=0.3),
         hills(w, h, h * 0.4, seed, color="#7A9A5A", amp=18), ground(w, h, h * 0.56, "#B89A6A", dy=0)]
    o.append(J.oak(w * 0.2, h * 0.7, min(1.4, h / 300), seed))
    if stone:
        o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.72)} L {f(w * 0.31)} {f(h * 0.44)} C {f(w * 0.33)} {f(h * 0.38)} {f(w * 0.39)} {f(h * 0.38)} {f(w * 0.41)} {f(h * 0.44)} L {f(w * 0.42)} {f(h * 0.72)} Z" '
                 f'fill="#A89A86" stroke="#0D0D0F" stroke-width="2.4"></path><path d="M{f(w * 0.33)} {f(h * 0.5)} L {f(w * 0.36)} {f(h * 0.56)}" stroke="#7A6A5A" stroke-width="2"></path>')
    s = fit(b, h * 0.42)
    if joshua: o.append(joshua_old_fig(p, w * 0.5, b, s, up=[(-22, -158), (-6, -196), (8, -228)]))
    if people: o.append(crowd_at(p, w, h, seed, w * 0.58, w + 10, h * 0.62, b, 24, fit(h * 0.62, h * 0.48) * 0.8, s * 0.94, flip=True))
    return "".join(o)

def hornet(w, h, seed):
    """The hornet sent before you (Joshua 24:12): a swarm over the hills, as a technical figure."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8B880"></rect>', hills(w, h, h * 0.6, seed, color="#9A6A3A", amp=16)]
    for _ in range(60):
        x, y = r.uniform(0, w), r.uniform(h * 0.1, h * 0.7); s = r.uniform(0.6, 1.4)
        o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><ellipse cx="0" cy="0" rx="7" ry="3.4" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></ellipse>'
                 '<path d="M-2 -3 L -2 3 M2 -3 L 2 3" stroke="#0D0D0F" stroke-width="1.4"></path><ellipse cx="-1" cy="-5" rx="4" ry="2" fill="#F3EFE6" opacity="0.8"></ellipse></g>')
    return "".join(o)

def vineyards(w, h, seed):
    """A land whereon thou hadst not labored: cities which ye built not, vineyards and oliveyards which ye planted not."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8FD0E2"></rect>', sun(w * 0.84, h * 0.16, 18, op=0.3),
         J.city_hill(w * 0.5, h * 0.5, w * 0.24, h * 0.24, seed), ground(w, h, h * 0.5, "#9CCB5E", dy=0)]
    r = random.Random(seed)
    for k in range(3):
        for i in range(9):
            x = w * (0.05 + i * 0.11 + (k % 2) * 0.05); y = h * (0.62 + k * 0.12)
            if k == 1: o.append(f'<circle cx="{f(x)}" cy="{f(y - 16)}" r="14" fill="#6A8A4A" stroke="#0D0D0F" stroke-width="1.6"></circle><rect x="{f(x - 2)}" y="{f(y - 4)}" width="4" height="12" fill="#5A3A22"></rect>')
            else: o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 20)}" stroke="#5A3A22" stroke-width="3"></path><circle cx="{f(x - 6)}" cy="{f(y - 22)}" r="7" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.2"></circle><circle cx="{f(x + 5)}" cy="{f(y - 16)}" r="4" fill="#6A2A7A"></circle>')
    return "".join(o)

def three_graves(w, h, seed):
    """Timnath-serah, Shechem and the hill of Phinehas at evening: three hills in the hill-country of Ephraim (no grave drawn)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A4A"></rect>', sun(w * 0.5, h * 0.62, 34, color="#FF8A3D", op=0.4),
         hills(w, h, h * 0.56, seed, color="#4A3050", amp=36, step=110), hills(w, h, h * 0.7, seed + 1, color="#2A1E30", amp=22)]
    for nm, x in (("TIMNATH-SERAH", 0.18), ("SHECHEM", 0.5), ("THE HILL OF PHINEHAS", 0.82)):
        o.append(label(w * x, h * 0.72, nm, "#F3D8A0", 9))
    return "".join(o)
