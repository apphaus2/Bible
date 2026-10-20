"""1 Samuel volume, Chapter 10 — Jonathan and David (1 Samuel 20–21). Every verse, word for word from ref/eng-asv.
What have I done?; a step between me and death; the covenant with the house of David; the new moon and David's place empty;
Saul's spear cast at Jonathan; three arrows by the stone Ezel — Is not the arrow beyond thee?; they kissed one another and
wept; then Nob, Ahimelech, the holy bread and the sword of Goliath wrapped in a cloth; Doeg the Edomite; and David feigning
himself mad at the gate of Gath."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from sa1 import G, art as K
from sa1.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, SAUL_MAD, DAVID, DAVID_GRIEVED, JONATHAN, PHILISTINE, RED, COLD, GOLDEN)
from sa1 import ch09 as _prev

v, sp = G.v, G.span
AHIMELECH = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#C8C2B6", hl="#8A867E", beard=True, beard_color="#C8C2B6", scarf="#F3EFE6", band=True, sweat=True, brow="sorrow", light="#FFE680")
ACHISH = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#1F5FAD", band=True, light="#FFC14D")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1SA-C10-00-Title", "Chapter 10 · Jonathan and David", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#F3D8A0"></rect><g transform="translate(0 360)">{K.arrows("t10", 760, 720, 1001)}</g>')
    return chapter_title(10, "第十話", "Jonathan and David", "1 Samuel 20 – 21", svg, "#F3D8A0", v("20:42", frm="Jehovah shall be between me and thee,", to="for ever."), "1 Samuel · Volume Nine")


SEGS = [face([cp("20:1", to="before Jonathan,"), say("20:1", frm="What have I done?")], "1SAM 20:1", DAVID_GRIEVED, bg=COLD, head="A Step between Me and Death", stamp=20),
        face([cp("20:2", to="said unto him,"), say("20:2", frm="Far from it;")], "1SAM 20:2", JONATHAN),
        face([cp("20:3", to="and said,"), say("20:3", frm="Thy father knoweth"), cp("20:4", to="unto David,"), say("20:4", frm="Whatsoever")], "1SAM 20:3–4", DAVID_GRIEVED, bg=COLD),
        face([cp("20:5", to="unto Jonathan,"), ("say", v("20:5", frm="Behold,") + " " + sp("20:6-8"))], "1SAM 20:5–8", DAVID),
        face([cp("20:9", to="And Jonathan said,"), say("20:9", frm="Far be it"), cp("20:10", to="to Jonathan,"), say("20:10", frm="Who shall tell"),
              cp("20:11", to="unto David,"), say("20:11", frm="Come,", to="into the field."), cp("20:11", frm="And they went out")], "1SAM 20:9–11", JONATHAN),
        face([cp("20:12", to="unto David,"), ("say", v("20:12", frm="Jehovah,") + " " + sp("20:13-15"))], "1SAM 20:12–15", JONATHAN, head="The Covenant with the House of David"),
        face([cp("20:16", to="saying,"), say("20:16", frm="And Jehovah will"), caps("20:17"), cp("20:18", to="said unto him,"), ("say", v("20:18", frm="To-morrow") + " " + v("20:19"))],
             "1SAM 20:16–19", JONATHAN),
        drawn([says("20:20-23")], "1SAM 20:20–23", lambda w, h: K.arrows("ar10", w, h, 1011), "#F3D8A0"),
        drawn([caps("20:24-25"), cp("20:26", to="for he thought,"), say("20:26", frm="Something")], "1SAM 20:24–26", lambda w, h: K.empty_seat(w, h, 1012), "#5A2A3A",
              head="David's Place Was Empty"),
        face([cp("20:27", to="unto Jonathan his son,"), say("20:27", frm="Wherefore cometh")], "1SAM 20:27", SAUL_MAD, bg=RED),
        face([cp("20:28", to="answered Saul,"), ("say", v("20:28", frm="David earnestly") + " " + v("20:29"))], "1SAM 20:28–29", JONATHAN),
        face([cp("20:30", to="and he said unto him,"), ("say", v("20:30", frm="Thou son") + " " + v("20:31"))], "1SAM 20:30–31", SAUL_MAD, bg=RED),
        face([cp("20:32", to="and said unto him,"), say("20:32", frm="Wherefore"), caps("20:33-34")], "1SAM 20:32–34", JONATHAN, bg=COLD),
        drawn([caps("20:35"), cp("20:36", to="unto his lad,"), say("20:36", frm="Run,", to="which I shoot."), cp("20:36", frm="And as the lad ran,"), cp("20:37", to="and said,"),
               say("20:37", frm="Is not the arrow")], "1SAM 20:35–37", lambda w, h: K.arrows("ar10b", w, h, 1013), "#F3D8A0", head="Is Not the Arrow beyond Thee?"),
        drawn([cp("20:38", to="after the lad,"), say("20:38", frm="Make speed,", to="stay not."), cp("20:38", frm="And Jonathan's lad"), caps("20:39"), cp("20:40", to="said unto him,"),
               say("20:40", frm="Go, carry")], "1SAM 20:38–40", lambda w, h: K.arrows("ar10c", w, h, 1014), "#F3D8A0"),
        over([caps("20:41")], "1SAM 20:41", "B8", 0),
        face([cp("20:42", to="to David,"), say("20:42", frm="Go in peace,", to="for ever."), cp("20:42", frm="And he arose")], "1SAM 20:42", JONATHAN, bg=COLD),
        face([cp("21:1", to="and said unto him,"), say("21:1", frm="Why art thou")], "1SAM 21:1", AHIMELECH, head="The Holy Bread", stamp=21),
        face([cp("21:2", to="the priest,"), ("say", v("21:2", frm="The king") + " " + v("21:3"))], "1SAM 21:2–3", DAVID),
        face([cp("21:4", to="and said,"), say("21:4", frm="There is no"), cp("21:5", to="said unto him,"), say("21:5", frm="Of a truth")], "1SAM 21:4–5", AHIMELECH),
        drawn([caps("21:6-7")], "1SAM 21:6–7", lambda w, h: K.showbread(w, h, 1015), "#2A1A2E"),
        face([cp("21:8", to="unto Ahimelech,"), say("21:8", frm="And is there not"), cp("21:9", to="And the priest said,"), say("21:9", frm="The sword of Goliath", to="save that here."),
              cp("21:9", frm="And David said,", to="And David said,"), say("21:9", frm="There is none")], "1SAM 21:8–9", AHIMELECH),
        drawn([caps("21:10"), cp("21:11", to="said unto him,"), say("21:11", frm="Is not this"), caps("21:12-13")], "1SAM 21:10–13", lambda w, h: K.gath_gate("gg10", w, h, 1016), "#E8B880",
              head="At the Gate of Gath"),
        face([cp("21:14", to="unto his servants,"), ("say", v("21:14", frm="Lo,") + " " + v("21:15"))], "1SAM 21:14–15", ACHISH)]
PG.extend(pack(SEGS, "1SA-C10-D", PG.next(), end=end_mark("NEXT · THE CAVE", "right: 10px; bottom: 34px")))
