"""Revelation volume, Chapter 4 — A Great Sign in Heaven (Revelation 12–14). Every verse, word for word from ref/eng-asv.
The woman arrayed with the sun, the moon under her feet and a crown of twelve stars — a figure of light high in heaven,
seen far off; her travail and the birth are in the words only. The great red dragon is never drawn: another sign is a red,
star-torn sky with the third part of the stars falling; the child caught up unto God and unto his throne as a light rising,
the woman far off fleeing into the wilderness. The war in heaven: Michael and his angels in light against a darkness with
no shape, the darkness cast down to the earth (the old serpent, the Devil and Satan, is named in the words only); rejoice,
O heavens, over the dark earth and sea; the woman borne on the two wings of the great eagle; the river cast after her
swallowed by the opened earth, no one shown casting it. The beast out of the sea and the beast out of the earth as
heraldic plates on Daniel's dark field (like a leopard, the feet of a bear, the mouth of a lion, seven heads and ten horns
with ten diadems; two horns like a lamb), standing still — what they do is in the words; the whole earth bowed toward the
far emblem; forty and two months as a plate; the chain and the sword in a medallion; the image of the beast on its pedestal
with the crowds bowed far off (no one killed is drawn); the mark and the number of his name as a technical plate. The Lamb
on mount Zion with the hundred and forty and four thousand in white, harps among them; the firstfruits as a numbered plate;
three angels flying in mid heaven — over the nations, over Babylon fallen far off, over the smoke of fire and brimstone far
off (no one drawn in it); tombs in a garden at dawn; one like unto a son of man on the white cloud (ntcast's Jesus, risen,
crowned, a sharp sickle), the ripe wheat; the angel with the sickle over the vine; the winepress without the city on an
empty plain at a red dusk — the blood unto the bridles is in the words only."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from rev import G, art4 as A, ch03 as _prev
from rev.common import K, Pages, D, F, cp, gd, sg, sy, v, said, title, nxt

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
K.art_k = 1.2
START, PAGES, P = PG.start, PG.pages, PG.P


@P("REV-C04-00-Title", "Chapter 4 · A Great Sign in Heaven", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B0B2A"></rect><g transform="translate(0 300)">{A.woman_sun("t4", 760, 780, 1201)}</g>'
    return title(4, "A Great Sign in Heaven", "Revelation 12 – 14", svg, "#0B0B2A", v("12:1", to="seen in heaven:"))


SEGS = [D([cp("12:1"), cp("12:2")], lambda w, h: A.woman_sun("ws1", w, h, 1201), "#0B0B2A", head="A Great Sign in Heaven", sky=12, art_h=320),
        D([cp("12:3"), cp("12:4")], lambda w, h: A.red_sky(w, h, 1203), "#3A0408", art_h=260),
        D([cp("12:5"), cp("12:6")], lambda w, h: A.woman_sun("ws2", w, h, 1205, "flee"), "#2A2A6A", art_h=260),
        D([cp("12:7"), cp("12:8")], lambda w, h: A.war_heaven("wh1", w, h, 1207), "#1A1440", head="War in Heaven", art_h=280),
        D([cp("12:9")], lambda w, h: A.war_heaven("wh2", w, h, 1209, fall=True), "#1A1440", art_h=240),
        D([*said("12:10", "saying,", "Now is come", "song"), sg("12:11"), sg("12:12")], lambda w, h: A.heaven_earth(w, h, 1210), "#5A4A8A", who="voice", art_h=200),
        D([cp("12:13"), cp("12:14")], lambda w, h: A.woman_sun("ws3", w, h, 1213, "wings"), "#2A2A6A", art_h=260),
        D([cp("12:15"), cp("12:16"), cp("12:17"), cp("13:1", to="sand of the sea.")], lambda w, h: A.woman_sun("ws4", w, h, 1215, "flood"), "#2A2A6A", art_h=240),
        D([cp("13:1", frm="And I saw a beast"), cp("13:2")], lambda w, h: A.beast_plate(w, h, "sea"), "#12102A", head="A Beast out of the Sea", sky=13, art_h=280),
        D([cp("13:3"), *said("13:4", "saying,", "Who is like")], lambda w, h: A.image("im0", w, h, 1303), "#1A1418", who="earth", art_h=240),
        D([cp("13:5"), cp("13:6"), cp("13:7"), cp("13:8")], lambda w, h: A.months(w, h), "#0B1A2E", art_h=200),
        D([cp("13:9"), cp("13:10")], lambda w, h: A.emblem_sword(w, h, 1309), "#1A1A2A", art_h=220),
        D([cp("13:11"), cp("13:12"), cp("13:13")], lambda w, h: A.beast_plate(w, h, "earth"), "#12102A", head="Another Beast out of the Earth", art_h=260),
        D([cp("13:14"), cp("13:15")], lambda w, h: A.image("im1", w, h, 1314), "#1A1418", art_h=260),
        D([cp("13:16"), cp("13:17"), cp("13:18")], lambda w, h: A.mark_plate(w, h), "#0B1A2E", art_h=180),
        D([cp("14:1"), cp("14:2"), cp("14:3")], lambda w, h: A.zion("zi1", w, h, 1401), "#2A3A7A", head="The Lamb on Mount Zion", sky=14, art_h=320),
        D([cp("14:4"), cp("14:5")], lambda w, h: A.firstfruits(w, h), "#0B1A2E", art_h=220),
        D([cp("14:6"), *said("14:7", "great voice,", "Fear God")], lambda w, h: A.flying("fl1", w, h, 1406, "first"), "#3A6AB0", who="first", head="Three Angels", art_h=260),
        D([*said("14:8", "saying,", "Fallen, fallen")], lambda w, h: A.flying("fl2", w, h, 1408, "second"), "#3A2A4A", who="second", art_h=240),
        D([*said("14:9", "great voice,", "If any man"), sy("14:10"), sy("14:11"), cp("14:12")], lambda w, h: A.flying("fl3", w, h, 1409, "third"), "#1A0A0A", who="third", art_h=220),
        D([cp("14:13", to="saying,"), sy("14:13", frm="Write,", to="henceforth:"), sy("14:13", frm="yea, saith the Spirit,")], lambda w, h: A.tombs_dawn(w, h, 1413), "#3A3A7A", who="voice", art_h=240),
        D([cp("14:14"), *said("14:15", "sat on the cloud,", "Send forth thy sickle"), cp("14:16")], lambda w, h: A.harvest("hv1", w, h, 1414, "cloud"), "#5A8AC8", who="angel", head="The Harvest of the Earth", art_h=300),
        D([cp("14:17"), *said("14:18", "saying,", "Send forth thy sharp sickle")], lambda w, h: A.harvest("hv2", w, h, 1417, "vine"), "#5A4A8A", who="sickle", art_h=260),
        D([cp("14:19"), cp("14:20")], lambda w, h: A.harvest("hv3", w, h, 1419, "press"), "#2A0A10", art_h=260)]
PG.extend(K.pack(SEGS, "REV-C04-D", PG.next(), budget=1100, end=nxt("NEXT · FALLEN IS BABYLON THE GREAT")))
