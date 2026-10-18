"""Drawings for the 1 Samuel volume (chapter by chapter, added below). The Joshua and Judges drawings are reused where they
fit (jos.art, jdg.art); the digest's panels come in through sa1.common.D."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, numbers1 as N, joshua1 as J, samuel1 as S1, samuel2 as S2, samuel3 as S3
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg, node, route
from exo import art as A
from num.art import ALL, TRIBE_C
from jos.art import crowd_at, below, night, WAR

def f(v): return f"{v:.1f}"

# ---- 1 Samuel 1–2 -------------------------------------------------------------------------------------------------------
def flesh_hook(w, h, seed):
    """The priest's servant with a flesh-hook of three teeth struck into the caldron while the flesh was boiling."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2218"></rect>', ground(w, h, h * 0.8, "#2A1810", dy=0),
         E.blaze(w * 0.5, h * 0.92, w * 0.3, h * 0.2, seed, n=7)]
    cx, cy = w * 0.5, h * 0.66
    o.append(f'<path d="M{f(cx - w * 0.18)} {f(cy)} C {f(cx - w * 0.18)} {f(cy + h * 0.2)} {f(cx + w * 0.18)} {f(cy + h * 0.2)} {f(cx + w * 0.18)} {f(cy)} Z" fill="#5A5A6A" stroke="#0D0D0F" stroke-width="2.6"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(w * 0.18)}" ry="{f(h * 0.04)}" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    for k in range(4):
        o.append(f'<path d="M{f(cx - 40 + k * 26)} {f(cy - 10)} C {f(cx - 46 + k * 26)} {f(cy - 40)} {f(cx - 30 + k * 26)} {f(cy - 60)} {f(cx - 36 + k * 26)} {f(cy - 90)}" fill="none" stroke="#E8E2D6" stroke-width="3" opacity="0.5"></path>')
    hx = cx + w * 0.06
    o.append(f'<path d="M{f(hx + w * 0.3)} {f(h * 0.2)} L {f(hx)} {f(cy - 6)}" stroke="#6A4A2A" stroke-width="7" stroke-linecap="round"></path>'
             + "".join(f'<path d="M{f(hx - 12 + i * 12)} {f(cy - 14)} L {f(hx - 14 + i * 12)} {f(cy + 14)}" stroke="#C8C8D0" stroke-width="4"></path>' for i in range(3)))
    return "".join(o)

def little_robe(w, h, seed):
    """The little robe his mother made him and brought from year to year."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8D8B0"></rect>', V.rays(w * 0.5, h * 0.5, 30, 20, max(w, h), color="#FFF4C2", op=0.3)]
    cx, cy, s = w * 0.5, h * 0.52, min(w, h) / 300
    o.append(f'<path d="M{f(cx - 40 * s)} {f(cy - 80 * s)} L {f(cx + 40 * s)} {f(cy - 80 * s)} L {f(cx + 90 * s)} {f(cy - 50 * s)} L {f(cx + 70 * s)} {f(cy - 20 * s)} L {f(cx + 50 * s)} {f(cy - 36 * s)} '
             f'L {f(cx + 60 * s)} {f(cy + 90 * s)} L {f(cx - 60 * s)} {f(cy + 90 * s)} L {f(cx - 50 * s)} {f(cy - 36 * s)} L {f(cx - 70 * s)} {f(cy - 20 * s)} L {f(cx - 90 * s)} {f(cy - 50 * s)} Z" '
             f'fill="#2A6A5A" stroke="#0D0D0F" stroke-width="2.6"></path>'
             f'<path d="M{f(cx - 58 * s)} {f(cy + 76 * s)} L {f(cx + 58 * s)} {f(cy + 76 * s)}" stroke="#E8B830" stroke-width="{f(5 * s)}" stroke-dasharray="8 5"></path>')
    return "".join(o)

# ---- 1 Samuel 3–8 -------------------------------------------------------------------------------------------------------
ARK_ROUTE = [("EBEN-EZER", 0.82, 0.3), ("ASHDOD", 0.28, 0.5), ("GATH", 0.46, 0.66), ("EKRON", 0.44, 0.34), ("BETH-SHEMESH", 0.66, 0.42), ("KIRIATH-JEARIM", 0.74, 0.24)]
def ark_map(w, h, upto="EKRON"):
    """The ark carried about among the Philistines, as a technical map: Eben-ezer to Ashdod, Gath, Ekron (and home)."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.14)} -10 C {f(w * 0.12)} {f(h * 0.3)} {f(w * 0.1)} {f(h * 0.7)} {f(w * 0.06)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    n = [r[0] for r in ARK_ROUTE].index(upto) + 1
    o.append(route([(w * x, h * y) for _, x, y in ARK_ROUTE[:n]], color="#FFD23F"))
    for i, (nm, x, y) in enumerate(ARK_ROUTE[:n]):
        o.append(node(w * x, h * y, nm, "#D7261E" if i == n - 1 else "#FFD23F", r=6 if i == n - 1 else 4, dy=-12, size=9))
    return "".join(o)

def tumors(w, h, seed):
    """The cry of the city went up to heaven: a Philistine city at night, its people crying out on the roofs, a dark sky."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A3A"></rect>', mk.stars(30, w, h * 0.4, seed),
         J.city_hill(w * 0.5, h * 0.92, w * 0.46, h * 0.4, seed), ground(w, h, h * 0.92, "#1A0E1A", dy=0)]
    for _ in range(8):
        x = r.uniform(w * 0.2, w * 0.8); y = h * r.uniform(0.5, 0.6)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x - 6)} {f(y - 30)} M{f(x)} {f(y)} L {f(x + 6)} {f(y - 30)}" stroke="#12090A" stroke-width="3"></path><circle cx="{f(x)}" cy="{f(y + 6)}" r="6" fill="#12090A"></circle>')
    o.append(V.rays(w * 0.5, h * 0.5, 24, 10, max(w, h), color="#D7261E", op=0.12))
    return "".join(o)

def golden(w, h, seed):
    """The trespass-offering: five golden tumors and five golden mice in a coffer."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A2E"></rect>', V.rays(w * 0.5, h * 0.5, 30, 20, max(w, h), color="#FFD23F", op=0.16),
         ground(w, h, h * 0.84, "#3A2A2A", dy=0)]
    cx, cy = w * 0.5, h * 0.74
    o.append(f'<rect x="{f(cx - w * 0.3)}" y="{f(cy - h * 0.04)}" width="{f(w * 0.6)}" height="{f(h * 0.14)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    for i in range(5):
        x = cx - w * 0.24 + i * w * 0.12
        o.append(f'<ellipse cx="{f(x)}" cy="{f(cy - h * 0.12)}" rx="{f(w * 0.035)}" ry="{f(h * 0.05)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></ellipse>')
        o.append(f'<g transform="translate({f(x)} {f(cy - h * 0.02)})"><ellipse cx="0" cy="0" rx="14" ry="8" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
                 '<circle cx="12" cy="-4" r="5" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></circle><path d="M-14 0 C -24 4 -28 -6 -34 -2" fill="none" stroke="#E8B830" stroke-width="2"></path></g>')
    return "".join(o)

def eben_ezer(p, w, h, seed):
    """Samuel set a stone between Mizpah and Shen and called it Eben-ezer: a standing stone on the hill, thunder far off."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A6E8A"></rect>',
         hills(w, h, h * 0.5, seed, color="#4A5A3A", amp=16), ground(w, h, h * 0.62, "#8A7A5A", dy=0)]
    o.append(f'<path d="M{f(w * 0.46)} {f(h * 0.66)} L {f(w * 0.47)} {f(h * 0.3)} C {f(w * 0.5)} {f(h * 0.24)} {f(w * 0.56)} {f(h * 0.24)} {f(w * 0.58)} {f(h * 0.3)} L {f(w * 0.6)} {f(h * 0.66)} Z" fill="#A89A86" stroke="#0D0D0F" stroke-width="2.6"></path>')
    s = fit(b, h * 0.4)
    o.append(mk.person(p, round(w * 0.3), round(b), round(s, 3), body=SKIN, cloth="#1E2A5A", sw=3, up=[(-22, -158), (-6, -196), (8, -228)], extra=A.headcloth("#1E2A5A") + A.WHITE_BEARD))
    return "".join(o)

# ---- 1 Samuel 9–10 ------------------------------------------------------------------------------------------------------
SAUL_C = "#8A1A2A"
def saul_fig(p, x, y, s, flip=False, up=None, crown=False):
    """Saul at a distance: crimson headcloth and tunic, a head taller than everyone."""
    ex = A.headcloth(SAUL_C) + A.BLACK_BEARD + ('<path d="M-14 -200 L -14 -214 L -7 -206 L 0 -218 L 7 -206 L 14 -214 L 14 -200 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>' if crown else "")
    return mk.person(p, round(x), round(y), round(s * 1.12, 3), body=SKIN, cloth=SAUL_C, kind="Tunic", sw=3, flip=flip, up=up, extra=ex)

def samuel_fig(p, x, y, s, flip=False, up=None):
    """Samuel grown old: midnight-blue headcloth and robe, grey beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#1E2A5A", sw=3, flip=flip, up=up, extra=A.headcloth("#1E2A5A") + A.WHITE_BEARD)

def asses_search(p, w, h, seed):
    """Saul and his servant seeking the lost asses through the hill-country, an empty land."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.84, h * 0.2, 18, color="#FF8A3D", op=0.3),
         hills(w, h, h * 0.42, seed, color="#9A8A6A", amp=18), hills(w, h, h * 0.56, seed + 1, color="#B89A6A", amp=12), ground(w, h, h * 0.64, "#C8A06A", dy=0)]
    s = fit(b, h * 0.4)
    o.append(saul_fig(p, w * 0.3, b, s, up=[(-22, -158), (4, -170), (30, -176)]) + man(p, w * 0.44, b, s * 0.9, "#7A6A4A"))
    return "".join(o)

def high_place(p, w, h, seed):
    """The city on its hill with the high place above, maidens going out to draw water."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8FD0E2"></rect>', sun(w * 0.86, h * 0.16, 16, op=0.3),
         J.city_hill(w * 0.6, h * 0.66, w * 0.34, h * 0.42, seed), ground(w, h, h * 0.66, "#B89A6A", dy=0)]
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.26)} L {f(w * 0.6)} {f(h * 0.18)} L {f(w * 0.64)} {f(h * 0.26)} Z" fill="#A89A86" stroke="#0D0D0F" stroke-width="2"></path>' + E.blaze(w * 0.6, h * 0.19, w * 0.04, h * 0.08, seed, n=4))
    s = fit(b, h * 0.42)
    o.append(saul_fig(p, w * 0.14, b, s) + man(p, w * 0.24, b, s * 0.9, "#7A6A4A"))
    for i in range(3):
        o.append(woman(p, w * (0.66 + i * 0.08), b, s * 0.86, ("#C2456A", "#5AC8C8", "#E8B830")[i], flip=True)
                 + f'<path d="M{f(w * (0.66 + i * 0.08) - 10)} {f(b - 210 * s * 0.86)} C {f(w * (0.66 + i * 0.08) - 20)} {f(b - 240 * s * 0.86)} {f(w * (0.66 + i * 0.08) + 10)} {f(b - 250 * s * 0.86)} {f(w * (0.66 + i * 0.08) + 4)} {f(b - 210 * s * 0.86)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return "".join(o)

def prophets(p, w, h, seed):
    """A band of prophets coming down from the high place with psaltery, timbrel, pipe and harp; Saul among them."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3B86A"></rect>', V.rays(w * 0.5, h * 0.1, 30, 20, max(w, h), color="#FFF4C2", op=0.3),
         f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.5)} {f(h * 0.3)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B89A6A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = fit(b, h * 0.42)
    for i in range(6):
        x = w * (0.08 + i * 0.13)
        if i == 3: o.append(saul_fig(p, x, b, s, up=[(-22, -158), (-6, -196), (8, -228)])); continue
        o.append(man(p, x, b - (i % 2) * 6, s * 0.92, ("#F3EFE6", "#E8D8B0", "#D8C8A0")[i % 3], up=[(-22, -158), (-6, -176), (12, -182)])
                 + S2.harp(x + 16 * s, b - 170 * s, 0.3 * s * 3) if i % 2 == 0 else man(p, x, b - (i % 2) * 6, s * 0.92, "#E8D8B0", up=[(-22, -158), (-30, -196), (-36, -228)]))
    return "".join(o)

def baggage(p, w, h, seed):
    """Saul hid himself among the baggage: bundles and stuff heaped in the camp at Mizpah, a head taller than the heap."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8C88A"></rect>', ground(w, h, h * 0.6, "#B89A6A", dy=0)]
    o.append(N.camp(14, -10, w + 10, h * 0.6, h * 0.7, seed))
    o.append(saul_fig(p, w * 0.5, h * 0.92, fit(h * 0.92, h * 0.5) * 0.9))
    for _ in range(14):
        x, y = r.uniform(w * 0.3, w * 0.7), r.uniform(h * 0.72, h * 0.96)
        o.append(f'<rect x="{f(x - 26)}" y="{f(y - 22)}" width="52" height="34" rx="8" fill="{r.choice(["#A8946A", "#8A6A4A", "#C8A06A"])}" stroke="#0D0D0F" stroke-width="2"></rect>')
    return "".join(o)

# ---- 1 Samuel 11–13 -----------------------------------------------------------------------------------------------------
import exodus2 as E2
def oxen_field(p, w, h, seed):
    """Saul came following the oxen out of the field at evening."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3B86A"></rect>', sun(w * 0.2, h * 0.36, 26, color="#FF8A3D", op=0.4),
         hills(w, h, h * 0.5, seed, color="#9A7A4A", amp=12), ground(w, h, h * 0.58, "#C8A06A", dy=0)]
    o.append(S1.cow(w * 0.62, b, min(0.9, h / 360), color="#8A5A30") + S1.cow(w * 0.8, b - 6, min(0.86, h / 380), color="#6A4A2A"))
    o.append(saul_fig(p, w * 0.36, b, fit(b, h * 0.44)))
    return "".join(o)

def harvest_thunder(w, h, seed):
    """Thunder and rain in the wheat harvest: lightning over a field of ripe grain."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2E4A"></rect>', E2.bolt(w * 0.62, 0, h * 0.62, seed, w=1.6),
         ground(w, h, h * 0.62, "#B8902A", dy=0)]
    r = random.Random(seed)
    for _ in range(80):
        x, y = r.uniform(0, w), r.uniform(0, h * 0.9)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x - 4)} {f(y + 18)}" stroke="#8FB8D8" stroke-width="1.6" opacity="0.7"></path>')
    for i in range(40):
        x = w * (i / 40); o.append(f'<path d="M{f(x)} {f(h)} L {f(x + 3)} {f(h * 0.7)}" stroke="#E8C040" stroke-width="3"></path><ellipse cx="{f(x + 3)}" cy="{f(h * 0.68)}" rx="3" ry="8" fill="#E8C040"></ellipse>')
    return "".join(o)

def no_smith(w, h, seed):
    """No smith in Israel: shares, coulters, axes and mattocks laid by a Philistine forge, a file beside them."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2218"></rect>', ground(w, h, h * 0.8, "#2A1810", dy=0),
         E.blaze(w * 0.82, h * 0.82, w * 0.16, h * 0.3, seed, n=6)]
    tools = [("M0 0 L 60 -10 L 70 4 L 4 14 Z", "#8A8A9A"), ("M0 0 L 10 -60 L 22 -58 L 12 2 Z", "#7A7A8A"), ("M0 -40 L 40 -40 L 40 -20 L 0 -30 Z", "#9A9AAA"), ("M0 0 L 50 -30 L 56 -20 L 6 10 Z", "#8A8A9A")]
    for i, (d, c) in enumerate(tools):
        x = w * (0.14 + i * 0.15); y = h * 0.78
        o.append(f'<path d="M{f(x - 30)} {f(y)} L {f(x + 40)} {f(y - 30)}" stroke="#6A4A2A" stroke-width="7" stroke-linecap="round"></path>'
                 f'<path transform="translate({f(x + 30)} {f(y - 36)})" d="{d}" fill="{c}" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

# ---- 1 Samuel 14 --------------------------------------------------------------------------------------------------------
JONATHAN_C = "#2A5A9A"
def jonathan_fig(p, x, y, s, flip=False, up=None):
    """Jonathan at a distance: blue headcloth and tunic."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=JONATHAN_C, kind="Tunic", sw=3, flip=flip, up=up, extra=A.headcloth(JONATHAN_C))

def crags(p, w, h, seed, climbing=False):
    """The pass of Michmash between the crags Bozez and Seneh, the Philistine garrison on the height."""
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8FD0E2"></rect>', sun(w * 0.86, h * 0.14, 16, op=0.3),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.2)} L {f(w * 0.18)} {f(h * 0.12)} L {f(w * 0.36)} {f(h * 0.5)} L {f(w * 0.4)} {f(h + 10)} Z" fill="#9A7A5A" stroke="#0D0D0F" stroke-width="2.6"></path>',
         f'<path d="M{f(w * 0.56)} {f(h + 10)} L {f(w * 0.6)} {f(h * 0.4)} L {f(w * 0.78)} {f(h * 0.1)} L {f(w + 10)} {f(h * 0.16)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.6"></path>',
         label(w * 0.14, h * 0.9, "BOZEZ", "#F3EFE6", 10) + label(w * 0.86, h * 0.9, "SENEH", "#F3EFE6", 10)]
    for i in range(4):
        x = w * (0.72 + i * 0.06); o.append(mk.person(p, round(x), round(h * 0.16), round(fit(h * 0.16, h * 0.04), 3), body="#12090A", cloth="#1F5FAD", kind="Tunic", sw=2, flip=True, extra=E4.SPEAR))
    if climbing:
        s = fit(h * 0.5, h * 0.3)
        o.append(jonathan_fig(p, w * 0.6, h * 0.46, s, up=[(-22, -158), (-6, -196), (8, -228)]) + man(p, w * 0.56, h * 0.62, s * 0.9, "#6A5A3A", up=[(-22, -158), (-6, -196), (8, -228)]))
    else:
        s = fit(h * 0.92, h * 0.5)
        o.append(jonathan_fig(p, w * 0.46, h * 0.92, s) + man(p, w * 0.52, h * 0.92, s * 0.92, "#6A5A3A", extra=E4.SPEAR))
    return "".join(o)

def honey_rod(w, h, seed):
    """The honey dropped in the forest; the end of Jonathan's rod dipped in the honeycomb."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2E4A2A"></rect>']
    for i in range(9):
        x = w * (0.04 + i * 0.12)
        o.append(f'<rect x="{f(x - 10)}" y="-10" width="20" height="{f(h * 0.86)}" fill="#3A2A1A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<circle cx="{f(x)}" cy="{f(h * 0.08)}" r="{f(w * 0.08)}" fill="#3F7A3A" stroke="#0D0D0F" stroke-width="2"></circle>')
    o.append(ground(w, h, h * 0.84, "#4A3A22", dy=0))
    cx, cy = w * 0.5, h * 0.78
    o.append(f'<path d="M{f(cx - w * 0.1)} {f(cy)} C {f(cx - w * 0.1)} {f(cy - h * 0.14)} {f(cx + w * 0.1)} {f(cy - h * 0.14)} {f(cx + w * 0.1)} {f(cy)} Z" fill="#E8A317" stroke="#8A5A10" stroke-width="2"></path>')
    for k in range(10):
        o.append(f'<path d="M{f(cx - w * 0.08 + k * w * 0.018)} {f(cy)} L {f(cx - w * 0.08 + k * w * 0.018)} {f(cy + r.uniform(8, 26))}" stroke="#E8A317" stroke-width="3" stroke-linecap="round"></path>')
    o.append(f'<path d="M{f(w * 0.96)} {f(h * 0.3)} L {f(cx + w * 0.02)} {f(cy - h * 0.08)}" stroke="#6A4A2A" stroke-width="7" stroke-linecap="round"></path>')
    return "".join(o)

SAUL_WARS = [("MOAB", 0.62, 0.7), ("AMMON", 0.74, 0.42), ("EDOM", 0.5, 0.94), ("ZOBAH", 0.72, 0.08), ("THE PHILISTINES", 0.12, 0.6), ("AMALEK", 0.2, 0.92)]
def saul_wars(w, h):
    """Saul fought against all his enemies on every side: Moab, Ammon, Edom, Zobah, the Philistines, Amalek."""
    o = [grid_bg(w, h)]
    cx, cy = w * 0.42, h * 0.46
    for nm, x, y in SAUL_WARS:
        o.append(route([(cx, cy), (w * x, h * y)], color="#D7261E", sw=1.8) + node(w * x, h * y, nm, "#FFD23F", r=5, dy=-10 if y > 0.1 else 18, size=9))
    o.append(node(cx, cy, "GIBEAH", "#8FD0E2", r=6, dy=18, size=9))
    return "".join(o)

# ---- 1 Samuel 15–16 -----------------------------------------------------------------------------------------------------
def spoil_flocks(w, h, seed):
    """The bleating of the sheep and the lowing of the oxen: the best of the spoil of Amalek driven to Gilgal."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8C88A"></rect>', hills(w, h, h * 0.44, seed, color="#B89A6A", amp=12), ground(w, h, h * 0.5, "#C8A06A", dy=0)]
    items = sorted((r.uniform(h * 0.56, h * 0.96), r.uniform(0, w), r.random()) for _ in range(26))
    for y, x, q in items:
        k = (y - h * 0.56) / (h * 0.4); s = 0.2 + 0.3 * k
        o.append(S1.cow(x, y, s * 0.9, color=r.choice(["#8A5A30", "#C9A27A", "#6A4A2A"]), flip=q < 0.5) if q < 0.3 else E.sheep(x, y, s * 1.1, flip=q < 0.6))
    return "".join(o)

def rent_skirt(w, h, seed):
    """The skirt of Samuel's robe rent in Saul's hand."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A3A"></rect>', V.rays(w * 0.5, h * 0.5, 24, 10, max(w, h), color="#9AA8C8", op=0.15)]
    o.append(S2.skirt_piece(w * 0.5, h * 0.56, min(2.6, h / 120), color="#1E2A5A"))
    return "".join(o)

# ---- 1 Samuel 18–19 -----------------------------------------------------------------------------------------------------
def women_singing(p, w, h, seed):
    """The women came out of all the cities of Israel, singing and dancing, with timbrels: Saul hath slain his thousands."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3B86A"></rect>', V.rays(w * 0.5, h * 0.2, 30, 20, max(w, h), color="#FFF4C2", op=0.3),
         J.city_hill(w * 0.82, h * 0.6, w * 0.2, h * 0.24, seed), ground(w, h, h * 0.6, "#C8A06A", dy=0)]
    s = fit(b, h * 0.44)
    for i in range(7):
        o.append(S3.musician(p, w * (0.06 + i * 0.13), b - (i % 2) * 8, s * (0.94 + 0.04 * (i % 2)), kind="timbrel", cloth=r.choice(["#C2456A", "#E8B830", "#5AC8C8", "#B88AE8", "#F3EFE6"]), seed=seed + i))
    return "".join(o)

def let_down(p, w, h, seed):
    """Michal let David down through the window by night."""
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#14123A"></rect>', mk.stars(30, w, h * 0.4, seed),
         f'<rect x="{f(w * 0.3)}" y="{f(h * 0.06)}" width="{f(w * 0.5)}" height="{f(h + 10)}" fill="#6A5A6A" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         S3.window(w * 0.55, h * 0.22, w * 0.12, h * 0.16, inner="#FFC14D")]
    o.append(f'<path d="M{f(w * 0.55)} {f(h * 0.34)} L {f(w * 0.56)} {f(h * 0.7)}" stroke="#C8A06A" stroke-width="3"></path>')
    s = fit(h * 0.84, h * 0.6)
    o.append(S2.david(p, w * 0.56, h * 0.84, s, staff=False, bag=False, up=[(-22, -158), (-6, -196), (8, -228)]))
    return "".join(o)

def teraphim_bed(w, h, seed):
    """The teraphim laid in the bed, a pillow of goats' hair at the head thereof, covered with the clothes."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A2A"></rect>', ground(w, h, h * 0.84, "#2A1A18", dy=0)]
    o.append(f'<rect x="{f(w * 0.14)}" y="{f(h * 0.6)}" width="{f(w * 0.72)}" height="{f(h * 0.14)}" rx="10" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<path d="M{f(w * 0.24)} {f(h * 0.6)} C {f(w * 0.3)} {f(h * 0.44)} {f(w * 0.7)} {f(h * 0.46)} {f(w * 0.8)} {f(h * 0.6)} Z" fill="#8A6A8A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(w * 0.2)}" cy="{f(h * 0.54)}" rx="{f(w * 0.06)}" ry="{f(h * 0.06)}" fill="#3A2A20" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    from genesis.art4 import clay_lamp
    o.append(clay_lamp(w * 0.9, h * 0.44, min(1.2, h / 260)))
    return "".join(o)

def naioth(p, w, h, seed):
    """Naioth in Ramah: the company of the prophets prophesying, Samuel standing as head over them."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3B86A"></rect>', V.rays(w * 0.5, h * 0.1, 30, 20, max(w, h), color="#FFF4C2", op=0.3),
         hills(w, h, h * 0.5, seed, color="#9A8A6A", amp=12), ground(w, h, h * 0.6, "#C8A06A", dy=0)]
    s = fit(b, h * 0.42)
    o.append(samuel_fig(p, w * 0.5, b, s * 1.04, up=[(-22, -158), (-6, -196), (8, -228)]))
    for i in range(6):
        x = w * (0.08 + i * 0.16) if i < 3 else w * (0.6 + (i - 3) * 0.14)
        o.append(man(p, x, b - (i % 2) * 6, s * 0.9, "#F3EFE6", flip=x > w * 0.5, up=[(-22, -158), (-30, -196), (-36, -228)]))
    return "".join(o)

import judges2 as J2, samuel4 as S4

# ---- 1 Samuel 20–21 -----------------------------------------------------------------------------------------------------
def arrows(p, w, h, seed):
    """Jonathan shoots an arrow beyond the lad in the field by the stone Ezel; David hidden behind it."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#F3D8A0"></rect>', sun(w * 0.16, h * 0.2, 18, color="#FFE680", op=0.4),
         hills(w, h, h * 0.5, seed, color="#9AAA6A", amp=12), ground(w, h, h * 0.58, "#B8B07A", dy=0)]
    o.append(f'<path d="M{f(w * 0.84)} {f(b)} L {f(w * 0.85)} {f(h * 0.56)} C {f(w * 0.88)} {f(h * 0.5)} {f(w * 0.94)} {f(h * 0.5)} {f(w * 0.96)} {f(h * 0.56)} L {f(w * 0.98)} {f(b)} Z" fill="#A89A86" stroke="#0D0D0F" stroke-width="2.4"></path>')
    s = fit(b, h * 0.42)
    o.append(jonathan_fig(p, w * 0.18, b, s, up=[(-22, -158), (4, -170), (30, -176)]))
    o.append(f'<path d="M{f(w * 0.22)} {f(b - 176 * s)} C {f(w * 0.4)} {f(h * 0.2)} {f(w * 0.6)} {f(h * 0.2)} {f(w * 0.74)} {f(h * 0.5)}" fill="none" stroke="#FFF4C2" stroke-width="2" stroke-dasharray="6 6"></path>'
             f'<path d="M{f(w * 0.74)} {f(h * 0.5)} L {f(w * 0.72)} {f(h * 0.46)} M{f(w * 0.74)} {f(h * 0.5)} L {f(w * 0.7)} {f(h * 0.5)}" stroke="#3A2214" stroke-width="3"></path>')
    o.append(S1.boy(p, w * 0.56, b, s * 0.7, up=[(-22, -158), (-46, -140), (-60, -160)]))
    return "".join(o)

def empty_seat(w, h, seed):
    """The new moon feast: the king's table, and David's place empty by the wall."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A2A3A"></rect>', ground(w, h, h * 0.82, "#3A1A22", dy=0),
         S3.table(w * 0.5, h * 0.82, w * 0.7, min(1.3, h / 260))]
    o.append(S3.throne(w * 0.2, h * 0.82, min(0.9, h / 360)) + S1.seat(w * 0.8, h * 0.82, min(1.2, h / 260)))
    o.append(V.rays(w * 0.8, h * 0.6, 20, 10, w * 0.4, color="#FFF4C2", op=0.15))
    return "".join(o)

def showbread(w, h, seed):
    """The holy bread at Nob, and the sword of Goliath wrapped in a cloth behind the ephod."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A2E"></rect>', V.rays(w * 0.5, h * 0.5, 30, 20, max(w, h), color="#FFD23F", op=0.12),
         ground(w, h, h * 0.8, "#3A2A2A", dy=0)]
    o.append(f'<rect x="{f(w * 0.08)}" y="{f(h * 0.6)}" width="{f(w * 0.4)}" height="{f(h * 0.08)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    for row in range(2):
        for i in range(6):
            o.append(f'<ellipse cx="{f(w * (0.12 + i * 0.065))}" cy="{f(h * (0.56 - row * 0.05))}" rx="{f(w * 0.03)}" ry="{f(h * 0.025)}" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    o.append(f'<path d="M{f(w * 0.62)} {f(h * 0.78)} L {f(w * 0.92)} {f(h * 0.3)}" stroke="#C8C8D0" stroke-width="9" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.66)} {f(h * 0.74)} L {f(w * 0.84)} {f(h * 0.44)}" stroke="#E8E2D6" stroke-width="22" opacity="0.85"></path>'
             f'<path d="M{f(w * 0.6)} {f(h * 0.7)} L {f(w * 0.68)} {f(h * 0.76)}" stroke="#5A3A22" stroke-width="8"></path>')
    return "".join(o)

def gath_gate(p, w, h, seed):
    """The gate of Gath, and David scrabbling on its doors, feigning himself mad before Achish's servants."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8B880"></rect>',
         S4.gatehouse(w * 0.5, b, w * 0.6, h * 0.8), ground(w, h, b, "#9A7A4A", dy=0)]
    s = fit(b, h * 0.6)
    o.append(S2.david(p, w * 0.5, b, s, staff=False, bag=False, up=[(-22, -158), (-10, -190), (6, -210)]))
    o.append(J2.philistines(p, 4, w * 0.04, w * 0.22, b - 6, b, seed, s * 0.9, s, flip=False))
    return "".join(o)

# ---- 1 Samuel 22–24 -----------------------------------------------------------------------------------------------------
def adullam(p, w, h, seed):
    """The cave of Adullam: men in distress, in debt and discontented gathered at its mouth about David."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), S2.cave(w, h, w * 0.3, w * 0.4, h * 0.86, seed)]
    s = fit(h * 0.86, h * 0.5)
    o.append(S2.david(p, w * 0.5, h * 0.86, s, staff=True, bag=True))
    for i in range(8):
        x = w * (0.12 + i * 0.1)
        if abs(x - w * 0.5) < w * 0.06: continue
        o.append(mk.person(p, round(x), round(h * 0.86 - (i % 2) * 4), round(s * 0.86, 3), body="#12090A", cloth=r.choice(["#3A2A2A", "#4A3A2A", "#2A2A3A"]), kind="Tunic", sw=2, flip=x > w * 0.5))
    return "".join(o)

def tamarisk(p, w, h, seed):
    """Saul sitting under the tamarisk-tree in Ramah with his spear in his hand, his servants standing about him."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8C88A"></rect>', hills(w, h, h * 0.5, seed, color="#B89A6A", amp=12),
         ground(w, h, h * 0.56, "#C8A06A", dy=0), S4.great_oak(w * 0.22, b, min(1.3, h / 320), seed)]
    s = fit(b, h * 0.44)
    o.append(S3.throne(w * 0.3, b, s * 0.9) + saul_fig(p, w * 0.3, b - 26 * s, s, crown=True, up=[(-22, -158), (-8, -150), (4, -150)])
             + f'<path d="M{f(w * 0.3 + 4 * s)} {f(b - 360 * s)} L {f(w * 0.3 + 8 * s)} {f(b)}" stroke="#3E2416" stroke-width="5"></path>')
    for i in range(5):
        o.append(man(p, w * (0.52 + i * 0.09), b - (i % 2) * 6, s * 0.92, random.Random(seed + i).choice(WAR), flip=True, extra=E4.SPEAR))
    return "".join(o)

def nob_smoke(w, h, seed):
    """Nob, the city of the priests, smoke rising from it at evening (22:18–19 are words only)."""
    from jos.art import burning
    return burning(w, h, seed, city="nob")

def ephod_inquire(p, w, h, seed):
    """Abiathar with the ephod; David inquiring of Jehovah."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A3A"></rect>', V.rays(w * 0.5, h * 0.1, 30, 20, max(w, h), color="#FFF4C2", op=0.2),
         ground(w, h, b, "#3A2A2A", dy=0)]
    s = fit(b, h * 0.62)
    o.append(S2.david(p, w * 0.32, b, s, staff=False, bag=False, up=[(-22, -158), (-6, -196), (8, -228)]))
    o.append(mk.person(p, round(w * 0.66), round(b), round(s, 3), body=SKIN, cloth="#F3EFE6", sw=3, flip=True,
                       extra='<path d="M-24 -160 L 24 -160 L 22 -90 L -22 -90 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'))
    return "".join(o)

def maon(p, w, h, seed):
    """Saul on this side of the mountain, David and his men on that side, in the wilderness of Maon."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8B880"></rect>', sun(w * 0.5, h * 0.12, 16, color="#FF8A3D", op=0.3),
         f'<path d="M-10 {f(h + 10)} L {f(w * 0.5)} {f(h * 0.2)} L {f(w + 10)} {f(h + 10)} Z" fill="#9A6A4A" stroke="#0D0D0F" stroke-width="2.6"></path>']
    for i in range(6):
        x = w * (0.08 + i * 0.05); y = h * (0.94 - i * 0.04)
        o.append(man(p, x, y, fit(y, y - h * 0.16), SAUL_C if i == 0 else r.choice(WAR), extra=E4.SPEAR))
    for i in range(5):
        x = w * (0.92 - i * 0.05); y = h * (0.94 - i * 0.04)
        o.append(man(p, x, y, fit(y, y - h * 0.16), "#C8A06A" if i == 0 else r.choice(("#5A4A3A", "#6A5A3A")), flip=True))
    return "".join(o)

def engedi_cave(p, w, h, seed):
    """Inside the cave by the sheepcotes: David cutting off the skirt of Saul's robe privily, his men in the innermost parts."""
    o = [mk.defs(p, *ALL), S2.cave(w, h, w * 0.58, w * 0.34, h * 0.88, seed)]
    s = fit(h * 0.88, h * 0.5)
    o.append(saul_fig(p, w * 0.76, h * 0.88, s * 0.9, flip=True).replace('fill="#C98E66"', 'fill="#12090A"'))
    o.append(mk.person(p, round(w * 0.5), round(h * 0.88), round(s * 0.7, 3), body="#12090A", cloth="#2A2220", kind="Tunic", sw=2))
    for i in range(4):
        o.append(f'<circle cx="{f(w * (0.08 + i * 0.07))}" cy="{f(h * (0.56 + (i % 2) * 0.04))}" r="3" fill="#FFF4C2"></circle><circle cx="{f(w * (0.08 + i * 0.07) + 9)}" cy="{f(h * (0.56 + (i % 2) * 0.04))}" r="3" fill="#FFF4C2"></circle>')
    return "".join(o)

import judges1 as J1

# ---- 1 Samuel 25–26 -----------------------------------------------------------------------------------------------------
ABIGAIL_C = "#3A7A6A"
def abigail_fig(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=ABIGAIL_C, woman=True, hair="#1A1210", sw=3, flip=flip, up=up, extra=A.headcloth("#E8B830"))

def shearing(p, w, h, seed):
    """Nabal shearing his three thousand sheep in Carmel."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8FD0E2"></rect>', hills(w, h, h * 0.4, seed, color="#7A9A5A", amp=14),
         ground(w, h, h * 0.48, "#9CCB5E", dy=0)]
    for _ in range(30):
        y = r.uniform(h * 0.52, h * 0.96); o.append(E.sheep(r.uniform(0, w), y, 0.16 + 0.26 * (y - h * 0.52) / (h * 0.44), flip=r.random() < 0.5))
    return "".join(o)

def abigail_gifts(p, w, h, seed):
    """Abigail on her ass coming down by the covert of the mountain, asses laden with loaves, wine, raisins and figs before her."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8B880"></rect>',
         f'<path d="M-10 {f(h * 0.4)} C {f(w * 0.3)} {f(h * 0.3)} {f(w * 0.5)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.44)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B89A6A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = fit(b, h * 0.44)
    for i in range(3):
        x = w * (0.1 + i * 0.16)
        o.append(N.ass(x, b - i * 4, s * 0.5, flip=True) + f'<rect x="{f(x - 28 * s * 0.5)}" y="{f(b - 130 * s * 0.5)}" width="{f(56 * s * 0.5)}" height="{f(40 * s * 0.5)}" rx="6" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(N.mount(w * 0.72, b, s * 0.6, flip=True, rider_cloth=ABIGAIL_C, p=p))
    return "".join(o)

def at_feet(p, w, h, seed):
    """Abigail fallen at David's feet on her face; his men behind him with swords girded."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8B880"></rect>', hills(w, h, h * 0.5, seed, color="#B89A6A", amp=12),
         ground(w, h, h * 0.58, "#C8A06A", dy=0)]
    s = fit(b, h * 0.42)
    o.append(E.kneel(w * 0.36, b, s * 0.9, color=ABIGAIL_C, skin="#8A5A3A"))
    o.append(S2.david(p, w * 0.58, b, s, staff=False, bag=False, flip=True))
    for i in range(5):
        o.append(man(p, w * (0.72 + i * 0.06), b - (i % 2) * 6, s * 0.9, random.Random(seed + i).choice(WAR), flip=True, extra=E4.SPEAR))
    return "".join(o)

def saul_asleep(p, w, h, seed, taken=False):
    """Saul asleep within the place of the wagons, his spear stuck in the ground at his head, the cruse beside it, by night."""
    o = [mk.defs(p, *ALL), night(w, h, seed, "#14123A"), ground(w, h, h * 0.62, "#2A2030", dy=0)]
    for i in range(5):
        x = w * (0.06 + i * 0.22); o.append(f'<circle cx="{f(x)}" cy="{f(h * 0.62)}" r="{f(h * 0.08)}" fill="none" stroke="#5A4A3A" stroke-width="5"></circle>')
    o.append(J1.rug_sleeper(w * 0.46, h * 0.86, min(1.2, h / 280), color=SAUL_C))
    if not taken:
        o.append(f'<path d="M{f(w * 0.72)} {f(h * 0.9)} L {f(w * 0.74)} {f(h * 0.3)}" stroke="#3E2416" stroke-width="6"></path><path d="M{f(w * 0.74)} {f(h * 0.3)} L {f(w * 0.73)} {f(h * 0.24)} L {f(w * 0.76)} {f(h * 0.3)} Z" fill="#C8C2D6" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<path d="M{f(w * 0.78)} {f(h * 0.9)} C {f(w * 0.76)} {f(h * 0.8)} {f(w * 0.84)} {f(h * 0.8)} {f(w * 0.82)} {f(h * 0.9)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>')
    for i in range(6):
        o.append(J1.rug_sleeper(w * (0.1 + i * 0.16), h * (0.72 + (i % 2) * 0.04), min(0.6, h / 520), color="#3A3448"))
    return "".join(o)

def hilltop_cry(p, w, h, seed):
    """David on the top of the mountain afar off, a great space between, holding up the king's spear and the cruse."""
    o = [mk.defs(p, *ALL), night(w, h, seed, "#2A2458"), sun(w * 0.86, h * 0.2, 14, color="#E8F0F6", op=0.3),
         f'<path d="M{f(w * 0.5)} {f(h + 10)} L {f(w * 0.74)} {f(h * 0.42)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} Z" fill="#3A3048" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.86, "#1E1A2E", dy=0), N.camp(10, -10, w * 0.4, h * 0.84, h * 0.96, seed, color=("#2A2030", "#3A2A3A", "#1A1420"))]
    s = fit(h * 0.42, h * 0.18)
    o.append(S2.david(p, w * 0.74, h * 0.42 + 2, s, staff=False, bag=False, up=[(-22, -158), (-6, -196), (8, -228)])
             + f'<path d="M{f(w * 0.74 - 10 * s)} {f(h * 0.42 - 300 * s)} L {f(w * 0.74 - 2 * s)} {f(h * 0.42 - 120 * s)}" stroke="#3E2416" stroke-width="4"></path>')
    return "".join(o)

# ---- 1 Samuel 27–29 -----------------------------------------------------------------------------------------------------
def endor(p, w, h, seed, rising=True):
    """The woman's house at En-dor by night: a clay lamp, the woman cowering, and an old man covered with a robe rising as a
    pale shape out of the earth (no face drawn)."""
    from genesis.art4 import clay_lamp
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1420"></rect>', ground(w, h, b, "#2A2026", dy=0),
         clay_lamp(w * 0.14, h * 0.5, min(1.2, h / 260)), f'<circle cx="{f(w * 0.14)}" cy="{f(h * 0.46)}" r="{f(h * 0.4)}" fill="#FFC14D" opacity="0.08"></circle>']
    s = fit(b, h * 0.36)
    if rising:
        o.append(f'<ellipse cx="{f(w * 0.62)}" cy="{f(b)}" rx="{f(w * 0.14)}" ry="{f(h * 0.04)}" fill="#8A8AB8" opacity="0.4"></ellipse>'
                 + f'<g opacity="0.55">' + mk.person(p, round(w * 0.62), round(b), round(s * 1.05, 3), body="#C8D0E8", cloth="#E8ECF8", stroke="#8A8AB8", sw=3) + '</g>'
                 + V.rays(w * 0.62, b - 120 * s, 24, 10, w * 0.5, color="#C8D0E8", op=0.18))
    o.append(E.kneel(w * 0.3, b, s * 0.9, color="#4A3A4A", skin="#6A4A3A"))
    o.append(mk.person(p, round(w * 0.88), round(b), round(s * 1.1, 3), body="#12090A", cloth="#3A3040", sw=3, flip=True))
    return "".join(o)

def unleavened(w, h, seed):
    """The fatted calf and the unleavened bread set before Saul and his servants by night."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A18"></rect>', ground(w, h, h * 0.82, "#1A100E", dy=0),
         S3.table(w * 0.5, h * 0.82, w * 0.62, min(1.3, h / 260))]
    from genesis.art4 import clay_lamp
    o.append(clay_lamp(w * 0.88, h * 0.4, min(1.2, h / 260)))
    return "".join(o)

# ---- 1 Samuel 30–31 -----------------------------------------------------------------------------------------------------
def tamarisk_alone(w, h, seed):
    """The tamarisk-tree in Jabesh at evening, where the men of Jabesh buried the bones and fasted seven days (no grave drawn)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A4A"></rect>', sun(w * 0.76, h * 0.56, 30, color="#FF8A3D", op=0.4),
         hills(w, h, h * 0.62, seed, color="#2A1E30", amp=18), ground(w, h, h * 0.74, "#1E1424", dy=0),
         S4.great_oak(w * 0.36, h * 0.86, min(1.4, h / 300), seed, dark=True)]
    return "".join(o)
