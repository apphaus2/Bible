"""Leviticus volume, Chapter 2 — The Consecration (Leviticus 6–8). Every verse, word for word from ref/eng-asv.
The law of each offering (6–7) as law cells; the consecration of Aaron and his sons (8), done as Exodus 29 commanded, as
narrated blueprint panels reusing Exodus chapter 9's drawings (exo/art9)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cap, god
from exo import art8 as B8, art9 as Q
from exo.kit import law_pages, set_book, blueprints
from lev import G, art as L
from genesis.ch02 import rows, W1

v, sp = G.v, G.span
set_book(G)
from lev import ch01 as _prev
START = _prev.START + len(_prev.PAGES) - 1     # straight after the previous chapter (its title page is unnumbered)
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco
SAY = "And Jehovah spake unto Moses, saying,"

def nar(refs): return [("nar", sp(refs))]

def chunks(refs, art, head, most=520):
    """Narration items for a run of verses, cut into even pieces of about `most` characters; the heading on the first."""
    c, vs = refs.split(":"); a, _, b = vs.partition("-"); a, b = int(a), int(b or a)
    total = sum(len(G.verses[(int(c), n)]) for n in range(a, b + 1))
    target = total / max(1, round(total / most + 0.49))
    out, cur, run = [], [], 0
    for n in range(a, b + 1):
        ln = len(G.verses[(int(c), n)])
        if cur and run + ln / 2 > target: out.append(cur); cur, run = [], 0
        cur.append(n); run += ln
    out.append(cur)
    return [(f"{c}:{g[0]}" + (f"–{g[-1]}" if len(g) > 1 else ""), nar(f"{c}:{g[0]}-{g[-1]}"), art, head if i == 0 else None) for i, g in enumerate(out)]


@P("LEV-C02-00-Title", "Chapter 2 · The Consecration")
def title():
    svg = Q.bp(760, 1080) + B8.V.rays(380, 600, 40, 40, 1000, color="#FFF4C2", op=0.2) + Q.stage("t2", 760, 1080, [(Q.son_priest, 0.5), (Q.high_priest, 0.42), (Q.son_priest, 0.5)], x0=0.2, x1=0.8)[len(Q.bp(760, 1080)):]
    return chapter_title(2, "第二話", "The Consecration", "Leviticus 6 – 8", svg, B8.INK, v("6:13"), "Leviticus · Volume Three")


LAWS = [
    ("A MATTER OF DEPOSIT", "6:1-3", L.pg_deposit, SAY, "The Law of the Trespass"),
    ("RESTORE IT IN FULL", "6:4-5", L.pg_restore, "", None),
    ("A RAM WITHOUT BLEMISH", "6:6-7", L.pg_ram, "", None),
    ("ON THE HEARTH ALL NIGHT", "6:8-9", L.pg_hearth, SAY, "The Law of the Burnt-offering"),
    ("HIS LINEN GARMENT", "6:10-11", L.pg_carry_ashes, "", None),
    ("IT SHALL NOT GO OUT", "6:12-13", L.pg_continual, "", None),
    ("THE LAW OF THE MEAL-OFFERING", "6:14-16", L.pg_handful, "", "The Law of the Meal-offering"),
    ("MOST HOLY", "6:17-18", L.pg_eat_court, "", None),
    ("IN THE DAY WHEN HE IS ANOINTED", "6:19-21", L.pg_anointed, SAY, None),
    ("WHOLLY BURNT", "6:22-23", L.pg_wholly, "", None),
    ("THE LAW OF THE SIN-OFFERING", "6:24-26", L.pg_eat_court, SAY, "The Law of the Sin-offering"),
    ("EARTHEN AND BRAZEN", "6:27-28", L.pg_holy_touch, "", None),
    ("IN THE HOLY PLACE", "6:29-30", L.pg_no_eat, "", None),
    ("THE LAW OF THE TRESPASS-OFFERING", "7:1-5", L.pg_fat, "", "The Law of the Trespass-offering"),
    ("ONE LAW FOR THEM", "7:6-7", L.pg_most_holy, "", None),
    ("THE SKIN · THE OVEN", "7:8-10", L.pg_skin, "", None),
    ("FOR A THANKSGIVING", "7:11-13", L.pg_thanks, "", "The Law of the Peace-offerings"),
    ("THE SAME DAY", "7:14-15", L.pg_same_day, "", None),
    ("A VOW, OR A FREEWILL-OFFERING", "7:16-18", L.pg_third, "", None),
    ("ANY UNCLEAN THING", "7:19-21", L.pg_unclean_flesh, "", None),
    ("NO FAT", "7:22-25", L.pg_no_fat, SAY, "Ye Shall Eat No Fat"),
    ("NO MANNER OF BLOOD", "7:26-27", L.pg_blood_bird, "", None),
    ("THE WAVE-BREAST", "7:28-31", L.pg_wave, SAY, "The Wave-breast and the Heave-thigh"),
    ("THE RIGHT THIGH", "7:32-34", L.pg_thigh, "", None),
    ("THE ANOINTING-PORTION", "7:35-36", L.pg_portion_ever, "", None),
    ("IN MOUNT SINAI", "7:37-38", L.pg_sinai, "", None),
]
PAGES += law_pages(LAWS, "LEV-C02", START, "The Law of the Offerings")
NEXT = START + len(PAGES) - 1                # the consecration pages follow (the title page is not numbered)

S8 = [
    ("8:1–3", [("cap", v("8:1")), ("god", sp("8:2-3"))], Q.bullock_rams, "Take Aaron and His Sons"),
    ("8:4–5", [("nar", v("8:4")), ("cap", v("8:5", to="the congregation,")), ("say", v("8:5", frm="This is"))], lambda w, h: Q.stage("q8a", w, h, [(Q.high_priest, 0.2)] + [(Q.son_priest, 0.3)] * 4), None),
    *chunks("8:6-9", Q.dressing, "Moses Clothed Aaron"),
    *chunks("8:10-13", lambda w, h: Q.dressing(w, h, oil=True), "The Anointing Oil"),
    *chunks("8:14-17", Q.offering_fire, "The Bullock of the Sin-offering"),
    *chunks("8:18-21", lambda w, h: Q.offering_fire(w, h, beast="ram"), "The Ram of the Burnt-offering"),
    *chunks("8:22-24", Q.marks, "The Ram of Consecration"),
    *chunks("8:25-29", Q.wave, None),
    ("8:30", nar("8:30"), lambda w, h: Q.dressing(w, h, oil=True), None),
    ("8:31–35", [("cap", v("8:31", to="his sons,")), ("say", v("8:31", frm="Boil") + " " + sp("8:32-35"))], lambda w, h: Q.days7(w, h, "SEVEN DAYS AT THE DOOR OF THE TENT"), "Seven Days"),
    ("8:36", nar("8:36"), Q.priests, None),
]
PAGES += blueprints(S8, "LEV-C02-S", NEXT, "The Consecration", book="Leviticus", end=end_mark("NEXT · STRANGE FIRE", "right: 12px; bottom: 12px"))
