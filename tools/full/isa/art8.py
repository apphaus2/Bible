"""Isaiah 28–30 drawings (on top of isa.art7): the crown of pride of Ephraim's drunkards, precept upon precept, the tried
corner-stone with the line and the plummet (a blueprint), the short bed, the plowman and the threshing of fitches and
cummin, the dreamer, the sealed book, the potter, the beasts of the South, the bulging wall, the beacon on the mountain,
the way behind thee, rain and pasture, the sevenfold light, the storm from far, the pipe in the night, and Topheth."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art7 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
from exo.art8 import bp, dim, tag, title_bar, box

def crown_pride(w, h, seed):
    """Woe to the crown of pride of the drunkards of Ephraim, and to the fading flower of his glorious beauty, which is on the
    head of the fat valley: a wreath of fading flowers lying on a hill above a rich valley, a storm of hail coming over it."""
    r = random.Random(seed)
    o = [bg(w, h, "#3A3A5A", "#C8B888"), hills(w, h, h * 0.6, seed, color="#6A8A4A", amp=10), ground(w, h, h * 0.78, "#7A9A4A", dy=0)]
    o.append(J.city_hill(w * 0.66, h * 0.62, w * 0.2, h * 0.24, seed))
    E2_h = E2.hail(40, 0, w * 0.5, 0, h * 0.5, seed)
    o.append(E2_h)
    s = min(1.3, h / 220); cx, cy = w * 0.3, h * 0.84
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(70 * s)}" ry="{f(18 * s)}" fill="none" stroke="#5A6A2A" stroke-width="{f(8 * s)}"></ellipse>')
    for i in range(12):
        a = i * math.pi * 2 / 12; x = cx + math.cos(a) * 70 * s; y = cy + math.sin(a) * 18 * s
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(7 * s)}" fill="{r.choice(["#C8A060", "#B8785A", "#A8885A"])}" stroke="#0D0D0F" stroke-width="1.2"></circle>')
    return "".join(o)

def toppled_cups(w, h, seed):
    """The priest and the prophet reel with strong drink; all tables are full: a long table after the feast, the cups
    overturned and the wine spilled across the boards, the lamps burned low."""
    r = random.Random(seed)
    o = [rect(w, h, "#2A1A24"), ground(w, h, h * 0.86, "#1A1218", dy=0)]
    s = min(1.2, h / 220); ty = h * 0.62
    o.append(f'<rect x="{f(w * 0.06)}" y="{f(ty)}" width="{f(w * 0.88)}" height="{f(14 * s)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(w * x)}" y="{f(ty + 14 * s)}" width="{f(8 * s)}" height="{f(h * 0.86 - ty - 14 * s)}" fill="#5A3A1E"></rect>' for x in (0.1, 0.5, 0.88)))
    for i in range(9):
        x = w * (0.1 + i * 0.09); rot = r.choice([80, -80, 100, -100, 0])
        o.append(f'<g transform="rotate({rot} {f(x)} {f(ty - 6 * s)})"><path d="M{f(x - 7 * s)} {f(ty - 16 * s)} L {f(x + 7 * s)} {f(ty - 16 * s)} L {f(x + 3 * s)} {f(ty - 4 * s)} L {f(x + 3 * s)} {f(ty)} L {f(x - 3 * s)} {f(ty)} L {f(x - 3 * s)} {f(ty - 4 * s)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></path></g>')
        if rot: o.append(f'<path d="M{f(x)} {f(ty)} q {f(10 * s)} {f(10 * s)} {f(4 * s)} {f(30 * s)}" stroke="#7A0A2A" stroke-width="{f(4 * s)}" fill="none"></path>')
    return "".join(o)

def precept(w, h, seed):
    """Precept upon precept, line upon line, here a little, there a little: a child's writing tablet ruled in short lines,
    the same marks repeated, row upon row."""
    r = random.Random(seed)
    o = [rect(w, h, "#3A2A2A")]
    tw, th = min(w * 0.6, h * 1.4), h * 0.8
    x0, y0 = w * 0.5 - tw / 2, h * 0.1
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(tw)}" height="{f(th)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="3"></rect>')
    rows = max(3, int(th / 26))
    for k in range(rows):
        y = y0 + 18 + k * (th - 30) / max(1, rows - 1)
        x = x0 + 20
        while x < x0 + tw - 30:
            o.append(f'<path d="M{f(x)} {f(y)} l {f(14)} 0 M{f(x + 4)} {f(y - 6)} l 0 12" stroke="#4A2E1A" stroke-width="2.2"></path>'); x += 30
    return "".join(o)

def cornerstone(w, h):
    """Behold, I lay in Zion for a foundation a stone, a tried stone, a precious corner-stone of sure foundation; and I will
    make justice the line, and righteousness the plummet (a blueprint)."""
    o = [bp(w, h), title_bar(w, "A TRIED STONE · A PRECIOUS CORNER-STONE")]
    u = min(w * 0.4, h * 0.6)
    x0, base = w * 0.18, h * 0.88
    o.append(box(x0, base, u * 0.9, u * 0.5, u * 0.45, fill="#C8BC9C", top="#E0D4B4", side="#A89C80"))
    o.append(dim(x0, base + 14, x0 + u * 0.9, base + 14, "SURE FOUNDATION"))
    lx = w * 0.78
    o.append(f'<path d="M{f(lx)} {f(h * 0.14)} L {f(lx)} {f(base - 30)}" stroke="#F3EFE6" stroke-width="1.6"></path>'
             f'<path d="M{f(lx - 10)} {f(base - 30)} L {f(lx + 10)} {f(base - 30)} L {f(lx)} {f(base - 6)} Z" fill="#B87333" stroke="#0D0D0F" stroke-width="1.4"></path>'
             f'<path d="M{f(w * 0.5)} {f(base - u * 0.62)} L {f(w * 0.96)} {f(base - u * 0.62)}" stroke="#FFD23F" stroke-width="1.6" stroke-dasharray="10 4"></path>')
    o.append(tag(lx, h * 0.5, "RIGHTEOUSNESS · THE PLUMMET", lx - 20, h * 0.36) + tag(w * 0.62, base - u * 0.62, "JUSTICE · THE LINE", w * 0.56, base - u * 0.8, color=GOLD))
    return "".join(o)

def short_bed(w, h):
    """The bed is shorter than that a man can stretch himself on it; and the covering narrower than that he can wrap himself
    in it (a plate)."""
    o = [bp(w, h), title_bar(w, "THE BED · THE COVERING")]
    s = min(1.0, h / 200)
    x0, y0 = w * 0.2, h * 0.6
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(w * 0.4)}" height="{f(30 * s)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(x0 + w * 0.05)}" y="{f(y0 - 18 * s)}" width="{f(w * 0.3)}" height="{f(18 * s)}" fill="#5A6A8A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(f'<path d="M{f(x0 - 30)} {f(y0 - 40 * s)} L {f(x0 + w * 0.56)} {f(y0 - 40 * s)}" stroke="#FF8A6A" stroke-width="1.4" stroke-dasharray="6 4"></path>')
    o.append(dim(x0, y0 + 40 * s, x0 + w * 0.4, y0 + 40 * s, "THE BED") + dim(x0 - 30, y0 - 54 * s, x0 + w * 0.56, y0 - 54 * s, "A MAN STRETCHED OUT", color="#FF8A6A"))
    return "".join(o)

def plowman(p, w, h, seed):
    """Doth he that ploweth to sow plow continually? doth he not cast abroad the fitches, and scatter the cummin, and put in the
    wheat in rows, and the barley in the appointed place, and the spelt in the border?: a field in strips — a plowman with
    his oxen, a sower, rows of wheat, the barley and the spelt."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FC8E8", "#F3E8C8"), hills(w, h, h * 0.44, seed, color="#9AA06A", amp=8), ground(w, h, h * 0.5, "#A8885A", dy=0)]
    for k in range(5):
        y = h * (0.56 + k * 0.08)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y - 6)}" stroke="#7A5A3A" stroke-width="2"></path>')
    o.append(R1.field(w * 0.56, w + 10, h * 0.62, h * 0.12, seed, rows=2) + R1.field(w * 0.56, w + 10, h * 0.78, h * 0.1, seed + 1, rows=2, color="#C8B060"))
    k = min(0.5, h / 560)
    o.append(S1.team(w * 0.22, b, k, low=True) if False else S1.cow(w * 0.16, b, k, color="#8A5A30") + S1.cow(w * 0.24, b - 4, k, color="#C9A27A"))
    s = fit(b, max(h * 0.6, b - 130))
    o.append(man(p, w * 0.36, b, s, "#6A5A3A") + f'<path d="M{f(w * 0.36 - 10)} {f(b - 60 * s)} L {f(w * 0.3)} {f(b)}" stroke="#5A3A22" stroke-width="3"></path>')
    o.append(R1.reaper(p, w * 0.5, b - 10, s * 0.9, cloth="#8A6A4A") if False else man(p, w * 0.5, b - 10, s * 0.9, "#7A5A3A", up=[(-22, -158), (-40, -150), (-62, -146)]))
    return "".join(o)

def threshing(w, h):
    """The fitches are beaten out with a staff, and the cummin with a rod; bread grain is ground, the cart wheel turned upon
    it: three cells of a plate."""
    o = [bp(w, h), title_bar(w, "THE FITCHES · THE CUMMIN · BREAD GRAIN")]
    s = min(1.0, h / 200); cw = w / 3; b = h * 0.8
    for i, (nm, tool) in enumerate((("THE FITCHES · A STAFF", "staff"), ("THE CUMMIN · A ROD", "rod"), ("BREAD GRAIN · THE CART WHEEL", "wheel"))):
        cx = cw * (i + 0.5)
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(b)}" rx="{f(cw * 0.36)}" ry="{f(10 * s)}" fill="#C8A060" stroke="#8FD0E2" stroke-width="1.4"></ellipse>')
        if tool == "wheel":
            o.append(f'<circle cx="{f(cx)}" cy="{f(b - 40 * s)}" r="{f(36 * s)}" fill="none" stroke="#B87333" stroke-width="{f(6 * s)}"></circle>'
                     + "".join(f'<path d="M{f(cx)} {f(b - 40 * s)} L {f(cx + math.cos(a) * 36 * s)} {f(b - 40 * s + math.sin(a) * 36 * s)}" stroke="#B87333" stroke-width="3"></path>' for a in [k * math.pi / 4 for k in range(8)]))
        else:
            ln = 90 if tool == "staff" else 60
            o.append(f'<path d="M{f(cx - ln * 0.5 * s)} {f(b - 70 * s)} L {f(cx + ln * 0.5 * s)} {f(b - 10 * s)}" stroke="#8A5A2A" stroke-width="{f((7 if tool == "staff" else 4) * s)}" stroke-linecap="round"></path>')
        o.append(label(cx, b + 26 * s, nm, CYAN, 9))
    return "".join(o)

def dreamer(w, h, seed):
    """As when a hungry man dreameth, and, behold, he eateth; but he awaketh, and his soul is empty: a man asleep on his mat by
    night, over him a faint dream of bread and a cup, beside him an empty bowl."""
    o = [rect(w, h, "#14122A"), mk.stars(30, w, h * 0.4, seed), ground(w, h, h * 0.84, "#2A2430", dy=0)]
    s = min(1.2, h / 260)
    o.append(S1.mat_sleeper(w * 0.4, h * 0.9, s, color="#5A5A7A", head="#8A5A3A"))
    o.append(f'<ellipse cx="{f(w * 0.6)}" cy="{f(h * 0.36)}" rx="{f(w * 0.18)}" ry="{f(h * 0.2)}" fill="#E8E0F8" opacity="0.25"></ellipse>'
             + "".join(f'<circle cx="{f(w * (0.48 + k * 0.03))}" cy="{f(h * (0.66 - k * 0.06))}" r="{f(4 + k * 2)}" fill="#E8E0F8" opacity="0.3"></circle>' for k in range(3))
             + f'<ellipse cx="{f(w * 0.56)}" cy="{f(h * 0.38)}" rx="{f(30 * s)}" ry="{f(12 * s)}" fill="#C8904A" opacity="0.6"></ellipse>'
             f'<path d="M{f(w * 0.66 - 8 * s)} {f(h * 0.3)} L {f(w * 0.66 + 8 * s)} {f(h * 0.3)} L {f(w * 0.66 + 4 * s)} {f(h * 0.3 + 16 * s)} L {f(w * 0.66 - 4 * s)} {f(h * 0.3 + 16 * s)} Z" fill="#E8B830" opacity="0.6"></path>')
    o.append(J1.bowl(w * 0.7, h * 0.88, 40 * s, full=False))
    return "".join(o)

def sealed_book(p, w, h, seed):
    """All vision is become unto you as the words of a book that is sealed: the sealed book held out to one that is learned,
    who turns his palms up — I cannot, for it is sealed."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), rect(w, h, "#3A2A2A"), V.rays(w * 0.5, h * 0.4, 20, 10, max(w, h), color="#E8C88A", op=0.1), ground(w, h, h * 0.86, "#2A1E1A", dy=0)]
    s = min(1.3, h / 240); cx, cy = w * 0.5, h * 0.42
    o.append(f'<rect x="{f(cx - 80 * s)}" y="{f(cy - 20 * s)}" width="{f(160 * s)}" height="{f(40 * s)}" rx="{f(20 * s)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             + "".join(f'<circle cx="{f(cx + (k - 3) * 22 * s)}" cy="{f(cy + 20 * s)}" r="{f(7 * s)}" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.4"></circle>' for k in range(7)))
    fs = fit(b, max(h * 0.5, b - 160))
    o.append(man(p, w * 0.22, b, fs, "#3A4A6A", up=[(-22, -158), (-4, -150), (20, -160)]) + man(p, w * 0.78, b, fs, "#6A3A2A", flip=True, up=[(-22, -158), (-40, -150), (-60, -160)]))
    return "".join(o)

def potter(p, w, h, seed):
    """Shall the potter be esteemed as clay; that the thing made should say of him that made it, He made me not?: a potter at
    his wheel shaping a jar, finished vessels on a shelf behind him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), rect(w, h, "#5A3A2A"), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.4)}" r="{f(max(w, h) * 0.4)}" fill="#8A5A3A" opacity="0.4"></circle>',
         ground(w, h, h * 0.86, "#3A2418", dy=0)]
    s = min(1.2, h / 260)
    for i in range(6):
        x = w * (0.62 + i * 0.06); y = h * 0.4
        o.append(f'<path d="M{f(x - 10 * s)} {f(y)} C {f(x - 18 * s)} {f(y - 20 * s)} {f(x - 8 * s)} {f(y - 36 * s)} {f(x - 5 * s)} {f(y - 40 * s)} L {f(x + 5 * s)} {f(y - 40 * s)} C {f(x + 8 * s)} {f(y - 36 * s)} {f(x + 18 * s)} {f(y - 20 * s)} {f(x + 10 * s)} {f(y)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append(f'<rect x="{f(w * 0.58)}" y="{f(h * 0.4)}" width="{f(w * 0.4)}" height="{f(8 * s)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    wx, wy = w * 0.42, b - 40 * s
    o.append(f'<ellipse cx="{f(wx)}" cy="{f(wy)}" rx="{f(50 * s)}" ry="{f(10 * s)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<rect x="{f(wx - 6 * s)}" y="{f(wy)}" width="{f(12 * s)}" height="{f(b - wy)}" fill="#4A2E1A"></rect>'
             f'<path d="M{f(wx - 24 * s)} {f(wy - 4 * s)} C {f(wx - 32 * s)} {f(wy - 30 * s)} {f(wx - 14 * s)} {f(wy - 50 * s)} {f(wx - 10 * s)} {f(wy - 56 * s)} L {f(wx + 10 * s)} {f(wy - 56 * s)} C {f(wx + 14 * s)} {f(wy - 50 * s)} {f(wx + 32 * s)} {f(wy - 30 * s)} {f(wx + 24 * s)} {f(wy - 4 * s)} Z" fill="#9A6A4A" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(E.kneel(w * 0.22, b, fit(b, max(h * 0.5, b - 170)), color="#6A5A3A", skin="#B98A6E"))
    return "".join(o)

def south_caravan(w, h, seed):
    """The burden of the beasts of the South: through the land of trouble and anguish, the lioness and the viper, they carry
    their riches upon the shoulders of young asses, and their treasures upon the humps of camels, to Egypt."""
    o = [bg(w, h, "#C86A3A", "#F3C890"), ground(w, h, h * 0.64, "#D8A870", dy=0), EG.pyramid(w * 0.92, h * 0.64, w * 0.12, h * 0.12)]
    k = min(0.5, h / 560)
    for i in range(3):
        o.append(J1.camel(w * (0.3 + i * 0.16), h * (0.86 - (i % 2) * 0.04), k, color="#B5844A"))
    for i in range(2):
        o.append(N.ass(w * (0.12 + i * 0.1), h * 0.92, k * 0.9, color="#8A8478") + f'<rect x="{f(w * (0.12 + i * 0.1) - 14 * k)}" y="{f(h * 0.92 - 90 * k)}" width="{f(28 * k)}" height="{f(20 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    o.append(J2.lion(w * 0.84, h * 0.5, min(0.3, h / 700), roar=False, flip=True))
    o.append(SN.snake([(w * 0.7, h * 0.97), (w * 0.74, h * 0.93), (w * 0.78, h * 0.96), (w * 0.8, h * 0.92)], 4, f"sv{seed}", head_scale=0.4))
    return "".join(o)

def bulging_wall(w, h, seed):
    """This iniquity shall be to you as a breach ready to fall, swelling out in a high wall, whose breaking cometh suddenly; he
    shall break it as a potter's vessel is broken, so that there shall not be found a sherd to take fire from the hearth."""
    r = random.Random(seed)
    o = [bg(w, h, "#6A6A7A", "#D8C8A8"), ground(w, h, h * 0.86, "#8A7A5A", dy=0)]
    o.append(f'<path d="M{f(w * 0.08)} {f(h * 0.86)} L {f(w * 0.08)} {f(h * 0.12)} L {f(w * 0.6)} {f(h * 0.12)} C {f(w * 0.68)} {f(h * 0.36)} {f(w * 0.7)} {f(h * 0.6)} {f(w * 0.6)} {f(h * 0.86)} Z" fill="#B8A88A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for k in range(10):
        y = h * (0.16 + k * 0.07)
        o.append(f'<path d="M{f(w * 0.08)} {f(y)} L {f(w * 0.6 + math.sin(k / 10 * math.pi) * w * 0.08)} {f(y)}" stroke="#8A7A5A" stroke-width="1.4"></path>')
    o.append(f'<path d="M{f(w * 0.64)} {f(h * 0.3)} L {f(w * 0.6)} {f(h * 0.4)} L {f(w * 0.66)} {f(h * 0.48)} L {f(w * 0.62)} {f(h * 0.6)}" stroke="#0D0D0F" stroke-width="3" fill="none"></path>')
    for _ in range(12):
        x = r.uniform(w * 0.72, w * 0.96); y = r.uniform(h * 0.88, h * 0.97)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(6, 14))} {f(r.uniform(-6, -2))} l {f(r.uniform(4, 8))} {f(r.uniform(2, 6))} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1"></path>')
    return "".join(o)

def beacon(w, h, seed):
    """Till ye be left as a beacon upon the top of a mountain, and as an ensign on a hill: a lone pole on a bare peak at
    evening, far below a scatter of horsemen in flight."""
    o = [bg(w, h, "#3A2A4A", "#E8906A"), f'<path d="M-10 {f(h + 10)} L {f(w * 0.4)} {f(h * 0.24)} L {f(w * 0.5)} {f(h * 0.2)} L {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} Z" fill="#4A3A3A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.46)} {f(h * 0.22)} L {f(w * 0.46)} {f(h * 0.04)}" stroke="#2A1A10" stroke-width="4"></path>' + E.blaze(w * 0.46, h * 0.06, w * 0.03, h * 0.05, seed, n=3)]
    k = min(0.24, h / 1000)
    for i in range(7):
        o.append(E3.horse(w * (0.66 + i * 0.045), h * (0.88 + (i % 2) * 0.04), k, color="#1A1010"))
    return "".join(o)

def way_voice(p, w, h, seed):
    """Thine ears shall hear a word behind thee, saying, This is the way, walk ye in it: a traveller at a fork of the road,
    the true way going up toward Zion in the light, the side ways turning off into the dark."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#5A6ABA", "#FFE0A8"), J.city_hill(w * 0.6, h * 0.42, w * 0.12, h * 0.14, seed), ground(w, h, h * 0.44, "#B8A070", dy=0)]
    o.append(f'<path d="M{f(w * 0.4)} {f(h + 10)} L {f(w * 0.56)} {f(h * 0.44)} L {f(w * 0.62)} {f(h * 0.44)} L {f(w * 0.6)} {f(h + 10)} Z" fill="#F3E0B0" stroke="#0D0D0F" stroke-width="1.6"></path>'
             f'<path d="M{f(w * 0.46)} {f(h * 0.76)} L {f(w * 0.06)} {f(h * 0.6)} L {f(w * 0.04)} {f(h * 0.66)} L {f(w * 0.44)} {f(h * 0.82)} Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="1.4"></path>'
             f'<path d="M{f(w * 0.58)} {f(h * 0.76)} L {f(w * 0.96)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.66)} L {f(w * 0.59)} {f(h * 0.82)} Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="1.4"></path>')
    o.append(man(p, w * 0.52, b, fit(b, max(h * 0.55, b - 140)), "#4A3A6A"))
    return "".join(o)

def rain_pasture(w, h, seed):
    """He will give the rain for thy seed; in that day shall thy cattle feed in large pastures; the oxen and the young asses
    shall eat savory provender, winnowed with the shovel and with the fork; brooks upon every high hill."""
    r = random.Random(seed)
    o = [bg(w, h, "#7A9AC8", "#E8F0D8")]
    for _ in range(40):
        x = r.uniform(0, w); y = r.uniform(0, h * 0.4)
        o.append(f'<path d="M{f(x)} {f(y)} l -4 12" stroke="#4A6A9A" stroke-width="1.4" opacity="0.6"></path>')
    o.append(hills(w, h, h * 0.44, seed, color="#5E8F3A", amp=14))
    o.append(f'<path d="M{f(w * 0.2)} {f(h * 0.44)} C {f(w * 0.22)} {f(h * 0.6)} {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.36)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="5" fill="none"></path>'
             f'<path d="M{f(w * 0.74)} {f(h * 0.44)} C {f(w * 0.72)} {f(h * 0.6)} {f(w * 0.66)} {f(h * 0.7)} {f(w * 0.62)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="4" fill="none"></path>')
    o.append(ground(w, h, h * 0.6, "#9CCB5E", dy=0) if False else "")
    k = min(0.5, h / 560)
    o.append(S1.cow(w * 0.46, h * 0.9, k, color="#8A5A30") + S1.cow(w * 0.88, h * 0.94, k * 0.9, color="#C9A27A", flip=True, low=True) + N.ass(w * 0.1, h * 0.94, k))
    return "".join(o)

def sevenfold(w, h, seed):
    """The light of the moon shall be as the light of the sun, and the light of the sun sevenfold, as the light of seven
    days: a blazing sun and a moon as bright as a sun over the hills of Zion."""
    o = [bg(w, h, "#FFE680", "#FFF8E0"), V.rays(w * 0.3, h * 0.3, 48, 20, max(w, h) * 1.4, color="#FFFFFF", op=0.5)]
    for k in range(7):
        o.append(f'<circle cx="{f(w * 0.3)}" cy="{f(h * 0.3)}" r="{f(min(w, h) * (0.04 + k * 0.025))}" fill="#FFF4C2" opacity="0.18"></circle>')
    o.append(f'<circle cx="{f(w * 0.3)}" cy="{f(h * 0.3)}" r="{f(min(w, h) * 0.07)}" fill="#FFFFFF"></circle><circle cx="{f(w * 0.78)}" cy="{f(h * 0.22)}" r="{f(min(w, h) * 0.06)}" fill="#FFF4C2" stroke="#FFD23F" stroke-width="3"></circle>')
    o.append(hills(w, h, h * 0.7, seed, color="#C8B060", amp=12) + J.city_hill(w * 0.5, h * 0.9, w * 0.2, h * 0.2, seed))
    return "".join(o)

def storm_far(w, h, seed):
    """Behold, the name of Jehovah cometh from far, burning, in thick rising smoke; with the flame of a devouring fire, with a
    blast, and tempest, and hailstones: a storm of fire and hail sweeping in from the far horizon (no one drawn)."""
    o = [bg(w, h, "#1A0A1A", "#8A3A2A"), smoke(w * 0.7, h * 0.7, 10, seed, r0=h * 0.06, spread=w * 0.12, color="#2A1A1A", op=0.85, rise=0.7)]
    o.append(E.blaze(w * 0.7, h * 0.8, w * 0.4, h * 0.3, seed, n=10))
    o.append(E2.hail(50, 0, w, h * 0.1, h * 0.7, seed) + E2.bolt(w * 0.3, 0, h * 0.5, seed))
    o.append(hills(w, h, h * 0.8, seed, color="#1A1010", amp=10))
    return "".join(o)

def pipe_night(p, w, h, seed):
    """Ye shall have a song as in the night when a holy feast is kept; as when one goeth with a pipe to come unto the
    mountain of Jehovah: pilgrims going up a night road by torchlight, a piper leading, the mount of the house above."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#0B0B2A", "#3A2A5A"), mk.stars(40, w, h * 0.4, seed),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.7)} {f(h * 0.3)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} Z" fill="#2A2440" stroke="#0D0D0F" stroke-width="2"></path>',
         K1.temple_front(w * 0.74, h * 0.32, min(w * 0.12, h * 0.26), seed), ground(w, h, h * 0.86, "#1A1630", dy=0)]
    s = fit(b, max(h * 0.55, b - 150))
    for i in range(5):
        x = w * (0.12 + i * 0.1); y = b - i * h * 0.05
        o.append(man(p, x, y, s * (1 - i * 0.08), ["#5A3A6A", "#2A5A7A", "#8A3A2A", "#3A6A3A", "#7A6A2A"][i]))
        if i % 2: o.append(E.blaze(x + 14 * s, y - 210 * s, 10 * s, 24 * s, seed + i, n=3))
    o.append(S3.notes(w * 0.62, h * 0.5, 4, seed, color="#FFE680"))
    return "".join(o)

def topheth(w, h, seed):
    """A Topheth is prepared of old; he hath made it deep and large; the pile thereof is fire and much wood; the breath of
    Jehovah, like a stream of brimstone, doth kindle it: a deep pit in a valley, a great pile of wood burning in it."""
    o = [bg(w, h, "#2A0A0A", "#8A3A1A"), f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.3)} {f(h * 0.56)} L {f(w * 0.36)} {f(h * 0.9)} L {f(w * 0.64)} {f(h * 0.9)} L {f(w * 0.7)} {f(h * 0.56)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A2018" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = min(1.2, h / 260)
    for k in range(5):
        o.append(f'<path d="M{f(w * 0.4)} {f(h * 0.88 - k * 10 * s)} L {f(w * 0.6)} {f(h * 0.86 - k * 10 * s)}" stroke="#5A3A1E" stroke-width="{f(8 * s)}"></path>')
    o.append(E.blaze(w * 0.5, h * 0.84, w * 0.24, h * 0.5, seed, n=9) + smoke(w * 0.5, h * 0.3, 7, seed, r0=h * 0.05, color="#2A1A1A", op=0.6))
    return "".join(o)
