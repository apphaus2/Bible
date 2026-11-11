"""2 Corinthians volume, Chapter 3 — My Grace Is Sufficient for Thee (2 Corinthians 10–13). Every verse, word for word
from ref/eng-asv. 10: Paul by lamplight in Macedonia; the strongholds cast down (a plate); his letters weighed (a plate);
the measure of the province and the parts beyond (a map). 11: the betrothal as an emblem, two rings and a lamp (the serpent
of 11:3 and Satan as an angel of light, 11:14, words only, beside Paul's face); the brethren from Macedonia at the tent-cloth;
the stars over Abraham's tents; then Paul's sufferings in words over empty places — the prison cell, the rods and the stones
before the gate, the broken ship on an empty sea, the eight perils, the cold camp — and the basket let down at Damascus. 12:
caught up to the third heaven, a road of light; the thorn branch (a messenger of Satan, words only); the light from heaven,
the Lord's answer in a speech box out of the light; the staff by the door; the empty street of shut doors (12:20–21). 13:
the gate and the witnesses (13:1, a song box); the letter sealed; the benediction (a glory panel) and the end of the letter."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from co2 import G, art3 as A, ch02 as _prev
from co2.common import (K, Pages, D, F, glory, lt, lp, lps, sg, sy, v, title, fin, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG,
                        LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2CO-C03-00-Title", "Chapter 3 · My Grace Is Sufficient for Thee", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A2438"></rect><g transform="translate(0 230)">{A.grace_light("t03", 760, 700, 3901)}</g>'
    return title(3, "My Grace Is Sufficient for Thee", "2 Corinthians 10–13", svg, "#2A2438", v("12:9", frm="My grace is sufficient for thee:", to="in weakness."))


def st(p, seed, **k): return lambda w, h: A.study2(p, w, h, seed, **k)

SEGS = [
    # 2 Corinthians 10
    D(lp("10:1-2"), st("st5", 2001, stage="read"), "#3A2418", head="The Meekness and Gentleness of Christ", sky=10, art_h=260),
    D(lp("10:3-6"), lambda w, h: A.strongholds(w, h), "#0B1A2E", head="The Casting Down of Strongholds", art_h=290),
    F(lp("10:7-9"), PAUL_STERN, bg=STERN_BG),
    D(lp("10:10-11"), lambda w, h: A.letters_weighed(w, h), "#0B1A2E", head="His Letters, They Say", art_h=230),
    F([lt("10:12")], PAUL),
    D(lp("10:13-16"), lambda w, h: A.province(w, h), "#0B1A2E", head="The Measure of the Province", art_h=270),
    F(lp("10:17-18"), PAUL_JOY, bg=JOY_BG),
    # 2 Corinthians 11
    D(lp("11:1-2"), lambda w, h: A.betrothal(w, h, 2101), "#3A2A4A", head="A Godly Jealousy", sky=11, art_h=220),
    F(lp("11:3-4"), PAUL_STERN, bg=STERN_BG),
    F(lp("11:5-8"), PAUL),
    D(lp("11:9-10"), lambda w, h: A.tent_cloth("tcl", w, h, 2109), "#C8A878", head="Not a Burden on Any Man", art_h=230),
    F(lp("11:11-15"), PAUL_STERN, bg=STERN_BG),
    F(lp("11:16-19"), PAUL),
    D(lp("11:20-22"), lambda w, h: A.abraham_stars(w, h, 2120), "#05051A", head="Are They Hebrews? So Am I", art_h=220),
    D([lt("11:23")], lambda w, h: A.prison_cell(w, h, 2123), "#2A2630", head="In Labors More Abundantly", art_h=240),
    D([lt("11:24"), lt("11:25", to="once was I stoned,")], lambda w, h: A.rods_stones(w, h, 2124), "#3A2A4A", art_h=240),
    D([lt("11:25", frm="thrice I suffered shipwreck,")], lambda w, h: A.wreck("wk1", w, h, 2125), "#2A3448", art_h=240),
    D([lt("11:26")], lambda w, h: A.perils(w, h), "#0B1A2E", head="In Perils", h=470),
    D([lt("11:27")], lambda w, h: A.cold_camp(w, h, 2127), "#05051A", art_h=230),
    F(lp("11:28-31"), PAUL_GRIEF, bg=GRIEF_BG),
    D(lp("11:32-33"), lambda w, h: A.basket_wall("bw2", w, h, 2132), "#05051A", head="Let Down in a Basket", h=450),
    # 2 Corinthians 12
    D(lp("12:1-4"), lambda w, h: A.third_heaven(w, h, 2201), "#FFF8DC", head="Caught Up into Paradise", sky=12, art_h=270),
    F(lp("12:5-6"), PAUL),
    D([lt("12:7")], lambda w, h: A.thorn_branch(w, h, 2207), "#3A1A2A", head="A Thorn in the Flesh", art_h=230),
    D([lt("12:8"), lt("12:9", to="And he hath said unto me,"), sy("12:9", frm="My grace is sufficient", to="in weakness."), lt("12:9", frm="Most gladly"), lt("12:10")],
      lambda w, h: A.grace_light("gl1", w, h, 2208), "#2A2438", head="My Grace Is Sufficient for Thee", art_h=260),
    F(lp("12:11-13"), PAUL),
    D(lp("12:14-15"), lambda w, h: A.ready_to_come(w, h, 2214), "#C8A878", head="The Third Time I Am Ready to Come", art_h=230),
    F(lp("12:16-18"), PAUL_STERN, bg=STERN_BG),
    D(lp("12:19-21"), lambda w, h: A.empty_street("es1", w, h, 2219), "#05050E", art_h=210),
    # 2 Corinthians 13
    D([lt("13:1", to="coming to you."), sg("13:1", frm="At the mouth")] + lp("13:2"), lambda w, h: A.witnesses("wt1", w, h, 2301), "#8FD0E2",
      head="Two Witnesses or Three", sky=13, art_h=230),
    F(lp("13:3-6"), PAUL_STERN, bg=STERN_BG),
    D(lp("13:7-10"), lambda w, h: A.still_life(w, h, 2307, sealed=True, night=True), "#3A2418", head="For Building Up", art_h=220),
    F(lp("13:11-13"), PAUL_JOY, bg=JOY_BG),
    glory([lt("13:14")], h=420),
]
PG.extend(K.pack(SEGS, "2CO-C03-D", PG.next(), end=fin("END OF 2 CORINTHIANS · NEXT · GALATIANS")))
