"""1 Thessalonians volume, Chapter 2 — The Trump of God (1 Thessalonians 4–5). Every verse, word for word from ref/eng-asv.
1 Thessalonians 4: the study at Corinth, the letter read back to Paul (4:1–2); a plain house front by day, its door shut
(4:3–7, words only); Paul beside his face (4:8–10); a potter at his own wheel (4:11–12); the tombs at dusk (4:13–14); Paul in
white light, "we that are alive" (4:15); the shout, the voice of the archangel and the trump of God — light breaking in the
clouds with no figure in it, the trumpet's blast with no one sounding it, the tombs opened and the risen and the living
caught up toward the light (4:16–18). 1 Thessalonians 5: the dark street and the open door, as a thief in the night (5:1–3,
travail in words only); the night and the day, the watchman on the wall at dawn (5:4–7); the breastplate and the helmet as a
plate (5:8–10); Paul beside his face (5:11–15); the seven short commands as a plate (5:16–22); the benediction of 5:23–24
over the light; the letter read to the church in Jason's house and the brethren greeting one another (5:25–27); the grace
(5:28) over the light."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from th1 import G, art as A, ch01 as _prev
from th1.common import (K, Pages, paged, pic, D, F, glory, lt, lp, v, title, fin, PAUL, PAUL_LAMP, PAUL_JOY, GOLD_BG, LAMP_BG, JOY_BG)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1TH-C02-00-Title", "Chapter 2 · The Trump of God", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A6A"></rect><g transform="translate(0 300)">{A.caught_up("t02", 760, 660, 5300)}</g>'
    return title(2, "The Trump of God", "1 Thessalonians 4–5", svg, "#2A2A6A", v("4:16", frm="and the dead in Christ"))


S = [
    # 1 Thessalonians 4 — how ye ought to walk; them that fall asleep
    [D(lp("4:1-2"), lambda w, h: A.study_thess("sr1", w, h, 5301, stage="read"), "#3A2418", head="How Ye Ought to Walk", sky=4, art_h=300),
     D(lp("4:3-7"), lambda w, h: A.house_front(w, h, 5303), "#8FD0E2", head="Your Sanctification", art_h=220)],
    [D(lp("4:8-10"), lambda w, h: A.welcome("wb1", w, h, 5308), "#8FD0E2", head="Taught of God to Love One Another", art_h=200),
     D(lp("4:11-12"), lambda w, h: A.potter("pt1", w, h, 5311), "#D8C098", head="Work with Your Hands", art_h=250)],
    [D(lp("4:13-15"), lambda w, h: A.tombs_dusk(w, h, 5313), "#4A2A5A", head="Them That Fall Asleep", art_h=200),
     D(lp("4:16-18"), lambda w, h: A.caught_up("cu1", w, h, 5316), "#2A2A6A", head="Caught Up in the Clouds", art_h=400)],
    # 1 Thessalonians 5 — the day of the Lord; sons of light
    [D(lp("5:1-3"), lambda w, h: A.thief_night(w, h, 5401), "#05051A", head="As a Thief in the Night", sky=5, art_h=240),
     D(lp("5:4-7"), lambda w, h: A.night_day("nd1", w, h, 5404), "#1E1650", head="Sons of Light", art_h=260)],
    [D(lp("5:8-10"), A.armour_plate, "#0B1A2E", head="The Breastplate and the Helmet", art_h=300),
     F(lp("5:11-15"), PAUL)],
    [D(lp("5:16-22"), A.commands_plate, "#0B1A2E", head="Rejoice Always", art_h=210),
     glory(lp("5:23-24"), flex=120)],
    [D(lp("5:25-27"), lambda w, h: A.read_to_all("ra1", w, h, 5425), "#C8A878", head="A Holy Kiss", art_h=330),
     glory([lt("5:28")], seed=2, flex=80)],
]
PG.extend(paged(K, S, "1TH-C02-D", PG.next(), end=fin("END OF 1 THESSALONIANS · NEXT · 2 THESSALONIANS")))
