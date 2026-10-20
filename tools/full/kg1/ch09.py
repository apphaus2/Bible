"""1 Kings volume, Chapter 9 — To Your Tents, O Israel (1 Kings 12–13). Every verse, word for word from ref/eng-asv.
Rehoboam at Shechem; thy father made our yoke grievous; the counsel of the old men and of the young men — my little finger is
thicker than my father's loins; what portion have we in David?; Adoram stoned (12:18 words over the people turning away);
Shemaiah — ye shall not go up; Jeroboam's two calves of gold in Beth-el and Dan. Then the man of God out of Judah crying
against the altar — O altar, altar; the king's hand dried up; the old prophet's lie; the lion in the way (13:24–28 words over
the ass and the lion standing, no body drawn); Alas, my brother!"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos import art as JA
from jos.art import below
from kg1 import G, art as K
from kg1.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, F, JEROBOAM, REHOBOAM, ISRAELITE, PROPHET, RED, COLD, GOLDEN)
from kg1 import ch08 as _prev

v, sp = G.v, G.span
OLD_MAN = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#E8E2D6", hl="#F3EFE6", beard=True, beard_color="#E8E2D6", scarf="#6A5A3A", cord=True, light="#FFE680")
YOUNG = F("adam", skin="#E3B08A", shadow="#8A4A3A", hair="#1A1210", hl="#4A3A2E", stubble="#1A1210", band=True, laugh=True, light="#FF8A3D")
SHEMAIAH = F("adam", skin="#B98A6E", shadow="#3A3A5A", hair="#6A645E", hl="#9A968E", beard=True, beard_color="#7A766E", scarf="#3A3A5A", light="#9AA8C8")
MAN_OF_GOD = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#4A3A2A", cord=True, brow="scowl", light="#FFD23F")
OLD_PROPHET = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#6A645E", cord=True, light="#FFC14D")
OLD_PROPHET_W = F("adam", skin="#B98A6E", shadow="#3A3A5A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#6A645E", cord=True, brow="sorrow", tear=True, light="#9AA8C8")
JEROBOAM_AFRAID = F("adam", skin="#C47A5A", shadow="#3A2A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#2E6B3A", band=True, brow="sorrow", sweat=True, light="#9AA8C8")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"


@P("1KI-C09-00-Title", "Chapter 9 · To Your Tents, O Israel", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#5A3A5A"></rect><g transform="translate(0 340)">{K.calves("t9", 760, 740, 901, people=False)}</g>')
    return chapter_title(9, "第九話", "To Your Tents, O Israel", "1 Kings 12 – 13", svg, "#5A3A5A", v("12:16", frm="What portion", to="O Israel:"), "1 Kings · Volume Eleven")


SEGS = [drawn([caps("12:1-3"), says("12:4")], "1KGS 12:1–4", below(lambda w, h: JA.shechem("sh9", w, h, 902, stone=False, joshua=False), 0.44), "#8FD0E2", head="Rehoboam at Shechem", stamp=12),
        face([cp("12:5", to="And he said unto them,"), say("12:5", frm="Depart yet", to="come again to me."), cp("12:5", frm="And the people departed."), cp("12:6", to="saying,"),
              say("12:6", frm="What counsel")], "1KGS 12:5–6", REHOBOAM),
        drawn([cp("12:7", to="saying,"), say("12:7", frm="If thou wilt"), caps("12:8")], "1KGS 12:7–8", below(lambda w, h: K.counsel("co9", w, h, 903), 0.4), "#5A2A1E", head="The Counsel of the Old Men"),
        drawn([cp("12:9", to="And he said unto them,"), say("12:9", frm="What counsel", to="saying,"), say("12:9", frm="Make the yoke")], "1KGS 12:9",
              below(lambda w, h: K.counsel("co9b", w, h, 904, young=True), 0.36), "#5A2A1E"),
        face([cp("12:10", to="spake unto him, saying,"), joined("say", ("12:10", "Thus shalt thou"), "12:11")], "1KGS 12:10–11", YOUNG, bg=RED),
        face([caps("12:12-13"), cp("12:14", to="saying,"), say("12:14", frm="My father made"), caps("12:15")], "1KGS 12:12–15", REHOBOAM, bg=RED, head="Whips and Scorpions"),
        face([cp("12:16", to="saying,"), say("12:16", frm="What portion", to="see to thine own house, David."), cp("12:16", frm="So Israel departed")], "1KGS 12:16", ISRAELITE, bg=RED,
             head="To Your Tents, O Israel"),
        drawn([caps("12:17-19")], "1KGS 12:17–19", below(lambda w, h: K.to_tents("tt9", w, h, 905), 0.3), "#C8B8A0"),
        face([caps("12:20")], "1KGS 12:20", JEROBOAM),
        drawn([caps("12:21"), cp("12:22"), cp("12:23"), joined("god", ("12:24", "Thus saith Jehovah,", "for this thing is of me.")),
               cp("12:24", frm="So they hearkened")], "1KGS 12:21–24", lambda w, h: __import__("sa2.art", fromlist=["x"]).nathan_night(w, h, 906), "#0F0E2A"),
        face([caps("12:25"), cp("12:26", to="in his heart,"), joined("say", ("12:26", "Now will the kingdom"), "12:27")], "1KGS 12:25–27", JEROBOAM_AFRAID, bg=COLD, head="Two Calves of Gold"),
        drawn([cp("12:28", to="and he said unto them,"), say("12:28", frm="It is too much"), caps("12:29-30")], "1KGS 12:28–30", below(lambda w, h: K.calves("cv9", w, h, 907), 0.34), "#5A3A5A"),
        drawn([caps("12:31-33")], "1KGS 12:31–33", below(lambda w, h: K.bethel_altar("ba9", w, h, 908), 0.4), "#5A3A5A"),
        drawn([caps("13:1"), cp("13:2", to="and said,"), say("13:2", frm="O altar, altar,")], "1KGS 13:1–2", below(lambda w, h: K.bethel_altar("ba9b", w, h, 909), 0.36), "#5A3A5A",
              head="O Altar, Altar", stamp=13),
        face([cp("13:3", to="saying,"), say("13:3", frm="This is the sign")], "1KGS 13:3", MAN_OF_GOD),
        drawn([cp("13:4", to="saying,"), say("13:4", frm="Lay hold on him.", to="Lay hold on him."), cp("13:4", frm="And his hand,"), caps("13:5")], "1KGS 13:4–5",
              below(lambda w, h: K.bethel_altar("ba9c", w, h, 910, rent=True, hand=True), 0.36), "#5A3A5A"),
        face([cp("13:6", to="unto the man of God,"), say("13:6", frm="Entreat now", to="restored me again."), cp("13:6", frm="And the man of God entreated")], "1KGS 13:6", JEROBOAM_AFRAID, bg=COLD),
        face([cp("13:7", to="unto the man of God,"), say("13:7", frm="Come home"), cp("13:8", to="unto the king,"), joined("say", ("13:8", "If thou wilt give"), "13:9"), caps("13:10")],
             "1KGS 13:7–10", MAN_OF_GOD),
        face([caps("13:11"), cp("13:12", to="said unto them,"), say("13:12", frm="What way went he?", to="What way went he?"), cp("13:12", frm="Now his sons"), cp("13:13", to="unto his sons,"),
              say("13:13", frm="Saddle me the ass.", to="Saddle me the ass."), cp("13:13", frm="So they saddled")], "1KGS 13:11–13", OLD_PROPHET, head="The Old Prophet"),
        drawn([cp("13:14", to="and he said unto him,"), say("13:14", frm="Art thou", to="from Judah?"), cp("13:14", frm="And he said,", to="And he said,", after="Art thou"), say("13:14", frm="I am."),
               cp("13:15", to="Then he said unto him,"), say("13:15", frm="Come home")], "1KGS 13:14–15", below(lambda w, h: K.oak_sitting("os9", w, h, 911), 0.36), "#E8C8A0"),
        face([cp("13:16", to="And he said,"), joined("say", ("13:16", "I may not"), "13:17")], "1KGS 13:16–17", MAN_OF_GOD),
        face([cp("13:18", to="And he said unto him,"), say("13:18", frm="I also am", to="drink water."), cp("13:18", frm="But he lied"), caps("13:19")], "1KGS 13:18–19", OLD_PROPHET, bg=RED),
        face([caps("13:20"), cp("13:21", to="saying,"), joined("god", ("13:21", "Thus saith Jehovah,"), "13:22")], "1KGS 13:20–22", OLD_PROPHET, bg=NIGHT),
        drawn([caps("13:23-25")], "1KGS 13:23–25", lambda w, h: K.lion_way("lw9", w, h, 912), "#C8B8A0", head="A Lion in the Way"),
        face([cp("13:26", to="he said,"), say("13:26", frm="It is the man of God,"), cp("13:27", to="saying,"), say("13:27", frm="Saddle me", to="the ass."), cp("13:27", frm="And they saddled it.")],
             "1KGS 13:26–27", OLD_PROPHET_W, bg=COLD),
        drawn([caps("13:28-29")], "1KGS 13:28–29", lambda w, h: K.lion_way("lw9b", w, h, 913), "#C8B8A0"),
        face([cp("13:30", to="saying,"), say("13:30", frm="Alas, my brother!"), cp("13:31", to="saying,"), joined("say", ("13:31", "When I am dead,"), "13:32")], "1KGS 13:30–32", OLD_PROPHET_W, bg=COLD),
        drawn([caps("13:33-34")], "1KGS 13:33–34", lambda w, h: K.calves("cv9b", w, h, 914, people=False), "#5A3A5A")]
PG.extend(pack(SEGS, "1KI-C09-D", PG.next(), end=end_mark("NEXT · AHIJAH'S WORD", "right: 10px; bottom: 34px")))
