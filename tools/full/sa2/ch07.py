"""2 Samuel volume, Chapter 7 — Absalom (2 Samuel 13–14). Every verse, word for word from ref/eng-asv.
Amnon and Jonadab's counsel; Tamar's cakes; 13:11–14 words over the chamber door and the shut door (no one drawn); Tamar
going her way with ashes on her head; two full years, then the shearers at Baal-hazor (13:28–29 words over the empty feast
and the king's sons fleeing on their mules); Amnon only is dead; Absalom fled to Geshur. Then the wise woman of Tekoa and
her parable; Absalom brought home; no blemish in him and the hair weighed (the digest's panels); Joab's barley field on
fire; and the king kissed Absalom."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from jdg import art as JG
from sa1 import art as K1
from sa2 import G, art as K
from sa2.common import (pack, say, cp, says, caps, over, face, drawn, D, F, DAVID_KING, DAVID_GRIEF, JOAB, ABSALOM, ABSALOM_SLY, RED, COLD, GOLDEN)
from sa2 import ch06 as _prev

v, sp = G.v, G.span
AMNON = F("adam", skin="#D9A27A", shadow="#6A3A3A", hair="#6A2A14", hl="#9A502A", stubble="#6A2A14", band=True, brow="sorrow", light="#9AA8C8")
JONADAB = F("adam", skin="#C98E66", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#3A5A3A", cord=True, light="#FFC14D")
TAMAR = F("eve", skin="#D9A27A", shadow="#6A3A4A", hair="#1A1210", scarf="#C2456A", band=True, brow="sorrow", tear=True, light="#9AA8C8")
TEKOA = F("eve", skin="#B98A6E", shadow="#3A2A3A", hair="#3A3430", scarf="#2A2A2E", brow="sorrow", light="#9AA8C8")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2SA-C07-00-Title", "Chapter 7 · Absalom", title=True)
def title(n):
    bg, art = D("B1", 0)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#C8402A"></rect><g transform="translate(0 300)">{art(760, 780)}</g>')
    return chapter_title(7, "第七話", "Absalom", "2 Samuel 13 – 14", svg, "#C8402A", v("14:25", frm="from the sole of his foot"), "2 Samuel · Volume Ten")


SEGS = [face([caps("13:1-2")], "2SAM 13:1–2", AMNON, bg=COLD, head="Tamar", stamp=13),
        face([caps("13:3"), cp("13:4", to="And he said unto him,"), say("13:4", frm="Why, O son", to="tell me?"), cp("13:4", frm="And Amnon said unto him,", to="said unto him,"), say("13:4", frm="I love Tamar,")],
             "2SAM 13:3–4", JONADAB),
        face([cp("13:5", to="said unto him,"), say("13:5", frm="Lay thee down")], "2SAM 13:5", JONADAB),
        face([cp("13:6", to="said unto the king,"), say("13:6", frm="Let my sister"), cp("13:7", to="saying,"), say("13:7", frm="Go now")], "2SAM 13:6–7", AMNON, bg=COLD),
        drawn([caps("13:8"), cp("13:9", to="And Amnon said,"), say("13:9", frm="Have out all men", to="from me."), cp("13:9", frm="And they went out")], "2SAM 13:8–9",
              lambda w, h: K.kitchen(w, h, 701), "#4A2A1E"),
        drawn([cp("13:10", to="unto Tamar,"), say("13:10", frm="Bring the food", to="from thy hand."), cp("13:10", frm="And Tamar took"), cp("13:11", to="and said unto her,"),
               say("13:11", frm="Come, lie with me,")], "2SAM 13:10–11", lambda w, h: K.chamber(w, h, 702), "#3A2A2E"),
        face([cp("13:12", to="And she answered him,"), ("say", v("13:12", frm="Nay,") + " " + v("13:13"))], "2SAM 13:12–13", TAMAR, bg=COLD),
        drawn([caps("13:14"), cp("13:15", to="said unto her,"), say("13:15", frm="Arise, be gone.")], "2SAM 13:14–15", lambda w, h: JG.shut_door(w, h, 703), "#14123A"),
        face([cp("13:16", to="And she said unto him,"), say("13:16", frm="Not so,", to="thou didst unto me."), cp("13:16", frm="But he would not")], "2SAM 13:16", TAMAR, bg=COLD),
        drawn([cp("13:17", to="and said,"), say("13:17", frm="Put now"), caps("13:18")], "2SAM 13:17–18", lambda w, h: JG.shut_door(w, h, 704, dawn=True), "#7A7A8A"),
        drawn([caps("13:19")], "2SAM 13:19", lambda w, h: K.tamar_away("tw7", w, h, 705), "#5A5A7A"),
        face([cp("13:20", to="said unto her,"), say("13:20", frm="Hath Amnon", to="this thing to heart."), cp("13:20", frm="So Tamar remained"), caps("13:21-22")], "2SAM 13:20–22", ABSALOM, bg=COLD),
        drawn([caps("13:23"), cp("13:24", to="and said,"), say("13:24", frm="Behold now,")], "2SAM 13:23–24", lambda w, h: K1.shearing("sh7", w, h, 706), "#8FD0E2", head="Baal-hazor"),
        face([cp("13:25", to="to Absalom,"), say("13:25", frm="Nay, my son,", to="burdensome unto thee."), cp("13:25", frm="And he pressed him:"), cp("13:26", to="Then said Absalom,"),
              say("13:26", frm="If not,", to="go with us."), cp("13:26", frm="And the king said unto him,", to="said unto him,"), say("13:26", frm="Why should he"), caps("13:27")], "2SAM 13:25–27", DAVID_KING),
        face([cp("13:28", to="saying,"), say("13:28", frm="Mark ye now,")], "2SAM 13:28", ABSALOM_SLY, bg=RED),
        drawn([caps("13:29")], "2SAM 13:29", lambda w, h: K.feast_fled("ff7", w, h, 707), "#E8B880"),
        drawn([cp("13:30", to="saying,"), say("13:30", frm="Absalom hath slain"), caps("13:31")], "2SAM 13:30–31", lambda w, h: K.night_vigil("nv7", w, h, 708), "#1A1430", head="Amnon Only Is Dead"),
        face([cp("13:32", to="answered and said,"), ("say", v("13:32", frm="Let not my lord") + " " + v("13:33"))], "2SAM 13:32–33", JONADAB),
        drawn([caps("13:34"), cp("13:35", to="unto the king,"), say("13:35", frm="Behold,")], "2SAM 13:34–35", below(lambda w, h: K.watch("wt7", w, h, 709), 0.3), "#F3D8A0"),
        face([caps("13:36-39")], "2SAM 13:36–39", DAVID_GRIEF, bg=COLD),
        face([caps("14:1"), cp("14:2", to="and said unto her,"), ("say", v("14:2", frm="I pray thee,") + " " + v("14:3", to="speak on this manner unto him.")), cp("14:3", frm="So Joab put")],
             "2SAM 14:1–3", JOAB, head="The Wise Woman of Tekoa", stamp=14),
        drawn([cp("14:4", to="and said,"), say("14:4", frm="Help, O king."), cp("14:5", to="said unto her,"), say("14:5", frm="What aileth thee?", to="What aileth thee?"),
               cp("14:5", frm="And she answered,", to="And she answered,"), say("14:5", frm="Of a truth")], "2SAM 14:4–5", below(lambda w, h: K.tekoa("tk7", w, h, 710), 0.4), "#5A2A1E"),
        face([says("14:6-7")], "2SAM 14:6–7", TEKOA, bg=COLD),
        face([cp("14:8", to="unto the woman,"), say("14:8", frm="Go to thy house,"), cp("14:9", to="unto the king,"), say("14:9", frm="My lord,"), cp("14:10", to="And the king said,"),
              say("14:10", frm="Whosoever")], "2SAM 14:8–10", DAVID_KING),
        face([cp("14:11", to="Then said she,"), say("14:11", frm="I pray thee,", to="destroy my son."), cp("14:11", frm="And he said,", to="And he said,"), say("14:11", frm="As Jehovah liveth,"),
              cp("14:12", to="Then the woman said,"), say("14:12", frm="Let thy handmaid", to="the king."), cp("14:12", frm="And he said,", to="And he said,"), say("14:12", frm="Say on.")],
             "2SAM 14:11–12", TEKOA, bg=COLD),
        face([cp("14:13", to="And the woman said,"), ("say", v("14:13", frm="Wherefore") + " " + v("14:14"))], "2SAM 14:13–14", TEKOA, bg=COLD),
        face([says("14:15-17")], "2SAM 14:15–17", TEKOA, bg=COLD),
        face([cp("14:18", to="unto the woman,"), say("14:18", frm="Hide not", to="ask thee."), cp("14:18", frm="And the woman said,", to="And the woman said,"), say("14:18", frm="Let my lord"),
              cp("14:19", to="And the king said,"), say("14:19", frm="Is the hand", to="in all this?")], "2SAM 14:18–19", DAVID_KING, head="Is the Hand of Joab with Thee?"),
        face([cp("14:19", frm="And the woman answered", to="and said,"), ("say", v("14:19", frm="As thy soul") + " " + v("14:20"))], "2SAM 14:19–20", TEKOA, bg=COLD),
        face([cp("14:21", to="unto Joab,"), say("14:21", frm="Behold now,"), cp("14:22", to="and Joab said,"), say("14:22", frm="To-day"), caps("14:23")], "2SAM 14:21–23", JOAB),
        drawn([cp("14:24", to="And the king said,"), say("14:24", frm="Let him turn", to="my face."), cp("14:24", frm="So Absalom turned")], "2SAM 14:24",
              lambda w, h: JG.shut_door(w, h, 711, dawn=True), "#7A7A8A"),
        over([caps("14:25")], "2SAM 14:25", "B1", 0, head="No Blemish in Him"),
        over([caps("14:26")], "2SAM 14:26", "B1", 1),
        face([caps("14:27-29")], "2SAM 14:27–29", ABSALOM),
        drawn([cp("14:30", to="unto his servants,"), say("14:30", frm="See,", to="set it on fire."), cp("14:30", frm="And Absalom's servants")], "2SAM 14:30", lambda w, h: K.barley_fire(w, h, 712), "#3A1A1A"),
        face([cp("14:31", to="and said unto him,"), say("14:31", frm="Wherefore have")], "2SAM 14:31", JOAB, bg=RED),
        face([cp("14:32", to="answered Joab,"), say("14:32", frm="Behold,")], "2SAM 14:32", ABSALOM_SLY),
        drawn([caps("14:33")], "2SAM 14:33", lambda w, h: K.bowed("bw7", w, h, 713), "#5A2A1E")]
PG.extend(pack(SEGS, "2SA-C07-D", PG.next(), end=end_mark("NEXT · THE MOUNT OF OLIVES", "right: 10px; bottom: 34px")))
