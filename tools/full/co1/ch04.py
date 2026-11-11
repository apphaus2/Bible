"""1 Corinthians volume, Chapter 4 — The Greatest of These Is Love (1 Corinthians 12–14). Every verse, word for word from
ref/eng-asv. 1 Corinthians 12: the dumb idols and those bowed before them (12:2); the nine gifts of the one Spirit about a
light with no figure in it (12:8–11); the body and its members as technical plates — the whole body tagged (12:12), foot,
hand, ear and eye (12:15–17), eye, hand, head and feet (12:21); the church gathered, the body of Christ (12:27); the ministries
set in the church (12:28). 1 Corinthians 13: sounding brass and a clanging cymbal (13:1); love's kindness at a door (13:4);
the child and the man (13:11); the bronze mirror, darkly, and the full light, face to face (13:12); faith, hope and love,
three lamps (13:13). 1 Corinthians 14: the assembly by lamplight — one prophesying (14:3), one praying in a tongue and the
unlearned puzzled (14:16), the psalm and the teaching waiting their turn (14:26), the women veiled and listening (14:34);
the pipe, the harp and the trumpet's uncertain voice (14:7–8); two men barbarians to each other (14:11); the Voice box over
a storm for Isaiah 28:11 (14:21); the stranger fallen on his face (14:25)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from co1 import G, art4 as A, ch03 as _prev
from co1.common import (K, Pages, D, F, lt, lts, lp, ltj, lj, sg, gd, sy, wq, qw, v, title, nxt, PAUL, PAUL_LAMP, PAUL_STERN, PAUL_JOY, PAUL_GRIEF,
                        GOLD_BG, LAMP_BG, STERN_BG, JOY_BG, GRIEF_BG)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1CO-C04-00-Title", "Chapter 4 · The Greatest of These Is Love", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#1A1028"></rect><g transform="translate(0 340)">{A.three_lamps(760, 700, 1301)}</g>'
    return title(4, "The Greatest of These Is Love", "1 Corinthians 12–14", svg, "#1A1028", v("13:13", frm="the greatest of these is love"))


SEGS = [
    # 1 Corinthians 12
    D(lp("12:1-3"), lambda w, h: A.dumb_idols("di1", w, h, 2201), "#4A3A4A", head="Concerning Spiritual Gifts", sky=12, art_h=230),
    F(lp("12:4-7"), PAUL_LAMP, bg=LAMP_BG),
    D(lp("12:8-11"), lambda w, h: A.gifts_plate(w, h), "#0B1A2E", head="The Same Spirit", art_h=250),
    D(lp("12:12-13"), lambda w, h: A.body_plate("bp1", w, h), "#0B1A2E", head="One Body, Many Members", art_h=260),
    D(lp("12:14-17"), lambda w, h: A.members(w, h), "#0B1A2E", art_h=220),
    F(lp("12:18-20"), PAUL),
    D(lp("12:21-24"), lambda w, h: A.members(w, h, which=("EYE", "HAND", "HEAD", "FEET"), title="1 CORINTHIANS 12:21 · I HAVE NO NEED OF THEE"), "#0B1A2E", art_h=220),
    D(lp("12:25-27"), lambda w, h: A.plain_folk("pf2", w, h, 2225), "#3A2418", head="Ye Are the Body of Christ", art_h=230),
    D(lp("12:28-31"), lambda w, h: A.ministries(w, h), "#0B1A2E", art_h=230),
    # 1 Corinthians 13
    D([lt("13:1")], lambda w, h: A.brass_cymbal(w, h, 2301), "#1A1418", head="The Greatest of These Is Love", sky=13, art_h=230),
    F(lp("13:2-3"), PAUL),
    D(lp("13:4-7"), lambda w, h: A.kindness("kd1", w, h, 2304), "#3A2A5A", art_h=240),
    F(lp("13:8-10"), PAUL_JOY, bg=JOY_BG),
    D([lt("13:11")], lambda w, h: A.child_man("ch1", w, h, 2311), "#C8A878", art_h=230),
    D([lt("13:12")], lambda w, h: A.bronze_mirror(w, h, 2312), "#1E1820", head="In a Mirror, Darkly", art_h=230),
    D([lt("13:13")], lambda w, h: A.three_lamps(w, h, 2313), "#1A1028", art_h=220),
    # 1 Corinthians 14
    D(lp("14:1-3"), lambda w, h: A.assembly("as1", w, h, 2401), "#5A3E2E", head="Follow After Love", sky=14, art_h=230),
    F(lp("14:4-5"), PAUL),
    D(lp("14:6-9"), lambda w, h: A.instruments(w, h, 2406), "#2A2A4A", head="An Uncertain Voice", art_h=230),
    D(lp("14:10-12"), lambda w, h: A.barbarians("bb1", w, h, 2410), "#8FD0E2", art_h=230),
    F(lp("14:13-15"), PAUL_LAMP, bg=LAMP_BG),
    D(lp("14:16-17"), lambda w, h: A.assembly("as2", w, h, 2416, stage="unlearned"), "#5A3E2E", art_h=240),
    F(lp("14:18-20"), PAUL),
    D([lt("14:21", to="In the law it is written,"), gd("14:21", frm="By men of strange tongues")], lambda w, h: A.voice_storm(w, h, 2421), "#14141E", art_h=210),
    F(lp("14:22-23"), PAUL_STERN, bg=STERN_BG),
    D(lp("14:24-25"), lambda w, h: A.falls_down("fd2", w, h, 2424), "#5A3E2E", art_h=240),
    D(lp("14:26-28"), lambda w, h: A.assembly("as3", w, h, 2426, stage="order"), "#5A3E2E", head="Decently and in Order", art_h=240),
    F(lp("14:29-33"), PAUL),
    D(lp("14:34-35"), lambda w, h: A.assembly("as4", w, h, 2434, stage="women"), "#5A3E2E", art_h=230),
    F(lp("14:36-38"), PAUL_STERN, bg=STERN_BG),
    D(lp("14:39-40"), lambda w, h: A.assembly("as5", w, h, 2439), "#5A3E2E", art_h=240),
]
PG.extend(K.pack(SEGS, "1CO-C04-D", PG.next(), lone=1.5, end=nxt("NEXT · O DEATH, WHERE IS THY VICTORY?")))
