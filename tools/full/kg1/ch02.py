"""1 Kings volume, Chapter 2 — Show Thyself a Man (1 Kings 2). Every verse, word for word from ref/asv.
David's charge to Solomon — be thou strong therefore, and show thyself a man; David sleeps with his fathers (the city at
dusk, no grave drawn); Adonijah asks for Abishag through Bath-sheba, the throne set for the king's mother; Adonijah's end
(2:25 words only); Abiathar sent to Anathoth; Joab at the horns of the altar (2:34 words over the altar alone); Shimei bound
to Jerusalem, the brook Kidron, his servants at Gath (2:46 words over the road)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg1 import G, art as K
from kg1.common import (pack, say, gd, cp, says, caps, joined, face, drawn, DAVID_OLD, SOLOMON, SOLOMON_STERN, BATHSHEBA, ADONIJAH, JOAB, BENAIAH, SHIMEI, MESSENGER,
                        RED, COLD, GOLDEN)
from kg1 import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1KI-C02-00-Title", "Chapter 2 · Show Thyself a Man", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#5A2A1E"></rect><g transform="translate(0 340)">{K.charge("t2", 760, 740, 201)}</g>')
    return chapter_title(2, "第二話", "Show Thyself a Man", "1 Kings 2", svg, "#5A2A1E", v("2:2", frm="be thou strong"), "1 Kings · Volume Eleven")


SEGS = [drawn([cp("2:1", to="saying,"), joined("say", "2:2", "2:3")], "1KGS 2:1–3", below(lambda w, h: K.charge("ch2", w, h, 202), 0.5), "#5A2A1E", head="David's Charge", stamp=2),
        face([says("2:4")], "1KGS 2:4", DAVID_OLD),
        face([says("2:5-7")], "1KGS 2:5–7", DAVID_OLD),
        face([says("2:8-9")], "1KGS 2:8–9", DAVID_OLD),
        drawn([caps("2:10-12")], "1KGS 2:10–12", lambda w, h: K.city_dusk("cd2", w, h, 203), "#2A1A3A", head="David Slept with His Fathers"),
        face([cp("2:13", to="And she said,"), say("2:13", frm="Comest thou", to="peaceably?"), cp("2:13", frm="And he said,", to="And he said,"), say("2:13", frm="Peaceably."),
              cp("2:14", to="He said moreover,"), say("2:14", frm="I have somewhat", to="unto thee."), cp("2:14", frm="And she said,", to="And she said,"), say("2:14", frm="Say on.")],
             "1KGS 2:13–14", BATHSHEBA, head="One Petition"),
        face([cp("2:15", to="And he said,"), say("2:15", frm="Thou knowest"), say("2:16", to="deny me not."), cp("2:16", frm="And she said unto him,", to="unto him,"), say("2:16", frm="Say on."),
              cp("2:17", to="And he said,"), say("2:17", frm="Speak,")], "1KGS 2:15–17", ADONIJAH),
        face([cp("2:18", to="And Bath-sheba said,"), say("2:18", frm="Well;")], "1KGS 2:18", BATHSHEBA),
        drawn([caps("2:19")], "1KGS 2:19", lambda w, h: K.two_thrones("tt2", w, h, 204), "#5A2A1E"),
        face([cp("2:20", to="Then she said,"), say("2:20", frm="I ask one", to="deny me not."), cp("2:20", frm="And the king said unto her,", to="said unto her,"), say("2:20", frm="Ask on,"),
              cp("2:21", to="And she said,"), say("2:21", frm="Let Abishag")], "1KGS 2:20–21", BATHSHEBA),
        face([cp("2:22", to="unto his mother,"), say("2:22", frm="And why")], "1KGS 2:22", SOLOMON_STERN, bg=RED),
        face([cp("2:23", to="saying,"), joined("say", ("2:23", "God do so"), "2:24"), caps("2:25")], "1KGS 2:23–25", SOLOMON_STERN, bg=RED),
        drawn([cp("2:26", to="said the king,"), say("2:26", frm="Get thee to Anathoth,"), caps("2:27")], "1KGS 2:26–27", below(lambda w, h: K.anathoth("an2", w, h, 205), 0.4), "#C8D8E8",
              head="Abiathar"),
        drawn([caps("2:28"), cp("2:29", to="And it was told king Solomon,"), say("2:29", frm="Joab is fled", to="by the altar."), cp("2:29", frm="Then Solomon sent", to="saying,"),
               say("2:29", frm="Go, fall upon him.")], "1KGS 2:28–29", below(lambda w, h: K.altar_horns("ah2", w, h, 206, who="#6A2A1A"), 0.36), "#3A2A4A", head="Joab"),
        face([cp("2:30", to="and said unto him,"), say("2:30", frm="Thus saith the king,", to="Come forth."), cp("2:30", frm="And he said,", to="And he said,"), say("2:30", frm="Nay;", to="die here."),
              cp("2:30", frm="And Benaiah brought", to="saying,"), say("2:30", frm="Thus said Joab,")], "1KGS 2:30", BENAIAH),
        face([cp("2:31", to="said unto him,"), joined("say", ("2:31", "Do as he"), "2:32", "2:33")], "1KGS 2:31–33", SOLOMON_STERN, bg=RED),
        drawn([caps("2:34-35")], "1KGS 2:34–35", lambda w, h: K.altar_horns("ah2b", w, h, 207, empty=True), "#3A2A4A"),
        face([cp("2:36", to="and said unto him,"), joined("say", ("2:36", "Build thee"), "2:37")], "1KGS 2:36–37", SOLOMON, head="Shimei"),
        face([cp("2:38", to="unto the king,"), say("2:38", frm="The saying", to="so will thy servant do."), cp("2:38", frm="And Shimei dwelt")], "1KGS 2:38", SHIMEI),
        drawn([cp("2:39", to="saying,"), say("2:39", frm="Behold, thy servants"), caps("2:40-41")], "1KGS 2:39–41", below(lambda w, h: K.kidron("kd2", w, h, 208, ass=True), 0.36), "#8FD0E2"),
        face([cp("2:42", to="and said unto him,"), joined("say", ("2:42", "Did I not"), "2:43"), cp("2:44", to="to Shimei,"), joined("say", ("2:44", "Thou knowest"), "2:45")], "1KGS 2:42–45",
             SOLOMON_STERN, bg=RED),
        drawn([caps("2:46")], "1KGS 2:46", lambda w, h: K.kidron("kd2b", w, h, 209), "#8FD0E2")]
PG.extend(pack(SEGS, "1KI-C02-D", PG.next(), end=end_mark("NEXT · AN UNDERSTANDING HEART", "right: 10px; bottom: 34px")))
