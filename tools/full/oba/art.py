"""Drawings for the Obadiah volume, on the minor prophets' kit (oba.minor): Edom's red rock with its dwellings cut in the
cliff, the eagle's nest among the stars, the vineyard gleaned by night, the border road and the snare, Jerusalem's smoke
seen from the other side, the empty crossway, the cup on the holy mountain, the stubble burning, and the map of the land
possessed."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from oba.minor import *

def clefts(w, h, seed, nest=True):
    """Thou that dwellest in the clefts of the rock: the red cliff of Edom by night, an eagle's nest on its highest point
    among the stars."""
    o = [sky(w, h, "#05051A", "#2A1A4A"), starfield(w, h, seed, 90, 0.9), hills(w, h, h * 0.8, seed, color="#1A1030", amp=12),
         crag(w * 0.12, w * 0.92, h * 1.02, h * 0.22, seed, color="#8A3A2A", dark="#4A1A12", doors=5)]
    if nest:
        x, y = w * 0.5, h * 0.24
        o.append(f'<path d="M{f(x - 34)} {f(y)} C {f(x - 20)} {f(y + 12)} {f(x + 20)} {f(y + 12)} {f(x + 34)} {f(y)} L {f(x + 26)} {f(y - 8)} L {f(x - 26)} {f(y - 8)} Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.8"></path>'
                 + "".join(f'<path d="M{f(x - 30 + k * 10)} {f(y - 6)} l {f(14 - k * 3)} {f(-6 + k % 3 * 4)}" stroke="#8A6A3A" stroke-width="1.6"></path>' for k in range(7)))
        o.append(eagle(w * 0.72, h * 0.16, min(0.9, h / 360), color="#3A2414"))
    return "".join(o)

def gleaning(w, h, seed):
    """Robbers by night and grape-gatherers: a moonlit vineyard stripped, a few gleaning clusters left on the vines, and the
    doors of the rock-houses standing open."""
    o = [sky(w, h, "#05051A", "#1E1A4A"), J.moon(w * 0.82, h * 0.16, max(12, h * 0.05)), starfield(w, h, seed, 40, 0.4),
         crag(w * 0.46, w * 1.04, h * 0.66, h * 0.12, seed, color="#6A2E22", dark="#3A140E", doors=3),
         ground(w, h, h * 0.62, "#1A1428", dy=0), vines(w * 0.04, w * 0.96, h * 0.74, h * 0.96, seed, rows=3, fruit=False)]
    r = random.Random(seed)
    for _ in range(3):
        x, y = r.uniform(w * 0.1, w * 0.9), h * r.uniform(0.82, 0.92)
        o.append("".join(f'<circle cx="{f(x + dx)}" cy="{f(y + dy)}" r="3.6" fill="#7A2A7A" stroke="#0D0D0F" stroke-width="0.8"></circle>' for dx, dy in ((0, 0), (5, 2), (-4, 4), (1, 7))))
    return "".join(o)

def border_snare(p, w, h, seed):
    """The men of thy confederacy brought thee on thy way, even to the border: a road to a border stone, the allies turning
    back, bread on a cloth and a snare laid under it."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE6A0", "#E8A070"), hills(w, h, h * 0.5, seed, color="#A8704A", amp=16), ground(w, h, h * 0.56, "#C8985A", dy=0),
         f'<path d="M{f(w * 0.42)} {f(h * 0.56)} L {f(w * 0.48)} {f(h * 0.56)} L {f(w * 0.9)} {f(h + 10)} L {f(w * 0.1)} {f(h + 10)} Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.6"></path>',
         f'<path d="M{f(w * 0.56)} {f(h * 0.6)} L {f(w * 0.56)} {f(h * 0.5)} Q {f(w * 0.58)} {f(h * 0.46)} {f(w * 0.6)} {f(h * 0.5)} L {f(w * 0.6)} {f(h * 0.6)} Z" fill="#B8A890" stroke="#0D0D0F" stroke-width="1.8"></path>',
         label(w * 0.58, h * 0.44, "BORDER", "#3A2214", 9)]
    s = fit(b, h * 0.42)
    for i, (x, c) in enumerate(((0.12, "#5A3A6A"), (0.22, "#2A5A6A"))):
        o.append(man(p, w * x, b - i * 6, s * 0.8, c, flip=True))
    cx, cy = w * 0.7, b - h * 0.02
    o.append(f'<path d="M{f(cx - 60)} {f(cy)} C {f(cx - 30)} {f(cy - 16)} {f(cx + 30)} {f(cy - 16)} {f(cx + 60)} {f(cy)} Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.8"></path>'
             + "".join(f'<ellipse cx="{f(cx + dx)}" cy="{f(cy - 12)}" rx="14" ry="7" fill="#C8904A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>' for dx in (-22, 4, 28))
             + "".join(f'<path d="M{f(cx - 70 + k * 14)} {f(cy + 4)} L {f(cx - 60 + k * 14)} {f(cy + 22)}" stroke="#3A2A1A" stroke-width="1.4"></path>' for k in range(11))
             + f'<path d="M{f(cx - 74)} {f(cy + 12)} L {f(cx + 80)} {f(cy + 12)}" stroke="#3A2A1A" stroke-width="1.4"></path>')
    return "".join(o)

def teman(w, h, seed):
    """Thy mighty men, O Teman, shall be dismayed: the mount of Esau at dusk, spears and shields thrown down on the slope."""
    o = [vista(w, h, seed, tone="dusk", far="crag", cx=0.55, cw=0.8, hills_n=1, horizon=0.66)]
    r = random.Random(seed)
    for i in range(5):
        x, y = w * (0.1 + i * 0.19), h * r.uniform(0.82, 0.94); a = r.randint(-30, 30)
        o.append(f'<g transform="rotate({a} {f(x)} {f(y)})"><path d="M{f(x - 50)} {f(y)} L {f(x + 50)} {f(y)}" stroke="#5A3A22" stroke-width="4"></path>'
                 f'<path d="M{f(x + 50)} {f(y - 5)} L {f(x + 64)} {f(y)} L {f(x + 50)} {f(y + 5)} Z" fill="#B8B8C0" stroke="#0D0D0F" stroke-width="1"></path></g>'
                 f'<ellipse cx="{f(x + 20)}" cy="{f(y + 8)}" rx="16" ry="7" fill="#9A7A3A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    return "".join(o)

def other_side(p, w, h, seed):
    """In the day that thou stoodest on the other side: Jerusalem's smoke across the valley, dark figures on the near ridge
    looking on (no one harmed is drawn)."""
    o = [sky(w, h, "#3A1A1A", "#C8602A"), walls(w * 0.3, w * 0.95, h * 0.5, h * 0.24, seed, color="#8A6A5A", towers=3),
         fires(w * 0.32, w * 0.94, h * 0.42, h * 0.16, seed, n=4), smokes([w * 0.4, w * 0.6, w * 0.8], h * 0.3, seed, k=max(0.6, h / 360), color="#2A1A1E"),
         hills(w, h, h * 0.62, seed, color="#3A2420", amp=10), mk.defs(p, *ALL),
         f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.72)} {f(w * 0.6)} {f(h * 0.74)} {f(w + 10)} {f(h * 0.82)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1A0E0C" stroke="#0D0D0F" stroke-width="2"></path>']
    b = h * 0.86
    for i in range(4):
        o.append(mk.person(p, round(w * (0.08 + i * 0.07)), round(b - i * 3), round(fit(b, h * 0.52), 3), body="#0D0D0F", cloth="#1A0E0C", sw=2, flip=False))
    return "".join(o)

def crossway(w, h, seed):
    """Stand thou not in the crossway: two roads crossing on an empty plain at dusk, the city far off."""
    o = [sky(w, h, "#2A1A3A", "#E8803A"), walls(w * 0.62, w * 0.9, h * 0.44, h * 0.14, seed, color="#6A4A4A", towers=2),
         smokes([w * 0.7, w * 0.82], h * 0.34, seed, k=0.5, color="#3A2A2E"), ground(w, h, h * 0.44, "#5A3A2E", dy=0),
         f'<path d="M{f(w * 0.48)} {f(h * 0.44)} L {f(w * 0.52)} {f(h * 0.44)} L {f(w * 0.72)} {f(h + 10)} L {f(w * 0.28)} {f(h + 10)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.6"></path>',
         f'<path d="M-10 {f(h * 0.66)} L {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.74)} L -10 {f(h * 0.8)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.6"></path>',
         f'<path d="M{f(w * 0.36)} {f(h * 0.86)} l 22 -10 l 18 8 l -16 10 Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="1.6"></path>']
    return "".join(o)

def cup_mount(w, h, seed):
    """As ye have drunk upon my holy mountain: the cup on the dark mountain, the nations' lights far off below."""
    o = [vista(w, h, seed, tone="red", far="zion", cx=0.28, cw=0.5, hills_n=1, horizon=0.7, stars=True), cup(w * 0.72, h * 0.9, min(1.4, h / 220), spill=True)]
    return "".join(o)

def stubble(w, h, seed):
    """The house of Jacob a fire, the house of Joseph a flame, the house of Esau for stubble: a field of stubble burning
    under the red rock."""
    o = [sky(w, h, "#1A0A0A", "#8A2A1A"), crag(w * 0.4, w * 1.05, h * 0.62, h * 0.14, seed, color="#6A2A1E", dark="#3A120A", doors=3),
         ground(w, h, h * 0.6, "#3A1E14", dy=0), grain(-10, w + 10, h * 0.98, h * 0.12, seed, color="#C8A060"),
         fires(-10, w * 0.7, h * 0.96, h * 0.34, seed, n=6), smokes([w * 0.2, w * 0.45, w * 0.65], h * 0.6, seed, k=max(0.6, h / 360), color="#2A1A1E")]
    return "".join(o)

def possess_map(w, h, lit=()):
    """And they of the South shall possess the mount of Esau …: a technical map of the land and who shall possess it."""
    o = [grid_bg(w, h, color="#1E3A5A", step=28, bg="#0B1A2E")]
    sea_x = w * 0.24
    o.append(f'<path d="M-10 -10 L {f(sea_x)} -10 C {f(sea_x - 20)} {f(h * 0.3)} {f(sea_x - 40)} {f(h * 0.6)} {f(sea_x - 70)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#12385A" stroke="#8FD0E2" stroke-width="1.6"></path>')
    o.append(label(sea_x * 0.4, h * 0.5, "THE SEA", "#8FD0E2", 10))
    jx = w * 0.56
    o.append(f'<path d="M{f(jx)} {f(h * 0.12)} C {f(jx + 6)} {f(h * 0.3)} {f(jx - 6)} {f(h * 0.4)} {f(jx)} {f(h * 0.52)}" stroke="#8FD0E2" stroke-width="2.4" fill="none"></path>'
             f'<ellipse cx="{f(jx)}" cy="{f(h * 0.64)}" rx="{f(w * 0.025)}" ry="{f(h * 0.11)}" fill="#12385A" stroke="#8FD0E2" stroke-width="1.6"></ellipse>')
    pts = [("ZAREPHATH", 0.3, 0.1, "start"), ("SAMARIA", 0.38, 0.26, "end"), ("EPHRAIM", 0.4, 0.4, "end"), ("GILEAD", 0.72, 0.34, "start"), ("BENJAMIN", 0.42, 0.52, "end"),
           ("ZION", 0.47, 0.62, "start"), ("PHILISTINES", 0.24, 0.72, "end"), ("THE SOUTH", 0.4, 0.88, "end"), ("MOUNT OF ESAU", 0.62, 0.8, "start")]
    for name, x, y, an in pts:
        c = "#FFD23F" if name in lit else "#8FD0E2"
        o.append(node(w * x, h * y, "", color=c, r=5) + label(w * x + (12 if an == "start" else -12), h * y + 4, name, c, 10, anchor=an))
    o += [route([(w * 0.42, h * 0.86), (w * 0.59, h * 0.81)], color="#FF8A6A"), route([(w * 0.44, h * 0.6), (w * 0.27, h * 0.7)], color="#FF8A6A"),
          route([(w * 0.44, h * 0.5), (w * 0.69, h * 0.36)], color="#FF8A6A"), route([(w * 0.37, h * 0.24), (w * 0.31, h * 0.13)], color="#FF8A6A"),
          label(w * 0.86, h * 0.12, "SEPHARAD →", "#FFD23F", 10)]
    return "".join(o)

def kingdom(w, h, seed):
    """And the kingdom shall be Jehovah's: mount Zion at sunrise, the light breaking over it."""
    o = [sky(w, h, "#2A2A5A", "#FFB07A"), halo(w * 0.5, h * 0.4, max(w, h) * 0.4, "#FFE680", 0.5), rays(w * 0.5, h * 0.4, 24, h * 0.12, max(w, h), "#FFF4C2", 0.25, 4),
         hills(w, h, h * 0.66, seed, color="#5A3A4A", amp=14), mount_zion(w * 0.5, h * 0.98, w * 0.34, h * 0.5, seed, color="#7A5A4A")]
    return "".join(o)

def ambassador(p, w, h, seed):
    """An ambassador sent among the nations: a rider going out on the road past the cities of the nations."""
    from est.art import rider
    b = h * 0.94
    o = [mk.defs(p, *ALL), vista(w, h, seed, tone="dawn", horizon=0.56, hills_n=2), walls(w * 0.62, w * 0.9, h * 0.6, h * 0.14, seed, towers=2),
         walls(w * 0.04, w * 0.24, h * 0.58, h * 0.1, seed + 1, towers=1)]
    o.append(rider(p, w * 0.42, b, min(0.9, h / 380), "#2A5A6A"))
    return "".join(o)
