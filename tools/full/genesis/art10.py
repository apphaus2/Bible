"""New drawings for Genesis chapter 10 (Genesis 34–36), and stage(): a general scene builder for the rest of Genesis.

stage(p, w, h, seed, setting, cast, props) lays out a panel: a setting (sky, ground, horizon pieces), then the cast as a
list of (who, x, top, flip, pose) where x is a fraction of the width and top is the fraction of the height the head
should reach (so heads stay where the captions are not), then props drawn on top."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus4 as E4, exodus5 as V, joshua1 as J, judges1 as G1, judges2 as S, samuel1 as A, samuel2 as A2, samuel4 as A4, numbers1 as N, egypt as EG
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art4 as Q, art5 as K, art6 as R6, art7 as J7, art8 as L, art9 as M
from genesis.art2 import fit, ground, hills, birds, city, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg, node, route, STAFF, HOLD_STAFF, GREY_BEARD
def f(v): return f"{v:.1f}"

POSES = {"raise": [(-22, -158), (-30, -196), (-36, -232)], "reach": [(-22, -158), (-40, -126), (-58, -110)],
         "point": [(-22, -158), (4, -150), (30, -150)], "staff": HOLD_STAFF, "run": [(-22, -158), (-46, -140), (-60, -160)],
         "hold": [(-22, -158), (-10, -128), (14, -124)], "up": [(-22, -158), (-6, -200), (14, -236)]}
SWORD = '<path d="M14 -150 L 46 -236" stroke="#C8C8D0" stroke-width="5" stroke-linecap="round"></path><path d="M8 -158 L 22 -146" stroke="#5A3A22" stroke-width="6"></path>'

def figure(p, who, x, y, s, flip=False, pose=None):
    """Draw one of the cast by name. who is a key below, or ("man"|"woman", colour)."""
    up = POSES.get(pose) if isinstance(pose, str) else pose
    if isinstance(who, tuple):
        kind, c = who
        if kind == "woman": return woman(p, x, y, s, c, flip=flip, up=up)
        if kind == "sword": return man(p, x, y, s, c, flip=flip, up=POSES["point"], extra=SWORD)
        if kind == "egypt": return man(p, x, y, s, c, flip=flip, up=up, extra='<path d="M-14 -190 L 14 -190 L 18 -170 L -18 -170 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></path>')
        if kind == "lad": return K.lad(p, x, y, s, cloth=c, flip=flip, up=up)
        if kind == "shade": return mk.person(p, round(x), round(y), round(s, 3), body="#12090A", flip=flip, up=up)
        return man(p, x, y, s, c, flip=flip, up=up)
    staff = pose == "staff"
    if who == "jacob": return L.jacob_man(p, x, y, s, flip=flip, up=up, staff=staff)
    if who == "israel": return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=J7.JACOB_ROBE, sw=3, flip=flip, up=up, extra=Y.WHITE_BEARD + (STAFF if staff else ""))
    if who == "rachel": return L.rachel(p, x, y, s, flip=flip, up=up)
    if who == "leah": return L.leah(p, x, y, s, flip=flip, up=up)
    if who == "esau": return M.esau_old(p, x, y, s, flip=flip, up=up)
    if who == "joseph": return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#F3EFE6", kind="Tunic", sw=3, flip=flip, up=up, extra=COAT)
    if who == "joseph_plain": return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#D8C8A0", kind="Tunic", sw=3, flip=flip, up=up)
    if who == "joseph_eg": return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#F3EFE6", sw=3, flip=flip, up=up, extra=NEMES_BLUE)
    if who == "pharaoh": return mk.person(p, round(x), round(y), round(s, 3), body="#8A4A2E", cloth="#F3EFE6", sw=3, flip=flip, up=up, extra=NEMES_GOLD)
    if who == "dinah": return woman(p, x, y, s, "#E07A9A", flip=flip, up=up)
    if who == "benjamin": return K.lad(p, x, y, s, cloth="#C2456A", flip=flip, up=up)
    raise KeyError(who)

COAT = ("".join(f'<path d="M{-25 + i * 7} -160 L {-27 + i * 7.6} -60" stroke="{c}" stroke-width="7"></path>'
                for i, c in enumerate(["#D7261E", "#FF8A3D", "#FFD23F", "#5E8F26", "#1F5FAD", "#7A3BA8", "#D7261E", "#FFD23F"])))
NEMES_BLUE = ('<path d="M-16 -198 L 16 -198 L 22 -150 L 12 -160 L -12 -160 L -22 -150 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.8"></path>'
              '<path d="M-16 -186 L 16 -186 M-18 -174 L 18 -174 M-20 -162 L 20 -162" stroke="#1F5FAD" stroke-width="4"></path>')
NEMES_GOLD = NEMES_BLUE.replace("#1F5FAD", "#D7261E") + A2.crown(0, -200, 0.32)

def stage(p, w, h, seed, setting="field", cast=(), props="", base=0.88, sun_at=None):
    """A scene: setting + cast + props. Each cast entry is (who, x, top) or (who, x, top, flip) or (who, x, top, flip, pose)."""
    b = h * base
    S_ = {"field": ("#8AAA5A", True), "sand": ("#C8A06A", True), "rock": ("#8A7A6A", True), "night": ("#1A1430", False),
          "egypt": ("#D8B878", True), "palace": ("#B59A7A", False), "tent": ("#2A1408", False), "dusk": ("#2A1A2E", False)}
    g, day = S_.get(setting, ("#8AAA5A", True))
    o = []
    if setting == "night": o.append(mk.stars(70, w, h * 0.6, seed))
    if setting == "tent": o.append(J7.tent_inside(w, h, 0.3))
    if setting == "palace":
        o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1F3F7A"></rect>')
        for x in (0.06, 0.94):
            o.append(f'<rect x="{f(w * x - 16)}" y="-10" width="32" height="{f(b + 10)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></rect>'
                     + "".join(f'<path d="M{f(w * x - 16)} {f(y)} L {f(w * x + 16)} {f(y)}" stroke="#1F5FAD" stroke-width="5"></path>' for y in range(20, int(b), 34)))
    if day and setting not in ("tent",):
        o.append(sun(w * (sun_at if sun_at is not None else 0.86), h * 0.18, 14, color="#FFE680", op=0.25))
    if setting == "egypt": o.append(EG.pyramid(w * 0.8, b - h * 0.02, w * 0.26, h * 0.34) + EG.pyramid(w * 0.94, b - h * 0.02, w * 0.16, h * 0.2))
    o.append(ground(w, h, b, g, dy=0))
    for c in cast:
        who, x, top = c[0], c[1], c[2]
        flip = c[3] if len(c) > 3 else False
        pose = c[4] if len(c) > 4 else None
        o.append(figure(p, who, w * x, b, fit(b, h * top), flip=flip, pose=pose))
    return "".join(o) + props

# ---- faces for Genesis 34–36 ------------------------------------------------------------------------------
HAMOR = F("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#E8E2D6", hl="#B8B2A6", beard=True, scarf="#2A6A5A", band=True, light="#FFC14D")
SHECHEM = F("adam", skin="#C98E66", shadow="#6A3A2A", hair="#1A1210", hl="#4A3A2E", stubble="#2A1A10", scarf="#2A6A5A", band=True, light="#FF8A3D")
SIMEON = F("adam", skin="#B9785A", shadow="#4A1A16", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", brow="scowl", light="#D7261E")
LEVI = F("adam", skin="#C47A5A", shadow="#4A1A16", hair="#3A2214", hl="#6A5A4E", stubble="#2A1A10", brow="scowl", light="#D7261E")
JACOB_GRIEVED = F("adam", skin="#B98A7E", shadow="#4A3A5A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", brow="sorrow", light="#9A8AFF")
JACOB_AWE = F("adam", skin="#B9A6B8", shadow="#4A3A6E", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", brow="sorrow", light="#FFF4C2")
MIDWIFE = F("eve", skin="#C99A84", shadow="#6A4A3A", hair="#5A4A3E", scarf="#4A5A7A", light="#FFC14D")
RACHEL_DYING = F("eve", skin="#C8A8A0", shadow="#5A4A5A", hair="#1A1210", brow="sorrow", sweat=True, light="#9FB8FF")

def dinah_walk(p, w, h, seed):
    """Dinah went out to see the daughters of the land: a young woman walking toward the city's women at the well."""
    return stage(p, w, h, seed, "field", [("dinah", 0.24, 0.48, False), (("woman", "#2A6A5A"), 0.68, 0.5, True), (("woman", "#B5652E"), 0.78, 0.5, True), (("woman", "#E8B830"), 0.88, 0.52, True)])

def shechem_city(p, w, h, seed, gate=False, smoke=False):
    """The city of Shechem: a walled Hivite town on its hill; with smoke rising after the sword."""
    b = h * 0.86
    o = [sun(w * 0.86, h * 0.2, 14, op=0.2), city(w * 0.56, b, w * 0.7, h * 0.5, seed, color="#8A6A5A", lit="#FFC14D", wall="#9A7A6A"), ground(w, h, b, "#9AAA5A", dy=0)]
    if gate: o.append(A4.gatehouse(w * 0.56, b, w * 0.24, h * 0.5))
    if smoke:
        o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A1A1A"></rect>'] + o[1:]
        o += [f'<path d="M{f(w * x)} {f(b - h * 0.3)} C {f(w * x - 40)} {f(h * 0.3)} {f(w * x + 30)} {f(h * 0.1)} {f(w * x - 10)} -20" fill="none" stroke="#4A3A3E" stroke-width="40" opacity="0.6" stroke-linecap="round"></path>' for x in (0.36, 0.56, 0.76)]
    return "".join(o)

def foreign_gods(p, w, h, seed):
    """They gave unto Jacob the foreign gods, and the rings in their ears; and Jacob hid them under the oak by Shechem."""
    b = h * 0.88; r = random.Random(seed)
    rings = "".join(f'<circle cx="{f(w * 0.62 + r.uniform(-40, 40))}" cy="{f(b - r.uniform(2, 12))}" r="{f(r.uniform(4, 7))}" fill="none" stroke="#E8B830" stroke-width="2.4"></circle>' for _ in range(10))
    return (sun(w * 0.86, h * 0.2, 14, op=0.25) + ground(w, h, b, "#8AAA5A", dy=0) + A4.great_oak(w * 0.5, b, round(h / 280, 3), seed=seed)
            + f'<ellipse cx="{f(w * 0.62)}" cy="{f(b)}" rx="{f(w * 0.1)}" ry="10" fill="#3A2A1E"></ellipse>' + M.teraphim(w * 0.6, b - 4, h / 260) + rings
            + L.jacob_man(p, w * 0.24, b, fit(b, h * 0.42), up=POSES["reach"]))

def terror(p, w, h, seed):
    """A terror of God upon the cities round about: walled towns under a dark sky crossed with light; no one pursues."""
    b = h * 0.84
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A3E"></rect>' + V.rays(w * 0.5, -30, 30, 30, h * 1.4, color="#FFF4C2", op=0.25)
            + "".join(city(w * x, b, w * 0.18, h * 0.3, seed + i, color="#3A2A3E", lit="#FFC14D", wall="#4A3A4E") for i, x in enumerate((0.14, 0.86)))
            + ground(w, h, b, "#2A1A2E", dy=0) + Z.caravan(p, w * 0.32, w * 0.68, b + 4, 0.5, seed))

def allon_bacuth(p, w, h, seed):
    """Deborah Rebekah's nurse died, and was buried below Beth-el under the oak: Allon-bacuth, the oak of weeping."""
    b = h * 0.86
    return (sun(w * 0.86, b - 10, h * 0.2, color="#C2456A", op=0.2) + hills(w, h, b, seed, color="#2A1A2E", amp=6)
            + A4.great_oak(w * 0.4, b, round(h / 260, 3), seed=seed, dark=True) + A4.stone_heap(w * 0.56, b + 4, w * 0.12, h * 0.08)
            + label(w * 0.56, b + 22, "ALLON-BACUTH", "#F3EFE6", 9))

def drink_offering(p, w, h, seed):
    """A pillar of stone; he poured out a drink-offering thereon, and poured oil thereon."""
    return L.oil_pillar(p, w, h, seed)

def roadside_grave(p, w, h, seed):
    """Rachel buried in the way to Ephrath, and a pillar upon her grave: a lone stone by the road at dusk."""
    b = h * 0.84
    return (sun(w * 0.8, b - 6, h * 0.2, color="#FF8A3D", op=0.25) + hills(w, h, b, seed, color="#3A2A3E", amp=8) + ground(w, h, b, "#5A4A4E", dy=0)
            + f'<path d="M-10 {f(h + 10)} C {f(w * 0.3)} {f(b + 6)} {f(w * 0.6)} {f(b + 6)} {f(w + 10)} {f(b + 2)}" fill="none" stroke="#8A7A6A" stroke-width="16"></path>'
            + f'<rect x="{f(w * 0.46)}" y="{f(b - h * 0.36)}" width="{f(w * 0.06)}" height="{f(h * 0.36)}" rx="5" fill="#8A8478" stroke="#0D0D0F" stroke-width="2.2"></rect>'
            + A4.stone_heap(w * 0.49, b + 4, w * 0.16, h * 0.06) + label(w * 0.49, b + 24, "THE WAY TO EPHRATH", "#F3EFE6", 9))

def tower_eder(p, w, h, seed):
    """Israel spread his tent beyond the tower of Eder: a watch-tower over the flocks."""
    b = h * 0.86
    tower = (f'<path d="M{f(w * 0.72)} {f(b)} L {f(w * 0.74)} {f(b - h * 0.56)} L {f(w * 0.84)} {f(b - h * 0.56)} L {f(w * 0.86)} {f(b)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             + "".join(f'<rect x="{f(w * (0.735 + i * 0.03))}" y="{f(b - h * 0.6)}" width="{f(w * 0.02)}" height="{f(h * 0.04)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.6"></rect>' for i in range(4)))
    return (sun(w * 0.2, h * 0.2, 14, op=0.25) + ground(w, h, b, "#8AAA5A", dy=0) + tower + E4.tent(w * 0.24, b, w * 0.18, h * 0.26)
            + Z.flock(w * 0.36, w * 0.66, b - 2, b + 20, 8, seed, cows=0, smin=0.2, smax=0.26))

def isaac_buried(p, w, h, seed):
    """Isaac was gathered unto his people, old and full of days: and Esau and Jacob his sons buried him."""
    return (K.machpelah(p, w, h, seed) + M.esau_old(p, w * 0.5, h * 0.88, fit(h * 0.88, h * 0.42), flip=True)
            + L.jacob_man(p, w * 0.6, h * 0.88, fit(h * 0.88, h * 0.42), flip=True))

def seir(p, w, h, seed):
    """Esau went into a land away from his brother: the red mount Seir, his caravan going up into it."""
    b = h * 0.86
    return (sun(w * 0.2, h * 0.2, 16, color="#FFE680", op=0.25)
            + f'<path d="M{f(w * 0.3)} {f(b)} L {f(w * 0.56)} {f(h * 0.2)} L {f(w * 0.74)} {f(h * 0.34)} L {f(w * 0.9)} {f(h * 0.16)} L {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(b)} Z" fill="#B5421E" stroke="#0D0D0F" stroke-width="2.4"></path>'
            + ground(w, h, b, "#C8885A", dy=0) + Z.caravan(p, w * 0.04, w * 0.5, b + 4, 0.6, seed) + label(w * 0.74, h * 0.48, "MOUNT SEIR", "#F3EFE6", 11))

def kings_of_edom(w, h, seed):
    """The kings that reigned in Edom: eight crowns in a line, each struck as the next reigned in his stead."""
    o = [mk.stars(40, w, h, seed)]
    names = ["BELA", "JOBAB", "HUSHAM", "HADAD", "SAMLAH", "SHAUL", "BAAL-HANAN", "HADAR"]
    for i, nm in enumerate(names):
        x = w * (0.07 + i * 0.123)
        o.append(A2.crown(x, h * 0.56, 0.5) + label(x, h * 0.78, nm, "#FFD23F" if i == 7 else "#C8C2B6", 8.5, ls=0.04))
        if i < 7: o.append(f'<path d="M{f(x + 20)} {f(h * 0.5)} L {f(x + w * 0.1)} {f(h * 0.5)}" stroke="#5A5A7A" stroke-width="2" stroke-dasharray="4 3"></path>')
    return "".join(o)
