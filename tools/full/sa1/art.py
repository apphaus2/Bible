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
