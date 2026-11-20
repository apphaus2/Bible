"""Revelation volume, Chapter 2 — Worthy Is the Lamb (Revelation 4–7). Every verse, word for word from ref/eng-asv.
A door opened in heaven over the night sea and John on the rock; the throne set in heaven — empty, in light (God is never
drawn), the rainbow round about it like an emerald, lightnings, the seven lamps of fire, the sea of glass like crystal; the
four and twenty elders in white with crowns of gold on their thrones in a ring; the throne room as a technical plan, every
part named; the four living creatures as heraldic medallions of light (a lion, a calf, a man's face, a flying eagle, six
wings, full of eyes); the elders fallen down, their crowns cast before the throne. The book close sealed with seven seals
lying in the light on the throne (no hand drawn); John weeping beside his face; one of the elders, Weep not; the Lamb
standing as though it had been slain — an emblem of light with seven horns and seven eyes, no wound drawn; the elders with
harps and golden bowls of incense; many angels in rings about the throne (figures of light, no faces); every created thing
in heaven, on the earth and on the sea. The seals: the four horses each seen far off on the horizon — the white at morning
(the bow, the crown), the red at a red dusk (the great sword is in the words only), the black over the fields of wheat and
barley (the balance), the pale over an empty grey plain (Death and Hades are named in the words only, not drawn); the souls
underneath the altar as figures of white light; the sixth seal's black sun, blood moon, falling stars and rolled-up heaven;
the kings and every bondman hiding in the caves of the mountains. The four angels holding the four winds and another from the
sunrising with the seal of the living God; the hundred and forty and four thousand as a numbered plate of the twelve tribes;
the great multitude in white robes with palms; the elder and John; the Lamb leading them to fountains of waters of life."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from rev import G, art2 as A, ch01 as _prev
from rev.common import K, Pages, D, F, cp, gd, sg, sy, v, said, title, nxt, JOHN_GRIEF, JOHN_AWE, ELDER, GRIEF_BG, LIGHT_BG

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("REV-C02-00-Title", "Chapter 2 · Worthy Is the Lamb", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B0B2A"></rect><g transform="translate(0 330)">{A.throne_room("t2", 760, 750, 401, lamb_=True)}</g>'
    return title(2, "Worthy Is the Lamb", "Revelation 4 – 7", svg, "#0B0B2A", v("5:12", frm="Worthy is the Lamb", to="slain"))


TR = A.throne_room
SEGS = [D([*said("4:1", "one saying,", "Come up hither")], lambda w, h: A.door_heaven("dh1", w, h, 401), "#05051A", who="trumpet", head="A Door Opened in Heaven", sky=4, art_h=280),
        D([cp("4:2"), cp("4:3")], lambda w, h: TR("tr1", w, h, 402, elders=None, creatures_=False), "#0B0B2A", head="A Throne Set in Heaven", art_h=300),
        D([cp("4:4"), cp("4:5")], lambda w, h: TR("tr2", w, h, 404, creatures_=False), "#0B0B2A", art_h=300),
        D([cp("4:6"), cp("4:7")], lambda w, h: A.throne_plan(w, h), "#0B1A2E", art_h=300),
        D([*said("4:8", "saying,", "Holy, holy, holy", "song")], lambda w, h: A.creatures(w, h), "#12102A", who="living", head="Holy, Holy, Holy", art_h=240),
        D([cp("4:9"), cp("4:10"), sg("4:11")], lambda w, h: TR("tr3", w, h, 409, elders="bow", crowns=True), "#0B0B2A", who="elders", art_h=280),
        D([cp("5:1"), *said("5:2", "great voice,", "Who is worthy")], lambda w, h: A.sealed_book(w, h, 501), "#1A1440", who="mighty", head="A Book Close Sealed", sky=5, art_h=220),
        F([cp("5:3"), cp("5:4")], JOHN_GRIEF, bg=GRIEF_BG),
        D([*said("5:5", "saith unto me,", "Weep not;")], lambda w, h: A.elder_john("ej1", w, h, 505, weep=True), "#1A1440", who="elder", art_h=280),
        D([cp("5:6"), cp("5:7")], lambda w, h: TR("tr4", w, h, 506, lamb_=True), "#0B0B2A", head="A Lamb Standing", art_h=320),
        D([cp("5:8"), *said("5:9", "saying,", "Worthy art thou", "song"), sg("5:10")], lambda w, h: TR("tr5", w, h, 508, elders="harps", lamb_=True), "#0B0B2A", who="elders", art_h=260),
        D([cp("5:11"), *said("5:12", "great voice,", "Worthy is the Lamb", "song")], lambda w, h: TR("tr6", w, h, 511, elders=None, angels=2, lamb_=True), "#0B0B2A", who="angels", art_h=280),
        D([*said("5:13", "heard I saying,", "Unto him that sitteth", "song"), cp("5:14", to="said,"), sy("5:14", frm="Amen.", to="Amen."), cp("5:14", frm="And the elders")],
          lambda w, h: A.every_creature("ec1", w, h, 513), "#3A3A8A", who="every", art_h=260),
        D([*said("6:1", "voice of thunder,", "Come."), cp("6:2")], lambda w, h: A.horsemen("hw", w, h, 601, "white"), "#5AA8D8", who="creature", head="The Seals", sky=6, art_h=260),
        D([*said("6:3", "saying,", "Come."), cp("6:4")], lambda w, h: A.horsemen("hr", w, h, 603, "red"), "#3A0A10", who="creature", art_h=260),
        D([cp("6:5", to="saying,"), sy("6:5", frm="Come.", to="Come."), cp("6:5", frm="And I saw"), *said("6:6", "saying,", "A measure")],
          lambda w, h: A.horsemen("hb", w, h, 605, "black"), "#4A4A5A", who="creature", art_h=240),
        D([*said("6:7", "saying,", "Come."), cp("6:8")], lambda w, h: A.horsemen("hp", w, h, 607, "pale"), "#2A2E36", who="creature", art_h=260),
        D([cp("6:9"), *said("6:10", "saying,", "How long"), cp("6:11")], lambda w, h: A.souls_altar("sa1", w, h, 609), "#1A1440", who="souls", head="Underneath the Altar", art_h=260),
        D([cp("6:12"), cp("6:13"), cp("6:14")], lambda w, h: A.sixth_seal(w, h, 612), "#1A0A10", head="The Great Day of Their Wrath", art_h=300),
        D([cp("6:15"), *said("6:16", "to the rocks,", "Fall on us"), sy("6:17")], lambda w, h: A.caves("cv1", w, h, 615), "#1A0A10", who="kings", art_h=280),
        D([cp("7:1"), cp("7:2"), *said("7:3", "saying,", "Hurt not")], lambda w, h: A.four_winds("fw1", w, h, 701), "#2A3A6A", who="angel", head="The Servants of Our God", sky=7, art_h=280),
        D([cp("7:4"), cp("7:5"), cp("7:6"), cp("7:7"), cp("7:8")], lambda w, h: A.tribes_plate(w, h), "#0B1A2E", art_h=260),
        D([cp("7:9"), *said("7:10", "saying,", "Salvation", "song")], lambda w, h: A.multitude("mu1", w, h, 709), "#1A1440", who="multitude", head="A Great Multitude", art_h=320),
        D([cp("7:11"), *said("7:12", "saying,", "Amen: Blessing", "song")], lambda w, h: TR("tr7", w, h, 711, elders="bow", angels=2), "#0B0B2A", who="angels", art_h=260),
        F([*said("7:13", "saying unto me,", "These that are"), cp("7:14", to="unto him,"), sy("7:14", frm="My lord,", to="thou knowest."),
           cp("7:14", frm="And he said to me,", to="to me,"), sy("7:14", frm="These are they")], ELDER, bg=LIGHT_BG, who="elder"),
        D([sy("7:15"), sy("7:16"), sy("7:17")], lambda w, h: A.multitude("mu2", w, h, 715, "fountains"), "#6AB0D8", who="elder", art_h=280)]
PG.extend(K.pack(SEGS, "REV-C02-D", PG.next(), end=nxt("NEXT · SILENCE IN HEAVEN")))
