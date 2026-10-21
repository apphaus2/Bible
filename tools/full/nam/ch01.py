"""Nahum volume, Chapter 1 — The Burden of Nineveh (Nahum 1–3). Every verse, word for word from ref/asv.
The burden (1:1 in a caption) beside Nahum's face; the whirlwind and the storm; the stronghold and the over-running flood;
thorns and stubble; Jehovah's words breaking the yoke; the feet of him that bringeth good tidings on the mountains; then
the siege: the chariots raging in the streets, the gates of the rivers opened, the spoil, the empty den of the lions, the
chariots burning in the smoke; woe to the bloody city (3:3 words over the walls by night); the city a gazing-stock;
No-amon by the Nile (3:10 words only); the fig-tree fortresses; the brickkiln; the locusts in the hedges; and the people
scattered on the mountains. God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, fin, NIGHT
from nam import G, art as A
from nam.common import K, cp, gd, sg, gds, sgs, NAHUM, NAHUM_STERN, NAHUM_STORM, COLD, GOLDEN, RED, DUSK

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("NAM-C01-00-Title", "Chapter 1 · The Burden of Nineveh", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A0A1A"></rect><g transform="translate(0 280)">{A.chariots_streets("tc", 760, 800, 101, night_=True)}</g>'
    return title(1, "The Burden of Nineveh", "Nahum 1 – 3", svg, "#2A0A1A", v("2:4", to="like the lightnings."), "Nahum · Volume Thirty-Four")


SEGS = [K.face([cp("1:1"), sg("1:2")], NAHUM, head="The Burden of Nineveh", stamp=1),
        K.drawn(sgs("1:3-6"), lambda w, h: A.whirlwind(w, h, 102), "#0B0B1A", head="In the Whirlwind and in the Storm"),
        K.drawn(sgs("1:7-8"), lambda w, h: A.flood(w, h, 103), "#2A3A5A"),
        K.drawn(sgs("1:9-11"), lambda w, h: A.thorns_fire(w, h, 104), "#2A0A0A"),
        K.drawn([cp("1:12", to="Thus saith Jehovah:"), gd("1:12", frm="Though they"), *gds("1:13-14")], lambda w, h: A.broken_yoke(w, h, 105), "#3A3A6A"),
        K.drawn(sgs("1:15"), lambda w, h: A.tidings("td1", w, h, 106), "#2A2A5A", head="The Feet of Him That Bringeth Good Tidings"),
        K.drawn(sgs("2:1-3"), lambda w, h: A.chariots_streets("cs1", w, h, 107), "#8A5A3A", head="He That Dasheth in Pieces", stamp=2),
        K.drawn(sgs("2:4-5"), lambda w, h: A.chariots_streets("cs2", w, h, 108, night_=True), "#2A0A1A"),
        K.drawn(sgs("2:6-8"), lambda w, h: A.river_gates(w, h, 109), "#3A4A6A", head="The Gates of the Rivers Are Opened"),
        K.drawn(sgs("2:9-10"), lambda w, h: A.spoil(w, h, 110), "#2A1A14"),
        K.drawn(sgs("2:11-12"), lambda w, h: A.lions_den(w, h, 111), "#5A4A4A", head="Where Is the Den of the Lions?"),
        K.drawn(gds("2:13"), lambda w, h: A.burnt_chariots(w, h, 112), "#1A0A0A"),
        K.drawn(sgs("3:1-4"), lambda w, h: A.bloody_city(w, h, 113), "#0A0508", head="Woe to the Bloody City", stamp=3),
        K.drawn(gds("3:5-7"), lambda w, h: A.gazing("gz1", w, h, 114), "#5A5A6A"),
        K.drawn(sgs("3:8-10"), lambda w, h: A.no_amon(w, h, 115), "#E8C890", head="Art Thou Better than No-amon?"),
        K.drawn(sgs("3:11-13"), lambda w, h: A.fig_fortress(w, h, 116), "#6A3A2A"),
        K.drawn(sgs("3:14-15"), lambda w, h: A.brickkiln("bk1", w, h, 117), "#8A6A4A"),
        K.drawn(sgs("3:16-17"), lambda w, h: A.locust_hedges(w, h, 118), "#5A6A8A"),
        K.drawn(sgs("3:18-19"), lambda w, h: A.scattered("sc1", w, h, 119), "#2A1A3A", head="Thy Shepherds Slumber")]
PG.extend(K.pack(SEGS, "NAM-C01-D", PG.next(), end=fin("END OF NAHUM · NEXT · HABAKKUK")))
