"""New drawings for Exodus chapter 6 (Exodus 19–21): eagles' wings, the camp before the mount, the bounds, garments washed,
the altar of earth, and the pictograms for the ordinances (kit.law cells, each a 320 x 100 strip).

Pictograms keep the law readable at a glance and never show violence: a closed door for the servant who stays, a pair
of scales for the judges, an ox with a rope for the ox that goreth, an open pit for the pit left uncovered."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4, exodus5 as V, samuel1 as S1, samuel4 as A4, numbers1 as N
from genesis import art2 as Y, art3 as Z, art10 as T
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg
from exo import art as A
def f(v): return f"{v:.1f}"

def eagle(x, y, s=1.0, flip=False):
    """An eagle with wings spread, gliding (side view)."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            '<path d="M-90 -10 C -60 -40 -30 -46 -6 -20 C 10 -50 50 -60 96 -36 C 60 -30 36 -14 20 0 C 10 8 -10 8 -20 2 C -40 -4 -70 -2 -90 -10 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M18 -4 C 28 -10 40 -10 46 -4 L 56 -2 L 44 4 C 38 8 26 8 18 4 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M56 -2 L 62 2 L 52 4 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>'
            '<path d="M-20 2 L -40 12 L -14 8 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path>'
            + "".join(f'<path d="M{x0} {y0} l -10 6" stroke="#0D0D0F" stroke-width="1.4" opacity="0.6"></path>' for x0, y0 in ((-70, -14), (-54, -22), (40, -40), (60, -38), (76, -38))) + '</g>')

def wings(p, w, h, seed):
    """I bare you on eagles' wings: an eagle over the long file of the people in the wilderness, Sinai far off."""
    b = h * 0.86
    return (sun(w * 0.86, h * 0.2, 14, op=0.3) + E4.sinai(w * 0.82, b, w * 0.3, h * 0.5, seed, fire=False) + ground(w, h, b, "#C8A06A", dy=0)
            + Z.caravan(p, w * 0.04, w * 0.7, b, 0.22, seed) + eagle(w * 0.38, h * 0.3, min(1.2, h / 220)))

def camp_before(p, w, h, seed, fire=False, bounds=False, people=True):
    """Israel encamped before the mount: rows of tents on the plain, the granite massif beyond; bounds = a line of stakes."""
    b = h * 0.92; r = random.Random(seed)
    o = [E4.sinai(w * 0.5, h * 0.62, w * 0.9, h * 0.6, seed, fire=fire), ground(w, h, h * 0.62, "#8A6A4A", dy=0)]
    if bounds:
        o.append(f'<path d="M-10 {f(h * 0.66)} L {f(w + 10)} {f(h * 0.66)}" stroke="#D7261E" stroke-width="2.4" stroke-dasharray="3 9"></path>'
                 + "".join(f'<path d="M{f(x)} {f(h * 0.66)} L {f(x)} {f(h * 0.62)}" stroke="#5A3A22" stroke-width="3"></path>' for x in range(10, int(w), 34)))
    for row in range(2):
        for i in range(8):
            x = w * (0.04 + i * 0.13) + row * w * 0.06; y = h * (0.76 + row * 0.12)
            o.append(A.black_tent(x, y, w * (0.08 + row * 0.02), h * (0.08 + row * 0.02)))
    return "".join(o)

def washing(p, w, h, seed):
    """They washed their garments: women and men at a stream below the mount, white cloth spread on the stones."""
    r = random.Random(seed); b = h * 0.9
    o = [E4.sinai(w * 0.7, h * 0.5, w * 0.6, h * 0.46, seed, fire=False), ground(w, h, h * 0.5, "#8A6A4A", dy=0),
         f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.58)} {f(w * 0.6)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.66)} L {f(w + 10)} {f(h * 0.74)} C {f(w * 0.6)} {f(h * 0.78)} {f(w * 0.3)} {f(h * 0.66)} -10 {f(h * 0.7)} Z" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></path>']
    o += [f'<rect x="{f(w * x)}" y="{f(h * 0.8 + (i % 2) * 8)}" width="{f(w * 0.08)}" height="{f(h * 0.05)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></rect>' for i, x in enumerate((0.06, 0.2, 0.52, 0.7, 0.86))]
    for i, x in enumerate((0.14, 0.34, 0.62, 0.8)):
        o.append(E.kneel(w * x, h * 0.78, 0.34, color=r.choice(A.HEBREW + ["#5A6E8A", "#C2456A"]), skin="#8A5A3E", flip=i % 2 == 1))
    return "".join(o)

def altar_earth(w, h, seed):
    """An altar of earth, or of unhewn stones, with no steps up to it: the smoking altar in the open."""
    b = h * 0.88
    return (sun(w * 0.84, h * 0.22, 14, op=0.25) + hills(w, h, b - 8, seed, color="#6A4A3A", amp=8) + ground(w, h, b, "#8A6A4A", dy=0)
            + A4.altar(w * 0.5, b, min(1.1, h / 300), seed=seed))

def idols_no(w, h, seed):
    """Gods of silver, or gods of gold, ye shall not make: two small cast figures under a red bar."""
    cx, cy = w * 0.5, h * 0.56; s = min(1.0, h / 260)
    fig = lambda x, c: (f'<g transform="translate({f(x)} {f(cy)}) scale({f(s)})"><path d="M-14 50 L -18 -10 C -18 -30 18 -30 18 -10 L 14 50 Z" fill="{c}" stroke="#0D0D0F" stroke-width="2.4"></path>'
                        f'<circle cx="0" cy="-42" r="14" fill="{c}" stroke="#0D0D0F" stroke-width="2.4"></circle><path d="M-26 50 L 26 50 L 22 62 L -22 62 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path></g>')
    return (fig(cx - 60 * s, "#C8C8D0") + fig(cx + 60 * s, "#E8B830")
            + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(110 * s)}" fill="none" stroke="#D7261E" stroke-width="10"></circle>'
            + f'<path d="M{f(cx - 78 * s)} {f(cy + 78 * s)} L {f(cx + 78 * s)} {f(cy - 78 * s)}" stroke="#D7261E" stroke-width="10"></path>')

# ---- pictograms for the ordinances (320 x 100) ------------------------------------------------------------
GND = '<rect x="-200" y="-400" width="720" height="500" fill="#2A2458"></rect><rect x="-200" y="84" width="720" height="16" fill="#1A1640"></rect>'

def pg_servant(p):
    """Six years he shall serve; in the seventh he shall go out free: six dark day-marks, the seventh lit, a man walking out."""
    o = [GND] + [f'<rect x="{14 + i * 26}" y="20" width="20" height="20" fill="{"#FFD23F" if i == 6 else "#12113A"}" stroke="#8FD0E2" stroke-width="1.4"></rect>' for i in range(7)]
    o.append(man(p, 240, 86, 0.36, "#8A6A4A", flip=False) + label(24, 58, "6 YEARS · THE 7TH FREE", "#8FD0E2", 9, "start"))
    return "".join(o)

def pg_door(p):
    """He shall bring him to the door, or unto the door-post: a house door and its post, the servant standing at it."""
    return (GND + E3.door(150, 18, 54, 66, blood=False, light="#5A3A26").replace("#8A6A4A", "#8A6A4A") + man(p, 230, 86, 0.36, "#8A6A4A", flip=True)
            + man(p, 100, 86, 0.38, "#4A3A6A"))

def pg_maid(p):
    """A maid-servant and her redemption: a young woman and a little bag of silver."""
    return (GND + woman(p, 120, 86, 0.36, "#7A3A5A") + f'<path d="M190 84 C 182 70 186 58 200 56 C 214 58 218 70 210 84 Z" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="2"></path>'
            + f'<path d="M194 58 L 206 58" stroke="#5A3A22" stroke-width="3"></path>')

def pg_refuge(p):
    """I will appoint thee a place whither he shall flee: a man running toward a walled town with a lit gate."""
    return (GND + Y.city(250, 84, 110, 60, 3, color="#4A3A5A", lit="#FFC14D", wall="#5A4A6A") + T.figure(p, ("man", "#8A6A4A"), 110, 86, 0.34, pose="run")
            + f'<path d="M140 50 L 190 50" stroke="#FFD23F" stroke-width="2" stroke-dasharray="6 5"></path><path d="M190 50 l -8 -5 l 0 10 Z" fill="#FFD23F"></path>')

def pg_parents(p):
    """Thy father and thy mother: an old man and an old woman side by side."""
    return GND + mk.person(p, 130, 86, 0.36, body=SKIN, cloth="#5A3A22", sw=3, extra=Y.WHITE_BEARD) + woman(p, 190, 86, 0.34, "#5A6E8A")

def pg_staff(p):
    """If he rise again, and walk abroad upon his staff: a man on a staff, a bed behind him."""
    return (GND + f'<rect x="40" y="62" width="90" height="12" rx="4" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></rect><path d="M44 74 L 44 84 M126 74 L 126 84" stroke="#0D0D0F" stroke-width="3"></path>'
            + A.moses(p, 200, 86, 0.36, up=T.HOLD_STAFF).replace(A.headcloth("#E2D8C4"), "").replace(A.BLACK_BEARD, ""))

def pg_scales(p):
    """He shall pay as the judges determine: a pair of balance-scales over a little heap of silver."""
    return (GND + '<path d="M160 18 L 160 80 M120 30 L 200 30" stroke="#E8B830" stroke-width="4"></path><path d="M140 82 L 180 82" stroke="#E8B830" stroke-width="5"></path>'
            + "".join(f'<path d="M{x - 18} 60 C {x - 18} 72 {x + 18} 72 {x + 18} 60 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path><path d="M{x} 30 L {x - 16} 60 M{x} 30 L {x + 16} 60" stroke="#E8B830" stroke-width="1.6"></path>' for x in (120, 200))
            + "".join(f'<circle cx="{194 + i * 6}" cy="56" r="4" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1"></circle>' for i in range(3)))

def pg_free(p):
    """He shall let him go free: a servant going out of an open door into the light."""
    return GND + E3.door(60, 18, 54, 66, blood=False, light="#FFD23F") + T.figure(p, ("man", "#8A6A4A"), 170, 86, 0.36, pose="raise") + sun(270, 30, 10, op=0.4)

def pg_ox(p, rope=True):
    """The ox that goreth: a great ox with long horns; rope=True, tethered to a post (kept in)."""
    return (GND + S1.cow(170, 84, 0.5, color="#5A3A22", patch="#3A2214")
            + '<path d="M218 50 C 230 40 240 38 248 42 M214 46 C 220 34 228 30 236 30" fill="none" stroke="#E8E2D6" stroke-width="4" stroke-linecap="round"></path>'
            + ('<path d="M60 84 L 60 30" stroke="#5A3A22" stroke-width="6"></path><path d="M60 40 C 100 50 160 54 214 56" fill="none" stroke="#C8A06A" stroke-width="2.4"></path>' if rope else ""))

def pg_silver(p):
    """Thirty shekels of silver: thirty small coins in three rows."""
    return GND + "".join(f'<circle cx="{40 + (i % 10) * 26}" cy="{28 + (i // 10) * 22}" r="8" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1.4"></circle>' for i in range(30)) + label(160, 96, "30 SHEKELS", "#8FD0E2", 9)

def pg_pit(p):
    """If a man dig a pit and not cover it: an open pit in the ground, an ass beside it."""
    return (GND + '<path d="M80 84 L 100 84 L 104 96 L 176 96 L 180 84 L 200 84" fill="#0D0D0F" stroke="#0D0D0F" stroke-width="2"></path><ellipse cx="140" cy="86" rx="44" ry="8" fill="#0D0D0F"></ellipse>'
            + N.ass(250, 84, 0.3, flip=True) + '<path d="M60 84 L 70 64 L 78 84" fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.6"></path>')

def pg_two_oxen(p):
    """If one man's ox hurt another's: two oxen head to head."""
    return GND + S1.cow(110, 84, 0.42, color="#5A3A22", patch="#3A2214") + S1.cow(220, 84, 0.42, flip=True, color="#8A5A30", patch="#5A3A22")

def pg_measure(p):
    """Life for life, eye for eye: an even balance, both pans level (the law of like for like)."""
    return (GND + '<path d="M160 18 L 160 80 M100 40 L 220 40" stroke="#E8B830" stroke-width="4"></path><path d="M140 82 L 180 82" stroke="#E8B830" stroke-width="5"></path>'
            + "".join(f'<path d="M{x - 22} 66 C {x - 22} 78 {x + 22} 78 {x + 22} 66 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path><path d="M{x} 40 L {x - 20} 66 M{x} 40 L {x + 20} 66" stroke="#E8B830" stroke-width="1.6"></path>' for x in (100, 220)))
