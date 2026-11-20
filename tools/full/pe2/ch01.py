"""2 Peter volume, Chapter 1 — Until the Day Dawn (2 Peter 1–3). Every verse, word for word from ref/eng-asv.
2 Peter 1: Peter old, writing at Rome, seated now; partakers of the divine nature beside his face in white light; the eight
graces as a stair; the putting off of his tabernacle — his tent at night, the pegs drawn; the holy mount, Jesus in white
light with Moses and Elijah, "This is my beloved Son" in the Voice box; the lamp in a dark place and the day-star. 2 Peter 2:
the false teachers as words over a dividing road; the angels cast down, in words beside Peter's stern face; Noah with seven
others in the ark; Sodom and Gomorrah in ashes and righteous Lot going away; their railing, beside Peter's stern face; the
empty feast-hall; Balaam on the ass in the narrow way; springs without water and mists driven by a storm; the last state
worse than the first, beside Peter's grieving face; the true proverb in a song box over its emblem. 2 Peter 3: the first and
the second epistle; the mockers, beside his stern face; the world that then was overflowed with water; one day as a thousand
years on a balance; the Lord not slack, beside his face in white light; the day of the Lord as a thief, the elements melting
(no one drawn); what manner of persons, beside his stern face; new heavens and a new earth; Paul's epistles in their
pigeonholes; the doxology over the light."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from pe2 import G, art as A
from pe2.common import (K, Pages, D, F, glory, lt, lts, lp, ltj, lj, sg, gd, v, title, fin, PETER_OLD, PETER_LAMP, PETER_GRIEF, PETER_JOY, PETER_STERN,
                        GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG)
from gal.art import art

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2PE-C01-00-Title", "Chapter 1 · Until the Day Dawn", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2418"></rect><g transform="translate(0 300)">{A.study_old("t01", 760, 640, 6101, fig_h=400)}</g>'
    return title(1, "Until the Day Dawn", "2 Peter 1–3", svg, "#3A2418", v("1:19", frm="as unto a lamp", to="until the day dawn"))


SEGS = [
    # 2 Peter 1 — the divine nature; the holy mount; the lamp
    D(lp("1:1-2"), art(A.study_old, "so1", 6111), "#3A2418", head="Simon Peter", sky=1, art_h=280),
    F(lp("1:3-4"), PETER_JOY, bg=JOY_BG),
    D(lp("1:5-7"), A.graces_stair, "#0B1A2E", head="Supply Virtue", art_h=240),
    F(lp("1:8-11"), PETER_OLD),
    D(lp("1:12-15"), art(A.tent_struck, "ts1", 6113), "#0B0B2A", head="The Putting Off of My Tabernacle", art_h=240),
    D([lt("1:16"), lt("1:17", to="by the Majestic Glory,"), gd("1:17", frm="This is my beloved Son"), lt("1:18")],
      art(A.holy_mount, "hm1", 6116), "#2A2A6A", head="The Holy Mount", art_h=260),
    D([lt("1:19")] + lp("1:20-21"), art(A.lamp_daystar, 6119), "#14183A", head="A Lamp in a Dark Place", art_h=250),
    # 2 Peter 2 — false teachers; Noah, Lot, Balaam
    D(lp("2:1-3"), art(A.two_ways, 6121), "#2A1A3A", head="False Teachers", sky=2, art_h=230),
    D(lp("2:4-5"), art(A.ark_noah, 6125), "#3A4A6A", art_h=240),
    D(lp("2:6-9"), art(A.ashes_plain, "ap2", 6126), "#3A1A1A", head="Righteous Lot", art_h=240),
    F(lp("2:10-12"), PETER_STERN, bg=STERN_BG),
    D(lp("2:13-14"), art(A.empty_feast, 6213), "#B8987A", art_h=230),
    D(lp("2:15-16"), art(A.balaam_ass, "ba2", 6215), "#8FD0E2", head="The Way of Balaam", art_h=240),
    D(lp("2:17-19"), art(A.dry_springs, 6217), "#1A1A2A", head="Springs Without Water", art_h=230),
    F(lp("2:20-21"), PETER_GRIEF, bg=GRIEF_BG),
    D([lt("2:22", to="the true proverb,"), sg("2:22", frm="The dog turning")], A.dog_sow, "#0B1A2E", art_h=220),
    # 2 Peter 3 — the promise of his coming; the day of the Lord
    D(lp("3:1-2"), art(A.two_epistles, 6301), "#3A2418", head="The Second Epistle", sky=3, art_h=220),
    F(lp("3:3-4"), PETER_STERN, bg=STERN_BG, head="Where Is the Promise?"),
    D(lp("3:5-7"), art(A.overflowed, 6305), "#14182A", art_h=230),
    D([lt("3:8")], A.thousand_years, "#0B1A2E", head="As a Thousand Years", art_h=240),
    F([lt("3:9")], PETER_JOY, bg=JOY_BG),
    D([lt("3:10")], art(A.day_fire, 6310), "#2A0A0A", head="As a Thief", art_h=250),
    F(lp("3:11-12"), PETER_STERN, bg=STERN_BG),
    D(lp("3:13-14"), art(A.new_heavens, 6313), "#8FD0E2", head="A New Earth", art_h=250),
    D(lp("3:15-16"), art(A.pauls_letters, 6315), "#3A2418", head="Our Beloved Brother Paul", art_h=250),
    F([lt("3:17")], PETER_STERN, bg=STERN_BG),
    glory([lt("3:18")]),
]
PG.extend(K.pack(SEGS, "2PE-C01-D", PG.next(), end=fin("END OF 2 PETER · NEXT · 1 JOHN"), lone=3))
