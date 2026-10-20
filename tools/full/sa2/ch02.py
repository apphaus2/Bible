"""2 Samuel volume, Chapter 2 — Abner (2 Samuel 3–4). Every verse, word for word from ref/eng-asv.
Long war between the houses; the sons born in Hebron; Rizpah and Abner's wrath — am I a dog's head?; Michal taken from
Paltiel, who followed weeping to Bahurim; Abner's league and the feast in Hebron; Joab: what hast thou done?; Abner slain in
the gate (3:27 words over the empty gate at dusk); the bier and David's lament — should Abner die as a fool dieth?;
Mephibosheth lamed in the flight; Ish-bosheth slain at noon (4:5–7 words over the house) and Rechab and Baanah requited
(4:12 words over the pool of Hebron)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from sa1 import art as K1
from sa2 import G, art as K
from sa2.common import (pack, say, gd, cp, sg, sgs, says, caps, over, face, drawn, D, F, DAVID_KING, DAVID_WRATH, DAVID_GRIEF, ABNER, JOAB, ISHBOSHETH, MICHAL,
                        RED, COLD, GOLDEN)
from sa2 import ch01 as _prev

v, sp = G.v, G.span
BEEROTHITE = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", scarf="#3A3A2A", brow="scowl", sweat=True, light="#FF8A3D")
ABNER_WROTH = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#5A5A2A", cord=True, brow="scowl", light="#D7261E")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2SA-C02-00-Title", "Chapter 2 · Abner", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#3A1A2A"></rect><g transform="translate(0 360)">{K.gate_dusk(760, 720, 201)}</g>')
    return chapter_title(2, "第二話", "Abner", "2 Samuel 3 – 4", svg, "#3A1A2A", v("3:38", frm="there is a prince"), "2 Samuel · Volume Ten")


SEGS = [drawn([caps("3:1-5")], "2SAM 3:1–5", below(lambda w, h: K.sons_hebron(w, h), 0.5), "#1A1430", head="Sons Born in Hebron", stamp=3),
        face([caps("3:6"), cp("3:7", to="said to Abner,"), say("3:7", frm="Wherefore")], "2SAM 3:6–7", ISHBOSHETH, bg=COLD),
        face([cp("3:8", to="and said,"), ("say", v("3:8", frm="Am I") + " " + sp("3:9-10")), caps("3:11")], "2SAM 3:8–11", ABNER_WROTH, bg=RED, head="Am I a Dog's Head?"),
        drawn([cp("3:12", to="saying,"), say("3:12", frm="Whose is the land?", to="Whose is the land?"), cp("3:12", frm="saying also,", to="saying also,"), say("3:12", frm="Make thy league")],
              "2SAM 3:12", below(lambda w, h: K.messengers("ms2", w, h, 202), 0.4), "#8FD0E2"),
        face([cp("3:13", to="And he said,"), say("3:13", frm="Well;")], "2SAM 3:13", DAVID_KING),
        drawn([cp("3:14", to="saying,"), say("3:14", frm="Deliver me"), caps("3:15"), cp("3:16", to="Then said Abner unto him,"), say("3:16", frm="Go, return:", to="Go, return:"),
               cp("3:16", frm="and he returned.")], "2SAM 3:14–16", lambda w, h: K.taken_away("ta2", w, h, 203), "#8A9AB8", head="Michal"),
        face([cp("3:17", to="saying,"), ("say", v("3:17", frm="In times past") + " " + v("3:18")), caps("3:19")], "2SAM 3:17–19", ABNER),
        drawn([caps("3:20"), cp("3:21", to="unto David,"), say("3:21", frm="I will arise", to="thy soul desireth."), cp("3:21", frm="And David sent Abner away;")], "2SAM 3:20–21",
              below(lambda w, h: K.feast_hebron("fh2", w, h, 204), 0.3), "#5A2A1E"),
        drawn([caps("3:22"), cp("3:23", to="saying,"), say("3:23", frm="Abner the son of Ner")], "2SAM 3:22–23", lambda w, h: K1.spoil_flocks(w, h, 205), "#E8C88A", head="Joab"),
        face([cp("3:24", to="and said,"), ("say", v("3:24", frm="What hast thou done?") + " " + v("3:25"))], "2SAM 3:24–25", JOAB, bg=RED),
        drawn([caps("3:26-27")], "2SAM 3:26–27", lambda w, h: K.gate_dusk(w, h, 206), "#3A1A2A"),
        face([cp("3:28", to="he said,"), ("say", v("3:28", frm="I and my kingdom") + " " + v("3:29")), caps("3:30")], "2SAM 3:28–30", DAVID_WRATH, bg=RED),
        drawn([cp("3:31", to="that were with him,"), say("3:31", frm="Rend your clothes,", to="before Abner."), cp("3:31", frm="And king David followed"), caps("3:32")], "2SAM 3:31–32",
              below(lambda w, h: K.bier("bi2", w, h, 207), 0.42), "#5A5A7A", head="Should Abner Die as a Fool Dieth?"),
        face([cp("3:33", to="and said,"), sg("3:33", frm="Should Abner"), sg("3:34", to="so didst thou fall."), cp("3:34", frm="And all the people wept")], "2SAM 3:33–34", DAVID_GRIEF, bg=COLD),
        face([cp("3:35", to="saying,"), say("3:35", frm="God do so"), caps("3:36-37")], "2SAM 3:35–37", DAVID_GRIEF, bg=COLD),
        face([cp("3:38", to="unto his servants,"), ("say", v("3:38", frm="Know ye not") + " " + v("3:39"))], "2SAM 3:38–39", DAVID_GRIEF, bg=COLD),
        face([caps("4:1-3")], "2SAM 4:1–3", ISHBOSHETH, bg=COLD, head="His Hands Became Feeble", stamp=4),
        drawn([caps("4:4")], "2SAM 4:4", lambda w, h: K.nurse_flee("nf2", w, h, 208), "#C8703A", head="Mephibosheth"),
        drawn([caps("4:5-7")], "2SAM 4:5–7", lambda w, h: K.house_noon(w, h, 209), "#FFC14D"),
        face([cp("4:8", to="said to the king,"), say("4:8", frm="Behold,")], "2SAM 4:8", BEEROTHITE, bg=RED),
        face([cp("4:9", to="and said unto them,"), ("say", v("4:9", frm="As Jehovah liveth,") + " " + sp("4:10-11"))], "2SAM 4:9–11", DAVID_WRATH, bg=RED),
        drawn([caps("4:12")], "2SAM 4:12", lambda w, h: K.pool_dusk(w, h, 210), "#2A1A3A")]
PG.extend(pack(SEGS, "2SA-C02-D", PG.next(), end=end_mark("NEXT · THE CITY OF DAVID", "right: 10px; bottom: 34px")))
