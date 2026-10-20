"""Nehemiah volume, Chapter 1 — The Wall of Jerusalem (Nehemiah 1–2). Every verse, word for word from ref/eng-asv.
In Shushan the palace, Hanani and certain men out of Judah: the wall of Jerusalem is broken down, and the gates thereof are
burned with fire; Nehemiah weeps, fasts and prays (his prayer in full, God's word to Moses quoted in the Voice box); the
cupbearer before Artaxerxes — why is thy countenance sad?; the king's letters, the captains and horsemen; Sanballat and
Tobiah grieved; the night ride round the broken walls (a plan of the way he went); let us rise up and build; and the
three adversaries laughing them to scorn — the God of heaven, he will prosper us."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from neh import G, art as K
from neh.common import (pack, cp, say, gd, says, caps, drawn, face, joined, NEHEMIAH, NEHEMIAH_GRIEF, NEHEMIAH_PRAY, NEHEMIAH_AFRAID, NEHEMIAH_STERN,
                        ARTAXERXES, HANANI, SANBALLAT, TOBIAH, COLD, GOLDEN, RED)

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, NIGHT = "#0B1A2E", "#0B0B2A"
PAL = "#1F4F8D"


@P("NEH-C01-00-Title", "Chapter 1 · The Wall of Jerusalem", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 330)">{K.night_ride("t1", 760, 560, 101)}</g><rect x="0" y="0" width="760" height="332" fill="#0B0B2A"></rect>')
    return chapter_title(1, "第一話", "The Wall of Jerusalem", "Nehemiah 1 – 2", svg, NIGHT, v("2:17", frm="come, and let us build"), "Nehemiah · Volume Sixteen")


SEGS = [drawn([caps("1:1-2")], "NEH 1:1–2", below(lambda w, h: K.shushan("sh1", w, h, 102), 0.3), PAL, head="The Words of Nehemiah", stamp=1),
        drawn([cp("1:3", to="said unto me,"), say("1:3", frm="The remnant")], "NEH 1:3", below(lambda w, h: K.ruins(w, h, 103), 0.3), "#8A7A8A"),
        face([caps("1:4"), cp("1:5", to="and said,"), say("1:5", frm="I beseech thee")], "NEH 1:4–5", NEHEMIAH_GRIEF, bg=COLD, head="I Sat Down and Wept"),
        face([says("1:6-7")], "NEH 1:6–7", NEHEMIAH_PRAY, bg=COLD),
        face([say("1:8", to="saying,"), joined("god", ("1:8", "If ye trespass"), "1:9")], "NEH 1:8–9", NEHEMIAH_PRAY, bg=COLD),
        face([joined("say", "1:10", ("1:11", None, "in the sight of this man.")), cp("1:11", frm="Now I was cupbearer")], "NEH 1:10–11", NEHEMIAH_PRAY, bg=COLD)]
PG.extend(pack(SEGS, "NEH-C01-D", PG.next()))
SEGS2 = [drawn([caps("2:1")], "NEH 2:1", below(lambda w, h: K.cupbearer("cb1", w, h, 104), 0.24), PAL, head="Why Is Thy Countenance Sad?", stamp=2),
         face([cp("2:2", to="said unto me,"), say("2:2", frm="Why is thy", to="sorrow of heart."), cp("2:2", frm="Then I was")], "NEH 2:2", ARTAXERXES),
         face([cp("2:3", to="unto the king,"), say("2:3", frm="Let the king")], "NEH 2:3", NEHEMIAH_AFRAID),
         face([cp("2:4", to="said unto me,"), say("2:4", frm="For what", to="request?"), cp("2:4", frm="So I prayed")], "NEH 2:4", ARTAXERXES),
         face([cp("2:5", to="unto the king,"), say("2:5", frm="If it please")], "NEH 2:5", NEHEMIAH),
         drawn([cp("2:6", to="sitting by him),"), say("2:6", frm="For how long", to="return?"), cp("2:6", frm="So it pleased")], "NEH 2:6",
               below(lambda w, h: K.cupbearer("cb1b", w, h, 105, queen=True), 0.38), PAL),
         face([cp("2:7", to="unto the king,"), joined("say", ("2:7", "If it please"), ("2:8", None, "I shall enter into.")), cp("2:8", frm="And the king granted")], "NEH 2:7–8", NEHEMIAH),
         drawn([caps("2:9")], "NEH 2:9", below(lambda w, h: K.escort("es1", w, h, 106), 0.2), "#FFC890", head="Beyond the River"),
         face([caps("2:10")], "NEH 2:10", SANBALLAT, bg=RED)]
PG.extend(pack(SEGS2, "NEH-C01-E", PG.next()))
SEGS3 = [drawn([caps("2:11-12")], "NEH 2:11–12", below(lambda w, h: K.night_ride("nr1", w, h, 107), 0.3), NIGHT, head="I Arose in the Night"),
         drawn([caps("2:13-15")], "NEH 2:13–15", below(lambda w, h: K.wall_plan(w, h, lit=("VALLEY GATE", "DUNG GATE", "FOUNTAIN GATE"), night=True), 0.36), MAP),
         drawn([caps("2:16"), cp("2:17", to="unto them,"), say("2:17", frm="Ye see")], "NEH 2:16–17", below(lambda w, h: K.gathering("ga1", w, h, 108), 0.4), "#8A7A8A",
               head="Let Us Rise Up and Build"),
         drawn([cp("2:18", to="And they said,"), say("2:18", frm="Let us rise up", to="and build."), cp("2:18", frm="So they strengthened")], "NEH 2:18",
               below(lambda w, h: K.gathering("ga1b", w, h, 109), 0.3), "#8A7A8A"),
         drawn([cp("2:19", to="and said,"), say("2:19", frm="What is this")], "NEH 2:19", below(lambda w, h: K.scorners("sc1", w, h, 110), 0.3), "#5A3A4A", head="They Laughed Us to Scorn"),
         face([cp("2:20", to="and said unto them,"), say("2:20", frm="The God of heaven")], "NEH 2:20", NEHEMIAH_STERN, bg=RED)]
PG.extend(pack(SEGS3, "NEH-C01-F", PG.next(), end=end_mark("NEXT · THE BUILDERS", "right: 10px; bottom: 34px")))
