"""Drawings for 1 Corinthians 15–16 (chapter 5 of the volume), on co1.art4: died, buried, raised — the three crosses far off,
the sealed tomb, the stone rolled away and Jesus risen before the open tomb (no wounds, nothing nearer, 15:3–4); the witnesses as
greeting cells (15:5–8); the sealed tomb at night (15:12–14); the tombs at dusk (15:18); the firstfruits (15:20); the throne
and the footstool, no figure (15:25); the theatre at Ephesus empty (15:32, "fought with beasts", words only); the grain of
wheat (John's plan, 15:36–38); one flesh of men, of beasts, of birds, of fishes (15:39); the glory of the sun, the moon and the
stars (15:41); sown and raised (15:42–44); the earthy man and the heavenly — Jesus risen in white light (15:45–49); the last
trump over the opened tombs in light (15:52); the empty tomb, the linen folded (15:54–55); the collection laid by on the first
day of the week (16:2); Paul's road through Macedonia (16:5–9); Timothy setting out, Apollos staying (16:10–12); Paul's own
hand (16:21)."""
from co1.art4 import *
from co1.art4 import f, INK, _seated_lap
from mat.art11 import new_tomb, linen
from ntcast import JESUS_SKIN, _HAIR_FIG, _BEARD_FIG
from act.art4 import throne_footstool
from ecc.art import tombs as ecc_tombs
from jhn.art6 import grain_wheat
from oba.minor import eagle
from epistle import portrait

def risen_fig(p, x, y, s, flip=False, up=None):
    """Jesus risen (CLAUDE.md: the same man as ntcast draws him, after the resurrection in white light): ntcast's skin,
    shoulder-length dark-brown hair and short beard, his robe white and his mantle a pale blue-grey, drawn on the kit
    silhouette (epistle.robed) with a full ink line so he reads as a man; a white glow and soft rays behind him."""
    return (glow(x, y - 110 * s, 170 * s, "#FFFFFF", 0.9, f"{p}rz{int(x)}") + rays(x, y - 110 * s, 24, 70 * s, 230 * s, color="#FFFDF0", op=0.35)
            + robed(p, x, y, s, "#FFFFFF", skin=JESUS_SKIN, mantle="#C8D2E6", flip=flip, up=up, extra=_HAIR_FIG + _BEARD_FIG))

def risen_tomb(p, w, h, seed):
    """He hath been raised on the third day: the garden at dawn, the tomb in the rock with its stone rolled away and its door
    open and dark, and Jesus risen standing before it in white light, about seven tenths of the panel's height."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#3A3A7A", "#FFC890"),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.36)} {f(h * 0.2)} C {f(w * 0.6)} {f(h * 0.1)} {f(w * 0.86)} {f(h * 0.14)} {f(w + 10)} {f(h * 0.2)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.56)} {f(b - h * 0.04)} L {f(w * 0.56)} {f(h * 0.44)} Q {f(w * 0.66)} {f(h * 0.32)} {f(w * 0.76)} {f(h * 0.44)} L {f(w * 0.76)} {f(b - h * 0.04)} Z" fill="#1A1210" stroke="{INK}" stroke-width="2.4"></path>',
         ground(w, h, b - h * 0.04, "#5A6A3A", dy=0)]
    r = min(h * 0.14, w * 0.14)
    o.append(f'<circle cx="{f(w * 0.88)}" cy="{f(b - h * 0.04 - r)}" r="{f(r)}" fill="#A89A8A" stroke="{INK}" stroke-width="2.6"></circle>'
             f'<circle cx="{f(w * 0.88)}" cy="{f(b - h * 0.04 - r)}" r="{f(r * 0.6)}" fill="none" stroke="#8A7C6C" stroke-width="2"></circle>')
    s = h * 0.7 / 205
    o.append(risen_fig(p, w * 0.34, b, s, flip=True, up=[(-22, -158), (-44, -150), (-64, -160)]))
    return "".join(o)

def cells(p, w, h, fns, gap=0, line=True):
    """Several drawings side by side in one panel, each clipped to its cell: fns = [fn(p, w, h) …]."""
    n = len(fns); cw = w / n; o = []
    for i, fn in enumerate(fns):
        cid = f"{p}cl{i}"
        o.append(f'<defs><clipPath id="{cid}"><rect x="0" y="0" width="{f(cw)}" height="{f(h)}"></rect></clipPath></defs>'
                 f'<g transform="translate({f(i * cw)} 0)"><g clip-path="url(#{cid})">{fn(f"{p}c{i}", cw, h)}</g></g>')
    if line:
        o += [f'<path d="M{f(cw * k)} -10 L {f(cw * k)} {f(h + 10)}" stroke="{INK}" stroke-width="4"></path>' for k in range(1, n)]
    return "".join(o)

# ---- 1 Corinthians 15 --------------------------------------------------------------------------------------------------
def died_buried_raised(p, w, h, seed):
    """That Christ died … and that he was buried; and that he hath been raised on the third day: three cells — the hill of the
    three crosses far off under a black sky; the tomb with its stone sealed; the stone rolled away at dawn and Jesus risen
    standing before the open tomb in white light (risen_tomb)."""
    return cells(p, w, h, [lambda q, cw, hh: dark_hill(q, cw, hh, seed), lambda q, cw, hh: new_tomb(q, cw, hh, seed + 1, sealed=True),
                           lambda q, cw, hh: risen_tomb(q, cw, hh, seed + 2)])

def sealed_tomb(p, w, h, seed):
    """If Christ hath not been raised: the tomb hewn in the rock at evening, the great stone rolled to the door and sealed."""
    return new_tomb(p, w, h, seed, sealed=True)

def sleepers(w, h, seed):
    """They also that are fallen asleep in Christ: the sepulchres hewn in the hillside at dusk, their stones rolled to."""
    return ecc_tombs(w, h, seed)

def firstfruits(p, w, h, seed):
    """But now hath Christ been raised from the dead, the firstfruits of them that are asleep: a field of barley at dawn, the
    first sheaf cut and standing alone in a shaft of light, the whole harvest still standing behind it."""
    b = h * 0.9
    o = [vista(w, h, seed, tone="dawn", horizon=0.5, hills_n=1, glow_at=(0.5, 0.5, 0.7, "#FFF4C2"), sun_at=(0.5, 0.48))]
    r = random.Random(seed)
    for row in range(5):                                       # the standing grain
        y = h * (0.56 + row * 0.07)
        for i in range(int(w / 9)):
            x = i * 9 + r.uniform(-3, 3)
            if abs(x - w * 0.5) < w * 0.12 and row > 1: continue
            o.append(f'<path d="M{f(x)} {f(y + h * 0.06)} L {f(x + r.uniform(-2, 2))} {f(y)}" stroke="{["#C8A84A", "#D8B860", "#B8983A"][row % 3]}" stroke-width="2"></path>'
                     f'<ellipse cx="{f(x)}" cy="{f(y - 3)}" rx="2" ry="5" fill="#E8C870"></ellipse>')
    k = min(1.2, h / 220)
    sx = w * 0.5
    o.append(f'<path d="M{f(sx - 60)} {f(-10)} L {f(sx + 60)} -10 L {f(sx + 90)} {f(b)} L {f(sx - 90)} {f(b)} Z" fill="#FFF4C2" opacity="0.4"></path>')
    o.append(f'<path d="M{f(sx - 24 * k)} {f(b)} L {f(sx)} {f(b - 90 * k)} L {f(sx + 24 * k)} {f(b)} Z" fill="#E8C870" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(sx - 16 * k)} {f(b - 40 * k)} L {f(sx + 16 * k)} {f(b - 40 * k)}" stroke="#8A6A2A" stroke-width="3"></path>'
             + "".join(f'<ellipse cx="{f(sx + d * k)}" cy="{f(b - 96 * k)}" rx="{f(4 * k)}" ry="{f(10 * k)}" fill="#F3D880" stroke="{INK}" stroke-width="1" transform="rotate({d} {f(sx + d * k)} {f(b - 96 * k)})"></ellipse>' for d in (-14, -6, 2, 10)))
    return "".join(o)

def throne(p, w, h, seed):
    """For he must reign, till he hath put all his enemies under his feet: the vault of heaven full of light over the round
    of the earth, its footstool (Acts' drawing; no figure)."""
    return throne_footstool(p, w, h, seed)

def empty_theatre(p, w, h, seed):
    """If after the manner of men I fought with beasts at Ephesus: the theatre of Ephesus empty — the words only."""
    return theatre(p, w, h, seed, empty=True)

def grain(p, w, h, seed):
    """That which thou sowest is not quickened except it die … a bare grain: John's plan of the grain of wheat fallen into
    the earth, split, the shoot going up into the full ears."""
    return grain_wheat(p, w, h, seed)

def _fish(cx, cy, r, color="#5A8AAA"):
    return (f'<path d="M{f(cx - r)} {f(cy)} C {f(cx - r * 0.5)} {f(cy - r * 0.5)} {f(cx + r * 0.5)} {f(cy - r * 0.5)} {f(cx + r * 0.8)} {f(cy)} C {f(cx + r * 0.5)} {f(cy + r * 0.5)} {f(cx - r * 0.5)} {f(cy + r * 0.5)} {f(cx - r)} {f(cy)} Z" '
            f'fill="{color}" stroke="{INK}" stroke-width="2"></path><path d="M{f(cx + r * 0.7)} {f(cy)} L {f(cx + r * 1.2)} {f(cy - r * 0.4)} L {f(cx + r * 1.2)} {f(cy + r * 0.4)} Z" fill="{color}" stroke="{INK}" stroke-width="2"></path>'
            f'<circle cx="{f(cx - r * 0.6)}" cy="{f(cy - r * 0.08)}" r="{f(r * 0.08)}" fill="#0D0D0F"></circle>')

def fleshes(p, w, h, seed):
    """One flesh of men, and another flesh of beasts, and another flesh of birds, and another of fishes: four cells — a man,
    an ox, an eagle in the air, fishes in the water."""
    def man(q, cw, hh):
        b = hh * 0.92
        return (mk.defs(q, *ALL) + sky(cw, hh, "#E8D8B0", "#C8B080") + ground(cw, hh, b, "#A8865A", dy=0)
                + robed(q, cw * 0.5, b, fit(b, b - min(hh * 0.8, 210)), "#6A5A4A", hair="#2A1A10", beard="#2A1A10"))
    def beast(q, cw, hh):
        b = hh * 0.86
        return sky(cw, hh, "#9CCB5E", "#5A7A3A") + ground(cw, hh, b, "#4A6A2A", dy=0) + ox(cw * 0.46, b + 4, min(cw / 240, hh / 150))
    def bird(q, cw, hh):
        return sky(cw, hh, "#5A9AD8", "#CFEFFF") + eagle(cw * 0.5, hh * 0.46, min(cw / 140, hh / 110), color="#4A3A2A")
    def fish(q, cw, hh):
        r = min(cw, hh) * 0.13
        return (sky(cw, hh, "#1F6F9A", "#0F4C68") + _fish(cw * 0.4, hh * 0.36, r) + _fish(cw * 0.62, hh * 0.62, r * 0.8, "#8AAAC8") + _fish(cw * 0.3, hh * 0.78, r * 0.7, "#C8A86A"))
    return cells(p, w, h, [man, beast, bird, fish])

def glories(w, h, seed):
    """One glory of the sun, and another glory of the moon, and another glory of the stars: one sky passing from night at the
    left, full of stars of every brightness, through the moon, to the blaze of the sun at the right."""
    o = [f'<defs><linearGradient id="gl{seed}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#05051A"></stop><stop offset="0.5" stop-color="#2A2A6A"></stop>'
         f'<stop offset="0.75" stop-color="#E8905A"></stop><stop offset="1" stop-color="#FFE680"></stop></linearGradient></defs>',
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#gl{seed})"></rect>']
    r = random.Random(seed)
    for _ in range(int(w * h / 2500)):
        x, y = w * r.uniform(0, 0.4), h * r.uniform(0, 0.8); rr = r.choice([1, 1, 1.4, 2, 3])
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rr)}" fill="#F3EFE6" opacity="{r.uniform(0.5, 1):.2f}"></circle>')
    for x, y, rr in ((w * 0.12, h * 0.3, 5), (w * 0.28, h * 0.2, 7)):
        o.append(halo(x, y, rr * 4, "#FFFFFF", 0.5) + f'<path d="M{f(x - rr * 2)} {f(y)} L {f(x + rr * 2)} {f(y)} M{f(x)} {f(y - rr * 2)} L {f(x)} {f(y + rr * 2)}" stroke="#FFFFFF" stroke-width="1.6"></path>')
    mx, my, mr = w * 0.5, h * 0.36, min(h * 0.14, w * 0.06)
    o.append(halo(mx, my, mr * 2.4, "#E8E8FF", 0.4) + f'<circle cx="{f(mx)}" cy="{f(my)}" r="{f(mr)}" fill="#E8E8F0" stroke="{INK}" stroke-width="2"></circle>'
             f'<circle cx="{f(mx + mr * 0.4)}" cy="{f(my - mr * 0.2)}" r="{f(mr * 0.86)}" fill="#3A3A7A"></circle>')
    sx, sy, sr = w * 0.86, h * 0.4, min(h * 0.2, w * 0.08)
    o.append(halo(sx, sy, sr * 3, "#FFF4C2", 0.7) + rays(sx, sy, 24, sr * 1.2, sr * 3, "#FFF4C2", 0.5, 3) + f'<circle cx="{f(sx)}" cy="{f(sy)}" r="{f(sr)}" fill="#FFD23F" stroke="{INK}" stroke-width="2"></circle>')
    o.append(hills(w, h, h * 0.82, seed, color="#1A1430", amp=10, step=80))
    o.append(plate_label(w * 0.2, h * 0.94, "THE STARS", "#E8E2D6", 10, halo_="#05051A") + plate_label(w * 0.5, h * 0.94, "THE MOON", "#E8E2D6", 10, halo_="#1A1430")
             + plate_label(w * 0.86, h * 0.94, "THE SUN", "#FFF8E6", 10, halo_="#1A1430"))
    return "".join(o)

def sown_raised(w, h, seed):
    """It is sown in corruption; it is raised in incorruption … sown a natural body; raised a spiritual body: one field cut
    through — at the left under the dark earth the seed lying in the ground; at the right the same field in full light, the
    grain risen tall and golden."""
    gy = h * 0.6
    o = [f'<rect x="-10" y="-10" width="{f(w * 0.5 + 10)}" height="{f(gy + 10)}" fill="#2A2040"></rect>',
         f'<rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(gy + 10)}" fill="#FFF4C2"></rect>',
         f'<defs><clipPath id="sr{seed}"><rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}"></rect></clipPath></defs>',
         f'<g clip-path="url(#sr{seed})">' + halo(w * 0.75, h * 0.1, h * 0.6, "#FFFFFF", 0.8) + '</g>',
         f'<rect x="-10" y="{f(gy)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A2418" stroke="{INK}" stroke-width="2.4"></rect>']
    k = min(w / 560, h / 220)
    for i in range(5):                                         # seeds in the dark ground
        x = w * (0.08 + 0.08 * i); y = gy + (h - gy) * 0.5 + (i % 2) * 6
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(6 * k)}" ry="{f(3.6 * k)}" fill="#C8A060" stroke="{INK}" stroke-width="1.2"></ellipse>')
    r = random.Random(seed)
    for i in range(14):                                        # the grain risen in light
        x = w * (0.54 + 0.032 * i)
        top = gy - h * r.uniform(0.34, 0.5)
        o.append(f'<path d="M{f(x)} {f(gy + (h - gy) * 0.5)} L {f(x + r.uniform(-4, 4))} {f(top)}" stroke="#B8983A" stroke-width="2.4"></path>'
                 f'<ellipse cx="{f(x)}" cy="{f(top - 6 * k)}" rx="{f(4 * k)}" ry="{f(10 * k)}" fill="#E8C870" stroke="{INK}" stroke-width="1"></ellipse>')
    o.append(f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="{INK}" stroke-width="4"></path>')
    o.append(plate_label(w * 0.25, h * 0.1, "SOWN", "#E8E2D6", 12, halo_="#2A2040") + plate_label(w * 0.75, h * 0.1, "RAISED", "#7A4A2A", 12, halo_="#FFF4C2"))
    return "".join(o)

def earthy_heavenly(p, w, h, seed):
    """The first man is of the earth, earthy: the second man is of heaven: at the left on the bare brown earth a man in a
    robe of the colour of the dust; at the right, in the light of heaven, Jesus risen in white light."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp"), f'<rect x="-10" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#C8A06A"></rect>',
         f'<rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#2A3A7A"></rect>',
         f'<defs><clipPath id="{p}eh"><rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}"></rect></clipPath></defs>',
         f'<g clip-path="url(#{p}eh)">' + halo(w * 0.75, h * 0.4, h * 0.8, "#FFF4C2", 0.6) + rays(w * 0.75, h * 0.4, 20, h * 0.2, h, "#FFF4C2", 0.3, 4) + '</g>',
         f'<rect x="-10" y="{f(b)}" width="{f(w * 0.5 + 10)}" height="{f(h)}" fill="#7A5030" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, b - min(h * 0.78, 210))
    o.append(robed(p, w * 0.25, b, s, "#8A6A44", hair="#3A2A1A", beard="#3A2A1A", flip=True))
    o.append(f'<g clip-path="url(#{p}eh)">' + risen_fig(p, w * 0.75, b, h * 0.7 / 205) + '</g>')
    o.append(f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="{INK}" stroke-width="4"></path>')
    o.append(plate_label(w * 0.25, h * 0.08, "OF THE EARTH", "#3A2418", 11, halo_="#E8D0A0") + plate_label(w * 0.75, h * 0.08, "OF HEAVEN", "#FFF8E6", 11, halo_="#2A3A7A"))
    return "".join(o)

def last_trump(w, h, seed):
    """In the twinkling of an eye, at the last trump: for the trumpet shall sound, and the dead shall be raised: the dawn
    breaking in light over a hillside of tombs, every stone rolled back and every door open and empty, the trumpet's blast
    across the sky (no one sounding it drawn)."""
    o = [sky(w, h, "#2A2A6A", "#FFE6A0"), halo(w * 0.5, h * 0.3, max(w, h) * 0.5, "#FFFFFF", 0.7), rays(w * 0.5, h * 0.3, 30, h * 0.1, max(w, h), "#FFF4C2", 0.3, 4)]
    tx, ty = w * 0.16, h * 0.18                                # the blast of sound across the sky
    for k in range(4):
        rr = h * (0.12 + 0.08 * k)
        o.append(f'<path d="M{f(tx + rr * 0.6)} {f(ty - rr * 0.5)} A {f(rr)} {f(rr * 0.8)} 0 0 1 {f(tx + rr * 0.6)} {f(ty + rr * 0.5)}" fill="none" stroke="#FFD23F" stroke-width="3" opacity="{0.9 - 0.15 * k:.2f}"></path>')
    o.append(trumpet(tx - h * 0.1, ty + h * 0.02, min(0.5, h / 600), rot=-8))
    o.append(f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.5)} {f(w * 0.7)} {f(h * 0.54)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>')
    r = random.Random(seed)
    for i in range(6):                                         # the tombs, open and lit within
        x = w * (0.1 + 0.16 * i); y = h * (0.7 + 0.08 * (i % 2)); tw = min(w * 0.07, h * 0.16)
        o.append(f'<path d="M{f(x - tw / 2)} {f(y)} L {f(x - tw / 2)} {f(y - tw * 0.8)} Q {f(x)} {f(y - tw * 1.3)} {f(x + tw / 2)} {f(y - tw * 0.8)} L {f(x + tw / 2)} {f(y)} Z" fill="#FFF4C2" stroke="{INK}" stroke-width="2"></path>'
                 f'<circle cx="{f(x + tw * 0.9)}" cy="{f(y - tw * 0.4)}" r="{f(tw * 0.45)}" fill="#A89A8A" stroke="{INK}" stroke-width="2"></circle>')
    o.append(jp(w * 0.62, h * 0.2, "パーッ", min(40, h * 0.16), fill="#FFD23F", stroke="#0D0D0F", rot=-4, roman="PAA"))
    return "".join(o)

def empty_tomb(p, w, h, seed):
    """Death is swallowed up in victory: inside the tomb, the stone shelf empty, the linen lying folded, the morning light
    falling through the open door (Matthew's drawing)."""
    return linen(p, w, h, seed)

# ---- 1 Corinthians 16 --------------------------------------------------------------------------------------------------
def collection(p, w, h, seed):
    """Upon the first day of the week let each one of you lay by him in store: a room at dawn, a man of the church kneeling
    by a small chest and laying coins in it, his wife bringing her own; the window bright with the morning."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#C8A878", floor="#7A5A3A"),
         f'<rect x="{f(w * 0.08)}" y="{f(h * 0.16)}" width="{f(w * 0.14)}" height="{f(h * 0.3)}" fill="#FFE6A0" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.08)} {f(h * 0.16)} L {f(w * 0.4)} {f(b)} L {f(w * 0.16)} {f(b)} Z" fill="#FFF4C2" opacity="0.35"></path>']
    k = min(1.2, h / 220)
    cx = w * 0.5
    o.append(f'<rect x="{f(cx - 34 * k)}" y="{f(b - 40 * k)}" width="{f(68 * k)}" height="{f(40 * k)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2.2"></rect>'
             f'<path d="M{f(cx - 34 * k)} {f(b - 40 * k)} L {f(cx - 26 * k)} {f(b - 56 * k)} L {f(cx + 42 * k)} {f(b - 56 * k)} L {f(cx + 34 * k)} {f(b - 40 * k)} Z" fill="#8A5A30" stroke="{INK}" stroke-width="2"></path>'
             + "".join(f'<ellipse cx="{f(cx + d * k)}" cy="{f(b - 44 * k)}" rx="{f(5 * k)}" ry="{f(2 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="1"></ellipse>' for d in (-14, -2, 10, 20)))
    s = fit(b, b - min(h * 0.72, 196))
    o.append(E.kneel(cx - 70 * k, b, s * 0.86, color="#5A6A7A", skin=SKIN, flip=False))
    coin = '<circle cx="-62" cy="-140" r="5" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></circle>'
    o.append(robed(p, w * 0.78, b, s * 0.94, "#7A5A6A", woman=True, veil="#2A2A4A", up=[(-22, -158), (-42, -144), (-60, -140)], extra=coin))
    return "".join(o)

def journey_plan(w, h):
    """I will come unto you, when I shall have passed through Macedonia … but I will tarry at Ephesus until Pentecost: Paul's
    road on the map — from Ephesus up to Troas, over the sea to Macedonia, down to Corinth."""
    rt = ["EPHESUS", (26.9, 38.8), "TROAS", (25.4, 40.4), "NEAPOLIS", "PHILIPPI", "THESSALONICA", "BERŒA", (22.4, 39.0), "CORINTH"]
    return letter_road(w, h, rt, title="1 CORINTHIANS 16:5–8 · THROUGH MACEDONIA TO CORINTH", box=(21.2, 28.4, 37.2, 41.4),
                       places=("EPHESUS", "TROAS", "PHILIPPI", "THESSALONICA", "BERŒA", "CORINTH", "ATHENS"), hi=("EPHESUS", "CORINTH"),
                       regions=("ACHAIA", "ASIA", "MACEDONIA"))

def brethren_sent(p, w, h, seed):
    """Now if Timothy come … set him forward on his journey in peace … as touching Apollos the brother: the harbour of
    Ephesus at morning, Timothy with his staff and bundle setting out toward the ship, Apollos standing on the quay to see
    him off, the sea and the sail beyond."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#8FD0E2", "#F3E8C8"), sea_(w, h, h * 0.56, seed),
         f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h)}" fill="#B8A88A" stroke="{INK}" stroke-width="2.4"></rect>']
    o.append(ship(w * 0.76, h * 0.6, min(0.6, h / 360)))
    s = fit(b, b - min(h * 0.7, 190))
    bundle = '<path d="M-14 -170 L -40 -40" stroke="#6A4A2A" stroke-width="4"></path><ellipse cx="18" cy="-150" rx="14" ry="18" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
    o.append(timothy_r(p, w * 0.42, b, s, flip=True, extra=bundle))
    o.append(apollos_r(p, w * 0.16, b, s, flip=True, up=[(-22, -158), (-40, -176), (-50, -200)]))
    o.append(plate_label(w * 0.42, h * 0.08, "TIMOTHY", "#12113A", 11, halo_="#F3EFE6") + plate_label(w * 0.16, h * 0.08, "APOLLOS", "#12113A", 11, halo_="#F3EFE6"))
    return "".join(o)

def own_hand(p, w, h, seed):
    """The salutation of me Paul with mine own hand: Paul himself kneeling at the low table, the reed pen in his own hand,
    writing the last lines at the foot of the roll by the lamp; Sosthenes standing by."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp"), room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * 0.5, b - h * 0.3, max(w, h) * 0.6, f"{p}oh", op=0.55)]
    k = min(1.2, h / 220)
    tx = w * 0.36
    o.append(EP.low_table(tx, b, 150 * k, k) + clay_lamp(tx + 130 * k, b - 31 * k, k * 0.8) + inkpot(tx + 104 * k, b - 30 * k, k * 0.6))
    o.append(f'<g transform="rotate(-2 {f(tx + 50 * k)} {f(b - 34 * k)})">' + open_letter(tx + 10 * k, b - 40 * k, 80 * k, 10 * k, rows=2, seed=seed) + '</g>')
    s = fit(b, b - min(h * 0.72, 196))
    o.append(_seated_lap(tx - 6 * k, b, s * 0.8, ROBES["paul"], "#5A4A3A", "#3A2A1A", '<path d="M10 -96 L 64 -60" stroke="#0D0D0F" stroke-width="10" stroke-linecap="round"></path><path d="M10 -96 L 64 -60" stroke="#6A4A2A" stroke-width="7" stroke-linecap="round"></path><path d="M64 -60 L 76 -84" stroke="#C8A060" stroke-width="2.4"></path>'))
    o.append(sosthenes(p, w * 0.82, b, s))
    return "".join(o)

def three_portrait(t1, t2, t3, light="#FFE680", ground=("#3A2A3A", "#8A5A4A")):
    """A greeting cell's portrait of three: three shaded profile faces looking right, one behind another (epistle.face_portrait
    made for three)."""
    def draw(p, w, h):
        uid = f"{p}tp"
        o = [f'<defs><radialGradient id="{uid}" cx="0.7" cy="0.3" r="0.9"><stop offset="0" stop-color="{light}"></stop><stop offset="0.45" stop-color="{ground[1]}"></stop>'
             f'<stop offset="1" stop-color="{ground[0]}"></stop></radialGradient></defs><rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="url(#{uid})"></rect>']
        s3 = min(w / 360, (h + 10) / 460) * 0.86
        o.append(mk.face(t3, f(w * 0.36 - 40 * s3), f(h - 380 * s3 - h * 0.18), round(s3, 3)))
        s2 = min(w / 330, (h + 10) / 420) * 0.92
        o.append(mk.face(t2, f(w * 0.18 - 40 * s2), f(h - 380 * s2 - h * 0.08), round(s2, 3)))
        s = min(w / 330, (h + 10) / 380)
        o.append(mk.face(t1, f(-40 * s - w * 0.08), f(h - 380 * s + 6), round(s, 3)))
        return "".join(o)
    return draw

def crowd_portrait(n=5, seed=1):
    """A greeting cell's portrait of many: a little crowd of the brethren standing together."""
    def fig(p, x, y, s):
        o = []
        for i in range(n):
            o.append(folk(p, x + (i - (n - 1) / 2) * 30 * s, y - (i % 2) * 6 * s, s * (0.78 if i % 2 else 0.86), i + seed))
        return "".join(o)
    return portrait(fig, bg=("#8FD0E2", "#F3E8C8"))
