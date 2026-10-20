"""Job volume, Chapter 11 — Out of the Whirlwind (Job 38–39). Every verse, word for word from ref/eng-asv.
Jehovah answers Job out of the whirlwind, his words in the Voice box, a box a verse; God is never drawn. Over the
whirlwind coming down upon the ash heap; the foundations of the earth as a blueprint plate (the line stretched upon it, the
corner-stone, the morning stars); the sea shut up with doors; the dayspring along the rim of the earth; the springs of the
sea and the gates of death; the dwelling of light; the treasuries of the snow and the hail; rain on the wilderness where no
man is; the ice; the Pleiades, Orion and the Bear; the lightnings; the lioness and her young, the raven's young crying; the
wild goats and the hinds, the wild ass, the wild-ox, the ostrich and her eggs, the war-horse, the hawk and the eagle on the
point of the cliff (39:30 in words only, over the eagle)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from job import G, art11 as K
from job.common import (pack, drawn, gpd, gdl, gl, cp, label)
from job import ch10 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JOB-C11-00-Title", "Chapter 11 · Out of the Whirlwind", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 200)">{K.whirl_over("t11", 760, 880, 1101)}</g><rect x="0" y="0" width="760" height="202" fill="#05051A"></rect>')
    return chapter_title(11, "第十一話", "Out of the Whirlwind", "Job 38 – 39", svg, "#05051A", v("38:4", to="the earth?"), "Job · Volume Eighteen")


SEGS = [drawn([cp("38:1")] + gdl("38:2-3"), label("38:1-3"), lambda w, h: K.whirl_over("wo11", w, h, 1102), "#05051A", full=True, head="Jehovah Answered Job", stamp=38),
        gpd("38:4-7", lambda w, h: K.foundations(w, h, 1103), "#0B1A2E", head="Where Wast Thou?"),
        gpd("38:8-11", lambda w, h: K.sea_bound(w, h, 1104), "#1A1A3A"),
        gpd("38:12-15", lambda w, h: K.dayspring(w, h, 1105), "#05051A"),
        gpd("38:16-18", lambda w, h: K.deep_section(w, h, 1106), "#5A8AB8"),
        gpd("38:19-21", lambda w, h: K.light_bound(w, h, 1107), "#5A5A6A"),
        gpd("38:22-24", lambda w, h: K.hail(w, h, 1108), "#2A2A3A"),
        gpd("38:25-27", lambda w, h: K.desert_rain(w, h, 1109), "#5A6A7A"),
        gpd("38:28-30", lambda w, h: K.ice(w, h, 1110), "#5A6A8A"),
        gpd("38:31-33", lambda w, h: K.constellations(w, h, 1111), "#05051A", head="Canst Thou Bind the Pleiades?"),
        gpd("38:34-38", lambda w, h: K.lightning_world(w, h, 1112), "#05051A", full=True),
        gpd("38:39-41", lambda w, h: K.lioness(w, h, 1113), "#E8A06A"),
        gpd("39:1-4", lambda w, h: K.goats_hinds(w, h, 1114), "#8FB8D8", head="The Wild Goats of the Rock", stamp=39),
        gpd("39:5-8", lambda w, h: K.wild_ass_run(w, h, 1115), "#E8C890"),
        gpd("39:9-12", lambda w, h: K.wild_ox(w, h, 1116), "#8FB8D8"),
        gpd("39:13-18", lambda w, h: K.ostrich_eggs(w, h, 1117), "#E8C890", head="The Wings of the Ostrich"),
        gpd("39:19-22", lambda w, h: K.war_horse("wh11", w, h, 1118), "#C8805A", head="Hast Thou Given the Horse His Might?"),
        gpd("39:23-25", lambda w, h: K.war_horse("wh11b", w, h, 1119), "#C8805A"),
        gpd("39:26-30", lambda w, h: K.eagle_cliff(w, h, 1120), "#5A8AB8")]
PG.extend(pack(SEGS, "JOB-C11-D", PG.next(), end=end_mark("NEXT · MINE EYE SEETH THEE", "right: 10px; bottom: 34px")))
