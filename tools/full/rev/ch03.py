"""Revelation volume, Chapter 3 — Silence in Heaven (Revelation 8–11). Every verse, word for word from ref/eng-asv.
The seventh seal and the silence in heaven (the throne room hushed, no lightnings); the seven angels with their trumpets;
another angel with the golden censer at the golden altar, the smoke of the incense going up; the censer filled with the
fire of the altar and cast upon the earth. The trumpets, each over land, sea and sky with no one struck: hail and fire on
the trees and the grass (what is mingled with it is in the words), the great mountain burning cast into the sea among the
ships, the star Wormwood falling on the rivers, the third part of the sun and of the moon darkened, an eagle crying woe in
mid heaven. The pit of the abyss — a star fallen and the key, the smoke of the pit darkening the sun, the locusts going
out over a land whose trees and grass stay green; the locusts as a heraldic plate (their faces, hair and teeth in the
words; the angel of the abyss, Abaddon, named only); the voice from the horns of the golden altar; the great river
Euphrates and the host far off as a dark line on the horizon; the horses of the vision as a heraldic plate (their killing
in the words only); the idols of gold, silver, brass, stone and wood. The strong angel arrayed with a cloud, the rainbow on
his head, his face as the sun (a sun's disc), his feet as pillars of fire, one foot on the sea and one on the earth; the
seven thunders; the oath; John taking the little book, and beside his face, sweet as honey and bitter. The temple measured
(a plate); the two witnesses in sackcloth between the olive trees and the candlesticks; the heaven shut over a cracked
land; their death and their bodies in the street are told over the empty street of the great city at evening — no one is
drawn lying there; their rising as two figures of light going up into the cloud; the tenth part of the city fallen as a
ruin; the seventh angel sounding in great light; the elders fallen upon their faces; the temple opened in heaven and the
ark of his covenant seen, lightnings and great hail."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from rev import G, art3 as A, ch02 as _prev
from rev.common import K, Pages, D, F, cp, gd, sg, sy, v, said, title, nxt, JOHN_AWE, JOHN_JOY, LIGHT_BG, VISION_BG

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("REV-C03-00-Title", "Chapter 3 · Silence in Heaven", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#1A1440"></rect><g transform="translate(0 340)">{A.seven_angels("t3", 760, 740, 801)}</g>'
    return title(3, "Silence in Heaven", "Revelation 8 – 11", svg, "#1A1440", v("8:1", frm="there followed a silence in heaven"))


TR = A.throne_room
SEGS = [D([cp("8:1")], lambda w, h: TR("si1", w, h, 801, lightning=False), "#0B0B2A", head="Silence in Heaven", sky=8, art_h=300),
        D([cp("8:2")], lambda w, h: A.seven_angels("sv1", w, h, 802), "#1A1440", art_h=280),
        D([cp("8:3"), cp("8:4")], lambda w, h: A.censer("ce1", w, h, 803), "#1A1440", art_h=280),
        D([cp("8:5"), cp("8:6")], lambda w, h: A.censer("ce2", w, h, 805, cast=True), "#0B0B2A", art_h=260),
        D([cp("8:7")], lambda w, h: A.hail_fire(w, h, 807), "#2A0A10", head="The First Four Trumpets", art_h=260),
        D([cp("8:8"), cp("8:9")], lambda w, h: A.mountain_sea(w, h, 808), "#2A0A10", art_h=260),
        D([cp("8:10"), cp("8:11")], lambda w, h: A.wormwood(w, h, 810), "#0B0B2A", art_h=260),
        D([cp("8:12")], lambda w, h: A.darkened(w, h, 812), "#0B0B2A", art_h=260),
        D([*said("8:13", "great voice,", "Woe, woe, woe")], lambda w, h: A.eagle_woe(w, h, 813), "#1A1028", who="eagle", art_h=240),
        D([cp("9:1"), cp("9:2")], lambda w, h: A.pit("pt1", w, h, 901, "key"), "#0B0B2A", head="The Pit of the Abyss", sky=9, art_h=260),
        D([cp("9:3"), cp("9:4"), cp("9:5"), cp("9:6")], lambda w, h: A.pit("pt2", w, h, 903, "locusts"), "#1A1418", art_h=240),
        D([cp("9:7"), cp("9:8"), cp("9:9"), cp("9:10"), cp("9:11")], lambda w, h: A.locust_plate(w, h), "#0B1A2E", art_h=240),
        D([cp("9:12"), cp("9:13"), *said("9:14", "had the trumpet,", "Loose the four")], lambda w, h: A.altar_horns("ah1", w, h, 912), "#1A1440", who="altar", head="The Great River Euphrates", art_h=260),
        D([cp("9:15"), cp("9:16")], lambda w, h: A.euphrates(w, h, 915), "#2A1028", art_h=240),
        D([cp("9:17"), cp("9:18"), cp("9:19")], lambda w, h: A.horse_plate(w, h), "#0B1A2E", art_h=240),
        D([cp("9:20"), cp("9:21")], lambda w, h: A.idols(w, h, 920), "#1A1418", art_h=220),
        D([cp("10:1"), cp("10:2")], lambda w, h: A.mighty_angel("ma1", w, h, 1001), "#2A3A6A", head="The Little Book", sky=10, art_h=340),
        D([cp("10:3"), *said("10:4", "saying,", "Seal up")], lambda w, h: A.mighty_angel("ma2", w, h, 1003, "thunders"), "#14141E", who="voice", art_h=280),
        D([cp("10:5"), cp("10:6"), cp("10:7")], lambda w, h: A.mighty_angel("ma3", w, h, 1005, "oath"), "#2A3A6A", art_h=280),
        D([*said("10:8", "and saying,", "Go, take the book"), *said("10:9", "he saith unto me,", "Take it, and eat it up")],
          lambda w, h: A.mighty_angel("ma4", w, h, 1008, "book"), "#2A3A6A", who="voice", art_h=280),
        F([cp("10:10"), *said("10:11", "unto me,", "Thou must prophesy")], JOHN_AWE, bg=VISION_BG),
        D([*said("11:1", "one said,", "Rise, and measure"), sy("11:2")], lambda w, h: A.measure(w, h), "#0B1A2E", head="The Two Witnesses", sky=11, art_h=260),
        D([sy("11:3"), sy("11:4")], lambda w, h: A.witnesses("wi1", w, h, 1103), "#3A3A6A", art_h=300),
        D([sy("11:5"), sy("11:6")], lambda w, h: A.witnesses("wi2", w, h, 1105, "drought"), "#C8702A", art_h=240),
        D([cp("11:7"), cp("11:8"), cp("11:9"), cp("11:10")], lambda w, h: A.witnesses("wi3", w, h, 1107, "street"), "#1A1028", art_h=240),
        D([cp("11:11"), cp("11:12", to="saying unto them,"), sy("11:12", frm="Come up hither.", to="hither."), cp("11:12", frm="And they went up")],
          lambda w, h: A.witnesses("wi4", w, h, 1111, "rise"), "#2A3A7A", who="voice", art_h=260),
        D([cp("11:13"), cp("11:14")], lambda w, h: A.witnesses("wi5", w, h, 1113, "quake"), "#2A1A1A", art_h=240),
        D([*said("11:15", "they said,", "The kingdom of the world", "song")], lambda w, h: A.seventh("se1", w, h, 1115), "#1A1440", who="voices", head="The Kingdom of the World", art_h=280),
        D([cp("11:16"), *said("11:17", "saying,", "We give thee thanks", "song"), sg("11:18")], lambda w, h: TR("tr8", w, h, 1116, elders="bow"), "#0B0B2A", who="elders", art_h=240),
        D([cp("11:19")], lambda w, h: A.ark_heaven("ak1", w, h, 1119), "#14141E", art_h=320)]
PG.extend(K.pack(SEGS, "REV-C03-D", PG.next(), end=nxt("NEXT · A GREAT SIGN IN HEAVEN")))
