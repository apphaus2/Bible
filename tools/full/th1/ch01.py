"""1 Thessalonians volume, Chapter 1 — Turned unto God from Idols (1 Thessalonians 1–3). Every verse, word for word from
ref/eng-asv. The letter written at Corinth: Paul dictating in the study by lamplight, Timothy on the mat writing, Silvanus
standing by (1:1); the letter's road from Corinth to Thessalonica on Acts' map; the word sounding forth from Thessalonica in
rings over Macedonia and Achaia (1:8); the household shrine left empty, the family at the door turned to the dawn (1:9–10).
1 Thessalonians 2: the empty stocks of Philippi (2:2, words only of what was done there); Paul beside his face (2:3–6); a
nurse with her own children by lamplight (2:7–8); Paul and Silvanus at the tent-cloth by night (2:9–10); Paul exhorting the
church in Jason's house (2:11–12); Paul in white light giving thanks (2:13–14); the road out by night (2:15–16, "drove out
us"); the shut gate on the road north at dusk (2:17–18, "Satan hindered us" in words only); the victor's wreath in light
(2:19–20). 1 Thessalonians 3: Paul left at Athens, Timothy setting out (3:1–2); Paul grieving beside his face (3:3–5, the
tempter in words only); Timothy come back with the church's letter at the study's door (3:6–8); Paul in white light (3:9–10);
the prayer of 3:11–13 over the light."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from th1 import G, art as A
from th1.common import (K, Pages, paged, D, F, glory, lt, lp, v, title, nxt, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG)

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1TH-C01-00-Title", "Chapter 1 · Turned unto God from Idols", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2418"></rect><g transform="translate(0 300)">{A.study_thess("t01", 760, 640, 5211, fig_h=400)}</g>'
    return title(1, "Turned unto God from Idols", "1 Thessalonians 1–3", svg, "#3A2418", v("1:9", frm="how ye turned"))


S = [
    # 1 Thessalonians 1 — the letter, and the church that turned from idols
    [D([lt("1:1")], lambda w, h: A.study_thess("sb1", w, h, 5201), "#3A2418", head="Paul, and Silvanus, and Timothy", sky=1, art_h=300),
     D(lp("1:2-4"), A.thess_road, "#0B1A2E", art_h=260)],
    [F(lp("1:5-7"), PAUL),
     D([lt("1:8")], lambda w, h: A.sounded_forth(w, h, 5208), "#3A6A8A", head="The Word Sounded Forth", art_h=250),
     D(lp("1:9-10"), lambda w, h: A.from_idols("fi1", w, h, 5209), "#C8A878", head="Turned unto God from Idols", art_h=250)],
    # 1 Thessalonians 2 — our entering in unto you
    [D(lp("2:1-2"), lambda w, h: A.philippi_stocks("ps1", w, h, 5221), "#3A3238", head="Shamefully Treated at Philippi", sky=2, art_h=220),
     F(lp("2:3-6"), PAUL_LAMP, bg=LAMP_BG)],
    [D(lp("2:7-8"), lambda w, h: A.nurse("nu1", w, h, 5227), "#6A4A3A", head="Gentle in the Midst of You", art_h=250),
     D(lp("2:9-10"), lambda w, h: A.night_toil("nt1", w, h, 5229), "#3A2E2E", head="Working Night and Day", art_h=250),
     D(lp("2:11-12"), lambda w, h: A.jason_house("jh1", w, h, 5231), "#5A4232", head="As a Father with His Own Children", art_h=250)],
    [F(lp("2:13-14"), PAUL_JOY, bg=JOY_BG),
     D(lp("2:15-16"), lambda w, h: A.drove_out("do1", w, h, 5235), "#05051A", art_h=220),
     D(lp("2:17-18"), lambda w, h: A.gate_shut("gs1", w, h, 5237), "#2A1A3A", head="Bereaved of You", art_h=230)],
    [D(lp("2:19-20"), lambda w, h: A.crown_glory(w, h, 5239), "#0B0B2A", head="Our Glory and Our Joy", art_h=240),
     # 1 Thessalonians 3 — Timothy sent, and Timothy come back
     D(lp("3:1-2"), lambda w, h: A.athens_alone("aa1", w, h, 5241), "#8FD0E2", head="Left Behind at Athens Alone", sky=3, art_h=240)],
    [F(lp("3:3-5"), PAUL_GRIEF, bg=GRIEF_BG),
     D(lp("3:6-8"), lambda w, h: A.timothy_back("tb1", w, h, 5246), "#3A2418", head="Glad Tidings", art_h=290)],
    [D(lp("3:9-10"), lambda w, h: A.night_prayer("np1", w, h, 5249), "#1E1838", head="Night and Day Praying", art_h=420),
     glory(lp("3:11-13"))],
]
PG.extend(paged(K, S, "1TH-C01-D", PG.next(), end=nxt("NEXT · THE TRUMP OF GOD")))
