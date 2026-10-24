"""Matthew volume, Chapter 10 — Gethsemane (Matthew 26). Every verse, word for word from ref/eng-asv.
The council in the court of Caiaphas; the alabaster cruse at Bethany; the thirty pieces of silver on the balance (no one
drawn); the guest-chamber; the last supper — the twelve at the table under the lamps, the bread broken and the cup lifted;
the hymn and the mount of Olives by moonlight; Gethsemane — Jesus fallen on his face alone in a cold light, the three asleep;
the torches and staves; the sword dropped in the torchlight (the blow told in words only); the garden empty; Caiaphas'
hall, Jesus standing silent; the spitting and the blows told in words only over the shut door; Peter by the fire, the maids,
the cock crowing at dawn, Peter weeping beside his face."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mat import G, art10 as A, ch09 as _prev
from mat.common import (K, Pages, drawn, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        JESUS_PASSION, PETER, PETER_GRIEF, JUDAS, JOHN, CAIAPHAS, CAIAPHAS_RENT, PRIEST, MAID, WITNESS)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MAT-C10-00-Title", "Chapter 10 · Gethsemane", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#05051A"></rect><g transform="translate(0 300)">{A.gethsemane("t10", 760, 780, 2601)}</g>'
    return title(10, "Gethsemane", "Matthew 26", svg, "#05051A", v("26:39", frm="My Father,"))


def D(lines, fn, bg, **k): return drawn(lines, fn, bg, **{"art_h": 180, "size": 14, **k})
def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)
GRIEF = dict(tok=JESUS_GRIEF, bg=COLD)

SEGS = [F([cp("26:1"), sy("26:2")], JESUS_GRIEF, bg=COLD, head="The Passover Cometh", stamp=26),
        D([cp("26:3"), cp("26:4"), cp("26:5", to="they said,"), sy("26:5", frm="Not during")], lambda w, h: A.priests_court("pc1", w, h, 2601), "#0B0B2A"),
        D([cp("26:6"), cp("26:7"), cp("26:8", to="saying,"), sy("26:8", frm="To what"), sy("26:9")], lambda w, h: A.anointing("an1", w, h, 2602), "#B8987A", head="For My Burial"),
        F([cp("26:10", to="said unto them,"), sy("26:10", frm="Why trouble"), sy("26:11"), sy("26:12"), sy("26:13")], **GRIEF),
        F([cp("26:14"), cp("26:15", to="and said,"), sy("26:15", frm="What are ye", to="unto you?")], JUDAS, bg=RED, head="Thirty Pieces of Silver"),
        D([cp("26:15", frm="And they weighed"), cp("26:16")], lambda w, h: A.silver("sv1", w, h, 2603), "#1A1630"),
        D([cp("26:17", to="saying,"), sy("26:17", frm="Where wilt"), cp("26:18", to="And he said,"), sy("26:18", frm="Go into"), cp("26:19")],
          lambda w, h: A.guest_chamber("gc1", w, h, 2604), "#8A6A5A", head="The Last Supper"),
        D([cp("26:20"), cp("26:21", to="he said,"), sy("26:21", frm="Verily")], lambda w, h: A.supper("su1", w, h, 2605), "#4A3438"),
        F([cp("26:22", to="every one,"), sy("26:22", frm="Is it I")], JOHN, bg=COLD),
        F([cp("26:23", to="answered and said,"), sy("26:23", frm="He that dipped"), sy("26:24")], **GRIEF),
        F([cp("26:25", to="answered and said,"), sy("26:25", frm="Is it I, Rabbi?", to="Is it I, Rabbi?")], JUDAS, bg=RED),
        F([cp("26:25", frm="He saith unto him,", to="He saith unto him,"), sy("26:25", frm="Thou hast said.")], **GRIEF),
        D([cp("26:26", to="and said,"), sy("26:26", frm="Take, eat;")], lambda w, h: A.supper("su2", w, h, 2606, bread=True), "#4A3438"),
        D([cp("26:27", to="saying,"), sy("26:27", frm="Drink ye"), sy("26:28"), sy("26:29")], lambda w, h: A.supper("su3", w, h, 2607, cupup=True), "#4A3438"),
        D([cp("26:30"), cp("26:31", to="unto them,"), sy("26:31", frm="All ye shall", to="it is written,"), sg("26:31", frm="I will smite"), sy("26:32")],
          lambda w, h: A.olivet_night("on1", w, h, 2608), NIGHT, head="Before the Cock Crow"),
        F([cp("26:33", to="said unto him,"), sy("26:33", frm="If all")], PETER),
        F([cp("26:34", to="said unto him,"), sy("26:34", frm="Verily")], **GRIEF),
        F([cp("26:35", to="Peter saith unto him,"), sy("26:35", frm="Even if", to="deny thee."), cp("26:35", frm="Likewise")], PETER),
        D([cp("26:36", to="unto his disciples,"), sy("26:36", frm="Sit ye here,"), cp("26:37"), cp("26:38", to="unto them,"), sy("26:38", frm="My soul")],
          lambda w, h: A.gethsemane("gt1", w, h, 2609, sleeping=False, praying=False), "#05051A", head="Gethsemane"),
        D([cp("26:39", to="and prayed, saying,"), sy("26:39", frm="My Father,")], lambda w, h: A.gethsemane("gt2", w, h, 2610, sleeping=False), "#05051A"),
        F([cp("26:40", to="saith unto Peter,"), sy("26:40", frm="What, could"), sy("26:41")], JESUS_PASSION, bg=COLD),
        D([cp("26:42", to="and prayed, saying,"), sy("26:42", frm="My Father,"), cp("26:43"), cp("26:44")], lambda w, h: A.gethsemane("gt3", w, h, 2611), "#05051A"),
        F([cp("26:45", to="saith unto them,"), sy("26:45", frm="Sleep on"), sy("26:46")], JESUS_PASSION, bg=COLD),
        D([cp("26:47"), cp("26:48", to="saying,"), sy("26:48", frm="Whomsoever"), cp("26:49", to="and said,"), sy("26:49", frm="Hail, Rabbi;", to="Hail, Rabbi;"), cp("26:49", frm="and kissed him.")],
          lambda w, h: A.arrest("ar1", w, h, 2612), "#05051A", head="Friend, Do That for Which Thou Art Come"),
        F([cp("26:50", to="said unto him,"), sy("26:50", frm="Friend,", to="art come."), cp("26:50", frm="Then they came")], JESUS_PASSION, bg=COLD),
        D([cp("26:51"), cp("26:52", to="unto him,"), sy("26:52", frm="Put up"), sy("26:53"), sy("26:54")], lambda w, h: A.arrest("ar2", w, h, 2613, sword=True), "#05051A"),
        F([cp("26:55", to="to the multitudes,"), sy("26:55", frm="Are ye come"), sy("26:56", to="might be fulfilled.")], JESUS_PASSION, bg=COLD),
        D([cp("26:56", frm="Then all the disciples")], lambda w, h: A.arrest("ar3", w, h, 2614, empty=True), "#05051A"),
        D([cp("26:57"), cp("26:58")], lambda w, h: A.caiaphas_hall("ch1", w, h, 2615), "#2A1A2A", head="Before Caiaphas"),
        F([cp("26:59"), cp("26:60"), cp("26:61", to="and said,"), sy("26:61", frm="This man said,")], WITNESS, bg=RED),
        F([cp("26:62", to="and said unto him,"), sy("26:62", frm="Answerest"), cp("26:63", to="held his peace."), cp("26:63", frm="And the high priest", to="said unto him,"),
           sy("26:63", frm="I adjure")], CAIAPHAS, bg=RED),
        F([cp("26:64", to="Jesus saith unto him,"), sy("26:64", frm="Thou hast said:")], JESUS_PASSION, bg=COLD),
        F([cp("26:65", to="saying,"), sy("26:65", frm="He hath spoken"), sy("26:66", to="what think ye?")], CAIAPHAS_RENT, bg=RED),
        D([cp("26:66", frm="They answered", to="and said,"), sy("26:66", frm="He is worthy"), cp("26:67"), cp("26:68", to="saying,"), sy("26:68", frm="Prophesy")],
          lambda w, h: A.shut_door("sd1", w, h, 2616), "#2A2228"),
        D([cp("26:69", to="saying,"), sy("26:69", frm="Thou also"), cp("26:70", to="saying,"), sy("26:70", frm="I know not")], lambda w, h: A.court_fire("cf1", w, h, 2617), "#05051A",
          head="Thou Shalt Deny Me Thrice"),
        D([cp("26:71", to="that were there,"), sy("26:71", frm="This man also"), cp("26:72", to="with an oath,"), sy("26:72", frm="I know not")],
          lambda w, h: A.court_fire("cf2", w, h, 2618, porch=True), "#05051A"),
        D([cp("26:73", to="said to Peter,"), sy("26:73", frm="Of a truth"), cp("26:74", to="and to swear,"), sy("26:74", frm="I know not", to="the man."), cp("26:74", frm="And straightway")],
          lambda w, h: A.cockcrow("cc1", w, h, 2619), "#1A1A3A"),
        F([cp("26:75")], PETER_GRIEF, bg=COLD)]
PG.extend(K.pack(SEGS, "MAT-C10-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · HE IS RISEN")))
