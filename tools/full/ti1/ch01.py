"""1 Timothy volume, Chapter 1 — The Good Fight of the Faith (1 Timothy 1–6). Every verse, word for word from ref/eng-asv.
1 Timothy 1: Paul writing alone in a house in Macedonia, his staff and bag by the door (1:1–2); the letter's road from
Philippi by Troas to Ephesus; Timothy at his door in Ephesus taking the sealed roll from the brother; the law not made for
a righteous man as words over a dark, empty street (1:8–11); Saul laying waste the church (Acts' night street, 1:12–14);
"Christ Jesus came into the world to save sinners" in a song box beside Paul's grieving face; the doxology over the light
(1:17); Timothy reading the charge by his lamp; faith shipwrecked, a broken hull on the rocks (1:19–20, Satan words only).
1 Timothy 2: the church on a roof praying for kings, the governor's hall on the hill; one God and one mediator as a plate;
men praying in every place; modest apparel as a plate (the ornaments worn by no one); Paul's face at 2:11–15.
1 Timothy 3: the bishop and the deacons as plates of qualifications, Paul's face between them (the devil words only); the
pillar and ground of the truth as a plate; the mystery of godliness in a song box over the light (3:16).
1 Timothy 4: doctrines of demons beside Paul's stern face (words only); every creature of God received with thanksgiving at
the table; the palæstra and the lamp; Timothy young before the elders; the hands of the presbytery laid on him.
1 Timothy 5: the church as a family; a widow indeed praying night and day; the widow enrolled as a plate of good works;
the younger widows and the household (Satan words only); the ox treading out the corn with the scripture in a song box;
the gate of the two or three witnesses; the water and the little wine.
1 Timothy 6: a bondservant at the well; Paul stern at the false teachers; food and covering; the root of all kinds of evil
as a plate; the good fight (the boxer); Christ Jesus before Pontius Pilate (John's quiet hall); the blessed and only
Potentate in light unapproachable (light alone); the rich laying up good works; Timothy guarding the sealed roll."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from ti1 import G, art2 as A
from ti1.common import (K, Pages, D, F, glory, lt, lts, lp, ltj, lj, sg, v, title, fin, PAUL, PAUL_STERN, PAUL_JOY, PAUL_GRIEF,
                        GOLD_BG, STERN_BG, JOY_BG, GRIEF_BG)
from gal.art import art
from act.art5 import laid_waste
from rom.art5 import table_guests
from co1.art2 import household, bondservant, night_street
from co1.art3 import ox_tread, boxer
from co2.art3 import witnesses
from jhn.art9 import praetorium

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1TI-C01-00-Title", "Chapter 1 · The Good Fight of the Faith", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2418"></rect><g transform="translate(0 300)">{A.timothy_reads("t01", 760, 640, 5400)}</g>'
    return title(1, "The Good Fight of the Faith", "1 Timothy 1–6", svg, "#3A2418", v("6:12", to="faith,"), size=80)


SEGS = [
    # 1 Timothy 1 — the charge at Ephesus; the chief of sinners; the good warfare
    D(lp("1:1-2"), art(A.paul_writes, "pw1", 5401), "#3A2418", head="Paul, an Apostle", sky=1, art_h=280),
    D(lp("1:3-4"), art(A.ephesus_road), "#0B1A2E", head="Tarry at Ephesus", art_h=260),
    D(lp("1:5-7"), art(A.timothy_receives, "tr1", 5405), "#D8C098", art_h=280),
    D(lp("1:8-11"), art(night_street, "ns1", 5408), "#05050E", head="The Law Is Good", art_h=200),
    D(lp("1:12-14"), art(laid_waste, "lw1", 5412), "#0B0B2A", head="A Blasphemer, and a Persecutor", art_h=220),
    F([lt("1:15", to="acceptation,"), sg("1:15", frm="that Christ Jesus", to="sinners;"), lt("1:15", frm="of whom"), lt("1:16")], PAUL_GRIEF, bg=GRIEF_BG,
      head="Of Whom I Am Chief"),
    glory([lt("1:17")]),
    D([lt("1:18")], art(A.timothy_reads, "rd1", 5418), "#3A2418", head="The Good Warfare", art_h=260),
    D(lp("1:19-20"), art(A.wreck_rocks, "wr1", 5419), "#2A3448", art_h=230),
    # 1 Timothy 2 — prayers for all men; one mediator; men and women
    D(lp("2:1-4"), art(A.prayer_kings, "pk1", 5501), "#6A8AC0", head="For Kings", sky=2, art_h=240),
    D(lp("2:5-7"), art(A.mediator, "md1"), "#0B1A2E", head="One Mediator", art_h=280),
    D([lt("2:8")], art(A.holy_hands, "hh1", 5508), "#8FD0E2", head="Lifting Up Holy Hands", art_h=240),
    D(lp("2:9-10"), art(A.apparel), A.CREAM, head="Modest Apparel", art_h=240),
    F(lp("2:11-15"), PAUL),
    # 1 Timothy 3 — the bishop and the deacons; the house of God; the mystery of godliness
    D(lp("3:1-4"), art(A.bishop_plate, "bp1"), "#0B1A2E", head="The Office of a Bishop", sky=3, art_h=260),
    F(lp("3:5-7"), PAUL_STERN, bg=STERN_BG),
    D(lp("3:8-10"), art(A.deacon_plate, "dp1"), "#0B1A2E", head="Deacons in Like Manner", art_h=260),
    F(lp("3:11-13"), PAUL),
    D(lp("3:14-15"), art(A.pillar_plate), "#0B1A2E", head="The House of God", art_h=260),
    glory([lt("3:16", to="godliness;"), sg("3:16", frm="He who was manifested")], head="The Mystery of Godliness"),
    # 1 Timothy 4 — in later times; exercise thyself unto godliness; thy youth
    F(lp("4:1-3"), PAUL_STERN, bg=STERN_BG, head="In Later Times"),
    D(lp("4:4-5"), art(table_guests, "tg1", 5604), "#3A2418", art_h=230),
    D(lp("4:6-8"), art(A.palaestra, "px1", 5606), "#3A2418", head="Exercise Thyself unto Godliness", art_h=240),
    F(lp("4:9-11"), PAUL_JOY, bg=JOY_BG),
    D(lp("4:12-13"), art(A.youth, "yo1", 5612), "#D8C098", head="Let No Man Despise Thy Youth", art_h=260),
    D([lt("4:14")], art(A.hands_laid, "hl1", 5614), "#D8C098", art_h=260),
    F(lp("4:15-16"), PAUL),
    # 1 Timothy 5 — the household of faith: elders, widows, the laborer and his hire
    D(lp("5:1-2"), art(A.family, "fm1", 5701), "#8FD0E2", head="As a Father, as Brethren", sky=5, art_h=250),
    D(lp("5:3-5"), art(A.widow_prays, "wp1", 5703), "#3E3242", head="Widows Indeed", art_h=230),
    F(lp("5:6-8"), PAUL_STERN, bg=STERN_BG),
    D(lp("5:9-10"), art(A.enrolled), A.CREAM, art_h=240),
    F(lp("5:11-13"), PAUL_STERN, bg=STERN_BG),
    D(lp("5:14-16"), art(household, "hs1", 5714), "#8FD0E2", art_h=230),
    D([lt("5:17"), lt("5:18", to="saith,"), sg("5:18", frm="Thou shalt")], art(ox_tread, "ox1", 5717), "#8FD0E2", head="Worthy of Double Honor", art_h=230),
    D(lp("5:19-21"), art(witnesses, "wt1", 5719), "#8FD0E2", head="Two or Three Witnesses", art_h=230),
    D(lp("5:22-23"), art(A.wine_cup, 5722), "#C8A878", head="A Little Wine", art_h=220),
    F(lp("5:24-25"), PAUL),
    # 1 Timothy 6 — contentment; the love of money; the good fight; the rich; the deposit
    D(lp("6:1-2"), art(bondservant, "bs1", 5801), "#8FD0E2", head="Servants under the Yoke", sky=6, art_h=230),
    F(lp("6:3-5"), PAUL_STERN, bg=STERN_BG),
    D(lp("6:6-8"), art(A.food_covering, 5806), "#C8A878", head="Godliness with Contentment", art_h=220),
    D(lp("6:9-10"), art(A.money_root), A.CREAM, art_h=260),
    D(lp("6:11-12"), art(boxer, "bx1", 5811), "#E89A5A", head="Fight the Good Fight of the Faith", art_h=240),
    D(lp("6:13-14"), art(praetorium, "pr1", 5813, stage="within"), "#3A3048", art_h=240),
    glory(lp("6:15-16"), head="The Blessed and Only Potentate"),
    D(lp("6:17-19"), art(A.rich_poor, "rp1", 5817), "#3A3038", head="Them That Are Rich", art_h=240),
    D(lp("6:20-21"), art(A.guard_deposit, "gd1", 5820), "#3A2418", head="Guard That Which Is Committed", art_h=260),
]
PG.extend(K.pack(SEGS, "1TI-C01-D", PG.next(), end=fin("END OF 1 TIMOTHY · NEXT · 2 TIMOTHY")))
