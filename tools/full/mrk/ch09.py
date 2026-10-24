"""Mark volume, Chapter 9 — He Is Risen (Mark 14:43–16:20). Every verse, word for word from ref/eng-asv.
Restraint throughout the passion, as in Matthew: the torches and staves in the garden and the kiss; the sword dropped in
the torchlight, the blow told in words only, no blood; the garden left empty; the young man who fled told in words only
over the dark garden, never drawn. The high priest's hall, Jesus standing bound and silent; the false witnesses and the
high priest beside their faces; I am, beside Jesus' face; the spitting and the blows told in words only over the shut door;
Peter by the fire, the maid, the porch, the cock on the wall at the second crowing, and Peter weeping beside his face.
Jesus led bound at dawn to Pilate; the judgment-seat, Barabbas and the crowd; the scourging, the purple, the crown of
thorns and the mocking told in words only over the empty Prætorium court with the purple robe laid aside and the reed;
Simon of Cyrene bearing the cross out of the gate; Golgotha only as three crosses on the hill from far off, nothing on them
in any detail, the lots cast at its foot, the passers-by on the road below; the darkness over the whole land, his cry and
his death told in words over the darkened hill; the veil rent; the centurion beside his face; the women afar; Joseph of
Arimathæa and the tomb hewn out of the rock, the stone rolled against the door. Then the dawn: the three women with their
spices; the stone rolled back, no one on it; the young man in white sitting on the right side within — a figure of white
light with a gold rim and no face; the place where they laid him; the women fleeing; and Jesus risen in white light — the
mourners told by Mary Magdalene, the two on the country road, the eleven at meat, Go ye into all the world, received up
into the cloud of light (God never drawn), and the roads going out everywhere."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mrk import G, art9 as A, ch08 as _prev
from mrk.common import (K, Pages, D, S, cp, gd, sg, sy, v, title, fin, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_PASSION, JESUS_RISEN, PETER, PETER_GRIEF,
                        CAIAPHAS, CAIAPHAS_RENT, WITNESS, PILATE, PILATE_TROUBLED, CENTURION, ARIMATHAEA, MAGDALENE)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MRK-C09-00-Title", "Chapter 9 · He Is Risen", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#5A6A9A"></rect><g transform="translate(0 300)">{A.stone_back("t9", 760, 780, 1604, women=False)}</g>'
    return title(9, "He Is Risen", "Mark 14:43 – 16:20", svg, "#3A4A7A", v("16:6", frm="he is risen;", to="he is not here:"))


RISEN_LIGHT = "radial-gradient(circle at 26% 46%, #FFFFFF 0 70px, #FFF8DC 220px, #F3E2B0 460px)"
def F(lines, tok=JESUS_PASSION, bg=COLD, **k): return K.face(lines, tok, bg=bg, **k)

SEGS = [D([cp("14:43")], lambda w, h: A.arrest("ar1", w, h, 1443), "#05051A", head="Swords and Staves"),
        D([cp("14:44", to="saying,"), sy("14:44", frm="Whomsoever"), cp("14:45", to="and saith,"), sy("14:45", frm="Rabbi;", to="Rabbi;"), cp("14:45", frm="and kissed him."), cp("14:46")],
          lambda w, h: A.arrest("ar2", w, h, 1444), "#05051A"),
        D([cp("14:47")], lambda w, h: A.arrest("ar3", w, h, 1447, sword=True), "#05051A"),
        F([cp("14:48", to="said unto them,"), sy("14:48", frm="Are ye come"), sy("14:49")]),
        D([cp("14:50")], lambda w, h: A.arrest("ar4", w, h, 1450, empty=True), "#05051A"),
        D([cp("14:51"), cp("14:52")], lambda w, h: A.dark_garden("dg1", w, h, 1451), "#05051A"),
        D([cp("14:53")], lambda w, h: A.caiaphas_hall("ch1", w, h, 1453), "#2A1A2A", head="Before the High Priest"),
        D([cp("14:54")], lambda w, h: A.court_fire("cf1", w, h, 1454, maid=False), "#05051A"),
        F([cp("14:55"), cp("14:56"), cp("14:57"), sy("14:58"), cp("14:59")], WITNESS, bg=RED),
        F([cp("14:60", to="saying,"), sy("14:60", frm="Answerest"), cp("14:61", to="saith unto him,"), sy("14:61", frm="Art thou the Christ,")], CAIAPHAS, bg=RED),
        F([cp("14:62", to="And Jesus said,"), sy("14:62", frm="I am:")]),
        F([cp("14:63", to="and saith,"), sy("14:63", frm="What further"), sy("14:64", to="what think ye?"), cp("14:64", frm="And they all condemned")], CAIAPHAS_RENT, bg=RED),
        D([cp("14:65", to="unto him,"), sy("14:65", frm="Prophesy:", to="Prophesy:"), cp("14:65", frm="and the officers")], lambda w, h: A.shut_door("sd1", w, h, 1465), "#2A2228"),
        D([cp("14:66"), cp("14:67", to="and saith,"), sy("14:67", frm="Thou also"), cp("14:68", to="saying,"), sy("14:68", frm="I neither know", to="thou sayest:"), cp("14:68", frm="and he went out")],
          lambda w, h: A.court_fire("cf2", w, h, 1466), "#05051A", head="Peter by the Fire"),
        D([cp("14:69", to="stood by,"), sy("14:69", frm="This is one"), cp("14:70", to="said to Peter,"), sy("14:70", frm="Of a truth")],
          lambda w, h: A.court_fire("cf3", w, h, 1469, porch=True), "#05051A"),
        D([cp("14:71", to="to swear,"), sy("14:71", frm="I know not"), cp("14:72", to="said unto him,"), sy("14:72", frm="Before the cock", to="deny me thrice.")],
          lambda w, h: A.cockcrow("cc1", w, h, 1471), "#1A1A3A"),
        F([cp("14:72", frm="And when he thought")], PETER_GRIEF),
        # Mark 15
        D([cp("15:1")], lambda w, h: A.bound_dawn("bd1", w, h, 1501), "#2A2A4A", head="Delivered Up to Pilate", sky=(15, "left")),
        D([cp("15:2", to="Pilate asked him,"), sy("15:2", frm="Art thou", to="the Jews?"), cp("15:2", frm="And he answering", to="unto him,"), sy("15:2", frm="Thou sayest.")],
          lambda w, h: A.judgment_seat("js1", w, h, 1502, crowd_=False), "#8FD0E2"),
        F([cp("15:3"), cp("15:4", to="saying,"), sy("15:4", frm="Answerest"), cp("15:5")], PILATE, bg=GOLDEN),
        D([cp("15:6"), cp("15:7"), cp("15:8"), cp("15:9", to="saying,"), sy("15:9", frm="Will ye"), cp("15:10")], lambda w, h: A.judgment_seat("js2", w, h, 1506), "#8FD0E2",
          head="Barabbas", art_h=200),
        D([cp("15:11"), cp("15:12", to="said unto them,"), sy("15:12", frm="What then"), cp("15:13", to="again,"), sy("15:13", frm="Crucify him."), cp("15:14", to="said unto them,"),
           sy("15:14", frm="Why, what evil", to="hath he done?"), cp("15:14", frm="But they cried", to="exceedingly,"), sy("15:14", frm="Crucify him.")],
          lambda w, h: A.judgment_seat("js3", w, h, 1511), "#8FD0E2"),
        D([cp("15:15"), cp("15:16"), cp("15:17"), cp("15:18", to="salute him,"), sy("15:18", frm="Hail,"), cp("15:19"), cp("15:20")], lambda w, h: A.purple_laid("pl1", w, h, 1515),
          "#5A4A44", head="The King of the Jews"),
        D([cp("15:21")], lambda w, h: A.cyrene("cy1", w, h, 1521), "#8A8A9A", head="Golgotha"),
        D([cp("15:22"), cp("15:23"), cp("15:24"), cp("15:25"), cp("15:26"), cp("15:27")], lambda w, h: A.golgotha("gg1", w, h, 1522, lots=True), "#4A3A5A", art_h=240),
        D([cp("15:29", to="and saying,"), sy("15:29", frm="Ha!"), sy("15:30"), cp("15:31", to="scribes said,"), sy("15:31", frm="He saved"), sy("15:32", to="and believe."),
           cp("15:32", frm="And they that were")], lambda w, h: A.golgotha("gg2", w, h, 1529, passers=True), "#4A3A5A"),
        D([cp("15:33"), cp("15:34", to="loud voice,"), sy("15:34", frm="Eloi,", to="sabachthani?"), cp("15:34", frm="which is,", to="interpreted,"), sy("15:34", frm="My God,")],
          lambda w, h: A.golgotha("gg3", w, h, 1533, dark=True), "#05050E", head="Darkness over the Whole Land"),
        D([cp("15:35", to="said,"), sy("15:35", frm="Behold,"), cp("15:36", to="saying,"), sy("15:36", frm="Let be;"), cp("15:37")], lambda w, h: A.golgotha("gg4", w, h, 1535, dark=True),
          "#05050E"),
        D([cp("15:38")], lambda w, h: A.veil_rent("vr1", w, h, 1538), "#1A1018", head="The Veil of the Temple"),
        F([cp("15:39", to="he said,"), sy("15:39", frm="Truly")], CENTURION, bg=GOLDEN),
        D([cp("15:40"), cp("15:41")], lambda w, h: A.women_afar("wa1", w, h, 1540), "#05050E"),
        F([cp("15:42"), cp("15:43")], ARIMATHAEA, head="The Tomb Hewn out of a Rock"),
        F([cp("15:44"), cp("15:45")], PILATE_TROUBLED, h=280),
        D([cp("15:46"), cp("15:47")], lambda w, h: A.new_tomb("nt1", w, h, 1546, women=True), "#2A2A4A", art_h=220),
        # Mark 16
        D([cp("16:1"), cp("16:2"), cp("16:3", to="among themselves,"), sy("16:3", frm="Who shall roll")], lambda w, h: A.spices_dawn("sd2", w, h, 1601), "#3A3A7A",
          head="He Is Risen", stamp=16),
        D([cp("16:4")], lambda w, h: A.stone_back("sb1", w, h, 1604), "#5A6A9A"),
        D([cp("16:5")], lambda w, h: A.young_man("ym1", w, h, 1605), "#2A2220", art_h=240),
        D([cp("16:6", to="unto them,"), sy("16:6", frm="Be not amazed:"), sy("16:7")], lambda w, h: A.linen("ln1", w, h, 1606), "#2A2220"),
        D([cp("16:8")], lambda w, h: A.stone_back("sb2", w, h, 1608, women=False, fled=True), "#5A6A9A"),
        D([cp("16:9"), cp("16:10"), cp("16:11")], lambda w, h: A.mourners("mr1", w, h, 1609), "#5A4A4A", head="He Appeared First to Mary Magdalene", art_h=260),
        D([cp("16:12"), cp("16:13")], lambda w, h: A.two_country("tc1", w, h, 1612), "#5A3A6A"),
        D([cp("16:14")], lambda w, h: A.eleven_meat("em1", w, h, 1614), "#6A5A4A", head="Go Ye into All the World"),
        F([cp("16:15", to="said unto them,"), sy("16:15", frm="Go ye"), sy("16:16"), sy("16:17"), sy("16:18")], JESUS_RISEN, bg=RISEN_LIGHT),
        D([cp("16:19")], lambda w, h: A.received_up("ru1", w, h, 1619), "#2A3A7A", art_h=260),
        D([cp("16:20")], lambda w, h: A.everywhere("ev1", w, h, 1620), "#8FD0E2")]
PG.extend(K.pack(SEGS, "MRK-C09-D", PG.next(), most=4, lone=0.5, end=fin("END OF MARK · NEXT · LUKE")))
