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
