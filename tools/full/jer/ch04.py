"""Jeremiah volume, Chapter 4 — The Broken Covenant (Jeremiah 10–12). Every verse, word for word from ref/eng-asv.
Learn not the way of the nations: the tree cut out of the forest, decked with silver and gold and nailed fast (the image
drawn as a thing); Jehovah the true God, who stretched out the heavens; my tent is destroyed; O Jehovah, correct me, but in
measure; the words of this covenant and the conspiracy of Judah; the green olive-tree set on fire; the men of Anathoth that
sought his life (a lamb on the road, men whispering at the gate); wherefore doth the way of the wicked prosper?; if thou hast
run with the footmen; the speckled bird; and the evil neighbours plucked up and brought again (a map)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art4 as K
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, GOLDEN, COLD, RED, NIGHT
from jer import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W1, G1, S1, C1 = (jer(1, "word"), GOLDEN), (jer(1, "grief"), COLD), (jer(1, "stern"), RED), (jer(1, "calm"), GOLDEN)
MAP = "#0B1A2E"
NEIGH = ("EGYPT", "PHILISTIA", "MOAB", "AMMON", "EDOM", "TYRE", "DAMASCUS")


@P("JER-C04-00-Title", "Chapter 4 · The Broken Covenant", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.olive_fire(760, 780, 401)}</g><rect x="0" y="0" width="760" height="302" fill="#3A1A1A"></rect>')
    return chapter_title(4, "第四話", "The Broken Covenant", "Jeremiah 10 – 12", svg, "#3A1A1A", v("11:16", to="fair with goodly fruit:"), "Jeremiah · Volume Twenty-Four")


SEGS = [O("10:1-2", t=W1, head="Learn Not the Way of the Nations", stamp=10),
        O("10:3-5", a=("#8FB0C8", lambda w, h: K.idol_maker("im4", w, h, 402))),
        O("10:6-7", kind="say", t=C1),
        O("10:8-9", a=("#8FB0C8", lambda w, h: K.idol_maker("im4b", w, h, 403, decked=True))),
        S([say("10:10"), gd("10:11")], "10:10-11", t=C1),
        O("10:12-13", kind="say", a=("#1A1A3A", lambda w, h: K.heavens_waters(w, h, 404)), head="He Stretched Out the Heavens"),
        O("10:14-16", kind="say", t=W1),
        O("10:17-18", a=("#5A4A5A", lambda w, h: K.bundle(w, h, 405)), k=0.34),
        O("10:19-20", kind="say", a=("#4A3A4A", lambda w, h: K.tent_broken(w, h, 406)), head="My Tent Is Destroyed"),
        O("10:21-22", kind="say", a=(MAP, lambda w, h: K.north_map(w, h)), k=0.4),
        O("10:23-25", kind="say", t=G1, head="O Jehovah, Correct Me")]
PG.extend(pack(SEGS, "JER-C04-D", PG.next()))

SEGS2 = [S([cp("11:1"), gods("11:2-3")], "11:1-3", a=("#2A1A2A", lambda w, h: K.covenant_scroll(w, h, 407)), k=0.34, head="The Words of This Covenant", stamp=11),
         S([gd("11:4"), gd("11:5", to="as at this day."), cp("11:5", frm="Then answered I,", to="and said,"), say("11:5", frm="Amen,")], "11:4-5", t=W1),
         S([*cut("11:6", "And Jehovah said unto me,"), gd("11:7")], "11:6-7", t=W1),
         O("11:8", t=S1),
         S([*cut("11:9", "And Jehovah said unto me,"), gd("11:10")], "11:9-10", t=S1, head="A Conspiracy among the Men of Judah"),
         O("11:11-12", t=S1),
         O("11:13", a=("#8A8A9A", lambda w, h: K.altars_streets(w, h, 408)), k=0.28),
         O("11:14-15", t=G1),
         O("11:16-17", a=("#3A1A1A", lambda w, h: K.olive_fire(w, h, 409)), head="A Green Olive-Tree"),
         O("11:18-19", kind="say", a=("#2A1A3A", lambda w, h: K.anathoth_plot("ap4", w, h, 410)), head="Like a Gentle Lamb"),
         O("11:20", kind="say", t=G1),
         O("11:21-23", t=S1)]
PG.extend(pack(SEGS2, "JER-C04-E", PG.next()))

SEGS3 = [O("12:1-2", kind="say", t=G1, head="Wherefore Doth the Way of the Wicked Prosper?", stamp=12),
         O("12:3-4", kind="say", a=("#E8B070", lambda w, h: K.rain_field(w, h, 411, rain=False, dry=True))),
         O("12:5-6", a=("#8FB0C8", lambda w, h: K.footmen_horses("fh4", w, h, 412))),
         O("12:7-9", a=("#5A4A5A", lambda w, h: K.speckled_bird(w, h, 413)), head="I Have Forsaken My House"),
         O("12:10-11", a=("#8A8A9A", lambda w, h: K.trodden_vineyard(w, h, 414)), k=0.36),
         O("12:12-13", a=("#C8A070", lambda w, h: K.wheat_thorns(w, h, 415))),
         O("12:14-15", a=(MAP, lambda w, h: K.near_east(w, h, NEIGH + ("JUDAH",), hi=NEIGH, box=(29.5, 41.5, 27.0, 36.6))), head="Mine Evil Neighbours"),
         O("12:16-17", t=W1)]
PG.extend(pack(SEGS3, "JER-C04-F", PG.next(), end=end_mark("NEXT · THE MARRED GIRDLE", "right: 10px; bottom: 34px")))
