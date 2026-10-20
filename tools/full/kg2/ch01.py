"""2 Kings volume, Chapter 1 — The Chariot of Fire (2 Kings 1–2). Every verse, word for word from ref/eng-asv.
Ahaziah fallen through the lattice and inquiring of Baal-zebub; is it because there is no God in Israel?; a hairy man girt
with a girdle of leather; the captains of fifty (1:10–12 words over the fire on the slope: nothing of the men drawn); the
third captain on his knees; then Gilgal, Beth-el, Jericho — I will not leave thee; the Jordan divided by the mantle; a double
portion of thy spirit; the chariot of fire and horses of fire, and Elijah going up by a whirlwind — my father, my father;
the mantle that fell from him; the waters healed with salt; and the way to Beth-el (2:24 words over the empty way and the
wood)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from jdg import art as JG
from kg2 import G, art as K
from kg2.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, ELIJAH, ELIJAH_FIRE, ELISHA, ELISHA_BARE, AHAZIAH, CAPTAIN, MESSENGER, SONS_PROPHETS,
                        ISRAELITE, reign, reign_pages, RED, COLD, GOLDEN)

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"


@P("2KI-C01-00-Title", "Chapter 1 · The Chariot of Fire", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#2A1A3A"></rect><g transform="translate(0 300)">{K.whirlwind("t1", 760, 780, 101)}</g>')
    return chapter_title(1, "第一話", "The Chariot of Fire", "2 Kings 1 – 2", svg, "#2A1A3A", v("2:11", frm="and Elijah went up"), "2 Kings · Volume Twelve")


SEGS = [drawn([caps("1:1"), cp("1:2", to="and said unto them,"), say("1:2", frm="Go, inquire")], "2KGS 1:1–2", below(lambda w, h: K.lattice_fall(w, h, 102), 0.3), "#5A4A6A",
              head="Baal-zebub the God of Ekron", stamp=1),
        face([cp("1:3", to="said to Elijah the Tishbite,"), gd("1:3", frm="Arise,"), gd("1:4", to="but shalt surely die."), cp("1:4", frm="And Elijah departed.")], "2KGS 1:3–4", ELIJAH, bg=NIGHT),
        drawn([cp("1:5", to="he said unto them,"), say("1:5", frm="Why is it"), cp("1:6", to="said unto him,"), say("1:6", frm="There came up")], "2KGS 1:5–6",
              below(lambda w, h: K.sickbed("sb1", w, h, 103), 0.46), "#5A2A1E"),
        face([cp("1:7", to="And he said unto them,"), say("1:7", frm="What manner"), cp("1:8", to="And they answered him,"), say("1:8", frm="He was a hairy man,", to="about his loins."),
              cp("1:8", frm="And he said,", to="And he said,"), say("1:8", frm="It is Elijah")], "2KGS 1:7–8", AHAZIAH, bg=COLD, head="A Hairy Man"),
        drawn([cp("1:9", to="And he spake unto him,"), say("1:9", frm="O man of God,")], "2KGS 1:9", below(lambda w, h: K.hilltop("ht1", w, h, 104), 0.2), "#8FD0E2", head="Captains of Fifty"),
        drawn([cp("1:10", to="to the captain of fifty,"), say("1:10", frm="If I be", to="thy fifty."), cp("1:10", frm="And there came down")], "2KGS 1:10",
              lambda w, h: K.hilltop("ht1b", w, h, 105, fire=True), "#2A1A2A"),
        drawn([cp("1:11", to="and said unto him,"), say("1:11", frm="O man of God,"), cp("1:12", to="said unto them,"), say("1:12", frm="If I be", to="thy fifty."), cp("1:12", frm="And the fire of God")],
              "2KGS 1:11–12", below(lambda w, h: K.hilltop("ht1c", w, h, 106, fire=True), 0.36), "#2A1A2A"),
        drawn([cp("1:13", to="and said unto him,"), joined("say", ("1:13", "O man of God,"), "1:14")], "2KGS 1:13–14", below(lambda w, h: K.hilltop("ht1d", w, h, 107, kneel=True), 0.36), "#8FD0E2"),
        face([cp("1:15", to="said unto Elijah,"), gd("1:15", frm="Go down", to="be not afraid of him."), cp("1:15", frm="And he arose,"), cp("1:16", to="And he said unto him,"),
              say("1:16", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"), gd("1:16", frm="Forasmuch")], "2KGS 1:15–16", ELIJAH_FIRE, bg=RED),
        drawn([caps("1:17-18")], "2KGS 1:17–18", lambda w, h: K.sickbed("sb1b", w, h, 115), "#5A2A1E")]
PG.extend(pack(SEGS, "2KI-C01-D", PG.next()))
SEGS2 = [drawn([caps("2:1"), cp("2:2", to="unto Elisha,"), say("2:2", frm="Tarry here,", to="as far as Beth-el."), cp("2:2", frm="And Elisha said,", to="And Elisha said,"), say("2:2", frm="As Jehovah liveth,", to="leave thee."),
                cp("2:2", frm="So they went down")], "2KGS 2:1–2", below(lambda w, h: JG.travellers("tv1", w, h, 108, dusk=False), 0.4), "#8FD0E2", head="I Will Not Leave Thee", stamp=2),
         face([cp("2:3", to="and said unto him,"), say("2:3", frm="Knowest thou", to="to-day?"), cp("2:3", frm="And he said,", to="And he said,"), say("2:3", frm="Yea, I know it;"),
               cp("2:4", to="said unto him,"), say("2:4", frm="Elisha,", to="to Jericho."), cp("2:4", frm="And he said,", to="And he said,"), say("2:4", frm="As Jehovah liveth,", to="leave thee."),
               cp("2:4", frm="So they came")], "2KGS 2:3–4", SONS_PROPHETS),
         face([cp("2:5", to="and said unto him,"), say("2:5", frm="Knowest thou", to="to-day?"), cp("2:5", frm="And he answered,", to="And he answered,"), say("2:5", frm="Yea, I know it;"),
               cp("2:6", to="said unto him,"), say("2:6", frm="Tarry here,", to="to the Jordan."), cp("2:6", frm="And he said,", to="And he said,"), say("2:6", frm="As Jehovah liveth,", to="leave thee."),
               cp("2:6", frm="And they two went on.")], "2KGS 2:5–6", ELISHA),
         drawn([caps("2:7-8")], "2KGS 2:7–8", below(lambda w, h: K.jordan_part("jp1", w, h, 109), 0.24), "#8FD0E2"),
         face([cp("2:9", to="that Elijah said unto Elisha,"), say("2:9", frm="Ask what", to="taken from thee."), cp("2:9", frm="And Elisha said,", to="And Elisha said,"), say("2:9", frm="I pray thee,"),
               cp("2:10", to="And he said,"), say("2:10", frm="Thou hast asked")], "2KGS 2:9–10", ELIJAH, head="A Double Portion"),
         drawn([caps("2:11"), cp("2:12", to="and he cried,"), say("2:12", frm="My father,", to="the horsemen thereof!"), cp("2:12", frm="And he saw him no more:")], "2KGS 2:11–12",
               lambda w, h: K.whirlwind("ww1", w, h, 110), "#2A1A3A", head="The Chariot of Fire"),
         drawn([caps("2:13"), cp("2:14", to="and said,"), say("2:14", frm="Where is Jehovah,", to="the God of Elijah?"), cp("2:14", frm="and when he also")], "2KGS 2:13–14",
               below(lambda w, h: K.jordan_part("jp1b", w, h, 111, two=False), 0.3), "#8FD0E2"),
         face([cp("2:15", to="they said,"), say("2:15", frm="The spirit of Elijah", to="on Elisha."), cp("2:15", frm="And they came to meet him,"), cp("2:16", to="said unto him,"),
               say("2:16", frm="Behold now,", to="into some valley."), cp("2:16", frm="And he said,", to="And he said,"), say("2:16", frm="Ye shall not send.")], "2KGS 2:15–16", SONS_PROPHETS),
         face([cp("2:17", to="he said,"), say("2:17", frm="Send.", to="Send."), cp("2:17", frm="They sent therefore"), cp("2:18", to="and he said unto them,"), say("2:18", frm="Did I not")], "2KGS 2:17–18",
              ELISHA),
         drawn([cp("2:19", to="said unto Elisha,"), say("2:19", frm="Behold, we pray thee,"), cp("2:20", to="And he said,"), say("2:20", frm="Bring me", to="put salt therein."), cp("2:20", frm="And they brought it")],
               "2KGS 2:19–20", below(lambda w, h: K.salt_spring("ss1", w, h, 112), 0.36), "#8FD0E2", head="The Waters Healed"),
         drawn([cp("2:21", to="and said,"), say("2:21", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"), gd("2:21", frm="I have healed"), caps("2:22")], "2KGS 2:21–22",
               below(lambda w, h: K.salt_spring("ss1b", w, h, 113), 0.3), "#8FD0E2"),
         drawn([cp("2:23", to="and said unto him,"), say("2:23", frm="Go up,"), caps("2:24-25")], "2KGS 2:23–25", below(lambda w, h: K.bethel_way("bw1", w, h, 114), 0.36), "#C8B8A0")]
PG.extend(pack(SEGS2, "2KI-C01-E", PG.next(), end=end_mark("NEXT · THE POT OF OIL", "right: 10px; bottom: 34px")))
