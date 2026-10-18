"""1 Kings volume, Chapter 1 — Long Live King Solomon (1 Kings 1). Every verse, word for word from ref/asv.
King David old and covered with clothes, and Abishag the Shunammite; Adonijah exalting himself — I will be king — with his
feast by the stone of Zoheleth; Nathan's counsel to Bath-sheba; Bath-sheba and Nathan before the king; the oath: assuredly
Solomon thy son shall reign after me; Solomon on the king's mule down to Gihon, the horn of oil, long live king Solomon;
the guests' fear, and Adonijah holding the horns of the altar."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from sa2 import art as K2
from kg1 import G, art as K
from kg1.common import (pack, say, gd, cp, says, caps, joined, face, drawn, DAVID_OLD, NATHAN, SOLOMON, BATHSHEBA, ADONIJAH, ADONIJAH_AFRAID, JOAB, BENAIAH, JONATHAN_PR,
                        MESSENGER, RED, COLD, GOLDEN)

v, sp = G.v, G.span
SERVANT = MESSENGER
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1KI-C01-00-Title", "Chapter 1 · Long Live King Solomon", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 320)">{K.gihon("t1", 760, 760, 101, anoint=True)}</g>')
    return chapter_title(1, "第一話", "Long Live King Solomon", "1 Kings 1", svg, "#2C7DA8", v("1:39", frm="Long live king Solomon."), "1 Kings · Volume Eleven")


SEGS = [drawn([caps("1:1"), cp("1:2", to="said unto him,"), say("1:2", frm="Let there be sought"), caps("1:3-4")], "1KGS 1:1–4", below(lambda w, h: K.old_bed("ob1", w, h, 102), 0.36), "#5A2A1E",
              head="King David Was Old", stamp=1),
        face([cp("1:5", to="saying,"), say("1:5", frm="I will be king:", to="I will be king:"), cp("1:5", frm="and he prepared"), caps("1:6")], "1KGS 1:5–6", ADONIJAH),
        drawn([caps("1:7-8")], "1KGS 1:7–8", lambda w, h: K2.chariot_runners("cr1", w, h, 103), "#FFE680"),
        drawn([caps("1:9-10")], "1KGS 1:9–10", below(lambda w, h: K.zoheleth("zh1", w, h, 104), 0.3), "#E8B880", head="The Stone of Zoheleth"),
        face([cp("1:11", to="saying,"), joined("say", ("1:11", "Hast thou not"), "1:12", "1:13", "1:14")], "1KGS 1:11–14", NATHAN, head="Nathan and Bath-sheba"),
        drawn([caps("1:15"), cp("1:16", to="And the king said,"), say("1:16", frm="What wouldest thou?")], "1KGS 1:15–16", below(lambda w, h: K.chamber("cb1", w, h, 105), 0.3), "#5A2A1E"),
        face([cp("1:17", to="And she said unto him,"), joined("say", ("1:17", "My lord,"), "1:18", "1:19")], "1KGS 1:17–19", BATHSHEBA),
        face([says("1:20-21")], "1KGS 1:20–21", BATHSHEBA, bg=COLD),
        drawn([caps("1:22"), cp("1:23", to="saying,"), say("1:23", frm="Behold, Nathan", to="the prophet."), cp("1:23", frm="And when he was come in")], "1KGS 1:22–23",
              below(lambda w, h: K.chamber("cb1b", w, h, 106, who="nathan"), 0.3), "#5A2A1E"),
        face([cp("1:24", to="And Nathan said,"), joined("say", ("1:24", "My lord,"), "1:25")], "1KGS 1:24–25", NATHAN),
        face([says("1:26-27")], "1KGS 1:26–27", NATHAN),
        face([cp("1:28", to="answered and said,"), say("1:28", frm="Call to me", to="Bath-sheba."), cp("1:28", frm="And she came"), cp("1:29", to="and said,"),
              joined("say", ("1:29", "As Jehovah liveth,"), "1:30")], "1KGS 1:28–30", DAVID_OLD, head="Assuredly Solomon Shall Reign"),
        face([cp("1:31", to="and said,"), say("1:31", frm="Let my lord")], "1KGS 1:31", BATHSHEBA),
        face([cp("1:32", to="And king David said,"), say("1:32", frm="Call to me", to="Jehoiada."), cp("1:32", frm="And they came"), cp("1:33", to="unto them,"),
              joined("say", ("1:33", "Take with you"), "1:34", "1:35")], "1KGS 1:32–35", DAVID_OLD),
        face([cp("1:36", to="and said,"), joined("say", ("1:36", "Amen:"), "1:37")], "1KGS 1:36–37", BENAIAH),
        drawn([caps("1:38")], "1KGS 1:38", below(lambda w, h: K.gihon("gh1", w, h, 107), 0.24), "#8FD0E2", head="Gihon"),
        drawn([cp("1:39", to="all the people said,"), say("1:39", frm="Long live")], "1KGS 1:39", below(lambda w, h: K.gihon("gh1b", w, h, 108, anoint=True), 0.2), "#8FD0E2"),
        drawn([caps("1:40")], "1KGS 1:40", lambda w, h: K.rejoicing("rj1", w, h, 109), "#FFE680"),
        face([cp("1:41", to="he said,"), say("1:41", frm="Wherefore is this noise")], "1KGS 1:41", JOAB, bg=RED, head="The City Rang Again"),
        face([cp("1:42", to="and Adonijah said,"), say("1:42", frm="Come in;")], "1KGS 1:42", ADONIJAH),
        face([cp("1:43", to="to Adonijah,"), joined("say", ("1:43", "Verily"), "1:44", "1:45", "1:46")], "1KGS 1:43–46", JONATHAN_PR),
        face([joined("say", "1:47", "1:48")], "1KGS 1:47–48", JONATHAN_PR),
        face([caps("1:49-50")], "1KGS 1:49–50", ADONIJAH_AFRAID, bg=COLD),
        drawn([cp("1:51", to="saying,"), say("1:51", frm="Behold, Adonijah")], "1KGS 1:51",
              below(lambda w, h: K.altar_horns("ah1", w, h, 110), 0.3), "#3A2A4A", head="The Horns of the Altar"),
        ]
SEGS2 = [face([cp("1:52", to="And Solomon said,"), say("1:52", frm="If he shall"), cp("1:53", to="and Solomon said unto him,"), say("1:53", frm="Go to thy house.")], "1KGS 1:52–53", SOLOMON)]
PG.extend(pack(SEGS, "1KI-C01-D", PG.next()))
PG.extend(pack(SEGS2, "1KI-C01-E", PG.next(), end=end_mark("NEXT · SHOW THYSELF A MAN", "right: 10px; bottom: 34px")))
