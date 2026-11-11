"""2 Corinthians volume, Chapter 2 — God Loveth a Cheerful Giver (2 Corinthians 6–9). Every verse, word for word from
ref/eng-asv. 6: the day of salvation, God's word of 6:2 in the Voice box; the hardships of 6:4–10 in words over a shut
prison door at night and the armour of righteousness on its stand, then beside Paul's face; the unequal yoke, an ox and an
ass; the temple of the living God, light over the saints gathered (6:16–18 in the Voice box; Belial, 6:15, words only); come
out from among them. 7: the basin of clean water; fightings without, fears within — Paul alone by the lamp in Macedonia; the
coming of Titus; the church at Corinth hearing the letter; the joy of Titus. 8: the churches of Macedonia bringing their
gifts to the chest; Bethlehem (8:9); the manna and the omers (8:15, a song box); Titus and the brethren on the road with the
bounty; the sealed letter given to Titus. 9: the collection ready in Achaia; the two sowers; the cheerful giver; the
harvest (9:9, a song box); the gift carried to Jerusalem on the map; thanks be to God for his unspeakable gift (a glory
panel)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from co2 import G, art2 as A, ch01 as _prev
from co2.common import (K, Pages, D, F, glory, lt, lp, lps, sg, gd, gds, v, title, nxt, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG,
                        LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2CO-C02-00-Title", "Chapter 2 · God Loveth a Cheerful Giver", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#FFE6A0"></rect><g transform="translate(0 300)">{A.cheerful_giver("t02", 760, 700, 2901)}</g>'
    return title(2, "God Loveth a Cheerful Giver", "2 Corinthians 6–9", svg, "#FFE6A0", v("9:7", frm="God loveth a cheerful giver."))


def st(p, seed, **k): return lambda w, h: A.study2(p, w, h, seed, **k)

SEGS = [
    # 2 Corinthians 6
    D([lt("6:1"), lt("6:2", to="(for he saith,"), gd("6:2", frm="At an acceptable time", to="did I succor thee:"), lt("6:2", frm="behold, now is")],
      lambda w, h: A.salvation_day(w, h, 1601), "#2A2A5A", head="Now Is the Day of Salvation", sky=6, art_h=230),
    D(lp("6:3-5"), lambda w, h: A.prison_night("pn1", w, h, 1603), "#14141E", head="In Much Patience", art_h=220),
    D(lp("6:6-7"), lambda w, h: A.armour(w, h), "#0B1A2E", art_h=230),
    F(lp("6:8-10"), PAUL_JOY, bg=JOY_BG),
    F(lp("6:11-13"), PAUL),
    D([lt("6:14")], lambda w, h: A.unequal_yoke(w, h, 1614), "#5A3A6A", head="Be Not Unequally Yoked", art_h=250),
    D([lt("6:15"), lt("6:16", to="even as God said,"), gd("6:16", frm="I will dwell in them")], lambda w, h: A.temple_living("tl1", w, h, 1615), "#5A4A5A",
      head="A Temple of the Living God", art_h=240),
    D(gds("6:17-18"), lambda w, h: A.come_out("co1", w, h, 1617), "#2A2A5A", art_h=230),
    # 2 Corinthians 7
    D(lp("7:1-2"), lambda w, h: A.basin_water(w, h, 1701), "#D8C8A8", head="Open Your Hearts to Us", sky=7, art_h=210),
    F(lp("7:3-4"), PAUL_JOY, bg=JOY_BG),
    D([lt("7:5")], lambda w, h: A.fears_within("fw1", w, h, 1705), "#3A2E3A", head="Fightings Without, Fears Within", art_h=250),
    D(lp("7:6-7"), lambda w, h: A.titus_comes("tc1", w, h, 1706), "#C8A878", head="The Coming of Titus", art_h=260),
    F(lp("7:8-10"), PAUL_GRIEF, bg=GRIEF_BG),
    D(lp("7:11-12"), lambda w, h: A.corinth_reading("cr1", w, h, 1711), "#5A4232", head="What Earnest Care", art_h=220),
    D(lp("7:13-16"), st("st3", 1713, bearer=True), "#3A2418", head="The Joy of Titus", art_h=260),
    # 2 Corinthians 8
    D(lp("8:1-5"), lambda w, h: A.macedonia_giving("mg1", w, h, 1801), "#8FD0E2", head="The Churches of Macedonia", sky=8, art_h=230),
    F(lp("8:6-8"), PAUL),
    D([lt("8:9")], lambda w, h: A.bethlehem(w, h, 1809, star=True), "#0B0B2A", head="For Your Sakes He Became Poor", art_h=250),
    D(lp("8:10-14") + [lt("8:15", to="as it is written,"), sg("8:15", frm="He that gathered")], lambda w, h: A.manna_omers(w, h, 1815), "#0B1A2E",
      head="That There May Be Equality", art_h=230),
    D(lp("8:16-19"), lambda w, h: A.titus_road("trd", w, h, 1816), "#8FD0E2", head="Titus and the Brother", art_h=230),
    F(lp("8:20-22"), PAUL_STERN, bg=STERN_BG),
    D(lp("8:23-24"), st("st4", 1823, stage="give", bearer=True), "#3A2418", head="My Partner and My Fellow-Worker", art_h=280),
    # 2 Corinthians 9
    D(lp("9:1-2"), lambda w, h: A.achaia_ready("ar1", w, h, 1901), "#C8A878", head="The Ministering to the Saints", sky=9, art_h=210),
    F(lp("9:3-5"), PAUL),
    D([lt("9:6")], lambda w, h: A.two_sowers("ts1", w, h, 1906), "#8FD0E2", head="He That Soweth Bountifully", art_h=260),
    D([lt("9:7")], lambda w, h: A.cheerful_giver("cg1", w, h, 1907), "#FFE6A0", head="God Loveth a Cheerful Giver", art_h=260),
    D([lt("9:8"), lt("9:9", to="as it is written,"), sg("9:9", frm="He hath scattered")] + lp("9:10-11"), lambda w, h: A.harvest_poor("hp1", w, h, 1908), "#5A3A6A",
      art_h=220),
    D(lp("9:12-14"), lambda w, h: A.to_jerusalem_gift(w, h), "#0B1A2E", head="Thanksgivings unto God", art_h=250),
    glory([lt("9:15")]),
]
PG.extend(K.pack(SEGS, "2CO-C02-D", PG.next(), end=nxt("NEXT · MY GRACE IS SUFFICIENT FOR THEE")))
