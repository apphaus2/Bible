"""2 Samuel Book Two — O My Son Absalom (2 Samuel 14–24). Writes the .dc.html pages into the given folder.
Usage: python3 samuel4_book2.py <out_dir>"""
import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1] / "kit"))  # shared drawing kit
import sys, pathlib, random
import mk, exodus as E, exodus4 as Z, exodus5 as V, numbers1 as N, joshua1 as J, judges2 as S, samuel1 as A, samuel2 as B, samuel3 as C, samuel4 as G
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, stars
from exodus_book3 import crowd
from numbers_book1 import badge, hills
from judges_book1 import shout
from judges_book2 import end_mark
from samuel_book1 import D, POINT, shouting
FX = G.tokens()
PAGES = {}
KING = C.KING
DO = G.DAVID_OLD


def forest(W, base, seed, dark=False, n=9, smin=0.5, smax=0.8):
    r = random.Random(seed)
    return "".join(J.oak(r.uniform(-20, W + 20), base + r.uniform(-10, 20), r.uniform(smin, smax), seed=seed + i) for i in range(n))


def mourners(p, n, x0, x1, y0, y1, seed, smin, smax):
    """People going up with covered heads (robes drawn over the head)."""
    r = random.Random(seed); o = []
    for y, x in sorted((r.uniform(y0, y1), r.uniform(x0, x1)) for _ in range(n)):
        s = smin + (smax - smin) * (y - y0) / max(1, y1 - y0)
        o.append(person(p, round(x), round(y), round(s, 3), body="#2A140C", cloth=r.choice(["#5A4A5E", "#4A3A4E", "#6A5A6E", "#3A3A4E"]), sw=3, flip=True))
    return "".join(o)


# ───────────────────────── Cover ─────────────────────────
def cover():
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {D("c1")}
    {J.sun(560, 760, 120)}
    {V.rays(560, 760, 40, 120, 900, color="#FFF4C2", op=0.14)}
    {hills(900, "#2A0A1A", 2001, 40, 760)}
    {G.great_oak(260, 1010, 2.0, seed=2002, dark=True)}
    {G.hanging(560, 640, 1.0, "cvh")}
    {G.bough_over(560, 640, 1.3, seed=2003, dark=True)}
    {N.ass(660, 1010, 0.7, color="#3A3030")}
    <path d="M-10 1000 L 770 1000 L 770 1090 L -10 1090 Z" fill="#12090A"></path>
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The Second Book of</span>
    <span>No. 02</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 124px; line-height: 1.2; letter-spacing: -1px; color: #F3EFE6">SAMUEL</h1>
  <div style="position: absolute; top: 236px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 252px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book Two — O My Son Absalom</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 14 – 24</span>
  </div>
  <div style="position: absolute; top: 40px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 40px; line-height: 1.04; color: #F3EFE6"><span>サ</span><span>ム</span><span>エ</span><span>ル</span><span>記</span><span>下</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.14em; color: #F3EFE6">SAMUERU-KI GE</span>
  </div>
  <div style="position: absolute; left: 38px; top: 322px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 280px; line-height: 1.45">O my son Absalom, my son, my son Absalom!</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 2</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #12090A 0%, #4A0A1A 30%, #B5121B 60%, #FF8A3D 85%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("2 Samuel Book Two — Cover", None, body, root_style=root)
PAGES["SB2-Cover"] = cover


# ───────────────────────── 01 · No Blemish in Him (14:25–26) ─────────────────────────
def p01():
    s1 = f'''      {V.rays(200, 280, 40, 60, 800, color="#FFF4C2", op=0.3)}
      {face(FX["__FACE_ABSALOM__"], -40, 60, 1.05)}'''
    o1 = (cap("Now in all Israel there was none to be so much praised as Absalom for his beauty: from the sole of his foot even to the crown of his head there was no blemish in him.", "right: 14px; top: 16px", size=13, maxw=300)
          + stamp(14, "right: 16px; bottom: 14px")
          + ref("ABSALOM", "left: 12px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6"))
    P1 = panel("radial-gradient(circle at 30% 50%, #FFF4C2 0 40px, #FFC14D 220px, #B5121B 480px, #4A0A1A 680px)", 702, 684, s1, o1, "1 · No blemish in him")

    s2 = f'''      <path d="M-10 270 L 712 270 L 712 314 L -10 314 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>
      {G.balance(470, 270, 1.3)}'''
    o2 = (cap("And when he cut the hair of his head (now it was at every year's end that he cut it; because it was heavy on him, therefore he cut it); he weighed the hair of his head at two hundred shekels, after the king's weight.", "left: 12px; top: 12px", size=11, maxw=260)
          + badge("二百シェケル", "right: 14px; top: 14px", size=16))
    P2 = panel("linear-gradient(180deg, #F3E0B8 0%, #C9A86A 100%)", 702, 314, s2, o2, "2 · Two hundred shekels")
    body = P1 + P2
    return mk.page("2 Samuel 14:25–26 — No Blemish in Him", "minmax(0, 1fr) 320px", body, 1)
PAGES["SB2-P01-Absalom"] = p01


# ───────────────────────── 02 · He Stole the Hearts (15:2–6) ─────────────────────────
def p02():
    s1 = f'''      {D("b1")}
      {G.gatehouse(560, 260, 300, 240)}
      <path d="M-10 260 L 712 260 L 712 294 L -10 294 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {G.absalom("b1", 330, 284, 0.82, up=[(-22, -158), (-46, -166), (-70, -172)])}
      {person("b1", 180, 286, 0.76, body="#3A1E14", cloth="#8A6A4A", kind="Tunic", sw=4)}'''
    o1 = (cap("And Absalom rose up early, and stood beside the way of the gate:", "left: 12px; top: 12px", size=10.5, maxw=260)
          + balloon("Of what city art thou?", "left: 360px; top: 30px", 160, size=14, pad="14px 16px")
          + balloon("Thy servant is of one of the tribes of Israel.", "left: 12px; top: 90px", 170, size=12.5, pad="14px 16px")
          + stamp(15, "right: 16px; top: 14px"))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 294, s1, o1, "1 · Of what city art thou")

    s2 = f'''      {face(FX["__FACE_ABSALOM_SLY__"], -40, -20, 0.74)}'''
    o2 = (cap("Absalom said moreover,", "left: 320px; top: 12px", size=10)
          + tail(290, 130, "l")
          + balloon("Oh that I were made judge in the land, that every man who hath any suit or cause might come unto me, and I would do him justice!", "left: 330px; top: 44px", 350, size=14.5, pad="24px 36px"))
    P2 = panel("radial-gradient(circle at 25% 50%, #FFE680 0 30px, #FF8A3D 200px, #8A1E2E 460px)", 702, 294, s2, o2, "2 · Oh that I were made judge")

    s3 = f'''      {D("b3")}
      {G.gatehouse(120, 230, 220, 200)}
      <path d="M-10 230 L 712 230 L 712 404 L -10 404 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {crowd("b3", 22, 200, 712, 260, 330, 2201, 0.3, 0.5)}
      {G.absalom("b3", 420, 390, 0.9, up=[(-22, -158), (-50, -150), (-74, -152)])}
      {person("b3", 330, 392, 0.86, body="#3A1E14", cloth="#5A6E8A", kind="Tunic", sw=4, flip=True)}'''
    o3 = (cap("And on this manner did Absalom to all Israel that came to the king for judgment:", "left: 12px; top: 12px", size=10.5, maxw=330)
          + shout("so Absalom stole the hearts of the men of Israel.", "right: 14px; top: 14px", size=22, maxw=300))
    P3 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 394, s3, o3, "3 · He stole the hearts")
    body = P1 + P2 + P3
    return mk.page("2 Samuel 15:2–6 — He Stole the Hearts", "300px 300px minmax(0, 1fr)", body, 2)
PAGES["SB2-P02-Hearts"] = p02


# ───────────────────────── 03 · Absalom Is King in Hebron (15:10–14) ─────────────────────────
def p03():
    s1 = f'''      {D("c1")}
      {J.sun(560, 120, 50)}
      {hills(240, "#6A3A2A", 2301, 50)}
      <path d="M-10 280 L 712 280 L 712 334 L -10 334 Z" fill="#8A4A22" stroke="#0D0D0F" stroke-width="2"></path>
      {J.trumpeter("c1", 200, 300, 0.9)}
      {J.blasts(230, 120, 1.6, 4)}
      {"".join(J.trumpeter("c1", x, 250, 0.3) for x in (520, 600, 660))}'''
    o1 = (cap("But Absalom sent spies throughout all the tribes of Israel, saying, As soon as ye hear the sound of the trumpet, then ye shall say,", "right: 12px; top: 12px", size=10.5, maxw=320)
          + shout("Absalom is king in Hebron.", "right: 14px; top: 110px", size=30, maxw=320)
          + sfx("ブォーッ", "BWOOO", "left: 30px; top: 20px", size=36, fill="#FFD23F", stroke="#0D0D0F", rot=-6, align="flex-start"))
    P1 = panel("linear-gradient(180deg, #4A0A1A 0%, #D7261E 60%, #FF8A3D 100%)", 702, 334, s1, o1, "1 · The sound of the trumpet")

    s2 = f'''      {mk.speed(200, 220, 50, 160, 700, 2302, color="#FFD23F", op=0.3)}
      {face(FX["__FACE_DAVID_OLD_ALARM__"], -40, 40, 0.9)}'''
    o2 = (cap("And David said unto all his servants that were with him at Jerusalem,", "right: 14px; top: 14px", size=11, maxw=320)
          + tail(340, 300, "l")
          + balloon("Arise, and let us flee; for else none of us shall escape from Absalom: make speed to depart, lest he overtake us quickly, and bring down evil upon us, and smite the city with the edge of the sword.", "left: 380px; top: 120px", 310, size=14.5, pad="34px 30px"))
    P2 = panel("radial-gradient(circle at 25% 50%, #FFC14D 0 30px, #8A1E2E 240px, #12090A 520px)", 702, 674, s2, o2, "2 · Arise, and let us flee")
    body = P1 + P2
    return mk.page("2 Samuel 15:10–14 — Absalom Is King in Hebron", "340px minmax(0, 1fr)", body, 3)
PAGES["SB2-P03-Flee"] = p03


# ───────────────────────── 04 · The Mount of Olives (15:23–30) ─────────────────────────
def p04():
    s1 = f'''      {D("d1")}
      {hills(140, "#6A6A4A", 2401, 30)}
      <path d="M-10 170 L 712 170 L 712 294 L -10 294 Z" fill="#A89A6A" stroke="#0D0D0F" stroke-width="2"></path>
      {B.brook(-10, 712, 220, 40, 2402)}
      {"".join(person("d1", x, 252 + (x % 3) * 4, 0.42, body="#2A140C", cloth=c, sw=3) for x, c in [(80, "#5A4A5E"), (140, "#6A5A4E"), (200, "#4A3A4E"), (260, "#5A6E8A"), (420, "#6A5A6E"), (480, "#8A6A4A"), (540, "#4A3A4E"), (600, "#5A4A5E")])}
      {person("d1", 340, 258, 0.5, **DO, extra=KING)}'''
    o1 = cap("And all the country wept with a loud voice, and all the people passed over: the king also himself passed over the brook Kidron, and all the people passed over, toward the way of the wilderness.", "left: 12px; top: 12px", size=10.5, maxw=440)
    P1 = panel("linear-gradient(180deg, #5A6E8A 0%, #C8D0DE 100%)", 702, 294, s1, o1, "1 · The brook Kidron")

    r = random.Random(4)
    s2 = f'''      {D("d2")}
      {J.moon(600, 80, 30)}
      <path d="M-10 704 L -10 560 C 200 520 420 360 712 200 L 712 704 Z" fill="#3A4A3A" stroke="#0D0D0F" stroke-width="2.4"></path>
      {"".join(S.olive(x, y, 0.8, seed=i) for i, (x, y) in enumerate([(80, 560), (300, 470), (520, 330), (640, 260), (420, 420)]))}
      {mourners("d2", 12, 380, 700, 300, 520, 2403, 0.32, 0.5)}
      {person("d2", 230, 640, 1.05, body="#5A2A16", cloth="#4A2A7A", sw=3, flip=True)}
      <path d="M200 642 l 8 4 M246 642 l -6 4" stroke="#5A2A16" stroke-width="4"></path>'''
    o2 = (cap("And David went up by the ascent of the mount of Olives, and wept as he went up; and he had his head covered, and went barefoot:", "left: 12px; top: 12px", size=12, maxw=360)
          + cap("and all the people that were with him covered every man his head, and they went up, weeping as they went up.", "left: 12px; top: 150px", size=10.5, maxw=300))
    P2 = panel("linear-gradient(180deg, #05050A 0%, #2A2A4E 50%, #4A3A5E 100%)", 702, 704, s2, o2, "2 · Weeping as they went up")
    body = P1 + P2
    return mk.page("2 Samuel 15:23–30 — The Mount of Olives", "300px minmax(0, 1fr)", body, 4)
PAGES["SB2-P04-Olives"] = p04


# ───────────────────────── 05 · Deal Gently (18:5–8) ─────────────────────────
def p05():
    s1 = f'''      {D("e1")}
      {G.gatehouse(120, 260, 220, 220)}
      <path d="M-10 260 L 712 260 L 712 314 L -10 314 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("e1", 280, 300, 0.8, **DO, up=[(-22, -158), (-50, -170), (-80, -176)], extra=KING, flip=True)}
      {"".join(person("e1", x, 304, 0.74, body="#2A140C", cloth=c, kind="Tunic", sw=4, extra=Z.SPEAR) for x, c in [(420, "#5A6E8A"), (500, "#8A6A4A"), (580, "#3F8A44")])}'''
    o1 = (cap("And the king commanded Joab and Abishai and Ittai, saying,", "right: 12px; top: 12px", size=10.5, maxw=260)
          + balloon("Deal gently for my sake with the young man, even with Absalom.", "left: 300px; top: 70px", 220, size=14, pad="18px 22px")
          + stamp(18, "left: 16px; top: 14px", rot=-4))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 314, s1, o1, "1 · Deal gently")

    s2 = f'''      {D("e2")}
      {forest(702, 260, 2501, n=10, smin=0.9, smax=1.2)}
      <path d="M-10 360 L 712 360 L 712 704 L -10 704 Z" fill="#1A241A" stroke="#0D0D0F" stroke-width="2"></path>
      {forest(702, 420, 2502, n=8, smin=1.2, smax=1.6)}
      {fleeing("e2", 10, 40, 680, 470, 560, 2503, 0.34, 0.5)}
      {forest(702, 700, 2504, n=6, smin=1.6, smax=2.0)}
      <rect x="-10" y="-10" width="722" height="704" fill="#05050A" opacity="0.25"></rect>'''
    o2 = (cap("So the people went out into the field against Israel: and the battle was in the forest of Ephraim.", "left: 12px; top: 12px", size=11, maxw=340)
          + shout("and the forest devoured more people that day than the sword devoured.", "right: 14px; bottom: 16px", size=20, maxw=360))
    P2 = panel("linear-gradient(180deg, #2A3A2A 0%, #12201A 100%)", 702, 694, s2, o2, "2 · The forest of Ephraim")
    body = P1 + P2
    return mk.page("2 Samuel 18:5–8 — Deal Gently", "320px minmax(0, 1fr)", body, 5)
PAGES["SB2-P05-Gently"] = p05


def fleeing(p, n, x0, x1, y0, y1, seed, smin, smax):
    r = random.Random(seed); o = []
    for y, x in sorted((r.uniform(y0, y1), r.uniform(x0, x1)) for _ in range(n)):
        s = smin + (smax - smin) * (y - y0) / max(1, y1 - y0)
        o.append(person(p, round(x), round(y), round(s, 3), body="#1A1210", cloth=r.choice(["#3A3A2E", "#4A3A2A", "#2A3A3E"]), kind="Tunic", sw=3, flip=r.random() < 0.5, extra=Z.SPEAR))
    return "".join(o)


# ───────────────────────── 06 · Between Heaven and Earth (18:9–17) ─────────────────────────
def p06():
    s1 = f'''      {D("f1")}
      {G.great_oak(260, 700, 1.8, seed=2601)}
      <path d="M-10 690 L 712 690 L 712 734 L -10 734 Z" fill="#3A4A2A" stroke="#0D0D0F" stroke-width="2"></path>
      {G.hanging(470, 330, 1.05, "p6h")}
      {G.bough_over(470, 330, 1.3, seed=2602)}
      {N.ass(620, 696, 0.75, color="#6A645A")}
      {mk.speed(560, 640, 14, 30, 140, 2603, color="#F3EFE6", op=0.5)}'''
    o1 = (cap("And Absalom was riding upon his mule, and the mule went under the thick boughs of a great oak, and his head caught hold of the oak,", "left: 12px; top: 12px", size=11, maxw=300)
          + shout("and he was taken up between heaven and earth;", "right: 14px; top: 14px", size=24, maxw=260)
          + cap("and the mule that was under him went on.", "right: 12px; bottom: 60px", size=10.5))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #C8D8A8 60%, #6A8A4A 100%)", 702, 724, s1, o1, "1 · Between heaven and earth")

    s2 = f'''      {forest(702, 220, 2604, dark=True, n=8, smin=0.7, smax=0.9)}
      <path d="M-10 200 L 712 200 L 712 274 L -10 274 Z" fill="#1A241A" stroke="#0D0D0F" stroke-width="2"></path>
      {G.stone_heap(470, 250, 280, 120, seed=2605)}
      <rect x="-10" y="-10" width="722" height="294" fill="#2A0A1A" opacity="0.35"></rect>'''
    o2 = cap("And they took Absalom, and cast him into the great pit in the forest, and raised over him a very great heap of stones: and all Israel fled every one to his tent.", "left: 12px; top: 12px", size=10.5, maxw=300)
    P2 = panel("linear-gradient(180deg, #4A1D55 0%, #8A3A4A 100%)", 702, 274, s2, o2, "2 · A very great heap of stones")
    body = P1 + P2
    return mk.page("2 Samuel 18:9–17 — Between Heaven and Earth", "minmax(0, 1fr) 280px", body, 6)
PAGES["SB2-P06-Oak"] = p06


# ───────────────────────── 07 · Tidings (18:24–32) ─────────────────────────
def p07():
    s1 = f'''      {D("g1")}<g transform="translate(0 230)">
      {G.gatehouse(200, 360, 300, 250)}
      {person("g1", 200, 112, 0.38, body="#3A1E14", cloth="#5A6E8A", kind="Tunic", sw=3, up=POINT, flip=True)}
      <path d="M-10 360 C 200 350 500 340 712 330 L 712 520 L -10 520 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("g1", 200, 430, 0.62, **DO, extra=KING)}
      {G.runner("g1", 600, 350, 0.5, flip=True, cloth="#5A6E8A", body="#2A140C")}</g>'''
    o1 = (cap("Now David was sitting between the two gates: and the watchman went up to the roof of the gate unto the wall, and lifted up his eyes, and looked, and, behold, a man running alone.", "right: 12px; top: 12px", size=10.5, maxw=330)
          + cap("And the king said,", "right: 12px; top: 150px", size=10)
          + balloon("If he be alone, there is tidings in his mouth.", "right: 14px; top: 186px", 230, size=14, pad="16px 22px"))
    P1 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 704, s1, o1, "1 · A man running alone")

    s2 = f'''      {face(FX["__FACE_DAVID_OLD__"], -50, 20, 0.74)}'''
    o2 = (cap("And the king said unto the Cushite,", "right: 10px; top: 10px", size=10, maxw=150)
          + balloon("Is it well with the young man Absalom?", "right: 8px; bottom: 16px", 170, size=14, pad="18px 18px"))
    P2a = panel("radial-gradient(circle at 30% 50%, #FFE680 0 20px, #7A3BA8 150px, #12113A 330px)", 342, 294, s2, o2, "2a · Is it well")
    s3 = f'''      {face(FX["__FACE_CUSHITE__"], 392, 20, 0.74, flip=True)}'''
    o3 = (cap("And the Cushite answered,", "left: 10px; top: 10px", size=10)
          + balloon("The enemies of my lord the king, and all that rise up against thee to do thee hurt, be as that young man is.", "left: 8px; bottom: 12px", 190, size=12, pad="22px 20px"))
    P2b = panel("radial-gradient(circle at 70% 50%, #F3EFE6 0 20px, #8A8478 150px, #2A2220 330px)", 342, 294, s3, o3, "2b · Be as that young man is")
    body = P1 + cols(P2a, P2b)
    return mk.page("2 Samuel 18:24–32 — Tidings", "minmax(0, 1fr) 300px", body, 7)
PAGES["SB2-P07-Tidings"] = p07


# ───────────────────────── 08 · O My Son (18:33 – 19:2) ─────────────────────────
def p08():
    s1 = f'''      {face(FX["__FACE_DAVID_OLD_WEEP__"], -60, 160, 1.1)}'''
    o1 = (cap("And the king was much moved, and went up to the chamber over the gate, and wept: and as he went, thus he said,", "right: 14px; top: 14px", size=12, maxw=340)
          + '    <div style="position: absolute; right: 18px; top: 150px; max-width: 330px; padding: 22px 24px; background: #12113A; color: #F3EFE6; box-shadow: inset 0 0 0 4px #12113A, inset 0 0 0 5.5px #8FD0E2; font-family: Anton, sans-serif; font-size: 34px; line-height: 1.12; letter-spacing: 0.03em; text-transform: uppercase">O my son Absalom, my son, my son Absalom! would I had died for thee, O Absalom, my son, my son!</div>\n')
    P1 = panel("radial-gradient(circle at 25% 60%, #8FD0E2 0 30px, #2A3A6A 260px, #05050A 600px)", 702, 724, s1, o1, "1 · O my son Absalom")

    s2 = f'''      {stars(50, 702, 120, 2801)}
      {G.gatehouse(351, 274, 280, 230, lit=True)}
      <path d="M-10 270 L 712 270 L 712 284 L -10 284 Z" fill="#2A1A14"></path>'''
    o2 = cap("And the victory that day was turned into mourning unto all the people; for the people heard say that day, The king grieveth for his son.", "left: 12px; top: 12px", size=10, maxw=190)
    P2 = panel("linear-gradient(180deg, #05050A 0%, #12113A 100%)", 702, 274, s2, o2, "2 · Turned into mourning")
    body = P1 + P2
    return mk.page("2 Samuel 18:33 – 19:2 — O My Son", "minmax(0, 1fr) 280px", body, 8)
PAGES["SB2-P08-MySon"] = p08


# ───────────────────────── 09 · Which Cost Me Nothing (24:18–25) ─────────────────────────
def p09():
    s1 = f'''      {face(FX["__FACE_GAD__"], 760, -20, 0.74, flip=True)}'''
    o1 = (cap("And Gad came that day to David, and said unto him,", "left: 12px; top: 12px", size=10.5, maxw=260)
          + balloon("Go up, rear an altar unto Jehovah in the threshing-floor of Araunah the Jebusite.", "left: 12px; top: 70px", 280, size=14.5, pad="20px 28px")
          + stamp(24, "left: 16px; bottom: 14px", rot=-4))
    P1 = panel("radial-gradient(circle at 80% 50%, #FFE3B8 0 30px, #C9A86A 200px, #5A3A22 460px)", 702, 274, s1, o1, "1 · Rear an altar")

    s2 = f'''      {D("i2")}
      {J.city_hill(600, 150, 200, 90, 2901)}
      <path d="M-10 150 L 712 150 L 712 344 L -10 344 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {G.threshing_floor(470, 270, 300)}
      {A.cow(420, 280, 0.5, color="#8A5A30")}{A.cow(540, 290, 0.5, flip=True)}
      {person("i2", 180, 330, 0.84, **DO, extra=KING)}
      {person("i2", 300, 330, 0.78, body="#3A1E14", cloth="#2C9DB8", kind="Tunic", sw=4, flip=True)}'''
    o2 = (cap("And the king said unto Araunah,", "left: 12px; top: 12px", size=10)
          + balloon("Nay; but I will verily buy it of thee at a price; neither will I offer burnt-offerings unto Jehovah my God which cost me nothing.", "left: 230px; top: 12px", 300, size=13.5, pad="22px 30px")
          + cap("So David bought the threshing-floor and the oxen for fifty shekels of silver.", "right: 12px; bottom: 12px", size=10, maxw=260))
    P2 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 344, s2, o2, "2 · Which cost me nothing")

    s3 = f'''      {V.rays(351, 0, 40, 40, 700, color="#FFF4C2", op=0.3)}
      {G.threshing_floor(351, 340, 360)}
      {G.altar(351, 330, 0.9)}'''
    o3 = (cap("And David built there an altar unto Jehovah, and offered burnt-offerings and peace-offerings. So Jehovah was entreated for the land, and the plague was stayed from Israel.", "left: 12px; top: 12px", size=10.5, maxw=230)
          + end_mark("END OF 2 SAMUEL", "right: 14px; bottom: 12px"))
    P3 = panel("linear-gradient(180deg, #FFE680 0%, #FFC14D 50%, #FF8A3D 100%)", 702, 364, s3, o3, "3 · An altar unto Jehovah")
    body = P1 + P2 + P3
    return mk.page("2 Samuel 24:18–25 — Which Cost Me Nothing", "280px 350px minmax(0, 1fr)", body, 9)
PAGES["SB2-P09-Altar"] = p09


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "2samuel/project"))
