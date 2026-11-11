"""Drawings for Romans chapter 4 (Romans 9–11), on top of rom.art3. The emblems of Israel's gifts; Sarah old with the child
of promise at the tent door; the lineage of the promise (Abraham, Isaac, Esau and Jacob); the cleft of the rock with the
glory passing (God never drawn); Pharaoh before his pylon gate (the black-and-gold nemes, as Exodus draws him); the potter
at his wheel (Jeremiah's drawing); the vessels of wrath and the vessels of mercy; the nations called at dawn; the sand of
the sea and the remnant; the smoke over the empty plain of Sodom (words only); the stone of stumbling in the road to Zion;
the plate of heaven and the abyss, the word nigh thee; the herald on the mountains at dawn (how beautiful are the feet);
the sound gone out into all the earth (Acts' map); Jerusalem at dusk, its gates open; Elijah at the mouth of the cave on
Horeb (1 Kings' drawing); the table in the dark; the olive tree as a botanical plate — the root, the natural branches,
some broken off, and the wild olive grafted in; Zion at dawn."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from rom.art3 import *
from rom.art3 import f, INK, GOLD, CY, plate_label, _heart, abraham, sarah_old, ABRAM_ROBE
from rom.art import _tablets
from rom.art2 import SARAI_ROBE
from epistle import paul_fig, robed
from jer.art6 import potter as _potter
from kg1.art import horeb_cave, elijah_fig
from exo.art import NEMES
from exo.art2 import palace_gate
import ruth1 as R1
from oba.minor import mount_zion

def israel_gifts(w, h):
    """Whose is the adoption, and the glory, and the covenants, and the giving of the law, and the service of God, and the
    promises; whose are the fathers: a plate of seven emblems in a row, each in its medallion."""
    o = [plate_bg(w, h, "ROMANS 9:4–5 · TO WHOM PERTAINETH")]
    names = ["THE ADOPTION", "THE GLORY", "THE COVENANTS", "THE LAW", "THE SERVICE", "THE PROMISES", "THE FATHERS"]
    n = len(names); R = min(w / (n * 2.5), h * 0.22); cy = h * 0.55
    for i, t in enumerate(names):
        cx = w * (i + 0.5) / n
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R)}" fill="#12304A" stroke="{GOLD}" stroke-width="2"></circle>')
        k = R / 40
        if i == 0: o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(14 * k)}" fill="none" stroke="#E8B830" stroke-width="{f(5 * k)}"></circle>')
        elif i == 1: o.append(halo(cx, cy, 30 * k, "#FFF4C2", 0.8) + rays(cx, cy, 12, 10 * k, 30 * k, "#FFF4C2", 0.6, 2))
        elif i == 2: o.append(f'<path d="M{f(cx - 24 * k)} {f(cy + 10 * k)} C {f(cx - 20 * k)} {f(cy - 30 * k)} {f(cx + 20 * k)} {f(cy - 30 * k)} {f(cx + 24 * k)} {f(cy + 10 * k)}" fill="none" stroke="#8FD0E2" stroke-width="{f(4 * k)}"></path>'
                              f'<path d="M{f(cx - 18 * k)} {f(cy + 10 * k)} C {f(cx - 14 * k)} {f(cy - 18 * k)} {f(cx + 14 * k)} {f(cy - 18 * k)} {f(cx + 18 * k)} {f(cy + 10 * k)}" fill="none" stroke="#FFD23F" stroke-width="{f(4 * k)}"></path>')
        elif i == 3: o.append(_tablets(cx, cy + 4 * k, 0.32 * k))
        elif i == 4: o.append(f'<path d="M{f(cx)} {f(cy + 24 * k)} L {f(cx)} {f(cy - 14 * k)}" stroke="#E8B830" stroke-width="{f(3 * k)}"></path>'
                              + "".join(f'<path d="M{f(cx)} {f(cy + 8 * k)} C {f(cx + d * 6 * k)} {f(cy)} {f(cx + d * 14 * k)} {f(cy - 2 * k)} {f(cx + d * 14 * k)} {f(cy - 14 * k)}" fill="none" stroke="#E8B830" stroke-width="{f(3 * k)}"></path>' for d in (-1, 1))
                              + "".join(E.flame(cx + d * 14 * k, cy - 16 * k, 3 * k, 9 * k, 1) for d in (-1, 0, 1)))
        elif i == 5: o.append(mk.stars(14, 2 * R, 2 * R, 95 + i).replace('<g fill="#F3EFE6">', f'<g fill="#FFF4C2" transform="translate({f(cx - R * 0.8)} {f(cy - R * 0.8)}) scale(0.8)">', 1))
        else: o.append("".join(f'<path d="M{f(cx + d * 14 * k - 10 * k)} {f(cy + 16 * k)} L {f(cx + d * 14 * k)} {f(cy - 8 * k)} L {f(cx + d * 14 * k + 10 * k)} {f(cy + 16 * k)} Z" fill="#3A2214" stroke="#C8A06A" stroke-width="1.4"></path>' for d in (-1, 0, 1)))
        o.append(label(cx, cy + R + 16, t, GOLD, max(7, min(9.5, R / 4.6))))
    return "".join(o)

def child_promise(p, w, h, seed):
    """Sarah shall have a son: Sarah, grey-haired, sitting at the tent door at morning with the child Isaac in her arms,
    Abraham standing by (Genesis' colours)."""
    b = h * 0.93
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#8FB0D8", "#FFE6B0"), sun(w * 0.86, h * 0.2, max(14, h * 0.05), color="#FFE680", op=0.4),
         hills(w, h, h * 0.6, seed, color="#B8A07A", amp=10, step=90), ground(w, h, h * 0.66, "#C8A06A", dy=0)]
    o.append(G1.tent_big(w * 0.66, b, w * 0.5, h * 0.6, color="#3A2214"))
    s = (h * 0.66) / 205
    o.append(abraham(p, w * 0.26, b, s, flip=True))
    o.append(sarah_old(p, w * 0.44, b, s, up=R1.HOLD_BABY))
    o.append(R1.baby(w * 0.44 + 10 * s * 0.94, b - 130 * s * 0.94, s * 0.8))
    return "".join(o)

def promise_line(w, h):
    """The children of the promise: a lineage plate — ABRAHAM, ISAAC (In Isaac shall thy seed be called), and of Rebecca the
    twins ESAU and JACOB, the line of the promise lit, THE ELDER SHALL SERVE THE YOUNGER."""
    o = [plate_bg(w, h, "ROMANS 9:7–13 · THE CHILDREN OF THE PROMISE")]
    pts = {"ABRAHAM": (0.14, 0.5), "ISAAC": (0.38, 0.5), "ESAU": (0.66, 0.32), "JACOB": (0.66, 0.72)}
    P = {k: (w * x, h * y) for k, (x, y) in pts.items()}
    o.append(route([P["ABRAHAM"], P["ISAAC"]], color=GOLD, sw=3, dash="") + route([P["ISAAC"], P["JACOB"]], color=GOLD, sw=3, dash="")
             + route([P["ISAAC"], P["ESAU"]], color="#6A7A9A", sw=2, dash="6 5"))
    for k_, (x, y) in P.items():
        c = "#6A8AB0" if k_ == "ESAU" else GOLD
        o.append(node(x, y, "", c, r=8) + plate_label(x, y - 18, k_, c, 11))
    o.append(plate_label(P["ESAU"][0] + 70, P["ESAU"][1] + 4, "THE ELDER", "#8AA0C0", 9, "start") + plate_label(P["JACOB"][0] + 70, P["JACOB"][1] + 4, "THE YOUNGER", GOLD, 9, "start"))
    o.append(plate_label(P["ISAAC"][0], P["ISAAC"][1] + 26, "SARAH · REBECCA", CY, 9))
    return "".join(o)

def cleft_rock(w, h, seed):
    """I will have mercy on whom I have mercy (said to Moses on the mount): a cleft in the rock of the mountain, a great light
    passing before it (God never drawn)."""
    o = [sky(w, h, "#2A2A4A", "#6A5A7A"), halo(w * 0.62, h * 0.4, max(w, h) * 0.55, "#FFF4C2", 0.75), rays(w * 0.62, h * 0.4, 30, h * 0.08, max(w, h), "#FFFDF0", 0.3, 4)]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.2)} L {f(w * 0.18)} {f(h * 0.1)} L {f(w * 0.4)} {f(h * 0.3)} L {f(w * 0.44)} {f(h + 10)} Z" fill="#5A4A4A" stroke="{INK}" stroke-width="2.6"></path>'
             f'<path d="M{f(w * 0.22)} {f(h * 0.3)} L {f(w * 0.3)} {f(h * 0.34)} L {f(w * 0.28)} {f(h * 0.9)} L {f(w * 0.2)} {f(h * 0.86)} Z" fill="#120A0A" stroke="{INK}" stroke-width="2"></path>')
    for i in range(5):
        y = h * (0.3 + i * 0.12)
        o.append(f'<path d="M{f(w * 0.02)} {f(y)} L {f(w * 0.16)} {f(y + 8)}" stroke="#3A2E2E" stroke-width="2"></path>')
    return "".join(o)

def pharaoh_gate(p, w, h, seed):
    """For this very purpose did I raise thee up: Pharaoh standing before his pylon gate under the sun, in the black-and-gold
    nemes and white robe of Exodus."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#C8A060", "#FFE6A0"), palace_gate(p, w, h, seed)]
    s = (h * 0.62) / 205
    o.append(robed(p, w * 0.5, b, s, "#F3EFE6", skin="#8A4A2E", belt="#E8B830", extra=NEMES))
    return "".join(o)

def potter_wheel(p, w, h, seed):
    """Hath not the potter a right over the clay: the potter at his wheel with a vessel on it (Jeremiah's potter's house),
    without the prophet."""
    return _potter(p, w, h, seed, prophet=False)

def _jar(x, y, s, fill, cracked=False, glow_=False):
    o = (halo(x, y - 40 * s, 60 * s, "#FFE680", 0.5) if glow_ else "")
    o += (f'<path d="M{f(x - 14 * s)} {f(y - 80 * s)} L {f(x + 14 * s)} {f(y - 80 * s)} L {f(x + 12 * s)} {f(y - 70 * s)} C {f(x + 40 * s)} {f(y - 60 * s)} {f(x + 40 * s)} {f(y - 10 * s)} {f(x + 14 * s)} {f(y)} '
          f'L {f(x - 14 * s)} {f(y)} C {f(x - 40 * s)} {f(y - 10 * s)} {f(x - 40 * s)} {f(y - 60 * s)} {f(x - 12 * s)} {f(y - 70 * s)} Z" fill="{fill}" stroke="{INK}" stroke-width="2"></path>')
    if cracked: o += f'<path d="M{f(x - 6 * s)} {f(y - 66 * s)} L {f(x + 4 * s)} {f(y - 46 * s)} L {f(x - 6 * s)} {f(y - 30 * s)} L {f(x + 6 * s)} {f(y - 12 * s)}" fill="none" stroke="#0D0D0F" stroke-width="2"></path>'
    return o

def vessels(w, h):
    """Vessels of wrath fitted unto destruction, vessels of mercy prepared unto glory: a plate — grey cracked jars at the
    left, gold jars in light at the right, the same clay."""
    o = [plate_bg(w, h, "ROMANS 9:21–23 · FROM THE SAME LUMP")]
    s = min(1.4, (h - 60) / 110); y = h - 30
    for i in range(3): o.append(_jar(w * (0.12 + i * 0.11), y, s * (0.9 + 0.1 * (i % 2)), "#5A5A64", cracked=True))
    for i in range(3): o.append(_jar(w * (0.66 + i * 0.11), y, s * (0.9 + 0.1 * (i % 2)), "#E8B830", glow_=True))
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(y - 14)}" rx="{f(30 * s)}" ry="{f(16 * s)}" fill="#B8784A" stroke="{INK}" stroke-width="2"></ellipse>' + label(w * 0.5, y + 16, "THE CLAY", "#C8A07A", 9))
    o.append(label(w * 0.23, 52, "VESSELS OF WRATH · UNTO DISHONOR", "#C8C8E8", 9.5) + label(w * 0.77, 52, "VESSELS OF MERCY · UNTO HONOR", GOLD, 9.5))
    return "".join(o)

CROWD_CLOTH = ["#3A4A6A", "#2A3A4A", "#5A4A6A", "#3A5A5A", "#4A3A3A", "#2A2A3A", "#5A5A6A", "#3A4A3A", "#6A5A4A", "#E8E2D6"]
CROWD_HEAD = ["#E8E2D6", "#2A2A4A", "#1F3A4A", "#3A3A4A", "#4A4A5A", "#1A2A3A", "#D8D2C6"]

def crowd_back(p, w, h, seed, rows=3, height=0.5, base=0.99, x0=-0.02, x1=1.02, ups=0.0, women=0.45):
    """A crowd seen from behind, standing in overlapping rows on the kit silhouettes (epistle.robed): men in headcloths with
    cords or bareheaded, women veiled, cool and dark cloths with a few off-white; the front row `height` of the drawing tall,
    each row behind a little smaller and higher; ups= the share with an arm lifted. Needs mk.defs(p, *ALL, "ManUp",
    "WomanUp") in the panel (the function adds it)."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp")]
    for j in range(rows):                                          # the back row first
        depth = rows - 1 - j
        by = h * (base - depth * 0.07); s = h * (height - depth * 0.07) / 205
        n = max(3, int((x1 - x0) * w / (30 * s)))
        for i in range(n):
            x = w * (x0 + (x1 - x0) * (i + 0.5) / n) + r.uniform(-6, 6) * s + (15 * s if j % 2 else 0)
            woman = r.random() < women
            cloth = r.choice(CROWD_CLOTH); hd = r.choice(CROWD_HEAD)
            up = [(-22, -158), (-46, -182), (-52, -214)] if r.random() < ups else None
            back = f'<circle cx="0" cy="-190" r="13.6" fill="{hd if (woman or r.random() < 0.7) else "#2A1A10"}" stroke="#0D0D0F" stroke-width="1.6"></circle>'
            ss = s * r.uniform(0.94, 1.04)
            if woman: o.append(robed(p, x, by, ss * 0.95, cloth, woman=True, veil=hd, flip=r.random() < 0.5, up=up, extra=back))
            else: o.append(robed(p, x, by, ss, cloth, head=hd, cord="#1A1210", mantle=r.choice([None, "#2A2A34", "#4A3A2A"]), flip=r.random() < 0.5, up=up, extra=back))
    return "".join(o)

def nations_dawn(p, w, h, seed):
    """I will call that my people, which was not my people: the peoples of the nations, men and women, seen from behind in a
    great company on the plain at dawn, looking toward the light; a city of the Gentiles on the far hill."""
    o = [sky(w, h, "#4A3A6A", "#FFC890"), halo(w * 0.6, h * 0.34, max(w, h) * 0.4, "#FFF4C2", 0.6), hills(w, h, h * 0.3, seed, color="#6A5A6A", amp=12, step=90),
         walls(w * 0.52, w * 0.84, h * 0.34, h * 0.14, seed, towers=2), ground(w, h, h * 0.36, "#8A7A5A", dy=0)]
    o.append(crowd_back(p, w, h, seed, rows=3, height=0.52))
    return "".join(o)

def sand_shore(w, h, seed):
    """As the sand of the sea: an endless shore at evening, the sand reaching away to the horizon, the waves on it (no one)."""
    o = [sky(w, h, "#4A5A8A", "#F3C890"), sea_(w, h, h * 0.42, seed, color="#2C6A8A", deep="#1A4A6A"),
         f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.3)} {f(h * 0.5)} {f(w * 0.7)} {f(h * 0.58)} {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#E8D0A0" stroke="{INK}" stroke-width="2"></path>']
    r = random.Random(seed)
    o.append("".join(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.62, h))}" r="{f(r.uniform(0.6, 1.6))}" fill="#B8985A"></circle>' for _ in range(int(w * h / 600))))
    return "".join(o)

def sodom_plain(w, h, seed):
    """We had become as Sodom: the plain by the Salt Sea at evening, smoke going up from the ground as the smoke of a furnace,
    no city left, no one (words only)."""
    return vista(w, h, seed, tone="red", horizon=0.62, hills_n=2, ruins=True, smoke_=4, city="ruin", cx=0.55, cw=0.6)

def stumbling_stone(w, h, seed):
    """Behold, I lay in Zion a stone of stumbling and a rock of offence: the road climbing to mount Zion, and lying in the
    road a great hewn corner-stone."""
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), mount_zion(w * 0.62, h * 0.66, w * 0.34, h * 0.55, seed), ground(w, h, h * 0.66, "#C8B07A", dy=0)]
    o.append(f'<path d="M{f(w * 0.2)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.86)} {f(w * 0.46)} {f(h * 0.76)} {f(w * 0.56)} {f(h * 0.68)}" stroke="#E8D8B0" stroke-width="{f(max(14, h * 0.12))}" fill="none"></path>')
    from exo.art8 import box
    k = min(1.6, h / 240)
    o.append(box(w * 0.3, h * 0.94, 90 * k, 40 * k, 46 * k, fill="#B8B0A0", top="#D8D0C0", side="#8A8278"))
    return "".join(o)

def nigh_plate(w, h):
    """Say not in thy heart, Who shall ascend into heaven? or, Who shall descend into the abyss? The word is nigh thee, in thy
    mouth, and in thy heart: a plate — the heavens above, the abyss below, the arrows up and down crossed out, and between
    them a man with the word at his mouth and in his heart."""
    o = [plate_bg(w, h, "ROMANS 10:6–8 · THE WORD IS NIGH THEE"), mk.defs("np106", *ALL)]
    o.append(f'<rect x="0" y="34" width="{f(w)}" height="{f(h * 0.14)}" fill="#14204A"></rect>' + label(w * 0.82, 34 + h * 0.08, "HEAVEN", "#C8D8FF", 10)
             + f'<rect x="0" y="{f(h * 0.86)}" width="{f(w)}" height="{f(h * 0.14)}" fill="#05050E"></rect>' + label(w * 0.82, h * 0.94, "THE ABYSS", "#8A8AA8", 10))
    cx = w * 0.32
    for y0, y1 in ((h * 0.36, 40 + h * 0.1), (h * 0.66, h * 0.88)):
        o.append(route([(cx, y0), (cx, y1)], color="#FF6A4A", sw=2) + f'<path d="M{f(cx - 12)} {f((y0 + y1) / 2 - 12)} L {f(cx + 12)} {f((y0 + y1) / 2 + 12)} M{f(cx + 12)} {f((y0 + y1) / 2 - 12)} L {f(cx - 12)} {f((y0 + y1) / 2 + 12)}" stroke="#FF6A4A" stroke-width="3"></path>')
    s = (h * 0.5) / 205; mx = w * 0.56; by = h * 0.8
    o.append(mk.person("np106", round(mx), round(by), round(s, 3), body="#1E4A6A", cloth="#163A56", kind="Tunic", stroke=CY, sw=2.4, flip=True))
    o.append(halo(mx, by - 120 * s, 26 * s, "#FFE680", 0.7) + halo(mx + 8 * s, by - 186 * s, 16 * s, "#FFE680", 0.7))
    o.append(tag(mx + 10 * s, by - 184 * s, "IN THY MOUTH", mx + 80 * s, by - 200 * s, color=GOLD) + tag(mx, by - 122 * s, "IN THY HEART", mx + 90 * s, by - 110 * s, color=GOLD))
    return "".join(o)

def herald(p, w, h, seed):
    """How beautiful are the feet of them that bring glad tidings of good things: a messenger on the mountain ridge at dawn,
    his arm lifted, coming down the path toward the city below."""
    b = h * 0.6
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#2A2A6A", "#FFC890"), halo(w * 0.7, h * 0.5, max(w, h) * 0.4, "#FFF4C2", 0.6),
         f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.2)} {f(h * 0.5)} L {f(w * 0.34)} {f(b)} L {f(w * 0.56)} {f(h * 0.62)} L {f(w * 0.8)} {f(h * 0.44)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#4A3A5A" stroke="{INK}" stroke-width="2.4"></path>',
         walls(w * 0.04, w * 0.3, h * 0.96, h * 0.18, seed, towers=2, lit=True),
         f'<path d="M{f(w * 0.36)} {f(b + 2)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.28)} {f(h * 0.78)} {f(w * 0.22)} {f(h * 0.8)}" stroke="#C8A890" stroke-width="5" fill="none"></path>']
    s = (h * 0.42) / 205
    o.append(robed(p, w * 0.36, b + 2, s, "#E8D8B0", hair="#2A1A10", beard="#2A1A10", belt="#8A5A30", up=[(-22, -158), (-30, -196), (-40, -232)]))
    return "".join(o)

def all_the_earth(w, h):
    """Their sound went out into all the earth: the whole map of Acts with rings of the word going out over every land."""
    import act.geo as G_
    return G_.med_map(w, h, box=(-6, 56, 22, 47), places=("JERUSALEM", "ROME", "ANTIOCH", "ALEXANDRIA", "ATHENS"), hi=("JERUSALEM",), rings="JERUSALEM",
                      regions=("ITALY", "EGYPT", "ASIA", "MESOPOTAMIA", "ARABIA", "PARTHIA"), title="ROMANS 10:18 · UNTO THE ENDS OF THE WORLD", size=8)

def jerusalem_dusk(w, h, seed):
    """All the day long did I spread out my hands unto a disobedient and gainsaying people: Jerusalem on its hill at dusk, its
    gate open, the light of the evening on the house (God never drawn)."""
    return vista(w, h, seed, tone="dusk", horizon=0.66, far="zion", cx=0.55, cw=0.6, sun_at=(0.85, 0.5))

def elijah_cave(p, w, h, seed):
    """Elijah at Horeb: the mouth of the cave in the mount (1 Kings' drawing), the prophet in its entrance, his face wrapped
    in his mantle."""
    return horeb_cave(p, w, h, seed, stage="still")

def dark_table(w, h, seed):
    """Let their table be made a snare, and a trap: a set table in a dark hall, the lamps out, a snare's cord lying across
    it (no one)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1418"></rect>']
    ty = h * 0.62; k = min(1.4, h / 260)
    o.append(f'<rect x="{f(w * 0.12)}" y="{f(ty)}" width="{f(w * 0.76)}" height="{f(12 * k)}" fill="#4A2A1A" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(x)}" y="{f(ty + 12 * k)}" width="{f(10 * k)}" height="{f(h * 0.3)}" fill="#3A1E12" stroke="{INK}" stroke-width="1.6"></rect>' for x in (w * 0.16, w * 0.82)))
    for i in range(5):
        x = w * (0.2 + i * 0.14)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(ty - 4)}" rx="{f(22 * k)}" ry="{f(6 * k)}" fill="#6A5A4A" stroke="{INK}" stroke-width="1.4"></ellipse>')
    o.append(f'<path d="M{f(w * 0.1)} {f(ty - 2)} C {f(w * 0.3)} {f(ty - 20 * k)} {f(w * 0.5)} {f(ty + 10 * k)} {f(w * 0.7)} {f(ty - 14 * k)} C {f(w * 0.76)} {f(ty - 20 * k)} {f(w * 0.8)} {f(ty - 6)} {f(w * 0.84)} {f(ty - 30 * k)}" '
             f'fill="none" stroke="#C8A060" stroke-width="2.4"></path><circle cx="{f(w * 0.84)}" cy="{f(ty - 38 * k)}" r="{f(8 * k)}" fill="none" stroke="#C8A060" stroke-width="2.4"></circle>')
    o.append(f'<g opacity="0.6">{clay_lamp(w * 0.5, ty - 6, k)}</g>')
    return "".join(o)

def olive_graft(w, h, again=False):
    """The olive tree: a botanical plate — the trunk on its root (THE ROOT), the natural branches in leaf, some broken off and
    falling away (dashed, BROKEN OFF BY UNBELIEF), and a branch of the wild olive grafted in among them, bound at the graft
    (GRAFTED IN · STANDEST BY THY FAITH), partaker of the root of the fatness."""
    o = [plate_bg(w, h, "ROMANS 11:17–24 · THE OLIVE TREE")]
    cx, base = w * 0.48, h * 0.86; k = min(w / 700, h / 380)
    o.append(f'<path d="M{f(cx - 40 * k)} {f(base)} C {f(cx - 70 * k)} {f(base + 20 * k)} {f(cx - 120 * k)} {f(base + 26 * k)} {f(cx - 160 * k)} {f(base + 40 * k)} M{f(cx + 30 * k)} {f(base)} C {f(cx + 60 * k)} {f(base + 24 * k)} {f(cx + 130 * k)} {f(base + 22 * k)} {f(cx + 170 * k)} {f(base + 40 * k)} '
             f'M{f(cx)} {f(base)} L {f(cx + 6 * k)} {f(base + 44 * k)}" stroke="#8A6A3A" stroke-width="{f(7 * k)}" fill="none"></path>')
    o.append(f'<path d="M{f(cx - 34 * k)} {f(base)} C {f(cx - 20 * k)} {f(base - 80 * k)} {f(cx - 30 * k)} {f(base - 140 * k)} {f(cx - 10 * k)} {f(base - 190 * k)} L {f(cx + 18 * k)} {f(base - 190 * k)} '
             f'C {f(cx + 30 * k)} {f(base - 140 * k)} {f(cx + 20 * k)} {f(base - 80 * k)} {f(cx + 34 * k)} {f(base)} Z" fill="#6A5A40" stroke="{CY}" stroke-width="2"></path>')
    branches = [(-1, 0.55, 170, False), (1, 0.6, 180, False), (-1, 0.8, 150, True), (1, 0.82, 140, False), (-1, 0.98, 120, False), (1, 1.0, 110, True)]
    leaf = lambda x, y, c: f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(9 * k)}" ry="{f(3.6 * k)}" transform="rotate(-20 {f(x)} {f(y)})" fill="{c}" stroke="#0D0D0F" stroke-width="0.8"></ellipse>'
    for d, t, L, broken in branches:
        y0 = base - 190 * k * t; x0 = cx + d * 8 * k
        x1, y1 = x0 + d * L * k, y0 - 50 * k
        if broken and not again:
            o.append(f'<path d="M{f(x0)} {f(y0)} L {f(x0 + d * 16 * k)} {f(y0 - 6 * k)}" stroke="#6A5A40" stroke-width="{f(6 * k)}"></path>'
                     f'<path d="M{f(x0 + d * 30 * k)} {f(y0 + 18 * k)} Q {f(x0 + d * L * 0.6 * k)} {f(y0 + 10 * k)} {f(x1 + d * 10 * k)} {f(y0 + 50 * k)}" stroke="#7A6A5A" stroke-width="{f(4 * k)}" stroke-dasharray="6 4" fill="none"></path>'
                     + "".join(leaf(x0 + d * (40 + j * 18) * k, y0 + (16 + j * 5) * k, "#7A7A5A") for j in range(5)))
            if d < 0: o.append(tag(x0 + d * 70 * k, y0 + 26 * k, "BROKEN OFF · BY UNBELIEF", 30, y0 + 70 * k, color="#FF8A6A"))
        else:
            o.append(f'<path d="M{f(x0)} {f(y0)} Q {f((x0 + x1) / 2)} {f(y0 - 40 * k)} {f(x1)} {f(y1)}" stroke="#6A5A40" stroke-width="{f(6 * k)}" fill="none"></path>'
                     + "".join(leaf(x0 + (x1 - x0) * (j + 1) / 7, y0 - 34 * k * (j + 1) / 7 - (6 * k if j % 2 else -6 * k), "#5E8A4A") for j in range(7)))
            if broken:                                  # again: the natural branch grafted into its own olive tree, bound at the graft
                o.append(f'<rect x="{f(x0 + d * 8 * k - 8 * k)}" y="{f(y0 - 10 * k)}" width="{f(16 * k)}" height="{f(10 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="1.2"></rect>')
                if d < 0: o.append(tag(x0 + d * 10 * k, y0 - 6 * k, "GRAFTED IN AGAIN", 30, y0 + 50 * k, color=GOLD))
    gx0, gy0 = cx + 10 * k, base - 190 * k * 0.8
    gx1, gy1 = gx0 + 150 * k, gy0 - 80 * k
    o.append(f'<path d="M{f(gx0)} {f(gy0)} Q {f(gx0 + 70 * k)} {f(gy0 - 60 * k)} {f(gx1)} {f(gy1)}" stroke="#A88A50" stroke-width="{f(5 * k)}" fill="none"></path>'
             + "".join(leaf(gx0 + (gx1 - gx0) * (j + 1) / 7, gy0 + (gy1 - gy0) * (j + 1) / 7 - 20 * k * math.sin((j + 1) / 7 * 3.1) + (5 * k if j % 2 else -5 * k), "#A8B85A") for j in range(7))
             + f'<rect x="{f(gx0 - 4 * k)}" y="{f(gy0 - 12 * k)}" width="{f(16 * k)}" height="{f(10 * k)}" fill="#C8A060" stroke="{INK}" stroke-width="1.2" transform="rotate(-30 {f(gx0)} {f(gy0)})"></rect>')
    o.append(tag(gx0 + 4 * k, gy0 - 8 * k, "GRAFTED IN · THE WILD OLIVE", w - 20, gy0 - 30 * k, color=GOLD))
    o.append(tag(cx, base + 30 * k, "THE ROOT · THE FATNESS", w - 20, base + 10 * k, color=CY))
    return "".join(o)

def zion_dawn(w, h, seed):
    """There shall come out of Zion the Deliverer: mount Zion at dawn, the light rising behind the city."""
    return vista(w, h, seed, tone="dawn", horizon=0.66, far="zion", cx=0.5, cw=0.6, glow_at=(0.5, 0.36, 0.5, "#FFF4C2"))
