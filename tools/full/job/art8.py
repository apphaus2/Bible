"""Drawings for Job 25–28 (Bildad's third speech, Job's answer, his parable, and where shall wisdom be found): the mine
in section and the measures of creation drawn as technical plates."""
from job.art7 import *
from job.art7 import f, K2, K3, sea, label, SHIELD

def moon_worm(w, h, seed):
    """Even the moon hath no brightness, and the stars are not pure in his sight; how much less man, that is a worm: a full
    moon dimmed by haze over the stars, and in the dust at the foot of the panel a worm."""
    o = [K2.sky(w, h, "#05051A", "#1E1A3A"), mk.stars(120, w, h * 0.8, seed, color="#A8A8C8"), J.moon(w * 0.7, h * 0.6, min(34, h * 0.1)),
         f'<circle cx="{f(w * 0.7)}" cy="{f(h * 0.6)}" r="{f(min(34, h * 0.1) * 1.6)}" fill="#3A3A5A" opacity="0.45"></circle>', ground(w, h, h * 0.9, "#3A2E28", dy=0)]
    x, y = w * 0.3, h * 0.95
    o.append(f'<path d="M{f(x)} {f(y)} C {f(x + 14)} {f(y - 10)} {f(x + 28)} {f(y + 6)} {f(x + 44)} {f(y - 4)}" stroke="#C88A8A" stroke-width="6" stroke-linecap="round" fill="none"></path>')
    return "".join(o)

def deep_section(w, h, seed):
    """They that are deceased tremble beneath the waters; Sheol is naked before God, and Abaddon hath no covering: a section
    through the sea and the deep below it, layer under layer down into the dark, laid open."""
    o = [K2.sky(w, h, "#5A8AB8", "#C8E0F0")]
    y0 = h * 0.62
    o.append(f'<rect x="-10" y="{f(y0)}" width="{f(w + 20)}" height="{f(h * 0.12)}" fill="#1F6F9A"></rect>'
             f'<rect x="-10" y="{f(y0 + h * 0.12)}" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#3A2A2A"></rect>'
             f'<rect x="-10" y="{f(y0 + h * 0.22)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#0B0606"></rect>'
             f'<path d="M-10 {f(y0)} L {f(w + 10)} {f(y0)}" stroke="#E8F6FA" stroke-width="2"></path>')
    o.append(label(w * 0.86, y0 + h * 0.07, "THE WATERS", "#E8F6FA", 9) + label(w * 0.86, y0 + h * 0.18, "BENEATH", "#C8A88A", 9) + label(w * 0.86, y0 + h * 0.3, "SHEOL · ABADDON", "#FF8A6A", 9))
    o.append(f'<path d="M{f(w * 0.06)} {f(y0 + h * 0.24)} L {f(w * 0.7)} {f(y0 + h * 0.24)}" stroke="#FF8A6A" stroke-width="1.4" stroke-dasharray="6 5"></path>')
    return "".join(o)

def hung_nothing(w, h, seed):
    """He stretcheth out the north over empty space, and hangeth the earth upon nothing: the round earth hanging in the dark,
    its seas and lands lit on one side, nothing under it but stars."""
    o = [rect(w, h, "#020210"), mk.stars(180, w, h, seed)]
    R = min(h * 0.22, w * 0.18); cx, cy = w * 0.5, h * 0.74
    o.append(f'<defs><radialGradient id="ea{seed}" cx="0.35" cy="0.35" r="0.8"><stop offset="0" stop-color="#5AA8C8"></stop><stop offset="0.7" stop-color="#1F4A6A"></stop><stop offset="1" stop-color="#05101A"></stop></radialGradient></defs>'
             f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R)}" fill="url(#ea{seed})" stroke="#0D0D0F" stroke-width="2"></circle>'
             f'<path d="M{f(cx - R * 0.6)} {f(cy - R * 0.3)} C {f(cx - R * 0.3)} {f(cy - R * 0.6)} {f(cx + R * 0.1)} {f(cy - R * 0.2)} {f(cx - R * 0.1)} {f(cy + R * 0.1)} C {f(cx - R * 0.4)} {f(cy + R * 0.3)} {f(cx - R * 0.7)} {f(cy)} {f(cx - R * 0.6)} {f(cy - R * 0.3)} Z" fill="#6A8A4A" opacity="0.8"></path>'
             f'<path d="M{f(cx + R * 0.2)} {f(cy + R * 0.3)} C {f(cx + R * 0.5)} {f(cy + R * 0.1)} {f(cx + R * 0.7)} {f(cy + R * 0.4)} {f(cx + R * 0.4)} {f(cy + R * 0.6)} Z" fill="#8A7A4A" opacity="0.7"></path>'
             f'<path d="M{f(cx + R * 0.2)} {f(cy - R)} A {f(R)} {f(R)} 0 0 1 {f(cx + R * 0.2)} {f(cy + R)} A {f(R * 0.6)} {f(R)} 0 0 0 {f(cx + R * 0.2)} {f(cy - R)} Z" fill="#000000" opacity="0.35"></path>')
    return "".join(o)

def light_bound(w, h, seed):
    """He hath described a boundary upon the face of the waters, unto the confines of light and darkness; he bindeth up the
    waters in his thick clouds: the open sea under heavy clouds, the light on one side and the night on the other, a line
    drawn across the water between them."""
    o = [f'<defs><linearGradient id="lb{seed}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFE6A0"></stop><stop offset="0.48" stop-color="#8FB8D8"></stop><stop offset="0.52" stop-color="#1A1A3A"></stop><stop offset="1" stop-color="#05051A"></stop></linearGradient></defs>'
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#lb{seed})"></rect>', mk.stars(40, w * 0.45, h * 0.7, seed).replace("<g ", f'<g transform="translate({f(w * 0.55)} 0)" '),
         clouds(w, h * 0.6, seed, 9, color="#5A5A6A", op=0.9, ry=0.06, h=h),
         f'<rect x="-10" y="{f(h * 0.78)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#1F4A6A"></rect>',
         f'<rect x="{f(w * 0.5)}" y="{f(h * 0.78)}" width="{f(w * 0.6)}" height="{f(h * 0.3)}" fill="#0B1A2A"></rect>',
         f'<path d="M{f(w * 0.5)} {f(h * 0.78)} L {f(w * 0.5)} {f(h + 10)}" stroke="#FFD23F" stroke-width="2" stroke-dasharray="7 6"></path>']
    return "".join(o)

def silver_dust(w, h, seed):
    """Though he heap up silver as the dust, and prepare raiment as the clay, the just shall put it on, and the innocent
    shall divide the silver: heaps of silver pieces and piles of folded garments in a storeroom."""
    r = random.Random(seed)
    o = [rect(w, h, "#3A2E2A"), f'<circle cx="{f(w * 0.4)}" cy="{f(h * 0.9)}" r="{f(h * 0.3)}" fill="#FFC14D" opacity="0.1"></circle>', ground(w, h, h * 0.92, "#2A2018", dy=0)]
    for cx in (0.2, 0.42):
        for i in range(40):
            a = r.uniform(0, math.pi); rr = r.uniform(0, 1) ** 0.5
            x = w * cx + math.cos(a) * rr * w * 0.1; y = h * 0.94 - math.sin(a) * rr * h * 0.12
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="6" ry="3" fill="#D8D8E0" stroke="#5A5A6A" stroke-width="1"></ellipse>')
    for i in range(5):
        y = h * (0.94 - i * 0.03)
        o.append(f'<rect x="{f(w * 0.62)}" y="{f(y - h * 0.03)}" width="{f(w * 0.22)}" height="{f(h * 0.03)}" fill="{["#B5121B", "#1F5FAD", "#E8B830", "#2E6B3A", "#7A3BA8"][i]}" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    return "".join(o)

def booth(w, h, seed):
    """He buildeth his house as the moth, and as a booth which the keeper maketh: a flimsy watchman's booth of poles and
    branches in a vineyard, leaning in the wind."""
    o = [K2.sky(w, h, "#8FD0E2", "#E8F0D8"), ground(w, h, h * 0.84, "#9A8A5A", dy=0)]
    for i in range(10):
        x = w * (0.05 + i * 0.1)
        o.append(f'<path d="M{f(x)} {f(h * 0.98)} L {f(x)} {f(h * 0.86)}" stroke="#6A4A2A" stroke-width="3"></path><ellipse cx="{f(x)}" cy="{f(h * 0.86)}" rx="16" ry="8" fill="#4A8A3A" stroke="#0D0D0F" stroke-width="1.2"></ellipse>')
    cx = w * 0.55
    o.append(f'<g transform="rotate(-6 {f(cx)} {f(h * 0.96)})">' + f'<path d="M{f(cx - 40)} {f(h * 0.96)} L {f(cx - 34)} {f(h * 0.7)} M{f(cx + 40)} {f(h * 0.96)} L {f(cx + 34)} {f(h * 0.7)}" stroke="#6A4A2A" stroke-width="5"></path>'
             + P(f"M{f(cx - 54)} {f(h * 0.72)} L {f(cx)} {f(h * 0.62)} L {f(cx + 54)} {f(h * 0.72)} Z", "#8A9A4A", 2)
             + f'<path d="M{f(cx - 34)} {f(h * 0.82)} L {f(cx + 34)} {f(h * 0.82)}" stroke="#6A4A2A" stroke-width="4"></path></g>')
    return "".join(o)

def mine(p, w, h, seed):
    """Surely there is a mine for silver, and a place for gold which they refine; he breaketh open a shaft away from where
    men sojourn; they hang afar from men, they swing to and fro: a section through the mountain — the shaft, the miners
    hanging on ropes with their lamps, the galleries following veins of silver and gold, the ore going up in baskets."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#E8E0C8")]
    top = h * 0.4
    o.append(P(f"M-10 {f(h + 10)} L -10 {f(top + 40)} L {f(w * 0.3)} {f(top)} L {f(w * 0.6)} {f(top + 30)} L {f(w + 10)} {f(top + 10)} L {f(w + 10)} {f(h + 10)} Z", "#6A5444"))
    for k in range(5):
        y = top + 60 + k * (h - top) / 5
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 20)} {f(w * 0.6)} {f(y + 20)} {f(w + 10)} {f(y)}" stroke="#5A4434" stroke-width="2" fill="none"></path>')
    sx = w * 0.3
    o.append(f'<rect x="{f(sx - 14)}" y="{f(top - 4)}" width="28" height="{f(h - top)}" fill="#120A08" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(sx - 30)} {f(top)} L {f(sx)} {f(top - 40)} L {f(sx + 30)} {f(top)}" stroke="#5A3A1E" stroke-width="5" fill="none"></path>')
    for gy, gx0, gx1 in ((0.6, 0.3, 0.9), (0.78, 0.04, 0.3), (0.92, 0.3, 0.8)):
        o.append(f'<rect x="{f(w * gx0)}" y="{f(h * gy - 12)}" width="{f(w * (gx1 - gx0))}" height="24" fill="#120A08" stroke="#0D0D0F" stroke-width="1.6"></rect>')
        for i in range(4):
            x = w * (gx0 + (gx1 - gx0) * (i + 0.5) / 4)
            o.append(f'<circle cx="{f(x)}" cy="{f(h * gy - 4)}" r="3" fill="#FFC14D"></circle><circle cx="{f(x)}" cy="{f(h * gy - 4)}" r="9" fill="#FFC14D" opacity="0.25"></circle>')
    for i in range(14):
        x = r.uniform(0, w); y = r.uniform(top + 50, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(10, 40))} {f(r.uniform(-6, 6))}" stroke="{r.choice(["#D8D8E0", "#E8B830"])}" stroke-width="3" stroke-linecap="round"></path>')
    for i, y in enumerate((0.5, 0.68)):
        o.append(f'<path d="M{f(sx)} {f(top - 40)} L {f(sx - 2 + i * 4)} {f(h * y - 16)}" stroke="#C8A878" stroke-width="1.6"></path>'
                 + mk.person(p, round(sx), round(h * y + 10), round(min(0.16, h / 2200), 3), body="#3A1E14", cloth="#7A6A5A", kind="Tunic", sw=3, up=[(-22, -158), (-6, -190), (0, -224)]))
    o.append(label(w * 0.62, h * 0.6 + 26, "SILVER", "#D8D8E0", 9) + label(w * 0.17, h * 0.78 + 26, "GOLD", "#FFD23F", 9) + label(w * 0.55, h * 0.92 + 26, "IRON · COPPER", "#C8A88A", 9))
    return "".join(o)

def bread_fire(w, h, seed):
    """As for the earth, out of it cometh bread; and underneath it is turned up as it were by fire; the stones thereof are
    the place of sapphires: a field of grain above, and under it in section the rock glowing as with fire, blue sapphires
    and dust of gold."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8FD0E2", "#F0F0D8"), f'<rect x="-10" y="{f(h * 0.72)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#3A2420"></rect>']
    for i in range(50):
        x = w * i / 49
        o.append(f'<path d="M{f(x)} {f(h * 0.72)} L {f(x + 2)} {f(h * 0.64)}" stroke="#C8A040" stroke-width="2"></path><ellipse cx="{f(x + 2)}" cy="{f(h * 0.63)}" rx="3" ry="7" fill="#E8C050"></ellipse>')
    o.append(f'<path d="M-10 {f(h * 0.72)} L {f(w + 10)} {f(h * 0.72)}" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.98)}" rx="{f(w * 0.5)}" ry="{f(h * 0.12)}" fill="#D7261E" opacity="0.4"></ellipse>')
    for i in range(10):
        x = r.uniform(0, w); y = h * r.uniform(0.78, 0.98)
        o.append(f'<path d="M{f(x)} {f(y - 8)} L {f(x + 7)} {f(y)} L {f(x)} {f(y + 8)} L {f(x - 7)} {f(y)} Z" fill="#2C5FDA" stroke="#0D0D0F" stroke-width="1.2"></path>')
    for i in range(30):
        o.append(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(h * r.uniform(0.76, 1.0))}" r="1.6" fill="#FFD23F"></circle>')
    return "".join(o)

def falcon_path(w, h, seed):
    """That path no bird of prey knoweth, neither hath the falcon's eye seen it; the fierce lion hath not passed thereby: a
    falcon hanging over bare mountains, a lion on the ridge, and the mine's mouth hidden in the rock below them."""
    import exo.art6 as A6
    o = [K2.sky(w, h, "#8FB8D8", "#E8E0C8"), P(f"M-10 {f(h + 10)} L {f(w * 0.2)} {f(h * 0.7)} L {f(w * 0.46)} {f(h * 0.82)} L {f(w * 0.7)} {f(h * 0.68)} L {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} Z", "#8A7060"),
         A6.eagle(w * 0.46, h * 0.78, min(0.7, h / 500)), J2.lion(w * 0.74, h * 0.74, min(0.24, h / 1300), roar=False),
         f'<path d="M{f(w * 0.28)} {f(h * 0.96)} L {f(w * 0.28)} {f(h * 0.9)} Q {f(w * 0.31)} {f(h * 0.86)} {f(w * 0.34)} {f(h * 0.9)} L {f(w * 0.34)} {f(h * 0.96)} Z" fill="#120A08" stroke="#0D0D0F" stroke-width="1.6"></path>']
    return "".join(o)

def channels(w, h, seed):
    """He putteth forth his hand upon the flinty rock; he cutteth out channels among the rocks; he bindeth the streams that
    they trickle not: rock cut away in steps, a channel hewn through it carrying the stream aside, a dam of stones."""
    o = [K2.sky(w, h, "#8FB8D8", "#E8E0C8"), P(f"M-10 {f(h + 10)} L -10 {f(h * 0.72)} L {f(w * 0.2)} {f(h * 0.72)} L {f(w * 0.2)} {f(h * 0.8)} L {f(w * 0.4)} {f(h * 0.8)} L {f(w * 0.4)} {f(h * 0.88)} L {f(w + 10)} {f(h * 0.88)} L {f(w + 10)} {f(h + 10)} Z", "#8A7A6A"),
         f'<path d="M-10 {f(h * 0.76)} L {f(w * 0.2)} {f(h * 0.76)} L {f(w * 0.2)} {f(h * 0.84)} L {f(w * 0.4)} {f(h * 0.84)} L {f(w * 0.4)} {f(h * 0.92)} L {f(w + 10)} {f(h * 0.92)}" stroke="#5AA8C8" stroke-width="8" fill="none"></path>',
         S4.stone_heap(w * 0.7, h * 0.88, w * 0.12, h * 0.06, seed)]
    return "".join(o)

def jewels(w, h, seed):
    """It cannot be gotten for gold, nor valued with the gold of Ophir, the precious onyx, or the sapphire; coral, crystal,
    rubies, the topaz of Ethiopia: the treasures laid out on a cloth — gold, onyx, sapphire, coral, crystal, ruby, topaz —
    each named, and beside them a balance with its pan empty."""
    o = [rect(w, h, "#2A1A2A"), P(f"M{f(w * 0.04)} {f(h * 0.98)} L {f(w * 0.1)} {f(h * 0.76)} L {f(w * 0.7)} {f(h * 0.76)} L {f(w * 0.72)} {f(h * 0.98)} Z", "#5A2A5A")]
    items = [("GOLD", "#FFD23F"), ("ONYX", "#2A2A2A"), ("SAPPHIRE", "#2C5FDA"), ("CORAL", "#FF7A6A"), ("CRYSTAL", "#E8F6FA"), ("RUBY", "#C8102E"), ("TOPAZ", "#E8A830")]
    for i, (nm, c) in enumerate(items):
        x = w * (0.14 + i * 0.08); y = h * (0.84 + (i % 2) * 0.06)
        o.append(f'<path d="M{f(x)} {f(y - 10)} L {f(x + 10)} {f(y)} L {f(x)} {f(y + 8)} L {f(x - 10)} {f(y)} Z" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 f'<path d="M{f(x - 4)} {f(y - 5)} L {f(x + 3)} {f(y - 2)}" stroke="#FFFFFF" stroke-width="1.4" opacity="0.7"></path>' + label(x, y + 22, nm, "#F3EFE6", 8))
    bx = w * 0.86; k = min(1.0, h / 320)
    o.append(f'<g transform="translate({f(bx)} {f(h * 0.98)}) scale({f(k)})"><path d="M0 0 L 0 -110" stroke="#B5844A" stroke-width="5"></path><path d="M-60 -110 L 60 -110" stroke="#E8B830" stroke-width="4"></path>'
             '<path d="M-60 -110 L -80 -70 M-60 -110 L -40 -70 M60 -110 L 40 -70 M60 -110 L 80 -70" stroke="#F3EFE6" stroke-width="1.2"></path>'
             '<path d="M-84 -70 Q -60 -56 -36 -70 Z M36 -70 Q 60 -56 84 -70 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path></g>')
    return "".join(o)

def measures2(w, h, seed):
    """To make a weight for the wind, to mete out the waters by measure, a decree for the rain and a way for the lightning of
    the thunder: a blueprint plate — the wind in a balance, the waters in a measuring vessel, the rain falling in ruled
    lines, the lightning's path drawn with its arrow."""
    o = [grid_bg(w, h)]
    y = h * 0.78; k = min(0.9, h / 400)
    def cap(x, t): return label(x, h * 0.9, t, "#8FD0E2", 9)
    x = w * 0.14
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})"><path d="M0 30 L 0 -60 M-50 -60 L 50 -60" stroke="#8FD0E2" stroke-width="2" fill="none"></path>'
             '<path d="M-50 -60 L -66 -20 L -34 -20 Z M50 -60 L 34 -20 L 66 -20 Z" fill="none" stroke="#8FD0E2" stroke-width="1.6"></path>'
             '<path d="M-64 -30 C -56 -40 -46 -26 -38 -36" stroke="#F3EFE6" stroke-width="2" fill="none"></path></g>' + cap(x, "A WEIGHT FOR THE WIND"))
    x = w * 0.38
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})"><path d="M-30 30 L -30 -60 M30 30 L 30 -60 M-30 30 L 30 30" stroke="#8FD0E2" stroke-width="2" fill="none"></path>'
             '<rect x="-29" y="-10" width="58" height="40" fill="#2C7DA0" opacity="0.7"></rect>'
             + "".join(f'<path d="M30 {yy} L 40 {yy}" stroke="#8FD0E2" stroke-width="1.4"></path>' for yy in range(-50, 30, 10)) + '</g>' + cap(x, "THE WATERS BY MEASURE"))
    x = w * 0.62
    o.append("".join(f'<path d="M{f(x - 40 + i * 12)} {f(y - 60 * k)} L {f(x - 46 + i * 12)} {f(y + 20 * k)}" stroke="#8FD0E2" stroke-width="1.6" stroke-dasharray="6 4"></path>' for i in range(8))
             + cap(x, "A DECREE FOR THE RAIN"))
    x = w * 0.86
    o.append(f'<path d="M{f(x)} {f(y - 70 * k)} l -14 {f(30 * k)} l 16 0 l -16 {f(50 * k)}" stroke="#FFD23F" stroke-width="2.6" fill="none"></path>'
             f'<path d="M{f(x - 14)} {f(y + 10 * k)} l -4 -12 l 10 6 Z" fill="#FFD23F"></path>' + cap(x, "A WAY FOR THE LIGHTNING"))
    return "".join(o)
