"""2 Thessalonians volume, Chapter 1 — Stand Fast (2 Thessalonians 1–3). Every verse, word for word from ref/eng-asv.
2 Thessalonians 1: the study at Corinth, Paul dictating, Timothy writing, Silvanus by (1:1–2); Paul in white light giving
thanks (1:3–4); the balance of righteous judgment over the city at night (1:5–6); the heavens opened in white light and
flaming fire over an empty plain (1:7–10: no figure in the light, the angels not drawn, the vengeance in words only); Paul
beside his face (1:11–12). 2 Thessalonians 2: a stranger at Jason's door with a letter "as from us" (2:1–2); the empty seat
in the dark temple (2:3–4: the man of sin never drawn); Paul teaching in Jason's house (2:5–7); the light breaking into the
sanctuary, the seat thrown down (2:8–12: words only of the lawless one and of Satan); Paul in white light (2:13–14); the
first epistle open and the second sealed (2:15); the benediction over the light (2:16–17). 2 Thessalonians 3: a messenger on
the road with the sealed roll (3:1–2); Paul beside his face (3:3–5); Paul and Silvanus at the tent-cloth by night (3:6–9);
the worker at his own bread and the idle man at the door (3:10–12); Paul beside his face (3:13–15); the peace over the light
(3:16); Paul's own hand (3:17); the grace (3:18)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from th2 import G, art as A
from th2.common import K, Pages, paged, D, F, glory, lt, lp, v, title, fin, PAUL, PAUL_JOY, JOY_BG

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2TH-C01-00-Title", "Chapter 1 · Stand Fast", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2418"></rect><g transform="translate(0 300)">{A.study_thess("t01", 760, 640, 5311, stage="read", fig_h=400)}</g>'
    return title(1, "Stand Fast", "2 Thessalonians 1–3", svg, "#3A2418", v("2:15", to="hold the traditions"))


S = [
    # 2 Thessalonians 1 — your faith groweth; the Lord revealed in flaming fire
    [D(lp("1:1-2"), lambda w, h: A.study_thess("sb1", w, h, 5321), "#3A2418", head="Paul, and Silvanus, and Timothy", sky=1, art_h=300),
     F(lp("1:3-4"), PAUL_JOY, bg=JOY_BG)],
    [D(lp("1:5-6"), lambda w, h: A.judgment_balance(w, h, 5325), "#0B0B2A", head="The Righteous Judgment of God", art_h=220),
     D(lp("1:7-10"), lambda w, h: A.flaming_fire(w, h, 5327), "#5A1A1A", head="In Flaming Fire", art_h=300)],
    [F(lp("1:11-12"), PAUL),
     # 2 Thessalonians 2 — the day of the Lord not yet; the falling away
     D(lp("2:1-2"), lambda w, h: A.letter_as_from_us("lf1", w, h, 5331), "#4A3A34", head="Be Not Quickly Shaken", sky=2, art_h=280)],
    [D(lp("2:3-4"), lambda w, h: A.empty_seat(w, h, 5333), "#1A1018", head="The Falling Away", art_h=260),
     D(lp("2:5-7"), lambda w, h: A.teaching("tg1", w, h, 5335), "#5A4232", head="When I Was Yet with You", art_h=240)],
    [D(lp("2:8-12"), lambda w, h: A.light_breaks(w, h, 5338), "#1A1018", head="The Breath of His Mouth", art_h=260),
     F(lp("2:13-14"), PAUL_JOY, bg=JOY_BG)],
    [D([lt("2:15")], lambda w, h: A.traditions(w, h, 5345), "#3A2418", head="Stand Fast", art_h=220),
     glory(lp("2:16-17")),
     # 2 Thessalonians 3 — pray for us; the disorderly; his own hand
     D(lp("3:1-2"), lambda w, h: A.word_runs("wr1", w, h, 5351), "#6AB0D8", head="That the Word of the Lord May Run", sky=3, art_h=240)],
    [F(lp("3:3-5"), PAUL),
     D(lp("3:6-9"), lambda w, h: A.night_toil("nt1", w, h, 5356), "#3A2E2E", head="Working Night and Day", art_h=260)],
    [D(lp("3:10-12"), lambda w, h: A.work_bread("wb1", w, h, 5360), "#8A6A4A", head="Neither Let Him Eat", art_h=280),
     F(lp("3:13-15"), PAUL)],
    [glory([lt("3:16")], flex=120),
     D([lt("3:17")], lambda w, h: A.own_hand(w, h, 5367), "#4A2E1E", head="With Mine Own Hand", art_h=380),
     glory([lt("3:18")], seed=2, flex=80)],
]
PG.extend(paged(K, S, "2TH-C01-D", PG.next(), end=fin("END OF 2 THESSALONIANS · NEXT · 1 TIMOTHY")))
