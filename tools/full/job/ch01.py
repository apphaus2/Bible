"""Job volume, Chapter 1 — The Land of Uz (Job 1–3). Every verse, word for word from ref/asv.
A man in the land of Uz, perfect and upright: his sons and daughters, his flocks and herds, the burnt-offerings at dawn for
his children. The sons of God before Jehovah, and Satan among them — his words set over the heavens, never a figure; a dark
streak falling from the court at most. Four messengers, each escaped alone (the slain told in words over the empty field,
the burnt pasture, the dust of the three bands and the fallen house). Job rends his robe and worships; the boils as
sackcloth, a potsherd and the ash heap; his wife; the three friends weeping afar off and sitting silent seven days and
seven nights. Then Job's lament, Let the day perish, in song lines over the darkened day, the barren night, the rest of
kings and prisoners, the pit and the hedged way."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from job import G, art as K
from job.common import (pack, cp, say, gd, says, caps, drawn, face, joined, pf, pd, sgs, MESSENGER, JOB, JOB_ASH, JOB_GRIEF, WIFE, COLD, GOLDEN, RED, NIGHT)

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
HEAV = "#0B0B2A"


@P("JOB-C01-00-Title", "Chapter 1 · The Land of Uz", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 280)">{K.uz_estate("t1", 760, 800, 101)}</g><rect x="0" y="0" width="760" height="282" fill="#8FD0E2"></rect>')
    return chapter_title(1, "第一話", "The Land of Uz", "Job 1 – 3", svg, "#5A7A9A", v("1:21", frm="Jehovah gave,"), "Job · Volume Eighteen")


SEGS = [drawn([caps("1:1-3")], "JOB 1:1–3", lambda w, h: K.uz_estate("uz1", w, h, 102), "#8FD0E2", head="A Man in the Land of Uz", stamp=1),
        drawn([caps("1:4")], "JOB 1:4", lambda w, h: K.feast_house("fh1", w, h, 103), "#3A2A4A"),
        drawn([cp("1:5", to="for Job said,"), say("1:5", frm="It may be", to="in their hearts."), cp("1:5", frm="Thus did Job")], "JOB 1:5",
              lambda w, h: K.dawn_offering("do1", w, h, 104), "#3A3A6A"),
        drawn([caps("1:6"), cp("1:7", to="unto Satan,"), gd("1:7", frm="Whence comest", to="thou?"), cp("1:7", frm="Then Satan", to="and said,"),
               say("1:7", frm="From going")], "JOB 1:6–7", lambda w, h: K.heavens(w, h, 105), HEAV, head="Before Jehovah", full=True),
        drawn([cp("1:8", to="unto Satan,"), gd("1:8", frm="Hast thou"), cp("1:9", to="and said,"), say("1:9", frm="Doth Job"), says("1:10-11")], "JOB 1:8–11",
              lambda w, h: K.hedge("hg1", w, h, 106), "#2A2A5A"),
        drawn([cp("1:12", to="unto Satan,"), gd("1:12", frm="Behold,", to="thy hand."), cp("1:12", frm="So Satan")], "JOB 1:12",
              lambda w, h: K.heavens(w, h, 107, shadow=True), HEAV, full=True),
        drawn([caps("1:13"), cp("1:14", to="and said,"), joined("say", ("1:14", "The oxen"), "1:15")], "JOB 1:13–15", lambda w, h: K.runner_scene("rs1", w, h, 108, "plow"), "#8FD0E2",
              head="I Only Am Escaped Alone"),
        drawn([cp("1:16", to="and said,"), say("1:16", frm="The fire of God")], "JOB 1:16", lambda w, h: K.runner_scene("rs2", w, h, 109, "fire"), "#1A0A0A"),
        drawn([cp("1:17", to="and said,"), say("1:17", frm="The Chaldeans")], "JOB 1:17", lambda w, h: K.runner_scene("rs3", w, h, 110, "bands"), "#C8A87A"),
        face([cp("1:18", to="and said,"), joined("say", ("1:18", "Thy sons"), "1:19")], "JOB 1:18–19", MESSENGER, bg=RED),
        drawn([caps("1:20")], "JOB 1:20", lambda w, h: K.job_mourn("jm1", w, h, 111), "#2A2A5A"),
        face([cp("1:21", to="and he said,"), say("1:21", frm="Naked came I"), caps("1:22")], "JOB 1:21–22", JOB_GRIEF, bg=COLD)]
SEGS2 = [drawn([caps("2:1"), cp("2:2", to="unto Satan,"), gd("2:2", frm="From whence", to="comest thou?"), cp("2:2", frm="And Satan", to="and said,"), say("2:2", frm="From going")], "JOB 2:1–2",
               lambda w, h: K.heavens(w, h, 201), HEAV, head="Skin for Skin", stamp=2, full=True),
         drawn([cp("2:3", to="unto Satan,"), gd("2:3", frm="Hast thou"), cp("2:4", to="and said,"), say("2:4", frm="Skin for skin,"), says("2:5")], "JOB 2:3–5",
               lambda w, h: K.heavens(w, h, 202), HEAV, full=True),
         drawn([cp("2:6", to="unto Satan,"), gd("2:6", frm="Behold,"), caps("2:7-8")], "JOB 2:6–8", lambda w, h: K.ash_heap("ah2", w, h, 203), "#6A6A7A", head="Among the Ashes"),
         face([cp("2:9", to="unto him,"), say("2:9", frm="Dost thou")], "JOB 2:9", WIFE, bg=COLD, who="wife"),
         drawn([cp("2:10", to="unto her,"), say("2:10", frm="Thou speakest", to="receive evil?"), cp("2:10", frm="In all this")], "JOB 2:10",
               lambda w, h: K.ash_heap("ah2b", w, h, 204, wife=True), "#6A6A7A"),
         drawn([caps("2:11")], "JOB 2:11", lambda w, h: K.friends_road("fr2", w, h, 205), "#A8B8C8", head="Job's Three Friends"),
         drawn([caps("2:12")], "JOB 2:12", lambda w, h: K.friends_road("fr2b", w, h, 206, mourn=True), "#A8B8C8"),
         drawn([caps("2:13")], "JOB 2:13", lambda w, h: K.ash_heap("ah2c", w, h, 207, friends=3, night=True, shard=False), NIGHT)]
SEGS3 = [drawn([caps("3:1-2")] + sgs("3:3-5"), "JOB 3:1–5", lambda w, h: K.dark_day(w, h, 301), "#1A1A2A", who="job", head="Let the Day Perish", stamp=3),
         pd("job", "3:6-10", lambda w, h: K.barren_night(w, h, 302), "#05050A"),
         pf("job", "3:11-13", JOB_GRIEF, bg=COLD),
         pd("job", "3:14-16", lambda w, h: K.kings_rest(w, h, 303), "#2A2A4A"),
         pd("job", "3:17-19", lambda w, h: K.prison_open(w, h, 304), "#3A3438"),
         pd("job", "3:20-22", lambda w, h: K.dug_pit(w, h, 305), "#3A2A4A"),
         pd("job", "3:23-24", lambda w, h: K.hedged_way(w, h, 306), "#2A2A3A"),
         pf("job", "3:25-26", JOB_ASH, bg=COLD)]
PG.extend(pack(SEGS + SEGS2 + SEGS3, "JOB-C01-D", PG.next(), end=end_mark("NEXT · THE VISION OF THE NIGHT", "right: 10px; bottom: 34px")))
