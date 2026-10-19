"""Hosea volume, Chapter 2 — The Cake Not Turned (Hosea 4–8). Every verse, word for word from ref/asv.
Jehovah's controversy with the inhabitants of the land (the land mourning); my people are destroyed for lack of knowledge;
the high places under oaks and poplars and terebinths; Israel like a stubborn heifer; a snare at Mizpah and a net upon
Tabor (a map); blow ye the cornet in Gibeah (a map); as a moth and as rottenness; as a lion; come, and let us return unto
Jehovah (the people's words); your goodness is as a morning cloud — I desire goodness, and not sacrifice; the oven heated
by the baker and Ephraim a cake not turned; a silly dove; a deceitful bow; then set the trumpet to thy mouth, the calf of
Samaria broken in pieces, they sow the wind and reap the whirlwind, a wild ass alone, altars for sinning, and the fire upon
the cities. Jehovah's words in the Voice box; the prophet's and the people's in song boxes."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from hos import G, art2 as K
from hos.common import L, HOSEA, HOSEA_GRIEF, HOSEA_STERN, HOSEA_WORD, COLD, GOLDEN, RED, NIGHT
from hos import ch01 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
SKY, BP, DUSK, DAWN, GREY = "#8FD0E2", "#0B2A4A", "#5A3A5A", "#9AB8D8", "#8A8A9A"


@P("HOS-C02-00-Title", "Chapter 2 · The Cake Not Turned", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 280)">{K.oven(760, 800, 201, cake=True)}</g><rect x="0" y="0" width="760" height="282" fill="#3A2A22"></rect>')
    return chapter_title(2, "第二話", "The Cake Not Turned", "Hosea 4 – 8", svg, "#3A2A22", v("7:8"), "Hosea · Volume Twenty-Eight")


c, cs, s, ss, sl, A, T, Nt, gls = L.c, L.cs, L.s, L.ss, L.sl, L.A, L.T, L.N, L.gls
hs = lambda refs: ss(refs, "hosea")

SEGS = [A([hs("4:1-3")], "4:1-3", lambda w, h: K.land_mourns(w, h, 202), "#C8A880", who="hosea", head="Jehovah Hath a Controversy", stamp=4),
        T([*gls("4:4-6")], "4:4-6", HOSEA_STERN, RED, head="Destroyed for Lack of Knowledge"),
        T([*gls("4:7-10")], "4:7-10", HOSEA_GRIEF, COLD),
        A([*gls("4:11-13")], "4:11-13", lambda w, h: K.oaks("oa2", w, h, 203), DUSK),
        T([*gls("4:14")], "4:14", HOSEA_STERN, RED),
        A([hs("4:15-19")], "4:15-19", lambda w, h: K.heifer(w, h, 204), GREY, who="hosea")]
PG.extend(L.pack(SEGS, "HOS-C02-D", PG.next()))

SEGS2 = [A([*gls("5:1-3")], "5:1-3", lambda w, h: K.israel_map(w, h, ("MIZPAH", "TABOR", "SAMARIA"), icon="net", title="A SNARE AT MIZPAH · A NET UPON TABOR"), BP,
           head="Hear This, O Ye Priests", stamp=5),
         A([hs("5:4-7")], "5:4-7", lambda w, h: K.flocks("fl2", w, h, 205), SKY, who="hosea"),
         A([*gls("5:8-9")], "5:8-9", lambda w, h: K.israel_map(w, h, ("GIBEAH", "RAMAH", "BETH-AVEN"), icon="horn", title="SOUND AN ALARM"), BP),
         A([*gls("5:10-12")], "5:10-12", lambda w, h: K.moth(w, h), BP),
         A([*gls("5:13-15")], "5:13-15", lambda w, h: K.lion_field(w, h, 206), K.FIELD),
         A([ss("6:1-3", "people")], "6:1-3", lambda w, h: K.latter_rain(w, h, 207), DAWN, who="people", head="Come, and Let Us Return", stamp=6),
         A([*gls("6:4-6")], "6:4-6", lambda w, h: K.morning_cloud(w, h, 208), DAWN, head="I Desire Goodness, and Not Sacrifice"),
         T([*gls("6:7-11")], "6:7-11", HOSEA_GRIEF, COLD)]
PG.extend(L.pack(SEGS2, "HOS-C02-E", PG.next()))

SEGS3 = [T([*gls("7:1-3")], "7:1-3", HOSEA_STERN, RED, head="As an Oven Heated by the Baker", stamp=7),
         A([*gls("7:4-7")], "7:4-7", lambda w, h: K.oven(w, h, 209), "#3A2A22"),
         A([*gls("7:8-10")], "7:8-10", lambda w, h: K.oven(w, h, 210, cake=True), "#3A2A22", head="A Cake Not Turned"),
         A([*gls("7:11-12")], "7:11-12", lambda w, h: K.silly_dove(w, h, 211), BP),
         T([*gls("7:13-15")], "7:13-15", HOSEA_GRIEF, COLD),
         A([*gls("7:16")], "7:16", lambda w, h: K.bow_plate(w, h), BP)]
PG.extend(L.pack(SEGS3, "HOS-C02-F", PG.next()))

SEGS4 = [A([*gls("8:1-3")], "8:1-3", lambda w, h: K.trumpet_eagle(w, h, 212), GREY, head="Set the Trumpet to Thy Mouth", stamp=8),
         A([*gls("8:4-5")], "8:4-5", lambda w, h: K.calf_broken(w, h, 213), "#3A2A3A"),
         A([*gls("8:6")], "8:6", lambda w, h: K.calf_broken(w, h, 214, broken=True), "#3A2A3A"),
         A([*gls("8:7-8")], "8:7-8", lambda w, h: K.whirlwind_field(w, h, 215), GREY, head="They Sow the Wind"),
         A([*gls("8:9-10")], "8:9-10", lambda w, h: K.wild_ass_run(w, h, 216), "#E8C890"),
         A([*gls("8:11-12"), hs("8:13")], "8:11-13", lambda w, h: K.altars(w, h, 217), DUSK),
         A([*gls("8:14")], "8:14", lambda w, h: K.fire_cities(w, h, 218), "#2A0A0A")]
PG.extend(L.pack(SEGS4, "HOS-C02-G", PG.next(), end=end_mark("NEXT · I WILL BE AS THE DEW", "right: 10px; bottom: 34px")))
