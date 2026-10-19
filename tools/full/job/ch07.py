"""Job volume, Chapter 7 — Where I Might Find Him (Job 21–24). Every verse, word for word from ref/asv.
Job answers Zophar: wherefore do the wicked live? — their houses safe, their children dancing to the timbrel and harp; as
stubble before the wind, as chaff that the storm carrieth away; one dieth in full strength, another in bitterness, and they
lie down alike in the dust; the wayfaring men; borne to the grave. Eliphaz's third speech (teal): is not thy wickedness
great? — the widow sent away empty (his charge, drawn as a shut door); the height of the stars and the thick clouds; the
gold of Ophir among the stones of the brooks. Job: oh that I knew where I might find him! — forward, backward, the left
hand and the right (a compass of four empty ways); I shall come forth as gold; then the poor of the earth: the landmarks
removed, the rock embraced in the rain, the winepresses trodden in thirst, the houses dug through in the dark."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from job import G, art7 as K
from job.common import (pack, pf, pd, pf2, pd2, ELIPHAZ, ELIPHAZ_STERN, JOB_ASH, JOB_GRIEF, JOB_BOLD, JOB_HOPE, JOB_AWE, COLD, GOLDEN, RED)
from job import ch06 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JOB-C07-00-Title", "Chapter 7 · Where I Might Find Him", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.four_ways(760, 820, 701)}</g><rect x="0" y="0" width="760" height="262" fill="#0B1A2E"></rect>')
    return chapter_title(7, "第七話", "Where I Might Find Him", "Job 21 – 24", svg, "#0B1A2E", v("23:3"), "Job · Volume Eighteen")


SEGS = [pd2("job", "21:1-4", lambda w, h: K.debate("db7", w, h, 702, "zop", speaker="job"), "#7A7A8A", head="Wherefore Do the Wicked Live?", stamp=21),
        pf("job", "21:5-6", JOB_AWE, bg=COLD),
        pd("job", "21:7-10", lambda w, h: K.prosper("pr7", w, h, 703), "#6A8AB8"),
        pd("job", "21:11-13", lambda w, h: K.dancing("dn7", w, h, 704), "#8FD0E2"),
        pf("job", "21:14-16", JOB_BOLD, bg=RED),
        pd("job", "21:17-18", lambda w, h: K.chaff(w, h, 705), "#3A3A4A"),
        pf("job", "21:19-22", JOB_ASH, bg=COLD),
        pd("job", "21:23-26", lambda w, h: K.two_graves(w, h, 706), "#4A3A5A"),
        pd("job", "21:27-30", lambda w, h: K.wayfarers("wf7", w, h, 707), "#8FB8D8"),
        pd("job", "21:31-34", lambda w, h: K.K2.bier("br7", w, h, 708), "#8A7A8A"),
        pd2("eli", "22:1-5", lambda w, h: K.debate("db7b", w, h, 709, "eli"), "#7A7A8A", head="Eliphaz the Third Time", stamp=22),
        pd("eli", "22:6-9", lambda w, h: K.turned_away("ta7", w, h, 710), "#6A6A7A"),
        pd("eli", "22:10-11", lambda w, h: K.flood(w, h, 711), "#4A5A6A"),
        pd("eli", "22:12-14", lambda w, h: K.stars_clouds(w, h, 712), "#05051A"),
        pd("eli", "22:15-20", lambda w, h: K.desolate(w, h, 713), "#3A2A3A"),
        pf("eli", "22:21-23", ELIPHAZ),
        pd("eli", "22:24-27", lambda w, h: K.gold_brook(w, h, 714), "#8FD0E2"),
        pd("eli", "22:28-30", lambda w, h: K.morning("mn7", w, h, 715), "#2A2A5A"),
        pd2("job", "23:1-3", lambda w, h: K.redeemer("rd7", w, h, 716), "#2A2A6A", head="Oh That I Knew Where I Might Find Him", stamp=23),
        pd("job", "23:4-7", lambda w, h: K.cause_scroll(w, h, 717), "#3A2A2A"),
        pd("job", "23:8-9", lambda w, h: K.four_ways(w, h, 718), "#0B1A2E"),
        pd("job", "23:10-12", lambda w, h: K.crucible(w, h, 719), "#2A1210"),
        pf("job", "23:13-15", JOB_AWE, bg=COLD),
        pd("job", "23:16-17", lambda w, h: K.dark_land(w, h, 720), "#020206"),
        pd("job", "24:1-4", lambda w, h: K.landmark("lm7", w, h, 721), "#8A9AB8", head="They Remove the Landmarks", stamp=24),
        pd("job", "24:5-8", lambda w, h: K.huddled("hd7", w, h, 722), "#4A5060"),
        pd("job", "24:9-12", lambda w, h: K.winepress_thirst("wp7", w, h, 723), "#E8B880"),
        pd("job", "24:13-17", lambda w, h: K.dug_wall(w, h, 724), "#05051A"),
        pd("job", "24:18-20", lambda w, h: K.brook(w, h, 725, dry=True), "#8FD0E2"),
        pd("job", "24:21-25", lambda w, h: K.grain_tops(w, h, 726), "#8FD0E2")]
PG.extend(pack(SEGS, "JOB-C07-D", PG.next(), end=end_mark("NEXT · WHERE SHALL WISDOM BE FOUND?", "right: 10px; bottom: 34px")))
