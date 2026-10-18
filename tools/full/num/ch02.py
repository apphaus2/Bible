"""Numbers volume, Chapter 2 — The Charge of the Levites (Numbers 3–4). Every verse, word for word from ref/asv.
Numbers 3: the sons of Aaron, the Levites given to Aaron instead of the first-born, the three families with their places
about the tabernacle (a plan) and their charges, and the redemption of the 273. Numbers 4: the holy things wrapped for the
journey and the burdens of Gershon and Merari (blueprint plates, exo.kit.blueprints), and the numbering from thirty
years old to fifty as tally cells. Page numbers are given in reading order by P() (see num.pages)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cols, cap, god
from exo import art as A, art8 as B8
from exo.kit import blueprints
from lev import art3 as L3
from num import G, art as K, art2 as K2
from num.pages import Pages
from num.ch01 import tally
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY
from genesis.ch03 import SAND, hud, clan
from num import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)   # straight after the previous chapter (its title page is unnumbered)
START, PAGES, P = PG.start, PG.pages, PG.P
INK = B8.INK
GC, KC, MC = K2.LEVI_C["GERSHON"], K2.LEVI_C["KOHATH"], K2.LEVI_C["MERARI"]
FIRE = "linear-gradient(180deg, #2A0A0A 0%, #8A1E16 60%, #FF8A3D 100%)"

def night(h, over): return new(NIGHT, W1, h, X.cosmic(W1, h), over)


@P("NUM-C02-00-Title", "Chapter 2 · The Charge of the Levites", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2A1A"></rect>' + f'<g transform="translate(0 360)">{K2.bearers("t2", 760, 720, 201)}</g>'
    return chapter_title(2, "第二話", "The Charge of the Levites", "Numbers 3 – 4", svg, SAND,
                         v("3:12", frm="the Levites shall be mine:"), "Numbers · Volume Four")


@P("NUM-C02-P01-Generations", "The Generations of Aaron and Moses")
def p01(n):
    t, h = rows(400, None)
    r1 = new(SAND, W1, h[0], K2.aaron_sons("m1a", W1, h[0], 211),
             cap(sp("3:1-3"), "left: 12px; top: 12px", size=12, maxw=470) + mk.stamp(3, "right: 14px; top: 12px") + vref("NUM 3:1–3", "right: 12px; bottom: 12px"))
    r2 = new(FIRE, W1, h[1], L3.censers_fallen(W1, h[1], 212), cap(v("3:4"), "left: 12px; top: 12px", size=13, maxw=460) + vref("NUM 3:4", "right: 12px; bottom: 12px"))
    return page("Numbers 3:1–4 — The Generations of Aaron and Moses", t, r1 + r2, n)


@P("NUM-C02-P02-Given", "Wholly Given unto Him")
def p02(n):
    t, h = rows(None, 360)
    r1 = night(h[0], cap(v("3:5"), "left: 12px; top: 12px", size=11) + god(sp("3:6-8"), "left: 12px; top: 50px", size=18, maxw=600) + vref("NUM 3:5–8", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], K.levites_round("m2b", W1, h[1], 222), god(sp("3:9-10"), "left: 12px; top: 12px", size=16, maxw=520) + vref("NUM 3:9–10", "right: 12px; bottom: 12px"))
    return page("Numbers 3:5–10 — Wholly Given unto Him", t, r1 + r2, n)


@P("NUM-C02-P03-Mine", "All the First-born Are Mine")
def p03(n):
    t, h = rows(470, None)
    r1 = night(h[0], cap(v("3:11"), "left: 12px; top: 12px", size=11) + god(sp("3:12-13"), "left: 12px; top: 50px", size=21, maxw=620) + vref("NUM 3:11–13", "right: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], K.wilderness_camp("m3b", W1, h[1], 232, cast=[(A.moses, 0.44, 0.52, True)]),
             cap(v("3:14"), "left: 12px; top: 12px", size=11) + god(v("3:15"), "left: 12px; top: 50px", size=16, maxw=430)
             + cap(v("3:16"), "right: 12px; bottom: 34px", size=11, maxw=280) + vref("NUM 3:14–16", "right: 12px; bottom: 10px"))
    return page("Numbers 3:11–16 — All the First-born Are Mine", t, r1 + r2, n)


@P("NUM-C02-P04-SonsOfLevi", "The Sons of Levi by Their Names")
def p04(n):
    t, h = rows(None, 300)
    cells = [clan("Levi", v("3:17"), "NUM 3:17", "#E04A2A", size=16), clan("Gershon", v("3:18"), "NUM 3:18", GC, of="OF LEVI", size=16),
             clan("Kohath", v("3:19"), "NUM 3:19", KC, of="OF LEVI", size=16), clan("Merari", v("3:20"), "NUM 3:20", MC, of="OF LEVI", size=15)]
    r2 = new(INK, W1, h[1], K2.levite_plan(W1, h[1]), "")
    return page("Numbers 3:17–20 — The Sons of Levi by Their Names", t, grid(cells, "repeat(2, minmax(0, 1fr))") + r2, n)


def family_page(n, side, plan_title, cells, plate, refs, head, cols_=2):
    """One family of the Levites: the plan with its side lit, its cells, and a plate of its charge with the verses."""
    t, h = rows(230, None, 360)
    plan = new(INK, W1, h[0], K2.levite_plan(W1, h[0], hi=side, title=plan_title), "")
    words, ref = plate[0], plate[1]
    r3 = new(INK, W1, h[2], plate[2](W1, h[2]), cap(words, "left: 12px; top: 30px", size=12.5, maxw=380) + vref(ref, "right: 12px; top: 8px"))
    return page(f"Numbers {refs} — {head}", t, plan + grid(cells, "minmax(0, 1fr)", ncol=cols_) + r3, n)


@P("NUM-C02-P05-Gershon", "Behind the Tabernacle Westward")
def p05(n):
    cells = [tally("GERSHON", "3:21-22", "7,500", accent=GC, size=15), clan("Westward", sp("3:23-24"), "NUM 3:23–24", GC, of="GERSHON", size=17)]
    plate = (sp("3:25-26"), "NUM 3:25–26", lambda w, h: K2.wrap_plate(w, h, "THE CHARGE OF GERSHON", "curtains", [("CURTAINS · COVERINGS", "#F3EFE6"), ("HANGINGS · SCREENS · CORDS", "#8A3A2A")], staves=False))
    return family_page(n, "W", "GERSHON · WESTWARD", cells, plate, "3:21–26", "Behind the Tabernacle Westward")


@P("NUM-C02-P06-Kohath", "The Charge of the Sanctuary")
def p06(n):
    cells = [tally("KOHATH", "3:27-28", "8,600", accent=KC, size=11), clan("Southward", sp("3:29-30"), "NUM 3:29–30", KC, of="KOHATH", size=13),
             clan("Eleazar", v("3:32"), "NUM 3:32", "#F3EFE6", of="PRINCE", size=13)]
    plate = (v("3:31"), "NUM 3:31", lambda w, h: K2.wrap_plate(w, h, "THE CHARGE OF KOHATH", "ark", [("ARK · TABLE · CANDLESTICK · ALTARS", "#E8B830")]))
    return family_page(n, "S", "KOHATH · SOUTHWARD", cells, plate, "3:27–32", "The Charge of the Sanctuary", cols_=3)


@P("NUM-C02-P07-Merari", "On the Side of the Tabernacle Northward")
def p07(n):
    cells = [tally("MERARI", "3:33-34", "6,200", accent=MC, size=15), clan("Northward", v("3:35"), "NUM 3:35", MC, of="MERARI", size=17)]
    plate = (sp("3:36-37"), "NUM 3:36–37", lambda w, h: K2.wrap_plate(w, h, "THE CHARGE OF MERARI", "boards", [("BOARDS · BARS · PILLARS · SOCKETS", "#C8A06A")], staves=False))
    return family_page(n, "N", "MERARI · NORTHWARD", cells, plate, "3:33–37", "On the Side of the Tabernacle Northward")


@P("NUM-C02-P08-Eastward", "Before the Tent of Meeting toward the Sunrising")
def p08(n):
    t, h = rows(400, None)
    r1 = new(INK, W1, h[0], K2.levite_plan(W1, h[0], hi="E", title="MOSES · AARON AND HIS SONS · EASTWARD"), "")
    r2 = new(SAND, W1, h[1], K.levites_round("m8b", W1, h[1], 282),
             cap(v("3:38"), "left: 12px; top: 12px", size=12, maxw=440) + cap(v("3:39"), "left: 12px; top: 150px", size=12, maxw=440)
             + hud("22,000", "right: 16px; top: 16px", size=40) + vref("NUM 3:38–39", "right: 12px; bottom: 12px"))
    return page("Numbers 3:38–39 — Before the Tent of Meeting toward the Sunrising", t, r1 + r2, n)


@P("NUM-C02-P09-FirstBorn", "Number All the First-born")
def p09(n):
    t, h = rows(300, None, 300)
    r1 = new(SKY, W1, h[0], K.wilderness_camp("m9a", W1, h[0], 291, cast=[(A.moses, 0.44, 0.52, True)]),
             cap(v("3:40", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("3:40", frm="Number all"), "left: 12px; top: 50px", size=16, maxw=430) + vref("NUM 3:40", "right: 12px; bottom: 12px"))
    r2 = night(h[1], god(v("3:41"), "left: 12px; top: 12px", size=19, maxw=640) + vref("NUM 3:41", "right: 12px; bottom: 12px"))
    r3 = new(INK, W1, h[2], K2.firstborn_chart(W1, h[2]), cap(sp("3:42-43"), "left: 12px; top: 30px", size=11, maxw=600) + vref("NUM 3:42–43", "right: 12px; top: 8px"))
    return page("Numbers 3:40–43 — Number All the First-born", t, r1 + r2 + r3, n)


@P("NUM-C02-P10-Redemption", "The Redemption-money")
def p10(n):
    t, h = rows(None, 340)
    r1 = night(h[0], cap(v("3:44"), "left: 12px; top: 12px", size=11) + god(sp("3:45-48"), "left: 12px; top: 50px", size=18, maxw=640) + vref("NUM 3:44–48", "right: 12px; bottom: 12px"))
    r2 = new(INK, W1, h[1], K2.redemption(W1, h[1]), cap(sp("3:49-51"), "left: 12px; top: 30px", size=12, maxw=330) + vref("NUM 3:49–51", "right: 12px; top: 8px"))
    return page("Numbers 3:44–51 — The Redemption-money", t, r1 + r2, n)


@P("NUM-C02-P11-Thirty", "From Thirty Years Old until Fifty")
def p11(n):
    t, h = rows(None, 380)
    r1 = night(h[0], mk.stamp(4, "right: 14px; top: 12px") + cap(v("4:1"), "left: 12px; top: 12px", size=11)
               + god(sp("4:2-4"), "left: 12px; top: 50px", size=20, maxw=560) + vref("NUM 4:1–4", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], K.levites_round("m11b", W1, h[1], 2112), "")
    return page("Numbers 4:1–4 — From Thirty Years Old until Fifty", t, r1 + r2, n)


def plate(title, kind, layers, staves=True, frame=False):
    return lambda w, h: K2.wrap_plate(w, h, title, kind, layers, staves=staves, frame=frame)
VEIL, SEALS = ("THE VEIL OF THE SCREEN", "#C8202A"), ("A COVERING OF SEALSKIN", K2.SEAL)
BLUEC = ("A CLOTH OF BLUE", K2.BLUE)
PG.extend(blueprints([
    ("4:5–6", [("god", sp("4:5-6"))], plate("THE ARK OF THE TESTIMONY", "ark", [VEIL, SEALS, ("A CLOTH ALL OF BLUE", K2.BLUE)]), "The Burden of the Sons of Kohath"),
    ("4:7–8", [("god", sp("4:7-8"))], plate("THE TABLE OF SHOWBREAD", "table", [BLUEC, ("A CLOTH OF SCARLET", K2.SCARLET), SEALS]), None),
    ("4:9–10", [("god", sp("4:9-10"))], plate("THE CANDLESTICK OF THE LIGHT", "lamp", [BLUEC, SEALS], staves=False, frame=True), None),
    ("4:11–12", [("god", sp("4:11-12"))], plate("THE GOLDEN ALTAR · THE VESSELS", "altar_gold", [BLUEC, SEALS]), None),
    ("4:13–14", [("god", sp("4:13-14"))], plate("THE ALTAR", "altar", [("A PURPLE CLOTH", K2.PURPLE), SEALS]), None),
    ("4:15", [("god", v("4:15"))], lambda w, h: K2.bearers("bp15", w, h, 2150, n=1), None),
], "NUM-C02-B", PG.next(), "The Burden of the Sons of Kohath", budget=900, book="Numbers"))


@P("NUM-C02-P12-LestTheyDie", "Lest They Die")
def p12(n):
    t, h = rows(None, 360)
    r1 = new(SAND, W1, h[0], K2.aaron_sons("m12a", W1, h[0], 2121), cap(v("4:16"), "left: 12px; top: 12px", size=12.5, maxw=480) + vref("NUM 4:16", "right: 12px; bottom: 12px"))
    r2 = night(h[1], cap(v("4:17"), "left: 12px; top: 12px", size=11) + god(sp("4:18-20"), "left: 12px; top: 50px", size=19, maxw=620) + vref("NUM 4:17–20", "right: 12px; bottom: 12px"))
    return page("Numbers 4:16–20 — Lest They Die", t, r1 + r2, n)


PG.extend(blueprints([
    ("4:21–24", [("cap", v("4:21")), ("god", sp("4:22-24"))], lambda w, h: K.levites_round("bp21", w, h, 2210), "The Service of the Gershonites"),
    ("4:25–26", [("god", sp("4:25-26"))], plate("THE BURDEN OF GERSHON", "curtains", [("THE CURTAINS · THE TENT", "#F3EFE6"), SEALS, ("THE HANGINGS · THE SCREENS", "#E8E2D6")], staves=False), None),
    ("4:27–28", [("god", sp("4:27-28"))], lambda w, h: K2.aaron_sons("bp27", w, h, 2270), None),
    ("4:29–30", [("god", sp("4:29-30"))], lambda w, h: K.levites_round("bp29", w, h, 2290), "The Service of the Sons of Merari"),
    ("4:31–32", [("god", sp("4:31-32"))], plate("THE BURDEN OF MERARI", "boards", [("BOARDS · BARS · PILLARS · SOCKETS", "#C8A06A"), ("PINS · CORDS · INSTRUMENTS", "#8A6A4A")], staves=False), None),
    ("4:33", [("god", v("4:33"))], lambda w, h: K2.aaron_sons("bp33", w, h, 2330), None),
], "NUM-C02-C", PG.next(), "The Service of the Gershonites", budget=900, book="Numbers"))


@P("NUM-C02-P13-NumberedKohath", "Those That Were Numbered")
def p13(n):
    cells = [tally("KOHATH", "4:34-37", "2,750", accent=KC, size=13), tally("GERSHON", "4:38-41", "2,630", accent=GC, size=13)]
    return page("Numbers 4:34–41 — Those That Were Numbered", "minmax(0, 1fr)", grid(cells, "repeat(2, minmax(0, 1fr))", ncol=1), n)


@P("NUM-C02-P14-EightThousand", "Every One According to His Service")
def p14(n):
    t, h = rows(None, 430)
    top = grid([tally("MERARI", "4:42-45", "3,200", accent=MC, size=13)], "minmax(0, 1fr)", ncol=1)
    r2 = new(SAND, W1, h[1], K2.bearers("m14b", W1, h[1], 2142),
             cap(sp("4:46-49"), "left: 12px; top: 12px", size=11.5, maxw=470) + hud("8,580", "right: 16px; top: 16px", size=40)
             + vref("NUM 4:46–49", "left: 12px; bottom: 12px") + end_mark("NEXT · JEHOVAH BLESS THEE", "right: 10px; bottom: 10px"))
    return page("Numbers 4:42–49 — Every One According to His Service", t, top + r2, n)
