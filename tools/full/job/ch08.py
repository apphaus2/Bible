"""Job volume, Chapter 8 — The Price of Wisdom (Job 25–28). Every verse, word for word from ref/eng-asv.
Bildad's third and last speech (purple): the moon hath no brightness, man is a worm. Job: Sheol is naked before God; he
hangeth the earth upon nothing (the earth hanging among the stars); a boundary upon the face of the waters unto the
confines of light and darkness; the pillars of heaven tremble. His parable: till I die I will not put away mine integrity;
the portion of a wicked man — silver heaped as dust, a house as the moth, a booth which the keeper maketh, the east wind.
Then where shall wisdom be found? — the mine for silver in section, the miners hanging on their ropes; the path no falcon
knoweth; the jewels named one by one; the weight for the wind and the way for the lightning as a blueprint plate; the fear
of the Lord, that is wisdom."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from job import G, art8 as K
from job.common import (pack, pf, pd, pf2, pd2, BILDAD, BILDAD_STERN, JOB_ASH, JOB_GRIEF, JOB_BOLD, JOB_HOPE, JOB_AWE, COLD, GOLDEN, RED)
from job import ch07 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JOB-C08-00-Title", "Chapter 8 · The Price of Wisdom", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 280)">{K.mine("t8", 760, 800, 801)}</g><rect x="0" y="0" width="760" height="282" fill="#8FD0E2"></rect>')
    return chapter_title(8, "第八話", "The Price of Wisdom", "Job 25 – 28", svg, "#4A7A9A", v("28:18", frm="Yea, the price of wisdom"), "Job · Volume Eighteen")


SEGS = [pd2("bil", "25:1-3", lambda w, h: K.debate("db8", w, h, 802, "bil", night=True), "#1A1A3A", head="Bildad the Third Time", stamp=25),
        pd("bil", "25:4-6", lambda w, h: K.moon_worm(w, h, 803), "#05051A"),
        pd2("job", "26:1-4", lambda w, h: K.debate("db8b", w, h, 804, "bil", speaker="job"), "#7A7A8A", head="He Hangeth the Earth upon Nothing", stamp=26),
        pd("job", "26:5-6", lambda w, h: K.deep_section(w, h, 805), "#5A8AB8"),
        pd("job", "26:7-9", lambda w, h: K.hung_nothing(w, h, 806), "#020210", full=True),
        pd("job", "26:10-11", lambda w, h: K.light_bound(w, h, 807), "#5A5A6A"),
        pd("job", "26:12-14", lambda w, h: K.tempest(w, h, 808, sea_=True), "#0B0B1A"),
        pd2("job", "27:1-4", lambda w, h: K.redeemer("rd8", w, h, 809), "#2A2A6A", head="I Will Not Put Away Mine Integrity", stamp=27),
        pf("job", "27:5-7", JOB_BOLD, bg=RED),
        pf("job", "27:8-10", JOB_ASH, bg=COLD),
        pd("job", "27:11-15", lambda w, h: K.debate("db8c", w, h, 810, "zop", speaker="job"), "#7A7A8A"),
        pd("job", "27:16-17", lambda w, h: K.silver_dust(w, h, 811), "#3A2E2A"),
        pd("job", "27:18-19", lambda w, h: K.booth(w, h, 812), "#8FD0E2"),
        pd("job", "27:20-23", lambda w, h: K.east_wind(w, h, 813), "#E8C890"),
        pd("job", "28:1-4", lambda w, h: K.mine("mn8", w, h, 814), "#8FD0E2", head="Surely There Is a Mine for Silver", stamp=28),
        pd("job", "28:5-6", lambda w, h: K.bread_fire(w, h, 815), "#8FD0E2"),
        pd("job", "28:7-8", lambda w, h: K.falcon_path(w, h, 816), "#8FB8D8"),
        pd("job", "28:9-11", lambda w, h: K.channels(w, h, 817), "#8FB8D8"),
        pd("job", "28:12-14", lambda w, h: K.deep_section(w, h, 818), "#5A8AB8", head="Where Shall Wisdom Be Found?"),
        pd("job", "28:15-19", lambda w, h: K.jewels(w, h, 819), "#2A1A2A"),
        pd("job", "28:20-22", lambda w, h: K.dark_land(w, h, 820), "#020206"),
        pd("job", "28:23-27", lambda w, h: K.measures2(w, h, 821), "#0B1A2E"),
        pf("job", "28:28", JOB_HOPE, head="The Fear of the Lord, That Is Wisdom")]
PG.extend(pack(SEGS, "JOB-C08-D", PG.next(), end=end_mark("NEXT · THE MONTHS OF OLD", "right: 10px; bottom: 34px")))
