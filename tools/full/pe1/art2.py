"""Drawings for 1 Peter 3–5: the household, Sarah, a reason of the hope, the ark, hospitality, the fiery trial, the faithful
Creator, the flock and the crown of glory, the brethren greeting (see pe1/art.py)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from pe1.art import *
from jas.art import art, plate_label, _street, _road

def sarah_r(p, x, y, s, flip=False, up=None, extra=""):
    """Sarah in her old age (Genesis' look: a mulberry robe and veil, grey hair)."""
    return robed(p, x, y, s * 0.94, "#8A3A5A", woman=True, veil="#8A3A5A", hair="#B8B2A6", flip=flip, up=up, extra=extra)

def household(p, w, h, seed):
    """Ye wives, be in subjection to your own husbands; that, even if any obey not the word, they may without the word be
    gained by the behavior of their wives: the courtyard of a house at morning, the wife plainly veiled bringing bread and
    water to the table, the husband sitting at his work, watching her (the outward adorning, 3:3, is left in words)."""
    b = h * 0.94
    o = [D_(p), room(w, h, b, wall="#D8C098", floor="#A88A5A")]
    s = fit(b, max(h * 0.16, b - 225))
    o.append(f'<rect x="{f(w * 0.06)}" y="{f(h * 0.2)}" width="{f(w * 0.16)}" height="{f(b - h * 0.2)}" fill="#8FD0E2" stroke="{INK}" stroke-width="2.4"></rect>'
             + olive(w * 0.14, b, h / 600, seed=seed))
    o.append(low_table(w * 0.42, b, 110 * s, s) + f'<circle cx="{f(w * 0.42 + 30 * s)}" cy="{f(b - 36 * s)}" r="{f(7 * s)}" fill="#D8A860" stroke="{INK}" stroke-width="1.4"></circle>')
    jar = '<path d="M-74 -170 C -84 -170 -86 -150 -78 -140 L -60 -140 C -52 -150 -54 -170 -64 -170 Z" fill="#C8784A" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(robed(p, w * 0.34, b, s * 0.94, "#5A6A8A", woman=True, veil="#2A3A5A", flip=True, up=[(-22, -158), (-46, -150), (-66, -158)], extra=jar))
    o.append(robed(p, w * 0.7, b, s, "#7A5A3A", hair="#2A1A10", beard="#2A1A10", mantle="#4A3A2A", flip=False, pose="sit", seat="stool",
                   up=[(-22, -158), (-40, -130), (-56, -118)]))
    o.append(plate_label(w * 0.5, h * 0.08, "THE HIDDEN MAN OF THE HEART · A MEEK AND QUIET SPIRIT", "#3A2A1A", 9, halo_="#E8D8B0"))
    return "".join(o)

def sarah_tent(p, w, h, seed):
    """As Sarah obeyed Abraham, calling him lord: Abraham's tent at evening by the oaks, Sarah at the tent door greeting
    Abraham coming home with his staff (Genesis' looks)."""
    b = h * 0.92
    o = [D_(p), sky(w, h, "#3A2A5A", "#FFB07A"), hills(w, h, h * 0.58, seed, color="#6A5A5A", amp=12, step=90), ground(w, h, h * 0.66, "#A8885A", dy=0),
         olive(w * 0.92, h * 0.7, h / 360, seed=seed)]
    tx, tw = w * 0.3, w * 0.4
    o.append(black_tent(tx, b - 4, tw, h * 0.36))
    s = fit(b, max(h * 0.24, b - 200))
    o.append(sarah_r(p, tx + tw * 0.16, b, s, flip=True, up=[(-22, -158), (-40, -140), (-58, -136)]))
    staff = '<path d="M-52 -176 L -46 4" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"></path>'
    o.append(abraham_r(p, w * 0.7, b, s, flip=False, up=[(-22, -158), (-38, -124), (-48, -96)], extra=staff))
    o.append(plate_label(w * 0.5, h * 0.1, "SARAH OBEYED ABRAHAM, CALLING HIM LORD", "#3A1A2A", 9, halo_="#FFE0C0"))
    return "".join(o)

def couple_prayer(p, w, h, seed):
    """Ye husbands, … dwell with your wives according to knowledge, … joint-heirs of the grace of life; to the end that your
    prayers be not hindered: a husband and wife kneeling side by side in prayer at evening in their house, the lamp lit."""
    b = h * 0.94
    o = [D_(p), room(w, h, b, wall="#4A3A3A", floor="#2E2420"), lamp_glow(w * 0.5, h * 0.4, h * 0.7, f"{p}cp", op=0.5)]
    s = fit(b, max(h * 0.16, b - 225))
    o.append(f'<rect x="{f(w * 0.42)}" y="{f(h * 0.16)}" width="{f(w * 0.16)}" height="{f(h * 0.3)}" fill="#14183A" stroke="{INK}" stroke-width="2.4"></rect>'
             + f'<g transform="translate({f(w * 0.42)} {f(h * 0.16)})">' + mk.stars(8, w * 0.16, h * 0.3, seed) + '</g>'
             + clay_lamp(w * 0.5, b - 4, s * 0.8))
    o.append(E.kneel(w * 0.36, b, s * 0.92, color="#5A4A3A", skin=SKIN))
    o.append(luk_kneel(w * 0.64, b, s * 0.88, "#5A6A8A", "#2A3A5A", flip=True))
    o.append(plate_label(w * 0.5, h * 0.08, "JOINT-HEIRS OF THE GRACE OF LIFE", "#FFE6A0", 9, halo_="#2A1A1A"))
    return "".join(o)

from luk.art import kneel_w as luk_kneel

def answer(p, w, h, seed):
    """Being ready always to give answer to every man that asketh you a reason concerning the hope that is in you, yet with
    meekness and fear: a market street, a believer standing quietly, his hand on his breast, answering two townsmen who
    question him, others listening."""
    bg, b = _street(w, h, seed)
    s = fit(b, max(h * 0.16, b - 225))
    o = [D_(p), bg]
    o.append(man_r(p, w * 0.3, b, s, 1, flip=True, up=[(-22, -158), (-30, -128), (-20, -118)]))
    o.append(robed(p, w * 0.52, b, s, "#C8B898", hair="#4A3A2A", beard="#4A3A2A", mantle="#6A3A3A", flip=False, up=[(-22, -158), (-50, -150), (-76, -160)]))
    o.append(robed(p, w * 0.64, b, s * 0.98, "#E8DCC0", hair="#2A1A10", mantle="#3A5A7A"))
    o.append(woman_r(p, w * 0.12, b, s, 0))
    o.append(plate_label(w * 0.42, h * 0.08, "A REASON CONCERNING THE HOPE THAT IS IN YOU", "#3A2A1A", 9, halo_="#F3E8C8"))
    return "".join(o)

def ark_eight(w, h, seed):
    """When the longsuffering of God waited in the days of Noah, while the ark was a preparing, wherein few, that is, eight
    souls, were saved through water: the ark riding the flood under a clearing sky, the rain passing, and at its window the
    eight souls, eight faces small in the light."""
    r = random.Random(seed)
    o = [sky(w, h, "#3A4A6A", "#C8D8E0"), halo(w * 0.8, h * 0.2, h * 0.5, "#FFF4C2", 0.6),
         clouds(w, h * 0.1, seed, n=5, color="#5A6A80", op=0.9, ry=0.08, h=h)]
    for i in range(24):
        x = w * r.uniform(0.0, 0.45); y = h * r.uniform(0.1, 0.5)
        o.append(f'<path d="M{f(x)} {f(y)} l -4 14" stroke="#C8D8E8" stroke-width="1.6" opacity="0.7"></path>')
    wl = h * 0.7
    aw = w * 0.56; ax = w * 0.22
    o.append(ark_afloat(ax, wl, aw, "ae8"))
    ah = aw * 0.18
    wy = wl + ah * 0.35 - ah * 0.86                                     # the window under the roof, eight faces in it
    o.append(f'<rect x="{f(ax + aw * 0.2)}" y="{f(wy - ah * 0.08)}" width="{f(aw * 0.6)}" height="{f(ah * 0.2)}" fill="#FFC14D" stroke="{INK}" stroke-width="1.6"></rect>')
    for i in range(8):
        cx = ax + aw * (0.25 + i * 0.5 / 7)
        o.append(f'<circle cx="{f(cx)}" cy="{f(wy + ah * 0.04)}" r="{f(ah * 0.06)}" fill="#C98E66" stroke="{INK}" stroke-width="1"></circle>')
    o.append(sea_(w, h, wl, seed))
    o.append(dove(w * 0.84, h * 0.32, h / 500, wings="up"))
    o.append(plate_label(w * 0.5, h * 0.95, "EIGHT SOULS · SAVED THROUGH WATER", "#E8F6FA", 10, halo_="#0B2E4A"))
    return "".join(o)

def hospitality(p, w, h, seed):
    """Be sober unto prayer: above all things being fervent in your love among yourselves; … using hospitality one to
    another without murmuring: a house by lamplight, the brethren — men and women — sitting about one low table, the
    bread broken and passed, a traveller just come in at the door and welcomed."""
    b = h * 0.94
    o = [D_(p), room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * 0.46, h * 0.5, h * 0.8, f"{p}hs", op=0.5)]
    s = fit(b, max(h * 0.16, b - 225))
    o.append(f'<rect x="{f(w * 0.68)}" y="{f(b - 210 * s)}" width="{f(w * 0.12)}" height="{f(210 * s)}" fill="#141838" stroke="{INK}" stroke-width="2.4"></rect>')
    tx = w * 0.14
    o.append(low_table(tx, b, 170 * s, s) + clay_lamp(tx + 86 * s, b - 31 * s, s * 0.6)
             + "".join(f'<circle cx="{f(tx + (26 + i * 40) * s)}" cy="{f(b - 36 * s)}" r="{f(7 * s)}" fill="#D8A860" stroke="{INK}" stroke-width="1.4"></circle>' for i in (0, 1, 3)))
    o.append(robed(p, tx - 4 * s, b, s, "#6A5A4A", hair="#2A1A10", beard="#2A1A10", flip=True, pose="sit", seat="stool", up=[(-22, -158), (-44, -134), (-66, -128)]))
    o.append(robed(p, tx + 214 * s, b, s * 0.96, "#4A6A6A", woman=True, veil="#1F3A3A", flip=False, pose="sit", seat="stool"))
    o.append(man_r(p, w * 0.6, b, s, 2, flip=True, up=[(-22, -158), (-48, -148), (-70, -150)]))
    staff = '<path d="M-52 -176 L -46 4" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"></path>'
    o.append(robed(p, w * 0.74, b, s * 0.98, "#7A7262", head="#3A3A4A", cord="#1A1210", beard="#3A2A1A", flip=False, up=[(-22, -158), (-38, -124), (-48, -96)], extra=staff))
    o.append(plate_label(w * 0.44, h * 0.08, "USING HOSPITALITY ONE TO ANOTHER", "#FFE6A0", 9, halo_="#2A1A12"))
    return "".join(o)

def fiery_trial(w, h, seed):
    """Think it not strange concerning the fiery trial among you, which cometh upon you to prove you: the refiner's furnace
    roaring, the silver in the crucible within it, and the refiner's lamp and tongs set by — the trial as the fire that proves
    metal."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A0E0A"></rect>', halo(w * 0.5, h * 0.62, h * 0.9, "#FF6A2A", 0.55)]
    k = h / 300
    cx, b = w * 0.5, h * 0.9
    o.append(f'<path d="M{f(cx - 150 * k)} {f(b)} L {f(cx - 120 * k)} {f(b - 200 * k)} C {f(cx - 60 * k)} {f(b - 250 * k)} {f(cx + 60 * k)} {f(b - 250 * k)} {f(cx + 120 * k)} {f(b - 200 * k)} L {f(cx + 150 * k)} {f(b)} Z" fill="#5A3A2A" stroke="{INK}" stroke-width="3"></path>')
    for i in range(6):
        y = b - i * 34 * k
        o.append(f'<path d="M{f(cx - 146 * k + i * 4 * k)} {f(y)} L {f(cx + 146 * k - i * 4 * k)} {f(y)}" stroke="#3A2418" stroke-width="2"></path>')
    o.append(f'<path d="M{f(cx - 70 * k)} {f(b)} L {f(cx - 70 * k)} {f(b - 90 * k)} C {f(cx - 70 * k)} {f(b - 150 * k)} {f(cx + 70 * k)} {f(b - 150 * k)} {f(cx + 70 * k)} {f(b - 90 * k)} L {f(cx + 70 * k)} {f(b)} Z" fill="#FFE680" stroke="{INK}" stroke-width="2.4"></path>')
    for i in range(7):
        o.append(flame(cx + (i - 3) * 20 * k, b - 4, k * r.uniform(0.7, 1.1), seed + i))
    o.append(f'<path d="M{f(cx - 26 * k)} {f(b - 70 * k)} L {f(cx + 26 * k)} {f(b - 70 * k)} L {f(cx + 18 * k)} {f(b - 30 * k)} L {f(cx - 18 * k)} {f(b - 30 * k)} Z" fill="#8A4A2A" stroke="{INK}" stroke-width="2"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(b - 70 * k)}" rx="{f(26 * k)}" ry="{f(6 * k)}" fill="#F3F3FF" stroke="{INK}" stroke-width="1.6"></ellipse>')
    o.append(smoke(cx, b - 260 * k, 4, seed, color="#3A2A2A", op=0.6, k=k))
    o.append(plate_label(w * 0.5, h * 0.08, "THE FIERY TRIAL · TO PROVE YOU", "#FFE6A0", 10, halo_="#1A0E0A"))
    return "".join(o)

def faithful_creator(p, w, h, seed):
    """Let them also that suffer according to the will of God commit their souls in well-doing unto a faithful Creator: the
    dawn coming up over the sea and the hills of the earth, the works of his hands, and a believer standing on the shore
    with his hands lifted."""
    b = h * 0.92
    o = [D_(p), sky(w, h, "#2A2A5A", "#FFC890"), halo(w * 0.7, h * 0.56, h * 0.6, "#FFE680", 0.6),
         f'<circle cx="{f(w * 0.7)}" cy="{f(h * 0.56)}" r="{f(h * 0.08)}" fill="#FFF4C2"></circle>', rays(w * 0.7, h * 0.56, 24, h * 0.12, w, "#FFF4C2", 0.25, 3),
         sea_(w, h, h * 0.58, seed), hills(w, h, h * 0.54, seed, color="#3A3A5A", amp=20, step=120).replace('M-10', 'M-10', 1)]
    o.append(f'<path d="M-10 {f(h * 0.72)} C {f(w * 0.2)} {f(h * 0.7)} {f(w * 0.4)} {f(h * 0.76)} {f(w * 0.55)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B8A07A" stroke="{INK}" stroke-width="2"></path>')
    s = fit(b, max(h * 0.24, b - 200))
    o.append(man_r(p, w * 0.24, b, s, 0, flip=True, up=[(-22, -158), (-28, -196), (-30, -232)]))
    for i in range(3): o.append(bird(w * (0.5 + i * 0.06), h * (0.24 + (i % 2) * 0.04), h / 300, "#2A2A3A"))
    o.append(plate_label(w * 0.5, h * 0.1, "UNTO A FAITHFUL CREATOR", "#2A1A3A", 10, halo_="#FFE0C0"))
    return "".join(o)

# ---- 1 Peter 5 ------------------------------------------------------------------------------------------------------------
def elder_flock(p, w, h, seed):
    """Tend the flock of God which is among you, exercising the oversight, … making yourselves ensamples to the flock: an
    elder of the church as a shepherd on the hillside at morning, his staff in hand, going before the flock, a lamb carried
    in his arm."""
    b = h * 0.92
    o = [D_(p), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.5, seed, color="#8AAA6A", amp=14, step=90),
         f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.58)} {f(w * 0.7)} {f(h * 0.62)} {f(w + 10)} {f(h * 0.58)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#9ABA6A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.2, b - 210))
    crook = '<path d="M30 -170 L 36 4" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"></path><path d="M30 -170 C 26 -186 40 -192 46 -182" stroke="#5A3A22" stroke-width="5" fill="none"></path>'
    o.append(elder_r(p, w * 0.24, b, s, 2, flip=True, up=[(-22, -158), (-46, -150), (-70, -150)], extra=crook))
    r = random.Random(seed)
    for i in range(9):
        x = w * (0.36 + i * 0.06) + r.uniform(-10, 10); y = b - r.uniform(0, h * 0.18)
        o.append(E.sheep(x, y, s * r.uniform(0.48, 0.6), flip=True))
    o.append(plate_label(w * 0.6, h * 0.1, "TEND THE FLOCK OF GOD", "#2A3A1A", 10, halo_="#F3F8E8"))
    return "".join(o)

def crown_glory(w, h, seed):
    """When the chief Shepherd shall be manifested, ye shall receive the crown of glory that fadeth not away: the gold wreath
    on its stone in the falling light (as James' crown of life)."""
    return crown_of_life(w, h, seed).replace("THE CROWN OF LIFE", "THE CROWN OF GLORY THAT FADETH NOT AWAY")

def greeting(p, w, h, seed):
    """Salute one another with a kiss of love. Peace be unto you all that are in Christ: the church in a house at Rome by
    lamplight, the brethren — men and women — rising to greet one another, two brothers clasping hands and embracing."""
    b = h * 0.94
    o = [D_(p), room(w, h, b, wall="#5E4A3C", floor="#3A2E26"), lamp_glow(w * 0.34, h * 0.45, h * 0.8, f"{p}gr", op=0.5)]
    s = fit(b, max(h * 0.3, b - 250))
    o.append(rome_window(w * 0.66, b - 230 * s, min(w * 0.17, 115 * s), min(h * 0.3, 95 * s), True, seed))
    o.append(woman_r(p, w * 0.08, b, s, 0, flip=True))
    o.append(man_r(p, w * 0.2, b, s, 1, flip=True, up=[(-22, -158), (-46, -150), (-66, -146)]))
    o.append(man_r(p, w * 0.32, b, s, 2, flip=False, up=[(-22, -158), (-46, -150), (-66, -146)]))
    o.append(woman_r(p, w * 0.425, b, s, 1, flip=True, up=[(-22, -158), (-44, -140), (-60, -134)]))
    o.append(robed(p, w * 0.535, b, s * 0.98, "#C8B898", hair="#4A3A2A", beard="#4A3A2A", mantle="#6A3A3A", flip=False, up=[(-22, -158), (-44, -140), (-60, -134)]))
    o.append(plate_label(w * 0.32, h * 0.08, "A KISS OF LOVE · PEACE BE UNTO YOU ALL", "#FFE6A0", 9, halo_="#2A1A12"))
    return "".join(o)

from epistle import rome_window
from gal.art import black_tent
