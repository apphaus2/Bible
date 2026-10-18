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

# ---- 2 Samuel 7–8 -------------------------------------------------------------------------------------------------------
def nathan_night(w, h, seed):
    """The same night: Jerusalem's rooftops under the stars, one window lit in the prophet's house."""
    o = [night(w, h, seed, "#0F0E2A"), S3.roof(w, h, h * 0.56, seed), J.moon(w * 0.82, h * 0.18, 16)]
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(h * 0.46)}" width="16" height="20" fill="#FFE680" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             f'<circle cx="{f(w * 0.3 + 8)}" cy="{f(h * 0.46 + 10)}" r="40" fill="#FFE680" opacity="0.12"></circle>')
    return "".join(o)

def throne_glory(w, h, seed):
    """I will establish the throne of his kingdom for ever: an empty throne in light under the stars."""
    o = [night(w, h, seed, "#14123A"), V.rays(w * 0.5, h * 0.62, 40, 30, max(w, h), color="#FFD23F", op=0.18),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.92)}" rx="{f(w * 0.3)}" ry="{f(h * 0.05)}" fill="#2A2458" stroke="#FFD23F" stroke-width="1.6"></ellipse>',
         S3.throne(w * 0.5, h * 0.92, min(1.6, h / 260))]
    return "".join(o)

def prayer(p, w, h, seed):
    """David the king sitting before Jehovah in the tent of the ark, by lamplight."""
    from genesis.art4 import clay_lamp
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A1A2A"></rect>']
    for i in range(12):
        o.append(f'<rect x="{f(i * w / 11 - 10)}" y="-10" width="{f(w / 11 + 2)}" height="{f(b + 10)}" fill="{["#5A2A6A", "#2A3A7A", "#8A1E2E"][i % 3]}" opacity="0.85"></rect>')
    o.append(ground(w, h, b, "#2A1A14", dy=0))
    o.append(J.ark(w * 0.72, b, min(0.9, h / 360), uid=p + "ak", pole=0))
    o.append(E.kneel(w * 0.34, b, fit(b, h * 0.3) * 0.9, color="#4A2A7A", skin="#9A5A3A"))
    o.append(clay_lamp(w * 0.1, h * 0.7, min(1.2, h / 260)))
    return "".join(o)

WARS = [("JERUSALEM", 0.42, 0.56), ("GATH", 0.2, 0.6), ("MOAB", 0.6, 0.72), ("RABBAH OF AMMON", 0.64, 0.5), ("VALLEY OF SALT", 0.46, 0.9),
        ("AMALEK", 0.22, 0.88), ("DAMASCUS", 0.66, 0.24), ("ZOBAH", 0.76, 0.12), ("HAMATH", 0.64, 0.05)]
def wars_map(w, h, hi=()):
    """David's wars as a technical map: the Philistines, Moab, Zobah and Damascus to the River, Hamath, Ammon, Amalek, Edom."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.1)} -10 C {f(w * 0.12)} {f(h * 0.3)} {f(w * 0.08)} {f(h * 0.7)} {f(w * 0.04)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.3)} C {f(w * 0.52)} {f(h * 0.5)} {f(w * 0.5)} {f(h * 0.7)} {f(w * 0.52)} {f(h * 0.78)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>'
             f'<ellipse cx="{f(w * 0.52)}" cy="{f(h * 0.74)}" rx="{f(w * 0.015)}" ry="{f(h * 0.06)}" fill="#2C9DB8"></ellipse>')
    o.append(f'<path d="M{f(w * 0.86)} -10 C {f(w * 0.92)} {f(h * 0.1)} {f(w * 0.94)} {f(h * 0.2)} {f(w + 10)} {f(h * 0.3)}" stroke="#2C9DB8" stroke-width="4" fill="none"></path>'
             + label(w * 0.97, h * 0.34, "THE RIVER", "#8FD0E2", 8, "end"))
    jx, jy = w * 0.42, h * 0.56
    for nm, x, y in WARS[1:]:
        if nm in hi: o.append(route([(jx, jy), (w * x, h * y)], color="#D7261E"))
    for nm, x, y in WARS:
        c = "#D7261E" if nm in hi else ("#FFD23F" if nm == "JERUSALEM" else "#8FD0E2")
        o.append(node(w * x, h * y, nm, c, r=6 if nm in hi or nm == "JERUSALEM" else 4, dy=-12, size=9))
    return "".join(o)

def gold_shields(w, h, seed):
    """The shields of gold taken from the servants of Hadadezer, and the brass of Betah and Berothai, brought to Jerusalem."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2214"></rect>', S3.cedar(w, h, h * 0.86)]
    for i in range(6):
        x = w * (0.1 + i * 0.16); y = h * (0.36 + (i % 2) * 0.16); rr = min(w, h) * 0.09
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rr)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.6"></circle>'
                 f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rr * 0.6)}" fill="none" stroke="#A8721A" stroke-width="2"></circle><circle cx="{f(x)}" cy="{f(y)}" r="{f(rr * 0.16)}" fill="#FFF4C2" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    return "".join(o)

def vessels(w, h, seed):
    """Vessels of silver, vessels of gold and vessels of brass, dedicated unto Jehovah."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A3A"></rect>', V.rays(w * 0.5, h * 0.7, 30, 20, max(w, h), color="#FFD23F", op=0.12),
         ground(w, h, h * 0.84, "#1A1024", dy=0)]
    cols = ["#C8C8D0", "#E8B830", "#C8703A"]
    for i in range(7):
        x = w * (0.12 + i * 0.126); s = min(w, h) / 260 * (0.8 + 0.3 * (i % 2)); c = cols[i % 3]; y = h * 0.86
        o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-22 0 C -30 -30 -30 -54 -12 -64 L -10 -80 L 10 -80 L 12 -64 C 30 -54 30 -30 22 0 Z" fill="{c}" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<ellipse cx="0" cy="-80" rx="14" ry="4" fill="{c}" stroke="#0D0D0F" stroke-width="2"></ellipse><path d="M-20 -40 L 20 -40" stroke="#0D0D0F" stroke-width="1.4" opacity="0.5"></path></g>')
    return "".join(o)

def court(p, w, h, seed):
    """David reigning over all Israel: the king on his throne in the house of cedar, his officers standing before him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), S3.throne(w * 0.2, b, min(1.3, h / 260))]
    s = fit(b, h * 0.42)
    o.append(king_fig(p, w * 0.2, b - 40 * min(1.3, h / 260), s * 0.9))
    for i, c in enumerate([JOAB_C, "#3A4A6A", "#E8E2D6", "#E8E2D6", "#5A4A3A", "#2A4A3A"]):
        o.append(captain(p, w * (0.42 + i * 0.105), b, s * (0.72 if i % 2 else 0.68), cloth=c, flip=True, spear=i in (0, 5)))
    return "".join(o)

# ---- 2 Samuel 9–10 ------------------------------------------------------------------------------------------------------
import judges1 as J1
def jericho_wait(p, w, h, seed):
    """Tarry at Jericho until your beards be grown: the city of palm-trees, the king's servants sitting apart in the shade,
    their mantles drawn about them."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), J.city_hill(w * 0.76, h * 0.6, w * 0.34, h * 0.26, seed), ground(w, h, h * 0.62, "#C8A06A", dy=0)]
    for i, x in enumerate((0.12, 0.3, 0.54)):
        o.append(J1.palm(w * x, h * 0.86, min(1.2, h / 300) * (0.9 + 0.1 * i)))
    s = fit(b, h * 0.3)
    for i in range(4):
        o.append(E.kneel(w * (0.2 + i * 0.12), b - (i % 2) * h * 0.03, s * 0.8, color=["#5A5A6A", "#6A5A4A", "#4A4A5A", "#5A4A4A"][i], skin="#9A6A4A", flip=i % 2 == 1))
    return "".join(o)

def ammon_map(w, h, stage=0):
    """The battle before the gate of Rabbah as a technical map: Ammon in array at the gate, the hired Syrians in the field
    behind; Joab's choice men against the Syrians, Abishai against Ammon (stage 1); and the flight (stage 2)."""
    o = [grid_bg(w, h)]
    gx, gy = w * 0.82, h * 0.5
    o.append(f'<rect x="{f(gx)}" y="{f(h * 0.2)}" width="{f(w * 0.16)}" height="{f(h * 0.6)}" fill="#1E3A5A" stroke="#8FD0E2" stroke-width="2"></rect>' + label(gx + w * 0.08, h * 0.16, "RABBAH", "#8FD0E2", 9))
    def block(x, y, bw, bh, name, c):
        return (f'<rect x="{f(x - bw / 2)}" y="{f(y - bh / 2)}" width="{f(bw)}" height="{f(bh)}" fill="{c}" fill-opacity="0.25" stroke="{c}" stroke-width="2"></rect>'
                + label(x, y + 4, name, c, 8))
    if stage < 2:
        o.append(block(w * 0.7, gy, w * 0.12, h * 0.4, "AMMON", "#D7261E"))
        o.append(block(w * 0.16, gy, w * 0.2, h * 0.5, "SYRIA", "#D7261E"))
    if stage >= 1:
        o.append(block(w * 0.36, gy, w * 0.1, h * 0.3, "JOAB", "#FFD23F") + block(w * 0.52, gy, w * 0.1, h * 0.3, "ABISHAI", "#FFD23F"))
    if stage == 2:
        o.append(route([(w * 0.2, gy), (w * 0.04, gy)], color="#D7261E") + label(w * 0.12, gy - h * 0.12, "SYRIA FLED", "#D7261E", 8))
        o.append(route([(w * 0.7, gy), (w * 0.86, gy)], color="#D7261E") + label(w * 0.7, gy - h * 0.12, "AMMON INTO THE CITY", "#D7261E", 8))
    return "".join(o)

def audience(p, w, h, seed, cloth="#7A5A3A", n=1):
    """The king on his throne in the house of cedar, and one (or more) standing before him."""
    b = h * 0.92; k = min(1.3, h / 300)
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), S3.throne(w * 0.24, b, k)]
    s = fit(b, h * 0.36)
    o.append(king_fig(p, w * 0.24, b - 40 * k, s * 0.9))
    for i in range(n):
        o.append(captain(p, w * (0.7 + i * 0.12), b, s * 0.86, cloth=cloth, flip=True, spear=False))
    return "".join(o)

# ---- 2 Samuel 11–12 -----------------------------------------------------------------------------------------------------
def rabbah(p, w, h, seed, camp=True, dusk=False):
    """Rabbah of the children of Ammon, the city of waters, walled on its hill; Israel's tents about it (camp=False: the
    city alone at dusk)."""
    o = [mk.defs(p, *ALL), sky(w, h, "#3A1A2A" if dusk else "#8FD0E2", "#C8603A" if dusk else "#F3E8C8"),
         f'<path d="M{f(w * 0.1)} {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.36)} {f(w * 0.7)} {f(h * 0.34)} {f(w * 0.94)} {f(h * 0.7)} Z" fill="{"#3A2A2A" if dusk else "#8A6A4A"}" stroke="#0D0D0F" stroke-width="2.6"></path>',
         J.jericho(w * 0.28, w * 0.76, h * 0.22, h * 0.44, seed, towers=4, houses=True), ground(w, h, h * 0.68, "#2A1E1E" if dusk else "#B89A6A", dy=0),
         f'<path d="M-10 {f(h * 0.74)} C {f(w * 0.3)} {f(h * 0.72)} {f(w * 0.6)} {f(h * 0.78)} {f(w + 10)} {f(h * 0.74)}" stroke="#2C9DB8" stroke-width="6" fill="none"></path>']
    if camp: o.append(N.camp(16, -10, w + 10, h * 0.82, h * 0.98, seed))
    return "".join(o)

def uriah_door(p, w, h, seed):
    """Uriah asleep at the door of the king's house among the servants of his lord, by night."""
    o = [mk.defs(p, *ALL), night(w, h, seed, "#14123A"), f'<rect x="{f(w * 0.08)}" y="{f(h * 0.12)}" width="{f(w * 0.84)}" height="{f(h * 0.64)}" fill="#5A4A5A" stroke="#0D0D0F" stroke-width="2.6"></rect>',
         f'<path d="M{f(w * 0.42)} {f(h * 0.76)} L {f(w * 0.42)} {f(h * 0.4)} C {f(w * 0.42)} {f(h * 0.3)} {f(w * 0.58)} {f(h * 0.3)} {f(w * 0.58)} {f(h * 0.4)} L {f(w * 0.58)} {f(h * 0.76)} Z" fill="#2A1A14" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.76, "#2A2030", dy=0)]
    for i in range(6):
        o.append(J1.rug_sleeper(w * (0.1 + i * 0.16), h * (0.86 + (i % 2) * 0.04), min(0.8, h / 400), color="#8A2A2A" if i == 2 else "#3A3448"))
    return "".join(o)

def night_vigil(p, w, h, seed):
    """David lying all night upon the earth, the elders of his house standing beside him, a single lamp."""
    from genesis.art4 import clay_lamp
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1430"></rect>', ground(w, h, b, "#120E1E", dy=0),
         clay_lamp(w * 0.5, h * 0.62, min(1.2, h / 260)), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.58)}" r="{f(h * 0.4)}" fill="#FFC14D" opacity="0.08"></circle>']
    s = fit(b, h * 0.42)
    o.append(N.prostrate(w * 0.32, b, s * 0.9, color="#4A2A7A", skin="#9A5A3A"))
    for i in range(3):
        o.append(mk.person(p, round(w * (0.66 + i * 0.1)), round(b), round(s * 0.8, 3), body="#0B0814", cloth=["#3A3040", "#4A3A3A", "#2A3040"][i], sw=3, flip=True, extra=A.WHITE_BEARD))
    return "".join(o)

def crown_talent(w, h, seed):
    """The crown of the king of Ammon, a talent of gold set with precious stones."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A3A"></rect>', V.rays(w * 0.5, h * 0.6, 36, 20, max(w, h), color="#FFD23F", op=0.2),
         S2.crown(w * 0.5, h * 0.78, min(w, h) / 90)]
    return "".join(o)

# ---- 2 Samuel 13–14 -----------------------------------------------------------------------------------------------------
import judges2 as J2
def kitchen(w, h, seed):
    """Tamar's dough, the kneading-trough, the cakes and the pan by the fire in Amnon's house."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A2A1E"></rect>', ground(w, h, h * 0.76, "#2A1810", dy=0),
         E.blaze(w * 0.7, h * 0.9, w * 0.2, h * 0.24, seed, n=6),
         f'<ellipse cx="{f(w * 0.7)}" cy="{f(h * 0.66)}" rx="{f(w * 0.14)}" ry="{f(h * 0.03)}" fill="#3A3A42" stroke="#0D0D0F" stroke-width="2.4"></ellipse>',
         f'<path d="M{f(w * 0.12)} {f(h * 0.7)} L {f(w * 0.46)} {f(h * 0.7)} L {f(w * 0.42)} {f(h * 0.84)} L {f(w * 0.16)} {f(h * 0.84)} Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<ellipse cx="{f(w * 0.29)}" cy="{f(h * 0.7)}" rx="{f(w * 0.14)}" ry="{f(h * 0.04)}" fill="#F3E0B8" stroke="#0D0D0F" stroke-width="2"></ellipse>']
    for i in range(4):
        o.append(f'<ellipse cx="{f(w * (0.62 + i * 0.05))}" cy="{f(h * 0.64)}" rx="{f(w * 0.022)}" ry="{f(h * 0.012)}" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    return "".join(o)

def chamber(w, h, seed):
    """The door of Amnon's inner chamber, a lamp's light within; the cakes in the doorway."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A2E"></rect>',
         f'<rect x="{f(w * 0.36)}" y="{f(h * 0.2)}" width="{f(w * 0.28)}" height="{f(h * 0.7)}" fill="#FFC14D" stroke="#0D0D0F" stroke-width="2.6"></rect>',
         f'<path d="M{f(w * 0.64)} {f(h * 0.2)} L {f(w * 0.78)} {f(h * 0.14)} L {f(w * 0.78)} {f(h * 0.96)} L {f(w * 0.64)} {f(h * 0.9)} Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.9, "#1A0E10", dy=0)]
    return "".join(o)

def tamar_away(p, w, h, seed):
    """Tamar going her way with ashes on her head, her rent garment of divers colors, her hand laid on her head."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#5A5A7A", "#C8B8C8"), ground(w, h, h * 0.62, "#6A6070", dy=0)]
    s = fit(b, h * 0.44)
    stripes = "".join(f'<path d="M{x} -150 L {x + 2} -10" stroke="{c}" stroke-width="6"></path>' for x, c in zip(range(-24, 30, 12), ["#D7261E", "#FFD23F", "#1F5FAD", "#2E6B3A", "#C2456A"]))
    o.append(mk.person(p, round(w * 0.5), round(b), round(s, 3), body="#3A1E14", cloth="#8A6A9A", woman=True, hair="#1A1210", sw=3, up=[(-22, -158), (-16, -196), (0, -206)],
                       extra=stripes + '<path d="M-8 -150 L 4 -100 L -6 -60" stroke="#0D0D0F" stroke-width="2"></path><ellipse cx="0" cy="-200" rx="14" ry="6" fill="#8A8478" opacity="0.8"></ellipse>'))
    return "".join(o)

def feast_fled(p, w, h, seed):
    """The shearers' feast at Baal-hazor left empty: the table, a cup overturned, and the king's sons fleeing on their mules
    far off."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#E8B880", "#C8603A"), hills(w, h, h * 0.5, seed, color="#7A5A4A", amp=14), ground(w, h, h * 0.58, "#A88A5A", dy=0)]
    for i in range(4):
        x = w * (0.56 + i * 0.1); y = h * (0.6 + (i % 2) * 0.03)
        o.append(N.mount(x, y, min(0.28, h / 1400), flip=False, rider_cloth=["#8A3A1E", "#3A4A6A", "#5A5A2A", "#6A2A4A"][i], p=p + str(i)))
    o.append(S3.table(w * 0.3, b, w * 0.44, min(1.2, h / 300)))
    o.append(f'<g transform="translate({f(w * 0.42)} {f(b - 74 * min(1.2, h / 300))}) rotate(80)"><path d="M0 0 l -8 -20 l 16 0 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path></g>')
    return "".join(o)

def watch(p, w, h, seed):
    """The young man that kept the watch on the wall, and much people coming by the way of the hill-side behind him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#F3D8A0", "#E8B880"), f'<path d="M-10 {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.6)} {f(w * 0.5)} {f(h * 0.3)} {f(w + 10)} {f(h * 0.34)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B89A6A" stroke="#0D0D0F" stroke-width="2"></path>',
         S4.gatehouse(w * 0.24, b, w * 0.36, h * 0.6)]
    o.append(mk.person(p, round(w * 0.24), round(b - h * 0.62), round(fit(b, h * 0.6) * 0.5, 3), body="#2A140C", cloth="#5A6A8A", kind="Tunic", sw=3, up=[(22, -158), (40, -170), (60, -176)]))
    for i in range(8):
        t = i / 7; x = w * (0.6 + 0.36 * t); y = h * (0.62 - 0.22 * t)
        o.append(mk.person(p, round(x), round(y), round(fit(y, y - h * (0.14 - 0.06 * t)), 3), body="#2A140C", cloth=WAR[i % 4], kind="Tunic", sw=2, flip=True))
    return "".join(o)

def tekoa(p, w, h, seed):
    """The woman of Tekoa in mourning apparel fallen on her face before the king on his throne."""
    b = h * 0.92; k = min(1.3, h / 300)
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), S3.throne(w * 0.24, b, k)]
    s = fit(b, h * 0.36)
    o.append(king_fig(p, w * 0.24, b - 40 * k, s * 0.9))
    o.append(N.prostrate(w * 0.56, b, s * 0.8, color="#2A2A2E", skin="#8A5A3A", flip=True))
    return "".join(o)

def barley_fire(w, h, seed):
    """Joab's field of barley set on fire by Absalom's servants."""
    o = [sky(w, h, "#3A1A1A", "#C8603A"), ground(w, h, h * 0.6, "#5A4A2A", dy=0), J2.grain(-10, w + 10, h * 0.8, h * 0.24, seed, burning=True),
         J2.grain(-10, w + 10, h * 0.98, h * 0.3, seed + 1, burning=True)]
    for i in range(5):
        o.append(f'<circle cx="{f(w * (0.1 + i * 0.2))}" cy="{f(h * 0.3)}" r="{f(w * 0.1)}" fill="#3A2A2E" opacity="0.6"></circle>')
    return "".join(o)

def bowed(p, w, h, seed):
    """Absalom bowed himself on his face to the ground before the king."""
    b = h * 0.92; k = min(1.3, h / 300)
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), S3.throne(w * 0.24, b, k)]
    s = fit(b, h * 0.36)
    o.append(king_fig(p, w * 0.36, b, s * 0.9, flip=False))
    o.append(N.prostrate(w * 0.6, b, s * 0.8, color="#B5121B", skin="#8A5A3A", flip=True))
    return "".join(o)

# ---- 2 Samuel 15–16 -----------------------------------------------------------------------------------------------------
OLD_C = "#4A2A7A"
def old_king(p, x, y, s, flip=False, up=None, covered=False):
    """David old at a distance: purple tunic, the gold crown (covered=True: his head covered, no crown, barefoot)."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#5A2A16", cloth=OLD_C, kind="Robe" if covered else "Tunic", sw=3, flip=flip, up=up,
                     extra=(A.headcloth("#3A2A5A") if covered else S3.KING))

def chariot_runners(p, w, h, seed):
    """Absalom's chariot and horses, and fifty men running before him."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE680", "#F3D8A0"), J.city_hill(w * 0.82, h * 0.5, w * 0.3, h * 0.26, seed), ground(w, h, h * 0.52, "#C8A06A", dy=0)]
    for k in range(2):
        for i in range(6):
            x = w * (0.5 + i * 0.08 + k * 0.04); y = h * (0.66 + k * 0.08)
            o.append(S4.runner(p, x, y, fit(y, y - h * 0.18), flip=True, cloth="#E8E2D6"))
    o.append(E3.chariot(w * 0.24, b, min(1.0, h / 360), flip=True, color="#3A2214", driver="#B5121B"))
    return "".join(o)

def gate_out(p, w, h, seed):
    """The king went forth out of the city and all his household after him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8C8", "#E8C8A0"), S4.gatehouse(w * 0.76, b, w * 0.46, h * 0.76), ground(w, h, b, "#A88A6A", dy=0)]
    s = fit(b, h * 0.42)
    o.append(old_king(p, w * 0.42, b, s, flip=True))
    o.append(crowd_at(p, w, h, seed, w * 0.04, w * 0.34, h * 0.78, b, 7, s * 0.7, s * 0.9, flip=True))
    o.append(crowd_at(p, w, h, seed + 1, w * 0.5, w * 0.66, h * 0.84, b, 4, s * 0.7, s * 0.9, flip=True))
    return "".join(o)

def march_by(p, w, h, seed):
    """The Cherethites, the Pelethites and the six hundred Gittites passing on before the king."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#E8C8A0", "#F3D8A0"), hills(w, h, h * 0.5, seed, color="#9A8A6A", amp=12), ground(w, h, h * 0.6, "#B89A6A", dy=0)]
    s = fit(b, h * 0.38)
    o.append(old_king(p, w * 0.12, b, s))
    for k in range(3):
        for i in range(9):
            x = w * (0.26 + i * 0.085 + (k % 2) * 0.04); y = h * (0.7 + k * 0.1)
            o.append(warrior(p, x, y, fit(y, y - h * (0.18 + 0.04 * k)), ["#8A2A2A", "#2A4A6A", "#5A5A2A"][k], flip=True))
    return "".join(o)

def ark_kidron(p, w, h, seed):
    """Zadok and the Levites bearing the ark of the covenant of God, set down beside the brook Kidron."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8A9AB8", "#E8D8C8"), hills(w, h, h * 0.44, seed, color="#6A6A5A", amp=14), ground(w, h, h * 0.54, "#A8906A", dy=0),
         f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.6)} {f(w * 0.6)} {f(h * 0.66)} {f(w + 10)} {f(h * 0.62)}" stroke="#2C9DB8" stroke-width="10" fill="none"></path>']
    s = fit(b, h * 0.4)
    o.append(J.ark_borne(p, w * 0.5, b, s * 0.9, uid=p + "ab"))
    o.append(mk.person(p, round(w * 0.16), round(b), round(s, 3), body=SKIN, cloth="#E8E2D6", sw=3, extra=A.headcloth("#E8E2D6") + A.WHITE_BEARD))
    return "".join(o)

def ziba_asses(p, w, h, seed):
    """Ziba with a couple of asses saddled, laden with loaves, raisins, summer fruits and a bottle of wine."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#E8B880", "#F3D8A0"), hills(w, h, h * 0.5, seed, color="#8A7A5A", amp=14), ground(w, h, h * 0.6, "#B89A6A", dy=0)]
    k = min(1.0, h / 300)
    for i, x in enumerate((0.42, 0.68)):
        o.append(N.ass(w * x, b - i * 6, k, flip=True))
        o.append(f'<rect x="{f(w * x - 34 * k)}" y="{f(b - 112 * k)}" width="{f(60 * k)}" height="{f(26 * k)}" rx="6" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 + "".join(f'<circle cx="{f(w * x - 24 * k + j * 16 * k)}" cy="{f(b - 116 * k)}" r="{f(7 * k)}" fill="{["#D9A25A", "#6A2A4A", "#C8703A"][j % 3]}" stroke="#0D0D0F" stroke-width="1.4"></circle>' for j in range(4)))
    o.append(captain(p, w * 0.16, b, fit(b, h * 0.36), cloth="#7A5A3A", spear=False))
    return "".join(o)

def shimei(p, w, h, seed):
    """Shimei on the hill-side over against David, cursing and casting stones and dust; David's men on the way below."""
    r = random.Random(seed)
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#E8C8A0"),
         f'<path d="M{f(w * 0.4)} {f(h * 0.5)} C {f(w * 0.6)} {f(h * 0.2)} {f(w * 0.8)} {f(h * 0.16)} {f(w + 10)} {f(h * 0.2)} L {f(w + 10)} {f(h * 0.62)} Z" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.62, "#A8906A", dy=0)]
    sx, sy = w * 0.78, h * 0.24
    o.append(mk.person(p, round(sx), round(sy), round(fit(sy, sy - h * 0.16), 3), body="#2A140C", cloth="#6A5A3A", sw=2, flip=True, up=[(22, -158), (40, -190), (30, -220)]))
    for i in range(6):
        x = r.uniform(w * 0.3, w * 0.7); y = r.uniform(h * 0.3, h * 0.6)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="6" ry="5" fill="#7A746A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    o.append(f'<path d="M{f(w * 0.72)} {f(h * 0.2)} C {f(w * 0.6)} {f(h * 0.2)} {f(w * 0.5)} {f(h * 0.3)} {f(w * 0.44)} {f(h * 0.44)}" stroke="#C8B89A" stroke-width="18" fill="none" opacity="0.4"></path>')
    s = fit(b, h * 0.6)
    o.append(old_king(p, w * 0.2, b, s, flip=False))
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.4, h * 0.76, b, 8, s * 0.6, s * 0.9))
    return "".join(o)

def roof_tent(w, h, seed):
    """A tent spread upon the top of the king's house, over the rooftops of Jerusalem (16:22 told in words only)."""
    o = [sky(w, h, "#5A3A5A", "#E8A06A"), S3.roof(w, h, h * 0.6, seed), E4.tent(w * 0.5, h * 0.66, w * 0.3, h * 0.24, color="#B5121B", stripe="#5A0A0A")]
    return "".join(o)

# ---- 2 Samuel 17–18 -----------------------------------------------------------------------------------------------------
def well_court(p, w, h, seed, men=False):
    """The court of a house in Bahurim: the well's mouth covered with a spread covering and bruised grain strewn on it, the
    woman of the house beside it (men=True: Absalom's servants at the door)."""
    r = random.Random(seed)
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#D8B88A"></rect>',
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></rect>', ground(w, h, h * 0.6, "#B89A6A", dy=0),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.8)}" rx="{f(w * 0.16)}" ry="{f(h * 0.06)}" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.79)}" rx="{f(w * 0.15)}" ry="{f(h * 0.05)}" fill="#C8A060" stroke="#0D0D0F" stroke-width="1.6"></ellipse>']
    for i in range(30):
        o.append(f'<circle cx="{f(w * 0.5 + r.uniform(-w * 0.12, w * 0.12))}" cy="{f(h * 0.79 + r.uniform(-h * 0.03, h * 0.03))}" r="2" fill="#E8D8A0"></circle>')
    s = fit(b, h * 0.4)
    o.append(woman(p, w * 0.76, b, s, "#6A4A6A", flip=True))
    if men:
        for i in range(3): o.append(captain(p, w * (0.08 + i * 0.1), b, s * 0.95, cloth=["#B5121B", "#5A3A2A", "#3A3A5A"][i]))
    return "".join(o)

def jordan_dawn(p, w, h, seed):
    """By the morning light all the people gone over the Jordan."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5A5A8A", "#FFC89A"), sun(w * 0.8, h * 0.4, 26, color="#FFE680", op=0.5), hills(w, h, h * 0.44, seed, color="#5A5A6A", amp=14),
         f'<path d="M-10 {f(h * 0.58)} C {f(w * 0.3)} {f(h * 0.54)} {f(w * 0.6)} {f(h * 0.64)} {f(w + 10)} {f(h * 0.58)} L {f(w + 10)} {f(h * 0.7)} C {f(w * 0.6)} {f(h * 0.76)} {f(w * 0.3)} {f(h * 0.66)} -10 {f(h * 0.7)} Z" fill="#2C7DA8" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, h * 0.7, "#8A7A5A", dy=0)]
    s = fit(b, h * 0.3)
    o.append(old_king(p, w * 0.7, b, s))
    o.append(crowd_at(p, w, h, seed, w * 0.04, w * 0.96, h * 0.76, b, 14, s * 0.6, s * 0.9))
    return "".join(o)

def ahithophel_home(p, w, h, seed):
    """Ahithophel's city at dusk, the ass he saddled standing at the door (17:23 told in words only)."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A", "#C8603A"), J.city_hill(w * 0.5, h * 0.66, w * 0.6, h * 0.36, seed), ground(w, h, h * 0.68, "#3A2A2A", dy=0),
         N.ass(w * 0.3, b, min(1.0, h / 320), color="#5A5650")]
    return "".join(o)

def gilead_camp(p, w, h, seed):
    """Israel and Absalom encamped in the land of Gilead: tents and watch-fires on the hills by night."""
    o = [mk.defs(p, *ALL), night(w, h, seed, "#14123A"), hills(w, h, h * 0.4, seed, color="#1E1A3A", amp=20), ground(w, h, h * 0.56, "#1A1628", dy=0),
         N.camp(18, -10, w + 10, h * 0.62, h * 0.96, seed, color=("#2A2040", "#3A2A4A", "#1A1428"))]
    for i in range(5):
        o.append(E.blaze(w * (0.1 + i * 0.2), h * (0.7 + (i % 2) * 0.1), w * 0.03, h * 0.06, seed + i, n=3))
    return "".join(o)

def provisions(w, h, seed):
    """Beds, basins and earthen vessels, wheat, barley, meal, parched grain, beans and lentils, honey, butter, sheep and cheese,
    brought to David at Mahanaim."""
    r = random.Random(seed)
    o = [sky(w, h, "#E8B880", "#F3D8A0"), ground(w, h, h * 0.6, "#B89A6A", dy=0)]
    for i in range(6):
        x = w * (0.08 + i * 0.12); c = ["#C8A060", "#E8D8A0", "#D9A25A", "#8A5A30", "#C8B070", "#6A4A2A"][i]
        o.append(f'<path d="M{f(x - 22)} {f(h * 0.88)} C {f(x - 30)} {f(h * 0.7)} {f(x - 16)} {f(h * 0.64)} {f(x)} {f(h * 0.64)} C {f(x + 16)} {f(h * 0.64)} {f(x + 30)} {f(h * 0.7)} {f(x + 22)} {f(h * 0.88)} Z" fill="{c}" stroke="#0D0D0F" stroke-width="2"></path>')
    for i in range(3):
        x = w * (0.8 + i * 0.07)
        o.append(f'<g transform="translate({f(x)} {f(h * 0.88)}) scale({f(min(1.0, h / 300))})"><path d="M-18 0 C -24 -26 -22 -44 -10 -50 L -8 -60 L 8 -60 L 10 -50 C 22 -44 24 -26 18 0 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path></g>')
    o.append(E.sheep(w * 0.62, h * 0.94, min(0.8, h / 400)))
    return "".join(o)

def dark_oak(w, h, seed):
    """The great oak in the forest of Ephraim, a black shape against a red sky (18:14–15 told in words only)."""
    o = [sky(w, h, "#2A0A0A", "#C8402A"), ground(w, h, h * 0.86, "#1A0A0A", dy=0), S4.great_oak(w * 0.5, h * 0.9, min(1.6, h / 260), seed, dark=True)]
    return "".join(o)

def pillar(w, h, seed):
    """Absalom's monument: the pillar he reared up for himself in the king's dale."""
    o = [sky(w, h, "#5A4A6A", "#E8B880"), hills(w, h, h * 0.5, seed, color="#6A5A5A", amp=20), ground(w, h, h * 0.7, "#8A7A5A", dy=0),
         f'<path d="M{f(w * 0.46)} {f(h * 0.86)} L {f(w * 0.47)} {f(h * 0.14)} L {f(w * 0.5)} {f(h * 0.08)} L {f(w * 0.53)} {f(h * 0.14)} L {f(w * 0.54)} {f(h * 0.86)} Z" fill="#B8A890" stroke="#0D0D0F" stroke-width="2.6"></path>'
         f'<rect x="{f(w * 0.42)}" y="{f(h * 0.84)}" width="{f(w * 0.16)}" height="{f(h * 0.06)}" fill="#9A8A72" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    return "".join(o)

def two_runners(p, w, h, seed):
    """The watchman on the roof of the gate, and two men running alone, one far behind the other."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#FFE6A0", "#E8B880"), ground(w, h, h * 0.6, "#C8A06A", dy=0), S4.gatehouse(w * 0.24, b, w * 0.36, h * 0.66)]
    o.append(mk.person(p, round(w * 0.24), round(b - h * 0.68), round(fit(b, h * 0.6) * 0.5, 3), body="#2A140C", cloth="#5A6A8A", kind="Tunic", sw=3, up=[(22, -158), (40, -170), (60, -176)]))
    o.append(S4.runner(p, w * 0.62, h * 0.78, fit(h * 0.78, h * 0.6), flip=True) + S4.runner(p, w * 0.9, h * 0.66, fit(h * 0.66, h * 0.56), flip=True, cloth="#F3EFE6", body="#2A140C"))
    return "".join(o)

# ---- 2 Samuel 19–20 -----------------------------------------------------------------------------------------------------
def gate_king(p, w, h, seed):
    """The king sitting in the gate, and all the people coming before him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#F3D8A0"), S4.gatehouse(w * 0.3, b, w * 0.5, h * 0.8), ground(w, h, b, "#B89A6A", dy=0)]
    s = fit(b, h * 0.4)
    o.append(f'<rect x="{f(w * 0.3 - 30 * s)}" y="{f(b - 50 * s)}" width="{f(60 * s)}" height="{f(50 * s)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(old_king(p, w * 0.3, b - 40 * s, s * 0.9))
    o.append(crowd_at(p, w, h, seed, w * 0.6, w * 0.98, h * 0.76, b, 9, s * 0.7, s * 0.95, flip=True))
    return "".join(o)

def ferry(p, w, h, seed):
    """The ferry-boat over the Jordan bringing the king's household, the men of Judah on the bank, Shimei fallen down
    before the king."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#E8F6FA"), hills(w, h, h * 0.36, seed, color="#6A7A5A", amp=14),
         f'<rect x="-10" y="{f(h * 0.44)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#2C7DA8" stroke="#0D0D0F" stroke-width="2"></rect>', ground(w, h, h * 0.64, "#A89A6A", dy=0),
         f'<path d="M{f(w * 0.2)} {f(h * 0.54)} L {f(w * 0.56)} {f(h * 0.54)} L {f(w * 0.52)} {f(h * 0.6)} L {f(w * 0.24)} {f(h * 0.6)} Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for i in range(5):
        o.append(mk.person(p, round(w * (0.26 + i * 0.06)), round(h * 0.55), round(fit(h * 0.55, h * 0.42), 3), body="#2A140C", cloth=WAR[i % 4], sw=2))
    s = fit(b, h * 0.36)
    o.append(old_king(p, w * 0.72, b, s, flip=True))
    o.append(N.prostrate(w * 0.42, b, s * 0.8, color="#6A5A3A", skin="#9A6A4A", flip=False))
    return "".join(o)

def judah_israel(p, w, h, seed):
    """The men of Judah and the men of Israel face to face, their words fierce."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#E8B880", "#C8603A"), ground(w, h, h * 0.6, "#A88A5A", dy=0)]
    s = fit(b, h * 0.42)
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.42, h * 0.7, b, 10, s * 0.6, s))
    o.append(crowd_at(p, w, h, seed + 1, w * 0.58, w * 0.98, h * 0.7, b, 10, s * 0.6, s, flip=True))
    o.append(V.rays(w * 0.5, h * 0.66, 12, 8, w * 0.2, color="#FFF4C2", op=0.6))
    return "".join(o)

def sheba(p, w, h, seed):
    """Sheba the son of Bichri blowing the trumpet on a hill: every man to his tents, O Israel."""
    b = h * 0.6
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A5A", "#E8803A"), sun(w * 0.7, h * 0.5, 30, color="#FFB04A", op=0.4),
         f'<path d="M{f(w * 0.2)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.6)} {f(w * 0.5)} {f(h * 0.58)} {f(w * 0.64)} {f(h * 0.62)} C {f(w * 0.8)} {f(h * 0.7)} {f(w * 0.9)} {f(h * 0.9)} {f(w + 10)} {f(h + 10)} Z" fill="#3A2A2A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = fit(b, h * 0.26)
    o.append(J.trumpeter(p, w * 0.46, b, s, body="#2A140C") + J.blasts(w * 0.46 + 70 * s, b - 170 * s, s))
    for i in range(6):
        x = w * (0.04 + i * 0.06); y = h * (0.86 + (i % 2) * 0.06)
        o.append(mk.person(p, round(x), round(y), round(fit(y, y - h * 0.18), 3), body="#0B0814", cloth="#2A2030", kind="Tunic", sw=2, flip=True))
    return "".join(o)

def ward(w, h, seed):
    """The house of ward: a shut house with barred lattices, a lamp in one window."""
    o = [sky(w, h, "#3A3A5A", "#8A7A8A"), ground(w, h, h * 0.88, "#3A3440", dy=0),
         f'<rect x="{f(w * 0.14)}" y="{f(h * 0.2)}" width="{f(w * 0.72)}" height="{f(h * 0.68)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.6"></rect>']
    for i in range(4):
        x = w * (0.2 + i * 0.16); y = h * 0.34
        lit = i == 2
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.08)}" height="{f(h * 0.14)}" fill="{"#FFC14D" if lit else "#1A1214"}" stroke="#0D0D0F" stroke-width="2"></rect>'
                 + "".join(f'<path d="M{f(x + k * w * 0.02)} {f(y)} L {f(x + k * w * 0.02)} {f(y + h * 0.14)}" stroke="#3A2A1A" stroke-width="2.4"></path>' for k in range(1, 4)))
    o.append(f'<rect x="{f(w * 0.44)}" y="{f(h * 0.6)}" width="{f(w * 0.12)}" height="{f(h * 0.28)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    return "".join(o)

def great_stone(p, w, h, seed):
    """The great stone which is in Gibeon, and Amasa coming to meet Joab's men."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#E8C8A0"), ground(w, h, h * 0.66, "#A8906A", dy=0),
         f'<path d="M{f(w * 0.36)} {f(b)} C {f(w * 0.34)} {f(h * 0.5)} {f(w * 0.44)} {f(h * 0.34)} {f(w * 0.52)} {f(h * 0.36)} C {f(w * 0.62)} {f(h * 0.38)} {f(w * 0.68)} {f(h * 0.6)} {f(w * 0.66)} {f(b)} Z" fill="#8A8478" stroke="#0D0D0F" stroke-width="2.6"></path>']
    s = fit(b, h * 0.4)
    o.append(captain(p, w * 0.24, b, s) + captain(p, w * 0.8, b, s, cloth="#3A5A4A", flip=True))
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.16, h * 0.74, b, 5, s * 0.6, s * 0.85))
    return "".join(o)

def highway(w, h, seed):
    """The highway, and a garment cast over something in the field beside it (20:10–12 told in words only)."""
    o = [sky(w, h, "#5A4A5A", "#C88A6A"), hills(w, h, h * 0.44, seed, color="#5A4A4A", amp=12), ground(w, h, h * 0.54, "#8A7A5A", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.46)} {f(h * 0.54)} L {f(w * 0.54)} {f(h * 0.54)} L {f(w * 0.7)} {f(h + 10)} Z" fill="#B8A88A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.06)} {f(h * 0.86)} C {f(w * 0.1)} {f(h * 0.78)} {f(w * 0.2)} {f(h * 0.76)} {f(w * 0.26)} {f(h * 0.84)} L {f(w * 0.24)} {f(h * 0.88)} L {f(w * 0.08)} {f(h * 0.88)} Z" fill="#6A2A2A" stroke="#0D0D0F" stroke-width="2"></path>']
    return "".join(o)

def abel_siege(p, w, h, seed, battering=True):
    """Abel of Beth-maacah besieged: a mound cast up against the wall, the people battering it; the wise woman on the wall."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), J.jericho(w * 0.4, w + 10, h * 0.16, h * 0.62, seed, towers=3, houses=True), ground(w, h, h * 0.62, "#B89A6A", dy=0),
         f'<path d="M{f(w * 0.04)} {f(b)} L {f(w * 0.36)} {f(h * 0.6)} L {f(w * 0.46)} {f(h * 0.6)} L {f(w * 0.5)} {f(b)} Z" fill="#9A7A4A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    o.append(mk.person(p, round(w * 0.62), round(h * 0.16), round(fit(h * 0.16, h * 0.04), 3), body="#3A1E14", cloth="#6A4A6A", woman=True, hair="#1A1210", sw=2))
    if battering:
        s = fit(b, h * 0.3)
        for i in range(5):
            o.append(warrior(p, w * (0.14 + i * 0.06), b - i * h * 0.05, s * (1 - i * 0.08), WAR[i % 4]))
    else:
        o.append(J.trumpeter(p, w * 0.2, b, fit(b, h * 0.5), body="#3A1E14") + J.blasts(w * 0.2 + 70 * fit(b, h * 0.5), b - 170 * fit(b, h * 0.5), fit(b, h * 0.5)))
    return "".join(o)

# ---- 2 Samuel 21–22 -----------------------------------------------------------------------------------------------------
def famine(w, h, seed):
    """Famine three years: a cracked field under a white sun, the stalks withered."""
    r = random.Random(seed)
    o = [sky(w, h, "#FFF4C2", "#E8B880"), sun(w * 0.7, h * 0.2, 30, color="#FFFFFF", op=0.7), ground(w, h, h * 0.5, "#C8A06A", dy=0)]
    for i in range(14):
        x = r.uniform(0, w); y = r.uniform(h * 0.56, h); l = r.uniform(30, 90)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(l * 0.4)} {f(-l * 0.1)} l {f(l * 0.3)} {f(l * 0.12)} l {f(l * 0.3)} {f(-l * 0.06)}" stroke="#7A5A3A" stroke-width="2" fill="none"></path>')
    for i in range(12):
        x = w * (0.04 + i * 0.08)
        o.append(f'<path d="M{f(x)} {f(h * 0.6)} C {f(x + 2)} {f(h * 0.54)} {f(x + 10)} {f(h * 0.52)} {f(x + 16)} {f(h * 0.56)}" stroke="#8A6A3A" stroke-width="2.4" fill="none"></path>')
    return "".join(o)

def harvest_mount(w, h, seed):
    """The mountain before Jehovah at the beginning of barley harvest, the ripe barley below it (21:9 told in words only)."""
    o = [sky(w, h, "#C8B8A0", "#F3D8A0"), f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.3)} {f(h * 0.2)} {f(w * 0.6)} {f(h * 0.16)} {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         R1.field(-10, w + 10, h * 0.76, h * 0.2, seed)]
    return "".join(o)

def rizpah(p, w, h, seed):
    """Rizpah upon the rock on her spread sackcloth, keeping watch from harvest until the rain, birds wheeling above."""
    r = random.Random(seed)
    b = h * 0.62
    o = [mk.defs(p, *ALL), sky(w, h, "#5A4A5A", "#C8A080"),
         f'<path d="M{f(w * 0.1)} {f(h + 10)} L {f(w * 0.2)} {f(h * 0.62)} L {f(w * 0.7)} {f(h * 0.6)} L {f(w * 0.86)} {f(h + 10)} Z" fill="#7A6A5A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.3)} {f(b)} L {f(w * 0.56)} {f(b)} L {f(w * 0.54)} {f(b + 10)} L {f(w * 0.32)} {f(b + 10)} Z" fill="#3A3430" stroke="#0D0D0F" stroke-width="1.6"></path>']
    o.append(mk.person(p, round(w * 0.42), round(b), round(fit(b, h * 0.3), 3), body="#3A1E14", cloth="#3A3430", woman=True, hair="#6A645E", sw=3, up=[(-22, -158), (-50, -190), (-70, -220)]))
    for i in range(6):
        x = r.uniform(w * 0.2, w * 0.9); y = r.uniform(h * 0.08, h * 0.36); s = r.uniform(8, 14)
        o.append(f'<path d="M{f(x - s)} {f(y)} Q {f(x - s / 2)} {f(y - s / 2)} {f(x)} {f(y)} Q {f(x + s / 2)} {f(y - s / 2)} {f(x + s)} {f(y)}" stroke="#0D0D0F" stroke-width="2.4" fill="none"></path>')
    return "".join(o)

def giant(p, w, h, seed, fallen=False):
    """One of the sons of the giant in brass, his great spear; (fallen=True: fallen upon his face)."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#E8B880", "#F3D8A0"), hills(w, h, h * 0.5, seed, color="#9A7A5A", amp=12), ground(w, h, h * 0.62, "#B89A6A", dy=0)]
    s = fit(b, h * 0.1)
    if fallen: o.append(S2.goliath_fallen(w * 0.5, b, min(1.0, h / 360)))
    else:
        o.append(S2.goliath(p, w * 0.62, b, s * 0.95, flip=True))
        o.append(captain(p, w * 0.22, b, s * 0.55, cloth="#5A5A6A"))
    return "".join(o)

def waves(w, h, seed):
    """The waves of death compassed me; the floods of ungodliness."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0B1A2E"></rect>', E3.crash(w, h, seed)]
    return "".join(o)

def storm(w, h, seed, sea=False):
    """The earth shook and trembled, thick darkness and the clouds, lightning out of the brightness (God is never drawn)."""
    r = random.Random(seed)
    o = [sky(w, h, "#0B0B2A", "#3A2A5A"), A.horeb(w, h, h * 0.92, seed, color="#2A1E2E", lit="#5A3A4A") if not sea else
         f'<rect x="-10" y="{f(h * 0.6)}" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#0F3A5A"></rect>']
    for i in range(7):
        o.append(f'<ellipse cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(0, h * 0.3))}" rx="{f(w * r.uniform(0.15, 0.3))}" ry="{f(h * 0.08)}" fill="#1A1430" opacity="0.9"></ellipse>')
    for i in range(3):
        x = r.uniform(w * 0.2, w * 0.8); y = h * 0.2
        o.append(f'<path d="M{f(x)} {f(y)} l -14 {f(h * 0.14)} l 16 0 l -22 {f(h * 0.2)}" stroke="#FFF4C2" stroke-width="4" fill="none"></path>')
    return "".join(o)

def large_place(w, h, seed):
    """He brought me forth also into a large place: a broad sunlit plain under an open sky."""
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.5, h * 0.36, 40, color="#FFE680", op=0.6), V.rays(w * 0.5, h * 0.36, 30, 20, max(w, h), color="#FFF4C2", op=0.25),
         hills(w, h, h * 0.6, seed, color="#9CCB5E", amp=8), ground(w, h, h * 0.66, "#B8C86A", dy=0)]
    return "".join(o)

def lamp(w, h, seed):
    """For thou art my lamp, O Jehovah; and Jehovah will lighten my darkness."""
    from genesis.art4 import clay_lamp
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0B0B1A"></rect>',
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.6)}" r="{f(max(w, h) * 0.5)}" fill="#FFC14D" opacity="0.12"></circle>',
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.6)}" r="{f(max(w, h) * 0.25)}" fill="#FFC14D" opacity="0.15"></circle>',
         clay_lamp(w * 0.5, h * 0.8, min(2.4, h / 140))]
    return "".join(o)

def hinds(p, w, h, seed):
    """He maketh my feet like hinds' feet, and setteth me upon my high places: a figure on the crags above the valley."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#E8F6FA"), hills(w, h, h * 0.66, seed, color="#8A9A7A", amp=10),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.46)} {f(h * 0.3)} L {f(w * 0.56)} {f(h * 0.26)} L {f(w * 0.66)} {f(h * 0.44)} L {f(w * 0.8)} {f(h + 10)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.6"></path>']
    o.append(king_fig(p, w * 0.53, h * 0.27, fit(h * 0.27, h * 0.08), up=[(-22, -158), (-6, -196), (8, -228)]))
    return "".join(o)

# ---- 2 Samuel 23–24 -----------------------------------------------------------------------------------------------------
def well_gate(p, w, h, seed, pour=False):
    """The well of Beth-lehem which is by the gate; (pour=True) David pouring out the water unto Jehovah."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#E8B880", "#F3D8A0"), S4.gatehouse(w * 0.74, b, w * 0.4, h * 0.6), ground(w, h, b, "#B89A6A", dy=0),
         f'<ellipse cx="{f(w * 0.36)}" cy="{f(b - h * 0.02)}" rx="{f(w * 0.1)}" ry="{f(h * 0.03)}" fill="#8A8478" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
         f'<rect x="{f(w * 0.26)}" y="{f(b - h * 0.1)}" width="{f(w * 0.2)}" height="{f(h * 0.08)}" fill="#A89E92" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    if pour:
        s = fit(b, h * 0.36)
        o.append(old_king(p, w * 0.24, b, s, up=[(22, -158), (40, -150), (62, -150)]))
        o.append(f'<path d="M{f(w * 0.24 + 62 * s)} {f(b - 150 * s)} C {f(w * 0.24 + 70 * s)} {f(b - 100 * s)} {f(w * 0.24 + 64 * s)} {f(b - 50 * s)} {f(w * 0.24 + 70 * s)} {f(b)}" stroke="#8FD0E2" stroke-width="5" fill="none"></path>')
        o.append(crowd_at(p, w, h, seed, w * 0.5, w * 0.62, h * 0.8, b, 3, s * 0.8, s * 0.95, flip=True))
    return "".join(o)

CENSUS = [("JERUSALEM", 0.42, 0.62), ("AROER", 0.62, 0.74), ("JAZER", 0.66, 0.56), ("GILEAD", 0.66, 0.4), ("DAN-JAAN", 0.54, 0.12), ("SIDON", 0.32, 0.08),
          ("TYRE", 0.26, 0.18), ("BEER-SHEBA", 0.34, 0.92), ("JERUSALEM", 0.42, 0.62)]
def census_map(w, h):
    """Joab's numbering as a technical map: over the Jordan to Aroer and Jazer, Gilead, Dan-jaan, round to Sidon and Tyre,
    south to Beer-sheba, and back to Jerusalem after nine months and twenty days."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.2)} -10 C {f(w * 0.2)} {f(h * 0.3)} {f(w * 0.14)} {f(h * 0.7)} {f(w * 0.1)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.52)} {f(h * 0.2)} C {f(w * 0.54)} {f(h * 0.4)} {f(w * 0.52)} {f(h * 0.6)} {f(w * 0.54)} {f(h * 0.72)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>')
    o.append(route([(w * x, h * y) for _, x, y in CENSUS], color="#FFD23F"))
    for nm, x, y in CENSUS[:-1]:
        o.append(node(w * x, h * y, nm, "#D7261E" if nm == "JERUSALEM" else "#FFD23F", r=5, dy=-12, size=9))
    return "".join(o)

def sum_board(w, h):
    """The sum of the numbering, as a tally board: Israel and Judah."""
    o = [grid_bg(w, h, color="#3A2A5A", bg="#1A1430")]
    for i, (nm, n, c) in enumerate([("ISRAEL", "800,000", "#8FD0E2"), ("JUDAH", "500,000", "#FFD23F")]):
        x = w * (0.28 + i * 0.44)
        o.append(f'<rect x="{f(x - w * 0.18)}" y="{f(h * 0.2)}" width="{f(w * 0.36)}" height="{f(h * 0.6)}" fill="none" stroke="{c}" stroke-width="2"></rect>'
                 + label(x, h * 0.36, nm, c, 14) + f'<text x="{f(x)}" y="{f(h * 0.62)}" fill="{c}" font-family="Anton, sans-serif" font-size="{f(min(w * 0.08, h * 0.2))}" text-anchor="middle">{n}</text>')
    return "".join(o)

def pestilence(w, h, seed):
    """From Dan even to Beer-sheba: the land silent under a dark sky, the tents shut (no one drawn)."""
    o = [sky(w, h, "#1A1A2A", "#5A4A5A"), hills(w, h, h * 0.5, seed, color="#2A2430", amp=16), ground(w, h, h * 0.62, "#2A2228", dy=0),
         N.camp(14, -10, w + 10, h * 0.7, h * 0.96, seed, color=("#3A3038", "#2A2228", "#4A3A40"))]
    return "".join(o)

def angel_city(p, w, h, seed):
    """The angel of Jehovah by the threshing-floor of Araunah, his hand stretched out toward Jerusalem."""
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A", "#8A5A6A"), J.city_hill(w * 0.36, h * 0.8, w * 0.6, h * 0.36, seed), ground(w, h, h * 0.82, "#3A2A2A", dy=0),
         S4.threshing_floor(w * 0.76, h * 0.92, w * 0.36), V.rays(w * 0.76, h * 0.4, 24, 12, w * 0.4, color="#FFF4C2", op=0.25),
         N.angel(p, w * 0.76, h * 0.86, fit(h * 0.86, h * 0.16), sword=True, glow=True, flip=True)]
    return "".join(o)

def araunah(p, w, h, seed):
    """Araunah bowing himself with his face to the ground before the king at his threshing-floor, his oxen beside it."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), J.city_hill(w * 0.8, h * 0.56, w * 0.36, h * 0.26, seed), ground(w, h, h * 0.58, "#C8A06A", dy=0),
         S4.threshing_floor(w * 0.6, b, w * 0.5)]
    s = fit(b, h * 0.38)
    o.append(old_king(p, w * 0.2, b, s) + captain(p, w * 0.08, b, s * 0.9, cloth="#3A4A6A"))
    o.append(N.prostrate(w * 0.44, b, s * 0.8, color="#7A6A4A", skin="#9A6A4A", flip=True))
    o.append(S1.cow(w * 0.72, b - h * 0.06, min(0.8, h / 400), color="#8A5A30") + S1.cow(w * 0.84, b - h * 0.04, min(0.8, h / 400)))
    return "".join(o)

def altar_floor(p, w, h, seed):
    """David's altar on the threshing-floor of Araunah, the burnt-offering burning, the king before it, Jerusalem beyond."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#FFB04A", "#FFE680"), V.rays(w * 0.56, h * 0.5, 30, 20, max(w, h), color="#FFF4C2", op=0.3),
         J.city_hill(w * 0.86, h * 0.6, w * 0.3, h * 0.24, seed), ground(w, h, h * 0.62, "#C8A06A", dy=0), S4.threshing_floor(w * 0.56, b, w * 0.6),
         S4.altar(w * 0.56, b - h * 0.04, min(1.2, h / 300), seed=seed)]
    o.append(old_king(p, w * 0.2, b, fit(b, h * 0.4), up=[(-22, -158), (-6, -196), (8, -228)]))
    return "".join(o)
