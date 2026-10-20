"""Exodus volume, Chapter 11 — The Willing Offering (Exodus 35–38). Every verse, word for word from ref/eng-asv.
The making of the tabernacle (36:8–38:20) follows the pattern of chapters 25–30 almost word for word; it is set in full as
blueprint pages (kit.blueprints) reusing the drawings of art8 and art9, with the narration in caption boxes."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cap
from exo import G, art8 as B8, art9 as Q, art11 as N
from exo.kit import blueprints
from genesis.ch02 import rows, W1

v, sp = G.v, G.span
START = 175                                  # chapter 10 ends on page 174
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def nar(refs): return [("nar", sp(refs))]

def chunks(refs, art, head, most=520):
    """Narration items for a run of verses, cut into pieces of at most `most` characters (whole verses), all with one
    drawing; the heading goes on the first piece only."""
    c, vs = refs.split(":"); a, _, b = vs.partition("-"); a, b = int(a), int(b or a)
    total = sum(len(G.verses[(int(c), n)]) for n in range(a, b + 1))
    target = total / max(1, round(total / most + 0.49))         # even pieces, none much over `most`
    out, cur, run = [], [], 0
    for n in range(a, b + 1):
        ln = len(G.verses[(int(c), n)])
        if cur and run + ln / 2 > target:
            out.append(cur); cur, run = [], 0
        cur.append(n); run += ln
    out.append(cur)
    return [(f"{c}:{g[0]}" + (f"–{g[-1]}" if len(g) > 1 else ""), nar(f"{c}:{g[0]}-{g[-1]}"), art, head if i == 0 else None) for i, g in enumerate(out)]
def moses(ref, to, rest=None):
    """Narration up to `to` ("saying,"), then Moses' words, with any following verses, in a speech box."""
    t = v(ref); after = t[t.index(to) + len(to):].strip()
    return [("cap", v(ref, to=to)), ("say", v(ref, frm=after) + (" " + sp(rest) if rest else ""))]

def S(scene, p):
    return lambda w, h: scene(p, w, h, len(p) * 97)

ITEMS = [
    ("35:1–3", moses("35:1", "said unto them,", "35:2-3"), S(N.assembly, "n1"), "These Are the Words"),
    ("35:4–9", moses("35:4", "saying,", "35:5-9"), B8.offering, None),
    ("35:10–19", [("say", sp("35:10-19"))], Q.works, "Let Every Wise-hearted Man Come"),
    ("35:20–24", nar("35:20-24"), S(N.bringing, "n2"), "Every One Whose Heart Stirred Him Up"),
    ("35:25–29", nar("35:25-29"), S(N.spinning, "n3"), None),
    ("35:30–35", moses("35:30", "the children of Israel,", "35:31-35"), lambda w, h: Q.craftsmen("n4", w, h), "Bezalel and Oholiab"),
    ("36:1–4", nar("36:1-4"), S(N.enough, "n5"), "Much More than Enough"),
    ("36:5–7", [("cap", v("36:5", to="saying,")), ("say", v("36:5", frm="The people")), ("nar", v("36:6", to="saying,")), ("say", v("36:6", frm="Let neither", to="sanctuary.")), ("nar", v("36:6", frm="So the people") + " " + v("36:7"))],
     S(N.enough, "n6"), None),
    *chunks("36:8-13", lambda w, h: B8.curtains(w, h, area=(0.14, 0.62)), "They Made the Tabernacle"),
    *chunks("36:14-19", B8.coverings, None),
    *chunks("36:20-26", B8.board, "The Boards and the Sockets"),
    *chunks("36:27-34", lambda w, h: B8.frame_plan(w, h, bars=True), None),
    *chunks("36:35-38", B8.veil_elev, "The Veil and the Screen"),
    *chunks("37:1-5", B8.ark, "Bezalel Made the Ark"),
    *chunks("37:6-9", B8.mercy_seat, None),
    *chunks("37:10-16", B8.table, "The Table and Its Vessels"),
    *chunks("37:17-24", B8.lampstand, "The Candlestick"),
    *chunks("37:25-29", lambda w, h: Q.incense_altar(w, h, smoke=True), "The Altar of Incense"),
    *chunks("38:1-7", B8.altar, "The Altar of Burnt-offering"),
    *chunks("38:8", N.mirrors, None),
    *chunks("38:9-15", B8.court, "The Court"),
    *chunks("38:16-20", B8.court_elev, None),
    *chunks("38:21-23", lambda w, h: Q.craftsmen("n7", w, h), "The Sum of the Things"),
    *chunks("38:24-25", N.metals, None),
    *chunks("38:26-31", N.census, None),
]


@P("EXO-C11-00-Title", "Chapter 11 · The Willing Offering")
def title():
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A1A2E"></rect>' + N.bringing("t11", 760, 1080, 1101)
    return chapter_title(11, "第十一話", "The Willing Offering", "Exodus 35 – 38", svg, B8.INK, v("35:29", to="freewill-offering unto Jehovah;").rstrip(";"), "Exodus · Volume Two")

PAGES += blueprints(ITEMS, "EXO-C11", START, "The Willing Offering", end=end_mark("NEXT · THE GLORY", "right: 12px; bottom: 12px"))
