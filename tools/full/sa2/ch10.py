"""2 Samuel volume, Chapter 10 — The King Returned (2 Samuel 19–20). Every verse, word for word from ref/asv.
The victory turned into mourning (the digest's gate by night); Joab: thou lovest them that hate thee; the king sitting in the
gate; the men of Judah bring the king back over the Jordan; Shimei fallen before him — thou shalt not die; Mephibosheth
unwashed; Barzillai fourscore years old; the ten parts in the king; Sheba's trumpet — every man to his tents; Amasa at the
great stone in Gibeon (20:10–12 words over the empty highway and a garment in the field); the wise woman of Abel (20:22
words over the wall); and the officers of the king."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from sa2 import G, art as K
from sa2.common import (pack, say, cp, says, caps, over, face, drawn, D, F, DAVID_OLD, DAVID_OLD_WEEP, JOAB, ABISHAI, ISRAELITE, MEPHIBOSHETH, RED, COLD, GOLDEN)
from sa2 import ch09 as _prev

v, sp = G.v, G.span
SHIMEI_LOW = F("adam", skin="#C47A5A", shadow="#5A2A1E", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#6A5A3A", brow="sorrow", sweat=True, light="#9AA8C8")
BARZILLAI = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#E8E2D6", hl="#F3EFE6", beard=True, beard_color="#E8E2D6", scarf="#8A6A3A", cord=True, light="#FFE680")
WISE = F("eve", skin="#C98E66", shadow="#5A3A3A", hair="#3A2A20", scarf="#2A6A5A", light="#FFE680")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("2SA-C10-00-Title", "Chapter 10 · The King Returned", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 340)">{K.ferry("t10", 760, 740, 1001)}</g>')
    return chapter_title(10, "第十話", "The King Returned", "2 Samuel 19 – 20", svg, "#2C7DA8", v("19:15", to="came to the Jordan."), "2 Samuel · Volume Ten")


SEGS = [over([caps("19:1-3")], "2SAM 19:1–3", "B8", 1, head="The Victory Was Turned into Mourning", stamp=19),
        face([cp("19:4", to="with a loud voice,"), say("19:4", frm="O my son")], "2SAM 19:4", DAVID_OLD_WEEP, bg=COLD),
        face([cp("19:5", to="and said,"), ("say", v("19:5", frm="Thou hast shamed") + " " + sp("19:6-7"))], "2SAM 19:5–7", JOAB, bg=RED),
        drawn([cp("19:8", to="saying,"), say("19:8", frm="Behold, the king", to="in the gate:"), cp("19:8", frm="and all the people came")], "2SAM 19:8",
              below(lambda w, h: K.gate_king("gk10", w, h, 1002), 0.24), "#C8B8A0"),
        face([cp("19:9", to="saying,"), ("say", v("19:9", frm="The king delivered") + " " + v("19:10"))], "2SAM 19:9–10", ISRAELITE, head="Bring the King Back"),
        face([cp("19:11", to="saying,"), ("say", v("19:11", frm="Speak unto") + " " + sp("19:12-13"))], "2SAM 19:11–13", DAVID_OLD),
        drawn([cp("19:14", to="saying,"), say("19:14", frm="Return thou,"), caps("19:15")], "2SAM 19:14–15", below(lambda w, h: K.jordan_dawn("jd10", w, h, 1003), 0.3), "#5A5A8A"),
        drawn([caps("19:16-18")], "2SAM 19:16–18", below(lambda w, h: K.ferry("fy10", w, h, 1004), 0.3), "#8FD0E2", head="Shimei"),
        face([cp("19:19", to="unto the king,"), ("say", v("19:19", frm="Let not") + " " + v("19:20"))], "2SAM 19:19–20", SHIMEI_LOW, bg=COLD),
        face([cp("19:21", to="and said,"), say("19:21", frm="Shall not")], "2SAM 19:21", ABISHAI, bg=RED),
        face([cp("19:22", to="And David said,"), say("19:22", frm="What have I"), cp("19:23", to="unto Shimei,"), say("19:23", frm="Thou shalt not die.", to="Thou shalt not die."),
              cp("19:23", frm="And the king sware")], "2SAM 19:22–23", DAVID_OLD),
        face([caps("19:24"), cp("19:25", to="said unto him,"), say("19:25", frm="Wherefore wentest")], "2SAM 19:24–25", MEPHIBOSHETH, bg=COLD, head="Mephibosheth"),
        face([cp("19:26", to="And he answered,"), ("say", v("19:26", frm="My lord,") + " " + sp("19:27-28"))], "2SAM 19:26–28", MEPHIBOSHETH, bg=COLD),
        face([cp("19:29", to="said unto him,"), say("19:29", frm="Why speakest"), cp("19:30", to="unto the king,"), say("19:30", frm="yea,")], "2SAM 19:29–30", DAVID_OLD),
        face([caps("19:31-32"), cp("19:33", to="unto Barzillai,"), say("19:33", frm="Come thou")], "2SAM 19:31–33", BARZILLAI, head="Barzillai"),
        face([cp("19:34", to="unto the king,"), ("say", v("19:34", frm="How many") + " " + sp("19:35-37"))], "2SAM 19:34–37", BARZILLAI),
        face([cp("19:38", to="And the king answered,"), say("19:38", frm="Chimham"), caps("19:39-40")], "2SAM 19:38–40", DAVID_OLD),
        face([cp("19:41", to="and said unto the king,"), say("19:41", frm="Why have")], "2SAM 19:41", ISRAELITE, bg=RED, head="Ten Parts in the King"),
        drawn([cp("19:42", to="the men of Israel,"), say("19:42", frm="Because the king"), cp("19:43", to="and said,"), say("19:43", frm="We have ten parts", to="our king?"),
               cp("19:43", frm="And the words")], "2SAM 19:42–43", below(lambda w, h: K.judah_israel("ji10", w, h, 1005), 0.36), "#E8B880"),
        drawn([cp("20:1", to="and said,"), say("20:1", frm="We have no portion"), caps("20:2")], "2SAM 20:1–2", lambda w, h: K.sheba("sb10", w, h, 1006), "#5A3A5A",
              head="Sheba the Son of Bichri", stamp=20),
        drawn([caps("20:3")], "2SAM 20:3", lambda w, h: K.ward(w, h, 1007), "#3A3A5A"),
        face([cp("20:4", to="to Amasa,"), say("20:4", frm="Call me"), caps("20:5"), cp("20:6", to="to Abishai,"), say("20:6", frm="Now will")], "2SAM 20:4–6", DAVID_OLD),
        drawn([caps("20:7")], "2SAM 20:7", lambda w, h: K.dawn_hebron("dh10", w, h, 1008), "#2A2A5A"),
        drawn([caps("20:8"), cp("20:9", to="to Amasa,"), say("20:9", frm="Is it well", to="my brother?"), cp("20:9", frm="And Joab took")], "2SAM 20:8–9",
              below(lambda w, h: K.great_stone("gs10", w, h, 1009), 0.3), "#C8B8A0", head="The Great Stone in Gibeon"),
        drawn([caps("20:10"), cp("20:11", to="and said,"), say("20:11", frm="He that favoreth"), caps("20:12-13")], "2SAM 20:10–13", lambda w, h: K.highway(w, h, 1010), "#5A4A5A"),
        drawn([caps("20:14-15")], "2SAM 20:14–15", lambda w, h: K.abel_siege("ab10", w, h, 1011), "#8FD0E2", head="A Wise Woman of Abel"),
        face([cp("20:16", to="out of the city,"), say("20:16", frm="Hear, hear;"), cp("20:17", to="and the woman said,"), say("20:17", frm="Art thou Joab?", to="Art thou Joab?"),
              cp("20:17", frm="And he answered,", to="And he answered,"), say("20:17", frm="I am.", to="I am."), cp("20:17", frm="Then she said unto him,", to="said unto him,"),
              say("20:17", frm="Hear the words", to="thy handmaid."), cp("20:17", frm="And he answered,", to="And he answered,", after="thy handmaid."), say("20:17", frm="I do hear.")],
             "2SAM 20:16–17", WISE),
        face([cp("20:18", to="saying,"), ("say", v("20:18", frm="They were wont") + " " + v("20:19"))], "2SAM 20:18–19", WISE),
        face([cp("20:20", to="and said,"), ("say", v("20:20", frm="Far be it,") + " " + v("20:21", to="depart from the city.")), cp("20:21", frm="And the woman said unto Joab,", to="unto Joab,"),
              say("20:21", frm="Behold, his head")], "2SAM 20:20–21", JOAB),
        drawn([caps("20:22")], "2SAM 20:22", lambda w, h: K.abel_siege("ab10b", w, h, 1012, battering=False), "#8FD0E2"),
        drawn([caps("20:23-26")], "2SAM 20:23–26", below(lambda w, h: K.court("ct10", w, h, 1013), 0.3), "#5A2A1E", head="The Officers of the King")]
PG.extend(pack(SEGS, "2SA-C10-D", PG.next(), end=end_mark("NEXT · JEHOVAH IS MY ROCK", "right: 10px; bottom: 34px")))
