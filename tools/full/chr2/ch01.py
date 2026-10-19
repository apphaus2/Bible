"""2 Chronicles volume, Chapter 1 — Wisdom and Knowledge (2 Chronicles 1–4). Every verse, word for word from ref/asv.
Solomon and all the assembly at the high place at Gibeon, a thousand burnt-offerings on the brazen altar; in that night,
ask what I shall give thee — give me now wisdom and knowledge (God's words in the Voice box over the dream); chariots and
horsemen, silver and gold as stones; the letter to Huram king of Tyre and Huram's answer in writing; the burden-bearers and
hewers; then the house on mount Moriah, measure by measure, as 1 Kings' blueprints: the plan, the porch, the most holy house
and its cherubim, the veil, Jachin and Boaz, the brazen altar, the molten sea on twelve oxen, the lavers, the candlesticks,
the courts, and the vessels of gold."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr2 import G, art as K
from chr2.common import pack, cp, say, gd, says, gods, caps, drawn, face, joined, SOLOMON, SOLOMON_WISE, HIRAM, COLD, GOLDEN

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK, NIGHT = "#0B1A2E", "#0F0E2A"


@P("2CH-C01-00-Title", "Chapter 1 · Wisdom and Knowledge", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.dream("t1", 760, 780, 101)}</g><rect x="0" y="0" width="760" height="302" fill="#0F0E2A"></rect>')
    return chapter_title(1, "第一話", "Wisdom and Knowledge", "2 Chronicles 1 – 4", svg, NIGHT, v("1:10", to="before this people;"), "2 Chronicles · Volume Fourteen")


def bp(refs, fn, k=0.3, **kw):
    a, _, b = refs.partition("-")
    return drawn([caps(refs)], f"2CHR {a}" + (f"–{b}" if b else ""), below(fn, k), INK, **kw)

SEGS = [drawn([caps("1:1-3")], "2CHR 1:1–3", below(lambda w, h: K.gibeon("gb1", w, h, 102), 0.3), "#FFB04A", head="The High Place at Gibeon", stamp=1),
        drawn([caps("1:4-6")], "2CHR 1:4–6", below(lambda w, h: K.gibeon("gb1b", w, h, 103), 0.3), "#FFB04A"),
        drawn([cp("1:7", to="and said unto him,"), gd("1:7", frm="Ask what")], "2CHR 1:7", lambda w, h: K.dream("dr1", w, h, 104), NIGHT, head="Ask What I Shall Give Thee"),
        face([cp("1:8", to="unto God,"), joined("say", ("1:8", "Thou hast showed"), "1:9", "1:10")], "2CHR 1:8–10", SOLOMON_WISE, bg=COLD),
        drawn([cp("1:11", to="to Solomon,"), joined("god", ("1:11", "Because this"), "1:12")], "2CHR 1:11–12", lambda w, h: K.dream("dr1b", w, h, 105), NIGHT),
        drawn([caps("1:13-14")], "2CHR 1:13–14", below(lambda w, h: K.stalls("st1", w, h, 106), 0.3), "#E8C890", head="Chariots and Horsemen"),
        drawn([caps("1:15-17")], "2CHR 1:15–17", below(lambda w, h: K.K2.gold_shields(w, h, 107), 0.36), "#3A2214")]
PG.extend(pack(SEGS, "2CH-C01-D", PG.next()))
SEGS2 = [drawn([caps("2:1-2")], "2CHR 2:1–2", below(lambda w, h: K.hewers("hw1", w, h, 108), 0.24), "#E8C8A0", head="Solomon Sent to Huram", stamp=2),
         face([cp("2:3", to="saying,"), say("2:3", frm="As thou didst")], "2CHR 2:3", SOLOMON),
         face([says("2:4-6")], "2CHR 2:4–6", SOLOMON),
         face([says("2:7-10")], "2CHR 2:7–10", SOLOMON),
         face([cp("2:11", to="which he sent to Solomon,"), say("2:11", frm="Because Jehovah"), cp("2:12", to="Huram said moreover,"), joined("say", ("2:12", "Blessed be"), "2:13", "2:14")],
              "2CHR 2:11–14", HIRAM, head="Huram Answered in Writing"),
         drawn([says("2:15-16")], "2CHR 2:15–16", below(lambda w, h: K.lebanon("lb1", w, h, 109, rafts=True), 0.3), "#8FD0E2"),
         drawn([caps("2:17-18")], "2CHR 2:17–18", below(lambda w, h: K.hewers("hw1b", w, h, 110), 0.3), "#E8C8A0")]
PG.extend(pack(SEGS2, "2CH-C01-E", PG.next()))
SEGS3 = [drawn([caps("3:1-2")], "2CHR 3:1–2", below(lambda w, h: K.fire_altar("mo1", w, h, 111, king=False), 0.3), "#7A2A0A", head="Mount Moriah", stamp=3),
         bp("3:3-4", lambda w, h: K.temple_plan(w, h), 0.34),
         bp("3:5-7", lambda w, h: K.cedar_within(w, h, gold=True), 0.24),
         bp("3:8-9", lambda w, h: K.temple_plan(w, h, oracle=True), 0.3, head="The Most Holy House"),
         bp("3:10-13", lambda w, h: K.cherubim(w, h), 0.36),
         bp("3:14", lambda w, h: K.doors(w, h, folding=True), 0.16),
         bp("3:15-17", lambda w, h: K.pillar_elev(w, h, names=True), 0.36, head="Jachin and Boaz")]
PG.extend(pack(SEGS3, "2CH-C01-F", PG.next()))
SEGS4 = [bp("4:1", lambda w, h: K.horned_altar(w * 0.5, h * 0.84, min(1.6, h / 190)) + K.label(w * 0.5, h * 0.96, "THE ALTAR OF BRASS · 20 × 20 × 10 CUBITS", "#8FD0E2", 10), 0.3,
            head="The Altar and the Sea", stamp=4),
         bp("4:2-5", lambda w, h: K.molten_sea(w, h), 0.36),
         bp("4:6-8", lambda w, h: K.base_laver(w, h), 0.36),
         bp("4:9-10", lambda w, h: K.court_plan(w, h), 0.24),
         drawn([caps("4:11-18")], "2CHR 4:11–18", below(lambda w, h: K.casting("cs1", w, h, 112), 0.5), "#5A3A2A", head="The Work of Huram"),
         bp("4:19-22", lambda w, h: K.gold_vessels(w, h), 0.42)]
PG.extend(pack(SEGS4, "2CH-C01-G", PG.next(), end=end_mark("NEXT · THE GLORY FILLED THE HOUSE", "right: 10px; bottom: 34px")))
