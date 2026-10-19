"""2 Chronicles volume, Chapter 6 — Jehoshaphat (2 Chronicles 17–19). Every verse, word for word from ref/asv.
Jehoshaphat who walked in the first ways of David; the princes and Levites teaching in the cities with the book of the law;
the fear of Jehovah on the kingdoms round about; the mighty men numbered; then affinity with Ahab — I am as thou art; the
four hundred prophets and Micaiah the son of Imla (1 Kings' gate of Samaria and the host of heaven); the arrow at a venture
(18:33–34 words over the chariot at sunset); Jehu the seer — shouldest thou help the wicked?; and the judges set city by
city — ye judge not for man, but for Jehovah."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg1.ch14 import ZEDEKIAH as ZEDEKIAH_P
from chr2 import G, art as K
from chr2.common import (pack, cp, say, gd, says, gods, caps, drawn, face, joined, cell, cells, roll, JEHOSHAPHAT, AHAB, AHAB_ANGRY, MICAIAH, MESSENGER, HANANI, COLD, GOLDEN, RED)
from chr2 import ch05 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#0F0E2A"
JEHU_SEER = HANANI


@P("2CH-C06-00-Title", "Chapter 6 · Jehoshaphat", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.two_thrones_gate("t6", 760, 820, 601, horns=True)}</g><rect x="0" y="0" width="760" height="262" fill="#8FD0E2"></rect>')
    return chapter_title(6, "第六話", "Jehoshaphat", "2 Chronicles 17 – 19", svg, "#3A5A7A", v("18:13", frm="As Jehovah liveth,"), "2 Chronicles · Volume Fourteen")


SEGS = [face([caps("17:1-4")], "2CHR 17:1–4", JEHOSHAPHAT, head="Jehoshaphat", stamp=17),
        drawn([caps("17:5-6")], "2CHR 17:5–6", below(lambda w, h: K.asa_idol("ai6", w, h, 602), 0.36), "#3A2A3A"),
        drawn([caps("17:7-9")], "2CHR 17:7–9", below(lambda w, h: K.teachers("te6", w, h, 603), 0.4), "#8FD0E2", head="The Book of the Law of Jehovah"),
        drawn([caps("17:10-13")], "2CHR 17:10–13", below(lambda w, h: K.tribute("tb6", w, h, 604), 0.4), "#FFE680")]
PG.extend(pack(SEGS, "2CH-C06-D", PG.next()))
R = cells(17, 14, 19, "The Mighty Men of Valor", "#FFD23F", head="The Numbering of Them", budget=420)
PG.extend(roll(R, "2CH-C06-R", PG.next(), "THE MEN OF WAR · 2 CHRONICLES 17"))
SEGS2 = [face([caps("18:1-2"), cp("18:3", to="king of Judah,"), say("18:3", frm="Wilt thou", to="Ramoth-gilead?"), cp("18:3", frm="And he answered him,", to="answered him,"),
               say("18:3", frm="I am as thou art,")], "2CHR 18:1–3", AHAB, head="Ramoth-gilead", stamp=18),
         face([cp("18:4", to="unto the king of Israel,"), say("18:4", frm="Inquire first,")], "2CHR 18:4", JEHOSHAPHAT),
         drawn([cp("18:5", to="and said unto them,"), say("18:5", frm="Shall we go", to="forbear?"), cp("18:5", frm="And they said,", to="And they said,"), say("18:5", frm="Go up;"),
                cp("18:6", to="But Jehoshaphat said,"), say("18:6", frm="Is there not")], "2CHR 18:5–6", below(lambda w, h: K.two_thrones_gate("tg6", w, h, 605), 0.44), "#8FD0E2"),
         face([cp("18:7", to="unto Jehoshaphat,"), say("18:7", frm="There is yet", to="the son of Imla."), cp("18:7", frm="And Jehoshaphat said,", to="And Jehoshaphat said,"),
               say("18:7", frm="Let not the king"), cp("18:8", to="and said,"), say("18:8", frm="Fetch quickly")], "2CHR 18:7–8", AHAB_ANGRY, bg=RED, head="Micaiah the Son of Imla"),
         drawn([caps("18:9"), cp("18:10", to="and said,"), say("18:10", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"), say("18:10", frm="With these"), cp("18:11", to="saying,"), say("18:11", frm="Go up")],
               "2CHR 18:9–11", below(lambda w, h: K.two_thrones_gate("tg6b", w, h, 606, horns=True), 0.44), "#8FD0E2"),
         face([cp("18:12", to="saying,"), say("18:12", frm="Behold,"), cp("18:13", to="And Micaiah said,"), say("18:13", frm="As Jehovah liveth,")], "2CHR 18:12–13", MESSENGER),
         face([cp("18:14", to="the king said unto him,"), say("18:14", frm="Micaiah,", to="forbear?"), cp("18:14", frm="And he said,", to="And he said,"), say("18:14", frm="Go ye up,"),
               cp("18:15", to="said to him,"), say("18:15", frm="How many")], "2CHR 18:14–15", AHAB),
         face([cp("18:16", to="And he said,"), say("18:16", frm="I saw all Israel", to="and Jehovah said,"), gd("18:16", frm="These have no master;")], "2CHR 18:16", MICAIAH, bg=COLD,
              head="As Sheep That Have No Shepherd"),
         face([cp("18:17", to="to Jehoshaphat,"), say("18:17", frm="Did I not")], "2CHR 18:17", AHAB_ANGRY, bg=RED),
         drawn([cp("18:18", to="And Micaiah said,"), say("18:18", frm="Therefore hear"), say("18:19", to="And Jehovah said,"), gd("18:19", frm="Who shall entice", to="Ramoth-gilead?"),
                say("18:19", frm="And one spake")], "2CHR 18:18–19", lambda w, h: K.heaven_host(w, h, 607), "#14123A"),
         face([say("18:20", to="and said,"), say("18:20", frm="I will entice him.", to="I will entice him."), say("18:20", frm="And Jehovah said unto him,", to="And Jehovah said unto him,"), gd("18:20", frm="Wherewith?"),
               say("18:21", to="And he said,"), say("18:21", frm="I will go forth,", to="all his prophets."), say("18:21", frm="And he said,", to="And he said,", after="prophets."),
               gd("18:21", frm="Thou shalt entice"), says("18:22")], "2CHR 18:20–22", MICAIAH, bg=NIGHT),
         face([cp("18:23", to="and said,"), say("18:23", frm="Which way"), cp("18:24", to="And Micaiah said,"), say("18:24", frm="Behold,")], "2CHR 18:23–24", ZEDEKIAH_P, bg=RED),
         drawn([cp("18:25", to="And the king of Israel said,"), joined("say", ("18:25", "Take ye Micaiah,"), "18:26"), cp("18:27", to="And Micaiah said,"), say("18:27", frm="If thou return", to="by me."),
                cp("18:27", frm="And he said,", to="And he said,"), say("18:27", frm="Hear, ye peoples,")], "2CHR 18:25–27", below(lambda w, h: K.prison(w, h, 608), 0.4), "#3A3438"),
         face([caps("18:28"), cp("18:29", to="unto Jehoshaphat,"), say("18:29", frm="I will disguise", to="thy robes."), cp("18:29", frm="So the king of Israel disguised")], "2CHR 18:28–29", AHAB,
              head="At a Venture"),
         drawn([cp("18:30", to="saying,"), say("18:30", frm="Fight neither"), cp("18:31", to="that they said,"), say("18:31", frm="It is the king", to="king of Israel."), cp("18:31", frm="Therefore they turned"),
                caps("18:32")], "2CHR 18:30–32", below(lambda w, h: K.ramoth("rm6", w, h, 609), 0.36), "#8FD0E2"),
         drawn([cp("18:33", to="to the driver of the chariot,"), say("18:33", frm="Turn thy hand,"), caps("18:34")], "2CHR 18:33–34", below(lambda w, h: K.ramoth("rm6b", w, h, 610, dusk=True), 0.3), "#2A1A2A")]
PG.extend(pack(SEGS2, "2CH-C06-E", PG.next()))
SEGS3 = [face([caps("19:1"), cp("19:2", to="to king Jehoshaphat,"), say("19:2", frm="Shouldest thou"), says("19:3")], "2CHR 19:1–3", JEHU_SEER, bg=COLD, head="Jehu the Seer", stamp=19),
         drawn([caps("19:4-5"), cp("19:6", to="to the judges,"), joined("say", ("19:6", "Consider what"), "19:7")], "2CHR 19:4–7", below(lambda w, h: K.judges_gate("jg6", w, h, 611), 0.5), "#C8B8A0",
               head="Ye Judge Not for Man"),
         face([caps("19:8"), cp("19:9", to="saying,"), say("19:9", frm="Thus shall ye"), says("19:10-11")], "2CHR 19:8–11", JEHOSHAPHAT)]
PG.extend(pack(SEGS3, "2CH-C06-F", PG.next(), end=end_mark("NEXT · THE BATTLE IS NOT YOURS", "right: 10px; bottom: 34px")))
