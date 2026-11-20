"""Revelation volume, Chapter 5 — Fallen Is Babylon the Great (Revelation 15–18). Every verse, word for word from ref/eng-asv.
The seven angels having the seven last plagues, in white with golden girdles; the sea of glass mingled with fire and the
victors standing by it with harps, the song of Moses and of the Lamb in song boxes; the temple of the tabernacle of the
testimony opened, the seven coming out, the seven golden bowls given by a living creature, the temple filled with smoke.
God's words — the great voice out of the temple (16:1), "It is done" from the throne (16:17), and the voice from heaven,
"Come forth, my people" (18:4–20, with the kings', merchants' and shipmasters' laments in balloons inside it) — in the Voice
box. The bowls are poured by an angel in the sky over the land, the sea turned dark crimson, the rivers, the scorching sun
over cracked earth, the darkness on the beast's empty throne, the Euphrates dried with kings far off at the sunrising, the
air with its lightnings and earthquake — no one drawn suffering; the sores, the gnawing of tongues and the blasphemies are
in the words. The unclean spirits like frogs (16:13) are demons: words only, over the kings' camps on a far plain;
Jesus' words, "Behold, I come as a thief", beside his face in light; Har-Magedon an empty plain; the great city split in
three under the hail. Babylon the great harlot: no woman is drawn — the angel and John by the many waters with the city far
off; the scarlet-coloured beast's heraldic plate with the golden cup set beside it (her name, her array and her drunkenness
are in the words only); John wondering beside his face; the seven heads, mountains and kings as a chart; the ten kings'
crowns under the Lamb in light; the waters as peoples, multitudes, nations and tongues; what the ten horns do to her is in
the words only. Her fall: an angel lightening the earth over the ruined city with its birds; her people going out at the gate
toward the light; the city lit in its pride; the kings, the merchants and the shipmasters standing afar off watching the
smoke of her burning; the merchandise as a roll plate (souls of men set apart); the strong angel casting the millstone into
the sea; the city dark, no lamp, a broken harp and a cold millstone."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from rev import G, art5 as A, ch04 as _prev
from rev.common import K, Pages, D, F, cp, gd, sg, sy, v, said, title, nxt, JESUS_RISEN, JOHN_AWE, LIGHT_BG, VISION_BG

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
K.art_k = 1.0
START, PAGES, P = PG.start, PG.pages, PG.P


@P("REV-C05-00-Title", "Chapter 5 · Fallen Is Babylon the Great", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#1A0A10"></rect><g transform="translate(0 300)">{A.babylon("t5", 760, 780, 1801, "kings")}</g>'
    return title(5, "Fallen Is Babylon the Great", "Revelation 15 – 18", svg, "#1A0A10", v("18:2", frm="Fallen, fallen is Babylon the great", to="Babylon the great,"))


B = A.bowl
SEGS = [D([cp("15:1")], lambda w, h: A.bowl_angels("ba1", w, h, 1501), "#2A1440", head="Seven Angels Having Seven Plagues", sky=15, art_h=280),
        D([cp("15:2"), *said("15:3", "saying,", "Great and marvellous", "song"), sg("15:4")], lambda w, h: A.glass_fire("gf1", w, h, 1502), "#1A1440", who="victors", art_h=260),
        D([cp("15:5"), cp("15:6")], lambda w, h: A.tabernacle("tb1", w, h, 1505, "open"), "#1A1440", art_h=280),
        D([cp("15:7"), cp("15:8")], lambda w, h: A.tabernacle("tb2", w, h, 1507, "smoke"), "#1A1440", art_h=260),
        D([cp("16:1", to="seven angels,"), gd("16:1", frm="Go ye,")], lambda w, h: A.bowl_angels("ba2", w, h, 1601, bowls=True), "#2A1440", head="The Seven Bowls", sky=16, art_h=260),
        D([cp("16:2")], lambda w, h: B("bw1", w, h, 1602, "earth"), "#2A1A2A", art_h=240),
        D([cp("16:3")], lambda w, h: B("bw2", w, h, 1603, "sea"), "#2A0A10", art_h=240),
        D([cp("16:4"), *said("16:5", "saying,", "Righteous art thou"), sy("16:6"), *said("16:7", "saying,", "Yea, O Lord God")], lambda w, h: B("bw3", w, h, 1604, "rivers"), "#2A1A20", who="waters", art_h=220),
        D([cp("16:8"), cp("16:9")], lambda w, h: B("bw4", w, h, 1608, "sun"), "#C8501A", art_h=240),
        D([cp("16:10"), cp("16:11")], lambda w, h: B("bw5", w, h, 1610, "throne"), "#05050A", art_h=240),
        D([cp("16:12")], lambda w, h: B("bw6", w, h, 1612, "euphrates"), "#3A2A5A", art_h=240),
        D([cp("16:13"), cp("16:14")], lambda w, h: A.gathering(w, h, 1613), "#2A1A2A", art_h=220),
        F([sy("16:15")], JESUS_RISEN, bg=LIGHT_BG, who="christ"),
        D([cp("16:16")], lambda w, h: A.gathering(w, h, 1616, empty=True), "#2A1A2A", art_h=240),
        D([cp("16:17", to="saying,"), gd("16:17", frm="It is done:"), cp("16:18")], lambda w, h: B("bw7", w, h, 1617, "air"), "#14141E", art_h=240),
        D([cp("16:19"), cp("16:20"), cp("16:21")], lambda w, h: A.city_split(w, h, 1619), "#14141E", art_h=260),
        D([cp("17:1", to="saying,"), sy("17:1", frm="Come hither"), sy("17:2")], lambda w, h: A.many_waters("mw1", w, h, 1701), "#2A2A5A", who="bowl", head="The Great Harlot", sky=17, art_h=260),
        D([cp("17:3"), cp("17:4"), cp("17:5")], lambda w, h: A.beast_plate(w, h, "scarlet", cup_=True), "#12102A", art_h=260),
        F([cp("17:6"), *said("17:7", "said unto me,", "Wherefore didst thou wonder?")], JOHN_AWE, bg=VISION_BG),
        D([sy("17:8"), sy("17:9"), sy("17:10"), sy("17:11")], lambda w, h: A.seven_kings(w, h), "#0B1A2E", who="bowl", art_h=240),
        D([sy("17:12"), sy("17:13"), sy("17:14")], lambda w, h: A.ten_kings(w, h, 1712), "#1A1440", who="bowl", art_h=240),
        D([*said("17:15", "unto me,", "The waters"), sy("17:16"), sy("17:17"), sy("17:18")], lambda w, h: A.waters_plate(w, h), "#0B1A2E", who="bowl", art_h=200),
        D([cp("18:1"), *said("18:2", "saying,", "Fallen, fallen"), sy("18:3")], lambda w, h: A.babylon("by1", w, h, 1801, "glory"), "#3A2A4A", who="angel", head="Fallen, Fallen Is Babylon the Great", sky=18, art_h=260),
        D([cp("18:4", to="saying,"), gd("18:4", frm="Come forth,"), gd("18:5"), gd("18:6")], lambda w, h: A.babylon("by2", w, h, 1804, "exodus"), "#1A1028", art_h=240),
        D([gd("18:7"), gd("18:8")], lambda w, h: A.babylon("by3", w, h, 1807, "proud"), "#0B0B2A", art_h=240),
        D([gd("18:9"), gd("18:10", to="saying,"), sy("18:10", frm="Woe, woe")], lambda w, h: A.babylon("by4", w, h, 1809, "kings"), "#1A0A10", who="kings", art_h=240),
        D([gd("18:11"), gd("18:12"), gd("18:13")], lambda w, h: A.cargo(w, h), "#0B1A2E", art_h=260),
        D([gd("18:14"), gd("18:15"), gd("18:16", to="saying,"), sy("18:16", frm="Woe, woe"), sy("18:17", to="made desolate.")],
          lambda w, h: A.babylon("by5", w, h, 1814, "merchants"), "#1A0A10", who="merchants", art_h=220),
        D([gd("18:17", frm="And every shipmaster"), gd("18:18", to="saying,"), sy("18:18", frm="What city"), gd("18:19", to="saying,"), sy("18:19", frm="Woe, woe"), gd("18:20")],
          lambda w, h: A.babylon("by6", w, h, 1817, "ships"), "#1A0A10", who="ships", art_h=220),
        D([cp("18:21", to="saying,"), sy("18:21", frm="Thus with a mighty fall")], lambda w, h: A.babylon("by7", w, h, 1821, "millstone"), "#2A2A4A", who="mighty", art_h=280),
        D([sy("18:22"), sy("18:23"), cp("18:24")], lambda w, h: A.babylon("by8", w, h, 1822, "empty"), "#0B0B2A", who="mighty", art_h=240)]
PG.extend(K.pack(SEGS, "REV-C05-D", PG.next(), end=nxt("NEXT · BEHOLD, I MAKE ALL THINGS NEW")))
