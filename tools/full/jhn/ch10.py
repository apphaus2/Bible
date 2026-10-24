"""John volume, Chapter 10 — Lovest Thou Me? (John 20–21). Every verse, word for word from ref/eng-asv.
The first day of the week while it was yet dark: the stone taken away, Mary Magdalene before the tomb; Peter and the other
disciple running; within, the linen cloths lying and the napkin rolled up in a place by itself, no one there; the two
angels in white sitting where the body had lain — white light, a gold rim, no face; Woman, why weepest thou?; Jesus risen
in white light in the garden, Mary — Rabboni; Touch me not; I have seen the Lord. The shut and barred doors and Jesus in
the midst in white light, Peace be unto you (his hands and his side told in words only, no wound drawn); Receive ye the
Holy Spirit, a soft light; Thomas apart, then kneeling — My Lord and my God; these are written, that ye may believe. The sea
of Tiberias: the boat by night with its empty net; daybreak and Jesus on the beach; the net on the right side full;
It is the Lord, Peter in the sea; the fire of coals with fish and bread, the hundred and fifty and three; break your fast;
Lovest thou me? beside Jesus' and Peter's faces and over the two walking by the water; Follow thou me; and the books the
world itself would not contain."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jhn import G, art10 as A, ch09 as _prev
from jhn.common import (K, Pages, D, F, S, said, cp, gd, sg, sy, v, title, fin, COLD, GOLDEN, RED, NIGHT, NIGHTF, WHITE, JESUS_RISEN, PETER, PETER_GRIEF,
                        JOHN, THOMAS, MAGDALENE_GRIEF, MAGDALENE_JOY)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JHN-C10-00-Title", "Chapter 10 · Lovest Thou Me?", title=True)
def title_page(n):
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#3A3A7A"></rect><g transform="translate(0 200)">{A.tiberias("t10", 760, 720, 2001, stage="fire")}</g>'
           '<rect x="0" y="899" width="760" height="181" fill="#B8A07A"></rect>')
    return title(10, "Lovest Thou Me?", "John 20 – 21", svg, "#3A3A7A", v("21:17", frm="Lovest thou me?", to="Lovest thou me?"))


R = lambda lines, **k: F(lines, JESUS_RISEN, bg=WHITE, **k)
SEGS = [D([cp("20:1")], lambda w, h: A.tomb_morning("tm1", w, h, 2002), "#0B0B2A", head="The Stone Taken Away", sky=20, art_h=260),
        F([cp("20:2", to="saith unto them,"), sy("20:2", frm="They have taken")], MAGDALENE_GRIEF, bg=COLD),
        D([cp("20:3"), cp("20:4")], lambda w, h: A.tomb_morning("tm2", w, h, 2003, stage="run"), "#3A3A7A", art_h=240),
        D([cp("20:5")], lambda w, h: A.inside_tomb("it1", w, h, 2004, look=True), "#2A2220", art_h=240),
        D([cp("20:6"), cp("20:7")], lambda w, h: A.inside_tomb("it2", w, h, 2005), "#2A2220", head="The Napkin by Itself", art_h=260),
        F([cp("20:8"), cp("20:9"), cp("20:10")], JOHN),
        D([cp("20:11"), cp("20:12")], lambda w, h: A.inside_tomb("it3", w, h, 2006, angels=True), "#2A2220", head="Woman, Why Weepest Thou?", art_h=260),
        D([cp("20:13", to="say unto her,"), sy("20:13", frm="Woman,", to="weepest thou?"), cp("20:13", frm="She saith", to="unto them,"), sy("20:13", frm="Because")],
          lambda w, h: A.tomb_morning("tm3", w, h, 2007, stage="weep"), "#3A3A7A", art_h=240),
        D([cp("20:14")], lambda w, h: A.tomb_morning("tm4", w, h, 2008, stage="gardener"), "#8FD0E2", art_h=260),
        R([cp("20:15", to="saith unto her,"), sy("20:15", frm="Woman,", to="seekest thou?")]),
        F([cp("20:15", frm="She, supposing", to="saith unto him,"), sy("20:15", frm="Sir,")], MAGDALENE_GRIEF, bg=COLD),
        R([cp("20:16", to="saith unto her,"), sy("20:16", frm="Mary.", to="Mary.")], head="Rabboni"),
        F([cp("20:16", frm="She turneth", to="in Hebrew,"), sy("20:16", frm="Rabboni;", to="Rabboni;"), cp("20:16", frm="which is to say,")], MAGDALENE_JOY, bg=WHITE),
        D([cp("20:17", to="saith to her,"), sy("20:17", frm="Touch me not;")], lambda w, h: A.tomb_morning("tm5", w, h, 2009, stage="gardener"), "#8FD0E2", art_h=240),
        D([cp("20:18", to="telleth the disciples,"), sy("20:18", frm="I have seen the Lord;", to="the Lord;"), cp("20:18", frm="and that he had")],
          lambda w, h: A.mourners("mo1", w, h, 2010), "#5A4A4A", art_h=240),
        D([cp("20:19", to="and saith unto them,"), sy("20:19", frm="Peace be unto you.")], lambda w, h: A.shut_room("sr1", w, h, 2011), "#5A4A4A", head="Peace Be unto You",
          art_h=260),
        D([cp("20:20"), cp("20:21", to="said to them again,"), sy("20:21", frm="Peace be unto you:")], lambda w, h: A.shut_room("sr2", w, h, 2012), "#5A4A4A"),
        D([cp("20:22", to="saith unto them,"), sy("20:22", frm="Receive ye"), sy("20:23")], lambda w, h: A.shut_room("sr3", w, h, 2013, stage="breathe"), "#5A4A4A", art_h=240),
        D([cp("20:24"), cp("20:25", to="said unto him,"), sy("20:25", frm="We have seen the Lord.", to="the Lord.")], lambda w, h: A.shut_room("sr4", w, h, 2014, stage="absent"),
          "#5A4A4A", head="My Lord and My God"),
        F([cp("20:25", frm="But he said", to="unto them,"), sy("20:25", frm="Except")], THOMAS, bg=COLD),
        D([cp("20:26", to="and said,"), sy("20:26", frm="Peace be unto you.")], lambda w, h: A.shut_room("sr5", w, h, 2015), "#5A4A4A"),
        R([cp("20:27", to="to Thomas,"), sy("20:27", frm="Reach hither")]),
        D([cp("20:28", to="said unto him,"), sy("20:28", frm="My Lord")], lambda w, h: A.shut_room("sr6", w, h, 2016, stage="thomas"), "#5A4A4A", art_h=260),
        R([said("20:29", "saith unto him,", "Because")]),
        D([cp("20:30"), cp("20:31")], lambda w, h: A.word_light("wl1", w, h, 2017, "glory"), "#FFC14D", head="That Ye May Believe"),
        # John 21
        D([cp("21:1"), cp("21:2"), cp("21:3", to="saith unto them,"), sy("21:3", frm="I go a fishing.", to="a fishing."), cp("21:3", frm="They say unto him,", to="unto him,"),
           sy("21:3", frm="We also come", to="with thee."), cp("21:3", frm="They went forth")], lambda w, h: A.tiberias("tb1", w, h, 2101), "#05051A",
          head="By the Sea of Tiberias", sky=21, art_h=240),
        D([cp("21:4"), cp("21:5", to="saith unto them,"), sy("21:5", frm="Children,", to="to eat?"), cp("21:5", frm="They answered him,", to="answered him,"), sy("21:5", frm="No.")],
          lambda w, h: A.tiberias("tb2", w, h, 2102, stage="beach"), "#3A3A7A"),
        D([cp("21:6", to="said unto them,"), sy("21:6", frm="Cast the net", to="shall find."), cp("21:6", frm="They cast")], lambda w, h: A.tiberias("tb3", w, h, 2103, stage="net"),
          "#3A3A7A", art_h=240),
        D([cp("21:7", to="saith unto Peter,"), sy("21:7", frm="It is the Lord.", to="It is the Lord."), cp("21:7", frm="So when Simon Peter"), cp("21:8")],
          lambda w, h: A.tiberias("tb4", w, h, 2104, stage="peter"), "#3A3A7A", art_h=240),
        D([cp("21:9"), cp("21:10", to="saith unto them,"), sy("21:10", frm="Bring of the fish"), cp("21:11")], lambda w, h: A.tiberias("tb5", w, h, 2105, stage="fire"), "#3A3A7A",
          head="Come and Break Your Fast", art_h=260),
        D([cp("21:12", to="saith unto them,"), sy("21:12", frm="Come and break", to="your fast."), cp("21:12", frm="And none of the disciples"), cp("21:13"), cp("21:14")],
          lambda w, h: A.tiberias("tb6", w, h, 2106, stage="meal"), "#3A3A7A", art_h=240),
        R([cp("21:15", to="saith to Simon Peter,"), sy("21:15", frm="Simon, son of John,", to="more than these?")], head="Lovest Thou Me?"),
        F([cp("21:15", frm="He saith unto him,", to="He saith unto him,"), sy("21:15", frm="Yea, Lord;", to="I love thee.")], PETER),
        D([cp("21:15", after="I love thee.", frm="He saith unto him,", to="He saith unto him,"), sy("21:15", frm="Feed my lambs.")], lambda w, h: A.lovest("lv1", w, h, 2107),
          "#8FD0E2", art_h=240),
        R([cp("21:16", to="a second time,"), sy("21:16", frm="Simon, son of John,", to="lovest thou me?")]),
        F([cp("21:16", frm="He saith unto him,", to="He saith unto him,"), sy("21:16", frm="Yea, Lord;", to="I love thee.")], PETER),
        D([cp("21:16", after="I love thee.", frm="He saith unto him,", to="He saith unto him,"), sy("21:16", frm="Tend my sheep.")], lambda w, h: A.lovest("lv2", w, h, 2108),
          "#8FD0E2", art_h=240),
        R([cp("21:17", to="the third time,"), sy("21:17", frm="Simon, son of John,", to="lovest thou me?")]),
        F([cp("21:17", frm="Peter was grieved", to="And he said unto him,"), sy("21:17", frm="Lord, thou knowest", to="I love thee.")], PETER_GRIEF, bg=COLD),
        R([cp("21:17", frm="Jesus saith", to="unto him,"), sy("21:17", frm="Feed my sheep."), sy("21:18")]),
        R([cp("21:19", to="saith unto him,"), sy("21:19", frm="Follow me.")]),
        D([cp("21:20"), cp("21:21", to="saith to Jesus,"), sy("21:21", frm="Lord,")], lambda w, h: A.lovest("lv3", w, h, 2109, follow=True), "#8FD0E2", head="Follow Thou Me",
          art_h=240),
        R([said("21:22", "saith unto him,", "If I will")]),
        F([cp("21:23"), cp("21:24")], JOHN),
        D([cp("21:25")], lambda w, h: A.books("bk1", w, h, 2110), "#3A2A5A", art_h=300)]
PG.extend(K.pack(SEGS, "JHN-C10-D", PG.next(), lone=1.5, end=fin("END OF JOHN · NEXT · ACTS")))
