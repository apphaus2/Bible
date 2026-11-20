"""Revelation volume, Chapter 6 — Behold, I Make All Things New (Revelation 19–22). Every verse, word for word from ref/eng-asv.
The last chapter of the volume and of the Bible. The hallelujahs of the great multitude over the throne room, the elders
fallen down; the marriage supper of the Lamb — a long table in light spread with white linen, the bidden in white, the Lamb
at its head, the fine linen hung over it (the bride is the city and the linen; no woman drawn); John fallen before the
angel, see thou do it not. Heaven opened and he that sat upon the white horse, Faithful and True, the Word of God: a figure
of light on a white horse, ntcast's Jesus in white with many diadems — his eyes, the name, the garment sprinkled with blood,
the sword of his mouth and the winepress are in the words only; the armies of heaven on white horses behind. The angel
standing in the sun and the birds in the empty sky (the great supper of God, the flesh of kings and the slain are words
only); the beast and the false prophet cast into the lake of fire — fire with no one in it. The angel with the key of the
abyss and the great chain over the pit shut and sealed (the dragon, the Devil and Satan, never drawn); thrones and the souls
as figures of white light; the beloved city and the camp of the saints compassed by a dark host far off, fire falling on the
host; the lake of fire again; the great white throne, empty in a blaze of light, nothing about it, the books opened; the
sea under the light, empty (the dead, death and Hades and the lake of fire are words over light and fire, no figures in
torment). A new heaven and a new earth with no sea, the holy city coming down out of heaven made ready as a bride; men of
every nation in white before its light; "Behold, I make all things new" — God's words in the Voice box over the throne in
light with its rainbow; John and the angel on a mountain great and high; the city in plan — twelve gates of pearl, a tribe's
name on each (the gates as Ezekiel 48:31–34 names them), an angel at each, the twelve foundations; the city foursquare
measured, twelve thousand furlongs, the wall 144 cubits, the golden reed; the twelve foundations, each stone named and
coloured; the street of pure gold as transparent glass to a gate of one pearl, no temple, no sun, the Lamb its lamp; the
nations and the kings walking into its open gates. The river of water of life out of the throne, the tree of life on either
side bearing twelve manner of fruits; the servants before the throne in light; the angel and John; Jesus' last words beside
his face in light and over the morning star; the Spirit and the bride say, Come — the water of life flowing out to all; the
book of this prophecy open; the last morning over the new earth; and the grace of the Lord Jesus over a burst of light,
END OF REVELATION · THE END, with 完."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from rev import G, art6 as A, ch05 as _prev
from rev.art import morning_star, throne_light
from rev.common import K, Pages, D, F, glory, cp, gd, sg, sy, v, said, title, fin, JESUS_RISEN, LIGHT_BG, LIGHT_BG_R

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
K.art_k = 1.1
START, PAGES, P = PG.start, PG.pages, PG.P


@P("REV-C06-00-Title", "Chapter 6 · Behold, I Make All Things New", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A5AA8"></rect><g transform="translate(0 300)">{A.new_earth("t6", 760, 780, 2101, "descend")}</g>'
    return title(6, "Behold, I Make All Things New", "Revelation 19 – 22", svg, "#3A5AA8", v("21:5", frm="Behold, I make all things new.", to="new."), size=84)


TR, NE, C = A.throne_room, A.new_earth, "christ"
SEGS = [D([*said("19:1", "saying,", "Hallelujah;", "song"), sg("19:2")], lambda w, h: A.multitude("mu1", w, h, 1901), "#1A1440", who="multitude", head="Hallelujah", sky=19, art_h=260),
        D([cp("19:3", to="they say,"), sg("19:3", frm="Hallelujah.", to="Hallelujah."), cp("19:3", frm="And her smoke"), *said("19:4", "saying,", "Amen;", "song")],
          lambda w, h: TR("tr1", w, h, 1903, elders="bow"), "#0B0B2A", who="elders", art_h=240),
        D([*said("19:5", "saying,", "Give praise"), *said("19:6", "saying,", "Hallelujah:", "song"), sg("19:7"), cp("19:8")], lambda w, h: A.marriage_supper("ms1", w, h, 1905), "#2A2A6A", who="multitude", head="The Marriage of the Lamb", art_h=240),
        D([cp("19:9", to="unto me,"), sy("19:9", frm="Write,", to="of the Lamb."), cp("19:9", frm="And he saith unto me,", to="unto me,", after="Lamb."), sy("19:9", frm="These are true words"),
           cp("19:10", to="saith unto me,"), sy("19:10", frm="See thou do it not:")], lambda w, h: A.angel_john("aj1", w, h, 1909), "#2A2A6A", who="angel", art_h=240),
        D([cp("19:11"), cp("19:12"), cp("19:13")], lambda w, h: A.white_horse("wh1", w, h, 1911), "#1A1440", head="Faithful and True", art_h=320),
        D([cp("19:14"), cp("19:15"), cp("19:16")], lambda w, h: A.white_horse("wh2", w, h, 1914, armies=True), "#1A1440", art_h=280),
        D([cp("19:17", to="mid heaven,"), sy("19:17", frm="Come and be gathered"), sy("19:18")], lambda w, h: A.sun_angel("su1", w, h, 1917), "#C8601A", who="sun", art_h=260),
        D([cp("19:19"), cp("19:20"), cp("19:21")], lambda w, h: A.lake_fire(w, h, 1919), "#0A0406", art_h=220),
        D([cp("20:1"), cp("20:2"), cp("20:3")], lambda w, h: A.abyss_sealed("ab1", w, h, 2001), "#0B0B2A", head="A Thousand Years", sky=20, art_h=260),
        D([cp("20:4"), cp("20:5"), cp("20:6")], lambda w, h: A.thrones_souls("ts1", w, h, 2004), "#2A2A6A", art_h=240),
        D([cp("20:7"), cp("20:8"), cp("20:9")], lambda w, h: A.beloved_city(w, h, 2007), "#1A1028", art_h=240),
        D([cp("20:10")], lambda w, h: A.lake_fire(w, h, 2010), "#0A0406", art_h=220),
        D([cp("20:11"), cp("20:12")], lambda w, h: A.white_throne(w, h, 2011), "#0A0A12", head="A Great White Throne", art_h=320),
        D([cp("20:13"), cp("20:14"), cp("20:15")], lambda w, h: A.sea_light(w, h, 2013), "#1A1A3A", art_h=220),
        D([cp("21:1"), cp("21:2")], lambda w, h: NE("ne1", w, h, 2101, "descend"), "#3A5AA8", head="A New Heaven and a New Earth", sky=21, art_h=340),
        D([*said("21:3", "saying,", "Behold, the tabernacle"), sy("21:4")], lambda w, h: NE("ne2", w, h, 2103, "dwell"), "#3A5AA8", who="throne", art_h=260),
        D([cp("21:5", to="throne said,"), gd("21:5", frm="Behold, I make", to="new."), cp("21:5", frm="And he saith,", to="saith,"), gd("21:5", frm="Write:"),
           cp("21:6", to="unto me,"), gd("21:6", frm="They are come"), gd("21:7"), gd("21:8")], lambda w, h: throne_light(w, h, 2105, rainbow=True), "#1A1440", head="Behold, I Make All Things New", art_h=240),
        D([*said("21:9", "saying,", "Come hither"), cp("21:10"), cp("21:11")], lambda w, h: NE("ne3", w, h, 2109, "mountain"), "#3A5AA8", who="bowl", head="The Holy City Jerusalem", art_h=280),
        D([cp("21:12"), cp("21:13"), cp("21:14")], lambda w, h: A.city_plan(w, h), "#0B1A2E", art_h=320),
        D([cp("21:15"), cp("21:16"), cp("21:17")], lambda w, h: A.city_measure(w, h), "#0B1A2E", art_h=280),
        D([cp("21:18"), cp("21:19"), cp("21:20")], lambda w, h: A.foundations(w, h), "#0B1A2E", art_h=320),
        D([cp("21:21"), cp("21:22"), cp("21:23")], lambda w, h: A.street_gold("sg1", w, h, 2121), "#FFF8DC", art_h=280),
        D([cp("21:24"), cp("21:25"), cp("21:26"), cp("21:27")], lambda w, h: NE("ne4", w, h, 2124, "nations"), "#3A5AA8", art_h=260),
        D([cp("22:1"), cp("22:2")], lambda w, h: A.river_life("rl1", w, h, 2201), "#FFF8DC", head="The River of Water of Life", sky=22, art_h=340),
        D([cp("22:3"), cp("22:4"), cp("22:5")], lambda w, h: A.servants("sv1", w, h, 2203), "#FFF8DC", art_h=260),
        D([*said("22:6", "unto me,", "These words")], lambda w, h: A.angel_john("aj2", w, h, 2206, fallen=False), "#2A2A6A", who="angel", art_h=260),
        F([sy("22:7")], JESUS_RISEN, bg=LIGHT_BG, who=C),
        D([cp("22:8"), cp("22:9", to="unto me,"), sy("22:9", frm="See thou do it not:")], lambda w, h: A.angel_john("aj3", w, h, 2208), "#2A2A6A", who="angel", art_h=240),
        D([cp("22:10", to="unto me,"), sy("22:10", frm="Seal not up"), sy("22:11")], lambda w, h: A.open_book(w, h, 2210), "#1A1440", who="angel", art_h=220),
        F([sy("22:12"), sy("22:13"), sy("22:14"), sy("22:15")], JESUS_RISEN, bg=LIGHT_BG, who=C, head="I Come Quickly"),
        D([sy("22:16")], lambda w, h: morning_star(w, h, 2216), "#0B0B2A", who=C, art_h=280),
        D([cp("22:17", to="the bride say,"), sy("22:17", frm="Come.", to="Come."), cp("22:17", frm="And he that heareth,")], lambda w, h: A.water_life("wl1", w, h, 2217), "#3A5AA8", who="bride", art_h=280),
        D([sy("22:18"), sy("22:19")], lambda w, h: A.open_book(w, h, 2218), "#1A1440", who=C, art_h=200),
        D([cp("22:20", to="saith,"), sy("22:20", frm="Yea:", to="quickly."), cp("22:20", frm="Amen:")], lambda w, h: NE("ne5", w, h, 2220, "dawn"), "#1A1A5A", who=C, art_h=300),
        glory([cp("22:21")], h=330, seed=2221)]
PG.extend(K.pack(SEGS, "REV-C06-D", PG.next(), end=fin("END OF REVELATION · THE END")))
