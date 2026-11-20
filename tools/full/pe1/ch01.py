"""1 Peter volume, Chapter 1 — Living Stones (1 Peter 1–5). Every verse, word for word from ref/eng-asv.
1 Peter 1: the letter's road from Babylon (Rome) to the five provinces on Acts' map; a living hope beside Peter's face in
white light; gold proved by fire; the prophets searching and angels desiring to look into it; "Ye shall be holy; for I am
holy" in the Voice box; the lamb without blemish as an emblem; "All flesh is as grass" in a song box over the withering
grass and the abiding word. 1 Peter 2: as newborn babes; living stones built up a spiritual house; "Behold, I lay in Zion"
in the Voice box and the stone the builders rejected and the stone of stumbling in a song box, over the masonry plate; out
of darkness into his marvellous light; sojourners and pilgrims; honor the king; servants, beside Peter's grieving face;
three crosses far off (2:24); the straying sheep returned to the Shepherd. 1 Peter 3: wives and the hidden man of the heart;
Sarah and Abraham; husbands and wives at prayer; "He that would love life" in a song box; a reason of the hope; Christ put
to death in the flesh, beside Peter's face; the ark and the eight souls. 1 Peter 4: the Gentiles' revellings as words over
an empty street; hospitality; the fiery trial; the faithful Creator. 1 Peter 5: tend the flock; the crown of glory; "God
resisteth the proud" in a song box, and the adversary as a roaring lion in words only beside Peter's face; the doxology over
the light; by Silvanus from Babylon with Mark; the kiss of love."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from pe1 import G, art2 as A
from pe1.common import (K, Pages, D, F, glory, lt, lts, lp, ltj, lj, sg, gd, sj, v, title, fin, PETER_OLD, PETER_LAMP, PETER_GRIEF, PETER_JOY,
                        PETER_STERN, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG)
from gal.art import art

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1PE-C01-00-Title", "Chapter 1 · Living Stones", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2418"></rect><g transform="translate(0 300)">{A.study_babylon("t01", 760, 640, 6001, fig_h=400)}</g>'
    return title(1, "Living Stones", "1 Peter 1–5", svg, "#3A2418", v("2:9", to="a royal priesthood"))


SEGS = [
    # 1 Peter 1 — a living hope; be ye holy
    D([lt("1:1")], A.five_provinces, "#0B1A2E", head="To the Sojourners", sky=1, art_h=300),
    F(lp("1:2-5"), PETER_JOY, bg=JOY_BG, head="A Living Hope"),
    D(lp("1:6-7"), art(A.crucible, 6006), "#1E120E", head="Proved by Fire", art_h=240),
    F(lp("1:8-9"), PETER_OLD),
    D(lp("1:10-12"), art(A.prophets_search, "ps1", 6010), "#3A2A2A", head="The Prophets Sought", art_h=240),
    F(lp("1:13-15") + [lt("1:16", to="it is written,"), gd("1:16", frm="Ye shall be holy")], PETER_STERN, bg=STERN_BG, head="Be Ye Holy"),
    D(lp("1:17-19"), art(A.lamb_emblem, 6017), "#0B1A2E", head="A Lamb Without Blemish", art_h=240),
    F(lp("1:20-22") + [lj("1:23", ("1:24", None, "For,"))], PETER_JOY, bg=JOY_BG),
    D([sj(("1:24", "All flesh", None), ("1:25", None, "abideth for ever.")), lt("1:25", frm="And this is")],
      art(A.grass_word, 6024), "#9AD0E8", head="All Flesh Is as Grass", art_h=240),
    # 1 Peter 2 — living stones; a royal priesthood; the Shepherd
    D(lp("2:1-3"), art(A.mother_babe, "mb2", 6031), "#2A1A12", head="As Newborn Babes", sky=2, art_h=240),
    D(lp("2:4-5"), art(A.living_stones, "ls2", 6034), "#8FD0E2", head="Living Stones", art_h=240),
    D([lt("2:6", to="contained in scripture,"), gd("2:6", frm="Behold, I lay"), lt("2:7", to="disbelieve,"),
       sj(("2:7", "The stone which", None), ("2:8", None, "rock of offence;")), lt("2:8", frm="for they stumble")], A.corner_plate, "#0B1A2E", art_h=240),
    D(lp("2:9-10"), art(A.into_light, "il2", 6039), "#05050E", head="A Royal Priesthood", art_h=240),
    D(lp("2:11-12"), art(A.pilgrims, "pg2", 6041), "#2A1A3A", head="Sojourners and Pilgrims", art_h=240),
    F(lp("2:13-16"), PETER_OLD),
    D([lt("2:17")], A.four_honors, "#0B1A2E", head="Honor the King", art_h=240),
    F(lp("2:18-20"), PETER_GRIEF, bg=GRIEF_BG, head="Servants"),
    D(lp("2:21-24"), art(A.far_crosses, 6044), "#05050E", head="Upon the Tree", art_h=220),
    D([lt("2:25")], art(A.shepherd_return, "sr2", 6045), "#5A6A9A", art_h=250),
    # 1 Peter 3 — wives and husbands; a reason of the hope; the ark
    D(lp("3:1-4"), art(A.household, "hh3", 6051), "#D8C098", head="Ye Wives", sky=3, art_h=240),
    D(lp("3:5-6"), art(A.sarah_tent, "st3", 6055), "#3A2A5A", art_h=240),
    D([lt("3:7")], art(A.couple_prayer, "cp3", 6057), "#4A3A3A", head="Ye Husbands", art_h=240),
    F([lj("3:8", "3:9", ("3:10", None, "For,")), sj(("3:10", "He that would", None), "3:11", "3:12")], PETER_OLD),
    D(lp("3:13-17"), art(A.answer, "an3", 6063), "#8FD0E2", head="A Reason of the Hope", art_h=230),
    F(lp("3:18-19"), PETER_JOY, bg=JOY_BG),
    D(lp("3:20-22"), art(A.ark_eight, 6070), "#3A4A6A", head="Eight Souls", art_h=240),
    # 1 Peter 4 — the will of God; the fiery trial
    D(lp("4:1-3"), art(A.dark_street, 6071), "#05050E", head="The Will of God", sky=4, art_h=210),
    F(lp("4:4-6"), PETER_STERN, bg=STERN_BG),
    D(lp("4:7-9"), art(A.hospitality, "hs4", 6077), "#5A3E2E", head="The End of All Things", art_h=240),
    F(lp("4:10-11"), PETER_JOY, bg=JOY_BG),
    D(lp("4:12-14"), art(A.fiery_trial, 6082), "#1A0E0A", head="The Fiery Trial", art_h=240),
    F(lp("4:15-16"), PETER_STERN, bg=STERN_BG),
    D(lp("4:17-19"), art(A.faithful_creator, "fc4", 6087), "#2A2A5A", art_h=240),
    # 1 Peter 5 — the elders; humble yourselves; by Silvanus
    D(lp("5:1-3"), art(A.elder_flock, "ef5", 6091), "#8FD0E2", head="Tend the Flock", sky=5, art_h=240),
    D([lt("5:4")], art(A.crown_glory, 6094), "#140E2A", art_h=250),
    F([lt("5:5", to="serve one another: for"), sg("5:5", frm="God resisteth")] + lp("5:6-9"), PETER_OLD, head="Humble Yourselves"),
    glory(lp("5:10-11")),
    D(lp("5:12-13"), art(A.study_babylon, "sb5", 6102, stage="give"), "#3A2418", head="By Silvanus", art_h=280),
    D([lt("5:14")], art(A.greeting, "gr5", 6104), "#5E4A3C", art_h=250),
]
PG.extend(K.pack(SEGS, "1PE-C01-D", PG.next(), end=fin("END OF 1 PETER · NEXT · 2 PETER")))
