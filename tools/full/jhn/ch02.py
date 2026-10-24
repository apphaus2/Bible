"""John volume, Chapter 2 — Ye Must Be Born Anew (John 3–4). Every verse, word for word from ref/eng-asv.
Nicodemus by night: the two sitting on a Jerusalem roof under the lamp, the city dark below; their words beside their faces
in the night light; the wind blowing through the olive trees in the dark; the serpent of brass lifted up on its standard
over the camp; God so loved the world — the whole land under the dawn; the light come into the world, the shut doors and
the open. John at Ænon and the disciples baptizing in Judæa; the friend of the bridegroom at the lit door. Samaria: the road
between the mountains; Jacob's well at the sixth hour, Jesus wearied, sitting by it; the woman with her waterpot, the
living water, the five husbands told in words only beside her face, the mountain of worship; I that speak unto thee am he;
the disciples marvelling; the waterpot left on the well-head and the woman running to the city; the fields white unto
harvest, the reapers; the Samaritans at the gate of Sychar. Galilee: the nobleman at Cana, the servants on the road down,
the son standing whole in the house at Capernaum."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jhn import G, art2 as A, ch01 as _prev
from jhn.common import (K, Pages, D, F, S, said, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, NIGHTF, JESUS, JESUS_TEACH, JESUS_STERN,
                        BAPTIST, BAPTIST_HUMBLE, JOHN_DISC, NICODEMUS, SAMARITAN, SAMARITAN_AWE, PETER, ANDREW, NOBLEMAN)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JHN-C02-00-Title", "Chapter 2 · Ye Must Be Born Anew", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#05051A"></rect><g transform="translate(0 220)">{A.roof_night("t2", 760, 680, 301)}</g><rect x="0" y="900" width="760" height="180" fill="#4A4060"></rect>'
    return title(2, "Ye Must Be Born Anew", "John 3 – 4", svg, "#05051A", v("3:7", frm="Ye must be born anew."))


W = lambda kind, seed: (lambda w, h: A.word_light(f"wl{seed}", w, h, seed, kind))
SEGS = [D([cp("3:1"), cp("3:2", to="by night,")], lambda w, h: A.roof_night("rn1", w, h, 302), "#05051A", head="Nicodemus by Night", sky=3, art_h=260),
        F([cp("3:2", frm="and said to him,", to="said to him,"), sy("3:2", frm="Rabbi,")], NICODEMUS, bg=NIGHTF),
        F([said("3:3", "said unto him,", "Verily,")], JESUS_TEACH, bg=NIGHTF),
        F([said("3:4", "saith unto him,", "How can")], NICODEMUS, bg=NIGHTF),
        F([said("3:5", "Jesus answered,", "Verily,"), sy("3:6"), sy("3:7")], JESUS, bg=NIGHTF),
        D([sy("3:8")], lambda w, h: A.wind_night("wn1", w, h, 303), "#0B0B2A", art_h=220),
        F([said("3:9", "said unto him,", "How can")], NICODEMUS, bg=NIGHTF),
        F([said("3:10", "said unto him,", "Art thou"), sy("3:11"), sy("3:12")], JESUS_TEACH, bg=NIGHTF),
        D([sy("3:13"), sy("3:14"), sy("3:15")], lambda w, h: A.serpent_lifted("sl1", w, h, 304), "#3A2A4A", head="The Son of Man Lifted Up", art_h=260),
        D([sy("3:16"), sy("3:17")], lambda w, h: A.world_light("wl1", w, h, 305), "#3A4A8A", head="God So Loved the World", art_h=240),
        F([sy("3:18")], JESUS),
        D([sy("3:19"), sy("3:20")], lambda w, h: A.shut_doors("sd3", w, h, 306), "#05051A"),
        D([sy("3:21")], lambda w, h: A.shut_doors("sd4", w, h, 307, open_=True), "#05051A"),
        D([cp("3:22")], lambda w, h: A.judaea_water("jw1", w, h, 308), "#8FD0E2", head="He Must Increase"),
        D([cp("3:23"), cp("3:24")], lambda w, h: A.judaea_water("jw2", w, h, 309, john=True), "#8FD0E2"),
        F([cp("3:25"), said("3:26", "said to him,", "Rabbi,")], JOHN_DISC),
        F([said("3:27", "John answered and said,", "A man can"), sy("3:28")], BAPTIST_HUMBLE),
        D([sy("3:29")], lambda w, h: A.bridegroom("bg1", w, h, 310), "#0B0B2A", art_h=240),
        F([sy("3:30"), sy("3:31")], BAPTIST_HUMBLE),
        D([sy("3:32"), sy("3:33"), sy("3:34"), sy("3:35"), sy("3:36")], W("glory", 311), "#FFC14D"),
        # John 4
        D([cp("4:1"), cp("4:2"), cp("4:3"), cp("4:4")], lambda w, h: A.samaria_road("sr1", w, h, 401), "#8FD0E2", head="Jacob's Well", sky=4),
        D([cp("4:5"), cp("4:6")], lambda w, h: A.jacobs_well("jw3", w, h, 402), "#7AC0E0"),
        D([cp("4:7", to="saith unto her,"), sy("4:7", frm="Give me to drink."), cp("4:8")], lambda w, h: A.jacobs_well("jw4", w, h, 403, stage="woman"), "#7AC0E0",
          head="The Woman of Samaria", art_h=240),
        F([cp("4:9", to="therefore saith unto him,"), sy("4:9", frm="How is it", to="Samaritan woman?"), cp("4:9", frm="(For Jews")], SAMARITAN),
        F([said("4:10", "said unto her,", "If thou")], JESUS),
        F([said("4:11", "saith unto him,", "Sir,"), sy("4:12")], SAMARITAN),
        D([said("4:13", "said unto her,", "Every one"), sy("4:14")], lambda w, h: A.jacobs_well("jw5", w, h, 404, stage="talk"), "#7AC0E0", head="Living Water"),
        F([said("4:15", "saith unto him,", "Sir,")], SAMARITAN),
        F([said("4:16", "saith unto her,", "Go,")], JESUS_TEACH),
        F([cp("4:17", to="said unto him,"), sy("4:17", frm="I have no husband.", to="I have no husband.")], SAMARITAN),
        F([cp("4:17", frm="Jesus saith", to="unto her,"), sy("4:17", frm="Thou saidst well,"), sy("4:18")], JESUS),
        F([said("4:19", "saith unto him,", "Sir,"), sy("4:20")], SAMARITAN_AWE),
        F([said("4:21", "saith unto her,", "Woman,"), sy("4:22")], JESUS_TEACH, head="In Spirit and Truth"),
        D([sy("4:23"), sy("4:24")], lambda w, h: A.jacobs_well("jw6", w, h, 405, stage="talk"), "#7AC0E0"),
        F([said("4:25", "saith unto him,", "I know")], SAMARITAN_AWE),
        F([said("4:26", "saith unto her,", "I that speak")], JESUS),
        D([cp("4:27")], lambda w, h: A.jacobs_well("jw7", w, h, 406, stage="disciples"), "#7AC0E0"),
        D([cp("4:28"), sy("4:29"), cp("4:30")], lambda w, h: A.jacobs_well("jw8", w, h, 407, stage="left"), "#7AC0E0"),
        F([said("4:31", "saying,", "Rabbi, eat.")], PETER, head="My Meat"),
        F([said("4:32", "said unto them,", "I have meat")], JESUS),
        F([said("4:33", "one to another,", "Hath any")], ANDREW),
        F([said("4:34", "saith unto them,", "My meat")], JESUS_TEACH),
        D([sy("4:35")], lambda w, h: A.white_fields("wf1", w, h, 408), "#8FD0E2", head="White unto Harvest", art_h=260),
        D([sy("4:36"), sy("4:37"), sy("4:38")], lambda w, h: A.reaping("rp1", w, h, 409), "#5A3A6A"),
        D([cp("4:39", to="who testified,"), sy("4:39", frm="He told me"), cp("4:40")], lambda w, h: A.sychar_gate("sg1", w, h, 410), "#8FD0E2"),
        D([cp("4:41"), cp("4:42", to="said to the woman,"), sy("4:42", frm="Now we believe")], lambda w, h: A.sychar_gate("sg2", w, h, 411, believe=True), "#8FD0E2"),
        D([cp("4:43"), cp("4:44"), cp("4:45")], lambda w, h: A.galilee("gl2", w, h, 412), "#8FD0E2", head="Thy Son Liveth"),
        D([cp("4:46"), cp("4:47")], lambda w, h: A.nobleman_cana("nc1", w, h, 413), "#8FD0E2", art_h=240),
        F([said("4:48", "said unto him,", "Except")], JESUS_STERN, bg=RED),
        F([said("4:49", "saith unto him,", "Sir,")], NOBLEMAN, bg=COLD),
        F([cp("4:50", to="saith unto him,"), sy("4:50", frm="Go thy way;", to="thy son liveth."), cp("4:50", frm="The man believed")], JESUS),
        D([cp("4:51"), cp("4:52", to="said therefore unto him,"), sy("4:52", frm="Yesterday")], lambda w, h: A.servants_meet("sm1", w, h, 414), "#8FD0E2", art_h=220),
        D([cp("4:53"), cp("4:54")], lambda w, h: A.whole_house("wh1", w, h, 415), "#C8A878", art_h=240)]
PG.extend(K.pack(SEGS, "JHN-C02-D", PG.next(), end=nxt("NEXT · THE BREAD OF LIFE")))
