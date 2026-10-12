"""New drawings for Exodus chapter 5 (Exodus 16–18): the flesh-pots, the omer, the gathering of manna, the worms, the
sabbath, the pot of manna laid up, Rephidim, the altar Jehovah-nissi, Jethro's coming, and Moses judging the people."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4, exodus5 as V, samuel4 as A4, egypt as EG
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art10 as T
from genesis.art2 import fit, ground, hills, city, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg
from exo import art as A
def f(v): return f"{v:.1f}"

JOSHUA = A.tok("JOSHUA")
WOMAN, WOMAN_FEAR = A.tok("WOMAN"), A.tok("WOMAN_FEAR")
MOSES_TIRED = F("adam", skin="#C98E66", shadow="#6A4A5A", hair="#2A1A10", hl="#5A4A3E", beard=True, scarf="#E2D8C4", cord=True, brow="sorrow", sweat=True, light="#FFC14D")
ELIEZER = F("adam", skin="#C98E66", shadow="#8A5A3E", hair="#2A1A10", hl="#5A4A3E", light="#FFE680")    # Moses' younger son, a lad
JETHRO_JOY = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#E8E2D6", hl="#B8B2A6", beard=True, beard_color="#E8E2D6", scarf="#1F4A5A", band=True, light="#FFE680", laugh=True)

def joshua(p, x, y, s, flip=False, up=None):
    """Joshua the young captain: bareheaded, black hair, a sword."""
    sw = '<path d="M14 -150 L 46 -236" stroke="#C8C8D0" stroke-width="5" stroke-linecap="round"></path>' if up else ""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#7A2A1E", kind="Tunic", sw=3, flip=flip, up=up, extra=sw)

def hur(p, x, y, s, flip=False, up=None):
    """Hur: a silhouette in a brown robe (the Exodus character guide)."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#2A1A10", cloth="#5A3A22", sw=3, flip=flip, up=up)

def flesh_pots(w, h, seed):
    """When we sat by the flesh-pots, when we did eat bread to the full: a remembered Egypt, pots steaming over fires, loaves piled."""
    b = h * 0.84
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A1A2E"></rect>', EG.pyramid(w * 0.82, b, w * 0.3, h * 0.5), ground(w, h, b, "#5A3A3A", dy=0)]
    for x in (0.18, 0.46):
        o.append(E.blaze(w * x, b, w * 0.12, h * 0.16, seed + int(x * 10), n=5)
                 + f'<path d="M{f(w * x - w * 0.09)} {f(b - h * 0.18)} C {f(w * x - w * 0.09)} {f(b - h * 0.02)} {f(w * x + w * 0.09)} {f(b - h * 0.02)} {f(w * x + w * 0.09)} {f(b - h * 0.18)} Z" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 + "".join(f'<path d="M{f(w * x + d)} {f(b - h * 0.2)} c 8 -14 -8 -24 0 -40" fill="none" stroke="#F3EFE6" stroke-width="3" opacity="0.6"></path>' for d in (-14, 0, 14)))
    o += [f'<ellipse cx="{f(w * 0.64 + i * 18)}" cy="{f(b - 6 - (i % 2) * 10)}" rx="16" ry="7" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></ellipse>' for i in range(4)]
    return "".join(o)

def glory_cloud(p, w, h, seed):
    """They looked toward the wilderness, and, behold, the glory of Jehovah appeared in the cloud: a bright cloud on the horizon, the people turned toward it."""
    b = h * 0.88; r = random.Random(seed)
    o = [V.rays(w * 0.7, h * 0.3, 30, 30, max(w, h), color="#FFF4C2", op=0.3), E3.pillar_cloud(w * 0.7, h * 0.56, h * 0.04, w * 0.08, seed).replace("#E8E2D6", "#FFF4C2"),
         ground(w, h, h * 0.56, "#E8C88A", dy=0)]
    for i in range(12):
        x = w * (0.04 + i * 0.05); s = 0.2 + 0.06 * (i % 3)
        o.append((man if i % 2 else woman)(p, x, b - (i % 3) * 8, s, r.choice(A.HEBREW + ["#5A6E8A", "#C2456A"])))
    return "".join(o)

def dew_camp(w, h, seed):
    """In the morning the dew lay round about the camp: the tents at dawn, the ground silvered."""
    r = random.Random(seed); b = h * 0.66
    o = [sun(w * 0.2, b, 24, color="#FFC14D", op=0.3), ground(w, h, b, "#C8B8A0", dy=0)]
    o += [A.black_tent(w * x, b + 4, w * 0.12, h * 0.16) for x in (0.12, 0.3, 0.5, 0.7, 0.88)]
    o += [f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(b + 10, h))}" r="{f(r.uniform(1.2, 2.6))}" fill="#F3EFE6" opacity="0.9"></circle>' for _ in range(160)]
    return "".join(o)

def gathering(p, w, h, seed, some=False):
    """Gather ye of it every man according to his eating: men and women stooping over the white flakes with baskets and jars."""
    r = random.Random(seed); b = h * 0.9
    o = [sun(w * 0.86, h * 0.16, 14, op=0.3), ground(w, h, h * 0.4, "#E8D8B0", dy=0), E4.manna(220, 0, w, h * 0.42, h, seed)]
    for i in range(6):
        x = w * (0.08 + i * 0.17); y = b - r.uniform(0, h * 0.2)
        o.append(E.kneel(x, y, 0.3 + 0.2 * (y - h * 0.5) / (h * 0.5), color=r.choice(A.HEBREW + ["#5A6E8A", "#C2456A"]), skin="#8A5A3E", flip=i % 2 == 1) + E4.basket(x + 30, y, 0.8))
    return "".join(o)

def omers(w, h, seed, n=7, double=False):
    """An omer a head: a row of clay measures, each filled level; on the sixth day, two to each one."""
    o = [grid_bg(w, h, color="#3A2A1A", step=24, bg="#2A1A10")]
    k = 2 if double else 1; cols = n * k; cw = (w - 40) / cols
    for i in range(cols):
        x = 20 + cw * (i + 0.5); y = h * 0.84; hh = min(h * 0.36, cw * 1.2)
        o.append(f'<path d="M{f(x - cw * 0.34)} {f(y - hh)} L {f(x + cw * 0.34)} {f(y - hh)} L {f(x + cw * 0.28)} {f(y)} L {f(x - cw * 0.28)} {f(y)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<ellipse cx="{f(x)}" cy="{f(y - hh)}" rx="{f(cw * 0.34)}" ry="6" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    o.append(label(w / 2, h * 0.96, ("TWO OMERS FOR EACH ONE" if double else "AN OMER A HEAD"), "#FFD23F", 11))
    return "".join(o)

def worms(w, h, seed):
    """It bred worms, and became foul: a jar of yesterday's manna gone grey, worms crawling over the rim, flies above."""
    r = random.Random(seed); cx, b = w * 0.5, h * 0.92; jw, jh = min(w * 0.36, h * 0.46), min(h * 0.4, w * 0.3)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A3A2A"></rect>', ground(w, h, b, "#4A3A2A", dy=0),
         f'<path d="M{f(cx - jw / 2)} {f(b - jh)} L {f(cx + jw / 2)} {f(b - jh)} L {f(cx + jw * 0.4)} {f(b)} L {f(cx - jw * 0.4)} {f(b)} Z" fill="#8A5A3E" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<ellipse cx="{f(cx)}" cy="{f(b - jh)}" rx="{f(jw / 2)}" ry="10" fill="#8A8A6A" stroke="#0D0D0F" stroke-width="2"></ellipse>']
    for _ in range(9):
        x = cx + r.uniform(-jw * 0.45, jw * 0.45); y = b - jh + r.uniform(-4, 30)
        o.append(f'<path d="M{f(x)} {f(y)} c 4 -6 8 6 12 0 c 4 -6 8 6 12 0" fill="none" stroke="#E8E2D6" stroke-width="3.4" stroke-linecap="round"></path>')
    o.append(E2.swarm(12, cx, b - jh - 40, jw * 0.6, 30, seed, smin=0.4, smax=0.7))
    return "".join(o)

def melted(w, h, seed, p=None, people=0):
    """When the sun waxed hot, it melted: the white flakes running to nothing under a hard noon sun; people = searchers who find none."""
    r = random.Random(seed); b = h * 0.4
    o = [sun(w * 0.5, h * 0.16, 22, color="#FFF4C2", op=0.5), ground(w, h, b, "#E8C88A", dy=0)]
    o += [f'<ellipse cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(b + 10, h))}" rx="{f(r.uniform(3, 9))}" ry="1.6" fill="#F3EFE6" opacity="0.6"></ellipse>' for _ in range(60)]
    o += [f'<path d="M{f(x)} {f(b + 30)} c 6 -10 -6 -20 0 -30" fill="none" stroke="#FFF4C2" stroke-width="2" opacity="0.6"></path>' for x in [r.uniform(0, w) for _ in range(10)]]
    for i in range(people):
        x = w * (0.12 + i * 0.76 / max(1, people - 1)); y = h * 0.92
        o.append(man(p, x, y, fit(y, h * 0.44), r.choice(A.HEBREW), flip=i % 2 == 1, up=[(-22, -158), (-40, -126), (-58, -110)]) + E4.basket(x + (-30 if i % 2 else 30), y, 1.0))
    return "".join(o)

def sabbath_camp(w, h, seed):
    """So the people rested on the seventh day: the camp still, lamps in the tent doors, no one in the field."""
    b = h * 0.7
    o = [sun(w * 0.84, h * 0.2, 14, color="#FFE680", op=0.3), ground(w, h, b, "#E8D8B0", dy=0)]
    o += [A.black_tent(w * x, b + 6, w * 0.14, h * 0.2) for x in (0.1, 0.3, 0.5, 0.7, 0.9)]
    o.append(label(w * 0.5, h * 0.94, "THE SEVENTH DAY", "#5A3A22", 12))
    return "".join(o)

def pot(w, h, seed):
    """Take a pot, and put an omerful of manna therein, and lay it up before Jehovah: a golden pot, lid off, white manna within."""
    cx, b = w * 0.5, h * 0.86; pw, ph = min(w * 0.3, h * 0.6), min(w * 0.34, h * 0.6)
    return (V.rays(cx, b - ph * 0.6, 30, 20, max(w, h), color="#FFF4C2", op=0.25)
            + f'<path d="M{f(cx - pw / 2)} {f(b - ph)} C {f(cx - pw * 0.7)} {f(b - ph * 0.4)} {f(cx - pw * 0.5)} {f(b)} {f(cx)} {f(b)} C {f(cx + pw * 0.5)} {f(b)} {f(cx + pw * 0.7)} {f(b - ph * 0.4)} {f(cx + pw / 2)} {f(b - ph)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.6"></path>'
            + f'<ellipse cx="{f(cx)}" cy="{f(b - ph)}" rx="{f(pw / 2)}" ry="9" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></ellipse>'
            + f'<path d="M{f(cx - pw * 0.3)} {f(b - ph * 0.6)} L {f(cx + pw * 0.3)} {f(b - ph * 0.6)}" stroke="#FFF4C2" stroke-width="3" opacity="0.7"></path>')

def ephah(w, h, seed):
    """Now an omer is the tenth part of an ephah: a technical gauge, one ephah divided into ten omers."""
    o = [grid_bg(w, h)]
    x0, x1, y = 20, w - 20, h * 0.5; cw = (x1 - x0) / 10
    for i in range(10):
        o.append(f'<rect x="{f(x0 + i * cw + 2)}" y="{f(y - 24)}" width="{f(cw - 4)}" height="48" fill="{"#FFD23F" if i == 0 else "#12113A"}" stroke="#2C9DB8" stroke-width="1.6"></rect>')
    o.append(label(x0 + cw / 2, y + 44, "1 OMER", "#FFD23F", 10) + label((x0 + x1) / 2, y - 40, "1 EPHAH = 10 OMERS", "#8FD0E2", 12))
    return "".join(o)

def rephidim(p, w, h, seed, strive=False):
    """Rephidim, and there was no water: a dry camp among red rocks; with strive=True, the people pressing round Moses, stones in hand."""
    r = random.Random(seed); b = h * 0.9
    o = [sun(w * 0.86, h * 0.18, 18, color="#FFF4C2", op=0.4), hills(w, h, h * 0.5, seed, color="#8A3A2A", amp=20), ground(w, h, h * 0.5, "#C8682E", dy=0)]
    if strive:
        o.append(A.moses(p, w * 0.5, b, fit(b, h * 0.5)))
        for i, x in enumerate((0.14, 0.24, 0.34, 0.66, 0.76, 0.86)):
            o.append(man(p, w * x, b - (i % 2) * 6, fit(b, h * 0.56), r.choice(A.HEBREW), flip=x > 0.5, up=T.POSES["raise"] if i % 3 == 0 else T.POSES["point"]))
    else:
        o += [A.black_tent(w * x, h * 0.62, w * 0.1, h * 0.12) for x in (0.1, 0.24, 0.38, 0.62, 0.76)]
        o += [E2.kine_dead(w * 0.86, h * 0.8, 0.3)]
    return "".join(o)

def hill_top(p, w, h, seed, sitting=False):
    """Moses on the top of the hill with the rod of God: Aaron and Hur on either side holding up his hands, the stone under him."""
    b = h * 0.86; hx = w * 0.5
    o = [sun(hx, h * 0.5, 40, color="#FF8A3D", op=0.35), f'<path d="M-10 {f(h + 10)} C {f(w * 0.2)} {f(b - h * 0.04)} {f(w * 0.8)} {f(b - h * 0.04)} {f(w + 10)} {f(h + 10)} Z" fill="#4A2418" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = fit(b - h * 0.04, h * 0.42)
    if sitting:
        o.append(f'<rect x="{f(hx - 26 * s)}" y="{f(b - 70 * s)}" width="{f(52 * s)}" height="{f(30 * s)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(E4.figure_both(hx, b - (40 * s if sitting else 0), s, SKIN, A.MOSES_ROBE, [(-22, -158), (-44, -190), (-60, -222)], [(22, -158), (44, -190), (60, -222)], p + "hm")
             + f'<g transform="translate({f(hx)} {f(b - (40 * s if sitting else 0))}) scale({f(s)})">{A.headcloth("#E2D8C4")}{A.BLACK_BEARD}<path d="M60 -222 L 66 -300" stroke="#5A3A22" stroke-width="6" stroke-linecap="round"></path></g>')
    o.append(A.aaron(p, hx - 74 * s, b, s, up=[(-22, -158), (10, -186), (20, -210)] if sitting else None, flip=True) + hur(p, hx + 74 * s, b, s, up=[(-22, -158), (10, -186), (20, -210)] if sitting else None))
    return "".join(o)

def battle(p, w, h, seed, prevail="israel"):
    """Joshua fought with Amalek: two lines of spearmen clashing in the plain at Rephidim."""
    b = h * 0.92
    o = [sun(w * 0.5, h * 0.3, 30, color="#FF8A3D", op=0.3), ground(w, h, h * 0.44, "#8A5A3A", dy=0)]
    o.append(E4.warriors(p, 14, -10, w * 0.48, h * 0.5, b, seed, 0.22, 0.48, flip=False, body=SKIN, cloth=tuple(A.HEBREW[:4])))
    o.append(E4.warriors(p, 14, w * 0.52, w + 10, h * 0.5, b, seed + 1, 0.22, 0.48, flip=True, body="#3A1A10", cloth=("#5A1A16", "#3A1A1A", "#7A2A1E")))
    return "".join(o)

def book(w, h, seed):
    """Write this for a memorial in a book: an open scroll and a reed pen on a stone, by lamplight."""
    cx, cy = w * 0.5, h * 0.6; sw = min(w * 0.7, h * 1.4)
    return (f'<rect x="{f(cx - sw / 2)}" y="{f(cy - sw * 0.18)}" width="{f(sw)}" height="{f(sw * 0.36)}" fill="#F3E8D0" stroke="#0D0D0F" stroke-width="2.4"></rect>'
            + "".join(f'<ellipse cx="{f(cx + d * sw / 2)}" cy="{f(cy)}" rx="{f(sw * 0.04)}" ry="{f(sw * 0.2)}" fill="#C9A86A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>' for d in (-1, 1))
            + "".join(f'<path d="M{f(cx - sw * 0.4)} {f(cy - sw * 0.12 + i * sw * 0.05)} L {f(cx + sw * 0.4)} {f(cy - sw * 0.12 + i * sw * 0.05)}" stroke="#5A3A22" stroke-width="2" stroke-dasharray="{6 + i} 4" opacity="0.7"></path>' for i in range(6))
            + f'<path d="M{f(cx + sw * 0.3)} {f(cy - sw * 0.3)} L {f(cx + sw * 0.1)} {f(cy - sw * 0.02)}" stroke="#5A3A22" stroke-width="4"></path>')

def nissi(p, w, h, seed):
    """Moses built an altar, and called the name of it Jehovah-nissi (Jehovah is my banner): an altar of stones with the rod set up beside it."""
    b = h * 0.88
    return (sun(w * 0.76, h * 0.3, 30, color="#FF8A3D", op=0.3) + hills(w, h, b - 6, seed, color="#4A2418", amp=10) + ground(w, h, b, "#8A5A3A", dy=0)
            + A4.altar(w * 0.5, b, min(1.0, h / 320), seed=seed)
            + f'<path d="M{f(w * 0.66)} {f(b)} L {f(w * 0.66)} {f(b - h * 0.62)}" stroke="#5A3A22" stroke-width="6" stroke-linecap="round"></path>'
            + f'<path d="M{f(w * 0.66)} {f(b - h * 0.62)} L {f(w * 0.8)} {f(b - h * 0.56)} L {f(w * 0.66)} {f(b - h * 0.48)} Z" fill="#D7261E" stroke="#0D0D0F" stroke-width="2"></path>'
            + A.moses(p, w * 0.26, b, fit(b, h * 0.36), up=T.POSES["raise"]))

def family_coming(p, w, h, seed):
    """Jethro came with his sons and his wife unto Moses into the wilderness: Jethro leading, Zipporah on an ass, Gershom and Eliezer."""
    b = h * 0.88; s = fit(b, h * 0.44)
    return (sun(w * 0.86, h * 0.16, 16, op=0.25) + A.horeb(w, h, b, seed) + ground(w, h, b, "#C8A06A", dy=0)
            + A.jethro(p, w * 0.24, b, s) + A.N.mount(w * 0.44, b, round(s * 1.15, 3), rider_body=SKIN, rider_cloth=A.ZIPPORAH_ROBE, p=p)
            + T.figure(p, ("lad", "#C8A06A"), w * 0.6, b, fit(b, h * 0.52)) + T.figure(p, ("lad", "#E8E2D6"), w * 0.68, b, fit(b, h * 0.6))
            + A.moses(p, w * 0.86, b, s, flip=True, up=[(-22, -158), (4, -150), (30, -150)]))

def obeisance(p, w, h, seed):
    """Moses went out to meet his father-in-law, and did obeisance, and kissed him: the two embracing before the tent."""
    b = h * 0.88; s = fit(b, h * 0.36); arm = [(-22, -158), (4, -150), (30, -160)]
    return (sun(w * 0.86, h * 0.16, 16, op=0.25) + ground(w, h, b, "#C8A06A", dy=0) + A.black_tent(w * 0.22, b, w * 0.3, h * 0.32)
            + A.jethro(p, w * 0.56, b, s, up=arm) + A.moses(p, w * 0.64, b, s, flip=True, up=arm))

def feast(p, w, h, seed):
    """Aaron came, and all the elders of Israel, to eat bread with Moses' father-in-law before God: the altar smoking, a meal on a rug."""
    b = h * 0.9
    o = [A4.altar(w * 0.86, b, min(0.8, h / 360), seed=seed), ground(w, h, b, "#8A6A4A", dy=0),
         f'<rect x="{f(w * 0.1)}" y="{f(b - 10)}" width="{f(w * 0.6)}" height="16" fill="#7A2A3A" stroke="#0D0D0F" stroke-width="2"></rect>']
    o += [f'<ellipse cx="{f(w * (0.16 + i * 0.1))}" cy="{f(b - 12)}" rx="16" ry="6" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></ellipse>' for i in range(6)]
    cast = [(A.jethro, 0.12, 0.36), (A.aaron, 0.24, 0.38), (A.moses, 0.36, 0.36)] + [(A.elder(c, i), 0.48 + i * 0.08, 0.4, True) for i, c in enumerate(A.HEBREW[:3])]
    o += [T.figure(p, c[0], w * c[1], b - 12, fit(b - 12, h * c[2]), flip=c[3] if len(c) > 3 else False) for c in cast]
    return "".join(o)

def judging(p, w, h, seed):
    """Moses sat to judge the people: Moses on a seat before his tent, a press of people standing about him from morning unto evening."""
    r = random.Random(seed); b = h * 0.9
    o = [sun(w * 0.9, h * 0.4, 20, color="#FF8A3D", op=0.3), ground(w, h, b, "#C8A06A", dy=0), A.black_tent(w * 0.14, b, w * 0.26, h * 0.32),
         f'<rect x="{f(w * 0.24)}" y="{f(b - 50)}" width="40" height="50" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></rect>']
    o.append(A.moses(p, w * 0.27, b - 30, min(fit(b - 30, h * 0.36), w / 800), flip=True, up=T.POSES["point"]))
    items = sorted((r.uniform(b - h * 0.2, b + 4), r.uniform(w * 0.36, w * 1.02)) for _ in range(22))
    for y, x in items:
        s = min(fit(y, y - h * 0.42), w / 900) * (0.7 + 0.3 * (y - (b - h * 0.2)) / (h * 0.2))
        o.append((man if r.random() < 0.6 else woman)(p, x, y, s, r.choice(A.HEBREW + ["#5A6E8A", "#C2456A"]), flip=True))
    return "".join(o)

def rulers(w, h, seed):
    """Rulers of thousands, rulers of hundreds, rulers of fifties, and rulers of tens: a technical chart of the judges set over the people."""
    o = [grid_bg(w, h)]
    tiers = [("MOSES · THE HARD CAUSES", 1, "#FFD23F"), ("THOUSANDS", 3, "#D7261E"), ("HUNDREDS", 6, "#8FD0E2"), ("FIFTIES", 10, "#9CCB5E"), ("TENS", 16, "#F3EFE6")]
    for i, (nm, n, c) in enumerate(tiers):
        y = h * (0.12 + i * 0.19); span = w * (0.06 + 0.13 * i)
        for k in range(n):
            x = w * 0.42 - span / 2 + (span * (k + 0.5) / n)
            o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(max(3, 8 - i))}" fill="{c}" stroke="#0D0D0F" stroke-width="1.2"></circle>')
            if i: o.append(f'<path d="M{f(x)} {f(y - 6)} L {f(w * 0.42)} {f(y - h * 0.15)}" stroke="{c}" stroke-width="0.8" opacity="0.4"></path>')
        o.append(label(w * 0.02, y + 4, nm, c, 9, "start"))
    return "".join(o)
