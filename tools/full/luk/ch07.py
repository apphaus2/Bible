"""Luke volume, Chapter 7 — Thou Art the Christ (Luke 9). Every verse, word for word from ref/eng-asv.
The twelve sent forth with nothing for the journey, the dust shaken off, the sick healed in the villages; Herod perplexed
beside his face — John I beheaded (words only). Bethsaida and the desert place: five loaves and two fishes, the companies of
fifty, twelve baskets. Praying apart: who say ye that I am? — The Christ of God, beside Peter's face; the Son of man must
suffer; take up his cross daily. The mountain: his raiment white and dazzling, Moses and Elijah in glory, the three heavy
with sleep, the three tabernacles, the cloud and the Father's voice in the Voice box (nothing drawn in the cloud), Jesus
found alone. The boy below: the spirit never drawn — the father's words beside his face, the throwing down told in words
over the ring of the multitude, the boy given back to his father at peace. The little child by his side; Forbid him not.
His face set to go to Jerusalem; the village of the Samaritans that would not receive him, James and John and the fire from
heaven rebuked; the foxes have holes; leave the dead to bury their own dead; the hand to the plow."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art5 as A, ch06 as _prev
from luk.common import (K, Pages, D, F, Q, N, T, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, ANDREW, JAMES, JOHN, PHILIP, HEROD, HEROD_SORRY, FATHER_BOY, CROWD_MAN)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C07-00-Title", "Chapter 7 · Thou Art the Christ", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A6A"></rect><g transform="translate(0 300)">{A.transfigured("t7", 760, 780, 901)}</g>'
    return title(7, "Thou Art the Christ", "Luke 9", svg, "#2A2A6A", v("9:20", frm="The Christ of God."))


SEGS = [D([cp("9:1"), cp("9:2"), N("9:3", "said unto them,")], lambda w, h: A.sent_forth("sf1", w, h, 901), "#8FD0E2", head="Take Nothing for Your Journey", sky=9),
        D([sy("9:4"), sy("9:5"), cp("9:6")], lambda w, h: A.dust_gate("dg1", w, h, 902), "#C8A890"),
        F([cp("9:7"), cp("9:8")], HEROD_SORRY, bg=COLD, head="Who Is This?"),
        F([Q("9:9", "c", "And Herod said,", "s", "such things?", "c")], HEROD, bg=RED),
        D([cp("9:10"), cp("9:11")], lambda w, h: A.desert_place("dp1", w, h, 903), "#8FD0E2", head="Give Ye Them to Eat"),
        D([N("9:12", "said unto him,")], lambda w, h: A.five_loaves("fl0", w, h, 904), "#D8B860"),
        F((q13 := Q("9:13", "c", "said unto them,", "s", "Give ye them to eat.", "c", "And they said,", "s"))[:2], JESUS),
        F(q13[2:], PHILIP, bg=COLD, ref="LUKE 9:13"),
        D([Q("9:14", "c", "unto his disciples,", "s"), cp("9:15")], lambda w, h: A.companies("cm1", w, h, 905), "#8AB84A", art_h=240),
        D([cp("9:16")], lambda w, h: A.five_loaves("fl1", w, h, 906), "#D8B860", art_h=240),
        D([cp("9:17")], lambda w, h: A.baskets("bk1", w, h, 907), "#8AB84A"),
        D([N("9:18", "asked them, saying,")], lambda w, h: A.caesarea("cs1", w, h, 908), "#8FD0E2", head="Who Say Ye That I Am?"),
        F([N("9:19", "answering said,")], ANDREW, bg=COLD),
        F((q20 := Q("9:20", "c", "said unto them,", "s", "that I am?", "c", "answering said,", "s"))[:2], JESUS),
        F(q20[2:], PETER, ref="LUKE 9:20"),
        F([cp("9:21"), Q("9:22", "c", "saying,", "s")], JESUS_GRIEF, bg=COLD),
        F([N("9:23", "said unto all,"), sy("9:24"), sy("9:25")], JESUS_TEACH, head="Take Up His Cross Daily"),
        D([sy("9:26"), sy("9:27")], lambda w, h: A.clouds_glory("cg1", w, h, 909), "#2A2A6A"),
        D([cp("9:28"), cp("9:29")], lambda w, h: A.transfigured("tf1", w, h, 910), "#2A2A6A", head="His Raiment Became White and Dazzling", art_h=240),
        D([cp("9:30"), cp("9:31"), cp("9:32")], lambda w, h: A.transfigured("tf2", w, h, 911), "#2A2A6A"),
        F([Q("9:33", "c", "Peter said unto Jesus,", "s", "one for Elijah:", "c")], PETER, bg=GOLDEN),
        D([cp("9:34"), N("9:35", "saying,", "g")], lambda w, h: A.transfigured("tf3", w, h, 912, cloud=True), "#E8E2D6", art_h=240),
        D([cp("9:36")], lambda w, h: A.transfigured("tf4", w, h, 913, after=True), "#2A2A6A"),
        D([cp("9:37")], lambda w, h: A.foot_mountain("fm1", w, h, 914), "#8FD0E2", head="I Beseech Thee, Look upon My Son"),
        F([N("9:38", "cried, saying,"), sy("9:39"), sy("9:40")], FATHER_BOY, bg=COLD),
        F([N("9:41", "answered and said,")], JESUS_STERN, bg=RED),
        D([cp("9:42", to="tare him grievously.")], lambda w, h: A.crowd_ring("cr1", w, h, 915), "#8FD0E2"),
        D([cp("9:42", frm="But Jesus rebuked")], lambda w, h: A.boy_healed("bh1", w, h, 916, kneeling=False), "#8FD0E2"),
        F([N("9:43", "said unto his disciples,"), sy("9:44"), cp("9:45")], JESUS_GRIEF, bg=COLD),
        D([cp("9:46"), cp("9:47"), N("9:48", "said unto them,")], lambda w, h: A.child_midst("ch1", w, h, 917), "#C8A878", head="He That Is Least among You", art_h=220),
        F([N("9:49", "answered and said,")], JOHN, bg=GOLDEN),
        F([N("9:50", "said unto him,")], JESUS),
        D([cp("9:51"), cp("9:52")], lambda w, h: A.to_jerusalem("tj1", w, h, 918), "#4A3A6A", head="He Stedfastly Set His Face", art_h=220),
        D([cp("9:53")], lambda w, h: A.samaritan_village("sv1", w, h, 919), "#4A3A6A"),
        F([N("9:54", "they said,")], JAMES, bg=RED),
        D([cp("9:55"), cp("9:56")], lambda w, h: A.samaritan_village("sv2", w, h, 920), "#4A3A6A"),
        D([N("9:57", "said unto him,"), N("9:58", "said unto him,")], lambda w, h: A.foxes("fx1", w, h, 921), "#4A2A5A", head="Follow Me"),
        F((q59 := Q("9:59", "c", "said unto another,", "s", "Follow me.", "c", "But he said,", "s"))[:2], JESUS),
        F(q59[2:], CROWD_MAN, bg=COLD, ref="LUKE 9:59"),
        F([N("9:60", "said unto him,")], JESUS),
        F([N("9:61", "And another also said,")], CROWD_MAN, bg=COLD),
        D([N("9:62", "said unto him,")], A.footed(lambda w, h: A.plough("pl1", w, h, 922), "#6A4A3A"), "#4A3A6A", art_h=260)]
PG.extend(K.pack(SEGS, "LUK-C07-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THE GOOD SAMARITAN")))
