"""Genesis volume, Chapter 3 — Babel to Abram's Covenant (Genesis 10–15). Every verse, word for word from ref/asv.
Genesis 10 (the table of the nations) is set as three 'scroll' pages of clan cells, and 11:10–26 (the generations of
Shem) as one scroll page with a lifespan bar per patriarch, like Genesis 5 in chapter 2."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus2 as E2, judges2 as S
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from genesis import G, art as X, art2 as Y, art3 as Z
from genesis.ch02 import rows, entry, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from mk import defs, face

v, sp = G.v, G.span
B3 = "digest/genesis/book-03/"
Brk, Bab, Call = (panels(B3 + n + ".dc.html") for n in ["B3-P01-Brick", "B3-P02-Babel", "B3-P03-Call"])
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
SAND = "linear-gradient(180deg, #FFE3B8 0%, #E8C88A 100%)"
HOT = "linear-gradient(180deg, #FFF4C2 0%, #FFC14D 100%)"
EGYPT = "linear-gradient(180deg, #FFC14D 0%, #E8A35A 100%)"
BLOOD = "linear-gradient(180deg, #2A0A0A 0%, #8A2A2A 60%, #FF8A3D 100%)"
GREEN = "linear-gradient(180deg, #8FD0E2 0%, #DDF0C8 100%)"
JAPHETH, HAM, SHEM = Y.SONS["japheth"], Y.SONS["ham"], Y.SONS["shem"]
START = 41                                   # chapter 2 ends on page 40
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def cosmic(w, h, cx=None): return X.cosmic(w, h, cx)

def clan(name, text, ref, accent="#FFD23F", of=None, size=12):
    """One cell of the table of the nations: the father's name, his line, and the verse in full."""
    tag = f"{of} · {ref}" if of else ref
    rule = (f'<svg viewBox="0 0 1000 12" preserveAspectRatio="none" style="display: block; width: 100%; height: 8px">'
            f'<rect x="0" y="5" width="1000" height="2" fill="{accent}"></rect>'
            + "".join(f'<rect x="{x}" y="1" width="10" height="10" fill="{accent}"></rect>' for x in (0, 330, 660, 990)) + '</svg>')
    return (f'\n    <div style="position: relative; min-height: 0; border: 3px solid #0D0D0F; background: #12113A; color: #F3EFE6; padding: 8px 11px 10px; display: flex; flex-direction: column; gap: 6px">'
            f'\n      <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px"><span data-label style="font-family: Anton, sans-serif; font-size: 24px; line-height: 1; letter-spacing: 0.04em; text-transform: uppercase; color: {accent}">{name}</span>'
            f'<span data-label style="font-size: 9px; font-weight: 600; letter-spacing: 0.18em; white-space: nowrap">{tag}</span></div>'
            f'\n      {rule}'
            f'\n      <div style="font-size: {size}px; font-weight: 600; line-height: 1.5; letter-spacing: 0.03em; text-transform: uppercase">{text}</div>\n    </div>')

def hud(text, pos, color="#D7261E", size=26):
    return f'    <span data-label style="position: absolute; {pos}; padding: 4px 10px; border: 2px solid {color}; background: #F3EFE6; color: {color}; font-family: Anton, sans-serif; font-size: {size}px; letter-spacing: 0.06em">{text}</span>\n'


@P("GEN-C03-00-Title", "Chapter 3 · Babel to Abram's Covenant")
def title():
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#0B0B2A"></rect>' + mk.stars(260, 760, 900, 3) + mk.stars(40, 760, 700, 4, color="#FFE680")
           + Z.sun(560, 760, 120, color="#FF8A3D", glow="#FFD23F", op=0.25)
           + Y.hills(760, 1080, 900, 5, color="#1A0A1E", amp=10)
           + Z.TW.tower(560, 900, 300, 60, 8, 0.88, "tt", unfinished=3, light="#5A2A3A", dark="#2A0A1A", brick="#3A1424"))
    return chapter_title(3, "第三話", "Babel to Abram's Covenant", "Genesis 10 – 15", svg, NIGHT,
                         v("15:5", frm="Look now", to="number them:"), "Genesis · Volume One · The Full Edition")


@P("GEN-C03-P01-Nations", "41 · The Generations of the Sons of Noah")
def p01():
    t, h = rows(250, None)
    ch = (h[1] - 24) / 3
    r1 = new(NIGHT, W1, h[0], defs("c31a", *ALL) + Z.three_sons("c31a", W1, h[0], 311),
             cap(v("10:1"), "left: 12px; top: 12px", size=11.5, maxw=420) + vref("GEN 10:1", "right: 12px; bottom: 12px"))
    cells = [clan("Japheth", v("10:2"), "GEN 10:2", JAPHETH, size=16),
             clan("Gomer", v("10:3"), "GEN 10:3", JAPHETH, of="OF JAPHETH", size=17),
             clan("Javan", v("10:4"), "GEN 10:4", JAPHETH, of="OF JAPHETH", size=17),
             new(SKY, W2, ch, Z.isles(W2, ch, 312), cap(v("10:5"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 10:5", "right: 8px; bottom: 8px")),
             clan("Ham", v("10:6"), "GEN 10:6", HAM, size=17),
             clan("Cush", v("10:7"), "GEN 10:7", HAM, of="OF HAM", size=15)]
    return page("Genesis 10:1–7 — The Generations of the Sons of Noah", t, r1 + grid(cells, "repeat(3, minmax(0, 1fr))"), START + 0)


@P("GEN-C03-P02-Nimrod", "42 · A Mighty Hunter before Jehovah")
def p02():
    t, h = rows(320, 200, 220, None)
    r1 = cols(new("radial-gradient(circle at 70% 40%, #FFC14D 0 20px, #B5421E 180px, #2A0A0A 380px)", W2, h[0], face(Z.NIMROD, -40, -10, 0.9),
                  cap(v("10:8"), "right: 8px; bottom: 8px", size=11, maxw=200) + vref("GEN 10:8", "left: 8px; top: 8px")),
              new(DUSK, W2, h[0], defs("c32a", *ALL) + Z.hunter("c32a", W2, h[0], 321),
                  cap(v("10:9"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 10:9", "right: 8px; bottom: 8px")))
    r2 = new(SAND, W1, h[1], Z.kingdom(W1, h[1], 322, ["BABEL", "ERECH", "ACCAD", "CALNEH"]),
             cap(v("10:10"), "left: 12px; top: 12px", size=11, maxw=520) + vref("GEN 10:10", "right: 12px; top: 12px"))
    r3 = new("linear-gradient(180deg, #4A1D55 0%, #C2456A 60%, #FFC14D 100%)", W1, h[2], Z.nineveh(W1, h[2], 323),
             cap(v("10:11") + " " + v("10:12"), "left: 12px; top: 12px", size=11, maxw=420) + vref("GEN 10:11–12", "right: 12px; bottom: 12px"))
    r4 = cols(clan("Mizraim", sp("10:13-14"), "GEN 10:13–14", HAM, of="OF HAM", size=13),
              new(SKY, W2, h[3], defs("c32d", *ALL) + Y.ground(W2, h[3], h[3] * 0.86, "#C8A06A", dy=0) + S.philistines("c32d", 7, 10, W2 - 10, h[3] * 0.8, h[3] * 0.96, 324, 0.3, 0.42),
                  vref("GEN 10:14", "right: 8px; top: 8px")))
    return page("Genesis 10:8–14 — A Mighty Hunter before Jehovah", t, r1 + r2 + r3 + r4, START + 1)


@P("GEN-C03-P03-Canaan", "43 · The Border of the Canaanite")
def p03():
    t, h = rows(290, None)
    r1 = new("#0B1A2E", W1, h[0], Z.canaan_map(W1, h[0], 331),
             cap(v("10:19"), "right: 12px; top: 12px", size=11, maxw=300) + vref("GEN 10:19", "right: 12px; bottom: 12px"))
    cells = [clan("Canaan", sp("10:15-18"), "GEN 10:15–18", HAM, of="OF HAM", size=13),
             clan("The Sons of Ham", v("10:20"), "GEN 10:20", HAM, size=15.5),
             clan("Shem", v("10:21"), "GEN 10:21", SHEM, size=15),
             clan("The Sons of Shem", v("10:22"), "GEN 10:22", SHEM, size=16),
             clan("Aram", v("10:23"), "GEN 10:23", SHEM, of="OF SHEM", size=17),
             clan("Arpachshad", v("10:24"), "GEN 10:24", SHEM, of="OF SHEM", size=17)]
    return page("Genesis 10:15–24 — The Border of the Canaanite", t, r1 + grid(cells, "repeat(3, minmax(0, 1fr))"), START + 2)


@P("GEN-C03-P04-Peleg", "44 · In His Days Was the Earth Divided")
def p04():
    t, h = rows(270, None, 300)
    r1 = new(NIGHT, W1, h[0], defs("c34a", *ALL) + Z.divided("c34a", W1, h[0], 341),
             cap(v("10:25"), "left: 12px; top: 12px", size=11.5, maxw=380) + vref("GEN 10:25", "right: 12px; top: 12px"))
    r2 = cols(clan("Joktan", sp("10:26-29"), "GEN 10:26–29", SHEM, of="OF SHEM", size=13.5),
              new(DAWN, W2, h[1], Z.mount_east(W2, h[1], 342), cap(v("10:30"), "left: 8px; top: 8px", size=11, maxw=320) + vref("GEN 10:30", "right: 8px; bottom: 8px")))
    r3 = new("#0B1226", W1, h[2], Z.nations_spread(W1, h[2], 343),
             cap(v("10:31"), "right: 12px; top: 12px", size=11, maxw=300)
             + cap(v("10:32"), "right: 12px; bottom: 14px", size=12, maxw=360) + vref("GEN 10:31–32", "left: 12px; bottom: 12px"))
    return page("Genesis 10:25–32 — In His Days Was the Earth Divided", t, r1 + r2 + r3, START + 3)


@P("GEN-C03-P05-Brick", "45 · Let Us Make Brick")
def p05():
    t, h = rows(240, 300, None)
    r1 = use(Brk[0], over=cap(v("11:1") + " " + v("11:2"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("GEN 11:1–2", "right: 12px; bottom: 12px"))
    r2 = cols(use(Brk[3], over=cap(v("11:3", to="one to another,"), "left: 8px; top: 8px", size=10.5)
                  + balloon(v("11:3", frm="Come,", to="thoroughly."), "left: 8px; bottom: 10px", 230, size=13, pad="18px 22px")
                  + sfx("ゴウッ", "GOU", "right: 12px; top: 52px", size=40, fill="#FFD23F", stroke="#0D0D0F", rot=6)),
              use(Brk[2], over=cap(v("11:3", frm="And they had"), "left: 8px; top: 8px", size=11, maxw=300) + vref("GEN 11:3", "right: 8px; bottom: 8px")))
    r3 = use(Brk[1], over=cap(v("11:4", to="said,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("11:4", frm="Come, let us build"), "left: 12px; top: 48px", 320, size=13, pad="24px 30px")
             + sfx("カンカン", "KAN KAN", "left: 24px; bottom: 26px", size=48, fill="#0D0D0F", stroke="#F3EFE6", rot=-6) + vref("GEN 11:4", "right: 12px; bottom: 12px"))
    return page("Genesis 11:1–4 — Let Us Make Brick", t, r1 + r2 + r3, START + 4)


@P("GEN-C03-P06-Babel", "46 · Confound Their Language")
def p06():
    t, h = rows(380, 200, 210, None)
    r1 = use(Bab[0], over=cap(v("11:5"), "left: 12px; top: 12px", size=10.5, maxw=290)
             + cap(v("11:6", to="said,"), "right: 12px; top: 12px", size=10.5)
             + god(v("11:6", frm="Behold"), "right: 12px; top: 48px", size=15, maxw=330) + vref("GEN 11:5–6", "left: 12px; bottom: 12px"))
    r2 = cols(new(NIGHT, W3, h[1], cosmic(W3, h[1]), god(v("11:7"), "left: 8px; top: 8px", size=14, maxw=200) + vref("GEN 11:7", "right: 8px; bottom: 8px")),
              new("#FFC890", W3, h[1], Z.babble(W3, h[1], 361, "#FFC890"), ""),
              new("#8FD0E2", W3, h[1], Z.babble(W3, h[1], 362, "#8FD0E2"), sfx("ガヤガヤ", "GAYA GAYA", "left: 12px; top: 8px", size=30, fill="#D7261E", stroke="#F3EFE6", rot=-4)))
    r3 = new("linear-gradient(180deg, #4A1D55 0%, #FF8A3D 100%)", W1, h[2], defs("c36c", *ALL) + Z.scattering("c36c", W1, h[2], 363),
             cap(v("11:8"), "left: 12px; top: 12px", size=11, maxw=400) + vref("GEN 11:8", "right: 12px; top: 12px"))
    r4 = use(Bab[1], over=cap(v("11:9"), "left: 12px; bottom: 12px", size=11, maxw=470) + vref("GEN 11:9", "right: 12px; top: 12px"))
    return page("Genesis 11:5–9 — Confound Their Language", t, r1 + r2 + r3 + r4, START + 5)


@P("GEN-C03-P07-Shem", "47 · The Generations of Shem")
def p07():
    ch = (1022 - 48) / 5 - 6
    head = new(NIGHT, W2, ch, Y.generations(W2, ch, 371, n=9, hi=8),
               cap(v("11:10", to="Shem."), "left: 8px; top: 8px", size=12, maxw=300) + vref("GEN 11:10", "right: 8px; bottom: 8px"))
    cells = [head,
             entry("Shem", 600, 100, v("11:10", frm="Shem was") + " " + v("11:11"), "GEN 11:10–11", size=13),
             entry("Arpachshad", 438, 35, sp("11:12-13"), "GEN 11:12–13", size=13),
             entry("Shelah", 433, 30, sp("11:14-15"), "GEN 11:14–15", size=13),
             entry("Eber", 464, 34, sp("11:16-17"), "GEN 11:16–17", size=13),
             entry("Peleg", 239, 30, sp("11:18-19"), "GEN 11:18–19", size=13),
             entry("Reu", 239, 32, sp("11:20-21"), "GEN 11:20–21", size=13),
             entry("Serug", 230, 30, sp("11:22-23"), "GEN 11:22–23", size=13),
             entry("Nahor", 148, 29, sp("11:24-25"), "GEN 11:24–25", size=13),
             entry("Terah", 205, 70, v("11:26"), "GEN 11:26", accent="#FF8A3D", size=15)]
    return page("Genesis 11:10–26 — The Generations of Shem", "minmax(0, 1fr)", grid(cells, "repeat(5, minmax(0, 1fr))"), START + 6)


@P("GEN-C03-P08-Terah", "48 · Ur of the Chaldees")
def p08():
    t, h = rows(250, 260, None)
    r1 = new(NIGHT, W1, h[0], Z.ur(W1, h[0], 381),
             cap(v("11:27"), "left: 12px; top: 12px", size=11.5, maxw=380) + vref("GEN 11:27", "right: 12px; bottom: 12px"))
    r2 = cols(new("radial-gradient(circle at 70% 40%, #C8D0DE 0 20px, #5A6A8A 180px, #12113A 380px)", W2, h[1], face(Z.TERAH, -50, -10, 0.82),
                  cap(v("11:28"), "right: 8px; bottom: 8px", size=10.5, maxw=190) + vref("GEN 11:28", "left: 8px; top: 8px")),
              new(DUSK, W2, h[1], defs("c38b", *ALL) + Z.two_couples("c38b", W2, h[1], 382),
                  cap(v("11:29"), "left: 8px; top: 8px", size=10, maxw=320) + vref("GEN 11:29", "right: 8px; top: 8px")))
    r3 = cols(new("radial-gradient(circle at 30% 40%, #E8D8C8 0 20px, #8A6A7A 180px, #2A1A2E 380px)", W2, h[2], face(Z.SARAI_SAD, -40, h[2] - 400, 1.05),
                  cap(v("11:30"), "right: 8px; top: 8px", size=12, maxw=150) + vref("GEN 11:30", "right: 8px; bottom: 8px")),
              new("#0B1A2E", W2, h[2], Z.journey_map(W2, h[2], 383, ["UR", "HARAN"], cur="HARAN", band=(0.34, 0.84)),
                  cap(v("11:31"), "left: 8px; top: 8px", size=10, maxw=320)
                  + cap(v("11:32"), "left: 8px; bottom: 8px", size=11, maxw=320) + vref("GEN 11:31–32", "right: 8px; bottom: 8px")))
    return page("Genesis 11:27–32 — Ur of the Chaldees", t, r1 + r2 + r3, START + 7)


@P("GEN-C03-P09-Call", "49 · Get Thee Out of Thy Country")
def p09():
    t, h = rows(340, 270, None)
    r1 = use(Call[0], over=cap(v("12:1", to="unto Abram,"), "right: 12px; top: 12px", size=10.5)
             + god(v("12:1", frm="Get thee"), "right: 12px; top: 48px", size=18, maxw=390) + vref("GEN 12:1", "right: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], defs("c39b", *ALL) + Z.look_up("c39b", W1, h[1], 392),
             god(v("12:2") + " " + v("12:3"), "right: 12px; top: 12px", size=15, maxw=440) + vref("GEN 12:2–3", "left: 12px; top: 12px"))
    r3 = use(Call[1], over=cap(v("12:4"), "left: 12px; top: 12px", size=12, maxw=440) + vref("GEN 12:4", "right: 12px; bottom: 12px"))
    return page("Genesis 12:1–4 — Get Thee Out of Thy Country", t, r1 + r2 + r3, START + 8)


@P("GEN-C03-P10-Shechem", "50 · Unto Thy Seed Will I Give This Land")
def p10():
    t, h = rows(210, 240, 270, None)
    r1 = new(SAND, W1, h[0], defs("c40a", *ALL) + Y.ground(W1, h[0], h[0] * 0.66, "#E8C88A", dy=0) + Z.caravan("c40a", 20, W1 - 20, h[0] * 0.86, 0.9, 401),
             cap(v("12:5"), "left: 12px; top: 12px", size=11, maxw=560) + vref("GEN 12:5", "right: 12px; bottom: 12px"))
    r2 = new(GREEN, W1, h[1], defs("c40b", *ALL) + Z.shechem("c40b", W1, h[1], 402),
             cap(v("12:6"), "right: 12px; top: 12px", size=11, maxw=300) + vref("GEN 12:6", "left: 12px; bottom: 12px"))
    r3 = use(Call[2], over=cap(v("12:7", to="and said,"), "left: 12px; top: 12px", size=10.5)
             + god(v("12:7", frm="Unto thy seed", to="this land:"), "left: 12px; top: 48px", size=22, maxw=340)
             + cap(v("12:7", frm="and there builded"), "left: 12px; bottom: 14px", size=11, maxw=380) + vref("GEN 12:7", "right: 12px; bottom: 12px"))
    r4 = cols(new(SKY, W2, h[3], Z.bethel(None, W2, h[3], 404),
                  cap(v("12:8"), "left: 8px; top: 8px", size=10, maxw=320) + vref("GEN 12:8", "right: 8px; bottom: 8px")),
              new(HOT, W2, h[3], defs("c40d", *ALL) + Z.southward("c40d", W2, h[3], 405),
                  cap(v("12:9"), "left: 8px; top: 8px", size=12, maxw=230) + vref("GEN 12:9", "right: 8px; bottom: 8px")))
    return page("Genesis 12:5–9 — Unto Thy Seed Will I Give This Land", t, r1 + r2 + r3 + r4, START + 9)


@P("GEN-C03-P11-Famine", "51 · Thou Art a Fair Woman")
def p11():
    t, h = rows(230, 240, None)
    r1 = new(HOT, W1, h[0], Z.famine(W1, h[0], 411),
             cap(v("12:10"), "right: 12px; top: 12px", size=12, maxw=360) + vref("GEN 12:10", "left: 12px; bottom: 12px"))
    r2 = new(EGYPT, W1, h[1], defs("c41b", *ALL) + Z.to_egypt("c41b", W1, h[1], 412),
             cap(v("12:11", to="Sarai his wife,"), "left: 12px; top: 12px", size=11.5, maxw=380) + vref("GEN 12:11", "right: 12px; bottom: 12px"))
    hh = h[2]
    r3 = new("linear-gradient(90deg, #5A2A16 0%, #C8885A 50%, #5A2A16 100%)", W1, hh,
             face(Z.ABRAM_GRAVE, -40, hh - 380, 1.0) + face(Z.SARAI, W1 + 40, hh - 380, 1.0, flip=True),
             balloon(v("12:11", frm="Behold now"), "left: 20px; top: 14px", 280, size=13, pad="20px 26px")
             + balloon(v("12:12"), "left: 230px; top: 112px", 300, size=12.5, pad="24px 30px")
             + balloon(v("12:13"), "right: 20px; top: 14px", 240, size=12.5, pad="22px 26px") + vref("GEN 12:11–13", "left: 12px; bottom: 12px"))
    return page("Genesis 12:10–13 — Thou Art a Fair Woman", t, r1 + r2 + r3, START + 10)


@P("GEN-C03-P12-Pharaoh", "52 · Pharaoh's House")
def p12():
    t, h = rows(200, 220, 240, None)
    r1 = new(SAND, W1, h[0], defs("c42a", *ALL) + Z.beheld("c42a", W1, h[0], 421),
             cap(v("12:14"), "left: 12px; top: 12px", size=11, maxw=330) + vref("GEN 12:14", "right: 12px; top: 12px"))
    r2 = new("#1F3F7A", W1, h[1], defs("c42b", *ALL) + Z.throne_room("c42b", W1, h[1], 422),
             cap(v("12:15"), "right: 12px; top: 12px", size=11, maxw=230) + vref("GEN 12:15", "right: 12px; bottom: 12px"))
    r3 = cols(new(EGYPT, W2, h[2], defs("c42c", *ALL) + Z.gifts("c42c", W2, h[2], 423),
                  cap(v("12:16"), "left: 8px; top: 8px", size=10, maxw=320) + vref("GEN 12:16", "right: 8px; top: 8px")),
              new("#3A0A0A", W2, h[2], Z.plagued(W2, h[2], 424),
                  cap(v("12:17"), "left: 8px; bottom: 8px", size=11, maxw=320)
                  + sfx("ドクン", "DOKUN", "right: 12px; top: 10px", size=40, fill="#D7261E", stroke="#F3EFE6", rot=6) + vref("GEN 12:17", "left: 8px; top: 8px")))
    r4 = new("radial-gradient(circle at 20% 40%, #FF8A3D 0 20px, #B5421E 200px, #2A0A0A 460px)", W1, h[3], face(Z.PHARAOH, -40, -10, 1.0),
             cap(v("12:18", to="and said,"), "left: 330px; top: 12px", size=10.5)
             + balloon(v("12:18", frm="What is this"), "left: 320px; top: 46px", 340, size=13, pad="20px 28px")
             + balloon(v("12:19"), "left: 300px; top: 150px", 370, size=12.5, pad="22px 30px")
             + cap(v("12:20"), "left: 330px; bottom: 14px", size=10.5, maxw=340) + vref("GEN 12:18–20", "left: 12px; bottom: 12px"))
    return page("Genesis 12:14–20 — Pharaoh's House", t, r1 + r2 + r3 + r4, START + 11)


@P("GEN-C03-P13-Strife", "53 · Very Rich in Cattle")
def p13():
    t, h = rows(220, 250, 230, None)
    r1 = new(HOT, W1, h[0], defs("c43a", *ALL) + Z.riches("c43a", W1, h[0], 431),
             cap(v("13:1"), "left: 12px; top: 12px", size=11, maxw=380)
             + cap(v("13:2"), "right: 12px; top: 12px", size=11.5, maxw=230) + vref("GEN 13:1–2", "right: 12px; bottom: 12px"))
    r2 = new("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", W1, h[1], Z.old_altar(None, W1, h[1], 432),
             cap(v("13:3") + " " + v("13:4"), "left: 12px; top: 12px", size=11, maxw=440) + vref("GEN 13:3–4", "right: 12px; bottom: 12px"))
    r3 = new(SKY, W1, h[2], Z.crowded(W1, h[2], 433),
             cap(v("13:5"), "left: 12px; top: 12px", size=11, maxw=300)
             + cap(v("13:6"), "right: 12px; top: 12px", size=11, maxw=330) + vref("GEN 13:5–6", "right: 12px; bottom: 12px"))
    r4 = new(HOT, W1, h[3], defs("c43d", *ALL) + Z.strife("c43d", W1, h[3], 434),
             cap(v("13:7"), "left: 12px; top: 12px", size=11, maxw=360)
             + sfx("ガッ", "GAH", "right: 30px; top: 16px", size=52, fill="#D7261E", stroke="#F3EFE6", rot=8) + vref("GEN 13:7", "right: 12px; bottom: 12px"))
    return page("Genesis 13:1–7 — Very Rich in Cattle", t, r1 + r2 + r3 + r4, START + 12)


@P("GEN-C03-P14-Choose", "54 · Lot Chose Him All the Plain")
def p14():
    t, h = rows(330, 240, 200, None)
    hh = h[0]
    r1 = new("linear-gradient(90deg, #2C4A7A 0%, #C8A06A 50%, #7A2A3A 100%)", W1, hh,
             face(Z.ABRAM, -40, hh - 370, 0.98) + face(Z.LOT, W1 + 40, hh - 370, 0.98, flip=True),
             cap(v("13:8", to="unto Lot,"), "left: 250px; top: 12px", size=10.5)
             + balloon(v("13:8", frm="Let there"), "left: 230px; top: 46px", 260, size=12, pad="22px 26px")
             + balloon(v("13:9"), "left: 200px; bottom: 12px", 330, size=11.5, pad="24px 34px") + vref("GEN 13:8–9", "left: 12px; top: 12px"))
    r2 = new(GREEN, W1, h[1], Z.plain_jordan(W1, h[1], 442),
             cap(v("13:10"), "left: 12px; top: 12px", size=11, maxw=520) + vref("GEN 13:10", "right: 12px; bottom: 12px"))
    r3 = new(SAND, W1, h[2], defs("c44c", *ALL) + Z.parting_ways("c44c", W1, h[2], 443),
             cap(v("13:11"), "left: 12px; top: 40px", size=11, maxw=440) + vref("GEN 13:11", "right: 12px; bottom: 12px"))
    r4 = new(BLOOD, W1, h[3], defs("c44d", *ALL) + Z.sodom_sky("c44d", W1, h[3], 444),
             cap(v("13:12"), "left: 12px; top: 12px", size=11, maxw=360)
             + cap(v("13:13"), "right: 12px; top: 12px", size=12, maxw=260) + vref("GEN 13:12–13", "left: 12px; bottom: 12px"))
    return page("Genesis 13:8–13 — Lot Chose Him All the Plain", t, r1 + r2 + r3 + r4, START + 13)


@P("GEN-C03-P15-Lift", "55 · Lift Up Now Thine Eyes")
def p15():
    t, h = rows(300, 250, 210, None)
    r1 = new(SKY, W1, h[0], defs("c45a", *ALL) + Z.compass("c45a", W1, h[0], 451),
             cap(v("13:14", to="from him,"), "left: 12px; top: 12px", size=10.5, maxw=340)
             + god(v("13:14", frm="Lift up"), "right: 12px; top: 12px", size=15, maxw=320) + vref("GEN 13:14", "left: 12px; bottom: 12px"))
    r2 = cols(new(SKY, W2, h[1], Z.panorama(W2, h[1], 452), god(v("13:15"), "left: 8px; top: 8px", size=16, maxw=320) + vref("GEN 13:15", "right: 8px; bottom: 8px")),
              new("#2A1A0A", W2, h[1], Z.dust(W2, h[1], 453), god(v("13:16"), "left: 8px; top: 8px", size=13.5, maxw=320) + vref("GEN 13:16", "right: 8px; bottom: 8px")))
    r3 = new(SKY, W1, h[2], defs("c45c", *ALL) + Z.walk_land("c45c", W1, h[2], 454),
             god(v("13:17"), "right: 12px; top: 12px", size=16, maxw=380) + vref("GEN 13:17", "right: 12px; bottom: 12px"))
    r4 = new(GREEN, W1, h[3], defs("c45d", *ALL) + Z.mamre("c45d", W1, h[3], 455),
             cap(v("13:18"), "right: 12px; top: 12px", size=11.5, maxw=300) + vref("GEN 13:18", "left: 12px; bottom: 12px"))
    return page("Genesis 13:14–18 — Lift Up Now Thine Eyes", t, r1 + r2 + r3 + r4, START + 14)


@P("GEN-C03-P16-Kings", "56 · Four Kings against the Five")
def p16():
    t, h = rows(230, 230, 140, None)
    r1 = new(DUSK, W1, h[0], defs("c46a", *ALL) + Z.kings_row("c46a", W1, h[0], 461,
             ["AMRAPHEL|SHINAR", "ARIOCH|ELLASAR", "CHEDORLAOMER|ELAM", "TIDAL|GOIIM"], ["#1F5FAD", "#1F7A8C", "#5A1A4A", "#3A2214"]),
             cap(v("14:1"), "left: 12px; top: 12px", size=11, maxw=560) + vref("GEN 14:1", "right: 12px; top: 12px"))
    r2 = new(BLOOD, W1, h[1], defs("c46b", *ALL) + Z.kings_row("c46b", W1, h[1], 462,
             ["BERA|SODOM", "BIRSHA|GOMORRAH", "SHINAB|ADMAH", "SHEMEBER|ZEBOIIM", "BELA|ZOAR"], ["#8A3A1E", "#B5421E", "#C9A86A", "#5A2A16", "#7A3BA8"], flip=True),
             cap(v("14:2"), "left: 12px; top: 12px", size=10.5, maxw=440)
             + cap(v("14:3"), "right: 12px; top: 12px", size=10.5, maxw=220) + vref("GEN 14:2–3", "right: 12px; bottom: 6px"))
    r3 = new("#12113A", W1, h[2], Z.tally(W1, h[2], 463),
             cap(v("14:4"), "left: 12px; top: 10px", size=11.5) + vref("GEN 14:4", "right: 12px; top: 10px"))
    r4 = new("#1A0A0E", W1, h[3], Z.campaign(W1, h[3], 464),
             cap(sp("14:5-7"), "left: 12px; top: 12px", size=10.5, maxw=290) + vref("GEN 14:5–7", "left: 12px; bottom: 12px"))
    return page("Genesis 14:1–7 — Four Kings against the Five", t, r1 + r2 + r3 + r4, START + 15)


@P("GEN-C03-P17-Siddim", "57 · The Vale of Siddim")
def p17():
    t, h = rows(300, 280, None)
    r1 = new(DUSK, W1, h[0], defs("c47a", *ALL) + Z.battle_array("c47a", W1, h[0], 471),
             cap(v("14:8"), "left: 12px; top: 12px", size=10.5, maxw=400)
             + cap(v("14:9"), "right: 12px; top: 12px", size=10.5, maxw=260)
             + sfx("ワアアッ", "WAAAH", "right: 24px; bottom: 30px", size=40, fill="#D7261E", stroke="#F3EFE6", rot=-4) + vref("GEN 14:8–9", "left: 12px; bottom: 12px"))
    r2 = new("linear-gradient(180deg, #5A3A4E 0%, #C8885A 100%)", W1, h[1], defs("c47b", *ALL) + Z.slime_pits("c47b", W1, h[1], 472),
             cap(v("14:10"), "left: 12px; top: 12px", size=11, maxw=400) + vref("GEN 14:10", "right: 12px; bottom: 12px"))
    r3 = cols(new(DUSK, W2, h[2], defs("c47c", *ALL) + Z.plunder("c47c", W2, h[2], 473),
                  cap(v("14:11"), "left: 8px; top: 8px", size=11, maxw=320) + vref("GEN 14:11", "right: 8px; bottom: 8px")),
              new("radial-gradient(circle at 30% 40%, #C8D0DE 0 20px, #6A4A5A 180px, #2A1A2E 380px)", W2, h[2], face(Z.LOT_TAKEN, -50, h[2] - 400, 1.05),
                  cap(v("14:12"), "right: 8px; top: 8px", size=11.5, maxw=180) + vref("GEN 14:12", "right: 8px; bottom: 8px")))
    return page("Genesis 14:8–12 — The Vale of Siddim", t, r1 + r2 + r3, START + 16)


@P("GEN-C03-P18-Pursuit", "58 · Abram the Hebrew")
def p18():
    t, h = rows(250, 250, 260, None)
    r1 = new(GREEN, W1, h[0], defs("c48a", *ALL) + Z.messenger("c48a", W1, h[0], 481),
             cap(v("14:13"), "right: 12px; top: 12px", size=10.5, maxw=380) + vref("GEN 14:13", "left: 12px; bottom: 12px"))
    r2 = cols(new("radial-gradient(circle at 70% 40%, #FFD23F 0 20px, #FF6A2A 160px, #5A1A16 380px)", W2, h[1], face(Z.ABRAM_BOLD, -40, -10, 0.78),
                  cap(v("14:14", to="taken captive,"), "right: 8px; bottom: 8px", size=11, maxw=180) + vref("GEN 14:14", "left: 8px; top: 8px")),
              new(DUSK, W2, h[1], defs("c48b", *ALL) + Z.count318("c48b", W2, h[1], 482),
                  hud("318", "right: 10px; top: 10px", size=40) + cap(v("14:14", frm="he led forth"), "left: 8px; top: 8px", size=10, maxw=210)))
    r3 = new(NIGHT, W1, h[2], defs("c48c", *ALL) + Z.night_raid("c48c", W1, h[2], 483),
             cap(v("14:15"), "left: 12px; top: 12px", size=11, maxw=440)
             + sfx("ザッザッ", "ZAH ZAH", "right: 180px; bottom: 30px", size=34, fill="#FFD23F", stroke="#0D0D0F", rot=-6) + vref("GEN 14:15", "right: 12px; bottom: 12px"))
    r4 = new(DAWN, W1, h[3], defs("c48d", *ALL) + Z.brought_back("c48d", W1, h[3], 484),
             cap(v("14:16"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("GEN 14:16", "right: 12px; top: 12px"))
    return page("Genesis 14:13–16 — Abram the Hebrew", t, r1 + r2 + r3 + r4, START + 17)


@P("GEN-C03-P19-Melchizedek", "59 · Priest of God Most High")
def p19():
    t, h = rows(230, 290, None)
    r1 = new(SAND, W1, h[0], defs("c49a", *ALL) + Z.kings_vale("c49a", W1, h[0], 491),
             cap(v("14:17"), "left: 12px; top: 12px", size=11, maxw=500) + vref("GEN 14:17", "right: 12px; bottom: 12px"))
    r2 = new(HOT, W1, h[1], defs("c49b", *ALL) + Z.bread_wine("c49b", W1, h[1], 492),
             cap(v("14:18"), "left: 12px; top: 12px", size=12.5, maxw=340) + vref("GEN 14:18", "left: 12px; bottom: 12px"))
    r3 = cols(new("radial-gradient(circle at 70% 30%, #FFF4C2 0 30px, #FFC14D 160px, #B5652E 420px)", W2, h[2], face(Z.MELCHIZEDEK, -60, h[2] - 400, 1.05),
                  cap(v("14:19", to="said,"), "right: 8px; top: 8px", size=10.5)
                  + balloon(v("14:19", frm="Blessed") + " " + v("14:20", to="into thy hand."), "right: 8px; top: 44px", 230, size=12, pad="24px 22px")
                  + vref("GEN 14:19–20", "left: 8px; top: 8px")),
              new("#12113A", W2, h[2], Z.tithe(W2, h[2], 493), cap(v("14:20", frm="And he gave"), "left: 8px; bottom: 10px", size=13, maxw=320) + vref("GEN 14:20", "right: 8px; top: 8px")))
    return page("Genesis 14:17–20 — Priest of God Most High", t, r1 + r2 + r3, START + 18)


@P("GEN-C03-P20-Thread", "60 · From a Thread to a Shoe-Latchet")
def p20():
    t, h = rows(280, 320, None)
    hh = h[0]
    r1 = new("linear-gradient(90deg, #5A1A4A 0%, #C8885A 60%, #2C4A7A 100%)", W1, hh,
             face(Z.KING_SODOM, -40, hh - 370, 0.98) + face(Z.ABRAM_GRAVE, W1 + 40, hh - 370, 0.98, flip=True),
             cap(v("14:21", to="unto Abram,"), "left: 260px; top: 12px", size=10.5)
             + balloon(v("14:21", frm="Give me"), "left: 240px; top: 52px", 240, size=13.5, pad="22px 26px") + vref("GEN 14:21", "left: 12px; top: 12px"))
    raise_ = Z.abram("c50b", W2 * 0.3, h[1] * 0.92, Y.fit(h[1] * 0.92, h[1] * 0.36), up=[(-22, -158), (-10, -200), (4, -246)])
    r2 = cols(new(NIGHT, W2, h[1], defs("c50b", *ALL) + mk.stars(60, W2, h[1], 501) + Y.ground(W2, h[1], h[1] * 0.92, "#1A1430", dy=0) + raise_,
                  cap(v("14:22", to="Sodom,"), "left: 8px; top: 8px", size=10.5, maxw=320)
                  + balloon(v("14:22", frm="I have"), "right: 8px; top: 44px", 230, size=12, pad="20px 22px") + vref("GEN 14:22", "left: 8px; bottom: 8px")),
              new("#C8A06A", W2, h[1], Z.thread_shoe(W2, h[1], 502),
                  balloon(v("14:23"), "left: 8px; top: 8px", 300, size=12.5, pad="24px 30px") + vref("GEN 14:23", "right: 8px; bottom: 8px")))
    r3 = new(NIGHT, W1, h[2], defs("c50c", *ALL) + Z.allies("c50c", W1, h[2], 503),
             balloon(v("14:24"), "right: 12px; top: 12px", 340, size=13, pad="26px 34px") + vref("GEN 14:24", "left: 12px; top: 12px"))
    return page("Genesis 14:21–24 — From a Thread to a Shoe-Latchet", t, r1 + r2 + r3, START + 19)


@P("GEN-C03-P21-Stars", "61 · Number the Stars")
def p21():
    t, h = rows(250, 220, 160, None)
    r1 = cols(new("radial-gradient(circle at 70% 30%, #CFE0FF 0 20px, #4A3A8E 180px, #0B0B2A 400px)", W2, h[0], face(Z.ABRAM_STARS, -40, -10, 0.74),
                  cap(v("15:1", to="saying,"), "right: 8px; bottom: 8px", size=10.5, maxw=190) + vref("GEN 15:1", "left: 8px; top: 8px")),
              new(NIGHT, W2, h[0], cosmic(W2, h[0]), god(v("15:1", frm="Fear not"), "left: 8px; top: 8px", size=21, maxw=320)))
    r2 = new("linear-gradient(90deg, #2A1A3E 0%, #6A4A7A 100%)", W1, h[1], face(Z.ABRAM_GRAVE, -40, -16, 0.66),
             cap(v("15:2", to="said,"), "left: 230px; top: 10px", size=10.5)
             + balloon(v("15:2", frm="O Lord"), "left: 216px; top: 44px", 250, size=11.5, pad="20px 24px")
             + cap(v("15:3", to="said,"), "right: 12px; top: 10px", size=10.5)
             + balloon(v("15:3", frm="Behold"), "right: 10px; top: 44px", 210, size=11.5, pad="20px 22px") + vref("GEN 15:2–3", "left: 12px; bottom: 10px"))
    r3 = new(NIGHT, W1, h[2], cosmic(W1, h[2]),
             cap(v("15:4", to="saying,"), "left: 12px; top: 10px", size=10.5)
             + god(v("15:4", frm="This man"), "left: 12px; top: 44px", size=16, maxw=660) + vref("GEN 15:4"))
    r4 = new("#0B0B2A", W1, h[3], defs("c51d", *ALL) + Z.star_count("c51d", W1, h[3], 514),
             cap(v("15:5", to="and said,"), "left: 12px; top: 12px", size=10.5)
             + god(v("15:5", frm="Look now", to="number them:"), "left: 12px; top: 46px", size=17, maxw=360)
             + cap(v("15:5", frm="and he said unto him,", to="unto him,"), "right: 12px; top: 120px", size=10.5)
             + god(v("15:5", frm="So shall"), "right: 12px; top: 156px", size=22, maxw=320)
             + cap(v("15:6"), "right: 12px; bottom: 14px", size=11.5, maxw=300) + vref("GEN 15:5–6", "right: 12px; top: 12px"))
    return page("Genesis 15:1–6 — Number the Stars", t, r1 + r2 + r3 + r4, START + 20)


@P("GEN-C03-P22-Pieces", "62 · Between These Pieces")
def p22():
    t, h = rows(220, 230, 250, None)
    r1 = cols(new(NIGHT, W2, h[0], cosmic(W2, h[0]),
                  cap(v("15:7", to="unto him,"), "left: 8px; top: 8px", size=10.5)
                  + god(v("15:7", frm="I am"), "left: 8px; top: 44px", size=15, maxw=320) + vref("GEN 15:7", "right: 8px; bottom: 8px")),
              new("radial-gradient(circle at 30% 40%, #FFE680 0 20px, #C8885A 180px, #3A2214 400px)", W2, h[0], face(Z.ABRAM, -40, -10, 0.66),
                  cap(v("15:8", to="said,"), "right: 8px; top: 8px", size=10.5)
                  + balloon(v("15:8", frm="O Lord"), "right: 8px; top: 44px", 170, size=12, pad="18px 16px") + vref("GEN 15:8", "right: 8px; bottom: 8px")))
    r2 = new(SAND, W1, h[1], Z.offerings(W1, h[1], 522),
             cap(v("15:9", to="unto him,"), "left: 12px; top: 12px", size=10.5)
             + god(v("15:9", frm="Take me"), "left: 12px; top: 46px", size=14, maxw=430) + vref("GEN 15:9", "right: 12px; top: 12px"))
    r3 = cols(new(SAND, W2, h[2], Z.pieces(W2, h[2], 523),
                  cap(v("15:10"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 15:10", "right: 8px; bottom: 8px")),
              new(HOT, W2, h[2], defs("c52c", *ALL) + Z.prey("c52c", W2, h[2], 524),
                  cap(v("15:11"), "right: 8px; bottom: 8px", size=11, maxw=200)
                  + sfx("バサバサ", "BASA BASA", "right: 10px; top: 10px", size=28, fill="#0D0D0F", stroke="#F3EFE6", rot=6) + vref("GEN 15:11", "left: 8px; bottom: 8px")))
    r4 = new("#0B0510", W1, h[3], defs("c52d", *ALL) + Z.deep_sleep("c52d", W1, h[3], 525),
             cap(v("15:12"), "left: 12px; top: 12px", size=12, maxw=420)
             + sfx("ズズズ", "ZUZUZU", "right: 30px; top: 20px", size=44, fill="#7A3BA8", stroke="#F3EFE6", rot=-4) + vref("GEN 15:12", "right: 12px; bottom: 12px"))
    return page("Genesis 15:7–12 — Between These Pieces", t, r1 + r2 + r3 + r4, START + 21)


@P("GEN-C03-P23-Sojourners", "63 · Four Hundred Years")
def p23():
    t, h = rows(300, 270, None)
    r1 = new(BLOOD, W1, h[0], defs("c53a", *ALL) + Z.bondage("c53a", W1, h[0], 531),
             cap(v("15:13", to="unto Abram,"), "left: 12px; top: 12px", size=10.5)
             + god(v("15:13", frm="Know"), "left: 12px; top: 46px", size=16, maxw=430)
             + hud("400 YEARS", "right: 14px; top: 12px") + vref("GEN 15:13", "right: 12px; bottom: 12px"))
    r2 = new(DAWN, W1, h[1], defs("c53b", *ALL) + Z.going_out("c53b", W1, h[1], 532),
             god(v("15:14"), "left: 12px; top: 12px", size=16, maxw=430) + vref("GEN 15:14", "right: 12px; bottom: 12px"))
    r3 = cols(new("radial-gradient(circle at 70% 30%, #FFF4C2 0 20px, #FFC14D 160px, #8A4A3A 420px)", W2, h[2], face(Z.ABRAM, -40, h[2] - 390, 1.0),
                  god(v("15:15"), "right: 8px; top: 8px", size=15, maxw=220) + vref("GEN 15:15", "right: 8px; bottom: 8px")),
              new(NIGHT, W2, h[2], Z.four_generations(W2, h[2], 534),
                  god(v("15:16"), "left: 8px; top: 8px", size=15, maxw=320) + vref("GEN 15:16", "right: 8px; bottom: 8px")))
    return page("Genesis 15:13–16 — Four Hundred Years", t, r1 + r2 + r3, START + 22)


@P("GEN-C03-P24-Furnace", "64 · A Smoking Furnace and a Flaming Torch")
def p24():
    t, h = rows(400, 270, None)
    r1 = new("#05050A", W1, h[0], Z.furnace(W1, h[0], 541),
             cap(v("15:17"), "left: 12px; top: 12px", size=12.5, maxw=420)
             + sfx("ゴオオ", "GOOO", "right: 30px; top: 24px", size=56, fill="#FF8A3D", stroke="#0D0D0F", rot=-6) + vref("GEN 15:17", "left: 12px; bottom: 12px"))
    r2 = new("#0B1A2E", W1, h[1], Z.land_grant(W1, h[1], 542),
             cap(v("15:18", to="saying,"), "right: 12px; top: 12px", size=10.5, maxw=330)
             + god(v("15:18", frm="Unto thy seed"), "right: 12px; top: 72px", size=15, maxw=330) + vref("GEN 15:18", "right: 12px; bottom: 12px"))
    r3 = new(NIGHT, W1, h[2], defs("c54c", *ALL) + Z.peoples("c54c", W1, h[2], 543),
             god(sp("15:19-21"), "left: 12px; top: 12px", size=15, maxw=560)
             + end_mark("NEXT · SARAI AND HAGAR", "right: 14px; bottom: 12px") + vref("GEN 15:19–21", "left: 12px; bottom: 12px"))
    return page("Genesis 15:17–21 — A Smoking Furnace and a Flaming Torch", t, r1 + r2 + r3, START + 23)
