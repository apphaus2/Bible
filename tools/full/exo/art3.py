"""New drawings for Exodus chapter 3 (Exodus 9–12): the cattle in the field, the hail, the flax and the wheat, the locusts,
the darkness, the quiet dog, the calendar of the first month, the passover meal, the unleavened cakes, the night of the going out."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4, judges1 as G1, joshua1 as J, numbers1 as N, samuel1 as S1, egypt as EG
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art10 as T
from genesis.art2 import fit, ground, hills, city, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg, node
from exo import art as A
def f(v): return f"{v:.1f}"

COURTIER = F("adam", skin="#B9785A", shadow="#4A2A3A", egypt=("#E8E2D6", "#5A6E8A"), kohl=True, collar=True, brow="sorrow", sweat=True, light="#FFC14D")
MAGICIAN_BOILS = A.tok("MAGICIAN_BOILS")
PHARAOH_WEEP = A.tok("PHARAOH_WEEP")
HEBREW_FEAR = A.tok("HEBREW_FEAR")
BOTH_L, BOTH_R = [(-22, -158), (-38, -194), (-46, -228)], [(22, -158), (38, -194), (46, -228)]

def herds(w, h, seed, dead=False):
    """Thy cattle which are in the field: horses, asses, camels, herds and flocks along the river pasture."""
    r = random.Random(seed); b = h * 0.5
    o = [sun(w * 0.86, h * 0.16, 14, op=0.25), EG.pyramid(w * 0.8, b, w * 0.18, h * 0.2), ground(w, h, b, "#9CBB5E", dy=0)]
    items = []
    for i in range(14):
        y = r.uniform(b + 16, h * 0.98); x = r.uniform(w * 0.02, w * 0.98); k = (y - b) / (h - b); s = 0.18 + 0.32 * k
        items.append((y, x, s, i % 5))
    for y, x, s, k in sorted(items):
        fl = r.random() < 0.5
        if dead:
            o.append(E2.kine_dead(x, y, s * 0.9, color=r.choice(["#8A5A30", "#C9A27A", "#5A3A22"]), flip=fl)); continue
        o.append([E3.horse(x, y, s * 0.9, flip=fl), N.ass(x, y, s * 0.9, flip=fl), G1.camel(x, y, s * 0.8, flip=fl), S1.cow(x, y, s, flip=fl), E.sheep(x, y, s * 1.2, flip=fl)][k])
    return "".join(o)

def hail_field(w, h, seed):
    """The hail smote every herb of the field, and brake every tree: a split tree, flattened crops, hailstones heaped white."""
    r = random.Random(seed); b = h * 0.66
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2A4A"></rect>', ground(w, h, b, "#5A6A3A", dy=0)]
    o += [f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-14, 14))} {f(r.uniform(-4, 2))}" stroke="#8A9A4A" stroke-width="2.4"></path>' for x, y in [(r.uniform(0, w), r.uniform(b + 6, h)) for _ in range(90)]]
    tx = w * 0.7
    o.append(f'<path d="M{f(tx - 12)} {f(b + 10)} L {f(tx - 8)} {f(b - h * 0.3)} L {f(tx + 10)} {f(b - h * 0.34)} L {f(tx + 14)} {f(b + 10)} Z" fill="#4A2A1A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(tx + 6)} {f(b - h * 0.32)} L {f(tx + 80)} {f(b + 4)} L {f(tx + 66)} {f(b + 12)} Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(tx - 8)} {f(b - h * 0.3)} L {f(tx - 70)} {f(b - h * 0.42)}" stroke="#4A2A1A" stroke-width="8" stroke-linecap="round"></path>')
    o.append(E2.hail(60, 0, w, 0, h, seed))
    o += [f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="5" ry="3" fill="#E8F6FA" stroke="#0D0D0F" stroke-width="1"></ellipse>' for x, y in [(r.uniform(0, w), r.uniform(b + 4, h)) for _ in range(40)]]
    return "".join(o)

def crops(w, h, seed):
    """The flax and the barley were smitten; the wheat and the spelt were not: broken stalks on the left, green blades on the right."""
    r = random.Random(seed); b = h * 0.86; mid = w * 0.5
    o = [f'<rect x="-10" y="-10" width="{f(mid + 10)}" height="{f(h + 20)}" fill="#4A4A6A"></rect>', f'<rect x="{f(mid)}" y="-10" width="{f(w - mid + 10)}" height="{f(h + 20)}" fill="#8FD0E2"></rect>',
         ground(w, h, b, "#6A5A3A", dy=0), sun(w * 0.84, h * 0.2, 12, op=0.3)]
    for i in range(18):
        x = r.uniform(w * 0.03, mid - 10); top = b - r.uniform(h * 0.2, h * 0.4)
        o.append(f'<path d="M{f(x)} {f(b)} L {f(x + 2)} {f(top + 20)} L {f(x + r.choice([-26, 24]))} {f(top + 34)}" fill="none" stroke="#B8A05A" stroke-width="3"></path>'
                 + (f'<circle cx="{f(x + 2)}" cy="{f(top + 18)}" r="4" fill="#5A7ACA" stroke="#0D0D0F" stroke-width="1"></circle>' if i % 2 else ""))
    for i in range(22):
        x = r.uniform(mid + 10, w * 0.97)
        o.append(f'<path d="M{f(x)} {f(b)} C {f(x + 2)} {f(b - 20)} {f(x + 6)} {f(b - 34)} {f(x + 4)} {f(b - r.uniform(30, 52))}" fill="none" stroke="#5E8F26" stroke-width="3.4"></path>')
    o.append(f'<path d="M{f(mid)} -10 L {f(mid)} {f(h + 10)}" stroke="#F3EFE6" stroke-width="3" stroke-dasharray="10 6"></path>')
    o.append(label(w * 0.25, h * 0.96, "FLAX · BARLEY", "#F3EFE6", 10) + label(w * 0.75, h * 0.96, "WHEAT · SPELT", "#0D0D0F", 10))
    return "".join(o)

def spread_hands(p, w, h, seed):
    """Moses went out of the city and spread abroad his hands unto Jehovah: the storm breaking up behind him."""
    b = h * 0.86
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#3A3A5A"></rect>' + sun(w * 0.5, h * 0.3, 18, color="#FFE680", op=0.35)
            + city(w * 0.18, b, w * 0.34, h * 0.4, seed, color="#8A6A5A", lit="#FFC14D", wall="#9A7A6A") + ground(w, h, b, "#8A7A5A", dy=0)
            + E4.figure_both(w * 0.6, b, fit(b, h * 0.36), SKIN, A.MOSES_ROBE, BOTH_L, BOTH_R, p + "fb")
            + f'<g transform="translate({f(w * 0.6)} {f(b)}) scale({f(fit(b, h * 0.36))})">{A.headcloth("#E2D8C4")}{A.BLACK_BEARD}</g>')

def father_son(p, w, h, seed):
    """That thou mayest tell in the ears of thy son, and of thy son's son: an old man and the boys by the lamp."""
    b = h * 0.9
    return (T.stage(p, w, h, seed, "tent", [(A.elder("#5A3A22", 2), 0.3, 0.3), (("lad", "#C8A06A"), 0.5, 0.56, True), (("lad", "#E8E2D6"), 0.62, 0.66, True)])
            + A.lamp(w * 0.82, h * 0.5, 1.2))

def locust_land(w, h, seed, dark=True):
    """They covered the face of the whole earth, so that the land was darkened: fields under a brown cloud of locusts."""
    b = h * 0.62
    sky = "#4A3A1A" if dark else "#C8A06A"
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{sky}"></rect>' + EG.pyramid(w * 0.82, b, w * 0.22, h * 0.26) + ground(w, h, b, "#6A5A2A", dy=0)
            + "".join(f'<path d="M{f(w * x)} {f(b)} L {f(w * x)} {f(b - h * 0.18)} M{f(w * x)} {f(b - h * 0.12)} L {f(w * x - 14)} {f(b - h * 0.2)} M{f(w * x)} {f(b - h * 0.08)} L {f(w * x + 16)} {f(b - h * 0.16)}" stroke="#3A2A1A" stroke-width="3"></path>' for x in (0.1, 0.3, 0.5))
            + E2.locusts(140, 0, w, 0, h, seed, smin=0.15, smax=0.5))

def houses_filled(w, h, seed):
    """Thy houses shall be filled, and the houses of all thy servants: flat-roofed houses black with locusts."""
    b = h * 0.86
    return (sun(w * 0.86, h * 0.18, 14, op=0.2) + city(w * 0.5, b, w * 0.96, h * 0.56, seed, color="#C8A06A", lit="#FFC14D", wall="#D8B878") + ground(w, h, b, "#C8A06A", dy=0)
            + E2.locusts(90, 0, w, h * 0.3, h, seed, smin=0.2, smax=0.6))

def driven_out(p, w, h, seed):
    """They were driven out from Pharaoh's presence: guards with spears thrusting Moses and Aaron out between the columns."""
    b = h * 0.88; top = 0.56 if w < 400 else 0.4; sc = fit(b, h * top)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1F3F7A"></rect>', E2.columns([w * 0.06, w * 0.94], -10, b, 24, color="#E8B830", band="#1F5FAD"), ground(w, h, b, "#B59A7A", dy=0)]
    o.append(A.moses(p, w * 0.2, b, sc, flip=True) + A.aaron(p, w * 0.34, b, sc * 1.02, flip=True))
    for i, x in enumerate((0.56, 0.72)):
        o.append(A.taskmaster(p, w * x, b, sc, flip=True, up=[(-22, -158), (2, -150), (30, -150)]))
        o.append(f'<path d="M{f(w * x - 50 * sc)} {f(b - 150 * sc)} L {f(w * x + 40 * sc)} {f(b - 150 * sc)}" stroke="#5A3A22" stroke-width="3.4"></path>'
                 f'<path d="M{f(w * x - 50 * sc)} {f(b - 150 * sc)} l 10 -5 l 0 10 Z" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1.2"></path>')
    o.append(A.pharaoh(p, w * 0.88, b, sc * 1.05, flip=True))
    return "".join(o)

def west_wind(w, h, seed):
    """An exceeding strong west wind took up the locusts and drove them into the Red Sea: wind-lines and the swarm going out over the waves."""
    b = h * 0.5
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(b + 10)}" fill="#8FD0E2"></rect>', Y.sea(w, h, b, seed)]
    o += [f'<path d="M{f(-20 + i * 30)} {f(h * (0.1 + 0.07 * i))} C {f(w * 0.3)} {f(h * (0.05 + 0.07 * i))} {f(w * 0.6)} {f(h * (0.15 + 0.07 * i))} {f(w + 20)} {f(h * (0.08 + 0.07 * i))}" fill="none" stroke="#F3EFE6" stroke-width="2" opacity="0.7"></path>' for i in range(5)]
    o.append(E2.locusts(60, w * 0.45, w, h * 0.05, h * 0.5, seed, smin=0.15, smax=0.4))
    return "".join(o)

def dark_land(p, w, h, seed):
    """Thick darkness in all the land of Egypt: shapes of men who saw not one another, each in his place."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#05050A"></rect>']
    b = h * 0.9
    for x in (0.2, 0.5, 0.8):
        o.append(mk.person(p, round(w * x), round(b), fit(b, h * 0.4), body="#0B0B12", cloth="#12121C", stroke="#2A2A3A", sw=2))
    return "".join(o)

DOG = ('<path d="M-70 0 C -74 -20 -56 -34 -24 -34 L 34 -32 C 44 -32 52 -26 54 -16 L 84 -10 C 92 -8 92 0 84 0 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>'
       '<path d="M30 -30 C 30 -52 50 -62 66 -56 C 76 -52 80 -44 92 -40 C 98 -38 98 -30 90 -28 L 68 -26 C 60 -22 44 -20 36 -24 Z" fill="#9A7A5A" stroke="#0D0D0F" stroke-width="2.4"></path>'
       '<path d="M50 -56 C 42 -54 38 -44 42 -32 C 48 -36 52 -44 50 -56 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>'
       '<circle cx="66" cy="-46" r="2.6" fill="#0D0D0F"></circle><circle cx="94" cy="-36" r="3" fill="#0D0D0F"></circle>'
       '<path d="M-66 -10 C -84 -14 -96 -4 -104 -14" fill="none" stroke="#0D0D0F" stroke-width="6" stroke-linecap="round"></path><path d="M-66 -10 C -84 -14 -96 -4 -104 -14" fill="none" stroke="#8A6A4A" stroke-width="3.4" stroke-linecap="round"></path>')

def quiet_dog(w, h, seed):
    """Against any of the children of Israel shall not a dog move his tongue: a hound lying quiet, head on its paws, before a Hebrew house by moonlight."""
    b = h * 0.86
    return (mk.stars(40, w, h * 0.5, seed) + f'<circle cx="{f(w * 0.84)}" cy="{f(h * 0.5)}" r="14" fill="#E8E2D6"></circle>' + ground(w, h, b, "#2A2438", dy=0)
            + E3.door(w * 0.12, b - h * 0.42, w * 0.18, h * 0.42, blood=True) + f'<g transform="translate({f(w * 0.6)} {f(b)}) scale({f(min(0.9, h / 360))})">{DOG}</g>')

def lambs(p, w, h, seed):
    """A lamb for a household: the families before their tents, each with a yearling lamb."""
    r = random.Random(seed); b = h * 0.88
    o = [sun(w * 0.86, h * 0.2, 14, op=0.25), ground(w, h, b, "#9CBB5E", dy=0)]
    for i, x in enumerate((0.14, 0.42, 0.7)):
        o.append(A.black_tent(w * x, b - 6, w * 0.2, h * 0.24))
        o.append(man(p, w * x + w * 0.1, b, fit(b, h * 0.5), r.choice(A.HEBREW), up=[(-22, -158), (-30, -120), (-40, -96)]) + E3.lamb(w * x + w * 0.04, b, 0.42))
    return "".join(o)

def dawn_fire(w, h, seed):
    """That which remaineth of it until the morning ye shall burn with fire: a fire in the grey of dawn."""
    b = h * 0.84
    return (hills(w, h, b - 8, seed, color="#4A2A4E", amp=10) + ground(w, h, b, "#2A1A2E", dy=0) + E.blaze(w * 0.7, b, w * 0.16, h * 0.34, seed, n=6)
            + A.black_tent(w * 0.28, b, w * 0.24, h * 0.24))

def calendar(w, h, hi=(), mark=(), title="THE FIRST MONTH", note=None):
    """A technical calendar of the first month: 30 day-cells in two rows of 15 along the top of the panel (the bottom is
    left free for the Voice box); hi = days lit gold (the feast), mark = days ringed red."""
    o = [grid_bg(w, h, color="#1E3A5A", step=24), label(14, 24, title, "#FFD23F", 12, "start")]
    cw = (w - 28) / 15; ch = min(46, (h - 120) / 2)
    for d in range(1, 31):
        x = 14 + ((d - 1) % 15) * cw; y = 36 + ((d - 1) // 15) * ch
        lit = d in hi
        o.append(f'<rect x="{f(x + 2)}" y="{f(y + 2)}" width="{f(cw - 4)}" height="{f(ch - 4)}" fill="{"#FFD23F" if lit else "#12113A"}" fill-opacity="{0.85 if lit else 0.8}" stroke="{"#D7261E" if d in mark else "#2C9DB8"}" stroke-width="{3 if d in mark else 1.2}"></rect>'
                 + label(x + cw / 2, y + ch / 2 + 5, str(d), "#0D0D0F" if lit else "#8FD0E2", 13))
    if note: o.append(label(w / 2, 24, note, "#8FD0E2", 9))
    return "".join(o)

def roast(w, h, seed):
    """Roast with fire, and unleavened bread; with bitter herbs: the lamb on a spit over the coals, flat loaves, a bowl of herbs."""
    b = h * 0.84
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1408"></rect>' + ground(w, h, b, "#3A2418", dy=0)
            + E.blaze(w * 0.5, b, w * 0.3, h * 0.3, seed, n=7)
            + f'<path d="M{f(w * 0.24)} {f(b - h * 0.42)} L {f(w * 0.76)} {f(b - h * 0.42)}" stroke="#5A3A22" stroke-width="5"></path>'
            + f'<path d="M{f(w * 0.24)} {f(b)} L {f(w * 0.26)} {f(b - h * 0.46)} M{f(w * 0.76)} {f(b)} L {f(w * 0.74)} {f(b - h * 0.46)}" stroke="#5A3A22" stroke-width="5"></path>'
            + f'<ellipse cx="{f(w * 0.5)}" cy="{f(b - h * 0.42)}" rx="{f(w * 0.14)}" ry="{f(h * 0.07)}" fill="#8A3A1E" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
            + "".join(f'<ellipse cx="{f(w * x)}" cy="{f(b + 10)}" rx="{f(w * 0.06)}" ry="7" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></ellipse>' for x in (0.1, 0.22))
            + f'<path d="M{f(w * 0.82)} {f(b + 4)} C {f(w * 0.82)} {f(b + 22)} {f(w * 0.96)} {f(b + 22)} {f(w * 0.96)} {f(b + 4)} Z" fill="#8A5A3E" stroke="#0D0D0F" stroke-width="2"></path>'
            + "".join(f'<path d="M{f(w * x)} {f(b + 6)} l {f(d)} -18" stroke="#5E8F26" stroke-width="3"></path>' for x, d in ((0.85, -4), (0.88, 3), (0.91, -2), (0.93, 5))))

def cakes(w, h, seed):
    """Unleavened cakes of the dough: flat round loaves baking on hot stones by the fire."""
    r = random.Random(seed); b = h * 0.84
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A2E"></rect>', mk.stars(30, w, h * 0.4, seed), ground(w, h, b, "#3A2418", dy=0),
         E.blaze(w * 0.2, b, w * 0.18, h * 0.3, seed, n=6)]
    for i in range(7):
        x = w * (0.38 + i * 0.085); y = b - 8 + (i % 2) * 10
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y + 6)}" rx="{f(w * 0.05)}" ry="8" fill="#6A6A6A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
                 f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.04)}" ry="7" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></ellipse>'
                 + "".join(f'<circle cx="{f(x + r.uniform(-12, 12))}" cy="{f(y + r.uniform(-3, 3))}" r="1.6" fill="#8A5A2E"></circle>' for _ in range(4)))
    return "".join(o)

def bundles(p, w, h, seed):
    """Their kneading-troughs being bound up in their clothes upon their shoulders: people hurrying by night with bundles."""
    r = random.Random(seed); b = h * 0.9; n = max(3, int(w / 110))
    o = [mk.stars(40, w, h * 0.5, seed), ground(w, h, b, "#2A2438", dy=0)]
    for i in range(n):
        x = w * (0.1 + i * 0.8 / max(1, n - 1)); s_ = fit(b, h * (0.5 + (i % 2) * 0.06)); hx = x - 20 * s_; hy = b - 168 * s_
        up = [(-22, -158), (-18, -186), (-6, -196)]
        o.append(man(p, x, b, s_, r.choice(A.HEBREW), flip=True, up=up) if i % 2 == 0 else woman(p, x, b, s_, r.choice(["#5A6E8A", "#7A3A5A"]), flip=True, up=up))
        o.append(f'<ellipse cx="{f(hx)}" cy="{f(hy)}" rx="{f(30 * s_)}" ry="{f(16 * s_)}" fill="{r.choice(["#C8A06A", "#E8E2D6", "#8A6A4A"])}" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    return "".join(o)

def household_meal(p, w, h, seed):
    """When your children shall say unto you, What mean ye by this service?: a family about the passover table by lamplight."""
    b = h * 0.9
    tbl = f'<rect x="{f(w * 0.3)}" y="{f(b - h * 0.16)}" width="{f(w * 0.4)}" height="12" fill="#8A5A3E" stroke="#0D0D0F" stroke-width="2"></rect>'
    return (T.stage(p, w, h, seed, "tent", [(A.elder("#5A3A22", 1), 0.22, 0.34), (("woman", "#5A6E8A"), 0.78, 0.38, True), (("lad", "#C8A06A"), 0.62, 0.6, True)])
            + tbl + f'<ellipse cx="{f(w * 0.5)}" cy="{f(b - h * 0.17)}" rx="{f(w * 0.06)}" ry="8" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></ellipse>' + A.lamp(w * 0.42, b - h * 0.2, 0.8))
