"""Philemon volume, Chapter 1 — More Than a Servant (Philemon 1–25, the whole letter). Every verse, word for word from
ref/eng-asv. Paul a prisoner at Rome, chained to the soldier, Timothy writing and Onesimus standing by (1–3); the church in
Philemon's house at Colossæ — Philemon, Apphia and Archippus at the open door, the saints coming in (4–7); Paul the aged by
lamplight beside his face (8–9); Onesimus serving Paul in his bonds, Paul's hand on his shoulder (10–12); "without thy mind I
would do nothing" beside Paul's face (13–14); Onesimus and Tychicus on the road up the Lycus to Colossæ, "a brother beloved"
(15–16); Paul's own hand writing the pledge, "I will repay it" (17–19); the upper room made ready, "prepare me also a lodging"
(20–22); the fellow-workers with Paul at Rome — Epaphras, Mark, Aristarchus, Demas, Luke (23–24); the grace over the light."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from phm import G, art as A
from phm.common import (K, Pages, D, F, glory, lt, lp, v, title, fin, PAUL, PAUL_LAMP, PAUL_JOY, GOLD_BG, LAMP_BG, JOY_BG)
from php.art import art

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PHM-C01-00-Title", "Chapter 1 · More Than a Servant", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2E26"></rect><g transform="translate(0 300)">{A.onesimus_serves("t01", 760, 640, 5701)}</g>'
    return title(1, "More Than a Servant", "Philemon 1–25", svg, "#3A2E26", v("1:16", frm="more than a servant", to="a brother beloved,"))


SEGS = [
    D(lp("1:1-3"), art(A.prison_study, "ps1", 5711, others=(A.onesimus,)), "#3A2418", head="Paul, a Prisoner", sky=1, art_h=300),
    D(lp("1:4-7"), art(A.philemon_house, "pc1", 5714), "#8FD0E2", head="The Church in Thy House", art_h=280),
    F(lp("1:8-9"), PAUL_LAMP, bg=LAMP_BG),
    D(lp("1:10-12"), art(A.onesimus_serves, "os1", 5710), "#3A2E26", head="My Child Onesimus", art_h=280),
    F(lp("1:13-14"), PAUL),
    D(lp("1:15-16"), art(A.road_to_colossae, "rc1", 5715), "#8FD0E2", head="A Brother Beloved", art_h=280),
    D(lp("1:17-19"), art(A.own_hand, 5719, ledger=True), "#3A2418", head="Put That to Mine Account", art_h=280),
    D(lp("1:20-22"), art(A.lodging, "lg1", 5722), "#E8DCC4", head="Prepare Me Also a Lodging", art_h=270),
    D(lp("1:23-24"), art(A.fellow_workers, "fw1", 5723), "#3A2418", head="My Fellow-Workers", art_h=460),
    glory([lt("1:25")]),
]
PG.extend(K.pack(SEGS, "PHM-C01-D", PG.next(), end=fin("END OF PHILEMON · NEXT · HEBREWS"), most=2, lone=3))
