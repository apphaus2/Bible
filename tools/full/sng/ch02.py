"""Song of Solomon volume, Chapter 2 — A Garden Shut Up (Song of Solomon 3–5). Every verse, word for word from ref/asv.
By night on my bed (the city at night, the watchmen with torches, the bride small in the street); the roes and hinds again;
the litter of Solomon coming up from the wilderness like pillars of smoke, threescore mighty men about it; the palanquin as a
blueprint with its silver, gold and purple; the king crowned and the daughters of Zion; then the beloved's likenesses as
plates of cells only — doves behind a veil, the goats on Gilead, the ewes from the washing, the scarlet thread and the
pomegranate, the tower of David hung with shields, twin fawns among the lilies; the mountain of myrrh; Lebanon, Amana, Senir
and Hermon with the lions' dens and the leopards; honey and milk; a garden shut up and a fountain sealed; the spices as nine
cells; the north and south winds; the door by night and the myrrh on the bolt; the keepers of the walls (5:7 words over the
wall and a mantle in the street); and the beloved described as gold, a raven, doves by the brooks, spices, lilies, rings,
ivory, marble pillars and the cedars of Lebanon."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from discourse import seg
from sng import G, art as K
from sng.common import (paged, face, drawn, sg, sgs, BRIDE, BRIDE_GLAD, BRIDE_NIGHT, BRIDE_SAD, BELOVED, BELOVED_NIGHT, DAUGHTER, DAUGHTER2,
                        COLD, GOLDEN, DUSK, ROSE, LEAF)
from sng import ch01 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#0B0B2A"


@P("SNG-C02-00-Title", "Chapter 2 · A Garden Shut Up", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 260)">{K.garden_shut(760, 820, 201)}</g>')
    return chapter_title(2, "第二話", "A Garden Shut Up", "Song of Solomon 3 – 5", svg, "#4A7A5A", v("4:12", to="my bride;"), "Song of Solomon · Volume Twenty-Two")


PAGE = [[face("3:1-2", BRIDE_NIGHT, bg=COLD, head="By Night on My Bed", stamp=3),
         drawn("3:3-4", lambda w, h: K.night_streets("ns2", w, h, 202), NIGHT)],
        [drawn("3:5", lambda w, h: K.roes_field(w, h, 203), "#6A5A8A"),
         drawn("3:6-8", lambda w, h: K.litter("lt2", w, h, 204), "#E8A06A", head="The Litter of Solomon")],
        [drawn("3:9-10", lambda w, h: K.palanquin(w, h), "#0B1A2E"),
         drawn("3:11", lambda w, h: K.crowned("cr2", w, h, 205), "#8FD0E2")],
        [drawn("4:1-2", lambda w, h: K.likeness(w, h, ["dove_veil", "gilead", "ewes"]), "#1A1430", head="Thou Art Fair, My Love", stamp=4),
         drawn("4:3-5", lambda w, h: K.likeness(w, h, ["scarlet", "tower", "fawns"]), "#1A1430")],
        [drawn("4:6-7", lambda w, h: K.myrrh_hill(w, h, 206), "#5A4A7A"),
         drawn("4:8", lambda w, h: K.lebanon_peaks(w, h, 207), "#8FB8D8")],
        [drawn("4:9-11", lambda w, h: K.honey_milk(w, h, 208), "#5A3A2A"),
         drawn("4:12-15", lambda w, h: K.garden_shut(w, h, 209), "#8FD0E2", head="A Garden Shut Up")],
        [seg([], "SONG 4:13–14", art=lambda w, h: K.spices(w, h), bg="#1A1430", h=380),
         drawn("4:16", lambda w, h: K.winds_garden("wg2", w, h, 210), "#8FD0E2")],
        [face("5:1", BELOVED, head="I Am Come into My Garden", stamp=5),
         drawn("5:2-3", lambda w, h: K.door_night(w, h, 211), "#2A2238", lines=[sg("5:2", to="saying,"), sg("5:2", frm="Open to me"), sg("5:3")])],
        [face("5:4-6", BRIDE_NIGHT, bg=COLD),
         drawn("5:7-8", lambda w, h: K.walls_night("wn2", w, h, 212), NIGHT)],
        [face("5:9", DAUGHTER, bg=ROSE, head="My Beloved Is White and Ruddy"),
         drawn("5:10-13", lambda w, h: K.likeness(w, h, ["gold", "raven", "doves_brook", "spice_bed", "lily_myrrh"]), "#1A1430")],
        [drawn("5:14-16", lambda w, h: K.plate(w, h, [(K.CELL[k], "") for k in ("rings", "ivory", "marble", "cedars")], cols=2), "#1A1430")]]
PG.extend(paged(PAGE, "SNG-C02-", PG.next(), end=end_mark("NEXT · LOVE IS STRONG AS DEATH", "right: 10px; bottom: 34px")))
