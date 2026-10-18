"""Numbers volume, Chapter 13 — The Daughters of Zelophehad (Numbers 27–29). Every verse, word for word from ref/asv.
The daughters of Zelophehad and the law of inheritance; Moses shown the land from the mountain of Abarim; Joshua set
before Eleazar; and the offerings of every day, sabbath, new moon and set feast as law cells (the beasts counted)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cols, cap, god, balloon
from exo import art as A, art8 as B8
from exo.kit import talk, law_pages, set_book
from num import G, art as K, art13 as K13
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY, DUSK
from genesis.ch03 import SAND
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from num import ch12 as _prev

v, sp = G.v, G.span
set_book(G)
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
SAY = "And Jehovah spake unto Moses, saying,"

def night(h, over, w=W1): return new(NIGHT, w, h, X.cosmic(w, h), over)
def after(ref, to):
    t = v(ref); return v(ref, frm=t[t.index(to) + len(to):].strip())


@P("NUM-C13-00-Title", "Chapter 13 · The Daughters of Zelophehad", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2A1A"></rect>' + f'<g transform="translate(0 380)">{K13.daughters("t13", 760, 700, 1301)}</g>'
    return chapter_title(13, "第十三話", "The Daughters of Zelophehad", "Numbers 27 – 29", svg, SAND, v("27:7", to="speak right:"), "Numbers · Volume Four")


@P("NUM-C13-P01-Daughters", "The Daughters of Zelophehad")
def p01(n):
    t, h = rows(360, None)
    r1 = new(SAND, W1, h[0], K13.daughters("w1a", W1, h[0], 1311), mk.stamp(27, "right: 14px; top: 12px") + cap(v("27:1") + " " + v("27:2", to="saying,"), "left: 12px; top: 12px", size=11.5, maxw=500) + vref("NUM 27:1–2", "right: 12px; bottom: 12px"))
    r2 = talk(K13.MAHLAH, h[1], GOLDEN, [("say", v("27:3") + " " + v("27:4"))], ref="NUM 27:3–4", size=17)
    return page("Numbers 27:1–4 — The Daughters of Zelophehad", t, r1 + r2, n)


@P("NUM-C13-P02-SpeakRight", "The Daughters of Zelophehad Speak Right")
def p02(n):
    t, h = rows(560, None)
    r1 = night(h[0], cap(v("27:5") + " " + v("27:6"), "left: 12px; top: 12px", size=11) + god(v("27:7") + " " + sp("27:8-11"), "left: 12px; top: 50px", size=19, maxw=660) + vref("NUM 27:5–11", "right: 12px; bottom: 12px"))
    r2 = new(B8.INK, W1, h[1], K13.inheritance(W1, h[1]), "")
    return page("Numbers 27:5–11 — The Daughters of Zelophehad Speak Right", t, r1 + r2, n)


@P("NUM-C13-P03-Abarim", "This Mountain of Abarim")
def p03(n):
    t, h = rows(None, 300)
    r1 = new("#F3C88A", W1, h[0], K13.abarim("w3a", W1, h[0], 1331), cap(v("27:12", to="unto Moses,"), "right: 12px; top: 12px", size=11)
             + god(after("27:12", "unto Moses,") + " " + v("27:13") + " " + v("27:14"), "right: 12px; top: 50px", size=17, maxw=420) + vref("NUM 27:12–14", "right: 12px; bottom: 12px"))
    r2 = talk(A.MOSES_CALM, h[1], GOLDEN, [("cap", v("27:15")), ("say", v("27:16") + " " + v("27:17"))], ref="NUM 27:15–17", size=15)
    return page("Numbers 27:12–17 — This Mountain of Abarim", t, r1 + r2, n)


@P("NUM-C13-P04-Joshua", "Take Thee Joshua the Son of Nun")
def p04(n):
    t, h = rows(400, None)
    r1 = night(h[0], cap(v("27:18", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(after("27:18", "unto Moses,") + " " + sp("27:19-21"), "left: 12px; top: 50px", size=19, maxw=660) + vref("NUM 27:18–21", "right: 12px; bottom: 12px"))
    r2 = new(GOLDEN, W1, h[1], K13.joshua_set("w4b", W1, h[1], 1342), cap(v("27:22") + " " + v("27:23"), "left: 12px; top: 12px", size=12.5, maxw=520) + vref("NUM 27:22–23", "right: 12px; bottom: 12px"))
    return page("Numbers 27:18–23 — Take Thee Joshua the Son of Nun", t, r1 + r2, n)


LAWS = [
    ("MY FOOD", "28:1-2", K13.pg_my_food, SAY, "The Continual Burnt-offering"),
    ("TWO HE-LAMBS DAY BY DAY", "28:3-4", K13.pg_continual, "", None),
    ("THE MEAL-OFFERING", "28:5", K13.pg_morning, "", None),
    ("ORDAINED IN MOUNT SINAI", "28:6", K13.pg_sinai, "", None),
    ("THE DRINK-OFFERING", "28:7-8", K13.pg_drink, "", None),
    ("EVERY SABBATH", "28:9-10", K13.pg_sabbath, "", "The Sabbath and the New Moon"),
    ("THE BEGINNINGS OF YOUR MONTHS", "28:11", K13.pg_new_moon, "", None),
    ("FOR EVERY MONTH", "28:12-14", K13.pg_new_moon_meal, "", None),
    ("ONE HE-GOAT", "28:15", K13.pg_goat, "", None),
    ("JEHOVAH'S PASSOVER", "28:16-18", K13.pg_unleavened, "", "Passover and Unleavened Bread"),
    ("AN OFFERING MADE BY FIRE", "28:19-22", K13.pg_feast_herd, "", None),
    ("DAILY, FOR SEVEN DAYS", "28:23-25", K13.pg_daily7, "", None),
    ("THE DAY OF THE FIRST-FRUITS", "28:26-27", K13.pg_firstfruits, "", "The Day of the First-fruits"),
    ("THREE TENTH PARTS", "28:28-31", K13.pg_goat, "", None),
    ("A DAY OF BLOWING OF TRUMPETS", "29:1-2", K13.pg_trumpets, "", "The Seventh Month"),
    ("THE MEAL-OFFERING THEREOF", "29:3-6", K13.pg_seventh_herd, "", None),
    ("THE TENTH DAY", "29:7-8", K13.pg_atonement, "", None),
    ("BESIDES THE SIN-OFFERING OF ATONEMENT", "29:9-11", K13.pg_goat, "", None),
    ("THE FIFTEENTH DAY", "29:12-13", K13.pg_booths, "", "Seven Days unto Jehovah"),
    ("THIRTEEN BULLOCKS", "29:14-16", K13.day_herd("FIRST", 13), "", None),
    ("THE SECOND DAY", "29:17-19", K13.day_herd("SECOND", 12), "", None),
    ("THE THIRD DAY", "29:20-22", K13.day_herd("THIRD", 11), "", None),
    ("THE FOURTH DAY", "29:23-25", K13.day_herd("FOURTH", 10), "", None),
    ("THE FIFTH DAY", "29:26-28", K13.day_herd("FIFTH", 9), "", None),
    ("THE SIXTH DAY", "29:29-31", K13.day_herd("SIXTH", 8), "", None),
    ("THE SEVENTH DAY", "29:32-34", K13.day_herd("SEVENTH", 7), "", None),
    ("A SOLEMN ASSEMBLY", "29:35-38", K13.pg_eighth, "", "The Eighth Day"),
    ("IN YOUR SET FEASTS", "29:39", K13.pg_set_feasts, "", None),
    ("AND MOSES TOLD THE CHILDREN OF ISRAEL", "29:40", K13.pg_told, "", None),
]
PG.extend(law_pages(LAWS, "NUM-C13-L", PG.next(), "The Continual Burnt-offering", title_book="Numbers", carry=True,
                    end=end_mark("NEXT · VOWS AND THE WAR WITH MIDIAN", "right: 10px; top: 10px")))
