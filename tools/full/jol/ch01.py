"""Joel volume, Chapter 1 — The Day of Jehovah (Joel 1–3), the whole book. Every verse, word for word from ref/asv.
The word of Jehovah to Joel; hear this, ye old men; the palmer-worm, the locust, the canker-worm and the caterpillar (a
plate); the vine laid waste and the fig-tree barked white; the priests in sackcloth; the trees of the field withered, the
barns broken down, the beasts groaning, the fire in the pastures; blow ye the trumpet in Zion — a day of darkness, a great
people as the dawn spread upon the mountains, as the appearance of horses, climbing the wall and entering at the windows
(locusts, never anything gory); the sun and the moon darkened; yet even now, rend your heart; the solemn assembly and the
priests' prayer; the northern army driven into the seas (a map); the former rain and the latter, the floors full of wheat;
I will pour out my Spirit upon all flesh (light upon old and young); blood, and fire, and pillars of smoke; the valley of
Jehoshaphat and Tyre, Sidon and Philistia (maps); beat your plowshares into swords; the sickle and the winepress;
multitudes in the valley of decision; and the mountains dropping sweet wine. Jehovah's words in the Voice box, Joel's in
his own song boxes."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jol import G, art as K
from jol.common import L, JOEL, JOEL_CRY, JOEL_GRIEF, JOEL_GLAD, COLD, GOLDEN, RED, NIGHT

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
SKY, BP, DUSK, GREY, DARK, FIRE = "#8FD0E2", "#0B2A4A", "#5A3A5A", "#8A8A9A", "#1A1220", "#3A1A1A"


@P("JOL-C01-00-Title", "Chapter 1 · The Day of Jehovah", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.zion_trumpet("t1", 760, 820, 101)}</g><rect x="0" y="0" width="760" height="262" fill="#2A2230"></rect>')
    return chapter_title(1, "第一話", "The Day of Jehovah", "Joel 1 – 3", svg, "#2A2230", v("2:1", to="in my holy mountain;"), "Joel · Volume Twenty-Nine")


c, cs, s, ss, sl, A, T, Nt, gls, cut, sp2 = L.c, L.cs, L.s, L.ss, L.sl, L.A, L.T, L.N, L.gls, L.cut, L.split
js = lambda refs: ss(refs, "joel")

SEGS = [A([c("1:1"), js("1:2-3")], "1:1-3", lambda w, h: K.joel_land("jl1", w, h, 102), GREY, who="joel", head="The Word of Jehovah", stamp=1),
        A([js("1:4")], "1:4", lambda w, h: K.locust_plate(w, h), BP, who="joel", head="The Palmer-worm and the Locust"),
        A([js("1:5-7")], "1:5-7", lambda w, h: K.bare_vine(w, h, 103), GREY, who="joel"),
        A([js("1:8-10")], "1:8-10", lambda w, h: K.priests_mourn("pm1", w, h, 104), "#5A5A6A", who="joel"),
        A([js("1:11-12")], "1:11-12", lambda w, h: K.withered(w, h, 105), "#9A9A9A", who="joel"),
        A([js("1:13-14")], "1:13-14", lambda w, h: K.priests_mourn("pm2", w, h, 106, porch=True), "#5A5A6A", who="joel"),
        A([js("1:15-17")], "1:15-17", lambda w, h: K.barns_broken(w, h, 107), GREY, who="joel", head="Alas for the Day!"),
        A([js("1:18")], "1:18", lambda w, h: K.beasts_groan(w, h, 108), "#C8A880", who="joel"),
        A([js("1:19-20")], "1:19-20", lambda w, h: K.fire_pastures(w, h, 109), FIRE, who="joel")]
PG.extend(L.pack(SEGS, "JOL-C01-D", PG.next()))

SEGS2 = [A([js("2:1-2")], "2:1-2", lambda w, h: K.zion_trumpet("zt1", w, h, 110), "#2A2230", who="joel", head="Blow Ye the Trumpet in Zion", stamp=2),
         A([js("2:3")], "2:3", lambda w, h: K.army_dawn(w, h, 111), DARK, who="joel"),
         A([js("2:4-6")], "2:4-6", lambda w, h: K.horses_plate(w, h), BP, who="joel"),
         A([js("2:7-9")], "2:7-9", lambda w, h: K.wall_locusts(w, h, 112), "#5A4A3A", who="joel"),
         A([js("2:10-11")], "2:10-11", lambda w, h: K.sky_dark(w, h, 113, quake=True), DARK, who="joel"),
         T([*gls("2:12"), js("2:13-14")], "2:12-14", JOEL, GOLDEN, who="joel", head="Rend Your Heart"),
         A([js("2:15-16"), *sp2("2:17", "and let them say,", "joel", "priests")], "2:15-17", lambda w, h: K.assembly("as1", w, h, 114), GREY, who="joel"),
         A([c("2:18"), *cut("2:19", "said unto his people,"), *gls("2:20")], "2:18-20", lambda w, h: K.army_map(w, h), BP, head="Jehovah Was Jealous for His Land"),
         A([js("2:21-23")], "2:21-23", lambda w, h: K.latter_rain(w, h, 115), "#9AB8D8", who="joel"),
         A([js("2:24"), *gls("2:25-27")], "2:24-27", lambda w, h: K.plenty(w, h, 116), SKY, who="joel"),
         A([*gls("2:28-29")], "2:28-29", lambda w, h: K.spirit("sp1", w, h, 117), "#3A3A6A", head="I Will Pour Out My Spirit"),
         A([*gls("2:30-31")], "2:30-31", lambda w, h: K.sky_dark(w, h, 118, blood=True, smoke_=True), DARK),
         T([js("2:32")], "2:32", JOEL_GLAD, GOLDEN, who="joel")]
PG.extend(L.pack(SEGS2, "JOL-C01-E", PG.next()))

SEGS3 = [A([*gls("3:1-3")], "3:1-3", lambda w, h: K.nations_map(w, h, ("JERUSALEM", "THE VALLEY OF JEHOSHAPHAT", "TYRE", "PHILISTIA", "EGYPT", "EDOM"),
                                                                 moves=[("TYRE", "THE VALLEY OF JEHOSHAPHAT"), ("PHILISTIA", "THE VALLEY OF JEHOSHAPHAT"), ("EGYPT", "THE VALLEY OF JEHOSHAPHAT"), ("EDOM", "THE VALLEY OF JEHOSHAPHAT")],
                                                                 hi=("THE VALLEY OF JEHOSHAPHAT",)), BP, head="The Valley of Jehoshaphat", stamp=3),
         A([*gls("3:4-6")], "3:4-6", lambda w, h: K.nations_map(w, h, ("TYRE", "SIDON", "PHILISTIA", "JERUSALEM", "THE GRECIANS"),
                                                                moves=[("JERUSALEM", "THE GRECIANS")], hi=("TYRE", "SIDON", "PHILISTIA")), BP),
         A([*gls("3:7-8")], "3:7-8", lambda w, h: K.nations_map(w, h, ("TYRE", "SIDON", "PHILISTIA", "JERUSALEM", "SHEBA"), moves=[("JERUSALEM", "SHEBA")], hi=("SHEBA",)), BP),
         A([*gls("3:9-11")], "3:9-11", lambda w, h: K.plowshares(w, h), BP, head="Beat Your Plowshares into Swords"),
         A([*gls("3:12-13")], "3:12-13", lambda w, h: K.sickle_press(w, h, 119), "#3A1A2A"),
         A([js("3:14-16")], "3:14-16", lambda w, h: K.valley(w, h, 120), DARK, who="joel", head="The Valley of Decision"),
         A([*gls("3:17-18")], "3:17-18", lambda w, h: K.sweet_wine(w, h, 121), SKY, head="The Mountains Shall Drop Down Sweet Wine"),
         A([*gls("3:19-21")], "3:19-21", lambda w, h: K.zion_refuge(w, h, 122), "#2A2A4A")]
PG.extend(L.pack(SEGS3, "JOL-C01-F", PG.next(), end=end_mark("END OF JOEL · NEXT · AMOS", "right: 10px; bottom: 34px", ch="完")))
