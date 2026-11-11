"""Drawings for Romans chapter 2 (Romans 4–7), on top of rom.art. Abraham under the stars (Genesis 15) and at his tent door
with Sarah, both old; the harp and the psalm of David; the plate of faith reckoned before the sign (Genesis 15, then 17);
Abraham's road from Ur (Acts' map); the seed as the stars; the tomb opened at dawn; the chain of tribulation to hope; the
three crosses far off against the darkened sky (ntcast's rule: from a distance, nothing in detail); the garden shut and
the tree; the plate of death reigning from Adam until Moses; the one and the many; grace abounding as light over the
waters; baptism in the river, the sealed tomb and the dawn; the broken chains; wages and the free gift; the bond of the
law; Sinai and the two tables; a man standing between the lamp and his own shadow (no torment drawn). Abraham and Sarah
keep Genesis' colours (a slate-blue robe, grey hair and beard; Sarah's mulberry headscarf over grey hair), drawn on the
kit silhouettes (epistle.robed)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from rom.art import *
from rom.art import f, INK, GOLD, CY, plate_label, _heart, _tablets
from genesis.art3 import ABRAM_ROBE, SARAI_ROBE
import exodus4 as E4, exodus5 as V5, judges1 as G1
from ecc.art import tree
from kg1.art import ship

ABRAHAM_HAIR, ABRAHAM_BEARD = "#9A948A", "#B8B2A6"
def abraham(p, x, y, s, flip=False, up=None):
    """Abraham as Genesis draws him: a slate-blue robe, grey hair and beard (on the kit silhouette)."""
    return robed(p, x, y, s, ABRAM_ROBE, hair=ABRAHAM_HAIR, beard=ABRAHAM_BEARD, mantle="#1E3458", belt="#1A2A44", flip=flip, up=up)
def sarah_old(p, x, y, s, flip=False, up=None):
    """Sarah old: her mulberry headscarf over grey hair (Genesis)."""
    return robed(p, x, y, s * 0.94, "#6A4A5A", woman=True, veil=SARAI_ROBE, flip=flip, up=up).replace('fill="#2A1A10"></path>', 'fill="#B8B2A6"></path>', 1)

def _milky(w, h, seed, n=320):
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0B0B2A"></rect>'
            f'<path d="M-10 {f(h * 0.75)} C {f(w * 0.3)} {f(h * 0.35)} {f(w * 0.6)} {f(h * 0.2)} {f(w + 10)} {f(-10)}" fill="none" stroke="#5B2470" stroke-width="{f(h * 0.3)}" opacity="0.4"></path>'
            + mk.stars(n, w, h * 0.85, seed) + mk.stars(n // 5, w, h * 0.7, seed + 1, color="#FFE680"))

def abraham_stars(p, w, h, seed, tent=True):
    """Look now toward heaven, and number the stars (Genesis 15:5): Abraham on the hill at night, his arm lifted to the stars,
    his tent below."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), _milky(w, h, seed)]
    r = random.Random(seed)
    o += [f'<path d="M{f(x)} {f(y - 8)} L {f(x + 2)} {f(y - 2)} L {f(x + 8)} {f(y)} L {f(x + 2)} {f(y + 2)} L {f(x)} {f(y + 8)} L {f(x - 2)} {f(y + 2)} L {f(x - 8)} {f(y)} L {f(x - 2)} {f(y - 2)} Z" fill="#FFF4C2"></path>'
          for x, y in [(r.uniform(0, w), r.uniform(0, h * 0.5)) for _ in range(7)]]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(b - h * 0.08)} C {f(w * 0.3)} {f(b - h * 0.16)} {f(w * 0.6)} {f(b - h * 0.04)} {f(w + 10)} {f(b + 4)} L {f(w + 10)} {f(h + 10)} Z" fill="#1A1430" stroke="#3A2A6A" stroke-width="2"></path>')
    if tent:
        tx, k = w * 0.76, min(1.4, h / 300)
        o.append(f'<path d="M{f(tx - 80 * k)} {f(b + 2)} L {f(tx - 50 * k)} {f(b - 64 * k)} L {f(tx + 54 * k)} {f(b - 68 * k)} L {f(tx + 86 * k)} {f(b + 2)} Z" fill="#2A1E1A" stroke="{INK}" stroke-width="2"></path>'
                 f'<path d="M{f(tx - 14 * k)} {f(b + 2)} L {f(tx)} {f(b - 50 * k)} L {f(tx + 14 * k)} {f(b + 2)} Z" fill="#FFC14D" stroke="{INK}" stroke-width="1.4"></path>')
    s = (h * 0.62) / 205
    o.append(abraham(p, w * 0.34, b - h * 0.1, s, up=[(-22, -158), (-14, -200), (0, -244)]))
    return "".join(o)

def seed_stars(w, h, seed):
    """So shall thy seed be: a sky crowded with stars to the horizon, a counter overflowing (a plate in the night)."""
    o = [_milky(w, h, seed, n=520), ground(w, h, h * 0.9, "#05050A", dy=0)]
    for i, (t, c) in enumerate([("NUMBERED ··· 001,284", "#8F9AFF"), ("NUMBERED ··· 048,911", "#8F9AFF"), ("NUMBERED ··· BEYOND COUNT", "#FFD23F")]):
        o.append(label(16, h * 0.9 - 36 + i * 13, t, c, 9.5, "start"))
    return "".join(o)

def tent_old(p, w, h, seed):
    """His own body now as good as dead (about a hundred years old), and the deadness of Sarah's womb: Abraham and Sarah,
    old, at the door of the tent at dusk under the oak, looking up to the first stars."""
    b = h * 0.93
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#2A1A3A", "#E8803A"), mk.stars(14, w, h * 0.3, seed),
         hills(w, h, h * 0.62, seed, color="#4A2A3A", amp=10, step=90), ground(w, h, h * 0.7, "#5A3A2A", dy=0)]
    o.append(G1.tent_big(w * 0.66, b, w * 0.5, h * 0.62, color="#3A2214", glow="#5A2A12") if hasattr(G1, "tent_big") else "")
    o.append(tree(w * 0.08, b, min(1.4, h / 300), color="#3A4A2A", seed=seed))
    s = (h * 0.66) / 205
    o.append(abraham(p, w * 0.32, b, s, flip=True) + sarah_old(p, w * 0.44, b, s))
    return "".join(o)

def harp(w, h, seed):
    """Blessed are they whose iniquities are forgiven (David, Psalm 32): the king's harp (a kinnor) and the open scroll of
    the psalm on a table by lamplight; no one there."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A2A"></rect>', lamp_glow(w * 0.6, h * 0.5, max(w, h) * 0.55, f"hp{seed}", op=0.5)]
    ty = h * 0.74
    o.append(f'<rect x="-10" y="{f(ty)}" width="{f(w + 20)}" height="{f(h)}" fill="#5A2E16" stroke="{INK}" stroke-width="2.4"></rect>')
    k = min(1.6, h / 220); x0 = w * 0.36
    o.append(f'<g transform="translate({f(x0)} {f(ty)}) scale({f(k)})">'
             '<path d="M-40 0 C -48 -40 -52 -90 -44 -120 L -30 -124 C -32 -90 -26 -50 -20 -8 Z" fill="#8A5A2A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<path d="M30 0 C 40 -40 50 -100 56 -128 L 44 -132 C 34 -100 22 -50 12 -6 Z" fill="#8A5A2A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<path d="M-50 -124 C -20 -142 30 -142 60 -134 L 58 -122 C 30 -128 -20 -128 -46 -112 Z" fill="#A86A30" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<path d="M-44 0 C -20 10 20 10 36 0 L 30 -14 C 10 -6 -16 -6 -36 -12 Z" fill="#6A3A1A" stroke="#0D0D0F" stroke-width="2.2"></path>'
             + "".join(f'<path d="M{-30 + i * 9} -8 L {-36 + i * 13} -126" stroke="#E8D8A0" stroke-width="1.4"></path>' for i in range(7)) + '</g>')
    o.append(f'<g transform="rotate(-4 {f(w * 0.66)} {f(ty)})">' + open_letter(w * 0.52, ty + h * 0.04, w * 0.3, h * 0.16, rows=4, seed=seed) + '</g>' + clay_lamp(w * 0.88, ty - 2, k * 0.8))
    return "".join(o)

def sign_after(w, h):
    """Faith reckoned in uncircumcision, the sign received after it as a seal: a technical timeline — Genesis 15, faith
    reckoned for righteousness; Genesis 17, the sign of circumcision, a seal; and from Abraham two lines of children, the
    uncircumcision and the circumcision, both walking in the steps of his faith."""
    o = [plate_bg(w, h, "ROMANS 4:10–12 · RECKONED, THEN SEALED")]
    y = h * 0.3; x0, x1 = w * 0.1, w * 0.9
    o.append(f'<path d="M{f(x0)} {f(y)} L {f(x1)} {f(y)}" stroke="{CY}" stroke-width="2"></path>')
    for x, t, c in ((x0 + (x1 - x0) * 0.18, "GENESIS 15 · FAITH RECKONED", GOLD), (x0 + (x1 - x0) * 0.72, "GENESIS 17 · THE SIGN, A SEAL", CY)):
        o.append(node(x, y, "", c, r=7) + label(x, y - 18, t, c, 10))
    o.append(dim(x0 + (x1 - x0) * 0.18, y + 22, x0 + (x1 - x0) * 0.72, y + 22, "IN UNCIRCUMCISION", size=9, color="#FFB07A"))
    ax = x0 + (x1 - x0) * 0.18
    o.append(mk.defs("sg412", *ALL))
    by = h - 16; s = (by - y - 70) / 205
    for i in range(5):
        xx = w * (0.12 + i * 0.07)
        o.append(mk.person("sg412", round(xx), round(by), round(s * (0.9 + 0.05 * (i % 2)), 3), body="#1E4A6A", cloth="#163A56", kind="Tunic", woman=i % 2 == 1, stroke=CY, sw=2.4))
    for i in range(5):
        xx = w * (0.6 + i * 0.07)
        o.append(mk.person("sg412", round(xx), round(by), round(s * (0.9 + 0.05 * (i % 2)), 3), body="#1E4A6A", cloth="#24506E", kind="Tunic", woman=i % 2 == 0, stroke=CY, sw=2.4, flip=True))
    o.append(route([(ax, y + 8), (w * 0.26, by - s * 215)], color=GOLD, sw=1.8, arrow=True) + route([(ax, y + 8), (w * 0.74, by - s * 215)], color=GOLD, sw=1.8, arrow=True))
    o.append(plate_label(w * 0.26, by - s * 215 - 8, "THE UNCIRCUMCISION", GOLD, 9) + plate_label(w * 0.74, by - s * 215 - 8, "THE CIRCUMCISION", GOLD, 9))
    return "".join(o)

def tomb_dawn(p, w, h, seed):
    """Raised for our justification: the tomb in the garden at dawn, the great stone rolled away, the door open on the dark,
    light rising behind the hill — no one drawn."""
    b = h * 0.92
    o = [sky(w, h, "#3A3A7A", "#FFC890"), halo(w * 0.78, h * 0.6, max(w, h) * 0.4, "#FFF4C2", 0.6), hills(w, h, h * 0.56, seed, color="#5A5A6A", amp=12, step=80),
         f'<path d="M{f(w * 0.12)} {f(b)} C {f(w * 0.16)} {f(h * 0.3)} {f(w * 0.66)} {f(h * 0.26)} {f(w * 0.72)} {f(b)} Z" fill="#9A8A7A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.3)} {f(b)} L {f(w * 0.3)} {f(h * 0.6)} Q {f(w * 0.37)} {f(h * 0.48)} {f(w * 0.44)} {f(h * 0.6)} L {f(w * 0.44)} {f(b)} Z" fill="#1A1210" stroke="{INK}" stroke-width="2.2"></path>',
         f'<circle cx="{f(w * 0.58)}" cy="{f(b - h * 0.16)}" r="{f(h * 0.16)}" fill="#B8A898" stroke="{INK}" stroke-width="2.4"></circle>',
         ground(w, h, b, "#6A7A4A", dy=0), olive(w * 0.88, h * 0.98, min(1.0, h / 330), seed=seed)]
    return "".join(o)

def hope_chain(w, h):
    """Tribulation worketh stedfastness; and stedfastness, approvedness; and approvedness, hope: a plate — four links of a
    chain from dark to light, and the heart into which the love of God is shed abroad."""
    o = [plate_bg(w, h, "ROMANS 5:3–5 · TRIBULATION · STEDFASTNESS · APPROVEDNESS · HOPE")]
    y = h * 0.5; n = 4
    cols = ["#4A4A5A", "#6A6A7A", "#B8A06A", "#FFD23F"]
    names = ["TRIBULATION", "STEDFASTNESS", "APPROVEDNESS", "HOPE"]
    k = min(w / 760, h / 240)
    for i in range(n):
        x = w * (0.12 + i * 0.19)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(46 * k)}" ry="{f(28 * k)}" fill="none" stroke="#0D0D0F" stroke-width="{f(16 * k)}"></ellipse>'
                 f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(46 * k)}" ry="{f(28 * k)}" fill="none" stroke="{cols[i]}" stroke-width="{f(11 * k)}"></ellipse>')
        o.append(label(x, y + 52 * k, names[i], cols[i] if i else "#9A9AB0", 9.5))
    hx = w * 0.86
    o.append(_heart(hx, y - 4, 40 * k, writing=False) + rays(hx, y - 4, 14, 44 * k, 80 * k, "#FFF4C2", 0.35, 3)
             + label(hx, y + 52 * k, "THE LOVE OF GOD", GOLD, 9.5))
    return "".join(o)

def crosses_far(p, w, h, seed):
    """Christ died for the ungodly: Golgotha far off, three crosses small against the darkened sky (Matthew's drawing)."""
    return golgotha(p, w, h, seed, dark=True)

def garden_shut(w, h, seed):
    """Through one man sin entered into the world, and death through sin: the garden in the east shut — its wall and its
    closed gate, the tree beyond it, and the flame of the sword turning every way before it (Genesis 3:24; no cherub drawn,
    no serpent); outside, the bare ground under a dusk sky."""
    b = h * 0.92
    o = [sky(w, h, "#2A1A3A", "#C8704A"), hills(w, h, h * 0.5, seed, color="#3A2A3A", amp=12, step=90)]
    wy = h * 0.42
    o.append(f'<rect x="-10" y="{f(wy)}" width="{f(w + 20)}" height="{f(h * 0.28)}" fill="#8A7A5A" stroke="{INK}" stroke-width="2.4"></rect>')
    for i in range(int(w / 40) + 1):
        o.append(f'<path d="M{f(i * 40)} {f(wy)} L {f(i * 40)} {f(wy + h * 0.28)}" stroke="#6A5A3A" stroke-width="1.4"></path>')
    tk = min(1.6, h / 260)
    o.append(f'<g>{tree(w * 0.62, wy + 10, tk, color="#2E6B3A", seed=seed)}</g>'.replace("<g>", "<g>", 1))
    gx, gw = w * 0.36, w * 0.14
    o.append(f'<rect x="{f(gx - gw / 2)}" y="{f(wy + h * 0.04)}" width="{f(gw)}" height="{f(h * 0.24)}" fill="#4A3018" stroke="{INK}" stroke-width="3"></rect>'
             f'<path d="M{f(gx)} {f(wy + h * 0.04)} L {f(gx)} {f(wy + h * 0.28)}" stroke="{INK}" stroke-width="2.4"></path>'
             f'<rect x="{f(gx - gw / 2 - 6)}" y="{f(wy + h * 0.14)}" width="{f(gw + 12)}" height="{f(h * 0.025)}" fill="#2A1A0A" stroke="{INK}" stroke-width="1.6"></rect>')
    fx, fy = gx + gw * 0.9, wy - h * 0.06
    o.append(halo(fx, fy, h * 0.14, "#FF8A3D", 0.6))
    for a in range(0, 360, 45):
        r_ = math.radians(a)
        o.append(f'<path d="M{f(fx)} {f(fy)} L {f(fx + math.cos(r_) * h * 0.09)} {f(fy + math.sin(r_) * h * 0.09)}" stroke="#FFD23F" stroke-width="3" stroke-linecap="round"></path>')
    o.append(ground(w, h, wy + h * 0.28, "#5A4A3A", dy=0))
    return "".join(o)

def adam_moses(w, h):
    """Death reigned from Adam until Moses: a technical timeline — ADAM at the left, MOSES and the law at the right, the
    span between dark under the word DEATH REIGNED, and from the law onward the trespass abounding."""
    o = [plate_bg(w, h, "ROMANS 5:12–14 · FROM ADAM UNTIL MOSES")]
    y = h * 0.56; x0, x1 = w * 0.1, w * 0.86
    o.append(f'<rect x="{f(x0)}" y="{f(y - h * 0.16)}" width="{f(x1 - x0)}" height="{f(h * 0.16)}" fill="#05050E" stroke="#FF6A4A" stroke-width="1.4"></rect>'
             + label((x0 + x1) / 2, y - h * 0.065, "DEATH REIGNED", "#FF6A4A", 11))
    o.append(f'<path d="M{f(x0)} {f(y)} L {f(w * 0.96)} {f(y)}" stroke="{CY}" stroke-width="2"></path>')
    o.append(node(x0, y, "", GOLD, r=7) + label(x0, y + 26, "ADAM", GOLD, 11) + node(x1, y, "", CY, r=7) + label(x1, y + 26, "MOSES · THE LAW", CY, 11))
    o.append(_tablets(x1, y - h * 0.3, min(0.5, h / 600)))
    for i in range(7):
        xx = x0 + (x1 - x0) * (i + 1) / 8
        o.append(f'<path d="M{f(xx)} {f(y - 6)} L {f(xx)} {f(y + 6)}" stroke="{CY}" stroke-width="1.4"></path>')
    return "".join(o)

def one_many(w, h):
    """As through the one man's disobedience the many were made sinners, even so through the obedience of the one shall
    the many be made righteous: a plate — at the left one node in shadow branching to many figures in shadow; at the
    right one node of light branching to many figures in light."""
    o = [plate_bg(w, h, "ROMANS 5:18–19 · THE ONE AND THE MANY"), mk.defs("om519", *ALL)]
    by = h - 14; ny = h * 0.3
    s = (by - ny - 50) / 205 * 0.7
    for side, (cx, col, glow_, t1, t2) in enumerate(((w * 0.25, "#3A3A4A", "#FF6A4A", "ONE TRESPASS", "UNTO CONDEMNATION"),
                                                     (w * 0.75, "#E8D8A0", "#FFE680", "ONE ACT OF RIGHTEOUSNESS", "UNTO JUSTIFICATION OF LIFE"))):
        o.append((halo(cx, ny, 50, glow_, 0.5) if side else "") + node(cx, ny, "", glow_, r=9) + label(cx, ny - 18, t1, glow_ if side else "#C8C8E8", 10))
        for i in range(7):
            xx = cx + (i - 3) * w * 0.055
            o.append(f'<path d="M{f(cx)} {f(ny + 10)} L {f(xx)} {f(by - s * 205 - 6)}" stroke="{glow_}" stroke-width="1.2" opacity="0.6"></path>')
            o.append(mk.person("om519", round(xx), round(by), round(s, 3), body="#1E2A3A" if not side else "#E8D8A0", cloth="#141C28" if not side else "#C8B880",
                               kind="Tunic", woman=i % 2 == 1, stroke=CY if not side else "#8A6A2A", sw=2.4, flip=i % 2 == 0))
        o.append(label(cx, by - s * 205 - 16, t2, glow_ if side else "#C8C8E8", 9))
    o.append(f'<path d="M{f(w * 0.5)} 34 L {f(w * 0.5)} {f(h - 8)}" stroke="#2C5A7A" stroke-width="1.4" stroke-dasharray="5 5"></path>')
    return "".join(o)

def grace_flood(w, h, seed):
    """Where sin abounded, grace did abound more exceedingly: the great sea at sunrise, a river of light poured over the
    waters from the dawn."""
    o = [sky(w, h, "#2A2A6A", "#FFE6A0"), halo(w * 0.5, h * 0.6, max(w, h) * 0.6, "#FFF4C2", 0.7), rays(w * 0.5, h * 0.6, 32, h * 0.06, max(w, h), "#FFF4C2", 0.3, 4),
         sea_(w, h, h * 0.6, seed, color="#1F6F9A", deep="#0F4C68"),
         f'<path d="M{f(w * 0.46)} {f(h * 0.6)} L {f(w * 0.54)} {f(h * 0.6)} L {f(w * 0.8)} {f(h + 10)} L {f(w * 0.2)} {f(h + 10)} Z" fill="#FFF4C2" opacity="0.5"></path>']
    return "".join(o)

def baptism(p, w, h, seed):
    """Baptized into his death, buried with him through baptism: a river at dawn, a man standing in the water to the waist,
    bowed to go under, another beside him with a hand on his shoulder; the bank and reeds."""
    b = h * 0.95
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#3A3A7A", "#FFC890"), hills(w, h, h * 0.4, seed, color="#6A6A5A", amp=14, step=90),
         ground(w, h, h * 0.5, "#8A8A5A", dy=0)]
    wy = h * 0.6
    s = (h * 0.9) / 205; b = h * 1.08
    o.append(paul_fig(p, w * 0.42, b, s, flip=True, up=[(-22, -158), (-40, -150), (-58, -150)]))
    o.append(robed(p, w * 0.42 + 70 * s, b + 14 * s, s * 0.98, "#E8E2D6", hair="#2A1A10", beard="#2A1A10", flip=True))
    o.append(f'<rect x="-10" y="{f(wy)}" width="{f(w + 20)}" height="{f(h)}" fill="#2C7DA8" opacity="0.92"></rect>'
             + "".join(f'<path d="M{f(x)} {f(wy + 8 + (i % 3) * 14)} l {f(40)} 0" stroke="#BFE6F2" stroke-width="2" opacity="0.8"></path>' for i, x in enumerate(range(10, int(w), 70)))
             + f'<path d="M-10 {f(wy)} L {f(w + 10)} {f(wy)}" stroke="{INK}" stroke-width="2"></path>')
    for i in range(14):
        x = w * (0.02 + i * 0.012) if i < 7 else w * (0.86 + (i - 7) * 0.018)
        o.append(f'<path d="M{f(x)} {f(wy + 4)} L {f(x + 3)} {f(wy - h * 0.18)}" stroke="#4A6A2A" stroke-width="2.4"></path>')
    return "".join(o)

def sealed_tomb(p, w, h, seed):
    """Buried with him: the tomb in the rock at dusk, the round stone rolled to its door and sealed (Matthew's drawing)."""
    return tomb(p, w, h, seed, sealed=True)

def broken_chains(w, h, seed):
    """Being made free from sin: a chain broken open on the stones in the morning light, its links scattered (no one)."""
    o = [sky(w, h, "#6A8AB0", "#FFF4C2"), halo(w * 0.7, h * 0.3, max(w, h) * 0.4, "#FFFFFF", 0.6), ground(w, h, h * 0.62, "#A89A80", dy=0)]
    k = min(w / 600, h / 240)
    pts = [(w * 0.12 + i * 34 * k, h * 0.78 + math.sin(i * 0.9) * 10 * k) for i in range(8)] + [(w * 0.62 + i * 34 * k, h * 0.8 + math.sin(i * 1.2) * 10 * k) for i in range(6)]
    for i, (x, y) in enumerate(pts):
        rot = 0 if i % 2 else 90
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(18 * k)}" ry="{f(10 * k)}" transform="rotate({rot} {f(x)} {f(y)})" fill="none" stroke="#0D0D0F" stroke-width="{f(9 * k)}"></ellipse>'
                 f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(18 * k)}" ry="{f(10 * k)}" transform="rotate({rot} {f(x)} {f(y)})" fill="none" stroke="#8A8A94" stroke-width="{f(5.5 * k)}"></ellipse>')
    bx = w * 0.5
    o.append(f'<path d="M{f(bx - 20 * k)} {f(h * 0.8)} c 6 -14 14 -16 18 -6 M{f(bx + 12 * k)} {f(h * 0.78)} c 4 10 -2 18 -12 16" fill="none" stroke="#8A8A94" stroke-width="{f(5.5 * k)}"></path>')
    return "".join(o)

def wages_gift(w, h):
    """The wages of sin is death; but the free gift of God is eternal life: a plate — at the left the wages counted out, dark
    coins on a dark cloth, beside them an empty grave; at the right a gift in light."""
    o = [plate_bg(w, h, "ROMANS 6:23 · THE WAGES · THE FREE GIFT")]
    k = min(w / 700, h / 220); y = h * 0.66
    for i in range(5):
        for j in range(4 - i % 2):
            x = w * 0.14 + i * 24 * k
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y - j * 7 * k)}" rx="{f(11 * k)}" ry="{f(4 * k)}" fill="#4A4A54" stroke="{CY}" stroke-width="1.2"></ellipse>')
    o.append(f'<path d="M{f(w * 0.3)} {f(y)} L {f(w * 0.3)} {f(y - 50 * k)} C {f(w * 0.3)} {f(y - 72 * k)} {f(w * 0.38)} {f(y - 72 * k)} {f(w * 0.38)} {f(y - 50 * k)} L {f(w * 0.38)} {f(y)} Z" fill="#2A3040" stroke="{CY}" stroke-width="1.6"></path>')
    o.append(label(w * 0.24, y + 30 * k, "THE WAGES OF SIN · DEATH", "#C8C8E8", 10))
    gx = w * 0.74
    o.append(halo(gx, y - 30 * k, 90 * k, "#FFE680", 0.6) + rays(gx, y - 30 * k, 18, 40 * k, 100 * k, "#FFF4C2", 0.35, 3)
             + f'<rect x="{f(gx - 26 * k)}" y="{f(y - 46 * k)}" width="{f(52 * k)}" height="{f(40 * k)}" fill="#FFD23F" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(gx)} {f(y - 46 * k)} L {f(gx)} {f(y - 6 * k)} M{f(gx - 26 * k)} {f(y - 28 * k)} L {f(gx + 26 * k)} {f(y - 28 * k)}" stroke="#B5121B" stroke-width="{f(5 * k)}"></path>'
             + label(gx, y + 30 * k, "THE FREE GIFT OF GOD · ETERNAL LIFE", GOLD, 10))
    o.append(f'<path d="M{f(w * 0.5)} 34 L {f(w * 0.5)} {f(h - 8)}" stroke="#2C5A7A" stroke-width="1.4" stroke-dasharray="5 5"></path>')
    return "".join(o)

def bond(w, h):
    """The law hath dominion over a man for so long time as he liveth: a plate — the marriage bond, a scroll sealed with two
    seals, BOUND WHILE HE LIVETH; then the same bond with its seals loosed, DISCHARGED FROM THE LAW."""
    o = [plate_bg(w, h, "ROMANS 7:1–3 · THE BOND OF THE LAW")]
    k = min(w / 700, h / 220)
    for i, (x, t, loose) in enumerate(((w * 0.27, "BOUND · WHILE HE LIVETH", False), (w * 0.73, "DISCHARGED FROM THE LAW", True))):
        o.append(open_letter(x - 80 * k, h * 0.3, 160 * k, 90 * k, rows=5, seed=71 + i, color="#C8B888"))
        for dx in (-30, 30):
            sx, sy = x + dx * k, h * 0.3 + 90 * k
            if loose: sx += dx * 0.8 * k; sy += 18 * k
            o.append(f'<circle cx="{f(sx)}" cy="{f(sy)}" r="{f(10 * k)}" fill="#B5121B" stroke="{INK}" stroke-width="1.6"></circle>')
            if not loose: o.append(f'<path d="M{f(x)} {f(h * 0.3 + 90 * k)} L {f(sx)} {f(sy)}" stroke="#8A5A30" stroke-width="2"></path>')
        o.append(label(x, min(h - 12, h * 0.3 + 130 * k), t, GOLD if loose else CY, 10))
    o.append(route([(w * 0.44, h * 0.48), (w * 0.56, h * 0.48)], color=GOLD, sw=2.4, dash="7 5"))
    return "".join(o)

def sinai_tables(w, h, seed):
    """The commandment: mount Sinai in its cloud and fire, and before it the two tables of stone (Exodus' drawings)."""
    b = h * 0.96
    o = [sky(w, h, "#1A1430", "#6A4A5A"), V.rays(w * 0.5, h * 0.12, 30, 20, max(w, h), color="#FFF4C2", op=0.25),
         E4.sinai(w * 0.42, b, w * 0.9, h * 0.8, seed, fire=True)]
    o.append(V5.tables(w * 0.82, b - h * 0.2, min(0.5, h / 520), uid=f"st{seed}", glow=True))
    return "".join(o)

def shadow_man(p, w, h, seed, light=True):
    """The body of this death: a man standing in a bare room between the lamp and the wall, his own shadow long and dark on
    the wall behind him, his head bowed (no torment drawn); light=False the lamp low."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2E2E"></rect>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2020" stroke="{INK}" stroke-width="2"></rect>']
    lx = w * 0.16
    o.append(lamp_glow(lx, b - h * 0.2, max(w, h) * (0.5 if light else 0.3), f"{p}sm", op=0.55) + clay_lamp(lx, b - h * 0.2, min(1.2, h / 260)))
    o.append(f'<rect x="{f(lx - 20)}" y="{f(b - h * 0.2)}" width="40" height="{f(h * 0.2)}" fill="#4A3424" stroke="{INK}" stroke-width="1.6"></rect>')
    s = (h * 0.8) / 205
    mx = w * 0.42
    shadow_ = robed(p, mx + w * 0.22, b, s * 1.5, "#120C0C", skin="#120C0C", line="#120C0C", flip=True)
    o.append(f'<g opacity="0.7">{shadow_}</g>')
    o.append(robed(p, mx, b, s, "#5A4A3A", head="#4A3A2A", cord="#2A1A10", beard="#2A1A10", flip=True))
    return "".join(o)

def deliverance(w, h, seed):
    """I thank God through Jesus Christ our Lord: the dark room's door thrown open on the morning, a path of light across the
    floor (no one)."""
    b = h * 0.92
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2E2E"></rect>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2020" stroke="{INK}" stroke-width="2"></rect>']
    dx, dw = w * 0.56, w * 0.18
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.12)}" width="{f(dw)}" height="{f(b - h * 0.12)}" fill="#FFF4C2" stroke="{INK}" stroke-width="3"></rect>'
             + halo(dx + dw / 2, h * 0.5, max(w, h) * 0.4, "#FFFFFF", 0.6)
             + f'<path d="M{f(dx)} {f(b)} L {f(dx + dw)} {f(b)} L {f(dx + dw + w * 0.2)} {f(h + 10)} L {f(dx - w * 0.3)} {f(h + 10)} Z" fill="#FFE680" opacity="0.55"></path>'
             + f'<path d="M{f(dx)} {f(h * 0.12)} L {f(dx - dw * 0.5)} {f(h * 0.18)} L {f(dx - dw * 0.5)} {f(b + h * 0.04)} L {f(dx)} {f(b)} Z" fill="#5A3A1E" stroke="{INK}" stroke-width="2.4"></path>')
    return "".join(o)

def two_laws(w, h):
    """A different law in my members, warring against the law of my mind: a plate — a man's silhouette, his head lit gold
    (the law of God, the inward man, the mind), his members crossed by dark bands (the law of sin), the arrows meeting."""
    o = [plate_bg(w, h, "ROMANS 7:22–23 · THE LAW OF MY MIND · THE LAW OF SIN"), mk.defs("tl723", *ALL)]
    by = h - 14; s = (by - 50) / 205
    cx = w * 0.5
    o.append(halo(cx, by - 190 * s, 50 * s, "#FFE680", 0.7))
    o.append(mk.person("tl723", round(cx), round(by), round(s, 3), body="#1E4A6A", cloth="#163A56", kind="Tunic", stroke=CY, sw=2.4))
    for i in range(4):
        y = by - (40 + i * 26) * s
        o.append(f'<path d="M{f(cx - 34 * s)} {f(y)} L {f(cx + 34 * s)} {f(y - 10 * s)}" stroke="#FF6A4A" stroke-width="{f(3 * s)}" opacity="0.8"></path>')
    o.append(label(w * 0.2, h * 0.36, "THE LAW OF GOD", GOLD, 10) + label(w * 0.2, h * 0.36 + 14, "THE INWARD MAN · THE MIND", GOLD, 9))
    o.append(label(w * 0.8, h * 0.7, "A DIFFERENT LAW", "#FF6A4A", 10) + label(w * 0.8, h * 0.7 + 14, "IN MY MEMBERS · SIN", "#FF6A4A", 9))
    o.append(route([(w * 0.3, h * 0.4), (cx - 30 * s, by - 186 * s)], color=GOLD, sw=2) + route([(w * 0.7, h * 0.66), (cx + 30 * s, by - 80 * s)], color="#FF6A4A", sw=2))
    return "".join(o)
