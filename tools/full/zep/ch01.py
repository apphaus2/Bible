"""Zephaniah volume, Chapter 1 — The Great Day of Jehovah (Zephaniah 1–3). Every verse, word for word from ref/asv.
The word (1:1 in a caption) beside Zephaniah's face; I will utterly consume all things (an empty land); the housetops and
the host of heaven; the day of Jehovah's sacrifice at the threshold; the cry from the fish gate; Jerusalem searched with
lamps; the day of darkness and the trumpet over the battlements; the land devoured by fire (1:17 words only); the chaff
and the meek; the Philistine coast as a map and as pastures; Moab's saltpits; the isles bowing; Nineveh's ruin with the
pelican and the porcupine; the oppressing city with wolves at its gate; the empty streets of the nations; the suppliants
from beyond the rivers of Ethiopia; the remnant's flock lying down; and Zion singing. God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, fin, NIGHT
from zep import G, art as A
from zep.common import K, cp, gd, sg, gds, sgs, ZEPHANIAH, ZEPHANIAH_STERN, ZEPHANIAH_GLAD, COLD, GOLDEN, RED, DUSK

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ZEP-C01-00-Title", "Chapter 1 · The Great Day of Jehovah", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#05050A"></rect><g transform="translate(0 280)">{A.day_dark(760, 800, 101)}</g>'
    return title(1, "The Great Day of Jehovah", "Zephaniah 1 – 3", svg, "#05050A", v("1:15", to="a day of wrath,"), "Zephaniah · Volume Thirty-Six")


SEGS = [K.face([cp("1:1")], ZEPHANIAH, head="The Word That Came unto Zephaniah", stamp=1),
        K.drawn(gds("1:2-3"), lambda w, h: A.desolate(w, h, 102), "#1A1418"),
        K.drawn(gds("1:4-6"), lambda w, h: A.housetops("ht1", w, h, 103), "#05051A"),
        K.drawn([sg("1:7"), *gds("1:8-9")], lambda w, h: A.sacrifice_day(w, h, 104), "#3A0A10", head="Hold Thy Peace"),
        K.drawn(gds("1:10-11"), lambda w, h: A.fish_gate(w, h, 105), "#3A2A3A"),
        K.drawn(gds("1:12-13"), lambda w, h: A.lamps(w, h, 106), "#0B0B1A"),
        K.drawn(sgs("1:14-16"), lambda w, h: A.day_dark(w, h, 107), "#05050A", head="The Great Day of Jehovah Is Near"),
        K.drawn([gd("1:17"), sg("1:18")], lambda w, h: A.fire_land(w, h, 108), "#1A0505"),
        K.drawn(sgs("2:1-3"), lambda w, h: A.chaff("cf1", w, h, 109), "#5A6A8A", head="Seek Ye Jehovah", stamp=2),
        K.drawn([sg("2:4"), gd("2:5")], lambda w, h: A.coast_map(w, h), "#0B1A2E"),
        K.drawn([gd("2:6"), sg("2:7")], lambda w, h: A.coast_pasture("pa1", w, h, 110), "#2A1A3A"),
        K.drawn(gds("2:8-10"), lambda w, h: A.saltpits(w, h, 111), "#C8A880"),
        K.drawn([sg("2:11"), gd("2:12")], lambda w, h: A.isles(w, h, 112), "#2A3A6A"),
        K.drawn(sgs("2:13-15"), lambda w, h: A.nineveh_ruin(w, h, 113), "#8A7A8A", head="This Is the Joyous City"),
        K.drawn(sgs("3:1-5"), lambda w, h: A.wolves_city(w, h, 114), "#1A1030", head="Woe to the Oppressing City", stamp=3),
        K.drawn(gds("3:6-7"), lambda w, h: A.empty_streets(w, h, 115), "#6A6A7A"),
        K.drawn(gds("3:8-10"), lambda w, h: A.suppliants("sp1", w, h, 116), "#3A4A8A"),
        K.drawn(gds("3:11-13"), lambda w, h: A.flock_rest(w, h, 117), "#2A1A3A"),
        K.drawn(sgs("3:14-17"), lambda w, h: A.zion_sings("zs1", w, h, 118), "#2A2A5A", head="Sing, O Daughter of Zion"),
        K.drawn(gds("3:18-20"), lambda w, h: A.remnant("rm1", w, h, 119), "#2A2A5A")]
PG.extend(K.pack(SEGS, "ZEP-C01-D", PG.next(), end=fin("END OF ZEPHANIAH · NEXT · HAGGAI")))
