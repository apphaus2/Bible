"""Job volume, Chapter 9 — The Months of Old (Job 29–31). Every verse, word for word from ref/asv.
Job's parable: oh that I were as in the months of old — his lamp over the tent door and his children about him; his seat
in the gate, the aged rising and the princes silent; eyes to the blind and feet to the lame; the tree whose root is spread
out to the waters. But now: the derision of the young, the outcasts of the frightful valleys; the rabble through a wide
breach; lifted up to the wind and dissolved in the storm; a brother to jackals and a companion to ostriches; the harp
turned to mourning. Then his oath of clearing: a covenant with mine eyes; the even balance; the hand-mill at the door (31:10
drawn as the mill alone); the fatherless fed and the poor warmed with the fleece; the sun and the moon; the door opened to
the traveller; here is my signature; thistles instead of wheat. The words of Job are ended."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from job import G, art9 as K
from job.common import (pack, pf, pd, pf2, pd2, drawn, sg, sgs, cp, label, JOB_OLD, JOB_ASH, JOB_GRIEF, JOB_BOLD, JOB_HOPE, JOB_AWE, COLD, GOLDEN, RED)
from job import ch08 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JOB-C09-00-Title", "Chapter 9 · The Months of Old", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 280)">{K.past_tent("t9", 760, 800, 901)}</g><rect x="0" y="0" width="760" height="282" fill="#3A3A6A"></rect>')
    return chapter_title(9, "第九話", "The Months of Old", "Job 29 – 31", svg, "#3A3A6A", v("29:2"), "Job · Volume Eighteen")


SEGS = [pd2("job", "29:1-5", lambda w, h: K.past_tent("pt9", w, h, 902), "#3A3A6A", head="Oh That I Were as in the Months of Old", stamp=29),
        pf("job", "29:6", JOB_OLD),
        pd("job", "29:7-10", lambda w, h: K.gate_seat("gs9", w, h, 903), "#8FB8D8"),
        pd("job", "29:11-16", lambda w, h: K.helper("hp9", w, h, 904), "#8FD0E2"),
        pf("job", "29:17-18", JOB_OLD),
        pd("job", "29:19-20", lambda w, h: K.dew_tree(w, h, 905), "#5A6A9A"),
        pd("job", "29:21-25", lambda w, h: K.gate_seat("gs9b", w, h, 906), "#8FB8D8"),
        pd("job", "30:1-4", lambda w, h: K.outcasts("oc9", w, h, 907), "#5A4A4A", head="But Now They Have Me in Derision", stamp=30),
        pd("job", "30:5-8", lambda w, h: K.outcasts("oc9b", w, h, 908), "#5A4A4A"),
        pd("job", "30:9-11", lambda w, h: K.mockers("mk9", w, h, 909), "#5A3A3A"),
        pd("job", "30:12-15", lambda w, h: K.breach(w, h, 910), "#8A7A6A"),
        pf("job", "30:16-19", JOB_GRIEF, bg=COLD),
        pd("job", "30:20-23", lambda w, h: K.tempest(w, h, 911), "#0B0B1A"),
        pd("job", "30:24-28", lambda w, h: K.dark_day(w, h, 912), "#1A1A2A"),
        pd("job", "30:29", lambda w, h: K.jackals_ostriches(w, h, 913), "#2A2A4A"),
        pd("job", "30:30-31", lambda w, h: K.harp_mourning(w, h, 914), "#2A2430"),
        pf("job", "31:1-4", JOB_BOLD, bg=RED, head="I Made a Covenant with Mine Eyes", stamp=31),
        pd("job", "31:5-8", lambda w, h: K.balances(w, h, 915), "#5A5A7A"),
        pd("job", "31:9-12", lambda w, h: K.hand_mill(w, h, 916), "#5A4A3A"),
        pf("job", "31:13-15", JOB_ASH, bg=COLD),
        pd("job", "31:16-20", lambda w, h: K.sharing("sh9", w, h, 917), "#E8A06A"),
        pd("job", "31:21-25", lambda w, h: K.silver_dust(w, h, 918), "#3A2E2A"),
        pd("job", "31:26-28", lambda w, h: K.sun_moon(w, h, 919), "#F3B87A"),
        pf("job", "31:29-31", JOB_HOPE),
        pd("job", "31:32-34", lambda w, h: K.open_door("od9", w, h, 920), "#0B0B2A"),
        pd("job", "31:35-37", lambda w, h: K.signature(w, h, 921), "#3A2A2A", head="Here Is My Signature"),
        drawn(sgs("31:38-39") + [sg("31:40", to="barley."), cp("31:40", frm="The words of Job")], label("31:38-40"), lambda w, h: K.thistles(w, h, 922), "#7A7A8A", who="job")]
PG.extend(pack(SEGS, "JOB-C09-D", PG.next(), end=end_mark("NEXT · ELIHU", "right: 10px; bottom: 34px")))
