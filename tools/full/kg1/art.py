"""Drawings for the 1 Kings volume (chapter by chapter, added below). The 2 Samuel, 1 Samuel, Judges and Joshua drawings are
reused where they fit (sa2.art, sa1.art, jdg.art, jos.art).

Solomon at a distance: a deep-blue tunic and the gold crown (sol_fig). David old: purple (sa2.art.old_king). Bath-sheba:
a plum robe. Elijah: a brown hairy mantle with a leather girdle, bareheaded. Ahab: crimson with the crown. Jezebel: black
and gold."""
import sys, pathlib, random, math, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, numbers1 as N, joshua1 as J, judges1 as J1, samuel1 as S1, samuel2 as S2, samuel3 as S3, samuel4 as S4
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg, node, route
from exo import art as A
from num.art import ALL, TRIBE_C
from jos.art import crowd_at, below, night, WAR, warrior
from sa2.art import sky, king_fig, captain, old_king, CROWN

def f(v): return f"{v:.1f}"
SOL_C, BATH_C, ELIJAH_C, AHAB_C = "#1F3A7A", "#7A3A6A", "#6A4A2A", "#7A1A2A"

def sol_fig(p, x, y, s, flip=False, up=None):
    """Solomon at a distance: deep-blue tunic and the gold crown."""
    return king_fig(p, x, y, s, flip=flip, up=up, cloth=SOL_C)

def priest(p, x, y, s, flip=False, up=None):
    """Zadok at a distance: white robe and headcloth, white beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#F3EFE6", sw=3, flip=flip, up=up, extra=A.headcloth("#F3EFE6") + A.WHITE_BEARD)

def prophet_fig(p, x, y, s, cloth="#5E7A4A", flip=False, up=None, beard=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, sw=3, flip=flip, up=up, extra=A.headcloth(cloth) + (beard or A.WHITE_BEARD))

def horned_altar(x, y, s=1.0, fire=False, seed=1):
    """An altar with a horn at each corner; (x, y) = its foot."""
    o = (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><rect x="-60" y="-90" width="120" height="90" fill="#B07A3A" stroke="#0D0D0F" stroke-width="2.6"></rect>'
         '<rect x="-66" y="-98" width="132" height="12" fill="#C8963E" stroke="#0D0D0F" stroke-width="2.4"></rect>'
         + "".join(f'<path d="M{dx - 8} -98 L {dx} -122 L {dx + 8} -98 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>' for dx in (-58, 58))
         + '<path d="M-60 -50 L 60 -50" stroke="#7A4A1A" stroke-width="2"></path></g>')
    if fire: o += E.blaze(x, y - 98 * s, 50 * s, 70 * s, seed, n=5)
    return o

def bed(w, h, x0, x1, b, cover="#4A2A7A", head="#C98E66", hair="#B8A89A"):
    """A bed with a figure under its covering, the head on the left."""
    hh = h * 0.12
    return (f'<rect x="{f(x0)}" y="{f(b - hh * 1.6)}" width="{f(x1 - x0)}" height="{f(hh)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></rect>'
            f'<path d="M{f(x0)} {f(b - hh * 1.6)} L {f(x0)} {f(b - hh * 2.8)}" stroke="#5A3A1E" stroke-width="10"></path>'
            f'<path d="M{f(x0 + 8)} {f(b - hh * 1.6)} C {f(x0 + (x1 - x0) * 0.1)} {f(b - hh * 2.6)} {f(x1 - (x1 - x0) * 0.1)} {f(b - hh * 2.6)} {f(x1 - 8)} {f(b - hh * 1.6)} Z" fill="{cover}" stroke="#0D0D0F" stroke-width="2.4"></path>'
            f'<circle cx="{f(x0 + hh * 0.5)}" cy="{f(b - hh * 2.1)}" r="{f(hh * 0.36)}" fill="{head}" stroke="#0D0D0F" stroke-width="2"></circle>'
            f'<path d="M{f(x0 + hh * 0.14)} {f(b - hh * 2.1)} C {f(x0 + hh * 0.2)} {f(b - hh * 2.6)} {f(x0 + hh * 0.8)} {f(b - hh * 2.6)} {f(x0 + hh * 0.86)} {f(b - hh * 2.0)}" fill="{hair}"></path>')

# ---- 1 Kings 1 ----------------------------------------------------------------------------------------------------------
def old_bed(p, w, h, seed):
    """King David old and stricken in years in his chamber, covered with clothes; Abishag the Shunammite ministering."""
    from genesis.art4 import clay_lamp
    b = h * 0.92
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), bed(w, h, w * 0.1, w * 0.62, b), clay_lamp(w * 0.9, h * 0.5, min(1.2, h / 260))]
    o.append(woman(p, w * 0.76, b, fit(b, h * 0.36), "#2A6A6A", flip=True))
    return "".join(o)

def zoheleth(p, w, h, seed):
    """The stone of Zoheleth beside En-rogel: sheep and oxen slain, the fire of the feast, the guests at Adonijah's table."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#E8B880", "#F3D8A0"), hills(w, h, h * 0.44, seed, color="#9A7A5A", amp=14), ground(w, h, h * 0.56, "#B89A6A", dy=0),
         f'<path d="M{f(w * 0.06)} {f(b)} C {f(w * 0.06)} {f(h * 0.5)} {f(w * 0.12)} {f(h * 0.4)} {f(w * 0.18)} {f(h * 0.42)} C {f(w * 0.24)} {f(h * 0.46)} {f(w * 0.26)} {f(h * 0.6)} {f(w * 0.26)} {f(b)} Z" fill="#8A8478" stroke="#0D0D0F" stroke-width="2.4"></path>',
         S4.altar(w * 0.36, b, min(1.0, h / 360), seed=seed)]
    s = fit(b, h * 0.36)
    for i in range(5):
        o.append(man(p, w * (0.52 + i * 0.09), b - h * 0.05, s * 0.75, ["#B5652E", "#6A2A1A", "#F3EFE6", "#5A5A2A", "#3A4A6A"][i], flip=i % 2 == 1))
    o.append(S3.table(w * 0.7, b, w * 0.44, min(1.1, h / 320)))
    return "".join(o)

def chamber(p, w, h, seed, who="bath"):
    """The king's chamber: David old on his bed, one bowing before him (who: bath / nathan), Abishag standing by."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), bed(w, h, w * 0.04, w * 0.44, b)]
    s = fit(b, h * 0.4)
    if who == "bath": o.append(E.kneel(w * 0.62, b, s * 0.8, color=BATH_C, skin="#D9A27A", flip=True))
    else: o.append(N.prostrate(w * 0.64, b, s * 0.8, color="#5E7A4A", skin="#C98E66", flip=True))
    o.append(woman(p, w * 0.9, b, s * 0.9, "#2A6A6A", flip=True))
    return "".join(o)

def gihon(p, w, h, seed, anoint=False):
    """Solomon riding upon king David's mule down to Gihon, the priest and the prophet, the Cherethites and the Pelethites; and
    (anoint=True) Zadok pouring the horn of oil, the trumpet blown."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), J.city_hill(w * 0.84, h * 0.46, w * 0.32, h * 0.26, seed), ground(w, h, h * 0.5, "#B89A6A", dy=0),
         f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.2)} {f(h * 0.58)} {f(w * 0.36)} {f(h * 0.66)} {f(w * 0.56)} {f(h * 0.6)}" stroke="#2C9DB8" stroke-width="8" fill="none"></path>']
    s = fit(b, h * 0.44); k = min(1.1, h / 300)
    hx, hy = w * 0.36 - 14 * k, b - 40 * k - 200 * 0.62 * k
    if anoint:
        ps = s * 0.9; px = hx + 26 * k + 20 * ps
        o.append(priest(p, px, b, ps, flip=True, up=[(22, -158), (30, -196), (20, -232)]))
    o.append(N.mount(w * 0.36, b, k, flip=False, color="#6A5A4A", rider_cloth=SOL_C, p=p, extra=CROWN))
    if anoint:
        o.append(S1.vial(px - 20 * ps, b - 232 * ps, 0.6 * k, rot=150, pour=max(10, b - 232 * ps - hy + 10)) + S1.drops(hx, hy - 6 * k, 4, seed, spread=10 * k))
        o.append(J.trumpeter(p, w * 0.86, b, s * 0.9, flip=True) + J.blasts(w * 0.86 - 70 * s * 0.9, b - 170 * s * 0.9, s * 0.9))
    else:
        o.append(priest(p, w * 0.66, b, s * 0.95) + prophet_fig(p, w * 0.76, b, s * 0.95))
        for i in range(4): o.append(warrior(p, w * (0.04 + i * 0.06), b - (i % 2) * h * 0.02, s * 0.8, ["#8A2A2A", "#2A4A6A"][i % 2]))
    return "".join(o)

def rejoicing(p, w, h, seed):
    """All the people came up after him piping with pipes, so that the earth rent with the sound of them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE680", "#FFB04A"), V.rays(w * 0.5, h * 0.4, 30, 20, max(w, h), color="#FFF4C2", op=0.3),
         J.city_hill(w * 0.5, h * 0.5, w * 0.7, h * 0.24, seed), ground(w, h, h * 0.52, "#C8A06A", dy=0)]
    s = fit(b, h * 0.4)
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.98, h * 0.62, b, 16, s * 0.5, s))
    o.append(S3.notes(w * 0.5, h * 0.3, 8, seed))
    return "".join(o)

def altar_horns(p, w, h, seed, who="#B5652E", empty=False):
    """Adonijah (or Joab: who=his colour) laid hold on the horns of the altar before the Tent; empty=True: the altar alone."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#3A2A4A", "#C88A6A"), E4.tent(w * 0.76, b, w * 0.4, h * 0.6, color="#E8E2D6", stripe="#8A6A3A"), ground(w, h, b, "#7A6A5A", dy=0),
         horned_altar(w * 0.4, b, min(1.3, h / 260))]
    if not empty: o.append(E.kneel(w * 0.22, b, fit(b, h * 0.4) * 0.8, color=who, skin="#E3B08A"))
    return "".join(o)

# ---- 1 Kings 2 ----------------------------------------------------------------------------------------------------------
import ruth1 as R1
def charge(p, w, h, seed):
    """David on his bed charging Solomon his son, who stands beside it."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), bed(w, h, w * 0.06, w * 0.5, b)]
    o.append(sol_fig(p, w * 0.7, b, fit(b, h * 0.4), flip=True))
    return "".join(o)

def city_dusk(p, w, h, seed):
    """The city of David at dusk, its towers dark against the sky (David slept with his fathers)."""
    o = [sky(w, h, "#2A1A3A", "#E8803A"), sun(w * 0.8, h * 0.62, 26, color="#FF8A3D", op=0.5), J.city_hill(w * 0.46, h * 0.84, w * 0.8, h * 0.46, seed),
         ground(w, h, h * 0.86, "#2A1E2A", dy=0)]
    return "".join(o)

def two_thrones(p, w, h, seed):
    """King Solomon on his throne, and a throne set for the king's mother on his right hand."""
    b = h * 0.92; k = min(1.2, h / 300)
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), S3.throne(w * 0.38, b, k), S3.throne(w * 0.66, b, k * 0.9)]
    s = fit(b, h * 0.4)
    o.append(sol_fig(p, w * 0.38, b - 40 * k, s * 0.86))
    o.append(mk.person(p, round(w * 0.66), round(b - 36 * k), round(s * 0.8, 3), body="#3A1E14", cloth=BATH_C, woman=True, hair="#1A1210", sw=3, flip=True))
    return "".join(o)

def anathoth(p, w, h, seed):
    """Abiathar the priest going home to his fields at Anathoth."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#C8D8E8", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#8A9A6A", amp=12),
         R1.field(-10, w + 10, h * 0.72, h * 0.18, seed), ground(w, h, h * 0.8, "#A89A6A", dy=0)]
    o.append(prophet_fig(p, w * 0.3, b, fit(b, h * 0.4), cloth="#E8E2D6"))
    return "".join(o)

def kidron(p, w, h, seed, ass=False):
    """The brook Kidron below the city wall; ass=True: Shimei with his saddled ass going out on the road toward Gath."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), J.jericho(w * 0.4, w + 10, h * 0.2, h * 0.5, seed, towers=3, houses=True), ground(w, h, h * 0.5, "#A89A6A", dy=0),
         f'<path d="M-10 {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.66)} {f(w * 0.6)} {f(h * 0.74)} {f(w + 10)} {f(h * 0.7)}" stroke="#2C9DB8" stroke-width="12" fill="none"></path>']
    if ass:
        k = min(0.9, h / 360)
        o.append(N.ass(w * 0.24, b, k, flip=True) + mk.person(p, round(w * 0.1), round(b), round(fit(b, h * 0.4) * 0.8, 3), body="#3A1E14", cloth="#6A5A3A", sw=3, flip=True,
                                                               extra=A.headcloth("#6A5A3A") + A.WHITE_BEARD))
    return "".join(o)

# ---- 1 Kings 3–4 --------------------------------------------------------------------------------------------------------
def gibeon(p, w, h, seed):
    """The great high place at Gibeon: the altar on the height smoking with a thousand burnt-offerings, the people below."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#FFB04A", "#F3D8A0"),
         f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.2)} {f(h * 0.5)} {f(w * 0.4)} {f(h * 0.36)} {f(w * 0.56)} {f(h * 0.36)} C {f(w * 0.74)} {f(h * 0.36)} {f(w * 0.86)} {f(h * 0.56)} {f(w + 10)} {f(h * 0.76)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         S4.altar(w * 0.56, h * 0.37, min(1.0, h / 380), seed=seed)]
    for i in range(5):
        o.append(f'<path d="M{f(w * (0.5 + i * 0.03))} {f(h * 0.26)} C {f(w * (0.46 + i * 0.04))} {f(h * 0.16)} {f(w * (0.54 + i * 0.03))} {f(h * 0.08)} {f(w * (0.5 + i * 0.05))} -10" stroke="#6A5A5A" stroke-width="14" fill="none" opacity="0.35"></path>')
    s = fit(b, h * 0.6)
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.98, h * 0.8, b, 14, s * 0.6, s))
    return "".join(o)

def dream(p, w, h, seed):
    """In Gibeon Jehovah appeared to Solomon in a dream by night: the king asleep in his tent under a sky of light (God is
    never drawn)."""
    o = [mk.defs(p, *ALL), night(w, h, seed, "#0F0E2A"), V.rays(w * 0.5, -h * 0.1, 40, 24, h * 1.2, color="#FFD23F", op=0.18),
         ground(w, h, h * 0.8, "#1A1430", dy=0), E4.tent(w * 0.5, h * 0.84, w * 0.6, h * 0.5, color="#2A3A6A", stripe="#1A2040"),
         J1.rug_sleeper(w * 0.5, h * 0.84, min(1.2, h / 280), color=SOL_C)]
    return "".join(o)

def two_women(p, w, h, seed, sword=False):
    """Two women standing before the king on his throne, one holding the living child; sword=True: a sword brought before the
    king (held, not used)."""
    b = h * 0.92; k = min(1.2, h / 320)
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), S3.throne(w * 0.2, b, k)]
    s = fit(b, h * 0.4)
    o.append(sol_fig(p, w * 0.2, b - 40 * k, s * 0.86))
    o.append(mk.person(p, round(w * 0.6), round(b), round(s * 0.92, 3), body="#3A1E14", cloth="#8A3A4A", woman=True, hair="#1A1210", sw=3, flip=True,
                       up=[(-22, -158), (-10, -128), (14, -124)], extra='<g transform="translate(10 -130)"><ellipse cx="0" cy="0" rx="20" ry="11" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></ellipse><circle cx="-14" cy="-4" r="6" fill="#D9A27A" stroke="#0D0D0F" stroke-width="1.4"></circle></g>'))
    o.append(mk.person(p, round(w * 0.8), round(b), round(s * 0.92, 3), body="#3A1E14", cloth="#4A5A3A", woman=True, hair="#1A1210", sw=3, flip=True))
    if sword:
        o.append(mk.person(p, round(w * 0.4), round(b), round(s * 0.9, 3), body=SKIN, cloth="#3A4A6A", kind="Tunic", sw=3, flip=True, up=[(22, -158), (10, -120), (-10, -110)])
                 + f'<path d="M{f(w * 0.4 + 10 * s)} {f(b - 110 * s)} L {f(w * 0.4 - 50 * s)} {f(b - 110 * s)}" stroke="#C8C2D6" stroke-width="{f(5 * s)}"></path>')
    return "".join(o)

def vine_fig(p, w, h, seed):
    """Every man under his vine and under his fig-tree: a man and his household in the shade, a vineyard on the hills."""
    r = random.Random(seed)
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#7A9A5A", amp=14), ground(w, h, h * 0.6, "#B8A86A", dy=0)]
    for i in range(16):
        x = w * (0.04 + i * 0.06); y = h * (0.56 + (i % 3) * 0.02)
        o.append(f'<path d="M{f(x)} {f(y + 14)} L {f(x)} {f(y - 4)}" stroke="#5A3A22" stroke-width="3"></path><circle cx="{f(x)}" cy="{f(y - 8)}" r="8" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    o.append(f'<path d="M{f(w * 0.5)} {f(b)} C {f(w * 0.48)} {f(h * 0.6)} {f(w * 0.52)} {f(h * 0.44)} {f(w * 0.5)} {f(h * 0.36)}" stroke="#5A3A22" stroke-width="14" fill="none"></path>')
    for i in range(10):
        o.append(f'<ellipse cx="{f(w * 0.5 + r.uniform(-w * 0.22, w * 0.22))}" cy="{f(h * r.uniform(0.18, 0.4))}" rx="{f(w * 0.08)}" ry="{f(h * 0.06)}" fill="{r.choice(["#3F8A44", "#2E6A32", "#5E8F26"])}" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    s = fit(b, h * 0.44)
    o.append(man(p, w * 0.36, b, s, "#6A5A3A") + woman(p, w * 0.64, b, s * 0.94, "#8A4A5A", flip=True))
    return "".join(o)

def stalls(p, w, h, seed):
    """Solomon's stalls of horses for his chariots, and his horsemen."""
    tall = h > w * 0.9; n = 4 if tall else 3; top = 0.3 if tall else 0.5
    o = [mk.defs(p, *ALL), sky(w, h, "#E8C8A0", "#F3D8A0"), ground(w, h, h * top, "#B89A6A", dy=0)]
    for k in range(n):
        y = h * (top + 0.12 + k * (0.5 / n if tall else 0.14)); sc = min(1.2, h / 420) * (0.36 + k * 0.14) * (0.8 if tall else 1)
        for i in range(6):
            o.append(E3.horse(w * (0.06 + i * 0.18 + (k % 2) * 0.08), y, sc, color=["#3A2214", "#6A4A2A", "#2A1A14"][i % 3]))
    o.append(E3.chariot(w * 0.7, h * 0.97, min(1.0, h / 360), color="#3A2214", driver="#1F3A7A"))
    return "".join(o)

NATURE = [("CEDAR", "tree"), ("HYSSOP", "herb"), ("BEASTS", "beast"), ("BIRDS", "bird"), ("CREEPING THINGS", "creep"), ("FISHES", "fish")]
def nature(w, h):
    """He spake of trees, from the cedar to the hyssop, of beasts, birds, creeping things and fishes: a plate of six cells."""
    o = [grid_bg(w, h, color="#3A2A5A", bg="#1A1430")]
    cw, ch = w / 3, h / 2
    for i, (nm, kind) in enumerate(NATURE):
        cx, cy = cw * (i % 3) + cw / 2, ch * (i // 3) + ch / 2 + 10; s = min(cw, ch) / 120
        g = {"tree": f'<path d="M0 40 L 0 0" stroke="#8A5A30" stroke-width="6"></path><path d="M-40 10 L 0 -40 L 40 10 Z M-30 -10 L 0 -50 L 30 -10 Z" fill="#2E6B3A" stroke="#9CCB5E" stroke-width="2"></path>',
             "herb": "".join(f'<path d="M{dx} 40 C {dx} 20 {dx + 6} 0 {dx + 2} -20" stroke="#9CCB5E" stroke-width="3" fill="none"></path><circle cx="{dx + 2}" cy="-22" r="5" fill="#E8F0B8"></circle>' for dx in (-14, 0, 14)),
             "beast": '<ellipse cx="0" cy="10" rx="36" ry="18" fill="#C8A06A" stroke="#E8C88A" stroke-width="2"></ellipse><circle cx="36" cy="-6" r="12" fill="#C8A06A" stroke="#E8C88A" stroke-width="2"></circle><path d="M-24 24 L -24 44 M-8 24 L -8 44 M14 24 L 14 44 M28 24 L 28 44" stroke="#E8C88A" stroke-width="4"></path>',
             "bird": '<path d="M-40 0 Q -20 -24 0 0 Q 20 -24 40 0" stroke="#8FD0E2" stroke-width="5" fill="none"></path><path d="M-30 30 Q -16 14 0 30 Q 16 14 30 30" stroke="#8FD0E2" stroke-width="4" fill="none"></path>',
             "creep": '<path d="M-40 10 C -20 -10 0 30 20 10 S 40 -10 44 0" stroke="#C8B070" stroke-width="7" fill="none" stroke-linecap="round"></path>',
             "fish": '<path d="M-36 0 C -16 -22 16 -22 30 0 C 16 22 -16 22 -36 0 Z M30 0 L 44 -14 L 44 14 Z" fill="#2C9DB8" stroke="#8FD0E2" stroke-width="2"></path>'}[kind]
        o.append(f'<g transform="translate({f(cx)} {f(cy)}) scale({f(s)})">{g}</g>' + label(cx, cy + 66 * s, nm, "#FFD23F", 9))
        o.append(f'<rect x="{f(cw * (i % 3) + 6)}" y="{f(ch * (i // 3) + 6)}" width="{f(cw - 12)}" height="{f(ch - 12)}" fill="none" stroke="#5A4A8A" stroke-width="1.4"></rect>')
    return "".join(o)

# ---- 1 Kings 5–6 --------------------------------------------------------------------------------------------------------
from exo.art8 import bp, dim, box, tag, title_bar, CY, GOLD, INK
CEDAR_C = "#B5793A"

def lebanon(p, w, h, seed, rafts=False):
    """Cedar-trees on the mountains of Lebanon, the hewers at work; rafts=True: the timber floated down by sea in rafts."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#E8F6FA")]
    if rafts:
        o += [hills(w, h, h * 0.3, seed, color="#4A6A4A", amp=24), f'<rect x="-10" y="{f(h * 0.4)}" width="{f(w + 20)}" height="{f(h * 0.7)}" fill="#1F6F9A"></rect>']
        for i in range(3):
            x = w * (0.16 + i * 0.3); y = h * (0.56 + i * 0.12)
            o.append("".join(f'<rect x="{f(x)}" y="{f(y + k * 9)}" width="{f(w * 0.2)}" height="8" rx="4" fill="{CEDAR_C}" stroke="#0D0D0F" stroke-width="1.6"></rect>' for k in range(4)))
            o.append(f'<path d="M{f(x - 10)} {f(y + 40)} C {f(x + w * 0.1)} {f(y + 34)} {f(x + w * 0.2)} {f(y + 46)} {f(x + w * 0.26)} {f(y + 40)}" stroke="#E8F6FA" stroke-width="2" fill="none"></path>')
        return "".join(o)
    o += [f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.3)} {f(h * 0.14)} L {f(w * 0.56)} {f(h * 0.44)} L {f(w * 0.78)} {f(h * 0.08)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A6A5A" stroke="#0D0D0F" stroke-width="2.4"></path>',
          f'<path d="M{f(w * 0.22)} {f(h * 0.26)} L {f(w * 0.3)} {f(h * 0.14)} L {f(w * 0.38)} {f(h * 0.26)} Z M{f(w * 0.7)} {f(h * 0.2)} L {f(w * 0.78)} {f(h * 0.08)} L {f(w * 0.86)} {f(h * 0.2)} Z" fill="#F3EFE6"></path>']
    for i in range(9):
        x = w * (0.06 + i * 0.11); y = h * (0.62 + (i % 3) * 0.1); s = min(1.0, h / 400) * (0.7 + 0.1 * (i % 3))
        o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M0 0 L 0 -90" stroke="#5A3A22" stroke-width="8"></path>'
                 + "".join(f'<path d="M{-60 + k * 8} {-30 - k * 22} L {60 - k * 8} {-30 - k * 22} L 0 {-50 - k * 22} Z" fill="#1F4A34" stroke="#0D0D0F" stroke-width="1.6"></path>' for k in range(4)) + '</g>')
    s = fit(h * 0.96, h * 0.6)
    for i in range(3):
        o.append(mk.person(p, round(w * (0.3 + i * 0.22)), round(h * 0.96), round(s, 3), body="#3A1E14", cloth=["#6A1A5A", "#5A5A3A", "#3A4A6A"][i], kind="Tunic", sw=3,
                           up=[(-22, -158), (-30, -200), (-10, -226)]))
    return "".join(o)

def hewers(p, w, h, seed):
    """Burden-bearers and hewers in the mountains: great stones, costly stones, hewn for the foundation."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#E8C8A0", "#F3D8A0"), f'<path d="M-10 {f(h * 0.5)} L {f(w * 0.4)} {f(h * 0.3)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B8A890" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i in range(5):
        x = w * (0.1 + i * 0.18); y = h * (0.66 + (i % 2) * 0.1)
        o.append(box(x, y, w * 0.1, w * 0.06, h * 0.1, fill="#D8CCB0", top="#E8DCC0", side="#B8AC90"))
    s = fit(b, h * 0.4)
    for i in range(4):
        o.append(mk.person(p, round(w * (0.16 + i * 0.22)), round(b), round(s, 3), body="#3A1E14", cloth=WAR[i % 4], kind="Tunic", sw=3, flip=i % 2 == 1))
    return "".join(o)

def temple_elev(w, h):
    """The house of Jehovah, front elevation: threescore cubits long, twenty broad, thirty high; the porch before it; the
    side-chambers in three stories; windows of fixed lattice-work."""
    o = [bp(w, h), title_bar(w, "THE HOUSE OF JEHOVAH · ELEVATION")]
    u = min(w * 0.8 / 60, h * 0.7 / 30); x0 = w * 0.5 - 30 * u; base = h * 0.9
    o.append(box(x0 + 10 * u, base, 40 * u, 0, 30 * u, fill="#D8CCB0"))
    for k in range(3):
        o.append(f'<rect x="{f(x0)}" y="{f(base - (k + 1) * 5 * u)}" width="{f(10 * u)}" height="{f(5 * u)}" fill="#C8BC9C" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<rect x="{f(x0 + 50 * u)}" y="{f(base - (k + 1) * 5 * u)}" width="{f(10 * u)}" height="{f(5 * u)}" fill="#C8BC9C" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    for i in range(5):
        wx = x0 + (14 + i * 7.5) * u; wy = base - 26 * u
        o.append(f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(3 * u)}" height="{f(3 * u)}" fill="{INK}" stroke="{CY}" stroke-width="1.2"></rect>'
                 f'<path d="M{f(wx)} {f(wy)} L {f(wx + 3 * u)} {f(wy + 3 * u)} M{f(wx + 3 * u)} {f(wy)} L {f(wx)} {f(wy + 3 * u)}" stroke="{CY}" stroke-width="1"></path>')
    o.append(f'<path d="M{f(x0 + 26 * u)} {f(base)} L {f(x0 + 26 * u)} {f(base - 12 * u)} L {f(x0 + 34 * u)} {f(base - 12 * u)} L {f(x0 + 34 * u)} {f(base)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(dim(x0 + 10 * u, base - 30 * u - 12, x0 + 50 * u, base - 30 * u - 12, "20 CUBITS"))
    o.append(dim(x0 + 50 * u + 4, base, x0 + 50 * u + 4, base - 30 * u, "30 CUBITS", off=-14))
    o.append(tag(x0 + 55 * u, base - 12 * u, "SIDE-CHAMBERS · THREE STORIES", x0 + 44 * u, base - 36 * u))
    o.append(tag(x0 + 20 * u, base - 24 * u, "WINDOWS OF FIXED LATTICE-WORK", x0 + 34 * u, base - 36 * u))
    return "".join(o)

def temple_plan(w, h, oracle=False):
    """The house in plan: the porch (20 × 10), the temple (40 × 20), the oracle (20 × 20), side-chambers round about."""
    o = [bp(w, h), title_bar(w, "THE HOUSE OF JEHOVAH · PLAN")]
    u = min(w * 0.86 / 74, h * 0.7 / 32); x0 = w * 0.5 - 37 * u; y0 = h * 0.56 - 16 * u
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(74 * u)}" height="{f(32 * u)}" fill="none" stroke="{CY}" stroke-width="1.4" stroke-dasharray="4 3"></rect>')
    o.append(f'<rect x="{f(x0 + 4 * u)}" y="{f(y0 + 6 * u)}" width="{f(10 * u)}" height="{f(20 * u)}" fill="#3A4A5A" stroke="{CY}" stroke-width="2"></rect>' + label(x0 + 9 * u, y0 + 16 * u, "PORCH", CY, 8))
    o.append(f'<rect x="{f(x0 + 14 * u)}" y="{f(y0 + 6 * u)}" width="{f(40 * u)}" height="{f(20 * u)}" fill="{"#5A4A1A" if oracle else "#2A3A4A"}" stroke="{CY}" stroke-width="2"></rect>'
             + label(x0 + 34 * u, y0 + 16 * u, "THE TEMPLE · 40 CUBITS", CY, 9))
    o.append(f'<rect x="{f(x0 + 54 * u)}" y="{f(y0 + 6 * u)}" width="{f(20 * u)}" height="{f(20 * u)}" fill="{GOLD if oracle else "#3A3A2A"}" stroke="{CY}" stroke-width="2.4"></rect>'
             + label(x0 + 64 * u, y0 + 13 * u, "THE ORACLE", INK if oracle else CY, 9) + label(x0 + 64 * u, y0 + 25 * u, "20 × 20 × 20", INK if oracle else CY, 8))
    o.append(f'<rect x="{f(x0 + 60 * u)}" y="{f(y0 + 14 * u)}" width="{f(8 * u)}" height="{f(4 * u)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(dim(x0 + 14 * u, y0 + 30 * u, x0 + 74 * u, y0 + 30 * u, "THREESCORE CUBITS"))
    o.append(dim(x0 - 6, y0 + 6 * u, x0 - 6, y0 + 26 * u, "20", off=0))
    o.append(tag(x0 + 40 * u, y0 + 3 * u, "SIDE-CHAMBERS ROUND ABOUT", x0 + 40 * u, y0 - 4 * u))
    return "".join(o)

def stories(w, h):
    """The stories against the wall in section: five, six and seven cubits broad, offsets in the wall so the beams rest
    without hold; the winding stairs; each story five cubits high."""
    o = [bp(w, h), title_bar(w, "THE SIDE-CHAMBERS · SECTION")]
    u = min(w * 0.6 / 14, h * 0.7 / 18); x0 = w * 0.3; base = h * 0.9
    o.append(f'<path d="M{f(x0 + 8 * u)} {f(base)} L {f(x0 + 8 * u)} {f(base - 18 * u)} L {f(x0 + 10 * u)} {f(base - 18 * u)} L {f(x0 + 10 * u)} {f(base)} Z" fill="#D8CCB0" stroke="#0D0D0F" stroke-width="2"></path>')
    for k, wd in enumerate((5, 6, 7)):
        y = base - k * 5 * u
        o.append(f'<rect x="{f(x0 + (8 - wd) * u)}" y="{f(y - 5 * u)}" width="{f(wd * u)}" height="{f(5 * u)}" fill="#2A3A4A" stroke="{CY}" stroke-width="1.6"></rect>'
                 f'<rect x="{f(x0 + (8 - wd) * u)}" y="{f(y - 5 * u)}" width="{f(wd * u)}" height="{f(0.5 * u)}" fill="{CEDAR_C}" stroke="#0D0D0F" stroke-width="1"></rect>'
                 + dim(x0 + (8 - wd) * u, y - 2.5 * u, x0 + 8 * u, y - 2.5 * u, f"{wd} CUBITS"))
    o.append(dim(x0 - 0.6 * u - 14, base, x0 - 0.6 * u - 14, base - 5 * u, "5", off=0))
    o.append("".join(f'<path d="M{f(x0 + 6.5 * u + math.sin(t) * u)} {f(base - t * 2.2 * u)} L {f(x0 + 6.5 * u + math.sin(t + 0.4) * u)} {f(base - (t + 0.4) * 2.2 * u)}" stroke="{GOLD}" stroke-width="2"></path>' for t in [i * 0.4 for i in range(16)]))
    o.append(tag(x0 + 6.5 * u, base - 7 * u, "WINDING STAIRS", x0 + 12 * u, base - 12 * u))
    return "".join(o)

def no_tool(w, h):
    """Stone made ready at the quarry: a dressed block, and the hammer, axe and iron tool crossed out — none heard in the house."""
    o = [bp(w, h), title_bar(w, "STONE MADE READY AT THE QUARRY")]
    o.append(box(w * 0.12, h * 0.82, w * 0.3, w * 0.14, h * 0.32, fill="#D8CCB0", top="#E8DCC0", side="#B8AC90"))
    for i, nm in enumerate(("HAMMER", "AXE", "TOOL OF IRON")):
        x = w * (0.6 + i * 0.13); y = h * 0.6
        o.append(f'<rect x="{f(x - 6)}" y="{f(y - 30)}" width="12" height="60" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.6"></rect><rect x="{f(x - 20)}" y="{f(y - 40)}" width="40" height="14" fill="#9AA0A8" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<circle cx="{f(x)}" cy="{f(y - 10)}" r="40" fill="none" stroke="#D7261E" stroke-width="4"></circle><path d="M{f(x - 28)} {f(y - 38)} L {f(x + 28)} {f(y + 18)}" stroke="#D7261E" stroke-width="4"></path>'
                 + label(x, y + 50, nm, CY, 8))
    return "".join(o)

def cedar_within(w, h, gold=False):
    """The walls within of cedar carved with knops and open flowers, the floor of fir; gold=True: all overlaid with gold, the
    chains of gold across before the oracle."""
    o = [bp(w, h), title_bar(w, "WITHIN THE HOUSE" + (" · OVERLAID WITH GOLD" if gold else " · CEDAR"))]
    c = GOLD if gold else CEDAR_C; x0, x1, y0, y1 = w * 0.08, w * 0.92, h * 0.16, h * 0.84
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(x1 - x0)}" height="{f(y1 - y0)}" fill="{c}" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    for i in range(8):
        for k in range(3):
            cx = x0 + (i + 0.5) * (x1 - x0) / 8; cy = y0 + (k + 0.5) * (y1 - y0) / 3
            o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(min(w, h) * 0.03)}" fill="none" stroke="#5A3A1A" stroke-width="2"></circle>'
                     + "".join(f'<ellipse cx="{f(cx + math.cos(a) * min(w, h) * 0.045)}" cy="{f(cy + math.sin(a) * min(w, h) * 0.045)}" rx="5" ry="3" fill="#5A3A1A" transform="rotate({f(math.degrees(a))} {f(cx + math.cos(a) * min(w, h) * 0.045)} {f(cy + math.sin(a) * min(w, h) * 0.045)})"></ellipse>' for a in [j * 1.047 for j in range(6)]))
    if gold:
        o.append("".join(f'<path d="M{f(x0)} {f(y0 + 20 + k * 14)} Q {f((x0 + x1) / 2)} {f(y0 + 60 + k * 14)} {f(x1)} {f(y0 + 20 + k * 14)}" stroke="#FFF4C2" stroke-width="3" stroke-dasharray="6 3" fill="none"></path>' for k in range(2)))
    o.append(tag(x0 + 30, y0 + 30, "KNOPS AND OPEN FLOWERS", x0 + 60, y0 - 4))
    return "".join(o)

def cherubim(w, h):
    """The two cherubim of olive-wood in the oracle, each ten cubits high, wings five cubits each, touching the walls and one
    another in the midst; overlaid with gold."""
    o = [bp(w, h), title_bar(w, "THE ORACLE · THE CHERUBIM")]
    u = min(w * 0.8 / 20, h * 0.74 / 12); x0 = w * 0.5 - 10 * u; base = h * 0.9
    o.append(f'<rect x="{f(x0)}" y="{f(base - 11 * u)}" width="{f(20 * u)}" height="{f(11 * u)}" fill="none" stroke="{CY}" stroke-width="2"></rect>')
    for i in range(2):
        cx = x0 + (5 + i * 10) * u
        o.append(f'<path d="M{f(cx - 1.2 * u)} {f(base)} L {f(cx - 0.8 * u)} {f(base - 6 * u)} L {f(cx + 0.8 * u)} {f(base - 6 * u)} L {f(cx + 1.2 * u)} {f(base)} Z" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<circle cx="{f(cx)}" cy="{f(base - 6.8 * u)}" r="{f(0.8 * u)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2"></circle>'
                 + "".join(f'<path d="M{f(cx)} {f(base - 6.6 * u)} L {f(cx + d * 5 * u)} {f(base - 8.6 * u)} L {f(cx + d * 5 * u)} {f(base - 7.6 * u)} L {f(cx)} {f(base - 5.6 * u)} Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.6"></path>' for d in (-1, 1)))
    o.append(dim(x0, base - 11 * u - 14, x0 + 10 * u, base - 11 * u - 14, "10 CUBITS") + dim(x0 + 10 * u, base - 11 * u - 14, x0 + 20 * u, base - 11 * u - 14, "10 CUBITS"))
    o.append(dim(x0 + 20 * u + 10, base, x0 + 20 * u + 10, base - 10 * u, "10 CUBITS HIGH", off=-12))
    o.append(f'<rect x="{f(w * 0.5 - 2 * u)}" y="{f(base - 1.4 * u)}" width="{f(4 * u)}" height="{f(1.4 * u)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)

def doors(w, h, folding=False):
    """The doors of olive-wood carved with cherubim, palm-trees and open flowers, overlaid with gold; folding=True: the two
    doors of fir-wood, each of two folding leaves."""
    o = [bp(w, h), title_bar(w, "THE DOORS OF THE TEMPLE · FIR-WOOD, FOLDING" if folding else "THE DOORS OF THE ORACLE · OLIVE-WOOD")]
    n = 4 if folding else 2; x0, x1, y0, y1 = w * 0.22, w * 0.78, h * 0.14, h * 0.9
    lw = (x1 - x0) / n
    for i in range(n):
        x = x0 + i * lw
        o.append(f'<rect x="{f(x)}" y="{f(y0)}" width="{f(lw)}" height="{f(y1 - y0)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2.4"></rect>')
        cx = x + lw / 2
        o.append(f'<path d="M{f(cx)} {f(y1 - 20)} L {f(cx)} {f(y0 + (y1 - y0) * 0.4)}" stroke="#8A5A1A" stroke-width="4"></path>'
                 + "".join(f'<path d="M{f(cx)} {f(y0 + (y1 - y0) * 0.4)} Q {f(cx + d * lw * 0.3)} {f(y0 + (y1 - y0) * 0.3)} {f(cx + d * lw * 0.4)} {f(y0 + (y1 - y0) * 0.42)}" stroke="#8A5A1A" stroke-width="3" fill="none"></path>' for d in (-1, 1))
                 + f'<path d="M{f(cx - lw * 0.3)} {f(y0 + 50)} C {f(cx - lw * 0.2)} {f(y0 + 20)} {f(cx)} {f(y0 + 30)} {f(cx + lw * 0.3)} {f(y0 + 40)}" stroke="#8A5A1A" stroke-width="3" fill="none"></path>'
                 + f'<circle cx="{f(cx)}" cy="{f(y1 - (y1 - y0) * 0.22)}" r="{f(lw * 0.12)}" fill="none" stroke="#8A5A1A" stroke-width="2.4"></circle>')
        if folding and i % 2 == 0: o.append(f'<path d="M{f(x + lw)} {f(y0)} L {f(x + lw)} {f(y1)}" stroke="{CY}" stroke-width="2" stroke-dasharray="6 3"></path>')
    o.append(tag(x0 + lw * 0.5, y0 + 40, "CHERUBIM", x0 - 20, y0 + 20) + tag(x0 + lw * 0.5, y0 + (y1 - y0) * 0.5, "PALM-TREES", x0 - 20, y0 + (y1 - y0) * 0.5)
             + tag(x0 + lw * 0.5, y1 - (y1 - y0) * 0.22, "OPEN FLOWERS", x0 - 20, y1 - (y1 - y0) * 0.2))
    return "".join(o)

def inner_court(w, h):
    """The inner court wall: three courses of hewn stone and a course of cedar beams."""
    o = [bp(w, h), title_bar(w, "THE INNER COURT · THE WALL")]
    x0, x1, base = w * 0.1, w * 0.9, h * 0.84; ch = h * 0.12
    for k in range(3):
        for i in range(8):
            off = (k % 2) * (x1 - x0) / 16
            bx = x0 + off + i * (x1 - x0) / 8
            if bx + (x1 - x0) / 8 > x1 + 1: continue
            o.append(f'<rect x="{f(bx)}" y="{f(base - (k + 1) * ch)}" width="{f((x1 - x0) / 8)}" height="{f(ch)}" fill="#D8CCB0" stroke="#0D0D0F" stroke-width="1.8"></rect>')
    o.append(f'<rect x="{f(x0)}" y="{f(base - 3 * ch - ch * 0.5)}" width="{f(x1 - x0)}" height="{f(ch * 0.5)}" fill="{CEDAR_C}" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(label(x0, base + 16, "THREE COURSES OF HEWN STONE · A COURSE OF CEDAR BEAMS", CY, 9, "start"))
    return "".join(o)

def years(w, h):
    """In the fourth year, in the month Ziv, the foundation laid; in the eleventh year, in the month Bul, finished: seven years."""
    o = [bp(w, h), title_bar(w, "SEVEN YEARS IN BUILDING")]
    x0, x1, y = w * 0.1, w * 0.9, h * 0.36
    o.append(f'<path d="M{f(x0)} {f(y)} L {f(x1)} {f(y)}" stroke="{CY}" stroke-width="2"></path>')
    for i in range(8):
        x = x0 + i * (x1 - x0) / 7; yr = 4 + i
        o.append(node(x, y, f"YEAR {yr}", "#FFD23F" if i in (0, 7) else CY, r=6 if i in (0, 7) else 4, dy=-14, size=9))
    o.append(label(x0, y + 34, "FOUNDATION · ZIV", "#FFD23F", 9, "start") + label(x1, y + 34, "FINISHED · BUL", "#FFD23F", 9, "end"))
    return "".join(o)

# ---- 1 Kings 7 ----------------------------------------------------------------------------------------------------------
BRASS = "#B87333"

def forest_house(w, h):
    """The house of the forest of Lebanon: a hundred cubits long, fifty broad, thirty high, upon four rows of cedar pillars with
    cedar beams; windows over against window in three ranks."""
    o = [bp(w, h), title_bar(w, "THE HOUSE OF THE FOREST OF LEBANON")]
    u = min(w * 0.84 / 100, h * 0.66 / 30); x0 = w * 0.5 - 50 * u; base = h * 0.9
    o.append(f'<rect x="{f(x0)}" y="{f(base - 30 * u)}" width="{f(100 * u)}" height="{f(30 * u)}" fill="#D8CCB0" stroke="#0D0D0F" stroke-width="2"></rect>')
    for i in range(15):
        x = x0 + (3 + i * 6.7) * u
        o.append(f'<rect x="{f(x - 0.8 * u)}" y="{f(base - 14 * u)}" width="{f(1.6 * u)}" height="{f(14 * u)}" fill="{CEDAR_C}" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    o.append(f'<rect x="{f(x0)}" y="{f(base - 15.6 * u)}" width="{f(100 * u)}" height="{f(1.6 * u)}" fill="{CEDAR_C}" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    for k in range(3):
        for i in range(10):
            x = x0 + (5 + i * 10) * u; y = base - (19 + k * 4) * u
            o.append(f'<rect x="{f(x - 1.2 * u)}" y="{f(y - 1.4 * u)}" width="{f(2.4 * u)}" height="{f(2.4 * u)}" fill="{INK}" stroke="{CY}" stroke-width="1"></rect>')
    o.append(dim(x0, base - 30 * u - 12, x0 + 100 * u, base - 30 * u - 12, "100 CUBITS") + dim(x0 + 100 * u + 8, base, x0 + 100 * u + 8, base - 30 * u, "30", off=-10))
    o.append(tag(x0 + 3 * u, base - 8 * u, "CEDAR PILLARS · FOUR ROWS", x0 + 10 * u, base + 8))
    return "".join(o)

def judgment_porch(p, w, h, seed):
    """The porch of the throne where he was to judge, covered with cedar from floor to floor."""
    b = h * 0.92; k = min(1.3, h / 280)
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84)]
    for x in (0.12, 0.88):
        o.append(f'<rect x="{f(w * x - 14)}" y="0" width="28" height="{f(b)}" fill="#9A5A30" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(S3.throne(w * 0.5, b, k) + sol_fig(p, w * 0.5, b - 40 * k, fit(b, h * 0.4) * 0.86))
    return "".join(o)

def great_stones(w, h):
    """Costly stones, great stones, stones of ten cubits and of eight cubits, sawed with saws, for the foundation."""
    o = [bp(w, h), title_bar(w, "THE FOUNDATION · COSTLY STONES")]
    u = min(w * 0.8 / 22, h * 0.5 / 6); x0 = w * 0.1; base = h * 0.84
    o.append(box(x0, base, 10 * u, 3 * u, 3 * u, fill="#D8CCB0", top="#E8DCC0", side="#B8AC90") + dim(x0, base + 10, x0 + 10 * u, base + 10, "10 CUBITS"))
    o.append(box(x0 + 12 * u, base, 8 * u, 3 * u, 3 * u, fill="#D8CCB0", top="#E8DCC0", side="#B8AC90") + dim(x0 + 12 * u, base + 10, x0 + 20 * u, base + 10, "8 CUBITS"))
    return "".join(o)

def casting(p, w, h, seed):
    """Hiram casting the brass in the clay ground of the plain of the Jordan: furnace, crucible and moulds."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#5A2A1E", "#C8603A"), ground(w, h, h * 0.6, "#6A4A2A", dy=0),
         f'<path d="M{f(w * 0.2)} {f(b)} L {f(w * 0.24)} {f(h * 0.5)} L {f(w * 0.36)} {f(h * 0.5)} L {f(w * 0.4)} {f(b)} Z" fill="#7A5A3A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         E.blaze(w * 0.3, h * 0.52, w * 0.08, h * 0.2, seed, n=6),
         f'<path d="M{f(w * 0.42)} {f(h * 0.7)} C {f(w * 0.5)} {f(h * 0.74)} {f(w * 0.56)} {f(h * 0.8)} {f(w * 0.62)} {f(h * 0.82)}" stroke="#FFB04A" stroke-width="8" fill="none"></path>']
    for i in range(3):
        x = w * (0.64 + i * 0.1)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(h * 0.86)}" rx="{f(w * 0.04)}" ry="{f(h * 0.03)}" fill="#3A2A1A" stroke="#0D0D0F" stroke-width="2"></ellipse><ellipse cx="{f(x)}" cy="{f(h * 0.855)}" rx="{f(w * 0.03)}" ry="{f(h * 0.018)}" fill="#FF8A3D"></ellipse>')
    o.append(mk.person(p, round(w * 0.5), round(b), round(fit(b, h * 0.4), 3), body="#3A1E14", cloth="#6A3A2A", kind="Tunic", sw=3, extra=A.headcloth("#6A1A5A") + A.BLACK_BEARD))
    return "".join(o)

def pillar_elev(w, h, names=False):
    """A pillar of brass, eighteen cubits high, twelve round; the capital five cubits, nets of checker-work, wreaths of chain-work,
    two rows of pomegranates, lily-work at the top; names=True: the two pillars at the porch, Jachin and Boaz."""
    o = [bp(w, h), title_bar(w, "JACHIN AND BOAZ" if names else "THE PILLARS OF BRASS · ELEVATION")]
    u = h * 0.74 / 23; base = h * 0.92
    xs = (w * 0.32, w * 0.68) if names else (w * 0.4,)
    for x in xs:
        o.append(f'<rect x="{f(x - 1.9 * u)}" y="{f(base - 18 * u)}" width="{f(3.8 * u)}" height="{f(18 * u)}" fill="{BRASS}" stroke="#0D0D0F" stroke-width="2"></rect>')
        cy = base - 18 * u
        o.append(f'<path d="M{f(x - 1.9 * u)} {f(cy)} C {f(x - 3.4 * u)} {f(cy - 1.5 * u)} {f(x - 3.4 * u)} {f(cy - 3.5 * u)} {f(x - 2.4 * u)} {f(cy - 5 * u)} L {f(x + 2.4 * u)} {f(cy - 5 * u)} C {f(x + 3.4 * u)} {f(cy - 3.5 * u)} {f(x + 3.4 * u)} {f(cy - 1.5 * u)} {f(x + 1.9 * u)} {f(cy)} Z" fill="#C8863E" stroke="#0D0D0F" stroke-width="2"></path>')
        for i in range(7):
            o.append(f'<path d="M{f(x - 3 * u)} {f(cy - (0.6 + i * 0.5) * u)} L {f(x + 3 * u)} {f(cy - (0.6 + i * 0.5) * u)}" stroke="#7A4A1A" stroke-width="1" opacity="0.7"></path>')
        for row in range(2):
            for i in range(6):
                o.append(f'<circle cx="{f(x - 2.5 * u + i * u)}" cy="{f(cy - (1 + row * 2.2) * u)}" r="{f(0.32 * u)}" fill="#B5121B" stroke="#0D0D0F" stroke-width="1"></circle>')
        for i in range(5):
            o.append(f'<path d="M{f(x - 2.4 * u + i * 1.2 * u)} {f(cy - 5 * u)} C {f(x - 2.8 * u + i * 1.2 * u)} {f(cy - 6.4 * u)} {f(x - 1.6 * u + i * 1.2 * u)} {f(cy - 6.4 * u)} {f(x - 2 * u + i * 1.2 * u)} {f(cy - 5 * u)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></path>')
        if names:
            o.append(label(x, base + 2 - 9 * u, "JACHIN" if x < w * 0.5 else "BOAZ", "#FFD23F", 13))
    x = xs[-1]
    if not names:
        o.append(dim(x + 4 * u, base, x + 4 * u, base - 18 * u, "18 CUBITS", off=-14) + dim(x + 4 * u, base - 18 * u, x + 4 * u, base - 23 * u, "5", off=-14))
        o.append(tag(x + 3 * u, base - 21 * u, "NETS OF CHECKER-WORK", x + 8 * u, base - 21 * u) + tag(x - 2.5 * u, base - 19 * u, "POMEGRANATES", x - 7 * u, base - 15 * u)
                 + tag(x, base - 23.4 * u, "LILY-WORK", x - 7 * u, base - 23 * u))
    return "".join(o)

def molten_sea(w, h):
    """The molten sea: ten cubits brim to brim, five high, a line of thirty compassing it; knops under the brim in two rows; set
    upon twelve oxen, three toward each quarter."""
    o = [bp(w, h), title_bar(w, "THE MOLTEN SEA")]
    u = min(w * 0.7 / 12, h * 0.66 / 7); cx = w * 0.5; base = h * 0.9; top = base - 6.6 * u
    for i in range(6):
        x = cx - 5 * u + i * 2 * u
        o.append(S1.cow(x + (u if i >= 3 else 0), base, u / 80, color=BRASS, patch="#C8863E", flip=i >= 3))
    o.append(f'<path d="M{f(cx - 5 * u)} {f(top)} C {f(cx - 5 * u)} {f(top + 4 * u)} {f(cx - 3 * u)} {f(top + 5 * u)} {f(cx)} {f(top + 5 * u)} C {f(cx + 3 * u)} {f(top + 5 * u)} {f(cx + 5 * u)} {f(top + 4 * u)} {f(cx + 5 * u)} {f(top)} Z" fill="{BRASS}" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(top)}" rx="{f(5.3 * u)}" ry="{f(0.9 * u)}" fill="#C8863E" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(top + 0.1 * u)}" rx="{f(4.6 * u)}" ry="{f(0.6 * u)}" fill="#1F6F9A"></ellipse>')
    for row in range(2):
        for i in range(11):
            o.append(f'<circle cx="{f(cx - 4.5 * u + i * 0.9 * u)}" cy="{f(top + (0.9 + row * 0.6) * u)}" r="{f(0.2 * u)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="0.8"></circle>')
    o.append(dim(cx - 5.3 * u, top - 1.6 * u, cx + 5.3 * u, top - 1.6 * u, "10 CUBITS · BRIM TO BRIM") + dim(cx + 6 * u, top, cx + 6 * u, top + 5 * u, "5", off=-10))
    o.append(tag(cx - 4 * u, base - 0.6 * u, "TWELVE OXEN", cx - 7 * u, base - 4 * u))
    return "".join(o)

def base_laver(w, h, laver=True):
    """A base of brass: four cubits by four, three high; panels between the ledges with lions, oxen and cherubim; four
    wheels like chariot wheels; laver=True: a laver of forty baths upon it."""
    o = [bp(w, h), title_bar(w, "A BASE OF BRASS" + (" · AND ITS LAVER" if laver else ""))]
    u = min(w * 0.5 / 5, h * 0.66 / (7 if laver else 4.5)); cx = w * 0.46; base = h * 0.9
    o.append(box(cx - 2 * u, base - 0.8 * u, 4 * u, 2 * u, 2.4 * u, fill=BRASS, top="#C8863E", side="#8A5A2A"))
    for i, nm in enumerate(("LION", "OX", "CHERUB")):
        x = cx - 1.4 * u + i * 1.4 * u; y = base - 2 * u
        o.append(f'<rect x="{f(x - 0.55 * u)}" y="{f(y - 0.9 * u)}" width="{f(1.1 * u)}" height="{f(1.8 * u)}" fill="none" stroke="#5A3A1A" stroke-width="1.6"></rect>' + label(x, y + 4, nm, "#3A2210", 7))
    for dx in (-1.6, 1.6):
        o.append(f'<circle cx="{f(cx + dx * u)}" cy="{f(base - 0.75 * u)}" r="{f(0.75 * u)}" fill="none" stroke="#0D0D0F" stroke-width="{f(0.18 * u)}"></circle>'
                 f'<circle cx="{f(cx + dx * u)}" cy="{f(base - 0.75 * u)}" r="{f(0.75 * u)}" fill="none" stroke="{BRASS}" stroke-width="{f(0.12 * u)}"></circle>'
                 + "".join(f'<path d="M{f(cx + dx * u)} {f(base - 0.75 * u)} l {f(0.7 * u * math.cos(a))} {f(0.7 * u * math.sin(a))}" stroke="{BRASS}" stroke-width="2"></path>' for a in [j * 0.785 for j in range(8)]))
    if laver:
        ly = base - 3.2 * u
        o.append(f'<path d="M{f(cx - 2 * u)} {f(ly - 2.4 * u)} C {f(cx - 2 * u)} {f(ly - 0.4 * u)} {f(cx - 1 * u)} {f(ly)} {f(cx + 0.2 * u)} {f(ly)} C {f(cx + 1.4 * u)} {f(ly)} {f(cx + 2.4 * u)} {f(ly - 0.4 * u)} {f(cx + 2.4 * u)} {f(ly - 2.4 * u)} Z" fill="{BRASS}" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<ellipse cx="{f(cx + 0.2 * u)}" cy="{f(ly - 2.4 * u)}" rx="{f(2.2 * u)}" ry="{f(0.4 * u)}" fill="#1F6F9A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
        o.append(tag(cx + 2.2 * u, ly - 1.4 * u, "A LAVER · FORTY BATHS", cx + 3.4 * u, ly - 3 * u))
    o.append(dim(cx - 2 * u, base + 8, cx + 2 * u, base + 8, "4 CUBITS") + tag(cx + 1.6 * u, base - 0.75 * u, "WHEELS · 1½ CUBITS", cx + 3.4 * u, base - 0.4 * u))
    return "".join(o)

def court_plan(w, h):
    """The bases set five on the right side of the house and five on the left; the sea on the right side eastward."""
    o = [bp(w, h), title_bar(w, "THE COURT · THE BASES AND THE SEA")]
    u = min(w * 0.8 / 60, h * 0.7 / 40); x0 = w * 0.5 - 30 * u; y0 = h * 0.54 - 10 * u
    o.append(f'<rect x="{f(x0 + 14 * u)}" y="{f(y0)}" width="{f(46 * u)}" height="{f(20 * u)}" fill="#2A3A4A" stroke="{CY}" stroke-width="2"></rect>' + label(x0 + 37 * u, y0 + 10 * u, "THE HOUSE", CY, 9))
    for i in range(5):
        o.append(f'<rect x="{f(x0 + (18 + i * 8) * u)}" y="{f(y0 - 6 * u)}" width="{f(3 * u)}" height="{f(3 * u)}" fill="{BRASS}" stroke="#0D0D0F" stroke-width="1.4"></rect>'
                 f'<rect x="{f(x0 + (18 + i * 8) * u)}" y="{f(y0 + 23 * u)}" width="{f(3 * u)}" height="{f(3 * u)}" fill="{BRASS}" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    o.append(f'<circle cx="{f(x0 + 6 * u)}" cy="{f(y0 + 25 * u)}" r="{f(5 * u)}" fill="{BRASS}" stroke="#0D0D0F" stroke-width="2"></circle>' + label(x0 + 6 * u, y0 + 25.5 * u, "SEA", INK, 8))
    o.append(label(x0 + 2 * u, y0 + 10 * u, "EAST", "#FFD23F", 9) + label(x0 + 37 * u, y0 + 31 * u, "SOUTH · THE RIGHT SIDE", "#FFD23F", 9))
    return "".join(o)

def gold_vessels(w, h):
    """The candlesticks of pure gold, five on the right side and five on the left, before the oracle."""
    o = [bp(w, h), title_bar(w, "THE VESSELS OF GOLD · TEN CANDLESTICKS")]
    s = min(w / 1900, h / 260)
    for i in range(10):
        x = w * (0.06 + i * 0.08) + (w * 0.12 if i >= 5 else 0)
        o.append(re.sub(r'<path d="M[^"]*" fill="none" stroke="#8A8478"[^>]*></path>', "", S1.lamp(x, h * 0.9, s, lit=True)))
    o.append(f'<rect x="{f(w * 0.47)}" y="{f(h * 0.3)}" width="{f(w * 0.06)}" height="{f(h * 0.6)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2"></rect>' + label(w * 0.5, h * 0.26, "ORACLE", CY, 8))
    return "".join(o)

# ---- 1 Kings 8 ----------------------------------------------------------------------------------------------------------
def temple_front(x, base, wd, seed=1):
    """The house of Jehovah seen from the court: the stone house, the porch, Jachin and Boaz, the side-chambers. wd = width."""
    u = wd / 60
    o = [f'<rect x="{f(x - 30 * u)}" y="{f(base - 18 * u)}" width="{f(60 * u)}" height="{f(18 * u)}" fill="#C8BC9C" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<rect x="{f(x - 20 * u)}" y="{f(base - 34 * u)}" width="{f(40 * u)}" height="{f(34 * u)}" fill="#E8DCC0" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(x - 22 * u)}" y="{f(base - 36 * u)}" width="{f(44 * u)}" height="{f(3 * u)}" fill="#B8AC90" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<path d="M{f(x - 6 * u)} {f(base)} L {f(x - 6 * u)} {f(base - 16 * u)} L {f(x + 6 * u)} {f(base - 16 * u)} L {f(x + 6 * u)} {f(base)} Z" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2"></path>']
    for dx in (-12, 12):
        px = x + dx * u
        o.append(f'<rect x="{f(px - 1.4 * u)}" y="{f(base - 20 * u)}" width="{f(2.8 * u)}" height="{f(20 * u)}" fill="{BRASS}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<ellipse cx="{f(px)}" cy="{f(base - 21.5 * u)}" rx="{f(2.4 * u)}" ry="{f(2 * u)}" fill="#C8863E" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    for i in range(5):
        wx = x + (-16 + i * 7.5) * u
        o.append(f'<rect x="{f(wx)}" y="{f(base - 30 * u)}" width="{f(2.4 * u)}" height="{f(2.4 * u)}" fill="#3A2A1A" stroke="#0D0D0F" stroke-width="1"></rect>')
    return "".join(o)

def court_scene(p, w, h, seed, cloud=False, solomon=None, crowd=True, smoke=False):
    """The court before the house of Jehovah full of the assembly; cloud=True: the cloud filling the house; solomon='pray'
    (hands spread toward heaven before the altar) or 'bless' (standing, turned to the people)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2" if not cloud else "#E8E2D6", "#F3E8C8" if not cloud else "#FFF4C2"),
         ground(w, h, h * 0.66, "#C8B88A", dy=0), temple_front(w * 0.5, h * 0.66, w * 0.6, seed)]
    if cloud:
        r = random.Random(seed)
        for i in range(14):
            o.append(f'<circle cx="{f(w * 0.5 + r.uniform(-w * 0.3, w * 0.3))}" cy="{f(h * r.uniform(0.1, 0.5))}" r="{f(w * r.uniform(0.06, 0.12))}" fill="#F3EFE6" opacity="0.85"></circle>')
        o.append(V.rays(w * 0.5, h * 0.4, 30, 20, max(w, h), color="#FFD23F", op=0.25))
    if smoke:
        o.append(horned_altar(w * 0.5, h * 0.86, min(0.8, h / 400), fire=True, seed=seed))
    s = fit(b, h * 0.3)
    if solomon == "pray":
        o.append(horned_altar(w * 0.5, h * 0.82, min(0.7, h / 440)))
        o.append(S3.dancer(w * 0.5, b, s * 1.1, p + "sd", [(-22, -158), (-40, -200), (-46, -238)], [(22, -158), (40, -200), (46, -238)], cloth=SOL_C, body="#5A2A16"))
    elif solomon == "bless":
        o.append(sol_fig(p, w * 0.5, b, s * 1.1, up=[(-22, -158), (-40, -190), (-50, -220)]))
    if crowd:
        o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.3, h * 0.74, b, 8, s * 0.6, s))
        o.append(crowd_at(p, w, h, seed + 1, w * 0.7, w * 0.98, h * 0.74, b, 8, s * 0.6, s, flip=True))
    return "".join(o)

def ark_up(p, w, h, seed):
    """The priests bringing up the ark of the covenant out of the city of David, the elders following, sacrifices by the way."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE680", "#F3D8A0"), J.city_hill(w * 0.84, h * 0.6, w * 0.3, h * 0.3, seed), ground(w, h, h * 0.62, "#C8A06A", dy=0)]
    s = fit(b, h * 0.4)
    o.append(J.ark_borne(p, w * 0.46, b, s, uid=p + "ab"))
    o.append(crowd_at(p, w, h, seed, w * 0.7, w * 0.98, h * 0.7, b, 8, s * 0.6, s * 0.9, flip=True))
    o.append(S4.altar(w * 0.1, b, min(0.9, h / 360), seed=seed))
    return "".join(o)

def ark_oracle(w, h):
    """The ark in its place in the oracle under the wings of the cherubim, the ends of the staves seen from the holy place;
    nothing in it save the two tables of stone."""
    o = [cherubim(w, h)]
    u = min(w * 0.8 / 20, h * 0.74 / 12); base = h * 0.9
    o.append(f'<path d="M{f(w * 0.5 - 6 * u)} {f(base - 0.9 * u)} L {f(w * 0.5 + 6 * u)} {f(base - 0.9 * u)}" stroke="#8A5A1A" stroke-width="{f(0.25 * u)}"></path>')
    o.append(tag(w * 0.5 + 5.6 * u, base - 0.9 * u, "THE STAVES", w * 0.5 + 7 * u, base - 3 * u) + tag(w * 0.5, base - 0.7 * u, "THE TWO TABLES OF STONE WITHIN", w * 0.5 - 6 * u, base - 4 * u))
    return "".join(o)

def feast_tents(p, w, h, seed):
    """Fourteen days of feast, from the entrance of Hamath to the brook of Egypt; then the people going to their tents."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#FFB04A", "#F3D8A0"), J.city_hill(w * 0.5, h * 0.44, w * 0.5, h * 0.2, seed), ground(w, h, h * 0.46, "#C8A06A", dy=0),
         N.camp(20, -10, w + 10, h * 0.5, h * 0.74, seed)]
    s = fit(b, h * 0.3)
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.98, h * 0.8, b, 12, s * 0.7, s))
    return "".join(o)

# ---- 1 Kings 9–10 -------------------------------------------------------------------------------------------------------
import judges2 as J2, egypt as EG
def ship(x, y, s=1.0, sail="#E8E2D6", flip=False):
    """A ship of the navy: a curved hull, a mast and a square sail, a row of oars. (x, y) = waterline centre."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            '<path d="M-90 -10 C -70 14 70 14 96 -16 L 100 -30 C 80 -14 -60 -14 -94 -28 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M-94 -28 C -100 -40 -96 -52 -88 -56" stroke="#8A5A30" stroke-width="6" fill="none"></path>'
            '<path d="M0 -20 L 0 -140" stroke="#3A2214" stroke-width="5"></path>'
            f'<path d="M-46 -132 L 46 -132 L 40 -50 L -40 -50 Z" fill="{sail}" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M-48 -134 L 48 -134" stroke="#3A2214" stroke-width="4"></path>'
            + "".join(f'<path d="M{dx} -6 L {dx - 10} 20" stroke="#5A3A22" stroke-width="3"></path>' for dx in range(-60, 70, 20)) + '</g>')

def navy(p, w, h, seed, port=True):
    """The navy of ships at Ezion-geber on the shore of the Red Sea (port=False: on the open sea, bound for Ophir)."""
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.8, h * 0.2, 20, color="#FFE680", op=0.4)]
    if port:
        o += [hills(w, h, h * 0.4, seed, color="#A8704A", amp=20), f'<rect x="-10" y="{f(h * 0.54)}" width="{f(w + 20)}" height="{f(h * 0.6)}" fill="#1F6F9A"></rect>',
              f'<path d="M-10 {f(h * 0.54)} L {f(w * 0.3)} {f(h * 0.54)} L {f(w * 0.2)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>']
    else:
        o.append(f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.6)}" fill="#1F6F9A"></rect>')
    k = min(1.0, h / 320)
    for i in range(3):
        o.append(ship(w * (0.42 + i * 0.22), h * (0.7 + (i % 2) * 0.08), k * (0.8 + 0.1 * (i % 2)), sail=["#E8E2D6", "#B5121B", "#E8E2D6"][i]))
    return "".join(o)

def cabul(p, w, h, seed):
    """The cities of Galilee given to Hiram: poor hill-towns among stones, Hiram looking and not pleased."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#C8C0B0", "#E8D8C0"), hills(w, h, h * 0.5, seed, color="#8A8070", amp=16), ground(w, h, h * 0.58, "#A89A80", dy=0)]
    for i in range(4):
        o.append(J.city_hill(w * (0.4 + i * 0.16), h * 0.6, w * 0.12, h * 0.1, seed + i))
    o.append(S4.stone_heap(w * 0.6, b, w * 0.2, h * 0.1, seed))
    o.append(king_fig(p, w * 0.16, b, fit(b, h * 0.4), cloth="#6A1A5A"))
    return "".join(o)

def cities_map(w, h):
    """The levy's works as a technical map: Jerusalem and Millo, Hazor, Megiddo, Gezer, Beth-horon, Baalath, Tamar."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.14)} -10 C {f(w * 0.12)} {f(h * 0.3)} {f(w * 0.1)} {f(h * 0.7)} {f(w * 0.06)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    for nm, x, y in [("HAZOR", 0.56, 0.12), ("MEGIDDO", 0.4, 0.3), ("GEZER", 0.3, 0.6), ("BETH-HORON", 0.38, 0.52), ("BAALATH", 0.24, 0.7), ("JERUSALEM · MILLO", 0.5, 0.62),
                     ("TAMAR", 0.56, 0.92)]:
        o.append(node(w * x, h * y, nm, "#FFD23F" if "JERUSALEM" in nm else "#8FD0E2", r=5, dy=-11, size=9))
    o.append(node(w * 0.6, h * 0.98, "EZION-GEBER", "#D7261E", r=5, dy=-11, size=9))
    return "".join(o)

def sheba_train(p, w, h, seed):
    """The queen of Sheba coming to Jerusalem with a very great train, camels that bare spices, gold and precious stones."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#FFB04A", "#F3D8A0"), J.city_hill(w * 0.86, h * 0.5, w * 0.3, h * 0.26, seed), ground(w, h, h * 0.52, "#D8B070", dy=0)]
    k = min(0.9, h / 360)
    for i in range(5):
        x = w * (0.1 + i * 0.16); y = b - (4 - i) * h * 0.04
        o.append(J1.camel(x, y, k * (0.7 + 0.08 * i), color="#B5844A", rider="#E8B830" if i == 4 else None))
        o.append(f'<rect x="{f(x - 20 * k)}" y="{f(y - 120 * k)}" width="{f(30 * k)}" height="{f(16 * k)}" fill="#7A3A6A" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    return "".join(o)

def sheba_court(p, w, h, seed):
    """The queen before Solomon on his throne, the gifts set down: gold, spices, precious stones."""
    b = h * 0.92; k = min(1.2, h / 300)
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), S3.throne(w * 0.22, b, k)]
    s = fit(b, h * 0.4)
    o.append(sol_fig(p, w * 0.22, b - 40 * k, s * 0.86))
    o.append(mk.person(p, round(w * 0.72), round(b), round(s * 0.95, 3), body="#5A2A16", cloth="#E8B830", woman=True, hair="#0D0D0F", sw=3, flip=True, extra=CROWN))
    for i in range(3):
        x = w * (0.42 + i * 0.08)
        o.append(f'<rect x="{f(x - 18)}" y="{f(b - 26)}" width="36" height="26" fill="{["#E8B830", "#8A5A30", "#7A3A6A"][i]}" stroke="#0D0D0F" stroke-width="2"></rect>')
    return "".join(o)

def gold_shields_king(w, h, seed):
    """Two hundred bucklers and three hundred shields of beaten gold hung in the house of the forest of Lebanon."""
    import sa2.art as K2
    return K2.gold_shields(w, h, seed)

def ivory_throne(w, h):
    """The great throne of ivory overlaid with gold: six steps, the top round behind, two lions by the stays, twelve lions
    upon the steps."""
    o = [bp(w, h), title_bar(w, "THE THRONE OF IVORY · SIX STEPS · TWELVE LIONS")]
    cx, base = w * 0.5, h * 0.92; u = min(w / 16, h / 11)
    for i in range(6):
        sw = (6 - i) * 1.2 * u + 3 * u
        o.append(f'<rect x="{f(cx - sw / 2)}" y="{f(base - (i + 1) * 0.7 * u)}" width="{f(sw)}" height="{f(0.7 * u)}" fill="#F3E8D0" stroke="#0D0D0F" stroke-width="1.6"></rect>')
        for d in (-1, 1):
            o.append(J2.lion(cx + d * (sw / 2 - 0.4 * u), base - (i + 1) * 0.7 * u, u / 160, flip=d > 0, roar=False))
    ty = base - 4.2 * u
    o.append(f'<path d="M{f(cx - 1.6 * u)} {f(ty)} L {f(cx - 1.6 * u)} {f(ty - 3 * u)} C {f(cx - 1.6 * u)} {f(ty - 4.4 * u)} {f(cx + 1.6 * u)} {f(ty - 4.4 * u)} {f(cx + 1.6 * u)} {f(ty - 3 * u)} L {f(cx + 1.6 * u)} {f(ty)} Z" fill="{GOLD}" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<rect x="{f(cx - 1.8 * u)}" y="{f(ty - 0.4 * u)}" width="{f(3.6 * u)}" height="{f(0.5 * u)}" fill="#F3E8D0" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    for d in (-1, 1):
        o.append(J2.lion(cx + d * 2.2 * u, ty, u / 120, flip=d > 0, roar=False))
    o.append(tag(cx + 1.6 * u, ty - 3.4 * u, "THE TOP ROUND BEHIND", cx + 4 * u, ty - 4 * u) + tag(cx - 2.6 * u, ty - 0.6 * u, "TWO LIONS BESIDE THE STAYS", cx - 5 * u, ty - 3 * u))
    return "".join(o)

def tarshish(p, w, h, seed):
    """The navy of Tarshish every three years: gold, silver, ivory, apes and peacocks."""
    o = [navy(p, w, h, seed, port=False)]
    cx, cy = w * 0.18, h * 0.86
    o.append(f'<path d="M{f(cx)} {f(cy)} C {f(cx - 40)} {f(cy - 30)} {f(cx - 30)} {f(cy - 70)} {f(cx)} {f(cy - 80)} C {f(cx + 30)} {f(cy - 70)} {f(cx + 40)} {f(cy - 30)} {f(cx)} {f(cy)} Z" fill="#1F5F7A" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<circle cx="{f(cx + 26 * math.cos(a))}" cy="{f(cy - 44 + 34 * math.sin(a))}" r="5" fill="#2C9DB8" stroke="#E8B830" stroke-width="2"></circle>' for a in [j * 0.7 - 2.6 for j in range(6)])
             + f'<circle cx="{f(cx)}" cy="{f(cy - 4)}" r="9" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="2"></circle>')
    return "".join(o)

def tribute(p, w, h, seed):
    """All the earth bringing tribute: vessels of silver and gold, raiment, armor, spices, horses and mules."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE680", "#F3D8A0"), J.city_hill(w * 0.86, h * 0.5, w * 0.3, h * 0.26, seed), ground(w, h, h * 0.52, "#C8A06A", dy=0)]
    s = fit(b, h * 0.36)
    for i in range(5):
        x = w * (0.08 + i * 0.13)
        o.append(man(p, x, b - (i % 2) * 8, s * 0.9, ["#6A1A5A", "#1F5FAD", "#2E6B3A", "#B5652E", "#E8E2D6"][i], up=[(22, -158), (30, -170), (36, -186)])
                 + f'<path d="M{f(x + 36 * s * 0.9)} {f(b - 186 * s * 0.9)} l -10 -18 l 20 0 Z" fill="{["#C8C8D0", "#E8B830"][i % 2]}" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append(E3.horse(w * 0.78, b, min(0.7, h / 400)))
    return "".join(o)

# ---- 1 Kings 11 ---------------------------------------------------------------------------------------------------------
def high_places(p, w, h, seed):
    """The mount before Jerusalem with the high places of Chemosh and Molech, smoke going up from strange altars; the city
    below at dusk."""
    o = [mk.defs(p, *ALL), sky(w, h, "#3A1A3A", "#C8603A"),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.46)} {f(h * 0.3)} {f(w * 0.8)} {f(h * 0.26)} {f(w + 10)} {f(h * 0.36)} L {f(w + 10)} {f(h + 10)} Z" fill="#4A3A3A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         J.city_hill(w * 0.2, h * 0.92, w * 0.4, h * 0.3, seed), ground(w, h, h * 0.92, "#2A1E1E", dy=0)]
    for i, (x, y) in enumerate(((0.6, 0.36), (0.78, 0.3), (0.92, 0.36))):
        o.append(f'<path d="M{f(w * x - 14)} {f(h * y)} L {f(w * x - 10)} {f(h * y - 20)} L {f(w * x + 10)} {f(h * y - 20)} L {f(w * x + 14)} {f(h * y)} Z" fill="#5A5A6A" stroke="#0D0D0F" stroke-width="2"></path>'
                 + E.blaze(w * x, h * y - 20, 12, 24, seed + i, n=3)
                 + f'<path d="M{f(w * x)} {f(h * y - 30)} C {f(w * x - 14)} {f(h * y - 60)} {f(w * x + 14)} {f(h * y - 90)} {f(w * x)} -10" stroke="#5A4A5A" stroke-width="10" fill="none" opacity="0.5"></path>')
    return "".join(o)

def wives(p, w, h, seed):
    """Solomon among his foreign wives, each with her own god's incense burning."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84)]
    s = fit(b, h * 0.4)
    o.append(sol_fig(p, w * 0.5, b, s * 0.95))
    for i, c in enumerate(("#8A1E2E", "#2E6B3A", "#B5652E", "#6A1A5A", "#1F5F7A", "#C8A030")):
        x = w * (0.08 + i * 0.17) if i < 3 else w * (0.08 + i * 0.17 + 0.06)
        o.append(mk.person(p, round(x), round(b - (i % 2) * 6), round(s * 0.84, 3), body="#5A2A16", cloth=c, woman=True, hair="#1A1210", sw=3, flip=i >= 3))
    return "".join(o)

def hadad(p, w, h, seed):
    """Hadad the Edomite, a little child, fled into Egypt; Pharaoh's house by the Nile."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE680", "#F3D8A0"), EG.pyramid(w * 0.78, h * 0.62, w * 0.3, h * 0.3), ground(w, h, h * 0.62, "#E8C88A", dy=0),
         f'<path d="M-10 {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.68)} {f(w * 0.6)} {f(h * 0.74)} {f(w + 10)} {f(h * 0.7)}" stroke="#2C7DA8" stroke-width="10" fill="none"></path>']
    s = fit(b, h * 0.36)
    for i in range(3):
        o.append(man(p, w * (0.2 + i * 0.1), b, s * (0.9 if i != 1 else 0.5), ["#8A6A4A", "#C8703A", "#6A5A3A"][i]))
    return "".join(o)

def damascus(p, w, h, seed):
    """Rezon reigning in Damascus, a walled city on the plain under the mountains."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, color="#8A8A9A", amp=30),
         ground(w, h, h * 0.6, "#B8A86A", dy=0), J.jericho(w * 0.2, w * 0.8, h * 0.4, h * 0.7, seed, towers=4, houses=True)]
    return "".join(o)

def rent_garment(p, w, h, seed, pieces=False):
    """Ahijah and Jeroboam alone in the field, Ahijah's new garment; pieces=True: the garment rent in twelve pieces, ten held
    out to Jeroboam."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#E8F6FA"), hills(w, h, h * 0.5, seed, color="#7A9A5A", amp=12), ground(w, h, h * 0.6, "#9CCB5E", dy=0)]
    s = fit(b, h * 0.42)
    o.append(prophet_fig(p, w * 0.32, b, s, cloth="#5A5A6A", up=[(22, -158), (40, -150), (60, -146)] if pieces else None))
    o.append(mk.person(p, round(w * 0.7), round(b), round(s, 3), body=SKIN, cloth="#2E6B3A", kind="Tunic", sw=3, flip=True, extra=A.headcloth("#2E6B3A") + A.BLACK_BEARD))
    if pieces:
        r = random.Random(seed)
        for i in range(12):
            x = w * 0.5 + (i % 6 - 2.5) * w * 0.04; y = b - (150 if i < 10 else 40) * s - (i // 6) * 22
            if i >= 10: x = w * (0.2 + (i - 10) * 0.06); y = b - 4
            o.append(f'<rect x="{f(x - 10)}" y="{f(y - 8)}" width="20" height="16" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6" transform="rotate({f(r.uniform(-20, 20))} {f(x)} {f(y)})"></rect>')
    else:
        o.append(f'<path d="M{f(w * 0.32 - 30 * s)} {f(b - 150 * s)} L {f(w * 0.32 + 30 * s)} {f(b - 150 * s)} L {f(w * 0.32 + 40 * s)} {f(b - 10 * s)} L {f(w * 0.32 - 40 * s)} {f(b - 10 * s)} Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2" opacity="0.9"></path>')
    return "".join(o)

def ten_two(w, h):
    """The kingdom rent: twelve tribes, ten given to Jeroboam, one kept for David's sake (a technical map of the tribes)."""
    o = [grid_bg(w, h)]
    names = ["REUBEN", "SIMEON", "LEVI", "JUDAH", "ISSACHAR", "ZEBULUN", "DAN", "NAPHTALI", "GAD", "ASHER", "EPHRAIM", "MANASSEH", "BENJAMIN"]
    tribes = [n for n in names if n not in ("LEVI",)]
    for i, n in enumerate(tribes):
        x = w * (0.08 + (i % 6) * 0.17); y = h * (0.3 + (i // 6) * 0.3)
        c = "#FFD23F" if n == "JUDAH" else ("#8FD0E2" if n == "BENJAMIN" else "#D7261E")
        o.append(node(x, y, n, c, r=6, dy=-12, size=9))
    o.append(label(w * 0.04, h * 0.84, "RED · TEN TRIBES TO JEROBOAM", "#D7261E", 9, "start") + label(w * 0.96, h * 0.84, "GOLD · ONE TRIBE FOR DAVID'S SAKE", "#FFD23F", 9, "end"))
    return "".join(o)

# ---- 1 Kings 12–13 ------------------------------------------------------------------------------------------------------
JERO_C, REHO_C = "#2E6B3A", "#1F3A7A"
def counsel(p, w, h, seed, young=False):
    """Rehoboam on his throne taking counsel: the old men (white beards) or the young men grown up with him."""
    b = h * 0.92; k = min(1.2, h / 300)
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), S3.throne(w * 0.2, b, k)]
    s = fit(b, h * 0.4)
    o.append(king_fig(p, w * 0.2, b - 40 * k, s * 0.86, cloth=REHO_C))
    for i in range(4):
        c = ["#8A6A4A", "#5A5A6A", "#6A4A3A", "#4A5A4A"][i]
        if young: o.append(mk.person(p, round(w * (0.5 + i * 0.12)), round(b), round(s * 0.86, 3), body="#5A2A16", cloth=["#B5121B", "#E8B830", "#1F5FAD", "#6A1A5A"][i], kind="Tunic", sw=3, flip=True))
        else: o.append(prophet_fig(p, w * (0.5 + i * 0.12), b, s * 0.86, cloth=c, flip=True))
    return "".join(o)

def to_tents(p, w, h, seed):
    """To your tents, O Israel: the people turning away to their tents, the king's chariot fleeing to Jerusalem."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#E8C8A0"), J.city_hill(w * 0.12, h * 0.5, w * 0.3, h * 0.2, seed), ground(w, h, h * 0.52, "#A89A6A", dy=0),
         N.camp(10, w * 0.4, w + 10, h * 0.56, h * 0.7, seed)]
    s = fit(b, h * 0.3)
    o.append(crowd_at(p, w, h, seed, w * 0.36, w * 0.98, h * 0.74, b, 10, s * 0.7, s))
    o.append(E3.chariot(w * 0.18, b, min(0.9, h / 360), flip=True, driver=REHO_C))
    return "".join(o)

def calves(p, w, h, seed, people=True):
    """The two calves of gold: one in Beth-el and the other in Dan, each on its high place with an altar; the people bowing."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A5A", "#E8A06A"), hills(w, h, h * 0.5, seed, color="#6A5A4A", amp=14), ground(w, h, h * 0.62, "#8A7A5A", dy=0)]
    for i, (x, nm) in enumerate(((0.28, "BETH-EL"), (0.74, "DAN"))):
        o.append(V.calf(w * x, h * 0.66, min(0.9, h / 360), uid=f"{p}c{i}") + label(w * x, h * 0.72, nm, "#FFD23F", 10))
        o.append(horned_altar(w * x + w * 0.12, h * 0.7, min(0.4, h / 700), fire=True, seed=seed + i))
    if people:
        for i in range(6):
            o.append(N.prostrate(w * (0.08 + i * 0.16), b, fit(b, h * 0.3) * 0.6, color=WAR[i % 4], skin="#9A6A4A"))
    return "".join(o)

def bethel_altar(p, w, h, seed, rent=False, hand=False):
    """The altar at Beth-el: Jeroboam standing by it to burn incense, the man of God out of Judah crying against it; rent=True:
    the altar rent and its ashes poured out; hand=True: the king's hand put forth and dried up."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A5A", "#E8A06A"), V.calf(w * 0.86, h * 0.6, min(0.6, h / 500), uid=p + "c"), ground(w, h, h * 0.62, "#8A7A5A", dy=0)]
    if rent:
        o.append(f'<g transform="translate({f(w * 0.5)} {f(b)}) scale({f(min(1.3, h / 260))})"><path d="M-60 0 L -60 -90 L -6 -96 L -14 -50 L 0 0 Z" fill="#B07A3A" stroke="#0D0D0F" stroke-width="2.4" transform="rotate(-6)"></path>'
                 '<path d="M8 0 L -2 -48 L 8 -98 L 66 -90 L 62 0 Z" fill="#B07A3A" stroke="#0D0D0F" stroke-width="2.4" transform="rotate(6)"></path>'
                 '<path d="M-90 0 C -70 -20 -40 -16 -20 -4 Z M20 -4 C 40 -18 70 -20 96 0 Z" fill="#6A6460"></path></g>')
    else:
        o.append(horned_altar(w * 0.5, b, min(1.2, h / 280), fire=True, seed=seed))
    s = fit(b, h * 0.42)
    o.append(king_fig(p, w * 0.24, b, s, cloth=JERO_C, up=[(22, -158), (60, -150), (100, -150)] if hand else None))
    o.append(prophet_fig(p, w * 0.8, b, s, cloth="#4A3A2A", flip=True, up=[(22, -158), (40, -200), (40, -230)] if not hand else None))
    return "".join(o)

def oak_sitting(p, w, h, seed):
    """The man of God sitting under an oak by the way; the old prophet riding up on his ass."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#E8C8A0", "#F3D8A0"), hills(w, h, h * 0.5, seed, color="#9A8A6A", amp=12), ground(w, h, h * 0.6, "#B89A6A", dy=0),
         S4.great_oak(w * 0.24, b, min(1.0, h / 360), seed)]
    s = fit(b, h * 0.4)
    o.append(E.kneel(w * 0.3, b, s * 0.8, color="#4A3A2A", skin="#B98A6E"))
    o.append(N.mount(w * 0.74, b, min(1.0, h / 320), flip=True, rider_cloth="#6A645E", p=p + "m"))
    return "".join(o)

def lion_way(p, w, h, seed, body=True):
    """The way: the ass standing, and the lion standing still beside it (13:24–28 told in words; no body drawn)."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#E8B880"), hills(w, h, h * 0.5, seed, color="#8A7A5A", amp=12), ground(w, h, h * 0.58, "#A89A6A", dy=0),
         f'<path d="M{f(w * 0.2)} {f(h + 10)} C {f(w * 0.36)} {f(h * 0.78)} {f(w * 0.5)} {f(h * 0.64)} {f(w * 0.6)} {f(h * 0.58)}" stroke="#C8B890" stroke-width="{f(w * 0.08)}" fill="none"></path>']
    k = min(1.0, h / 340)
    o.append(N.ass(w * 0.36, b, k * 0.9) + J2.lion(w * 0.66, b, k * 0.8, flip=True, roar=False))
    return "".join(o)

def grave_bethel(w, h, seed):
    """The old prophet's own grave at Beth-el, a sealed tomb in the rock at evening."""
    import jos.art as JA
    return JA.cave(w, h, seed, sealed=True, dusk=True)

# ---- 1 Kings 14–15 ------------------------------------------------------------------------------------------------------
def ahijah_door(p, w, h, seed):
    """The house of Ahijah at Shiloh: the old prophet, blind, sitting within; Jeroboam's wife disguised at the door with her
    loaves, cakes and cruse of honey."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A2A"></rect>',
         f'<rect x="{f(w * 0.62)}" y="{f(h * 0.14)}" width="{f(w * 0.3)}" height="{f(b - h * 0.14)}" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2.6"></rect>', ground(w, h, b, "#2A1A14", dy=0)]
    s = fit(b, h * 0.4)
    o.append(E.kneel(w * 0.28, b, s * 0.85, color="#5A5A6A", skin="#B98A6E"))
    o.append(mk.person(p, round(w * 0.74), round(b), round(s * 0.9, 3), body="#3A1E14", cloth="#5A4A3A", woman=True, hair="#3A3430", sw=3, flip=True,
                       extra='<path d="M-24 -200 C -30 -170 -28 -130 -20 -110 L 20 -110 C 28 -130 30 -170 24 -200 Z" fill="#4A4038" opacity="0.95"></path>'))
    o.append(f'<rect x="{f(w * 0.5)}" y="{f(b - 20)}" width="34" height="20" rx="8" fill="#D9A25A" stroke="#0D0D0F" stroke-width="2"></rect>')
    return "".join(o)

def threshold(p, w, h, seed):
    """At Tirzah: the threshold of the house at evening, the woman's feet upon it (the child's death told in words only)."""
    o = [mk.defs(p, *ALL), sky(w, h, "#3A2A4A", "#C88A6A"), J.city_hill(w * 0.2, h * 0.6, w * 0.4, h * 0.3, seed), ground(w, h, h * 0.62, "#5A4A4A", dy=0),
         f'<rect x="{f(w * 0.46)}" y="{f(h * 0.2)}" width="{f(w * 0.44)}" height="{f(h * 0.62)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.6"></rect>',
         f'<rect x="{f(w * 0.6)}" y="{f(h * 0.4)}" width="{f(w * 0.16)}" height="{f(h * 0.42)}" fill="#1A0E10" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.56)}" y="{f(h * 0.82)}" width="{f(w * 0.24)}" height="{f(h * 0.04)}" fill="#A89A80" stroke="#0D0D0F" stroke-width="2"></rect>']
    o.append(mk.person(p, round(w * 0.5), round(h * 0.86), round(fit(h * 0.86, h * 0.42), 3), body="#3A1E14", cloth="#5A4A3A", woman=True, hair="#3A3430", sw=3))
    return "".join(o)

def shishak(p, w, h, seed):
    """Shishak king of Egypt carrying away the treasures and the shields of gold from Jerusalem: chariots and bearers on the road."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE680", "#F3D8A0"), J.city_hill(w * 0.86, h * 0.5, w * 0.3, h * 0.28, seed), ground(w, h, h * 0.52, "#C8A06A", dy=0)]
    s = fit(b, h * 0.34)
    for i in range(4):
        x = w * (0.3 + i * 0.12)
        o.append(man(p, x, b - i * 6, s * 0.9, ["#F3EFE6", "#E8B830", "#1F5FAD", "#F3EFE6"][i], flip=True, up=[(-22, -158), (-26, -190), (-14, -210)])
                 + f'<circle cx="{f(x - 14 * s)}" cy="{f(b - i * 6 - 218 * s * 0.9)}" r="{f(18 * s)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></circle>')
    o.append(E3.chariot(w * 0.12, b, min(0.9, h / 360), flip=True, color="#3A2214", driver="#1F5FAD"))
    return "".join(o)

def brass_shields(w, h, seed):
    """The shields of brass made in their stead, borne by the guard."""
    import sa2.art as K2
    return K2.gold_shields(w, h, seed).replace("#E8B830", BRASS).replace("#FFF4C2", "#E8B880")

def ramah(p, w, h, seed):
    """All Judah carrying away the stones and the timber of Ramah to build Geba and Mizpah."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.46, seed, color="#8A8A6A", amp=12), ground(w, h, h * 0.56, "#B89A6A", dy=0),
         S4.stone_heap(w * 0.78, h * 0.72, w * 0.3, h * 0.14, seed)]
    s = fit(b, h * 0.36)
    for i in range(5):
        x = w * (0.08 + i * 0.13)
        o.append(man(p, x, b - (i % 2) * 8, s * 0.9, WAR[i % 4], flip=True, up=[(-22, -158), (-20, -196), (0, -210)])
                 + f'<ellipse cx="{f(x - 4)}" cy="{f(b - (i % 2) * 8 - 218 * s * 0.9)}" rx="{f(20 * s)}" ry="{f(12 * s)}" fill="#A89E92" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    return "".join(o)

def asa_idol(p, w, h, seed):
    """Asa cutting down the abominable image made for an Asherah, burnt at the brook Kidron."""
    o = [mk.defs(p, *ALL), sky(w, h, "#3A2A3A", "#C8603A"), ground(w, h, h * 0.66, "#4A3A2A", dy=0),
         f'<path d="M-10 {f(h * 0.76)} C {f(w * 0.3)} {f(h * 0.72)} {f(w * 0.6)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.76)}" stroke="#2C7DA8" stroke-width="10" fill="none"></path>',
         f'<path d="M{f(w * 0.36)} {f(h * 0.7)} L {f(w * 0.64)} {f(h * 0.6)}" stroke="#5A3A22" stroke-width="18" stroke-linecap="round"></path>',
         E.blaze(w * 0.5, h * 0.7, w * 0.16, h * 0.36, seed, n=7)]
    o.append(king_fig(p, w * 0.16, h * 0.92, fit(h * 0.92, h * 0.4), cloth="#1F3A7A"))
    return "".join(o)

# ---- 1 Kings 16–17 ------------------------------------------------------------------------------------------------------
MANTLE = ('<path d="M-30 -168 C -40 -150 -42 -120 -38 -90 L 38 -90 C 42 -120 40 -150 30 -168 Z" fill="#5A3A1E" stroke="#0D0D0F" stroke-width="2.4"></path>'
          + "".join(f'<path d="M{x} -160 l -3 10 M{x + 6} -140 l -3 10 M{x - 4} -120 l -3 10" stroke="#3A2210" stroke-width="2"></path>' for x in (-24, -10, 4, 18))
          + '<path d="M-26 -110 L 26 -110" stroke="#2A1408" stroke-width="5"></path>')
def elijah_fig(p, x, y, s, flip=False, up=None):
    """Elijah at a distance: a hairy mantle of brown over a dark tunic, a girdle of leather, bareheaded, black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#4A3A2A", kind="Tunic", sw=3, flip=flip, up=up, extra=MANTLE + A.BLACK_BEARD)

def baal_altar(p, w, h, seed):
    """The house of Baal in Samaria: an altar for Baal and the Asherah pole, Ahab and Jezebel before it."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5A2A3A", "#E8803A"), ground(w, h, h * 0.66, "#6A5A4A", dy=0),
         f'<path d="M{f(w * 0.46)} {f(h * 0.2)} L {f(w * 0.54)} {f(h * 0.2)} L {f(w * 0.53)} {f(h * 0.7)} L {f(w * 0.47)} {f(h * 0.7)} Z" fill="#7A5A3A" stroke="#0D0D0F" stroke-width="2.4"></path>'
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.2)}" r="{f(w * 0.04)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></circle>',
         horned_altar(w * 0.5, h * 0.84, min(0.8, h / 380), fire=True, seed=seed)]
    s = fit(b, h * 0.42)
    o.append(king_fig(p, w * 0.18, b, s, cloth=AHAB_C))
    o.append(mk.person(p, round(w * 0.82), round(b), round(s * 0.95, 3), body="#5A2A16", cloth="#1A1214", woman=True, hair="#0D0D0F", sw=3, flip=True, extra=CROWN))
    return "".join(o)

def samaria_hill(p, w, h, seed, city=True):
    """The hill Samaria bought of Shemer for two talents of silver, and the city built upon it."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#7A8A6A", amp=12),
         f'<path d="M{f(w * 0.1)} {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.4)} {f(w * 0.7)} {f(h * 0.4)} {f(w * 0.9)} {f(h * 0.86)} Z" fill="#8A9A5A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.86, "#A89A6A", dy=0)]
    if city: o.append(J.jericho(w * 0.3, w * 0.7, h * 0.3, h * 0.52, seed, towers=3, houses=True))
    return "".join(o)

def cherith(p, w, h, seed, dry=False):
    """Elijah hidden by the brook Cherith before the Jordan, the ravens bringing bread and flesh; dry=True: the brook dried up."""
    r = random.Random(seed)
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE6A0" if dry else "#8FD0E2", "#F3D8A0" if dry else "#E8F6FA"),
         f'<path d="M-10 {f(h * 0.3)} L {f(w * 0.3)} {f(h * 0.36)} L {f(w * 0.36)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w + 10)} {f(h * 0.26)} L {f(w * 0.7)} {f(h * 0.34)} L {f(w * 0.64)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} Z" fill="#7A5A3A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.72, "#A89070", dy=0)]
    if dry: o.append(f'<path d="M{f(w * 0.36)} {f(h * 0.8)} C {f(w * 0.46)} {f(h * 0.76)} {f(w * 0.56)} {f(h * 0.84)} {f(w * 0.66)} {f(h * 0.8)}" stroke="#C8B080" stroke-width="18" fill="none"></path>'
                     + "".join(f'<path d="M{f(w * (0.4 + i * 0.06))} {f(h * 0.8)} l 8 6 l -4 6" stroke="#7A5A3A" stroke-width="2" fill="none"></path>' for i in range(4)))
    else: o.append(f'<path d="M{f(w * 0.36)} {f(h * 0.8)} C {f(w * 0.46)} {f(h * 0.76)} {f(w * 0.56)} {f(h * 0.84)} {f(w * 0.66)} {f(h * 0.8)}" stroke="#2C9DB8" stroke-width="16" fill="none"></path>')
    s = fit(b, h * 0.4)
    o.append(elijah_fig(p, w * 0.24, b, s))
    if not dry:
        for i in range(2):
            x = w * (0.46 + i * 0.16); y = h * (0.2 + i * 0.08)
            o.append(f'<path d="M{f(x - 30)} {f(y)} Q {f(x - 14)} {f(y - 20)} {f(x)} {f(y)} Q {f(x + 14)} {f(y - 20)} {f(x + 30)} {f(y)}" fill="#0D0D0F" stroke="#0D0D0F" stroke-width="3"></path>'
                     f'<ellipse cx="{f(x)}" cy="{f(y + 4)}" rx="10" ry="6" fill="#0D0D0F"></ellipse><rect x="{f(x - 6)}" y="{f(y + 8)}" width="12" height="8" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1"></rect>')
    return "".join(o)

def zarephath(p, w, h, seed):
    """At the gate of Zarephath a widow gathering sticks; Elijah calling to her."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE6A0", "#F3D8A0"), S4.gatehouse(w * 0.76, b, w * 0.4, h * 0.6), ground(w, h, b, "#C8A06A", dy=0)]
    s = fit(b, h * 0.42)
    o.append(E.kneel(w * 0.52, b, s * 0.8, color="#3A3A3E", skin="#B98A6E", flip=True))
    o.append("".join(f'<path d="M{f(w * 0.44 + i * 8)} {f(b - 4)} L {f(w * 0.5 + i * 8)} {f(b - 20)}" stroke="#5A3A22" stroke-width="4"></path>' for i in range(2)))
    o.append(elijah_fig(p, w * 0.16, b, s))
    return "".join(o)

def jar_cruse(w, h, seed):
    """The jar of meal and the cruse of oil that failed not."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A1E"></rect>', V.rays(w * 0.5, h * 0.6, 30, 20, max(w, h), color="#FFE680", op=0.15),
         ground(w, h, h * 0.84, "#2A1A10", dy=0)]
    k = min(w, h) / 260
    o.append(f'<g transform="translate({f(w * 0.38)} {f(h * 0.86)}) scale({f(k)})"><path d="M-40 0 C -56 -40 -52 -90 -30 -110 L -26 -126 L 26 -126 L 30 -110 C 52 -90 56 -40 40 0 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2.6"></path>'
             '<ellipse cx="0" cy="-126" rx="26" ry="7" fill="#F3E8D0" stroke="#0D0D0F" stroke-width="2"></ellipse></g>'
             f'<g transform="translate({f(w * 0.64)} {f(h * 0.86)}) scale({f(k)})"><path d="M-22 0 C -30 -20 -28 -44 -12 -54 L -10 -66 L 10 -66 L 12 -54 C 28 -44 30 -20 22 0 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<path d="M12 -54 C 30 -60 36 -66 40 -76" stroke="#8A5A30" stroke-width="6" fill="none"></path><ellipse cx="0" cy="-66" rx="10" ry="3" fill="#E8C840"></ellipse></g>')
    return "".join(o)

def upper_chamber(p, w, h, seed, down=False):
    """The chamber where Elijah abode, his own bed and a lamp; down=True: Elijah coming down the stair with the child to his
    mother."""
    from genesis.art4 import clay_lamp
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#D8B88A"></rect>', ground(w, h, b, "#8A6A4A", dy=0)]
    s = fit(b, h * 0.42)
    if down:
        o.append("".join(f'<rect x="{f(w * (0.1 + i * 0.06))}" y="{f(b - (6 - i) * h * 0.06)}" width="{f(w * 0.06)}" height="{f(h * 0.06)}" fill="#A88A5A" stroke="#0D0D0F" stroke-width="1.6"></rect>' for i in range(6)))
        o.append(elijah_fig(p, w * 0.46, b, s, up=[(-22, -158), (-10, -128), (14, -124)]) + f'<ellipse cx="{f(w * 0.46 + 12 * s)}" cy="{f(b - 128 * s)}" rx="{f(18 * s)}" ry="{f(10 * s)}" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2"></ellipse>')
        o.append(mk.person(p, round(w * 0.74), round(b), round(s * 0.92, 3), body="#3A1E14", cloth="#3A3A3E", woman=True, hair="#3A3430", sw=3, flip=True, up=[(22, -158), (0, -150), (-20, -146)]))
    else:
        o.append(bed(w, h, w * 0.3, w * 0.8, b, cover="#E8E2D6", head="#D9A27A", hair="#2A1A10") + clay_lamp(w * 0.12, h * 0.5, min(1.2, h / 260)))
        o.append(E.kneel(w * 0.2, b, s * 0.8, color="#4A3A2A", skin="#B98A6E"))
    return "".join(o)

# ---- 1 Kings 18 ---------------------------------------------------------------------------------------------------------
def stone_altar(x, y, s=1.0, wet=False, fire=False, seed=1, trench=True):
    """Elijah's altar of twelve stones with the wood and the offering upon it, a trench about it (wet: water running round)."""
    r = random.Random(seed)
    o = []
    if trench:
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(110 * s)}" ry="{f(22 * s)}" fill="{"#2C9DB8" if wet else "#5A4A3A"}" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
                 f'<ellipse cx="{f(x)}" cy="{f(y - 4 * s)}" rx="{f(84 * s)}" ry="{f(14 * s)}" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    for row, n in enumerate((5, 4, 3)):
        for i in range(n):
            sx = x + (i - (n - 1) / 2) * 30 * s; sy = y - 18 * s - row * 22 * s
            o.append(f'<ellipse cx="{f(sx)}" cy="{f(sy)}" rx="{f(16 * s)}" ry="{f(12 * s)}" fill="{r.choice(["#8A8478", "#A89E92", "#7A746A"])}" stroke="#0D0D0F" stroke-width="1.8"></ellipse>')
    wy = y - 18 * s - 3 * 22 * s
    o.append("".join(f'<path d="M{f(x - 50 * s)} {f(wy - k * 7 * s)} L {f(x + 50 * s)} {f(wy - k * 7 * s - 4 * s)}" stroke="#6A4A2A" stroke-width="{f(6 * s)}" stroke-linecap="round"></path>' for k in range(3)))
    o.append(f'<path d="M{f(x - 34 * s)} {f(wy - 24 * s)} C {f(x - 30 * s)} {f(wy - 46 * s)} {f(x + 30 * s)} {f(wy - 46 * s)} {f(x + 34 * s)} {f(wy - 24 * s)} Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2"></path>')
    if wet:
        o.append("".join(f'<path d="M{f(x + d * 40 * s)} {f(wy - 10 * s)} C {f(x + d * 46 * s)} {f(wy + 20 * s)} {f(x + d * 52 * s)} {f(y - 30 * s)} {f(x + d * 60 * s)} {f(y - 6 * s)}" stroke="#8FD0E2" stroke-width="3" fill="none"></path>' for d in (-1, 1)))
    if fire:
        o.append(E.blaze(x, y - 10 * s, 120 * s, 220 * s, seed, n=9))
    return "".join(o)

def carmel(p, w, h, seed, stage="gather"):
    """Mount Carmel: the people on the slopes; stage 'gather' (Elijah before the people, the prophets of Baal massed), 'baal'
    (the prophets leaping about their altar, dark figures, nothing else drawn), 'water' (jars poured on Elijah's altar), 'fire'
    (the fire of Jehovah falling from a dark sky; the people on their faces)."""
    r = random.Random(seed); b = h * 0.94
    dark = stage == "fire"
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A" if dark else "#8FD0E2", "#C8603A" if dark else "#F3E8C8"),
         f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.3)} {f(w * 0.6)} {f(h * 0.26)} {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{"#3A3A2A" if dark else "#7A8A5A"}" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.64, "#4A4A3A" if dark else "#9A9A6A", dy=0)]
    s = fit(b, h * 0.36)
    if stage == "gather":
        o.append(elijah_fig(p, w * 0.5, b, s, up=[(-22, -158), (-40, -196), (-46, -228)]))
        o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.36, h * 0.66, b, 10, s * 0.5, s * 0.9))
        for i in range(10):
            x = w * (0.66 + (i % 5) * 0.07); y = h * (0.7 + (i // 5) * 0.1)
            o.append(mk.person(p, round(x), round(y), round(fit(y, y - h * 0.24), 3), body="#2A140C", cloth="#5A1A2A", sw=2, flip=True, extra=A.headcloth("#5A1A2A")))
    elif stage == "baal":
        o.append(horned_altar(w * 0.5, h * 0.78, min(0.9, h / 360)))
        o.append(f'<path d="M{f(w * 0.44)} {f(h * 0.56)} L {f(w * 0.56)} {f(h * 0.56)}" stroke="#6A4A2A" stroke-width="10"></path>')
        for i in range(8):
            a = i * 0.785; x = w * 0.5 + math.cos(a) * w * 0.3; y = h * 0.82 + math.sin(a) * h * 0.08
            o.append(mk.person(p, round(x), round(y), round(fit(y, y - h * 0.3), 3), body="#1A0E10", cloth="#3A1A2A", sw=2, flip=i % 2 == 1,
                               up=[(-22, -158), (-50, -200), (-40, -240)] if i % 2 else [(-22, -158), (-46, -176), (-66, -200)]))
        o.append(sun(w * 0.8, h * 0.16, 24, color="#FFF4C2", op=0.6))
    elif stage == "water":
        o.append(stone_altar(w * 0.5, h * 0.86, min(1.1, h / 300), wet=True, seed=seed))
        for i, x in enumerate((0.22, 0.78)):
            o.append(man(p, w * x, b, s, ["#6A5A3A", "#3A4A6A"][i], flip=i == 1, up=[(22, -158), (40, -200), (56, -210)] if i == 0 else [(22, -158), (40, -200), (56, -210)]))
        o.append(elijah_fig(p, w * 0.08, b, s * 0.9))
    else:
        o.append(V.rays(w * 0.5, -h * 0.2, 30, 14, h * 1.2, color="#FFB04A", op=0.35))
        o.append(f'<path d="M{f(w * 0.4)} -10 L {f(w * 0.46)} {f(h * 0.4)} L {f(w * 0.42)} {f(h * 0.42)} L {f(w * 0.5)} {f(h * 0.7)} L {f(w * 0.56)} {f(h * 0.4)} L {f(w * 0.6)} -10 Z" fill="#FFE680" opacity="0.8"></path>')
        o.append(stone_altar(w * 0.5, h * 0.86, min(1.1, h / 300), fire=True, seed=seed))
        for i in range(8):
            o.append(N.prostrate(w * (0.04 + i * 0.12) if i < 4 else w * (0.52 + (i - 4) * 0.12 + 0.08), b - (i % 2) * 10, s * 0.5, color=WAR[i % 4], skin="#9A6A4A", flip=i >= 4))
    return "".join(o)

def kishon(p, w, h, seed):
    """The brook Kishon below Carmel at evening, its banks empty (18:40 told in words only)."""
    return "".join([sky(w, h, "#2A1A3A", "#C8603A"), hills(w, h, h * 0.4, seed, color="#3A2A2A", amp=18), ground(w, h, h * 0.56, "#3A2A22", dy=0),
                    f'<path d="M-10 {f(h * 0.72)} C {f(w * 0.3)} {f(h * 0.66)} {f(w * 0.6)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.72)}" stroke="#5A3A4A" stroke-width="22" fill="none"></path>',
                    f'<path d="M-10 {f(h * 0.72)} C {f(w * 0.3)} {f(h * 0.66)} {f(w * 0.6)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.72)}" stroke="#C86A4A" stroke-width="4" fill="none" opacity="0.5"></path>'])

def small_cloud(p, w, h, seed, rain=False):
    """The top of Carmel: Elijah bowed down with his face between his knees, his servant looking toward the sea, a cloud as
    small as a man's hand; rain=True: the heavens black with clouds and wind, and a great rain."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A3A" if rain else "#8FD0E2", "#5A5A6A" if rain else "#E8F6FA"),
         f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#1F6F9A"></rect>',
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.7)} L {f(w * 0.5)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.66)} L {f(w + 10)} {f(h + 10)} Z" fill="#6A7A4A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = fit(b, h * 0.36)
    if rain:
        r = random.Random(seed)
        o.append("".join(f'<path d="M{f(r.uniform(0, w))} {f(r.uniform(0, h))} l -8 26" stroke="#B8C8E8" stroke-width="2" opacity="0.7"></path>' for _ in range(90)))
        o.append(E3.chariot(w * 0.66, b, min(0.9, h / 360), color="#3A2214", driver=AHAB_C))
        o.append(S4.runner(p, w * 0.3, b, s, cloth="#4A3A2A", body=SKIN))
    else:
        o.append(f'<ellipse cx="{f(w * 0.74)}" cy="{f(h * 0.44)}" rx="{f(w * 0.03)}" ry="{f(h * 0.015)}" fill="#F3EFE6"></ellipse>')
        o.append(E.kneel(w * 0.3, b, s * 0.8, color="#5A3A1E", skin="#B98A6E"))
        o.append(man(p, w * 0.6, b - h * 0.04, s * 0.9, "#6A5A3A", up=[(22, -158), (30, -180), (26, -200)]))
    return "".join(o)

def obadiah_way(p, w, h, seed):
    """Obadiah in the way fallen on his face before Elijah."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE6A0", "#E8C890"), hills(w, h, h * 0.5, seed, color="#9A8A6A", amp=12), ground(w, h, h * 0.6, "#C8B080", dy=0)]
    s = fit(b, h * 0.4)
    o.append(elijah_fig(p, w * 0.26, b, s))
    o.append(N.prostrate(w * 0.6, b, s * 0.8, color="#2A5A6A", skin="#C98E66", flip=True))
    return "".join(o)

# ---- 1 Kings 19–20 ------------------------------------------------------------------------------------------------------
def juniper(p, w, h, seed, angel=False):
    """Elijah asleep under a juniper-tree in the wilderness; angel=True: a figure of light touching him, and a cake baken on
    the coals and a cruse of water at his head."""
    b = h * 0.86
    o = [mk.defs(p, *ALL), sky(w, h, "#E8B880" if not angel else "#2A2A5A", "#F3D8A0" if not angel else "#8A7AA8"), ground(w, h, h * 0.62, "#C8A070" if not angel else "#6A5A6A", dy=0)]
    r = random.Random(seed)
    o.append(f'<path d="M{f(w * 0.3)} {f(b)} C {f(w * 0.28)} {f(h * 0.6)} {f(w * 0.34)} {f(h * 0.44)} {f(w * 0.3)} {f(h * 0.34)}" stroke="#5A3A22" stroke-width="8" fill="none"></path>'
             + "".join(f'<path d="M{f(w * 0.3)} {f(h * 0.4)} L {f(w * 0.3 + math.cos(a) * w * 0.18)} {f(h * 0.4 + math.sin(a) * h * 0.18)}" stroke="#5A6A3A" stroke-width="3"></path>' for a in [-2.6 + i * 0.35 for i in range(8)]))
    o.append(J1.rug_sleeper(w * 0.48, b, min(1.2, h / 280), color="#5A3A1E"))
    if angel:
        o.append(V.rays(w * 0.76, h * 0.5, 20, 12, w * 0.3, color="#FFF4C2", op=0.4))
        o.append(f'<path d="M{f(w * 0.76)} {f(h * 0.2)} C {f(w * 0.68)} {f(h * 0.4)} {f(w * 0.66)} {f(h * 0.7)} {f(w * 0.68)} {f(b)} L {f(w * 0.84)} {f(b)} C {f(w * 0.86)} {f(h * 0.7)} {f(w * 0.84)} {f(h * 0.4)} {f(w * 0.76)} {f(h * 0.2)} Z" fill="#FFF4C2" opacity="0.85"></path>')
        o.append(f'<ellipse cx="{f(w * 0.36)}" cy="{f(b - 6)}" rx="16" ry="7" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
                 f'<path d="M{f(w * 0.42)} {f(b)} C {f(w * 0.41)} {f(b - 20)} {f(w * 0.45)} {f(b - 20)} {f(w * 0.44)} {f(b)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return "".join(o)

def horeb_cave(p, w, h, seed, stage="cave"):
    """Horeb the mount of God: the cave mouth; stage 'wind' (rocks broken in pieces), 'quake' (the mountain split), 'fire',
    'still' (Elijah in the entrance of the cave, his face wrapped in his mantle). Jehovah is never drawn."""
    r = random.Random(seed)
    o = [sky(w, h, "#2A2A4A" if stage != "still" else "#5A5A7A", "#5A4A6A" if stage != "still" else "#C8C0D0"), A.horeb(w, h, h * 0.96, seed)]
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.96)} C {f(w * 0.3)} {f(h * 0.6)} {f(w * 0.5)} {f(h * 0.56)} {f(w * 0.52)} {f(h * 0.96)} Z" fill="#12090A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    if stage == "wind":
        for i in range(10):
            y = h * r.uniform(0.1, 0.6)
            o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 20)} {f(w * 0.6)} {f(y + 20)} {f(w + 10)} {f(y)}" stroke="#C8C8E8" stroke-width="2" fill="none" opacity="0.6"></path>')
        for i in range(8):
            o.append(f'<path d="M{f(w * r.uniform(0.5, 1))} {f(h * r.uniform(0.2, 0.6))} l 14 -6 l 6 12 l -12 8 Z" fill="#6A5A5A" stroke="#0D0D0F" stroke-width="1.4"></path>')
    elif stage == "quake":
        o.append(f'<path d="M{f(w * 0.7)} {f(h * 0.2)} l -20 60 l 26 30 l -30 80 l 20 50 l -16 70" stroke="#0D0D0F" stroke-width="6" fill="none"></path>')
        o.append(mk.speed(w * 0.5, h * 0.5, 16, w * 0.3, w * 0.7, seed, color="#C8C0D0", op=0.4))
    elif stage == "fire":
        o += [E.blaze(w * (0.2 + i * 0.2), h * 0.9, w * 0.16, h * 0.4, seed + i, n=6) for i in range(4)]
    elif stage == "still":
        o.append(elijah_fig(p, w * 0.42, h * 0.95, fit(h * 0.95, h * 0.56) * 0.9, up=[(-22, -158), (-10, -180), (4, -186)]))
    return "".join(o)

def plowing(p, w, h, seed, mantle=False):
    """Elisha plowing with twelve yoke of oxen before him, he with the twelfth; mantle=True: Elijah casting his mantle upon him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#E8F6FA"), hills(w, h, h * 0.4, seed, color="#7A9A5A", amp=12), ground(w, h, h * 0.5, "#8A6A4A", dy=0)]
    for k in range(4):
        y = h * (0.56 + k * 0.08)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#6A4A2A" stroke-width="2"></path>')
    for i in range(3):
        o.append(S1.cow(w * (0.12 + i * 0.22), h * (0.6 + i * 0.03), min(0.5, h / 700), color=["#8A5A30", "#C9A27A", "#6A4A2A"][i]))
    s = fit(b, h * 0.36)
    o.append(S1.cow(w * 0.52, b, min(0.9, h / 400), color="#8A5A30"))
    o.append(man(p, w * 0.82, b, s, "#8A6A3A", flip=True, extra=A.headcloth("#8A6A3A")))
    if mantle:
        o.append(elijah_fig(p, w * 0.96, b, s, flip=True, up=[(22, -158), (0, -200), (-30, -220)]))
    return "".join(o)

def pavilions(p, w, h, seed):
    """Ben-hadad and the thirty and two kings drinking in their pavilions before Samaria besieged."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#F3D8A0"), samaria_hill(p, w, h, seed), N.camp(14, -10, w + 10, h * 0.7, h * 0.94, seed, color=("#7A1A2A", "#5A3A6A", "#8A6A3A"))]
    return "".join(o)

def two_flocks(w, h):
    """At Aphek: Israel encamped like two little flocks of kids, and the Syrians filling the country — a technical map."""
    o = [grid_bg(w, h)]
    for x in (0.16, 0.3):
        o.append(f'<circle cx="{f(w * x)}" cy="{f(h * 0.5)}" r="{f(min(w, h) * 0.06)}" fill="#FFD23F" fill-opacity="0.3" stroke="#FFD23F" stroke-width="2"></circle>')
    o.append(label(w * 0.23, h * 0.72, "ISRAEL · TWO LITTLE FLOCKS", "#FFD23F", 9))
    o.append(f'<rect x="{f(w * 0.48)}" y="{f(h * 0.12)}" width="{f(w * 0.48)}" height="{f(h * 0.76)}" fill="#D7261E" fill-opacity="0.25" stroke="#D7261E" stroke-width="2"></rect>'
             + label(w * 0.72, h * 0.5, "SYRIA FILLED THE COUNTRY", "#D7261E", 10) + node(w * 0.86, h * 0.2, "APHEK", "#8FD0E2", r=5, dy=-10, size=9))
    return "".join(o)

def ropes(p, w, h, seed):
    """Ben-hadad's servants with sackcloth on their loins and ropes on their heads, before the king of Israel in his chariot."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#E8C8A0"), ground(w, h, h * 0.6, "#A89A6A", dy=0)]
    s = fit(b, h * 0.38)
    for i in range(3):
        x = w * (0.16 + i * 0.12)
        o.append(E.kneel(x, b, s * 0.8, color="#8A7A5A", skin="#B98A6E", flip=True) + f'<ellipse cx="{f(x + 4)}" cy="{f(b - 112 * s * 0.8)}" rx="{f(14 * s)}" ry="{f(5 * s)}" fill="none" stroke="#C8A060" stroke-width="3"></ellipse>')
    o.append(E3.chariot(w * 0.76, b, min(0.9, h / 360), flip=True, color="#3A2214", driver=AHAB_C))
    return "".join(o)

def headband(p, w, h, seed):
    """The prophet waiting for the king by the way, disguised with his headband over his eyes."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#E8C8A0", "#F3D8A0"), hills(w, h, h * 0.5, seed, color="#9A8A6A", amp=12), ground(w, h, h * 0.6, "#B89A6A", dy=0)]
    s = fit(b, h * 0.4)
    o.append(prophet_fig(p, w * 0.3, b, s, cloth="#6A645E", beard=A.BLACK_BEARD) + f'<rect x="{f(w * 0.3 - 16 * s)}" y="{f(b - 196 * s)}" width="{f(32 * s)}" height="{f(8 * s)}" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    o.append(E3.chariot(w * 0.72, b, min(0.9, h / 360), flip=True, color="#3A2214", driver=AHAB_C))
    return "".join(o)
