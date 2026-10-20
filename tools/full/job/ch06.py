"""Job volume, Chapter 6 — My Redeemer Liveth (Job 18–20). Every verse, word for word from ref/eng-asv.
Bildad's second speech (purple): the lamp of the wicked put out; the net, the gin, the noose and the trap; brimstone
scattered upon his habitation. Job's answer: he hath walled up my way; the crown taken from my head, my hope plucked up
like a tree; his troops encamp round about my tent; my household counteth me a stranger (they walk away from the ash heap);
have pity upon me, O ye my friends; oh that my words were graven in the rock; I know that my Redeemer liveth (the dawn
over the earth, Job's hands lifted toward it; no one is drawn in the light). Zophar's second speech (blue): the triumphing
of the wicked is short; the poison of asps; the streams of honey and butter; the bow of brass; a fire not blown by man."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from job import G, art6 as K
from job.common import (pack, pf, pd, pf2, pd2, BILDAD, BILDAD_STERN, ZOPHAR, ZOPHAR_STERN, JOB_ASH, JOB_GRIEF, JOB_BOLD, JOB_HOPE, COLD, GOLDEN, RED)
from job import ch05 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JOB-C06-00-Title", "Chapter 6 · My Redeemer Liveth", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 280)">{K.redeemer("t6", 760, 800, 601, jx=0.76)}</g><rect x="0" y="0" width="760" height="282" fill="#2A2A6A"></rect>')
    return chapter_title(6, "第六話", "My Redeemer Liveth", "Job 18 – 20", svg, "#2A2A6A", v("19:25", to="liveth,"), "Job · Volume Eighteen")


SEGS = [pd2("bil", "18:1-4", lambda w, h: K.debate("db6", w, h, 602, "bil"), "#7A7A8A", head="Bildad Answered Again", stamp=18),
        pd("bil", "18:5-7", lambda w, h: K.lamp_out(w, h, 603), "#0F0B0E"),
        pd("bil", "18:8-10", lambda w, h: K.snares(w, h, 604), "#8A9A7A"),
        pd("bil", "18:11-14", lambda w, h: K.fleeing("fl6", w, h, 605), "#1A0A1A"),
        pd("bil", "18:15-17", lambda w, h: K.brimstone(w, h, 606), "#5A4A2A"),
        pf("bil", "18:18-21", BILDAD_STERN, bg=RED),
        pd2("job", "19:1-5", lambda w, h: K.debate("db6b", w, h, 607, "bil", speaker="job"), "#7A7A8A", head="Have Pity upon Me", stamp=19),
        pd("job", "19:6-8", lambda w, h: K.walled_way(w, h, 608), "#1A1A2A"),
        pd("job", "19:9-10", lambda w, h: K.uprooted(w, h, 609), "#6A6A8A"),
        pd("job", "19:11-12", lambda w, h: K.siege_tent(w, h, 610), "#1A1A3A"),
        pd("job", "19:13-19", lambda w, h: K.estranged("es6", w, h, 611), "#5A5A7A"),
        pf("job", "19:20-22", JOB_GRIEF, bg=COLD),
        pd("job", "19:23-24", lambda w, h: K.graven(w, h, 612), "#8A8A9A", head="Oh That My Words Were Written"),
        pd("job", "19:25-27", lambda w, h: K.redeemer("rd6", w, h, 613), "#2A2A6A", head="My Redeemer Liveth"),
        pf("job", "19:28-29", JOB_BOLD, bg=RED),
        pd2("zop", "20:1-5", lambda w, h: K.debate("db6c", w, h, 614, "zop"), "#7A7A8A", head="Zophar Answered Again", stamp=20),
        pd("zop", "20:6-9", lambda w, h: K.pillar_clouds(w, h, 615), "#5A6A8A"),
        pf("zop", "20:10-13", ZOPHAR),
        pd("zop", "20:14-16", lambda w, h: K.viper(w, h, 616), "#E8C890"),
        pd("zop", "20:17-19", lambda w, h: K.honey_streams(w, h, 617), "#8FD0E2"),
        pf("zop", "20:20-22", ZOPHAR_STERN, bg=RED),
        pd("zop", "20:23", lambda w, h: K.storm_feast(w, h, 618), "#0B0B1A"),
        pd("zop", "20:24-25", lambda w, h: K.brass_bow(w, h, 619), "#5A4A4A"),
        pd("zop", "20:26-29", lambda w, h: K.tent_fire(w, h, 620), "#05051A")]
PG.extend(pack(SEGS, "JOB-C06-D", PG.next(), end=end_mark("NEXT · WHERE I MIGHT FIND HIM", "right: 10px; bottom: 34px")))
