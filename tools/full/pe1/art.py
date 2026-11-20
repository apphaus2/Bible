"""Drawings for the 1 Peter volume. 1 Peter starts from all of James' drawings (`from jas.art3 import *`, which carries
Galatians', Acts', Mark's and Matthew's drawings, the epistle kit and the writers' figures) and adds its own.

The people at a distance: Peter only ever jas.art.peter_fig (old: ntcast's brown robe, grey hair and beard), Silvanus
jas.art.silvanus_fig (Acts' Silas), Mark jas.art.mark_r; Jesus only ever ntcast.jesus_fig; Sarah and Abraham as Genesis
draws them (Sarah a mulberry robe and veil, grey-haired; Abraham grey, a white robe in old age). Angels are figures of white
light with a gold rim and no face; God, Satan and demons are never drawn. Every function takes (p, w, h, seed, ...) or
(w, h, ...); p, a prefix unique to the panel, names the figure defs and gradients."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from jas.art3 import *
from jas.art import art, plate_label, light_fig, _street, _road
from jas.common import SILVANUS_LOOK
from gal.art import far_crosses, dark_street
from ntcast import jesus_fig
from genesis.art2 import ark_afloat, dove
import exodus as E, exodus3 as E3

ROME = "ROME"

# ---- the study at Babylon (Rome) -----------------------------------------------------------------------------------------
def study_babylon(p, w, h, seed, stage="dictate", fig_h=None):
    """Peter writing by Silvanus at Babylon: a room at Rome by lamplight (epistle.study, window="rome"), Peter standing, his
    hand out, Silvanus on his mat writing, Mark standing at the right listening; stage "give": Peter handing the sealed
    letter to Silvanus in the doorway onto the night street, Mark beside him."""
    if stage == "give":
        return study(p, w, h, seed, stage="give", scribe=False, bearer=silvanus_fig, writer=peter_fig, window="rome", fig_h=fig_h, others=(mark_r,))
    return study(p, w, h, seed, stage=stage, scribe=SILVANUS_LOOK, writer=peter_fig, window="rome", fig_h=fig_h, others=(mark_r,))

# ---- 1 Peter 1 ------------------------------------------------------------------------------------------------------------
def five_provinces(w, h):
    """To the elect who are sojourners of the Dispersion in Pontus, Galatia, Cappadocia, Asia, and Bithynia: the letter's
    road from Babylon (Rome) by sea and over the land into the five provinces of Asia Minor, on Acts' map."""
    rt = ["ROME", (14.1, 40.8), (15.6, 38.1), (19.5, 37.0), (23.0, 36.6), (26.2, 37.8), "EPHESUS", (30.0, 38.6), (32.6, 39.6), (35.5, 40.6)]
    return geo.med_map(w, h, box=(11.0, 42.0, 34.0, 44.0), places=("ROME", "EPHESUS", "CORINTH", "TROAS", "TARSUS", "ANTIOCH OF PISIDIA"),
                       routes=[rt], hi=("ROME",), regions=("PONTUS", "GALATIA", "CAPPADOCIA", "ASIA", "BITHYNIA", "ITALY", "MACEDONIA", "ACHAIA"),
                       title="1 PETER 1:1 · FROM BABYLON TO PONTUS, GALATIA, CAPPADOCIA, ASIA, AND BITHYNIA", red=True)

def crucible(w, h, seed):
    """Gold that perisheth though it is proved by fire: the goldsmith's furnace, the crucible glowing in the coals, the
    molten gold poured out bright into the mould, the dross skimmed off black at the side."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1E120E"></rect>', halo(w * 0.36, h * 0.6, h * 0.8, "#FF6A2A", 0.5),
         f'<rect x="-10" y="{f(h * 0.82)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#3A2A22" stroke="{INK}" stroke-width="2"></rect>']
    k = h / 300
    fx, fb = w * 0.3, h * 0.84                                       # the furnace of clay bricks, the coals
    o.append(f'<path d="M{f(fx - 110 * k)} {f(fb)} L {f(fx - 96 * k)} {f(fb - 110 * k)} L {f(fx + 96 * k)} {f(fb - 110 * k)} L {f(fx + 110 * k)} {f(fb)} Z" fill="#6A3A2A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(fx - 70 * k)} {f(fb)} L {f(fx - 70 * k)} {f(fb - 50 * k)} C {f(fx - 70 * k)} {f(fb - 80 * k)} {f(fx + 70 * k)} {f(fb - 80 * k)} {f(fx + 70 * k)} {f(fb - 50 * k)} L {f(fx + 70 * k)} {f(fb)} Z" fill="#FF8A2A" stroke="{INK}" stroke-width="2"></path>')
    for i in range(14):
        o.append(f'<circle cx="{f(fx + r.uniform(-60, 60) * k)}" cy="{f(fb - r.uniform(4, 40) * k)}" r="{f(r.uniform(5, 10) * k)}" fill="{r.choice(("#FFD23F", "#FF6A2A", "#D7261E"))}" stroke="{INK}" stroke-width="1"></circle>')
    cx, cy = w * 0.5, fb - 150 * k                                  # the crucible tipped, held in tongs, the gold pouring
    o.append(f'<g transform="rotate(38 {f(cx)} {f(cy)})"><path d="M{f(cx - 34 * k)} {f(cy - 34 * k)} L {f(cx + 34 * k)} {f(cy - 34 * k)} L {f(cx + 22 * k)} {f(cy + 30 * k)} L {f(cx - 22 * k)} {f(cy + 30 * k)} Z" fill="#8A4A2A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy - 34 * k)}" rx="{f(34 * k)}" ry="{f(8 * k)}" fill="#FFD23F" stroke="{INK}" stroke-width="2"></ellipse></g>'
             f'<path d="M{f(cx - 70 * k)} {f(cy - 60 * k)} L {f(cx - 10 * k)} {f(cy - 10 * k)} M{f(cx - 70 * k)} {f(cy - 50 * k)} L {f(cx - 6 * k)} {f(cy)}" stroke="#4A4A54" stroke-width="{f(5 * k)}" stroke-linecap="round"></path>')
    mx, my = w * 0.66, fb - 10 * k                                   # the stream of gold into the mould
    o.append(f'<path d="M{f(cx + 30 * k)} {f(cy - 30 * k)} C {f(cx + 60 * k)} {f(cy - 20 * k)} {f(mx - 10 * k)} {f(cy + 40 * k)} {f(mx)} {f(my - 24 * k)}" stroke="#FFD23F" stroke-width="{f(7 * k)}" fill="none" stroke-linecap="round"></path>'
             + halo(mx, my - 20 * k, 60 * k, "#FFE680", 0.7)
             + f'<rect x="{f(mx - 60 * k)}" y="{f(my - 22 * k)}" width="{f(120 * k)}" height="{f(22 * k)}" fill="#5A5A5A" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(mx - 50 * k)}" y="{f(my - 20 * k)}" width="{f(100 * k)}" height="{f(10 * k)}" fill="#FFD23F"></rect>')
    o.append(f'<path d="M{f(w * 0.84)} {f(fb)} C {f(w * 0.82)} {f(fb - 20 * k)} {f(w * 0.9)} {f(fb - 26 * k)} {f(w * 0.92)} {f(fb)} Z" fill="#1A1210" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(tag(mx, my - 14 * k, "GOLD PROVED BY FIRE", w * 0.7, h * 0.18, color=GOLD, size=9) + tag(w * 0.87, fb - 12 * k, "DROSS", w * 0.84, h * 0.5, color="#C8B8A8", size=9))
    return "".join(o)

def prophets_search(p, w, h, seed):
    """The prophets sought and searched diligently … which things angels desire to look into: a prophet of old in his
    chamber by lamplight, bent over the scroll, more rolls heaped beside him; behind him two figures of white light with a
    gold rim and no face, bending to look into it."""
    b = h * 0.94
    o = [D_(p), room(w, h, b, wall="#3A2A2A", floor="#2A1E1A"), lamp_glow(w * 0.42, h * 0.5, h * 0.7, f"{p}ps", op=0.5)]
    s = fit(b, max(h * 0.16, b - 225))
    o.append(low_table(w * 0.3, b, 150 * s, s) + clay_lamp(w * 0.3 + 120 * s, b - 31 * s, s * 0.7))
    o.append(f'<g transform="translate({f(w * 0.3 + 55 * s)} {f(b - 34 * s)})">' + open_letter(-45 * s, -16 * s, 90 * s, 20 * s, rows=3, seed=seed) + '</g>')
    for i in range(4):
        o.append(sealed_scroll(w * 0.12 + i * 22 * s, b - 10 * s - (i % 2) * 14 * s, 0.32 * s, rot=-10 + i * 6))
    o.append(robed(p, w * 0.24, b, s, "#4A3A5A", head="#E8E2D6", cord="#6A5A3A", beard="#C8C2B6", mantle="#2A2A3A", flip=True, pose="sit", seat="stool",
                   up=[(-22, -158), (-44, -132), (-62, -118)]))
    for i, x in enumerate((0.64, 0.8)):
        ss = s * (0.96 - i * 0.04)
        o.append(angel_r(p, w * x, b, ss, flip=False, up=[(-22, -158), (-44, -140), (-62, -128)]))
    o.append(plate_label(w * 0.28, h * 0.1, "THE PROPHETS SOUGHT AND SEARCHED", "#FFE6A0", 9, halo_="#2A1A1A")
             + plate_label(w * 0.72, h * 0.1, "ANGELS DESIRE TO LOOK INTO", "#FFF4C2", 9, halo_="#2A1A1A"))
    return "".join(o)

def lamb_emblem(w, h, seed):
    """Redeemed, not with corruptible things, with silver or gold, … but with precious blood, as of a lamb without blemish
    and without spot: an emblem on a plate — the silver and the gold set aside at the left, struck through; at the centre a
    white lamb standing in a ring of light, without blemish (no slaughter, no blood drawn)."""
    o = [plate_bg(w, h, "1 PETER 1:18–19 · A LAMB WITHOUT BLEMISH AND WITHOUT SPOT")]
    k = min(w / 702, h / 300)
    cx, cy = w * 0.56, h * 0.74
    o.append(halo(cx, cy - 50 * k, 150 * k, "#FFF4C2", 0.45) + f'<circle cx="{f(cx)}" cy="{f(cy - 50 * k)}" r="{f(110 * k)}" fill="none" stroke="{GOLD}" stroke-width="2"></circle>')
    o.append(E3.lamb(cx - 10 * k, cy + 10 * k, 1.5 * k).replace("#F3EFE6", "#FFFFFF"))
    sx = w * 0.16                                                    # silver and gold, set aside
    for i in range(5):
        o.append(f'<ellipse cx="{f(sx + (i % 3) * 22 * k)}" cy="{f(cy - (i // 3) * 12 * k)}" rx="{f(14 * k)}" ry="{f(6 * k)}" fill="{"#E8B830" if i % 2 else "#C8C8D0"}" stroke="{INK}" stroke-width="1.4"></ellipse>')
    o.append(f'<path d="M{f(sx - 30 * k)} {f(cy - 50 * k)} L {f(sx + 80 * k)} {f(cy + 20 * k)} M{f(sx + 80 * k)} {f(cy - 50 * k)} L {f(sx - 30 * k)} {f(cy + 20 * k)}" stroke="#FF6A4A" stroke-width="3"></path>')
    o.append(label(sx + 25 * k, cy + 44 * k, "NOT WITH SILVER OR GOLD", "#FF8A6A", 9) + label(cx, cy + 44 * k, "PRECIOUS · WITHOUT SPOT", GOLD, 9)
             + label(w * 0.86, h * 0.36, "FOREKNOWN", CY, 9) + label(w * 0.86, h * 0.36 + 16, "BEFORE THE FOUNDATION", CY, 8) + label(w * 0.86, h * 0.36 + 30, "OF THE WORLD", CY, 8))
    return "".join(o)

def grass_word(w, h, seed):
    """All flesh is as grass … The grass withereth, and the flower falleth: But the word of the Lord abideth for ever: the
    field of grass and wild flowers withering under the scorching sun (as James), and on a stone in the foreground an open
    scroll, untouched, lit gold."""
    o = [withering(w, h, seed)]
    k = h / 300
    x, y = w * 0.36, h * 0.86
    o.append(f'<path d="M{f(x - 80 * k)} {f(h + 10)} L {f(x - 70 * k)} {f(y - 10 * k)} L {f(x + 80 * k)} {f(y - 16 * k)} L {f(x + 90 * k)} {f(h + 10)} Z" fill="#8A8278" stroke="{INK}" stroke-width="2.4"></path>'
             + halo(x, y - 30 * k, 90 * k, "#FFF4C2", 0.7)
             + f'<ellipse cx="{f(x - 56 * k)}" cy="{f(y - 30 * k)}" rx="{f(8 * k)}" ry="{f(16 * k)}" fill="#D8C49A" stroke="{INK}" stroke-width="1.6"></ellipse>'
             + open_letter(x - 54 * k, y - 46 * k, 108 * k, 32 * k, rows=4, seed=seed)
             + f'<ellipse cx="{f(x + 56 * k)}" cy="{f(y - 30 * k)}" rx="{f(8 * k)}" ry="{f(16 * k)}" fill="#D8C49A" stroke="{INK}" stroke-width="1.6"></ellipse>')
    o.append(plate_label(x, y - 64 * k, "THE WORD OF THE LORD ABIDETH", "#5A3A0A", 9, halo_="#FFF4C2"))
    return "".join(o)

# ---- 1 Peter 2 ------------------------------------------------------------------------------------------------------------
def mother_babe(p, w, h, seed):
    """As newborn babes, long for the spiritual milk which is without guile: a mother sitting by the lamp in a house at
    evening, her newborn wrapped and held in her arms, a jar of milk and a cup on the low table beside her."""
    b = h * 0.94
    o = [D_(p), room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * 0.5, h * 0.5, h * 0.7, f"{p}mb", op=0.5)]
    s = fit(b, max(h * 0.16, b - 225))
    babe = ('<path d="M-56 -128 C -60 -142 -40 -150 -22 -144 C -8 -140 -2 -128 -10 -120 C -24 -112 -50 -114 -56 -128 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.8"></path>'
            '<circle cx="-50" cy="-134" r="7" fill="#C98E66" stroke="#0D0D0F" stroke-width="1.4"></circle>'
            '<path d="M-48 -124 C -36 -126 -22 -130 -14 -136" stroke="#C8C0B0" stroke-width="1.4" fill="none"></path>')
    o.append(robed(p, w * 0.42, b, s * 0.98, "#4A6A8A", woman=True, veil="#2A3A5A", flip=False, pose="sit", seat="stool",
                   up=[(-22, -158), (-40, -130), (-30, -124)], extra=babe))
    o.append(low_table(w * 0.56, b, 80 * s, s) + clay_lamp(w * 0.56 + 60 * s, b - 31 * s, s * 0.6)
             + f'<path d="M{f(w * 0.56 + 14 * s)} {f(b - 30 * s)} C {f(w * 0.56 + 6 * s)} {f(b - 50 * s)} {f(w * 0.56 + 12 * s)} {f(b - 64 * s)} {f(w * 0.56 + 20 * s)} {f(b - 68 * s)} '
               f'L {f(w * 0.56 + 32 * s)} {f(b - 68 * s)} C {f(w * 0.56 + 40 * s)} {f(b - 64 * s)} {f(w * 0.56 + 46 * s)} {f(b - 50 * s)} {f(w * 0.56 + 38 * s)} {f(b - 30 * s)} Z" fill="#E8DCC0" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(plate_label(w * 0.5, h * 0.1, "AS NEWBORN BABES", "#FFE6A0", 10, halo_="#2A1A12"))
    return "".join(o)

def stone_block(x, y, wd, ht, color="#B8A890", lit=False):
    return (f'<rect x="{f(x)}" y="{f(y - ht)}" width="{f(wd)}" height="{f(ht)}" fill="{color}" stroke="{INK}" stroke-width="2"></rect>'
            f'<path d="M{f(x + 3)} {f(y - ht + 4)} L {f(x + wd - 3)} {f(y - ht + 4)}" stroke="#E8DCC8" stroke-width="1.6" opacity="0.7"></path>'
            + (f'<rect x="{f(x)}" y="{f(y - ht)}" width="{f(wd)}" height="{f(ht)}" fill="#FFE680" opacity="0.35"></rect>' if lit else ""))

def living_stones(p, w, h, seed):
    """Ye also, as living stones, are built up a spiritual house: a house of hewn stones going up on a hill at morning, the
    courses laid on the great corner stone (lit), the builders at work — one setting a stone in its place, one carrying a
    stone up — and the scaffold of poles."""
    b = h * 0.92
    o = [D_(p), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.6, seed, color="#9AA07A", amp=10, step=90), ground(w, h, b, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.2, b - 210))
    x0, bw, bh = w * 0.42, 60 * s, 32 * s                            # the wall: courses of stones, the corner stone at the left foot
    rows_ = 5
    for rr in range(rows_):
        n = 6 - (1 if rr == rows_ - 1 else 0)
        for c in range(n):
            xx = x0 + c * bw + (bw / 2 if rr % 2 else 0)
            if xx + bw > w * 0.98: continue
            o.append(stone_block(xx, b - rr * bh, bw, bh, color=["#B8A890", "#C8B8A0", "#A89880"][(c + rr) % 3]))
    o.append(stone_block(x0 - bw * 0.2, b, bw * 1.2, bh * 1.3, color="#D8C8A8", lit=True) + halo(x0 + bw * 0.4, b - bh * 0.6, 60 * s, "#FFE680", 0.5))
    for xx in (x0 - 10 * s, w * 0.96):
        o.append(f'<path d="M{f(xx)} {f(b)} L {f(xx)} {f(b - 230 * s)}" stroke="#7A5A3A" stroke-width="{f(5 * s)}"></path>')
    o.append(f'<path d="M{f(x0 - 14 * s)} {f(b - rows_ * bh - 6)} L {f(w * 0.97)} {f(b - rows_ * bh - 6)}" stroke="#7A5A3A" stroke-width="{f(4 * s)}"></path>')
    stone = '<rect x="-96" y="-180" width="40" height="24" fill="#C8B8A0" stroke="#0D0D0F" stroke-width="2"></rect>'
    o.append(man_r(p, w * 0.24, b, s, 2, flip=True, up=[(-22, -158), (-50, -168), (-72, -176)], extra=stone.replace("-96", "-92")))
    o.append(man_r(p, w * 0.1, b, s * 0.97, 0, flip=True, up=[(-22, -158), (-40, -176), (-50, -186)], extra='<rect x="-72" y="-206" width="38" height="22" fill="#B8A890" stroke="#0D0D0F" stroke-width="2"></rect>'))
    o.append(tag(x0 + bw * 0.3, b - bh * 0.6, "THE CHIEF CORNER STONE", w * 0.28, h * 0.12, color="#7A3A0A", size=9).replace(f'fill="#7A3A0A"', 'fill="#7A3A0A"'))
    return "".join(o)

def corner_plate(w, h):
    """The chief corner stone, the stone which the builders rejected, the stone of stumbling: a masonry plate — at the left
    the corner of a house, the corner stone at its foot binding the two walls (head of the corner); at the right the same
    stone lying in the road, a foot stumbling on it."""
    o = [plate_bg(w, h, "1 PETER 2:6–8 · THE HEAD OF THE CORNER · A STONE OF STUMBLING")]
    k = min(w / 702, h / 330)
    cx, b = w * 0.3, h * 0.78
    for rr in range(6):                                              # two walls meeting at a corner, drawn in isometric
        for c in range(4):
            x = cx - (c + 1) * 34 * k + (rr % 2) * 10 * k; y = b - rr * 24 * k + (c + 1) * 10 * k
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x + 34 * k)} {f(y - 10 * k)} L {f(x + 34 * k)} {f(y - 34 * k)} L {f(x)} {f(y - 24 * k)} Z" fill="#2A4A6A" stroke="{CY}" stroke-width="1.2"></path>')
            x2 = cx + c * 34 * k - (rr % 2) * 10 * k; y2 = b - rr * 24 * k + c * 10 * k
            o.append(f'<path d="M{f(x2)} {f(y2)} L {f(x2 + 34 * k)} {f(y2 + 10 * k)} L {f(x2 + 34 * k)} {f(y2 - 14 * k)} L {f(x2)} {f(y2 - 24 * k)} Z" fill="#1F3A5A" stroke="{CY}" stroke-width="1.2"></path>')
    o.append(f'<path d="M{f(cx - 40 * k)} {f(b + 14 * k)} L {f(cx)} {f(b + 2 * k)} L {f(cx + 40 * k)} {f(b + 14 * k)} L {f(cx + 40 * k)} {f(b + 40 * k)} L {f(cx)} {f(b + 52 * k)} L {f(cx - 40 * k)} {f(b + 40 * k)} Z" fill="#E8B830" stroke="{INK}" stroke-width="2"></path>'
             + halo(cx, b + 26 * k, 50 * k, "#FFE680", 0.5))
    o.append(tag(cx + 20 * k, b + 30 * k, "THE HEAD OF THE CORNER", w * 0.47, h * 0.62, color=GOLD, size=9))
    o.append(tag(cx - 20 * k, b + 34 * k, "ELECT · PRECIOUS", w * 0.16, h * 0.3, color=GOLD, size=9))
    sx, sy = w * 0.78, h * 0.86                                      # the stone in the road, a foot striking it
    o.append(f'<path d="M{f(w * 0.56)} {f(sy + 10)} L {f(w - 10)} {f(sy + 10)}" stroke="{CY}" stroke-width="1.4" stroke-dasharray="6 4"></path>'
             f'<path d="M{f(sx - 30 * k)} {f(sy + 10)} L {f(sx - 22 * k)} {f(sy - 16 * k)} L {f(sx + 26 * k)} {f(sy - 20 * k)} L {f(sx + 32 * k)} {f(sy + 10)} Z" fill="#E8B830" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(sx - 90 * k)} {f(sy - 10 * k)} C {f(sx - 70 * k)} {f(sy - 6 * k)} {f(sx - 50 * k)} {f(sy - 8 * k)} {f(sx - 30 * k)} {f(sy - 14 * k)} L {f(sx - 34 * k)} {f(sy - 26 * k)} '
             f'C {f(sx - 56 * k)} {f(sy - 26 * k)} {f(sx - 80 * k)} {f(sy - 34 * k)} {f(sx - 92 * k)} {f(sy - 48 * k)} Z" fill="{SKIN}" stroke="{INK}" stroke-width="1.6"></path>'
             f'<path d="M{f(sx - 34 * k)} {f(sy - 30 * k)} l 10 -12 M{f(sx - 26 * k)} {f(sy - 24 * k)} l 14 -6" stroke="#FF6A4A" stroke-width="2"></path>')
    o.append(label(sx, h * 0.24, "REJECTED OF THE BUILDERS", "#FF8A6A", 9) + label(sx, h * 0.24 + 16, "A STONE OF STUMBLING", "#FF8A6A", 9)
             + label(sx, h * 0.24 + 32, "A ROCK OF OFFENCE", "#FF8A6A", 9))
    return "".join(o)

def into_light(p, w, h, seed):
    """Him who called you out of darkness into his marvellous light: a dark valley at the left, a company of men and women
    walking up out of it toward the right into a great light rising over the hill (no figure in the light)."""
    b = h * 0.92
    o = [D_(p), f'<defs><linearGradient id="{p}il" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#05050E"></stop><stop offset="0.45" stop-color="#2A2A5A"></stop>'
         f'<stop offset="0.75" stop-color="#FFC890"></stop><stop offset="1" stop-color="#FFF8E0"></stop></linearGradient></defs><rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{p}il)"></rect>',
         halo(w * 0.94, h * 0.5, h * 0.8, "#FFFFFF", 0.7), rays(w * 0.94, h * 0.5, 30, h * 0.1, w, "#FFF4C2", 0.3, 4),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.9)} {f(w * 0.6)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} Z" fill="#3A3448" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.24, b - 190))
    people = [(0.14, "m", 3), (0.26, "w", 1), (0.38, "m", 0), (0.5, "w", 0), (0.62, "m", 2)]
    for i, (x, kind, c) in enumerate(people):
        yy = b - (x - 0.1) * h * 0.3
        ss = s * (0.86 + x * 0.2)
        o.append((woman_r if kind == "w" else man_r)(p, w * x, yy, ss, c, flip=True, pose="walk"))
    o.append(plate_label(w * 0.3, h * 0.1, "OUT OF DARKNESS", "#C8C8E8", 10, halo_="#05050E") + plate_label(w * 0.74, h * 0.1, "INTO HIS MARVELLOUS LIGHT", "#5A3A0A", 10, halo_="#FFE6C0"))
    return "".join(o)

def pilgrims(p, w, h, seed):
    """I beseech you as sojourners and pilgrims: a long road over the hills at evening, a family of travellers walking it
    with their staves and their bundles, a city of the Gentiles behind them and the road going on far ahead."""
    bg, b = _road(w, h, seed, "dusk")
    s = fit(b, max(h * 0.2, b - 210))
    o = [D_(p), bg, walls(w * 0.02, w * 0.26, h * 0.5, h * 0.12, seed, lit=True, towers=2)]
    staff = '<path d="M-52 -176 L -46 4" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"></path>'
    bundle = '<path d="M10 -170 C 30 -176 40 -150 30 -130 L 8 -136 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(man_r(p, w * 0.62, b, s, 0, flip=True, pose="walk", up=[(-22, -158), (-38, -124), (-48, -96)], extra=staff + bundle))
    o.append(woman_r(p, w * 0.48, b, s, 2, flip=True, pose="walk"))
    o.append(robed(p, w * 0.38, b, s * 0.6, "#8A7A5A", hair="#2A1A10", belt="#5A4A2A", flip=True, pose="walk"))
    o.append(plate_label(w * 0.6, h * 0.1, "SOJOURNERS AND PILGRIMS", "#FFE6C0", 10, halo_="#2A1A3A"))
    return "".join(o)

def four_honors(w, h):
    """Honor all men. Love the brotherhood. Fear God. Honor the king.: a plate of four cells — a crowd of all men; two
    brothers' hands clasped; a light falling from above on bowed heads (God is not drawn); a Roman coin with the emperor's
    head and the laurel."""
    o = [plate_bg(w, h, "1 PETER 2:17")]
    cw = w / 4; k = min(cw / 175, h / 300); base = h * 0.78
    names = ("HONOR ALL MEN", "LOVE THE BROTHERHOOD", "FEAR GOD", "HONOR THE KING")
    for i, name in enumerate(names):
        x0 = cw * i; cx = x0 + cw / 2
        o.append(f'<rect x="{f(x0 + 8)}" y="{f(h * 0.14)}" width="{f(cw - 16)}" height="{f(h * 0.72)}" fill="#0F2238" stroke="{CY}" stroke-width="1.2"></rect>')
        if i == 0:
            for j in range(7):
                xx = cx + (j - 3) * 18 * k; yy = base - (j % 2) * 8 * k
                o.append(f'<circle cx="{f(xx)}" cy="{f(yy - 70 * k)}" r="{f(9 * k)}" fill="#C98E66" stroke="{INK}" stroke-width="1.4"></circle>'
                         f'<path d="M{f(xx - 13 * k)} {f(yy)} L {f(xx - 10 * k)} {f(yy - 56 * k)} C {f(xx - 6 * k)} {f(yy - 62 * k)} {f(xx + 6 * k)} {f(yy - 62 * k)} {f(xx + 10 * k)} {f(yy - 56 * k)} L {f(xx + 13 * k)} {f(yy)} Z" '
                         f'fill="{["#5A6A8A", "#8A5A3A", "#6A7A5A", "#7A4A6A", "#4A5A5A", "#8A7A5A", "#5A4A6A"][j]}" stroke="{INK}" stroke-width="1.4"></path>')
        elif i == 1:
            o.append(f'<path d="M{f(cx - 70 * k)} {f(base - 40 * k)} C {f(cx - 40 * k)} {f(base - 46 * k)} {f(cx - 20 * k)} {f(base - 56 * k)} {f(cx - 4 * k)} {f(base - 60 * k)} L {f(cx + 4 * k)} {f(base - 46 * k)} '
                     f'C {f(cx - 20 * k)} {f(base - 40 * k)} {f(cx - 40 * k)} {f(base - 30 * k)} {f(cx - 70 * k)} {f(base - 26 * k)} Z" fill="#6A5A4A" stroke="{INK}" stroke-width="1.6"></path>'
                     f'<path d="M{f(cx + 70 * k)} {f(base - 40 * k)} C {f(cx + 40 * k)} {f(base - 46 * k)} {f(cx + 20 * k)} {f(base - 56 * k)} {f(cx + 4 * k)} {f(base - 60 * k)} L {f(cx - 4 * k)} {f(base - 46 * k)} '
                     f'C {f(cx + 20 * k)} {f(base - 40 * k)} {f(cx + 40 * k)} {f(base - 30 * k)} {f(cx + 70 * k)} {f(base - 26 * k)} Z" fill="#4A5A6A" stroke="{INK}" stroke-width="1.6"></path>'
                     f'<ellipse cx="{f(cx)}" cy="{f(base - 54 * k)}" rx="{f(14 * k)}" ry="{f(11 * k)}" fill="{SKIN}" stroke="{INK}" stroke-width="1.6"></ellipse>'
                     f'<path d="M{f(cx - 8 * k)} {f(base - 60 * k)} l 4 10 M{f(cx)} {f(base - 62 * k)} l 2 12 M{f(cx + 8 * k)} {f(base - 60 * k)} l 0 10" stroke="{INK}" stroke-width="1.2"></path>')
        elif i == 2:
            o.append(f'<path d="M{f(cx - 10 * k)} {f(h * 0.14)} L {f(cx + 10 * k)} {f(h * 0.14)} L {f(cx + 50 * k)} {f(base)} L {f(cx - 50 * k)} {f(base)} Z" fill="#FFF4C2" opacity="0.45"></path>'
                     + halo(cx, h * 0.16, 40 * k, "#FFFFFF", 0.8))
            for j in range(3):
                xx = cx + (j - 1) * 30 * k
                o.append(f'<path d="M{f(xx - 14 * k)} {f(base)} C {f(xx - 16 * k)} {f(base - 30 * k)} {f(xx - 8 * k)} {f(base - 46 * k)} {f(xx + 6 * k)} {f(base - 48 * k)} C {f(xx + 14 * k)} {f(base - 40 * k)} {f(xx + 16 * k)} {f(base - 20 * k)} {f(xx + 14 * k)} {f(base)} Z" fill="#4A4A5A" stroke="{INK}" stroke-width="1.4"></path>'
                         f'<circle cx="{f(xx + 8 * k)}" cy="{f(base - 50 * k)}" r="{f(8 * k)}" fill="#C98E66" stroke="{INK}" stroke-width="1.4"></circle>')
        else:
            R = 54 * k; cy = base - 60 * k
            o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R)}" fill="#C8A040" stroke="{INK}" stroke-width="2.4"></circle><circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R * 0.86)}" fill="none" stroke="#8A6A1A" stroke-width="1.6"></circle>'
                     f'<path d="M{f(cx - 22 * k)} {f(cy + 30 * k)} C {f(cx - 26 * k)} {f(cy)} {f(cx - 20 * k)} {f(cy - 28 * k)} {f(cx + 2 * k)} {f(cy - 32 * k)} C {f(cx + 14 * k)} {f(cy - 32 * k)} {f(cx + 18 * k)} {f(cy - 20 * k)} {f(cx + 16 * k)} {f(cy - 12 * k)} '
                     f'L {f(cx + 24 * k)} {f(cy - 2 * k)} L {f(cx + 16 * k)} {f(cy + 2 * k)} C {f(cx + 16 * k)} {f(cy + 14 * k)} {f(cx + 8 * k)} {f(cy + 18 * k)} {f(cx + 2 * k)} {f(cy + 18 * k)} L {f(cx + 4 * k)} {f(cy + 30 * k)} Z" fill="#A8801A" stroke="#5A4010" stroke-width="1.6"></path>'
                     + "".join(f'<ellipse cx="{f(cx - 14 * k + j * 6 * k)}" cy="{f(cy - 30 * k + j * 1.5 * k)}" rx="{f(4 * k)}" ry="{f(2 * k)}" fill="#5E8F26" transform="rotate({-30 + j * 10} {f(cx - 14 * k + j * 6 * k)} {f(cy - 30 * k)})"></ellipse>' for j in range(5)))
        o.append(label(cx, h * 0.82, name, GOLD, 8))
    return "".join(o)

def shepherd_return(p, w, h, seed):
    """Ye were going astray like sheep; but are now returned unto the Shepherd and Bishop of your souls: a green hillside at
    evening, Jesus (ntcast's look) standing with his staff, the sheep that had strayed coming back over the hill to him."""
    b = h * 0.92
    o = [D_(p), sky(w, h, "#5A6A9A", "#FFD8A0"), hills(w, h, h * 0.5, seed, color="#6A8A5A", amp=14, step=90),
         f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.56)} {f(w * 0.7)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.54)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7A9A5A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.2, b - 210))
    o.append(jesus_fig(p, round(w * 0.3), round(b), round(s, 3), flip=True, up=[(-22, -158), (-46, -140), (-62, -150)]))
    o.append(f'<path d="M{f(w * 0.3 - 64 * s)} {f(b - 220 * s)} C {f(w * 0.3 - 76 * s)} {f(b - 236 * s)} {f(w * 0.3 - 92 * s)} {f(b - 226 * s)} {f(w * 0.3 - 86 * s)} {f(b - 210 * s)} L {f(w * 0.3 - 60 * s)} {f(b)}" stroke="#5A3A22" stroke-width="{f(4 * s)}" fill="none" stroke-linecap="round"></path>')
    r = random.Random(seed)
    for i in range(7):
        x = w * (0.44 + i * 0.075) + r.uniform(-10, 10); y = b - r.uniform(0, h * 0.22) - i * h * 0.01
        o.append(E.sheep(x, y, s * r.uniform(0.5, 0.62) * (1 - i * 0.04), flip=False))
    o.append(plate_label(w * 0.66, h * 0.1, "RETURNED UNTO THE SHEPHERD AND BISHOP OF YOUR SOULS", "#2A1A3A", 9, halo_="#FFE8C8"))
    return "".join(o)
