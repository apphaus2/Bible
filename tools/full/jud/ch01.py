"""Jude volume, Chapter 1 — Contend for the Faith (Jude 1–25). Every verse, word for word from ref/eng-asv.
Jude writing by lamplight, a young scribe on his mat; contend earnestly for the faith, beside Jude's stern face; the people
saved out of Egypt walking through the sea; the angels in everlasting bonds (words) and the smoke of Sodom over the empty
plain; Michael the archangel on mount Nebo, white light with no face, "The Lord rebuke thee" in a balloon (the devil never
drawn); Cain, Balaam and Korah as a plate of three; the hidden rocks, clouds without water, trees twice dead, wild waves and
wandering stars as a plate of five; Enoch under the sky full of lights, his prophecy in a song box; the mockers, beside
Jude's stern face; building up yourselves on your most holy faith (1 Peter's builders and the corner stone); a brand snatched out of the fire; the doxology over the light."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jud import G, art as A
from jud.common import (K, Pages, D, F, glory, lt, lts, lp, ltj, lj, sg, gd, sy, sj, v, title, fin, JUDE, JUDE_LAMP, JUDE_GRIEF, JUDE_JOY, JUDE_STERN,
                        GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG)
from gal.art import art

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JUD-C01-00-Title", "Chapter 1 · Contend for the Faith", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2418"></rect><g transform="translate(0 300)">{A.study_jude("t01", 760, 640, 6501, fig_h=400)}</g>'
    return title(1, "Contend for the Faith", "Jude 1–25", svg, "#3A2418", v("1:3", frm="contend earnestly", to="unto the saints."))


SEGS = [
    D(lp("1:1-2"), art(A.study_jude, "sj1", 6511), "#3A2418", head="Jude, Brother of James", sky=1, art_h=280),
    F(lp("1:3-4"), JUDE_STERN, bg=STERN_BG, head="Contend Earnestly"),
    D([lt("1:5")], art(A.through_sea, "ts5", 6515), "#0B0B2A", head="Out of the Land of Egypt", art_h=250),
    D(lp("1:6-8"), art(A.sodom_smoke, 6516), "#1A0A0A", art_h=230),
    D([lt("1:9", to="but said,"), sy("1:9", frm="The Lord rebuke thee.")], art(A.michael_nebo, "mn9", 6519), "#2A1A4A", head="Michael the Archangel", art_h=260),
    D(lp("1:10-11"), art(A.three_ways, "tw11", 6520), "#0B1A2E", head="Woe unto Them", art_h=230),
    D(lp("1:12-13"), art(A.five_plate, 6522), "#0B1A2E", art_h=200),
    D([lt("1:14", to="prophesied, saying,"), sj(("1:14", "Behold, the Lord came", None), "1:15")], art(A.enoch_lights, "el14", 6524), "#05051A", head="Enoch Prophesied", art_h=210),
    F(lp("1:16-19"), JUDE),
    D(lp("1:20-21"), art(A.living_stones, "ls20", 6520), "#8FD0E2", head="Keep Yourselves in the Love of God", art_h=220),
    D(lp("1:22-23"), art(A.brand_fire, 6530), "#140A08", art_h=220),
    glory(lp("1:24-25")),
]
PG.extend(K.pack(SEGS, "JUD-C01-D", PG.next(), end=fin("END OF JUDE · NEXT · REVELATION"), lone=3))
