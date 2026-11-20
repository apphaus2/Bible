"""Philippians volume, Chapter 2 — Rejoice in the Lord (Philippians 3–4). Every verse, word for word from ref/eng-asv.
Philippians 3: Epaphroditus home again, reading the letter to the church at Philippi by lamplight (3:1); "beware of the
dogs" in words beside Paul's stern face (3:2–4); his credentials as a plate — the eighth day, the stock of Israel, the tribe
of Benjamin, a Hebrew of Hebrews, a Pharisee, persecuting the church, blameless; all things counted loss on the balance
(3:7–8); "that I may know him" beside his face in white light; the runner in the stadium pressing toward the goal
(3:12–14); the straight road and the surveyor's rule, the brethren walking in one another's steps (3:15–17); "enemies of
the cross" beside his grieving face; Philippi the Roman colony, its arch on the Egnatian Way under the opened light of
heaven (3:20–21). Philippians 4: Euodia and Syntyche and the true yokefellow; "Rejoice in the Lord always" beside his face;
the peace of God keeping guard over a town by night (4:6–7); "whatsoever things are true" as a plate of six emblems; want
and plenty, the bare cell and the spread table (4:10–12); "I can do all things"; the gifts sent from Philippi on the map
(4:15–17); Epaphroditus bringing the gift, the censer's sweet smoke (4:18–20); Cæsar's household at the Palatine
(4:21–22); the grace over the light."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from php import G, art as A, art2 as A2, ch01 as _prev
from php.common import (K, Pages, D, F, glory, lt, lp, ltj, lj, v, title, fin, PAUL, PAUL_LAMP, PAUL_JOY, PAUL_STERN, PAUL_GRIEF, GOLD_BG, LAMP_BG,
                        JOY_BG, STERN_BG, GRIEF_BG)
from php.art import art

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PHP-C02-00-Title", "Chapter 2 · Rejoice in the Lord", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A2.runner("t02", 760, 640, 5201)}</g>'
    return title(2, "Rejoice in the Lord", "Philippians 3–4", svg, "#3A6A8A", v("4:4"))


SEGS = [
    # Philippians 3 — loss for Christ; I press on; our citizenship is in heaven
    D([lt("3:1")], art(A.philippi_house, "ph2", 5301, stage="read"), "#2A2050", head="Rejoice in the Lord", sky=3, art_h=300),
    F(lp("3:2-4"), PAUL_STERN, bg=STERN_BG),
    D(lp("3:5-6"), art(A2.credentials), "#0B1A2E", head="A Hebrew of Hebrews", art_h=290),
    D(lp("3:7-11"), art(A2.loss_scales), "#0B1A2E", art_h=260),
    D(lp("3:12-14"), art(A2.runner, "rn1", 5312), "#8FD0E2", head="I Press On toward the Goal", art_h=260),
    D(lp("3:15-17"), art(A2.rule_road, "rr1", 5315), "#8FD0E2", art_h=240),
    F(lp("3:18-19"), PAUL_GRIEF, bg=GRIEF_BG),
    D(lp("3:20-21"), art(A2.colony_gate, "cg1", 5320), "#3A3A7A", head="Our Citizenship Is in Heaven", art_h=280),
    # Philippians 4 — stand fast; rejoice; the peace of God; the gift
    D(lp("4:1-3"), art(A2.euodia_syntyche, "es1", 5401), "#E8D8B0", head="Of the Same Mind", sky=4, art_h=260),
    F(lp("4:4-5"), PAUL_JOY, bg=JOY_BG),
    D(lp("4:6-7"), art(A2.peace_guard, "pg2", 5406), "#05051A", head="The Peace of God", art_h=270),
    D(lp("4:8-9"), art(A2.whatsoever), "#0B1A2E", head="Think on These Things", art_h=290),
    D(lp("4:10-12"), art(A2.want_plenty, "wp1", 5410), "#4A4E5E", head="Content", art_h=250),
    F(lp("4:13-14"), PAUL_JOY, bg=JOY_BG),
    D(lp("4:15-17"), art(A2.macedonia_gifts), "#0B1A2E", art_h=250),
    D(lp("4:18-20"), art(A2.the_gift, "tg1", 5418), "#D8C8A8", head="An Odor of a Sweet Smell", art_h=260),
    D(lp("4:21-22"), art(A2.caesars_household, "ch1", 5421), "#2A2A5A", head="Cæsar's Household", art_h=440),
    glory([lt("4:23")], h=330),
]
PG.extend(K.pack(SEGS, "PHP-C02-D", PG.next(), end=fin("END OF PHILIPPIANS · NEXT · COLOSSIANS"), lone=3, most=2))
