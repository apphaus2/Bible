"""Exodus volume, Chapter 9 — Holy to Jehovah (Exodus 28–31). Every verse, word for word from ref/asv.
Blueprint pages like chapter 8, laid out by pack(): the verses are listed as panels (verses, drawing, heading) and packed
into pages of up to three panels and about 1,250 characters, each panel's height in proportion to its words."""
import sys, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god
from reuse import panels
from exo import G, art8 as B8, art9 as Q
from genesis.ch02 import rows, W1

v, sp = G.v, G.span
TB, = [panels("digest/exodus/book-05/" + n + ".dc.html") for n in ["EX5-P02-Tables"]]
INK = B8.INK
START = 136                                  # chapter 8 ends on page 135
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def say(refs):
    """God's words for a run of verses ("28:1-2")."""
    return [("god", sp(refs))]

def intro(ref, to, rest_refs=None, frm=None):
    """A narration lead-in ("And Jehovah spake unto Moses, saying,") then God's words."""
    out = [("cap", v(ref, to=to))]
    if frm: out.append(("god", v(ref, frm=frm) + ((" " + sp(rest_refs)) if rest_refs else "")))
    elif rest_refs: out.append(("god", sp(rest_refs)))
    return out

# (verse label, words, drawing, heading)
ITEMS = [
    ("28:1–2", say("28:1-2"), Q.priests, "Holy Garments for Glory and for Beauty"),
    ("28:3–4", say("28:3-4"), Q.garments, None),
    ("28:5–8", say("28:5-8"), Q.ephod, None),
    ("28:9–12", say("28:9-12"), Q.onyx, "Stones of Memorial"),
    ("28:13–14", say("28:13-14"), Q.chains, None),
    ("28:15–16", say("28:15-16"), lambda w, h: Q.breastplate(w, h, names=False), None),
    ("28:17–21", say("28:17-21"), Q.breastplate, "The Breastplate of Judgment"),
    ("28:22–25", say("28:22-25"), lambda w, h: Q.ephod(w, h, stones=True, chains=True), None),
    ("28:26–28", say("28:26-28"), lambda w, h: Q.breastplate(w, h, names=False, rings=True), "Upon His Heart"),
    ("28:29–30", say("28:29-30"), Q.urim, None),
    ("28:31–33", say("28:31-33"), Q.robe, "A Golden Bell and a Pomegranate"),
    ("28:34–35", say("28:34-35"), lambda w, h: Q.robe(w, h, zoom=True), None),
    ("28:36–38", say("28:36-38"), Q.plate, "Holy to Jehovah"),
    ("28:39–41", say("28:39-41"), Q.sons_garments, None),
    ("28:42–43", say("28:42-43"), Q.sons_garments, None),
    ("29:1–3", say("29:1-3"), Q.bullock_rams, "To Hallow Them"),
    ("29:4–6", say("29:4-6"), Q.dressing, None),
    ("29:7–9", say("29:7-9"), lambda w, h: Q.dressing(w, h, oil=True), None),
    ("29:10–14", say("29:10-14"), Q.offering_fire, "The Bullock of the Sin-offering"),
    ("29:15–18", say("29:15-18"), lambda w, h: Q.offering_fire(w, h, beast="ram"), None),
    ("29:19–21", say("29:19-21"), Q.marks, "The Ram of Consecration"),
    ("29:22–25", say("29:22-25"), Q.wave, None),
    ("29:26–28", say("29:26-28"), Q.wave, "A Wave-offering before Jehovah"),
    ("29:29–30", say("29:29-30"), lambda w, h: Q.days7(w, h, "SEVEN DAYS · THE HOLY GARMENTS"), None),
    ("29:31–34", say("29:31-34"), Q.boil, "Seven Days Shalt Thou Consecrate Them"),
    ("29:35–37", say("29:35-37"), lambda w, h: Q.days7(w, h, "SEVEN DAYS · ATONEMENT FOR THE ALTAR"), None),
    ("29:38–42", say("29:38-42"), Q.lambs_day, "Two Lambs Day by Day"),
    ("29:43–46", say("29:43-46"), Q.glory_tent, None),
    ("30:1–5", say("30:1-5"), Q.incense_altar, "An Altar to Burn Incense"),
    ("30:6–10", say("30:6-10"), lambda w, h: Q.incense_altar(w, h, smoke=True), None),
    ("30:11–13", intro("30:11", "saying,", "30:12-13"), Q.half_shekel, "Half a Shekel"),
    ("30:14–16", say("30:14-16"), Q.half_shekel, None),
    ("30:17–21", intro("30:17", "saying,", "30:18-21"), Q.laver, "A Laver of Brass"),
    ("30:22–25", intro("30:22", "saying,", "30:23-25"), Q.spices, "A Holy Anointing Oil"),
    ("30:26–30", say("30:26-30"), Q.anointed, None),
    ("30:31–33", say("30:31-33"), Q.spices, None),
    ("30:34–38", intro("30:34", "unto Moses,", "30:35-38", frm="Take unto thee"), Q.incense_mix, "Incense, Pure and Holy"),
    ("31:1–5", intro("31:1", "saying,", "31:2-5"), lambda w, h: Q.craftsmen("qa", w, h), "I Have Called by Name Bezalel"),
    ("31:6–11", say("31:6-11"), Q.works, None),
    ("31:12–14", intro("31:12", "saying,", "31:13-14"), lambda w, h: Q.days7(w, h, "VERILY YE SHALL KEEP MY SABBATHS"), "A Sign between Me and You"),
    ("31:15–17", say("31:15-17"), lambda w, h: Q.days7(w, h, "SIX DAYS · A SABBATH OF SOLEMN REST"), None),
]

def nchars(words): return sum(len(t) for _, t in words)

def panel(h, label_, words, art, extra=""):
    """One blueprint panel: the drawing, and in the left half the words (caption then Voice box), sized to fit."""
    bw = 380; n = nchars(words)
    size = max(11.5, min(19, (bw * (h - 60) / (0.6 * n)) ** 0.5 * 0.82))
    o, y = [], 34
    for kind, text in words:
        if kind == "cap":
            o.append(cap(text, f"left: 12px; top: {y}px", size=10.5, maxw=bw)); y += 38
        else:
            o.append(god(text, f"left: 12px; top: {y}px", size=round(size * 2) / 2, maxw=bw))
    return new(INK, W1, h, art(W1, h), "".join(o) + vref("EX " + label_, "right: 8px; top: 8px") + extra)

def pack(items, budget=1500, most=3):
    pages, cur, chars = [], [], 0
    for it in items:
        n = nchars(it[1])
        if cur and (chars + n > budget or len(cur) == most or it[3]):
            pages.append(cur); cur, chars = [], 0
        cur.append(it); chars += n
    if cur: pages.append(cur)
    return pages

def span_label(group):
    a = group[0][0].split("–")[0]; ca = a.split(":")[0]
    cb, vb = group[-1][0].split(":"); vb = vb.split("–")[-1]
    return f"{a}–{vb}" if ca == cb else f"{a}–{cb}:{vb}"

def make(k, group):
    total = sum(nchars(it[1]) for it in group); gaps = 12 * (len(group) - 1)
    hs = [max(190, round((1022 - gaps) * nchars(it[1]) / total)) for it in group]
    hs[-1] = None
    t, h = rows(*hs)
    stamp = lambda lab: mk.stamp(int(lab.split(":")[0]), "right: 14px; bottom: 14px") if lab.split(":")[1].split("–")[0] == "1" else ""   # a chapter stamp where a Bible chapter begins
    body = "".join(panel(hh, it[0], it[1], it[2], stamp(it[0])) for hh, it in zip(h, group))
    head = group[0][3] or "Holy to Jehovah"
    title = f"Exodus {span_label(group)} — {head}"
    def fn(): return page(title, t, body, START + k)
    slug = re.sub(r"[^A-Za-z]", "", head.title())[:18]
    return (f"EXO-C09-P{k + 1:02d}-{slug}", f"{START + k} · {head}", fn)


@P("EXO-C09-00-Title", "Chapter 9 · Holy to Jehovah")
def title():
    svg = Q.bp(760, 1080) + Q.stage("qt", 760, 1080, [(Q.high_priest, 0.3)], x0=0.3, x1=0.7)[len(Q.bp(760, 1080)):]
    return chapter_title(9, "第九話", "Holy to Jehovah", "Exodus 28 – 31", svg, INK, v("28:36", frm="HOLY TO JEHOVAH"), "Exodus · Volume Two")

GROUPS = pack(ITEMS)
for _k, _g in enumerate(GROUPS):
    PAGES.append(make(_k, _g))

@P(f"EXO-C09-P{len(GROUPS) + 1:02d}-Tables", f"{START + len(GROUPS)} · Tables of Stone")
def tables():
    t, h = rows(None)
    k = len(GROUPS)
    r1 = use(TB[0], over=cap(v("31:18"), "left: 12px; bottom: 60px", size=13, maxw=420) + end_mark("NEXT · THE GOLDEN CALF", "left: 12px; bottom: 12px") + vref("EX 31:18", "right: 12px; top: 12px"))
    return page("Exodus 31:18 — Tables of Stone", t, r1, START + k)
