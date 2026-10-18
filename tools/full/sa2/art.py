"""Drawings for the 2 Samuel volume (chapter by chapter, added below). The Joshua, Judges and 1 Samuel drawings are reused
where they fit (jos.art, jdg.art, sa1.art); the digest's panels come in through sa2.common.D.

David as king at a distance: purple tunic and a small gold crown (king_fig). Joab: rust headcloth and tunic. Abner: olive.
Ish-bosheth: Saul's crimson with a crown."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, numbers1 as N, joshua1 as J, samuel1 as S1, samuel2 as S2, samuel3 as S3, samuel4 as S4
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg, node, route
from exo import art as A
from num.art import ALL, TRIBE_C
from jos.art import crowd_at, below, night, WAR, warrior

def f(v): return f"{v:.1f}"
DAVID_C, JOAB_C, ABNER_C, SAUL_C = "#4A2A7A", "#8A3A1E", "#5A5A2A", "#8A1E2E"
CROWN = '<path d="M-14 -200 L -14 -214 L -7 -206 L 0 -218 L 7 -206 L 14 -214 L 14 -200 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>'

def king_fig(p, x, y, s, flip=False, up=None, cloth=DAVID_C):
    """David as king at a distance: purple tunic, auburn beard, a small gold crown."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#5A2A16", cloth=cloth, kind="Tunic", sw=3, flip=flip, up=up, extra=S3.KING)

def captain(p, x, y, s, cloth=JOAB_C, flip=False, up=None, spear=True):
    """A captain at a distance (Joab, Abner, Abishai): tunic, headcloth and a spear."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind="Tunic", sw=3, flip=flip, up=up,
                     extra=A.headcloth(cloth) + A.BLACK_BEARD + (E4.SPEAR if spear else ""))

def sky(w, h, top, bot):
    return (f'<defs><linearGradient id="sk{int(w)}{int(h)}{top[1:]}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"></stop>'
            f'<stop offset="1" stop-color="{bot}"></stop></linearGradient></defs><rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#sk{int(w)}{int(h)}{top[1:]})"></rect>')

# ---- 2 Samuel 1–2 -------------------------------------------------------------------------------------------------------
def tidings(p, w, h, seed):
    """At Ziklag on the third day: a man out of the camp, his clothes rent and earth upon his head, fallen to the earth
    before David."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#E8B880", "#C86A3A"), sun(w * 0.18, h * 0.22, 18, color="#FFE680", op=0.4),
         J.city_hill(w * 0.74, h * 0.62, w * 0.34, h * 0.32, seed), ground(w, h, h * 0.62, "#8A6A4A", dy=0)]
    for i in range(4):
        o.append(f'<path d="M{f(w * (0.62 + i * 0.07))} {f(h * 0.4)} C {f(w * (0.6 + i * 0.07))} {f(h * 0.26)} {f(w * (0.66 + i * 0.07))} {f(h * 0.18)} {f(w * (0.63 + i * 0.07))} {f(h * 0.06)}" '
                 f'stroke="#5A4A4A" stroke-width="8" fill="none" opacity="0.4"></path>')
    s = fit(b, h * 0.36)
    o.append(S2.david(p, w * 0.3, b, s, staff=False, bag=False))
    o.append(E.kneel(w * 0.56, b, s * 0.9, color="#8A6A4A", skin="#9A6A4A", flip=True))
    o.append(f'<path d="M{f(w * 0.53)} {f(b - 96 * s)} l 6 -6 l 6 4 l 6 -7" stroke="#5A4A3A" stroke-width="3" fill="none"></path>')
    return "".join(o)

def crown_bracelet(w, h, seed):
    """The crown that was upon his head and the bracelet that was on his arm, laid down before David."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A1A2A"></rect>', V.rays(w * 0.5, h * 0.62, 30, 14, max(w, h), color="#E8B830", op=0.12),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.78)}" rx="{f(w * 0.36)}" ry="{f(h * 0.08)}" fill="#5A2A1E" stroke="#0D0D0F" stroke-width="2"></ellipse>']
    s = min(w, h) / 160
    o.append(S2.crown(w * 0.42, h * 0.76, s, rot=-8))
    cx, cy = w * 0.66, h * 0.76
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(22 * s)}" ry="{f(9 * s)}" fill="none" stroke="#0D0D0F" stroke-width="{f(6 * s + 3)}"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(22 * s)}" ry="{f(9 * s)}" fill="none" stroke="#E8B830" stroke-width="{f(6 * s)}"></ellipse>')
    return "".join(o)

def gilboa_dusk(w, h, seed):
    """Ye mountains of Gilboa: the mountains at dusk, with no dew nor rain, a shield cast away on the slope."""
    o = [sky(w, h, "#2A1A3A", "#C8603A"), sun(w * 0.7, h * 0.6, 26, color="#FF8A3D", op=0.5), S2.gilboa(w, h * 0.92, h * 0.5, seed)]
    o.append(f'<g transform="translate({f(w * 0.3)} {f(h * 0.84)}) rotate(-18)"><ellipse cx="0" cy="0" rx="{f(h * 0.08)}" ry="{f(h * 0.06)}" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
             f'<circle cx="0" cy="0" r="{f(h * 0.015)}" fill="#C8A06A" stroke="#0D0D0F" stroke-width="1.6"></circle></g>')
    return "".join(o)

def hebron_anointed(p, w, h, seed):
    """The men of Judah at Hebron anointing David king over the house of Judah."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE680", "#FFB04A"), V.rays(w * 0.5, h * 0.4, 30, 20, max(w, h), color="#FFF4C2", op=0.25),
         J.city_hill(w * 0.8, h * 0.6, w * 0.3, h * 0.3, seed), ground(w, h, h * 0.62, "#C8A06A", dy=0)]
    s = fit(b, h * 0.42)
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.28, h * 0.66, h * 0.8, 7, s * 0.4, s * 0.6))
    o.append(crowd_at(p, w, h, seed + 1, w * 0.76, w * 0.98, h * 0.66, h * 0.8, 7, s * 0.4, s * 0.6, flip=True))
    o.append(S2.david(p, w * 0.48, b, s, staff=False, bag=False))
    o.append(mk.person(p, round(w * 0.6), round(b), round(s, 3), body=SKIN, cloth="#6A5A3A", sw=3, flip=True, up=[(22, -158), (0, -190), (-24, -206)], extra=A.headcloth("#6A5A3A") + A.WHITE_BEARD)
             + S1.vial(w * 0.6 - 24 * s, b - 214 * s, s * 0.8, rot=150, pour=60 * s))
    return "".join(o)

def messengers(p, w, h, seed):
    """Messengers sent from Hebron over the hills toward Jabesh-gilead beyond the Jordan."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#E8F6FA"), hills(w, h, h * 0.4, seed, color="#6A7A5A", amp=16),
         f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.48)} {f(w * 0.6)} {f(h * 0.54)} {f(w + 10)} {f(h * 0.5)}" fill="none" stroke="#2C9DB8" stroke-width="6"></path>',
         ground(w, h, h * 0.56, "#B89A6A", dy=0)]
    s = fit(b, h * 0.34)
    o.append(S4.runner(p, w * 0.42, b, s, cloth="#E8E2D6") + S4.runner(p, w * 0.66, b - h * 0.08, s * 0.82, cloth="#C8B89A"))
    return "".join(o)

def mahanaim(p, w, h, seed):
    """Abner bringing Ish-bosheth the son of Saul over to Mahanaim and making him king."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A5A", "#C88A6A"), J.city_hill(w * 0.62, h * 0.58, w * 0.4, h * 0.38, seed), ground(w, h, h * 0.6, "#6A5A4A", dy=0)]
    s = fit(b, h * 0.38)
    o.append(mk.person(p, round(w * 0.36), round(b), round(s * 1.04, 3), body=SKIN, cloth=SAUL_C, kind="Tunic", sw=3, extra=A.headcloth(SAUL_C) + A.BLACK_BEARD + CROWN))
    o.append(captain(p, w * 0.2, b, s, cloth=ABNER_C))
    o.append(crowd_at(p, w, h, seed, w * 0.56, w * 0.98, h * 0.7, b, 8, s * 0.5, s * 0.8, flip=True))
    return "".join(o)

def pool(p, w, h, seed, men=True):
    """The pool of Gibeon, Abner's men on the one side and Joab's on the other; or (men=False) the field of sharp edges
    afterwards: swords lying in the grass by the pool, no one drawn."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2" if men else "#5A3A4A", "#E8F6FA" if men else "#C8603A"),
         J.city_hill(w * 0.5, h * 0.36, w * 0.34, h * 0.22, seed), ground(w, h, h * 0.38, "#B89A6A" if men else "#6A5A3A", dy=0),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.66)}" rx="{f(w * 0.2)}" ry="{f(h * 0.12)}" fill="#0F4C68" stroke="#0D0D0F" stroke-width="3"></ellipse>'
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.64)}" rx="{f(w * 0.16)}" ry="{f(h * 0.07)}" fill="#1F6F9A" opacity="0.7"></ellipse>']
    if men:
        s = fit(h * 0.86, h * 0.3)
        for i in range(6):
            o.append(warrior(p, w * (0.05 + i * 0.045), h * (0.72 + (i % 2) * 0.1), s * 0.8, ABNER_C if i % 2 else "#3A3A2A"))
            o.append(warrior(p, w * (0.95 - i * 0.045), h * (0.72 + (i % 2) * 0.1), s * 0.8, JOAB_C if i % 2 else "#5A2A16"))
    else:
        for i in range(12):
            x = r.uniform(w * 0.06, w * 0.94); y = r.uniform(h * 0.82, h * 0.96)
            if abs(x - w * 0.5) < w * 0.22 and y < h * 0.8: continue
            a = r.uniform(-30, 30)
            o.append(f'<g transform="translate({f(x)} {f(y)}) rotate({f(a)})"><path d="M-30 0 L 22 0" stroke="#C8C2D6" stroke-width="4"></path>'
                     f'<path d="M-30 0 L -40 0 M-30 -6 L -30 6" stroke="#3E2416" stroke-width="5"></path></g>')
    return "".join(o)

def pursuit(p, w, h, seed):
    """Asahel, light of foot as a wild roe, running after Abner across the open land."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#F3D8A0", "#E8B880"), hills(w, h, h * 0.5, seed, color="#A88A5A", amp=12), ground(w, h, h * 0.6, "#C8A06A", dy=0)]
    s = fit(b, h * 0.36)
    o.append(captain(p, w * 0.78, b - h * 0.1, s * 0.7, cloth=ABNER_C, flip=True))
    o.append(S4.runner(p, w * 0.36, b, s, cloth="#6A8A4A"))
    return "".join(o)

def spear_road(w, h, seed):
    """The place where Asahel fell down and died: a spear standing in the ground by the empty way, the sun going down."""
    o = [sky(w, h, "#3A1A2A", "#E8703A"), sun(w * 0.3, h * 0.6, 24, color="#FF8A3D", op=0.5), hills(w, h, h * 0.62, seed, color="#3A2A2A", amp=10), ground(w, h, h * 0.7, "#2A1E1E", dy=0),
         f'<path d="M{f(w * 0.2)} {f(h + 10)} C {f(w * 0.4)} {f(h * 0.82)} {f(w * 0.5)} {f(h * 0.74)} {f(w * 0.56)} {f(h * 0.7)}" stroke="#4A3A30" stroke-width="{f(w * 0.05)}" fill="none"></path>',
         f'<path d="M{f(w * 0.66)} {f(h * 0.92)} L {f(w * 0.7)} {f(h * 0.3)}" stroke="#0D0D0F" stroke-width="7"></path>'
         f'<path d="M{f(w * 0.7)} {f(h * 0.3)} L {f(w * 0.695)} {f(h * 0.22)} L {f(w * 0.715)} {f(h * 0.3)} Z" fill="#0D0D0F"></path>']
    return "".join(o)

def hill_ammah(p, w, h, seed, trumpet=False):
    """The children of Benjamin as one band on the top of a hill at sunset; Joab below (trumpet=True: blowing the trumpet)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A", "#E8803A"), sun(w * 0.5, h * 0.5, 26, color="#FFB04A", op=0.5),
         f'<path d="M{f(w * 0.34)} {f(h * 0.62)} C {f(w * 0.5)} {f(h * 0.3)} {f(w * 0.7)} {f(h * 0.3)} {f(w * 0.96)} {f(h * 0.62)} Z" fill="#2A1E2A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.62, "#3A2A2A", dy=0)]
    for i in range(9):
        x = w * (0.5 + i * 0.03); y = h * 0.38 + abs(i - 4) * h * 0.012
        o.append(mk.person(p, round(x), round(y), round(fit(y, y - h * 0.1), 3), body="#0B0814", cloth="#1A1220", kind="Tunic", sw=2, extra=E4.SPEAR))
    s = fit(b, h * 0.36)
    if trumpet: o.append(J.trumpeter(p, w * 0.18, b, s, body="#3A1E14") + J.blasts(w * 0.18 + 70 * s, b - 170 * s, s))
    else: o.append(captain(p, w * 0.2, b, s))
    o.append(captain(p, w * 0.08, b, s * 0.9, cloth="#3A3A5A"))
    return "".join(o)

def dawn_hebron(p, w, h, seed):
    """Joab and his men went all night, and the day brake upon them at Hebron."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A5A", "#FFB04A"), sun(w * 0.8, h * 0.62, 30, color="#FFE680", op=0.6), J.city_hill(w * 0.76, h * 0.64, w * 0.3, h * 0.3, seed),
         ground(w, h, h * 0.64, "#3A2A2A", dy=0)]
    for i in range(10):
        t = i / 9; x = w * (0.06 + 0.5 * t); y = b - t * h * 0.2
        o.append(mk.person(p, round(x), round(y), round(fit(y, y - h * (0.3 - 0.12 * t)), 3), body="#0B0814", cloth="#2A2030", kind="Tunic", sw=2, extra=E4.SPEAR))
    return "".join(o)

# ---- 2 Samuel 3–4 -------------------------------------------------------------------------------------------------------
import ruth1 as R1
SONS = [("AMNON", "AHINOAM"), ("CHILEAB", "ABIGAIL"), ("ABSALOM", "MAACAH"), ("ADONIJAH", "HAGGITH"), ("SHEPHATIAH", "ABITAL"), ("ITHREAM", "EGLAH")]
def sons_hebron(w, h, names=None, hi="ABSALOM"):
    """Sons born to David, as a strip (or two) of nodes, each with his mother's name when known."""
    names = names or SONS
    o = [grid_bg(w, h, color="#3A2A5A", bg="#1A1430")]
    rows = [names[:6], names[6:]] if len(names) > 6 else [names]
    for k, row in enumerate(rows):
        y = h * (0.62 if len(rows) == 1 else 0.42 + k * 0.32)
        o.append(f'<path d="M{f(w * 0.08)} {f(y)} L {f(w * 0.92)} {f(y)}" stroke="#FFD23F" stroke-width="2" stroke-dasharray="6 5"></path>')
        for i, (son, mother) in enumerate(row):
            x = w * (0.1 + i * 0.16)
            o.append(node(x, y, son, "#D7261E" if son == hi else "#FFD23F", r=7, dy=-16, size=10) + (label(x, y + 26, "OF " + mother, "#B8B0D8", 8) if mother else ""))
    return "".join(o)

def taken_away(p, w, h, seed):
    """Michal taken from Paltiel: she goes on the road with Abner's men, her husband weeping behind as far as Bahurim."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8A9AB8", "#E8D8C8"), hills(w, h, h * 0.5, seed, color="#7A7A6A", amp=14), ground(w, h, h * 0.6, "#A8906A", dy=0)]
    s = fit(b, h * 0.36)
    o.append(captain(p, w * 0.78, b - h * 0.06, s * 0.8, cloth=ABNER_C, flip=True) + captain(p, w * 0.88, b - h * 0.04, s * 0.84, cloth="#3A3A2A", flip=True))
    o.append(mk.person(p, round(w * 0.64), round(b), round(s * 0.92, 3), body=SKIN, cloth="#8A1E2E", woman=True, hair="#1A1210", sw=3, flip=True))
    o.append(E.kneel(w * 0.3, b, s * 0.85, color="#5A5A6A", skin="#9A6A4A", flip=True))
    return "".join(o)

def feast_hebron(p, w, h, seed):
    """David made Abner and the twenty men with him a feast in Hebron: the table set, lamps, the guests."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A2A1E"></rect>', S3.cedar(w, h, h * 0.8)]
    s = fit(b, h * 0.4)
    o.append(king_fig(p, w * 0.14, b, s))
    o.append(captain(p, w * 0.86, b, s, cloth=ABNER_C, flip=True, spear=False))
    for i in range(5):
        o.append(man(p, w * (0.6 + i * 0.05), b - h * 0.04, s * 0.7, r_c(i), flip=True))
    o.append(S3.table(w * 0.46, b, w * 0.42, min(1.2, h / 300)))
    return "".join(o)

def r_c(i): return ["#5A5A2A", "#6A4A2A", "#3A4A5A", "#5A3A2A", "#4A4A3A"][i % 5]

def gate_dusk(w, h, seed, people=False):
    """The gate of Hebron at dusk, its passage dark and empty (Abner's death is told in words only)."""
    o = [sky(w, h, "#3A1A2A", "#C8603A"), sun(w * 0.86, h * 0.7, 22, color="#FF8A3D", op=0.4), ground(w, h, h * 0.86, "#3A2A2A", dy=0),
         S4.gatehouse(w * 0.5, h * 0.88, min(w * 0.5, h * 0.9), h * 0.66)]
    return "".join(o)

def bier(p, w, h, seed):
    """Abner's bier carried to the grave at Hebron, king David following it, the people with rent clothes and sackcloth."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#5A5A7A", "#C8B8A8"), J.city_hill(w * 0.82, h * 0.56, w * 0.3, h * 0.3, seed), ground(w, h, h * 0.58, "#7A6A5A", dy=0)]
    s = fit(b, h * 0.32)
    xs = [w * 0.46, w * 0.62]
    for x in xs:
        o.append(mk.person(p, round(x - 20 * s), round(b), round(s, 3), body="#2A140C", cloth="#3A3430", kind="Tunic", sw=3, flip=True)
                 + mk.person(p, round(x + 20 * s), round(b), round(s, 3), body="#2A140C", cloth="#4A4038", kind="Tunic", sw=3, flip=True))
    o.append(f'<rect x="{f(xs[0] - 40 * s)}" y="{f(b - 150 * s)}" width="{f(xs[1] - xs[0] + 80 * s)}" height="{f(22 * s)}" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    o.append(king_fig(p, w * 0.24, b, s * 1.02, flip=True))
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.16, h * 0.66, b - 10, 6, s * 0.5, s * 0.8, flip=True))
    return "".join(o)

def nurse_flee(p, w, h, seed):
    """His nurse took him up and fled when the tidings came out of Jezreel: a woman running with a child of five."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#C8703A", "#F3D8A0"), hills(w, h, h * 0.5, seed, color="#8A6A5A", amp=16), ground(w, h, h * 0.6, "#B89A6A", dy=0)]
    s = fit(b, h * 0.4)
    o.append(mk.person(p, round(w * 0.46), round(b), round(s, 3), body="#3A1E14", cloth="#4A5A7A", woman=True, hair="#1A1210", sw=3, flip=True, up=R1.HOLD_BABY,
                       extra=f'<g transform="translate(10 -134)"><ellipse cx="0" cy="0" rx="14" ry="22" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="2"></ellipse><circle cx="0" cy="-26" r="10" fill="#D9A27A" stroke="#0D0D0F" stroke-width="2"></circle></g>')
             + mk.speed(w * 0.46 + 60 * s, b - 90 * s, 10, 20 * s, 120 * s, seed, color="#F3EFE6", op=0.6))
    return "".join(o)

def house_noon(w, h, seed):
    """The house of Ish-bosheth in the heat of the day: a blazing sun, the doorway dark, sacks of wheat by the wall."""
    o = [sky(w, h, "#FFF4C2", "#FFC14D"), V.rays(w * 0.8, h * 0.1, 30, 20, max(w, h) * 1.2, color="#FFFFFF", op=0.3), sun(w * 0.8, h * 0.1, 30, color="#FFF4C2", op=0.8),
         ground(w, h, h * 0.86, "#C8A06A", dy=0),
         f'<rect x="{f(w * 0.12)}" y="{f(h * 0.3)}" width="{f(w * 0.6)}" height="{f(h * 0.56)}" fill="#D8B88A" stroke="#0D0D0F" stroke-width="2.6"></rect>'
         f'<rect x="{f(w * 0.08)}" y="{f(h * 0.26)}" width="{f(w * 0.68)}" height="{f(h * 0.05)}" fill="#A8885A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
         f'<path d="M{f(w * 0.34)} {f(h * 0.86)} L {f(w * 0.34)} {f(h * 0.54)} C {f(w * 0.34)} {f(h * 0.44)} {f(w * 0.5)} {f(h * 0.44)} {f(w * 0.5)} {f(h * 0.54)} L {f(w * 0.5)} {f(h * 0.86)} Z" fill="#12090A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i in range(3):
        x = w * (0.58 + i * 0.07)
        o.append(f'<path d="M{f(x - 18)} {f(h * 0.86)} C {f(x - 24)} {f(h * 0.74)} {f(x - 14)} {f(h * 0.7)} {f(x)} {f(h * 0.7)} C {f(x + 14)} {f(h * 0.7)} {f(x + 24)} {f(h * 0.74)} {f(x + 18)} {f(h * 0.86)} Z" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def pool_dusk(w, h, seed):
    """The pool in Hebron at dusk, nothing beside it but the reeds (4:12 told in words only)."""
    o = [sky(w, h, "#2A1A3A", "#C86A4A"), J.city_hill(w * 0.5, h * 0.42, w * 0.4, h * 0.26, seed), ground(w, h, h * 0.44, "#4A3A3A", dy=0),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.7)}" rx="{f(w * 0.26)}" ry="{f(h * 0.13)}" fill="#0F3A5A" stroke="#0D0D0F" stroke-width="3"></ellipse>'
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.68)}" rx="{f(w * 0.2)}" ry="{f(h * 0.06)}" fill="#C86A4A" opacity="0.3"></ellipse>']
    return "".join(o)

# ---- 2 Samuel 5–6 -------------------------------------------------------------------------------------------------------
SONS_J = [(n, None) for n in ("SHAMMUA", "SHOBAB", "NATHAN", "SOLOMON", "IBHAR", "ELISHUA", "NEPHEG", "JAPHIA", "ELISHAMA", "ELIADA", "ELIPHELET")]

def jebus(p, w, h, seed):
    """Jerusalem of the Jebusites on its height, the stronghold of Zion above the valleys; David's men below."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.86, h * 0.16, 18, color="#FFE680", op=0.4),
         f'<path d="M{f(w * 0.2)} {f(h * 0.8)} C {f(w * 0.36)} {f(h * 0.4)} {f(w * 0.8)} {f(h * 0.36)} {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.2)} {f(h + 10)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.6"></path>',
         J.jericho(w * 0.42, w * 0.96, h * 0.24, h * 0.46, seed, towers=3, houses=True), ground(w, h, h * 0.86, "#B89A6A", dy=0)]
    s = fit(b, h * 0.62)
    for i in range(6):
        o.append(warrior(p, w * (0.04 + i * 0.04), b - (i % 2) * h * 0.03, s * 0.9, WAR[i % 4]))
    o.append(king_fig(p, w * 0.32, b, s))
    return "".join(o)

def breach(w, h, seed):
    """Jehovah hath broken mine enemies before me, like the breach of waters: a flood bursting through the hills."""
    r = random.Random(seed)
    o = [sky(w, h, "#2A3A5A", "#8FD0E2"), f'<path d="M-10 {f(h * 0.3)} L {f(w * 0.36)} {f(h * 0.36)} L {f(w * 0.42)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w + 10)} {f(h * 0.28)} L {f(w * 0.64)} {f(h * 0.34)} L {f(w * 0.58)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.36)} {f(h * 0.36)} C {f(w * 0.44)} {f(h * 0.5)} {f(w * 0.56)} {f(h * 0.5)} {f(w * 0.64)} {f(h * 0.34)} L {f(w * 0.58)} {f(h + 10)} L {f(w * 0.42)} {f(h + 10)} Z" fill="#1F6F9A" stroke="#0D0D0F" stroke-width="2"></path>']
    for i in range(14):
        x = w * r.uniform(0.38, 0.62); y = h * r.uniform(0.4, 1.0)
        o.append(f'<path d="M{f(x - 14)} {f(y)} C {f(x - 6)} {f(y - 10)} {f(x + 6)} {f(y - 10)} {f(x + 14)} {f(y)}" stroke="#E8F6FA" stroke-width="3" fill="none"></path>')
    for i in range(6):
        x = w * r.uniform(0.3, 0.7); y = h * r.uniform(0.3, 0.42)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(6, 14))}" fill="#E8F6FA" opacity="0.8"></circle>')
    return "".join(o)

def mulberry(p, w, h, seed):
    """The sound of marching in the tops of the mulberry-trees: a row of trees bowed by a wind, David's men waiting behind them."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), night(w, h, seed, "#14123A"), ground(w, h, h * 0.84, "#1A1A2A", dy=0)]
    for i in range(6):
        x = w * (0.08 + i * 0.17); base = h * 0.86; tilt = 18
        o.append(f'<path d="M{f(x)} {f(base)} C {f(x + 4)} {f(h * 0.6)} {f(x + tilt * 0.5)} {f(h * 0.4)} {f(x + tilt)} {f(h * 0.34)}" stroke="#2A1A10" stroke-width="10" fill="none"></path>')
        for k in range(5):
            o.append(f'<ellipse cx="{f(x + tilt + r.uniform(-30, 40))}" cy="{f(h * r.uniform(0.18, 0.4))}" rx="{f(w * 0.06)}" ry="{f(h * 0.06)}" fill="{r.choice(["#1F4A34", "#2E6B3A", "#24503A"])}" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    for i in range(5):
        y = h * (0.1 + i * 0.07)
        o.append(f'<path d="M{f(w * 0.02)} {f(y)} C {f(w * 0.3)} {f(y - 10)} {f(w * 0.6)} {f(y + 10)} {f(w * 0.98)} {f(y)}" stroke="#B8C8E8" stroke-width="1.6" fill="none" opacity="0.5"></path>')
    for i in range(7):
        o.append(mk.person(p, round(w * (0.1 + i * 0.13)), round(h * 0.92), round(fit(h * 0.92, h * 0.68), 3), body="#0B0814", cloth="#1A1630", kind="Tunic", sw=2, extra=E4.SPEAR))
    return "".join(o)

def nacon(p, w, h, seed):
    """The threshing-floor of Nacon under a darkening sky: the new cart with the ark of God, the oxen stumbling."""
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A4A", "#8A6A5A"), ground(w, h, h * 0.7, "#8A6A4A", dy=0), S4.threshing_floor(w * 0.5, h * 0.86, w * 0.9),
         S1.team(w * 0.22, h * 0.86, min(1.2, h / 300), low=True)]
    o.append(f'<path d="M{f(w * 0.8)} -10 L {f(w * 0.74)} {f(h * 0.2)} L {f(w * 0.78)} {f(h * 0.22)} L {f(w * 0.7)} {f(h * 0.44)}" stroke="#FFF4C2" stroke-width="4" fill="none"></path>')
    return "".join(o)

def obed_edom(p, w, h, seed):
    """The house of Obed-edom the Gittite, the ark of God within, a soft light at its door; his household, the vines and
    sheaves of a blessed house."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE680", "#F3D8A0"), ground(w, h, h * 0.8, "#C8A06A", dy=0),
         f'<rect x="{f(w * 0.3)}" y="{f(h * 0.3)}" width="{f(w * 0.44)}" height="{f(h * 0.5)}" fill="#D8B88A" stroke="#0D0D0F" stroke-width="2.6"></rect>'
         f'<rect x="{f(w * 0.27)}" y="{f(h * 0.26)}" width="{f(w * 0.5)}" height="{f(h * 0.05)}" fill="#A8885A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
         f'<rect x="{f(w * 0.45)}" y="{f(h * 0.5)}" width="{f(w * 0.14)}" height="{f(h * 0.3)}" fill="#FFE680" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         V.rays(w * 0.52, h * 0.64, 20, 14, w * 0.3, color="#FFF4C2", op=0.4)]
    s = fit(b, h * 0.3)
    o.append(crowd_at(p, w, h, seed, w * 0.04, w * 0.26, h * 0.82, b, 4, s * 0.8, s))
    o.append(crowd_at(p, w, h, seed + 2, w * 0.78, w * 0.96, h * 0.82, b, 4, s * 0.8, s, flip=True))
    return "".join(o)

def tent_ark(p, w, h, seed):
    """The ark set in its place in the midst of the tent David pitched, the altar smoking, the people with their cakes."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#FFB04A", "#F3D8A0"), J.city_hill(w * 0.5, h * 0.5, w * 0.9, h * 0.24, seed), ground(w, h, h * 0.52, "#C8A06A", dy=0),
         E4.tent(w * 0.36, h * 0.8, w * 0.36, h * 0.34, color="#E8E2D6", stripe="#8A6A3A"),
         J.ark(w * 0.36, h * 0.8, min(0.5, h / 700), uid=p + "ak", pole=0), S4.altar(w * 0.72, h * 0.82, min(1.0, h / 360), seed=seed)]
    s = fit(b, h * 0.26)
    o.append(king_fig(p, w * 0.56, b, s, up=[(-22, -158), (-6, -196), (8, -228)]))
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.16, h * 0.84, b + 6, 4, s * 0.8, s))
    o.append(crowd_at(p, w, h, seed + 1, w * 0.86, w * 0.98, h * 0.84, b + 6, 4, s * 0.8, s, flip=True))
    return "".join(o)
