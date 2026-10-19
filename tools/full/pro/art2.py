"""Drawings for Proverbs 4–9 (chapters 2 and 3 of the volume), on top of pro.art (everything there is re-exported here)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from pro.art import *
from pro.art import f, K2, K1, EM, INK, SON_C, WIS_C, STRANGE_C, glow, son_fig, wisdom_fig, veiled, emb_art

# ---- Proverbs 4–6 ----------------------------------------------------------------------------------------------------------
def david_teaching(p, w, h, seed):
    """For I was a son unto my father: king David old, his hand toward young Solomon, Bath-sheba beside them."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A2A18"></rect>',
         "".join(f'<rect x="{f(x)}" y="-10" width="{f(w / 14 - 4)}" height="{f(h + 20)}" fill="#5A341E"></rect>' for x in [i * w / 14 for i in range(15)]),
         ground(w, h, b, "#2A1A10", dy=0), glow(w * 0.5, b - h * 0.3, h * 0.5, "#FFC14D", 0.3)]
    s = min(fit(b, h * 0.2), 1.3)
    o.append(K2.old_king(p, w * 0.4, b, s, flip=True, up=[(-22, -158), (-44, -150), (-62, -138)]))
    o.append(son_fig(p, w * 0.56, b, s * 0.78).replace(SON_C, SOL_C))
    o.append(woman(p, w * 0.7, b, s * 0.92, "#7A3A6A", flip=True))
    return "".join(o)

def runner_fig(x, y, s, cloth=SON_C, skin="#C98E66", hood=True):
    legs = f'<path d="M-6 -90 L -26 -44 L -46 -10 M6 -90 L 20 -48 L 44 -34" fill="none" stroke="{skin}" stroke-width="11" stroke-linecap="round"></path>'
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">{legs}<path d="M-24 -170 C -30 -140 -28 -110 -20 -86 L 24 -86 C 30 -110 26 -140 20 -170 C 10 -176 -14 -176 -24 -170 Z" fill="{cloth}" stroke="{INK}" stroke-width="3"></path>'
            f'<path d="M-20 -160 L -48 -128 L -66 -138 M20 -160 L 48 -134 L 66 -150" fill="none" stroke="{skin}" stroke-width="10" stroke-linecap="round"></path><circle cx="0" cy="-190" r="16" fill="{skin}" stroke="{INK}" stroke-width="2"></circle>'
            + (f'<path d="M-16 -196 C -16 -214 16 -214 16 -196 L 20 -176 L 12 -184 L -12 -184 L -20 -176 Z" fill="{cloth}" stroke="{INK}" stroke-width="2"></path>' if hood else "") + '</g>')

def run_path(p, w, h, seed):
    """When thou runnest, thou shalt not stumble: the son running on a straight road in the morning."""
    b = h * 0.92
    s = min(fit(b, h * 0.36), 1.1)
    return straight_path(w, h, seed) + runner_fig(w * 0.5, b, s)

def door_away(p, w, h, seed):
    """Come not nigh the door of her house: a shut door in a dark street at dusk, the son walking the other way."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#1A0A1A", "#8A2A3A"), ground(w, h, b, "#2A1A20", dy=0)]
    hw, hh = min(w * 0.36, h * 0.9), h * 0.66
    o.append(f'<rect x="{f(w * 0.6)}" y="{f(b - hh)}" width="{f(hw)}" height="{f(hh)}" fill="#4A2A3A" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.6 + hw * 0.3)}" y="{f(b - hh * 0.6)}" width="{f(hw * 0.3)}" height="{f(hh * 0.6)}" fill="#1A0A10" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.6 + hw * 0.7)}" y="{f(b - hh * 0.86)}" width="{f(hw * 0.14)}" height="{f(hh * 0.14)}" fill="#D7261E" opacity="0.6"></rect>')
    s = min(fit(b, h * 0.32), 1.1)
    o.append(son_fig(p, w * 0.22, b, s))
    o.append(f'<path d="M{f(w * 0.3)} {f(b - 60 * s)} l {f(-60 * s)} 0" stroke="#F3EFE6" stroke-width="3"></path><path d="M{f(w * 0.3 - 60 * s)} {f(b - 66 * s)} l {f(-12 * s)} {f(6 * s)} l {f(12 * s)} {f(6 * s)}" fill="#F3EFE6"></path>')
    return "".join(o)

def stone_well(x, y, k):
    """A stone well with its frame, rope and bucket; (x, y) = the ground under its middle."""
    def X(v): return f(x + (v - 160) * k)
    def Y(v): return f(y + (v - 104) * k)
    stones = "".join(f'<path d="M{X(a)} {Y(c)} L {X(a + 24)} {Y(c)}" stroke="#6A6058" stroke-width="1.2"></path>' for c in (82, 92) for a in range(118, 200, 30))
    return (f'<path d="M{X(120)} {Y(40)} L {X(120)} {Y(76)} M{X(200)} {Y(40)} L {X(200)} {Y(76)} M{X(114)} {Y(40)} L {X(206)} {Y(40)}" stroke="#5A3A22" stroke-width="{f(5 * k)}" fill="none"></path>'
            f'<path d="M{X(160)} {Y(40)} L {X(160)} {Y(58)}" stroke="#3A2214" stroke-width="1.6"></path><path d="M{X(152)} {Y(58)} L {X(168)} {Y(58)} L {X(166)} {Y(70)} L {X(154)} {Y(70)} Z" fill="#8A5A30" stroke="{INK}" stroke-width="1.6"></path>'
            f'<path d="M{X(112)} {Y(74)} L {X(112)} {Y(102)} C {X(130)} {Y(108)} {X(190)} {Y(108)} {X(208)} {Y(102)} L {X(208)} {Y(74)} Z" fill="#A89E92" stroke="{INK}" stroke-width="2"></path>' + stones
            + f'<ellipse cx="{X(160)}" cy="{Y(74)}" rx="{f(48 * k)}" ry="{f(8 * k)}" fill="#1F6F9A" stroke="{INK}" stroke-width="2"></ellipse><ellipse cx="{X(160)}" cy="{Y(74)}" rx="{f(38 * k)}" ry="{f(5 * k)}" fill="#2C9DB8"></ellipse>')

def well_home(p, w, h, seed):
    """Drink waters out of thine own cistern, and running waters out of thine own well: a well in the court of a house."""
    b = h * 0.9
    k = min(1.6, h / 130)
    return "".join([sky(w, h, "#8FD0E2", "#FFE3B8"), ground(w, h, b, "#C8A06A", dy=0), EM.house(w * 0.72, b, min(w * 0.4, h * 0.9), h * 0.56), stone_well(w * 0.3, b, k)])

def deer(x, y, s, flip=False, color="#B8763A"):
    """A hind (no antlers): slender legs, long neck, large ears; (x, y) = the ground under her."""
    sx = -s if flip else s
    body = ("M-50 -50 C -50 -64 -20 -68 20 -66 L 34 -96 C 38 -104 48 -108 54 -100 L 62 -92 L 58 -86 L 46 -88 L 36 -60 C 30 -50 20 -46 12 -46 "
            "L 16 0 L 10 0 L 2 -44 L -30 -44 L -34 0 L -40 0 L -42 -44 C -48 -46 -52 -48 -50 -50 Z")
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})"><path d="{body}" fill="{color}" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"></path>'
            f'<path d="M42 -102 L 40 -116 L 48 -104 Z" fill="{color}" stroke="{INK}" stroke-width="1.6"></path><circle cx="50" cy="-98" r="2" fill="{INK}"></circle>'
            f'<path d="M-50 -52 C -56 -54 -58 -60 -54 -62" fill="none" stroke="{INK}" stroke-width="2"></path></g>')

def hinds_fountain(w, h, seed):
    """Let thy fountain be blessed: a spring among the rocks, a hind and a doe beside it."""
    b = h * 0.9
    k = min(1.6, h / 160)
    o = [sky(w, h, "#8FD0E2", "#E8F6FA"), hills(w, h, h * 0.5, seed, "#6A9A4A", amp=10, step=80), ground(w, h, h * 0.62, "#9CCB5E", dy=0),
         EM.E4rock(w * 0.5, b - 20 * k, 200 * k, 110 * k)]
    d = f'M{f(w * 0.52)} {f(b - 100 * k)} C {f(w * 0.56)} {f(b - 80 * k)} {f(w * 0.57)} {f(b - 50 * k)} {f(w * 0.58)} {f(b - 16 * k)}'
    o.append(f'<path d="{d}" fill="none" stroke="#E8F6FA" stroke-width="{f(9 * k)}" stroke-linecap="round"></path><path d="{d}" fill="none" stroke="#2C9DB8" stroke-width="{f(4 * k)}" stroke-linecap="round"></path>'
             f'<ellipse cx="{f(w * 0.56)}" cy="{f(b - 6 * k)}" rx="{f(90 * k)}" ry="{f(12 * k)}" fill="#2C9DB8" stroke="{INK}" stroke-width="2"></ellipse>')
    o.append(deer(w * 0.28, b, k * 0.9) + deer(w * 0.82, b, k * 0.8, flip=True, color="#C8864A"))
    return "".join(o)

def handshake(p, w, h, seed):
    """If thou hast stricken thy hands for a stranger: two men at the gate striking hands."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE3B8", "#E8C88A"), ground(w, h, b, "#C8A06A", dy=0), S4.gatehouse(w * 0.8, b, min(w * 0.36, h * 0.9), h * 0.7)]
    s = min(fit(b, h * 0.3), 1.1)
    o.append(son_fig(p, w * 0.32, b, s, flip=True, up=[(-22, -158), (-46, -132), (-64, -128)]))
    o.append(man(p, w * 0.46, b, s, "#6A2A2A", up=[(-22, -158), (-46, -132), (-64, -128)]))
    return "".join(o)

def roe_flee(w, h, seed):
    """Deliver thyself as a roe from the hand of the hunter, and as a bird from the hand of the fowler."""
    b = h * 0.9
    k = min(1.4, h / 150)
    o = [sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.55, seed, "#8A9A6A", amp=8, step=80), ground(w, h, h * 0.66, "#B8A070", dy=0),
         f'<g transform="rotate(-12 {f(w * 0.4)} {f(b)})">' + deer(w * 0.4, b - 10 * k, k) + '</g>',
         "".join(f'<path d="M{f(w * 0.4 - 80 * k - i * 24)} {f(b - (50 + i * 10) * k)} l -40 0" stroke="#0D0D0F" stroke-width="2"></path>' for i in range(3)),
         EM.E4quail(w * 0.76, h * 0.26).replace("scale(0.8", f"scale({f(k)}")]
    nw = 120 * k
    for i in range(7):
        x = w * 0.7 + i * nw / 6
        o.append(f'<path d="M{f(x)} {f(b)} L {f(x + nw / 6)} {f(b - 30 * k)} M{f(x + nw / 6)} {f(b)} L {f(x)} {f(b - 30 * k)}" stroke="#5A4A3A" stroke-width="1.4"></path>')
    return "".join(o)

def ant_fig(x, y, s, grain=True):
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})" stroke="{INK}" stroke-width="2">'
            '<path d="M-14 -6 L -26 6 M-14 -6 L -20 8 M0 -6 L 0 8 M0 -6 L 6 8 M10 -6 L 22 6 M10 -6 L 16 8" fill="none" stroke-width="2.4"></path>'
            '<ellipse cx="-22" cy="-10" rx="13" ry="9" fill="#3A1A10"></ellipse><ellipse cx="0" cy="-10" rx="7" ry="5" fill="#3A1A10"></ellipse><circle cx="16" cy="-12" r="7" fill="#3A1A10"></circle>'
            '<path d="M20 -18 C 26 -30 34 -30 36 -24 M18 -18 C 20 -32 28 -36 32 -34" fill="none" stroke-width="1.6"></path>'
            + ('<ellipse cx="28" cy="-6" rx="7" ry="4" fill="#E8C060" stroke-width="1.4"></ellipse>' if grain else "") + "</g>")

def ant_hill(w, h, seed):
    """Go to the ant, thou sluggard: ants carrying grain from the harvest field to their hole."""
    b = h * 0.86
    k = min(3.0, h / 90)
    o = [sky(w, h, "#FFE3B8", "#E8C88A"), R.field(-10, w + 10, h * 0.46, h * 0.14, seed, rows=2), ground(w, h, h * 0.52, "#C8A06A", dy=0),
         f'<ellipse cx="{f(w * 0.84)}" cy="{f(b + 4)}" rx="{f(40 * k)}" ry="{f(10 * k)}" fill="#A8885A" stroke="{INK}" stroke-width="2"></ellipse><ellipse cx="{f(w * 0.84)}" cy="{f(b)}" rx="{f(9 * k)}" ry="{f(4 * k)}" fill="#2A1A10"></ellipse>',
         ant_fig(w * 0.44, b, k)]
    for i in range(7):
        o.append(ant_fig(w * (0.06 + i * 0.05), b + 6 - (i % 2) * 4, k * 0.3) + ant_fig(w * (0.6 + i * 0.03), b + 4, k * 0.26, grain=i % 2 == 0))
    return "".join(o)

def sluggard_bed(p, w, h, seed):
    """How long wilt thou sleep, O sluggard? Asleep in the day, the field gone to weeds outside the window, and poverty
    like an armed man coming up the road."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#6A4A3A"></rect>', ground(w, h, b, "#3A2A1E", dy=0)]
    wx, ww, wh, wy = w * 0.58, min(w * 0.36, h * 0.9), h * 0.5, h * 0.12
    o.append(f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}" fill="#FFE3B8" stroke="{INK}" stroke-width="2.4"></rect>')
    o.append("".join(f'<path d="M{f(wx + 10 + i * ww / 9)} {f(wy + wh)} l {f((i % 3 - 1) * 6)} {f(-wh * 0.3)}" stroke="#4A3A22" stroke-width="2.4"></path>' for i in range(9)))
    s = min(fit(wy + wh, wy + wh * 0.3), 0.6)
    o.append(warrior(p, wx + ww * 0.7, wy + wh - 2, s, WAR[0]))
    o.append(K1.bed(w, h, w * 0.06, w * 0.5, b, cover="#5A4A2A", head="#C98E66", hair="#2A1A10"))
    o.append("".join(f'<text x="{f(w * 0.08 + i * 18)}" y="{f(b - h * 0.42 - i * 16)}" font-family="Anton, sans-serif" font-size="{14 + i * 4}" fill="#FFE680">Z</text>' for i in range(3)))
    return "".join(o)

SEVEN_SIGNS = [
    '<path d="M-20 0 C -10 -12 10 -12 20 0 C 10 12 -10 12 -20 0 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></path><circle cx="2" cy="0" r="6" fill="#2A1A10"></circle><path d="M-22 -12 L 20 -18" stroke="#F3EFE6" stroke-width="3"></path>',
    '<path d="M-16 -8 C -4 -14 10 -10 18 -2 C 10 6 -4 8 -16 4 Z" fill="#C8465A" stroke="#0D0D0F" stroke-width="2"></path><path d="M-18 -2 L -24 -10 M-18 2 L -24 8" stroke="#9A6AC8" stroke-width="2"></path>',
    '<path d="M-18 16 L -18 -6 C -18 -14 -8 -14 -8 -6 L -8 -14 C -8 -20 2 -20 2 -14 L 2 -12 C 2 -18 12 -18 12 -12 L 12 4 C 12 14 6 18 -2 18 Z" fill="#C98E66" stroke="#0D0D0F" stroke-width="2"></path>',
    '<path d="M0 16 C -26 0 -22 -18 -10 -18 C -4 -18 0 -12 0 -10 C 0 -12 4 -18 10 -18 C 22 -18 26 0 0 16 Z" fill="#5A1A3A" stroke="#0D0D0F" stroke-width="2"></path>',
    '<path d="M-14 -16 L -6 0 L -18 14 M2 -16 L 10 0 L 20 4" fill="none" stroke="#C98E66" stroke-width="5" stroke-linecap="round"></path><path d="M-28 -6 l -8 0 M-28 4 l -10 0" stroke="#F3EFE6" stroke-width="2"></path>',
    '<path d="M-6 18 L -6 -6 L -14 -10 L -6 -10 L -6 -22 C -6 -26 2 -26 2 -22 L 2 18 Z" fill="#C98E66" stroke="#0D0D0F" stroke-width="2"></path><circle cx="-2" cy="-28" r="6" fill="#5A3A6A" stroke="#0D0D0F" stroke-width="1.4"></circle><path d="M8 -20 l 10 -4 M8 -12 l 12 0" stroke="#9A6AC8" stroke-width="2"></path>',
    '<circle cx="-12" cy="-6" r="7" fill="#C98E66" stroke="#0D0D0F" stroke-width="1.6"></circle><circle cx="12" cy="-6" r="7" fill="#C98E66" stroke="#0D0D0F" stroke-width="1.6"></circle><path d="M-20 18 L -20 4 L -4 4 L -4 18 Z M4 18 L 4 4 L 20 4 L 20 18 Z" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M-2 -18 L 2 -8 L -2 -2 L 2 8" fill="none" stroke="#D7261E" stroke-width="2.4"></path>',
]

def numbered(w, h, signs, red_last=True, bg="#14102A", line="#2A1A3A"):
    """Numbered roundels in a row on the blueprint grid, each with its small sign (for the lists of Proverbs 6 and 30)."""
    o = [grid_bg(w, h, color=line, bg=bg)]
    n = len(signs)
    r = min(h * 0.3, w / (n * 2.4))
    cy = h * 0.42
    for i, sg in enumerate(signs):
        cx = w * (i + 0.5) / n
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="#2A2458" stroke="#FFD23F" stroke-width="2"></circle>'
                 f'<text x="{f(cx)}" y="{f(cy + r + r * 0.62)}" text-anchor="middle" font-family="Anton, sans-serif" font-size="{f(r * 0.55)}" fill="{"#D7261E" if red_last and i == n - 1 else "#FFD23F"}">{i + 1}</text>'
                 f'<g transform="translate({f(cx)} {f(cy)}) scale({f(r / 30)})">{sg}</g>')
    return "".join(o)

def seven(w, h, seed):
    """Six things which Jehovah hateth, yea, seven: seven numbered roundels, each with its sign — the haughty eyes, the lying
    tongue, the hands, the heart, the running feet, the false witness, the sower of discord (no blood drawn)."""
    return numbered(w, h, SEVEN_SIGNS)

def lamp_light(w, h, seed):
    """The commandment is a lamp, and the law is light: a lamp lit in the dark."""
    return emb_art("lamp", w, h, seed, k=min(2.2, h / 130))

def coals_scene(w, h, seed):
    """Can a man take fire in his bosom, or walk upon hot coals? A fire of coals in the dark."""
    return emb_art("coals", w, h, seed, k=min(2.6, h / 110))

def thief(p, w, h, seed):
    """Men do not despise a thief, if he steal to satisfy himself when he is hungry: a lean man at night by a storehouse
    door with a loaf."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#05050A", "#1E1650"), mk.stars(30, w, h * 0.5, seed), ground(w, h, b, "#2A2430", dy=0)]
    hw, hh = min(w * 0.4, h * 0.9), h * 0.6
    o.append(f'<rect x="{f(w * 0.5)}" y="{f(b - hh)}" width="{f(hw)}" height="{f(hh)}" fill="#3A3040" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.5 + hw * 0.1)}" y="{f(b - hh * 0.62)}" width="{f(hw * 0.24)}" height="{f(hh * 0.62)}" fill="#12090A" stroke="{INK}" stroke-width="2"></rect>')
    s = min(fit(b, h * 0.3), 1.0)
    o.append(man(p, w * 0.36, b, s, "#4A4A3A", flip=True, up=[(-22, -158), (-36, -120), (-50, -110)]))
    o.append(f'<ellipse cx="{f(w * 0.36 + 52 * s)}" cy="{f(b - 112 * s)}" rx="{f(14 * s)}" ry="{f(8 * s)}" fill="#C8862E" stroke="{INK}" stroke-width="1.6"></ellipse>')
    return "".join(o)
