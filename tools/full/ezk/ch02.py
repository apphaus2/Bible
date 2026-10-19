"""Ezekiel volume, Chapter 2 — The Siege on a Tile (Ezekiel 4–7). Every verse, word for word from ref/asv.
The tile with Jerusalem portrayed, the forts, the mound and the iron pan (a plate); Ezekiel lying on his left side and his
right, each day for a year (a plate of the days); the bread of the siege by weight and the water by measure; Ah Lord
Jehovah! my soul hath not been polluted; the staff of bread broken; the hair shaven and divided in three (a plate); this is
Jerusalem, set in the midst of the nations (a map); famine, pestilence and the sword words over empty streets; the
mountains of Israel, their altars and sun-images thrown down (no slain drawn); the remnant carried among the nations; an
end is come upon the four corners of the land; the rod hath blossomed; the trumpet and none going to battle; the silver
cast in the streets; make the chain; the king shall mourn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from ezk import G, art2 as K
from ezk.common import (pack, cp, say, gd, wl, fz, dz, run, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF, EZEKIEL_TEAR, NIGHT, COLD, GOLDEN, RED)
from ezk import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("EZK-C02-00-Title", "Chapter 2 · The Siege on a Tile", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.jerusalem("t2", 760, 780, 201, mode="siege")}</g><rect x="0" y="0" width="760" height="302" fill="#5A4A5A"></rect>')
    return chapter_title(2, "第二話", "The Siege on a Tile", "Ezekiel 4 – 7", svg, "#3A2A3A", v("4:1", frm="portray upon it a city"), "Ezekiel · Volume Twenty-Six")


SEGS = [dz("4:1-3", lambda w, h: K.tile_plan(w, h), MAP, k=0.3, head="Portray upon It a City", stamp=4),
        dz("4:4-6", lambda w, h: K.days_plate(w, h), MAP, k=0.34, head="Each Day for a Year"),
        dz("4:7-8", lambda w, h: K.lying("ly2", w, h, 202), "#3A2A2A", k=0.36),
        dz("4:9-12", lambda w, h: K.ration_plate(w, h), MAP, k=0.34, head="The Bread of the Siege"),
        fz("4:13-15", EZEKIEL_GRIEF, COLD),
        dz("4:16-17", lambda w, h: K.lying("ly2b", w, h, 203, side="right", bread=True), "#3A2A2A")]
SEGS += run(5, 1, 17, arts={1: (MAP, lambda w, h: K.hair_plate(w, h)), 5: (MAP, lambda w, h: K.nations_center(w, h)),
                            9: ("#5A4A5A", lambda w, h: K.jerusalem("j2a", w, h, 204, mode="siege")), 12: ("#6A6A7A", lambda w, h: K.jerusalem("j2b", w, h, 205, mode="empty")),
                            16: ("#3A2A2A", lambda w, h: K.staff_broken(w, h, 217))}, faces=FZ,
            heads={1: "As a Barber's Razor", 5: "This Is Jerusalem", 11: "A Third Part"}, budget=620)
SEGS += run(6, 1, 14, arts={2: ("#3A2A4A", lambda w, h: K.mountains(w, h, 206, "idols")), 6: ("#3A3A4A", lambda w, h: K.mountains(w, h, 207, "broken")),
                            9: ("#5A4A5A", lambda w, h: KK2_captives(w, h)), 13: ("#3A3A4A", lambda w, h: K.mountains(w, h, 208, "broken"))}, faces=FZ,
            heads={1: "Ye Mountains of Israel", 8: "Yet Will I Leave a Remnant", 11: "Smite with Thy Hand"})
SEGS += run(7, 1, 27, arts={2: (MAP, lambda w, h: K.four_corners(w, h)), 10: ("#1A0A0A", lambda w, h: K.rod(w, h, 209)), 14: ("#4A3A4A", lambda w, h: K.trumpet_gate("tg2", w, h, 210)),
                            16: ("#8A6A5A", lambda w, h: K.doves(w, h, 211)), 19: ("#5A5A6A", lambda w, h: K.silver_street(w, h, 212)), 23: ("#2A2A3A", lambda w, h: K.chain(w, h, 213)),
                            21: ("#2A0A0A", lambda w, h: K.jerusalem("j2c", w, h, 214, mode="burning")), 27: ("#2A2A3A", lambda w, h: K.crown_dust(w, h, 215))},
            faces=FZ + [(EZEKIEL_GRIEF, COLD)], heads={1: "An End Is Come", 10: "The Rod Hath Blossomed", 14: "They Have Blown the Trumpet", 23: "Make the Chain"})


def KK2_captives(w, h):
    return K.KK2.captives("cp2", w, h, 216, city="jerusalem")


PG.extend(pack(SEGS, "EZK-C02-D", PG.next(), end=end_mark("NEXT · THE GLORY DEPARTS", "right: 10px; bottom: 34px")))
