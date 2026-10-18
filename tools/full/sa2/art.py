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
