"""Job volume, Chapter 2 — The Vision of the Night (Job 4–7). Every verse, word for word from ref/asv.
Eliphaz the Temanite's first speech in song lines (teal): they that plow iniquity reap the same; the old lion and the
scattered whelps; the vision of the night — a form without appearance passing before a sleeper's face; houses of clay
crushed before the moth; man born unto trouble as the sparks fly upward; rain upon the fields; a shock of grain in its
season. Job's answer (red): his vexation in the balances, heavier than the sand of the seas; the wild ass and the ox; his
brethren deceitful as a brook dark with ice and gone in the heat, the caravans of Tema at the dry channel; the hireling
longing for the shadow; days swifter than a weaver's shuttle; the cloud that vanisheth; the sea and the watch set over it."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from job import G, art2 as K
from job.common import (pack, pf, pd, pf2, pd2, ELIPHAZ, ELIPHAZ_STERN, ELIPHAZ_NIGHT, JOB_ASH, JOB_GRIEF, JOB_BOLD, COLD, GOLDEN, RED)
from job import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JOB-C02-00-Title", "Chapter 2 · The Vision of the Night", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.night_spirit(760, 780, 201)}</g><rect x="0" y="0" width="760" height="302" fill="#0F0E2A"></rect>')
    return chapter_title(2, "第二話", "The Vision of the Night", "Job 4 – 7", svg, "#0F0E2A", v("4:17"), "Job · Volume Eighteen")


SEGS = [pf2("eli", "4:1-3", ELIPHAZ, head="Eliphaz the Temanite", stamp=4),
        pd("eli", "4:4-9", lambda w, h: K.thorn_field(w, h, 202), "#E8D8A0"),
        pd("eli", "4:10-11", lambda w, h: K.lions(w, h, 203), "#E8B880"),
        pd("eli", "4:12-16", lambda w, h: K.night_spirit(w, h, 204), "#0F0E2A", head="A Spirit Passed Before My Face"),
        pf("eli", "4:17-18", ELIPHAZ_NIGHT, bg=COLD),
        pd("eli", "4:19-21", lambda w, h: K.clay_houses(w, h, 205), "#5A4A6A"),
        pf("eli", "5:1-2", ELIPHAZ_STERN, bg=RED, stamp=5),
        pd("eli", "5:3-5", lambda w, h: K.thorn_field(w, h, 221), "#E8D8A0"),
        pd("eli", "5:6-9", lambda w, h: K.sparks(w, h, 206), "#05050F"),
        pd("eli", "5:10-13", lambda w, h: K.rain_fields(w, h, 207), "#5A6A7A"),
        pd("eli", "5:14-16", lambda w, h: K.dark_day(w, h, 222), "#1A1A2A"),
        pf("eli", "5:17-18", ELIPHAZ),
        pd("eli", "5:19-22", lambda w, h: K.K2.famine(w, h, 208), "#FFF4C2"),
        pd("eli", "5:23-27", lambda w, h: K.shocks("sh2", w, h, 209), "#5A4A7A"),
        pd2("job", "6:1-4", lambda w, h: K.balances(w, h, 210), "#5A5A7A", head="Oh That My Vexation Were Weighed", stamp=6),
        pd("job", "6:5-7", lambda w, h: K.ass_ox(w, h, 211), "#8FD0E2"),
        pf("job", "6:8-10", JOB_GRIEF, bg=COLD),
        pd("job", "6:11-13", lambda w, h: K.ash_heap("ah2a", w, h, 223), "#6A6A7A"),
        pd("job", "6:14-17", lambda w, h: K.brook(w, h, 212), "#5A6A8A"),
        pd("job", "6:18-21", lambda w, h: K.dry_caravan("dc2", w, h, 213), "#E8C890"),
        pf("job", "6:22-24", JOB_BOLD, bg=RED),
        pd("job", "6:25-30", lambda w, h: K.brook(w, h, 214, dry=True), "#8FD0E2"),
        pd("job", "7:1-4", lambda w, h: K.hireling("hl2", w, h, 215), "#E89A5A", head="Swifter Than a Weaver's Shuttle", stamp=7),
        pd("job", "7:5-7", lambda w, h: K.loom(w, h, 216), "#4A2A3A"),
        pd("job", "7:8-10", lambda w, h: K.cloud_gone(w, h, 217), "#5A8AB8"),
        pd("job", "7:11-12", lambda w, h: K.sea_watch(w, h, 218), "#0B1A2E"),
        pd("job", "7:13-16", lambda w, h: K.dream_bed(w, h, 219), "#0F0E2A"),
        pf("job", "7:17-18", JOB_GRIEF, bg=COLD),
        pd("job", "7:19-21", lambda w, h: K.ash_heap("ah2", w, h, 220, night=True), "#0B0B2A")]
PG.extend(pack(SEGS, "JOB-C02-D", PG.next(), end=end_mark("NEXT · NO UMPIRE BETWIXT US", "right: 10px; bottom: 34px")))
