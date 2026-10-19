"""Esther volume, Chapter 3 — The King Could Not Sleep (Esther 5–7). Every verse, word for word from ref/asv.
On the third day Esther in her royal apparel in the inner court; the golden sceptre held out and the top of it touched — what
wilt thou, queen Esther?; the first banquet of wine; Haman joyful, then full of wrath at Mordecai in the gate; his friends and
Zeresh — let a gallows be made fifty cubits high (the gallows only ever standing, empty); then on that night could not the
king sleep: the book of the records read before him; whom the king delighteth to honor — Haman leading Mordecai on the king's
horse through the street of the city; Haman home mourning, his head covered; the second banquet: let my life be given me at
my petition — an adversary and an enemy, even this wicked Haman; the palace garden; and Harbonah: behold also, the gallows.
Haman's death (7:10) is words only, over the empty gallows far off at dusk."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from jos.art import below
from est import G, art as K
from est.common import (pack, cp, say, says, caps, drawn, face, joined, tshade as shade, AHASUERUS, AHAS_WROTH, AHAS_NIGHT, ESTHER_QUEEN, ESTHER_RESOLVE,
                        HAMAN, HAMAN_GLAD, ZERESH, ZERESH_FEAR, HARBONAH, COLD, GOLDEN, RED)
from est import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#0F0E2A"


@P("EST-C03-00-Title", "Chapter 3 · The King Could Not Sleep", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.bedchamber("t3", 760, 820, 501)}</g><rect x="0" y="0" width="760" height="262" fill="#0F0E2A"></rect>')
    return chapter_title(3, "第三話", "The King Could Not Sleep", "Esther 5 – 7", svg, NIGHT, v("6:1", to="sleep;"), "Esther · Volume Seventeen")


SEGS = [drawn([caps("5:1")], "ESTH 5:1", below(lambda w, h: K.inner_court("ic5", w, h, 502, mirror=True), 0.26), "#C8B08A", head="On the Third Day", stamp=5),
        drawn([caps("5:2")], "ESTH 5:2", below(lambda w, h: K.inner_court("ic5b", w, h, 503, stage="touch", mirror=True), 0.26), "#C8B08A", head="The Golden Sceptre"),
        face([cp("5:3", to="unto her,"), say("5:3", frm="What wilt thou")], "ESTH 5:3", AHASUERUS),
        face([cp("5:4", to="And Esther said,"), say("5:4", frm="If it seem good")], "ESTH 5:4", ESTHER_QUEEN),
        face([cp("5:5", to="Then the king said,"), say("5:5", frm="Cause Haman", to="as Esther hath said."), cp("5:5", frm="So the king and Haman")], "ESTH 5:5", AHASUERUS),
        drawn([cp("5:6", to="at the banquet of wine,"), say("5:6", frm="What is thy petition?")], "ESTH 5:6", below(lambda w, h: K.banquet("bq5", w, h, 504), 0.36), "#C8B08A",
              head="The Banquet of Wine"),
        face([cp("5:7", to="and said,"), say("5:7", frm="My petition"), says("5:8")], "ESTH 5:7–8", ESTHER_QUEEN),
        drawn([caps("5:9")], "ESTH 5:9", below(lambda w, h: K.kings_gate("kg5", w, h, 505, mord="sit", haman_by=True), 0.26), "#8FD0E2", head="Haman Went Forth Joyful"),
        drawn([caps("5:10-11")], "ESTH 5:10–11", below(lambda w, h: K.haman_home("hh5", w, h, 506, tree=False), 0.3), "#FFB04A"),
        face([cp("5:12", to="Haman said moreover,"), say("5:12", frm="Yea, Esther"), says("5:13")], "ESTH 5:12–13", HAMAN_GLAD, bg=RED),
        face([cp("5:14", to="unto him,"), say("5:14", frm="Let a gallows", to="unto the banquet."), cp("5:14", frm="And the thing pleased")], "ESTH 5:14", ZERESH, bg=RED,
             head="A Gallows Fifty Cubits High"),
        drawn([], "ESTH 5:14", lambda w, h: K.haman_home("hh5b", w, h, 507, mood="talk", building=True), "#3A2A5A", h=300)]
PG.extend(pack(SEGS, "EST-C03-D", PG.next()))
SEGS2 = [drawn([caps("6:1-2")], "ESTH 6:1–2", below(lambda w, h: K.bedchamber("bc6", w, h, 601), 0.3), NIGHT, head="On That Night", stamp=6),
         drawn([cp("6:3", to="And the king said,"), say("6:3", frm="What honor", to="for this?"), cp("6:3", frm="Then said the king's servants", to="unto him,"),
                say("6:3", frm="There is nothing")], "ESTH 6:3", below(lambda w, h: K.bedchamber("bc6b", w, h, 602, servants=True), 0.44), NIGHT),
         drawn([cp("6:4", to="And the king said,"), say("6:4", frm="Who is in", to="the court?"), cp("6:4", frm="Now Haman"), cp("6:5", to="said unto him,"),
                say("6:5", frm="Behold, Haman", to="in the court."), cp("6:5", frm="And the king said,", to="said,"), say("6:5", frm="Let him come in.")], "ESTH 6:4–5",
               below(lambda w, h: K.audience("au6", w, h, 603), 0.5), "#E8C8A0", head="Whom the King Delighteth to Honor"),
         drawn([cp("6:6", to="said unto him,"), say("6:6", frm="What shall be done", to="to honor?"), cp("6:6", frm="Now Haman said", to="in his heart,"),
                say("6:6", frm="To whom would")], "ESTH 6:6", below(lambda w, h: K.audience("au6b", w, h, 604), 0.5), "#E8C8A0"),
         face([cp("6:7", to="unto the king,"), say("6:7", frm="For the man"), says("6:8-9")], "ESTH 6:7–9", HAMAN_GLAD, bg=RED),
         drawn([cp("6:10", to="said to Haman,"), say("6:10", frm="Make haste")], "ESTH 6:10", below(lambda w, h: K.audience("au6c", w, h, 605, point=True), 0.4), "#E8C8A0"),
         drawn([caps("6:11")], "ESTH 6:11", below(lambda w, h: K.honour_ride("hr6", w, h, 606), 0.2), "#8FD0E2", head="Thus Shall It Be Done"),
         drawn([caps("6:12")], "ESTH 6:12", below(lambda w, h: K.haman_home("hh6", w, h, 607, mood="mourn"), 0.2), "#3A2A5A"),
         face([cp("6:13", to="unto him,"), say("6:13", frm="If Mordecai")], "ESTH 6:13", ZERESH_FEAR, bg=COLD),
         drawn([caps("6:14")], "ESTH 6:14", below(lambda w, h: K.haman_home("hh6b", w, h, 608, mood="talk", chamberlains=True), 0.2), "#3A2A5A")]
PG.extend(pack(SEGS2, "EST-C03-E", PG.next()))
SEGS3 = [drawn([caps("7:1"), cp("7:2", to="at the banquet of wine,"), say("7:2", frm="What is thy petition")], "ESTH 7:1–2", below(lambda w, h: K.banquet("bq7", w, h, 701), 0.44),
               "#C8B08A", head="The Second Banquet", stamp=7),
         face([cp("7:3", to="answered and said,"), say("7:3", frm="If I have found"), says("7:4")], "ESTH 7:3–4", ESTHER_RESOLVE, head="Let My Life Be Given Me"),
         face([cp("7:5", to="unto Esther the queen,"), say("7:5", frm="Who is he")], "ESTH 7:5", AHAS_WROTH, bg=RED),
         drawn([cp("7:6", to="And Esther said,"), say("7:6", frm="An adversary", to="wicked Haman."), cp("7:6", frm="Then Haman was afraid")], "ESTH 7:6",
               below(lambda w, h: K.banquet("bq7b", w, h, 702, stage="accuse"), 0.36), "#5A3A5A", head="This Wicked Haman"),
         drawn([caps("7:7")], "ESTH 7:7", below(lambda w, h: K.palace_garden("pg7", w, h, 703), 0.3), NIGHT),
         drawn([cp("7:8", to="Then said the king,"), say("7:8", frm="Will he even", to="in the house?"), cp("7:8", frm="As the word")], "ESTH 7:8",
               below(lambda w, h: K.banquet("bq7c", w, h, 704, stage="fallen"), 0.4), "#5A3A5A"),
         face([cp("7:9", to="before the king,"), say("7:9", frm="Behold also", to="house of Haman.")], "ESTH 7:9", HARBONAH, head="Behold Also, the Gallows"),
         drawn([cp("7:9", frm="And the king said,", to="said,"), say("7:9", frm="Hang him thereon."), caps("7:10")], "ESTH 7:9–10",
               below(lambda w, h: K.gallows_far(w, h, 705), 0.4), "#2A1A3A", h=470)]
PG.extend(pack(SEGS3, "EST-C03-F", PG.next(), end=end_mark("NEXT · THE DAYS OF PURIM", "right: 10px; bottom: 34px")))
