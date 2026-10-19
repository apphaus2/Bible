"""Job volume, Chapter 10 — Elihu (Job 32–37). Every verse, word for word from ref/asv.
The three men cease; Elihu the son of Barachel the Buzite, young, his wrath kindled (green, standing before the four seated
men): I am young, and ye are very old; my breast is as new wine-skins ready to burst; I also am formed out of the clay; God
speaketh in a dream, in a vision of the night; the sick man on his bed and the pit with the light over it — I have found a
ransom. Hear my words, ye wise men: far be it from God that he should do wickedness; in a moment they die, even at midnight;
no darkness where the workers of iniquity may hide. Look unto the heavens; who giveth songs in the night. Behold, God is
great: the drops of water, the spreadings of the clouds, the cattle that tell of the storm; the lightning unto the ends of
the earth; the snow, the beasts in their dens, the ice; the sky strong as a molten mirror; out of the north cometh golden
splendor (God never drawn)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from job import G, art10 as K
from job.common import (pack, pf, pd, pf2, pd2, drawn, face, caps, cp, sg, sgs, label, ELIHU, ELIHU_HOT, ELIHU_AWE, COLD, GOLDEN, RED)
from job import ch09 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JOB-C10-00-Title", "Chapter 10 · Elihu", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 280)">{K.golden_north(760, 800, 1001)}</g><rect x="0" y="0" width="760" height="282" fill="#2A2A5A"></rect>')
    return chapter_title(10, "第十話", "Elihu", "Job 32 – 37", svg, "#2A2A5A", v("37:22", to="golden splendor:"), "Job · Volume Eighteen")


SEGS = [drawn([caps("32:1-5")], label("32:1-5"), lambda w, h: K.elihu_scene("es10", w, h, 1002, speaking=False), "#7A7A8A", head="Elihu the Son of Barachel", stamp=32),
        face([cp("32:6", to="and said,"), sg("32:6", "elihu", frm="I am young,")] + sgs("32:7-8", "elihu"), label("32:6-8"), ELIHU, who="elihu"),
        pd("elihu", "32:9-14", lambda w, h: K.elihu_scene("es10b", w, h, 1003), "#7A7A8A"),
        pd("elihu", "32:15-19", lambda w, h: K.wineskins(w, h, 1004), "#4A3428"),
        pf("elihu", "32:20-22", ELIHU_HOT, bg=RED),
        pf("elihu", "33:1-4", ELIHU, head="I Also Am Formed out of the Clay", stamp=33),
        pd("elihu", "33:5-7", lambda w, h: K.potter(w, h, 1005), "#5A3A2A"),
        pd("elihu", "33:8-11", lambda w, h: K.stocks(w, h, 1006), "#5A5048"),
        pf("elihu", "33:12-14", ELIHU_HOT, bg=RED),
        pd("elihu", "33:15-18", lambda w, h: K.night_spirit(w, h, 1007), "#0F0E2A", head="In a Dream, in a Vision of the Night"),
        pd("elihu", "33:19-22", lambda w, h: K.sick_bed(w, h, 1008), "#2A2430"),
        pd("elihu", "33:23-25", lambda w, h: K.pit_light(w, h, 1009, rising=True), "#0B0806", full=True, head="I Have Found a Ransom"),
        pd("elihu", "33:26-28", lambda w, h: K.morning("mn10", w, h, 1010), "#2A2A5A"),
        pf("elihu", "33:29-33", ELIHU),
        pd2("elihu", "34:1-4", lambda w, h: K.elihu_scene("es10c", w, h, 1011), "#7A7A8A", head="Hear My Words, Ye Wise Men", stamp=34),
        pd("elihu", "34:5-9", lambda w, h: K.ash_heap("ah10", w, h, 1012), "#6A6A7A"),
        pf("elihu", "34:10-12", ELIHU_HOT, bg=RED),
        pd("elihu", "34:13-15", lambda w, h: K.hung_nothing(w, h, 1013), "#020210", full=True),
        pd("elihu", "34:16-20", lambda w, h: K.midnight_palace(w, h, 1014), "#05051A"),
        pd("elihu", "34:21-25", lambda w, h: K.dug_wall(w, h, 1015), "#05051A"),
        pd("elihu", "34:26-30", lambda w, h: K.huddled("hd10", w, h, 1016), "#4A5060"),
        pf("elihu", "34:31-33", ELIHU),
        pd("elihu", "34:34-37", lambda w, h: K.elihu_scene("es10d", w, h, 1017), "#7A7A8A"),
        pd2("elihu", "35:1-4", lambda w, h: K.elihu_scene("es10e", w, h, 1018, night=True), "#1A1A3A", head="Look unto the Heavens", stamp=35),
        pd("elihu", "35:5-8", lambda w, h: K.stars_clouds(w, h, 1019), "#05051A"),
        pd("elihu", "35:9-11", lambda w, h: K.night_singer("ns10", w, h, 1020), "#05051A"),
        pf("elihu", "35:12-16", ELIHU),
        pf2("elihu", "36:1-4", ELIHU, head="Behold, God Is Mighty", stamp=36),
        pf("elihu", "36:5-7", ELIHU_AWE, bg=COLD),
        pd("elihu", "36:8-12", lambda w, h: K.prison_open(w, h, 1021), "#3A3438"),
        pf("elihu", "36:13-15", ELIHU_HOT, bg=RED),
        pd("elihu", "36:16-21", lambda w, h: K.K2.large_place(w, h, 1022), "#8FD0E2"),
        pf("elihu", "36:22-26", ELIHU_AWE, bg=COLD, head="Behold, God Is Great"),
        pd("elihu", "36:27-30", lambda w, h: K.rain_fields(w, h, 1023), "#5A6A7A"),
        pd("elihu", "36:31-33", lambda w, h: K.storm_cattle("sc10", w, h, 1024), "#3A3A4A"),
        pd("elihu", "37:1-5", lambda w, h: K.lightning_world(w, h, 1025), "#05051A", full=True, head="Hear the Noise of His Voice", stamp=37),
        pd("elihu", "37:6-7", lambda w, h: K.snow_land("sn10", w, h, 1026), "#8A9AB0"),
        pd("elihu", "37:8-9", lambda w, h: K.den(w, h, 1027), "#3A3A4A"),
        pd("elihu", "37:10-13", lambda w, h: K.ice(w, h, 1028), "#5A6A8A"),
        pd("elihu", "37:14-18", lambda w, h: K.mirror_sky(w, h, 1029), "#C8D8E0", head="Consider the Wondrous Works of God"),
        pf("elihu", "37:19-21", ELIHU_AWE, bg=COLD),
        pd("elihu", "37:22-24", lambda w, h: K.golden_north(w, h, 1030), "#2A2A5A", full=True)]
PG.extend(pack(SEGS, "JOB-C10-D", PG.next(), end=end_mark("NEXT · OUT OF THE WHIRLWIND", "right: 10px; bottom: 34px")))
