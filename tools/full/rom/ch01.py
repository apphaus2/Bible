"""Romans volume, Chapter 1 — The Power of God unto Salvation (Romans 1–3). Every verse, word for word from ref/eng-asv.
The letter written: a house at Corinth by lamplight, Paul dictating and Tertius writing at a low table (16:22); Paul's
words to the saints in letter boxes beside his face or over the drawings; the scroll handed to Phoebe at the door
(16:1–2) for "to all that are in Rome"; the letter's road from Cenchreæ to Rome on Acts' map (1:8); Greeks and Barbarians
(1:14); the light going out from Jerusalem, to the Jew first (1:16), with Habakkuk's
word in a song box; the wrath revealed from heaven as a storm over the hills, nothing struck (1:18); creation's everlasting
power — the stars, the dawn, the sea (1:20); the images of man, bird, beast and creeping thing on their plinths (1:23); then
1:24–32 in words over the idol-temple's shut doors and its darkened, empty court (no one drawn). Romans 2: the judgment-seat
empty with the scales; the two roads; the law written in the heart as a plate; the teacher of the law and the lamp; the
outward and the inward. Romans 3: the ark of the scrolls; the psalms and prophets of 3:10–18 in song boxes over the dark
road and the open, empty sepulchre; the light over all the world; the dawn; the plate of 3:23 (fall short of the glory of
God); the mercy-seat and the light between the cherubim (3:25)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from rom import G, art as A
from rom.common import (K, Pages, D, F, lt, lts, lp, ltj, lj, sg, gd, wq, qw, v, title, nxt, PAUL, PAUL_LAMP, PAUL_STERN, PAUL_JOY, GOLD_BG, LAMP_BG,
                        STERN_BG, JOY_BG, TERTIUS_LOOK, PHOEBE_LOOK)

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ROM-C01-00-Title", "Chapter 1 · The Power of God unto Salvation", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2418"></rect><g transform="translate(0 300)">{A.study("t01", 760, 640, 101, fig_h=330)}</g>'
    return title(1, "The Power of God unto Salvation", "Romans 1–3", svg, "#3A2418", v("1:16", frm="the power of God unto salvation", to="unto salvation"))


def st(p, seed, **k): return lambda w, h: A.study(p, w, h, seed, **k)

SEGS = [
    # Romans 1 — the letter written at Corinth
    D(lp("1:1-3"), st("st1", 1101), "#3A2418", head="Paul, a Servant of Jesus Christ", sky=1, art_h=220),
    F(lp("1:4-6"), PAUL_LAMP, bg=LAMP_BG),
    D([lt("1:7")], st("st2", 1107, stage="give", bearer=PHOEBE_LOOK), "#3A2418", art_h=230),
    D([lt("1:8")], lambda w, h: A.letter_to_rome(w, h), "#0B1A2E", head="I Long to See You", art_h=280),
    F(lp("1:9-13"), PAUL),
    D(lp("1:14-15"), lambda w, h: A.debtors("db1", w, h, 1114), "#8FD0E2", head="Not Ashamed of the Gospel", art_h=200),
    D([lt("1:16"), lt("1:17", to="as it is written,"), sg("1:17", frm="But the righteous")], lambda w, h: A.jew_first(w, h), "#0B1A2E", art_h=260),
    D(lp("1:18-19"), lambda w, h: A.wrath(w, h, 1118), "#2A2A36", head="Without Excuse"),
    D([lt("1:20")], lambda w, h: A.creation(w, h, 1120), "#0B0B2A", art_h=190),
    F(lp("1:21-22"), PAUL_STERN, bg=STERN_BG),
    D([lt("1:23")], lambda w, h: A.idols(w, h, 1123), "#5A3A4A", art_h=230),
    D(lp("1:24-25"), lambda w, h: A.temple_doors(w, h, 1124), "#3A2440", head="God Gave Them Up", art_h=170),
    D(lp("1:26-27"), lambda w, h: A.dark_court(w, h, 1126), "#05050E", art_h=160),
    D(lp("1:28-31"), lambda w, h: A.shut_doors(w, h, 1128), "#1A1418", art_h=170),
    F([lt("1:32")], PAUL_STERN, bg=STERN_BG),
    # Romans 2
    D(lp("2:1-3"), lambda w, h: A.judgment_seat("js1", w, h, 1201), "#8FD0E2", head="Thou That Judgest", sky=2),
    F(lp("2:4-5"), PAUL),
    D(lp("2:6-8"), lambda w, h: A.two_roads(w, h, 1206), "#4A3A4A", head="According to His Works", art_h=190),
    F(lp("2:9-11"), PAUL_STERN, bg=STERN_BG),
    D(lp("2:12-13"), st("st3", 1212, stage="read"), "#3A2418", art_h=220),
    D(lp("2:14-16"), lambda w, h: A.law_in_hearts(w, h), "#0B1A2E", head="The Law Written in Their Hearts", art_h=220),
    D(lp("2:17-20"), lambda w, h: A.teacher("tc1", w, h, 1217), "#C8B490", head="A Light of Them in Darkness"),
    F(lp("2:21-23") + qw("2:24", "because of you,", "even as it is written."), PAUL_STERN, bg=STERN_BG),
    F(lp("2:25-27"), PAUL),
    D(lp("2:28-29"), lambda w, h: A.letter_spirit(w, h), "#0B1A2E", art_h=210),
    # Romans 3
    D(lp("3:1-2"), lambda w, h: A.oracles(w, h, 1301), "#3A2A22", head="The Oracles of God", sky=3, art_h=190),
    F([lt("3:3"), lt("3:4", to="as it is written,"), sg("3:4", frm="That thou mightest")], PAUL),
    D(lp("3:5-8"), st("st4", 1305), "#3A2418", art_h=220),
    D([lt("3:9"), lt("3:10", to="as it is written,"), sg("3:10", frm="There is none righteous")], lambda w, h: A.under_sin(w, h), "#0B1A2E", art_h=190,
      head="None Righteous"),
    D([sg("3:11"), sg("3:12")], lambda w, h: A.dark_road(w, h, 1311), "#05050E"),
    D([sg("3:13"), sg("3:14")], lambda w, h: A.open_tomb("ot1", w, h, 1313), "#0B0B2A"),
    D([sg("3:15"), sg("3:16"), sg("3:17"), sg("3:18")], lambda w, h: A.ruined_way(w, h, 1315), "#05050E"),
    D(lp("3:19-20"), lambda w, h: A.throne_light("tl1", w, h, 1319), "#2A3A7A", head="Apart from the Law"),
    D(lp("3:21-22"), lambda w, h: A.dawn(w, h, 1321), "#2A2A5A"),
    D([lt("3:23")], lambda w, h: A.fall_short(w, h), "#0B1A2E", art_h=240),
    D(lp("3:24-26"), lambda w, h: A.propitiation(w, h), "#0B1A2E", head="Justified Freely by His Grace", art_h=240),
    F(lp("3:27-31"), PAUL_JOY, bg=JOY_BG),
]
PG.extend(K.pack(SEGS, "ROM-C01-D", PG.next(), end=nxt("NEXT · JUSTIFIED BY FAITH")))
