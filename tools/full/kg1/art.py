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

def altar_horns(p, w, h, seed):
    """Adonijah laid hold on the horns of the altar before the Tent."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#3A2A4A", "#C88A6A"), E4.tent(w * 0.76, b, w * 0.4, h * 0.6, color="#E8E2D6", stripe="#8A6A3A"), ground(w, h, b, "#7A6A5A", dy=0),
         horned_altar(w * 0.4, b, min(1.3, h / 260))]
    o.append(E.kneel(w * 0.22, b, fit(b, h * 0.4) * 0.8, color="#B5652E", skin="#E3B08A"))
    return "".join(o)
