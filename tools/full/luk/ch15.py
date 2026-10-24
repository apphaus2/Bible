"""Luke volume, Chapter 15 — This Do in Remembrance of Me (Luke 22). Every verse, word for word from ref/eng-asv.
The chief priests in council; Satan entered into Judas — words only (Satan never drawn), over the balance and the money; the
man bearing a pitcher of water and the large upper room; the passover: the cup divided, the bread broken — this is my body
which is given for you: this do in remembrance of me — and the cup of the new covenant; the hand of him that betrayeth me
on the table; who is greatest — I am in the midst of you as he that serveth; thrones judging the twelve tribes; Simon,
Simon, Satan asked to have you (words only); the two swords. The mount of Olives: not my will, but thine; the angel from
heaven strengthening him — a figure of white light, Jesus kneeling far off; the sweat as great drops of blood told in words
only over the dark garden; the disciples sleeping for sorrow. The multitude and the kiss; the servant's ear struck off and
healed — the sword in the torchlight, the blow and the healing in words, no blood; this is your hour, and the power of
darkness. Peter at the fire, the maid, the second and the third; the cock; the Lord turned and looked upon Peter; wept
bitterly. The mocking, the blindfold and the blows in words over the shut door; the council at day — Ye say that I am."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art12 as A, ch14 as _prev
from luk.common import (K, Pages, D, F, Q, N, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        JESUS_PASSION, PETER, PETER_GRIEF, ANDREW, CAIAPHAS, CAIAPHAS_RENT)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C15-00-Title", "Chapter 15 · This Do in Remembrance of Me", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A1E1A"></rect><g transform="translate(0 300)">{A.supper("t15", 760, 780, 2201, bread=True)}</g>'
    return title(15, "This Do in Remembrance of Me", "Luke 22", svg, "#2A1E1A", v("22:19", frm="this do in remembrance of me."))


SEGS = [D([cp("22:1"), cp("22:2")], lambda w, h: A.priests_court("pc1", w, h, 2201), "#2A1A2A", head="The Feast of Unleavened Bread", sky=22),
        D([cp("22:3"), cp("22:4"), cp("22:5"), cp("22:6")], lambda w, h: A.silver("sv1", w, h, 2202), "#2A1E1A"),
        D([cp("22:7"), N("22:8", "saying,")], lambda w, h: A.pitcher("pt1", w, h, 2203), "#C8A878", head="A Large Upper Room Furnished"),
        F([N("22:9", "said unto him,")], PETER),
        F([N("22:10", "said unto them,"), sy("22:11"), sy("22:12")]),
        D([cp("22:13")], lambda w, h: A.guest_chamber("gc1", w, h, 2204), "#5A3A2A"),
        D([cp("22:14"), N("22:15", "said unto them,"), sy("22:16")], lambda w, h: A.supper("su1", w, h, 2205), "#2A1E1A", head="This Do in Remembrance of Me"),
        D([Q("22:17", "c", "he said,", "s"), sy("22:18")], lambda w, h: A.supper("su2", w, h, 2206, cupup=True), "#2A1E1A"),
        D([Q("22:19", "c", "saying,", "s")], lambda w, h: A.supper("su3", w, h, 2207, bread=True), "#2A1E1A", art_h=240),
        D([Q("22:20", "c", "saying,", "s")], lambda w, h: A.supper("su4", w, h, 2208, cupup=True), "#2A1E1A", art_h=240),
        F([sy("22:21"), sy("22:22")], JESUS_GRIEF, bg=COLD),
        D([cp("22:23"), cp("22:24")], lambda w, h: A.supper("su5", w, h, 2209), "#2A1E1A", head="As He That Serveth"),
        F([N("22:25", "said unto them,"), sy("22:26"), sy("22:27")], JESUS_TEACH),
        D([sy("22:28"), sy("22:29"), sy("22:30")], lambda w, h: A.thrones("th1", w, h, 2210), "#1A1630"),
        F([sy("22:31"), sy("22:32")], JESUS_GRIEF, bg=COLD, head="Simon, Simon"),
        F([N("22:33", "said unto him,")], PETER),
        F([N("22:34", "And he said,")], JESUS_GRIEF, bg=COLD),
        F((q35 := Q("22:35", "c", "said unto them,", "s", "lacked ye anything?", "c", "And they said,", "s"))[:2], JESUS),
        F(q35[2:], ANDREW, bg=COLD, ref="LUKE 22:35"),
        F([N("22:36", "said unto them,"), sy("22:37")], JESUS_STERN, bg=RED),
        D([Q("22:38", "c", "And they said,", "s", "two swords.", "c", "said unto them,", "s")], lambda w, h: A.two_swords("ts1", w, h, 2211), "#2A1E1A", art_h=220),
        D([cp("22:39"), N("22:40", "said unto them,")], lambda w, h: A.olivet_night("on1", w, h, 2212), NIGHT, head="Not My Will, but Thine, Be Done"),
        D([cp("22:41"), Q("22:42", "c", "saying,", "s")], lambda w, h: A.gethsemane("gs1", w, h, 2213, sleeping=False), "#05051A", art_h=240),
        D([cp("22:43")], lambda w, h: A.strengthened("sg1", w, h, 2214), "#05051A", art_h=260),
        D([cp("22:44")], lambda w, h: A.gethsemane("gs2", w, h, 2215, sleeping=False), "#05051A", art_h=260),
        D([cp("22:45"), N("22:46", "said unto them,")], lambda w, h: A.gethsemane("gs3", w, h, 2216), "#05051A"),
        D([cp("22:47")], lambda w, h: A.arrest("ar1", w, h, 2247), "#05051A", head="Betrayest Thou the Son of Man with a Kiss?"),
        F([N("22:48", "said unto him,")], JESUS_PASSION, bg=COLD),
        D([N("22:49", "they said,"), cp("22:50")], lambda w, h: A.arrest("ar2", w, h, 2249, sword=True), "#05051A"),
        F([Q("22:51", "c", "answered and said,", "s", "thus far.", "c")], JESUS_PASSION, bg=COLD),
        F([N("22:52", "come against him,"), sy("22:53")], JESUS_PASSION, bg=COLD),
        D([cp("22:54"), cp("22:55")], lambda w, h: A.court_fire("cf1", w, h, 2254, maid=False), "#05051A", head="Peter Followed Afar Off"),
        D([N("22:56", "upon him, said,"), N("22:57", "denied, saying,")], lambda w, h: A.court_fire("cf2", w, h, 2256), "#05051A"),
        D([Q("22:58", "c", "saw him, and said,", "s", "one of them.", "c", "But Peter said,", "s")], lambda w, h: A.court_fire("cf3", w, h, 2258, porch=True), "#05051A"),
        D([N("22:59", "affirmed, saying,"), Q("22:60", "c", "But Peter said,", "s", "what thou sayest.", "c")], lambda w, h: A.cockcrow("cc1", w, h, 2259), "#1A1A3A"),
        F([cp("22:61", to="looked upon Peter.")], JESUS_PASSION, bg=COLD),
        F([cp("22:61", frm="And Peter remembered"), cp("22:62")], PETER_GRIEF, bg=COLD),
        D([cp("22:63"), N("22:64", "asked him, saying,"), cp("22:65")], lambda w, h: A.shut_door("sd1", w, h, 2263), "#2A2228", head="Ye Say That I Am"),
        D([cp("22:66")], lambda w, h: A.caiaphas_hall("ch1", w, h, 2266), "#2A1A2A"),
        F((q67 := Q("22:67", "s", "tell us.", "c", "said unto them,", "s"))[:1], CAIAPHAS, bg=RED),
        F([q67[1:], sy("22:68"), sy("22:69")], JESUS_PASSION, bg=COLD, ref="LUKE 22:67–69"),
        F((q70 := Q("22:70", "c", "And they all said,", "s", "Son of God?", "c", "said unto them,", "s"))[:2], CAIAPHAS_RENT, bg=RED),
        F(q70[2:], JESUS_PASSION, bg=COLD, ref="LUKE 22:70"),
        F([N("22:71", "And they said,")], CAIAPHAS_RENT, bg=RED)]
PG.extend(K.pack(SEGS, "LUK-C15-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · FATHER, INTO THY HANDS")))
