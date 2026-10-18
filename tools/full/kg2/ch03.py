"""2 Kings volume, Chapter 3 — Naaman (2 Kings 5–6). Every verse, word for word from ref/asv.
Naaman the leper and the little maiden of Israel; the letter to the king of Israel — am I God?; go and wash in the Jordan
seven times; are not Abanah and Pharpar better?; his flesh as the flesh of a little child; two mules' burden of earth;
Gehazi's lie and the leprosy as white as snow. Then the axe-head that swam; the king of Syria's bedchamber; Dothan and the
mountain full of horses and chariots of fire; the host smitten with blindness and fed in Samaria; the siege and the famine
(6:28–29 words over the wall, nothing drawn); this son of a murderer."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg2 import G, art as K
from kg2.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, ELISHA, ELISHA_STERN, JEHORAM, JEHORAM_SACK, GEHAZI, GEHAZI_LEPER, NAAMAN, NAAMAN_WROTH,
                        NAAMAN_CLEAN, MAIDEN, SYRIA_KING, SONS_PROPHETS, MESSENGER, WIDOW, RED, COLD, GOLDEN)
from kg2 import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"


@P("2KI-C03-00-Title", "Chapter 3 · Naaman", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{K.jordan_wash("t3", 760, 780, 301, clean=True)}</g>')
    return chapter_title(3, "第三話", "Naaman", "2 Kings 5 – 6", svg, "#2C7DA8", v("5:14", frm="and his flesh came again"), "2 Kings · Volume Twelve")


SEGS = [face([caps("5:1")], "2KGS 5:1", NAAMAN, head="Naaman the Leper", stamp=5),
        drawn([caps("5:2"), cp("5:3", to="unto her mistress,"), say("5:3", frm="Would that")], "2KGS 5:2–3", below(lambda w, h: K.naaman_house("nh3", w, h, 302), 0.36), "#5A2A1E"),
        face([cp("5:4", to="saying,"), say("5:4", frm="Thus and thus"), cp("5:5", to="said,"), say("5:5", frm="Go now,", to="king of Israel."), cp("5:5", frm="And he departed,")], "2KGS 5:4–5", SYRIA_KING),
        drawn([cp("5:6", to="saying,"), say("5:6", frm="And now")], "2KGS 5:6", below(lambda w, h: K.letters(w, h, 303), 0.36), "#3A1A2A"),
        face([cp("5:7", to="and said,"), say("5:7", frm="Am I God,")], "2KGS 5:7", JEHORAM_SACK, bg=COLD),
        face([cp("5:8", to="saying,"), say("5:8", frm="Wherefore")], "2KGS 5:8", ELISHA),
        drawn([caps("5:9"), cp("5:10", to="saying,"), say("5:10", frm="Go and wash")], "2KGS 5:9–10", below(lambda w, h: K.chariots_door("cd3", w, h, 304), 0.3), "#8FD0E2", head="Wash in the Jordan"),
        face([cp("5:11", to="and said,"), joined("say", ("5:11", "Behold, I thought,"), ("5:12", "Are not", "and be clean?")), cp("5:12", frm="So he turned")], "2KGS 5:11–12", NAAMAN_WROTH, bg=RED),
        face([cp("5:13", to="and said,"), say("5:13", frm="My father,")], "2KGS 5:13", SONS_PROPHETS),
        drawn([caps("5:14")], "2KGS 5:14", lambda w, h: K.jordan_wash("jw3", w, h, 305), "#8FD0E2"),
        face([cp("5:15", to="and he said,"), say("5:15", frm="Behold now,")], "2KGS 5:15", NAAMAN_CLEAN, head="There Is No God but in Israel"),
        face([cp("5:16", to="But he said,"), say("5:16", frm="As Jehovah liveth,", to="I will receive none."), cp("5:16", frm="And he urged him")], "2KGS 5:16", ELISHA),
        face([cp("5:17", to="And Naaman said,"), joined("say", ("5:17", "If not,"), "5:18")], "2KGS 5:17–18", NAAMAN_CLEAN),
        drawn([cp("5:19", to="And he said unto him,"), say("5:19", frm="Go in peace.", to="Go in peace."), cp("5:19", frm="So he departed")], "2KGS 5:19", below(lambda w, h: K.mules_earth("me3", w, h, 306), 0.2),
              "#E8C8A0"),
        face([cp("5:20", to="said,"), say("5:20", frm="Behold, my master")], "2KGS 5:20", GEHAZI, bg=RED, head="Gehazi"),
        face([cp("5:21", to="and said,"), say("5:21", frm="Is all well?"), cp("5:22", to="And he said,"), say("5:22", frm="All is well."), cp("5:23", to="And Naaman said,"),
              say("5:23", frm="Be pleased", to="two talents."), cp("5:23", frm="And he urged him,")], "2KGS 5:21–23", GEHAZI),
        drawn([caps("5:24")], "2KGS 5:24", below(lambda w, h: K.silver_bags("sv3", w, h, 307), 0.2), "#C8B8A0"),
        face([cp("5:25", to="And Elisha said unto him,"), say("5:25", frm="Whence comest", to="Gehazi?"), cp("5:25", frm="And he said,", to="And he said,"), say("5:25", frm="Thy servant went"),
              cp("5:26", to="And he said unto him,"), joined("say", ("5:26", "Went not"), ("5:27", "The leprosy", "for ever."))], "2KGS 5:25–27", ELISHA_STERN, bg=RED),
        face([cp("5:27", frm="And he went out")], "2KGS 5:27", GEHAZI_LEPER, bg=COLD),
        face([cp("6:1", to="said unto Elisha,"), joined("say", ("6:1", "Behold now,"), ("6:2", "Let us go,", "where we may dwell.")), cp("6:2", frm="And he answered,", to="And he answered,"),
              say("6:2", frm="Go ye."), cp("6:3", to="And one said,"), say("6:3", frm="Be pleased,", to="thy servants."), cp("6:3", frm="And he answered,", to="And he answered,"), say("6:3", frm="I will go.")],
             "2KGS 6:1–3", SONS_PROPHETS, head="The Iron Did Swim", stamp=6),
        drawn([caps("6:4"), cp("6:5", to="and said,"), say("6:5", frm="Alas,"), cp("6:6", to="said,"), say("6:6", frm="Where fell it?", to="Where fell it?"), cp("6:6", frm="And he showed him"),
               cp("6:7", to="And he said,"), say("6:7", frm="Take it up", to="to thee."), cp("6:7", frm="So he put out")], "2KGS 6:4–7", below(lambda w, h: K.axe_head("ax3", w, h, 308), 0.4), "#8FD0E2"),
        face([cp("6:8", to="saying,"), say("6:8", frm="In such"), cp("6:9", to="saying,"), say("6:9", frm="Beware"), caps("6:10")], "2KGS 6:8–10", SYRIA_KING, bg=RED, head="Dothan"),
        face([cp("6:11", to="and said unto them,"), say("6:11", frm="Will ye not"), cp("6:12", to="said,"), say("6:12", frm="Nay, my lord,"), cp("6:13", to="And he said,"), say("6:13", frm="Go and see", to="fetch him."),
              cp("6:13", frm="And it was told him,", to="saying,"), say("6:13", frm="Behold, he is in Dothan.")], "2KGS 6:11–13", SYRIA_KING, bg=RED),
        drawn([caps("6:14"), cp("6:15", to="And his servant said unto him,"), say("6:15", frm="Alas, my master!"), cp("6:16", to="And he answered,"), say("6:16", frm="Fear not;")], "2KGS 6:14–16",
              below(lambda w, h: K.dothan("dt3", w, h, 309), 0.4), "#2A2A4A"),
        drawn([cp("6:17", to="and said,"), say("6:17", frm="Jehovah, I pray thee,", to="that he may see."), cp("6:17", frm="And Jehovah opened")], "2KGS 6:17",
              lambda w, h: K.dothan("dt3b", w, h, 310, fire=True), "#2A2A4A", head="Horses and Chariots of Fire"),
        drawn([cp("6:18", to="and said,"), say("6:18", frm="Smite this people,", to="with blindness."), cp("6:18", frm="And he smote them"), cp("6:19", to="said unto them,"), say("6:19", frm="This is not the way,", to="whom ye seek."),
               cp("6:19", frm="And he led them")], "2KGS 6:18–19", below(lambda w, h: K.blind_host("bh3", w, h, 311), 0.4), "#C8B8A0"),
        face([cp("6:20", to="that Elisha said,"), say("6:20", frm="Jehovah,", to="that they may see."), cp("6:20", frm="And Jehovah opened"), cp("6:21", to="when he saw them,"), say("6:21", frm="My father,"),
              cp("6:22", to="And he answered,"), say("6:22", frm="Thou shalt not"), caps("6:23")], "2KGS 6:20–23", JEHORAM),
        drawn([caps("6:24-25")], "2KGS 6:24–25", lambda w, h: K.siege_wall("sw3", w, h, 312, king=False), "#5A4A4A", head="The Siege of Samaria"),
        drawn([cp("6:26", to="saying,"), say("6:26", frm="Help,"), cp("6:27", to="And he said,"), say("6:27", frm="If Jehovah"), cp("6:28", to="And the king said unto her,"), say("6:28", frm="What aileth thee?", to="What aileth thee?"),
               cp("6:28", frm="And she answered,", to="And she answered,"), say("6:28", frm="This woman"), says("6:29")], "2KGS 6:26–29", below(lambda w, h: K.siege_wall("sw3b", w, h, 313), 0.5), "#5A4A4A"),
        face([caps("6:30"), cp("6:31", to="Then he said,"), say("6:31", frm="God do so")], "2KGS 6:30–31", JEHORAM_SACK, bg=RED),
        face([cp("6:32", to="he said to the elders,"), say("6:32", frm="See ye how"), cp("6:33", to="and he said,"), say("6:33", frm="Behold, this evil")], "2KGS 6:32–33", ELISHA_STERN, bg=COLD)]
PG.extend(pack(SEGS, "2KI-C03-D", PG.next(), end=end_mark("NEXT · THE SIEGE OF SAMARIA", "right: 10px; bottom: 34px")))
