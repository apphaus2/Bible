"""1 Chronicles volume, Chapter 8 — The Threshing-floor of Ornan (1 Chronicles 21–22). Every verse, word for word from ref/asv.
Satan moves David to number Israel; Joab's protest and the sum as a tally board; I have done very foolishly; Gad and the
three things; the pestilence (21:14 words over the silent tents); it is enough, now stay thy hand; the angel with his sword
stretched out over Jerusalem, David and the elders in sackcloth on their faces; Ornan's threshing-floor bought for the full
price — I will not offer a burnt-offering without cost; the answer by fire from heaven; then this is the house of Jehovah
God: the stores of gold, silver, brass, iron and cedar, and David's charge to Solomon and to the princes."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from faces_ex import F
from chr1 import G, art as K
from chr1.common import (pack, cp, say, gd, says, gods, caps, drawn, face, joined, DAVID_OLD, DAVID_OLD_ALARM, DAVID_OLD_WEEP, JOAB, GAD, SOLOMON, COLD, GOLDEN, RED)
from chr1 import ch07 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
ORNAN = F("adam", skin="#C98E66", shadow="#5A3A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#C8A06A", cord=True, light="#FFE680")


@P("1CH-C08-00-Title", "Chapter 8 · The Threshing-floor of Ornan", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.fire_altar("t8", 760, 820, 801)}</g><rect x="0" y="0" width="760" height="262" fill="#7A2A0A"></rect>')
    return chapter_title(8, "第八話", "The Threshing-floor of Ornan", "1 Chronicles 21 – 22", svg, "#7A2A0A", v("21:24", frm="nor offer a burnt-offering"), "1 Chronicles · Volume Thirteen")


SEGS = [drawn([caps("21:1"), cp("21:2", to="the princes of the people,"), say("21:2", frm="Go, number")], "1CHR 21:1–2", lambda w, h: K.K2.storm(w, h, 802), "#0B0B2A",
              head="Go, Number Israel", stamp=21),
        face([cp("21:3", to="And Joab said,"), say("21:3", frm="Jehovah make"), caps("21:4")], "1CHR 21:3–4", JOAB, bg=RED),
        drawn([caps("21:5-6")], "1CHR 21:5–6", below(lambda w, h: K.tally(w, h, [("ISRAEL", "1,100,000", "#8FD0E2"), ("JUDAH", "470,000", "#FFD23F")],
                                                                            "LEVI AND BENJAMIN COUNTED HE NOT"), 0.34), "#1A1430"),
        face([caps("21:7"), cp("21:8", to="unto God,"), say("21:8", frm="I have sinned")], "1CHR 21:7–8", DAVID_OLD_WEEP, bg=COLD),
        face([caps("21:9"), gods("21:10")], "1CHR 21:9–10", GAD, head="Gad, David's Seer"),
        face([cp("21:11", to="said unto him,"), joined("say", ("21:11", "Thus saith Jehovah,"), "21:12")], "1CHR 21:11–12", GAD),
        face([cp("21:13", to="unto Gad,"), say("21:13", frm="I am in")], "1CHR 21:13", DAVID_OLD_ALARM, bg=COLD),
        drawn([caps("21:14")], "1CHR 21:14", lambda w, h: K.K2.pestilence(w, h, 803), "#1A1A2A"),
        drawn([cp("21:15", to="to the destroying angel,"), gd("21:15", frm="It is enough;", to="stay thy hand."), cp("21:15", frm="And the angel of Jehovah")], "1CHR 21:15",
              lambda w, h: K.K2.angel_city("ac8", w, h, 804), "#2A1A3A", head="It Is Enough"),
        drawn([caps("21:16")], "1CHR 21:16", lambda w, h: K.sackcloth_elders("se8", w, h, 805), "#2A1A3A"),
        face([cp("21:17", to="unto God,"), say("21:17", frm="Is it not I")], "1CHR 21:17", DAVID_OLD_WEEP, bg=COLD),
        face([caps("21:18-19")], "1CHR 21:18–19", GAD, head="The Threshing-floor of Ornan"),
        drawn([caps("21:20-21")], "1CHR 21:20–21", below(lambda w, h: K.K2.araunah("or8", w, h, 806), 0.3), "#8FD0E2"),
        face([cp("21:22", to="to Ornan,"), say("21:22", frm="Give me")], "1CHR 21:22", DAVID_OLD),
        face([cp("21:23", to="unto David,"), say("21:23", frm="Take it")], "1CHR 21:23", ORNAN),
        face([cp("21:24", to="to Ornan,"), say("21:24", frm="Nay;"), caps("21:25")], "1CHR 21:24–25", DAVID_OLD),
        drawn([caps("21:26")], "1CHR 21:26", lambda w, h: K.fire_altar("fa8", w, h, 807), "#7A2A0A", head="He Answered Him by Fire"),
        drawn([caps("21:27-30")], "1CHR 21:27–30", below(lambda w, h: K.K2.altar_floor("af8", w, h, 808), 0.36), "#FFB04A")]
PG.extend(pack(SEGS, "1CH-C08-D", PG.next()))
SEGS2 = [face([cp("22:1", to="Then David said,"), say("22:1", frm="This is")], "1CHR 22:1", DAVID_OLD, head="This Is the House of Jehovah God", stamp=22),
         drawn([caps("22:2-4")], "1CHR 22:2–4", below(lambda w, h: K.hewers("hw8", w, h, 809), 0.3), "#E8C8A0"),
         face([cp("22:5", to="And David said,"), say("22:5", frm="Solomon my son", to="preparation for it."), cp("22:5", frm="So David prepared")], "1CHR 22:5", DAVID_OLD),
         drawn([caps("22:6"), cp("22:7", to="his son,"), say("22:7", frm="As for me,")], "1CHR 22:6–7", below(lambda w, h: K.charge_son("cs8", w, h, 810), 0.36), "#8A4A26",
               head="Build the House of Jehovah"),
         face([says("22:8-10")], "1CHR 22:8–10", DAVID_OLD),
         face([says("22:11-13")], "1CHR 22:11–13", DAVID_OLD),
         drawn([says("22:14-16")], "1CHR 22:14–16", below(lambda w, h: K.stores(w, h, 811), 0.4), "#3A2A1A"),
         drawn([cp("22:17", to="his son, saying,"), says("22:18-19")], "1CHR 22:17–19", below(lambda w, h: K.charge_son("cs8b", w, h, 812, princes=True), 0.4), "#8A4A26")]
PG.extend(pack(SEGS2, "1CH-C08-E", PG.next(), end=end_mark("NEXT · THE COURSES", "right: 10px; bottom: 34px")))
