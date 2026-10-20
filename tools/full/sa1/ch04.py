"""1 Samuel volume, Chapter 4 — Saul Anointed (1 Samuel 9–10). Every verse, word for word from ref/eng-asv.
Kish's lost asses and Saul, higher than any of the people; the servant's quarter shekel and the seer; Jehovah's word to
Samuel a day before; the thigh reserved; the vial of oil (the digest's anointing panels); the three signs and the band of
prophets — Is Saul also among the prophets?; the lot at Mizpah and Saul hid among the baggage; Long live the king."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from genesis import art as X
from jos import art as JA
from sa1 import G, art as K
from sa1.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, SAUL, SAUL_ANOINTED, SAMUEL_OLD, ISRAELITE, RED, COLD, GOLDEN)
from sa1 import ch03 as _prev

v, sp = G.v, G.span
SERVANT = F("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", light="#FFE680")
UNCLE = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#8A8478", hl="#6A645E", beard=True, beard_color="#8A8478", scarf="#7A3A2A", cord=True, light="#FFC14D")
MAIDEN = F("eve", skin="#D9A27A", shadow="#8A5A3E", hair="#1A1210", scarf="#5AC8C8", light="#FFE680")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHTA = lambda w, h: X.cosmic(w, h)


@P("1SA-C04-00-Title", "Chapter 4 · Saul Anointed", title=True)
def title(n):
    bg, art = D("A9", 1)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#FFC14D"></rect><g transform="translate(0 340)">{art(760, 740)}</g>')
    return chapter_title(4, "第四話", "Saul Anointed", "1 Samuel 9 – 10", svg, "#FFC14D", v("10:1", frm="Is it not that Jehovah"), "1 Samuel · Volume Nine")


SEGS = [over([caps("9:1-2")], "1SAM 9:1–2", "A9", 0, head="The Asses of Kish", stamp=9),
        drawn([cp("9:3", to="said to Saul his son,"), say("9:3", frm="Take now"), caps("9:4")], "1SAM 9:3–4", lambda w, h: K.asses_search("as4", w, h, 411), "#F3D8A0"),
        face([cp("9:5", to="that was with him,"), say("9:5", frm="Come,")], "1SAM 9:5", SAUL),
        face([cp("9:6", to="said unto him,"), say("9:6", frm="Behold now,")], "1SAM 9:6", SERVANT),
        face([cp("9:7", to="to his servant,"), say("9:7", frm="But, behold,")], "1SAM 9:7", SAUL),
        face([cp("9:8", to="and said,"), say("9:8", frm="Behold, I have"), caps("9:9")], "1SAM 9:8–9", SERVANT),
        drawn([cp("9:10", to="to his servant,"), say("9:10", frm="Well said;", to="let us go."), cp("9:10", frm="So they went"), cp("9:11", to="and said unto them,"), say("9:11", frm="Is the seer here?")],
              "1SAM 9:10–11", lambda w, h: K.high_place("hp4", w, h, 412), "#8FD0E2", head="Is the Seer Here?"),
        face([cp("9:12", to="and said,"), ("say", v("9:12", frm="He is;") + " " + v("9:13"))], "1SAM 9:12–13", MAIDEN),
        drawn([caps("9:14-15"), gods("9:16")], "1SAM 9:14–16", NIGHTA, "#0B0B2A"),
        face([cp("9:17", to="said unto him,"), gd("9:17", frm="Behold, the man"), cp("9:18", to="and said,"), say("9:18", frm="Tell me,")], "1SAM 9:17–18", SAMUEL_OLD,
             head="I Am the Seer"),
        face([cp("9:19", to="and said,"), ("say", v("9:19", frm="I am the seer;") + " " + v("9:20"))], "1SAM 9:19–20", SAMUEL_OLD),
        face([cp("9:21", to="answered and said,"), say("9:21", frm="Am not I")], "1SAM 9:21", SAUL, bg=COLD),
        face([caps("9:22"), cp("9:23", to="unto the cook,"), say("9:23", frm="Bring the portion"), cp("9:24", to="And Samuel said,"), say("9:24", frm="Behold, that which", to="I have invited the people."),
              cp("9:24", frm="So Saul did eat")], "1SAM 9:22–24", SAMUEL_OLD),
        drawn([caps("9:25"), cp("9:26", to="saying,"), say("9:26", frm="Up,", to="send thee away."), cp("9:26", frm="And Saul arose,"), cp("9:27", to="said to Saul,"),
               say("9:27", frm="Bid the servant")], "1SAM 9:25–27", lambda w, h: JA.night(w, h, 413, "#2A2458") + JA.J.city_hill(w * 0.5, h, w * 0.5, h * 0.4, 413), "#2A2458"),
        over([cp("10:1", to="and kissed him, and said,"), say("10:1", frm="Is it not")], "1SAM 10:1", "A9", 1, head="The Vial of Oil", stamp=10),
        face([says("10:2-4")], "1SAM 10:2–4", SAMUEL_OLD),
        face([says("10:5-8")], "1SAM 10:5–8", SAMUEL_OLD),
        drawn([caps("10:9-10")], "1SAM 10:9–10", lambda w, h: K.prophets("pr4", w, h, 414), "#F3B86A", head="Is Saul Also among the Prophets?"),
        face([cp("10:11", to="one to another,"), say("10:11", frm="What is this"), cp("10:12", to="answered and said,"), say("10:12", frm="And who is", to="their father?"),
              cp("10:12", frm="Therefore it became", to="a proverb,"), say("10:12", frm="Is Saul also"), caps("10:13")], "1SAM 10:11–13", ISRAELITE),
        face([cp("10:14", to="and to his servant,"), say("10:14", frm="Whither went ye?", to="Whither went ye?"), cp("10:14", frm="And he said,", to="And he said,"), say("10:14", frm="To seek"),
              cp("10:15", to="And Saul's uncle said,"), say("10:15", frm="Tell me,")], "1SAM 10:14–15", UNCLE),
        face([cp("10:16", to="unto his uncle,"), say("10:16", frm="He told us", to="were found."), cp("10:16", frm="But concerning")], "1SAM 10:16", SAUL),
        drawn([caps("10:17"), cp("10:18", to="Thus saith Jehovah, the God of Israel,"), gd("10:18", frm="I brought up"), gd("10:19", to="set a king over us."), say("10:19", frm="Now therefore present")],
              "1SAM 10:17–19", lambda w, h: JA.armed("mz4", w, h, 415, tribes=("JUDAH", "BENJAMIN", "EPHRAIM")), "#F3D8A0", head="Long Live the King"),
        drawn([caps("10:20-21"), cp("10:22", to="Is there yet a man to come hither?"), cp("10:22", frm="And Jehovah answered,", to="And Jehovah answered,"), gd("10:22", frm="Behold,")],
              "1SAM 10:20–22", lambda w, h: K.baggage("bg4", w, h, 416), "#E8C88A"),
        over([caps("10:23"), cp("10:24", to="to all the people,"), say("10:24", frm="See ye him", to="among all the people?"), cp("10:24", frm="And all the people shouted,", to="and said,"),
              say("10:24", frm="Long live the king.")], "1SAM 10:23–24", "A9", 2),
        drawn([caps("10:25-26"), cp("10:27", to="said,"), say("10:27", frm="How shall", to="save us?"), cp("10:27", frm="And they despised")], "1SAM 10:25–27",
              lambda w, h: JA.ai("gb4", w, h, 417), "#F3D8A0")]
PG.extend(pack(SEGS, "1SA-C04-D", PG.next(), end=end_mark("NEXT · TO OBEY IS BETTER", "right: 10px; bottom: 34px")))
