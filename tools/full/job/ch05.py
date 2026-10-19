"""Job volume, Chapter 5 — My Witness Is in Heaven (Job 15–17). Every verse, word for word from ref/asv.
Eliphaz's second speech (teal): fill himself with the east wind?; art thou the first man that was born?; the heavens are
not clean in his sight; the wicked man travaileth with pain, runneth upon God with the bosses of his bucklers, dwelleth in
desolate cities; the unripe grape and the olive's flower. Job's answer: miserable comforters are ye all; they gape upon me
(dark figures about the ash heap, no blow drawn); his archers compass me round (a post stuck with arrows); even now, behold,
my witness is in heaven (one great light over the ash heap at night, no one drawn in it); strike hands with me; the bars of
Sheol."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from job import G, art5 as K
from job.common import (pack, pf, pd, pf2, pd2, ELIPHAZ, ELIPHAZ_STERN, JOB_ASH, JOB_GRIEF, JOB_BOLD, JOB_HOPE, COLD, GOLDEN, RED)
from job import ch04 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JOB-C05-00-Title", "Chapter 5 · My Witness Is in Heaven", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 280)">{K.witness("t5", 760, 800, 501, jx=0.76)}</g><rect x="0" y="0" width="760" height="282" fill="#05051A"></rect>')
    return chapter_title(5, "第五話", "My Witness Is in Heaven", "Job 15 – 17", svg, "#05051A", v("16:19"), "Job · Volume Eighteen")


SEGS = [pd2("eli", "15:1-3", lambda w, h: K.east_wind(w, h, 502), "#E8C890", head="Eliphaz Answered Again", stamp=15),
        pf("eli", "15:4-6", ELIPHAZ_STERN, bg=RED),
        pd("eli", "15:7-10", lambda w, h: K.debate("db5", w, h, 503, "eli"), "#7A7A8A"),
        pf("eli", "15:11-13", ELIPHAZ),
        pd("eli", "15:14-16", lambda w, h: K.constellations(w, h, 504, names=False), "#05051A"),
        pd("eli", "15:17-19", lambda w, h: K.old_stones(w, h, 505), "#4A3A6A"),
        pd("eli", "15:20-24", lambda w, h: K.lost_way("lw5", w, h, 506), "#05050F", head="The Wicked Man Travaileth with Pain"),
        pd("eli", "15:25-27", lambda w, h: K.charger("ch5", w, h, 507), "#1A1A2E"),
        pd("eli", "15:28-30", lambda w, h: K.desolate(w, h, 508), "#3A2A3A"),
        pd("eli", "15:31-35", lambda w, h: K.vine_olive(w, h, 509), "#8FD0E2"),
        pd2("job", "16:1-5", lambda w, h: K.debate("db5b", w, h, 510, "eli", speaker="job"), "#7A7A8A", head="Miserable Comforters Are Ye All", stamp=16),
        pf("job", "16:6-8", JOB_GRIEF, bg=COLD),
        pd("job", "16:9-11", lambda w, h: K.mockers("mk5", w, h, 511), "#5A3A3A"),
        pd("job", "16:12-14", lambda w, h: K.target("tg5", w, h, 512), "#8A7A8A"),
        pf("job", "16:15-17", JOB_GRIEF, bg=COLD),
        pd("job", "16:18-19", lambda w, h: K.witness("wt5", w, h, 513), "#05051A", head="My Witness Is in Heaven"),
        pd("job", "16:20-22", lambda w, h: K.road_away(w, h, 514), "#1A1A3A"),
        pd("job", "17:1-2", lambda w, h: K.open_tomb(w, h, 515), "#3A2A4A", stamp=17),
        pd("job", "17:3-5", lambda w, h: K.strike_hands(w, h, 516), "#5A4A3A"),
        pf("job", "17:6-9", JOB_ASH, bg=COLD),
        pd("job", "17:10-12", lambda w, h: K.twilight(w, h, 517), "#0B0B2A"),
        pd("job", "17:13-16", lambda w, h: K.sheol_bars(w, h, 518), "#05050A")]
PG.extend(pack(SEGS, "JOB-C05-D", PG.next(), end=end_mark("NEXT · MY REDEEMER LIVETH", "right: 10px; bottom: 34px")))
