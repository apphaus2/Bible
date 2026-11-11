"""Romans volume, Chapter 4 — The Depth of the Riches (Romans 9–11). Every verse, word for word from ref/eng-asv.
Paul's face in the grieving blue light for 9:1–3; the plate of Israel's gifts; Sarah old with the child Isaac and the
lineage of the promise, God's words to Abraham, Rebecca and Moses (9:7, 9:9, 9:12, 9:13, 9:15, 9:17) in the Voice box over
the tent, the plate, the cleft of the rock with the glory passing and Pharaoh before his gate; the potter at his wheel,
the thing formed's question in a song box; the vessels of wrath and of mercy; Hosea's words (God's own) in the Voice box
over the nations at dawn; Isaiah in song boxes over the sand of the sea and the smoke over the empty plain of Sodom; the
stone of stumbling in the road to Zion (9:33, God's words, the Voice box). Romans 10: the plate of heaven, the abyss and the
word nigh thee; the herald on the mountains at dawn; the sound gone out into all the earth on Acts' map; God's words by
Moses and Isaiah in the Voice box over Jerusalem at dusk. Romans 11: Elijah at the cave on Horeb, his plea in a song box and
God's answer in the Voice box; the table in the dark (11:9–10, words only); the olive tree as a botanical plate; Zion at
dawn (11:26–27, God's covenant in the Voice box); and the doxology of 11:33–36 over the burst of light."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from rom import G, art4 as A, ch03 as _prev
from rom.common import (K, Pages, D, F, lt, lp, sg, gd, v, title, nxt, glory, PAUL, PAUL_STERN, PAUL_JOY, PAUL_GRIEF, GOLD_BG, STERN_BG, JOY_BG, GRIEF_BG)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ROM-C04-00-Title", "Chapter 4 · The Depth of the Riches", title=True)
def title_page(n):
    svg = f'<g transform="translate(0 300)">{A.herald("t04", 760, 780, 404)}</g><rect x="0" y="0" width="760" height="302" fill="#2A2A6A"></rect>'
    return title(4, "The Depth of the Riches", "Romans 9–11", svg, "#2A2A6A", v("11:33", to="knowledge of God!"))


def st(p, seed, **k): return lambda w, h: A.study(p, w, h, seed, **k)

SEGS = [
    # Romans 9
    F(lp("9:1-3"), PAUL_GRIEF, bg=GRIEF_BG, head="Great Sorrow"),
    D(lp("9:4-5"), lambda w, h: A.israel_gifts(w, h), "#0B1A2E", sky=9, art_h=200),
    D([lt("9:6"), lt("9:7", to="but,"), gd("9:7", frm="In Isaac"), lt("9:8"), lt("9:9", to="a word of promise,"), gd("9:9", frm="According to this season")],
      lambda w, h: A.child_promise("cp1", w, h, 1906), "#8FB0D8", head="The Children of the Promise", art_h=230),
    D([K.lj("9:10", "9:11", ("9:12", None, "it was said unto her,")), gd("9:12", frm="The elder shall serve"), lt("9:13", to="Even as it is written,"),
       gd("9:13", frm="Jacob I loved")], lambda w, h: A.promise_line(w, h), "#0B1A2E", art_h=200),
    D([lt("9:14"), lt("9:15", to="he saith to Moses,"), gd("9:15", frm="I will have mercy"), lt("9:16")], lambda w, h: A.cleft_rock(w, h, 1914), "#2A2A4A",
      head="Of God That Hath Mercy", art_h=220),
    D([lt("9:17", to="unto Pharaoh,"), gd("9:17", frm="For this very purpose"), lt("9:18")], lambda w, h: A.pharaoh_gate("ph1", w, h, 1917), "#C8A060", art_h=230),
    D([lt("9:19"), lt("9:20", to="him that formed it,"), sg("9:20", frm="Why didst thou make me thus?"), lt("9:21")], lambda w, h: A.potter_wheel("pw1", w, h, 1919),
      "#7A5A3A", head="The Potter and the Clay", art_h=240),
    D(lp("9:22-24"), lambda w, h: A.vessels(w, h), "#0B1A2E", art_h=210),
    D([lt("9:25", to="in Hosea,"), gd("9:25", frm="I will call that my people"), gd("9:26")], lambda w, h: A.nations_dawn("nd1", w, h, 1925), "#4A2A5A", art_h=230),
    D([lt("9:27", to="concerning Israel,"), sg("9:27", frm="If the number"), sg("9:28")], lambda w, h: A.sand_shore(w, h, 1927), "#4A5A8A", art_h=200),
    D([lt("9:29", to="hath said before,"), sg("9:29", frm="Except the Lord")], lambda w, h: A.sodom_plain(w, h, 1929), "#3A0A10", art_h=190),
    F(lp("9:30-32"), PAUL, head="The Stone of Stumbling"),
    D([lt("9:33", to="even as it is written,"), gd("9:33", frm="Behold, I lay in Zion")], lambda w, h: A.stumbling_stone(w, h, 1933), "#8FD0E2", art_h=240),
    # Romans 10
    F(lp("10:1-4"), PAUL_GRIEF, bg=GRIEF_BG, head="The Word Is Nigh Thee"),
    D(lp("10:5-8"), lambda w, h: A.nigh_plate(w, h), "#0B1A2E", sky=10, art_h=240),
    F([lt("10:9"), K.lj("10:10", ("10:11", None, "the scripture saith,")), sg("10:11", frm="Whosoever believeth")], PAUL_JOY, bg=JOY_BG),
    F([K.lj("10:12", ("10:13", None, "for,")), sg("10:13", frm="Whosoever shall call")], PAUL),
    D([lt("10:14"), lt("10:15", to="even as it is written,"), sg("10:15", frm="How beautiful")], lambda w, h: A.herald("hd1", w, h, 1014), "#2A2A6A",
      head="How Beautiful Are the Feet", art_h=260),
    D([lt("10:16", to="For Isaiah saith,"), sg("10:16", frm="Lord, who hath believed"), lt("10:17"), lt("10:18", to="Yea, verily,"), sg("10:18", frm="Their sound")],
      lambda w, h: A.all_the_earth(w, h), "#0B1A2E", art_h=240),
    D([lt("10:19", to="First Moses saith,"), gd("10:19", frm="I will provoke you"), lt("10:20", to="and saith,"), gd("10:20", frm="I was found"),
       lt("10:21", to="he saith,"), gd("10:21", frm="All the day long")], lambda w, h: A.jerusalem_dusk(w, h, 1019), "#2A1A3A", art_h=200),
    # Romans 11
    F(lp("11:1-2"), PAUL, head="A Remnant"),
    D([sg("11:3"), lt("11:4", to="unto him?"), gd("11:4", frm="I have left for myself")], lambda w, h: A.elijah_cave("ec1", w, h, 1103), "#5A5A7A", sky=11, art_h=240),
    F(lp("11:5-7"), PAUL_STERN, bg=STERN_BG),
    D([lt("11:8", to="according as it is written,"), sg("11:8", frm="God gave them"), lt("11:9", to="And David saith,"), sg("11:9", frm="Let their table"), sg("11:10")],
      lambda w, h: A.dark_table(w, h, 1108), "#1A1418", art_h=190),
    F(lp("11:11-12"), PAUL),
    F(lp("11:13-15"), PAUL_JOY, bg=JOY_BG),
    D(lp("11:16-18"), lambda w, h: A.olive_graft(w, h), "#0B1A2E", head="The Olive Tree", art_h=380),
    F(lp("11:19-21"), PAUL_STERN, bg=STERN_BG),
    D(lp("11:22-24"), lambda w, h: A.olive_graft(w, h, again=True), "#0B1A2E", art_h=300),
    D([lt("11:25"), lt("11:26", to="even as it is written,"), gd("11:26", frm="There shall come out of Zion"), gd("11:27")], lambda w, h: A.zion_dawn(w, h, 1125),
      "#2A2A5A", head="This Mystery", art_h=200),
    F(lp("11:28-32"), PAUL),
    glory([lt("11:33"), sg("11:34"), sg("11:35"), lt("11:36")], seed=1133, head="O the Depth of the Riches", h=640),
]
PG.extend(K.pack(SEGS, "ROM-C04-D", PG.next(), end=nxt("NEXT · A LIVING SACRIFICE")))
