"""Drawings for Deuteronomy chapter 15 (Deuteronomy 33–34): the land that Moses saw from the top of Pisgah as a technical
map, the valley in the land of Moab over against Beth-peor (no grave is drawn: no man knoweth of his sepulchre), and
Israel weeping for Moses in the plains of Moab."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import exodus as E
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, grid_bg, node
from num.art import TRIBE_C

def f(v): return f"{v:.1f}"

def nebo_map(w, h):
    """All the land: Gilead unto Dan, Naphtali, Ephraim and Manasseh, Judah unto the hinder sea, the South, the Plain of
    the valley of Jericho unto Zoar; the sight lines run out from mount Nebo across the Jordan."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.12)} -10 C {f(w * 0.1)} {f(h * 0.3)} {f(w * 0.06)} {f(h * 0.7)} {f(w * 0.02)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(label(w * 0.05, h * 0.5, "THE HINDER SEA", "#8FD0E2", 8, ls=0.1).replace("<text ", f'<text transform="rotate(-90 {f(w * 0.05)} {f(h * 0.5)})" '))
    regions = [("NAPHTALI", 0.36, 0.08, 0.6, 0.24, "NAPHTALI"), ("MANASSEH", 0.24, 0.26, 0.6, 0.38, "MANASSEH"), ("EPHRAIM", 0.24, 0.4, 0.6, 0.5, "EPHRAIM"),
               ("JUDAH", 0.2, 0.52, 0.62, 0.78, "JUDAH"), ("THE SOUTH", 0.16, 0.8, 0.66, 0.96, "SIMEON"), ("GILEAD", 0.68, 0.2, 0.96, 0.46, "GAD")]
    for nm, x0, y0, x1, y1, t in regions:
        c = TRIBE_C[t]
        o.append(f'<rect x="{f(w * x0)}" y="{f(h * y0)}" width="{f(w * (x1 - x0))}" height="{f(h * (y1 - y0))}" fill="{c}" opacity="0.45" stroke="{c}" stroke-width="2"></rect>'
                 + label(w * x0 + 8, h * y0 + 15, nm, "#F3EFE6", 9, "start", ls=0.1))
    o.append(f'<ellipse cx="{f(w * 0.63)}" cy="{f(h * 0.2)}" rx="{f(w * 0.018)}" ry="{f(h * 0.04)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>')
    o.append(f'<path d="M{f(w * 0.63)} {f(h * 0.24)} C {f(w * 0.61)} {f(h * 0.34)} {f(w * 0.66)} {f(h * 0.44)} {f(w * 0.645)} {f(h * 0.56)}" fill="none" stroke="#8FD0E2" stroke-width="3"></path>'
             + label(w * 0.665, h * 0.48, "JORDAN", "#8FD0E2", 8, "start"))
    o.append(f'<ellipse cx="{f(w * 0.65)}" cy="{f(h * 0.66)}" rx="{f(w * 0.03)}" ry="{f(h * 0.1)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>')
    nx, ny = w * 0.78, h * 0.56
    for tx, ty in ((0.62, 0.05), (0.08, 0.3), (0.06, 0.62), (0.4, 0.92), (0.63, 0.84)):
        o.append(f'<path d="M{f(nx)} {f(ny)} L {f(w * tx)} {f(h * ty)}" stroke="#FFD23F" stroke-width="1.6" stroke-dasharray="5 6" opacity="0.8"></path>')
    o.append(node(w * 0.62, h * 0.05, "DAN", "#FFD23F", r=4, dy=18, size=8))
    o.append(node(w * 0.6, h * 0.53, "JERICHO", "#F3EFE6", r=4, dy=-9, size=8, anchor="end"))
    o.append(node(w * 0.63, h * 0.84, "ZOAR", "#F3EFE6", r=4, dy=-9, size=8))
    o.append(node(nx, ny, "MOUNT NEBO · PISGAH", "#FFD23F", r=6, dy=22, size=9))
    return "".join(o)

def beth_peor(w, h, seed):
    """The valley in the land of Moab over against Beth-peor at evening: the hills, the empty valley floor, the town far off."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A4A"></rect>', sun(w * 0.24, h * 0.36, 26, color="#FF8A3D", op=0.4),
         hills(w, h, h * 0.42, seed, color="#5A3A4A", amp=26, step=90), hills(w, h, h * 0.5, seed + 1, color="#4A2E3A", amp=18)]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.56)} C {f(w * 0.2)} {f(h * 0.62)} {f(w * 0.36)} {f(h * 0.82)} {f(w * 0.5)} {f(h * 0.84)} '
             f'C {f(w * 0.64)} {f(h * 0.82)} {f(w * 0.8)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.56)} L {f(w + 10)} {f(h + 10)} Z" fill="#2A1E2A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    bx = w * 0.8
    for i in range(6):
        x = bx + (i - 3) * w * 0.018; hh = h * r.uniform(0.025, 0.045)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.5 - hh)}" width="{f(w * 0.016)}" height="{f(hh)}" fill="#6A4A5A" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    o.append(label(bx, h * 0.5 + 16, "BETH-PEOR", "#F3D8A0", 8))
    for i in range(30):
        o.append(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(0, h * 0.3))}" r="1.2" fill="#F3EFE6" opacity="{r.uniform(0.3, 0.8):.2f}"></circle>')
    return "".join(o)

def weeping(w, h, seed):
    """The children of Israel wept for Moses in the plains of Moab thirty days: the camp, people bowed in dark robes."""
    r = random.Random(seed); b = h * 0.92
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A3450"></rect>', hills(w, h, h * 0.4, seed, color="#4A4460", amp=14),
         f'<path d="M-10 {f(h * 0.46)} C {f(w * 0.3)} {f(h * 0.44)} {f(w * 0.6)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.46)}" fill="none" stroke="#5A8AA8" stroke-width="5"></path>',
         ground(w, h, h * 0.5, "#4A4A5A", dy=0)]
    for i in range(9):
        x = w * (0.08 + i * 0.1); y = h * 0.56
        o.append(f'<path d="M{f(x - 22)} {f(y)} L {f(x)} {f(y - 22)} L {f(x + 22)} {f(y)} Z" fill="#2A2430" stroke="#0D0D0F" stroke-width="1.6"></path>')
    for i in range(12):
        x = w * (0.05 + i * 0.08); y = b - (i % 3) * 10
        o.append(E.kneel(x, y, fit(y, h * 0.5) * 0.9, color=r.choice(["#3A3430", "#4A3A3E", "#2A2A3A", "#5A4A4E"]), skin="#6A4A3A", flip=i % 2 == 1))
    return "".join(o)
