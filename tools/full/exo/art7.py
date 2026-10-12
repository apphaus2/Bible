"""New drawings for Exodus chapter 7 (Exodus 22–24): pictograms for the ordinances of chapters 22–23 (kit.law cells, each a
320 x 100 strip on art6.GND), the angel sent before the people, the hornet, the borders of the land, the altar and twelve
pillars, the blood of the covenant, and the paved work of sapphire stone (God is never drawn)."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4, exodus5 as V, samuel1 as S1, samuel2 as A2, samuel4 as A4, numbers1 as N, ruth1 as R
from genesis import art2 as Y, art3 as Z, art10 as T
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg, node
from exo import art as A, art3 as C, art6 as S6
from exo.art6 import GND
def f(v): return f"{v:.1f}"

def coins(x, y, n, r=6):
    return "".join(f'<circle cx="{f(x + (i % 5) * r * 2.2)}" cy="{f(y - (i // 5) * r * 1.6)}" r="{r}" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1.2"></circle>' for i in range(n))

def ban(x, y, r):
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="none" stroke="#D7261E" stroke-width="6"></circle>'
            f'<path d="M{f(x - r * 0.7)} {f(y + r * 0.7)} L {f(x + r * 0.7)} {f(y - r * 0.7)}" stroke="#D7261E" stroke-width="6"></path>')

# ---- Exodus 22 ----
def pg_restore(p):
    """Five oxen for an ox, and four sheep for a sheep: one ox and one sheep on the left, the restitution on the right."""
    return (GND + S1.cow(40, 84, 0.24, color="#5A3A22", patch="#3A2214") + E.sheep(40, 50, 0.26) + '<path d="M80 50 L 110 50 M100 42 L 112 50 L 100 58" stroke="#FFD23F" stroke-width="3" fill="none"></path>'
            + "".join(S1.cow(140 + i * 36, 84, 0.2, color="#5A3A22", patch="#3A2214") for i in range(5)) + "".join(E.sheep(146 + i * 40, 46, 0.22) for i in range(4))
            + label(16, 96, "1 → 5 · 1 → 4", "#8FD0E2", 9, "start"))

def pg_night(p, day=False):
    """The thief breaking in: a house wall with a hole broken through it, by night (or, with the sun risen)."""
    sky = sun(270, 26, 12, op=0.4) if day else '<circle cx="270" cy="26" r="10" fill="#E8E2D6"></circle>' + mk.stars(10, 320, 50, 5)
    return (GND + sky + '<rect x="80" y="30" width="140" height="54" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
            '<path d="M150 84 L 146 62 L 158 52 L 172 60 L 174 84 Z" fill="#0D0D0F"></path>' + "".join(f'<rect x="{x}" y="{y}" width="18" height="8" fill="#A88A5A" stroke="#0D0D0F" stroke-width="1"></rect>' for x, y in ((92, 40), (114, 48), (186, 40), (196, 66))))

def pg_double(p):
    """He shall pay double: an ox, an ass and a sheep, each with its double beside it."""
    return GND + S1.cow(70, 84, 0.22, color="#5A3A22", patch="#3A2214") + S1.cow(110, 84, 0.22, color="#5A3A22", patch="#3A2214") + N.ass(180, 84, 0.18) + N.ass(214, 84, 0.18) + E.sheep(260, 84, 0.26) + E.sheep(290, 84, 0.26)

def pg_field(p):
    """His beast loose in another man's field: a cow grazing over a boundary line into rows of grain."""
    return GND + R.field(150, 320, 84, 30, 3, rows=2) + '<path d="M150 84 L 150 40" stroke="#FFD23F" stroke-width="2" stroke-dasharray="4 4"></path>' + S1.cow(150, 84, 0.34, color="#8A5A30", patch="#5A3A22", low=True)

def pg_fire(p):
    """Fire caught in thorns, and the shocks of grain consumed: a burning thorn hedge, sheaves beside it."""
    return GND + E.blaze(110, 84, 80, 60, 7, n=6) + R.sheaf(200, 84, 0.6) + R.sheaf(240, 84, 0.6) + R.sheaf(280, 84, 0.6)

def pg_deposit(p):
    """Money or stuff delivered to a neighbor to keep: a bound chest and a bag of silver inside a house."""
    return (GND + '<rect x="70" y="20" width="180" height="64" fill="#5A3A26" stroke="#0D0D0F" stroke-width="2.4"></rect>'
            '<rect x="110" y="52" width="60" height="32" fill="#8A5A3E" stroke="#0D0D0F" stroke-width="2"></rect><path d="M110 64 L 170 64" stroke="#E8B830" stroke-width="3"></path>'
            + R.sack(206, 84, 0.6))

def pg_beast_kept(p):
    """An ass, or an ox, or a sheep delivered to keep: a herdsman with his staff and a neighbor's beasts."""
    return GND + A.moses(p, 70, 86, 0.34, up=T.HOLD_STAFF).replace(A.headcloth("#E2D8C4"), A.headcloth("#C8BCA6")) + N.ass(150, 84, 0.2) + S1.cow(220, 84, 0.24, color="#5A3A22", patch="#3A2214") + E.sheep(280, 84, 0.24)

def pg_torn(p):
    """If it be torn in pieces, let him bring it for witness: a broken fold-fence, a lion's track in the sand."""
    return (GND + '<path d="M40 84 L 40 50 M80 84 L 80 50 M120 84 L 120 60 M30 58 L 130 58 M30 72 L 90 72" stroke="#8A6A4A" stroke-width="5"></path>'
            '<path d="M120 60 L 150 76" stroke="#8A6A4A" stroke-width="5"></path>' + "".join(f'<g transform="translate({x} {y})"><ellipse rx="9" ry="7" fill="#0D0D0F" opacity="0.6"></ellipse>' + "".join(f'<circle cx="{dx}" cy="-11" r="3.4" fill="#0D0D0F" opacity="0.6"></circle>' for dx in (-7, -2, 3, 8)) + '</g>' for x, y in ((190, 80), (226, 72), (262, 80), (296, 72))))

def pg_borrow(p):
    """If a man borrow aught of his neighbor: one man handing an ox's rope to another."""
    return GND + man(p, 60, 86, 0.34, "#5A3A22") + S1.cow(160, 84, 0.3, color="#8A5A30", patch="#5A3A22") + '<path d="M70 58 C 100 66 130 64 156 60" stroke="#C8A06A" stroke-width="2" fill="none"></path>' + man(p, 260, 86, 0.34, "#4A3A6A", flip=True)

def pg_dowry(p):
    """He shall pay a dowry: a young woman, her father, and a bag of silver between them."""
    return GND + mk.person(p, 80, 86, 0.36, body=SKIN, cloth="#5A3A22", sw=3, extra=Y.WHITE_BEARD) + R.sack(160, 84, 0.6) + woman(p, 240, 86, 0.34, "#C2456A", flip=True)

def pg_idols(p):
    """Thou shalt not suffer a sorceress; he that sacrificeth unto any god save Jehovah: a little idol on a pedestal, struck through."""
    return (GND + '<path d="M146 84 L 150 34 C 150 24 170 24 170 34 L 174 84 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path><circle cx="160" cy="22" r="10" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></circle>'
            + ban(160, 52, 40))

def pg_sojourner(p):
    """A sojourner shalt thou not wrong: a stranger with his staff and bundle at a tent door, made welcome."""
    return GND + A.black_tent(110, 84, 120, 54) + T.figure(p, ("man", "#7A5A3A"), 220, 86, 0.36, flip=True, pose="staff")

def pg_widow(p):
    """Ye shall not afflict any widow, or fatherless child: a woman in a dark veil and a child holding her hand."""
    return GND + woman(p, 150, 86, 0.38, "#3A3450") + T.figure(p, ("lad", "#C8A06A"), 186, 86, 0.22, pose="reach")

def pg_lend(p):
    """If thou lend money to the poor, lay upon him no interest: coins passing from one hand to another, no more coming back."""
    return GND + man(p, 60, 86, 0.34, "#4A3A6A") + coins(120, 70, 5) + '<path d="M120 50 L 200 50 M190 42 L 202 50 L 190 58" stroke="#FFD23F" stroke-width="3" fill="none"></path>' + man(p, 260, 86, 0.32, "#8A7A6A", flip=True)

def pg_pledge(p):
    """Thou shalt restore the garment before the sun goeth down: a folded cloak, the sun low on the horizon."""
    return (GND + sun(250, 80, 16, color="#FF8A3D", op=0.4) + '<rect x="0" y="84" width="320" height="16" fill="#1A1640"></rect>'
            '<path d="M70 84 L 80 60 L 180 60 L 190 84 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path><path d="M84 70 L 176 70" stroke="#5A3A22" stroke-width="2"></path>')

def pg_firstfruits(p):
    """Of thy harvest, and of the outflow of thy presses; the firstling with its dam: a sheaf, grapes, and a lamb by the ewe."""
    return GND + R.sheaf(60, 84, 0.7) + N.grapes(130, 30, 0.5) + E.sheep(230, 84, 0.34) + E3.lamb(270, 84, 0.24)

def pg_dog(p):
    """Flesh that is torn of beasts in the field: cast it to the dogs."""
    return GND + f'<g transform="translate(150 84) scale(0.7)">{C.DOG}</g>'

# ---- Exodus 23 ----
def pg_witness(p):
    """Thou shalt not take up a false report: a witness before the judges, a red mark over the lie."""
    return GND + A.elder("#5A6E8A", 2)(p, 70, 86, 0.36) + A.elder("#6A4A5A", 4)(p, 110, 86, 0.36) + man(p, 230, 86, 0.36, "#5A3A22", flip=True, up=T.POSES["point"]) + ban(270, 30, 18)

def pg_crowd(p):
    """Thou shalt not follow a multitude to do evil: a press of people all one way, and one man standing apart."""
    r = random.Random(4)
    return GND + "".join(man(p, 20 + i * 22, 86, 0.26, r.choice(A.HEBREW), flip=True) for i in range(9)) + man(p, 280, 86, 0.32, "#E2D8C4")

def pg_astray(p):
    """Thine enemy's ox going astray, his ass lying under his burden: an ass down under its load, a man lifting it."""
    return (GND + '<g transform="translate(150 84)"><path d="M-50 0 C -54 -14 -40 -24 -10 -24 L 30 -24 C 40 -30 52 -30 56 -20 L 60 -6 L 50 0 Z" fill="#8A8478" stroke="#0D0D0F" stroke-width="2.2"></path>'
            '<rect x="-34" y="-46" width="50" height="24" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></rect></g>' + man(p, 240, 86, 0.36, "#5A3A22", flip=True, up=T.POSES["reach"]))

def pg_bribe(p):
    """Thou shalt take no bribe: a hand held back from a bag of silver."""
    return GND + R.sack(150, 84, 0.8) + ban(150, 54, 40)

def pg_fallow(p):
    """Six years sow; the seventh let it rest: six rows of grain, the seventh field bare, a beast grazing on it."""
    return GND + "".join(R.sheaf(26 + i * 36, 84, 0.5) for i in range(6)) + '<rect x="230" y="78" width="80" height="6" fill="#6A5A3A"></rect>' + E.sheep(270, 84, 0.26) + label(270, 30, "7TH YEAR", "#FFD23F", 9)

def pg_rest(p):
    """That thine ox and thine ass may have rest: an ox and an ass lying down, the seventh day mark above."""
    return (GND + '<g transform="translate(110 84)"><path d="M-60 0 C -64 -18 -44 -30 -10 -30 L 40 -30 C 52 -38 64 -34 66 -22 L 70 -6 L 58 0 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.2"></path></g>'
            '<g transform="translate(240 84)"><path d="M-46 0 C -50 -14 -36 -22 -8 -22 L 26 -22 C 34 -30 46 -28 48 -18 L 50 -4 L 42 0 Z" fill="#8A8478" stroke="#0D0D0F" stroke-width="2.2"></path></g>'
            + label(160, 22, "THE SEVENTH DAY", "#FFD23F", 10))

def pg_three(p):
    """Three times in the year: unleavened cakes, a sheaf of the harvest, the grapes of the ingathering."""
    return (GND + "".join(f'<ellipse cx="{50 + i * 12}" cy="{80 - i * 6}" rx="22" ry="6" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>' for i in range(3))
            + R.sheaf(160, 84, 0.7) + N.grapes(256, 26, 0.5) + label(60, 22, "I", "#FFD23F", 14) + label(160, 22, "II", "#FFD23F", 14) + label(256, 22, "III", "#FFD23F", 14))

def pg_kid(p):
    """The first of the first-fruits into the house of Jehovah: a basket of first-fruits; and a kid kept by its mother."""
    return GND + E4.basket(90, 84, 2.2) + N.grapes(90, 30, 0.3) + E.sheep(220, 84, 0.34, wool="#5A4A3A") + E3.lamb(262, 84, 0.24).replace("#F8F6F0", "#8A7A6A")

# ---- scenes ----
def angel_before(p, w, h, seed):
    """Behold, I send an angel before thee, to keep thee by the way: the angel in white going before the people in the wilderness."""
    b = h * 0.88
    return (sun(w * 0.9, h * 0.16, 14, op=0.3) + hills(w, h, h * 0.56, seed, color="#C8682E", amp=12) + ground(w, h, h * 0.56, "#E8C88A", dy=0)
            + Z.caravan(p, w * 0.04, w * 0.56, h * 0.72, 0.2, seed) + N.angel(p, w * 0.8, b, fit(b, h * 0.5), sword=False))

def hornet(x, y, s=1.0, rot=0):
    """A hornet: banded gold-and-black body, clear wings."""
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({f(s)})">'
            '<ellipse cx="-10" cy="-10" rx="10" ry="6" fill="#F3EFE6" opacity="0.7" stroke="#0D0D0F" stroke-width="1"></ellipse><ellipse cx="4" cy="-12" rx="10" ry="6" fill="#F3EFE6" opacity="0.7" stroke="#0D0D0F" stroke-width="1"></ellipse>'
            '<ellipse cx="0" cy="0" rx="16" ry="7" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
            '<path d="M-6 -6 L -6 6 M2 -7 L 2 7 M10 -5 L 10 5" stroke="#0D0D0F" stroke-width="3"></path><circle cx="-18" cy="0" r="5" fill="#0D0D0F"></circle></g>')

def hornets(w, h, seed):
    """I will send the hornet before thee: hornets swarming over a Canaanite town, its people going out the far gate."""
    r = random.Random(seed); b = h * 0.86
    return (sun(w * 0.86, h * 0.18, 14, op=0.25) + Y.city(w * 0.5, b, w * 0.6, h * 0.5, seed, color="#8A6A5A", lit="#FFC14D", wall="#9A7A6A") + ground(w, h, b, "#C8A06A", dy=0)
            + "".join(hornet(r.uniform(0, w), r.uniform(h * 0.1, h * 0.7), r.uniform(0.6, 1.4), r.uniform(-30, 30)) for _ in range(26)))

def borders(w, h):
    """From the Red Sea even unto the sea of the Philistines, and from the wilderness unto the River: the bounds as a technical map."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.12)} -10 C {f(w * 0.1)} {f(h * 0.4)} {f(w * 0.06)} {f(h * 0.7)} 0 {f(h + 10)} L -10 {f(h + 10)} L -10 -10 Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.34)} {f(h * 0.86)} L {f(w * 0.38)} {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.98)} -10 C {f(w * 0.9)} {f(h * 0.3)} {f(w * 0.94)} {f(h * 0.5)} {f(w * 0.86)} {f(h * 0.7)}" fill="none" stroke="#2C9DB8" stroke-width="5"></path>')
    o.append(f'<path d="M{f(w * 0.14)} {f(h * 0.2)} L {f(w * 0.9)} {f(h * 0.06)} L {f(w * 0.86)} {f(h * 0.7)} L {f(w * 0.36)} {f(h * 0.9)} L {f(w * 0.12)} {f(h * 0.7)} Z" fill="#9CCB5E" fill-opacity="0.12" stroke="#9CCB5E" stroke-width="2.4" stroke-dasharray="10 6"></path>')
    o += [label(w * 0.02, h * 0.1, "THE SEA OF THE PHILISTINES", "#8FD0E2", 9, "start"), label(w * 0.34, h * 0.82, "THE RED SEA", "#8FD0E2", 9),
          label(w * 0.84, h * 0.86, "THE WILDERNESS", "#E8C88A", 9), label(w * 0.86, h * 0.18, "THE RIVER", "#8FD0E2", 9, "end")]
    return "".join(o)

def pillars12(p, w, h, seed, sprinkle=False):
    """An altar under the mount, and twelve pillars, according to the twelve tribes: the altar smoking, the pillars in a row; sprinkle = Moses with the basin before the people."""
    b = h * 0.86
    o = [E4.sinai(w * 0.5, h * 0.56, w * 0.9, h * 0.54, seed, fire=False), ground(w, h, h * 0.56, "#8A6A4A", dy=0), A4.altar(w * 0.5, h * 0.72, min(0.6, h / 500), seed=seed)]
    for i in range(12):                        # six pillars on either side of the altar
        x = w * (0.08 + (i % 6) * 0.055) + (w * 0.56 if i >= 6 else 0); ph = min(44, h * 0.16)
        o.append(f'<rect x="{f(x - 6)}" y="{f(h * 0.74 - ph)}" width="12" height="{f(ph)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="2"></rect>')
    if sprinkle:
        sc = fit(b, h * 0.5)
        o.append(A.moses(p, w * 0.3, b, sc, up=[(-22, -158), (-30, -186), (-50, -200)]) + E3.basin(w * 0.36, b - 8, 30))
        o.append("".join(f'<circle cx="{f(w * 0.3 - 54 * sc - i * 9)}" cy="{f(b - 200 * sc + i * 9)}" r="3" fill="#B5121B"></circle>' for i in range(6)))
        o.append("".join(A.hebrew(c)(p, w * (0.06 + i * 0.05), b, sc * 0.9) for i, c in enumerate(A.HEBREW[:3])))
    return "".join(o)

def sapphire(p, w, h, seed):
    """Under his feet as it were a paved work of sapphire stone, and as it were the very heaven for clearness: blue paving and a
    blaze of light above; the elders eating and drinking below it (God himself is not drawn)."""
    r = random.Random(seed)
    o = [V.rays(w * 0.5, -20, 40, 20, h * 1.4, color="#FFF4C2", op=0.35)]
    py = h * 0.3
    for row in range(3):
        for i in range(14):
            x = -20 + i * (w / 12) + row * 14; y = py + row * 14
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x + w / 12 - 2)} {f(y)} L {f(x + w / 12 + 10)} {f(y + 12)} L {f(x + 12)} {f(y + 12)} Z" fill="{r.choice(["#1F5FAD", "#2C7ACD", "#3A8AE0"])}" stroke="#8FD0E2" stroke-width="1.2"></path>')
    b = h * 0.92
    o.append(ground(w, h, h * 0.7, "#5A4A6A", dy=0) + f'<rect x="{f(w * 0.1)}" y="{f(b - 10)}" width="{f(w * 0.8)}" height="14" fill="#7A2A3A" stroke="#0D0D0F" stroke-width="2"></rect>')
    o += [A.elder(r.choice(A.HEBREW), i)(p, w * (0.1 + i * 0.1), b - 10, fit(b - 10, h * 0.62)) for i in range(9)]
    return "".join(o)

def tarry(p, w, h, seed):
    """Moses rose up, and Joshua his minister, and went up into the mount; Aaron and Hur stay with the elders below."""
    b = h * 0.9
    o = [E4.sinai(w * 0.7, h * 0.86, w * 0.6, h * 0.8, seed, fire=False), ground(w, h, h * 0.86, "#8A6A4A", dy=0)]
    o.append(A.moses(p, w * 0.6, h * 0.7, fit(h * 0.7, h * 0.56), up=T.HOLD_STAFF) + T.figure(p, ("man", "#7A2A1E"), w * 0.56, h * 0.74, fit(h * 0.74, h * 0.6)))
    o.append(A.aaron(p, w * 0.1, b, fit(b, h * 0.44)) + mk.person(p, round(w * 0.18), round(b), fit(b, h * 0.44), body="#2A1A10", cloth="#5A3A22", sw=3)
             + "".join(A.elder(c, i)(p, w * (0.26 + i * 0.06), b, fit(b, h * 0.48), flip=True) for i, c in enumerate(A.HEBREW[:4])))
    return "".join(o)
