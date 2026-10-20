"""1 Kings volume, Chapter 12 — The Fire of Jehovah (1 Kings 18). Every verse, word for word from ref/eng-asv.
In the third year: go, show thyself unto Ahab; Obadiah who hid a hundred prophets by fifty in a cave; is it thou, thou troubler
of Israel?; mount Carmel — how long go ye limping between the two sides?; the prophets of Baal from morning until noon (18:28
words over dark figures about the altar, nothing else drawn); twelve stones, the trench, four jars of water three times; the
fire of Jehovah fell — Jehovah, he is God; the brook Kishon (18:40 words over the empty brook); a cloud as small as a man's
hand, and Elijah running before Ahab to Jezreel."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg1 import G, art as K
from kg1.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, AHAB, AHAB_ANGRY, ELIJAH, ELIJAH_FIRE, OBADIAH, ISRAELITE, RED, COLD, GOLDEN)
from kg1 import ch11 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"


@P("1KI-C12-00-Title", "Chapter 12 · The Fire of Jehovah", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#2A1A3A"></rect><g transform="translate(0 300)">{K.carmel("t12", 760, 780, 1201, stage="fire")}</g>')
    return chapter_title(12, "第十二話", "The Fire of Jehovah", "1 Kings 18", svg, "#2A1A3A", v("18:39", frm="Jehovah, he is God;"), "1 Kings · Volume Eleven")


SEGS = [drawn([cp("18:1", to="saying,"), gd("18:1", frm="Go, show"), caps("18:2")], "1KGS 18:1–2", lambda w, h: K.cherith("cd12", w, h, 1202, dry=True), "#FFE6A0", head="In the Third Year", stamp=18),
        face([caps("18:3-4"), cp("18:5", to="unto Obadiah,"), say("18:5", frm="Go through"), caps("18:6")], "1KGS 18:3–6", AHAB),
        drawn([cp("18:7", to="and said,"), say("18:7", frm="Is it thou,"), cp("18:8", to="And he answered him,"), say("18:8", frm="It is I:")], "1KGS 18:7–8",
              below(lambda w, h: K.obadiah_way("ob12", w, h, 1203), 0.36), "#FFE6A0", head="Obadiah"),
        face([cp("18:9", to="And he said,"), joined("say", ("18:9", "Wherein"), "18:10", "18:11")], "1KGS 18:9–11", OBADIAH, bg=COLD),
        face([says("18:12-14")], "1KGS 18:12–14", OBADIAH, bg=COLD),
        face([cp("18:15", to="And Elijah said,"), say("18:15", frm="As Jehovah of hosts"), caps("18:16")], "1KGS 18:15–16", ELIJAH),
        face([cp("18:17", to="said unto him,"), say("18:17", frm="Is it thou,")], "1KGS 18:17", AHAB_ANGRY, bg=RED, head="Thou Troubler of Israel"),
        face([cp("18:18", to="And he answered,"), joined("say", ("18:18", "I have not"), "18:19"), caps("18:20")], "1KGS 18:18–20", ELIJAH_FIRE, bg=RED),
        drawn([cp("18:21", to="and said,"), say("18:21", frm="How long", to="follow him."), cp("18:21", frm="And the people answered"), cp("18:22", to="unto the people,"), say("18:22", frm="I, even I")],
              "1KGS 18:21–22", below(lambda w, h: K.carmel("cg12", w, h, 1204), 0.4), "#8FD0E2", head="Mount Carmel"),
        face([joined("say", "18:23", ("18:24", "And call ye", "let him be God.")), cp("18:24", frm="And all the people", to="answered and said,"), say("18:24", frm="It is well spoken.")],
             "1KGS 18:23–24", ELIJAH_FIRE, bg=RED),
        face([cp("18:25", to="unto the prophets of Baal,"), say("18:25", frm="Choose you")], "1KGS 18:25", ELIJAH),
        drawn([cp("18:26", to="from morning even until noon, saying,"), say("18:26", frm="O Baal, hear us.", to="O Baal, hear us."), cp("18:26", frm="But there was no voice,")], "1KGS 18:26",
              below(lambda w, h: K.carmel("cb12", w, h, 1205, stage="baal"), 0.3), "#8FD0E2", head="O Baal, Hear Us"),
        face([cp("18:27", to="and said,"), say("18:27", frm="Cry aloud;")], "1KGS 18:27", ELIJAH_FIRE),
        drawn([caps("18:28-29")], "1KGS 18:28–29", lambda w, h: K.carmel("cb12b", w, h, 1206, stage="baal"), "#8FD0E2"),
        drawn([cp("18:30", to="unto all the people,"), say("18:30", frm="Come near unto me;", to="Come near unto me;"), cp("18:30", frm="and all the people came near"), caps("18:31-32")],
              "1KGS 18:30–32", below(lambda w, h: K.carmel("cw12", w, h, 1207, stage="water"), 0.4), "#8FD0E2", head="Twelve Stones"),
        drawn([cp("18:33", to="And he said,"), say("18:33", frm="Fill four jars"), cp("18:34", to="And he said,"), say("18:34", frm="Do it the second time;", to="the second time;"),
               cp("18:34", frm="and they did it the second time.", to="and they did it the second time."), cp("18:34", frm="And he said,", to="And he said,", after="second time."),
               say("18:34", frm="Do it the third time;", to="the third time;"), cp("18:34", frm="and they did it the third time."), caps("18:35")], "1KGS 18:33–35",
              below(lambda w, h: K.carmel("cw12b", w, h, 1208, stage="water"), 0.44), "#8FD0E2"),
        face([cp("18:36", to="and said,"), joined("say", ("18:36", "O Jehovah,"), "18:37")], "1KGS 18:36–37", ELIJAH, bg=NIGHT, head="Hear Me, O Jehovah"),
        drawn([caps("18:38"), cp("18:39", to="and they said,"), say("18:39", frm="Jehovah, he is God;")], "1KGS 18:38–39", lambda w, h: K.carmel("cf12", w, h, 1209, stage="fire"), "#2A1A3A",
              head="The Fire of Jehovah Fell"),
        drawn([cp("18:40", to="said unto them,"), say("18:40", frm="Take the prophets", to="escape."), cp("18:40", frm="And they took them;")], "1KGS 18:40", lambda w, h: K.kishon("ks12", w, h, 1210), "#2A1A3A"),
        drawn([cp("18:41", to="unto Ahab,"), say("18:41", frm="Get thee up,"), caps("18:42"), cp("18:43", to="to his servant,"), say("18:43", frm="Go up now,", to="toward the sea."),
               cp("18:43", frm="And he went up,", to="and said,"), say("18:43", frm="There is nothing.", to="There is nothing."), cp("18:43", frm="And he said,", to="And he said,", after="nothing."),
               say("18:43", frm="Go again")], "1KGS 18:41–43", below(lambda w, h: K.small_cloud("sc12", w, h, 1211), 0.46), "#8FD0E2", head="A Cloud as Small as a Man's Hand"),
        drawn([cp("18:44", to="that he said,"), say("18:44", frm="Behold, there ariseth", to="man's hand."), cp("18:44", frm="And he said,", to="And he said,", after="man's hand."),
               say("18:44", frm="Go up, say")], "1KGS 18:44", below(lambda w, h: K.small_cloud("sc12b", w, h, 1212), 0.3), "#8FD0E2"),
        drawn([caps("18:45-46")], "1KGS 18:45–46", lambda w, h: K.small_cloud("sc12c", w, h, 1213, rain=True), "#2A2A3A")]
PG.extend(pack(SEGS, "1KI-C12-D", PG.next(), end=end_mark("NEXT · A STILL SMALL VOICE", "right: 10px; bottom: 34px")))
