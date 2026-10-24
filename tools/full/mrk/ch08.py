"""Mark volume, Chapter 8 — Watch (Mark 13:1–14:42). Every verse, word for word from ref/eng-asv.
The great stones of the temple; the mount of Olives over against it, the four asking privately; wars and earthquakes
over the smoking plain (no one drawn); councils and synagogues beside his grieving face; the flight to the mountains, the
house left open and the cloak in the field; the sun darkened and the stars falling; the Son of man coming in clouds, the
angels as figures of white light at the four winds; the fig tree's tender branch; the porter at the door through the four
watches of the night. Then the passover: the chief priests' council by night; the alabaster cruse at Bethany; Judas
beside his face and the silver on the balance (no one drawn); the man bearing a pitcher of water; the upper room; the
supper, the bread broken and the cup; the hymn and the mount of Olives by moonlight; the cock crowing twice; Gethsemane —
Jesus fallen on the ground alone in a cold light, the three asleep, Abba, Father, in an ordinary balloon (the Father is
never drawn)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mrk import G, art8 as A, ch07 as _prev
from mrk.common import (K, Pages, D, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        JESUS_PASSION, PETER, JOHN, JUDAS)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MRK-C08-00-Title", "Chapter 8 · Watch", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2A5A"></rect><g transform="translate(0 300)">{A.olivet("t8", 760, 780, 1303)}</g>'
    return title(8, "Watch", "Mark 13:1 – 14:42", svg, "#3A2A5A", v("13:37", frm="And what I say"))


def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)
GRIEF = dict(tok=JESUS_GRIEF, bg=COLD)

SEGS = [D([cp("13:1", to="saith unto him,"), sy("13:1", frm="Teacher, behold,")], lambda w, h: A.temple_stones("ts1", w, h, 1301), "#8FD0E2", head="Not One Stone upon Another",
          stamp=13),
        F([cp("13:2", to="said unto him,"), sy("13:2", frm="Seest thou")], **GRIEF),
        D([cp("13:3"), sy("13:4")], lambda w, h: A.olivet("ol1", w, h, 1303), "#3A2A5A"),
        D([cp("13:5", to="say unto them,"), sy("13:5", frm="Take heed"), sy("13:6"), sy("13:7"), sy("13:8")], lambda w, h: A.wars_far("wf1", w, h, 1305), "#3A1A1A",
          head="The Beginning of Travail", art_h=200),
        F(S("13:9", 11), **GRIEF),
        F(S("13:12", 13), **GRIEF),
        D(S("13:14", 16), lambda w, h: A.flee("fl1", w, h, 1314), "#8A6A5A", head="Flee unto the Mountains"),
        F(S("13:17", 20), **GRIEF),
        F(S("13:21", 23), JESUS_STERN, bg=RED),
        D(S("13:24", 25), lambda w, h: A.darkened("dk1", w, h, 1324), "#05050E", head="Coming in Clouds"),
        D(S("13:26", 27), lambda w, h: A.clouds_glory("cg1", w, h, 1326), "#2A2A6A", art_h=300),
        D(S("13:28", 29), lambda w, h: A.fig_leaf("fg1", w, h, 1328), "#8FD0E2", head="Learn Her Parable"),
        F(S("13:30", 32), JESUS_TEACH),
        D(S("13:33", 37), lambda w, h: A.four_watches("fw1", w, h, 1333), "#2A2230", head="Watch", art_h=340),
        # Mark 14
        D([cp("14:1"), cp("14:2", to="they said,"), sy("14:2", frm="Not during")], lambda w, h: A.priests_court("pc1", w, h, 1401), "#0B0B2A", head="For the Burying", stamp=14),
        D([cp("14:3")], lambda w, h: A.anointing("an1", w, h, 1403), "#B8987A"),
        D([cp("14:4", to="saying,"), sy("14:4", frm="To what purpose"), sy("14:5", to="to the poor."), cp("14:5", frm="And they murmured")],
          lambda w, h: A.anointing("an2", w, h, 1404), "#B8987A"),
        F([cp("14:6", to="Jesus said,"), sy("14:6", frm="Let her alone;"), sy("14:7"), sy("14:8"), sy("14:9")], **GRIEF),
        F([cp("14:10")], JUDAS, bg=RED, head="Judas"),
        D([cp("14:11")], lambda w, h: A.silver("sv1", w, h, 1411), "#1A1630"),
        D([cp("14:12", to="say unto him,"), sy("14:12", frm="Where wilt"), cp("14:13", to="saith unto them,"), sy("14:13", frm="Go into the city,")],
          lambda w, h: A.pitcher("pi1", w, h, 1412), "#8FD0E2", head="The Guest-Chamber"),
        F([sy("14:14"), sy("14:15")], JESUS),
        D([cp("14:16"), cp("14:17")], lambda w, h: A.guest_chamber("gc1", w, h, 1416), "#8A6A5A"),
        D([cp("14:18", to="Jesus said,"), sy("14:18", frm="Verily")], lambda w, h: A.supper("su1", w, h, 1418), "#4A3438", head="Is It I?"),
        F([cp("14:19", to="one by one,"), sy("14:19", frm="Is it I?")], JOHN, bg=COLD),
        F([cp("14:20", to="said unto them,"), sy("14:20", frm="It is one"), sy("14:21")], **GRIEF),
        D([cp("14:22", to="and said,"), sy("14:22", frm="Take ye:")], lambda w, h: A.supper("su2", w, h, 1422, bread=True), "#4A3438", head="This Is My Body"),
        D([cp("14:23"), cp("14:24", to="said unto them,"), sy("14:24", frm="This is my blood"), sy("14:25")], lambda w, h: A.supper("su3", w, h, 1423, cupup=True), "#4A3438"),
        D([cp("14:26"), cp("14:27", to="saith unto them,"), sy("14:27", frm="All ye shall", to="it is written,"), sg("14:27", frm="I will smite"), sy("14:28")],
          lambda w, h: A.olivet_night("on1", w, h, 1426), NIGHT, head="Before the Cock Crow Twice"),
        F([cp("14:29", to="said unto him,"), sy("14:29", frm="Although")], PETER),
        F([cp("14:30", to="saith unto him,"), sy("14:30", frm="Verily")], **GRIEF),
        F([cp("14:31", to="vehemently,"), sy("14:31", frm="If I must", to="deny thee."), cp("14:31", frm="And in like manner")], PETER),
        D([cp("14:32", to="unto his disciples,"), sy("14:32", frm="Sit ye here,"), cp("14:33"), cp("14:34", to="saith unto them,"), sy("14:34", frm="My soul")],
          lambda w, h: A.gethsemane("gt1", w, h, 1432, sleeping=False, praying=False), "#05051A", head="Gethsemane"),
        D([cp("14:35"), cp("14:36", to="And he said,"), sy("14:36", frm="Abba, Father,")], lambda w, h: A.gethsemane("gt2", w, h, 1435, sleeping=False), "#05051A", art_h=220),
        F([cp("14:37", to="saith unto Peter,"), sy("14:37", frm="Simon, sleepest"), sy("14:38")], JESUS_PASSION, bg=COLD),
        D([cp("14:39"), cp("14:40")], lambda w, h: A.gethsemane("gt3", w, h, 1439), "#05051A"),
        F([cp("14:41", to="saith unto them,"), sy("14:41", frm="Sleep on now,"), sy("14:42")], JESUS_PASSION, bg=COLD)]
PG.extend(K.pack(SEGS, "MRK-C08-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · HE IS RISEN")))
