"""1 Corinthians volume, Chapter 2 — A Little Leaven (1 Corinthians 5–7). Every verse, word for word from ref/eng-asv.
Restraint throughout: 1 Corinthians 5 in words over a house front at night with its door shut and barred and an empty
street (5:5, Satan, words only, beside Paul's stern face); the leaven, the unleavened cakes and the passover lamb as an
emblem in light (5:6–8). 1 Corinthians 6: the tribunal in the forum, brother suing brother before the magistrate (6:1–8);
6:9–10 over an empty street at night; washed, the dawn over still water (6:11); the meat market (6:13); 6:15–18 over the
city dark under the Acrocorinth; the temple (6:19–20). 1 Corinthians 7 over plain household scenes, no one in the first:
a lamp on a table and a shut door (7:1–4; 7:5, Satan, words only); a house door (7:10); a man, his wife and their children
in their courtyard (7:14); the tables of the commandments (7:19); a bondservant at the well (7:21); the sun going down
over the sea (7:31); prayer and the household's table (7:32–34); a father and his daughter at the door (7:37); a widow at
her door at dusk (7:39)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from co1 import G, art2 as A, ch01 as _prev
from co1.common import (K, Pages, D, F, lt, lts, lp, ltj, lj, sg, gd, wq, qw, v, title, nxt, PAUL, PAUL_LAMP, PAUL_STERN, PAUL_JOY, PAUL_GRIEF,
                        GOLD_BG, LAMP_BG, STERN_BG, JOY_BG, GRIEF_BG)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1CO-C02-00-Title", "Chapter 2 · A Little Leaven", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2A22"></rect><g transform="translate(0 300)">{A.leaven_passover(760, 700, 501, labels=False)}</g>'
    return title(2, "A Little Leaven", "1 Corinthians 5–7", svg, "#3A2A22", v("5:6", frm="a little leaven"))


SEGS = [
    # 1 Corinthians 5
    D(lp("5:1-2"), lambda w, h: A.shut_house(w, h, 1501), "#05051A", head="Puffed Up", sky=5, art_h=260),
    F(lp("5:3-5"), PAUL_STERN, bg=STERN_BG),
    D(lp("5:6-8"), lambda w, h: A.leaven_passover(w, h, 1506), "#3A2A22", head="Christ Our Passover", art_h=260),
    D(lp("5:9-11"), lambda w, h: A.night_street("ns1", w, h, 1509), "#05051A", head="Not to Keep Company", art_h=260),
    F(lp("5:12-13"), PAUL_STERN, bg=STERN_BG),
    # 1 Corinthians 6
    D(lp("6:1-3"), lambda w, h: A.tribunal("tb1", w, h, 1601), "#8FD0E2", head="Brother Goeth to Law with Brother", sky=6, art_h=260),
    F(lp("6:4-6"), PAUL),
    D(lp("6:7-8"), lambda w, h: A.tribunal("tb2", w, h, 1607, stage="wrong"), "#8FD0E2", art_h=260),
    D(lp("6:9-10"), lambda w, h: A.night_street("ns2", w, h, 1609), "#05051A", head="Such Were Some of You", art_h=260),
    D([lt("6:11")], lambda w, h: A.washed(w, h, 1611), "#2A2A5A", art_h=260),
    D(lp("6:12-14"), lambda w, h: A.market_meats("mm1", w, h, 1612), "#E8905A", head="All Things Are Lawful", art_h=260),
    D(lp("6:15") + [lt("6:16", to="for,"), sg("6:16", frm="The twain")] + lp("6:17-18"), lambda w, h: A.city_night("cn1", w, h, 1615), "#0B0B2A", art_h=260),
    D(lp("6:19-20"), lambda w, h: A.temple_of_god("tg2", w, h, 1619), "#5A7AB0", head="Bought with a Price", art_h=260),
    # 1 Corinthians 7
    D(lp("7:1-4"), lambda w, h: A.lamp_table(w, h, 1701), "#3A2A20", head="Concerning the Things Whereof Ye Wrote", sky=7, art_h=260),
    F(lp("7:5-7"), PAUL),
    F(lp("7:8-9"), PAUL_LAMP, bg=LAMP_BG),
    D(lp("7:10-11"), lambda w, h: A.house_door(w, h, 1710), "#8FD0E2", art_h=260),
    D(lp("7:12-14"), lambda w, h: A.household("hh1", w, h, 1712), "#8FD0E2", head="Now Are They Holy", art_h=260),
    F(lp("7:15-16"), PAUL),
    D(lp("7:17-19"), lambda w, h: A.tablets(w, h), "#0B1A2E", head="As God Hath Called Each", art_h=260),
    D(lp("7:20-24"), lambda w, h: A.bondservant("bs1", w, h, 1720), "#FFB07A", art_h=260),
    F(lp("7:25-26"), PAUL_LAMP, bg=LAMP_BG, head="Concerning Virgins"),
    D(lp("7:27-28"), lambda w, h: A.cords(w, h, 1727), "#C8B490", art_h=240),
    D(lp("7:29-31"), lambda w, h: A.passing(w, h, 1729), "#2A1A3A", head="The Time Is Shortened", art_h=260),
    D(lp("7:32-34"), lambda w, h: A.cares("cr1", w, h, 1732), "#3A2A20", art_h=260),
    F(lp("7:35-36"), PAUL),
    D(lp("7:37-38"), lambda w, h: A.father_daughter("fd1", w, h, 1737), "#8FD0E2", art_h=260),
    D(lp("7:39-40"), lambda w, h: A.widow_door("wd1", w, h, 1739), "#3A2A5A", art_h=260),
]
PG.extend(K.pack(SEGS, "1CO-C02-D", PG.next(), budget=950, lone=1.5, end=nxt("NEXT · KNOWLEDGE PUFFETH UP")))
