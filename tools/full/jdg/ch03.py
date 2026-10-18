"""Judges volume, Chapter 3 — Gideon (Judges 6–7). Every verse, word for word from ref/asv.
Midian as locusts for multitude and Israel in the dens and caves; the prophet; the angel of Jehovah under the oak at Ophrah
(his words in the Voice box), Gideon beating out wheat in the winepress, the fire out of the rock, Jehovah-shalom; the altar
of Baal thrown down by night and Joash's answer, Jerubbaal; the fleece wet and dry; the three hundred that lapped; the dream
of the cake of barley bread; trumpets, pitchers and torches — the sword of Jehovah and of Gideon (the digest's panels); and
Oreb and Zeeb (7:25 as words over the Jordan: no heads drawn)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from genesis import art as X
from jdg import G, art as K
from jdg.common import pack, say, gd, cp, says, gods, caps, over, face, drawn, D, GIDEON, GIDEON_BOLD, GIDEON_CALM, ISRAELITE, RED, COLD, GOLDEN
from jdg import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHTA = lambda w, h: X.cosmic(w, h)


@P("JDG-C03-00-Title", "Chapter 3 · Gideon", title=True)
def title(n):
    bg, art = D("A7", 1)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#14123A"></rect><g transform="translate(0 300)">{art(760, 780)}</g>')
    return chapter_title(3, "第三話", "Gideon", "Judges 6 – 7", svg, "#14123A", v("7:20", frm="The sword of Jehovah"), "Judges · Volume Seven")


SEGS = [drawn([caps("6:1-2")], "JDG 6:1–2", lambda w, h: K.dens(w, h, 311), "#8A6A4A", head="As Locusts for Multitude", stamp=6),
        drawn([caps("6:3-6")], "JDG 6:3–6", lambda w, h: K.midian(w, h, 312), "#E8B880"),
        drawn([cp("6:7"), cp("6:8", to="and he said unto them,"), gd("6:8", frm="Thus saith Jehovah"), gods("6:9-10")], "JDG 6:7–10", NIGHTA, "#0B0B2A"),
        over([caps("6:11")], "JDG 6:11", "A4", 0, head="Thou Mighty Man of Valor"),
        over([cp("6:12", to="and said unto him,"), gd("6:12", frm="Jehovah is with thee,")], "JDG 6:12", "A4", 1),
        face([cp("6:13", to="And Gideon said unto him,"), say("6:13", frm="Oh, my lord,")], "JDG 6:13", GIDEON),
        face([cp("6:14", to="and said,"), gd("6:14", frm="Go in this"), cp("6:15", to="And he said unto him,"), say("6:15", frm="Oh, Lord,")], "JDG 6:14–15", GIDEON_BOLD, bg=GOLDEN),
        face([cp("6:16", to="said unto him,"), gd("6:16", frm="Surely"), cp("6:17", to="And he said unto him,"), ("say", v("6:17", frm="If now") + " " + v("6:18", to="before thee.")),
              cp("6:18", frm="And he said,", to="And he said,"), gd("6:18", frm="I will tarry")], "JDG 6:16–18", GIDEON, bg=COLD),
        drawn([caps("6:19"), cp("6:20", to="said unto him,"), gd("6:20", frm="Take the flesh", to="pour out the broth."), cp("6:20", frm="And he did so."), caps("6:21")], "JDG 6:19–21",
              lambda w, h: K.rock_fire(w, h, 313), "#3A2A1E", head="Fire out of the Rock"),
        face([cp("6:22", to="and Gideon said,"), say("6:22", frm="Alas,"), cp("6:23", to="said unto him,"), gd("6:23", frm="Peace be"), caps("6:24")], "JDG 6:22–24", GIDEON),
        drawn([cp("6:25", to="said unto him,"), gd("6:25", frm="Take thy father's"), gd("6:26")], "JDG 6:25–26", NIGHTA, "#0B0B2A", head="Jerubbaal"),
        drawn([caps("6:27-28")], "JDG 6:27–28", lambda w, h: K.baal_down(w, h, 314), "#F3B86A"),
        face([cp("6:29", to="one to another,"), say("6:29", frm="Who hath done", to="this thing?"), cp("6:29", frm="And when they inquired", to="they said,"),
              say("6:29", frm="Gideon the son"), cp("6:30", to="unto Joash,"), say("6:30", frm="Bring out")], "JDG 6:29–30", ISRAELITE, bg=RED),
        face([cp("6:31", to="stood against him,"), say("6:31", frm="Will ye contend"), cp("6:32", to="saying,"), say("6:32", frm="Let Baal")], "JDG 6:31–32", ISRAELITE),
        drawn([caps("6:33-35")], "JDG 6:33–35", lambda w, h: K.midian(w, h, 315), "#E8B880"),
        over([cp("6:36", to="And Gideon said unto God,"), ("say", v("6:36", frm="If thou") + " " + v("6:37"))], "JDG 6:36–37", "A5", 0, head="The Fleece"),
        over([caps("6:38")], "JDG 6:38", "A5", 1),
        face([cp("6:39", to="And Gideon said unto God,"), say("6:39", frm="Let not")], "JDG 6:39", GIDEON),
        over([caps("6:40")], "JDG 6:40", "A5", 3),
        drawn([caps("7:1"), cp("7:2", to="unto Gideon,"), gd("7:2", frm="The people"), gd("7:3", to="from mount Gilead."), cp("7:3", frm="And there returned")], "JDG 7:1–3",
              lambda w, h: K.midian(w, h, 316), "#E8B880", head="Three Hundred Men", stamp=7),
        over([cp("7:4", to="unto Gideon,"), gd("7:4", frm="The people are"), cp("7:5", to="unto Gideon,"), gd("7:5", frm="Every one")], "JDG 7:4–5", "A6", 0),
        over([caps("7:6")], "JDG 7:6", "A6", 1),
        over([cp("7:7", to="unto Gideon,"), gd("7:7", frm="By the three"), caps("7:8")], "JDG 7:7–8", "A6", 1),
        drawn([cp("7:9", to="said unto him,"), gd("7:9", frm="Arise,"), gods("7:10"), gd("7:11", to="into the camp."), cp("7:11", frm="Then went he down"), caps("7:12")], "JDG 7:9–12",
              lambda w, h: K.midian(w, h, 317, night_=True), "#14123A", head="A Cake of Barley Bread"),
        drawn([cp("7:13", to="and he said,"), say("7:13", frm="Behold, I dreamed"), cp("7:14", to="answered and said,"), say("7:14", frm="This is nothing")], "JDG 7:13–14",
              lambda w, h: K.dream_cake(w, h, 318), "#14123A"),
        face([cp("7:15", to="and said,"), say("7:15", frm="Arise;"), caps("7:16"), cp("7:17", to="And he said unto them,"), ("say", v("7:17", frm="Look on me") + " " + v("7:18"))],
             "JDG 7:15–18", GIDEON_BOLD, bg=RED),
        over([caps("7:19")], "JDG 7:19", "A7", 0, head="The Sword of Jehovah and of Gideon"),
        over([cp("7:20")], "JDG 7:20", "A7", 1),
        over([caps("7:21-23")], "JDG 7:21–23", "A8", 0),
        drawn([cp("7:24", to="saying,"), say("7:24", frm="Come down", to="even the Jordan."), cp("7:24", frm="So all the men"), caps("7:25")], "JDG 7:24–25",
              lambda w, h: K.ephraim_waters("ew3", w, h, 319), "#F3B86A", head="Oreb and Zeeb")]
PG.extend(pack(SEGS, "JDG-C03-D", PG.next(), end=end_mark("NEXT · ABIMELECH", "right: 10px; bottom: 34px")))
