"""Drawings for Philippians 3–4 (chapter 2 of the volume): Paul's credentials as a plate, all things counted loss on the
balance, the runner pressing toward the goal, the straight road and its rule, the colony's arch at Philippi under the
light of heaven, Euodia and Syntyche, the peace of God keeping guard over a town by night, "whatsoever things are true" as
a plate, want and plenty, the gifts sent from Philippi on the map, Epaphroditus bringing the gift (an odor of a sweet
smell), and Cæsar's household. Built on php.art (`from php.art import *`)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from php.art import *
from php.art import f, INK, _defs
from co1.art3 import athlete
from co2.art2 import bag

# ---- Philippians 3 ------------------------------------------------------------------------------------------------------------
def _icon(kind, x, y, r):
    """A small emblem in a credentials cell, centred on (x, y), about r across."""
    k = r / 40
    if kind == "eight":                                         # the eighth day: eight lamps in a row, the last one lit
        o = []
        for i in range(8):
            xx = x - 35 * k + i * 10 * k
            o.append(clay_lamp(xx, y + 6 * k, 0.28 * k) if i == 7 else f'<ellipse cx="{f(xx)}" cy="{f(y + 6 * k)}" rx="{f(3.4 * k)}" ry="{f(2.2 * k)}" fill="#8A6A4A" stroke="{INK}" stroke-width="1"></ellipse>')
        return "".join(o) + label(x, y - 10 * k, "VIII", GOLD, 12 * k)
    if kind == "stock":                                         # the stock of Israel: a vine-stock, cut and rooted
        return (f'<path d="M{f(x)} {f(y + 20 * k)} C {f(x - 6 * k)} {f(y)} {f(x + 6 * k)} {f(y - 8 * k)} {f(x)} {f(y - 18 * k)}" stroke="#8A5A30" stroke-width="{f(5 * k)}" fill="none"></path>'
                + "".join(f'<path d="M{f(x)} {f(y + yy * k)} C {f(x + sx * 10 * k)} {f(y + (yy - 6) * k)} {f(x + sx * 18 * k)} {f(y + (yy - 4) * k)} {f(x + sx * 22 * k)} {f(y + (yy - 10) * k)}" stroke="#8A5A30" stroke-width="{f(2.4 * k)}" fill="none"></path>'
                          f'<circle cx="{f(x + sx * 22 * k)}" cy="{f(y + (yy - 10) * k)}" r="{f(4 * k)}" fill="#4A8A3A" stroke="{INK}" stroke-width="1"></circle>' for sx, yy in ((-1, 2), (1, -6), (-1, -12)))
                + f'<path d="M{f(x - 14 * k)} {f(y + 22 * k)} L {f(x + 14 * k)} {f(y + 22 * k)}" stroke="#6A4A2A" stroke-width="{f(2 * k)}"></path>')
    if kind == "wolf":                                          # Benjamin, a wolf that raveneth (Genesis 49:27): a wolf's head in profile
        return (f'<path d="M{f(x - 18 * k)} {f(y + 16 * k)} L {f(x - 16 * k)} {f(y - 6 * k)} L {f(x - 12 * k)} {f(y - 22 * k)} L {f(x - 4 * k)} {f(y - 10 * k)} L {f(x + 4 * k)} {f(y - 8 * k)} '
                f'L {f(x + 22 * k)} {f(y + 2 * k)} L {f(x + 20 * k)} {f(y + 8 * k)} L {f(x + 4 * k)} {f(y + 8 * k)} L {f(x + 2 * k)} {f(y + 18 * k)} Z" fill="#8A8A94" stroke="{INK}" stroke-width="1.6"></path>'
                f'<circle cx="{f(x + 2 * k)}" cy="{f(y - 2 * k)}" r="{f(1.8 * k)}" fill="{INK}"></circle>')
    if kind == "scroll":                                        # a Hebrew of Hebrews: the roll of the law on its two rollers
        return (f'<rect x="{f(x - 16 * k)}" y="{f(y - 14 * k)}" width="{f(32 * k)}" height="{f(28 * k)}" fill="#EADBB4" stroke="{INK}" stroke-width="1.4"></rect>'
                + "".join(f'<path d="M{f(x - 11 * k)} {f(y + (j * 6 - 8) * k)} L {f(x + 11 * k)} {f(y + (j * 6 - 8) * k)}" stroke="#4A3020" stroke-width="1.4"></path>' for j in range(4))
                + "".join(f'<rect x="{f(x + sx * 18 * k - 3 * k)}" y="{f(y - 20 * k)}" width="{f(6 * k)}" height="{f(40 * k)}" rx="{f(2 * k)}" fill="#6A3A1E" stroke="{INK}" stroke-width="1.2"></rect>' for sx in (-1, 1)))
    if kind == "phylactery":                                    # a Pharisee: the phylactery box on its strap, the fringe
        return (f'<path d="M{f(x - 22 * k)} {f(y + 6 * k)} C {f(x - 10 * k)} {f(y - 4 * k)} {f(x + 10 * k)} {f(y - 4 * k)} {f(x + 22 * k)} {f(y + 6 * k)}" stroke="#2A1A10" stroke-width="{f(3 * k)}" fill="none"></path>'
                f'<rect x="{f(x - 8 * k)}" y="{f(y - 16 * k)}" width="{f(16 * k)}" height="{f(14 * k)}" fill="#1A1210" stroke="#E8B830" stroke-width="1.2"></rect>'
                + "".join(f'<path d="M{f(x + (i * 6 - 9) * k)} {f(y + 10 * k)} L {f(x + (i * 6 - 9) * k)} {f(y + 22 * k)}" stroke="#E8E2D6" stroke-width="{f(1.6 * k)}"></path>' for i in range(4))
                + f'<path d="M{f(x - 12 * k)} {f(y + 10 * k)} L {f(x + 12 * k)} {f(y + 10 * k)}" stroke="#2A4A8A" stroke-width="{f(2.4 * k)}"></path>')
    if kind == "door":                                          # persecuting the church: a house door broken in, no one there
        return (f'<rect x="{f(x - 14 * k)}" y="{f(y - 20 * k)}" width="{f(28 * k)}" height="{f(40 * k)}" fill="#1A1210" stroke="{INK}" stroke-width="1.4"></rect>'
                f'<path d="M{f(x - 12 * k)} {f(y - 18 * k)} L {f(x + 6 * k)} {f(y - 12 * k)} L {f(x + 8 * k)} {f(y + 20 * k)} L {f(x - 12 * k)} {f(y + 20 * k)} Z" fill="#6A3A1E" stroke="{INK}" stroke-width="1.4" transform="rotate(-14 {f(x)} {f(y)})"></path>'
                f'<path d="M{f(x - 2 * k)} {f(y - 4 * k)} L {f(x + 4 * k)} {f(y + 2 * k)}" stroke="#D7261E" stroke-width="{f(2 * k)}"></path>')
    if kind == "level":                                         # found blameless: a mason's level, its plumb line hanging true
        return (f'<path d="M{f(x - 20 * k)} {f(y + 16 * k)} L {f(x)} {f(y - 18 * k)} L {f(x + 20 * k)} {f(y + 16 * k)} M{f(x - 13 * k)} {f(y + 4 * k)} L {f(x + 13 * k)} {f(y + 4 * k)}" stroke="#C8A060" stroke-width="{f(3.4 * k)}" fill="none" stroke-linejoin="round"></path>'
                f'<path d="M{f(x)} {f(y - 18 * k)} L {f(x)} {f(y + 10 * k)}" stroke="#F3EFE6" stroke-width="1.2"></path><circle cx="{f(x)}" cy="{f(y + 12 * k)}" r="{f(3 * k)}" fill="#8A8A94" stroke="{INK}" stroke-width="1"></circle>')
    return ""

def credentials(w, h):
    """Though I myself might have confidence even in the flesh … I yet more (3:4–6): a plate, a ledger of seven entries, each
    in its cell with its emblem — circumcised the eighth day (eight lamps, the last lit), of the stock of Israel (a vine-stock),
    of the tribe of Benjamin (a wolf, Genesis 49:27), a Hebrew of Hebrews (the roll of the law), a Pharisee (the phylactery),
    persecuting the church (a door broken in), blameless (the level and its plumb line) — and the eighth cell the sum: GAIN."""
    o = [plate_bg(w, h, "PHILIPPIANS 3:5–6 · CONFIDENCE IN THE FLESH")]
    items = [("eight", "THE EIGHTH DAY"), ("stock", "STOCK OF ISRAEL"), ("wolf", "TRIBE OF BENJAMIN"), ("scroll", "A HEBREW OF HEBREWS"),
             ("phylactery", "A PHARISEE"), ("door", "PERSECUTING THE CHURCH"), ("level", "FOUND BLAMELESS"), (None, "GAIN")]
    cols, rows_ = 4, 2
    x0, y0, x1, y1 = 14, 34, w - 14, h - 40
    cw, ch = (x1 - x0) / cols, (y1 - y0) / rows_
    for i, (kind, lab) in enumerate(items):
        cx, cy = x0 + (i % cols) * cw, y0 + (i // cols) * ch
        last = kind is None
        o.append(f'<rect x="{f(cx + 4)}" y="{f(cy + 4)}" width="{f(cw - 8)}" height="{f(ch - 8)}" fill="{"#3A3018" if last else "#10243A"}" stroke="{GOLD if last else CY}" stroke-width="1.6"></rect>')
        r = min(cw, ch) * 0.42
        if last:
            o.append(plate_label(cx + cw / 2, cy + ch / 2 + 6, "GAIN", GOLD, max(14, r * 0.5)))
        else:
            o.append(_icon(kind, cx + cw / 2, cy + ch * 0.44, r))
        o.append(plate_label(cx + cw / 2, cy + ch - 12, lab if not last else "WHAT THINGS WERE GAIN", GOLD if last else "#F3EFE6", 8.5))
    o.append(plate_label(14, h - 18, "3:7 · THESE HAVE I COUNTED LOSS FOR CHRIST", "#FF8A6A", 9, anchor="start"))
    return "".join(o)

def loss_scales(w, h):
    """I count all things to be loss for the excellency of the knowledge of Christ Jesus my Lord … and do count them but
    refuse (3:7–8): a balance on a plate — in the left pan the things that were gain (the roll, the phylactery, the purse),
    flung up and light as refuse; in the right pan, borne down, a light."""
    o = [plate_bg(w, h, "PHILIPPIANS 3:8 · I COUNT ALL THINGS TO BE LOSS")]
    k = min(w / 520, (h - 50) / 230)
    left = (_icon("scroll", -16, -8, 22) + _icon("phylactery", 16, -6, 20) + bag(0, 0, 0.5))
    right = halo(0, -16, 40, "#FFE680", 0.7) + f'<circle cx="0" cy="-16" r="12" fill="#FFFDF0"></circle>' + rays(0, -16, 14, 14, 44, "#FFF4C2", 0.6, 2)
    o.append(balance(w / 2, 50 + 30 * k, k, -16, left, right))
    o.append(plate_label(w / 2 - 110 * k * math.cos(math.radians(16)), 50 + 30 * k - 110 * k * math.sin(math.radians(16)) - 12, "LOSS · REFUSE", "#FF8A6A", 10))
    o.append(plate_label(w / 2 + 110 * k * math.cos(math.radians(16)), min(h - 46, 50 + 30 * k + 110 * k * math.sin(math.radians(16)) + 120 * k), "THAT I MAY GAIN CHRIST", GOLD, 10))
    return "".join(o)

def runner(p, w, h, seed):
    """Forgetting the things which are behind, and stretching forward to the things which are before, I press on toward
    the goal unto the prize (3:13–14): the stadium, the banks of the crowd, one runner stretched out down the track toward
    the goal-post, the judge's stand beyond it with the victor's wreath; the track behind him empty."""
    b = h * 0.92
    o = [sky(w, h, "#8FD0E2", "#F3E8C8")]
    o.append(f'<path d="M-10 {f(h * 0.18)} C {f(w * 0.3)} {f(h * 0.26)} {f(w * 0.7)} {f(h * 0.26)} {f(w + 10)} {f(h * 0.18)} L {f(w + 10)} {f(h * 0.52)} L -10 {f(h * 0.52)} Z" fill="#B8A87A" stroke="{INK}" stroke-width="2"></path>')
    r = random.Random(seed)
    for row in range(5):
        y = h * (0.28 + row * 0.048)
        for i in range(int(w / 11)):
            if r.random() < 0.78:
                o.append(f'<circle cx="{f(i * 11 + r.uniform(-3, 3))}" cy="{f(y + r.uniform(-2, 2))}" r="{f(max(2.2, h * 0.011))}" fill="{r.choice(["#3A2A2A", "#E8E2D6", "#5A3A2A", "#B5121B", "#2A3A6A"])}"></circle>')
    o.append(f'<rect x="-10" y="{f(h * 0.52)}" width="{f(w + 20)}" height="{f(h)}" fill="#E8C890" stroke="{INK}" stroke-width="2"></rect>')
    for kk in range(4):
        y = h * (0.6 + kk * 0.1)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#F3EFE6" stroke-width="2" opacity="0.8"></path>')
    gx = w * 0.86                                              # the goal-post and the judge's stand with the wreath
    o.append(f'<rect x="{f(gx - 6)}" y="{f(h * 0.3)}" width="12" height="{f(b - h * 0.3)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.8"></rect>'
             f'<rect x="{f(gx + 20)}" y="{f(h * 0.4)}" width="{f(w * 0.12)}" height="{f(h * 0.12)}" fill="#E8E2D6" stroke="{INK}" stroke-width="1.8"></rect>'
             + halo(gx + 20 + w * 0.06, h * 0.32, h * 0.12, "#FFE680", 0.6)
             + f'<circle cx="{f(gx + 20 + w * 0.06)}" cy="{f(h * 0.32)}" r="{f(max(10, h * 0.05))}" fill="none" stroke="#4A8A3A" stroke-width="{f(max(4, h * 0.022))}" stroke-dasharray="4 2"></circle>')
    s = fit(b, b - min(h * 0.66, 190))
    rx = w * 0.5
    o.append(mk.speed(rx - 70 * s, b - 100 * s, 8, 30 * s, 110 * s, seed, color="#FFFFFF", op=0.6))
    o.append(athlete(rx, b, s, pose="run_a", skin="#C98E66", cloth="#F3EFE6", hair="#2A1A10"))
    return "".join(o)

def rule_road(p, w, h, seed):
    """Whereunto we have attained, by that same rule let us walk … be ye imitators together of me (3:16–17): a Roman road
    running straight to the hills, the surveyor's cross-staff (the groma) planted at its side, and three of the brethren
    walking along it one behind another, each in the steps of the one before."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#8FD0E2", "#FFE6B0"), hills(w, h, h * 0.4, seed, color="#8A9A7A", amp=14, step=90), ground(w, h, h * 0.48, "#B8B07A", dy=0)]
    vx, hz = w * 0.3, h * 0.48
    o.append(f'<path d="M{f(vx - 6)} {f(hz)} L {f(vx + 6)} {f(hz)} L {f(w * 0.98)} {f(h + 10)} L {f(-w * 0.2)} {f(h + 10)} Z" fill="#B8A890" stroke="{INK}" stroke-width="1.6"></path>')
    for j in range(1, 9):
        t = (j / 9) ** 1.6
        y = hz + (h - hz) * t
        o.append(f'<path d="M{f(vx - 6 + (-w * 0.2 - vx + 6) * t)} {f(y)} L {f(vx + 6 + (w * 0.98 - vx - 6) * t)} {f(y)}" stroke="#9A8A72" stroke-width="1.2"></path>')
    for t in (0.3, 0.55, 0.8):                                  # the curbstones' line, straight as a rule
        o.append(f'<path d="M{f(vx)} {f(hz)} L {f(vx + (w * 0.5 - vx) * 1.0)} {f(h + 10)}" stroke="#F3EFE6" stroke-width="1.2" stroke-dasharray="6 6" opacity="0.6"></path>')
        break
    gx, gb = w * 0.86, b                                       # the groma: a staff with a cross on top and four plumb-bobs
    o.append(f'<path d="M{f(gx)} {f(gb)} L {f(gx)} {f(gb - h * 0.5)}" stroke="#5A3A1E" stroke-width="4"></path>'
             f'<path d="M{f(gx - 34)} {f(gb - h * 0.5)} L {f(gx + 34)} {f(gb - h * 0.5)} M{f(gx - 14)} {f(gb - h * 0.5 - 10)} L {f(gx + 14)} {f(gb - h * 0.5 + 10)}" stroke="#5A3A1E" stroke-width="3"></path>'
             + "".join(f'<path d="M{f(gx + dx)} {f(gb - h * 0.5)} L {f(gx + dx)} {f(gb - h * 0.34)}" stroke="#F3EFE6" stroke-width="1"></path><circle cx="{f(gx + dx)}" cy="{f(gb - h * 0.34)}" r="3" fill="#8A8A94" stroke="{INK}" stroke-width="1"></circle>' for dx in (-34, 34)))
    s = fit(b, b - min(h * 0.7, 206))
    for i, (x, sc, k) in enumerate(((0.58, 1.0, 6), (0.44, 0.86, 2), (0.34, 0.74, 0))):
        o.append(saint(p, w * x, b - (1 - sc) * h * 0.28, s * sc, k, pose="walk"))
    return "".join(o)

def colony_gate(p, w, h, seed):
    """For our citizenship is in heaven; whence also we wait for a Saviour (3:20): Philippi, a Roman colony — the arch over
    the Egnatian Way outside the city, the walls and the acropolis beyond; and over all, the sky opened in light (no one
    drawn in it), citizens of the colony in their togas passing under the arch."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#3A3A7A", "#FFD890"), halo(w * 0.5, -h * 0.05, h * 0.9, "#FFF4C2", 0.55), rays(w * 0.5, -h * 0.1, 30, h * 0.1, h * 1.3, "#FFFDF0", 0.28, 5)]
    o.append(f'<path d="M{f(w * 0.52)} {f(h * 0.54)} L {f(w * 0.66)} {f(h * 0.24)} L {f(w * 0.78)} {f(h * 0.2)} L {f(w * 1.05)} {f(h * 0.46)} L {f(w * 1.05)} {f(h * 0.56)} Z" fill="#7A6A5A" stroke="{INK}" stroke-width="2"></path>')
    from oba.minor import walls
    o.append(walls(w * 0.5, w + 10, h * 0.58, h * 0.16, seed, towers=3))
    o.append(ground(w, h, h * 0.58, "#C8B07A", dy=0))
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.58)} L {f(w * 0.4)} {f(h * 0.58)} L {f(w * 0.75)} {f(h + 10)} L {f(-w * 0.1)} {f(h + 10)} Z" fill="#B8A890" stroke="{INK}" stroke-width="1.4"></path>')
    ax, aw, at = w * 0.24, min(w * 0.36, h * 0.9), h * 0.12   # the arch
    ab = b
    o.append(f'<path d="M{f(ax - aw / 2)} {f(ab)} L {f(ax - aw / 2)} {f(at)} L {f(ax + aw / 2)} {f(at)} L {f(ax + aw / 2)} {f(ab)} L {f(ax + aw * 0.24)} {f(ab)} L {f(ax + aw * 0.24)} {f(at + aw * 0.5)} '
             f'C {f(ax + aw * 0.24)} {f(at + aw * 0.18)} {f(ax - aw * 0.24)} {f(at + aw * 0.18)} {f(ax - aw * 0.24)} {f(at + aw * 0.5)} L {f(ax - aw * 0.24)} {f(ab)} Z" fill="#E8E0CC" stroke="{INK}" stroke-width="3"></path>'
             f'<rect x="{f(ax - aw / 2 - 6)}" y="{f(at)}" width="{f(aw + 12)}" height="{f(aw * 0.08)}" fill="#D8D0BC" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(ax - aw * 0.3)}" y="{f(at + aw * 0.1)}" width="{f(aw * 0.6)}" height="{f(aw * 0.07)}" fill="#C8BCA4" stroke="{INK}" stroke-width="1.4"></rect>')
    for sx in (-1, 1):
        o.append(f'<rect x="{f(ax + sx * aw * 0.37 - aw * 0.03)}" y="{f(at + aw * 0.14)}" width="{f(aw * 0.06)}" height="{f(ab - at - aw * 0.14)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>')
    s = fit(b, b - min(h * 0.6, 170))
    o.append(toga_r(p, w * 0.58, b, s, flip=True) + toga_r(p, w * 0.7, b, s * 0.97, border="#2A4A6A", hair="#6A5A4A"))
    o.append(saint(p, w * 0.84, b, s * 0.98, 5, flip=True, up=UP_HIGH))
    return "".join(o)

# ---- Philippians 4 ------------------------------------------------------------------------------------------------------------
def euodia_syntyche(p, w, h, seed):
    """I exhort Euodia, and I exhort Syntyche, to be of the same mind in the Lord. Yea, I beseech thee also, true yokefellow,
    help these women (4:2–3): the court of the house at Philippi, Euodia (a dark-teal veil) and Syntyche (an off-white veil)
    standing a little apart, turned from each other; between them the true yokefellow with a hand held out to each; Clement
    and others of the church at the sides."""
    b = h * 0.93
    o = [_defs(p), court(w, h, b, seed, "day")]
    s = fit(b, b - min(h * 0.72, 210))
    o.append(saint(p, w * 0.08, b, s, 0, flip=True) + saint(p, w * 0.92, b, s, 2))
    o.append(euodia(p, w * 0.3, b, s) + syntyche(p, w * 0.7, b, s, flip=True))
    yoke = robed(p, w * 0.5, b, s, "#6A5A4A", head="#E8E2D6", cord="#6A5A3A", beard="#5A4A3A", up=[(-22, -158), (-46, -142), (-72, -140)])
    yoke2 = f'<g transform="translate({f(w * 0.5)} {f(b)}) scale({f(s)})"><path d="M22 -158 L 46 -142 L 72 -140" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"></path><path d="M22 -158 L 46 -142 L 72 -140" fill="none" stroke="{SKIN}" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"></path></g>'
    o.append(yoke2 + yoke)
    o.append(plate_label(w * 0.3, b - 220 * s, "EUODIA", "#F3EFE6", 10, halo_="#3A2A1A") + plate_label(w * 0.7, b - 220 * s, "SYNTYCHE", "#F3EFE6", 10, halo_="#3A2A1A"))
    return "".join(o)

def peace_guard(p, w, h, seed):
    """The peace of God, which passeth all understanding, shall guard your hearts and your thoughts in Christ Jesus (4:7): a
    walled town asleep under the stars, its gate shut, a few windows lit; on the tower the watch-fire burning and a soldier of
    the watch at his post, keeping guard."""
    o = [_defs(p), sky(w, h, "#05051A", "#2A2A5A"), mk.stars(160, w, h * 0.55, seed), mk.stars(30, w, h * 0.5, seed + 1, color="#FFE680"),
         halo(w * 0.8, h * 0.2, h * 0.16, "#FFF4C2", 0.4), f'<circle cx="{f(w * 0.8)}" cy="{f(h * 0.2)}" r="{f(h * 0.05)}" fill="#F3EFE6"></circle>',
         hills(w, h, h * 0.64, seed, color="#14142E", amp=10, step=80)]
    from oba.minor import walls
    o.append(walls(-10, w + 10, h * 0.86, h * 0.26, seed, lit=True, towers=3, color="#4A4058"))
    o.append(f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#0B0B2A" opacity="0.45"></rect>')   # the town in the dark
    tx, ty = w * 0.5, h * 0.42                                # the watch-tower, the fire and the watchman
    o.append(f'<rect x="{f(tx - w * 0.06)}" y="{f(ty)}" width="{f(w * 0.12)}" height="{f(h * 0.5)}" fill="#3A3448" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<rect x="{f(tx - w * 0.06 + i * w * 0.03)}" y="{f(ty - h * 0.03)}" width="{f(w * 0.018)}" height="{f(h * 0.03)}" fill="#3A3448" stroke="{INK}" stroke-width="1.6"></rect>' for i in range(5)))
    o.append(glow(tx + w * 0.035, ty - 10, h * 0.16, "#FF9A3D", 0.6, f"{p}wf") + E.blaze(tx + w * 0.035, ty, h * 0.05, h * 0.06, seed, n=3))
    s = (h * 0.16) / 210
    o.append(guard_r(p, tx - w * 0.025, ty, s, flip=True))
    o.append(f'<rect x="-10" y="{f(h * 0.86)}" width="{f(w + 20)}" height="{f(h)}" fill="#1A1830"></rect>')
    return "".join(o)

def _virtue(kind, x, y, r):
    k = r / 40
    if kind == "true":                                          # a plumb line hanging true against a wall
        return (f'<rect x="{f(x - 18 * k)}" y="{f(y - 24 * k)}" width="{f(12 * k)}" height="{f(48 * k)}" fill="#8A7A6A" stroke="{INK}" stroke-width="1.2"></rect>'
                f'<path d="M{f(x + 8 * k)} {f(y - 24 * k)} L {f(x + 8 * k)} {f(y + 12 * k)}" stroke="#F3EFE6" stroke-width="1.4"></path>'
                f'<path d="M{f(x + 3 * k)} {f(y + 12 * k)} L {f(x + 13 * k)} {f(y + 12 * k)} L {f(x + 8 * k)} {f(y + 24 * k)} Z" fill="#C8A060" stroke="{INK}" stroke-width="1.2"></path>')
    if kind == "honorable":                                     # a laurel wreath
        return "".join(f'<ellipse cx="{f(x + 18 * k * math.cos(math.radians(a)))}" cy="{f(y + 18 * k * math.sin(math.radians(a)))}" rx="{f(6 * k)}" ry="{f(3 * k)}" '
                       f'transform="rotate({a + 90} {f(x + 18 * k * math.cos(math.radians(a)))} {f(y + 18 * k * math.sin(math.radians(a)))})" fill="#4A8A3A" stroke="{INK}" stroke-width="1"></ellipse>'
                       for a in range(-60, 241, 22))
    if kind == "just":                                          # the balance level
        return (f'<path d="M{f(x)} {f(y - 22 * k)} L {f(x)} {f(y + 20 * k)} M{f(x - 10 * k)} {f(y + 20 * k)} L {f(x + 10 * k)} {f(y + 20 * k)} M{f(x - 24 * k)} {f(y - 14 * k)} L {f(x + 24 * k)} {f(y - 14 * k)}" stroke="#E8B830" stroke-width="{f(2.6 * k)}"></path>'
                + "".join(f'<path d="M{f(x + sx * 24 * k)} {f(y - 14 * k)} L {f(x + sx * 24 * k - 8 * k)} {f(y + 2 * k)} L {f(x + sx * 24 * k + 8 * k)} {f(y + 2 * k)} Z" fill="none" stroke="#E8B830" stroke-width="1.2"></path>'
                          f'<path d="M{f(x + sx * 24 * k - 10 * k)} {f(y + 2 * k)} C {f(x + sx * 24 * k - 8 * k)} {f(y + 10 * k)} {f(x + sx * 24 * k + 8 * k)} {f(y + 10 * k)} {f(x + sx * 24 * k + 10 * k)} {f(y + 2 * k)} Z" fill="#E8B830" stroke="{INK}" stroke-width="1"></path>' for sx in (-1, 1)))
    if kind == "pure":                                          # a white lily
        return (f'<path d="M{f(x)} {f(y + 24 * k)} L {f(x)} {f(y - 2 * k)}" stroke="#4A8A3A" stroke-width="{f(2.4 * k)}"></path>'
                + "".join(f'<path d="M{f(x)} {f(y - 2 * k)} C {f(x + sx * 4 * k)} {f(y - 14 * k)} {f(x + sx * 14 * k)} {f(y - 22 * k)} {f(x + sx * 18 * k)} {f(y - 16 * k)} C {f(x + sx * 12 * k)} {f(y - 10 * k)} {f(x + sx * 6 * k)} {f(y - 4 * k)} {f(x)} {f(y - 2 * k)} Z" fill="#FFFDF0" stroke="{INK}" stroke-width="1.2"></path>' for sx in (-1, 1))
                + f'<path d="M{f(x)} {f(y - 2 * k)} C {f(x - 5 * k)} {f(y - 16 * k)} {f(x - 3 * k)} {f(y - 24 * k)} {f(x)} {f(y - 28 * k)} C {f(x + 3 * k)} {f(y - 24 * k)} {f(x + 5 * k)} {f(y - 16 * k)} {f(x)} {f(y - 2 * k)} Z" fill="#FFFDF0" stroke="{INK}" stroke-width="1.2"></path>')
    if kind == "lovely":                                        # a rose in bloom
        return (f'<path d="M{f(x)} {f(y + 24 * k)} L {f(x)} {f(y + 2 * k)}" stroke="#4A8A3A" stroke-width="{f(2.4 * k)}"></path>'
                + "".join(f'<circle cx="{f(x + 8 * k * math.cos(math.radians(a)))}" cy="{f(y - 8 * k + 8 * k * math.sin(math.radians(a)))}" r="{f(7 * k)}" fill="#D8486A" stroke="{INK}" stroke-width="1"></circle>' for a in range(0, 360, 72))
                + f'<circle cx="{f(x)}" cy="{f(y - 8 * k)}" r="{f(5 * k)}" fill="#A8283A" stroke="{INK}" stroke-width="1"></circle>')
    if kind == "report":                                        # a herald's trumpet
        return (f'<path d="M{f(x - 26 * k)} {f(y + 2 * k)} L {f(x + 10 * k)} {f(y - 2 * k)} L {f(x + 24 * k)} {f(y - 14 * k)} L {f(x + 24 * k)} {f(y + 14 * k)} L {f(x + 10 * k)} {f(y + 2 * k)} Z" fill="#E8B830" stroke="{INK}" stroke-width="1.4"></path>'
                + "".join(f'<path d="M{f(x + 30 * k)} {f(y + dy * k)} l {f(10 * k)} {f(dy * 0.5 * k)}" stroke="#FFE680" stroke-width="1.4"></path>' for dy in (-10, 0, 10)))
    return ""

def whatsoever(w, h):
    """Whatsoever things are true, honorable, just, pure, lovely, of good report (4:8): a plate of six cells, each with its
    emblem — a plumb line, a laurel wreath, a balance, a lily, a rose, a herald's trumpet — and under them the charge."""
    o = [plate_bg(w, h, "PHILIPPIANS 4:8 · THINK ON THESE THINGS")]
    items = [("true", "TRUE"), ("honorable", "HONORABLE"), ("just", "JUST"), ("pure", "PURE"), ("lovely", "LOVELY"), ("report", "OF GOOD REPORT")]
    cols = 3
    x0, y0, x1, y1 = 14, 34, w - 14, h - 40
    cw, ch = (x1 - x0) / cols, (y1 - y0) / 2
    for i, (kind, lab) in enumerate(items):
        cx, cy = x0 + (i % cols) * cw, y0 + (i // cols) * ch
        o.append(f'<rect x="{f(cx + 4)}" y="{f(cy + 4)}" width="{f(cw - 8)}" height="{f(ch - 8)}" fill="#10243A" stroke="{GOLD}" stroke-width="1.4"></rect>')
        r = min(cw, ch) * 0.4
        o.append(halo(cx + cw / 2, cy + ch * 0.44, r, "#FFE680", 0.18) + _virtue(kind, cx + cw / 2, cy + ch * 0.44, r))
        o.append(plate_label(cx + cw / 2, cy + ch - 12, lab, GOLD, 9))
    o.append(plate_label(14, h - 18, "IF THERE BE ANY VIRTUE · ANY PRAISE", "#F3EFE6", 9, anchor="start"))
    return "".join(o)

def _want(p, w, h):
    """Abased, hungry, in want: a bare stone room in a cold light, an empty bowl on the floor and a crust beside it, the
    chain hanging from its ring."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A4E5E"></rect>',
         f'<rect x="-10" y="{f(h * 0.72)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A3A44" stroke="{INK}" stroke-width="2"></rect>']
    r = random.Random(7)
    for j in range(5):
        y = h * 0.14 * (j + 1)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#3A3E4A" stroke-width="1.4"></path>')
    o.append(f'<rect x="{f(w * 0.62)}" y="{f(h * 0.18)}" width="{f(w * 0.16)}" height="{f(h * 0.14)}" fill="#8A9AB8" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.66)} {f(h * 0.18)} L {f(w * 0.66)} {f(h * 0.32)} M{f(w * 0.7)} {f(h * 0.18)} L {f(w * 0.7)} {f(h * 0.32)} M{f(w * 0.74)} {f(h * 0.18)} L {f(w * 0.74)} {f(h * 0.32)}" stroke="{INK}" stroke-width="2.4"></path>')
    k = min(w, h) / 200
    o.append(f'<path d="M{f(w * 0.4 - 26 * k)} {f(h * 0.8)} C {f(w * 0.4 - 24 * k)} {f(h * 0.8 + 16 * k)} {f(w * 0.4 + 24 * k)} {f(h * 0.8 + 16 * k)} {f(w * 0.4 + 26 * k)} {f(h * 0.8)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.6)} {f(h * 0.84)} c {f(8 * k)} {f(-6 * k)} {f(18 * k)} {f(-4 * k)} {f(20 * k)} {f(2 * k)} c {f(-6 * k)} {f(4 * k)} {f(-14 * k)} {f(4 * k)} {f(-20 * k)} {f(-2 * k)} Z" fill="#B8884A" stroke="{INK}" stroke-width="1.4"></path>')
    o.append(f'<circle cx="{f(w * 0.14)}" cy="{f(h * 0.4)}" r="{f(8 * k)}" fill="none" stroke="#8A8A94" stroke-width="{f(3 * k)}"></circle>' + chain(w * 0.14, h * 0.42, w * 0.22, h * 0.7, k, sag=0.1))
    return "".join(o)

def _plenty(p, w, h):
    """Filled, abounding: a warm room by lamplight, a table spread with bread, figs and grapes, a jug of wine and a cup."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#8A4A2A"></rect>', lamp_glow(w * 0.5, h * 0.4, max(w, h) * 0.7, f"{p}pl", op=0.55),
         f'<rect x="-10" y="{f(h * 0.72)}" width="{f(w + 20)}" height="{f(h)}" fill="#5A3020" stroke="{INK}" stroke-width="2"></rect>']
    k = min(w, h) / 200
    tx, ty = w * 0.5, h * 0.62
    o.append(f'<rect x="{f(tx - w * 0.38)}" y="{f(ty)}" width="{f(w * 0.76)}" height="{f(10 * k)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(xx)}" y="{f(ty + 10 * k)}" width="{f(8 * k)}" height="{f(h * 0.2)}" fill="#4A2A14" stroke="{INK}" stroke-width="1.6"></rect>' for xx in (tx - w * 0.34, tx + w * 0.32)))
    o.append(f'<ellipse cx="{f(tx - w * 0.2)}" cy="{f(ty - 8 * k)}" rx="{f(22 * k)}" ry="{f(10 * k)}" fill="#C88A4A" stroke="{INK}" stroke-width="1.6"></ellipse>'
             f'<path d="M{f(tx - w * 0.04)} {f(ty)} L {f(tx - w * 0.06)} {f(ty - 34 * k)} C {f(tx - w * 0.06)} {f(ty - 44 * k)} {f(tx + w * 0.06)} {f(ty - 44 * k)} {f(tx + w * 0.06)} {f(ty - 34 * k)} L {f(tx + w * 0.04)} {f(ty)} Z" fill="#B85A3A" stroke="{INK}" stroke-width="1.6"></path>')
    for i in range(9):
        o.append(f'<circle cx="{f(tx + w * 0.16 + (i % 3 - 1) * 6 * k)}" cy="{f(ty - 6 * k - (i // 3) * 6 * k)}" r="{f(3.6 * k)}" fill="#5A2A6A" stroke="{INK}" stroke-width="0.8"></circle>')
    for i in range(3):
        o.append(f'<circle cx="{f(tx + w * 0.28 + i * 7 * k)}" cy="{f(ty - 5 * k)}" r="{f(5 * k)}" fill="#7A4A6A" stroke="{INK}" stroke-width="1"></circle>')
    o.append(clay_lamp(tx + w * 0.02, h * 0.3, k * 0.9))
    return "".join(o)

def want_plenty(p, w, h, seed):
    """I know how to be abased, and I know also how to abound … both to be filled and to be hungry, both to abound and to be
    in want (4:12): one panel in two rooms — at the left the bare cell, the empty bowl and the chain; at the right the warm
    table spread; their names over them."""
    o = [cells(p, w, h, [_want, _plenty])]
    o.append(plate_label(w * 0.25, 22, "TO BE HUNGRY · IN WANT", "#F3EFE6", 10, halo_="#2A2A34") + plate_label(w * 0.75, 22, "TO BE FILLED · TO ABOUND", "#FFF4C2", 10, halo_="#5A2A14"))
    return "".join(o)

def macedonia_gifts(w, h):
    """In the beginning of the gospel, when I departed from Macedonia, no church had fellowship with me … but ye only; for
    even in Thessalonica ye sent once and again unto my need (4:15–16): Macedonia and Achaia on Acts' map, the gifts going
    out from Philippi to Thessalonica (lit), and on to Paul at Corinth (2 Cor 11:9)."""
    return geo.med_map(w, h, box=(21.2, 25.4, 37.5, 41.5), places=("PHILIPPI", "THESSALONICA", "BERŒA", "ATHENS", "CORINTH"),
                       routes=[["PHILIPPI", "AMPHIPOLIS", "APOLLONIA", "THESSALONICA", "BERŒA", (22.4, 39.2), "CORINTH"], ["PHILIPPI", "AMPHIPOLIS", "APOLLONIA", "THESSALONICA"]],
                       hi=("PHILIPPI", "THESSALONICA"), regions=(("MACEDONIA", 23.4, 41.3), ("ACHAIA", 22.0, 38.3)), title="PHILIPPIANS 4:16 · ONCE AND AGAIN UNTO MY NEED",
                       red=True, size=9)

def the_gift(p, w, h, seed):
    """Having received from Epaphroditus the things that came from you, an odor of a sweet smell, a sacrifice acceptable
    (4:18): Paul's room at Rome by day, Paul sitting chained to the soldier, Epaphroditus come in with the gift — a purse and
    a basket of good things set down before him; and by the window a censer burning, its sweet smoke going up."""
    b = h * 0.94
    o = [_defs(p), room(w, h, b, wall="#D8C8A8", floor="#8A7A62"), rome_window(w * 0.46, h * 0.14, min(w * 0.16, h * 0.4), h * 0.3, False, seed)]
    s = fit(b, b - min(h * 0.72, 210))
    o.append(censer(w * 0.62, b, s * 0.9, seed, f"{p}cn"))
    gx, px = w * 0.08, w * 0.27
    o.append(EP._shield(w * 0.0, b, s) if hasattr(EP, "_shield") else "")
    o.append(guard_r(p, gx, b, s) + bench(px - 52 * s, b, 110 * s, s) + paul_fig(p, px, b, s, flip=True, pose="sit", seat=None, up=[(-22, -158), (-50, -146), (-76, -150)]))
    o.append(chain(*guard_hand(gx, b, s), *robed_hand(px, b, s, flip=True, pose="sit"), s=s * 0.8))
    o.append(f'<path d="M{f(w * 0.43)} {f(b - 4)} L {f(w * 0.41)} {f(b - 30 * s)} L {f(w * 0.53)} {f(b - 30 * s)} L {f(w * 0.51)} {f(b - 4)} Z" fill="#C8A060" stroke="{INK}" stroke-width="2"></path>'
             + "".join(f'<circle cx="{f(w * 0.44 + i * 9 * s)}" cy="{f(b - 34 * s)}" r="{f(6 * s)}" fill="{["#7A4A6A", "#C8883A", "#5A2A6A", "#C8A040"][i % 4]}" stroke="{INK}" stroke-width="1"></circle>' for i in range(5)))
    o.append(epaphroditus(p, w * 0.8, b, s, up=[(-22, -158), (-44, -144), (-64, -140)], extra=bag(-64, -128, 0.5)))
    return "".join(o)

def caesars_household(p, w, h, seed):
    """All the saints salute you, especially they that are of Cæsar's household (4:22): the Palatine at dusk, the palace
    of the Cæsars with its colonnades on the hill; at a side door below, servants of the household — bondmen and freedmen in
    plain tunics, a woman with a lamp — greeting one another as brethren."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#2A2A5A", "#E8A060")]
    o.append(f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.2)} {f(h * 0.36)} {f(w * 0.6)} {f(h * 0.3)} {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h * 0.7)} L -10 {f(h * 0.7)} Z" fill="#5A4A4A" stroke="{INK}" stroke-width="2"></path>')
    px0, px1, py = w * 0.16, w * 0.94, h * 0.38                # the palace: a podium, two storeys of colonnades, red roofs
    o.append(f'<rect x="{f(px0)}" y="{f(py)}" width="{f(px1 - px0)}" height="{f(h * 0.2)}" fill="#E8DCC4" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(px0 - 8)} {f(py)} L {f(px0 + 20)} {f(py - h * 0.05)} L {f(px1 - 20)} {f(py - h * 0.05)} L {f(px1 + 8)} {f(py)} Z" fill="#A8483A" stroke="{INK}" stroke-width="2"></path>')
    n = int((px1 - px0) / 22)
    for i in range(n):
        x = px0 + 8 + i * 22
        o.append(f'<rect x="{f(x)}" y="{f(py + h * 0.02)}" width="7" height="{f(h * 0.16)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1"></rect>')
    o.append(f'<rect x="{f(px0)}" y="{f(py + h * 0.02)}" width="{f(px1 - px0)}" height="{f(h * 0.16)}" fill="#5A4A3A" opacity="0.3"></rect>')
    for i in range(6):
        if i % 2 == 0: o.append(f'<rect x="{f(px0 + 30 + i * (px1 - px0 - 60) / 6)}" y="{f(py + h * 0.08)}" width="10" height="12" fill="#FFC14D"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h)}" fill="#C8B088" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.06)}" y="{f(h * 0.62)}" width="{f(w * 0.88)}" height="{f(b - h * 0.62)}" fill="#D8C8A0" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.44)}" y="{f(h * 0.66)}" width="{f(w * 0.1)}" height="{f(b - h * 0.66)}" fill="#FFC14D" stroke="{INK}" stroke-width="2"></rect>')
    o.append(ground(w, h, b, "#8A7A5A", dy=0))
    s = fit(b, b - min(h * 0.4, 130))
    tunic = lambda c: dict(cloth=c)
    figs = [(0.2, "#C8B898", "#2A1A10", None, False), (0.3, "#8A9AA0", None, "#1F2F5A", True), (0.62, "#B8A070", "#3A2214", None, False),
            (0.72, "#D8D0C0", "#1A1210", None, False), (0.82, "#7A6A5A", None, "#E8E2D6", True)]
    for i, (x, c, hr, vl, wm) in enumerate(figs):
        fl = x < 0.5
        up = [(-22, -158), (-46, -150), (-66, -156)] if i in (1, 2) else None
        if wm: o.append(robed(p, w * x, b, s * 0.94, c, woman=True, veil=vl, flip=fl, up=up, extra=clay_lamp(-66, -160, 0.5) if i == 1 else ""))
        else: o.append(robed(p, w * x, b, s, c, hair=hr, belt="#5A3A1E", flip=fl, up=up))
    return "".join(o)
