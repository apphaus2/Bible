"""Ecclesiastes volume, Chapter 1 — Vanity of Vanities (Ecclesiastes 1–3). Every verse, word for word from ref/asv.
The words of the Preacher (1:1 in a caption) over the king on his roof at evening; one generation goeth and another cometh;
the sun's course, the wind's circuits and the rivers to the sea as diagrams; no remembrance over the ruins in the sand; the
crooked rod and the tally that cannot be numbered; mirth, the great works and the pools, the singers and the treasure; light
and darkness; the heir at the door; a time to every purpose as a ring of fourteen cells; eternity in their heart under the
stars; the place of justice; man and beast on one road at dusk. God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from ecc import G, art as K
from discourse import seg
from ecc.common import (pack, cp, sg, sgs, face, drawn, PREACHER, PREACHER_GOLD, PREACHER_WARM, PREACHER_NIGHT, COLD, GOLDEN, DUSK)

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ECC-C01-00-Title", "Chapter 1 · Vanity of Vanities", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#1F5F9A"></rect><g transform="translate(0 280)">{K.sun_course(760, 800, 100)}</g>')
    return chapter_title(1, "第一話", "Vanity of Vanities", "Ecclesiastes 1 – 3", svg, "#1F5F9A", v("1:9", frm="and there is no new thing"), "Ecclesiastes · Volume Twenty-One")


SEGS = [drawn("1:1-2", below(lambda w, h: K.roof_view("rv1", w, h, 101), 0.24), "#2A1A3A", lines=[cp("1:1"), sg("1:2")], head="Vanity of Vanities", stamp=1, h=340),
        drawn("1:3-4", below(lambda w, h: K.generations("gn1", w, h, 102), 0.26), "#FFE6A0"),
        drawn("1:5", below(lambda w, h: K.sun_course(w, h, 103), 0.26), "#1F5F9A", h=360),
        drawn("1:6", below(lambda w, h: K.wind_circuits(w, h, 104), 0.16), "#6A8AA8", h=330),
        drawn("1:7", below(lambda w, h: K.rivers_sea(w, h, 105), 0.16), "#7AB8D8", h=320),
        face("1:8-9", PREACHER, bg=COLD),
        drawn("1:10-11", below(lambda w, h: K.ruins(w, h, 106), 0.3), "#C88A5A"),
        face("1:12-13", PREACHER_GOLD, head="I the Preacher Was King"),
        drawn("1:14-15", below(lambda w, h: K.crooked(w, h), 0.26), "#0B1A2E"),
        face("1:16-18", PREACHER_WARM, bg=DUSK)]
PG.extend(pack(SEGS, "ECC-C01-D", PG.next()))
SEGS2 = [face("2:1-2", PREACHER_WARM, bg=DUSK, head="I Made Me Great Works", stamp=2),
         drawn("2:3", below(lambda w, h: K.feast_hall("fh1", w, h, 107), 0.3), "#8A4A26"),
         drawn("2:4-6", below(lambda w, h: K.works("wk1", w, h, 108), 0.3), "#8FD0E2"),
         drawn("2:7-8", below(lambda w, h: K.possessions("ps1", w, h, 109), 0.36), "#8FD0E2"),
         face("2:9-10", PREACHER_GOLD),
         drawn("2:11", below(lambda w, h: K.works("wk1b", w, h, 110, wind=True), 0.24), "#6A6A7A", head="A Striving After Wind"),
         drawn("2:12-14", below(lambda w, h: K.light_dark("ld1", w, h, 111), 0.4), "linear-gradient(90deg, #FFE680 0%, #FFC14D 45%, #1E1650 55%, #0B0B2A 100%)"),
         face("2:15-16", PREACHER, bg=COLD),
         drawn("2:17-19", below(lambda w, h: K.heir("hr1", w, h, 112), 0.42), "#8A4A26"),
         face("2:20-21", PREACHER_WARM, bg=DUSK),
         drawn("2:22-23", below(lambda w, h: K.sleepless("sl1", w, h, 113), 0.3), "#1A1430"),
         drawn("2:24-26", below(lambda w, h: K.vine_fig("vf1", w, h, 114), 0.44), "#8FD0E2")]
PG.extend(pack(SEGS2, "ECC-C01-E", PG.next()))
SEGS3 = [seg(sgs("3:1-8"), "ECCL 3:1–8", bg="#12113A", head="A Time to Every Purpose"),
         seg([], "ECCL 3:2–8", art=lambda w, h: K.seasons(w, h, top=56), bg="#12113A", h=330, stamp=3)]
PG.extend(pack(SEGS3, "ECC-C01-F", PG.next(), by_need=False, min_size=None))
SEGS4 = [drawn("3:9-11", below(lambda w, h: K.eternity("et1", w, h, 115), 0.36), "#05051A"),
         face("3:12-15", PREACHER_GOLD),
         drawn("3:16-17", below(lambda w, h: K.justice("js1", w, h, 116), 0.34), "#3A0A1A"),
         drawn("3:18-21", below(lambda w, h: K.man_beast("mb1", w, h, 117), 0.44), "#4A2A4A"),
         face("3:22", PREACHER_NIGHT, bg=COLD)]
PG.extend(pack(SEGS4, "ECC-C01-G", PG.next(), default_head="A Time to Every Purpose", end=end_mark("NEXT · TWO ARE BETTER THAN ONE", "right: 10px; bottom: 34px")))
