"""Drawings for the 1 Kings volume (chapter by chapter, added below). The 2 Samuel, 1 Samuel, Judges and Joshua drawings are
reused where they fit (sa2.art, sa1.art, jdg.art, jos.art).

Solomon at a distance: a deep-blue tunic and the gold crown (sol_fig). David old: purple (sa2.art.old_king). Bath-sheba:
a plum robe. Elijah: a brown hairy mantle with a leather girdle, bareheaded. Ahab: crimson with the crown. Jezebel: black
and gold."""
import sys, pathlib, random, math
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
    o = [mk.defs(p, *ALL), sky(w, h, "#E8C8A0", "#F3D8A0"), ground(w, h, h * 0.5, "#B89A6A", dy=0)]
    for k in range(3):
        y = h * (0.62 + k * 0.14)
        for i in range(7):
            o.append(E3.horse(w * (0.06 + i * 0.15 + (k % 2) * 0.06), y, 0.24 + k * 0.08, color=["#3A2214", "#6A4A2A", "#2A1A14"][i % 3]))
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
