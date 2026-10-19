"""Drawings for Job 4–7 (Eliphaz's first speech and Job's answer): the images of the poetry, each with its subject in the
lower part of the panel so the song lines above leave it clear."""
from job.art import *
from job.art import f, K2, K3
import judges2 as J2

def thorn_field(w, h, seed):
    """They that plow iniquity, and sow trouble, reap the same; by the blast of his anger are they consumed: a field of
    thorns and thistles under a hot white sun, the east wind's blast streaking across it, a sickle cast down."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#E8D8A0", "#F3C88A"), sun(w * 0.8, h * 0.2, min(26, h * 0.07), color="#FFF4C2", op=0.3), ground(w, h, h * 0.72, "#B8905A", dy=0)]
    for i in range(10):
        y = h * (0.1 + i * 0.07)
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 14)} {f(w * 0.6)} {f(y + 14)} {f(w + 10)} {f(y - 4)}" fill="none" stroke="#FFF4C2" stroke-width="{2 + i % 3}" opacity="0.45"></path>')
    for i in range(26):
        x = r.uniform(0, w); y = r.uniform(h * 0.76, h * 1.02); s = r.uniform(0.6, 1.2) * min(1.4, h / 300)
        o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M0 0 L -6 -30 M0 0 L 2 -38 M0 0 L 10 -26 M-4 -18 L -12 -22 M3 -24 L 10 -30" stroke="#3A3A22" stroke-width="2.6" fill="none"></path>'
                 f'<circle cx="2" cy="-40" r="5" fill="#8A4A8A" stroke="#0D0D0F" stroke-width="1.4"></circle></g>')
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.9)} q 30 -30 60 -6" fill="none" stroke="#8A8A9A" stroke-width="5" stroke-linecap="round"></path><path d="M{f(w * 0.3)} {f(h * 0.9)} l -26 10" stroke="#5A3A1E" stroke-width="6" stroke-linecap="round"></path>')
    return "".join(o)

def lions(w, h, seed):
    """The old lion perisheth for lack of prey, and the whelps of the lioness are scattered abroad: a gaunt old lion lying
    in the dry grass, two whelps running off over the plain."""
    k = min(1.0, h / 380)
    o = [K2.sky(w, h, "#E8B880", "#F3D8A0"), hills(w, h, h * 0.7, seed, "#B88A5A", amp=8, step=90), ground(w, h, h * 0.78, "#C8A06A", dy=0),
         J2.lion(w * 0.2, h * 0.98, k * 0.9, roar=True),
         J2.lion(w * 0.66, h * 0.9, k * 0.42, flip=True, roar=False), J2.lion(w * 0.86, h * 0.86, k * 0.36, roar=False)]
    o.append(mk.speed(w * 0.78, h * 0.8, 10, 10, w * 0.2, seed, color="#8A6A3A", op=0.5))
    return "".join(o)

def night_spirit(w, h, seed):
    """In thoughts from the visions of the night, when deep sleep falleth on men: a sleeper on his bed in a dark chamber,
    and a pale form without appearance passing before his face (no face is drawn in it)."""
    o = [rect(w, h, "#0F0E2A"), f'<rect x="{f(w * 0.06)}" y="{f(h * 0.1)}" width="{f(w * 0.16)}" height="{f(h * 0.3)}" fill="#1E2A5A" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         mk.stars(10, w * 0.16, h * 0.3, seed).replace("<g ", f'<g transform="translate({f(w * 0.06)} {f(h * 0.1)})" ')]
    o.append(K1.bed(w, h, w * 0.08, w * 0.5, h * 0.98, cover="#3A2A4A", head="#C98E66", hair="#E8E2D6"))
    cx = w * 0.66
    o.append(f'<defs><radialGradient id="sp{seed}" cx="0.5" cy="0.4" r="0.6"><stop offset="0" stop-color="#E8F0FF" stop-opacity="0.85"></stop><stop offset="1" stop-color="#8A9AC8" stop-opacity="0"></stop></radialGradient></defs>'
             f'<path d="M{f(cx - w * 0.06)} {f(h * 0.98)} C {f(cx - w * 0.14)} {f(h * 0.6)} {f(cx - w * 0.04)} {f(h * 0.2)} {f(cx + w * 0.02)} {f(h * 0.04)} C {f(cx + w * 0.1)} {f(h * 0.3)} {f(cx + w * 0.16)} {f(h * 0.7)} {f(cx + w * 0.1)} {f(h * 0.98)} Z" fill="url(#sp{seed})"></path>')
    for i in range(5):
        y = h * (0.3 + i * 0.13)
        o.append(f'<path d="M{f(cx + w * 0.1)} {f(y)} C {f(cx + w * 0.2)} {f(y - 10)} {f(cx + w * 0.26)} {f(y + 10)} {f(cx + w * 0.34)} {f(y)}" fill="none" stroke="#C8D8FF" stroke-width="2" opacity="0.5"></path>')
    return "".join(o)

def clay_houses(w, h, seed):
    """Them that dwell in houses of clay, whose foundation is in the dust, who are crushed before the moth; their tent-cord
    plucked up: mud houses on the dust at evening, a tent fallen in on its pole, and a great moth at rest in the foreground."""
    o = [K2.sky(w, h, "#5A4A6A", "#E8A06A"), ground(w, h, h * 0.8, "#A8865A", dy=0)]
    for i in range(4):
        x = w * (0.04 + i * 0.13); hh = h * (0.12 + (i % 2) * 0.04)
        o.append(house(x, h * 0.84, w * 0.1, hh, color="#B8885A"))
    o.append(P(f"M{f(w * 0.6)} {f(h * 0.86)} L {f(w * 0.68)} {f(h * 0.74)} L {f(w * 0.74)} {f(h * 0.8)} L {f(w * 0.86)} {f(h * 0.86)} Z", "#3A2A22", 2.2)
             + f'<path d="M{f(w * 0.68)} {f(h * 0.74)} L {f(w * 0.72)} {f(h * 0.66)}" stroke="#5A3A1E" stroke-width="4"></path>'
             + f'<path d="M{f(w * 0.86)} {f(h * 0.86)} C {f(w * 0.9)} {f(h * 0.84)} {f(w * 0.93)} {f(h * 0.9)} {f(w * 0.96)} {f(h * 0.88)}" fill="none" stroke="#C8A878" stroke-width="2"></path>')
    s = min(1.2, h / 300); x, y = w * 0.42, h * 0.92
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
             + P("M0 0 C -20 -30 -60 -36 -70 -14 C -64 4 -30 10 0 0 Z", "#A8987A", 1.8) + P("M0 0 C 20 -30 60 -36 70 -14 C 64 4 30 10 0 0 Z", "#A8987A", 1.8)
             + P("M0 0 C -14 6 -40 20 -44 32 C -26 30 -8 16 0 0 Z", "#8A7A62", 1.6) + P("M0 0 C 14 6 40 20 44 32 C 26 30 8 16 0 0 Z", "#8A7A62", 1.6)
             + '<ellipse cx="0" cy="4" rx="5" ry="16" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
             + '<path d="M-2 -10 C -10 -24 -18 -28 -24 -30 M2 -10 C 10 -24 18 -28 24 -30" fill="none" stroke="#0D0D0F" stroke-width="1.4"></path>'
             + '<circle cx="-40" cy="-16" r="5" fill="#5A4A3A"></circle><circle cx="40" cy="-16" r="5" fill="#5A4A3A"></circle></g>')
    return "".join(o)

def sparks(w, h, seed):
    """Man is born unto trouble, as the sparks fly upward: a fire of thorns in the dark, its sparks streaming up into the night."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#05050F", "#2A1A2A"), ground(w, h, h * 0.9, "#1A1210", dy=0),
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.9)}" r="{f(h * 0.3)}" fill="#FF6A2A" opacity="0.18"></circle>',
         E.blaze(w * 0.5, h * 0.95, w * 0.2, h * 0.22, seed, n=7)]
    for i in range(70):
        y = r.uniform(0, h * 0.8); spread = (h * 0.8 - y) / h
        x = w * 0.5 + r.gauss(0, 1) * w * (0.04 + spread * 0.3)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(1, 2.6))}" fill="{r.choice(["#FFD23F", "#FF8A3D", "#FFF4C2"])}" opacity="{r.uniform(0.5, 1):.2f}"></circle>')
    return "".join(o)

def rain_fields(w, h, seed):
    """Who giveth rain upon the earth, and sendeth waters upon the fields: rain from grey clouds over green fields and a
    full stream."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#5A6A7A", "#B8C8C8"), clouds(w, h * 0.08, seed, 8, color="#4A5A6A", op=0.9, ry=0.08, h=h),
         hills(w, h, h * 0.72, seed, "#2E6B3A", amp=10, step=90), ground(w, h, h * 0.8, "#4A8A3A", dy=0)]
    for i in range(5): o.append(f'<path d="M-10 {f(h * (0.84 + i * 0.035))} L {f(w + 10)} {f(h * (0.82 + i * 0.035))}" stroke="#9CCB5E" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.6)} {f(h * 0.8)} C {f(w * 0.55)} {f(h * 0.88)} {f(w * 0.75)} {f(h * 0.92)} {f(w * 0.7)} {f(h + 10)}" fill="none" stroke="#8FD0E2" stroke-width="14"></path>')
    for i in range(90):
        x = r.uniform(0, w + 40); y = r.uniform(0, h)
        o.append(f'<path d="M{f(x)} {f(y)} l -6 18" stroke="#DCEFF8" stroke-width="1.4" opacity="0.7"></path>')
    return "".join(o)

def shocks(p, w, h, seed):
    """Thou shalt come to thy grave in a full age, like as a shock of grain cometh in in its season: shocks of grain in a
    reaped field at evening, a tent in peace beyond and the fold."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A4A7A", "#F3B87A"), sun(w * 0.86, h * 0.72, min(24, h * 0.06), color="#FFB04A", op=0.3),
         hills(w, h, h * 0.74, seed, "#7A5A4A", amp=8, step=90), ground(w, h, h * 0.8, "#E8C070", dy=0),
         A.black_tent(w * 0.1, h * 0.8, w * 0.16, h * 0.1, color="#3A2A22"), flock(w * 0.3, w * 0.46, h * 0.78, h * 0.82, 6, seed, cows=0, smin=0.1, smax=0.14)]
    k = min(1.2, h / 300)
    for i in range(6):
        x = w * (0.52 + (i % 3) * 0.15) + (i // 3) * 30; y = h * (0.92 + (i // 3) * 0.05)
        o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k * (0.8 + (i // 3) * 0.2))})">'
                 + P("M-24 0 L -6 -50 L 6 -50 L 24 0 Z", "#E8B840", 2) + P("M-10 -46 L 0 -66 L 10 -46 Z", "#D8A830", 1.6)
                 + '<path d="M-14 -22 L 14 -22" stroke="#8A5A1E" stroke-width="3"></path><path d="M-16 0 L -8 -40 M0 0 L 0 -44 M16 0 L 8 -40" stroke="#B88A2A" stroke-width="1.4"></path></g>')
    return "".join(o)

def balances(w, h, seed):
    """Oh that my vexation were but weighed, and all my calamity laid in the balances! heavier than the sand of the seas: a
    great balance on the shore, one pan sunk under a heap of sand, the sea behind."""
    o = [K2.sky(w, h, "#5A5A7A", "#C8C0B0"), f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h * 0.12)}" fill="#3A6A8A"></rect>',
         f'<path d="M-10 {f(h * 0.7)} L {f(w + 10)} {f(h * 0.7)}" stroke="#CFEFFF" stroke-width="2"></path>', ground(w, h, h * 0.82, "#D8C08A", dy=0)]
    cx, by = w * 0.5, h * 0.98; k = min(1.2, h / 320)
    o.append(f'<g transform="translate({f(cx)} {f(by)}) scale({f(k)})">'
             + P("M-30 0 L 30 0 L 10 -20 L -10 -20 Z", "#8A5A30") + '<path d="M0 -20 L 0 -150" stroke="#0D0D0F" stroke-width="9"></path><path d="M0 -20 L 0 -150" stroke="#B5844A" stroke-width="6"></path>'
             + '<g transform="rotate(-14 0 -150)"><path d="M-120 -150 L 120 -150" stroke="#0D0D0F" stroke-width="8"></path><path d="M-120 -150 L 120 -150" stroke="#E8B830" stroke-width="5"></path>'
             + '<path d="M-120 -150 L -150 -90 M-120 -150 L -90 -90 M120 -150 L 90 -90 M120 -150 L 150 -90" stroke="#0D0D0F" stroke-width="1.6"></path></g></g>')
    # the pans hang plumb from the tilted beam's ends
    ang = math.radians(-14)
    for side, heap in ((-1, True), (1, False)):
        ex = cx + side * 120 * math.cos(ang) * k; ey = by + (-150 + side * 120 * math.sin(ang)) * k
        py = ey + 60 * k
        o.append(f'<path d="M{f(ex)} {f(ey)} L {f(ex - 30 * k)} {f(py)} M{f(ex)} {f(ey)} L {f(ex + 30 * k)} {f(py)}" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 + P(f"M{f(ex - 34 * k)} {f(py)} Q {f(ex)} {f(py + 22 * k)} {f(ex + 34 * k)} {f(py)} Z", "#E8B830", 2))
        if heap: o.append(P(f"M{f(ex - 30 * k)} {f(py)} Q {f(ex)} {f(py - 40 * k)} {f(ex + 30 * k)} {f(py)} Z", "#E8D8A0", 1.8))
    return "".join(o)

def ass_ox(w, h, seed):
    """Doth the wild ass bray when he hath grass? or loweth the ox over his fodder?: a wild ass grazing in green grass, and
    an ox at its crib of fodder."""
    k = min(1.0, h / 360)
    o = [K2.sky(w, h, "#8FD0E2", "#E8F0D8"), hills(w, h, h * 0.72, seed, "#7A9A5A", amp=8, step=90), ground(w, h, h * 0.78, "#9CCB5E", dy=0),
         N.ass(w * 0.24, h * 0.98, 0.62 * k, color="#A89A88")]
    o.append(P(f"M{f(w * 0.56)} {f(h * 0.98)} L {f(w * 0.58)} {f(h * 0.84)} L {f(w * 0.7)} {f(h * 0.84)} L {f(w * 0.72)} {f(h * 0.98)} Z", "#8A5A30", 2.2)
             + "".join(f'<path d="M{f(w * (0.585 + i * 0.012))} {f(h * 0.84)} l {f((i % 3 - 1) * 4)} -12" stroke="#C8B060" stroke-width="2"></path>' for i in range(10)))
    o.append(S1.cow(w * 0.84, h * 0.98, 0.5 * k, flip=True, color="#8A5A30", low=True))
    return "".join(o)

def brook(w, h, seed, dry=False):
    """My brethren have dealt deceitfully as a brook, black by reason of the ice, wherein the snow hideth itself; when it is
    hot they vanish: a ravine with its channel dark with ice and snow; dry=True: the same channel dry and cracked in the heat."""
    o = [K2.sky(w, h, "#8FD0E2" if dry else "#5A6A8A", "#F3E0B0" if dry else "#C8D0E0")]
    o.append(f'<path d="M-10 {f(h * 0.62)} L {f(w * 0.3)} {f(h * 0.56)} L {f(w * 0.42)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{"#B8905A" if dry else "#8A8A9A"}" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(w + 10)} {f(h * 0.6)} L {f(w * 0.66)} {f(h * 0.56)} L {f(w * 0.58)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} Z" fill="{"#A8804A" if dry else "#7A7A8A"}" stroke="#0D0D0F" stroke-width="2.4"></path>')
    ch = f"M{f(w * 0.42)} {f(h + 10)} L {f(w * 0.46)} {f(h * 0.62)} L {f(w * 0.54)} {f(h * 0.62)} L {f(w * 0.58)} {f(h + 10)} Z"
    if dry:
        o.append(P(ch, "#D8B88A", 2))
        r = random.Random(seed)
        for i in range(10):
            y = r.uniform(h * 0.66, h); x = w * 0.5 + r.uniform(-0.05, 0.05) * w
            o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-14, 14))} {f(r.uniform(4, 10))} l {f(r.uniform(-10, 10))} {f(r.uniform(4, 10))}" fill="none" stroke="#6A4A2A" stroke-width="1.6"></path>')
        o.append(sun(w * 0.8, h * 0.16, min(24, h * 0.06), op=0.35))
    else:
        o.append(P(ch, "#1A2A3A", 2) + f'<path d="M{f(w * 0.46)} {f(h * 0.7)} L {f(w * 0.52)} {f(h * 0.74)} L {f(w * 0.48)} {f(h * 0.84)} L {f(w * 0.55)} {f(h * 0.92)}" fill="none" stroke="#8FB8D8" stroke-width="2"></path>')
        o.append(f'<path d="M-10 {f(h * 0.62)} L {f(w * 0.3)} {f(h * 0.56)} L {f(w * 0.33)} {f(h * 0.66)} C {f(w * 0.2)} {f(h * 0.64)} {f(w * 0.1)} {f(h * 0.68)} -10 {f(h * 0.66)} Z" fill="#F3F6FA" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 f'<path d="M{f(w + 10)} {f(h * 0.6)} L {f(w * 0.66)} {f(h * 0.56)} L {f(w * 0.64)} {f(h * 0.64)} C {f(w * 0.8)} {f(h * 0.62)} {f(w * 0.9)} {f(h * 0.66)} {f(w + 10)} {f(h * 0.64)} Z" fill="#F3F6FA" stroke="#0D0D0F" stroke-width="1.6"></path>')
        o.append(mk.stars(60, w, h * 0.6, seed, color="#FFFFFF"))
    return "".join(o)

def dry_caravan(p, w, h, seed):
    """The caravans of Tema looked, the companies of Sheba waited: camels halted at the edge of a dry watercourse in the
    waste, a man standing with his empty water-skin."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E8C890", "#F3E0B0"), sun(w * 0.86, h * 0.18, min(24, h * 0.06), op=0.35), ground(w, h, h * 0.76, "#D8B87A", dy=0),
         P(f"M-10 {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.82)} {f(w * 0.6)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.86)} L {f(w + 10)} {f(h * 0.94)} C {f(w * 0.6)} {f(h * 0.98)} {f(w * 0.3)} {f(h * 0.9)} -10 {f(h * 0.94)} Z", "#E8D0A0", 1.8)]
    k = min(0.5, h / 700)
    for i in range(4): o.append(J1.camel(w * (0.12 + i * 0.13), h * 0.84, k, color=["#B5844A", "#C99A5A"][i % 2], rider=["#2C4A7A", "#7A2A3A", None, "#5A3A22"][i]))
    s = fit(h * 0.86, h * 0.68)
    o.append(man(p, w * 0.7, h * 0.86, s, "#7A5A3A", flip=True, up=[(-22, -158), (-46, -150), (-64, -170)]))
    from genesis.art5 import water_skin
    o.append(water_skin(w * 0.76, h * 0.9, min(1.0, h / 400), empty=True))
    return "".join(o)

def hireling(p, w, h, seed):
    """As a servant that earnestly desireth the shadow, and as a hireling that looketh for his wages: a labourer leaning on
    his mattock in a field under the late sun, the long shadow of a lone tree just out of his reach."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E89A5A", "#F3D8A0"), sun(w * 0.12, h * 0.62, min(26, h * 0.07), color="#FF8A3D", op=0.35), ground(w, h, h * 0.76, "#C8A06A", dy=0)]
    o.append(f'<path d="M{f(w * 0.84)} {f(h * 0.86)} L {f(w * 0.84)} {f(h * 0.62)}" stroke="#3A2214" stroke-width="10"></path>'
             f'<ellipse cx="{f(w * 0.84)}" cy="{f(h * 0.6)}" rx="{f(w * 0.08)}" ry="{f(h * 0.08)}" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<path d="M{f(w * 0.84)} {f(h * 0.86)} L {f(w + 10)} {f(h * 0.9)} L {f(w + 10)} {f(h * 0.96)} Z" fill="#5A4A2A" opacity="0.5"></path>')
    s = fit(h * 0.96, h * 0.7)
    o.append(man(p, w * 0.4, h * 0.96, s, "#8A6A4A", flip=False, extra='<path d="M30 -120 L 40 4" stroke="#5A3A1E" stroke-width="5"></path><path d="M30 6 L 52 0" stroke="#8A8A9A" stroke-width="6"></path>'))
    return "".join(o)

def loom(w, h, seed):
    """My days are swifter than a weaver's shuttle: an upright loom, the web half woven, the shuttle flying through the warp."""
    o = [rect(w, h, "#4A2A3A"), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.6)}" r="{f(h * 0.5)}" fill="#FFC14D" opacity="0.12"></circle>']
    x0, x1, y0, y1 = w * 0.2, w * 0.8, h * 0.5, h * 0.98
    o.append(f'<path d="M{f(x0)} {f(y0 - 10)} L {f(x0)} {f(y1)} M{f(x1)} {f(y0 - 10)} L {f(x1)} {f(y1)}" stroke="#8A5A30" stroke-width="10"></path>'
             f'<path d="M{f(x0 - 10)} {f(y0)} L {f(x1 + 10)} {f(y0)}" stroke="#8A5A30" stroke-width="8"></path>')
    for i in range(30):
        x = x0 + 8 + i * (x1 - x0 - 16) / 29
        o.append(f'<path d="M{f(x)} {f(y0)} L {f(x)} {f(y1)}" stroke="#E8E2D6" stroke-width="1.2"></path>')
    o.append(f'<rect x="{f(x0 + 6)}" y="{f(y0 + (y1 - y0) * 0.55)}" width="{f(x1 - x0 - 12)}" height="{f((y1 - y0) * 0.45)}" fill="#B5121B" opacity="0.9"></rect>')
    for i in range(6):
        y = y0 + (y1 - y0) * (0.6 + i * 0.065)
        o.append(f'<path d="M{f(x0 + 6)} {f(y)} L {f(x1 - 6)} {f(y)}" stroke="#E8B830" stroke-width="2"></path>')
    sy = y0 + (y1 - y0) * 0.45
    o.append("".join(f'<path d="M{f(w * (0.2 + i * 0.03))} {f(sy + (i - 3) * 4)} L {f(w * 0.54)} {f(sy + (i - 3) * 4)}" stroke="#FFF4C2" stroke-width="2" opacity="0.7"></path>' for i in range(7))
             + f'<path d="M{f(w * 0.56)} {f(sy)} C {f(w * 0.6)} {f(sy - 10)} {f(w * 0.7)} {f(sy - 10)} {f(w * 0.74)} {f(sy)} C {f(w * 0.7)} {f(sy + 10)} {f(w * 0.6)} {f(sy + 10)} {f(w * 0.56)} {f(sy)} Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def cloud_gone(w, h, seed):
    """As the cloud is consumed and vanisheth away, so he that goeth down to Sheol: a small cloud thinning to nothing in a
    clear sky over a house whose door is shut."""
    o = [K2.sky(w, h, "#5A8AB8", "#C8E0F0")]
    for i, (x, op) in enumerate(((0.2, 0.95), (0.42, 0.6), (0.62, 0.32), (0.8, 0.12))):
        o.append(clouds(w * 0.18, 0, seed + i, 4, color="#FFFFFF", op=op, ry=0.12, h=h * 0.5).replace("<ellipse", f'<ellipse transform="translate({f(w * x - w * 0.09)} {f(h * 0.72)})"'))
    o.append(hills(w, h, h * 0.84, seed, "#8A7A5A", amp=6, step=90) + ground(w, h, h * 0.9, "#A8905A", dy=0) + house(w * 0.7, h * 0.94, w * 0.1, h * 0.08, color="#C8A878"))
    return "".join(o)

def sea_watch(w, h, seed):
    """Am I a sea, or a sea-monster, that thou settest a watch over me?: a heaving sea at night, a long dark back in the
    waves, and a watch-tower on the headland with its fire lit."""
    o = [K2.sky(w, h, "#0B1A2E", "#2A3A5A"), mk.stars(30, w, h * 0.4, seed), sea(w, h, h * 0.72, seed, color="#1F4A6A", deep="#0B2A3A"),
         f'<path d="M{f(w * 0.22)} {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.78)} {f(w * 0.44)} {f(h * 0.78)} {f(w * 0.52)} {f(h * 0.86)}" fill="#1A2A2A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.3)} {f(h * 0.8)} l 6 -10 l 6 9 M{f(w * 0.38)} {f(h * 0.79)} l 6 -10 l 6 9" fill="#1A2A2A" stroke="#0D0D0F" stroke-width="2"></path>',
         P(f"M{f(w * 0.72)} {f(h + 10)} L {f(w * 0.76)} {f(h * 0.7)} L {f(w * 0.98)} {f(h * 0.64)} L {f(w + 10)} {f(h + 10)} Z", "#3A3430"),
         P(f"M{f(w * 0.82)} {f(h * 0.68)} L {f(w * 0.83)} {f(h * 0.46)} L {f(w * 0.91)} {f(h * 0.46)} L {f(w * 0.92)} {f(h * 0.66)} Z", "#5A5450"),
         E.blaze(w * 0.87, h * 0.46, w * 0.05, h * 0.08, seed, n=4),
         f'<circle cx="{f(w * 0.87)}" cy="{f(h * 0.42)}" r="{f(h * 0.12)}" fill="#FFC14D" opacity="0.15"></circle>']
    return "".join(o)

from genesis.art2 import sea

def dream_bed(w, h, seed):
    """When I say, My bed shall comfort me, then thou scarest me with dreams: an empty mat and its covering cast aside in the
    dark, and above it the night torn with pale jagged shapes."""
    r = random.Random(seed)
    o = [rect(w, h, "#0F0E2A")]
    for i in range(7):
        x = r.uniform(0, w); y = r.uniform(h * 0.05, h * 0.6)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(20, 60))} {f(r.uniform(10, 40))} l {f(r.uniform(-30, 10))} {f(r.uniform(10, 30))} l {f(r.uniform(30, 70))} {f(r.uniform(10, 40))}" fill="none" stroke="#8A7AB8" stroke-width="{r.uniform(2, 5):.1f}" opacity="0.6"></path>')
    o.append(f'<path d="M{f(w * 0.2)} {f(h * 0.96)} L {f(w * 0.24)} {f(h * 0.88)} L {f(w * 0.74)} {f(h * 0.88)} L {f(w * 0.8)} {f(h * 0.96)} Z" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.5)} {f(h * 0.88)} C {f(w * 0.6)} {f(h * 0.8)} {f(w * 0.74)} {f(h * 0.86)} {f(w * 0.86)} {f(h * 0.94)} L {f(w * 0.72)} {f(h * 0.98)} Z" fill="#3A2A4A" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)
