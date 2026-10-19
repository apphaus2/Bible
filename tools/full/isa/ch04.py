"""Isaiah volume, Chapter 4 — How Art Thou Fallen (Isaiah 13–16). Every verse, word for word from ref/asv.
The burden of Babylon (the map, Babylon lit; the Medes coming): the day of Jehovah, the sun darkened; 13:15–16 told in words
only, over sheep scattered on the plain; Babylon never inhabited, the beasts of the desert in her palaces; the parable
against the king of Babylon — the cedars rejoice, Sheol's thrones (pale shapes, no faces), how art thou fallen from heaven,
O day-star; the sepulchre empty and the crown on the stones (14:19–21 words only); the porcupine and the besom; the Assyrian
broken; the burden of Philistia (the fiery flying serpent as a plate); the burden of Moab — a map of its towns, mourners on
the housetops, the waters of Dimon at sunset, the vine of Sibmah, my heart soundeth like a harp."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art4 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, KING_BABYLON, COLD, GOLDEN, RED)
from isa import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
NIGHTC = "#0B0B2A"


@P("ISA-C04-00-Title", "Chapter 4 · How Art Thou Fallen", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 0)">{K.day_star(760, 1080, 401)}</g>')
    return chapter_title(4, "第四話", "How Art Thou Fallen", "Isaiah 13 – 16", svg, NIGHTC, v("14:12", to="son of the morning!"), "Isaiah · Volume Twenty-Three")


BABYLON = A(lambda w, h: K.nations_map(w, h, hi=("BABYLON",), arrows=(("MEDIA", "BABYLON"), ("ELAM", "BABYLON")), show=["BABYLON", "MEDIA", "ELAM", "NINEVEH", "JERUSALEM", "DAMASCUS", "EGYPT"]), MAP)
SEGS = (
    S("13:1-5", "god", [BABYLON, ISAIAH_STERN], kinds={1: "cap", 4: "say", 5: "say"}, head="The Burden of Babylon", split=[4])
    + S("13:6-10", "say", [ISAIAH_STERN, A(lambda w, h: K.dark_sun("ds4", w, h, 402), "#1A0A0A")], split=[9], head="The Day of Jehovah")
    + S("13:11-13", "god", ISAIAH_STERN)
    + S("13:14-16", "say", A(lambda w, h: K.scattered(w, h, 403), "#5A4A5A"))
    + S("13:17-18", "god", A(lambda w, h: K.medes("md4", w, h, 404), "#C86A3A"))
    + S("13:19-22", "say", [A(lambda w, h: K.babylon_ruins(w, h, 405), "#A87A5A"), ISAIAH_GRIEF], head="Babylon, the Glory of Kingdoms", budget=700)
    + S("14:1-2", "say", ISAIAH_JOY)
    + [face([caps("14:3"), cp("14:4", to="and say,"), sg("14:4", frm="How hath")], "ISA 14:3–4", ISAIAH, head="The Parable against the King of Babylon")]
    + S("14:5-8", "song", A(lambda w, h: K.cedars(w, h, 406), "#8FB8E0"), budget=600)
    + S("14:9-11", "song", A(lambda w, h: K.sheol_thrones(w, h, 407), "#0A0812"), budget=600)
    + S("14:12", "song", A(lambda w, h: K.day_star(w, h, 408), NIGHTC), head="How Art Thou Fallen from Heaven")
    + [face([cp("14:13", to="And thou saidst in thy heart,"), say("14:13", frm="I will ascend"), says("14:14")], "ISA 14:13–14", KING_BABYLON)]
    + S("14:15-17", "song", A(lambda w, h: K.day_star(w, h, 409, mount=True), NIGHTC))
    + S("14:18-21", "song", A(lambda w, h: K.cast_out(w, h, 410), "#3A2A3A"), budget=700)
    + S("14:22-23", "god", A(lambda w, h: K.babylon_ruins(w, h, 411, pools=True), "#A87A5A"))
    + S("14:24-27", "god", [ISAIAH_STERN, ISAIAH], pre=("cap", "Jehovah of hosts hath sworn, saying,"), kinds={26: "say", 27: "say"}, split=[26])
    + S("14:28-32", "god", [A(lambda w, h: K.serpents_root(w, h, 412), MAP), ISAIAH_STERN], kinds={28: "cap", 31: "say", 32: "say"}, head="The Burden of Philistia", split=[30])
    + S("15:1-4", "say", [A(lambda w, h: K.moab_map(w, h, hi=("AR", "KIR", "DIBON", "NEBO", "MEDEBA", "HESHBON", "ELEALEH", "JAHAZ")), MAP), A(lambda w, h: K.housetops("ht4", w, h, 413), "#4A3A5A")],
        pre=("cap", "The burden of Moab."), head="The Burden of Moab", split=[3])
    + S("15:5-9", "say", [ISAIAH_GRIEF, A(lambda w, h: K.moab_map(w, h, hi=("ZOAR", "LUHITH", "HORONAIM", "EGLAIM", "BEER-ELIM")), MAP, h=330)], at={9: A(lambda w, h: K.dimon("dm4", w, h, 414), "#5A1A1A")}, split=[8])
    + S("16:1-2", "say", [A(lambda w, h: K.lambs_selah("ls4", w, h, 415), "#C8A880"), A(lambda w, h: K.arnon_fords(w, h, 416), "#8FB0C8")], split=[2])
    + S("16:3-5", "say", [ISAIAH, A(lambda w, h: K.tent_throne("tt4", w, h, 417), "#8FB0D8")], split=[5])
    + S("16:6-8", "say", [ISAIAH_GRIEF, A(lambda w, h: K.sibmah(w, h, 418), "#A88A6A")], split=[8], head="The Vine of Sibmah")
    + S("16:9-12", "say", [ISAIAH_GRIEF, A(lambda w, h: K.harp_lament(w, h, 419), "#2A2040")], split=[11])
    + [face([caps("16:13"), cp("16:14", to="saying,"), gd("16:14", frm="Within three years")], "ISA 16:13–14", ISAIAH_STERN)]
)
PG.extend(pack(SEGS, "ISA-C04-D", PG.next(), end=end_mark("NEXT · THE BURDEN OF EGYPT", "right: 10px; bottom: 34px")))
