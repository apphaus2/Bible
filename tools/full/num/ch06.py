"""Numbers volume, Chapter 6 — Graves of Lust (Numbers 11–12). Every verse, word for word from ref/eng-asv.
Taberah; the mixed multitude lusting after the food of Egypt; the manna; Moses' burden and the seventy elders; Eldad and
Medad; the quails and Kibroth-hattaavah (11:33 shown only as the graves); Miriam and Aaron against Moses, Miriam leprous
and shut up without the camp seven days."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cols, cap, god, balloon
from exo import art as A, art5 as A5, art10 as A10, art8 as B8
from exo.kit import talk
from num import G, art as K, art6 as K6
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY, DUSK
from genesis.ch03 import SAND
from genesis.ch04 import COLD, EMBER
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED, BLUE
from num import ch05 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
FIRE = "linear-gradient(180deg, #2A0A0A 0%, #8A1E16 60%, #FF8A3D 100%)"

def night(h, over, w=W1): return new(NIGHT, w, h, X.cosmic(w, h), over)
def after(ref, to):
    t = v(ref); return v(ref, frm=t[t.index(to) + len(to):].strip())


@P("NUM-C06-00-Title", "Chapter 6 · Graves of Lust", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A1A2E"></rect>' + f'<g transform="translate(0 320)">{K6.quails_fall("t6", 760, 760, 601)}</g>'
    return chapter_title(6, "第六話", "Graves of Lust", "Numbers 11 – 12", svg, DUSK, v("11:23", frm="Is Jehovah's hand waxed short?"), "Numbers · Volume Four")


@P("NUM-C06-P01-Taberah", "Taberah")
def p01(n):
    t, h = rows(None, 360)
    r1 = new(FIRE, W1, h[0], K6.taberah("q1a", W1, h[0], 611), mk.stamp(11, "right: 14px; top: 12px") + cap(v("11:1"), "left: 12px; top: 12px", size=12.5, maxw=470) + vref("NUM 11:1", "right: 12px; bottom: 12px"))
    r2 = new("#4A3A3A", W1, h[1], K6.taberah("q1b", W1, h[1], 612, abated=True), cap(v("11:2") + " " + v("11:3"), "left: 12px; top: 12px", size=13, maxw=470) + vref("NUM 11:2–3", "right: 12px; bottom: 12px"))
    return page("Numbers 11:1–3 — Taberah", t, r1 + r2, n)


@P("NUM-C06-P02-Flesh", "Who Shall Give Us Flesh to Eat?")
def p02(n):
    t, h = rows(None, 260)
    r1 = talk(A.HEBREW_ANGRY, h[0], RED, [("cap", v("11:4", to="and said,")), ("say", after("11:4", "and said,") + " " + v("11:5") + " " + v("11:6"))], ref="NUM 11:4–6", size=16)
    r2 = new("#F3EFE6", W1, h[1], K6.egypt_food(W1, h[1]), "")
    return page("Numbers 11:4–6 — Who Shall Give Us Flesh to Eat?", t, r1 + r2, n)


@P("NUM-C06-P03-Manna", "Like Coriander Seed")
def p03(n):
    t, h = rows(230, None, 230)
    r1 = new(SKY, W1, h[0], A5.dew_camp(W1, h[0], 631), cap(v("11:7"), "left: 12px; top: 12px", size=13, maxw=440) + vref("NUM 11:7", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], mk.defs("q3b", *K.ALL) + A5.gathering("q3b", W1, h[1], 632), cap(v("11:8"), "left: 12px; top: 12px", size=13, maxw=470) + vref("NUM 11:8", "right: 12px; bottom: 12px"))
    r3 = new(NIGHT, W1, h[2], K.wilderness_camp("q3c", W1, h[2], 633, dusk=True, standards=False, sinai=False), cap(v("11:9"), "left: 12px; top: 12px", size=13, maxw=440) + vref("NUM 11:9", "right: 12px; bottom: 12px"))
    return page("Numbers 11:7–9 — Like Coriander Seed", t, r1 + r2 + r3, n)


@P("NUM-C06-P04-Burden", "Wherefore Hast Thou Dealt Ill with Thy Servant?")
def p04(n):
    t, h = rows(300, None)
    r1 = new("#2A2A4A", W1, h[0], K6.weeping("q4a", W1, h[0], 641), cap(v("11:10"), "left: 12px; top: 12px", size=12.5, maxw=500) + vref("NUM 11:10", "right: 12px; bottom: 12px"))
    r2 = talk(A5.MOSES_TIRED, h[1], BLUE, [("cap", v("11:11", to="unto Jehovah,")), ("say", after("11:11", "unto Jehovah,") + " " + v("11:12"))], ref="NUM 11:11–12", size=16)
    return page("Numbers 11:10–12 — Wherefore Hast Thou Dealt Ill with Thy Servant?", t, r1 + r2, n)


@P("NUM-C06-P05-TooHeavy", "It Is Too Heavy for Me")
def p05(n):
    t, h = rows(None, 330)
    r1 = talk(A5.MOSES_TIRED, h[0], BLUE, [("say", v("11:13") + " " + v("11:14"))], ref="NUM 11:13–14", size=19, flip=True)
    r2 = talk(A.MOSES_AFRAID, h[1], COLD, [("say", v("11:15"))], ref="NUM 11:15", size=18)
    return page("Numbers 11:13–15 — It Is Too Heavy for Me", t, r1 + r2, n)


@P("NUM-C06-P06-Seventy", "Gather unto Me Seventy Men")
def p06(n):
    t, h = rows(None, 330)
    r1 = night(h[0], cap(v("11:16", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(after("11:16", "unto Moses,") + " " + v("11:17"), "left: 12px; top: 50px", size=21, maxw=640) + vref("NUM 11:16–17", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], K6.elders_round("q6b", W1, h[1], 662), "")
    return page("Numbers 11:16–17 — Gather unto Me Seventy Men", t, r1 + r2, n)


@P("NUM-C06-P07-Nostrils", "Until It Come Out at Your Nostrils")
def p07(n):
    t, h = rows(None, 300)
    r1 = night(h[0], god(v("11:18") + " " + v("11:19") + " " + v("11:20"), "left: 12px; top: 12px", size=21, maxw=660) + vref("NUM 11:18–20", "right: 12px; bottom: 12px"))
    r2 = new("#F3EFE6", W1, h[1], K6.egypt_food(W1, h[1]), "")
    return page("Numbers 11:18–20 — Until It Come Out at Your Nostrils", t, r1 + r2, n)


@P("NUM-C06-P08-HandShort", "Is Jehovah's Hand Waxed Short?")
def p08(n):
    t, h = rows(None, 340)
    r1 = talk(A5.MOSES_TIRED, h[0], BLUE, [("cap", v("11:21", to="And Moses said,")), ("say", after("11:21", "Moses said,") + " " + v("11:22"))], ref="NUM 11:21–22", size=17)
    r2 = night(h[1], cap(v("11:23", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(after("11:23", "unto Moses,"), "left: 12px; top: 50px", size=28, maxw=640) + vref("NUM 11:23", "right: 12px; bottom: 12px"))
    return page("Numbers 11:21–23 — Is Jehovah's Hand Waxed Short?", t, r1 + r2, n)


@P("NUM-C06-P09-Prophesied", "When the Spirit Rested upon Them")
def p09(n):
    t, h = rows(400, None)
    r1 = new(SAND, W1, h[0], K6.elders_round("q9a", W1, h[0], 691), cap(v("11:24"), "left: 12px; top: 12px", size=12.5, maxw=500) + vref("NUM 11:24", "right: 12px; bottom: 12px"))
    r2 = new(GOLDEN, W1, h[1], K6.elders_round("q9b", W1, h[1], 692, spirit=True), cap(v("11:25"), "left: 12px; top: 12px", size=13, maxw=520) + vref("NUM 11:25", "right: 12px; bottom: 12px"))
    return page("Numbers 11:24–25 — When the Spirit Rested upon Them", t, r1 + r2, n)


@P("NUM-C06-P10-Eldad", "Eldad and Medad")
def p10(n):
    t, h = rows(250, 220, 210, None)
    r1 = new(SKY, W1, h[0], K.wilderness_camp("q10a", W1, h[0], 6101, standards=False, sinai=False), cap(v("11:26"), "left: 12px; top: 12px", size=12, maxw=520) + vref("NUM 11:26", "right: 12px; bottom: 12px"))
    r2 = talk(K6.YOUNG_MAN, h[1], GOLDEN, [("cap", v("11:27", to="and said,")), ("say", after("11:27", "and said,"))], ref="NUM 11:27", size=18)
    r3 = talk(A5.JOSHUA, h[2], RED, [("cap", v("11:28", to="answered and said,")), ("say", after("11:28", "answered and said,"))], ref="NUM 11:28", size=18, flip=True)
    r4 = talk(A.MOSES_CALM, h[3], GOLDEN, [("cap", v("11:29", to="unto him,")), ("say", after("11:29", "unto him,"))], ref="NUM 11:29", size=18)
    return page("Numbers 11:26–29 — Eldad and Medad", t, r1 + r2 + r3 + r4, n)


@P("NUM-C06-P11-Quails", "Quails from the Sea")
def p11(n):
    t, h = rows(None, 360)
    r1 = new(SKY, W1, h[0], K6.quails_fall("q11a", W1, h[0], 6111), cap(v("11:30") + " " + v("11:31"), "left: 12px; top: 12px", size=12.5, maxw=500) + vref("NUM 11:30–31", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], K6.quails_fall("q11b", W1, h[1], 6112, gathering=True), cap(v("11:32"), "left: 12px; top: 12px", size=12.5, maxw=500) + vref("NUM 11:32", "right: 12px; bottom: 12px"))
    return page("Numbers 11:30–32 — Quails from the Sea", t, r1 + r2, n)


@P("NUM-C06-P12-Graves", "Kibroth-hattaavah")
def p12(n):
    t, h = rows(None, 230)
    r1 = new(DUSK, W1, h[0], K6.graves_lust(W1, h[0], 6121), cap(v("11:33") + " " + v("11:34"), "left: 12px; top: 12px", size=13.5, maxw=500) + vref("NUM 11:33–34", "right: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], K.wilderness_camp("q12b", W1, h[1], 6122, standards=False, sinai=False), cap(v("11:35"), "left: 12px; top: 12px", size=12, maxw=440) + vref("NUM 11:35", "right: 12px; bottom: 12px"))
    return page("Numbers 11:33–35 — Kibroth-hattaavah", t, r1 + r2, n)


@P("NUM-C06-P13-Against", "Hath Jehovah Indeed Spoken Only with Moses?")
def p13(n):
    t, h = rows(None, 280)
    r1 = cols(talk(K6.MIRIAM_SCOWL, h[0], RED, [("cap", v("12:1")), ("cap", v("12:2", to="And they said,")), ("say", v("12:2", frm="Hath Jehovah", to="also with us?"))], w=W2, ref="NUM 12:1–2", size=13),
              talk(A10.AARON_PLEAD, h[0], RED, [("cap", v("12:2", frm="And Jehovah heard it."))], w=W2, ref="NUM 12:2", flip=True))
    r2 = talk(A.MOSES_CALM, h[1], GOLDEN, [("cap", v("12:3"))], ref="NUM 12:3")
    return page("Numbers 12:1–3 — Hath Jehovah Indeed Spoken Only with Moses?", t, mk.stamp(12, "right: 40px; top: 36px").replace("position: absolute;", "position: absolute; z-index: 2;") + r1 + r2, n)


@P("NUM-C06-P14-MouthToMouth", "With Him Will I Speak Mouth to Mouth")
def p14(n):
    t, h = rows(360, None)
    r1 = new(SKY, W1, h[0], K6.door_cloud("q14a", W1, h[0], 6141), cap(v("12:4", to="unto Miriam,"), "left: 12px; top: 12px", size=11.5, maxw=440)
             + god(v("12:4", frm="Come out", to="tent of meeting."), "left: 12px; top: 64px", size=17, maxw=400) + cap(v("12:4", frm="And they three") + " " + v("12:5"), "right: 12px; bottom: 30px", size=11.5, maxw=300) + vref("NUM 12:4–5", "right: 12px; bottom: 8px"))
    r2 = night(h[1], cap(v("12:6", to="And he said,"), "left: 12px; top: 12px", size=11) + god(after("12:6", "And he said,") + " " + v("12:7") + " " + v("12:8"), "left: 12px; top: 50px", size=22, maxw=660) + vref("NUM 12:6–8", "right: 12px; bottom: 12px"))
    return page("Numbers 12:4–8 — With Him Will I Speak Mouth to Mouth", t, r1 + r2, n)


@P("NUM-C06-P15-Leprous", "As White as Snow")
def p15(n):
    t, h = rows(300, None)
    r1 = new(SKY, W1, h[0], K6.door_cloud("q15a", W1, h[0], 6151, leprous=True), cap(v("12:9") + " " + v("12:10"), "right: 12px; top: 12px", size=12, maxw=380) + vref("NUM 12:9–10", "right: 12px; bottom: 12px"))
    r2 = cols(new(COLD, W2, h[1], mk.face(K6.MIRIAM_LEPROUS, -40, h[1] - 380 + 8, 1.0), ""),
              talk(A10.AARON_PLEAD, h[1], BLUE, [("cap", v("12:11", to="unto Moses,")), ("say", after("12:11", "unto Moses,") + " " + v("12:12"))], w=W2, ref="NUM 12:11–12", size=13, flip=True))
    return page("Numbers 12:9–12 — As White as Snow", t, r1 + r2, n)


@P("NUM-C06-P16-SevenDays", "Shut Up without the Camp Seven Days")
def p16(n):
    t, h = rows(200, 300, None)
    r1 = talk(A.MOSES_AFRAID, h[0], COLD, [("cap", v("12:13", to="saying,")), ("say", after("12:13", "saying,"))], ref="NUM 12:13", size=20)
    r2 = night(h[1], cap(v("12:14", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(after("12:14", "unto Moses,"), "left: 12px; top: 50px", size=20, maxw=660) + vref("NUM 12:14", "right: 12px; bottom: 12px"))
    r3 = new(SKY, W1, h[2], K6.miriam_without("q16c", W1, h[2], 6163), cap(v("12:15") + " " + v("12:16"), "right: 12px; top: 12px", size=12.5, maxw=380)
             + vref("NUM 12:15–16", "left: 12px; bottom: 12px") + end_mark("NEXT · THE TWELVE SPIES", "right: 10px; bottom: 10px"))
    return page("Numbers 12:13–16 — Shut Up without the Camp Seven Days", t, r1 + r2 + r3, n)
