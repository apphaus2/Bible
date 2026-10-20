"""Judges volume, Chapter 8 — Micah and the Danites (Judges 17–18). Every verse, word for word from ref/eng-asv.
Micah's eleven hundred pieces of silver and the graven image; the house of gods, the ephod and teraphim; the young Levite of
Beth-lehem-judah hired for ten pieces of silver; the five Danite spies and quiet Laish; the six hundred at the gate, the
image and the priest carried off, What aileth thee?; Laish burnt and called Dan (18:27 words over the smoke); and Micah's
graven image set up all the time the house of God was in Shiloh."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos import art as JA
from jdg import G, art as K
from jdg.common import pack, say, gd, cp, says, gods, caps, face, drawn, F, RED, COLD, GOLDEN
from jdg import ch07 as _prev

v, sp = G.v, G.span
MICAH = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#7A5A2A", cord=True, light="#FFC14D")
MICAH_GRIEF = F("adam", skin="#B98A7E", shadow="#3A3A5A", hair="#3A2214", hl="#6A5A4E", beard=True, beard_color="#3A2214", scarf="#7A5A2A", cord=True, brow="sorrow", sweat=True, light="#9AA8C8")
MOTHER = F("eve", skin="#C98E66", shadow="#6A4A3A", hair="#B8B2A6", scarf="#6A3A5A", light="#FFE680")
LEVITE = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#2A1A10", hl="#5A4A3E", stubble="#2A1A10", scarf="#F3EFE6", light="#FFE680")
DANITE = F("adam", skin="#B9785A", shadow="#5A2A1E", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#1F5FAD", cord=True, brow="scowl", light="#FF8A3D")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JDG-C08-00-Title", "Chapter 8 · Micah and the Danites", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#3A2A1E"></rect><g transform="translate(0 360)">{K.house_of_gods(760, 720, 801)}</g>')
    return chapter_title(8, "第八話", "Micah and the Danites", "Judges 17 – 18", svg, "#3A2A1E", v("17:6", frm="every man did"), "Judges · Volume Seven")


SEGS = [face([cp("17:1"), cp("17:2", to="unto his mother,"), say("17:2", frm="The eleven hundred", to="I took it."), cp("17:2", frm="And his mother said,", to="his mother said,"),
              say("17:2", frm="Blessed be")], "JDG 17:1–2", MICAH, head="The House of Micah", stamp=17),
        face([cp("17:3", to="and his mother said,"), say("17:3", frm="I verily")], "JDG 17:3", MOTHER),
        drawn([caps("17:4-6")], "JDG 17:4–6", lambda w, h: K.house_of_gods(w, h, 811), "#3A2A1E"),
        face([caps("17:7-8"), cp("17:9", to="said unto him,"), say("17:9", frm="Whence comest", to="Whence comest thou?"), cp("17:9", frm="And he said unto him,", to="said unto him,"),
              say("17:9", frm="I am a Levite")], "JDG 17:7–9", LEVITE, head="A Father and a Priest"),
        face([cp("17:10", to="said unto him,"), say("17:10", frm="Dwell with me,", to="thy victuals."), cp("17:10", frm="So the Levite"), caps("17:11-12"), cp("17:13", to="Then said Micah,"),
              say("17:13", frm="Now know I")], "JDG 17:10–13", MICAH),
        drawn([caps("18:1"), cp("18:2", to="and they said unto them,"), say("18:2", frm="Go, search", to="the land."), cp("18:2", frm="And they came")], "JDG 18:1–2",
              lambda w, h: K.ass_colts("dn8", w, h, 812, n=5), "#F3D8A0", head="The Danites", stamp=18),
        face([cp("18:3", to="and said unto him,"), say("18:3", frm="Who brought"), cp("18:4", to="said unto them,"), say("18:4", frm="Thus and thus")], "JDG 18:3–4", LEVITE),
        face([cp("18:5", to="said unto him,"), say("18:5", frm="Ask counsel"), cp("18:6", to="said unto them,"), say("18:6", frm="Go in peace:")], "JDG 18:5–6", DANITE),
        drawn([caps("18:7")], "JDG 18:7", lambda w, h: K.laish(w, h, 813), "#8FD0E2", head="A People Quiet and Secure"),
        face([cp("18:8", to="said unto them,"), say("18:8", frm="What say ye?"), cp("18:9", to="And they said,"), ("say", v("18:9", frm="Arise,") + " " + v("18:10"))], "JDG 18:8–10", DANITE, bg=RED),
        drawn([caps("18:11-13")], "JDG 18:11–13", lambda w, h: JA.armed("ar8", w, h, 814, tribes=("DAN",)), "#F3D8A0"),
        face([cp("18:14", to="unto their brethren,"), say("18:14", frm="Do ye know")], "JDG 18:14", DANITE, bg=RED),
        drawn([caps("18:15-17")], "JDG 18:15–17", lambda w, h: K.house_of_gods(w, h, 815), "#3A2A1E", head="What Do Ye?"),
        face([cp("18:18", to="the priest said unto them,"), say("18:18", frm="What do ye?"), cp("18:19", to="said unto him,"), say("18:19", frm="Hold thy peace,")], "JDG 18:18–19", LEVITE, bg=COLD),
        drawn([caps("18:20-22")], "JDG 18:20–22", lambda w, h: K.danites_march("dm8", w, h, 816), "#E8C88A"),
        face([cp("18:23", to="said unto Micah,"), say("18:23", frm="What aileth")], "JDG 18:23", DANITE, bg=RED),
        face([cp("18:24", to="And he said,"), say("18:24", frm="ye have taken")], "JDG 18:24", MICAH_GRIEF, bg=COLD),
        face([cp("18:25", to="said unto him,"), say("18:25", frm="Let not"), caps("18:26")], "JDG 18:25–26", DANITE, bg=RED),
        drawn([caps("18:27-29")], "JDG 18:27–29", lambda w, h: K.laish(w, h, 817, burning_=True), "#2A0A0A", head="Dan"),
        drawn([caps("18:30-31")], "JDG 18:30–31", lambda w, h: K.house_of_gods(w, h, 818), "#3A2A1E")]
PG.extend(pack(SEGS, "JDG-C08-D", PG.next(), end=end_mark("NEXT · GIBEAH", "right: 10px; bottom: 34px")))
