"""Isaiah 40–42 drawings (on top of isa.art10): the way prepared in the desert, the grass and the flower, the herald on a high
mountain, the flock and the lambs gathered (no shepherd drawn: he is Jehovah), the measure of the waters and the scales (a
plate), the drop of a bucket, the image cast by the goldsmith, the circle of the earth and the host of stars, eagles' wings,
one raised from the east, the threshing sledge with teeth, rivers on the bare heights and trees in the desert, the bruised
reed and the dimly burning wick, the new song from the ends of the earth, the blind led by a way, and the people snared."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art10 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
from genesis.art2 import birds
from exo.art8 import bp, dim, tag, title_bar, box

def comfort_city(w, h, seed):
    """Speak ye comfortably to Jerusalem; cry unto her, that her warfare is accomplished: Jerusalem at dawn after rain, the
    smoke of war gone, light breaking over the walls."""
    o = [bg(w, h, "#6A7ABA", "#FFE0B0"), V.rays(w * 0.7, h * 0.4, 30, 20, max(w, h), color="#FFF4C2", op=0.35),
         J.city_hill(w * 0.5, h * 0.96, w * 0.56, h * 0.4, seed), K1.temple_front(w * 0.5, h * 0.56, min(w * 0.16, h * 0.36), seed)]
    return "".join(o)

def way_prepared(w, h, seed):
    """Prepare ye in the wilderness the way of Jehovah; every valley shall be exalted, and every mountain and hill made low; the
    uneven made level, and the rough places a plain: a straight highway running across the desert to the horizon, the hills on
    either side cut down to it, the valleys filled."""
    o = [bg(w, h, "#E8A050", "#FFF0C8"), sun(w * 0.5, h * 0.3, min(30, h * 0.08), color="#FFF4C2", op=0.5)]
    o.append(f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.12)} {f(h * 0.3)} L {f(w * 0.26)} {f(h * 0.44)} L {f(w * 0.4)} {f(h * 0.5)} Z" fill="#B87A4A" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(w + 10)} {f(h * 0.5)} L {f(w * 0.88)} {f(h * 0.32)} L {f(w * 0.74)} {f(h * 0.42)} L {f(w * 0.6)} {f(h * 0.5)} Z" fill="#A86A3A" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(ground(w, h, h * 0.5, "#D8B070", dy=0))
    o.append(f'<path d="M{f(w * 0.48)} {f(h * 0.5)} L {f(w * 0.52)} {f(h * 0.5)} L {f(w * 0.8)} {f(h + 10)} L {f(w * 0.2)} {f(h + 10)} Z" fill="#F3E8C8" stroke="#0D0D0F" stroke-width="2"></path>')
    for k in range(6):
        t = (k + 1) / 7; y = h * 0.5 + (h * 0.5) * t * t
        x0 = w * 0.5 - (w * 0.3) * t * t; x1 = w * 0.5 + (w * 0.3) * t * t
        o.append(f'<path d="M{f(x0)} {f(y)} L {f(x1)} {f(y)}" stroke="#C8B080" stroke-width="1.4"></path>')
    return "".join(o)

def grass_flower(w, h, seed):
    """The grass withereth, the flower fadeth, because the breath of Jehovah bloweth upon it: grass and wild flowers bending in a
    hot wind, the near ones fresh, the far ones withered."""
    r = random.Random(seed)
    o = [bg(w, h, "#E8B070", "#FFF0C8"), ground(w, h, h * 0.4, "#C8A860", dy=0)]
    for _ in range(int(w / 5)):
        x = r.uniform(0, w); y = r.uniform(h * 0.42, h); sc = 0.4 + (y / h) * 1.2
        withered = x > w * 0.5
        col = "#A88A3A" if withered else "#5E8F26"
        o.append(f'<path d="M{f(x)} {f(y)} q {f(8 * sc)} {f(-16 * sc)} {f(18 * sc)} {f(-26 * sc)}" stroke="{col}" stroke-width="{f(1.6 * sc)}" fill="none"></path>')
        if r.random() < 0.12:
            fc = "#8A6A4A" if withered else r.choice(["#D7261E", "#FFD23F", "#E8406A"])
            o.append(f'<circle cx="{f(x + 18 * sc)}" cy="{f(y - 26 * sc)}" r="{f(3.6 * sc)}" fill="{fc}" stroke="#0D0D0F" stroke-width="0.8"></circle>')
    for k in range(5):
        y = h * (0.1 + k * 0.08)
        o.append(f'<path d="M{f(-10)} {f(y)} C {f(w * 0.3)} {f(y - 10)} {f(w * 0.6)} {f(y + 10)} {f(w + 10)} {f(y)}" stroke="#FFF4C2" stroke-width="2" fill="none" opacity="0.6"></path>')
    return "".join(o)

def herald(p, w, h, seed):
    """O thou that tellest good tidings to Zion, get thee up on a high mountain; lift up thy voice with strength; say unto the
    cities of Judah, Behold, your God!: a herald on a mountain-top, arm raised, the cities of Judah below in the morning."""
    o = [mk.defs(p, *ALL), bg(w, h, "#7AA8E0", "#FFF0C8"), hills(w, h, h * 0.66, seed, color="#9AA06A", amp=10)]
    for x in (0.56, 0.74, 0.9):
        o.append(J.city_hill(w * x, h * 0.74, w * 0.06, h * 0.08, seed + int(x * 10)))
    o.append(f'<path d="M-10 {f(h + 10)} L {f(w * 0.24)} {f(h * 0.3)} L {f(w * 0.48)} {f(h + 10)} Z" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    s = fit(h * 0.32, h * 0.06)
    o.append(woman(p, w * 0.24, h * 0.32, s, "#E8B830", flip=True, up=[(22, -158), (40, -190), (52, -222)]))
    return "".join(o)

def flock_fold(w, h, seed):
    """He will feed his flock like a shepherd, he will gather the lambs in his arm, and carry them in his bosom, and will gently
    lead those that have their young: a flock at rest in green pasture by still water, ewes with their lambs close, a shepherd's
    crook leaning on the fold wall (no shepherd drawn)."""
    r = random.Random(seed)
    o = [bg(w, h, "#8FC8E8", "#F8F0D0"), hills(w, h, h * 0.44, seed, color="#7AA04A", amp=10), ground(w, h, h * 0.52, "#9CCB5E", dy=0),
         f'<ellipse cx="{f(w * 0.8)}" cy="{f(h * 0.62)}" rx="{f(w * 0.14)}" ry="{f(h * 0.05)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="1.6"></ellipse>']
    for i in range(10):
        o.append(f'<rect x="{f(i * w * 0.05)}" y="{f(h * 0.56)}" width="{f(w * 0.048)}" height="{f(h * 0.06)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    o.append(f'<path d="M{f(w * 0.46)} {f(h * 0.62)} L {f(w * 0.5)} {f(h * 0.3)} c {f(2)} {f(-14)} {f(18)} {f(-14)} {f(16)} {f(4)}" stroke="#6A4A2A" stroke-width="5" fill="none" stroke-linecap="round"></path>')
    s = min(0.6, h / 500)
    for _ in range(9):
        x = r.uniform(w * 0.05, w * 0.95); y = r.uniform(h * 0.7, h * 0.96)
        o.append(E.sheep(x, y, s * (0.7 + (y / h - 0.7)), flip=r.random() < 0.5))
        if r.random() < 0.6: o.append(E3.lamb(x + 30 * s, y + 4, s * 0.5, flip=r.random() < 0.5))
    return "".join(o)

def measures(w, h):
    """Who hath measured the waters in the hollow of his hand, and meted out heaven with the span, and comprehended the dust of
    the earth in a measure, and weighed the mountains in scales, and the hills in a balance?: a plate of the measures — the
    hollow of the hand, the span, the measure, the scales — with the seas, the heavens, the dust and the mountains set against
    them (no hand drawn: the questions only)."""
    o = [bp(w, h), title_bar(w, "WHO HATH MEASURED THE WATERS?")]
    s = min(1.0, h / 220); cw = w / 4; b = h * 0.78
    items = [("THE WATERS", "THE HOLLOW OF HIS HAND"), ("HEAVEN", "THE SPAN"), ("THE DUST", "A MEASURE"), ("THE MOUNTAINS", "SCALES · A BALANCE")]
    for i, (what, by) in enumerate(items):
        cx = cw * (i + 0.5)
        if i == 0:
            o.append(f'<path d="M{f(cx - 40 * s)} {f(b - 20 * s)} C {f(cx - 20 * s)} {f(b - 40 * s)} {f(cx + 20 * s)} {f(b)} {f(cx + 40 * s)} {f(b - 20 * s)} L {f(cx + 40 * s)} {f(b)} L {f(cx - 40 * s)} {f(b)} Z" fill="#1F5A7A" stroke="#8FD0E2" stroke-width="1.4"></path>')
        elif i == 1:
            o.append(mk.stars(10, cw * 0.6, 50 * s, i).replace("<g", f'<g transform="translate({f(cx - cw * 0.3)} {f(b - 70 * s)})"', 1) if False else
                     "".join(f'<circle cx="{f(cx + (k - 3) * 12 * s)}" cy="{f(b - 30 * s - (k % 3) * 12 * s)}" r="2" fill="#FFF4C2"></circle>' for k in range(7))
                     + dim(cx - 40 * s, b, cx + 40 * s, b, "SPAN"))
        elif i == 2:
            o.append(f'<path d="M{f(cx - 26 * s)} {f(b - 40 * s)} L {f(cx + 26 * s)} {f(b - 40 * s)} L {f(cx + 20 * s)} {f(b)} L {f(cx - 20 * s)} {f(b)} Z" fill="none" stroke="#8FD0E2" stroke-width="2"></path>'
                     f'<path d="M{f(cx - 22 * s)} {f(b - 20 * s)} Q {f(cx)} {f(b - 34 * s)} {f(cx + 22 * s)} {f(b - 20 * s)} L {f(cx + 20 * s)} {f(b)} L {f(cx - 20 * s)} {f(b)} Z" fill="#C8A060"></path>')
        else:
            o.append(S4.balance(cx, b, 0.5 * s) + f'<path d="M{f(cx - 44 * s)} {f(b - 50 * s)} L {f(cx - 34 * s)} {f(b - 66 * s)} L {f(cx - 24 * s)} {f(b - 50 * s)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.4"></path>')
        o.append(label(cx, b + 24 * s, what, GOLD, 9) + label(cx, b + 38 * s, by, CYAN, 8))
    return "".join(o)

def bucket_drop(w, h, seed):
    """Behold, the nations are as a drop of a bucket, and are accounted as the small dust of the balance: a drop falling from the
    rim of a bucket, and in the drop the whole map of the nations."""
    o = [rect(w, h, "#0B1A2E")]
    s = min(1.2, h / 220)
    bx, by, bw_, bh_ = w * 0.3, h * 0.3, min(w * 0.2, h * 0.5), min(h * 0.36, w * 0.16)
    o.append(f'<g transform="rotate(-28 {f(bx)} {f(by)})"><path d="M{f(bx - bw_ / 2)} {f(by - bh_ / 2)} L {f(bx + bw_ / 2)} {f(by - bh_ / 2)} L {f(bx + bw_ * 0.38)} {f(by + bh_ / 2)} L {f(bx - bw_ * 0.38)} {f(by + bh_ / 2)} Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + "".join(f'<path d="M{f(bx - bw_ * (0.5 - k * 0.04))} {f(by - bh_ / 2 + k * bh_ * 0.33)} L {f(bx + bw_ * (0.5 - k * 0.04))} {f(by - bh_ / 2 + k * bh_ * 0.33)}" stroke="#3A3A40" stroke-width="4"></path>' for k in range(1, 3))
             + f'<ellipse cx="{f(bx)}" cy="{f(by - bh_ / 2)}" rx="{f(bw_ / 2)}" ry="{f(bh_ * 0.12)}" fill="#1F5A7A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
             f'<path d="M{f(bx - bw_ / 2)} {f(by - bh_ / 2)} C {f(bx - bw_ / 2)} {f(by - bh_ * 1.3)} {f(bx + bw_ / 2)} {f(by - bh_ * 1.3)} {f(bx + bw_ / 2)} {f(by - bh_ / 2)}" stroke="#5A5A60" stroke-width="3" fill="none"></path></g>')
    cx, cy, r = w * 0.62, h * 0.62, min(w, h) * 0.3
    o.append(f'<defs><clipPath id="bd{seed}"><path d="M{f(cx)} {f(cy - r * 1.3)} C {f(cx + r * 0.3)} {f(cy - r * 0.6)} {f(cx + r)} {f(cy - r * 0.2)} {f(cx + r)} {f(cy + r * 0.3)} A {f(r)} {f(r)} 0 0 1 {f(cx - r)} {f(cy + r * 0.3)} C {f(cx - r)} {f(cy - r * 0.2)} {f(cx - r * 0.3)} {f(cy - r * 0.6)} {f(cx)} {f(cy - r * 1.3)} Z"></path></clipPath></defs>'
             f'<g clip-path="url(#bd{seed})"><g transform="translate({f(cx - r)} {f(cy - r * 1.3)})">{nations_map(r * 2, r * 2.6, show=["EGYPT", "BABYLON", "JERUSALEM", "NINEVEH", "TYRE", "MEDIA"])}</g></g>'
             f'<path d="M{f(cx)} {f(cy - r * 1.3)} C {f(cx + r * 0.3)} {f(cy - r * 0.6)} {f(cx + r)} {f(cy - r * 0.2)} {f(cx + r)} {f(cy + r * 0.3)} A {f(r)} {f(r)} 0 0 1 {f(cx - r)} {f(cy + r * 0.3)} C {f(cx - r)} {f(cy - r * 0.2)} {f(cx - r * 0.3)} {f(cy - r * 0.6)} {f(cx)} {f(cy - r * 1.3)} Z" fill="none" stroke="#E8F6FA" stroke-width="3"></path>')
    return "".join(o)

def goldsmith(p, w, h, seed):
    """The image, a workman hath cast it, and the goldsmith overlayeth it with gold, and casteth for it silver chains; the
    carpenter encourageth the goldsmith, he that smootheth with the hammer him that smiteth the anvil: a workshop — a furnace, an
    anvil, a gilded idol being fastened with nails to its stand, two craftsmen at work."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), rect(w, h, "#3A2418"), f'<circle cx="{f(w * 0.2)}" cy="{f(h * 0.7)}" r="{f(h * 0.4)}" fill="#C8582A" opacity="0.3"></circle>', ground(w, h, h * 0.86, "#2A1A12", dy=0)]
    s = min(1.0, h / 280)
    o.append(f'<path d="M{f(w * 0.08)} {f(b)} L {f(w * 0.1)} {f(b - 90 * s)} L {f(w * 0.3)} {f(b - 90 * s)} L {f(w * 0.32)} {f(b)} Z" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="2"></path>'
             + E.blaze(w * 0.2, b - 40 * s, 50 * s, 40 * s, seed, n=5))
    ix = w * 0.56
    o.append(f'<rect x="{f(ix - 30 * s)}" y="{f(b - 20 * s)}" width="{f(60 * s)}" height="{f(20 * s)}" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(ix - 14 * s)}" y="{f(b - 110 * s)}" width="{f(28 * s)}" height="{f(90 * s)}" rx="{f(8 * s)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<circle cx="{f(ix)}" cy="{f(b - 124 * s)}" r="{f(16 * s)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></circle>'
             f'<path d="M{f(ix - 14 * s)} {f(b - 90 * s)} C {f(ix - 30 * s)} {f(b - 70 * s)} {f(ix - 30 * s)} {f(b - 50 * s)} {f(ix - 14 * s)} {f(b - 40 * s)}" stroke="#C8C8D0" stroke-width="2" fill="none" stroke-dasharray="3 2"></path>')
    fs = fit(b, max(h * 0.5, b - 170))
    o.append(man(p, w * 0.4, b, fs, "#6A5A3A", up=[(-22, -158), (-6, -176), (16, -170)]) + man(p, w * 0.76, b, fs, "#4A3A2A", flip=True, up=[(-22, -158), (-40, -150), (-58, -150)]))
    o.append(f'<rect x="{f(w * 0.86)}" y="{f(b - 30 * s)}" width="{f(40 * s)}" height="{f(30 * s)}" fill="#3A3A40" stroke="#0D0D0F" stroke-width="2"></rect>')
    return "".join(o)

def circle_earth(w, h, seed):
    """It is he that sitteth above the circle of the earth, and the inhabitants thereof are as grasshoppers; that stretcheth out
    the heavens as a curtain, and spreadeth them out as a tent to dwell in: the curve of the earth seen from high above, its
    seas and lands, the heavens drawn over it like a curtain of stars (no one drawn)."""
    o = [rect(w, h, "#05050A"), mk.stars(70, w, h, seed)]
    cx, cy, r = w * 0.5, h + max(w, h) * 0.9, max(w, h) * 1.25
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="#1F5A8A" stroke="#8FD0E2" stroke-width="3"></circle>'
             f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r + 14)}" fill="none" stroke="#8FD0E2" stroke-width="10" opacity="0.25"></circle>')
    o.append(f'<path d="M{f(cx - r * 0.5)} {f(cy - r * 0.9)} C {f(cx - r * 0.3)} {f(cy - r * 0.96)} {f(cx)} {f(cy - r * 0.92)} {f(cx + r * 0.1)} {f(cy - r * 0.97)} L {f(cx + r * 0.2)} {f(cy - r * 0.9)} Z" fill="#8A9A5A" stroke="#0D0D0F" stroke-width="1.6"></path>')
    for k in range(5):
        o.append(f'<path d="M{f(-10)} {f(h * (0.05 + k * 0.04))} C {f(w * 0.3)} {f(h * (0.1 + k * 0.04))} {f(w * 0.7)} {f(h * (0.1 + k * 0.04))} {f(w + 10)} {f(h * (0.05 + k * 0.04))}" stroke="#5A4A98" stroke-width="2" fill="none" opacity="0.5"></path>')
    return "".join(o)

def host_stars(w, h, seed):
    """Lift up your eyes on high, and see who hath created these, that bringeth out their host by number; he calleth them all by
    name: the night sky crowded with stars over the hills, a lone figure on a ridge looking up."""
    o = [bg(w, h, "#05051A", "#1E1650"), mk.stars(160, w, h * 0.8, seed)]
    for k in range(30):
        r = random.Random(seed + k)
        o.append(N.star(r.uniform(0, w), r.uniform(0, h * 0.6), r.uniform(2, 5), color="#FFF4C2"))
    o.append(hills(w, h, h * 0.84, seed, color="#0D0D1A", amp=10))
    s = fit(h * 0.86, h * 0.7)
    o.append(mk.defs(f"hs{seed}", *ALL) + mk.person(f"hs{seed}", round(w * 0.3), round(h * 0.86), round(s, 3), body="#0D0D12", cloth="#14142A", up=[(-22, -158), (-28, -186), (-24, -214)]))
    return "".join(o)

def eagles(w, h, seed):
    """They that wait for Jehovah shall renew their strength; they shall mount up with wings as eagles: eagles rising on broad
    wings over the cliffs into the morning."""
    o = [bg(w, h, "#5A8AD0", "#FFE8B0"), sun(w * 0.8, h * 0.7, min(30, h * 0.08), color="#FFF4C2", op=0.4),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.5)} L {f(w * 0.14)} {f(h * 0.44)} L {f(w * 0.22)} {f(h * 0.7)} L {f(w * 0.3)} {f(h + 10)} Z" fill="#8A6A5A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = min(1.3, h / 260)
    for i, (x, y, k) in enumerate(((0.42, 0.3, 1.0), (0.66, 0.5, 0.7), (0.26, 0.2, 0.55))):
        cx, cy, kk = w * x, h * y, s * k
        o.append(f'<path d="M{f(cx)} {f(cy)} C {f(cx - 40 * kk)} {f(cy - 30 * kk)} {f(cx - 90 * kk)} {f(cy - 26 * kk)} {f(cx - 130 * kk)} {f(cy - 6 * kk)} C {f(cx - 100 * kk)} {f(cy - 2 * kk)} {f(cx - 60 * kk)} {f(cy + 8 * kk)} {f(cx - 10 * kk)} {f(cy + 10 * kk)} Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<path d="M{f(cx)} {f(cy)} C {f(cx + 40 * kk)} {f(cy - 30 * kk)} {f(cx + 90 * kk)} {f(cy - 26 * kk)} {f(cx + 130 * kk)} {f(cy - 6 * kk)} C {f(cx + 100 * kk)} {f(cy - 2 * kk)} {f(cx + 60 * kk)} {f(cy + 8 * kk)} {f(cx + 10 * kk)} {f(cy + 10 * kk)} Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<ellipse cx="{f(cx)}" cy="{f(cy + 10 * kk)}" rx="{f(14 * kk)}" ry="{f(26 * kk)}" fill="#4A2E1A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
                 f'<circle cx="{f(cx)}" cy="{f(cy - 14 * kk)}" r="{f(9 * kk)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></circle><path d="M{f(cx - 3 * kk)} {f(cy - 8 * kk)} L {f(cx)} {f(cy - 2 * kk)} L {f(cx + 3 * kk)} {f(cy - 8 * kk)} Z" fill="#E8B830"></path>'
                 f'<path d="M{f(cx - 10 * kk)} {f(cy + 34 * kk)} L {f(cx)} {f(cy + 46 * kk)} L {f(cx + 10 * kk)} {f(cy + 34 * kk)} Z" fill="#4A2E1A" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return "".join(o)

def east_one(w, h, note="ONE FROM THE EAST"):
    """Who hath raised up one from the east, whom he calleth in righteousness to his foot? he giveth nations before him: a red
    arrow sweeping out of the east from Media and Elam across the nations to Babylon and beyond."""
    return nations_map(w, h, hi=("MEDIA", "ELAM"), arrows=(("MEDIA", "BABYLON"), ("ELAM", "BABYLON"), ("BABYLON", "DAMASCUS")), lit="#FFD23F",
                       show=["MEDIA", "ELAM", "BABYLON", "NINEVEH", "DAMASCUS", "JERUSALEM", "EGYPT", "TYRE"], note=note)

def threshing_sledge(w, h):
    """I have made thee to be a new sharp threshing instrument having teeth; thou shalt thresh the mountains, and make the hills
    as chaff (a plate of the sledge)."""
    o = [bp(w, h), title_bar(w, "A NEW SHARP THRESHING INSTRUMENT HAVING TEETH")]
    u = min(w * 0.7, h * 1.6); x0, y0 = w * 0.5 - u * 0.4, h * 0.6
    o.append(box(x0, y0, u * 0.8, u * 0.24, u * 0.04, fill="#B5793A", top="#C8904A", side="#8A5A2A"))
    for k in range(18):
        x = x0 + 8 + k * (u * 0.8 - 16) / 17
        o.append(f'<path d="M{f(x - 4)} {f(y0)} L {f(x)} {f(y0 + 12)} L {f(x + 4)} {f(y0)} Z" fill="#C8D0D8" stroke="#0D0D0F" stroke-width="1"></path>')
    o.append(tag(x0 + u * 0.4, y0 + 10, "TEETH OF IRON", x0 + u * 0.5, y0 + 50) + dim(x0, y0 + 30, x0 + u * 0.8, y0 + 30, "NEW · SHARP"))
    o.append(J1.chaff(26, w * 0.1, w * 0.9, h * 0.14, h * 0.4, 7))
    return "".join(o)

def desert_trees(w, h, seed):
    """I will open rivers on the bare heights, and fountains in the midst of the valleys; I will put in the wilderness the cedar,
    the acacia, and the myrtle, and the oil-tree; the fir-tree, the pine, and the box-tree together: a desert valley with a river
    running down from the bare heights, and a row of seven different trees growing along it."""
    r = random.Random(seed)
    o = [bg(w, h, "#8FC8E8", "#FFF0C8"), f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.2)} {f(h * 0.2)} L {f(w * 0.36)} {f(h * 0.4)} L {f(w * 0.5)} {f(h * 0.26)} L {f(w * 0.7)} {f(h * 0.46)} L {f(w * 0.86)} {f(h * 0.24)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8986A" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, h * 0.6, "#D8B880", dy=0),
         f'<path d="M{f(w * 0.5)} {f(h * 0.28)} C {f(w * 0.48)} {f(h * 0.44)} {f(w * 0.4)} {f(h * 0.6)} {f(w * 0.3)} {f(h * 0.7)} C {f(w * 0.2)} {f(h * 0.8)} {f(w * 0.5)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.86)}" stroke="#2C9DB8" stroke-width="{f(max(5, h * 0.025))}" fill="none"></path>']
    s = min(0.8, h / 380)
    names = ["CEDAR", "ACACIA", "MYRTLE", "OIL-TREE", "FIR", "PINE", "BOX"]
    for i, nm in enumerate(names):
        x = w * (0.08 + i * 0.14); y = h * (0.94 - (i % 2) * 0.04)
        if nm in ("CEDAR", "FIR", "PINE"):
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 110 * s)}" stroke="#4A2E1A" stroke-width="{f(5 * s)}"></path>'
                     + "".join(f'<path d="M{f(x - (38 - j * 8) * s)} {f(y - (30 + j * 22) * s)} L {f(x)} {f(y - (60 + j * 22) * s)} L {f(x + (38 - j * 8) * s)} {f(y - (30 + j * 22) * s)} Z" fill="#1F4A34" stroke="#0D0D0F" stroke-width="1.2"></path>' for j in range(4)))
        elif nm == "ACACIA":
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 70 * s)}" stroke="#5A3A22" stroke-width="{f(5 * s)}"></path><ellipse cx="{f(x)}" cy="{f(y - 80 * s)}" rx="{f(46 * s)}" ry="{f(14 * s)}" fill="#6A8A3A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
        else:
            col = {"MYRTLE": "#3E7A3A", "OIL-TREE": "#8A9A6A", "BOX": "#2E6A32"}[nm]
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 50 * s)}" stroke="#5A3A22" stroke-width="{f(5 * s)}"></path><circle cx="{f(x)}" cy="{f(y - 70 * s)}" r="{f(30 * s)}" fill="{col}" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    return "".join(o)

def reed_wick(w, h):
    """A bruised reed will he not break, and a dimly burning wick will he not quench (a plate)."""
    o = [bp(w, h), title_bar(w, "A BRUISED REED · A DIMLY BURNING WICK")]
    s = min(1.2, h / 220); b = h * 0.8
    rx = w * 0.3
    o.append(f'<path d="M{f(rx)} {f(b)} L {f(rx)} {f(b - 80 * s)} L {f(rx + 30 * s)} {f(b - 110 * s)} L {f(rx + 36 * s)} {f(b - 150 * s)}" stroke="#7AA040" stroke-width="{f(6 * s)}" fill="none" stroke-linejoin="round"></path>'
             f'<path d="M{f(rx + 36 * s)} {f(b - 150 * s)} l {f(-6 * s)} {f(-26 * s)} M{f(rx + 36 * s)} {f(b - 150 * s)} l {f(10 * s)} {f(-22 * s)}" stroke="#9CCB5E" stroke-width="3"></path>'
             + tag(rx + 4, b - 84 * s, "BRUISED · NOT BROKEN", rx + 80 * s, b - 60 * s))
    from genesis.art4 import clay_lamp
    lx = w * 0.7
    o.append(clay_lamp(lx, b, 1.2 * s).replace('fill="#FFD23F"', 'fill="#FF8A3D"') + f'<circle cx="{f(lx + 20 * s)}" cy="{f(b - 40 * s)}" r="{f(10 * s)}" fill="#FFC14D" opacity="0.4"></circle>'
             + tag(lx + 20 * s, b - 36 * s, "DIMLY BURNING · NOT QUENCHED", lx - 20 * s, b - 90 * s, color=GOLD))
    return "".join(o)

def light_nations(w, h):
    """I will give thee for a covenant of the people, for a light of the Gentiles; to open the blind eyes, to bring out the
    prisoners from the dungeon: the map of the nations with a light spreading out from Jerusalem over all of them."""
    o = [nations_map(w, h, show=["JERUSALEM", "EGYPT", "BABYLON", "NINEVEH", "TYRE", "DAMASCUS", "ETHIOPIA", "TARSHISH", "MEDIA", "EDOM"])]
    cx, cy = w * 0.225, h * 0.47
    for k in range(5):
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(30 + k * max(w, h) * 0.12)}" fill="none" stroke="#FFD23F" stroke-width="{f(3 - k * 0.4)}" opacity="{0.8 - k * 0.14:.2f}"></circle>')
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(max(w, h) * 0.08)}" fill="#FFF4C2" opacity="0.3"></circle>')
    return "".join(o)

def new_song(p, w, h, seed):
    """Sing unto Jehovah a new song; ye that go down to the sea, the isles; the villages that Kedar doth inhabit; let the
    inhabitants of Sela sing, let them shout from the top of the mountains: a ship at sea, tents of Kedar in the desert, and the
    rock of Sela with people on its top, arms raised."""
    o = [mk.defs(p, *ALL), bg(w, h, "#8FC8E8", "#FFF0C8"), f'<rect x="-10" y="{f(h * 0.6)}" width="{f(w * 0.36)}" height="{f(h * 0.5)}" fill="#1F6F9A"></rect>',
         K1.ship(w * 0.14, h * 0.78, min(0.6, h / 420)), f'<path d="M{f(w * 0.34)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.34)} {f(h + 10)} Z" fill="#D8B070" stroke="#0D0D0F" stroke-width="2"></path>']
    o.append(E4.tent(w * 0.44, h * 0.82, w * 0.08, h * 0.12, color="#2A1E1A") + E4.tent(w * 0.54, h * 0.86, w * 0.08, h * 0.12, color="#3A2A1E"))
    o.append(f'<path d="M{f(w * 0.66)} {f(h + 10)} L {f(w * 0.7)} {f(h * 0.36)} L {f(w * 0.92)} {f(h * 0.32)} L {f(w * 0.96)} {f(h + 10)} Z" fill="#B85A3A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    s = fit(h * 0.34, h * 0.14)
    for i in range(3):
        o.append(man(p, w * (0.74 + i * 0.06), h * 0.34 - (i % 2) * 2, s, ["#5A3A6A", "#2A5A7A", "#8A3A2A"][i], up=[(-22, -158), (-30, -190), (-24, -222)]))
    o.append(S3.notes(w * 0.56, h * 0.3, 5, seed, color="#3A2A6A"))
    return "".join(o)

def blind_led(p, w, h, seed):
    """I will bring the blind by a way that they know not; I will make darkness light before them, and crooked places straight:
    a line of travellers holding one another's shoulders, walking out of a dark crooked gorge onto a straight lit road."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), rect(w, h, "#14122A"), f'<path d="M{f(w * 0.5)} -10 L {f(w + 10)} -10 L {f(w + 10)} {f(h + 10)} L {f(w * 0.4)} {f(h + 10)} Z" fill="#FFE8B0"></path>',
         f'<path d="M-10 {f(h * 0.3)} L {f(w * 0.2)} {f(h * 0.4)} L {f(w * 0.1)} {f(h * 0.6)} L {f(w * 0.3)} {f(h * 0.7)} L {f(w * 0.2)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A2440" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.36)} {f(b + 4)} L {f(w + 10)} {f(b - 20)}" stroke="#E8D8A8" stroke-width="{f(h * 0.06)}"></path>']
    s = fit(b, max(h * 0.55, b - 150))
    for i in range(4):
        o.append(man(p, w * (0.36 + i * 0.12), b - i * 6, s, ["#5A4A6A", "#6A3A2A", "#3A4A6A", "#7A5A3A"][i], up=[(-22, -158), (-46, -150), (-66, -150)] if i > 0 else None))
    return "".join(o)

def snared(w, h, seed):
    """A people robbed and plundered; they are all of them snared in holes, and they are hid in prison-houses; for a prey, and
    none delivereth: an empty plundered house, its door broken, the pit and the snare before it, a barred prison window."""
    o = [bg(w, h, "#4A4A5A", "#B8A08A"), ground(w, h, h * 0.76, "#7A6A5A", dy=0)]
    o.append(f'<rect x="{f(w * 0.06)}" y="{f(h * 0.3)}" width="{f(w * 0.3)}" height="{f(h * 0.46)}" fill="#A8987A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.16)} {f(h * 0.76)} L {f(w * 0.16)} {f(h * 0.5)} L {f(w * 0.26)} {f(h * 0.5)} L {f(w * 0.26)} {f(h * 0.76)}" fill="#1A1414" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.26)} {f(h * 0.5)} L {f(w * 0.34)} {f(h * 0.58)} L {f(w * 0.32)} {f(h * 0.78)} L {f(w * 0.26)} {f(h * 0.76)} Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.88)}" rx="{f(w * 0.08)}" ry="{f(h * 0.04)}" fill="#1A1210" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    o.append(f'<rect x="{f(w * 0.64)}" y="{f(h * 0.2)}" width="{f(w * 0.3)}" height="{f(h * 0.56)}" fill="#5A5458" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.72)}" y="{f(h * 0.34)}" width="{f(w * 0.14)}" height="{f(h * 0.16)}" fill="#14121A" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(w * (0.74 + k * 0.03))} {f(h * 0.34)} L {f(w * (0.74 + k * 0.03))} {f(h * 0.5)}" stroke="#8A8A90" stroke-width="3"></path>' for k in range(4)))
    return "".join(o)
