"""Micah volume, Chapter 1 — Swords into Plowshares (Micah 1–4). Every verse, word for word from ref/asv.
The word that came to Micah (1:1 in a caption) beside his face; the mountains melting as wax (fire and storm); Samaria a
heap of the field; Micah's lament; the towns of the lowland as a technical map and the captives going; the devisers on
their beds and the boundary stone moved; the yoke and the line cast by lot; the houses emptied and the false prophet's
wine; the flock of Bozrah and the breaker; the heads of Jacob (3:2–3 words over empty judgment seats and a steaming pot);
the sun going down black on the prophets; Zion plowed as a field; then the mountain of Jehovah's house, swords beaten into
plowshares, every man under his vine and fig-tree, the remnant gathered, the tower of the flock, the daughter of Zion
going forth to Babylon, and the threshing-floor. God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, nxt, vista, NIGHT
from mic import G, art as A
from mic.common import K, cp, gd, sg, sy, gds, sgs, MICAH, MICAH_GRIEF, MICAH_STERN, MICAH_GOLD, COLD, GOLDEN, RED, DUSK

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MIC-C01-00-Title", "Chapter 1 · Swords into Plowshares", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A3A6A"></rect><g transform="translate(0 280)">{A.mountain_house(760, 800, 101)}</g>'
    return title(1, "Swords into Plowshares", "Micah 1 – 4", svg, "#2A3A6A", v("4:3", frm="nation shall not lift up"), "Micah · Volume Thirty-Three")


SEGS = [K.face([cp("1:1"), sg("1:2")], MICAH, head="The Word That Came to Micah", stamp=1),
        K.drawn(sgs("1:3-4"), lambda w, h: A.melting(w, h, 102), "#1A0A0A"),
        K.drawn([sg("1:5"), *gds("1:6-7")], lambda w, h: A.samaria_heap(w, h, 103), "#6A6A7A", head="Samaria as a Heap"),
        K.face(sgs("1:8-9"), MICAH_GRIEF, bg=COLD, head="I Will Lament and Wail"),
        K.drawn(sgs("1:10-14"), lambda w, h: A.towns_map(w, h, lit=("JERUSALEM", "LACHISH")), "#1A0A12"),
        K.drawn([gd("1:15"), sg("1:16")], lambda w, h: A.captives("cv1", w, h, 104, city="jerusalem"), "#5A4A5A")]
PG.extend(K.pack(SEGS, "MIC-C01-D", PG.next(), lone=0.5))
SEGS2 = [K.drawn(sgs("2:1-2"), lambda w, h: A.devisers(w, h, 105), "#1A1028", head="Woe to Them That Devise Iniquity", stamp=2),
         K.drawn([cp("2:3", to="thus saith Jehovah:"), gd("2:3", frm="Behold,"), *gds("2:4-5")], lambda w, h: A.yoke(w, h, 106), "#3A2A2A"),
         K.face([sg("2:6")], MICAH_STERN, bg=RED),
         K.drawn(gds("2:7-9"), lambda w, h: A.cast_out(w, h, 107), "#8A8A9A"),
         K.drawn(gds("2:10-11"), lambda w, h: A.wine_jars(w, h, 108), "#3A1A2A"),
         K.drawn([gd("2:12")], lambda w, h: A.fold("fd1", w, h, 109), "#2A2A5A", head="The Breaker Is Gone Up"),
         K.drawn([sg("2:13")], lambda w, h: A.breaker("bk1", w, h, 121), "#2A2A5A")]
PG.extend(K.pack(SEGS2, "MIC-C01-E", PG.next(), lone=0.5))
SEGS3 = [K.face([cp("3:1", to="And I said,"), sg("3:1", frm="Hear, I pray you")], MICAH_STERN, bg=RED, head="Ye Heads of Jacob", stamp=3),
         K.drawn(sgs("3:2-4"), lambda w, h: A.caldron(w, h, 110), "#1E0E10"),
         K.drawn([cp("3:5", to="Thus saith Jehovah"), gd("3:5", frm="concerning"), *gds("3:6-7")], lambda w, h: A.sun_down(w, h, 111), "#05050A"),
         K.face(sgs("3:8"), MICAH_GOLD, head="Full of Power by the Spirit of Jehovah"),
         K.drawn(sgs("3:9-11"), lambda w, h: A.balances(w, h, 112), "#2A2A3A"),
         K.drawn(sgs("3:12"), lambda w, h: A.plowed(w, h, 113), "#7A7A8A")]
PG.extend(K.pack(SEGS3, "MIC-C01-F", PG.next(), lone=0.5))
SEGS4 = [K.drawn(sgs("4:1-2"), lambda w, h: A.mountain_house(w, h, 114), "#2A3A6A", head="The Mountain of Jehovah's House", stamp=4),
         K.drawn(sgs("4:3"), lambda w, h: A.plowshares(w, h, 115), "#2A1A14"),
         K.drawn(sgs("4:4-5"), lambda w, h: A.vine_fig("vf1", w, h, 116), "#8FD0E2", head="Under His Vine and Under His Fig-tree"),
         K.drawn(gds("4:6-7"), lambda w, h: A.remnant("rm1", w, h, 117), "#2A2A5A"),
         K.drawn(sgs("4:8"), lambda w, h: A.tower_flock(w, h, 118), "#2A1A3A"),
         K.drawn(sgs("4:9-10"), lambda w, h: A.captives("cv2", w, h, 119, city="jerusalem"), "#5A4A5A", head="O Daughter of Zion"),
         K.drawn([*sgs("4:11-12"), gd("4:13")], lambda w, h: A.thresh(w, h, 120), "#FFE6A0")]
PG.extend(K.pack(SEGS4, "MIC-C01-G", PG.next(), lone=0.5, end=nxt("NEXT · WHAT DOTH JEHOVAH REQUIRE?")))
