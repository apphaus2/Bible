"""James volume, Chapter 1 — Doers of the Word (James 1–5). Every verse, word for word from ref/eng-asv.
James 1: to the twelve tribes of the Dispersion on Acts' map, rings spreading from Jerusalem; count it all joy beside James'
face in white light; the surge of the sea driven by the wind; the flower of the grass under the scorching sun; the crown of
life; let no man say, I am tempted of God, beside his stern face; the Father of lights (light only) and the firstfruits; be
ye doers of the word; the man beholding his face in a mirror; the fatherless and widows visited. James 2: the rich man and
the poor man at the synagogue door; the poor chosen, beside James' stern face; the royal law as a chain, one link broken,
Leviticus' "Thou shalt love thy neighbor" in a song box; the brother and sister in want sent away with words; the demons
believe and shudder — words only, beside his stern face; Abraham offering Isaac, Genesis' "And Abraham believed God" in a
song box, the ram in the thicket; Rahab's window and the scarlet cord. James 3: the bit and the rudder; how small a fire;
every kind of beast tamed; blessing and cursing beside James' grieving face; the fountain, the fig, the olive and the vine;
the wisdom from above; sown in peace. James 4: wars and fightings as words over an empty field; "God resisteth the proud" in
a song box; draw nigh to God; judge not; the merchants and the vapor. James 5: the rusted gold and the moth-eaten robe; the
mowers' hire kept back; the husbandman and the early and latter rain; the patience of Job (Job restored at his house in Uz);
swear not; the elders anointing the sick; Elijah, the little cloud and the rain (Kings' drawing); the erring brother
brought back from the error of his way."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jas import G, art3 as A
from jas.common import (K, Pages, D, F, lt, lts, lp, ltj, lj, sg, wq, qw, v, title, fin, JAMES, JAMES_LAMP, JAMES_GRIEF, JAMES_JOY, JAMES_STERN,
                        GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG)
from gal.art import art
from job.art import uz_estate
from kg1.art import small_cloud

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JAS-C01-00-Title", "Chapter 1 · Doers of the Word", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2418"></rect><g transform="translate(0 300)">{A.study_james("t01", 760, 640, 5901, fig_h=400)}</g>'
    return title(1, "Doers of the Word", "James 1–5", svg, "#3A2418", v("1:22", to="not hearers only"))


SEGS = [
    # James 1 — trials, the word, doers
    D([lt("1:1")], A.dispersion, "#0B1A2E", head="To the Twelve Tribes", sky=1, art_h=300),
    F(lp("1:2-5"), JAMES_JOY, bg=JOY_BG, head="Count It All Joy"),
    D(lp("1:6-8"), art(A.surge, 5906), "#141826", art_h=230),
    D(lp("1:9-11"), art(A.withering, 5911), "#9AD0E8", head="The Flower of the Grass", art_h=230),
    D([lt("1:12")], art(A.crown_of_life, 5912), "#140E2A", head="The Crown of Life", art_h=250),
    F(lp("1:13-16"), JAMES_STERN, bg=STERN_BG),
    D(lp("1:17-18"), art(A.father_of_lights, 5917), "#0B0B2A", head="The Father of Lights", art_h=280),
    F(lp("1:19-22"), JAMES, head="Doers of the Word"),
    D(lp("1:23-25"), art(A.mirror_man, "mm1", 5923), "#C8B088", art_h=250),
    D(lp("1:26-27"), art(A.widows, "wd1", 5926), "#4A2A5A", head="Pure Religion", art_h=240),
    # James 2 — no respect of persons; faith and works
    D(lp("2:1-4"), art(A.synagogue_door, "sd2", 5931), "#C8B490", head="Respect of Persons", sky=2, art_h=250),
    F(lp("2:5-7"), JAMES_STERN, bg=STERN_BG),
    D([lt("2:8", to="according to the scripture,"), sg("2:8", frm="Thou shalt love", to="as thyself,"), lj(("2:8", "ye do well:", None), "2:9"), ltj("2:10-11")],
      A.chain_law, "#0B1A2E", head="The Royal Law", art_h=230),
    F(lp("2:12-14"), JAMES),
    D(lp("2:15-17"), art(A.sent_away, "sa2", 5935), "#0B0B2A", head="Faith Without Works", art_h=240),
    F(lp("2:18-20"), JAMES_STERN, bg=STERN_BG),
    D([ltj("2:21-22"), lt("2:23", to="which saith,"), sg("2:23", frm="And Abraham believed God", to="for righteousness;"), lj(("2:23", "and he was called", None), "2:24")],
      art(A.akedah, "ak2", 5941), "#3A2A6A", head="Abraham Our Father", art_h=250),
    D(lp("2:25-26"), art(A.rahab_window, "rh2", 5945), "#0B0B2A", art_h=240),
    # James 3 — the tongue; the wisdom from above
    D(lp("3:1-4"), A.bit_rudder, "#0B1A2E", head="Be Not Many Teachers", sky=3, art_h=250),
    D(lp("3:5-6"), art(A.little_fire, 5951), "#0B0B1A", head="The Tongue Is a Fire", art_h=240),
    D(lp("3:7-8"), A.tamed, "#0B1A2E", art_h=250),
    F(lp("3:9-10"), JAMES_GRIEF, bg=GRIEF_BG),
    D(lp("3:11-12"), art(A.fountain_trees, 5961), "#0B1A2E", art_h=240),
    F(lp("3:13-16"), JAMES_STERN, bg=STERN_BG, head="The Wisdom from Above"),
    D(lp("3:17-18"), art(A.sown_in_peace, "sp3", 5967), "#3A2A5A", art_h=240),
    # James 4 — wars; draw nigh; a vapor
    D(lp("4:1-3"), art(A.empty_war, 5971), "#2A1A3A", head="Whence Come Wars", sky=4, art_h=240),
    F([lt("4:4"), lt("4:5"), lt("4:6", to="the scripture saith,"), sg("4:6", frm="God resisteth")], JAMES_STERN, bg=STERN_BG),
    D(lp("4:7-10"), art(A.draw_nigh, "dn4", 5977), "#14102A", head="Draw Nigh to God", art_h=240),
    F(lp("4:11-12"), JAMES),
    D(lp("4:13-17"), art(A.vapor, "vp4", 5983), "#3A2A4A", head="What Is Your Life?", art_h=240),
    # James 5 — ye rich; patience; the prayer of faith
    D(lp("5:1-3"), art(A.rusted, 5991), "#2A1E18", head="Come Now, Ye Rich", sky=5, art_h=240),
    D(lp("5:4-6"), art(A.mowers, "mw5", 5994), "#3A2A5A", art_h=240),
    D(lp("5:7-8"), art(A.early_latter, "el5", 5997), "#5A6A8A", head="Be Patient", art_h=260),
    F(lp("5:9-10"), JAMES),
    D([lt("5:11")], art(uz_estate, "uz5", 5911), "#8FD0E2", head="The Patience of Job", art_h=240),
    F([lt("5:12")], JAMES_STERN, bg=STERN_BG),
    D(lp("5:13-15"), art(A.anointing, "an5", 5913), "#2A1A12", head="The Prayer of Faith", art_h=250),
    F([lt("5:16")], JAMES_LAMP, bg=LAMP_BG),
    D(lp("5:17-18"), art(small_cloud, "sc5", 5917, rain=True), "#2A2A3A", head="Elijah Prayed", art_h=250),
    D(lp("5:19-20"), art(A.brought_back, "bb5", 5919), "#2A1A3A", art_h=250),
]
PG.extend(K.pack(SEGS, "JAS-C01-D", PG.next(), end=fin("END OF JAMES · NEXT · 1 PETER")))
