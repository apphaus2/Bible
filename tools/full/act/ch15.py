"""Acts volume, Chapter 15 — The Shipwreck (Acts 27). Every verse, word for word from ref/eng-asv.
Julius the centurion of the Augustan band beside his face; the voyage on the map leg by leg — Sidon, the lee of Cyprus, Myra
and the ship of Alexandria, Cnidus, the lee of Crete, Fair Havens; Paul's warning on the quay; the south wind blowing softly;
Euraquilo — the ship driven under the black sky, undergirded, the freight and the tackling cast out; neither sun nor stars;
Paul standing forth in the midst, beside his face; the angel of God standing by him in the night (white light, no face);
the fourteenth night in the sea of Adria, the soundings and the four anchors; the sailors' boat cut away; the bread broken
on the deck before the dawn; the wheat cast into the sea; the bay with a beach; the foreship stuck fast where two seas met
and the stern breaking up; the soldiers' counsel told in words only; and all escaped safe to the land — on planks and on
pieces of the ship, no one drawn drowning."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art15 as A, ch14 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, DUSK, PAUL, PAUL_COLD, JULIUS, JULIUS_COLD, WHITE_LIGHT, ROBES)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C15-00-Title", "Chapter 15 · The Shipwreck", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#05050E"></rect><g transform="translate(0 260)">{A.tempest("t15", 760, 820, 2714)}</g>'
    return title(15, "The Shipwreck", "Acts 27", svg, "#14141E", v("27:25", frm="be of good cheer: for I believe God,"))


vy = A.voyage
SEGS = [F([cp("27:1"), cp("27:2")], JULIUS, head="A Centurion Named Julius"),
        D([cp("27:3"), cp("27:4"), cp("27:5"), cp("27:6")], lambda w, h: vy(w, h, legs=2, lit=[0, 1], title="ACTS 27:3–6 · SIDON AND MYRA", box=(27.0, 37.0, 32.0, 38.0)),
          "#0B1A2E", art_h=260, sky=(27, "left")),
        D([cp("27:7"), cp("27:8")], lambda w, h: vy(w, h, legs=5, lit=[2, 3, 4], title="ACTS 27:7–8 · UNDER THE LEE OF CRETE", box=(22.0, 31.0, 33.6, 38.4)), "#0B1A2E", art_h=260),
        D([cp("27:9"), cp("27:10", to="and said unto them,"), sy("27:10", frm="Sirs, I perceive")], lambda w, h: A.harbour("hb1", w, h, 2709, warn=True), "#8FD0E2", head="Fair Havens",
          art_h=240),
        D([cp("27:11"), cp("27:12"), cp("27:13")], lambda w, h: A.harbour("hb2", w, h, 2711), "#8FD0E2", art_h=220),
        D([cp("27:14"), cp("27:15"), cp("27:16")], lambda w, h: A.tempest("tp1", w, h, 2714), "#05050E", head="Euraquilo", art_h=260),
        D([cp("27:17")], lambda w, h: A.tempest("tp2", w, h, 2717, stage="girded"), "#05050E", art_h=240),
        D([cp("27:18"), cp("27:19"), cp("27:20")], lambda w, h: A.tempest("tp3", w, h, 2718, stage="freight"), "#05050E", art_h=240),
        F([cp("27:21", to="and said,"), sy("27:21", frm="Sirs, ye should have"), sy("27:22")], PAUL_COLD, bg=COLD, head="Be of Good Cheer"),
        D([sy("27:23"), sy("27:24")], lambda w, h: A.angel_deck("ad1", w, h, 2723), "#05050E", art_h=260),
        F([sy("27:25"), sy("27:26")], PAUL),
        D([cp("27:27"), cp("27:28"), cp("27:29")], lambda w, h: A.soundings("sd1", w, h, 2727), "#05051A", head="The Fourteenth Night", art_h=240),
        D([cp("27:30"), cp("27:31", to="and to the soldiers,"), sy("27:31", frm="Except these abide"), cp("27:32")], lambda w, h: A.soundings("sd2", w, h, 2730, boat=True), "#05051A",
          art_h=240),
        D([cp("27:33", to="saying,"), sy("27:33", frm="This day is"), sy("27:34"), cp("27:35"), cp("27:36"), cp("27:37")], lambda w, h: A.bread_deck("bd1", w, h, 2733), "#3A3A5A",
          art_h=240),
        D([cp("27:38")], lambda w, h: A.bread_deck("bd2", w, h, 2738, wheat=True), "#3A3A5A", art_h=220),
        D([cp("27:39"), cp("27:40")], lambda w, h: A.aground("ag1", w, h, 2739), "#5A6A9A", head="All Escaped Safe to the Land", art_h=240),
        D([cp("27:41"), cp("27:42")], lambda w, h: A.aground("ag2", w, h, 2741, stage="aground"), "#5A6A9A", art_h=240),
        D([cp("27:43"), cp("27:44")], lambda w, h: A.aground("ag3", w, h, 2743, stage="safe"), "#5A6A9A", art_h=260)]
PG.extend(K.pack(SEGS, "ACT-C15-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · ROME")))
