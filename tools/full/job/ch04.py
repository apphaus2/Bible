"""Job volume, Chapter 4 — If a Man Die (Job 11–14). Every verse, word for word from ref/eng-asv.
Zophar the Naamathite's first speech (blue): canst thou by searching find out God? — high as heaven, deeper than Sheol (a
technical section of the world with its measures running off the edges); man born as a wild ass's colt; though there be
darkness, it shall be as the morning. Job's answer: no doubt but ye are the people; the tents of robbers prosper; ask now
the beasts, the birds and the fishes; he leadeth counsellors away stripped; proverbs of ashes and defences of clay; behold,
he will slay me; the driven leaf and the dry stubble; the stocks and the moth-eaten garment; man that is born of a woman
cometh forth like a flower; there is hope of a tree; if a man die, shall he live again?; the waters wear the stones."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from job import G, art4 as K
from job.common import (pack, pf, pd, pf2, pd2, ZOPHAR, ZOPHAR_STERN, JOB, JOB_ASH, JOB_GRIEF, JOB_BOLD, JOB_HOPE, COLD, GOLDEN, RED)
from job import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JOB-C04-00-Title", "Chapter 4 · If a Man Die", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.stump(760, 780, 401)}</g><rect x="0" y="0" width="760" height="302" fill="#8FD0E2"></rect>')
    return chapter_title(4, "第四話", "If a Man Die", "Job 11 – 14", svg, "#4A7A9A", v("14:14", to="live again?"), "Job · Volume Eighteen")


SEGS = [pd2("zop", "11:1-4", lambda w, h: K.debate("db4", w, h, 402, "zop"), "#7A7A8A", head="Zophar the Naamathite", stamp=11),
        pf("zop", "11:5-6", ZOPHAR_STERN, bg=RED),
        pd("zop", "11:7-9", lambda w, h: K.measures(w, h, 403), "#1E2A5A", head="Canst Thou by Searching Find Out God?"),
        pd("zop", "11:10-12", lambda w, h: K.wild_ass_run(w, h, 404), "#E8C890"),
        pf("zop", "11:13-15", ZOPHAR),
        pd("zop", "11:16-20", lambda w, h: K.morning("mn4", w, h, 405), "#2A2A5A"),
        pd2("job", "12:1-3", lambda w, h: K.debate("db4b", w, h, 406, "zop", speaker="job"), "#7A7A8A", head="Ask Now the Beasts", stamp=12),
        pf("job", "12:4-5", JOB_BOLD, bg=RED),
        pd("job", "12:6", lambda w, h: K.robber_tents("rt4", w, h, 407), "#2A1A3A"),
        pd("job", "12:7-10", lambda w, h: K.creatures(w, h, 408), "#8FD0E2"),
        pf("job", "12:11-13", JOB_HOPE),
        pd("job", "12:14-16", lambda w, h: K.flood(w, h, 409), "#4A5A6A"),
        pd("job", "12:17-21", lambda w, h: K.K3.captives("cp4", w, h, 410), "#5A4A5A"),
        pd("job", "12:22-25", lambda w, h: K.lost_way("lw4", w, h, 411), "#05050F"),
        pf("job", "13:1-3", JOB_BOLD, bg=RED, stamp=13),
        pd("job", "13:4-6", lambda w, h: K.debate("db4c", w, h, 412, "eli", speaker="job"), "#7A7A8A"),
        pd("job", "13:7-12", lambda w, h: K.crumbling(w, h, 413), "#6A6A7A"),
        pf("job", "13:13-16", JOB_BOLD, bg=RED, head="Behold, He Will Slay Me"),
        pd("job", "13:17-22", lambda w, h: K.cause_scroll(w, h, 414), "#3A2A2A"),
        pd("job", "13:23-25", lambda w, h: K.driven_leaf(w, h, 415), "#8A8A9A"),
        pd("job", "13:26-28", lambda w, h: K.stocks(w, h, 416), "#5A5048"),
        pd("job", "14:1-4", lambda w, h: K.flower_cut(w, h, 417), "#6A5A8A", head="Man That Is Born of a Woman", stamp=14),
        pd("job", "14:5-6", lambda w, h: K.hireling("hl4", w, h, 418), "#E89A5A"),
        pd("job", "14:7-9", lambda w, h: K.stump(w, h, 419), "#8FD0E2"),
        pd("job", "14:10-12", lambda w, h: K.brook(w, h, 420, dry=True), "#8FD0E2"),
        pf("job", "14:13-15", JOB_HOPE, head="If a Man Die"),
        pd("job", "14:16-17", lambda w, h: K.sealed_bag(w, h, 421), "#3A3038"),
        pd("job", "14:18-19", lambda w, h: K.worn_stones(w, h, 422), "#6A7A8A"),
        pf("job", "14:20-22", JOB_GRIEF, bg=COLD)]
PG.extend(pack(SEGS, "JOB-C04-D", PG.next(), end=end_mark("NEXT · MY WITNESS IS IN HEAVEN", "right: 10px; bottom: 34px")))
