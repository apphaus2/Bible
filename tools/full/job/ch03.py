"""Job volume, Chapter 3 — No Umpire Betwixt Us (Job 8–10). Every verse, word for word from ref/eng-asv.
Bildad the Shuhite's first speech (purple): doth God pervert justice?; inquire of the former age, our days upon earth are
a shadow (the standing stones of the fathers); the rush without mire, the spider's web, the green shoots about the
stone-heap. Job's answer: how can man be just with God? — him that removeth the mountains, that maketh the Bear, Orion and
the Pleiades (the night sky with the three asterisms named); he goeth by me and I see him not; days swifter than a post,
the swift ships, the eagle; snow water and the ditch; no umpire betwixt us (the empty seat between two seats in the gate);
fashioned as clay, poured out as milk and curdled like cheese; the land of darkness."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from job import G, art3 as K
from job.common import (pack, pf, pd, pf2, pd2, drawn, BILDAD, BILDAD_STERN, JOB_ASH, JOB_GRIEF, JOB_BOLD, JOB_HOPE, COLD, GOLDEN, RED)
from job import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JOB-C03-00-Title", "Chapter 3 · No Umpire Betwixt Us", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.umpire(760, 780, 301)}</g><rect x="0" y="0" width="760" height="302" fill="#5A5A7A"></rect>')
    return chapter_title(3, "第三話", "No Umpire Betwixt Us", "Job 8 – 10", svg, "#5A5A7A", v("9:33"), "Job · Volume Eighteen")


SEGS = [pd2("bil", "8:1-3", lambda w, h: K.debate("db3", w, h, 302, "bil"), "#7A7A8A", head="Bildad the Shuhite", stamp=8),
        pf("bil", "8:4-5", BILDAD),
        pd("bil", "8:6-10", lambda w, h: K.old_stones(w, h, 303), "#4A3A6A"),
        pd("bil", "8:11-13", lambda w, h: K.papyrus(w, h, 304), "#8FD0E2"),
        pd("bil", "8:14-15", lambda w, h: K.spider_web(w, h, 305), "#5A4A6A"),
        pd("bil", "8:16-19", lambda w, h: K.shoots(w, h, 306), "#8FD0E2"),
        pf("bil", "8:20-22", BILDAD_STERN, bg=RED),
        pd2("job", "9:1-4", lambda w, h: K.debate("db3b", w, h, 307, "bil", speaker="job"), "#7A7A8A", head="How Can Man Be Just with God?", stamp=9),
        pd("job", "9:5-7", lambda w, h: K.quake(w, h, 308), "#3A2A3A"),
        pd("job", "9:8-10", lambda w, h: K.constellations(w, h, 309), "#05051A"),
        pd("job", "9:11-13", lambda w, h: K.unseen(w, h, 310), "#C8B890"),
        pf("job", "9:14-16", JOB_GRIEF, bg=COLD),
        pd("job", "9:17-20", lambda w, h: K.tempest(w, h, 311), "#0B0B2A"),
        pf("job", "9:21-22", JOB_BOLD, bg=RED),
        pd("job", "9:23-26", lambda w, h: K.swift(w, h, 312), "#5A8AB8"),
        pd("job", "9:27-31", lambda w, h: K.snow_wash(w, h, 313), "#8A9AB8"),
        pd("job", "9:32-35", lambda w, h: K.umpire(w, h, 314), "#5A5A7A", head="No Umpire Betwixt Us"),
        pf("job", "10:1-2", JOB_ASH, bg=COLD, stamp=10),
        pd("job", "10:3-7", lambda w, h: K.K3.dial(w, h), "#FFE6A0"),
        pd("job", "10:8-11", lambda w, h: K.potter(w, h, 315), "#5A3A2A", head="Thou Hast Fashioned Me as Clay"),
        pf("job", "10:12-14", JOB_HOPE),
        pd("job", "10:15-17", lambda w, h: K.lions(w, h, 316), "#E8B880"),
        pd("job", "10:18-19", lambda w, h: K.kings_rest(w, h, 317), "#2A2A4A"),
        pd("job", "10:20-22", lambda w, h: K.dark_land(w, h, 318), "#020206")]
PG.extend(pack(SEGS, "JOB-C03-D", PG.next(), end=end_mark("NEXT · IF A MAN DIE", "right: 10px; bottom: 34px")))
