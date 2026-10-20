"""Exodus volume, Chapter 7 — The Book of the Covenant (Exodus 22–24). Every verse, word for word from ref/eng-asv.
The ordinances of 22:1–23:19 are five pages of law cells (kit.law) with pictograms from art7."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from exo import G, art as A, art6 as S6, art7 as L7
from exo.kit import talk, law
from exo.ch02 import night
from exo.ch06 import MOUNT, pic
from genesis import art as X, art2 as Y, art3 as Z, art10 as T
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from mk import defs, face

v, sp = G.v, G.span
CU, = [panels("reference/exodus/book-05/" + n + ".dc.html") for n in ["EX5-P01-ComeUp"]]
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
CELL = 326                                   # a cell's height on a page of three rows of law cells
START = 113                                  # chapter 6 ends on page 112
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def laws(title, num, cells):
    """A page of six law cells (three rows of two). cells: (heading, refs, pictogram fn); refs like "22:2-3" or "22:1"."""
    out = []
    for i, (hd, refs, fn) in enumerate(cells):
        c, vs = refs.split(":"); a, _, b = vs.partition("-")
        text = sp(refs); lab = f"EX {c}:{a}" + (f"–{b}" if b else "")
        out.append(law(hd, text, lab, pic(fn, f"z{num}{i}"), cell=CELL))
    return page(title, "minmax(0, 1fr)", grid(out, "repeat(3, minmax(0, 1fr))"), num)


@P("EXO-C07-00-Title", "Chapter 7 · The Book of the Covenant")
def title():
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B0B2A"></rect>' + defs("tt7", *ALL) + L7.sapphire("tt7", 760, 1080, 701)
    return chapter_title(7, "第七話", "The Book of the Covenant", "Exodus 22 – 24", svg, NIGHT,
                         v("24:8", frm="Behold the blood", to="all these words."), "Exodus · Volume Two")


@P("EXO-C07-P01-Restitution", "113 · He Shall Make Restitution")
def p01():
    return laws("Exodus 22:1–7 — He Shall Make Restitution", START + 0,
                [("FIVE OXEN FOR AN OX", "22:1", L7.pg_restore), ("THE THIEF BY NIGHT", "22:2-3", L7.pg_night), ("FOUND ALIVE IN HIS HAND", "22:4", L7.pg_double),
                 ("A BEAST LET LOOSE", "22:5", L7.pg_field), ("IF FIRE BREAK OUT", "22:6", L7.pg_fire), ("DELIVERED TO KEEP", "22:7", L7.pg_deposit)])

@P("EXO-C07-P02-Trespass", "114 · For Every Matter of Trespass")
def p02():
    return laws("Exodus 22:8–17 — For Every Matter of Trespass", START + 1,
                [("THE THIEF NOT FOUND", "22:8", S6.pg_scales), ("BEFORE GOD", "22:9", S6.pg_scales), ("THE OATH OF JEHOVAH", "22:10-11", L7.pg_beast_kept),
                 ("STOLEN · TORN IN PIECES", "22:12-13", L7.pg_torn), ("IF A MAN BORROW", "22:14-15", L7.pg_borrow), ("THE DOWRY OF VIRGINS", "22:16-17", L7.pg_dowry)])

@P("EXO-C07-P03-Widow", "115 · The Widow and the Fatherless")
def p03():
    return laws("Exodus 22:18–31 — The Widow and the Fatherless", START + 2,
                [("SAVE UNTO JEHOVAH ONLY", "22:18-20", L7.pg_idols), ("THE SOJOURNER", "22:21", L7.pg_sojourner), ("WIDOW AND FATHERLESS", "22:22-24", L7.pg_widow),
                 ("NO INTEREST", "22:25", L7.pg_lend), ("THE GARMENT IN PLEDGE", "22:26-27", L7.pg_pledge), ("HOLY MEN UNTO ME", "22:28-31", L7.pg_firstfruits)])

@P("EXO-C07-P04-Justice", "116 · Thou Shalt Not Wrest Justice")
def p04():
    return laws("Exodus 23:1–9 — Thou Shalt Not Wrest Justice", START + 3,
                [("A FALSE REPORT", "23:1", L7.pg_witness), ("A MULTITUDE", "23:2-3", L7.pg_crowd), ("THINE ENEMY'S OX", "23:4-5", L7.pg_astray),
                 ("THE INNOCENT AND RIGHTEOUS", "23:6-7", S6.pg_scales), ("NO BRIBE", "23:8", L7.pg_bribe), ("THE HEART OF A SOJOURNER", "23:9", L7.pg_sojourner)])

@P("EXO-C07-P05-Feasts", "117 · Three Times in the Year")
def p05():
    return laws("Exodus 23:10–19 — Three Times in the Year", START + 4,
                [("THE SEVENTH YEAR", "23:10-11", L7.pg_fallow), ("THE SEVENTH DAY", "23:12", L7.pg_rest), ("NO MENTION OF OTHER GODS", "23:13", L7.pg_idols),
                 ("THE FEAST OF UNLEAVENED BREAD", "23:14-15", L7.pg_three), ("HARVEST AND INGATHERING", "23:16-17", L7.pg_three), ("THE FIRST OF THE FIRST-FRUITS", "23:18-19", L7.pg_kid)])


@P("EXO-C07-P06-Angel", "118 · I Send an Angel before Thee")
def p06():
    t, h = rows(330, 270, None)
    r1 = new(SAND, W1, h[0], defs("x76a", *ALL) + L7.angel_before("x76a", W1, h[0], 1181), god(v("23:20") + " " + v("23:21"), "left: 12px; top: 12px", size=17, maxw=560) + mk.stamp(23, "right: 14px; bottom: 12px") + vref("EX 23:20–21", "left: 12px; bottom: 12px"))
    r2 = new("#0B1A2E", W1, h[1], A.peoples_map(W1, h[1], 1182), god(v("23:22") + " " + v("23:23"), "right: 12px; top: 12px", size=14.5, maxw=300) + vref("EX 23:22–23", "left: 12px; top: 12px"))
    r3 = new(NIGHT, W1, h[2], S6.idols_no(W1, h[2], 1183), god(v("23:24") + " " + v("23:25"), "left: 12px; top: 12px", size=16, maxw=400) + vref("EX 23:24–25", "right: 12px; bottom: 12px"))
    return page("Exodus 23:20–25 — I Send an Angel before Thee", t, r1 + r2 + r3, START + 5)


@P("EXO-C07-P07-Hornet", "119 · By Little and Little")
def p07():
    t, h = rows(220, 250, 230, None)
    r1 = new(SKY, W1, h[0], A.milk_honey(None, W1, h[0], 1191), god(v("23:26") + " " + v("23:27"), "left: 12px; top: 12px", size=15, maxw=560) + vref("EX 23:26–27", "right: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], L7.hornets(W1, h[1], 1192), god(v("23:28"), "left: 12px; top: 12px", size=16, maxw=380) + vref("EX 23:28", "right: 12px; bottom: 12px"))
    r3 = new(SAND, W1, h[2], defs("x77c", *ALL) + A.crowd("x77c", W1, h[2], 1193, n=30),
             god(v("23:29") + " " + v("23:30"), "left: 12px; top: 12px", size=15, maxw=560) + vref("EX 23:29–30", "right: 12px; bottom: 12px"))
    r4 = new("#0B1A2E", W1, h[3], L7.borders(W1, h[3]), god(v("23:31") + " " + v("23:32") + " " + v("23:33"), "left: 50%; top: 40px; transform: translateX(-50%)", size=12.5, maxw=380) + vref("EX 23:31–33", "right: 12px; bottom: 12px"))
    return page("Exodus 23:26–33 — By Little and Little", t, r1 + r2 + r3 + r4, START + 6)


@P("EXO-C07-P08-TwelvePillars", "120 · Twelve Pillars")
def p08():
    t, h = rows(240, 250, None)
    r1 = new(MOUNT, W1, h[0], E4.sinai(W1 * 0.7, h[0], W1 * 0.6, h[0] * 0.9, 1201, fire=False), cap(v("24:1", to="unto Moses,"), "left: 12px; top: 12px", size=11)
             + god(v("24:1", frm="Come up") + " " + v("24:2"), "left: 12px; top: 48px", size=15, maxw=420) + mk.stamp(24, "right: 14px; bottom: 12px") + vref("EX 24:1–2", "left: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], defs("x78b", *ALL) + A.elders("x78b", W1, h[1], 1202, setting="sand", extra_cast=[(A.moses, 0.92, 0.5, True, "raise")], top=0.56),
             cap(v("24:3", to="and said,"), "left: 12px; top: 12px", size=11, maxw=460) + balloon(v("24:3", frm="All the words"), "left: 20px; top: 80px", 280, size=13, pad="14px 20px") + vref("EX 24:3", "right: 12px; bottom: 12px"))
    r3 = new(DAWN, W1, h[2], defs("x78c", *ALL) + L7.pillars12("x78c", W1, h[2], 1203), cap(v("24:4"), "left: 12px; top: 12px", size=11, maxw=420)
             + cap(v("24:5") + " " + v("24:6"), "right: 12px; bottom: 14px", size=11, maxw=300) + hud("12", "right: 14px; top: 12px", size=28) + vref("EX 24:4–6", "left: 12px; bottom: 12px"))
    return page("Exodus 24:1–6 — Twelve Pillars", t, r1 + r2 + r3, START + 7)


@P("EXO-C07-P09-Sapphire", "121 · A Paved Work of Sapphire Stone")
def p09():
    t, h = rows(250, 260, None)
    r1 = new(SAND, W1, h[0], defs("x79a", *ALL) + A.elders("x79a", W1, h[0], 1211, setting="sand", extra_cast=[(A.moses, 0.92, 0.5, True, "raise")], top=0.56),
             cap(v("24:7", to="and they said,"), "left: 12px; top: 12px", size=11, maxw=440) + balloon(v("24:7", frm="All that"), "left: 20px; top: 74px", 320, size=13, pad="14px 22px") + vref("EX 24:7", "right: 12px; bottom: 12px"))
    r2 = new(DAWN, W1, h[1], defs("x79b", *ALL) + L7.pillars12("x79b", W1, h[1], 1212, sprinkle=True), cap(v("24:8", to="and said,"), "left: 12px; top: 12px", size=11, maxw=300)
             + balloon(v("24:8", frm="Behold the blood"), "right: 12px; top: 12px", 300, size=13, pad="20px 24px") + vref("EX 24:8", "left: 12px; bottom: 12px"))
    r3 = new(NIGHT, W1, h[2], defs("x79c", *ALL) + L7.sapphire("x79c", W1, h[2], 1213), cap(v("24:9") + " " + v("24:10") + " " + v("24:11"), "left: 12px; top: 12px", size=11, maxw=560) + vref("EX 24:9–11", "right: 12px; bottom: 12px"))
    return page("Exodus 24:7–11 — A Paved Work of Sapphire Stone", t, r1 + r2 + r3, START + 8)


@P("EXO-C07-P10-FortyDays", "122 · Forty Days and Forty Nights")
def p10():
    t, h = rows(220, 230, 250, None)
    r1 = use(CU[0], over=cap(v("24:12", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("24:12", frm="Come up"), "left: 12px; top: 48px", size=15, maxw=560) + vref("EX 24:12", "right: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], defs("x710b", *ALL) + L7.tarry("x710b", W1, h[1], 1222), cap(v("24:13"), "right: 12px; top: 12px", size=10.5, maxw=260)
             + cap(v("24:14", to="unto the elders,"), "left: 12px; top: 12px", size=10.5) + balloon(v("24:14", frm="Tarry ye"), "left: 12px; top: 46px", 330, size=11.5, pad="16px 22px") + vref("EX 24:13–14", "right: 12px; bottom: 12px"))
    r3 = use(CU[1], over=cap(v("24:15") + " " + v("24:16"), "left: 12px; top: 12px", size=11, maxw=420) + cap(v("24:17"), "left: 12px; bottom: 14px", size=11, maxw=380) + vref("EX 24:15–17", "right: 12px; bottom: 12px"))
    r4 = use(CU[2], over=cap(v("24:18"), "left: 12px; top: 12px", size=12, maxw=420) + hud("40 DAYS · 40 NIGHTS", "right: 14px; top: 14px", size=20)
             + end_mark("NEXT · THE PATTERN OF THE TABERNACLE", "left: 12px; bottom: 12px") + vref("EX 24:18", "right: 12px; bottom: 12px"))
    return page("Exodus 24:12–18 — Forty Days and Forty Nights", t, r1 + r2 + r3 + r4, START + 9)
