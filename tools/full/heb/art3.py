"""Drawings for the Hebrews volume, chapter 3 (Hebrews 9–10): the first tabernacle and its furniture as Exodus' blueprints
draw them (exo.art8), the ark and what was in it, the high priest alone before the veil once in the year, the greater
tabernacle not made with hands, heaven itself, the testament, the altar and the twelve pillars under Sinai, the shadow and
the very image, the roll of the book, the priest standing day by day, the veil rent, the church assembled, the fire of
judgment on a dark field.

Restraint: no blood is drawn anywhere — the high priest goes in with the censer and the golden bowl; Moses' sprinkling
(9:19–21) is the altar and the twelve pillars under the mount with the book, the hyssop and the scarlet wool laid by;
the death of the testator (9:16–17) is words; the crucifixion (10:10) the three crosses far off; judgment (10:26–31) words
over fire on an empty dark field and over a storm."""
from heb.art import *
from heb.art import art, plate_label, _defs, f, INK, defs_up, face_cell, cloud_bank, throne_of_light, angel_fig, GOLD, CY, CREAM, brother_fig
from heb.art2 import high_priest, priest_white, altar_fire, censer, tent_plan
from co1.art5 import cells, risen_fig
import mk

# ---- Hebrews 9 ------------------------------------------------------------------------------------------------------------
def candlestick(cx, b, k, lit=True):
    """The candlestick of beaten gold: the base, the shaft, six branches, cups like almond-blossoms, seven lamps; (cx, b) the
    middle of its foot, about 190 units tall at k = 1."""
    o = [f'<path d="M{f(cx - 34 * k)} {f(b)} L {f(cx - 12 * k)} {f(b - 22 * k)} L {f(cx + 12 * k)} {f(b - 22 * k)} L {f(cx + 34 * k)} {f(b)} Z" fill="#E8B830" stroke="{INK}" stroke-width="1.8"></path>',
         f'<path d="M{f(cx)} {f(b - 22 * k)} L {f(cx)} {f(b - 180 * k)}" stroke="#E8B830" stroke-width="{f(8 * k)}"></path>']
    for d in (1, 2, 3):
        for sg in (-1, 1):
            r = d * 22 * k
            o.append(f'<path d="M{f(cx)} {f(b - 180 * k + r + 10 * k)} C {f(cx + sg * r * 0.2)} {f(b - 180 * k + r + 30 * k)} {f(cx + sg * r)} {f(b - 180 * k + r + 20 * k)} {f(cx + sg * r)} {f(b - 180 * k)}" fill="none" stroke="#E8B830" stroke-width="{f(5 * k)}"></path>')
    for d in (-3, -2, -1, 0, 1, 2, 3):
        x = cx + d * 22 * k
        o.append(f'<path d="M{f(x - 8 * k)} {f(b - 180 * k)} L {f(x + 8 * k)} {f(b - 180 * k)} L {f(x + 5 * k)} {f(b - 172 * k)} L {f(x - 5 * k)} {f(b - 172 * k)} Z" fill="#FFD23F" stroke="{INK}" stroke-width="1.2"></path>')
        if lit:
            o.append(f'<path d="M{f(x)} {f(b - 182 * k)} c {f(-4 * k)} {f(-8 * k)} 0 {f(-16 * k)} 0 {f(-18 * k)} c {f(3 * k)} {f(6 * k)} {f(6 * k)} {f(11 * k)} 0 {f(18 * k)} Z" fill="#FFE680"></path>'
                     + halo(x, b - 192 * k, 12 * k, "#FFE680", 0.5))
    return "".join(o)

def holy_place(w, h):
    """A tabernacle prepared, the first, wherein were the candlestick, and the table, and the showbread; which is called the
    Holy place: a technical plate — the candlestick of beaten gold with its seven lamps lit at the left; the table overlaid
    with gold at the right, the twelve loaves of the showbread on it in two rows, a bowl beside it."""
    o = [plate_bg(w, h, "HEBREWS 9:2 · THE HOLY PLACE")]
    k = min(w / 700, (h - 40) / 220)
    b = h - 30
    o.append(candlestick(w * 0.26, b, k))
    o.append(tag(w * 0.26 + 66 * k, b - 150 * k, "THE CANDLESTICK · SEVEN LAMPS", w * 0.26 + 110 * k, b - 196 * k, GOLD, 9))
    tx, tw, ty = w * 0.68, 220 * k, b - 90 * k
    o.append(f'<rect x="{f(tx - tw / 2)}" y="{f(ty)}" width="{f(tw)}" height="{f(12 * k)}" fill="#FFD23F" stroke="{INK}" stroke-width="1.8"></rect>'
             + "".join(f'<path d="M{f(x)} {f(ty + 12 * k)} L {f(x)} {f(b)}" stroke="#E8B830" stroke-width="{f(7 * k)}"></path>' for x in (tx - tw / 2 + 12 * k, tx + tw / 2 - 12 * k))
             + f'<path d="M{f(tx - tw / 2 + 12 * k)} {f(b - 30 * k)} L {f(tx + tw / 2 - 12 * k)} {f(b - 30 * k)}" stroke="#E8B830" stroke-width="{f(4 * k)}"></path>')
    for row in range(2):
        for i in range(6):
            x = tx - tw * 0.4 + i * tw * 0.16 + row * tw * 0.03
            o.append(f'<ellipse cx="{f(x)}" cy="{f(ty - 6 * k - row * 9 * k)}" rx="{f(14 * k)}" ry="{f(6 * k)}" fill="#D9A25A" stroke="{INK}" stroke-width="1.2"></ellipse>')
    o.append(f'<path d="M{f(tx + tw / 2 + 20 * k)} {f(b)} L {f(tx + tw / 2 + 24 * k)} {f(b - 24 * k)} L {f(tx + tw / 2 + 44 * k)} {f(b - 24 * k)} L {f(tx + tw / 2 + 48 * k)} {f(b)} Z" fill="#E8B830" stroke="{INK}" stroke-width="1.4"></path>')
    o.append(tag(tx + 30 * k, ty - 22 * k, "THE TABLE · THE SHOWBREAD", tx + 50 * k, ty - 70 * k, GOLD, 9))
    return "".join(o)

def ark_contents(w, h):
    """After the second veil … the Holy of holies; having a golden altar of incense, and the ark of the covenant overlaid round
    about with gold, wherein was a golden pot holding the manna, and Aaron's rod that budded, and the tables of the covenant;
    and above it cherubim of glory overshadowing the mercy-seat: a technical plate — the golden altar of incense at the left
    with its smoke; the ark cut open in section, the pot of manna, the rod in blossom and the two tables within it; the
    mercy-seat its lid with the two cherubim of beaten gold over it, their wings spread, faces toward the seat (no face drawn)."""
    from rom.art import cherub
    o = [plate_bg(w, h, "HEBREWS 9:3–5 · THE HOLY OF HOLIES")]
    k = min(w / 700, (h - 34) / 250)
    ix, b = w * 0.14, h - 30                                                  # the altar of incense
    o.append(f'<rect x="{f(ix - 26 * k)}" y="{f(b - 90 * k)}" width="{f(52 * k)}" height="{f(90 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(ix - 32 * k)}" y="{f(b - 98 * k)}" width="{f(64 * k)}" height="{f(10 * k)}" fill="#FFD23F" stroke="{INK}" stroke-width="1.6"></rect>'
             + "".join(f'<path d="M{f(ix + sg * 32 * k)} {f(b - 98 * k)} L {f(ix + sg * 36 * k)} {f(b - 110 * k)} L {f(ix + sg * 24 * k)} {f(b - 98 * k)} Z" fill="#FFD23F" stroke="{INK}" stroke-width="1.2"></path>' for sg in (-1, 1))
             + f'<path d="M{f(ix)} {f(b - 104 * k)} C {f(ix - 20 * k)} {f(b - 140 * k)} {f(ix + 20 * k)} {f(b - 170 * k)} {f(ix - 6 * k)} {f(b - 210 * k)}" fill="none" stroke="#E8E2F0" stroke-width="{f(6 * k)}" opacity="0.7"></path>')
    ax, aw, ah = w * 0.58, 300 * k, 110 * k                                   # the ark, in section
    ay = b - ah
    o.append(f'<rect x="{f(ax - aw / 2)}" y="{f(ay)}" width="{f(aw)}" height="{f(ah)}" fill="#3A2A1A" stroke="{GOLD}" stroke-width="3"></rect>'
             f'<rect x="{f(ax - aw / 2 + 8 * k)}" y="{f(ay + 8 * k)}" width="{f(aw - 16 * k)}" height="{f(ah - 16 * k)}" fill="#1A120A" stroke="#C8962A" stroke-width="1.4" stroke-dasharray="5 3"></rect>')
    px = ax - aw * 0.32                                                       # the pot of manna
    o.append(f'<path d="M{f(px - 18 * k)} {f(b - 12 * k)} L {f(px - 22 * k)} {f(b - 56 * k)} C {f(px - 16 * k)} {f(b - 66 * k)} {f(px + 16 * k)} {f(b - 66 * k)} {f(px + 22 * k)} {f(b - 56 * k)} L {f(px + 18 * k)} {f(b - 12 * k)} Z" fill="#FFD23F" stroke="{INK}" stroke-width="1.6"></path>'
             f'<ellipse cx="{f(px)}" cy="{f(b - 60 * k)}" rx="{f(18 * k)}" ry="{f(5 * k)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1"></ellipse>')
    rx = ax                                                                   # Aaron's rod that budded
    o.append(f'<path d="M{f(rx - 30 * k)} {f(b - 14 * k)} L {f(rx + 40 * k)} {f(b - 92 * k)}" stroke="#8A5A2A" stroke-width="{f(5 * k)}" stroke-linecap="round"></path>'
             + "".join(f'<circle cx="{f(rx - 30 * k + 70 * k * q)}" cy="{f(b - 14 * k - 78 * k * q - 8 * k)}" r="{f(5 * k)}" fill="#FFF0F4" stroke="#C8708A" stroke-width="1.2"></circle>'
                       f'<ellipse cx="{f(rx - 30 * k + 70 * k * q + 9 * k)}" cy="{f(b - 14 * k - 78 * k * q + 2 * k)}" rx="{f(6 * k)}" ry="{f(3 * k)}" fill="#7AB04A" stroke="{INK}" stroke-width="0.8"></ellipse>' for q in (0.3, 0.55, 0.8)))
    tx = ax + aw * 0.3                                                        # the tables of the covenant
    for d in (-12, 10):
        o.append(f'<path d="M{f(tx + d * k - 16 * k)} {f(b - 12 * k)} L {f(tx + d * k - 16 * k)} {f(b - 70 * k)} C {f(tx + d * k - 16 * k)} {f(b - 86 * k)} {f(tx + d * k + 16 * k)} {f(b - 86 * k)} {f(tx + d * k + 16 * k)} {f(b - 70 * k)} L {f(tx + d * k + 16 * k)} {f(b - 12 * k)} Z" fill="#A8A0A0" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(f'<rect x="{f(ax - aw / 2 - 8 * k)}" y="{f(ay - 12 * k)}" width="{f(aw + 16 * k)}" height="{f(12 * k)}" fill="#FFD23F" stroke="{INK}" stroke-width="2"></rect>')
    o.append(cherub(ax - aw * 0.36, ay - 12 * k, k * 0.62, 1.0, False, "hc1") + cherub(ax + aw * 0.36, ay - 12 * k, k * 0.62, 1.0, True, "hc2"))
    o.append(glow(ax, ay - 50 * k, 90 * k, "#FFF4C2", 0.35, "hcg"))
    r1, r2 = 44, 62
    o.append(tag(px, b - 62 * k, "A GOLDEN POT HOLDING THE MANNA", ax - aw / 2 - 16 * k, r2 + 34, GOLD, 9))
    o.append(tag(rx + 30 * k, b - 84 * k, "AARON'S ROD THAT BUDDED", ax + 40 * k, r1, GOLD, 9))
    o.append(tag(tx + 10 * k, b - 72 * k, "THE TABLES OF THE COVENANT", ax + aw / 2 + 14 * k, r2 + 34, GOLD, 9))
    o.append(label(ax - 30 * k, r2, "CHERUBIM OF GLORY · THE MERCY-SEAT", CY, 9))
    o.append(label(ix, h - 10, "THE GOLDEN ALTAR OF INCENSE", CY, 8))
    return "".join(o)

def veil_curtain(x0, x1, top, b, k=1.0):
    """The veil before the Holy of holies: blue, purple and scarlet and fine twined linen in heavy folds, cherubim woven in it."""
    o = [f'<rect x="{f(x0)}" y="{f(top)}" width="{f(x1 - x0)}" height="{f(b - top)}" fill="#2A3F8A" stroke="{INK}" stroke-width="2.4"></rect>']
    cols = ["#1F3F8A", "#5A2A7A", "#A82A2A", "#2A3F8A"]
    n = max(4, int((x1 - x0) / (24 * k)))
    for i in range(n):
        x = x0 + (x1 - x0) * i / n
        o.append(f'<rect x="{f(x)}" y="{f(top)}" width="{f((x1 - x0) / n)}" height="{f(b - top)}" fill="{cols[i % 4]}" opacity="0.9"></rect>'
                 f'<path d="M{f(x)} {f(top)} L {f(x)} {f(b)}" stroke="#0D0D0F" stroke-width="1" opacity="0.5"></path>')
    for j in range(2):
        cx = x0 + (x1 - x0) * (0.3 + 0.4 * j); cy = top + (b - top) * 0.4
        o.append(f'<path d="M{f(cx - 22 * k)} {f(cy)} C {f(cx - 14 * k)} {f(cy - 26 * k)} {f(cx + 14 * k)} {f(cy - 26 * k)} {f(cx + 22 * k)} {f(cy)} M{f(cx)} {f(cy - 10 * k)} L {f(cx)} {f(cy + 26 * k)}" fill="none" stroke="#E8B830" stroke-width="{f(2.4 * k)}"></path>')
    return "".join(o)

def once_a_year(p, w, h, seed):
    """Into the second the high priest alone, once in the year: within the holy place by the light of the candlestick, the
    high priest in the holy garments going in alone toward the great veil, the censer smoking in his hand and the golden bowl
    in the other (no blood drawn); the altar of incense smoking before the veil."""
    b = h * 0.95
    o = [defs_up(p), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A10"></rect>',
         glow(w * 0.16, h * 0.36, h * 0.6, "#FFC14D", 0.55, f"{p}l")]
    k = min(1.0, h / 320)
    o.append(veil_curtain(w * 0.56, w + 10, -10, b, k))
    o.append(f'<path d="M-10 {f(b)} L {f(w + 10)} {f(b)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#4A3020" stroke="{INK}" stroke-width="2"></path>')
    lx = w * 0.12                                                             # the candlestick
    o.append(f'<path d="M{f(lx)} {f(b)} L {f(lx)} {f(b - 130 * k)}" stroke="#E8B830" stroke-width="{f(5 * k)}"></path>'
             + "".join(f'<path d="M{f(lx)} {f(b - 70 * k)} C {f(lx + d * 8 * k)} {f(b - 80 * k)} {f(lx + d * 14 * k)} {f(b - 110 * k)} {f(lx + d * 14 * k)} {f(b - 130 * k)}" fill="none" stroke="#E8B830" stroke-width="{f(3 * k)}"></path>' for d in (-3, -2, -1, 1, 2, 3))
             + "".join(f'<path d="M{f(lx + d * 14 * k)} {f(b - 132 * k)} c -3 -6 0 -12 0 -14 c 2 4 4 8 0 14 Z" fill="#FFE680"></path>' for d in (-3, -2, -1, 0, 1, 2, 3)))
    ix = w * 0.5                                                              # the altar of incense
    o.append(f'<rect x="{f(ix - 18 * k)}" y="{f(b - 64 * k)}" width="{f(36 * k)}" height="{f(64 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="1.8"></rect>'
             f'<path d="M{f(ix)} {f(b - 70 * k)} C {f(ix - 16 * k)} {f(b - 110 * k)} {f(ix + 16 * k)} {f(b - 150 * k)} {f(ix - 4 * k)} {f(b - 200 * k)}" fill="none" stroke="#E8E2F0" stroke-width="{f(8 * k)}" opacity="0.6"></path>')
    s = fit(b, max(h * 0.25, b - 230))
    bowl = '<ellipse cx="54" cy="-118" rx="12" ry="5" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
    o.append(high_priest(p, w * 0.32, b, s, up=[(-22, -158), (-44, -140), (-62, -132)], extra=censer(-64, -132, 1.0) + bowl))
    return "".join(o)

def first_tent(w, h):
    """While the first tabernacle is yet standing; which is a figure for the time present: the tabernacle in its court, as an
    elevation with a scale bar (Exodus' blueprint)."""
    import exo.art8 as B
    return B.sanctuary(w, h)

def not_made(w, h, seed):
    """Christ having come a high priest of the good things to come, through the greater and more perfect tabernacle, not made
    with hands, that is to say, not of this creation: the tabernacle drawn in lines of light on the night of the stars, larger
    than the sky can hold, its lines running off the edges; below, small and dark, the earth."""
    o = [sky(w, h, "#05051A", "#1E1650"), starfield(w, h, seed, 120, 0.9)]
    s = min(w / 560, h / 210)
    o.append(halo(w * 0.5, h * 0.5, max(w, h) * 0.5, "#FFE680", 0.22) + tent_plan(w * 0.5, h * 0.84, s, color="#FFE680", fill="none", sw=3))
    o.append(f'<path d="M-10 {f(h * 0.96)} C {f(w * 0.3)} {f(h * 0.93)} {f(w * 0.7)} {f(h * 0.93)} {f(w + 10)} {f(h * 0.96)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#14142E" stroke="#3A3A6A" stroke-width="1.6"></path>')
    o.append(plate_label(w * 0.5, h * 0.12, "NOT MADE WITH HANDS · NOT OF THIS CREATION", GOLD, 11))
    return "".join(o)

def ashes(w, h, seed):
    """The blood of goats and bulls, and the ashes of a heifer sprinkling them that have been defiled: on a stone ledge by
    lamplight, a jar of the ashes of the heifer, a basin of running water, a bunch of hyssop and a skein of scarlet wool laid
    by it (no beast drawn, no blood)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1E18"></rect>', glow(w * 0.8, h * 0.3, h * 0.6, "#FFC14D", 0.45, "ashg")]
    k = min(w / 600, h / 260)
    b = h * 0.78
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h - b + 10)}" fill="#6A5A4A" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M-10 {f(b + 18 * k)} L {f(w + 10)} {f(b + 18 * k)}" stroke="#4A3A2A" stroke-width="2"></path>')
    jx = w * 0.26                                                             # the jar of ashes
    o.append(f'<path d="M{f(jx - 40 * k)} {f(b)} C {f(jx - 60 * k)} {f(b - 60 * k)} {f(jx - 50 * k)} {f(b - 110 * k)} {f(jx - 22 * k)} {f(b - 124 * k)} L {f(jx + 22 * k)} {f(b - 124 * k)} '
             f'C {f(jx + 50 * k)} {f(b - 110 * k)} {f(jx + 60 * k)} {f(b - 60 * k)} {f(jx + 40 * k)} {f(b)} Z" fill="#9A5A3A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(jx)}" cy="{f(b - 124 * k)}" rx="{f(22 * k)}" ry="{f(6 * k)}" fill="#8A8480" stroke="{INK}" stroke-width="1.6"></ellipse>')
    bx = w * 0.56                                                             # the basin of water
    o.append(f'<path d="M{f(bx - 70 * k)} {f(b - 40 * k)} C {f(bx - 60 * k)} {f(b)} {f(bx + 60 * k)} {f(b)} {f(bx + 70 * k)} {f(b - 40 * k)} Z" fill="#B8863A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(bx)}" cy="{f(b - 40 * k)}" rx="{f(70 * k)}" ry="{f(10 * k)}" fill="#8FD0E2" stroke="{INK}" stroke-width="2"></ellipse>')
    hx = w * 0.8                                                              # hyssop and scarlet wool
    o.append("".join(f'<path d="M{f(hx - 50 * k)} {f(b - 4 * k)} C {f(hx - 20 * k)} {f(b - 10 * k - i * 3 * k)} {f(hx + 10 * k)} {f(b - 20 * k - i * 6 * k)} {f(hx + 40 * k)} {f(b - 28 * k - i * 9 * k)}" fill="none" stroke="#5A7A3A" stroke-width="{f(2.4 * k)}"></path>'
                     f'<circle cx="{f(hx + 40 * k)}" cy="{f(b - 28 * k - i * 9 * k)}" r="{f(5 * k)}" fill="#7A9A4A" stroke="{INK}" stroke-width="0.8"></circle>' for i in range(4))
             + f'<path d="M{f(hx - 46 * k)} {f(b - 4 * k)} C {f(hx - 40 * k)} {f(b - 14 * k)} {f(hx - 30 * k)} {f(b - 4 * k)} {f(hx - 24 * k)} {f(b - 12 * k)} C {f(hx - 18 * k)} {f(b - 4 * k)} {f(hx - 10 * k)} {f(b - 14 * k)} {f(hx - 4 * k)} {f(b - 6 * k)}" fill="none" stroke="#C8202A" stroke-width="{f(4 * k)}"></path>')
    o.append(plate_label(jx, b + 40 * k, "THE ASHES OF A HEIFER", "#FFD08A", 9, halo_="#2A1E18") + plate_label(bx, b + 40 * k, "WATER", "#FFD08A", 9, halo_="#2A1E18")
             + plate_label(hx - 10 * k, b + 40 * k, "HYSSOP · SCARLET WOOL", "#FFD08A", 9, halo_="#2A1E18"))
    return "".join(o)

def testament(w, h):
    """He is the mediator of a new covenant … where a testament is, there must of necessity be the death of him that made it;
    for a testament is of force where there hath been death: a plate — the testament written and sealed, its seals unbroken
    while he that made it liveth (DOTH NEVER AVAIL), and the same roll opened, its seals broken, OF FORCE: THE ETERNAL
    INHERITANCE."""
    o = [plate_bg(w, h, "HEBREWS 9:15–17 · A TESTAMENT IS OF FORCE")]
    k = min(w / 700, (h - 34) / 230)
    lx, rx, cy = w * 0.26, w * 0.72, h * 0.52
    o.append(sealed_scroll(lx, cy, 1.6 * k, rot=-6))
    o.append(label(lx, cy + 70 * k, "WHILE HE THAT MADE IT LIVETH", CY, 9) + label(lx, cy + 84 * k, "IT DOTH NEVER AVAIL", CY, 9))
    o.append(open_letter(rx - 110 * k, cy - 60 * k, 220 * k, 110 * k, rows=6, seed=9) + halo(rx, cy, 120 * k, "#FFE680", 0.2))
    for sx in (-1, 1):
        o.append(f'<path d="M{f(rx + sx * 118 * k)} {f(cy - 8 * k)} l {f(sx * 8 * k)} {f(-8 * k)} l {f(sx * 6 * k)} {f(10 * k)} l {f(sx * 6 * k)} {f(-6 * k)}" fill="none" stroke="#B5121B" stroke-width="{f(4 * k)}"></path>')
    o.append(label(rx, cy + 70 * k, "OF FORCE · THE PROMISE OF", GOLD, 9) + label(rx, cy + 84 * k, "THE ETERNAL INHERITANCE", GOLD, 9))
    o.append(f'<path d="M{f(lx + 100 * k)} {f(cy)} L {f(rx - 130 * k)} {f(cy)}" stroke="{GOLD}" stroke-width="2.4" stroke-dasharray="6 4"></path>')
    return "".join(o)

def covenant_altar(p, w, h, seed):
    """Moses … took the blood of the calves and the goats, with water and scarlet wool and hyssop, and sprinkled both the book
    itself and all the people: the altar under the mount with its smoke and the twelve pillars in a row (Exodus' drawing,
    Moses and the sprinkling not drawn)."""
    from exo.art7 import pillars12
    return mk.defs(p, *ALL) + pillars12(p, w, h, seed, sprinkle=False)

def heaven_itself(p, w, h, seed):
    """Christ entered not into a holy place made with hands, like in pattern to the true; but into heaven itself, now to appear
    before the face of God for us: steps of light going up from the clouds to a great doorway of light, and Jesus risen in
    white light standing on them, his hands lifted — the light beyond the door no one's figure."""
    o = [defs_up(p), sky(w, h, "#1A1440", "#C8A0D8"), starfield(w, h, seed, 30, 0.4)]
    o.append(cloud_bank(w, h * 0.8, seed, "#FFF8E8", 0.85, k=min(1.0, h / 320)))
    dx, dw, dt = w * 0.62, w * 0.2, h * 0.08
    o.append(glow(dx, h * 0.4, h * 0.7, "#FFFFFF", 0.85, f"{p}d") + rays(dx, h * 0.36, 36, h * 0.1, max(w, h), "#FFF4C2", 0.25, 4))
    o.append(f'<path d="M{f(dx - dw / 2)} {f(h * 0.7)} L {f(dx - dw / 2)} {f(dt + dw / 2)} A {f(dw / 2)} {f(dw / 2)} 0 0 1 {f(dx + dw / 2)} {f(dt + dw / 2)} L {f(dx + dw / 2)} {f(h * 0.7)} Z" fill="#FFFFFF" stroke="#E8B830" stroke-width="3"></path>')
    for i in range(5):                                                        # the steps
        y = h * 0.7 + i * h * 0.03; ww = dw * (1.1 + i * 0.25)
        o.append(f'<rect x="{f(dx - ww / 2)}" y="{f(y)}" width="{f(ww)}" height="{f(h * 0.03)}" fill="#FFF8DC" stroke="#C8962A" stroke-width="1.4"></rect>')
    s = h * 0.5 / 205
    o.append(risen_fig(p, w * 0.32, h * 0.86, s, flip=True, up=[(-22, -158), (-36, -186), (-40, -214)]))
    return "".join(o)

def year_by_year(w, h):
    """Nor yet that he should offer himself often, as the high priest entereth into the holy place year by year …; but now once
    at the end of the ages hath he been manifested to put away sin by the sacrifice of himself: a timeline plate — the day of
    atonement repeated year after year along the rule, each a small flame, running back into the dark; and at the end of the
    ages one gold mark: ONCE."""
    o = [plate_bg(w, h, "HEBREWS 9:25–26 · YEAR BY YEAR · ONCE AT THE END OF THE AGES")]
    y = h * 0.6; x0, x1 = w * 0.04, w * 0.8
    o.append(f'<path d="M{f(x0)} {f(y)} L {f(w * 0.96)} {f(y)}" stroke="{CY}" stroke-width="2"></path>')
    n = 18
    for i in range(n):
        x = x0 + (x1 - x0) * i / (n - 1); op = 0.3 + 0.7 * i / (n - 1); k = min(1.0, h / 260)
        o.append(f'<path d="M{f(x - 5 * k)} {f(y - 4)} C {f(x - 6 * k)} {f(y - 18 * k)} {f(x)} {f(y - 22 * k)} {f(x)} {f(y - 28 * k)} C {f(x + 2 * k)} {f(y - 20 * k)} {f(x + 6 * k)} {f(y - 16 * k)} {f(x + 5 * k)} {f(y - 4)} Z" fill="#FF8A3D" opacity="{op:.2f}"></path>'
                 f'<path d="M{f(x)} {f(y - 4)} L {f(x)} {f(y + 6)}" stroke="{CY}" stroke-width="1.4" opacity="{op:.2f}"></path>')
    o.append(label((x0 + x1) / 2, y + 26, "THE HIGH PRIEST ENTERETH · YEAR BY YEAR", CY, 9))
    gx = w * 0.9
    o.append(halo(gx, y, 50, "#FFE680", 0.5) + f'<rect x="{f(gx - 4)}" y="{f(y - 40)}" width="8" height="80" fill="{GOLD}"></rect>' + label(gx, y - 50, "ONCE", GOLD, 12)
             + label(gx - 20, y + 54, "AT THE END OF THE AGES", GOLD, 9, anchor="end"))
    return "".join(o)

def second_time(w, h, seed):
    """It is appointed unto men once to die, and after this cometh judgment; so Christ also … shall appear a second time, apart
    from sin, to them that wait for him, unto salvation: the sepulchres hewn in the hillside in the grey before dawn, their
    stones rolled to, and over the hills the clouds breaking open on a great light."""
    o = [sky(w, h, "#1A1A4A", "#FFD8A0"), glow(w * 0.62, h * 0.3, h * 0.7, "#FFFFFF", 0.8, "stg"), rays(w * 0.62, h * 0.3, 40, h * 0.12, max(w, h), "#FFF4C2", 0.25, 4)]
    o.append(cloud_bank(w * 0.4, h * 0.4, seed, "#8A80A8", 0.85, k=min(1.0, h / 300)))
    o.append(f'<g transform="translate({f(w * 0.74)} 0)">' + cloud_bank(w * 0.4, h * 0.36, seed + 1, "#8A80A8", 0.85, k=min(1.0, h / 300)) + '</g>')
    o.append(hills(w, h, h * 0.6, seed, color="#3A3048", amp=14, step=90))
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.66)} C {f(w * 0.3)} {f(h * 0.6)} {f(w * 0.6)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.68)} L {f(w + 10)} {f(h + 10)} Z" fill="#5A4A5A" stroke="{INK}" stroke-width="2"></path>')
    k = min(1.0, h / 300)
    for i in range(6):
        x = w * (0.08 + 0.16 * i); y = h * (0.82 + 0.04 * (i % 2))
        o.append(f'<path d="M{f(x - 20 * k)} {f(y)} L {f(x - 20 * k)} {f(y - 30 * k)} A {f(20 * k)} {f(20 * k)} 0 0 1 {f(x + 20 * k)} {f(y - 30 * k)} L {f(x + 20 * k)} {f(y)} Z" fill="#1A1218" stroke="{INK}" stroke-width="1.6"></path>'
                 f'<circle cx="{f(x + 10 * k)}" cy="{f(y - 22 * k)}" r="{f(22 * k)}" fill="#8A7A7A" stroke="{INK}" stroke-width="2"></circle>')
    return "".join(o)

# ---- Hebrews 10 -----------------------------------------------------------------------------------------------------------
def shadow(w, h, seed):
    """The law having a shadow of the good things to come, not the very image of the things: an emblem — a lamp at the right
    throwing the shadow of the tabernacle long across the floor to the left, the tent itself small and lit; the shadow dark
    and empty."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A22"></rect>', glow(w * 0.9, h * 0.4, h * 0.7, "#FFC14D", 0.55, "shg")]
    b = h * 0.8
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h - b + 10)}" fill="#6A5040"></rect>')
    s = min(w / 1300, h / 330)
    tx = w * 0.62
    o.append(f'<path d="M{f(tx - 120 * s)} {f(b)} L {f(-10)} {f(b - 40 * s)} L {f(-10)} {f(b + 30 * s)} Z" fill="#1A120E" opacity="0.85"></path>'
             f'<path d="M{f(tx - 120 * s)} {f(b - 160 * s)} L {f(-10)} {f(b - 70 * s)} L {f(-10)} {f(b - 40 * s)} L {f(tx - 120 * s)} {f(b)} Z" fill="#1A120E" opacity="0.7"></path>')
    o.append(tent_plan(tx, b, s, color="#0D0D0F", fill="#E8D8B0", sw=2))
    lx = w * 0.9                                                              # the lamp
    o.append(f'<path d="M{f(lx - 18)} {f(b)} L {f(lx - 6)} {f(b - 40)} L {f(lx + 6)} {f(b - 40)} L {f(lx + 18)} {f(b)} Z" fill="#8A5A3A" stroke="{INK}" stroke-width="1.6"></path>'
             f'<ellipse cx="{f(lx)}" cy="{f(b - 44)}" rx="16" ry="6" fill="#A86A3A" stroke="{INK}" stroke-width="1.6"></ellipse><path d="M{f(lx + 12)} {f(b - 46)} c -4 -10 2 -18 2 -24 c 4 8 6 16 -2 24 Z" fill="#FFE680"></path>')
    o.append(plate_label(w * 0.22, b + 24, "A SHADOW OF THE GOOD THINGS TO COME", "#FFD08A", 9, halo_="#3A2A22") + plate_label(tx, h * 0.14, "NOT THE VERY IMAGE OF THE THINGS", "#FFD08A", 9, halo_="#3A2A22"))
    return "".join(o)

def roll_of_book(p, w, h, seed):
    """In the roll of the book it is written of me: an open scroll on a reading-desk under a lamp, light about it (Matthew's
    drawing)."""
    from mat.art import prophecy
    return prophecy(p, w, h, seed)

def once_for_all(w, h, seed):
    """Through the offering of the body of Jesus Christ once for all: the hill of Golgotha from far off under a darkened sky,
    three crosses small on its top (Galatians' drawing)."""
    from gal.art import far_crosses
    return far_crosses(w, h, seed)

def standing_priest(p, w, h, seed):
    """Every priest indeed standeth day by day ministering and offering oftentimes the same sacrifices: a priest in white
    standing at the altar of burnt-offering in the morning, its fire and smoke, the sun low; and high above in the light, the
    throne standing empty — he sat down on the right hand of God."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#5A5A9A", "#FFD8A0"), halo(w * 0.86, h * 0.1, h * 0.3, "#FFFFFF", 0.6), ground(w, h, h * 0.72, "#D8C8A0", dy=0)]
    o.append(f'<rect x="-10" y="{f(h * 0.56)}" width="{f(w + 20)}" height="{f(h * 0.16)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(x)} {f(h * 0.54)} L {f(x)} {f(h * 0.72)}" stroke="#8A6A4A" stroke-width="3"></path>' for x in range(0, int(w) + 40, 46)))
    s = fit(b, max(h * 0.25, b - 220))
    o.append(altar_fire(w * 0.44, b, s * 0.9, f"{p}a"))
    o.append(priest_white(p, w * 0.2, b, s, flip=True, up=[(-22, -158), (-44, -150), (-60, -160)]))
    o.append(throne_of_light(w * 0.84, h * 0.4, min(h * 0.34 / 300, w * 0.14 / 220), f"{p}t", lit=0.8))
    return "".join(o)

def remember_no_more(w, h, seed):
    """Their sins and their iniquities will I remember no more. Now where remission of these is, there is no more offering for
    sin: a long roll of reckoning lying open, its rows of writing fading into light from the left to the right until the
    sheet is clean; the altar beside it cold, its fire gone out."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1E30"></rect>', glow(w * 0.85, h * 0.4, h * 0.7, "#FFF4C2", 0.6, "rmg")]
    k = min(w / 600, h / 260)
    x0, x1, y0, y1 = w * 0.08, w * 0.92, h * 0.24, h * 0.7
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(x1 - x0)}" height="{f(y1 - y0)}" fill="#EADBB4" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(x0 - 12 * k)}" y="{f(y0 - 6 * k)}" width="{f(16 * k)}" height="{f(y1 - y0 + 12 * k)}" rx="{f(6 * k)}" fill="#C8B488" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(x1 - 4 * k)}" y="{f(y0 - 6 * k)}" width="{f(16 * k)}" height="{f(y1 - y0 + 12 * k)}" rx="{f(6 * k)}" fill="#C8B488" stroke="{INK}" stroke-width="2"></rect>')
    r = random.Random(seed)
    for row in range(7):
        y = y0 + (y1 - y0) * (row + 0.8) / 7.6; x = x0 + 14
        while x < x1 - 20:
            L = (x1 - x0) * r.uniform(0.04, 0.1); t = (x - x0) / (x1 - x0)
            op = max(0.0, 1 - t * 1.25)
            if op > 0.02: o.append(f'<path d="M{f(x)} {f(y)} l {f(L)} 0" stroke="#4A3020" stroke-width="{f(max(1.2, 2.2 * k))}" opacity="{op:.2f}"></path>')
            x += L + 8
    o.append(halo(w * 0.8, (y0 + y1) / 2, (y1 - y0) * 0.7, "#FFFFFF", 0.45))
    o.append(plate_label(w * 0.5, h * 0.86, "WILL I REMEMBER NO MORE", "#FFE680", 11, halo_="#2A1E30"))
    return "".join(o)

def rent_veil(p, w, h, seed):
    """Boldness to enter into the holy place … by the way which he dedicated for us, a new and living way, through the veil:
    the great curtain before the holy place rent in two from the top to the bottom, light beyond it (Matthew's drawing)."""
    from mat.art11 import veil_rent
    return veil_rent(p, w, h, seed)

def assembling(p, w, h, seed):
    """Not forsaking our own assembling together … but exhorting one another: the church gathered by lamplight in a house, one
    of the brethren standing and reading a letter aloud from the roll (2 Corinthians' drawing)."""
    from co2.art2 import corinth_reading
    return corinth_reading(p, w, h, seed)

def fire_field(w, h, seed):
    """A certain fearful expectation of judgment, and a fierceness of fire which shall devour the adversaries: a fierce fire
    running across an empty dark plain at night, the smoke rolling up over it — no one in it."""
    r = random.Random(seed)
    o = [sky(w, h, "#05050E", "#3A0A10"), ground(w, h, h * 0.62, "#140A0A", dy=0)]
    for i in range(5):
        x = w * r.uniform(0.05, 0.95)
        o.append(f'<path d="M{f(x)} {f(h * 0.6)} C {f(x - 60)} {f(h * 0.4)} {f(x + 60)} {f(h * 0.2)} {f(x - 20)} -10" fill="none" stroke="#2A1A1E" stroke-width="{f(r.uniform(40, 80))}" stroke-linecap="round" opacity="0.7"></path>')
    for i in range(22):
        x = w * (i / 21) + r.uniform(-10, 10); hh = h * r.uniform(0.18, 0.42) * (1 - abs(i - 10.5) / 30)
        b = h * r.uniform(0.66, 0.9)
        o.append(f'<path d="M{f(x - 24)} {f(b)} C {f(x - 28)} {f(b - hh * 0.6)} {f(x - 6)} {f(b - hh * 0.8)} {f(x)} {f(b - hh)} C {f(x + 8)} {f(b - hh * 0.6)} {f(x + 26)} {f(b - hh * 0.5)} {f(x + 24)} {f(b)} Z" '
                 f'fill="{r.choice(["#FF6A2A", "#FFC14D", "#D7261E", "#FF8A3D"])}" opacity="0.9"></path>')
    o.append(halo(w * 0.5, h * 0.8, h * 0.6, "#FF6A2A", 0.35))
    return "".join(o)

def storm(w, h, seed):
    """Vengeance belongeth unto me, I will recompense … It is a fearful thing to fall into the hands of the living God: a
    storm breaking over the bare hills, lightning and rain — nothing struck, no figure (Romans' drawing)."""
    from rom.art import wrath
    return wrath(w, h, seed)

def bonds(p, w, h, seed):
    """Ye both had compassion on them that were in bonds, and took joyfully the spoiling of your possessions: a city street at
    night, the prison's iron-bound door shut in its stone wall, a torch burnt low (2 Corinthians' drawing)."""
    from co2.art2 import prison_night
    return prison_night(p, w, h, seed)

def endure(p, w, h, seed):
    """Ye have need of patience … For yet a very little while, he that cometh shall come, and shall not tarry. But my
    righteous one shall live by faith: a traveller with his staff walking on along a long road at first light, the city of
    light on the hills far ahead of him, the sun not yet up."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#2A2A5A", "#FFC890"), halo(w * 0.8, h * 0.5, h * 0.5, "#FFF4C2", 0.55),
         town_hill(w * 0.8, h * 0.56, w * 0.26, h * 0.18, seed, color="#C8A878", lit=True), hills(w, h, h * 0.58, seed, color="#5A3A4A", amp=12, step=90),
         ground(w, h, h * 0.66, "#7A5A4A", dy=0)]
    o.append(f'<path d="M{f(w * 0.02)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.86)} {f(w * 0.55)} {f(h * 0.72)} {f(w * 0.74)} {f(h * 0.66)} L {f(w * 0.77)} {f(h * 0.66)} '
             f'C {f(w * 0.62)} {f(h * 0.76)} {f(w * 0.46)} {f(h * 0.9)} {f(w * 0.3)} {f(h + 10)} Z" fill="#C8A878" stroke="{INK}" stroke-width="2"></path>')
    s = fit(b, max(h * 0.25, b - 230))
    staff = '<path d="M30 -150 L 44 4" stroke="#6A4A2A" stroke-width="5" stroke-linecap="round"></path>'
    o.append(robed(p, w * 0.3, b, s, "#5A4A3A", head="#2A3A4A", cord="#0D1A2A", beard="#2A1A10", mantle="#3A2A1A", flip=True, pose="walk", extra=staff))
    return "".join(o)
