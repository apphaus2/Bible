"""Judges volume, Chapter 6 — Samson (Judges 13–15). Every verse, word for word from ref/asv.
The angel of Jehovah to Manoah's wife (the Voice box; the digest's Nazirite panels), Manoah's prayer, the name that is
wonderful and the angel ascending in the flame of the altar; Samson born; the woman of Timnah, the young lion, the honey,
the riddle at the feast; the three hundred foxes and the burning grain (15:6 is words over the burnt field); the rock of
Etam, the new ropes, the jawbone of an ass, and En-hakkore (the slaughters are words over the digest's panels)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jdg import G, art as K
from jdg.common import pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, SAMSON, MANOAH_WIFE, ISRAELITE, RED, COLD, GOLDEN
from jdg import ch05 as _prev

v, sp = G.v, G.span
MANOAH = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#6A5A4E", hl="#8A867E", beard=True, beard_color="#6A5A4E", scarf="#5A6E8A", cord=True, light="#FFE680")
MANOAH_AFRAID = F("adam", skin="#E3B08A", shadow="#5A4A3A", hair="#6A5A4E", hl="#8A867E", beard=True, beard_color="#6A5A4E", scarf="#5A6E8A", cord=True, brow="sorrow", sweat=True, light="#FFF4C2")
TIMNITE = F("eve", skin="#D9A27A", shadow="#7A4A4A", hair="#1A1210", band=True, tear=True, light="#FF8A3D")
TIMNITE_FATHER = F("adam", skin="#B98A6E", shadow="#4A2A3A", hair="#B8B2A6", hl="#8A867E", beard=True, beard_color="#B8B2A6", scarf="#1F5FAD", band=True, light="#FFC14D")
PHILISTINE = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", scarf="#1F5FAD", band=True, brow="scowl", light="#D7261E")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JDG-C06-00-Title", "Chapter 6 · Samson", title=True)
def title(n):
    bg, art = D("B2", 1)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#D7261E"></rect><g transform="translate(0 340)">{art(760, 740)}</g>')
    return chapter_title(6, "第六話", "Samson", "Judges 13 – 15", svg, "#D7261E", v("14:14", frm="Out of the eater", to="came forth sweetness."), "Judges · Volume Seven")


SEGS = [over([caps("13:1-2"), cp("13:3", to="and said unto her,"), gd("13:3", frm="Behold now,")], "JDG 13:1–3", "B1", 0, head="A Nazirite unto God", stamp=13),
        face([gods("13:4-5")], "JDG 13:4–5", MANOAH_WIFE),
        face([cp("13:6", to="saying,"), ("say", v("13:6", frm="A man of God") + " " + v("13:7"))], "JDG 13:6–7", MANOAH_WIFE, bg=COLD),
        face([cp("13:8", to="and said,"), say("13:8", frm="Oh, Lord,"), caps("13:9")], "JDG 13:8–9", MANOAH),
        over([cp("13:10", to="and said unto him,"), say("13:10", frm="Behold,"), cp("13:11", to="said unto him,"), say("13:11", frm="Art thou", to="unto the woman?"),
              cp("13:11", frm="And he said,", to="And he said,"), gd("13:11", frm="I am.")], "JDG 13:10–11", "B1", 0),
        face([cp("13:12", to="And Manoah said,"), say("13:12", frm="Now let"), cp("13:13", to="unto Manoah,"), gd("13:13", frm="Of all"), gods("13:14")], "JDG 13:12–14", MANOAH),
        face([cp("13:15", to="the angel of Jehovah,"), say("13:15", frm="I pray thee,"), cp("13:16", to="unto Manoah,"), gd("13:16", frm="Though thou", to="unto Jehovah."),
              cp("13:16", frm="For Manoah knew")], "JDG 13:15–16", MANOAH, head="Seeing It Is Wonderful"),
        face([cp("13:17", to="the angel of Jehovah,"), say("13:17", frm="What is thy name,"), cp("13:18", to="said unto him,"), gd("13:18", frm="Wherefore")], "JDG 13:17–18", MANOAH),
        drawn([caps("13:19-21")], "JDG 13:19–21", lambda w, h: K.rock_fire(w, h, 611), "#3A2A1E"),
        face([cp("13:22", to="unto his wife,"), say("13:22", frm="We shall")], "JDG 13:22", MANOAH_AFRAID, bg=COLD),
        face([cp("13:23", to="said unto him,"), say("13:23", frm="If Jehovah")], "JDG 13:23", MANOAH_WIFE),
        over([caps("13:24-25")], "JDG 13:24–25", "B1", 2),
        over([caps("14:1"), cp("14:2", to="and said,"), say("14:2", frm="I have seen")], "JDG 14:1–2", "B2", 0, head="The Young Lion", stamp=14),
        face([cp("14:3", to="said unto him,"), say("14:3", frm="Is there never", to="Philistines?"), cp("14:3", frm="And Samson said", to="his father,"), say("14:3", frm="Get her"),
              caps("14:4")], "JDG 14:3–4", MANOAH),
        over([caps("14:5")], "JDG 14:5", "B2", 1),
        over([caps("14:6-7")], "JDG 14:6–7", "B2", 2),
        drawn([caps("14:8-9")], "JDG 14:8–9", lambda w, h: K.honey(w, h, 612), "#E8C88A"),
        drawn([caps("14:10-11"), cp("14:12", to="said unto them,"), ("say", v("14:12", frm="Let me now") + " " + v("14:13", to="changes of raiment.")),
               cp("14:13", frm="And they said unto him,", to="said unto him,"), say("14:13", frm="Put forth")], "JDG 14:10–13", lambda w, h: K.feast("fe6", w, h, 613), "#6A3A2A",
              head="Out of the Eater Came Forth Food"),
        face([cp("14:14", to="said unto them,"), say("14:14", frm="Out of the eater", to="sweetness."), cp("14:14", frm="And they could not")], "JDG 14:14", SAMSON),
        face([cp("14:15", to="Samson's wife,"), say("14:15", frm="Entice")], "JDG 14:15", PHILISTINE, bg=RED),
        face([cp("14:16", to="and said,"), say("14:16", frm="Thou dost", to="not told it me."), cp("14:16", frm="And he said unto her,", to="said unto her,"), say("14:16", frm="Behold,"),
              caps("14:17")], "JDG 14:16–17", TIMNITE, bg=COLD),
        drawn([cp("14:18", to="went down,"), say("14:18", frm="What is sweeter", to="than a lion?"), cp("14:18", frm="And he said unto them,", to="said unto them,"), say("14:18", frm="If ye had not")],
              "JDG 14:18", lambda w, h: K.feast("fe6b", w, h, 614), "#6A3A2A"),
        drawn([caps("14:19-20")], "JDG 14:19–20", lambda w, h: K.feast("fe6c", w, h, 615), "#6A3A2A"),
        face([cp("15:1", to="and he said,"), say("15:1", frm="I will go in", to="into the chamber."), cp("15:1", frm="But her father")], "JDG 15:1", SAMSON, head="Three Hundred Foxes", stamp=15),
        face([cp("15:2", to="And her father said,"), say("15:2", frm="I verily")], "JDG 15:2", TIMNITE_FATHER),
        face([cp("15:3", to="said unto them,"), say("15:3", frm="This time")], "JDG 15:3", SAMSON, bg=RED),
        over([caps("15:4")], "JDG 15:4", "B3", 0),
        over([caps("15:5")], "JDG 15:5", "B3", 1),
        drawn([cp("15:6", to="Then the Philistines said,"), say("15:6", frm="Who hath done this?", to="Who hath done this?"), cp("15:6", frm="And they said,", to="And they said,"),
               say("15:6", frm="Samson,", to="to his companion."), cp("15:6", frm="And the Philistines came up"), cp("15:7", to="said unto them,"), say("15:7", frm="If ye do"), caps("15:8")],
              "JDG 15:6–8", lambda w, h: K.etam("et6", w, h, 616), "#C8A06A", head="The Rock of Etam"),
        drawn([caps("15:9"), cp("15:10", to="said,"), say("15:10", frm="Why are ye", to="against us?"), cp("15:10", frm="And they said,", to="And they said,"), say("15:10", frm="To bind Samson")],
              "JDG 15:9–10", lambda w, h: K.etam("et6b", w, h, 617, judah=True), "#C8A06A"),
        face([cp("15:11", to="said to Samson,"), say("15:11", frm="Knowest", to="done unto us?"), cp("15:11", frm="And he said unto them,", to="said unto them,"), say("15:11", frm="As they did")],
             "JDG 15:11", ISRAELITE),
        face([cp("15:12", to="said unto him,"), say("15:12", frm="We are come", to="the Philistines."), cp("15:12", frm="And Samson said", to="unto them,"), say("15:12", frm="Swear unto me,"),
              cp("15:13", to="saying,"), say("15:13", frm="No;", to="not kill thee."), cp("15:13", frm="And they bound")], "JDG 15:12–13", SAMSON),
        over([caps("15:14")], "JDG 15:14", "B4", 0, head="The Jawbone of an Ass"),
        over([caps("15:15")], "JDG 15:15", "B4", 1),
        face([cp("15:16", to="And Samson said,"), say("15:16", frm="With the jawbone"), caps("15:17")], "JDG 15:16–17", SAMSON, bg=RED),
        drawn([cp("15:18", to="and said,"), say("15:18", frm="Thou hast given"), caps("15:19-20")], "JDG 15:18–20", lambda w, h: K.en_hakkore(w, h, 618), "#F3B86A", head="En-hakkore")]
PG.extend(pack(SEGS, "JDG-C06-D", PG.next(), end=end_mark("NEXT · DELILAH", "right: 10px; bottom: 34px")))
