"""2 Samuel volume, Chapter 5 — Mephibosheth (2 Samuel 9–10). Every verse, word for word from ref/asv.
Is there yet any that is left of the house of Saul?; Ziba; Mephibosheth fallen on his face — fear not; such a dead dog as
I am; he shall eat at my table as one of the king's sons (the digest's Mephibosheth page throughout). Then Hanun and the
comforters shamed (10:4 words over the men waiting at Jericho under the palms); the battle before the gate of Rabbah as a
technical map; be of good courage, and let us play the man; and the Syrians at Helam."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos import art as JA
from jos.art import below
from sa2 import G, art as K
from sa2.common import (pack, say, cp, says, caps, over, face, drawn, D, F, DAVID_KING, MEPHIBOSHETH, JOAB, RED, COLD, GOLDEN)
from sa2 import ch04 as _prev

v, sp = G.v, G.span
ZIBA = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#7A5A3A", cord=True, light="#FFC14D")
AMMONITE = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#2A5A4A", band=True, brow="scowl", light="#D7261E")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("2SA-C05-00-Title", "Chapter 5 · Mephibosheth", title=True)
def title(n):
    bg, art = D("A6", 3)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#5A2A1E"></rect><g transform="translate(0 340)">{art(760, 740)}</g>')
    return chapter_title(5, "第五話", "Mephibosheth", "2 Samuel 9 – 10", svg, "#5A2A1E", v("9:7", frm="thou shalt eat bread"), "2 Samuel · Volume Ten")


SEGS = [face([cp("9:1", to="And David said,"), say("9:1", frm="Is there yet")], "2SAM 9:1", DAVID_KING, head="For Jonathan's Sake", stamp=9),
        drawn([cp("9:2", to="said unto him,"), say("9:2", frm="Art thou Ziba?", to="Art thou Ziba?"), cp("9:2", frm="And he said,", to="And he said,"), say("9:2", frm="Thy servant is he."),
              cp("9:3", to="And the king said,"), say("9:3", frm="Is there not", to="unto him?"), cp("9:3", frm="And Ziba said", to="unto the king,"), say("9:3", frm="Jonathan hath")],
             "2SAM 9:2–3", below(lambda w, h: K.audience("au5", w, h, 504), 0.5), "#5A2A1E"),
        face([cp("9:4", to="said unto him,"), say("9:4", frm="Where is he?", to="Where is he?"), cp("9:4", frm="And Ziba said", to="unto the king,"), say("9:4", frm="Behold,"), caps("9:5")],
             "2SAM 9:4–5", ZIBA),
        over([cp("9:6", to="did obeisance."), cp("9:6", frm="And David said,", to="And David said,"), say("9:6", frm="Mephibosheth.", to="Mephibosheth."), cp("9:6", frm="And he answered,", to="And he answered,"),
              say("9:6", frm="Behold, thy servant!")], "2SAM 9:6", "A6", 1),
        face([cp("9:7", to="said unto him,"), say("9:7", frm="Fear not;")], "2SAM 9:7", DAVID_KING, head="Thou Shalt Eat Bread at My Table"),
        face([cp("9:8", to="and said,"), say("9:8", frm="What is thy servant,")], "2SAM 9:8", MEPHIBOSHETH, bg=COLD),
        face([cp("9:9", to="and said unto him,"), ("say", v("9:9", frm="All that") + " " + v("9:10", to="at my table.")), cp("9:10", frm="Now Ziba had")], "2SAM 9:9–10", DAVID_KING),
        face([cp("9:11", to="unto the king,"), say("9:11", frm="According to all", to="so shall thy servant do."), say("9:11", frm="As for Mephibosheth,", to="As for Mephibosheth,"),
              cp("9:11", frm="said the king,", to="said the king,"), say("9:11", frm="he shall eat"), caps("9:12")], "2SAM 9:11–12", ZIBA),
        over([caps("9:13")], "2SAM 9:13", "A6", 3),
        drawn([caps("10:1"), cp("10:2", to="And David said,"), say("10:2", frm="I will show", to="showed kindness unto me."), cp("10:2", frm="So David sent")], "2SAM 10:1–2",
              below(lambda w, h: K.messengers("ms5", w, h, 501), 0.36), "#8FD0E2", head="Hanun", stamp=10),
        face([cp("10:3", to="their lord,"), say("10:3", frm="Thinkest thou")], "2SAM 10:3", AMMONITE, bg=RED),
        drawn([caps("10:4"), cp("10:5", to="And the king said,"), say("10:5", frm="Tarry at Jericho")], "2SAM 10:4–5", below(lambda w, h: K.jericho_wait("jw5", w, h, 502), 0.3), "#8FD0E2"),
        drawn([caps("10:6-8")], "2SAM 10:6–8", below(lambda w, h: K.ammon_map(w, h, 0), 0.34), MAP, head="Before and Behind"),
        drawn([caps("10:9-10")], "2SAM 10:9–10", below(lambda w, h: K.ammon_map(w, h, 1), 0.22), MAP),
        face([cp("10:11", to="And he said,"), ("say", v("10:11", frm="If the Syrians") + " " + v("10:12"))], "2SAM 10:11–12", JOAB, bg=RED),
        drawn([caps("10:13-14")], "2SAM 10:13–14", below(lambda w, h: K.ammon_map(w, h, 2), 0.26), MAP),
        drawn([caps("10:15-19")], "2SAM 10:15–19", lambda w, h: JA.chariots("hl5", w, h, 503), "#8FD0E2", head="Helam")]
PG.extend(pack(SEGS, "2SA-C05-D", PG.next(), end=end_mark("NEXT · THOU ART THE MAN", "right: 10px; bottom: 34px")))
