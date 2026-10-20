"""Leviticus volume, Chapter 3 — Strange Fire (Leviticus 9–11). Every verse, word for word from ref/eng-asv.
The eighth day and Nadab and Abihu (9–10) as story pages; the clean and the unclean (11) as law cells."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus5 as V
from fx import new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from exo import art as A, art8 as B8, art9 as Q
from exo.kit import law_pages, set_book, talk
from lev import G, art as L, art3 as K
from genesis.ch02 import rows, W1, W2, NIGHT, SKY, DUSK
from genesis.ch03 import SAND
from genesis.ch04 import EMBER, COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED, BLUE

v, sp = G.v, G.span
set_book(G)
from lev import ch02 as _prev
START = _prev.START + len(_prev.PAGES) - 1     # straight after the previous chapter (its title page is unnumbered)
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco
FIRE = "linear-gradient(180deg, #2A0A0A 0%, #8A1E16 60%, #FF8A3D 100%)"
COURT = "linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)"

def after(ref, to):
    """The rest of a verse after the words `to` (for the speech that follows "and said,")."""
    t = v(ref); return v(ref, frm=t[t.index(to) + len(to):].strip())


@P("LEV-C03-00-Title", "Chapter 3 · Strange Fire")
def title():
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A0A0A"></rect>' + K.censers_fallen(760, 1080, 301)
    return chapter_title(3, "第三話", "Strange Fire", "Leviticus 9 – 11", svg, FIRE, v("10:3", frm="I will be sanctified", to="glorified."), "Leviticus · Volume Three")


@P("LEV-C03-P01-EighthDay", "33 · On the Eighth Day")
def p01():
    t, h = rows(300, 360, None)
    r1 = new(COURT, W1, h[0], K.court("k1a", W1, h[0], 311, cast=[(A.moses, 0.16, 0.42, False, "raise"), (K.hp, 0.28, 0.44, True), (K.sp, 0.7, 0.5, True), (K.sp, 0.78, 0.5, True),
                                                                   (A.elder("#5A3A22", 1), 0.88, 0.48, True), (A.elder("#4A3A6A", 3), 0.96, 0.48, True)]),
             cap(v("9:1"), "left: 12px; top: 12px", size=11.5, maxw=420) + mk.stamp(9, "right: 14px; top: 12px") + vref("LEV 9:1", "right: 12px; bottom: 12px"))
    r2 = talk(K.MOSES_CALM, h[1], GOLDEN, [("cap", v("9:2", to="and he said unto Aaron,")), ("say", after("9:2", "unto Aaron,") + " " + v("9:3") + " " + v("9:4"))], ref="LEV 9:2–4", size=14)
    r3 = new(SAND, W1, h[2], K.offerings_row(W1, h[2], 313), vref("LEV 9:2–4", "right: 12px; bottom: 12px"))
    return page("Leviticus 9:1–4 — On the Eighth Day", t, r1 + r2 + r3, START + 0)


@P("LEV-C03-P02-Draw", "34 · Draw Near unto the Altar")
def p02():
    t, h = rows(300, 240, None)
    r1 = new(COURT, W1, h[0], K.court("k2a", W1, h[0], 321, people=12), cap(v("9:5"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("LEV 9:5", "right: 12px; bottom: 12px"))
    r2 = talk(K.MOSES_CALM, h[1], GOLDEN, [("cap", v("9:6", to="And Moses said,")), ("say", after("9:6", "Moses said,"))], ref="LEV 9:6", size=15)
    r3 = talk(K.MOSES, h[2], GOLDEN, [("cap", v("9:7", to="unto Aaron,")), ("say", after("9:7", "unto Aaron,"))], ref="LEV 9:7", size=15)
    return page("Leviticus 9:5–7 — Draw Near unto the Altar", t, r1 + r2 + r3, START + 1)


@P("LEV-C03-P03-Offered", "35 · Aaron Drew Near unto the Altar")
def p03():
    t, h = rows(None, 470)
    cast = [(K.hp, 0.36, 0.4, False, L.REACH), (K.sp, 0.6, 0.48, True), (K.sp, 0.7, 0.48, True)]
    r1 = new(COURT, W1, h[0], K.court("k3a", W1, h[0], 331, cast=cast), cap(v("9:8") + " " + v("9:9") + " " + v("9:10") + " " + v("9:11"), "left: 12px; top: 12px", size=11, maxw=440) + vref("LEV 9:8–11", "right: 12px; bottom: 12px"))
    r2 = new(COURT, W1, h[1], K.court("k3b", W1, h[1], 332, cast=cast), cap(v("9:12") + " " + v("9:13") + " " + v("9:14"), "left: 12px; top: 12px", size=11, maxw=440) + vref("LEV 9:12–14", "right: 12px; bottom: 12px"))
    return page("Leviticus 9:8–14 — Aaron Drew Near unto the Altar", t, r1 + r2, START + 2)


@P("LEV-C03-P04-People", "36 · The People's Oblation")
def p04():
    t, h = rows(None, 470)
    cast = [(K.hp, 0.36, 0.4, False, L.REACH), (K.sp, 0.6, 0.48, True), (K.sp, 0.7, 0.48, True)]
    r1 = new(COURT, W1, h[0], K.court("k4a", W1, h[0], 341, cast=cast, people=6), cap(v("9:15") + " " + v("9:16") + " " + v("9:17"), "left: 12px; top: 12px", size=11, maxw=440) + vref("LEV 9:15–17", "right: 12px; bottom: 12px"))
    r2 = new(COURT, W1, h[1], K.court("k4b", W1, h[1], 342, cast=[(K.hp, 0.36, 0.4, False, K.BOTH), (K.sp, 0.6, 0.48, True)]),
             cap(v("9:18") + " " + v("9:19") + " " + v("9:20") + " " + v("9:21"), "left: 12px; top: 12px", size=11, maxw=440) + vref("LEV 9:18–21", "right: 12px; bottom: 12px"))
    return page("Leviticus 9:15–21 — The People's Oblation", t, r1 + r2, START + 3)


@P("LEV-C03-P05-Fire", "37 · There Came Forth Fire")
def p05():
    t, h = rows(250, None)
    r1 = cols(new(COURT, W2, h[0], K.court("k5a", W2, h[0], 351, cast=[(K.hp, 0.5, 0.4, False, K.BOTH)], people=6), cap(v("9:22"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("LEV 9:22", "right: 8px; bottom: 8px")),
              new(COURT, W2, h[0], K.court("k5b", W2, h[0], 352, cast=[(A.moses, 0.3, 0.44, False, "raise"), (K.hp, 0.42, 0.44)], glory=True), cap(v("9:23"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("LEV 9:23", "right: 8px; bottom: 8px")))
    r2 = new(FIRE, W1, h[1], K.fire_falls("k5c", W1, h[1], 353), cap(v("9:24"), "left: 12px; top: 12px", size=13, maxw=440)
             + sfx("ゴオオッ", "GOOO!", "right: 30px; top: 30px", size=54, fill="#FFD23F", stroke="#8A0E16", rot=-6) + vref("LEV 9:24", "right: 12px; bottom: 12px"))
    return page("Leviticus 9:22–24 — There Came Forth Fire", t, r1 + r2, START + 4)


@P("LEV-C03-P06-Strange", "38 · Strange Fire before Jehovah")
def p06():
    t, h = rows(330, 290, None)
    r1 = new(COURT, W1, h[0], K.strange_fire("k6a", W1, h[0], 361), cap(v("10:1"), "left: 12px; top: 12px", size=11.5, maxw=440) + mk.stamp(10, "right: 14px; top: 12px") + vref("LEV 10:1", "right: 12px; bottom: 12px"))
    r2 = new(FIRE, W1, h[1], K.censers_fallen(W1, h[1], 362), cap(v("10:2"), "left: 12px; top: 12px", size=13, maxw=440) + vref("LEV 10:2", "right: 12px; bottom: 12px"))
    r3 = cols(talk(K.MOSES_STERN, h[2], RED, [("cap", v("10:3", to="unto Aaron,")), ("say", v("10:3", frm="This is it", to="glorified."))], w=W2, ref="LEV 10:3", size=12),
              new(COLD, W2, h[2], mk.face(K.AARON_GRIEF, W2 + 40, h[2] - 380 * min(1, (h[2] + 10) / 380) + 8, min(1, (h[2] + 10) / 380), flip=True), cap(v("10:3", frm="And Aaron held"), "left: 8px; top: 8px", size=12, maxw=180)))
    return page("Leviticus 10:1–3 — Strange Fire before Jehovah", t, r1 + r2 + r3, START + 5)


@P("LEV-C03-P07-Coats", "39 · Carried in Their Coats")
def p07():
    t, h = rows(230, 260, None)
    r1 = talk(K.MOSES_STERN, h[0], RED, [("cap", v("10:4", to="and said unto them,")), ("say", after("10:4", "said unto them,"))], ref="LEV 10:4", size=14)
    r2 = new(DUSK, W1, h[1], K.carried("k7b", W1, h[1], 372), cap(v("10:5"), "left: 12px; top: 12px", size=12, maxw=380) + vref("LEV 10:5", "right: 12px; bottom: 12px"))
    r3 = talk(K.MOSES_STERN, h[2], RED, [("cap", v("10:6", to="his sons,")), ("say", after("10:6", "his sons,") + " " + v("10:7", to="upon you.")), ("cap", v("10:7", frm="And they did"))], ref="LEV 10:6–7", size=13)
    return page("Leviticus 10:4–7 — Carried in Their Coats", t, r1 + r2 + r3, START + 6)


@P("LEV-C03-P08-Wine", "40 · Drink No Wine nor Strong Drink")
def p08():
    t, h = rows(300, None)
    r1 = new(NIGHT, W1, h[0], K.wine(W1, h[0], 381), cap(v("10:8"), "left: 12px; top: 12px", size=11) + god(v("10:9") + " " + v("10:10") + " " + v("10:11"), "left: 12px; top: 48px", size=15, maxw=380) + vref("LEV 10:8–11", "right: 12px; bottom: 12px"))
    r2 = talk(K.MOSES_CALM, h[1], GOLDEN, [("cap", v("10:12", to="his sons that were left,")), ("say", after("10:12", "that were left,") + " " + v("10:13") + " " + v("10:14") + " " + v("10:15"))], ref="LEV 10:12–15", size=12.5)
    return page("Leviticus 10:8–15 — Drink No Wine nor Strong Drink", t, r1 + r2, START + 7)


@P("LEV-C03-P09-Goat", "41 · Behold, It Was Burnt")
def p09():
    t, h = rows(250, None, 290)
    r1 = new(DUSK, W1, h[0], K.goat_burnt(W1, h[0], 391), cap(v("10:16", to="saying,"), "left: 12px; top: 12px", size=11.5, maxw=420) + vref("LEV 10:16", "right: 12px; bottom: 12px"))
    r2 = talk(K.MOSES_STERN, h[1], RED, [("say", v("10:17") + " " + v("10:18"))], ref="LEV 10:17–18", size=14.5)
    r3 = cols(talk(K.AARON_GRIEF, h[2], COLD, [("cap", v("10:19", to="unto Moses,")), ("say", after("10:19", "unto Moses,"))], w=W2, ref="LEV 10:19", size=11),
              talk(K.MOSES_CALM, h[2], GOLDEN, [("cap", v("10:20"))], w=W2, flip=True, ref="LEV 10:20"))
    return page("Leviticus 10:16–20 — Behold, It Was Burnt", t, r1 + r2 + r3, START + 8)


SAY2 = "And Jehovah spake unto Moses and to Aaron, saying unto them,"
LAWS = [
    ("CLOVEN AND CHEWETH THE CUD", "11:1-3", K.pg_beasts_clean, SAY2, "The Living Things Which Ye May Eat"),
    ("THE CAMEL", "11:4", K.pg_camel, "", None),
    ("THE CONEY · THE HARE", "11:5-6", K.pg_coney_hare, "", None),
    ("THE SWINE", "11:7-8", K.pg_swine, "", None),
    ("FINS AND SCALES", "11:9-10", K.pg_fins, "", "In the Waters"),
    ("AN ABOMINATION", "11:11-12", K.pg_fins, "", None),
    ("AMONG THE BIRDS", "11:13-16", K.pg_birds, "", "Among the Birds"),
    ("THE OWL · THE STORK · THE BAT", "11:17-19", K.pg_bat, "", None),
    ("WINGED CREEPING THINGS", "11:20-23", K.pg_locusts, "", None),
    ("UNTIL THE EVEN", "11:24-25", K.pg_wash_even, "", "Unclean until the Even"),
    ("ON PAWS", "11:26-28", K.pg_paws, "", None),
    ("THAT CREEP UPON THE EARTH", "11:29-31", K.pg_creeping, "", None),
    ("ANY VESSEL", "11:32-33", K.pg_vessels, "", None),
    ("FOOD · DRINK · OVEN", "11:34-35", K.pg_oven_broken, "", None),
    ("A FOUNTAIN · SOWING SEED", "11:36-38", K.pg_fountain, "", None),
    ("THE CARCASS", "11:39-40", K.pg_carcass, "", None),
    ("UPON THE BELLY", "11:41-43", K.pg_belly, "", "Be Ye Holy"),
    ("I AM HOLY", "11:44-45", K.pg_holy, "", None),
    ("THE LAW OF THE BEAST", "11:46-47", K.pg_distinction, "", None),
]
PAGES += law_pages(LAWS, "LEV-C03-L", START + 9, "The Clean and the Unclean", end=end_mark("NEXT · THE PLAGUE OF LEPROSY", "right: 10px; top: 10px"))
