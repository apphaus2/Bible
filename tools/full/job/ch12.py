"""Job volume, Chapter 12 — Mine Eye Seeth Thee (Job 40–42), the last chapter of Job. Every verse, word for word from
ref/eng-asv. Jehovah again out of the whirlwind (the Voice box; God never drawn): shall he that cavilleth contend with the
Almighty? — Job: I lay my hand upon my mouth. Hast thou an arm like God? Behemoth, the river-horse grazing and lying under
the lotus-trees; leviathan, the great crocodile — no fishhook will draw him out; his scales shut up as with a close seal;
his breath lit gold at sunrise; the weapons that cannot avail; the path that shineth after him. Job: I had heard of thee by
the hearing of the ear, but now mine eye seeth thee; I repent in dust and ashes. Jehovah's word to Eliphaz; the seven
bullocks and seven rams, Job praying for his friends; his kin eating bread with him; the latter end as a tally board; the
three daughters named; four generations; and Job died, old and full of days (words over the tent at sunset)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from job import G, art12 as K
from job.jdiscourse import seg
from job.common import (pack, drawn, face, gpd, gdl, gd, cp, caps, sgs, pd, label, JOB_AWE, JOB_HOPE, JOB_OLD, COLD, GOLDEN)
from job import ch11 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JOB-C12-00-Title", "Chapter 12 · Mine Eye Seeth Thee", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 280)">{K.repent("t12", 760, 800, 1201)}</g><rect x="0" y="0" width="760" height="282" fill="#5A6A9A"></rect>')
    return chapter_title(12, "第十二話", "Mine Eye Seeth Thee", "Job 40 – 42", svg, "#5A6A9A", v("42:5"), "Job · Volume Eighteen")


SEGS = [drawn([cp("40:1")] + gdl("40:2"), label("40:1-2"), lambda w, h: K.whirl_over("wo12", w, h, 1202), "#05051A", full=True, head="Shall He That Cavilleth Contend?", stamp=40),
        face([cp("40:3")] + sgs("40:4-5", "job"), label("40:3-5"), JOB_AWE, bg=COLD, who="job"),
        drawn([cp("40:6")] + gdl("40:7-9"), label("40:6-9"), lambda w, h: K.whirl_over("wo12b", w, h, 1203), "#05051A", full=True),
        gpd("40:10-14", lambda w, h: K.pillar_clouds(w, h, 1204), "#5A6A8A"),
        gpd("40:15-19", lambda w, h: K.hippo_grazing(w, h, 1205), "#8FD0E2", head="Behold Now, Behemoth"),
        gpd("40:20-24", lambda w, h: K.lotus_river(w, h, 1206), "#8FD0E2"),
        gpd("41:1-7", lambda w, h: K.hook_cord(w, h, 1207), "#8FB8C8", head="Canst Thou Draw Out Leviathan?", stamp=41),
        gpd("41:8-11", lambda w, h: K.croc_bank(w, h, 1208), "#C8B890"),
        gpd("41:12-17", lambda w, h: K.scales(w, h, 1209), "#2A3A2A"),
        gpd("41:18-21", lambda w, h: K.croc_dawn(w, h, 1210), "#3A3A6A"),
        gpd("41:22-25", lambda w, h: K.croc_bank(w, h, 1211, open_=False), "#C8B890"),
        gpd("41:26-29", lambda w, h: K.broken_weapons(w, h, 1212), "#8A8A9A"),
        gpd("41:30-34", lambda w, h: K.shining_wake(w, h, 1213), "#5A8AB8"),
        face([cp("42:1")] + sgs("42:2-4", "job"), label("42:1-4"), JOB_AWE, bg=COLD, who="job", head="Mine Eye Seeth Thee", stamp=42),
        pd("job", "42:5-6", lambda w, h: K.repent("rp12", w, h, 1214), "#5A6A9A"),
        drawn([cp("42:7", to="the Temanite,"), gd("42:7", frm="My wrath")], label("42:7"), lambda w, h: K.ash_heap("ah12", w, h, 1215, friends=3), "#6A6A7A", head="My Servant Job Shall Pray for You"),
        drawn([gd("42:8"), caps("42:9")], label("42:8-9"), lambda w, h: K.friends_offering("fo12", w, h, 1216), "#8FB8D8"),
        drawn([caps("42:10-11")], label("42:10-11"), lambda w, h: K.kin_feast("kf12", w, h, 1217), "#3A2A4A", head="The Latter End of Job"),
        drawn([caps("42:12")], label("42:12"), lambda w, h: K.uz_estate("uz12", w, h, 1218), "#8FD0E2"),
        seg([], "JOB 42:12", art=lambda w, h: K.tally_board(w, h), bg="#1A1430", h=240),
        drawn([caps("42:13-15")], label("42:13-15"), lambda w, h: K.daughters("dg12", w, h, 1219), "#8FB8D8"),
        drawn([caps("42:16")], label("42:16"), lambda w, h: K.generations("gn12", w, h, 1220), "#E8A06A"),
        drawn([caps("42:17")], label("42:17"), lambda w, h: K.full_of_days(w, h, 1221), "#3A2A4A")]
PG.extend(pack(SEGS, "JOB-C12-D", PG.next(), end=end_mark("END OF JOB · NEXT · PSALMS", "right: 10px; bottom: 34px", ch="完")))
