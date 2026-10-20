"""2 Samuel volume, Chapter 12 — Which Cost Me Nothing (2 Samuel 23–24), the last chapter of 2 Samuel. Every verse, word for
word from ref/eng-asv. The last words of David in song boxes; the mighty men as roll cells, with the water of the well of
Beth-lehem poured out unto Jehovah as story panels; then the numbering (Joab's route as a technical map, the sum as a tally
board), Gad and the three things, the pestilence (24:15 words over the silent tents), the angel by the threshing-floor —
it is enough; and the threshing-floor of Araunah bought at a price (the digest's panels)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from rolls import roll_pages, verse_cells
from deu.common import shade
from jos.art import below
from sa1 import art as K1
from sa2 import G, art as K
from sa2.common import (pack, say, gd, cp, sg, sgs, says, gods, caps, over, face, drawn, D, F, DAVID_OLD, DAVID_OLD_ALARM, DAVID_OLD_WEEP, JOAB, GAD, RED, COLD, GOLDEN)
from sa2 import ch11 as _prev

v, sp = G.v, G.span
ARAUNAH = F("adam", skin="#C98E66", shadow="#5A3A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#C8A06A", cord=True, light="#FFE680")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("2SA-C12-00-Title", "Chapter 12 · Which Cost Me Nothing", title=True)
def title(n):
    bg, art = D("B9", 2)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#FFB04A"></rect><g transform="translate(0 300)">{art(760, 780)}</g>')
    return chapter_title(12, "第十二話", "Which Cost Me Nothing", "2 Samuel 23 – 24", svg, "#C8702A", v("24:25", frm="So Jehovah was entreated"), "2 Samuel · Volume Ten")


SEGS = [face([cp("23:1", to="the last words of David."), sg("23:1", frm="David the son of Jesse"), sg("23:2"), sg("23:3")], "2SAM 23:1–3", DAVID_OLD, head="The Last Words of David", stamp=23),
        drawn(sgs("23:4-5"), "2SAM 23:4–5", lambda w, h: K.large_place(w, h, 1201), "#8FD0E2"),
        drawn(sgs("23:6-7"), "2SAM 23:6–7", lambda w, h: K.barley_fire(w, h, 1202), "#3A1A1A")]
PG.extend(pack(SEGS, "2SA-C12-D", PG.next()))
MIGHTY = [("Josheb-basshebeth", v("23:8"), "2SAM 23:8", "#FFD23F", "The Mighty Men"),
          ("Eleazar the Son of Dodai", sp("23:9-10"), "2SAM 23:9–10", "#FFB04A", None),
          ("Shammah the Son of Agee", sp("23:11-12"), "2SAM 23:11–12", "#FFB04A", None)]
PG.extend(roll_pages(MIGHTY, "2SA-C12-R", PG.next(), "2 Samuel", "2SAM", tag="THE MIGHTY MEN WHOM DAVID HAD · 2 SAMUEL 23"))
SEGS2 = [drawn([caps("23:13-14")], "2SAM 23:13–14", lambda w, h: K1.adullam("ad12", w, h, 1203), "#2A1A14", head="The Well of Beth-lehem"),
         face([cp("23:15", to="and said,"), say("23:15", frm="Oh that")], "2SAM 23:15", DAVID_OLD),
         drawn([caps("23:16")], "2SAM 23:16", below(lambda w, h: K.well_gate("wg12", w, h, 1204), 0.2), "#E8B880"),
         drawn([cp("23:17", to="And he said,"), say("23:17", frm="Be it far from me,", to="their lives?"), cp("23:17", frm="therefore he would not")], "2SAM 23:17",
               below(lambda w, h: K.well_gate("wg12b", w, h, 1205, pour=True), 0.3), "#E8B880")]
PG.extend(pack(SEGS2, "2SA-C12-E", PG.next()))
MIGHTY2 = ([("Abishai the Brother of Joab", sp("23:18-19"), "2SAM 23:18–19", "#FFD23F", "Chief of the Three"),
            ("Benaiah the Son of Jehoiada", sp("23:20-23"), "2SAM 23:20–23", "#FFD23F", None)]
           + verse_cells(G, "2SAM", 23, 24, 39, "The Thirty", "#8FD0E2", head="The Thirty", budget=260))
PG.extend(roll_pages(MIGHTY2, "2SA-C12-S", PG.next(), "2 Samuel", "2SAM", tag="THE MIGHTY MEN WHOM DAVID HAD · 2 SAMUEL 23"))
SEGS3 = [drawn([cp("24:1", to="saying,"), gd("24:1", frm="Go, number")], "2SAM 24:1", lambda w, h: K.nathan_night(w, h, 1206), "#0F0E2A", head="Go, Number Israel", stamp=24),
         face([cp("24:2", to="who was with him,"), say("24:2", frm="Go now")], "2SAM 24:2", DAVID_OLD),
         face([cp("24:3", to="unto the king,"), say("24:3", frm="Now Jehovah"), caps("24:4")], "2SAM 24:3–4", JOAB, bg=RED),
         drawn([caps("24:5-8")], "2SAM 24:5–8", below(lambda w, h: K.census_map(w, h), 0.28), MAP),
         drawn([caps("24:9")], "2SAM 24:9", below(lambda w, h: K.sum_board(w, h), 0.24), "#1A1430"),
         face([cp("24:10", to="And David said unto Jehovah,"), say("24:10", frm="I have sinned")], "2SAM 24:10", DAVID_OLD_WEEP, bg=COLD),
         face([caps("24:11"), gods("24:12")], "2SAM 24:11–12", GAD, head="The Prophet Gad"),
         face([cp("24:13", to="and said unto him,"), say("24:13", frm="Shall seven years")], "2SAM 24:13", GAD),
         face([cp("24:14", to="unto Gad,"), say("24:14", frm="I am in")], "2SAM 24:14", DAVID_OLD_ALARM, bg=COLD),
         drawn([caps("24:15")], "2SAM 24:15", lambda w, h: K.pestilence(w, h, 1207), "#1A1A2A"),
         drawn([cp("24:16", to="that destroyed the people,"), gd("24:16", frm="It is enough;", to="stay thy hand."), cp("24:16", frm="And the angel of Jehovah")], "2SAM 24:16",
               lambda w, h: K.angel_city("ac12", w, h, 1208), "#2A1A3A", head="It Is Enough"),
         face([cp("24:17", to="and said,"), say("24:17", frm="Lo, I have sinned,")], "2SAM 24:17", DAVID_OLD_WEEP, bg=COLD),
         face([cp("24:18", to="and said unto him,"), say("24:18", frm="Go up,"), caps("24:19")], "2SAM 24:18–19", GAD, head="The Threshing-floor of Araunah"),
         drawn([caps("24:20"), cp("24:21", to="And Araunah said,"), say("24:21", frm="Wherefore", to="his servant?"), cp("24:21", frm="And David said,", to="And David said,"), say("24:21", frm="To buy")],
               "2SAM 24:20–21", below(lambda w, h: K.araunah("ar12", w, h, 1209), 0.36), "#8FD0E2"),
         face([cp("24:22", to="unto David,"), ("say", v("24:22", frm="Let my lord") + " " + v("24:23", to="unto the king.")), cp("24:23", frm="And Araunah said unto the king,", to="unto the king,"),
               say("24:23", frm="Jehovah thy God")], "2SAM 24:22–23", ARAUNAH),
         over([cp("24:24", to="unto Araunah,"), say("24:24", frm="Nay;", to="cost me nothing."), cp("24:24", frm="So David bought")], "2SAM 24:24", "B9", 1),
         drawn([caps("24:25")], "2SAM 24:25", below(lambda w, h: K.altar_floor("af12", w, h, 1210), 0.2), "#FFB04A")]
PG.extend(pack(SEGS3, "2SA-C12-F", PG.next(), end=end_mark("END OF 2 SAMUEL · NEXT · 1 KINGS", "right: 10px; bottom: 34px", ch="完")))
