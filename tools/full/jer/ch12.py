"""Jeremiah volume, Chapter 12 — The Roll (Jeremiah 34–36). Every verse, word for word from ref/asv.
Zedekiah told: thou shalt die in peace; Lachish and Azekah, the last fortified cities (a map); the covenant of liberty, the
servants set free and brought back; I proclaim unto you a liberty, to the sword; the calf cut in twain (the covenant pieces
covered on their stones); the Rechabites before the bowls of wine — we will drink no wine; then the roll: Baruch writes from the
prophet's mouth, reads it in the chamber of Gemariah on the fast-day, before the princes — go, hide thee, thou and Jeremiah;
the king in the winter-house cuts it with the penknife and casts it into the brazier; another roll written, and many like words
added besides; Jehoiakim's body cast out to the heat and the frost (words over the empty slope)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art12 as K
from jer.common import (pack, cp, say, gd, says, gods, caps, cut, S, O, jer, ZEDEKIAH, BARUCH, RECHABITE, PRINCE, PRINCE_CALM, JEHOIAKIM, GOLDEN, COLD, RED, NIGHT)
from jer import ch11 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W2, G2, S2, C2 = (jer(2, "word"), GOLDEN), (jer(2, "grief"), COLD), (jer(2, "stern"), RED), (jer(2, "calm"), GOLDEN)
MAP = "#0B1A2E"
CEDAR = "#5A3A2A"
ROOM = "#4A3424"


@P("JER-C12-00-Title", "Chapter 12 · The Roll", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.winter_house("t12", 760, 820, 1201)}</g><rect x="0" y="0" width="760" height="262" fill="#5A3A2A"></rect>')
    return chapter_title(12, "第十二話", "The Roll", "Jeremiah 34 – 36", svg, CEDAR, v("36:2", frm="Take thee a roll of a book,", to="all the words"), "Jeremiah · Volume Twenty-Four")


SEGS = [S([cp("34:1"), gd("34:2")], "34:1-2", a=("#5A4A5A", lambda w, h: K.siege_forts("sf12", w, h, 1202)), k=0.42, head="Thou Shalt Die in Peace", stamp=34),
        O("34:3-5", t=W2),
        O("34:6-7", kind="cap", a=(MAP, lambda w, h: K.lachish_map(w, h)), k=0.3),
        O("34:8-10", kind="cap", a=("#8FB0C8", lambda w, h: K.set_free("sf12b", w, h, 1203)), head="To Proclaim Liberty"),
        O("34:11", kind="cap", a=("#6A5A6A", lambda w, h: K.set_free("sf12c", w, h, 1204, back=True)), k=0.3),
        S([cp("34:12"), gd("34:13")], "34:12-13", t=W2),
        O("34:14-15", t=S2),
        O("34:16-17", t=S2, head="I Proclaim unto You a Liberty"),
        O("34:18-19", a=("#C8A880", lambda w, h: K.calf_parts("cp12", w, h, 1205))),
        O("34:20-22", t=S2)]
PG.extend(pack(SEGS, "JER-C12-D", PG.next()))

SEGS2 = [S([cp("35:1"), gd("35:2")], "35:1-2", t=W2, head="The House of the Rechabites", stamp=35),
         O("35:3-4", kind="cap", a=(CEDAR, lambda w, h: K.rechabites("rb12", w, h, 1206, refuse=False)), k=0.34),
         S([cp("35:5", to="and I said unto them,"), say("35:5", frm="Drink ye wine."), cp("35:6", to="But they said,"), say("35:6", frm="We will drink no wine;")], "35:5-6",
           a=(CEDAR, lambda w, h: K.rechabites("rb12b", w, h, 1207)), k=0.36, head="We Will Drink No Wine"),
         O("35:7-9", kind="say", a=("#E8A060", lambda w, h: K.tents_rechab(w, h, 1208))),
         O("35:10-11", kind="say", t=(RECHABITE, GOLDEN)),
         S([cp("35:12"), gd("35:13")], "35:12-13", t=W2),
         O("35:14-15", t=S2),
         O("35:16-17", t=S2),
         S([cp("35:18", to="And Jeremiah said unto the house of the Rechabites,"), gd("35:18", frm="Thus saith"), gd("35:19")], "35:18-19", a=(CEDAR, lambda w, h: K.rechabites("rb12c", w, h, 1209, refuse=False)))]
PG.extend(pack(SEGS2, "JER-C12-E", PG.next()))

SEGS3 = [S([cp("36:1"), gods("36:2-3")], "36:1-3", a=("#3A2A1E", lambda w, h: K.book_writing(w, h, 1210)), k=0.42, head="Take Thee a Roll of a Book", stamp=36),
         O("36:4", kind="cap", a=(ROOM, lambda w, h: K.baruch_writes("bw12", w, h, 1211)), k=0.22),
         S([cp("36:5", to="saying,"), say("36:5", frm="I am shut up;"), says("36:6-7")], "36:5-7", t=C2),
         O("36:8-10", kind="cap", a=("#8FB0C8", lambda w, h: K.reading_people("rp12", w, h, 1212)), head="Baruch Read in the Book"),
         O("36:11-13", kind="cap", a=(CEDAR, lambda w, h: K.princes_chamber("pc12", w, h, 1213)), head="All the Princes Were Sitting There"),
         S([cp("36:14", to="saying,"), say("36:14", frm="Take in thy hand", to="and come."), cp("36:14", frm="So Baruch"), cp("36:15", to="And they said unto him,"),
            say("36:15", frm="Sit down now,", to="in our ears."), cp("36:15", frm="So Baruch read it")], "36:14-15", t=(PRINCE_CALM, GOLDEN)),
         S([cp("36:16", to="and said unto Baruch,"), say("36:16", frm="We will surely tell"), cp("36:17", to="saying,"), say("36:17", frm="Tell us now,")], "36:16-17", t=(PRINCE_CALM, GOLDEN)),
         S([cp("36:18", to="Then Baruch answered them,"), say("36:18", frm="He pronounced")], "36:18", t=(BARUCH, GOLDEN)),
         S([cp("36:19", to="Then said the princes unto Baruch,"), say("36:19", frm="Go, hide thee,"), cp("36:20")], "36:19-20", t=(PRINCE_CALM, COLD), head="Go, Hide Thee"),
         O("36:21-22", kind="cap", a=(CEDAR, lambda w, h: K.winter_house("wh12", w, h, 1214, burning=False)), head="The King Was Sitting in the Winter-House"),
         O("36:23", kind="cap", a=(CEDAR, lambda w, h: K.winter_house("wh12b", w, h, 1215)), k=0.24),
         O("36:24-25", kind="cap", t=(JEHOIAKIM, RED)),
         O("36:26", kind="cap", a=("#0F0E2A", lambda w, h: K.hidden(w, h, 1216)), k=0.24),
         S([cp("36:27"), gd("36:28")], "36:27-28", a=("#3A2A1E", lambda w, h: K.book_writing(w, h, 1217)), head="Take Thee Again Another Roll"),
         O("36:29", t=S2),
         O("36:30-31", a=("#14183A", lambda w, h: K.cast_out(w, h, 1218))),
         O("36:32", kind="cap", a=(ROOM, lambda w, h: K.baruch_writes("bw12b", w, h, 1219)), k=0.3)]
PG.extend(pack(SEGS3, "JER-C12-F", PG.next(), end=end_mark("NEXT · THE DUNGEON", "right: 10px; bottom: 34px")))
