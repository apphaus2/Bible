"""Hosea volume, Chapter 3 — I Will Be as the Dew (Hosea 9–14), the last chapter of Hosea. Every verse, word for word from
ref/eng-asv. Rejoice not, O Israel (the threshing-floor and the winepress empty); the days of visitation; grapes in the
wilderness and the first-ripe fig; their glory shall fly away like a bird (9:11–16 over an empty cradle and a dried root —
nothing else drawn); wanderers among the nations; the luxuriant vine, the calves of Beth-aven carried to Assyria, the king as
foam upon the water, thistles on the altars, cover us and fall on us; sow to yourselves in righteousness, break up your
fallow ground; Beth-arbel (10:14, words over the ruins); when Israel was a child — I called my son out of Egypt, the cords
and the yoke lifted; how shall I give thee up, Ephraim?; the doves coming home; Ephraim feedeth on wind; Jacob at the heel
and at Beth-el; the balances of deceit; the lion, the leopard and the bear as emblems; O death, where are thy plagues?;
Samaria (13:16, words over the city dark); then O Israel, return — I will be as the dew unto Israel; the lily, the
olive-tree, Lebanon and the green fir-tree; and the ways of Jehovah are right."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from hos import G, art3 as K
from hos.common import L, HOSEA, HOSEA_GRIEF, HOSEA_STERN, HOSEA_WORD, COLD, GOLDEN, RED, NIGHT
from hos import ch02 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
SKY, BP, DUSK, DAWN, GREY, DRY = "#8FD0E2", "#0B2A4A", "#5A3A5A", "#9AB8D8", "#8A8A9A", "#E8C890"


@P("HOS-C03-00-Title", "Chapter 3 · I Will Be as the Dew", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 280)">{K.dew_land(760, 800, 301)}</g><rect x="0" y="0" width="760" height="282" fill="#9AB8D8"></rect>')
    return chapter_title(3, "第三話", "I Will Be as the Dew", "Hosea 9 – 14", svg, "#2A3A5A", v("14:5"), "Hosea · Volume Twenty-Eight")


c, cs, s, ss, sl, A, T, Nt, gls = L.c, L.cs, L.s, L.ss, L.sl, L.A, L.T, L.N, L.gls
hs = lambda refs: ss(refs, "hosea")

SEGS = [A([hs("9:1-4")], "9:1-4", lambda w, h: K.floor_press(w, h, 302), GREY, who="hosea", head="Rejoice Not, O Israel", stamp=9),
        A([hs("9:5-6")], "9:5-6", lambda w, h: K.nettles_tents(w, h, 303), GREY, who="hosea"),
        T([hs("9:7-9")], "9:7-9", HOSEA_GRIEF, COLD, who="hosea"),
        A([*gls("9:10")], "9:10", lambda w, h: K.grapes_wilderness(w, h, 304), DRY, head="Like Grapes in the Wilderness"),
        A([*gls("9:11-13"), hs("9:14")], "9:11-14", lambda w, h: K.cradle(w, h, 305), "#3A2E2A", who="hosea"),
        A([*gls("9:15-16")], "9:15-16", lambda w, h: K.dried_root(w, h, 306), DUSK),
        A([hs("9:17")], "9:17", lambda w, h: K.wanderers("wa3", w, h, 307), DUSK, who="hosea")]
PG.extend(L.pack(SEGS, "HOS-C03-D", PG.next()))

SEGS2 = [A([hs("10:1-2")], "10:1-2", lambda w, h: K.vine_altars(w, h, 308), SKY, who="hosea", head="A Luxuriant Vine", stamp=10),
         A([hs("10:3-4")], "10:3-4", lambda w, h: K.hemlock(w, h, 309), "#8A9AA8", who="hosea"),
         A([hs("10:5-6")], "10:5-6", lambda w, h: K.calf_carried("ca3", w, h, 310), DUSK, who="hosea"),
         A([hs("10:7")], "10:7", lambda w, h: K.foam(w, h, 311), "#3A3A5A", who="hosea"),
         A([hs("10:8")], "10:8", lambda w, h: K.thistle_altars(w, h, 312), "#C8B898", who="hosea"),
         A([*gls("10:9-11")], "10:9-11", lambda w, h: K.heifer(w, h, 313, wind=False), GREY),
         A([hs("10:12-13")], "10:12-13", lambda w, h: K.plow("pl3", w, h, 314, rain=True), GREY, who="hosea", head="Break Up Your Fallow Ground"),
         A([hs("10:14-15")], "10:14-15", lambda w, h: K.ruins(w, h, 315), "#5A4A5A", who="hosea")]
PG.extend(L.pack(SEGS2, "HOS-C03-E", PG.next()))

SEGS3 = [A([*gls("11:1-2")], "11:1-2", lambda w, h: K.child_egypt("ce3", w, h, 316), DRY, head="When Israel Was a Child", stamp=11),
         A([*gls("11:3-4")], "11:3-4", lambda w, h: K.yoke_plate(w, h), BP),
         T([*gls("11:5-7")], "11:5-7", HOSEA_GRIEF, COLD),
         T([*gls("11:8-9")], "11:8-9", HOSEA_WORD, GOLDEN, head="How Shall I Give Thee Up?"),
         A([*gls("11:10-11")], "11:10-11", lambda w, h: K.doves_home(w, h, 317), BP),
         T([*gls("11:12")], "11:12", HOSEA_STERN, RED),
         A([hs("12:1-2")], "12:1-2", lambda w, h: K.east_wind(w, h, 318), "#C8A880", who="hosea", head="Ephraim Feedeth on Wind", stamp=12),
         A([hs("12:3-6")], "12:3-6", lambda w, h: K.bethel(w, h, 319), NIGHT, who="hosea"),
         A([hs("12:7-8")], "12:7-8", lambda w, h: K.balances(w, h, 320), "#3A2A3A", who="hosea"),
         A([*gls("12:9-10")], "12:9-10", lambda w, h: K.feast_tents("ft3", w, h, 321), "#FFB04A"),
         A([*gls("12:11")], "12:11", lambda w, h: K.heaps(w, h, 322), "#8A9AA8"),
         A([hs("12:12-14")], "12:12-14", lambda w, h: K.flocks("fk3", w, h, 323), SKY, who="hosea")]
PG.extend(L.pack(SEGS3, "HOS-C03-F", PG.next()))

SEGS4 = [A([hs("13:1-3")], "13:1-3", lambda w, h: K.vanish(w, h, 324), BP, who="hosea", head="As the Morning Cloud", stamp=13),
         A([*gls("13:4-6")], "13:4-6", lambda w, h: K.wilderness(w, h, 325), DRY),
         A([*gls("13:7-8")], "13:7-8", lambda w, h: K.three_beasts(w, h, 326), K.FIELD),
         T([*gls("13:9-11")], "13:9-11", HOSEA_STERN, RED),
         A([*gls("13:12-14")], "13:12-14", lambda w, h: K.sheol_bars(w, h, 327), "#1A1A2A", head="O Death, Where Are Thy Plagues?"),
         A([hs("13:15-16")], "13:15-16", lambda w, h: K.samaria_dark(w, h, 328), "#1A1220", who="hosea"),
         A([hs("14:1-3")], "14:1-3", lambda w, h: K.return_road("rr3", w, h, 329), DAWN, who="hosea", head="O Israel, Return", stamp=14),
         A([*gls("14:4-5")], "14:4-5", lambda w, h: K.dew_land(w, h, 330), DAWN, head="I Will Be as the Dew"),
         A([*gls("14:6-7")], "14:6-7", lambda w, h: K.olive_lebanon(w, h, 331), SKY),
         A([*gls("14:8")], "14:8", lambda w, h: K.fir(w, h, 332), SKY),
         A([hs("14:9")], "14:9", lambda w, h: K.two_ways(w, h, 333), SKY, who="hosea")]
PG.extend(L.pack(SEGS4, "HOS-C03-G", PG.next(), end=end_mark("END OF HOSEA · NEXT · JOEL", "right: 10px; bottom: 34px", ch="完")))
