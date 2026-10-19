"""Drawings for Job 18–20 (Bildad's second speech, Job's answer — I know that my Redeemer liveth — and Zophar's second
speech)."""
from job.art5 import *
from job.art5 import f, K2, K3, sea, label, SHIELD
from snake import snake

def lamp_out(w, h, seed):
    """The light shall be dark in his tent, and his lamp above him shall be put out: the inside of a dark tent, a clay lamp
    on its ledge with a last thread of smoke and no flame."""
    o = [rect(w, h, "#0F0B0E"), P(f"M-10 {f(h * 0.5)} L {f(w * 0.5)} {f(h * 0.36)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z", "#1E1618"),
         "".join(f'<path d="M{f(w * k / 8)} {f(h * 0.42)} L {f(w * k / 8)} {f(h + 10)}" stroke="#2A2024" stroke-width="3"></path>' for k in range(1, 8)),
         ground(w, h, h * 0.94, "#1A1214", dy=0)]
    k = min(1.6, h / 220); x, y = w * 0.5, h * 0.9
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})"><path d="M-30 0 L 30 0 L 26 6 L -26 6 Z" fill="#3A2A1A" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-20 0 C -22 -12 6 -16 18 -8 L 30 -10 L 24 -2 L 16 0 Z" fill="#6A3A1E" stroke="#0D0D0F" stroke-width="2"></path></g>')
    o.append(f'<path d="M{f(x + 27 * k)} {f(y - 12 * k)} C {f(x + 20 * k)} {f(y - 30 * k)} {f(x + 36 * k)} {f(y - 44 * k)} {f(x + 26 * k)} {f(y - 64 * k)}" stroke="#8A8494" stroke-width="2" fill="none" opacity="0.7"></path>')
    return "".join(o)

def snares(w, h, seed):
    """A net by his own feet, a gin to take him by the heel, a noose hid in the ground, a trap in the way: a path through
    the grass with a net spread across it, a noose half-buried and a spring trap, set and waiting."""
    o = [K2.sky(w, h, "#8A9A7A", "#E8D8B0"), ground(w, h, h * 0.8, "#8A8A4A", dy=0),
         P(f"M{f(w * 0.0)} {f(h + 10)} L {f(w * 0.4)} {f(h * 0.8)} L {f(w * 0.56)} {f(h * 0.8)} L {f(w * 0.9)} {f(h + 10)} Z", "#B89A6A", 1.6)]
    nx0, nx1, ny0, ny1 = w * 0.3, w * 0.62, h * 0.86, h * 0.98
    for i in range(9):
        t = i / 8
        o.append(f'<path d="M{f(nx0 + (nx1 - nx0) * t - 10)} {f(ny0)} L {f(nx0 + (nx1 - nx0) * t + 10)} {f(ny1)}" stroke="#5A4A2A" stroke-width="1.6"></path>'
                 f'<path d="M{f(nx0)} {f(ny0 + (ny1 - ny0) * t)} L {f(nx1)} {f(ny0 + (ny1 - ny0) * t)}" stroke="#5A4A2A" stroke-width="1.6"></path>')
    o.append(f'<ellipse cx="{f(w * 0.18)}" cy="{f(h * 0.92)}" rx="{f(w * 0.05)}" ry="{f(h * 0.02)}" fill="none" stroke="#8A6A3A" stroke-width="3"></ellipse>'
             f'<path d="M{f(w * 0.23)} {f(h * 0.92)} C {f(w * 0.26)} {f(h * 0.86)} {f(w * 0.24)} {f(h * 0.8)} {f(w * 0.26)} {f(h * 0.74)}" stroke="#8A6A3A" stroke-width="3" fill="none"></path>'
             f'<path d="M{f(w * 0.26)} {f(h * 0.74)} L {f(w * 0.26)} {f(h * 0.94)}" stroke="#5A3A1E" stroke-width="4"></path>')
    tx, ty, k = w * 0.8, h * 0.94, min(1.2, h / 300)
    o.append(f'<g transform="translate({f(tx)} {f(ty)}) scale({f(k)})"><path d="M-30 0 A 30 14 0 0 1 30 0" stroke="#5A5A6A" stroke-width="4" fill="none"></path>'
             '<path d="M-30 0 A 30 14 0 0 0 30 0" stroke="#5A5A6A" stroke-width="4" fill="none"></path>'
             + "".join(f'<path d="M{x} -8 l 3 -8 l 3 8" stroke="#8A8A9A" stroke-width="1.6" fill="none"></path>' for x in range(-24, 24, 8)) + '</g>')
    return "".join(o)

def fleeing(p, w, h, seed):
    """Terrors shall make him afraid on every side, and shall chase him at his heels: a man running alone over a dark plain,
    his long shadow before him, shapes of smoke at his back."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#1A0A1A", "#6A2A2A"), ground(w, h, h * 0.84, "#2A1A1A", dy=0)]
    r = random.Random(seed)
    for i in range(6):
        o.append(f'<ellipse cx="{f(w * r.uniform(0.0, 0.3))}" cy="{f(h * r.uniform(0.6, 0.86))}" rx="{f(w * 0.08)}" ry="{f(h * 0.08)}" fill="#0B050B" opacity="0.6"></ellipse>')
    s = fit(h * 0.95, h * 0.72)
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.95)} L {f(w * 0.95)} {f(h * 0.99)} L {f(w * 0.95)} {f(h * 0.96)} Z" fill="#0B050B" opacity="0.6"></path>')
    o.append(man(p, w * 0.56, h * 0.95, s, "#5A4A4A", up=[(-22, -158), (-40, -176), (-64, -190)]))
    return "".join(o)

def brimstone(w, h, seed):
    """Brimstone shall be scattered upon his habitation; his roots dried up beneath, his branch cut off: an empty tent
    fallen in, yellow brimstone smoking about it, a dead tree cut off at the top."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#5A4A2A", "#C8B060"), ground(w, h, h * 0.84, "#8A7A4A", dy=0),
         P(f"M{f(w * 0.2)} {f(h * 0.94)} L {f(w * 0.3)} {f(h * 0.82)} L {f(w * 0.36)} {f(h * 0.88)} L {f(w * 0.5)} {f(h * 0.94)} Z", "#2A2220")]
    for i in range(18):
        x = w * r.uniform(0.05, 0.95); y = h * r.uniform(0.86, 0.98)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(r.uniform(6, 14))}" ry="{f(r.uniform(3, 6))}" fill="#E8D040" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    o.append(smoke(w * 0.6, h * 0.86, 7, seed, color="#D8C870", op=0.4, k=min(1.4, h / 300)))
    tx = w * 0.8
    o.append(f'<path d="M{f(tx)} {f(h * 0.92)} L {f(tx)} {f(h * 0.68)} M{f(tx)} {f(h * 0.76)} L {f(tx - 24)} {f(h * 0.68)}" stroke="#3A2A1E" stroke-width="8" stroke-linecap="round" fill="none"></path>'
             f'<path d="M{f(tx - 8)} {f(h * 0.68)} L {f(tx + 8)} {f(h * 0.66)}" stroke="#C8A06A" stroke-width="3"></path>')
    return "".join(o)

def walled_way(w, h, seed):
    """He hath walled up my way that I cannot pass, and hath set darkness in my paths: a road running into a wall of great
    stones built across it, the sky dark behind."""
    o = [K2.sky(w, h, "#1A1A2A", "#5A4A5A"), ground(w, h, h * 0.78, "#4A3A30", dy=0),
         P(f"M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.44)} {f(h * 0.8)} L {f(w * 0.56)} {f(h * 0.8)} L {f(w * 0.7)} {f(h + 10)} Z", "#8A7A5A", 1.6)]
    for row in range(4):
        y = h * (0.8 - row * 0.045)
        for i in range(8):
            x = w * (0.2 + i * 0.075) + (row % 2) * w * 0.035
            o.append(f'<rect x="{f(x)}" y="{f(y - h * 0.045)}" width="{f(w * 0.075)}" height="{f(h * 0.045)}" fill="{["#7A7068", "#8A8078", "#6A6058"][(i + row) % 3]}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)

def uprooted(w, h, seed):
    """He hath stripped me of my glory, and taken the crown from my head; my hope hath he plucked up like a tree: a tree
    lying uprooted, its roots in the air, and a gold crown fallen in the dust before it."""
    o = [K2.sky(w, h, "#6A6A8A", "#E8C8A0"), ground(w, h, h * 0.86, "#A88A5A", dy=0),
         f'<ellipse cx="{f(w * 0.3)}" cy="{f(h * 0.9)}" rx="{f(w * 0.06)}" ry="{f(h * 0.025)}" fill="#3A2A1A"></ellipse>']
    k = min(1.4, h / 300)
    o.append(f'<g transform="translate({f(w * 0.36)} {f(h * 0.9)}) scale({f(k)})">'
             + P("M0 -10 L 200 -24 L 200 -10 L 0 6 Z", "#5A3A1E")
             + '<g stroke="#5A3A1E" stroke-width="4" fill="none"><path d="M0 0 l -24 -40 M0 -4 l -40 -10 M0 4 l -36 20 M0 -6 l -10 -44 M0 2 l -46 4"></path></g>'
             + '<ellipse cx="230" cy="-30" rx="50" ry="30" fill="#4A6A3A" stroke="#0D0D0F" stroke-width="2"></ellipse></g>')
    o.append(f'<g transform="translate({f(w * 0.18)} {f(h * 0.97)}) rotate(-14) scale({f(k * 1.4)})">' + P("M-14 0 L -14 -14 L -7 -6 L 0 -18 L 7 -6 L 14 -14 L 14 0 Z", "#E8B830", 1.6) + '</g>')
    return "".join(o)

def siege_tent(w, h, seed):
    """His troops come on together, and cast up their way against me, and encamp round about my tent: a lone tent on a
    rise, the camp-fires of a host ringing it in the dusk."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#1A1A3A", "#8A5A5A"), ground(w, h, h * 0.8, "#3A2A2A", dy=0),
         A.black_tent(w * 0.42, h * 0.86, w * 0.16, h * 0.1, color="#4A3A30", lit="#FFC14D")]
    for i in range(24):
        a = 2 * math.pi * i / 24; x = w * 0.5 + math.cos(a) * w * 0.42; y = h * 0.88 + math.sin(a) * h * 0.08
        if y < h * 0.8: continue
        o.append(A.black_tent(x - 14, y, 28, 12, color="#120A0A") + f'<circle cx="{f(x + 18)}" cy="{f(y - 2)}" r="3" fill="#FF8A3D"></circle>')
    return "".join(o)

def estranged(p, w, h, seed):
    """My kinsfolk have failed; they that dwell in my house count me for a stranger: Job alone on the ash heap, his household
    walking away from him toward the city, none looking back."""
    b = h * 0.97
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A5A7A", "#E8C8A0"), J.city_hill(w * 0.86, h * 0.76, w * 0.26, h * 0.12, seed), ground(w, h, h * 0.78, "#8A7A62", dy=0),
         ash_mound(w * 0.18, b, w * 0.3, h * 0.08, seed)]
    o.append(seated_job(w * 0.18, b - h * 0.06, min(0.8, h * 0.2 / 140), shard=False))
    s = fit(b, max(h * 0.72, b - 200))
    cl = [WIFE_C, "#6A5A3A", "#3A4A6A", "#5A3A2A", "#4A5A3A"]
    for i in range(5):
        x = w * (0.48 + i * 0.09); y = b - i * h * 0.03; k = s * (1 - i * 0.12)
        o.append(wife_fig(p, x, y, k) if i == 0 else man(p, x, y, k, cl[i]))
    return "".join(o)

def graven(w, h, seed):
    """Oh that my words were inscribed in a book! that with an iron pen and lead they were graven in the rock for ever: a
    rock face with lines of letters cut into it, the chisel and hammer laid at its foot."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8A8A9A", "#E8D8C0"), P(f"M{f(w * 0.08)} {f(h + 10)} L {f(w * 0.12)} {f(h * 0.6)} L {f(w * 0.86)} {f(h * 0.58)} L {f(w * 0.94)} {f(h + 10)} Z", "#A89A8A")]
    for row in range(5):
        y = h * (0.66 + row * 0.055); x = w * 0.18
        while x < w * 0.8:
            g = r.choice(["w", "ww", "h", "c"]); s = h * 0.02          # wedge-marks, not letters
            d = {"w": f"M{f(x - 4)} {f(y - s)} L {f(x + 4)} {f(y - s)} L {f(x)} {f(y - s * 0.3)} Z M{f(x)} {f(y - s * 0.3)} L {f(x)} {f(y + s)}",
                 "ww": f"M{f(x - 6)} {f(y - s)} L {f(x)} {f(y - s)} L {f(x - 3)} {f(y - s * 0.4)} Z M{f(x + 1)} {f(y - s)} L {f(x + 7)} {f(y - s)} L {f(x + 4)} {f(y - s * 0.4)} Z",
                 "h": f"M{f(x - 5)} {f(y - s * 0.2)} L {f(x - 5)} {f(y + s * 0.6)} L {f(x + 6)} {f(y + s * 0.2)} Z",
                 "c": f"M{f(x + 4)} {f(y - s)} L {f(x - 4)} {f(y)} L {f(x + 4)} {f(y + s)}"}[g]
            o.append(f'<path d="{d}" stroke="#3A3028" stroke-width="2" fill="#5A4A3A"></path>')
            x += r.uniform(12, 20) + (14 if r.random() < 0.15 else 0)
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.98)} L {f(w * 0.42)} {f(h * 0.96)}" stroke="#5A5A6A" stroke-width="6" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.5)} {f(h * 0.98)} L {f(w * 0.6)} {f(h * 0.95)}" stroke="#6A4A2A" stroke-width="6" stroke-linecap="round"></path><rect x="{f(w * 0.59)}" y="{f(h * 0.93)}" width="18" height="12" fill="#5A5A6A" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    return "".join(o)

def redeemer(p, w, h, seed, jx=0.3):
    """I know that my Redeemer liveth, and at last he will stand up upon the earth: the dawn breaking over the whole earth,
    long rays climbing the sky, and Job small upon the ash heap with his hands lifted toward it (no one is drawn in the light)."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A2A6A", "#FFD8A0"), V.rays(w * (1 - jx), h * 0.86, 36, 20, max(w, h) * 1.2, color="#FFF4C2", op=0.3),
         f'<circle cx="{f(w * (1 - jx))}" cy="{f(h * 0.86)}" r="{f(h * 0.08)}" fill="#FFF4C2"></circle>',
         hills(w, h, h * 0.86, seed, "#4A3A5A", amp=10, step=80), ground(w, h, h * 0.92, "#5A4A4A", dy=0), ash_mound(w * jx, h * 0.995, w * 0.24, h * 0.06, seed)]
    k = min(0.8, h * 0.18 / 140); x, y = w * jx, h * 0.95
    o.append(seated(x, y, k, SACK, head=SACK, ash=True, shard=False, flip=jx > 0.5))
    sx = -k if jx > 0.5 else k
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(k)})"><path d="M-8 -90 L 14 -120 L 24 -150" stroke="#0D0D0F" stroke-width="13" fill="none" stroke-linecap="round"></path>'
             f'<path d="M-8 -90 L 14 -120 L 24 -150" stroke="{SACK}" stroke-width="9.5" fill="none" stroke-linecap="round"></path></g>')
    return "".join(o)

def pillar_clouds(w, h, seed):
    """Though his height mount up to the heavens, and his head reach unto the clouds, he shall fly away as a dream: a tall
    proud tower cracked through, its top in the clouds, pieces already falling."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#5A6A8A", "#D8D0C0"), ground(w, h, h * 0.92, "#8A7A5A", dy=0)]
    cx, tw = w * 0.5, w * 0.08
    o.append(P(f"M{f(cx - tw)} {f(h * 0.94)} L {f(cx - tw * 0.7)} {f(-10)} L {f(cx + tw * 0.7)} {f(-10)} L {f(cx + tw)} {f(h * 0.94)} Z", "#B8A080"))
    for k in range(12): o.append(f'<path d="M{f(cx - tw)} {f(h * (0.9 - k * 0.08))} L {f(cx + tw)} {f(h * (0.9 - k * 0.08))}" stroke="#8A7458" stroke-width="1.4"></path>')
    o.append(f'<path d="M{f(cx - tw * 0.2)} {f(h * 0.94)} L {f(cx + tw * 0.2)} {f(h * 0.8)} L {f(cx - tw * 0.3)} {f(h * 0.68)} L {f(cx + tw * 0.1)} {f(h * 0.5)}" stroke="#1A1210" stroke-width="3" fill="none"></path>')
    o.append(clouds(w, h * 0.3, seed, 8, color="#F3F3F3", op=0.85, ry=0.06, h=h))
    for i in range(8):
        o.append(f'<rect x="{f(cx + r.uniform(0.1, 0.4) * w)}" y="{f(h * r.uniform(0.6, 0.9))}" width="12" height="9" fill="#B8A080" stroke="#0D0D0F" stroke-width="1.4" transform="rotate({r.randint(-40, 40)})"></rect>')
    return "".join(o)

def viper(w, h, seed):
    """He shall suck the poison of asps; the viper's tongue shall slay him: a viper coiled among the stones of the desert
    floor, its head raised and tongue out."""
    o = [K2.sky(w, h, "#E8C890", "#F3E0B0"), ground(w, h, h * 0.82, "#C8A06A", dy=0), S4.stone_heap(w * 0.24, h * 0.98, w * 0.26, h * 0.1, seed)]
    k = min(1.0, h / 300)
    pts = [(w * 0.4, h * 0.97), (w * 0.52, h * 0.99), (w * 0.66, h * 0.96), (w * 0.62, h * 0.92), (w * 0.52, h * 0.93), (w * 0.5, h * 0.88), (w * 0.56, h * 0.84), (w * 0.62, h * 0.82)]
    o.append(snake(pts, 10 * k, f"vp{seed}", head_scale=0.8 * k))
    return "".join(o)

def honey_streams(w, h, seed):
    """He shall not look upon the rivers, the flowing streams of honey and butter: a green valley with two golden streams
    winding through it, a honeycomb and a jar of butter on the bank."""
    o = [K2.sky(w, h, "#8FD0E2", "#F0F0D8"), hills(w, h, h * 0.76, seed, "#5A8A4A", amp=10, step=90), ground(w, h, h * 0.82, "#7AAA4A", dy=0)]
    o.append(f'<path d="M{f(w * 0.2)} {f(h * 0.82)} C {f(w * 0.3)} {f(h * 0.88)} {f(w * 0.1)} {f(h * 0.94)} {f(w * 0.3)} {f(h + 10)}" stroke="#E8B830" stroke-width="16" fill="none"></path>'
             f'<path d="M{f(w * 0.6)} {f(h * 0.82)} C {f(w * 0.7)} {f(h * 0.9)} {f(w * 0.5)} {f(h * 0.94)} {f(w * 0.66)} {f(h + 10)}" stroke="#F3E8B0" stroke-width="16" fill="none"></path>')
    k = min(1.2, h / 300); x, y = w * 0.84, h * 0.96
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})">' + "".join(P(f"M{a} {b} l 8 -5 l 8 5 l 0 9 l -8 5 l -8 -5 Z", "#E8B830", 1.2) for a, b in ((-30, -20), (-14, -20), (-22, -34), (-6, -34), (2, -20))) + '</g>'
             + f'<g transform="translate({f(w * 0.44)} {f(y)}) scale({f(k)})">' + P("M-16 0 C -22 -20 -18 -36 -8 -40 L 8 -40 C 18 -36 22 -20 16 0 Z", "#C8A878") + '<ellipse cx="0" cy="-40" rx="9" ry="3" fill="#F3EAC0" stroke="#0D0D0F" stroke-width="1.4"></ellipse></g>')
    return "".join(o)

def storm_feast(w, h, seed):
    """When he is about to fill his belly, God will rain his wrath upon him while he is eating: a laden table set out under
    the open sky, the storm breaking over it, the cups overturned (no one at it)."""
    o = [tempest(w, h, seed, rain=True)]
    ty = h * 0.88
    o.append(P(f"M{f(w * 0.2)} {f(ty)} L {f(w * 0.8)} {f(ty)} L {f(w * 0.8)} {f(ty + 10)} L {f(w * 0.2)} {f(ty + 10)} Z", "#8A5A30")
             + f'<path d="M{f(w * 0.24)} {f(ty + 10)} L {f(w * 0.24)} {f(h * 0.98)} M{f(w * 0.76)} {f(ty + 10)} L {f(w * 0.76)} {f(h * 0.98)}" stroke="#0D0D0F" stroke-width="5"></path>')
    for i in range(6):
        x = w * (0.26 + i * 0.09)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(ty - 4)}" rx="14" ry="5" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>' if i % 2 else
                 P(f"M{f(x - 6)} {f(ty)} L {f(x + 10)} {f(ty - 4)} L {f(x + 10)} {f(ty - 12)} L {f(x - 6)} {f(ty - 8)} Z", "#E8B830", 1.4))
    return "".join(o)

def brass_bow(w, h, seed):
    """He shall flee from the iron weapon, and the bow of brass shall strike him through: a bow of brass and its arrows lying
    on the bare ground, an iron sword beside them (no one is drawn)."""
    o = [K2.sky(w, h, "#5A4A4A", "#C8A080"), ground(w, h, h * 0.84, "#7A6A4A", dy=0)]
    k = min(1.4, h / 300); x, y = w * 0.4, h * 0.92
    o.append(f'<g transform="translate({f(x)} {f(y)}) rotate(-6) scale({f(k)})"><path d="M-120 0 C -60 -40 60 -40 120 0" stroke="#0D0D0F" stroke-width="9" fill="none"></path><path d="M-120 0 C -60 -40 60 -40 120 0" stroke="#C8963E" stroke-width="6" fill="none"></path>'
             '<path d="M-120 0 L 120 0" stroke="#E8E2D6" stroke-width="1.4"></path></g>')
    for i in range(3):
        o.append(f'<path d="M{f(w * (0.2 + i * 0.05))} {f(h * 0.97)} L {f(w * (0.5 + i * 0.05))} {f(h * 0.95)}" stroke="#5A3A1E" stroke-width="2.4"></path>'
                 f'<path d="M{f(w * (0.5 + i * 0.05))} {f(h * 0.95)} l -10 -4 l 0 8 Z" fill="#8A8A9A" stroke="#0D0D0F" stroke-width="1"></path>')
    o.append(f'<path d="M{f(w * 0.66)} {f(h * 0.96)} L {f(w * 0.9)} {f(h * 0.9)}" stroke="#0D0D0F" stroke-width="8"></path><path d="M{f(w * 0.66)} {f(h * 0.96)} L {f(w * 0.9)} {f(h * 0.9)}" stroke="#A8A8B8" stroke-width="5"></path>'
             f'<path d="M{f(w * 0.68)} {f(h * 0.92)} L {f(w * 0.7)} {f(h * 0.99)}" stroke="#5A3A1E" stroke-width="6"></path>')
    return "".join(o)

def tent_fire(w, h, seed):
    """A fire not blown by man shall devour him; it shall consume that which is left in his tent; the heavens shall reveal
    his iniquity: a tent burning alone at night under the stars, its goods spilled out."""
    o = [K2.sky(w, h, "#05051A", "#2A1A2A"), mk.stars(80, w, h * 0.7, seed), ground(w, h, h * 0.86, "#1A1214", dy=0),
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.86)}" r="{f(h * 0.3)}" fill="#FF6A2A" opacity="0.15"></circle>',
         A.black_tent(w * 0.38, h * 0.92, w * 0.24, h * 0.12, color="#2A1A1A"), E.blaze(w * 0.5, h * 0.9, w * 0.2, h * 0.2, seed, n=7)]
    return "".join(o)
