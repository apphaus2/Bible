"""Philippians volume, Chapter 1 — To Live Is Christ (Philippians 1–2). Every verse, word for word from ref/eng-asv.
The letter written in Paul's bonds at Rome: Paul chained to the soldier, Timothy writing on his mat (1:1); the letter's road
from Rome by Brundisium and the Egnatian Way to Philippi; Paul by lamplight beside his face (1:6–8); the saints at Philippi
praying in the court of the house, the overseer with the roll (1:9–11); the whole prætorian guard, Paul chained and
speaking to the soldiers in their camp (1:12–14); "to live is Christ, and to die is gain" as a plate of the vine and the
sunrise (1:19–21); "to depart", a ship loosed from her moorings at dawn (1:22–24); the saints standing fast together in
the forum of Philippi before the magistrates (1:27–30). Philippians 2: the saints of one mind at table, serving one another;
2:5–11 as a plate of the way down and the way up (Christ as light, and once as ntcast's Jesus, small; the cross as three
crosses far off); lights in the world, a dark city with lamps in its windows; the drink-offering poured on the altar's fire;
Timothy standing ready with his staff; Epaphroditus sick on his bed, Paul beside him; Epaphroditus walking home along the
Egnatian Way with the letter."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from php import G, art as A
from php.common import (K, Pages, D, F, glory, lt, lp, ltj, lj, v, title, nxt, PAUL, PAUL_LAMP, PAUL_JOY, PAUL_STERN, PAUL_GRIEF, GOLD_BG, LAMP_BG,
                        JOY_BG, STERN_BG, GRIEF_BG, EPAPHRODITUS_SICK)
from php.art import art

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PHP-C01-00-Title", "Chapter 1 · To Live Is Christ", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2418"></rect><g transform="translate(0 300)">{A.prison_study("t01", 760, 640, 5001, fig_h=400)}</g>'
    return title(1, "To Live Is Christ", "Philippians 1–2", svg, "#3A2418", v("1:21"))


SEGS = [
    # Philippians 1 — the letter; my bonds; to live is Christ
    D([lt("1:1")], art(A.prison_study, "ps1", 5011), "#3A2418", head="Paul and Timothy", sky=1, art_h=300),
    D(lp("1:2-5"), art(A.philippi_road), "#0B1A2E", art_h=250),
    F(lp("1:6-8"), PAUL_LAMP, bg=LAMP_BG),
    D(lp("1:9-11"), art(A.philippi_house, "ph1", 5019), "#E8D8B0", art_h=250),
    D(lp("1:12-14"), art(A.praetorian, "pg1", 5022), "#8FD0E2", head="The Whole Prætorian Guard", art_h=270),
    F(lp("1:15-18"), PAUL),
    D(lp("1:19-21"), art(A.to_live), "#0B1A2E", head="To Live Is Christ", art_h=270),
    D(lp("1:22-24"), art(A.depart, "dp1", 5032), "#2A2A5A", art_h=260),
    F(lp("1:25-26"), PAUL_JOY, bg=JOY_BG),
    D(lp("1:27-30"), art(A.stand_fast, "sf1", 5037), "#8FD0E2", head="Stand Fast in One Spirit", art_h=250),
    # Philippians 2 — the mind of Christ; lights in the world; Timothy and Epaphroditus
    D(lp("2:1-4"), art(A.one_mind, "om1", 5041), "#E8D8B0", head="Of One Mind", sky=2, art_h=250),
    D(lp("2:5-8"), art(A.humbled), "#0B1A2E", head="Have This Mind in You", art_h=330),
    D(lp("2:9-11"), art(A.exalted), "#0B1A2E", art_h=330),
    F(lp("2:12-14"), PAUL),
    D(lp("2:15-16"), art(A.lights_world, 5055), "#05051A", head="Lights in the World", art_h=260),
    D(lp("2:17-18"), art(A.drink_offering, 5057), "#3A2A4A", art_h=220),
    F(lp("2:19-21"), PAUL),
    D(lp("2:22-24"), art(A.timothy_by, "tb1", 5059), "#3A2418", head="Timothy", art_h=250),
    D(lp("2:25-27"), art(A.sickbed, "sb1", 5065), "#3A2418", head="Epaphroditus", art_h=250),
    D(lp("2:28-30"), art(A.homeward, "hw1", 5068), "#8FD0E2", art_h=250),
]
PG.extend(K.pack(SEGS, "PHP-C01-D", PG.next(), end=nxt("NEXT · REJOICE IN THE LORD")))
