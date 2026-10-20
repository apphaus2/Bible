"""2 Chronicles volume, Chapter 13 — Manasseh and Josiah (2 Chronicles 33–34). Every verse, word for word from ref/eng-asv.
Manasseh's altars for the host of heaven in the two courts (33:6 words only); the graven image in the house of God; taken in
chains to Babylon, and in his distress humbling himself greatly — then Manasseh knew that Jehovah he was God; the outer wall
(a plan) and the idol cast out; Amon (33:24 words only); then Josiah, who while yet young began to seek after the God of
David; the purge from Judah to Naphtali; the money for the repairs; I have found the book of the law; the king rent his
clothes; Huldah — because thy heart was tender; the covenant read in the ears of all the people."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr2 import G, art as K
from chr2.common import (pack, cp, say, gd, says, gods, caps, drawn, face, joined, cell, cells, roll, F, MANASSEH, JOSIAH, JOSIAH_GRIEF, HILKIAH, SHAPHAN, HULDAH,
                         COLD, GOLDEN, RED)
from chr2 import ch12 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK, NIGHT = "#0B1A2E", "#14123A"
MANASSEH_HUMBLED = F("adam", skin="#C98E66", shadow="#3A2A4A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#4A4440", brow="sorrow", tear=True, light="#9AA8C8")


@P("2CH-C13-00-Title", "Chapter 13 · Manasseh and Josiah", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.book_found("t13", 760, 820, 1301)}</g><rect x="0" y="0" width="760" height="262" fill="#3A2A1A"></rect>')
    return chapter_title(13, "第十三話", "Manasseh and Josiah", "2 Chronicles 33 – 34", svg, "#3A2A1A", v("34:15", frm="I have found the book", to="house of Jehovah."), "2 Chronicles · Volume Fourteen")


SEGS = [face([caps("33:1-3")], "2CHR 33:1–3", MANASSEH, bg=RED, head="Manasseh", stamp=33),
        drawn([caps("33:4-6")], "2CHR 33:4–6", below(lambda w, h: K.high_places("hp13", w, h, 1302), 0.4), "#3A1A3A"),
        drawn([cp("33:7", to="to David and to Solomon his son,"), joined("god", ("33:7", "In this house,"), "33:8"), caps("33:9")], "2CHR 33:7–9",
              lambda w, h: K.K2.throne_glory(w, h, 1303), NIGHT),
        drawn([caps("33:10-11")], "2CHR 33:10–11", below(lambda w, h: K.chains_babylon("cb13", w, h, 1304), 0.3), "#5A4A5A", head="In Chains to Babylon"),
        face([caps("33:12-13")], "2CHR 33:12–13", MANASSEH_HUMBLED, bg=COLD, head="He Humbled Himself Greatly"),
        drawn([caps("33:14")], "2CHR 33:14", below(lambda w, h: K.outer_wall(w, h), 0.36), INK),
        drawn([caps("33:15-17")], "2CHR 33:15–17", below(lambda w, h: K.asa_idol("ai13", w, h, 1305), 0.44), "#3A2A3A")]
PG.extend(pack(SEGS, "2CH-C13-D", PG.next()))
R = (cells(33, 18, 20, "Manasseh", "#FFD23F", head="The Kings of Judah", budget=620) + cells(33, 21, 25, "Amon, King of Judah", "#FFD23F", budget=640))
PG.extend(roll(R, "2CH-C13-R", PG.next(), "THE KINGS OF JUDAH · 2 CHRONICLES 33"))
SEGS2 = [face([caps("34:1-3")], "2CHR 34:1–3", JOSIAH, head="Josiah", stamp=34),
         drawn([caps("34:4-5")], "2CHR 34:4–5", below(lambda w, h: K.kidron_fire(w, h, 1306), 0.44), "#3A2A3A"),
         drawn([caps("34:6-7")], "2CHR 34:6–7", below(lambda w, h: K.high_places("hp13b", w, h, 1307), 0.3), "#3A1A3A"),
         drawn([caps("34:8-9")], "2CHR 34:8–9", below(lambda w, h: K.chest("ch13", w, h, 1308), 0.5), "#8FD0E2", head="To Repair the House"),
         drawn([caps("34:10-11")], "2CHR 34:10–11", below(lambda w, h: K.repairers("rp13", w, h, 1309), 0.3), "#8FD0E2"),
         drawn([caps("34:12-13")], "2CHR 34:12–13", below(lambda w, h: K.singers("sg13", w, h, 1310, n=7, top=0.5), 0.44), "#FFB04A"),
         drawn([caps("34:14"), cp("34:15", to="to Shaphan the scribe,"), say("34:15", frm="I have found", to="house of Jehovah."), cp("34:15", frm="And Hilkiah delivered")], "2CHR 34:14–15",
               below(lambda w, h: K.book_found("bf13", w, h, 1311), 0.36), "#3A2A1A", head="The Book of the Law"),
         face([cp("34:16", to="saying,"), joined("say", ("34:16", "All that was"), "34:17"), cp("34:18", to="saying,"), say("34:18", frm="Hilkiah the priest", to="a book."),
               cp("34:18", frm="And Shaphan read")], "2CHR 34:16–18", SHAPHAN),
         drawn([caps("34:19-20"), says("34:21")], "2CHR 34:19–21", below(lambda w, h: K.book_found("bf13b", w, h, 1312, reading=True), 0.5), "#3A2A1A"),
         drawn([caps("34:22"), cp("34:23", to="And she said unto them,"), say("34:23", frm="Thus saith Jehovah,", to="the God of Israel:"), gd("34:23", frm="Tell ye")], "2CHR 34:22–23",
               below(lambda w, h: K.huldah("hd13", w, h, 1313), 0.44), "#C8A878", head="Huldah the Prophetess"),
         face([gods("34:24-25")], "2CHR 34:24–25", HULDAH, bg=NIGHT),
         face([say("34:26", to="thus shall ye say to him,"), say("34:26", frm="Thus saith Jehovah,", to="the God of Israel:"), gd("34:26", frm="As touching"), gods("34:27"),
               gd("34:28", to="and upon the inhabitants thereof."), cp("34:28", frm="And they brought back")], "2CHR 34:26–28", HULDAH, bg=NIGHT, head="Because Thy Heart Was Tender"),
         drawn([caps("34:29-30")], "2CHR 34:29–30", below(lambda w, h: K.law_read("lr13", w, h, 1314), 0.44), "#8FD0E2", head="The Book of the Covenant"),
         drawn([caps("34:31-33")], "2CHR 34:31–33", below(lambda w, h: K.covenant_pillar("cp13", w, h, 1315), 0.46), "#8FD0E2")]
PG.extend(pack(SEGS2, "2CH-C13-E", PG.next(), end=end_mark("NEXT · THE SEVENTY YEARS", "right: 10px; bottom: 34px")))
