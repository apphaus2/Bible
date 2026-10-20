"""2 Samuel volume, Chapter 9 — O My Son Absalom (2 Samuel 17–18). Every verse, word for word from ref/eng-asv.
Ahithophel's counsel and Hushai's — a bear robbed of her whelps, as the dew falleth on the ground; the priests' sons hidden
in the well at Bahurim; over the Jordan by morning light; Ahithophel's end (17:23 words over his city at dusk); Barzillai's
gifts at Mahanaim. Then deal gently for my sake with the young man; the forest devoured more than the sword; Absalom caught
in the oak (the digest's panel), 18:14–15 words over the dark oak, the heap of stones; Ahimaaz outrunning the Cushite; and
the chamber over the gate: O my son Absalom."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos import art as JA
from jos.art import below
from sa2 import G, art as K
from sa2.common import (pack, say, cp, says, caps, over, face, drawn, D, F, DAVID_OLD, DAVID_OLD_ALARM, ABSALOM, JOAB, ISRAELITE, MESSENGER, CUSHITE, RED, COLD, GOLDEN)
from sa2.ch08 import HUSHAI, AHITHOPHEL
from sa2 import ch08 as _prev

v, sp = G.v, G.span
AHIMAAZ = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#2A1A10", hl="#5A4A3E", stubble="#2A1A10", sweat=True, light="#FFE680")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2SA-C09-00-Title", "Chapter 9 · O My Son Absalom", title=True)
def title(n):
    bg, art = D("B6", 0)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#5E8F26"></rect><g transform="translate(0 280)">{art(760, 800)}</g>')
    return chapter_title(9, "第九話", "O My Son Absalom", "2 Samuel 17 – 18", svg, "#2E6A32", v("18:9", frm="and he was taken up", to="between heaven and earth;"), "2 Samuel · Volume Ten")


SEGS = [face([cp("17:1", to="unto Absalom,"), ("say", v("17:1", frm="Let me now") + " " + sp("17:2-3")), caps("17:4")], "2SAM 17:1–4", AHITHOPHEL, bg=RED, head="The Counsel of Hushai", stamp=17),
        face([cp("17:5", to="Then said Absalom,"), say("17:5", frm="Call now"), cp("17:6", to="saying,"), say("17:6", frm="Ahithophel hath")], "2SAM 17:5–6", ABSALOM),
        face([cp("17:7", to="unto Absalom,"), say("17:7", frm="The counsel"), cp("17:8", to="said moreover,"), ("say", v("17:8", frm="Thou knowest") + " " + v("17:9"))], "2SAM 17:7–9", HUSHAI),
        face([says("17:10-11")], "2SAM 17:10–11", HUSHAI),
        drawn([says("17:12-13")], "2SAM 17:12–13", lambda w, h: JA.armed("hs9", w, h, 901, tribes=()), "#F3D8A0"),
        face([cp("17:14", to="said,"), say("17:14", frm="The counsel of Hushai", to="Ahithophel."), cp("17:14", frm="For Jehovah had")], "2SAM 17:14", ABSALOM),
        face([cp("17:15", to="the priests,"), ("say", v("17:15", frm="Thus and thus") + " " + v("17:16"))], "2SAM 17:15–16", HUSHAI),
        drawn([caps("17:17-19")], "2SAM 17:17–19", lambda w, h: K.well_court("wc9", w, h, 902), "#D8B88A", head="The Well in Bahurim"),
        drawn([cp("17:20", to="and they said,"), say("17:20", frm="Where are", to="Jonathan?"), cp("17:20", frm="And the woman said unto them,", to="unto them,"), say("17:20", frm="They are gone", to="brook of water."),
               cp("17:20", frm="And when they had sought")], "2SAM 17:20", below(lambda w, h: K.well_court("wc9b", w, h, 903, men=True), 0.3), "#D8B88A"),
        drawn([cp("17:21", to="and they said unto David,"), say("17:21", frm="Arise ye,"), caps("17:22")], "2SAM 17:21–22", below(lambda w, h: K.jordan_dawn("jd9", w, h, 904), 0.3), "#5A5A8A"),
        drawn([caps("17:23")], "2SAM 17:23", lambda w, h: K.ahithophel_home("ah9", w, h, 905), "#2A1A3A"),
        drawn([caps("17:24-26")], "2SAM 17:24–26", lambda w, h: K.gilead_camp("gc9", w, h, 906), "#14123A"),
        drawn([caps("17:27-28"), cp("17:29", to="for they said,"), say("17:29", frm="The people")], "2SAM 17:27–29", below(lambda w, h: K.provisions(w, h, 907), 0.3), "#E8B880",
              head="Barzillai the Gileadite"),
        drawn([cp("18:1"), cp("18:2", to="unto the people,"), say("18:2", frm="I will surely")], "2SAM 18:1–2", below(lambda w, h: K.march_by("mb9", w, h, 908), 0.3), "#E8C8A0",
              head="Deal Gently for My Sake", stamp=18),
        face([cp("18:3", to="But the people said,"), say("18:3", frm="Thou shalt not")], "2SAM 18:3", ISRAELITE),
        over([cp("18:4", to="unto them,"), say("18:4", frm="What seemeth", to="I will do."), cp("18:4", frm="And the king stood"), cp("18:5", to="saying,"), say("18:5", frm="Deal gently", to="with Absalom."),
              cp("18:5", frm="And all the people heard")], "2SAM 18:4–5", "B5", 0),
        over([caps("18:6-8")], "2SAM 18:6–8", "B5", 1, head="The Forest of Ephraim"),
        over([caps("18:9")], "2SAM 18:9", "B6", 0, head="Between Heaven and Earth"),
        face([cp("18:10", to="and said,"), say("18:10", frm="Behold,"), cp("18:11", to="that told him,"), say("18:11", frm="And, behold,")], "2SAM 18:10–11", JOAB, bg=RED),
        face([cp("18:12", to="unto Joab,"), ("say", v("18:12", frm="Though I") + " " + v("18:13"))], "2SAM 18:12–13", MESSENGER),
        drawn([cp("18:14", to="Then said Joab,"), say("18:14", frm="I may not", to="with thee."), cp("18:14", frm="And he took"), caps("18:15")], "2SAM 18:14–15", lambda w, h: K.dark_oak(w, h, 909), "#2A0A0A"),
        drawn([caps("18:16")], "2SAM 18:16", lambda w, h: K.hill_ammah("ha9", w, h, 910, trumpet=True), "#2A1A3A"),
        over([caps("18:17")], "2SAM 18:17", "B6", 1),
        drawn([cp("18:18", to="for he said,"), say("18:18", frm="I have no son", to="in remembrance:"), cp("18:18", frm="and he called the pillar")], "2SAM 18:18",
              lambda w, h: K.pillar(w, h, 911), "#5A4A6A"),
        face([cp("18:19", to="the son of Zadok,"), say("18:19", frm="Let me now run,")], "2SAM 18:19", AHIMAAZ, head="Tidings"),
        face([cp("18:20", to="And Joab said unto him,"), say("18:20", frm="Thou shalt not"), cp("18:21", to="to the Cushite,"), say("18:21", frm="Go, tell", to="hast seen."), cp("18:21", frm="And the Cushite bowed")],
             "2SAM 18:20–21", JOAB),
        face([cp("18:22", to="yet again to Joab,"), say("18:22", frm="But come what may,", to="after the Cushite."), cp("18:22", frm="And Joab said,", to="And Joab said,"), say("18:22", frm="Wherefore wilt"),
              say("18:23", to="But come what may,"), cp("18:23", frm="said he,", to="said he,"), say("18:23", frm="I will run.", to="I will run."), cp("18:23", frm="And he said unto him,", to="said unto him,"),
              say("18:23", frm="Run.", to="Run."), cp("18:23", frm="Then Ahimaaz ran")], "2SAM 18:22–23", AHIMAAZ),
        over([caps("18:24"), cp("18:25", to="And the king said,"), say("18:25", frm="If he be alone,", to="in his mouth."), cp("18:25", frm="And he came apace,")], "2SAM 18:24–25", "B7", 0),
        drawn([cp("18:26", to="and said,"), say("18:26", frm="Behold, another", to="running alone."), cp("18:26", frm="And the king said,", to="And the king said,"), say("18:26", frm="He also"),
               cp("18:27", to="And the watchman said,"), say("18:27", frm="I think", to="son of Zadok."), cp("18:27", frm="And the king said,", to="And the king said,"), say("18:27", frm="He is a good man,")],
              "2SAM 18:26–27", below(lambda w, h: K.two_runners("tr9", w, h, 912), 0.4), "#FFE6A0"),
        face([cp("18:28", to="unto the king,"), say("18:28", frm="All is well.", to="All is well."), cp("18:28", frm="And he bowed", to="and said,"), say("18:28", frm="Blessed be")], "2SAM 18:28", AHIMAAZ),
        face([cp("18:29", to="And the king said,"), say("18:29", frm="Is it well", to="Absalom?"), cp("18:29", frm="And Ahimaaz answered,", to="And Ahimaaz answered,"), say("18:29", frm="When Joab"),
              cp("18:30", to="And the king said,"), say("18:30", frm="Turn aside,", to="stand here."), cp("18:30", frm="And he turned aside,")], "2SAM 18:29–30", DAVID_OLD_ALARM, bg=COLD),
        face([cp("18:31", to="and the Cushite said,"), say("18:31", frm="Tidings for"), cp("18:32", to="unto the Cushite,"), say("18:32", frm="Is it well", to="Absalom?"),
              cp("18:32", frm="And the Cushite answered,", to="And the Cushite answered,"), say("18:32", frm="The enemies")], "2SAM 18:31–32", CUSHITE, bg="#3A3A3A"),
        ]
SEGS2 = [over([cp("18:33", to="thus he said,"), say("18:33", frm="O my son")], "2SAM 18:33", "B8", 0, align="xMinYMid", head="O My Son Absalom")]
PG.extend(pack(SEGS, "2SA-C09-D", PG.next()))
PG.extend(pack(SEGS2, "2SA-C09-E", PG.next(), end=end_mark("NEXT · THE KING RETURNED", "right: 10px; bottom: 34px")))
