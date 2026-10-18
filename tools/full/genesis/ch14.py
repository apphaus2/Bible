"""Genesis volume, Chapter 14 — The Brothers in Egypt (Genesis 42–43). Word for word from ref/asv.
The brothers' retelling to Jacob (42:29–34) is abridged: 42:29–30 and the end of 42:34 in full, 42:31–33 omitted.
Every other verse is in full. talk() is a dialogue panel used by the later Joseph chapters: a close-up face with a
caption ("And he said,") and a balloon beside it."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from faces_ex import F
from reuse import panels
from genesis import G, art as X, art2 as Y, art3 as Z, art10 as T, art11 as U, art12 as V12
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import LAMP, RED, BLUE
from genesis.ch12 import NILE, COURT, CELL
from mk import defs, face

v, sp = G.v, G.span
B5 = "reference/genesis/book-05/"
Gr, = (panels(B5 + n + ".dc.html") for n in ["B5-P07-Granaries"])
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
BENJAMIN = F("adam", skin="#E3B08A", shadow="#B97A58", hair="#2A1A10", hl="#5A4A3E", light="#FFE680")
STEWARD = V12.BAKER
ISRAEL, ISRAEL_WEEP = U.ISRAEL, U.ISRAEL_WEEP
START = 216                                  # chapter 13 ends on page 215
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco


def talk(tok, h, bg, lines, w=W1, flip=False, ref=None, size=12.5, extra=""):
    """A dialogue panel: a face sized to the panel and, beside it, a column of (caption | balloon) pieces.
    lines is a list of ("cap", text) or ("say", text) in reading order."""
    full = w > 400
    left = 300 if full else 140
    side = f"left: {left}px" if not flip else "left: 12px"
    bw = (w - left - 14) if not flip else (w - 314 if full else w - 154)
    o, y = [], 12
    for kind, text in lines:
        n = len(text)
        if kind == "cap":
            o.append(cap(text, f"{side}; top: {y}px", size=10 if not full else 10.5, maxw=bw))
            y += 34 + 15 * (n // (bw // 7 or 1))
        else:
            long_ = n > 160                       # long speeches get a deeper oval so the corners don't cut the text
            pad = (f"{min(48, 18 + n // 12)}px 40px" if full else f"{min(36, 16 + n // 12)}px 26px") if long_ else ("18px 24px" if full else "16px 18px")
            o.append(balloon(text, f"{side}; top: {y}px", bw, size=size if full else size - 1, pad=pad))
            y += 50 + 17 * (n // max(1, (bw - 40) // 7)) + (n // 6 if long_ else 0)
    if ref: o.append(vref(ref, "left: 12px; bottom: 12px" if not flip else "right: 12px; bottom: 12px"))
    return new(bg, w, h, fc(tok, h, w=w, flip=flip), "".join(o) + extra)


@P("GEN-C14-00-Title", "Chapter 14 · The Brothers in Egypt")
def title():
    return chapter_title(14, "第十四話", "The Brothers in Egypt", "Genesis 42 – 43", f'<g transform="translate(-140 180) scale(1.5)">{Gr[1].svg}</g>', NIGHT,
                         v("42:8"), "Genesis · Volume One")


@P("GEN-C14-P01-GoDown", "216 · Get You Down Thither")
def p01():
    t, h = rows(330, 260, None)
    r1 = talk(ISRAEL, h[0], GOLDEN, [("cap", v("42:1", to="unto his sons,")), ("say", v("42:1", frm="Why do")), ("cap", v("42:2", to="he said,")), ("say", v("42:2", frm="Behold"))], ref="GEN 42:1–2")
    r2 = new(SAND, W1, h[1], defs("c141b", *ALL) + T.stage("c141b", W1, h[1], 1412, "sand", [(("man", c), 0.08 + i * 0.075, 0.46, False) for i, c in enumerate(U.BROS * 2)][:10],
                                                              props=Z.N.ass(W1 * 0.86, h[1] * 0.92, 0.22, flip=False)),
             cap(v("42:3"), "left: 12px; top: 12px", size=11, maxw=420) + hud("10", "right: 14px; top: 12px", size=28) + vref("GEN 42:3", "right: 12px; bottom: 12px"))
    r3 = cols(new(GREENLIT, W2, h[2], fc(BENJAMIN, h[2]), cap(v("42:4"), "right: 8px; top: 8px", size=10.5, maxw=200) + vref("GEN 42:4", "left: 8px; bottom: 8px")),
              new(SAND, W2, h[2], defs("c141c", *ALL) + V12.bread_lines("c141c", W2, h[2], 1413), cap(v("42:5"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 42:5", "right: 8px; bottom: 8px")))
    return page("Genesis 42:1–5 — Get You Down Thither", t, r1 + r2 + r3, START + 0)


@P("GEN-C14-P02-Bowed", "217 · Ye Are Spies")
def p02():
    t, h = rows(400, None)
    r1 = use(Gr[1], over=cap(v("42:6"), "left: 12px; bottom: 12px", size=11, maxw=420) + vref("GEN 42:6", "right: 12px; bottom: 12px"))
    r2 = talk(V12.JOSEPH_EG_STERN, h[1], COURT, [("cap", v("42:7", to="and he said unto them,")), ("say", v("42:7", frm="Whence", to="come ye?")),
                                                 ("cap", v("42:8") + " " + v("42:9", to="said unto them,")),
                                                 ("say", v("42:9", frm="Ye are spies;"))], ref="GEN 42:7–9", extra="")
    return page("Genesis 42:6–9 — Ye Are Spies", t, r1 + r2, START + 1)


@P("GEN-C14-P03-Twelve", "218 · We Are Twelve Brethren")
def p03():
    t, h = rows(420, 200, None)
    r1 = cols(talk(U.BROTHER, h[0], RED, [("cap", v("42:7", frm="And they said,", to="said,")), ("say", v("42:7", frm="From the land")), ("cap", v("42:10", to="unto him,")), ("say", v("42:10", frm="Nay") + " " + v("42:11"))], w=W2, ref="GEN 42:7, 10–11", size=11.5),
              talk(V12.JOSEPH_EG_STERN, h[0], COURT, [("cap", v("42:12", to="unto them,")), ("say", v("42:12", frm="Nay"))], w=W2, ref="GEN 42:12"))
    r2 = talk(U.REUBEN, h[1], GOLDEN, [("cap", v("42:13", to="they said,")), ("say", v("42:13", frm="We thy"))], ref="GEN 42:13")
    r3 = talk(V12.JOSEPH_EG_STERN, h[2], COURT, [("cap", v("42:14", to="saying,")), ("say", v("42:14", frm="Ye are spies:") + " " + v("42:15") + " " + v("42:16"))], ref="GEN 42:14–16")
    return page("Genesis 42:10–16 — We Are Twelve Brethren", t, r1 + r2 + r3, START + 2)


@P("GEN-C14-P04-Guilty", "219 · We Are Verily Guilty")
def p04():
    t, h = rows(150, 270, None)
    r1 = new(V12.JAIL, W1, h[0], defs("c144a", *ALL) + V12.prison("c144a", W1, h[0], 1441, figures=[(("shade", None), 0.1 + i * 0.09, 0.4, False) for i in range(10)]),
             cap(v("42:17"), "left: 12px; top: 12px", size=11.5) + hud("3 DAYS", "right: 14px; top: 12px", size=20) + vref("GEN 42:17", "right: 12px; bottom: 10px"))
    r2 = talk(V12.JOSEPH_EG, h[1], COURT, [("cap", v("42:18", to="the third day,")), ("say", v("42:18", frm="This do") + " " + v("42:19") + " " + v("42:20", to="shall not die.")),
                                            ("cap", v("42:20", frm="And they did"))], ref="GEN 42:18–20")
    r3 = cols(talk(U.BROTHER, h[2], RED, [("cap", v("42:21", to="one to another,")), ("say", v("42:21", frm="We are verily"))], w=W2, ref="GEN 42:21", size=12),
              talk(U.REUBEN, h[2], GOLDEN, [("cap", v("42:22", to="saying,")), ("say", v("42:22", frm="Spake I"))], w=W2, ref="GEN 42:22", size=12))
    return page("Genesis 42:17–22 — We Are Verily Guilty", t, r1 + r2 + r3, START + 3)


@P("GEN-C14-P05-Simeon", "220 · He Turned Himself About, and Wept")
def p05():
    t, h = rows(300, 240, None)
    r1 = new(COURT, W1, h[0], fc(V12.JOSEPH_EG_WEEP, h[0], w=W1),
             cap(v("42:23"), "left: 300px; top: 12px", size=11, maxw=380)
             + cap(v("42:24"), "left: 300px; top: 100px", size=11, maxw=380) + vref("GEN 42:23–24", "left: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], defs("c145b", *ALL) + V12.bread_lines("c145b", W1, h[1], 1452),
             cap(v("42:25"), "left: 12px; top: 12px", size=10.5, maxw=440) + cap(v("42:26"), "right: 12px; top: 12px", size=10.5, maxw=220) + vref("GEN 42:25–26", "right: 12px; bottom: 12px"))
    r3 = new(DUSK, W1, h[2], defs("c145c", *ALL) + T.stage("c145c", W1, h[2], 1453, "dusk", [(("man", c), 0.4 + i * 0.1, 0.42, True) for i, c in enumerate(U.BROS[:5])],
                                                              props=Z.N.ass(W1 * 0.2, h[2] * 0.9, 0.24) + Z.R.sack(W1 * 0.3, h[2] * 0.9, 1.4)
                                                              + "".join(f'<ellipse cx="{W1 * 0.3 + dx:.0f}" cy="{h[2] * 0.9 - 64:.0f}" rx="7" ry="3" fill="#E8E8F0" stroke="#0D0D0F" stroke-width="1"></ellipse>' for dx in (-6, 4, 12))),
             cap(v("42:27"), "left: 12px; top: 12px", size=10.5, maxw=330)
             + cap(v("42:28", to="unto his brethren,"), "right: 12px; top: 12px", size=10.5)
             + balloon(v("42:28", frm="My money", to="in my sack:"), "right: 12px; top: 46px", 230, size=12, pad="14px 18px")
             + cap(v("42:28", frm="and their heart", to="saying,"), "left: 12px; top: 120px", size=10.5, maxw=300)
             + balloon(v("42:28", frm="What is this"), "left: 12px; bottom: 12px", 280, size=12, pad="14px 18px") + vref("GEN 42:27–28", "right: 12px; bottom: 12px"))
    return page("Genesis 42:23–28 — He Turned Himself About, and Wept", t, r1 + r2 + r3, START + 4)


@P("GEN-C14-P06-Bereaved", "221 · Me Have Ye Bereaved")
def p06():
    t, h = rows(260, 330, None)
    told = v("42:30") + " … " + v("42:34", frm="so will I deliver")
    r1 = talk(U.REUBEN, h[0], GOLDEN, [("cap", v("42:29")), ("say", told)], ref="GEN 42:29–34",
              extra=f'    <span data-label style="position: absolute; right: 14px; bottom: 12px; padding: 3px 8px; background: #12113A; color: #FFD23F; font-size: 9px; font-weight: 600; letter-spacing: 0.18em">AS THEY TOLD IT · GEN 42:30–34 ABRIDGED</span>\n')
    r2 = talk(ISRAEL_WEEP, h[1], COLD, [("cap", v("42:35")), ("cap", v("42:36", to="unto them,")), ("say", v("42:36", frm="Me have"))], ref="GEN 42:35–36")
    r3 = cols(talk(U.REUBEN, h[2], GOLDEN, [("cap", v("42:37", to="saying,")), ("say", v("42:37", frm="Slay"))], w=W2, ref="GEN 42:37", size=12),
              talk(ISRAEL_WEEP, h[2], COLD, [("cap", v("42:38", to="he said,")), ("say", v("42:38", frm="My son"))], w=W2, ref="GEN 42:38", size=11.5))
    return page("Genesis 42:29–38 — Me Have Ye Bereaved", t, r1 + r2 + r3, START + 5)


@P("GEN-C14-P07-Judah", "222 · Ye Shall Not See My Face")
def p07():
    t, h = rows(150, 320, None)
    r1 = new(HOT, W1, h[0], Z.famine(W1, h[0], 1471), cap(v("43:1"), "left: 12px; top: 12px", size=13) + vref("GEN 43:1", "right: 12px; bottom: 10px"))
    r2 = talk(ISRAEL, h[1], GOLDEN, [("cap", v("43:2", to="said unto them,")), ("say", v("43:2", frm="Go again")), ("cap", v("43:6", to="Israel said,")), ("say", v("43:6", frm="Wherefore"))], ref="GEN 43:2, 6")
    r3 = talk(U.JUDAH, h[2], RUST, [("cap", v("43:3", to="saying,")), ("say", v("43:3", frm="The man") + " " + v("43:4") + " " + v("43:5"))], ref="GEN 43:3–5")
    return page("Genesis 43:1–6 — Ye Shall Not See My Face", t, r1 + r2 + r3, START + 6)


@P("GEN-C14-P08-Surety", "223 · I Will Be Surety for Him")
def p08():
    t, h = rows(300, None)
    r1 = talk(U.BROTHER, h[0], RED, [("cap", v("43:7", to="they said,")), ("say", v("43:7", frm="The man asked"))], ref="GEN 43:7")
    r2 = talk(U.JUDAH, h[1], RUST, [("cap", v("43:8", to="his father,")), ("say", v("43:8", frm="Send the lad") + " " + v("43:9") + " " + v("43:10"))], ref="GEN 43:8–10", size=13.5)
    return page("Genesis 43:7–10 — I Will Be Surety for Him", t, r1 + r2, START + 7)


@P("GEN-C14-P09-Present", "224 · A Little Balm, and a Little Honey")
def p09():
    t, h = rows(None, 230)
    r1 = talk(ISRAEL, h[0], GOLDEN, [("cap", v("43:11", to="unto them,")), ("say", v("43:11", frm="If it be so") + " " + v("43:12") + " " + v("43:13") + " " + v("43:14"))], ref="GEN 43:11–14", size=13.5)
    r2 = new(SAND, W1, h[1], defs("c149b", *ALL) + T.stage("c149b", W1, h[1], 1492, "sand", [("benjamin", 0.2, 0.46)] + [(("man", c), 0.3 + i * 0.07, 0.44) for i, c in enumerate(U.BROS[:5])],
                                                              props=Z.N.ass(W1 * 0.82, h[1] * 0.9, 0.22, flip=False) + Z.R.sack(W1 * 0.78, h[1] * 0.84, 1.2)),
             cap(v("43:15"), "right: 12px; top: 12px", size=10.5, maxw=330) + vref("GEN 43:15", "left: 12px; top: 12px"))
    return page("Genesis 43:11–15 — A Little Balm, and a Little Honey", t, r1 + r2, START + 8)


@P("GEN-C14-P10-Afraid", "225 · Because of the Money")
def p10():
    t, h = rows(260, 290, None)
    r1 = talk(V12.JOSEPH_EG, h[0], COURT, [("cap", v("43:16", to="of his house,")), ("say", v("43:16", frm="Bring the men")), ("cap", v("43:17"))], ref="GEN 43:16–17")
    r2 = talk(U.BROTHER, h[1], RED, [("cap", v("43:18", to="and they said,")), ("say", v("43:18", frm="Because of"))], ref="GEN 43:18")
    r3 = talk(U.JUDAH, h[2], RUST, [("cap", v("43:19") + " " + v("43:20", to="and said,")), ("say", v("43:20", frm="Oh, my lord") + " " + v("43:21") + " " + v("43:22"))], ref="GEN 43:19–22", size=12)
    return page("Genesis 43:16–22 — Because of the Money", t, r1 + r2 + r3, START + 9)


@P("GEN-C14-P11-Peace", "226 · Peace Be to You, Fear Not")
def p11():
    t, h = rows(260, 260, None)
    r1 = talk(STEWARD, h[0], COURT, [("cap", v("43:23", to="he said,")), ("say", v("43:23", frm="Peace be", to="your money.")), ("cap", v("43:23", frm="And he brought"))], ref="GEN 43:23")
    r2 = new(V12.EGYPT_BG, W1, h[1], defs("c1411b", *ALL) + V12.house_of_potiphar("c1411b", W1, h[1], 14112),
             cap(v("43:24") + " " + v("43:25"), "left: 12px; top: 12px", size=10.5, maxw=430) + vref("GEN 43:24–25", "right: 12px; bottom: 12px"))
    r3 = new(COURT, W1, h[2], defs("c1411c", *ALL) + T.stage("c1411c", W1, h[2], 14113, "palace", [("joseph_eg", 0.84, 0.36, True)],
                                                                 props="".join(Z.E.kneel(W1 * (0.12 + i * 0.07), h[2] * 0.9, round(h[2] / 560, 3), color=c, skin=Y.SKIN, flip=False) for i, c in enumerate(U.BROS * 2) if i < 9)),
             cap(v("43:26"), "left: 12px; top: 12px", size=11, maxw=500) + vref("GEN 43:26", "right: 12px; top: 12px"))
    return page("Genesis 43:23–26 — Peace Be to You, Fear Not", t, r1 + r2 + r3, START + 10)


@P("GEN-C14-P12-Benjamin", "227 · God Be Gracious unto Thee, My Son")
def p12():
    t, h = rows(260, 260, None)
    r1 = cols(talk(V12.JOSEPH_EG, h[0], COURT, [("cap", v("43:27", to="and said,")), ("say", v("43:27", frm="Is your father"))], w=W2, ref="GEN 43:27", size=12),
              talk(U.JUDAH, h[0], RUST, [("cap", v("43:28", to="they said,")), ("say", v("43:28", frm="Thy servant", to="yet alive.")), ("cap", v("43:28", frm="And they bowed"))], w=W2, ref="GEN 43:28", size=12))
    r2 = cols(new(GREENLIT, W2, h[1], fc(BENJAMIN, h[1]), cap(v("43:29", to="mother's son,"), "right: 8px; top: 8px", size=10.5, maxw=200) + vref("GEN 43:29", "left: 8px; bottom: 8px")),
              talk(V12.JOSEPH_EG, h[1], COURT, [("cap", v("43:29", frm="and said,", to="said,")), ("say", v("43:29", frm="Is this", to="unto me?")), ("cap", v("43:29", frm="And he said, God", to="said,")),
                                                ("say", v("43:29", frm="God be"))], w=W2, size=12))
    r3 = new(COURT, W1, h[2], fc(V12.JOSEPH_EG_WEEP, h[2], w=W1),
             cap(v("43:30"), "left: 300px; top: 12px", size=11, maxw=380)
             + cap(v("43:31", to="and said,"), "left: 300px; top: 100px", size=11, maxw=380)
             + balloon(v("43:31", frm="Set on"), "left: 290px; top: 150px", 200, size=14, pad="14px 18px") + vref("GEN 43:30–31", "left: 12px; bottom: 12px"))
    return page("Genesis 43:27–31 — God Be Gracious unto Thee, My Son", t, r1 + r2 + r3, START + 11)


@P("GEN-C14-P13-Feast", "228 · Five Times So Much")
def p13():
    t, h = rows(None, 260)
    r1 = new(COURT, W1, h[0], defs("c1413a", *ALL) + T.stage("c1413a", W1, h[0], 14131, "palace", [("joseph_eg", 0.86, 0.3, True)],
                                                                 props=feast_tables(W1, h[0])),
             cap(v("43:32"), "left: 12px; top: 12px", size=11, maxw=520)
             + cap(v("43:33"), "left: 12px; top: 116px", size=11, maxw=420) + vref("GEN 43:32–33", "right: 12px; bottom: 12px"))
    r2 = new("#12113A", W1, h[1], messes(W1, h[1]),
             cap(v("43:34"), "left: 12px; top: 12px", size=11.5, maxw=500) + hud("×5", "right: 14px; top: 12px", size=28)
             + end_mark("NEXT · I AM JOSEPH", "right: 14px; bottom: 12px") + vref("GEN 43:34", "left: 12px; bottom: 12px"))
    return page("Genesis 43:32–34 — Five Times So Much", t, r1 + r2, START + 12)

def feast_tables(w, h):
    """Three tables: Joseph by himself, the eleven by themselves, the Egyptians by themselves."""
    import exodus as E
    b = h * 0.9; o = []
    for x0, x1, n, c in [(0.04, 0.5, 11, None), (0.56, 0.74, 3, "#F3EFE6")]:
        o.append(f'<rect x="{w * x0:.0f}" y="{b - 46:.0f}" width="{w * (x1 - x0):.0f}" height="10" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>')
        for i in range(n):
            col = c or (U.BROS[i % 6] if i < 10 else "#C2456A")
            o.append(E.kneel(w * (x0 + 0.03 + i * (x1 - x0 - 0.06) / max(1, n - 1)), b, round(h / (1500 if n > 4 else 1200), 3), color=col, skin=Y.SKIN))
    return "".join(o)

def messes(w, h):
    o = []
    for i in range(11):
        x = w * (0.06 + i * 0.085); big = i == 10
        o.append(f'<ellipse cx="{x:.0f}" cy="{h * 0.7:.0f}" rx="{28 if big else 18}" ry="{10 if big else 7}" fill="#C9A86A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
        for k in range(5 if big else 1):
            o.append(f'<ellipse cx="{x + (k - 2) * 6 * big:.0f}" cy="{h * 0.7 - 6 - k * 6 * big:.0f}" rx="10" ry="5" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    return "".join(o) + Z.label(w * 0.91, h * 0.86, "BENJAMIN", "#FFD23F", 9)
