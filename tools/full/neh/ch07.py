"""Nehemiah volume, Chapter 7 — The Dedication of the Wall (Nehemiah 12–13), the last chapter of Nehemiah. Every verse, word
for word from ref/asv. The priests and Levites that went up with Zerubbabel, the line of the high priests from Jeshua to
Jaddua (a chart), the heads of fathers' houses in the days of Joiakim (a board of names), all as roll cells; the dedication
of the wall with gladness, cymbals, psalteries and harps; two great companies that gave thanks going round upon the wall
(the plan of the wall with both routes), meeting in the house of God, the joy of Jerusalem heard even afar off; the
portions for the singers and porters; then the book of Moses read — no Ammonite nor Moabite; Tobiah's chamber in the courts
and his household stuff cast forth; the Levites' portions restored; the sabbath kept, the gates shut before it; the
foreign wives (13:25 told in words over the shut gate); and the last prayer — remember me, O my God, for good."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from neh import G, art as K
from neh.common import (pack, cp, say, says, caps, drawn, face, joined, NEHEMIAH_OLD, NEHEMIAH_OLD_STERN, ELIASHIB, LEVITE, COLD, GOLDEN, RED, plan_pages)
from neh import ch06 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, BOARD, SKY, DUSK = "#0B1A2E", "#1A1430", "#8FD0E2", "#3A2A5A"
GOLD_C, CYAN_C, ROSE_C, LILAC = "#FFD23F", "#8FD0E2", "#FF8A6A", "#C8A0E8"
HIGH = ["JESHUA", "JOIAKIM", "ELIASHIB", "JOIADA", "JONATHAN", "JADDUA"]
HOUSES = ["SERAIAH · MERAIAH", "JEREMIAH · HANANIAH", "EZRA · MESHULLAM", "AMARIAH · JEHOHANAN", "MALLUCHI · JONATHAN", "SHEBANIAH · JOSEPH", "HARIM · ADNA",
          "MERAIOTH · HELKAI", "IDDO · ZECHARIAH", "GINNETHON · MESHULLAM", "ABIJAH · ZICHRI", "MINIAMIN …", "MOADIAH · PILTAI", "BILGAH · SHAMMUA", "SHEMAIAH · JEHONATHAN",
          "JOIARIB · MATTENAI", "JEDAIAH · UZZI", "SALLAI · KALLAI", "AMOK · EBER", "HILKIAH · HASHABIAH", "JEDAIAH · NETHANEL"]


@P("NEH-C07-00-Title", "Chapter 7 · The Dedication of the Wall", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 330)">{K.procession("t7", 760, 640, 701)}</g><rect x="0" y="0" width="760" height="332" fill="#FFC890"></rect>'
                '<rect x="0" y="968" width="760" height="120" fill="#C8B08A"></rect>')
    return chapter_title(7, "第七話", "The Dedication of the Wall", "Nehemiah 12 – 13", svg, "#8A5A3A", v("12:43", frm="so that the joy of Jerusalem"), "Nehemiah · Volume Sixteen")


LISTS = [("The Priests and the Levites", lambda w, h: K.lineage(w, h, HIGH, hi=("JESHUA", "JADDUA"), per=6, top=0.5, bot=0.5), 200,
          [("The Priests with Zerubbabel", "12:1-7", GOLD_C), ("The Levites", "12:8-9", CYAN_C), ("Jeshua Begat Joiakim", "12:10-11", ROSE_C)]),
         ("In the Days of Joiakim", lambda w, h: K.names_board(w, h, HOUSES, cols=4, color=GOLD_C), 300,
          [("The Heads of Fathers' Houses", "12:12-21", GOLD_C), ("The Sons of Levi", "12:22-26", CYAN_C)])]
PG.extend(plan_pages(LISTS, "NEH-C07-D", PG.next(), tag="THE PRIESTS AND THE LEVITES · NEHEMIAH 12", stamp=12))
SEGS = [drawn([caps("12:27-29")], "NEH 12:27–29", below(lambda w, h: K.musicians_court("mc7", w, h, 702), 0.4), "#FFB04A", head="The Dedication of the Wall"),
        drawn([caps("12:30")], "NEH 12:30", below(lambda w, h: K.wall_done("wd7", w, h, 703), 0.2), "#FFC890"),
        drawn([caps("12:31-34")], "NEH 12:31–34", below(lambda w, h: K.procession("pr7", w, h, 704), 0.36), "#FFC890", head="Two Great Companies"),
        drawn([caps("12:35-37")], "NEH 12:35–37", below(lambda w, h: K.wall_plan(w, h, lit=("VALLEY GATE", "DUNG GATE", "FOUNTAIN GATE", "WATER GATE"), companies=True), 0.4), MAP),
        drawn([caps("12:38-39")], "NEH 12:38–39", below(lambda w, h: K.procession("pr7b", w, h, 705, second=True), 0.4), "#FFC890"),
        drawn([caps("12:40-42")], "NEH 12:40–42", below(lambda w, h: K.musicians_court("mc7b", w, h, 706), 0.36), "#FFB04A"),
        drawn([caps("12:43")], "NEH 12:43", below(lambda w, h: K.court_scene("cs7", w, h, 707, smoke=True), 0.24), SKY, head="The Joy of Jerusalem"),
        drawn([caps("12:44-45")], "NEH 12:44–45", below(lambda w, h: K.heaps("hp7", w, h, 708), 0.4), SKY),
        drawn([caps("12:46-47")], "NEH 12:46–47", below(lambda w, h: K.night_song("ns7", w, h, 709), 0.36), "#0B0B2A")]
PG.extend(pack(SEGS, "NEH-C07-E", PG.next()))
SEGS2 = [drawn([caps("13:1-3")], "NEH 13:1–3", below(lambda w, h: K.pulpit("pu7", w, h, 710), 0.36), "#FFE6B0", head="On That Day", stamp=13),
         drawn([caps("13:4-5")], "NEH 13:4–5", below(lambda w, h: K.chamber_tobiah("ct7", w, h, 711), 0.4), "#E8DCC0", head="A Chamber for Tobiah"),
         face([caps("13:6-7")], "NEH 13:6–7", NEHEMIAH_OLD),
         drawn([caps("13:8-9")], "NEH 13:8–9", below(lambda w, h: K.cast_out("co7", w, h, 712), 0.24), SKY),
         face([caps("13:10"), cp("13:11", to="and said,"), say("13:11", frm="Why is the house", to="forsaken?"), cp("13:11", frm="And I gathered")], "NEH 13:10–11", NEHEMIAH_OLD_STERN,
              bg=RED, head="Why Is the House of God Forsaken?"),
         drawn([caps("13:12-13")], "NEH 13:12–13", below(lambda w, h: K.heaps("hp7b", w, h, 713), 0.44), SKY),
         face([says("13:14")], "NEH 13:14", NEHEMIAH_OLD, bg=COLD),
         drawn([caps("13:15-16")], "NEH 13:15–16", below(lambda w, h: K.sabbath_work("sw7", w, h, 714), 0.4), SKY, head="The Sabbath Day"),
         face([cp("13:17", to="and said unto them,"), joined("say", ("13:17", "What evil thing"), "13:18")], "NEH 13:17–18", NEHEMIAH_OLD_STERN, bg=RED),
         drawn([caps("13:19-20")], "NEH 13:19–20", below(lambda w, h: K.sabbath_gate("sg7c", w, h, 715), 0.42), DUSK),
         face([cp("13:21", to="and said unto them,"), say("13:21", frm="Why lodge ye", to="lay hands on you."), cp("13:21", frm="From that time")], "NEH 13:21", NEHEMIAH_OLD_STERN, bg=RED),
         face([cp("13:22", to="to sanctify the sabbath day."), say("13:22", frm="Remember unto me")], "NEH 13:22", NEHEMIAH_OLD, bg=COLD),
         drawn([caps("13:23-24")], "NEH 13:23–24", below(lambda w, h: K.strange_wives("sw7b", w, h, 716), 0.3), "#C8B8A0", head="The Speech of Ashdod"),
         drawn([cp("13:25", to="saying,")], "NEH 13:25", below(lambda w, h: K.sabbath_gate("sg7d", w, h, 717, merchants=False), 0.2), DUSK),
         face([say("13:25", frm="Ye shall not give"), joined("say", "13:26", "13:27")], "NEH 13:25–27", NEHEMIAH_OLD_STERN, bg=RED),
         drawn([caps("13:28")], "NEH 13:28", below(lambda w, h: K.departing("dp7", w, h, 718), 0.24), DUSK),
         face([says("13:29")], "NEH 13:29", NEHEMIAH_OLD, bg=COLD, head="Remember Me, O My God, for Good"),
         drawn([caps("13:30"), cp("13:31", to="and for the first-fruits."), say("13:31", frm="Remember me, O my God")], "NEH 13:30–31",
               below(lambda w, h: K.wall_done("wd7b", w, h, 719), 0.36), "#FFC890")]
PG.extend(pack(SEGS2, "NEH-C07-F", PG.next(), end=end_mark("END OF NEHEMIAH · NEXT · ESTHER", "right: 10px; bottom: 34px", ch="完")))
