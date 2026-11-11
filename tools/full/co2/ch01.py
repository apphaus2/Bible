"""2 Corinthians volume, Chapter 1 — Treasure in Earthen Vessels (2 Corinthians 1–5). Every verse, word for word from
ref/eng-asv. The letter written in Macedonia by lamplight, Paul dictating and Timothy writing (1:1), and its road from
Philippi to Corinth; the God of all comfort beside Paul's face; the affliction in Asia as words over the empty road and its
tombs (1:8–10); the journey purposed on the map (1:15–16); the seal and the earnest (1:22); the letter written with many
tears (2:4); the man forgiven and taken back at the door (2:7–8; Satan, 2:11, words only); the open door at Troas (2:12);
the triumph and the savour of incense (2:14–16). Then 3: the epistle written in hearts of flesh (a plate); Moses' shining
face and the veil; the mirror and the veil laid aside. 4: the veiled town (the god of this world, words only); light out of
darkness, God's word in the Voice box; the treasure in earthen vessels and the four cells of 4:8–9; the psalm of 4:13 in a
song box; the things seen and not seen. 5: the tent struck and the house not made with hands; the judgment-seat in the
light; the stone rolled back (5:15); a new creature at dawn; the light over the nations; the ambassador's seal."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from co2 import G, art as A
from co2.common import (K, Pages, D, F, lt, lp, lps, sg, gd, v, title, nxt, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GOLD_BG, LAMP_BG,
                        GRIEF_BG, JOY_BG, STERN_BG)

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2CO-C01-00-Title", "Chapter 1 · Treasure in Earthen Vessels", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#1E1418"></rect><g transform="translate(0 300)">{A.earthen_vessel(760, 700, 1401)}</g>'
    return title(1, "Treasure in Earthen Vessels", "2 Corinthians 1–5", svg, "#1E1418", v("4:7", frm="we have this treasure", to="earthen vessels"))


def st(p, seed, **k): return lambda w, h: A.study2(p, w, h, seed, **k)

SEGS = [
    # 2 Corinthians 1 — the letter written in Macedonia
    D([lt("1:1")], st("st1", 1101), "#3A2418", head="Paul, an Apostle, and Timothy", sky=1, art_h=300),
    D([lt("1:2")], lambda w, h: A.letter_to_corinth(w, h), "#0B1A2E", art_h=280),
    F(lp("1:3-7"), PAUL_LAMP, bg=LAMP_BG),
    D(lp("1:8-10"), lambda w, h: A.asia_road(w, h, 1108), "#1E1430", head="The Sentence of Death", art_h=210),
    F(lp("1:11-14"), PAUL),
    D(lp("1:15-16"), lambda w, h: A.purposed(w, h), "#0B1A2E", head="Yea and Nay", art_h=260),
    F(lp("1:17-20"), PAUL_STERN, bg=STERN_BG),
    D(lp("1:21-22"), lambda w, h: A.seal_earnest(w, h), "#0B1A2E", head="Sealed", art_h=220),
    F(lps("1:23-24", "2:1-2"), PAUL_GRIEF, bg=GRIEF_BG),
    # 2 Corinthians 2
    D(lp("2:3-4"), lambda w, h: A.tear_stained(w, h, 1203), "#3A2418", head="With Many Tears", sky=2, art_h=210),
    D(lp("2:5-8"), lambda w, h: A.welcomed("wc1", w, h, 1205), "#C8A878", head="Forgive Him and Comfort Him", art_h=230),
    F(lp("2:9-11"), PAUL_STERN, bg=STERN_BG),
    D(lp("2:12-13"), lambda w, h: A.troas_door("td1", w, h, 1212), "#4A3A30", head="A Door Opened at Troas", art_h=250),
    D(lp("2:14-17"), lambda w, h: A.triumph("tr1", w, h, 1214), "#5AB0D8", head="Led in Triumph", art_h=230),
    # 2 Corinthians 3
    D(lp("3:1-3"), lambda w, h: A.hearts_of_flesh(w, h), "#0B1A2E", head="Ye Are Our Epistle", sky=3, art_h=230),
    F(lp("3:4-6"), PAUL),
    D(lp("3:7-8"), lambda w, h: A.moses_shining("ms1", w, h, 1307), "#3A2A5A", head="The Glory of His Face", art_h=250),
    F(lp("3:9-12"), PAUL_JOY, bg=JOY_BG),
    D(lp("3:13-15"), lambda w, h: A.moses_veiled(w, h, 1313), "#2A2A3A", head="A Veil upon His Face", art_h=250),
    D(lp("3:16-18"), lambda w, h: A.mirror(w, h, 1316), "#C8904A", head="From Glory to Glory", art_h=220),
    # 2 Corinthians 4
    D(lp("4:1-2"), st("st2", 1401, stage="read"), "#3A2418", head="We Faint Not", sky=4, art_h=260),
    D(lp("4:3-4"), lambda w, h: A.veiled_city(w, h, 1403), "#05050E", art_h=200),
    D([lt("4:5"), lt("4:6", to="that said,"), gd("4:6", frm="Light shall shine", to="out of darkness,"), lt("4:6", frm="who shined")],
      lambda w, h: A.first_light(w, h, 1406), "#05050E", head="Light out of Darkness", art_h=210),
    D([lt("4:7")], lambda w, h: A.earthen_vessel(w, h, 1407), "#1E1418", head="Treasure in Earthen Vessels", art_h=280),
    D(lp("4:8-9"), lambda w, h: A.four_cells(w, h), "#0B1A2E", h=520),
    F(lp("4:10-12"), PAUL_GRIEF, bg=GRIEF_BG),
    D([lt("4:13", to="which is written,"), sg("4:13", frm="I believed,", to="did I speak;"), lt("4:13", frm="we also believe,")] + lp("4:14-15"),
      lambda w, h: A.preaching("pr1", w, h, 1413), "#D8C098", head="Therefore Also We Speak", art_h=220),
    D(lp("4:16-18"), lambda w, h: A.seen_unseen(w, h, 1416), "#0B0B2A", head="Things Not Seen", art_h=260),
    # 2 Corinthians 5
    D(lp("5:1-3"), lambda w, h: A.tent_house(w, h), "#0B1A2E", head="A House Not Made with Hands", sky=5, art_h=300),
    F(lp("5:4-5"), PAUL),
    F(lp("5:6-9"), PAUL_JOY, bg=JOY_BG),
    D([lt("5:10")], lambda w, h: A.bema_light(w, h, 1510), "#1A1440", head="The Judgment-Seat of Christ", art_h=240),
    F(lp("5:11-13"), PAUL_STERN, bg=STERN_BG),
    D(lp("5:14-16"), lambda w, h: A.stone_back("sb1", w, h, 1514, women=False), "#2A2A5A", head="The Love of Christ Constraineth Us", art_h=230),
    D([lt("5:17")], lambda w, h: A.new_creature(w, h, 1517), "#2A2A5A", head="A New Creature", art_h=260),
    D(lp("5:18-19"), lambda w, h: A.light_gentiles("lg1", w, h, 1518), "#2A2A5A", art_h=220),
    D([lt("5:20")], lambda w, h: A.ambassador(w, h), "#0B1A2E", head="Ambassadors on Behalf of Christ", art_h=240),
    F([lt("5:21")], PAUL_JOY, bg=JOY_BG),
]
PG.extend(K.pack(SEGS, "2CO-C01-D", PG.next(), end=nxt("NEXT · GOD LOVETH A CHEERFUL GIVER")))
