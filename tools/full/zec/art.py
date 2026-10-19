"""Drawings for the Zechariah volume, on the minor prophets' kit (oba.minor). The night visions are luminous symbolic plates
(vision(): a night field with a faint grid and stars, the drawing glowing on it, a title tag in technical type): the horses
among the myrtle-trees, the four horns and the four smiths, the man with the measuring line and the wall of fire, Joshua the
high priest, the stone with seven eyes, the candlestick of gold between two olive-trees, the flying roll, the ephah, the
four chariots between the mountains of brass. Angels are shapes of white light, no faces; the adversary (3:1) a shadow
with no face; God is never drawn. Later chapters: the king lowly riding upon an ass, the thirty pieces of silver, the
fountain opened, the day of Jehovah on the mount of Olives."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from oba.minor import *
from exo.art9 import high_priest

ZECH_C = "#3A5A6A"
GOLD, CY = "#FFD23F", "#8FD0E2"

def zech_fig(p, x, y, s, flip=False, up=None):
    """Zechariah at a distance: a slate-teal robe and headcloth, black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=ZECH_C, sw=3, flip=flip, up=up, extra=A.headcloth(ZECH_C) + BLACK_BEARD)

def vision(p, w, h, body, title=None, tags=(), bg="#070720", seed=1):
    """A vision plate: night field, faint grid, stars, the body (svg placed in panel coordinates) glowing."""
    o = [hgrad(f"{p}vg", [("0", "#0B0B2A"), ("0.6", "#1E1650"), ("1", "#2A1A4A")], vertical=True),
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{p}vg)"></rect>',
         "".join(f'<path d="M{x} 0 L {x} {f(h)}" stroke="#2A3A6A" stroke-width="0.8" opacity="0.5"></path>' for x in range(0, int(w) + 40, 40)),
         "".join(f'<path d="M0 {y} L {f(w)} {y}" stroke="#2A3A6A" stroke-width="0.8" opacity="0.5"></path>' for y in range(0, int(h) + 40, 40)),
         starfield(w, h, seed, 40, 1.0), glow(p, 4), f'<g filter="url(#{p}gl)">{body}</g>']
    if title: o.append(f'<rect x="10" y="{f(h - 30)}" width="{f(len(title) * 7.6 + 16)}" height="20" fill="#0B0B2A" stroke="{GOLD}" stroke-width="1.2"></rect>' + label(18, h - 15, title, GOLD, 10, anchor="start"))
    for x, y, t in tags: o.append(label(x, y, t, CY, 9))
    return "".join(o)

def light_fig(p, x, base, top, flip=False, up=None, color="#FFF4C2"):
    """An angel: a tall shape of white light, a gold rim, no face."""
    s = fit(base, top)
    return (halo(x, base - 110 * s, 110 * s, "#FFF4C2", 0.45)
            + mk.person(p, round(x), round(base), round(s, 3), body=color, cloth="#F3EFE6", stroke="#E8B830", sw=2.4, flip=flip, up=up))

def shadow_fig(p, x, base, top, flip=False):
    """The adversary: a dark shape with no face."""
    s = fit(base, top)
    return mk.person(p, round(x), round(base), round(s, 3), body="#0D0D0F", cloth="#1A1018", stroke="#4A2A3A", sw=2, flip=flip)

def myrtles(x0, x1, base, hh, seed):
    r = random.Random(seed); o = []
    for i in range(int((x1 - x0) / 34) + 1):
        x = x0 + i * 34 + r.uniform(-6, 6)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(base - hh * r.uniform(0.3, 0.5))}" rx="{f(hh * 0.4)}" ry="{f(hh * 0.5)}" fill="#1F5A3A" stroke="#5AC88A" stroke-width="1.4"></ellipse>')
    return "".join(o)

# ---- Zechariah 1–4 ------------------------------------------------------------------------------------------------------
def fathers(w, h, seed):
    """Your fathers, where are they? and the prophets, do they live for ever? — the old tombs in the hillside at dusk, below
    the broken walls of Jerusalem."""
    o = [sky(w, h, "#2A1A3A", "#C8805A"), ruin(w * 0.3, w + 10, h * 0.42, h * 0.2, seed, color="#8A7A6A"),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.44)} {f(w * 0.7)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.56)} L {f(w + 10)} {f(h + 10)} Z" fill="#6A5040" stroke="#0D0D0F" stroke-width="2"></path>']
    for i in range(5):
        x, y = w * (0.1 + i * 0.19), h * (0.72 + (i % 2) * 0.1)
        o.append(f'<path d="M{f(x - 20)} {f(y + 24)} L {f(x - 20)} {f(y)} Q {f(x)} {f(y - 22)} {f(x + 20)} {f(y)} L {f(x + 20)} {f(y + 24)} Z" fill="#1A100C" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<circle cx="{f(x + 30)}" cy="{f(y + 16)}" r="14" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    return "".join(o)

def myrtle_horses(p, w, h, seed, rider=True, report=False):
    """A man riding upon a red horse among the myrtle-trees in the bottom, and behind him horses, red, sorrel, and white."""
    b = h * 0.86
    body = [f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.9)} {f(w * 0.7)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.62)}" stroke="{CY}" stroke-width="1.6" fill="none" stroke-dasharray="6 5"></path>',
            myrtles(w * 0.05, w * 0.95, h * 0.94, h * 0.2, seed)]
    k = min(0.9, h / 300)
    cols = [("#C8302A", 0.3), ("#C8682E", 0.52), ("#C8302A", 0.68), ("#F3EFE6", 0.84)]
    for i, (c, x) in enumerate(cols):
        body.append(E3.horse(w * x, b, k * (1.0 if i == 0 else 0.8), color=c, flip=True, rim="#FFD23F"))
    if rider: body.append(mk.defs(p, *ALL) + light_fig(p, w * 0.3 + 6 * k, b - 70 * k, b - 70 * k - 120 * k))
    tags = [(w * 0.3, h * 0.2, "RED"), (w * 0.52, h * 0.28, "SORREL"), (w * 0.84, h * 0.28, "WHITE")]
    return vision(p, w, h, "".join(body), "I · THE HORSES AMONG THE MYRTLES", tags, seed=seed)

def line_jerusalem(w, h, seed):
    """My house shall be built in it, and a line shall be stretched forth over Jerusalem; my cities shall yet overflow with
    prosperity: the city on its hill at dawn, a measuring line drawn taut across it in gold."""
    o = [vista(w, h, seed, tone="dawn", far="zion", cx=0.5, cw=0.7, sun_at=(0.82, 0.3), hills_n=2, horizon=0.66)]
    o.append(f'<path d="M{f(w * 0.08)} {f(h * 0.3)} L {f(w * 0.92)} {f(h * 0.3)}" stroke="{GOLD}" stroke-width="2.4" stroke-dasharray="8 4"></path>'
             + "".join(f'<path d="M{f(w * (0.08 + i * 0.12))} {f(h * 0.27)} L {f(w * (0.08 + i * 0.12))} {f(h * 0.33)}" stroke="{GOLD}" stroke-width="2"></path>' for i in range(8)))
    return "".join(o)

def horn(x, y, s, rot=0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(s)})"><path d="M-14 0 C -20 -40 -10 -90 30 -120 C 6 -84 4 -40 14 0 Z" fill="#3A2A2A" stroke="#E86A4A" stroke-width="2.2"></path>'
            + "".join(f'<path d="M{-14 + k * 2} {-10 - k * 18} L {12 - k * 1} {-8 - k * 18}" stroke="#E86A4A" stroke-width="1.2"></path>' for k in range(5)) + '</g>')

def horns(p, w, h, seed, smiths=False):
    """Four horns — the horns which have scattered Judah, Israel, and Jerusalem; and four smiths come to cast them down."""
    k = min(1.2, h / 260)
    body = [horn(w * (0.2 + i * 0.2), h * 0.62, k, rot=(-12 + i * 8)) for i in range(4)]
    tags = [(w * (0.2 + i * 0.2), h * 0.72, t) for i, t in enumerate(("JUDAH", "ISRAEL", "JERUSALEM", "·"))][:3]
    if smiths:
        body.append(mk.defs(p, *ALL))
        for i in range(4):
            x = w * (0.12 + i * 0.25); bb = h * 0.96
            body.append(man(p, x, bb, fit(bb, h * 0.72), "#5A4A6A", up=[(22, -158), (34, -186), (40, -206)])
                        + f'<path d="M{f(x + 40 * fit(bb, h * 0.72))} {f(bb - 206 * fit(bb, h * 0.72))} l 10 -14 l 14 10 l -10 14 Z" fill="#B8B8C0" stroke="{GOLD}" stroke-width="1.4"></path>')
        body.append(mk.speed(w * 0.5, h * 0.5, 16, h * 0.1, h * 0.4, seed, color=GOLD, op=0.5))
    return vision(p, w, h, "".join(body), "II · THE FOUR HORNS AND THE FOUR SMITHS" if smiths else "II · THE FOUR HORNS", tags if not smiths else (), seed=seed)

def measuring(p, w, h, seed):
    """A man with a measuring line in his hand, going to measure Jerusalem — its breadth and its length."""
    body = [mk.defs(p, *ALL), f'<rect x="{f(w * 0.44)}" y="{f(h * 0.2)}" width="{f(w * 0.46)}" height="{f(h * 0.6)}" fill="none" stroke="{CY}" stroke-width="1.6" stroke-dasharray="6 4"></rect>',
            f'<path d="M{f(w * 0.44)} {f(h * 0.14)} L {f(w * 0.9)} {f(h * 0.14)} M{f(w * 0.96)} {f(h * 0.2)} L {f(w * 0.96)} {f(h * 0.8)}" stroke="{GOLD}" stroke-width="1.6"></path>',
            label(w * 0.67, h * 0.11, "BREADTH", GOLD, 9), f'<g transform="rotate(90 {f(w * 0.985)} {f(h * 0.5)})">{label(w * 0.985, h * 0.5, "LENGTH", GOLD, 9)}</g>',
            walls(w * 0.46, w * 0.88, h * 0.78, h * 0.36, seed, color="#3A4A6A", lit=True, towers=3)]
    b = h * 0.94
    body.append(light_fig(p, w * 0.2, b, h * 0.36, up=[(22, -158), (40, -150), (60, -146)]))
    body.append(f'<path d="M{f(w * 0.26)} {f(h * 0.6)} C {f(w * 0.32)} {f(h * 0.66)} {f(w * 0.38)} {f(h * 0.7)} {f(w * 0.44)} {f(h * 0.8)}" stroke="{GOLD}" stroke-width="2.4" fill="none"></path>')
    return vision(p, w, h, "".join(body), "III · THE MEASURING LINE", seed=seed)

def wall_fire(p, w, h, seed):
    """Jerusalem inhabited as villages without walls, for the multitude of men and cattle; I will be unto her a wall of fire
    round about, and the glory in the midst of her."""
    cx, cy, rx, ry = w * 0.5, h * 0.62, w * 0.42, h * 0.3
    r = random.Random(seed); body = []
    for i in range(14):
        a = math.radians(i * 360 / 14)
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a) * 0.9
        body.append(E.blaze(x, y + 10, w * 0.08, h * 0.16, seed + i, n=4))
    body.append(halo(cx, cy, ry * 0.8, "#FFF4C2", 0.6))
    for i in range(10):
        x, y = cx + r.uniform(-rx * 0.7, rx * 0.7), cy + r.uniform(-ry * 0.5, ry * 0.6)
        body.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(16 * min(1, h / 300))}" height="{f(12 * min(1, h / 300))}" fill="#D8C090" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    body.append(sheep_row(cx - rx * 0.5, cx + rx * 0.5, cy + ry * 0.7, 5, seed, s=min(0.4, h / 700)))
    return vision(p, w, h, "".join(body), "III · A WALL OF FIRE ROUND ABOUT", seed=seed)

def flee_north(w, h):
    """Ho, ho, flee from the land of the north; ho Zion, escape, thou that dwellest with the daughter of Babylon: the road
    home from Babylon to Zion as a technical map."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.68)} -10 C {f(w * 0.72)} {f(h * 0.4)} {f(w * 0.8)} {f(h * 0.7)} {f(w * 0.86)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>'
             f'<path d="M{f(w * 0.78)} -10 C {f(w * 0.82)} {f(h * 0.4)} {f(w * 0.9)} {f(h * 0.7)} {f(w * 0.96)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>')
    o.append(route([(w * 0.84, h * 0.7), (w * 0.62, h * 0.18), (w * 0.36, h * 0.2), (w * 0.18, h * 0.6)], color=GOLD))
    o += [node(w * 0.84, h * 0.7, "BABYLON", color="#FF8A6A"), node(w * 0.18, h * 0.6, "ZION", color=GOLD), label(w * 0.5, h * 0.12, "THE LAND OF THE NORTH", CY, 9)]
    o.append(label(w * 0.04, h * 0.94, "THE FOUR WINDS", CY, 9, anchor="start"))
    return "".join(o)

def zion_dwell(w, h, seed):
    """Sing and rejoice, O daughter of Zion; for, lo, I come, and I will dwell in the midst of thee; many nations shall join
    themselves to Jehovah: Zion in a great light, the roads of the nations coming to it. Be silent, all flesh."""
    o = [sky(w, h, "#2A2A5A", "#FFD8A0"), halo(w * 0.5, h * 0.4, max(w, h) * 0.5, "#FFF4C2", 0.6), rays(w * 0.5, h * 0.4, 30, h * 0.1, max(w, h), "#FFFFFF", 0.25, 3),
         mount_zion(w * 0.5, h * 0.92, w * 0.3, h * 0.5, seed, color="#7A6A8A", lit=True), ground(w, h, h * 0.92, "#5A4A5A", dy=0)]
    for side in (-1, 1):
        o.append(route([(w * 0.5 + side * w * 0.52, h * 0.82), (w * 0.5 + side * w * 0.3, h * 0.86)], color=GOLD, sw=3, dash="4 6"))
    return "".join(o)

def joshua_trial(p, w, h, seed, clean=False, mitre=False):
    """Joshua the high priest standing before the angel of Jehovah, the adversary a shadow at his right hand; clothed with
    filthy garments (clean=True: the filthy garments taken away; mitre=True: a clean mitre set on his head, and rich
    apparel)."""
    b = h * 0.94
    body = [mk.defs(p, *ALL), light_fig(p, w * 0.78, b, h * 0.18, flip=True, up=[(22, -158), (40, -150), (60, -146)] if clean else None)]
    s = fit(b, h * 0.26)
    if mitre: body.append(high_priest(p, w * 0.46, b, s))
    else:
        cloth = "#E8E2D6" if clean else "#5A4A30"
        body.append(mk.person(p, round(w * 0.46), round(b), round(s, 3), body=SKIN, cloth=cloth, sw=3, extra=GREY_BEARD))
        if not clean:
            r = random.Random(seed)
            body.append("".join(f'<circle cx="{f(w * 0.46 + r.uniform(-22, 22) * s)}" cy="{f(b - r.uniform(20, 140) * s)}" r="{f(r.uniform(3, 7) * s)}" fill="#2A1E10" opacity="0.8"></circle>' for _ in range(14)))
        else:
            body.append(f'<path d="M{f(w * 0.24)} {f(b)} l 40 -20 l 50 6 l 10 14 Z" fill="#5A4A30" stroke="#0D0D0F" stroke-width="1.6"></path>')
    if not clean and not mitre: body.append(shadow_fig(p, w * 0.2, b, h * 0.3))
    if mitre: body.append(halo(w * 0.46, b - 200 * s, 30 * s, "#FFF4C2", 0.6))
    return vision(p, w, h, "".join(body), "IV · JOSHUA THE HIGH PRIEST", seed=seed)

def seven_eyes(p, w, h, seed):
    """Upon one stone are seven eyes; I will engrave the graving thereof — and every man under the vine and under the
    fig-tree: a dressed stone glowing with seven eyes cut in it."""
    cx, cy = w * 0.5, h * 0.6; k = min(1.6, h / 220)
    body = [f'<path d="M{f(cx - 80 * k)} {f(cy + 40 * k)} L {f(cx - 70 * k)} {f(cy - 40 * k)} L {f(cx + 70 * k)} {f(cy - 44 * k)} L {f(cx + 84 * k)} {f(cy + 40 * k)} Z" fill="#3A3A4A" stroke="{GOLD}" stroke-width="2.4"></path>']
    for i in range(7):
        a = math.radians(-90 + i * 360 / 7)
        x, y = cx + 44 * k * math.cos(a), cy + 22 * k * math.sin(a)
        body.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(9 * k)}" ry="{f(5 * k)}" fill="#F3EFE6" stroke="{GOLD}" stroke-width="1.4"></ellipse><circle cx="{f(x)}" cy="{f(y)}" r="{f(3 * k)}" fill="#1F5FAD"></circle>')
    body.append(fig_tree(w * 0.12, h * 0.98, min(0.6, h / 400), seed=seed) + vines(w * 0.76, w * 0.98, h * 0.94, h * 0.94, seed, rows=1))
    return vision(p, w, h, "".join(body), "IV · THE STONE OF SEVEN EYES", seed=seed)

def lampstand(p, w, h, seed, trees=True, spouts=False):
    """A candlestick all of gold, with its bowl upon the top of it, and its seven lamps; seven pipes to each of the lamps;
    and two olive-trees by it, one upon the right side of the bowl, and the other upon the left (spouts=True: the two
    olive-branches emptying the golden oil through the golden spouts)."""
    k = min(1.4, h / 260); cx, base = w * 0.5, h * 0.96
    top = base - 200 * k
    body = [f'<path d="M{f(cx - 40 * k)} {f(base)} L {f(cx + 40 * k)} {f(base)} L {f(cx + 10 * k)} {f(base - 20 * k)} L {f(cx - 10 * k)} {f(base - 20 * k)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>',
            f'<rect x="{f(cx - 5 * k)}" y="{f(top)}" width="{f(10 * k)}" height="{f(180 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></rect>',
            f'<ellipse cx="{f(cx)}" cy="{f(top - 14 * k)}" rx="{f(30 * k)}" ry="{f(14 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></ellipse>']
    for i in range(7):
        x = cx + (i - 3) * 22 * k; y = top + 24 * k
        body.append(f'<path d="M{f(cx)} {f(top - 10 * k)} C {f(cx + (x - cx) * 0.4)} {f(top)} {f(x)} {f(y - 30 * k)} {f(x)} {f(y)}" stroke="#E8B830" stroke-width="1.6" fill="none"></path>'
                    f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(7 * k)}" ry="{f(4 * k)}" fill="#C8962E" stroke="#0D0D0F" stroke-width="1.2"></ellipse>'
                    + E.blaze(x, y - 2 * k, 10 * k, 18 * k, seed + i, n=3))
    if trees:
        for side in (-1, 1):
            tx = cx + side * w * 0.32
            body.append(olive(tx, base, k * 0.9, seed + side))
            if spouts:
                body.append(f'<path d="M{f(tx - side * 20 * k)} {f(base - 120 * k)} C {f(tx - side * 60 * k)} {f(base - 150 * k)} {f(cx + side * 40 * k)} {f(top - 30 * k)} {f(cx + side * 26 * k)} {f(top - 16 * k)}" stroke="#FFD23F" stroke-width="{f(4 * k)}" fill="none"></path>')
    tags = [(cx - w * 0.32, base - 150 * k, "OLIVE"), (cx + w * 0.32, base - 150 * k, "OLIVE"), (cx, top - 34 * k, "THE BOWL")] if trees else ()
    return vision(p, w, h, "".join(body), "V · THE CANDLESTICK AND THE TWO OLIVE-TREES", tags, seed=seed)

def mountain_plain(w, h, seed):
    """Who art thou, O great mountain? before Zerubbabel thou shalt become a plain; he shall bring forth the top stone with
    shoutings of Grace, grace: a great mountain sinking to a plain, the top stone lifted on the new house."""
    o = [sky(w, h, "#3A3A6A", "#FFD8A0"), f'<path d="M{f(w * 0.02)} {f(h * 0.78)} L {f(w * 0.24)} {f(h * 0.2)} L {f(w * 0.46)} {f(h * 0.78)} Z" fill="#6A5A7A" stroke="#0D0D0F" stroke-width="2" stroke-dasharray="6 4" opacity="0.6"></path>',
         f'<path d="M-10 {f(h * 0.78)} L {f(w * 0.6)} {f(h * 0.74)} L {f(w + 10)} {f(h * 0.78)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></path>',
         route([(w * 0.24, h * 0.3), (w * 0.24, h * 0.66)], color=GOLD, sw=3), temple_front(w * 0.72, h * 0.76, w * 0.24, seed)]
    o.append(f'<rect x="{f(w * 0.72 - 20)}" y="{f(h * 0.2)}" width="40" height="24" fill="#E8DCC8" stroke="#0D0D0F" stroke-width="2"></rect>' + halo(w * 0.72, h * 0.22, h * 0.2, "#FFF4C2", 0.6)
             + label(w * 0.72, h * 0.12, "GRACE, GRACE", GOLD, 11))
    return "".join(o)

def plummet(p, w, h, seed):
    """The hands of Zerubbabel have laid the foundation of this house; his hands shall also finish it; these seven shall
    rejoice and shall see the plummet in the hand of Zerubbabel: the foundation in courses, the plumb-line hanging from a
    raised hand, seven points of light above."""
    from ezr.art import altar_ruins
    o = [altar_ruins(p, w, h, seed, foundation=True)]
    x, y = w * 0.5, h * 0.2
    o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(h * 0.62)}" stroke="#3A2A1A" stroke-width="2"></path><path d="M{f(x - 8)} {f(h * 0.62)} L {f(x + 8)} {f(h * 0.62)} L {f(x)} {f(h * 0.7)} Z" fill="#6A6A72" stroke="#0D0D0F" stroke-width="1.4"></path>'
             f'<circle cx="{f(x)}" cy="{f(y)}" r="6" fill="#D9A27A" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    for i in range(7):
        o.append(halo(w * (0.2 + i * 0.1), h * 0.1, 10, "#FFE680", 0.9))
    return "".join(o)
