"""1 Samuel volume, Chapter 6 — Jonathan at Michmash (1 Samuel 14). Every verse, word for word from ref/asv.
Jonathan and his armorbearer between the crags Bozez and Seneh — no restraint to Jehovah to save by many or by few; Come up
unto us; the trembling and the earthquake; Saul's rash oath; the honey dropping in the forest; the people eating with the
blood and the great stone; the lot between Saul and Jonathan, and the people rescuing Jonathan; Saul's wars as a map, and
his house as roll cells."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from rolls import roll_pages
from deu.common import shade
from genesis import art as X
from jos import art as JA
from jdg import art as JG
from sa1 import G, art as K
from sa1.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, SAUL_KING, SAUL_MAD, JONATHAN, ISRAELITE, PHILISTINE, RED, COLD, GOLDEN)
from sa1 import ch05 as _prev

v, sp = G.v, G.span
ARMORBEARER = F("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", light="#FFC14D")
PRIEST = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E", scarf="#F3EFE6", band=True, light="#FFE680")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("1SA-C06-00-Title", "Chapter 6 · Jonathan at Michmash", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 340)">{K.crags("t6", 760, 740, 601, climbing=True)}</g>')
    return chapter_title(6, "第六話", "Jonathan at Michmash", "1 Samuel 14", svg, "#8FD0E2", v("14:6", frm="there is no restraint"), "1 Samuel · Volume Nine")


SEGS = [face([cp("14:1", to="that bare his armor,"), say("14:1", frm="Come,", to="yonder side."), cp("14:1", frm="But he told not"), caps("14:2-3")], "1SAM 14:1–3", JONATHAN,
             head="By Many or by Few", stamp=14),
        drawn([caps("14:4-5")], "1SAM 14:4–5", lambda w, h: K.crags("cr6", w, h, 611), "#8FD0E2"),
        face([cp("14:6", to="that bare his armor,"), say("14:6", frm="Come,")], "1SAM 14:6", JONATHAN),
        face([cp("14:7", to="said unto him,"), say("14:7", frm="Do all that")], "1SAM 14:7", ARMORBEARER),
        face([cp("14:8", to="Then said Jonathan,"), ("say", v("14:8", frm="Behold,") + " " + v("14:9") + " " + v("14:10"))], "1SAM 14:8–10", JONATHAN),
        drawn([cp("14:11", to="the Philistines said,"), say("14:11", frm="Behold, the Hebrews"), cp("14:12", to="and said,"), say("14:12", frm="Come up to us,", to="show you a thing."),
               cp("14:12", frm="And Jonathan said", to="his armorbearer,"), say("14:12", frm="Come up after me;")], "1SAM 14:11–12", lambda w, h: K.crags("cr6b", w, h, 612, climbing=True), "#8FD0E2",
              head="Come Up unto Us"),
        drawn([caps("14:13-15")], "1SAM 14:13–15", lambda w, h: K.crags("cr6c", w, h, 613, climbing=True), "#8FD0E2"),
        drawn([caps("14:16"), cp("14:17", to="that were with him,"), say("14:17", frm="Number now,", to="gone from us."), cp("14:17", frm="And when they had numbered,")], "1SAM 14:16–17",
              lambda w, h: JA.armed("gb6", w, h, 614, tribes=("BENJAMIN",)), "#F3D8A0", head="So Jehovah Saved Israel"),
        face([cp("14:18", to="unto Ahijah,"), say("14:18", frm="Bring hither", to="ark of God."), cp("14:18", frm="For the ark"), cp("14:19", to="said unto the priest,"), say("14:19", frm="Withdraw")],
             "1SAM 14:18–19", SAUL_KING),
        drawn([caps("14:20-23")], "1SAM 14:20–23", lambda w, h: JG.midian(w, h, 615), "#E8B880"),
        face([cp("14:24", to="saying,"), say("14:24", frm="Cursed be", to="mine enemies."), cp("14:24", frm="So none")], "1SAM 14:24", SAUL_MAD, bg=RED, head="The Honey Dropped"),
        drawn([caps("14:25-27")], "1SAM 14:25–27", lambda w, h: K.honey_rod(w, h, 616), "#2E4A2A"),
        face([cp("14:28", to="and said,"), say("14:28", frm="Thy father", to="this day."), cp("14:28", frm="And the people were faint."), cp("14:29", to="Then said Jonathan,"),
              ("say", v("14:29", frm="My father") + " " + v("14:30"))], "1SAM 14:28–30", JONATHAN),
        drawn([caps("14:31-32"), cp("14:33", to="saying,"), say("14:33", frm="Behold,", to="with the blood."), cp("14:33", frm="And he said,", to="And he said,"), say("14:33", frm="Ye have dealt")], "1SAM 14:31–33",
              lambda w, h: K.eben_ezer("st6", w, h, 617), "#5A6E8A", head="Ye Have Dealt Treacherously"),
        face([cp("14:34", to="And Saul said,"), say("14:34", frm="Disperse", to="with the blood."), cp("14:34", frm="And all the people brought"), caps("14:35")], "1SAM 14:34–35", SAUL_KING),
        face([cp("14:36", to="And Saul said,"), say("14:36", frm="Let us go down", to="a man of them."), cp("14:36", frm="And they said,", to="And they said,"), say("14:36", frm="Do whatsoever", to="unto thee."),
              cp("14:36", frm="Then said the priest,", to="Then said the priest,"), say("14:36", frm="Let us draw near")], "1SAM 14:36", SAUL_KING),
        drawn([cp("14:37", to="asked counsel of God,"), say("14:37", frm="Shall I go down", to="hand of Israel?"), cp("14:37", frm="But he answered")], "1SAM 14:37", lambda w, h: X.cosmic(w, h), "#0B0B2A",
              head="Jonathan Was Taken"),
        face([cp("14:38", to="And Saul said,"), ("say", v("14:38", frm="Draw nigh") + " " + v("14:39", to="he shall surely die.")), cp("14:39", frm="But there was not")], "1SAM 14:38–39", SAUL_MAD, bg=RED),
        face([cp("14:40", to="unto all Israel,"), say("14:40", frm="Be ye", to="other side."), cp("14:40", frm="And the people said", to="unto Saul,"), say("14:40", frm="Do what seemeth", to="unto thee."),
              cp("14:41", to="the God of Israel,"), say("14:41", frm="Show the right.", to="Show the right."), cp("14:41", frm="And Jonathan and Saul"), cp("14:42", to="And Saul said,"), say("14:42", frm="Cast lots", to="my son."),
              cp("14:42", frm="And Jonathan was taken.")], "1SAM 14:40–42", SAUL_KING),
        face([cp("14:43", to="said to Jonathan,"), say("14:43", frm="Tell me", to="thou hast done."), cp("14:43", frm="And Jonathan told him,", to="and said,"), say("14:43", frm="I did certainly")],
             "1SAM 14:43", JONATHAN, bg=COLD),
        face([cp("14:44", to="And Saul said,"), say("14:44", frm="God do so")], "1SAM 14:44", SAUL_MAD, bg=RED),
        face([cp("14:45", to="unto Saul,"), say("14:45", frm="Shall Jonathan", to="this day."), cp("14:45", frm="So the people rescued"), caps("14:46")], "1SAM 14:45–46", ISRAELITE),
        drawn([caps("14:47-48")], "1SAM 14:47–48", K.below(lambda w, h: K.saul_wars(w, h), 0.3), MAP, head="The House of Saul")]
PG.extend(pack(SEGS, "1SA-C06-D", PG.next()))
H = [("The Sons and Daughters of Saul", v("14:49"), "1SAM 14:49", "#FF6A5A", "The House of Saul"), ("Ahinoam · Abner", v("14:50"), "1SAM 14:50", "#FF6A5A", None),
     ("Kish · Ner", v("14:51"), "1SAM 14:51", "#FF6A5A", None), ("Sore War", v("14:52"), "1SAM 14:52", "#FFD23F", None)]
pages = roll_pages(H, "1SA-C06-R", PG.next(), "1 Samuel", "1SAM", tag="THE HOUSE OF SAUL · 1 SAMUEL 14")
name, board, fn = pages[-1]
mark = end_mark("NEXT · JEHOVAH LOOKETH ON THE HEART", "right: 26px; bottom: 34px")
pages[-1] = (name, board, lambda fn=fn: fn().replace("</div>\n</x-dc>", mark + "</div>\n</x-dc>", 1))
PG.extend(pages)
