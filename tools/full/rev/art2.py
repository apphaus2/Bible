"""Drawings for Revelation 4–7 (chapter 2 of the volume): the throne in heaven, the Lamb, the seals, the sealed and the great
multitude. God is never drawn: the throne is empty, in light, with the rainbow like an emerald, the sea of glass, the seven
lamps, the lightnings. The four living creatures are heraldic medallions of light (a lion, a calf, a man's face, a flying
eagle, six wings, full of eyes); the twenty-four elders robed in white with crowns of gold on thrones in a ring; the Lamb an
emblem of light, standing, seven horns and seven eyes, no wound drawn.

    door_heaven(p, w, h, seed)            a door opened in heaven over the sea at night, John on the rock of Patmos
    throne_room(p, w, h, seed, elders=, lamb=, angels=, bowls=, book=, lightning=)   the throne room in perspective
    throne_plan(w, h)                     the throne room as a technical plate (plan), every part named
    creatures(w, h, which=None)           the four living creatures as heraldic medallions (one, or all four in a row)
    sealed_book(w, h, seed, loosed=0)     the book written within and on the back, close sealed with seven seals, in light
    elder_fig(p, x, b, s, pose=, harp=, bowl=)   an elder: white robe, white hair and beard, a crown of gold
    lamb(x, b, s, glow=)                  the Lamb, an emblem of light
    elder_john(p, w, h, seed)             one of the elders speaking to John, who weeps (5:4–5; 7:13–14)
    every_creature(p, w, h, seed)         every created thing in heaven, on the earth and on the sea, under the light
    horse_rider(x, b, s, color, rider)    a horse and its rider far off · horsemen(p, w, h, seed, which) the horse on the horizon
    souls_altar(p, w, h, seed)            the souls underneath the altar: white robes in light under the golden altar
    sixth_seal(w, h, seed)                the sun black as sackcloth, the moon as blood, the stars falling, the heaven rolled up
    caves(p, w, h, seed)                  the mountains and their caves, small figures hiding in them
    four_winds(p, w, h, seed)             four angels at the four corners holding the winds; another from the sunrising
    tribes_plate(w, h)                    the hundred and forty and four thousand: twelve tribes, twelve thousand each
    multitude(p, w, h, seed, stage=)      the great multitude in white robes with palms before the throne ("palms";
                                          "fountains" — the Lamb leading them to fountains of waters of life)"""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from rev.art import *
from rev.art import f, INK, GOLD, GOLD_L, WHITE
import exodus as E, exodus3 as E3
from oba.minor import bolt, grain, eagle
from dan.art4 import wing, lion_walk
from ezk.art import eye
from exo.art8 import dim
from epistle import plate_bg

EMERALD = "#2E9A5A"

# ---- the figures of heaven --------------------------------------------------------------------------------------------
CROWN = ('<path d="M-13 -197 L -14 -209 L -7 -202 L 0 -213 L 7 -202 L 14 -209 L 13 -197 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>')
UP_HARP = [(-22, -158), (-40, -140), (-50, -122)]

def harp(x, y, s=1.0):
    """A small lyre (in the figure's units when used as an extra)."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-12 0 C -16 -16 -14 -30 -10 -40 L -6 -38 C -9 -28 -9 -16 -6 -4 L 6 -4 C 9 -16 9 -28 6 -38 L 10 -40 C 14 -30 16 -16 12 0 Z" '
            'fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path><path d="M-9 -34 L 9 -34" stroke="#C8962E" stroke-width="3"></path>'
            + "".join(f'<path d="M{dx} -34 L {dx} -4" stroke="#F3EFE6" stroke-width="0.8"></path>' for dx in (-4, 0, 4)) + '</g>')

def gold_bowl(x, y, s=1.0, smoke=True):
    o = (f'<path d="M{f(x - 12 * s)} {f(y)} C {f(x - 10 * s)} {f(y + 9 * s)} {f(x + 10 * s)} {f(y + 9 * s)} {f(x + 12 * s)} {f(y)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="{f(max(1, 1.4 * s))}"></path>')
    if smoke: o += f'<path d="M{f(x)} {f(y - 2 * s)} C {f(x - 6 * s)} {f(y - 12 * s)} {f(x + 6 * s)} {f(y - 20 * s)} {f(x)} {f(y - 30 * s)}" fill="none" stroke="#E8E2F0" stroke-width="{f(3 * s)}" opacity="0.7"></path>'
    return o

def elder_fig(p, x, b, s, pose="sit", harp_=False, bowl=False, flip=False, crown=True):
    """One of the four and twenty elders: arrayed in white garments, white hair and beard, a crown of gold on his head
    (4:4). pose "sit" (on his throne, which the drawing supplies: elder_throne), "stand", "bow" (fallen down, kneeling low,
    the crown cast before him — drawn by elder_bow)."""
    ex = CROWN if crown else ""
    if harp_: ex += harp(-50, -112, 0.9)
    if bowl: ex += gold_bowl(-52, -118, 1.0)
    up = UP_HARP if (harp_ or bowl) else None
    return robed(p, x, b, s, "#FAF8F0", hair="#EEECE6", beard="#EEECE6", up=up, flip=flip, pose=pose, seat=None, line="#3A3A4A", extra=ex)

def elder_throne(x, b, s, color="#E8D8A0"):
    """An elder's throne (its seat SEAT_Y·s up, as epistle.robed sits)."""
    t = b - 50 * s
    return (f'<rect x="{f(x - 30 * s)}" y="{f(t - 80 * s)}" width="{f(60 * s)}" height="{f(80 * s + 4 * s)}" rx="{f(6 * s)}" fill="{color}" stroke="#8A7A4A" stroke-width="{f(max(1, 2 * s))}"></rect>'
            f'<rect x="{f(x - 34 * s)}" y="{f(t)}" width="{f(68 * s)}" height="{f(50 * s)}" fill="{color}" stroke="#8A7A4A" stroke-width="{f(max(1, 2 * s))}"></rect>')

def elder_bow(x, b, s, flip=False, crown_cast=True, robe="#FAF8F0", legs="#F0EDE2", hair="#EEECE6", skin="#C98E66"):
    """An elder fallen down before the throne: kneeling low, bowed to the floor, white robe, white hair; his crown of gold
    cast before him (4:10)."""
    sx = -s if flip else s
    L = "#3A3A4A"
    o = (f'<g transform="translate({f(x)} {f(b)}) scale({f(sx)} {f(s)})">'
         # the legs folded under him: the shin flat on the floor, the thigh rising to the hips resting on the heels
         f'<path d="M48 0 L -6 0 C -14 0 -16 -10 -10 -16 L 18 -46 C 30 -56 50 -50 54 -36 C 56 -24 54 -10 48 0 Z" fill="{legs}" stroke="{L}" stroke-width="2.6" stroke-linejoin="round"></path>'
         f'<path d="M-6 -12 C 10 -20 26 -24 46 -22" fill="none" stroke="{L}" stroke-width="1.3" opacity="0.6"></path>'
         f'<path d="M50 -4 C 56 -4 60 -2 60 0 L 46 0 Z" fill="{skin}" stroke="{L}" stroke-width="1.2"></path>'
         # the back bowed forward from the hips to the shoulders, the head down near the floor
         f'<path d="M48 -38 C 46 -60 24 -74 -2 -72 C -24 -70 -40 -58 -46 -44 L -38 -30 C -26 -38 -6 -44 18 -42 Z" fill="{robe}" stroke="{L}" stroke-width="2.6" stroke-linejoin="round"></path>'
         f'<path d="M30 -60 C 14 -64 -6 -62 -22 -54" fill="none" stroke="{L}" stroke-width="1.2" opacity="0.5"></path>'
         f'<circle cx="-54" cy="-30" r="12" fill="{skin}" stroke="{L}" stroke-width="2"></circle>'
         f'<path d="M-44 -38 C -48 -46 -62 -46 -66 -36 C -67 -30 -64 -24 -60 -22 L -48 -26 Z" fill="{hair}" stroke="{L}" stroke-width="1.4"></path>'
         f'<path d="M-64 -24 C -70 -16 -70 -8 -66 -4 L -56 -18 Z" fill="{hair}" stroke="{L}" stroke-width="1.2"></path>'
         # the arm stretched to the floor in its white sleeve, the hand flat before him
         f'<path d="M-30 -52 C -46 -40 -60 -20 -72 -6" fill="none" stroke="{L}" stroke-width="13" stroke-linecap="round"></path>'
         f'<path d="M-30 -52 C -46 -40 -60 -20 -72 -6" fill="none" stroke="{robe}" stroke-width="10" stroke-linecap="round"></path>'
         f'<ellipse cx="-80" cy="-3" rx="8" ry="3.6" fill="{skin}" stroke="{L}" stroke-width="1.2"></ellipse>')
    if crown_cast: o += '<path d="M-112 0 L -113 -13 L -106 -7 L -99 -17 L -92 -7 L -85 -13 L -86 0 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>'
    return o + '</g>'

def lamb(x, b, s=1.0, glow=True, flip=False):
    """The Lamb standing (5:6): an emblem of light — a white lamb with seven golden horns and seven eyes set as a diadem of
    light above them, which are the seven Spirits of God. No wound is drawn."""
    sx = -s if flip else s
    o = halo(x, b - 60 * s, 110 * s, WHITE, 0.8) + rays(x, b - 60 * s, 20, 50 * s, 150 * s, "#FFFDF0", 0.4, max(1.5, 3 * s)) if glow else ""
    o += (f'<g transform="translate({f(x)} {f(b)}) scale({f(sx)} {f(s)})">'
          '<path d="M-44 -6 L -42 -30 C -60 -34 -64 -58 -46 -66 C -40 -80 -16 -84 -2 -76 C 10 -84 30 -80 34 -66 L 40 -64 L 40 -30 L 36 -6 L 28 -6 L 26 -26 L -26 -26 L -30 -6 Z" '
          'fill="#FFFFFF" stroke="#C8962E" stroke-width="2.6" stroke-linejoin="round"></path>'
          + "".join(f'<path d="M{dx} -44 c -6 2 -8 8 -4 12" fill="none" stroke="#E8DCC0" stroke-width="2"></path>' for dx in (-30, -16, -2, 12, 24))
          + '<path d="M34 -66 C 44 -82 64 -84 72 -72 C 78 -62 74 -50 64 -48 C 56 -46 46 -50 40 -56 Z" fill="#FFFFFF" stroke="#C8962E" stroke-width="2.6"></path>'
          '<path d="M44 -74 C 38 -80 32 -78 30 -72 C 34 -70 40 -70 44 -74 Z" fill="#F3EEE0" stroke="#C8962E" stroke-width="1.6"></path>'
          '<circle cx="64" cy="-66" r="2.6" fill="#3A2A1A"></circle>')
    for i in range(7):                                       # the seven horns, a crown of gold points
        a = math.radians(-160 + i * 22); hx, hy = 58 + 16 * math.cos(a), -78 + 12 * math.sin(a)
        o += f'<path d="M{f(hx - 2.6)} {f(hy)} L {f(hx + 8 * math.cos(a))} {f(hy - 14 + 4 * math.sin(a))} L {f(hx + 2.6)} {f(hy)} Z" fill="#FFD23F" stroke="#C8962E" stroke-width="1.2"></path>'
    for i in range(7):                                       # the seven eyes, a diadem of light above
        a = math.radians(-170 + i * 26.6); ex, ey = 58 + 34 * math.cos(a), -84 + 26 * math.sin(a)
        o += (f'<circle cx="{f(ex)}" cy="{f(ey)}" r="6.5" fill="#FFF4C2" opacity="0.7"></circle>'
              f'<path d="M{f(ex - 5)} {f(ey)} Q {f(ex)} {f(ey - 4)} {f(ex + 5)} {f(ey)} Q {f(ex)} {f(ey + 4)} {f(ex - 5)} {f(ey)} Z" fill="#FFFFFF" stroke="#C8962E" stroke-width="1"></path>'
              f'<circle cx="{f(ex)}" cy="{f(ey)}" r="1.6" fill="#3A5A8A"></circle>')
    return o + '</g>'

def calf(x, y, s, color="#C8783A"):
    """A calf (ox) in profile, heraldic."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-56 0 L -54 -26 C -66 -34 -64 -58 -44 -62 L 30 -64 C 40 -76 58 -78 66 -66 L 76 -50 C 78 -44 72 -40 66 -42 '
            'L 60 -44 L 52 -34 L 50 -26 L 50 0 L 40 0 L 38 -22 L -30 -22 L -34 0 L -44 0 L -46 -20 L -48 0 Z" fill="' + color + '" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>'
            '<path d="M40 -72 C 36 -84 40 -90 46 -92 C 44 -84 46 -78 48 -74 Z M58 -76 C 60 -88 66 -92 72 -90 C 68 -84 66 -80 64 -74 Z" fill="#F3E8C8" stroke="#0D0D0F" stroke-width="1.4"></path>'
            '<circle cx="58" cy="-62" r="2.4" fill="#0D0D0F"></circle><path d="M-56 -26 C -66 -20 -70 -8 -68 4" fill="none" stroke="#0D0D0F" stroke-width="2"></path></g>')

def man_face(x, y, s, color="#E8B830"):
    """A man's face in profile, struck as on a coin (the third creature)."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-30 40 C -34 10 -40 -20 -26 -44 C -10 -66 26 -64 36 -40 C 40 -30 40 -20 38 -12 L 48 6 '
            'C 50 10 46 12 42 12 L 42 18 C 44 22 40 24 36 24 L 34 32 C 30 40 18 40 8 38 L 6 50 Z" fill="' + color + '" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>'
            '<path d="M-26 -44 C -14 -60 20 -62 32 -44 C 20 -48 -6 -46 -18 -30 C -22 -20 -24 -8 -22 4 C -32 -10 -34 -30 -26 -44 Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M18 -10 C 22 -14 28 -14 31 -10" fill="none" stroke="#0D0D0F" stroke-width="2"></path><circle cx="25" cy="-6" r="2" fill="#0D0D0F"></circle></g>')

def six_wings(x, y, s, color="#F3E8C8"):
    """Six wings behind a creature: three pairs, spread up, out and down, full of eyes."""
    o = []
    for rot, k in ((-40, 1.0), (10, 0.9), (60, 0.8)):
        o.append(wing(x - 4 * s, y, s * k, color=color, flip=True, rot=-rot) + wing(x + 4 * s, y, s * k, color=color, rot=rot))
    r = random.Random(int(x))
    for _ in range(14):
        a = r.uniform(-math.pi, 0.4); d = r.uniform(40, 90) * s
        o.append(eye(x + d * math.cos(a) * (1 if r.random() < 0.5 else -1), y + d * math.sin(a) * 0.9, 4.5 * s))
    return "".join(o)

def creature(cx, cy, r, which):
    """One living creature as a heraldic medallion of light: six wings behind, full of eyes, the beast in gold."""
    s = r / 80
    o = [halo(cx, cy, r * 1.5, "#FFF4C2", 0.55), six_wings(cx, cy, s * 0.95),
         f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r * 0.72)}" fill="#12113A" stroke="#E8B830" stroke-width="{f(max(2, 3 * s))}"></circle>']
    if which == 0: o.append(lion_walk(cx - 8 * s, cy + 26 * s, s * 0.62, color="#E8B830"))
    elif which == 1: o.append(calf(cx - 6 * s, cy + 26 * s, s * 0.6, color="#E8A040"))
    elif which == 2: o.append(man_face(cx - 4 * s, cy - 2 * s, s * 0.8))
    else: o.append(eagle(cx, cy, s * 0.48, color="#E8B830"))
    for k in range(10):
        a = k * math.pi / 5
        o.append(eye(cx + r * 0.62 * math.cos(a), cy + r * 0.62 * math.sin(a), 3.4 * s))
    return "".join(o)

NAMES4 = ["LIKE A LION", "LIKE A CALF", "A FACE AS OF A MAN", "LIKE A FLYING EAGLE"]

def creatures(w, h, which=None, seed=4):
    """The four living creatures as heraldic medallions on a dark field, each named (4:7): which= one of them, else all four."""
    from dan.art4 import field
    o = [field(w, h, seed)]
    ks = [which] if which is not None else range(4)
    n = len(ks); r = min(h * 0.24, w / n * 0.26)
    for i, k in enumerate(ks):
        x = w * (i + 0.5) / n
        t = ("I", "II", "III", "IV")[k] + " · " + NAMES4[k]
        o.append(creature(x, h * 0.42, r, k) + label(x, h * 0.42 + r * 1.55, t, "#FFD23F", max(7, min(10, h / 26, (w / n - 12) / (len(t) * 0.76)))))
    o.append(label(w * 0.5, h * 0.09, "SIX WINGS · FULL OF EYES ROUND ABOUT AND WITHIN", "#8FD0E2", max(8, min(10, h / 26))))
    return "".join(o)

# ---- the throne room ----------------------------------------------------------------------------------------------------
def rainbow(cx, cy, rx, ry, sw):
    return "".join(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx - k * sw * 0.8)}" ry="{f(ry - k * sw * 0.8)}" fill="none" stroke="{c}" stroke-width="{f(sw)}" opacity="0.8"></ellipse>'
                   for k, c in enumerate((EMERALD, "#5AC88A", "#9CE8B8")))

def empty_throne(cx, b, s):
    """The throne set in heaven (4:2): a high throne of white and gold, empty, light pouring from it (God is never drawn)."""
    o = [halo(cx, b - 100 * s, 150 * s, WHITE, 0.95)]
    for k in range(3):
        o.append(f'<rect x="{f(cx - (70 - k * 14) * s)}" y="{f(b - (k + 1) * 11 * s)}" width="{f((140 - k * 28) * s)}" height="{f(11 * s)}" fill="#FFF4C2" stroke="#C8962E" stroke-width="{f(max(1, 1.8 * s))}"></rect>')
    y0 = b - 33 * s
    o.append(f'<path d="M{f(cx - 36 * s)} {f(y0)} L {f(cx - 36 * s)} {f(y0 - 130 * s)} C {f(cx - 32 * s)} {f(y0 - 152 * s)} {f(cx + 32 * s)} {f(y0 - 152 * s)} {f(cx + 36 * s)} {f(y0 - 130 * s)} L {f(cx + 36 * s)} {f(y0)} Z" '
             f'fill="#FFF8DC" stroke="#C8962E" stroke-width="{f(max(1.4, 2.6 * s))}"></path>'
             f'<rect x="{f(cx - 46 * s)}" y="{f(y0 - 52 * s)}" width="{f(92 * s)}" height="{f(13 * s)}" fill="#FFE680" stroke="#C8962E" stroke-width="{f(max(1, 2 * s))}"></rect>'
             + "".join(f'<rect x="{f(cx + d * 42 * s - 6 * s)}" y="{f(y0 - 82 * s)}" width="{f(12 * s)}" height="{f(82 * s)}" fill="#FFE680" stroke="#C8962E" stroke-width="{f(max(1, 2 * s))}"></rect>' for d in (-1, 1)))
    o.append(halo(cx, y0 - 80 * s, 80 * s, WHITE, 0.95))
    return "".join(o)

def seven_lamps(x0, x1, y, s):
    """The seven lamps of fire burning before the throne (4:5)."""
    o = []
    for i in range(7):
        x = x0 + (x1 - x0) * i / 6
        o.append(halo(x, y - 16 * s, 22 * s, "#FFB02E", 0.5)
                 + f'<path d="M{f(x - 8 * s)} {f(y)} L {f(x + 8 * s)} {f(y)} L {f(x + 5 * s)} {f(y - 6 * s)} L {f(x - 5 * s)} {f(y - 6 * s)} Z" fill="#E8B830" stroke="{INK}" stroke-width="1.2"></path>'
                 + f'<path d="M{f(x)} {f(y - 30 * s)} C {f(x + 8 * s)} {f(y - 18 * s)} {f(x + 6 * s)} {f(y - 8 * s)} {f(x)} {f(y - 6 * s)} C {f(x - 6 * s)} {f(y - 8 * s)} {f(x - 8 * s)} {f(y - 18 * s)} {f(x)} {f(y - 30 * s)} Z" fill="#FF8A2E" stroke="#C8401A" stroke-width="1"></path>')
    return "".join(o)

def throne_room(p, w, h, seed, elders="sit", lamb_=False, angels=0, bowls=False, book=False, lightning=True, creatures_=True, crowns=False, glory=False):
    """The throne room of 4–5 in perspective: the throne empty in light at the back with the emerald rainbow round about it,
    lightnings from it, the seven lamps before it, the sea of glass like crystal in front, the four living creatures (gold
    medallions of light) beside it, and the four and twenty elders on their thrones in a ring. elders "sit" / "bow" (fallen
    down, crowns cast: crowns=True) / "harps" (standing, harps and golden bowls of incense) / None; lamb_= the Lamb
    standing before the throne; angels= rings of angels round about; book= the sealed book on the throne in light."""
    r = random.Random(seed)
    o = [defs(p), sky(w, h, "#0B0B2A", "#3A2A6A"), starfield(w, h, seed, 60, 0.5)]
    cx, cy = w * 0.5, h * 0.5
    ts = min(h * 0.5 / 180, w * 0.25 / 140)
    tb = h * 0.56
    o.append(halo(cx, tb - 90 * ts, max(w, h) * 0.55, "#FFF4C2", 0.6) + rays(cx, tb - 90 * ts, 40, 60 * ts, max(w, h), "#FFFDF0", 0.25, 4))
    if angels:
        for ring in range(angels):
            n = 26 + ring * 8; rx, ry = w * (0.47 + ring * 0.05), h * (0.42 + ring * 0.04)
            for i in range(n):
                a = math.pi + math.pi * (i + 0.5) / n
                x, y = cx + rx * math.cos(a), h * 0.52 + ry * math.sin(a)
                o.append(angel(p, x, y + h * 0.05, h * 0.11 / 205, glow=False, flip=x > cx, line="#C8962E",
                               up=[(-22, -158), (-34, -178), (-40, -198)] if i % 3 == 0 else None))
    o.append(rainbow(cx, tb - 80 * ts, 130 * ts, 120 * ts, 9 * ts))
    if lightning:
        for i in range(4):
            x = cx + (-1 if i % 2 else 1) * (60 + 40 * i) * ts
            o.append(bolt(x, tb - 220 * ts, tb - 120 * ts, seed + i, sw=2.6))
    o.append(empty_throne(cx, tb, ts))
    if book: o.append(sealed_scroll(cx, tb - 70 * ts, 0.9 * ts))
    o.append(seven_lamps(cx - 110 * ts, cx + 110 * ts, tb + 14 * ts, ts * 0.8))
    # the sea of glass
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(h * 0.8)}" rx="{f(w * 0.3)}" ry="{f(h * 0.1)}" fill="#C8ECF8" stroke="#8FD0E2" stroke-width="2.4" opacity="0.9"></ellipse>'
             f'<ellipse cx="{f(cx - w * 0.08)}" cy="{f(h * 0.78)}" rx="{f(w * 0.1)}" ry="{f(h * 0.025)}" fill="#FFFFFF" opacity="0.7"></ellipse>')
    if creatures_:
        for k, (dx, dy) in enumerate(((-0.24, -0.08), (0.24, -0.08), (-0.18, 0.12), (0.18, 0.12))):
            o.append(creature(cx + w * dx, tb + h * dy - 40 * ts, 34 * ts, k))
    if lamb_:
        o.append(lamb(cx - 30 * ts, tb + 60 * ts, ts * 0.75))
    # the four and twenty elders in a ring (the back half behind the throne's light, the front half before the sea)
    if elders:
        rx, ry, ecy = w * 0.44, h * 0.3, h * 0.6
        pos = []
        for i in range(24):
            a = 2 * math.pi * (i + 0.5) / 24
            x, y = cx + rx * math.cos(a), ecy + ry * math.sin(a)
            if abs(x - cx) < w * 0.16 and y < ecy + ry * 0.2: continue       # not in front of the throne itself
            if abs(x - cx) < w * 0.3 and y > ecy + ry * 0.55: continue       # nor over the sea of glass
            pos.append((y, x, a))
        pos.sort()
        es = min(h * 0.2 / 157, 0.4)
        for y, x, a in pos:
            k = es * (0.75 + 0.25 * (y - (ecy - ry)) / (2 * ry))
            fl = x > cx
            if elders == "bow":
                o.append(elder_bow(x, y + 40 * k, k * 1.45, flip=not fl, crown_cast=crowns))
            elif elders == "harps":
                o.append(elder_fig(p, x, y + 40 * k, k * 1.05, pose="stand", harp_=bool(r.random() < 0.5), bowl=True, flip=fl))
            else:
                o.append(elder_throne(x, y + 40 * k, k) + elder_fig(p, x, y + 40 * k, k, pose="sit", flip=not fl))
    return "".join(o)

def sealed_scroll(cx, cy, s, loosed=0):
    """A book (a roll) written within and on the back, close sealed with seven seals (5:1); loosed= how many are broken."""
    o = [f'<rect x="{f(cx - 60 * s)}" y="{f(cy - 14 * s)}" width="{f(120 * s)}" height="{f(28 * s)}" rx="{f(12 * s)}" fill="#F3E8C8" stroke="{INK}" stroke-width="{f(max(1.2, 2 * s))}"></rect>']
    for k in range(4):
        o.append(f'<path d="M{f(cx - 50 * s)} {f(cy - 8 * s + k * 5 * s)} L {f(cx + 50 * s)} {f(cy - 8 * s + k * 5 * s)}" stroke="#8A7A5A" stroke-width="{f(max(0.6, s))}" stroke-dasharray="{f(6 * s)} {f(2 * s)}"></path>')
    for i in range(7):
        x = cx - 48 * s + i * 16 * s
        col = "#5A3A3A" if i < loosed else "#B5121B"
        o.append(f'<path d="M{f(x)} {f(cy - 16 * s)} L {f(x)} {f(cy + 16 * s)}" stroke="#8A5A30" stroke-width="{f(max(0.8, 1.6 * s))}"></path>'
                 f'<circle cx="{f(x)}" cy="{f(cy + 14 * s)}" r="{f(6 * s)}" fill="{col}" stroke="{INK}" stroke-width="{f(max(0.8, 1.2 * s))}"></circle>')
    return "".join(o)

def sealed_book(w, h, seed, loosed=0):
    """The book close sealed with seven seals, lying in the light upon the throne (5:1) — no hand is drawn."""
    o = [sky(w, h, "#1A1440", "#5A4A8A"), radiance(w, h, seed, cy=0.55)]
    s = min(w * 0.7 / 120, h * 0.5 / 40)
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.62)}" rx="{f(70 * s)}" ry="{f(10 * s)}" fill="#FFF4C2" opacity="0.6"></ellipse>')
    o.append(sealed_scroll(w * 0.5, h * 0.5, s, loosed))
    o.append(label(w * 0.5, h * 0.9, "WRITTEN WITHIN AND ON THE BACK · CLOSE SEALED WITH SEVEN SEALS", "#FFF4C2", max(8, min(10, h / 24))))
    return "".join(o)

def throne_plan(w, h):
    """The throne in heaven as a technical plate, seen from above (4:2–8): the throne at the centre (empty, light), the
    rainbow round about it, the four living creatures, the seven lamps of fire before it, the sea of glass, and the four and
    twenty thrones of the elders in a ring; every part named."""
    import exo.art8 as B
    o = [plate_bg(w, h, "THE THRONE SET IN HEAVEN · PLAN")]
    B._W[0] = w
    cx, cy = w * 0.42, h * 0.54
    R = min(h * 0.38, w * 0.3)
    for i in range(24):
        a = 2 * math.pi * i / 24
        x, y = cx + R * math.cos(a), cy + R * 0.92 * math.sin(a)
        o.append(f'<rect x="{f(x - 7)}" y="{f(y - 7)}" width="14" height="14" fill="#E8D8A0" stroke="#FFD23F" stroke-width="1.2" transform="rotate({f(math.degrees(a))} {f(x)} {f(y)})"></rect>'
                 f'<circle cx="{f(x)}" cy="{f(y)}" r="3" fill="#E8B830"></circle>')
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R * 0.42)}" fill="none" stroke="{EMERALD}" stroke-width="6" opacity="0.85"></circle>')
    o.append(halo(cx, cy, R * 0.3, "#FFF4C2", 0.8) + f'<rect x="{f(cx - 12)}" y="{f(cy - 12)}" width="24" height="24" fill="#FFF8DC" stroke="#FFD23F" stroke-width="2"></rect>')
    for k, (dx, dy) in enumerate(((0, -1), (1, 0), (0, 1), (-1, 0))):
        x, y = cx + dx * R * 0.6, cy + dy * R * 0.55
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="9" fill="#12113A" stroke="#E8B830" stroke-width="2"></circle>' + label(x, y + 3.5, ("I", "II", "III", "IV")[k], "#FFD23F", 8))
    for i in range(7):
        x = cx - R * 0.32 + i * R * 0.64 / 6
        o.append(f'<circle cx="{f(x)}" cy="{f(cy + R * 0.32)}" r="3.2" fill="#FF8A2E" stroke="#FFD23F" stroke-width="1"></circle>')
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy + R * 0.76)}" rx="{f(R * 0.36)}" ry="{f(R * 0.12)}" fill="#8FD0E2" opacity="0.55" stroke="#C8ECF8" stroke-width="1.6"></ellipse>')
    tx = w * 0.64
    o.append(tag(cx + 10, cy - 8, "THE THRONE · ONE SITTING", tx, h * 0.16))
    o.append(tag(cx + R * 0.42, cy - R * 0.1, "A RAINBOW LIKE AN EMERALD", tx, h * 0.27))
    o.append(tag(cx + R * 0.6, cy, "FOUR LIVING CREATURES", tx, h * 0.38))
    o.append(tag(cx + R * 0.32, cy + R * 0.32, "SEVEN LAMPS OF FIRE", tx, h * 0.5))
    o.append(tag(cx + R * 0.3, cy + R * 0.78, "A SEA OF GLASS LIKE CRYSTAL", tx, h * 0.62))
    o.append(tag(cx + R * 0.97, cy + R * 0.2, "FOUR AND TWENTY THRONES", tx, h * 0.74))
    o.append(label(14, h - 12, "THE CREATURES · I LION · II CALF · III MAN · IV EAGLE", "#8FD0E2", 9, anchor="start"))
    return "".join(o)

def door_heaven(p, w, h, seed):
    """After these things I saw, and behold, a door opened in heaven (4:1): the night sky over the sea, a doorway of light
    standing open among the clouds, John on the rock of Patmos looking up."""
    hz = h * 0.72
    o = [defs(p), sky(w, h, "#05051A", "#2A2A5A"), starfield(w, h, seed, 70, 0.7)]
    dx, dy, dw, dh = w * 0.58, h * 0.08, w * 0.12, h * 0.42
    o.append(halo(dx + dw / 2, dy + dh / 2, h * 0.5, "#FFF4C2", 0.7) + rays(dx + dw / 2, dy + dh / 2, 30, dh * 0.4, w * 0.6, "#FFFDF0", 0.3, 4))
    for k in range(5):
        ex = dx + dw / 2 + (k - 2) * w * 0.1
        o.append(f'<ellipse cx="{f(ex)}" cy="{f(dy + dh + 6)}" rx="{f(w * 0.09)}" ry="{f(h * 0.04)}" fill="#C8C0D8" stroke="#8A80A8" stroke-width="1.6" opacity="0.9"></ellipse>')
    o.append(f'<rect x="{f(dx)}" y="{f(dy)}" width="{f(dw)}" height="{f(dh)}" fill="#FFFDF0" stroke="#E8B830" stroke-width="3"></rect>'
             f'<path d="M{f(dx)} {f(dy)} L {f(dx - dw * 0.5)} {f(dy + dh * 0.08)} L {f(dx - dw * 0.5)} {f(dy + dh * 0.94)} L {f(dx)} {f(dy + dh)} Z" fill="#C8962E" stroke="{INK}" stroke-width="2"></path>')
    o.append(sea(w, h, hz, seed, color="#1A3A5A", deep="#0B1A2E"))
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.78)} L {f(w * 0.12)} {f(h * 0.74)} L {f(w * 0.3)} {f(h * 0.82)} L {f(w * 0.38)} {f(h + 10)} Z" fill="#3A2A2A" stroke="{INK}" stroke-width="2.4"></path>')
    s = h * 0.3 / 205
    o.append(john_fig(p, w * 0.18, h * 0.78, s, flip=True, up=[(-22, -158), (-36, -180), (-44, -204)]))
    return "".join(o)

def elder_john(p, w, h, seed, weep=False):
    """One of the elders speaking to John (5:5; 7:13–14): the elder standing in white with his crown of gold, his hand out,
    John before him (weeping, 5:4), the light of the throne behind them."""
    o = [defs(p), sky(w, h, "#1A1440", "#5A4A8A"), halo(w * 0.7, h * 0.3, w * 0.5, "#FFF4C2", 0.6), rays(w * 0.7, h * 0.3, 24, h * 0.1, w, "#FFFDF0", 0.25, 4)]
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.96)}" rx="{f(w * 0.48)}" ry="{f(h * 0.08)}" fill="#C8ECF8" opacity="0.5"></ellipse>')
    s = h * 0.82 / 205
    o.append(robed(p, w * 0.38, h * 0.98, s, "#FAF8F0", hair="#EEECE6", beard="#EEECE6", up=[(-22, -158), (-46, -150), (-60, -140)], flip=True, line="#3A3A4A", extra=CROWN))
    o.append(john_fig(p, w * 0.62, h * 0.98, s * 0.96, flip=False,
                      up=[(-22, -158), (-14, -172), (-6, -184)] if weep else None))
    return "".join(o)

def every_creature(p, w, h, seed):
    """Every created thing which is in the heaven, and on the earth, and under the earth, and on the sea (5:13): the light
    above, birds in the sky, the hills with their flocks and herds and people, the sea with its ships and fishes."""
    r = random.Random(seed)
    o = [defs(p), sky(w, h, "#3A3A8A", "#FFE6A0"), halo(w * 0.5, h * 0.05, w * 0.5, WHITE, 0.8), rays(w * 0.5, h * 0.02, 30, h * 0.06, w * 0.8, "#FFFDF0", 0.35, 4)]
    o.append(birds(9, w * 0.1, w * 0.9, h * 0.12, h * 0.34, seed, 0.6, 1.2))
    hz = h * 0.58
    o.append(hills(w, h, hz - h * 0.06, seed, color="#6A9A5A", amp=14, step=90) + ground(w * 0.58, h, hz, "#8AB86A", dy=0))
    o.append(sea(w, h, hz + h * 0.02, seed, color="#2A7AA8", deep="#0F4C68"))
    o.append(f'<path d="M-10 {f(hz)} L {f(w * 0.56)} {f(hz)} C {f(w * 0.6)} {f(hz + h * 0.2)} {f(w * 0.56)} {f(h * 0.8)} {f(w * 0.5)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8AB86A" stroke="{INK}" stroke-width="2"></path>')
    o.append(E3.horse(w * 0.1, hz + h * 0.16, h / 1100, color="#8A5A30") + E.sheep(w * 0.2, hz + h * 0.14, h / 900) + E.sheep(w * 0.26, hz + h * 0.17, h / 960, flip=True))
    o.append(crowd(p, w * 0.06, w * 0.48, h * 0.98, h * 0.76, 7, seed, up=[(-22, -158), (-40, -176), (-52, -198)]))
    o.append(ship(w * 0.8, hz + h * 0.14, h / 700))
    for i in range(6):
        x, y = w * r.uniform(0.62, 0.96), h * r.uniform(0.76, 0.96)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x + 10)} {f(y - 6)} {f(x + 20)} {f(y - 6)} {f(x + 26)} {f(y)} C {f(x + 20)} {f(y + 6)} {f(x + 10)} {f(y + 6)} {f(x)} {f(y)} Z '
                 f'M{f(x)} {f(y)} L {f(x - 8)} {f(y - 6)} L {f(x - 8)} {f(y + 6)} Z" fill="#E8B830" stroke="{INK}" stroke-width="1.2"></path>')
    return "".join(o)

# ---- the seals ----------------------------------------------------------------------------------------------------------
HORSES = {"white": ("#F8F6F0", "#E8E2D6"), "red": ("#B5281E", "#7A1A14"), "black": ("#1A1418", "#3A3036"), "pale": ("#B8C8B0", "#8A9A88")}

def horse_rider(x, b, s, color, cloth, flip=False, item=None):
    """A horse and its rider, far off: exodus3's horse, the rider sitting astride (robe, head, an arm forward); item "bow",
    "crown", "balance" in the rider's hand (the sword is in the words only)."""
    sx = -s if flip else s
    rim = "#0D0D0F"
    o = E3.horse(x, b, s, color=color, flip=flip, rim=rim)
    o += (f'<g transform="translate({f(x)} {f(b)}) scale({f(sx)} {f(s)})">'
          f'<path d="M-14 -70 C -16 -56 -14 -44 -8 -36 L 8 -36 C 10 -48 8 -60 6 -70 Z" fill="{cloth}" stroke="{rim}" stroke-width="2"></path>'
          f'<path d="M-12 -68 C -14 -90 -10 -108 0 -114 C 10 -110 14 -92 12 -68 Z" fill="{cloth}" stroke="{rim}" stroke-width="2"></path>'
          f'<circle cx="2" cy="-122" r="9" fill="#C98E66" stroke="{rim}" stroke-width="2"></circle>'
          f'<path d="M4 -104 C 16 -100 26 -96 34 -92" fill="none" stroke="{rim}" stroke-width="7" stroke-linecap="round"></path>'
          f'<path d="M4 -104 C 16 -100 26 -96 34 -92" fill="none" stroke="{cloth}" stroke-width="4.5" stroke-linecap="round"></path>')
    if item == "bow":
        o += '<path d="M36 -118 C 50 -104 50 -80 36 -66" fill="none" stroke="#8A5A30" stroke-width="3"></path><path d="M36 -118 L 36 -66" stroke="#F3EFE6" stroke-width="1"></path>'
    if item in ("bow", "crown"):
        o += '<path d="M-7 -129 L -8 -137 L -3 -133 L 2 -140 L 7 -133 L 12 -137 L 11 -129 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></path>'
    if item == "balance":
        o += ('<path d="M36 -96 L 36 -110 M24 -108 L 48 -108" stroke="#C8B080" stroke-width="2"></path>'
              '<path d="M24 -108 L 20 -98 L 28 -98 Z M48 -108 L 44 -98 L 52 -98 Z" fill="#C8B080" stroke="#0D0D0F" stroke-width="1"></path>')
    return o + '</g>'

def horsemen(p, w, h, seed, which="white"):
    """A horse and his rider seen far off on the horizon, coming forth (6:2–8): the white horse at morning, the red at a
    red dusk, the black over the fields of wheat and barley, the pale over a grey and empty plain. Small, distant; what
    they do is in the words."""
    tones = {"white": ("#5AA8D8", "#F3E8C8", "#C8B080"), "red": ("#3A0A10", "#C84A2A", "#5A2A1E"), "black": ("#4A4A5A", "#C8B888", "#8A7A4A"),
             "pale": ("#2A2E36", "#8A9A98", "#5A605A")}
    top, bot, earth = tones[which]
    hz = h * 0.7
    o = [sky(w, h, top, bot)]
    if which == "white": o.append(halo(w * 0.8, h * 0.3, h * 0.4, "#FFF4C2", 0.6))
    if which == "red": o.append(halo(w * 0.3, hz, h * 0.5, "#FF6A2A", 0.5))
    o.append(hills(w, h, hz - h * 0.04, seed, color=earth, amp=10, step=90) + ground(w, h, hz, earth, dy=0))
    if which == "black":
        o.append(grain(-10, w * 0.5, h * 0.98, h * 0.18, seed, color="#C8A050") + grain(w * 0.5, w + 10, h * 0.98, h * 0.14, seed + 1, color="#A89060"))
    if which == "pale":
        o.append(birds(4, w * 0.1, w * 0.9, h * 0.1, h * 0.4, seed, 0.5, 0.9, color="#1A1A1E"))
    s = h * 0.4 / 140
    col, rider = HORSES[which][0], {"white": "#F3EFE6", "red": "#7A1A14", "black": "#2A2A2E", "pale": "#5A6058"}[which]
    item = {"white": "bow", "black": "balance"}.get(which)
    o.append(halo(w * 0.5, hz + h * 0.04 - 70 * s, 110 * s, "#FFFFFF" if which == "white" else bot, 0.35))
    o.append(horse_rider(w * 0.5, hz + h * 0.16, s, col, rider, flip=False, item=item))
    if which != "pale":
        dust = "#C8B080" if which != "red" else "#8A3A2A"
        o.append("".join(f'<ellipse cx="{f(w * 0.5 - 90 * s - k * 22 * s)}" cy="{f(hz + h * 0.15)}" rx="{f((14 + k * 6) * s)}" ry="{f((6 + k * 2) * s)}" fill="{dust}" opacity="{0.5 - k * 0.1:.2f}"></ellipse>' for k in range(4)))
    return "".join(o)

def altar_gold(cx, b, s):
    """The golden altar (of incense) with its four horns."""
    return (f'<rect x="{f(cx - 50 * s)}" y="{f(b - 70 * s)}" width="{f(100 * s)}" height="{f(70 * s)}" fill="#E8B830" stroke="{INK}" stroke-width="{f(max(1.4, 2.4 * s))}"></rect>'
            f'<rect x="{f(cx - 58 * s)}" y="{f(b - 80 * s)}" width="{f(116 * s)}" height="{f(12 * s)}" fill="#FFD23F" stroke="{INK}" stroke-width="{f(max(1.2, 2 * s))}"></rect>'
            + "".join(f'<path d="M{f(cx + d * 58 * s)} {f(b - 80 * s)} L {f(cx + d * 58 * s)} {f(b - 94 * s)} L {f(cx + d * 46 * s)} {f(b - 80 * s)} Z" fill="#FFD23F" stroke="{INK}" stroke-width="{f(max(1, 1.6 * s))}"></path>' for d in (-1, 1))
            + f'<rect x="{f(cx - 40 * s)}" y="{f(b - 60 * s)}" width="{f(80 * s)}" height="{f(50 * s)}" fill="none" stroke="#C8962E" stroke-width="{f(max(1, 1.6 * s))}"></rect>')

def souls_altar(p, w, h, seed, robes=False):
    """The souls of them that had been slain, underneath the altar (6:9–11): the golden altar high in light, and below it
    figures of white light in white robes, faceless, their hands lifted (robes=True: each given a white robe)."""
    o = [defs(p), sky(w, h, "#1A1440", "#5A4A8A"), halo(w * 0.5, h * 0.25, w * 0.5, "#FFF4C2", 0.7), rays(w * 0.5, h * 0.22, 28, h * 0.08, w * 0.9, "#FFFDF0", 0.3, 4)]
    s = h * 0.36 / 94
    o.append(f'<rect x="-10" y="{f(h * 0.46)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(altar_gold(w * 0.5, h * 0.46, s))
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.46 - 80 * s)} C {f(w * 0.46)} {f(h * 0.1)} {f(w * 0.56)} {f(h * 0.06)} {f(w * 0.5)} -10" fill="none" stroke="#E8E2F0" stroke-width="10" opacity="0.5"></path>')
    fs = h * 0.42 / 205
    n = 9
    for i in range(n):
        x = w * (0.08 + 0.84 * i / (n - 1))
        o.append(angel(p, x, h * 0.98, fs * (0.9 + 0.1 * (i % 2)), up=[(-22, -158), (-36, -180), (-44, -202)] if i % 2 == 0 else None, flip=i % 4 == 0, line="#C8B8D8"))
    return "".join(o)

def sixth_seal(w, h, seed):
    """The sixth seal (6:12–14): the sun black as sackcloth of hair, the whole moon as blood, the stars of the heaven falling
    unto the earth as unripe figs, the heaven rolled up as a scroll at its edge, the mountains broken and moved."""
    r = random.Random(seed)
    o = [sky(w, h, "#1A0A10", "#5A2A2A")]
    o.append(f'<path d="M{f(w * 0.86)} -10 C {f(w * 0.9)} {f(h * 0.2)} {f(w * 0.84)} {f(h * 0.4)} {f(w * 0.9)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} -10 Z" fill="#05050A"></path>'
             f'<path d="M{f(w * 0.86)} -10 C {f(w * 0.9)} {f(h * 0.2)} {f(w * 0.84)} {f(h * 0.4)} {f(w * 0.9)} {f(h * 0.6)}" fill="none" stroke="#C8B080" stroke-width="10" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.86)} -10 C {f(w * 0.9)} {f(h * 0.2)} {f(w * 0.84)} {f(h * 0.4)} {f(w * 0.9)} {f(h * 0.6)}" fill="none" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(f'<circle cx="{f(w * 0.22)}" cy="{f(h * 0.24)}" r="{f(h * 0.12)}" fill="#0D0B0E" stroke="#5A4A4A" stroke-width="3"></circle>'
             + "".join(f'<path d="M{f(w * 0.22 + h * 0.12 * math.cos(a))} {f(h * 0.24 + h * 0.12 * math.sin(a))} L {f(w * 0.22 + h * 0.16 * math.cos(a))} {f(h * 0.24 + h * 0.16 * math.sin(a))}" stroke="#3A2A2A" stroke-width="2"></path>'
                       for a in (k * math.pi / 8 for k in range(16))))
    o.append(halo(w * 0.62, h * 0.18, h * 0.12, "#8A0E16", 0.6) + f'<circle cx="{f(w * 0.62)}" cy="{f(h * 0.18)}" r="{f(h * 0.07)}" fill="#8A0E16" stroke="#3A0408" stroke-width="2"></circle>')
    for _ in range(14):
        x, y = r.uniform(0.05, 0.85) * w, r.uniform(0.05, 0.55) * h; ln = r.uniform(20, 46)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x - ln * 0.4)} {f(y - ln)}" stroke="#FFE6A0" stroke-width="2" opacity="0.6"></path>' + star(x, y, 4.5, "#FFF4C2", 0.8))
    hz = h * 0.66
    o.append(f'<path d="M-10 {f(hz)} L {f(w * 0.14)} {f(h * 0.42)} L {f(w * 0.26)} {f(h * 0.56)} L {f(w * 0.3)} {f(h * 0.5)} L {f(w * 0.44)} {f(hz)} Z" fill="#3A2A2E" stroke="{INK}" stroke-width="2.2" transform="rotate(-4 {f(w * 0.2)} {f(hz)})"></path>'
             f'<path d="M{f(w * 0.4)} {f(hz)} L {f(w * 0.58)} {f(h * 0.4)} L {f(w * 0.7)} {f(h * 0.52)} L {f(w * 0.82)} {f(hz)} Z" fill="#2E2226" stroke="{INK}" stroke-width="2.2" transform="rotate(5 {f(w * 0.6)} {f(hz)})"></path>')
    o.append(ground(w, h, hz, "#2A1A1A", dy=0))
    for k in range(5):
        x0 = w * r.uniform(0.05, 0.9)
        o.append(f'<path d="M{f(x0)} {f(hz + 4)} L {f(x0 + 14)} {f(hz + h * 0.1)} L {f(x0 + 4)} {f(hz + h * 0.18)} L {f(x0 + 20)} {f(h + 10)}" fill="none" stroke="#0D0D0F" stroke-width="3"></path>')
    return "".join(o)

def caves(p, w, h, seed):
    """The kings of the earth and every bondman and freeman hiding themselves in the caves and in the rocks of the
    mountains (6:15–16): a mountainside of caves under the dark sky, small figures crouched in their mouths (a king's
    crown among them)."""
    r = random.Random(seed)
    o = [defs(p), sky(w, h, "#1A0A10", "#4A2A2A")]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.3)} L {f(w * 0.2)} {f(h * 0.12)} L {f(w * 0.42)} {f(h * 0.2)} L {f(w * 0.62)} {f(h * 0.08)} L {f(w * 0.84)} {f(h * 0.22)} L {f(w + 10)} {f(h * 0.16)} L {f(w + 10)} {f(h + 10)} Z" fill="#5A4A44" stroke="{INK}" stroke-width="2.6"></path>')
    for k in range(6):
        y = h * (0.3 + 0.1 * k)
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 14)} {f(w * 0.6)} {f(y + 12)} {f(w + 10)} {f(y - 6)}" fill="none" stroke="#3A2E2A" stroke-width="2" opacity="0.6"></path>')
    s = h * 0.24 / 205
    spots = [(0.14, 0.5), (0.4, 0.42), (0.66, 0.5), (0.86, 0.44), (0.26, 0.82), (0.56, 0.84), (0.8, 0.86)]
    for i, (x, y) in enumerate(spots):
        cw, ch = w * 0.08, h * 0.16
        o.append(f'<path d="M{f(w * x - cw)} {f(h * y)} C {f(w * x - cw)} {f(h * y - ch * 1.3)} {f(w * x + cw)} {f(h * y - ch * 1.3)} {f(w * x + cw)} {f(h * y)} Z" fill="#120C0C" stroke="{INK}" stroke-width="2"></path>')
        cl = r.choice(["#6A4A3A", "#3A4A6A", "#5A6A3A", "#7A3A3A", "#4A3A5A"])
        ex = '<path d="M-10 -196 L -11 -206 L -5 -200 L 0 -208 L 5 -200 L 11 -206 L 10 -196 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></path>' if i == 1 else ""
        o.append(robed(p, w * x, h * y, s, cl, head="#3A3A3A", beard="#2A1A10", flip=i % 4 == 1, pose="sit", seat=None,
                       up=[(-22, -158), (-14, -176), (-4, -190)]) if i % 2 else
                 robed(p, w * x + cw * 0.2, h * y, s, cl, head="#3A3A3A" if i != 1 else None, hair="#2A1A10" if i == 1 else None, beard="#2A1A10",
                       up=[(-22, -158), (-14, -176), (-4, -190)], flip=i % 4 == 0, extra=ex))
    for _ in range(8):
        x = r.uniform(0, w); y = r.uniform(0.6, 1.0) * h
        o.append(f'<path d="M{f(x)} {f(y)} l 18 -8 l 10 10 l -6 12 l -20 2 Z" fill="#6A5A54" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def four_winds(p, w, h, seed):
    """Four angels standing at the four corners of the earth, holding the four winds (7:1–3): the land and the sea between
    them still, not a leaf moving; the winds as coiled grey streams held in their hands; and another angel ascending from
    the sunrising at the centre, the seal of the living God (a gold signet) in his hand."""
    o = [defs(p), sky(w, h, "#2A3A6A", "#FFC890")]
    hz = h * 0.66
    o.append(halo(w * 0.5, hz, h * 0.5, "#FFE6A0", 0.8) + f'<circle cx="{f(w * 0.5)}" cy="{f(hz)}" r="{f(h * 0.08)}" fill="#FFE6A0"></circle>')
    o.append(sea(w, h, hz, seed, color="#3A7AA8", deep="#1F5A7A"))
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.74)} C {f(w * 0.2)} {f(h * 0.7)} {f(w * 0.34)} {f(h * 0.8)} {f(w * 0.4)} {f(h + 10)} Z" fill="#6A8A4A" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.62)} {f(h + 10)} C {f(w * 0.7)} {f(h * 0.78)} {f(w * 0.86)} {f(h * 0.72)} {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h + 10)} Z" fill="#6A8A4A" stroke="{INK}" stroke-width="2"></path>')
    o.append(olive(w * 0.12, h * 0.95, h / 500, seed) + olive(w * 0.9, h * 0.95, h / 520, seed + 1))
    s = h * 0.5 / 205
    for x, b, fl in ((0.11, 0.62, False), (0.89, 0.62, True), (0.22, 0.98, False), (0.78, 0.98, True)):
        o.append(angel(p, w * x, h * b, s * (0.8 if b < 0.9 else 1.0), up=[(-22, -158), (-46, -160), (-66, -170)], flip=fl))
        wx = w * x + (66 if fl else -66) * s * (0.8 if b < 0.9 else 1.0); wy = h * b - 170 * s * (0.8 if b < 0.9 else 1.0)
        o.append(f'<path d="M{f(wx)} {f(wy)} c 10 -14 30 -14 34 0 c 4 14 -16 22 -22 10 c -4 -8 6 -12 10 -6" fill="none" stroke="#B8C0D0" stroke-width="5" stroke-linecap="round" '
                 f'transform="translate({f(-17 if not fl else 17)} 0)"></path>')
    o.append(angel(p, w * 0.5, hz - h * 0.04, s * 0.7, up=[(-22, -158), (-36, -182), (-44, -206)],
                   extra='<circle cx="-44" cy="-216" r="9" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></circle>'))
    return "".join(o)

TRIBES = ["JUDAH", "REUBEN", "GAD", "ASHER", "NAPHTALI", "MANASSEH", "SIMEON", "LEVI", "ISSACHAR", "ZEBULUN", "JOSEPH", "BENJAMIN"]

def tribes_plate(w, h, title="THE SEALED · A HUNDRED AND FORTY AND FOUR THOUSAND", total="12 × 12,000 = 144,000"):
    """The number of them that were sealed (7:4–8): twelve tribes in the order John names them, twelve thousand each, as a
    numbered plate; the total at the foot."""
    import exo.art8 as B
    o = [plate_bg(w, h, title)]
    B._W[0] = w
    cols, rows_ = 6, 2
    cw, ch = (w - 40) / cols, (h - 80) / rows_
    for i, nm in enumerate(TRIBES):
        x = 20 + (i % cols) * cw; y = 36 + (i // cols) * ch
        o.append(f'<rect x="{f(x + 4)}" y="{f(y + 4)}" width="{f(cw - 8)}" height="{f(ch - 8)}" fill="#12223A" stroke="#8FD0E2" stroke-width="1.2"></rect>'
                 + label(x + cw / 2, y + ch * 0.36, nm, "#FFD23F", max(8, min(11, cw / 9)))
                 + label(x + cw / 2, y + ch * 0.66, "12,000", "#F3EFE6", max(9, min(16, ch / 5))))
        o.append(f'<circle cx="{f(x + cw / 2)}" cy="{f(y + ch * 0.84)}" r="{f(min(6, ch / 14))}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></circle>')
    o.append(label(w / 2, h - 14, total, "#8FD0E2", 11))
    return "".join(o)

def palm(x, b, s, rot=0):
    """A palm branch held up (in the figure's units)."""
    return (f'<g transform="translate({f(x)} {f(b)}) rotate({f(rot)}) scale({f(s)})"><path d="M0 0 C 2 -20 4 -40 2 -60" fill="none" stroke="#3F7A34" stroke-width="2.4"></path>'
            + "".join(f'<path d="M{f(2 + 0.6 * (k * 6 / 60))} {f(-12 - k * 6)} l {d * (12 - k * 0.8):.1f} {-6 - k * 0.3:.1f}" stroke="#4A9A3A" stroke-width="2.4" stroke-linecap="round"></path>'
                      for k in range(8) for d in (-1, 1)) + '</g>')

UP_PALM = [(-22, -158), (-34, -178), (-40, -198)]

def multitude(p, w, h, seed, stage="palms"):
    """A great multitude, which no man could number, of every nation, arrayed in white robes, palms in their hands, before
    the throne and the Lamb (7:9–10): rows of people in white, of many skins, the throne's light at the back. stage
    "fountains": the Lamb leading them to fountains of waters of life in a green land (7:17)."""
    r = random.Random(seed)
    skins = ["#5A3A2A", "#8A5A3A", "#C98E66", "#D9A27A", "#E3B896", "#A8704E", "#6A4430"]
    hairs = ["#1A1210", "#2A1A10", "#3A2214", "#0D0D0F", "#5A3A22"]
    if stage == "fountains":
        o = [defs(p), sky(w, h, "#6AB0D8", "#F3F0C8"), halo(w * 0.5, h * 0.1, w * 0.4, WHITE, 0.8)]
        o.append(hills(w, h, h * 0.5, seed, color="#7AB86A", amp=14, step=90) + ground(w, h, h * 0.56, "#9CCB5E", dy=0))
        for fx in (0.56, 0.8):
            o.append(f'<ellipse cx="{f(w * fx)}" cy="{f(h * 0.7)}" rx="{f(w * 0.08)}" ry="{f(h * 0.04)}" fill="#8FD0E2" stroke="#1F6F9A" stroke-width="2"></ellipse>'
                     f'<path d="M{f(w * fx)} {f(h * 0.7)} C {f(w * fx - 10)} {f(h * 0.6)} {f(w * fx + 10)} {f(h * 0.56)} {f(w * fx)} {f(h * 0.52)}" fill="none" stroke="#C8ECF8" stroke-width="5"></path>')
        o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.72)} C {f(w * 0.5)} {f(h * 0.86)} {f(w * 0.7)} {f(h * 0.9)} {f(w * 0.66)} {f(h + 10)}" fill="none" stroke="#8FD0E2" stroke-width="10"></path>')
        o.append(lamb(w * 0.66, h * 0.66, h * 0.22 / 90))
        s = h * 0.38 / 205
        for i in range(9):
            x = w * (0.04 + 0.05 * i) + r.uniform(-4, 4); b = h * (0.78 + 0.02 * (i % 3))
            o.append(robed(p, x, b, s * r.uniform(0.85, 1.0), "#FFFFFF", skin=r.choice(skins), hair=r.choice(hairs), flip=True, line="#3A3A4A", up=UP_PALM, extra=palm(-40, -198, 0.9)))
        return "".join(o)
    o = [defs(p), sky(w, h, "#1A1440", "#5A4A8A"), halo(w * 0.5, h * 0.12, w * 0.6, "#FFF4C2", 0.85), rays(w * 0.5, h * 0.1, 34, h * 0.05, w, "#FFFDF0", 0.3, 4)]
    o.append(empty_throne(w * 0.5, h * 0.3, h * 0.16 / 180))
    o.append(lamb(w * 0.62, h * 0.36, h * 0.07 / 90, glow=True))
    for row in range(4):
        k = 0.45 + row * 0.18; n = int(10 + (3 - row) * 3)
        b = h * (0.52 + row * 0.15); s = h * 0.3 * k / 205
        for i in range(n):
            x = w * (i + 0.5) / n + r.uniform(-8, 8)
            up = UP_PALM if r.random() < 0.7 else None
            o.append(robed(p, x, b, s, "#FFFFFF", skin=r.choice(skins), hair=r.choice(hairs), woman=r.random() < 0.4, flip=r.random() < 0.5, up=up, line="#3A3A4A",
                           extra=palm(-40, -198, 0.9) if up else ""))
    return "".join(o)
