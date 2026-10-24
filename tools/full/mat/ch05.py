"""Matthew volume, Chapter 5 — The Kingdom of Heaven Is Like (Matthew 13–14). Every verse, word for word from ref/eng-asv.
Jesus seated in the boat off the beach; the parables drawn as their own scenes with his words over them: the sower and the
four grounds, the field at night where the tares were sown (no one drawn), the wheat and the tares, the reapers and the
fire, the mustard tree, the leaven, the treasure, the pearl, the net; Isaiah's words in song boxes beside his face; the
furnace of fire is only fire. Nazareth's synagogue. Herod the tetrarch beside his face; John's imprisonment, Herod's feast
(the dance in words over the empty floor), his death in words over the prison door and his burial over the tomb. The desert
place, the five loaves and two fishes, the twelve baskets; Jesus alone on the mountain; walking upon the sea, Peter caught
by the hand, the wind ceased; Gennesaret."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mat import G, art5 as A, ch04 as _prev
from mat.common import (K, Pages, drawn, cp, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, HEROD)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MAT-C05-00-Title", "Chapter 5 · The Kingdom of Heaven Is Like", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.sower("t5", 760, 780, 1301)}</g>'
    return title(5, "The Kingdom of Heaven Is Like", "Matthew 13 – 14", svg, "#2A3A5A", v("13:31", frm="The kingdom"))


def D(lines, fn, bg, **k): return drawn(lines, fn, bg, **{"art_h": 180, "size": 14, **k})
def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)
def S(a, b):
    ch, x = a.split(":")
    return [sy(f"{ch}:{k}") for k in range(int(x), int(b) + 1)]

SEGS = [D([cp("13:1"), cp("13:2"), cp("13:3", to="saying,"), sy("13:3", frm="Behold, the sower")], lambda w, h: A.boat_preach("bp1", w, h, 1301), "#8FD0E2", head="The Sower", stamp=13),
        D(S("13:4", 9), lambda w, h: A.sower("so1", w, h, 1302), "#8FD0E2", art_h=240),
        F([cp("13:10", to="said unto him,"), sy("13:10", frm="Why speakest")], PETER),
        F([cp("13:11", to="said unto them,"), sy("13:11", frm="Unto you"), sy("13:12"), sy("13:13")]),
        F([sy("13:14", to="which saith,"), sg("13:14", frm="By hearing"), sg("13:15")], JESUS_GRIEF, bg=COLD),
        F(S("13:16", 17), JESUS),
        F(S("13:18", 21)),
        D(S("13:22", 23), lambda w, h: A.harvest("hv2", w, h, 1303), "#5A3A6A"),
        D([cp("13:24", to="saying,"), sy("13:24", frm="The kingdom"), sy("13:25")], lambda w, h: A.tares_night("tn1", w, h, 1304), NIGHT, head="The Tares of the Field"),
        D(S("13:26", 28), lambda w, h: A.tares_field("tf1", w, h, 1305), "#8FD0E2"),
        D(S("13:29", 30), lambda w, h: A.reapers("rp1", w, h, 1306), "#5A3A6A"),
        D([cp("13:31", to="saying,"), sy("13:31", frm="The kingdom"), sy("13:32")], lambda w, h: A.mustard("ms1", w, h, 1307), "#8FD0E2", head="A Grain of Mustard Seed"),
        D([cp("13:33", to="unto them;"), sy("13:33", frm="The kingdom")], lambda w, h: A.leaven("lv1", w, h, 1308), "#C8A878"),
        F([cp("13:34"), cp("13:35", to="saying,"), sg("13:35", frm="I will open")], JESUS),
        F([cp("13:36", to="saying,"), sy("13:36", frm="Explain")], PETER),
        F([cp("13:37", to="answered and said,"), sy("13:37", frm="He that soweth"), sy("13:38"), sy("13:39")]),
        D(S("13:40", 42), lambda w, h: A.furnace("fu1", w, h, 1309), "#1A0A08"),
        D(S("13:43", 43), lambda w, h: A.sun_field("sf1", w, h, 1310), "#FFE680"),
        D(S("13:44", 44), lambda w, h: A.treasure_field("tr1", w, h, 1311), "#8FD0E2", head="The Pearl of Great Price"),
        D(S("13:45", 46), lambda w, h: A.pearl("pl1", w, h, 1312), "#3A2A5A"),
        D(S("13:47", 48), lambda w, h: A.dragnet("dn1", w, h, 1313), "#8FD0E2"),
        F(S("13:49", 50), JESUS_STERN, bg=RED),
        D([sy("13:51", to="these things?"), cp("13:51", frm="They say unto him,", to="They say unto him,"), sy("13:51", frm="Yea."), cp("13:52", to="said unto them,"),
           sy("13:52", frm="Therefore every")], lambda w, h: A.at_meat("am2", w, h, 1314), "#8A6A4A"),
        D([cp("13:53"), cp("13:54", to="and said,"), sy("13:54", frm="Whence hath"), sy("13:55"), sy("13:56")], lambda w, h: A.synagogue("sg1", w, h, 1315), "#C8B490",
          head="A Prophet Is Not without Honor"),
        F([cp("13:57", to="said unto them,"), sy("13:57", frm="A prophet"), cp("13:58")], JESUS_GRIEF, bg=COLD),
        # Matthew 14
        F([cp("14:1"), cp("14:2", to="unto his servants,"), sy("14:2", frm="This is John")], HEROD, bg=RED, head="John the Baptist", stamp=14),
        D([cp("14:3"), cp("14:4", to="unto him,"), sy("14:4", frm="It is not lawful"), cp("14:5")], lambda w, h: A.prison("pr2", w, h, 1401), "#2A2A4A"),
        D([cp("14:6"), cp("14:7"), cp("14:8", to="saith,"), sy("14:8", frm="Give me")], lambda w, h: A.feast_hall("fh1", w, h, 1402), "#2A1A2A"),
        D([cp("14:9"), cp("14:10"), cp("14:11")], lambda w, h: A.prison_door("pd2", w, h, 1403), "#5A5048"),
        D([cp("14:12")], lambda w, h: A.tomb("tm1", w, h, 1404), "#3A2A4A"),
        D([cp("14:13"), cp("14:14")], lambda w, h: A.desert_place("dp1", w, h, 1405), "#8FD0E2", head="Five Loaves and Two Fishes"),
        D([cp("14:15", to="saying,"), sy("14:15", frm="The place"), cp("14:16", to="said unto them,"), sy("14:16", frm="They have no"), cp("14:17", to="unto him,"),
           sy("14:17", frm="We have here"), cp("14:18", to="he said,"), sy("14:18", frm="Bring them"), cp("14:19")], lambda w, h: A.five_loaves("fl1", w, h, 1406), "#5A3A6A", art_h=240),
        D([cp("14:20"), cp("14:21")], lambda w, h: A.baskets("bk1", w, h, 1407), "#3A2A5A"),
        D([cp("14:22"), cp("14:23")], lambda w, h: A.mount_alone("ma1", w, h, 1408), NIGHT),
        D([cp("14:24"), cp("14:25"), cp("14:26", to="saying,"), sy("14:26", frm="It is a ghost;", to="It is a ghost;"), cp("14:26", frm="and they cried")],
          lambda w, h: A.on_the_sea("os1", w, h, 1409), "#0B0B2A"),
        F([cp("14:27", to="saying,"), sy("14:27", frm="Be of good")], JESUS),
        F([cp("14:28", to="answered him and said,"), sy("14:28", frm="Lord, if")], PETER, bg=COLD),
        D([cp("14:29", to="he said,"), sy("14:29", frm="Come.", to="Come."), cp("14:29", frm="And Peter went"), cp("14:30", to="saying,"), sy("14:30", frm="Lord, save me.")],
          lambda w, h: A.on_the_sea("os2", w, h, 1410, peter=True), "#0B0B2A"),
        F([cp("14:31", to="saith unto him,"), sy("14:31", frm="O thou of")], JESUS_GRIEF, bg=COLD),
        D([cp("14:32"), cp("14:33", to="saying,"), sy("14:33", frm="Of a truth")], lambda w, h: A.on_the_sea("os3", w, h, 1411, calm=True), "#2A2A6A"),
        D([cp("14:34"), cp("14:35"), cp("14:36")], lambda w, h: A.gennesaret("gn1", w, h, 1412), "#8FD0E2")]
PG.extend(K.pack(SEGS, "MAT-C05-D", PG.next(), most=4, end=nxt("NEXT · THOU ART THE CHRIST")))
