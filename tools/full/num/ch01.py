"""Numbers volume, Chapter 1 — The Numbering (Numbers 1–2). Every verse, word for word from ref/eng-asv.
The census is set as tally cells (one tribe a cell, the number in a red tag); the twelve princes and the four camps of
Numbers 2 as Voice-box cells (God's words) beside a blueprint plan of the camp round about the tent of meeting."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus5 as V
from fx import new, vref, page, chapter_title, end_mark, cols, cap, god
from exo import art as A, art8 as B8
from exo.kit import law
from num import G, art as K
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY, DUSK
from genesis.ch03 import SAND, hud

v, sp = G.v, G.span
START = 1
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco
INK = B8.INK

def tally(tribe, refs, count, accent=None, size=12.5, of=None):
    """One tribe of the census: its name, the verses in full, and the number in a red tag (data-label)."""
    a, b = refs.split("-"); c = a.split(":")[0]
    accent = accent or K.TRIBE_C[tribe]
    text = sp(refs)
    rng = a if b.split(':')[-1] == a.split(':')[-1] else f"{a}–{b.split(':')[-1]}"
    tag = f"{of} · NUM {rng}" if of else f"NUM {rng}"
    return (f'\n    <div style="position: relative; min-height: 0; overflow: hidden; border: 3px solid #0D0D0F; background: #12113A; color: #F3EFE6; padding: 9px 12px 10px; display: flex; flex-direction: column; gap: 6px; box-shadow: inset 6px 0 0 {accent}">'
            f'\n      <div style="display: flex; justify-content: space-between; align-items: center; gap: 8px; padding-left: 6px"><span data-label style="font-family: Anton, sans-serif; font-size: 26px; line-height: 1; letter-spacing: 0.04em; color: {accent if accent not in ("#3A3A5A", "#6A6A8A") else "#B8C0E8"}">{tribe}</span>'
            f'<span data-label style="padding: 3px 9px; background: #F3EFE6; color: #D7261E; border: 2px solid #D7261E; font-family: Anton, sans-serif; font-size: 20px; letter-spacing: 0.06em">{count}</span></div>'
            f'\n      <span data-label style="padding-left: 6px; font-size: 9px; font-weight: 600; letter-spacing: 0.18em; opacity: 0.8">{tag}</span>'
            f'\n      <div style="padding-left: 6px; font-size: {size}px; font-weight: 600; line-height: 1.45; letter-spacing: 0.03em; text-transform: uppercase">{text}</div>\n    </div>')

def prince(tribe, text, ref, cell, w):
    """One of the twelve princes (Numbers 1:5–15, God's words): a Voice cell with the standard of the tribe."""
    svg = K.standard(146, 98, 2.0, K.TRIBE_C[tribe], pole=36)
    return law(tribe, text, ref, svg, cell=cell, w=w)

def fit_size(n, w, h, lo=12, hi=22):
    """The largest Anton size at which n characters fill a w x h box (with a heading line above)."""
    return max(lo, min(hi, round(((h - 44) * (w - 26) / (0.47 * 1.18 * n)) ** 0.5 * 0.9 * 2) / 2))

def camp_cells(items, hh):
    """Voice cells for one camp of Numbers 2, two by two: (heading, refs) — each a tribe and its host, then the camp's total."""
    out, ch = [], (hh - 12) // 2
    texts = [sp(refs) for _, refs in items]
    size = min(fit_size(len(t), 336, ch) for t in texts)        # one size for the whole camp
    for (hd, refs), text in zip(items, texts):
        a, _, b = refs.partition("-")
        out.append(law(hd, text, f"NUM {a}" + (f"–{b.split(':')[-1]}" if b else ""), "", size=size, cell=ch, w=336))
    return grid(out, "repeat(2, minmax(0, 1fr))")


@P("NUM-C01-00-Title", "Chapter 1 · The Numbering")
def title():
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#0B1A2E"></rect>'
           + f'<g transform="translate(0 370)">{K.camp_plan(760, 560, title="THE CAMP OF ISRAEL · NUMBERS 2", totals=False)}</g>')
    return chapter_title(1, "第一話", "The Numbering", "Numbers 1 – 2", svg, "#0B1A2E",
                         v("1:2", to="children of Israel,"), "Numbers · Volume Four")


@P("NUM-C01-P01-TakeYeTheSum", "1 · Take Ye the Sum")
def p01():
    t, h = rows(330, 300, None)
    r1 = new(SKY, W1, h[0], K.wilderness_camp("n1a", W1, h[0], 111, cast=[(A.moses, 0.42, 0.5, True)]),
             cap(v("1:1"), "left: 12px; top: 12px", size=11.5, maxw=380) + mk.stamp(1, "right: 14px; top: 12px") + vref("NUM 1:1", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], K.muster("n1b", W1, h[1], 112),
             god(v("1:2") + " " + v("1:3"), "left: 12px; top: 12px", size=17, maxw=470) + vref("NUM 1:2–3", "right: 12px; bottom: 12px"))
    r3 = new(SAND, W1, h[2], K.princes("n1c", W1, h[2], 113),
             god(v("1:4"), "left: 12px; top: 12px", size=18, maxw=520) + vref("NUM 1:4", "right: 12px; bottom: 12px"))
    return page("Numbers 1:1–4 — Take Ye the Sum", t, r1 + r2 + r3, START + 0)


@P("NUM-C01-P02-Princes", "2 · The Men That Shall Stand with You")
def p02():
    t, h = rows(200, None, 130)
    r1 = new(NIGHT, W1, h[0], X.cosmic(W1, h[0]), god(v("1:5", to="stand with you."), "left: 12px; top: 12px", size=22, maxw=560) + vref("NUM 1:5", "right: 12px; bottom: 12px"))
    names = [("REUBEN", v("1:5", frm="Of Reuben:"), "1:5"), ("SIMEON", v("1:6"), "1:6"), ("JUDAH", v("1:7"), "1:7"), ("ISSACHAR", v("1:8"), "1:8"),
             ("ZEBULUN", v("1:9"), "1:9"), ("EPHRAIM", v("1:10", to="Ammihud."), "1:10"), ("MANASSEH", v("1:10", frm="Of Manasseh:"), "1:10"),
             ("BENJAMIN", v("1:11"), "1:11"), ("DAN", v("1:12"), "1:12"), ("ASHER", v("1:13"), "1:13"), ("GAD", v("1:14"), "1:14"), ("NAPHTALI", v("1:15"), "1:15")]
    cell = (h[1] - 24) // 3
    cells = [prince(tr, tx, "NUM " + rf, cell, 160) for tr, tx, rf in names]
    r3 = new(SAND, W1, h[2], K.princes("n2c", W1, h[2], 123), cap(v("1:16"), "left: 12px; top: 12px", size=11, maxw=540))
    return page("Numbers 1:5–16 — The Men That Shall Stand with You", t, r1 + grid(cells, "repeat(3, minmax(0, 1fr))", ncol=4) + r3, START + 1)


@P("NUM-C01-P03-Assembled", "3 · They Declared Their Pedigrees")
def p03():
    t, h = rows(300, None)
    r1 = new(SAND, W1, h[0], K.muster("n3a", W1, h[0], 131, rows_=3, per=12),
             cap(v("1:17") + " " + v("1:18") + " " + v("1:19"), "left: 12px; top: 12px", size=11.5, maxw=460) + vref("NUM 1:17–19", "right: 12px; bottom: 12px"))
    cells = [tally("REUBEN", "1:20-21", "46,500", size=13.5), tally("SIMEON", "1:22-23", "59,300", size=13.5), tally("GAD", "1:24-25", "45,650", size=13.5)]
    return page("Numbers 1:17–25 — They Declared Their Pedigrees", t, r1 + grid(cells, "repeat(3, minmax(0, 1fr))", ncol=1), START + 2)


@P("NUM-C01-P04-Judah", "4 · All That Were Able to Go Forth to War")
def p04():
    cells = [tally("JUDAH", "1:26-27", "74,600"), tally("ISSACHAR", "1:28-29", "54,400"), tally("ZEBULUN", "1:30-31", "57,400"),
             tally("EPHRAIM", "1:32-33", "40,500", of="JOSEPH"), tally("MANASSEH", "1:34-35", "32,200", of="JOSEPH"), tally("BENJAMIN", "1:36-37", "35,400")]
    return page("Numbers 1:26–37 — All That Were Able to Go Forth to War", "minmax(0, 1fr)", grid(cells, "repeat(3, minmax(0, 1fr))"), START + 3)


@P("NUM-C01-P05-Total", "5 · Six Hundred Thousand")
def p05():
    t, h = rows(None, 440)
    cells = [tally("DAN", "1:38-39", "62,700"), tally("ASHER", "1:40-41", "41,500"), tally("NAPHTALI", "1:42-43", "53,400")]
    top = f'\n  <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; min-height: 0">' + "".join(cells) + "\n  </div>"
    r2 = new(SAND, W1, h[1], K.muster("n5b", W1, h[1], 151, rows_=5, per=14, scribes=False),
             cap(v("1:44") + " " + v("1:45") + " " + v("1:46"), "left: 12px; top: 12px", size=12, maxw=440)
             + hud("603,550", "right: 16px; top: 16px", size=46) + vref("NUM 1:44–46", "right: 12px; bottom: 12px"))
    return page("Numbers 1:38–46 — Six Hundred Thousand", t, top + r2, START + 4)


@P("NUM-C01-P06-Levites", "6 · The Tribe of Levi Thou Shalt Not Number")
def p06():
    t, h = rows(280, 330, None)
    r1 = new(SAND, W1, h[0], K.levites_round("n6a", W1, h[0], 161), cap(v("1:47"), "left: 12px; top: 12px", size=12, maxw=420) + vref("NUM 1:47", "right: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], X.cosmic(W1, h[1]), cap(v("1:48"), "left: 12px; top: 12px", size=11)
             + god(v("1:49") + " " + v("1:50") + " " + v("1:51"), "left: 12px; top: 50px", size=16.5, maxw=640) + vref("NUM 1:48–51", "right: 12px; bottom: 12px"))
    r3 = new(SKY, W1, h[2], K.wilderness_camp("n6c", W1, h[2], 163),
             god(v("1:52") + " " + v("1:53"), "left: 12px; top: 12px", size=15, maxw=480) + cap(v("1:54"), "right: 12px; bottom: 30px", size=11, maxw=300) + vref("NUM 1:52–54", "right: 12px; bottom: 8px"))
    return page("Numbers 1:47–54 — The Tribe of Levi Thou Shalt Not Number", t, r1 + r2 + r3, START + 5)


def camp_page(side, cap_items, refs_title, head, num, top=None, bottom=None):
    """A page for one camp of Numbers 2: the plan with that side lit, beside the Voice cells of its tribes."""
    ph = 300 if (top or bottom) else 400
    t, h = rows(*[x for x in (top[0] if top else False, ph, None, bottom[0] if bottom else False) if x is not False])
    parts, i = [], 0
    if top: parts.append(top[1](h[i])); i += 1
    parts.append(new(B8.INK, W1, h[i], K.camp_plan(W1, h[i], hi=side, title=f"{head} · NUMBERS 2"), "")); i += 1
    parts.append(camp_cells(cap_items, h[i])); i += 1
    if bottom: parts.append(bottom[1](h[i]))
    return page(f"Numbers {refs_title} — {head.title()}", t, "".join(parts), num)


@P("NUM-C01-P07-East", "7 · Toward the Sunrising")
def p07():
    top = (300, lambda hh: new(SKY, W1, hh, K.wilderness_camp("n7a", W1, hh, 171, cast=[(A.aaron, 0.38, 0.52), (A.moses, 0.45, 0.5, True)]),
                              cap(v("2:1"), "left: 12px; top: 12px", size=11) + god(v("2:2"), "left: 12px; top: 50px", size=16, maxw=420)
                              + mk.stamp(2, "right: 14px; top: 12px") + vref("NUM 2:1–2", "right: 12px; bottom: 12px")))
    items = [("THE CAMP OF JUDAH · EAST", "2:3-4"), ("ISSACHAR", "2:5-6"), ("ZEBULUN", "2:7-8"), ("186,400 · THEY SHALL SET FORTH FIRST", "2:9")]
    return camp_page("E", items, "2:1–9", "TOWARD THE SUNRISING", START + 6, top=top)


@P("NUM-C01-P08-South", "8 · On the South Side")
def p08():
    bottom = (250, lambda hh: new(SAND, W1, hh, K.levites_round("n8c", W1, hh, 183),
                                 god(v("2:17"), "left: 12px; top: 12px", size=16, maxw=520) + vref("NUM 2:17", "right: 12px; bottom: 12px")))
    items = [("THE CAMP OF REUBEN · SOUTH", "2:10-11"), ("SIMEON", "2:12-13"), ("GAD", "2:14-15"), ("151,450 · SECOND", "2:16")]
    return camp_page("S", items, "2:10–17", "ON THE SOUTH SIDE", START + 7, bottom=bottom)


@P("NUM-C01-P09-West", "9 · On the West Side")
def p09():
    items = [("THE CAMP OF EPHRAIM · WEST", "2:18-19"), ("MANASSEH", "2:20-21"), ("BENJAMIN", "2:22-23"), ("108,100 · THIRD", "2:24")]
    return camp_page("W", items, "2:18–24", "ON THE WEST SIDE", START + 8)


@P("NUM-C01-P10-North", "10 · So They Encamped by Their Standards")
def p10():
    bottom = (330, lambda hh: new(DUSK, W1, hh, K.wilderness_camp("n10c", W1, hh, 1103, dusk=True),
                                 cap(v("2:32") + " " + v("2:33") + " " + v("2:34"), "left: 12px; top: 12px", size=11.5, maxw=470)
                                 + hud("603,550", "right: 16px; top: 16px", size=36) + vref("NUM 2:32–34", "left: 12px; bottom: 12px")
                                 + end_mark("NEXT · THE CHARGE OF THE LEVITES", "right: 10px; bottom: 10px")))
    items = [("THE CAMP OF DAN · NORTH", "2:25-26"), ("ASHER", "2:27-28"), ("NAPHTALI", "2:29-30"), ("157,600 · HINDMOST", "2:31")]
    return camp_page("N", items, "2:25–34", "ON THE NORTH SIDE", START + 9, bottom=bottom)
