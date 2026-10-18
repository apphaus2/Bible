"""Judges volume, Chapter 4 — Abimelech (Judges 8–9). Every verse, word for word from ref/asv.
Ephraim's chiding; faint, yet pursuing; Succoth and Penuel; Zebah and Zalmunna (8:21 words only); I will not rule over you;
the golden ear-rings and the ephod in Ophrah; Gideon's death; then Abimelech made king at Shechem (9:5 as words over the
stone at Ophrah's ruin: nothing drawn), Jotham's fable from the top of Gerizim, Gaal and Zebul, Shechem sowed with salt, the
stronghold of El-berith burnt, and the tower of Thebez (9:53–54 are words over the tower: nothing of the blow drawn)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from genesis import art as X
from jos import art as JA
from jdg import G, art as K
from jdg.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, GIDEON_BOLD, GIDEON_CALM, GIDEON_OLD, ISRAELITE, KING_MIDIAN,
                        ABIMELECH, JOTHAM, GAAL, ZEBUL, RED, COLD, GOLDEN)
from jdg import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JDG-C04-00-Title", "Chapter 4 · Abimelech", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#2A0A0A"></rect><g transform="translate(0 340)">{K.fable(760, 740, "bramble", 401)}</g>')
    return chapter_title(4, "第四話", "Abimelech", "Judges 8 – 9", svg, "#2A0A0A", v("9:15", frm="let fire come out"), "Judges · Volume Seven")


SEGS = [face([cp("8:1", to="said unto him,"), say("8:1", frm="Why hast", to="fight with Midian?"), cp("8:1", frm="And they did chide")], "JDG 8:1", ISRAELITE, bg=RED,
             head="Faint, Yet Pursuing", stamp=8),
        face([cp("8:2", to="said unto them,"), ("say", v("8:2", frm="What have") + " " + v("8:3", to="in comparison with you?")), cp("8:3", frm="Then their anger")], "JDG 8:2–3", GIDEON_CALM),
        drawn([caps("8:4"), cp("8:5", to="men of Succoth,"), say("8:5", frm="Give, I pray"), cp("8:6", to="Succoth said,"), say("8:6", frm="Are the hands")], "JDG 8:4–6",
              lambda w, h: K.tower(w, h, 411), "#E8B880"),
        face([cp("8:7", to="And Gideon said,"), say("8:7", frm="Therefore"), caps("8:8"), cp("8:9", to="saying,"), say("8:9", frm="When I come")], "JDG 8:7–9", GIDEON_BOLD, bg=RED),
        drawn([caps("8:10-13")], "JDG 8:10–13", lambda w, h: K.midian(w, h, 412, night_=True), "#14123A", head="Zebah and Zalmunna"),
        drawn([caps("8:14"), cp("8:15", to="and said,"), say("8:15", frm="Behold Zebah"), caps("8:16-17")], "JDG 8:14–17", lambda w, h: K.tower(w, h, 413), "#E8B880"),
        face([cp("8:18", to="Zebah and Zalmunna,"), say("8:18", frm="What manner", to="at Tabor?"), cp("8:18", frm="And they answered,", to="And they answered,"),
              say("8:18", frm="As thou art,")], "JDG 8:18", KING_MIDIAN, bg=COLD),
        face([cp("8:19", to="And he said,"), say("8:19", frm="They were"), cp("8:20", to="his first-born,"), say("8:20", frm="Up,", to="slay them."), cp("8:20", frm="But the youth")],
             "JDG 8:19–20", GIDEON_BOLD, bg=RED),
        face([cp("8:21", to="Zalmunna said,"), say("8:21", frm="Rise thou,", to="his strength."), cp("8:21", frm="And Gideon arose")], "JDG 8:21", KING_MIDIAN, bg=COLD),
        over([cp("8:22", to="unto Gideon,"), say("8:22", frm="Rule thou")], "JDG 8:22", "A8", 1, head="Jehovah Shall Rule over You"),
        over([cp("8:23", to="said unto them,"), say("8:23", frm="I will not")], "JDG 8:23", "A8", 2),
        drawn([cp("8:24", to="said unto them,"), say("8:24", frm="I would make", to="of his spoil."), cp("8:24", frm="(For they"), cp("8:25", to="And they answered,"),
               say("8:25", frm="We will", to="give them."), cp("8:25", frm="And they spread"), caps("8:26")], "JDG 8:24–26", lambda w, h: K.earrings(w, h, 414), "#3A2A1E"),
        drawn([caps("8:27")], "JDG 8:27", lambda w, h: K.ephod(w, h, 415), "#2A1A2E"),
        over([caps("8:28")], "JDG 8:28", "A8", 3),
        face([caps("8:29-32")], "JDG 8:29–32", GIDEON_OLD, head="Gideon Died in a Good Old Age"),
        drawn([caps("8:33-35")], "JDG 8:33–35", lambda w, h: K.baalim(w, h, 416), "#5A1A2A"),
        face([cp("9:1"), says("9:2"), caps("9:3-4")], "JDG 9:1–4", ABIMELECH, bg=RED, head="Abimelech", stamp=9),
        drawn([caps("9:5-6")], "JDG 9:5–6", lambda w, h: JA.shechem("sc4", w, h, 417, stone=True, joshua=False), "#F3D8A0"),
        drawn([cp("9:7", to="and said unto them,"), say("9:7", frm="Hearken unto me,")], "JDG 9:7", lambda w, h: K.jotham("jo4", w, h, 418), "#8FD0E2", head="Jotham's Fable"),
        drawn([says("9:8-9")], "JDG 9:8–9", lambda w, h: K.fable(w, h, "olive", 419), "#E8E2C8"),
        drawn([says("9:10-11")], "JDG 9:10–11", lambda w, h: K.fable(w, h, "fig", 420), "#E8E2C8"),
        drawn([says("9:12-13")], "JDG 9:12–13", lambda w, h: K.fable(w, h, "vine", 421), "#E8E2C8"),
        drawn([says("9:14-15")], "JDG 9:14–15", lambda w, h: K.fable(w, h, "bramble", 422), "#2A0A0A"),
        face([says("9:16-18")], "JDG 9:16–18", JOTHAM),
        face([says("9:19-20"), caps("9:21")], "JDG 9:19–21", JOTHAM, bg=COLD),
        drawn([caps("9:22-25")], "JDG 9:22–25", lambda w, h: X.cosmic(w, h), "#0B0B2A", head="Gaal the Son of Ebed"),
        face([caps("9:26-27"), cp("9:28", to="said,"), ("say", v("9:28", frm="Who is") + " " + v("9:29", to="remove Abimelech.")), cp("9:29", frm="And he said to Abimelech,", to="to Abimelech,"),
              say("9:29", frm="Increase")], "JDG 9:26–29", GAAL, bg=RED),
        face([caps("9:30"), cp("9:31", to="saying,"), ("say", v("9:31", frm="Behold,") + " " + sp("9:32-33"))], "JDG 9:30–33", ZEBUL, bg=COLD),
        drawn([caps("9:34-35"), cp("9:36", to="to Zebul,"), say("9:36", frm="Behold, there come", to="mountains."), cp("9:36", frm="And Zebul said unto him,", to="said unto him,"),
               say("9:36", frm="Thou seest")], "JDG 9:34–36", lambda w, h: K.tower(w, h, 423), "#E8B880"),
        face([cp("9:37", to="again and said,"), say("9:37", frm="See,"), cp("9:38", to="unto him,"), say("9:38", frm="Where is now")], "JDG 9:37–38", ZEBUL),
        drawn([caps("9:39-45")], "JDG 9:39–45", lambda w, h: K.salt(w, h, 424), "#8A8A9A", head="Sowed It with Salt"),
        drawn([caps("9:46-47"), cp("9:48", to="were with him,"), say("9:48", frm="What ye have")], "JDG 9:46–48", lambda w, h: K.boughs("bo4", w, h, 425), "#E8B880"),
        drawn([caps("9:49")], "JDG 9:49", lambda w, h: K.tower(w, h, 426, night_=True, fire=True), "#14123A"),
        drawn([caps("9:50-53")], "JDG 9:50–53", lambda w, h: K.tower(w, h, 427, people_on_roof=True), "#E8B880", head="The Tower of Thebez"),
        drawn([cp("9:54", to="said unto him,"), say("9:54", frm="Draw thy", to="A woman slew him."), cp("9:54", frm="And his young man"), caps("9:55-57")], "JDG 9:54–57",
              lambda w, h: K.tower(w, h, 428, people_on_roof=True), "#E8B880")]
PG.extend(pack(SEGS, "JDG-C04-D", PG.next(), end=end_mark("NEXT · JEPHTHAH", "right: 10px; bottom: 34px")))
