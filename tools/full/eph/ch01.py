"""Ephesians volume, Chapter 1 — Rich in Mercy (Ephesians 1–3). Every verse, word for word from ref/eng-asv.
The letter written in bonds: Paul in his own hired dwelling at Rome, sitting on his bench dictating, the soldier that
guarded him standing by with his spear, chained wrist to wrist, the scribe on his mat, the window on Rome (1:1); the
letter's road from Rome to Ephesus on Acts' map (1:2); every spiritual blessing in the heavenly places as light over the
heavens (1:3–6); "the mystery of his will … to sum up all things in Christ" beside Paul's face in white light (1:7–10); the
seal and the earnest as a plate (1:11–14); Paul praying in his dwelling, his hand lifted (1:15–17); "the eyes of your heart
enlightened" beside his face (1:18–19); "far above all rule" as a plate of ranks of light under the right hand, no throne
and no figure (1:20–23). Ephesians 2: "dead through your trespasses", "the prince of the powers of the air" in words over
the dark sky above the roofs of Ephesus (2:1–3); "but God, being rich in mercy" beside Paul's face in white light (2:4–7);
"his workmanship" as a craftsman's plate (2:8–10); the temple courts in plan, the Gentiles far off outside the soreg (2:11–13),
then the middle wall of partition broken down (2:14–18); the household of God, the chief corner stone, as a mason's plate
(2:19–22). Ephesians 3: "I Paul, the prisoner" over the chain lying across the open letter (3:1–4); the Gentiles fellow-heirs
beside Paul's face (3:5–7); the mystery hid for ages unrolled into the light (3:8–12); Paul bowing his knees, the guard by
him (3:13–15); the breadth and length and height and depth as a diagram (3:16–19); the doxology over the light (3:20–21)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from eph import G, art as A
from eph.common import (K, Pages, D, F, glory, lt, lts, lp, ltj, lj, sg, v, title, nxt, PAUL, PAUL_LAMP, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG,
                        JOY_BG, STERN_BG)
from eph.art import art

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("EPH-C01-00-Title", "Chapter 1 · Rich in Mercy", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2418"></rect><g transform="translate(0 300)">{A.prison("t01", 760, 640, 4911, fig_h=400)}</g>'
    return title(1, "Rich in Mercy", "Ephesians 1–3", svg, "#3A2418", v("2:4", to="rich in mercy,"))


SEGS = [
    # Ephesians 1 — every spiritual blessing; far above all rule
    D([lt("1:1")], art(A.prison, "pr1", 4901), "#3A2418", head="Paul, an Apostle", sky=1, art_h=320),
    D([lt("1:2")], art(A.eph_road), "#0B1A2E", art_h=300),
    D(lp("1:3-6"), art(A.heavenly, 4903), "#1A1440", head="Every Spiritual Blessing", art_h=260),
    F(lp("1:7-10"), PAUL_JOY, bg=JOY_BG),
    D(lp("1:11-14"), art(A.seal_earnest), "#0B1A2E", head="Sealed with the Holy Spirit of Promise", art_h=290),
    D(lp("1:15-17"), art(A.prison, "pr2", 4915, up=A.PRAY), "#3A2418", head="Making Mention of You in My Prayers", art_h=280),
    F(lp("1:18-19"), PAUL),
    D(lp("1:20-23"), art(A.far_above), "#0B1A2E", head="Far Above All Rule", art_h=380),
    # Ephesians 2 — dead through trespasses, made alive; the middle wall broken down
    D(lp("2:1-3"), art(A.air_dark, 5001), "#0A0814", head="Dead Through Your Trespasses", sky=2, art_h=250),
    F(lp("2:4-7"), PAUL_JOY, bg=JOY_BG, head="Rich in Mercy"),
    D(lp("2:8-10"), art(A.workmanship), "#0B1A2E", head="His Workmanship", art_h=300),
    D(lp("2:11-13"), art(A.temple_courts), "#0B1A2E", head="Far Off", art_h=300),
    D(lp("2:14-18"), art(A.temple_courts, broken=True), "#0B1A2E", head="The Middle Wall of Partition", art_h=290),
    D(lp("2:19-22"), art(A.masonry), "#0B1A2E", head="The Chief Corner Stone", art_h=290),
    # Ephesians 3 — the prisoner; the mystery; the love of Christ
    D(lp("3:1-4"), art(A.prisoner_still, 5101), "#3A2418", head="I Paul, the Prisoner", sky=3, art_h=330),
    F(lp("3:5-7"), PAUL),
    D(lp("3:8-12"), art(A.mystery_scroll, 5108), "#0B0B2A", head="The Unsearchable Riches of Christ", art_h=250),
    D(lp("3:13-15"), art(A.bow_knees, "bk1", 5113), "#3A2E26", head="I Bow My Knees", art_h=320),
    D(lp("3:16-19"), art(A.dimensions), "#0B1A2E", head="Breadth and Length and Height and Depth", art_h=320),
    glory(lp("3:20-21")),
]
PG.extend(K.pack(SEGS, "EPH-C01-D", PG.next(), end=nxt("NEXT · THE WHOLE ARMOR OF GOD")))
