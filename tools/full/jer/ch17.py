"""Jeremiah volume, Chapter 17 — Babylon Is Taken (Jeremiah 49–50). Every verse, word for word from ref/eng-asv.
The burdens of the children of Ammon (Rabbah a desolate heap), of Edom (thou that dwellest in the clefts of the rock; the lion
from the pride of the Jordan; the eagle against Bozrah), of Damascus (a fire in the wall), of Kedar and Hazor (a nation that
dwelleth without care, its tents and camels taken), and of Elam (the bow broken, the four winds), each with its map; then the
word against Babylon: Babylon is taken, Bel is put to shame; Israel and Judah going home weeping, seeking Zion; flee out of
the midst of Babylon; the archers round about; Israel a hunted sheep, brought again to his pasture; the hammer of the whole
earth broken; the armory opened; a sword upon the Chaldeans; a drought upon her waters; the ostriches in her ruins; a people
from the north; and the earth trembleth at the noise of the taking of Babylon."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art17 as K
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, GOLDEN, COLD, RED, NIGHT
from jer import ch16 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W3, G3, S3, C3 = (jer(3, "word"), GOLDEN), (jer(3, "grief"), COLD), (jer(3, "stern"), RED), (jer(3, "calm"), GOLDEN)
MAP = "#0B1A2E"
BAB = "#2A1A3A"
def nmap(names, box, **kw): return (MAP, lambda w, h: K.near_east(w, h, names, hi=names, box=box, **kw))


@P("JER-C17-00-Title", "Chapter 17 · Babylon Is Taken", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.babylon(760, 780, 1701, burning=True)}</g><rect x="0" y="0" width="760" height="302" fill="#2A1A3A"></rect>')
    return chapter_title(17, "第十七話", "Babylon Is Taken", "Jeremiah 49 – 50", svg, BAB, v("50:2", frm="Babylon is taken,", to="Merodach is dismayed;"), "Jeremiah · Volume Twenty-Four")


SEGS = [O("49:1-2", a=nmap(K.AMMON_P, (34.6, 37.2, 31.2, 32.9)), k=0.42, head="Of the Children of Ammon", stamp=49),
        O("49:3-4", a=("#2A0A0A", lambda w, h: K.heshbon_fire(w, h, 1702))),
        O("49:5-6", t=S3),
        O("49:7-8", a=nmap(K.EDOM_P, (33.4, 39.4, 25.6, 33.2), under=("TEMAN",)), k=0.36, head="Of Edom"),
        O("49:9-11", t=S3),
        O("49:12-13", t=S3),
        S([say("49:14"), gods("49:15-16")], "49:14-16", a=("#E8A060", lambda w, h: K.petra(w, h, 1703)), head="Thou That Dwellest in the Clefts of the Rock"),
        O("49:17-18", a=("#2A2A3A", lambda w, h: K.cursed_day(w, h, 1704))),
        O("49:19", a=("#C8703A", lambda w, h: K.lion_thicket(w, h, 1705)), k=0.38),
        O("49:20-22", a=("#5A6A8A", lambda w, h: K.eagle(w, h, 1706))),
        O("49:23-24", a=nmap(K.DAM_P, (34.0, 39.0, 32.4, 37.4)), k=0.4, head="Of Damascus"),
        O("49:25-27", a=("#2A0A0A", lambda w, h: K.damascus_fire(w, h, 1707))),
        O("49:28-29", a=("#E8A060", lambda w, h: K.kedar_tents("kt17", w, h, 1708, taken=True)), head="Of Kedar and Hazor"),
        O("49:30-31", a=nmap(K.KEDAR_P + ("JERUSALEM",), (33.0, 46.0, 26.0, 34.4)), k=0.4),
        O("49:32-33", a=("#E8A060", lambda w, h: K.kedar_tents("kt17b", w, h, 1709))),
        S([cp("49:34"), gods("49:35-36")], "49:34-36", a=("#1A1A2A", lambda w, h: K.bow_broken(w, h, 1710)), k=0.42, head="Concerning Elam"),
        O("49:37-39", a=nmap(K.ELAM_P, (40.0, 51.0, 28.0, 35.6)), k=0.44)]


SEGS2 = [S([cp("50:1"), gd("50:2")], "50:1-2", a=("#5A3A4A", lambda w, h: K.bel_shamed(w, h, 1711)), k=0.42, head="Babylon Is Taken", stamp=50),
         O("50:3-5", a=("#4A4A7A", lambda w, h: K.going_home("gh17", w, h, 1712))),
         O("50:6-7", a=("#8A7A8A", lambda w, h: K.flock(w, h, 1713))),
         O("50:8-10", a=("#8FB0C8", lambda w, h: K.he_goats(w, h, 1714)), head="Flee out of the Midst of Babylon"),
         O("50:11-13", t=S3),
         O("50:14-15", a=("#8FB0C8", lambda w, h: K.archers("ar17", w, h, 1715))),
         O("50:16-17", a=("#8A7A8A", lambda w, h: K.hunted_sheep(w, h, 1716)), head="Israel Is a Hunted Sheep"),
         O("50:18-20", a=("#8FC0E0", lambda w, h: K.pasture(w, h, 1717))),
         O("50:21-23", a=("#3A2A2A", lambda w, h: K.hammer_broken(w, h, 1718)), head="The Hammer of the Whole Earth"),
         O("50:24-25", a=("#1A1A2A", lambda w, h: K.armory(w, h, 1719))),
         O("50:26-28", a=("#5A3A3A", lambda w, h: K.bullocks(w, h, 1720))),
         O("50:29-30", t=S3),
         O("50:31-32", a=("#2A1A3A", lambda w, h: K.babylon(w, h, 1721, burning=True))),
         O("50:33-34", t=C3, head="Their Redeemer Is Strong"),
         O("50:35-37", a=(BAB, lambda w, h: K.sword_upon(w, h, 1722)), head="A Sword upon the Chaldeans"),
         O("50:38-40", a=("#E8A060", lambda w, h: K.dry_river(w, h, 1723))),
         O("50:41-43", a=("#4A3A4A", lambda w, h: K.north_host("nh17", w, h, 1724)), head="A People Cometh from the North"),
         O("50:44", a=("#C8703A", lambda w, h: K.lion_thicket(w, h, 1725)), k=0.4),
         O("50:45-46", a=("#E8A060", lambda w, h: K.ostriches(w, h, 1726)))]
PG.extend(pack(SEGS + SEGS2, "JER-C17-D", PG.next(), end=end_mark("NEXT · THE HAMMER OF THE WHOLE EARTH", "right: 10px; bottom: 34px")))
