"""Micah volume, Chapter 2 — What Doth Jehovah Require? (Micah 5–7). Every verse, word for word from ref/asv.
The siege and the judge smitten (words over the siege forts); Beth-lehem Ephrathah, little among the thousands of Judah,
by night; the ruler feeding his flock in the strength of Jehovah (a shepherd in the light, no face); the Assyrian and the
seven shepherds (a map); dew on the grass and the young lion; horses, chariots, pillars and Asherim cut off; Jehovah's
controversy before the mountains; the way out of Egypt to Gilgal (a map); the worshipper's question at the altar and
Micah's answer beside his face; the wicked balances; sowing and not reaping; woe is me — the vintage gleaned; the thorn
hedge and the shut doors; I will look unto Jehovah; a day for building thy walls; the flock in Carmel; the nations bowed;
and the sins cast into the depths of the sea. God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, fin, vista, NIGHT
from mic import G, art as A, ch01 as _prev
from mic.common import K, cp, gd, sg, sy, gds, sgs, MICAH, MICAH_GRIEF, MICAH_STERN, MICAH_GOLD, WORSHIPPER, COLD, GOLDEN, RED, DUSK

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MIC-C02-00-Title", "Chapter 2 · What Doth Jehovah Require?", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#05051A"></rect><g transform="translate(0 280)">{A.bethlehem(760, 800, 201)}</g>'
    return title(2, "What Doth Jehovah Require?", "Micah 5 – 7", svg, "#2A2A5A", v("6:8", frm="and what doth Jehovah"), "Micah · Volume Thirty-Three")


SEGS = [K.drawn(sgs("5:1"), lambda w, h: A.siege_forts("sf1", w, h, 202), "#5A4A5A", stamp=5),
        K.drawn(gds("5:2"), lambda w, h: A.bethlehem(w, h, 203), "#05051A", head="Beth-lehem Ephrathah"),
        K.drawn(sgs("5:3-4"), lambda w, h: A.shepherd_ruler("sr1", w, h, 204), "#3A4A8A"),
        K.drawn(sgs("5:5-6"), lambda w, h: A.assyria_map(w, h, hi=("NINEVEH",)), "#0B1A2E"),
        K.drawn(sgs("5:7-9"), lambda w, h: A.dew_lion(w, h, 205), "#8FB8D8"),
        K.drawn(gds("5:10-15"), lambda w, h: A.cut_off(w, h, 206), "#5A3A3A")]
PG.extend(K.pack(SEGS, "MIC-C02-D", PG.next()))
SEGS2 = [K.drawn([cp("6:1", to="what Jehovah saith:"), gd("6:1", frm="Arise,"), sg("6:2")], lambda w, h: A.mountains_hear(w, h, 207), "#14142E", head="Jehovah's Controversy", stamp=6),
         K.drawn(gds("6:3-5"), lambda w, h: A.exodus_route(w, h), "#0B1A2E"),
         K.face(sgs("6:6-7"), WORSHIPPER, bg=DUSK),
         K.drawn([], lambda w, h: A.offerings("of1", w, h, 208), "#6A4A3A", h=260),
         K.face(sgs("6:8"), MICAH_GOLD, head="What Doth Jehovah Require of Thee?"),
         K.drawn([sg("6:9"), *gds("6:10-12")], lambda w, h: A.balances(w, h, 209), "#2A2A3A"),
         K.drawn(gds("6:13-16"), lambda w, h: A.futile(w, h, 210), "#C8A880")]
PG.extend(K.pack(SEGS2, "MIC-C02-E", PG.next()))
SEGS3 = [K.face(sgs("7:1-2"), MICAH_GRIEF, bg=COLD, head="Woe Is Me", stamp=7),
         K.drawn([], lambda w, h: A.gleaned(w, h, 211), "#2A1A3A", h=240),
         K.drawn(sgs("7:3-6"), lambda w, h: A.thorns(w, h, 212), "#2A1A2A"),
         K.face(sgs("7:7-9"), MICAH_GOLD, head="I Will Look unto Jehovah"),
         K.drawn(sgs("7:10-13"), lambda w, h: A.builders("bd1", w, h, 213), "#8FD0E2"),
         K.drawn([sg("7:14"), gd("7:15")], lambda w, h: A.carmel("cm1", w, h, 214), "#8FD0E2"),
         K.drawn(sgs("7:16-17"), lambda w, h: A.nations_bow(w, h, 215), "#2A1A3A"),
         K.drawn(sgs("7:18-20"), lambda w, h: A.depths(w, h, 216), "#2C7DA8", head="Who Is a God like unto Thee?")]
PG.extend(K.pack(SEGS3, "MIC-C02-F", PG.next(), end=fin("END OF MICAH · NEXT · NAHUM")))
