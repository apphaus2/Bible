"""Ezekiel volume, Chapter 5 — The Vine and the Foundling (Ezekiel 15–16). Every verse, word for word from ref/asv.
The vine-wood, meet for no work, cast into the fire; then Jerusalem the foundling, told with restraint — the words only,
over things and places, never a figure: the empty field at dawn; the broidered work and the ornaments laid out; the high
places decked with colours and the lofty place at the head of every way; the lovers as a map (Egypt, Assyria, Chaldea); the
judgment words over the city besieged and burned; Samaria and Sodom, thy sisters, as a map; and the everlasting covenant as
dawn over the city."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art5 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF,
                        AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch04 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("EZK-C05-00-Title", "Chapter 5 · The Vine and the Foundling", title=True)
def title(n):
    svg = title_art(lambda w, h: K.vine_fire(w, h, 501), "#1A0A0A")
    return chapter_title(5, "第五話", "The Vine and the Foundling", "Ezekiel 15 – 16", svg, "#1A0A0A", v("16:60"), "Ezekiel · Volume Twenty-Six")


SEGS = run(15, 1, 8, arts={2: ("#1A0A0A", lambda w, h: K.vine_fire(w, h, 502)), 7: ("#3A3A4A", lambda w, h: K.mountains(w, h, 503, "desolate"))}, faces=FZ,
           head="The Vine-Tree", budget=560)
SEGS += run(16, 1, 63, arts={4: ("#3A3A6A", lambda w, h: K.open_field(w, h, 504)), 10: ("#2A1A3A", lambda w, h: K.ornaments(w, h, 505)),
                             16: ("#4A3A6A", lambda w, h: K.high_places(w, h, 506)), 20: ("#3A3A4A", lambda w, h: K.mountains(w, h, 507, "broken")),
                             24: ("#4A3A6A", lambda w, h: K.high_places(w, h, 508, lofty=True)), 26: (MAP, lambda w, h: K.lovers_map(w, h)),
                             37: ("#5A4A5A", lambda w, h: K.jerusalem("j5a", w, h, 509, mode="siege")), 41: ("#2A0A0A", lambda w, h: K.jerusalem("j5b", w, h, 510, mode="burning")),
                             46: (MAP, lambda w, h: K.sisters_map(w, h)), 53: ("#6A6A7A", lambda w, h: K.jerusalem("j5c", w, h, 511, mode="empty")),
                             60: ("#6AB0D8", lambda w, h: K.covenant_dawn(w, h, 512))},
            faces=FZ + [(EZEKIEL_GRIEF, COLD)], generic=[("#2A1A3A", lambda w, h: K.jerusalem("j5d", w, h, 513, mode="dusk")), ("#3A3A6A", lambda w, h: K.open_field(w, h, 514))],
            heads={1: "Thy Birth and Thy Nativity", 15: "Thou Didst Trust in Thy Beauty", 23: "A Vaulted Place", 35: "I Will Judge Thee", 44: "As Is the Mother, So Is Her Daughter",
                   59: "An Everlasting Covenant"})
PG.extend(pack(SEGS, "EZK-C05-D", PG.next(), end=end_mark("NEXT · THE EAGLES AND THE CEDAR", "right: 10px; bottom: 34px")))
