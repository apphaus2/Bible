"""Drawings for the Hebrews volume, chapter 2 (Hebrews 5–8): the high priest, Melchizedek and Abraham, the oath and the
anchor, the priests of Levi dying one by one, the true tabernacle and the pattern in the mount, the new covenant. Built on
heb.art (which carries Galatians', Acts', Matthew's drawings and the epistle kit).

The high priest is Aaron in the holy garments as Exodus draws them (the robe of blue with bells and pomegranates at the hem,
the ephod and its band, the breastplate of twelve stones, the white mitre with its plate of gold), on the kit figure; the
sacrifices are altars, fire and smoke, no beast slain and no blood drawn. Melchizedek is Genesis' priest-king: white robe,
white beard, a gold band and crown. Abraham is Romans' (Genesis' slate-blue robe, grey hair and beard)."""
from heb.art import *
from heb.art import art, plate_label, _defs, f, INK, defs_up, face_cell, cloud_bank, throne_of_light, angel_fig, GOLD, CY, CREAM, through_heavens
from rom.art2 import abraham
import mk

# ---- the cast ---------------------------------------------------------------------------------------------------------------
def _hp_extra(k=1.0):
    """The high priest's garments over the robe, in the figure's own units: the ephod's band, the breastplate of twelve stones
    in four rows, and the bells and pomegranates round the hem."""
    stones = ["#D7261E", "#E8B830", "#2E8B57", "#1F5FAD", "#8A2BE2", "#F3EFE6", "#C8682E", "#3A3A3A", "#9A4A8A", "#5FB0C8", "#2E6B3A", "#E8C890"]
    o = ['<path d="M-20 -112 C -8 -108 8 -108 20 -112 L 21 -104 C 8 -100 -8 -100 -21 -104 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>',
         '<path d="M-17 -160 L -12 -112 M17 -160 L 12 -112" stroke="#E8B830" stroke-width="4"></path>',
         '<rect x="-11" y="-150" width="22" height="26" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></rect>']
    for i, c in enumerate(stones):
        o.append(f'<rect x="{-9 + (i % 3) * 6.4:.1f}" y="{-148 + (i // 3) * 6:.1f}" width="4.6" height="4.4" fill="{c}" stroke="#0D0D0F" stroke-width="0.6"></rect>')
    for j in range(9):
        x = -30 + j * 7.5
        o.append(f'<circle cx="{x:.1f}" cy="-5" r="2.6" fill="{"#E8B830" if j % 2 else "#A82A4A"}" stroke="#0D0D0F" stroke-width="0.8"></circle>')
    o.append('<rect x="-7" y="-206" width="14" height="5" fill="#FFD23F" stroke="#0D0D0F" stroke-width="0.8"></rect>')
    return "".join(o)

def high_priest(p, x, y, s, flip=False, up=None, extra=""):
    """Aaron the high priest in the holy garments: the robe of blue, the ephod, the breastplate, the white mitre with its gold
    plate, a grey beard (Exodus and Leviticus)."""
    return robed(p, x, y, s, "#1F3F8A", head="#F3EFE6", cord="#E8B830", beard="#9A968E", belt=None, flip=flip, up=up, extra=_hp_extra() + extra)

def priest_white(p, x, y, s, flip=False, up=None, extra=""):
    """A priest, a son of Aaron: the white linen coat, the girdle and the white head-tire."""
    return robed(p, x, y, s, "#F3EFE6", head="#F3EFE6", cord="#3A5A9A", beard="#2A1A10", belt="#3A5A9A", flip=flip, up=up, extra=extra)

def melchizedek(p, x, y, s, flip=False, up=None, extra=""):
    """Melchizedek, king of Salem, priest of God Most High: a white robe with a gold band at the hem, a white beard, a white
    headcloth bound with a gold band and a small gold crown (Genesis)."""
    crown = ('<path d="M-13 -214 L -13 -224 L -7 -218 L 0 -228 L 7 -218 L 13 -224 L 13 -214 Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.2"></path>'
             '<path d="M-34 -6 L 34 -6" stroke="#E8B830" stroke-width="4"></path>')
    return robed(p, x, y, s, "#F3EFE6", head="#F3EFE6", cord="#E8B830", beard="#F3EFE6", mantle="#E8E0CC", belt="#E8B830", flip=flip, up=up, extra=crown + extra)

def altar_fire(x, base, s, uid, smoke=True):
    """The altar of burnt-offering of acacia overlaid with brass, its horns at the corners, a fire on it and the smoke going up
    (no beast drawn); (x, base) the middle of its foot, about 130 units tall at s = 1."""
    o = [f'<path d="M{f(x - 70 * s)} {f(base)} L {f(x - 70 * s)} {f(base - 100 * s)} L {f(x + 70 * s)} {f(base - 100 * s)} L {f(x + 70 * s)} {f(base)} Z" fill="#B8863A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(x - 70 * s)} {f(base - 50 * s)} L {f(x + 70 * s)} {f(base - 50 * s)}" stroke="#7A5A2A" stroke-width="{f(3 * s)}"></path>']
    for sg in (-1, 1):
        o.append(f'<path d="M{f(x + sg * 70 * s)} {f(base - 100 * s)} L {f(x + sg * 76 * s)} {f(base - 116 * s)} L {f(x + sg * 60 * s)} {f(base - 100 * s)} Z" fill="#B8863A" stroke="{INK}" stroke-width="1.8"></path>')
    for i in range(5):
        fx = x + (i - 2) * 22 * s; hh = (40 - abs(i - 2) * 8) * s
        o.append(f'<path d="M{f(fx - 12 * s)} {f(base - 100 * s)} C {f(fx - 12 * s)} {f(base - 100 * s - hh * 0.6)} {f(fx)} {f(base - 100 * s - hh * 0.8)} {f(fx)} {f(base - 100 * s - hh)} '
                 f'C {f(fx + 4 * s)} {f(base - 100 * s - hh * 0.6)} {f(fx + 12 * s)} {f(base - 100 * s - hh * 0.5)} {f(fx + 12 * s)} {f(base - 100 * s)} Z" fill="{["#FF6A2A", "#FFC14D", "#FFE680"][i % 3]}"></path>')
    if smoke:
        o.append(f'<path d="M{f(x)} {f(base - 140 * s)} C {f(x - 40 * s)} {f(base - 200 * s)} {f(x + 40 * s)} {f(base - 260 * s)} {f(x - 10 * s)} {f(base - 340 * s)}" fill="none" stroke="#C8C0C8" stroke-width="{f(26 * s)}" stroke-linecap="round" opacity="0.5"></path>')
    return "".join(o)

def censer(x, y, s):
    """The golden censer in the high priest's hand, the incense smoke curling up from it."""
    return (f'<path d="M{f(x - 10 * s)} {f(y)} L {f(x + 10 * s)} {f(y)} L {f(x + 7 * s)} {f(y + 10 * s)} L {f(x - 7 * s)} {f(y + 10 * s)} Z" fill="#E8B830" stroke="{INK}" stroke-width="1.2"></path>'
            f'<path d="M{f(x)} {f(y - 2 * s)} C {f(x - 8 * s)} {f(y - 20 * s)} {f(x + 8 * s)} {f(y - 34 * s)} {f(x - 2 * s)} {f(y - 54 * s)}" fill="none" stroke="#E8E2F0" stroke-width="{f(4 * s)}" opacity="0.8"></path>')

# ---- Hebrews 5 ------------------------------------------------------------------------------------------------------------
def offering(p, w, h, seed):
    """Every high priest … appointed for men in things pertaining to God, that he may offer both gifts and sacrifices for sins:
    the court of the tabernacle in the morning, the altar of burnt-offering with its fire and smoke, Aaron in the holy
    garments standing before it with his hands lifted, a priest in white bringing the basket of the gifts."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#8FD0E2", "#FFF0D0"), ground(w, h, h * 0.66, "#D8C8A0", dy=0)]
    k = min(w / 700, h / 300)
    o.append(f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.16)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(x)} {f(h * 0.48)} L {f(x)} {f(h * 0.66)}" stroke="#8A6A4A" stroke-width="3"></path>' for x in range(0, int(w) + 40, 46)))
    s = fit(b, max(h * 0.25, b - 220))
    o.append(altar_fire(w * 0.66, b, s * 0.9, f"{p}a"))
    o.append(high_priest(p, w * 0.36, b, s, flip=True, up=[(-22, -158), (-40, -186), (-46, -212)]))
    basket = '<path d="M-74 -128 L -46 -128 L -50 -112 L -70 -112 Z" fill="#C8A060" stroke="#0D0D0F" stroke-width="1.4"></path><ellipse cx="-60" cy="-130" rx="12" ry="5" fill="#E8C890" stroke="#0D0D0F" stroke-width="1"></ellipse>'
    o.append(priest_white(p, w * 0.14, b, s * 0.96, flip=True, up=[(-22, -158), (-44, -140), (-58, -126)], extra=basket))
    return "".join(o)

def called(w, h):
    """No man taketh the honor unto himself, but when he is called of God, even as was Aaron … Thou art a priest for ever
    after the order of Melchizedek: two portrait cells — Aaron the high priest in his white mitre (Leviticus), and
    Melchizedek in white with his gold band (Genesis)."""
    from lev.art3 import AARON_HP
    from genesis.art3 import MELCHIZEDEK
    cw = w / 2
    return (face_cell(AARON_HP, 0, 0, cw, h, "cl0", light="#FFE680", ground=("#1A2A5A", "#4A6A9A"), name="AARON · CALLED OF GOD")
            + face_cell(MELCHIZEDEK, cw, 0, cw, h, "cl1", light="#FFF4C2", ground=("#3A2A4A", "#C8A060"), name="AFTER THE ORDER OF MELCHIZEDEK"))

def olive_garden(p, w, h, seed):
    """In the days of his flesh, having offered up prayers and supplications with strong crying and tears: the garden of
    olives on the mount at night, the great rock among the trees, the moon low, the city dark across the valley — no one
    drawn; the words carry it."""
    o = [sky(w, h, "#05051A", "#2A2A5A"), starfield(w, h, seed, 50, 0.5), halo(w * 0.82, h * 0.2, h * 0.14, "#FFF4C2", 0.4),
         f'<circle cx="{f(w * 0.82)}" cy="{f(h * 0.2)}" r="{f(max(8, h * 0.05))}" fill="#FFF8DC"></circle>',
         jerusalem_far(w, h, seed, tone="night", lit=True) if False else "",
         walls(w * 0.5, w * 0.98, h * 0.5, h * 0.14, seed, towers=3, color="#3A3450"),
         hills(w, h, h * 0.58, seed, color="#14142E", amp=12, step=90), ground(w, h, h * 0.66, "#1A1A2E", dy=0)]
    k = min(1.0, h / 320)
    o.append(f'<path d="M{f(w * 0.36)} {f(h * 0.92)} C {f(w * 0.36)} {f(h * 0.78)} {f(w * 0.46)} {f(h * 0.72)} {f(w * 0.56)} {f(h * 0.74)} C {f(w * 0.64)} {f(h * 0.76)} {f(w * 0.66)} {f(h * 0.86)} {f(w * 0.66)} {f(h * 0.92)} Z" '
             f'fill="#4A4458" stroke="{INK}" stroke-width="2.4"></path>')
    for i, (x, kk) in enumerate(((0.1, 1.0), (0.24, 0.8), (0.78, 0.9), (0.92, 1.05))):
        o.append(olive(w * x, h * 0.98, h / 330 * kk, seed=seed + i).replace("#6A8A4A", "#2A3A2A").replace("#8AA05A", "#3A4A32"))
    return "".join(o)

def milk_food(w, h, seed):
    """Such as have need of milk, and not of solid food: a jug and a cup of milk at the left, and set aside at the right the
    platter of solid food (1 Corinthians' drawing)."""
    from co1.art import milk_meat
    return milk_meat(w, h, seed)

# ---- Hebrews 6 ------------------------------------------------------------------------------------------------------------
def foundation_plate(w, h):
    """Not laying again a foundation of repentance from dead works, and of faith toward God, of the teaching of baptisms, and of
    laying on of hands, and of resurrection of the dead, and of eternal judgment … let us press on unto perfection: a
    technical plate — six foundation stones laid in a course, each named, and above them the walls rising in dashed outline to
    a gold band, PERFECTION."""
    o = [plate_bg(w, h, "HEBREWS 6:1–2 · THE FOUNDATION · PRESS ON UNTO PERFECTION")]
    names = ["REPENTANCE FROM DEAD WORKS", "FAITH TOWARD GOD", "THE TEACHING OF BAPTISMS", "LAYING ON OF HANDS", "RESURRECTION OF THE DEAD", "ETERNAL JUDGMENT"]
    x0, x1 = w * 0.05, w * 0.95; sw = (x1 - x0) / 6; y = h - 34; sh = min(46, h * 0.2)
    for i, nm in enumerate(names):
        x = x0 + i * sw
        o.append(f'<rect x="{f(x + 2)}" y="{f(y - sh)}" width="{f(sw - 4)}" height="{f(sh)}" fill="#3A4A5A" stroke="{CY}" stroke-width="1.8"></rect>')
        parts = nm.split(" ", 2) if len(nm) > 14 else [nm]
        a = " ".join(nm.split()[:len(nm.split()) // 2 + (len(nm.split()) % 2)]); b_ = " ".join(nm.split()[len(nm.split()) // 2 + (len(nm.split()) % 2):])
        o.append(label(x + sw / 2, y - sh / 2 - 2, a, CREAM, 8) + (label(x + sw / 2, y - sh / 2 + 10, b_, CREAM, 8) if b_ else ""))
    top = h * 0.2
    o.append(f'<path d="M{f(x0 + 4)} {f(y - sh)} L {f(x0 + 4)} {f(top + 20)} M{f(x1 - 4)} {f(y - sh)} L {f(x1 - 4)} {f(top + 20)}" stroke="{CY}" stroke-width="1.6" stroke-dasharray="6 5"></path>')
    for k in range(1, 4):
        yy = y - sh - k * (y - sh - top - 20) / 4
        o.append(f'<path d="M{f(x0 + 4)} {f(yy)} L {f(x1 - 4)} {f(yy)}" stroke="#2A5A7A" stroke-width="1.2" stroke-dasharray="6 5"></path>')
    o.append(f'<rect x="{f(x0 + 4)}" y="{f(top)}" width="{f(x1 - x0 - 8)}" height="20" fill="{GOLD}" opacity="0.85"></rect>' + label(w * 0.5, top + 14, "PRESS ON UNTO PERFECTION", "#12113A", 11))
    o.append(f'<path d="M{f(w * 0.5)} {f(y - sh - 8)} L {f(w * 0.5)} {f(top + 28)}" stroke="{GOLD}" stroke-width="2.4"></path><path d="M{f(w * 0.5 - 8)} {f(top + 38)} L {f(w * 0.5)} {f(top + 26)} L {f(w * 0.5 + 8)} {f(top + 38)}" fill="none" stroke="{GOLD}" stroke-width="2.4"></path>')
    return "".join(o)

def crosses_far(p, w, h, seed):
    """Seeing they crucify to themselves the Son of God afresh: the hill of the three crosses far off under a darkened sky
    (Romans' drawing): nothing nearer."""
    from rom.art2 import crosses_far as cf
    return cf(p, w, h, seed)

def rain_thorns(p, w, h, seed):
    """The land which hath drunk the rain … bringeth forth herbs … receiveth blessing; but if it beareth thorns and thistles,
    it is rejected and nigh unto a curse; whose end is to be burned: one field in two — at the left under a soft rain green
    herbs and grain in the furrows; at the right under a hard sky a waste of thorns and thistles, and the fire going through
    it."""
    r = random.Random(seed)
    o = [f'<defs><linearGradient id="{p}sk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5A7AA0"></stop><stop offset="0.48" stop-color="#9AB8D0"></stop>'
         f'<stop offset="0.52" stop-color="#C8783A"></stop><stop offset="1" stop-color="#5A1A10"></stop></linearGradient></defs><rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{p}sk)"></rect>']
    gy = h * 0.6
    o.append(f'<path d="M-10 {f(gy)} L {f(w * 0.5)} {f(gy)} L {f(w * 0.5)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A5A3A"></path>'
             f'<path d="M{f(w * 0.5)} {f(gy)} L {f(w + 10)} {f(gy)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.5)} {f(h + 10)} Z" fill="#4A3A2A"></path>')
    o.append(f'<path d="M-10 {f(gy * 0.36)} C {f(w * 0.1)} {f(gy * 0.2)} {f(w * 0.3)} {f(gy * 0.18)} {f(w * 0.46)} {f(gy * 0.32)} L {f(w * 0.46)} {f(gy * 0.4)} L -10 {f(gy * 0.4)} Z" fill="#8A9AB0" opacity="0.9"></path>')
    for i in range(46):                                                       # the rain
        x = r.uniform(0, w * 0.48); y = r.uniform(gy * 0.4, gy)
        o.append(f'<path d="M{f(x)} {f(y)} l -4 12" stroke="#DCEAF4" stroke-width="1.4"></path>')
    o.append(grain(-10, w * 0.49, h * 0.98, h * 0.3, seed, color="#7AB04A") + grain(-10, w * 0.49, h * 0.8, h * 0.16, seed + 1, color="#9CCB5E"))
    for i in range(16):                                                       # the thorns
        x = w * (0.53 + 0.028 * i) + r.uniform(-4, 4); y = h * r.uniform(0.78, 0.98); k = min(1.0, h / 320) * r.uniform(0.7, 1.1)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x - 10 * k)} {f(y - 40 * k)} M{f(x)} {f(y)} L {f(x + 12 * k)} {f(y - 34 * k)} M{f(x)} {f(y)} L {f(x + 2 * k)} {f(y - 48 * k)} M{f(x - 6 * k)} {f(y - 24 * k)} L {f(x - 14 * k)} {f(y - 28 * k)} M{f(x + 7 * k)} {f(y - 20 * k)} L {f(x + 15 * k)} {f(y - 22 * k)}" stroke="#2A1A10" stroke-width="2" fill="none"></path>'
                 + (f'<circle cx="{f(x + 2 * k)}" cy="{f(y - 50 * k)}" r="{f(4 * k)}" fill="#8A5A9A" stroke="{INK}" stroke-width="1"></circle>' if i % 3 == 0 else ""))
    for i in range(6):                                                        # the fire
        x = w * (0.66 + 0.06 * i); hh = h * r.uniform(0.18, 0.3)
        o.append(f'<path d="M{f(x - 16)} {f(h * 0.98)} C {f(x - 18)} {f(h * 0.98 - hh * 0.6)} {f(x - 4)} {f(h * 0.98 - hh * 0.8)} {f(x)} {f(h * 0.98 - hh)} C {f(x + 6)} {f(h * 0.98 - hh * 0.6)} {f(x + 18)} {f(h * 0.98 - hh * 0.5)} {f(x + 16)} {f(h * 0.98)} Z" '
                 f'fill="{["#FF6A2A", "#FFC14D", "#FF8A3D"][i % 3]}" opacity="0.9"></path>')
    o.append(f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="{INK}" stroke-width="4"></path>')
    o.append(plate_label(w * 0.25, h * 0.1, "RECEIVETH BLESSING FROM GOD", CREAM, 10, halo_="#3A5A7A") + plate_label(w * 0.75, h * 0.1, "WHOSE END IS TO BE BURNED", "#FFD08A", 10, halo_="#3A1A10"))
    return "".join(o)

def saints_table(p, w, h, seed):
    """Ye ministered unto the saints, and still do minister: the believers gathered at a long table in a house by lamplight,
    men and women, one passing bread (Romans' drawing)."""
    from rom.art5 import table_guests
    return table_guests(p, w, h, seed)

def oath_stars(p, w, h, seed):
    """When God made promise to Abraham … Surely blessing I will bless thee, and multiplying I will multiply thee: Abraham on
    the hill at night, his arm lifted to the stars, his tent below (Romans' drawing)."""
    from rom.art2 import abraham_stars
    return abraham_stars(p, w, h, seed)

def two_immutable(w, h):
    """Men swear by the greater … God … interposed with an oath; that by two immutable things, in which it is impossible for God
    to lie, we may have a strong encouragement: a technical plate — two seals side by side on one cord, THE PROMISE and THE
    OATH, each sealed and unbroken; under them IMPOSSIBLE FOR GOD TO LIE."""
    o = [plate_bg(w, h, "HEBREWS 6:16–18 · TWO IMMUTABLE THINGS")]
    k = min(w / 700, (h - 30) / 240)
    cy = h * 0.52
    o.append(f'<path d="M{f(w * 0.08)} {f(cy)} C {f(w * 0.3)} {f(cy + 30 * k)} {f(w * 0.7)} {f(cy + 30 * k)} {f(w * 0.92)} {f(cy)}" fill="none" stroke="#C8A060" stroke-width="3"></path>')
    for x, nm, sub in ((w * 0.32, "THE PROMISE", "SURELY BLESSING I WILL BLESS THEE"), (w * 0.68, "THE OATH", "HE SWARE BY HIMSELF")):
        R = 54 * k
        o.append(halo(x, cy, R * 1.8, "#FFE680", 0.25) + f'<circle cx="{f(x)}" cy="{f(cy)}" r="{f(R)}" fill="#B5121B" stroke="{INK}" stroke-width="2.4"></circle>'
                 f'<circle cx="{f(x)}" cy="{f(cy)}" r="{f(R * 0.72)}" fill="none" stroke="#7A0A10" stroke-width="2"></circle>'
                 + label(x, cy + 4, nm, GOLD, 11) + label(x, cy + R + 22, sub, CY, 9))
    o.append(label(w * 0.5, h - 14, "IN WHICH IT IS IMPOSSIBLE FOR GOD TO LIE", CREAM, 10))
    return "".join(o)

def anchor_veil(p, w, h, seed):
    """A hope … as an anchor of the soul, sure and stedfast and entering into that which is within the veil, whither as a
    forerunner Jesus entered for us: the anchor holding fast on the rock of the sea-bed in the dark water at the left, its
    cable rising up and passing through the folds of the great veil (blue, purple and scarlet) into the light beyond it."""
    o = [f'<defs><linearGradient id="{p}sea" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0B1A2E"></stop><stop offset="0.55" stop-color="#1F4A6A"></stop>'
         f'<stop offset="1" stop-color="#3A2A6A"></stop></linearGradient></defs><rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{p}sea)"></rect>']
    r = random.Random(seed)
    for i in range(14):
        x, y = r.uniform(0, w * 0.6), r.uniform(0, h)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(1.5, 4))}" fill="none" stroke="#5A8AAA" stroke-width="1"></circle>')
    o.append(f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.1)} {f(h * 0.8)} {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.46)} {f(h * 0.9)} L {f(w * 0.5)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A3A4A" stroke="{INK}" stroke-width="2.4"></path>')
    k = min(1.0, h / 300)
    ax, ay = w * 0.24, h * 0.8                                                # the anchor, its fluke bedded in the rock
    o.append(f'<g transform="translate({f(ax)} {f(ay)}) scale({f(k)})"><path d="M0 -150 L 0 0" stroke="#8A8A9A" stroke-width="9"></path>'
             '<circle cx="0" cy="-160" r="12" fill="none" stroke="#8A8A9A" stroke-width="6"></circle><path d="M-34 -120 L 34 -120" stroke="#8A8A9A" stroke-width="8" stroke-linecap="round"></path>'
             '<path d="M-56 -30 C -50 0 -20 10 0 10 C 20 10 50 0 56 -30" fill="none" stroke="#8A8A9A" stroke-width="9"></path>'
             '<path d="M-56 -30 L -66 -16 M-56 -30 L -44 -22 M56 -30 L 66 -16 M56 -30 L 44 -22" stroke="#8A8A9A" stroke-width="7" stroke-linecap="round"></path>'
             '<path d="M0 -150 L 0 0 M-34 -120 L 34 -120" stroke="#0D0D0F" stroke-width="1.5" fill="none" opacity="0.6"></path></g>')
    vx = w * 0.64                                                             # the veil
    o.append(f'<rect x="{f(vx)}" y="-10" width="{f(w - vx + 10)}" height="{f(h + 20)}" fill="#FFF4C2"></rect>' + glow(w * 0.92, h * 0.4, h * 0.6, "#FFFFFF", 0.9, f"{p}g"))
    cols = ["#1F3F8A", "#5A2A7A", "#A82A2A", "#F3EFE6"]
    for i in range(8):
        x = vx - 40 * k + i * 12 * k
        o.append(f'<path d="M{f(x)} -10 C {f(x + 6 * k)} {f(h * 0.3)} {f(x - 6 * k)} {f(h * 0.6)} {f(x + 4 * k)} {f(h + 10)} L {f(x + 14 * k)} {f(h + 10)} C {f(x + 4 * k)} {f(h * 0.6)} {f(x + 16 * k)} {f(h * 0.3)} {f(x + 12 * k)} -10 Z" '
                 f'fill="{cols[i % 4]}" stroke="{INK}" stroke-width="1.2"></path>')
    o.append(f'<path d="M{f(ax)} {f(ay - 160 * k)} C {f(ax + 40 * k)} {f(h * 0.2)} {f(vx - 80 * k)} {f(h * 0.3)} {f(vx + 60 * k)} {f(h * 0.34)}" fill="none" stroke="#C8A060" stroke-width="{f(5 * k)}"></path>'
             f'<path d="M{f(ax)} {f(ay - 160 * k)} C {f(ax + 40 * k)} {f(h * 0.2)} {f(vx - 80 * k)} {f(h * 0.3)} {f(vx + 60 * k)} {f(h * 0.34)}" fill="none" stroke="#7A5A2A" stroke-width="{f(5 * k)}" stroke-dasharray="3 5"></path>')
    o.append(plate_label(w * 0.3, h * 0.1, "AN ANCHOR OF THE SOUL · SURE AND STEDFAST", GOLD, 10) + plate_label(w * 0.84, h * 0.94, "WITHIN THE VEIL", "#7A4A10", 10, halo_="#FFF4C2"))
    return "".join(o)

# ---- Hebrews 7 ------------------------------------------------------------------------------------------------------------
def meeting(p, w, h, seed):
    """Melchizedek, king of Salem, priest of God Most High, who met Abraham returning from the slaughter of the kings and
    blessed him: Salem on its hill in the evening light at the right; Melchizedek come down from it in white with his gold
    crown, his hand lifted in blessing, bread and wine carried by a servant behind him; Abraham before him in his slate-blue
    robe, his head bowed, the men of his household and the spoil behind him — the battle told in words only."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#3A3A7A", "#FFC890"), halo(w * 0.8, h * 0.36, h * 0.4, "#FFE6A0", 0.55),
         town_hill(w * 0.84, h * 0.62, w * 0.3, h * 0.24, seed, color="#9A7A5A", lit=False), hills(w, h, h * 0.62, seed, color="#8A6A4A", amp=10, step=90),
         ground(w, h, h * 0.7, "#C8A06A", dy=0)]
    s = fit(b, max(h * 0.25, b - 220))
    o.append(plate_label(w * 0.84, h * 0.3, "SALEM", "#12113A", 10, halo_="#FFE6A0"))
    for i in range(3):                                                        # Abraham's men and the spoil, behind him
        o.append(robed(p, w * (0.05 + 0.07 * i), b - 4, s * 0.86, ["#5A4A3A", "#4A5A4A", "#6A4A3A"][i], head=["#2A3A4A", "#E8E2D6", "#1F2F2A"][i], cord="#2A1A10", beard="#2A1A10", flip=True))
    o.append(abraham(p, w * 0.34, b, s, flip=True))
    loaf = '<ellipse cx="-50" cy="-150" rx="13" ry="7" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1.6"></ellipse><path d="M-40 -160 L -28 -160 L -31 -146 L -34 -144 L -34 -134 L -29 -131 L -39 -131 L -36 -134 L -36 -144 L -39 -146 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></path>'
    o.append(robed(p, w * 0.72, b, s * 0.9, "#8A7A5A", head="#E8E2D6", cord="#6A5A3A", beard="#3A2A1A", up=[(-22, -158), (-40, -150), (-46, -152)], extra=loaf))
    o.append(melchizedek(p, w * 0.56, b, s * 1.02, up=[(-22, -158), (-40, -184), (-52, -204)]))
    return "".join(o)

def tenth(w, h):
    """To whom also Abraham divided a tenth part of all … gave a tenth out of the chief spoils: a plate — the spoil laid out in
    ten portions (sheep, oxen, bales, vessels, gold), the tenth set apart in gold before the priest-king's name."""
    o = [plate_bg(w, h, "HEBREWS 7:2–4 · A TENTH PART OF ALL")]
    x0, x1 = w * 0.06, w * 0.94; n = 10; cw = (x1 - x0) / n; y = h * 0.7; k = min(1.0, (h - 40) / 200)
    for i in range(n):
        x = x0 + i * cw + cw / 2; lit = i == n - 1
        c, st = ("#FFD23F", "#FFF4C2") if lit else ("#3A4A5A", CY)
        o.append(f'<rect x="{f(x - cw * 0.38)}" y="{f(y - 70 * k)}" width="{f(cw * 0.76)}" height="{f(70 * k)}" fill="{c}" opacity="{1 if lit else 0.7}" stroke="{st}" stroke-width="1.6"></rect>')
        kind = i % 4
        if kind == 0: o.append(f'<ellipse cx="{f(x)}" cy="{f(y - 40 * k)}" rx="{f(14 * k)}" ry="{f(9 * k)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1"></ellipse><circle cx="{f(x + 13 * k)}" cy="{f(y - 44 * k)}" r="{f(5 * k)}" fill="#3A3A3A"></circle>')
        elif kind == 1: o.append(f'<rect x="{f(x - 12 * k)}" y="{f(y - 54 * k)}" width="{f(24 * k)}" height="{f(26 * k)}" fill="#C8A060" stroke="{INK}" stroke-width="1"></rect><path d="M{f(x - 12 * k)} {f(y - 42 * k)} L {f(x + 12 * k)} {f(y - 42 * k)}" stroke="#7A5A2A" stroke-width="1.4"></path>')
        elif kind == 2: o.append(f'<path d="M{f(x - 10 * k)} {f(y - 24 * k)} L {f(x - 12 * k)} {f(y - 50 * k)} C {f(x - 8 * k)} {f(y - 60 * k)} {f(x + 8 * k)} {f(y - 60 * k)} {f(x + 12 * k)} {f(y - 50 * k)} L {f(x + 10 * k)} {f(y - 24 * k)} Z" fill="#B8863A" stroke="{INK}" stroke-width="1"></path>')
        else: o.append("".join(f'<circle cx="{f(x + (j - 1) * 8 * k)}" cy="{f(y - 30 * k - (j % 2) * 8 * k)}" r="{f(5 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="0.8"></circle>' for j in range(3)))
        o.append(label(x, y + 14, str(i + 1) if not lit else "1/10", GOLD if lit else CY, 10 if lit else 9))
    o.append(tag(x1 - cw / 2, y - 72 * k, "SET APART · TO MELCHIZEDEK", x1 - cw * 2.6, h * 0.2 + 22, GOLD, 10))
    o.append(label(x0, h * 0.2 + 26, "ABRAHAM, THE PATRIARCH", CREAM, 10, anchor="start"))
    return "".join(o)

def loins(w, h):
    """Through Abraham even Levi, who receiveth tithes, hath paid tithes; for he was yet in the loins of his father, when
    Melchizedek met him: a lineage plate — ABRAHAM lit at the left, and running from him in dashed outline (not yet born)
    ISAAC, JACOB, LEVI, and the priests of Levi with their tithes; MELCHIZEDEK above, the tithe going up to him from Abraham."""
    o = [plate_bg(w, h, "HEBREWS 7:9–10 · YET IN THE LOINS OF HIS FATHER")]
    y = h * 0.66; names = ["ABRAHAM", "ISAAC", "JACOB", "LEVI", "SONS OF LEVI"]
    xs = [w * (0.12 + 0.19 * i) for i in range(5)]
    for i, (x, nm) in enumerate(zip(xs, names)):
        lit = i == 0
        o.append(f'<rect x="{f(x - 62)}" y="{f(y - 16)}" width="124" height="32" fill="{"#FFD23F" if lit else "none"}" stroke="{GOLD if lit else CY}" stroke-width="2" {"" if lit else "stroke-dasharray=\"5 4\""}></rect>'
                 + label(x, y + 4, nm, "#12113A" if lit else CY, 10))
        if i: o.append(f'<path d="M{f(xs[i - 1] + 62)} {f(y)} L {f(x - 62)} {f(y)}" stroke="{CY}" stroke-width="1.6" stroke-dasharray="5 4"></path>')
    mx, my = w * 0.42, h * 0.3
    o.append(f'<rect x="{f(mx - 80)}" y="{f(my - 16)}" width="160" height="32" fill="#F3EFE6" stroke="{GOLD}" stroke-width="2.4"></rect>' + label(mx, my + 4, "MELCHIZEDEK", "#12113A", 11))
    o.append(f'<path d="M{f(xs[0])} {f(y - 16)} C {f(xs[0])} {f(my)} {f(mx - 120)} {f(my)} {f(mx - 82)} {f(my)}" fill="none" stroke="{GOLD}" stroke-width="2.4"></path>'
             + label((xs[0] + mx) / 2 - 40, (y + my) / 2 - 10, "THE TITHE", GOLD, 9))
    o.append(label(w * 0.6, y + 40, "NOT YET BORN · AND YET THROUGH ABRAHAM HE PAID TITHES", CY, 9))
    return "".join(o)

def two_tribes(w, h):
    """If there was perfection through the Levitical priesthood … what further need … another priest after the order of
    Melchizedek? … our Lord hath sprung out of Judah, as to which tribe Moses spake nothing concerning priests: a plate in two
    halves — LEVI at the left, the priests' white mitre and the censer; JUDAH at the right, the lion and the sceptre; an arrow
    from the one to the other: THE PRIESTHOOD BEING CHANGED."""
    o = [plate_bg(w, h, "HEBREWS 7:11–14 · THE PRIESTHOOD BEING CHANGED")]
    k = min(w / 700, (h - 30) / 240)
    lx, rx, cy = w * 0.26, w * 0.74, h * 0.54
    o.append(f'<path d="M{f(lx - 34 * k)} {f(cy + 10 * k)} C {f(lx - 40 * k)} {f(cy - 40 * k)} {f(lx + 40 * k)} {f(cy - 40 * k)} {f(lx + 34 * k)} {f(cy + 10 * k)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></path>'
             f'<rect x="{f(lx - 36 * k)}" y="{f(cy + 6 * k)}" width="{f(72 * k)}" height="{f(10 * k)}" fill="#3A5A9A" stroke="{INK}" stroke-width="1.4"></rect>'
             f'<rect x="{f(lx - 14 * k)}" y="{f(cy - 10 * k)}" width="{f(28 * k)}" height="{f(9 * k)}" fill="#FFD23F" stroke="{INK}" stroke-width="1"></rect>')
    o.append(label(lx, cy + 56 * k, "LEVI · THE ORDER OF AARON", CY, 10))
    o.append(f'<g transform="translate({f(rx - 60 * k)} {f(cy + 20 * k)}) scale({f(k * 0.5)})">' + __import__("dan.art", fromlist=["lion_walk"]).lion_walk(0, 0, 1.0, "#E8B830") + '</g>')
    o.append(f'<path d="M{f(rx + 50 * k)} {f(cy + 30 * k)} L {f(rx + 50 * k)} {f(cy - 70 * k)}" stroke="#E8B830" stroke-width="{f(6 * k)}"></path><circle cx="{f(rx + 50 * k)}" cy="{f(cy - 76 * k)}" r="{f(9 * k)}" fill="#FFD23F" stroke="{INK}" stroke-width="1.4"></circle>')
    o.append(label(rx, cy + 56 * k, "JUDAH · OUR LORD HATH SPRUNG OUT OF JUDAH", GOLD, 10))
    o.append(f'<path d="M{f(lx + 70 * k)} {f(cy - 20 * k)} L {f(rx - 90 * k)} {f(cy - 20 * k)}" stroke="{GOLD}" stroke-width="2.4"></path><path d="M{f(rx - 100 * k)} {f(cy - 28 * k)} L {f(rx - 88 * k)} {f(cy - 20 * k)} L {f(rx - 100 * k)} {f(cy - 12 * k)}" fill="none" stroke="{GOLD}" stroke-width="2.4"></path>')
    return "".join(o)

def melchizedek_light(w, h):
    """After the likeness of Melchizedek there ariseth another priest … after the power of an endless life: Melchizedek's face
    (Genesis) in a great white light — without father, without mother, having neither beginning of days nor end of life."""
    from genesis.art3 import MELCHIZEDEK
    return face_cell(MELCHIZEDEK, 0, 0, w, h, "mz", light="#FFFFFF", ground=("#3A2A5A", "#C8A0D8"), name="A PRIEST FOR EVER · AFTER THE ORDER OF MELCHIZEDEK")

def better_hope(w, h, seed):
    """A bringing in thereupon of a better hope, through which we draw nigh unto God: the dawn breaking over the hills, a great
    light rising (Romans' drawing)."""
    from rom.art import dawn
    return dawn(w, h, seed)

HIGH_PRIESTS = ["AARON", "ELEAZAR", "PHINEHAS", "ABISHUA", "BUKKI", "UZZI", "ZERAHIAH", "MERAIOTH", "AMARIAH", "AHITUB", "ZADOK", "AHIMAAZ",
                "AZARIAH", "JOHANAN", "AZARIAH", "AMARIAH", "AHITUB", "ZADOK", "SHALLUM", "HILKIAH", "AZARIAH", "SERAIAH", "JEHOZADAK"]

def many_priests(w, h):
    """They indeed have been made priests many in number, because that by death they are hindered from continuing: but he,
    because he abideth for ever, hath his priesthood unchangeable: a lineage plate — the high priests from Aaron (the line of
    1 Chronicles 6), each a short span that ends in a dark bar, one after another along the rule; and over them all one
    unbroken gold line that runs off the plate: FOR EVER."""
    o = [plate_bg(w, h, "HEBREWS 7:23–24 · MANY IN NUMBER · HINDERED BY DEATH")]
    n = len(HIGH_PRIESTS); x0, x1 = w * 0.04, w * 0.96; cw = (x1 - x0) / n
    y = h * 0.64
    for i, nm in enumerate(HIGH_PRIESTS):
        x = x0 + i * cw
        o.append(f'<path d="M{f(x + 2)} {f(y)} L {f(x + cw - 4)} {f(y)}" stroke="{CY}" stroke-width="3"></path><rect x="{f(x + cw - 5)}" y="{f(y - 8)}" width="3" height="16" fill="#0D0D0F" stroke="#5A6A7A" stroke-width="0.8"></rect>')
        o.append(f'<text x="{f(x + cw / 2)}" y="{f(y - 12)}" fill="{CY}" font-family="IBM Plex Mono, monospace" font-size="7.5" font-weight="600" letter-spacing="0.6" text-anchor="start" transform="rotate(-60 {f(x + cw / 2)} {f(y - 12)})">{nm}</text>')
    gy = h * 0.76
    o.append(f'<path d="M{f(x0)} {f(gy)} L {f(w + 10)} {f(gy)}" stroke="{GOLD}" stroke-width="5"></path>' + halo(w * 0.7, gy, 40, "#FFE680", 0.5)
             + label(w * 0.45, gy + 18, "HE ABIDETH FOR EVER · HIS PRIESTHOOD UNCHANGEABLE", GOLD, 10))
    return "".join(o)

def higher(p, w, h, seed):
    """Such a high priest became us, holy, guileless, undefiled, separated from sinners, and made higher than the heavens: the
    heavens one above another and a road of light going up through them (heb.art.through_heavens)."""
    return through_heavens(p, w, h, seed)

# ---- Hebrews 8 ------------------------------------------------------------------------------------------------------------
def tent_plan(cx, base, s, color="#FFE680", fill="none", sw=2.4):
    """The tabernacle in its court, in elevation: the hangings of the court on their pillars, the tent within, its door."""
    o = [f'<rect x="{f(cx - 230 * s)}" y="{f(base - 50 * s)}" width="{f(460 * s)}" height="{f(50 * s)}" fill="{fill}" stroke="{color}" stroke-width="{sw}"></rect>']
    o += [f'<path d="M{f(cx - 230 * s + 46 * s * i)} {f(base - 56 * s)} L {f(cx - 230 * s + 46 * s * i)} {f(base)}" stroke="{color}" stroke-width="{f(max(1, 2 * s))}"></path>' for i in range(11)]
    o.append(f'<path d="M{f(cx - 110 * s)} {f(base - 50 * s)} L {f(cx - 110 * s)} {f(base - 130 * s)} L {f(cx + 150 * s)} {f(base - 130 * s)} L {f(cx + 150 * s)} {f(base - 50 * s)} Z" fill="{fill}" stroke="{color}" stroke-width="{sw}"></path>'
             f'<path d="M{f(cx - 118 * s)} {f(base - 126 * s)} L {f(cx + 20 * s)} {f(base - 156 * s)} L {f(cx + 158 * s)} {f(base - 126 * s)} Z" fill="{fill}" stroke="{color}" stroke-width="{sw}"></path>'
             f'<path d="M{f(cx - 50 * s)} {f(base - 130 * s)} L {f(cx - 50 * s)} {f(base - 50 * s)}" stroke="{color}" stroke-width="{f(max(1, 1.6 * s))}" stroke-dasharray="4 3"></path>')
    return "".join(o)

def true_tabernacle(p, w, h, seed):
    """A minister of the sanctuary, and of the true tabernacle, which the Lord pitched, not man; who sat down on the right hand
    of the throne of the Majesty in the heavens: above the clouds in a great light, the tabernacle drawn in lines of light and
    beside it the throne standing empty; below, far down, the earth."""
    o = [sky(w, h, "#1A1440", "#E8C8A0"), starfield(w, h, seed, 40, 0.5), rays(w * 0.42, h * 0.6, 40, 0, max(w, h), "#FFF4C2", 0.2, 4)]
    o.append(cloud_bank(w, h * 0.74, seed, "#FFF8E8", 0.8, k=min(1.0, h / 320)))
    s = min(w / 900, h / 360)
    o.append(halo(w * 0.42, h * 0.6, h * 0.5, "#FFFFFF", 0.5) + tent_plan(w * 0.4, h * 0.74, s, color="#C8962A", fill="#FFFBEA", sw=2))
    o.append(throne_of_light(w * 0.84, h * 0.76, min(h * 0.55 / 300, w * 0.2 / 220), f"{p}t", lit=0.8))
    o.append(f'<path d="M-10 {f(h * 0.94)} C {f(w * 0.3)} {f(h * 0.9)} {f(w * 0.7)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.94)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A5A7A" opacity="0.7"></path>')
    o.append(plate_label(w * 0.4, h * 0.14, "THE TRUE TABERNACLE · WHICH THE LORD PITCHED, NOT MAN", "#7A4A10", 10, halo_="#FFF4E8"))
    return "".join(o)

def pattern_mount(p, w, h, seed):
    """See, saith he, that thou make all things according to the pattern that was showed thee in the mount: mount Sinai in its
    cloud and fire at the left, and over the plain at the right the pattern drawn in the sky as a plan of light — the court,
    the tent, the ark and the altar laid out — Moses small on the slope looking up at it."""
    from exo.art import moses
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#14123A", "#5A3A6A"), starfield(w, h, seed, 30, 0.4)]
    o.append(f'<path d="M-10 {f(h * 0.9)} L {f(w * 0.12)} {f(h * 0.36)} L {f(w * 0.2)} {f(h * 0.28)} L {f(w * 0.28)} {f(h * 0.38)} L {f(w * 0.46)} {f(h * 0.9)} Z" fill="#4A3A4A" stroke="{INK}" stroke-width="2.4"></path>'
             + halo(w * 0.2, h * 0.24, h * 0.24, "#FF8A3D", 0.55) + f'<ellipse cx="{f(w * 0.2)}" cy="{f(h * 0.24)}" rx="{f(w * 0.16)}" ry="{f(h * 0.1)}" fill="#3A3048" opacity="0.85"></ellipse>')
    gx, gy, gw, gh = w * 0.48, h * 0.1, w * 0.48, h * 0.56                  # the pattern in the sky
    o.append(f'<rect x="{f(gx)}" y="{f(gy)}" width="{f(gw)}" height="{f(gh)}" fill="#0B1A2E" opacity="0.6" stroke="{CY}" stroke-width="1.6"></rect>')
    o += [f'<path d="M{f(gx + gw * i / 10)} {f(gy)} L {f(gx + gw * i / 10)} {f(gy + gh)}" stroke="#1E3A5A" stroke-width="1"></path>' for i in range(1, 10)]
    o += [f'<path d="M{f(gx)} {f(gy + gh * i / 6)} L {f(gx + gw)} {f(gy + gh * i / 6)}" stroke="#1E3A5A" stroke-width="1"></path>' for i in range(1, 6)]
    cx, cyy = gx + gw / 2, gy + gh / 2
    o.append(f'<rect x="{f(gx + gw * 0.08)}" y="{f(gy + gh * 0.2)}" width="{f(gw * 0.84)}" height="{f(gh * 0.6)}" fill="none" stroke="{GOLD}" stroke-width="2"></rect>'
             f'<rect x="{f(gx + gw * 0.5)}" y="{f(gy + gh * 0.36)}" width="{f(gw * 0.34)}" height="{f(gh * 0.28)}" fill="none" stroke="{GOLD}" stroke-width="2"></rect>'
             f'<path d="M{f(gx + gw * 0.72)} {f(gy + gh * 0.36)} L {f(gx + gw * 0.72)} {f(gy + gh * 0.64)}" stroke="{GOLD}" stroke-width="1.4" stroke-dasharray="3 3"></path>'
             f'<rect x="{f(gx + gw * 0.76)}" y="{f(gy + gh * 0.46)}" width="{f(gw * 0.05)}" height="{f(gh * 0.08)}" fill="{GOLD}"></rect>'
             f'<rect x="{f(gx + gw * 0.2)}" y="{f(gy + gh * 0.44)}" width="{f(gw * 0.08)}" height="{f(gh * 0.12)}" fill="none" stroke="{GOLD}" stroke-width="2"></rect>'
             f'<path d="M{f(gx + gw * 0.08)} {f(gy + gh * 0.44)} L {f(gx + gw * 0.08)} {f(gy + gh * 0.56)}" stroke="#0B1A2E" stroke-width="4"></path>')
    o.append(plate_label(cx, gy + gh * 0.12, "THE PATTERN · SHOWED THEE IN THE MOUNT", GOLD, 9))
    o.append(halo(cx, cyy, gw * 0.6, "#8FD0E2", 0.15))
    o.append(ground(w, h, h * 0.9, "#2A2030", dy=0))
    b = h * 0.9
    s = fit(b, max(h * 0.4, b - 130))
    o.append(moses(p, w * 0.4, b, s, flip=True, up=[(-22, -158), (-34, -186), (-36, -214)]))
    return "".join(o)

def two_covenants(w, h):
    """If that first covenant had been faultless, then would no place have been sought for a second … Behold, the days come,
    saith the Lord, that I will make a new covenant: a plate in two halves — at the left the two tables of stone, grey, THE
    FIRST COVENANT · THEY CONTINUED NOT IN MY COVENANT; at the right the heart with the writing on it in light, A NEW
    COVENANT · UPON BETTER PROMISES."""
    from co2.art import tablets, heart
    o = [plate_bg(w, h, "HEBREWS 8:6–8 · THE MEDIATOR OF A BETTER COVENANT")]
    k = min(w / 700, (h - 30) / 240)
    o.append(tablets(w * 0.26, h * 0.54, k * 0.9, op=0.6) + heart(w * 0.74, h * 0.52, 62 * k, writing=True, glow_=True))
    o.append(label(w * 0.26, h - 18, "THE FIRST COVENANT · NOT FAULTLESS", CY, 10) + label(w * 0.74, h - 18, "A NEW COVENANT · BETTER PROMISES", GOLD, 10))
    o.append(f'<path d="M{f(w * 0.42)} {f(h * 0.54)} L {f(w * 0.58)} {f(h * 0.54)}" stroke="{GOLD}" stroke-width="2.4"></path><path d="M{f(w * 0.57)} {f(h * 0.54 - 7)} L {f(w * 0.59)} {f(h * 0.54)} L {f(w * 0.57)} {f(h * 0.54 + 7)}" fill="none" stroke="{GOLD}" stroke-width="2.4"></path>')
    return "".join(o)

def out_of_egypt(p, w, h, seed):
    """In the day that I took them by the hand to lead them forth out of the land of Egypt: the children of Israel walking upon
    dry land in the midst of the sea between the walls of water (Exodus' drawing)."""
    from exo.art4 import dry_walk
    return mk.defs(p, *ALL) + dry_walk(p, w, h, seed)

def laws_heart(w, h):
    """I will put my laws into their mind, and on their heart also will I write them: and I will be to them a God, and they
    shall be to me a people: the heart with the writing on it in light, a man's head in outline with the same rows of writing
    in it (a plate)."""
    from co2.art import heart
    o = [plate_bg(w, h, "HEBREWS 8:10 · INTO THEIR MIND · ON THEIR HEART")]
    k = min(w / 700, (h - 30) / 240)
    hx, hy = w * 0.3, h * 0.56                                                # a head in profile, outline, rows of writing in it
    o.append(f'<path d="M{f(hx - 50 * k)} {f(hy + 70 * k)} C {f(hx - 60 * k)} {f(hy + 20 * k)} {f(hx - 70 * k)} {f(hy - 50 * k)} {f(hx - 10 * k)} {f(hy - 70 * k)} C {f(hx + 40 * k)} {f(hy - 82 * k)} {f(hx + 70 * k)} {f(hy - 40 * k)} {f(hx + 62 * k)} {f(hy - 6 * k)} '
             f'L {f(hx + 76 * k)} {f(hy + 16 * k)} L {f(hx + 62 * k)} {f(hy + 22 * k)} C {f(hx + 64 * k)} {f(hy + 40 * k)} {f(hx + 50 * k)} {f(hy + 50 * k)} {f(hx + 30 * k)} {f(hy + 48 * k)} L {f(hx + 26 * k)} {f(hy + 70 * k)}" fill="none" stroke="{CY}" stroke-width="2.4"></path>')
    for i in range(5):
        y = hy - 46 * k + i * 12 * k
        o.append(f'<path d="M{f(hx - 40 * k)} {f(y)} L {f(hx + 30 * k)} {f(y)}" stroke="{GOLD}" stroke-width="2" stroke-dasharray="7 3"></path>')
    o.append(heart(w * 0.7, h * 0.52, 62 * k, writing=True, glow_=True))
    o.append(label(w * 0.3, h - 16, "INTO THEIR MIND", CY, 10) + label(w * 0.7, h - 16, "ON THEIR HEART", GOLD, 10))
    return "".join(o)

def least_greatest(p, w, h, seed):
    """All shall know me, from the least to the greatest of them: a company in the morning light, from a child at the left to an
    old man with a staff at the right, men and women, all turned toward the light."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#3A3A7A", "#FFE6C0"), halo(w * 0.5, h * 0.2, h * 0.5, "#FFF4C2", 0.6), hills(w, h, h * 0.6, seed, color="#8A7A6A", amp=10, step=90),
         ground(w, h, h * 0.68, "#B8A07A", dy=0)]
    s = fit(b, max(h * 0.25, b - 220))
    looks = [(0.08, 0.6, 0), (0.18, 0.78, 3), (0.3, 0.94, 1), (0.42, 0.92, 5), (0.54, 1.0, 2), (0.66, 0.94, 4), (0.78, 0.98, 0), (0.9, 1.0, 1)]
    for x, sc, i in looks:
        if sc < 0.7: o.append(robed(p, w * x, b, s * sc, "#C8A060", hair="#2A1A10", belt="#6A4A2A", flip=True))
        elif x > 0.86: o.append(robed(p, w * x, b, s * sc, "#8A8478", head="#F3EFE6", cord="#6A5A3A", beard="#F3EFE6", flip=True))
        else:
            from heb.art import brother_fig
            o.append(brother_fig(p, w * x, b, s * sc, i, flip=True))
    return "".join(o)
