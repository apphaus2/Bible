"""Numbers volume, Chapter 16 — The Borders of the Land (Numbers 34–36), the end of Numbers. Every verse, word for word
from ref/eng-asv. The borders of Canaan as a map lit border by border; the men that shall divide the land (cells); the cities
of the Levites and the cities of refuge as law cells; and the daughters of Zelophehad married within their tribe.
The volume ends with 完."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cols, cap, god, balloon
from exo import art as A, art8 as B8
from exo.kit import talk, law_pages, set_book
from num import G, art as K, art13 as K13, art15 as K15, art16 as K16
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY, DUSK
from genesis.ch03 import SAND, clan
from genesis.ch06 import GOLDEN
from num import ch15 as _prev

v, sp = G.v, G.span
set_book(G)
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK = "#0B1A2E"
SAY = "And Jehovah spake unto Moses, saying,"

def night(h, over, w=W1): return new(NIGHT, w, h, X.cosmic(w, h), over)
def after(ref, to):
    t = v(ref); return v(ref, frm=t[t.index(to) + len(to):].strip())
def border_panel(h, hi, refs, label_):
    return new(INK, W1, h, K16.borders(W1, h, hi=hi), god(sp(refs), "right: 12px; bottom: 12px", size=15, maxw=300) + vref(label_, "left: 12px; bottom: 12px"))


@P("NUM-C16-00-Title", "Chapter 16 · The Borders of the Land", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B1A2E"></rect>' + f'<g transform="translate(0 370)">{K16.borders(760, 690)}</g>'
    return chapter_title(16, "第十六話", "The Borders of the Land", "Numbers 34 – 36", svg, INK, v("34:12", frm="This shall be your land"), "Numbers · Volume Four")


@P("NUM-C16-P01-South", "When Ye Come into the Land of Canaan")
def p01(n):
    t, h = rows(250, None)
    r1 = night(h[0], mk.stamp(34, "right: 14px; top: 12px") + cap(v("34:1"), "left: 12px; top: 12px", size=11) + god(v("34:2"), "left: 12px; top: 50px", size=19, maxw=580) + vref("NUM 34:1–2", "right: 12px; bottom: 12px"))
    r2 = new(INK, W1, h[1], K16.borders(W1, h[1], hi="S"), god(sp("34:3-5"), "right: 12px; top: 12px", size=15, maxw=270) + vref("NUM 34:3–5", "left: 12px; bottom: 12px"))
    return page("Numbers 34:1–5 — When Ye Come into the Land of Canaan", t, r1 + r2, n)


@P("NUM-C16-P02-North", "This Shall Be Your North Border")
def p02(n):
    t, h = rows(500, None)
    r1 = new(INK, W1, h[0], K16.borders(W1, h[0], hi="W"), god(v("34:6"), "right: 12px; top: 120px", size=16, maxw=280) + vref("NUM 34:6", "left: 12px; bottom: 12px"))
    r2 = new(INK, W1, h[1], K16.borders(W1, h[1], hi="N"), god(sp("34:7-9"), "right: 12px; top: 80px", size=15, maxw=280) + vref("NUM 34:7–9", "left: 12px; bottom: 12px"))
    return page("Numbers 34:6–9 — This Shall Be Your North Border", t, r1 + r2, n)


@P("NUM-C16-P03-East", "According to the Borders Thereof Round About")
def p03(n):
    t, h = rows(500, None)
    r1 = new(INK, W1, h[0], K16.borders(W1, h[0], hi="E"), god(sp("34:10-12"), "left: 12px; bottom: 12px", size=15, maxw=280) + vref("NUM 34:10–12", "right: 12px; bottom: 12px"))
    r2 = talk(A.MOSES, h[1], GOLDEN, [("cap", v("34:13", to="saying,")), ("say", after("34:13", "saying,") + " " + v("34:14") + " " + v("34:15"))], ref="NUM 34:13–15", size=15)
    return page("Numbers 34:10–15 — According to the Borders Thereof Round About", t, r1 + r2, n)


@P("NUM-C16-P04-Dividers", "The Men That Shall Divide the Land")
def p04(n):
    t, h = rows(240, None)
    r1 = night(h[0], cap(v("34:16"), "left: 12px; top: 12px", size=11) + god(v("34:17") + " " + v("34:18"), "left: 12px; top: 50px", size=19, maxw=600) + vref("NUM 34:16–18", "right: 12px; bottom: 12px"))
    names = [("JUDAH", "34:19"), ("SIMEON", "34:20"), ("BENJAMIN", "34:21"), ("DAN", "34:22"), ("MANASSEH", "34:23"),
             ("EPHRAIM", "34:24"), ("ZEBULUN", "34:25"), ("ISSACHAR", "34:26"), ("ASHER", "34:27"), ("NAPHTALI", "34:28")]
    cells = [clan(t_.title(), v(r), "NUM " + r, K.TRIBE_C[t_] if K.TRIBE_C[t_] not in ("#3A3A5A", "#6A6A8A") else "#B8C0E8", size=12.5) for t_, r in names]
    cells.append(clan("These", v("34:29"), "NUM 34:29", "#FFD23F", size=12.5))
    return page("Numbers 34:16–29 — The Men That Shall Divide the Land", t, r1 + grid(cells, "repeat(6, minmax(0, 1fr))"), n)


LAWS = [
    ("CITIES TO DWELL IN", "35:1-2", K16.pg_levite_cities, "And Jehovah spake unto Moses in the plains of Moab by the Jordan at Jericho, saying,", "The Cities of the Levites"),
    ("FOR THEIR CATTLE", "35:3", K16.pg_cattle, "", None),
    ("A THOUSAND CUBITS", "35:4", K16.pg_thousand, "", None),
    ("TWO THOUSAND CUBITS", "35:5", K16.pg_suburbs, "", None),
    ("FORTY AND EIGHT CITIES", "35:6-7", K16.pg_forty_eight, "", None),
    ("FROM THE MANY · FROM THE FEW", "35:8", K16.pg_many_few, "", None),
    ("CITIES OF REFUGE", "35:9-11", K16.pg_refuge, SAY, "Cities of Refuge"),
    ("FROM THE AVENGER", "35:12", K16.pg_avenger, "", None),
    ("SIX CITIES", "35:13-14", K16.pg_six, "", None),
    ("THE STRANGER AND THE SOJOURNER", "35:15", K16.pg_stranger, "", None),
    ("AN INSTRUMENT OF IRON", "35:16", K16.pg_iron, "", "He Is a Murderer"),
    ("A STONE IN THE HAND", "35:17", K16.pg_stone, "", None),
    ("A WEAPON OF WOOD", "35:18", K16.pg_wood, "", None),
    ("THE AVENGER OF BLOOD", "35:19", K16.pg_avenger2, "", None),
    ("OF HATRED", "35:20-21", K16.pg_hatred, "", None),
    ("WITHOUT ENMITY", "35:22-23", K16.pg_suddenly, "", "If He Thrust Him Suddenly"),
    ("THE CONGREGATION SHALL JUDGE", "35:24-25", K16.pg_judge, "", None),
    ("BEYOND THE BORDER", "35:26-27", K16.pg_border, "", None),
    ("AFTER THE DEATH OF THE HIGH PRIEST", "35:28-29", K16.pg_return, "", None),
    ("AT THE MOUTH OF WITNESSES", "35:30", K16.pg_witnesses, "", "Ye Shall Not Pollute the Land"),
    ("NO RANSOM", "35:31-32", K16.pg_no_ransom, "", None),
    ("BLOOD POLLUTETH THE LAND", "35:33", K16.pg_pollute, "", None),
    ("I DWELL IN THE MIDST", "35:34", K16.pg_dwell, "", None),
]
PG.extend(law_pages(LAWS, "NUM-C16-L", PG.next(), "The Cities of the Levites", title_book="Numbers", carry=True))


@P("NUM-C16-P05-Gilead", "The Tribe of the Sons of Joseph Speaketh Right")
def p05(n):
    t, h = rows(None, 330)
    r1 = talk(K16.GILEADITE, h[0], GOLDEN, [("cap", v("36:1")), ("cap", v("36:2", to="and they said,")), ("say", after("36:2", "and they said,") + " " + v("36:3") + " " + v("36:4"))], ref="NUM 36:1–4", size=14)
    r2 = talk(A.MOSES_CALM, h[1], GOLDEN, [("cap", v("36:5", to="saying,")), ("say", after("36:5", "saying,") + " " + v("36:6") + " " + v("36:7"))], ref="NUM 36:5–7", size=14, flip=True)
    return page("Numbers 36:1–7 — The Tribe of the Sons of Joseph Speaketh Right", t, r1 + r2, n)


@P("NUM-C16-P06-End", "In the Plains of Moab")
def p06(n):
    t, h = rows(260, 300, None)
    r1 = night(h[0], god(v("36:8") + " " + v("36:9"), "left: 12px; top: 12px", size=18, maxw=640) + vref("NUM 36:8–9", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], K13.daughters("z6b", W1, h[1], 1662), cap(v("36:10") + " " + v("36:11") + " " + v("36:12"), "right: 12px; top: 12px", size=12, maxw=330) + vref("NUM 36:10–12", "right: 12px; bottom: 12px"))
    r3 = new(DUSK, W1, h[2], K.wilderness_camp("z6c", W1, h[2], 1663, dusk=True, sinai=False), cap(v("36:13"), "left: 12px; top: 12px", size=13, maxw=520)
             + vref("NUM 36:13", "left: 12px; bottom: 12px") + end_mark("END OF NUMBERS · NEXT · DEUTERONOMY", "right: 10px; bottom: 10px", ch="完"))
    return page("Numbers 36:8–13 — In the Plains of Moab", t, r1 + r2 + r3, n)
