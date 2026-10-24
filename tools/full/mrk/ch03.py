"""Mark volume, Chapter 3 — Talitha Cumi (Mark 5:1–6:29). Every verse, word for word from ref/eng-asv.
The country of the Gerasenes: the man of the tombs is told in words only, over the empty tombs at night and the chains and
fetters broken on the rocks; the cries and the name Legion stand over the tombs and beside Jesus' face, and the unclean
spirits are never drawn. The swine feeding on the mountain side, the herd running down the steep at a distance, the drowning
in words over the empty sea; the keepers at the city; then the man sitting at Jesus' feet, clothed and in his right mind,
the people standing off afraid; his asking, and his road through Decapolis. Jaïrus at his feet by the sea; the woman in the
crowd behind, touching his garment; Who touched my garments?; the word from the house; the tumult, the weeping; Talitha
cumi, the damsel risen from her bed, walking. Nazareth, the synagogue, the carpenter; the twelve sent two and two, the dust
shaken off, the sick anointed with oil. Herod and John: Herod's words beside his face; the prison on its hill; Herodias
beside her face; the birthday supper in the hall with the floor left empty (the dance in words only); the asking and the
answer over the empty doorway of the palace; Herod's sorrow beside his face; the beheading in words only, over the prison
door shut and barred (nothing of the head or the platter drawn); John's disciples and the tomb."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mrk import G, art3 as A, ch02 as _prev
from mrk.common import (K, Pages, D, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, HEROD, CROWD_MAN, JAIRUS, ISSUE, ISSUE_HEALED, GERASENE_PLEAD, HERODIAS, HEROD_SORRY, BAPTIST)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MRK-C03-00-Title", "Chapter 3 · Talitha Cumi", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8A6A4A"></rect><g transform="translate(0 290)">{A.talitha("t3", 760, 640, 501, tall=0.5)}</g>'
    return title(3, "Talitha Cumi", "Mark 5:1 – 6:29", svg, "#3A2A2A", v("5:41", frm="Damsel, I say"))


def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)

SEGS = [D([cp("5:1"), cp("5:2"), cp("5:3"), cp("5:4"), cp("5:5")], lambda w, h: A.empty_tombs("et1", w, h, 501), NIGHT, head="My Name Is Legion", stamp=5, art_h=220),
        D([cp("5:6"), cp("5:7", to="he saith,"), sy("5:7", frm="What have I")], lambda w, h: A.tombs("tb1", w, h, 502, men=False), "#6A6A8A"),
        F([cp("5:8", to="said unto him,"), sy("5:8", frm="Come forth,"), cp("5:9", to="And he asked him,"), sy("5:9", frm="What is thy name?", to="What is thy name?")],
          JESUS_STERN, bg=RED),
        D([cp("5:9", frm="And he saith", to="unto him,"), sy("5:9", frm="My name is Legion;"), cp("5:10")], lambda w, h: A.empty_tombs("et2", w, h, 509, night=False), "#6A6A8A"),
        D([cp("5:11"), cp("5:12", to="saying,"), sy("5:12", frm="Send us")], lambda w, h: A.tombs("tb2", w, h, 503, men=False, jesus_=False, swine=True), "#6A6A8A"),
        D([cp("5:13", to="about two thousand;")], lambda w, h: A.swine_steep("sw1", w, h, 504), "#6A6A8A"),
        D([cp("5:13", frm="and they were drowned")], lambda w, h: A.empty_sea("es1", w, h, 505), "#5A5A7A"),
        D([cp("5:14")], lambda w, h: A.city_gate("cg1", w, h, 506, crowd_n=7), "#8FD0E2", head="Clothed, and in His Right Mind"),
        D([cp("5:15"), cp("5:16"), cp("5:17")], lambda w, h: A.gerasene_sitting("gs1", w, h, 507), "#8FD0E2", art_h=220),
        F([cp("5:18")], GERASENE_PLEAD),
        F([cp("5:19", to="saith unto him,"), sy("5:19", frm="Go to thy house")], JESUS),
        D([cp("5:20")], lambda w, h: A.decapolis("dp1", w, h, 508), "#8FD0E2"),
        D([cp("5:21"), cp("5:22")], lambda w, h: A.jairus_feet("jf1", w, h, 509), "#8FD0E2", head="Who Touched My Garments?"),
        F([cp("5:23", to="saying,"), sy("5:23", frm="My little daughter")], JAIRUS, bg=COLD),
        D([cp("5:24"), cp("5:25"), cp("5:26"), cp("5:27")], lambda w, h: A.border("bd1", w, h, 510), "#8FD0E2", art_h=220),
        F([cp("5:28", to="she said,"), sy("5:28", frm="If I touch"), cp("5:29")], ISSUE),
        F([cp("5:30", to="and said,"), sy("5:30", frm="Who touched")], JESUS),
        F([cp("5:31", to="said unto him,"), sy("5:31", frm="Thou seest")], PETER),
        D([cp("5:32"), cp("5:33")], lambda w, h: A.border("bd2", w, h, 511), "#8FD0E2"),
        F([cp("5:34", to="said unto her,"), sy("5:34", frm="Daughter,")], JESUS),
        F([cp("5:35", to="saying,"), sy("5:35", frm="Thy daughter is dead:")], CROWD_MAN, bg=COLD, head="The Child Is Not Dead"),
        F([cp("5:36", to="of the synagogue,"), sy("5:36", frm="Fear not,")], JESUS),
        D([cp("5:37"), cp("5:38")], lambda w, h: A.ruler_house("rh1", w, h, 512), "#8FD0E2"),
        F([cp("5:39", to="saith unto them,"), sy("5:39", frm="Why make ye"), cp("5:40")], JESUS_TEACH),
        D([cp("5:41", to="saith unto her,"), sy("5:41", frm="Talitha cumi;", to="Talitha cumi;"), cp("5:41", frm="which is,", to="interpreted,"), sy("5:41", frm="Damsel,"),
           cp("5:42")], lambda w, h: A.talitha("tl1", w, h, 513), "#C8A878", art_h=240),
        F([cp("5:43")], JESUS),
        # Mark 6
        D([cp("6:1")], lambda w, h: A.nazareth("nz1", w, h, 601), "#8FD0E2", head="A Prophet Is Not without Honor", stamp=6),
        D([cp("6:2", to="saying,"), sy("6:2", frm="Whence hath"), sy("6:3", to="here with us?"), cp("6:3", frm="And they were offended")],
          lambda w, h: A.synagogue("sy1", w, h, 602), "#C8B490"),
        F([cp("6:4", to="unto them,"), sy("6:4", frm="A prophet"), cp("6:5"), cp("6:6")], JESUS_GRIEF, bg=COLD),
        D([cp("6:7"), cp("6:8"), cp("6:9", to="said he,"), sy("6:9", frm="put not on")], lambda w, h: A.sent_forth("sf1", w, h, 603), "#8FD0E2", head="By Two and Two"),
        D([cp("6:10", to="unto them,"), sy("6:10", frm="Wheresoever"), sy("6:11")], lambda w, h: A.dust_gate("dg1", w, h, 604), "#C8A890"),
        D([cp("6:12"), cp("6:13")], lambda w, h: A.anoint_sick("as1", w, h, 605), "#8FD0E2"),
        F([cp("6:14", to="and he said,"), sy("6:14", frm="John the Baptizer")], HEROD, bg=RED, head="John Whom I Beheaded"),
        F([cp("6:15", to="But others said,"), sy("6:15", frm="It is Elijah.", to="It is Elijah."), cp("6:15", frm="And others said,", to="And others said,"), sy("6:15", frm="It is a prophet,")],
          CROWD_MAN, h=300),
        F([cp("6:16", to="said,"), sy("6:16", frm="John, whom")], HEROD_SORRY, bg=COLD),
        D([cp("6:17"), cp("6:18", to="unto Herod,"), sy("6:18", frm="It is not lawful")], lambda w, h: A.prison("pr1", w, h, 606), "#2A2A4A"),
        F([cp("6:19")], HERODIAS, bg=RED),
        F([cp("6:20")], HEROD, bg=COLD),
        D([cp("6:21"), cp("6:22", to="unto the damsel,"), sy("6:22", frm="Ask of me"), cp("6:23", to="unto her,"), sy("6:23", frm="Whatsoever")],
          lambda w, h: A.feast_hall("fh1", w, h, 607), "#2A1A2A", head="Herod's Birthday", art_h=220),
        D([cp("6:24", to="unto her mother,"), sy("6:24", frm="What shall I ask?", to="What shall I ask?"), cp("6:24", frm="And she said,", to="And she said,"), sy("6:24", frm="The head of"),
           cp("6:25", to="and asked, saying,"), sy("6:25", frm="I will that")], lambda w, h: A.palace_door("pd1", w, h, 608), "#1E1420", art_h=140),
        F([cp("6:26")], HEROD_SORRY, bg=COLD),
        D([cp("6:27"), cp("6:28")], lambda w, h: A.prison_shut("ps1", w, h, 609), "#2A2428"),
        D([cp("6:29")], lambda w, h: A.tomb("tm1", w, h, 610), "#3A2A4A")]
PG.extend(K.pack(SEGS, "MRK-C03-D", PG.next(), most=4, lone=1.5, end=nxt("NEXT · IT IS I")))
