"""1 Chronicles volume, Chapter 5 — David King over Israel (1 Chronicles 10–12). Every verse, word for word from ref/eng-asv.
Mount Gilboa (the digest's panels; Saul's death 10:4–6 and 10:9–10 words only, over the mountain and the burning city); the
valiant men of Jabesh and the oak; so Saul died for his trespass (words over the crown laid down); then all Israel at
Hebron — we are thy bone and thy flesh; the stronghold of Zion; the mighty men as roll cells, with the water of the well of
Beth-lehem poured out unto Jehovah; those who came to David to Ziklag, Amasai's word — thine are we, David; the numbers that
came to Hebron to make David king; and three days of eating and drinking, for there was joy in Israel."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below, burning
from faces_ex import F
from sa1.common import over as over1
from sa1 import art as KS1
from sa2.common import over as over2, D as D2
from chr1 import G, art as K
from chr1.common import pack, cp, say, caps, drawn, face, cell, cells, roll, joined, DAVID_KING, DAVID_BOLD, ISRAELITE, COLD, GOLDEN, RED

v, sp = G.v, G.span
from chr1 import ch04 as _prev
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
TAG11, TAG12 = "THE MIGHTY MEN WHOM DAVID HAD · 1 CHRONICLES 11", "THEY THAT CAME TO DAVID · 1 CHRONICLES 12"
AMASAI = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#6A5A3A", cord=True, light="#FFF4C2")


@P("1CH-C05-00-Title", "Chapter 5 · David King over Israel", title=True)
def title(n):
    bg, art = D2("A2", 0)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#FFB04A"></rect><g transform="translate(0 300)">{art(760, 780)}</g>')
    return chapter_title(5, "第五話", "David King over Israel", "1 Chronicles 10 – 12", svg, "#C8702A", v("11:3", frm="and they anointed David"), "1 Chronicles · Volume Thirteen")


SEGS = [over1([caps("10:1-3")], "1CHR 10:1–3", "B10", 0, head="Mount Gilboa", stamp=10),
        over1([cp("10:4", to="unto his armor-bearer,"), say("10:4", frm="Draw thy sword,", to="abuse me."), cp("10:4", frm="But his armor-bearer"), caps("10:5-6")], "1CHR 10:4–6", "B10", 1),
        drawn([caps("10:7-10")], "1CHR 10:7–10", lambda w, h: burning(w, h, 501, city="beth-shan"), "#2A0A0A"),
        drawn([caps("10:11-12")], "1CHR 10:11–12", below(lambda w, h: K.oak_jabesh(w, h, 502), 0.24), "#2A1A3A"),
        drawn([caps("10:13-14")], "1CHR 10:13–14", below(lambda w, h: K.K2.crown_bracelet(w, h, 503), 0.3), "#3A1A2A")]
PG.extend(pack(SEGS, "1CH-C05-D", PG.next()))
SEGS2 = [face([cp("11:1", to="saying,"), joined("say", ("11:1", "Behold,"), "11:2")], "1CHR 11:1–2", ISRAELITE, head="King over All Israel", stamp=11),
         over2([caps("11:3")], "1CHR 11:3", "A2", 1),
         drawn([caps("11:4"), cp("11:5", to="said to David,"), say("11:5", frm="Thou shalt not", to="hither."), cp("11:5", frm="Nevertheless")], "1CHR 11:4–5",
               below(lambda w, h: K.K2.jebus("jb5", w, h, 504), 0.36), "#8FD0E2", head="The Stronghold of Zion"),
         face([cp("11:6", to="And David said,"), say("11:6", frm="Whosoever", to="captain."), cp("11:6", frm="And Joab")], "1CHR 11:6", DAVID_KING),
         over2([caps("11:7-9")], "1CHR 11:7–9", "A2", 3)]
PG.extend(pack(SEGS2, "1CH-C05-E", PG.next()))
R = [cell("The Chief of the Thirty", "11:10-11", "#FFD23F", head="The Mighty Men"), cell("Eleazar the Son of Dodo", "11:12-14", "#FFB04A")]
PG.extend(roll(R, "1CH-C05-R", PG.next(), TAG11))
SEGS3 = [drawn([caps("11:15-16")], "1CHR 11:15–16", lambda w, h: KS1.adullam("ad5", w, h, 505), "#2A1A14", head="The Well of Beth-lehem"),
         face([cp("11:17", to="and said,"), say("11:17", frm="Oh that")], "1CHR 11:17", DAVID_KING),
         drawn([caps("11:18")], "1CHR 11:18", below(lambda w, h: K.K2.well_gate("wg5", w, h, 506, pour=True), 0.3), "#E8B880"),
         face([cp("11:19", to="and said,"), say("11:19", frm="My God forbid", to="they brought it."), cp("11:19", frm="Therefore he would not")], "1CHR 11:19", DAVID_KING)]
PG.extend(pack(SEGS3, "1CH-C05-F", PG.next()))
R2 = ([cell("Abishai the Brother of Joab", "11:20-21", "#FFD23F", head="Chief of the Three"), cell("Benaiah the Son of Jehoiada", "11:22-25", "#FFD23F")]
      + cells(11, 26, 47, "The Mighty Men of the Armies", "#8FD0E2", head="The Mighty Men of the Armies", budget=330))
PG.extend(roll(R2, "1CH-C05-S", PG.next(), TAG11))
R3 = (cells(12, 1, 7, "Of Saul's Brethren of Benjamin", "#FFD23F", head="They That Came to David to Ziklag", budget=620)
      + cells(12, 8, 15, "The Gadites", "#8FD0E2", budget=520))
PG.extend(roll(R3, "1CH-C05-T", PG.next(), TAG12))
SEGS4 = [face([caps("12:16"), cp("12:17", to="said unto them,"), say("12:17", frm="If ye be come")], "1CHR 12:16–17", DAVID_BOLD, head="Thine Are We, David", stamp=12),
         face([cp("12:18", to="and he said,"), say("12:18", frm="Thine are we,", to="helpeth thee."), cp("12:18", frm="Then David received")], "1CHR 12:18", AMASAI)]
PG.extend(pack(SEGS4, "1CH-C05-G", PG.next()))
R4 = cells(12, 19, 22, "Of Manasseh", "#FFB04A", head="To Make David King", budget=620) + cells(12, 23, 37, "To Hebron", "#FFD23F", budget=420)
PG.extend(roll(R4, "1CH-C05-U", PG.next(), TAG12, most=4))
SEGS5 = [over2([caps("12:38")], "1CHR 12:38", "A2", 0, head="There Was Joy in Israel"),
         drawn([caps("12:39-40")], "1CHR 12:39–40", below(lambda w, h: K.bringing("br5", w, h, 507), 0.3), "#FFE680")]
PG.extend(pack(SEGS5, "1CH-C05-H", PG.next(), end=end_mark("NEXT · THE ARK OF GOD", "right: 40px; bottom: 50px")))
