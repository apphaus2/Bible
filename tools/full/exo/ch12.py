"""Exodus volume, Chapter 12 — The Glory (Exodus 39–40), the end of Exodus. Every verse, word for word from ref/asv.
The holy garments made (39:1–31) and the rearing up of the tabernacle (40:17–33) are blueprint pages (kit.blueprints);
the chapter ends on two story pages: the cloud covering the tent and the glory filling it."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus3 as E3, exodus4 as E4, exodus5 as V
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god
from reuse import panels
from exo import G, art as A, art8 as B8, art9 as Q, art11 as N
from exo.kit import blueprints
from exo.ch11 import chunks, nar
from genesis.ch02 import rows, W1, W2, NIGHT
from mk import defs

v, sp = G.v, G.span
TN, = [panels("digest/exodus/book-05/" + n + ".dc.html") for n in ["EX5-P08-Tabernacle"]]
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
START = 195                                  # chapter 11 ends on page 194
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def S(scene, p): return lambda w, h: scene(p, w, h, len(p) * 89)

def _blessing(p, w, h, seed):
    """Moses saw all the work, and, behold, they had done it: and Moses blessed them — Moses, hands raised, by the finished pieces."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), B8.bp(w, h), f'<path d="M{w * 0.5:.1f} {b:.1f} L {w:.1f} {b:.1f}" stroke="{B8.CY}" stroke-width="1.6"></path>',
         B8.box(w * 0.66, b, w * 0.06, w * 0.04, w * 0.04, fill=B8.GOLD, top="#FFD23F", side="#C8981E"), Q.laver_shape(w * 0.78, b, 0.5),
         B8.box(w * 0.86, b, w * 0.07, w * 0.07, w * 0.04, fill=B8.BRASS, top="#D8935A", side="#8A5222")]
    s = min(1.2, (b - h * 0.3) / 205)
    o.append(A.moses(p, w * 0.58, b, s, up=[(-22, -158), (-30, -196), (-36, -232)]))
    return "".join(o)

def camp(p, w, h, seed, moving=False):
    """The camp about the tabernacle under the cloud; moving=True, the cloud taken up and the people going onward."""
    import random
    from genesis.art2 import ground, fit
    from genesis.art3 import sun
    from genesis import art3 as Z
    b = h * 0.9
    o = [mk.defs(p, *ALL), E4.sinai(w * 0.2, h * 0.56, w * 0.4, h * 0.44, seed, fire=False), ground(w, h, h * 0.56, "#8A6A4A", dy=0)]
    if moving:
        o.append(E3.pillar_cloud(w * 0.82, h * 0.6, -20, w * 0.06, seed) + Z.caravan(p, w * 0.1, w * 0.74, h * 0.82, 0.3, seed, flip=False))
    else:
        o.append(V.tabernacle(w * 0.6, h * 0.76, w * 0.4, uid=p + "t") + E3.pillar_cloud(w * 0.62, h * 0.6, -20, w * 0.06, seed))
        o += [A.black_tent(w * x, b, w * 0.1, h * 0.14) for x in (0.08, 0.2, 0.92)]
    return "".join(o)

def cloud_tent(w, h, seed, night=False):
    """The cloud covered the tent of meeting (by night, fire therein): the tabernacle in its court under the pillar."""
    from genesis.art2 import ground
    o = [mk.stars(60, w, h * 0.5, seed) if night else "", V.rays(w * 0.5, h * 0.3, 36, 20, max(w, h), color="#FFF4C2", op=0.3), ground(w, h, h * 0.84, "#4A3A3E" if night else "#8A6A4A", dy=0),
         V.tabernacle(w * 0.5, h * 0.9, w * 0.66, uid=f"ct{seed}")]
    o.append(E3.pillar_fire(w * 0.52, h * 0.6, -20, w * 0.07, seed) if night else E3.pillar_cloud(w * 0.52, h * 0.62, -20, w * 0.1, seed))
    return "".join(o)

def bringing(w, h):
    """They brought the tabernacle unto Moses: the list of 39:33–41 as a checklist, every piece ticked."""
    return Q.works(w, h)

ITEMS = [
    *chunks("39:1-7", lambda w, h: Q.ephod(w, h, stones=True), "The Holy Garments for Aaron"),
    *chunks("39:8-14", Q.breastplate, "The Breastplate"),
    *chunks("39:15-21", lambda w, h: Q.breastplate(w, h, names=False, rings=True), None),
    *chunks("39:22-26", Q.robe, "The Robe of the Ephod"),
    *chunks("39:27-31", Q.plate, "Holy to Jehovah"),
    *chunks("39:32-42", bringing, "Thus Was Finished All the Work"),
    ("39:43", nar("39:43"), S(_blessing, "m1"), None),
    ("40:1–8", [("cap", v("40:1")), ("god", sp("40:2-8"))], lambda w, h: B8.frame_plan(w, h, veil=True, furniture=True, screen=True), "Thou Shalt Rear Up the Tabernacle"),
    ("40:9–11", [("god", sp("40:9-11"))], Q.anointed, None),
    ("40:12–15", [("god", sp("40:12-15"))], lambda w, h: Q.dressing(w, h, oil=True), None),
    ("40:16", nar("40:16"), lambda w, h: Q.dressing(w, h, oil=True), None),
    *chunks("40:17-21", lambda w, h: B8.frame_plan(w, h, bars=True, veil=True), "The Tabernacle Was Reared Up"),
    *chunks("40:22-27", lambda w, h: B8.frame_plan(w, h, veil=True, furniture=True), None),
    *chunks("40:28-33", B8.court, None),
]


@P("EXO-C12-00-Title", "Chapter 12 · The Glory")
def title():
    a = TN[3]
    return chapter_title(12, "第十二話", "The Glory", "Exodus 39 – 40", f'<g transform="translate(-340 120) scale(2.1)">{a.svg}</g>', a.bg,
                         v("40:34"), "Exodus · Volume Two")

PAGES += blueprints(ITEMS, "EXO-C12", START, "The Glory")
_N = START + len(PAGES) - 1


@P(f"EXO-C12-P{len(PAGES):02d}-Glory", f"{_N} · The Glory of Jehovah Filled the Tabernacle")
def glory():
    t, h = rows(560, None)
    r1 = new("linear-gradient(180deg, #2A1A5E 0%, #8A6AB8 60%, #FFE3B8 100%)", W1, h[0], cloud_tent(W1, h[0], 1290), cap(v("40:34"), "left: 12px; top: 12px", size=14, maxw=440) + vref("EX 40:34", "right: 12px; bottom: 12px"))
    r2 = new("linear-gradient(180deg, #FFF4C2 0%, #FFD23F 60%, #FF8A3D 100%)", W1, h[1],
             V.rays(W1 * 0.7, h[1] * 0.3, 36, 20, W1, color="#FFFFFF", op=0.5) + V.tabernacle(W1 * 0.7, h[1] * 0.92, W1 * 0.5, uid="glz") + E3.pillar_cloud(W1 * 0.7, h[1] * 0.6, -20, W1 * 0.08, 1291).replace("#E8E2D6", "#FFFFFF")
             + defs("glm", *ALL) + A.moses("glm", W1 * 0.3, h[1] * 0.92, 0.9),
             cap(v("40:35"), "left: 12px; top: 12px", size=13, maxw=380) + vref("EX 40:35", "right: 12px; bottom: 12px"))
    return page("Exodus 40:34–35 — The Glory of Jehovah Filled the Tabernacle", t, r1 + r2, _N)


@P(f"EXO-C12-P{len(PAGES):02d}-Journeys", f"{_N + 1} · Throughout All Their Journeys")
def journeys():
    t, h = rows(330, None)
    r1 = cols(new("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", W2, h[0], camp("jm1", W2, h[0], 1301, moving=True), cap(v("40:36"), "left: 8px; top: 8px", size=12, maxw=320) + vref("EX 40:36", "right: 8px; bottom: 8px")),
              new("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", W2, h[0], camp("jm2", W2, h[0], 1302), cap(v("40:37"), "left: 8px; top: 8px", size=12, maxw=320) + vref("EX 40:37", "right: 8px; bottom: 8px")))
    r2 = new(NIGHT, W1, h[1], cloud_tent(W1, h[1], 1303, night=True), cap(v("40:38"), "left: 12px; top: 12px", size=14, maxw=460)
             + end_mark("END OF EXODUS · NEXT · LEVITICUS", "right: 14px; bottom: 12px", ch="完") + vref("EX 40:38", "left: 12px; bottom: 12px"))
    return page("Exodus 40:36–38 — Throughout All Their Journeys", t, r1 + r2, _N + 1)
