"""Exodus Book Four — Sinai (Exodus 16–20). Writes the .dc.html pages into the given folder.
Usage: python3 exodus_book4.py <out_dir>"""
import sys, pathlib, random
import mk, exodus as E, exodus2 as X, exodus3 as Y, exodus4 as Z, egypt
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, speed, stars
from exodus_book3 import crowd
FX = Z.tokens()
PAGES = {}
ARMS_L = [(-22, -158), (-44, -212), (-36, -268)]
ARMS_R = [(22, -158), (44, -212), (36, -268)]

# ───────────────────────── Cover ─────────────────────────
def cover():
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {defs("c4", "Man", "Woman", "Robe", "Tunic")}
    {X.bolt(150, 330, 260, 11, w=1.2)}{X.bolt(640, 360, 220, 12, w=1.0)}
    {Z.sinai(400, 1000, 760, 560, 7)}
    <path d="M-10 960 C 200 950 500 966 770 956 L 770 1090 L -10 1090 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>
    {crowd("c4", 60, -10, 770, 960, 1050, 21, 0.1, 0.24, body=("#12090A",), cloth=("#3A2214", "#5A3A22", "#2A1A2E", "#4A2A1A"))}
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The Book of</span>
    <span>No. 04</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 168px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6">EXODUS</h1>
  <div style="position: absolute; top: 246px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 262px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book Four — Sinai</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 16 – 20</span>
  </div>
  <div style="position: absolute; top: 236px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>出</span><span>エ</span><span>ジ</span><span>プ</span><span>ト</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">SHUTSU</span>
  </div>
  <div style="position: absolute; left: 38px; top: 330px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 12px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 250px; line-height: 1.45">And mount Sinai, the whole of it, smoked, because Jehovah descended upon it in fire;</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 4</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #05050A 0%, #12113A 30%, #4A1D55 60%, #B5421E 85%, #3A2214 100%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Exodus Book Four — Cover", None, body, root_style=root)
PAGES["EX4-Cover"] = cover

# ───────────────────────── 01 · Bread from Heaven (16:2–4) ─────────────────────────
def p01():
    s1 = f'''      {defs("a1", "Man", "ManUp", "Woman", "Robe", "Tunic")}
      <circle cx="600" cy="70" r="44" fill="#FFF4C2"></circle>
      <path d="M-10 170 C 200 160 500 176 712 166 L 712 304 L -10 304 Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></path>
      {crowd("a1", 50, -10, 712, 176, 300, 31, 0.16, 0.42)}'''
    o1 = (cap("And the whole congregation of the children of Israel murmured against Moses and against Aaron in the wilderness:", "left: 12px; top: 12px", maxw=400)
          + sfx("ザワザワ", "ZAWA ZAWA", "right: 20px; top: 110px", size=38, fill="#0D0D0F", stroke="#F3EFE6", rot=6)
          + stamp(16, "right: 16px; top: 14px"))
    P1 = panel("linear-gradient(180deg, #FF9A6B 0%, #FFC98A 50%)", 702, 294, s1, o1, "1 · They murmured")

    s2 = f'''      {speed(170, 200, 50, 170, 800, 3, color="#0D0D0F", sw=1.6, op=0.35)}
      {face(FX["__FACE_HEBREW_ANGRY__"], -60, 0, 0.95)}'''
    o2 = (cap("and the children of Israel said unto them,", "left: 12px; top: 12px")
          + tail(168, 218, "l")
          + balloon("Would that we had died by the hand of Jehovah in the land of Egypt, when we sat by the flesh-pots, when we did eat bread to the full; for ye have brought us forth into this wilderness, to kill this whole assembly with hunger.", "left: 206px; top: 56px", 476, size=15, pad="34px 48px")
          + ref("EX 16:3", "right: 12px; bottom: 9px"))
    P2 = panel("radial-gradient(circle at 20% 50%, #FFC98A 0 30px, #E8A35A 200px, #8A3A1E 460px)", 702, 392, s2, o2, "2 · The flesh-pots")

    s3 = f'''      {stars(120, 702, 294, 3)}
      <path d="M-10 250 C 200 240 500 256 712 246 L 712 304 L -10 304 Z" fill="#2A1A10"></path>
      {"".join(Z.tent(x, 254, w, h, color="#3A2214") for x, w, h in [(80, 70, 50), (170, 60, 44), (520, 80, 56), (620, 64, 46)])}'''
    o3 = (cap("Then said Jehovah unto Moses,", "left: 12px; top: 12px")
          + god("Behold, I will rain bread from heaven for you; and the people shall go out and gather a day's portion every day, that I may prove them, whether they will walk in my law, or not.", "left: 12px; top: 58px", size=18, maxw=520))
    P3 = panel("linear-gradient(180deg, #05050A 0%, #12113A 100%)", 702, 294, s3, o3, "3 · Bread from heaven")
    body = P1 + P2 + P3
    return mk.page("Exodus 16:2–4 — Bread from Heaven", "300px minmax(0, 1fr) 300px", body, 1)
PAGES["EX4-P01-Murmur"] = p01

# ───────────────────────── 02 · Manna (16:13–31) ─────────────────────────
def p02():
    tents = "".join(Z.tent(x, 284, w, h) for x, w, h in [(60, 90, 70), (180, 80, 60), (300, 100, 76), (440, 90, 66), (580, 110, 80), (680, 80, 60)])
    s1 = f'''      <path d="M-10 230 C 200 220 500 236 712 226 L 712 304 L -10 304 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {tents}
      {Z.quails(40, -10, 712, 40, 220, 13, 0.35, 0.9)}
      {Z.quails(14, -10, 712, 250, 290, 14, 0.5, 0.8, flying=False)}'''
    o1 = cap("And it came to pass at even, that the quails came up, and covered the camp: and in the morning the dew lay round about the camp.", "left: 12px; top: 12px", maxw=400)
    P1 = panel("linear-gradient(180deg, #7A2A5A 0%, #FF8A3D 60%, #FFC98A 100%)", 702, 294, s1, o1, "1 · The quails")

    gatherers = "".join(E.kneel(x, y, s, color=c, flip=fl) + Z.basket(x + (40 if not fl else -40) * s, y, s) for x, y, s, c, fl in
                        [(110, 290, 0.6, "#C2456A", False), (260, 320, 0.8, "#5A6E8A", True), (420, 300, 0.66, "#C9A86A", False), (590, 340, 0.9, "#8A6A4A", True)])
    s2 = f'''      <circle cx="560" cy="80" r="50" fill="#FFF4C2"></circle>
      <path d="M-10 190 C 200 180 500 196 712 186 L 712 402 L -10 402 Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></path>
      {Z.manna(420, -10, 712, 196, 400, 15)}
      {gatherers}'''
    o2 = (cap("And when the dew that lay was gone up, behold, upon the face of the wilderness a small round thing, small as the hoar-frost on the ground.", "left: 12px; top: 12px", maxw=400)
          + cap("And the house of Israel called the name thereof Manna: and it was like coriander seed, white; and the taste of it was like wafers made with honey.", "right: 12px; bottom: 12px", maxw=330))
    P2 = panel("linear-gradient(180deg, #FFE3B8 0%, #FFF4C2 40%)", 702, 392, s2, o2, "2 · A small round thing")

    s3 = f'''      {face(FX["__FACE_WOMAN__"], -60, 10, 0.78)}'''
    o3 = (cap("And when the children of Israel saw it, they said one to another,", "left: 10px; top: 10px", size=10, maxw=210)
          + tail(116, 188, "l")
          + balloon("What is it?", "left: 154px; top: 156px", 160, size=19, pad="18px 12px")
          + cap("for they knew not what it was.", "right: 10px; bottom: 10px", size=10, maxw=180))
    P3a = panel("linear-gradient(180deg, #FFF4C2, #E8C88A)", 342, 294, s3, o3, "3a · What is it?")
    s4 = f'''      {face(FX["__FACE_MOSES_CALM__"], 400, 10, 0.78, flip=True)}'''
    o4 = (cap("And Moses said unto them,", "left: 10px; top: 10px", size=10)
          + tail(194, 180, "r")
          + balloon("It is the bread which Jehovah hath given you to eat.", "left: 8px; top: 120px", 196, size=14, pad="20px 20px"))
    P3b = panel("linear-gradient(180deg, #FFE3B8, #C9A86A)", 342, 294, s4, o4, "3b · The bread")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Exodus 16:13–31 — Manna", "300px minmax(0, 1fr) 300px", body, 2)
PAGES["EX4-P02-Manna"] = p02

# ───────────────────────── 03 · The Rock in Horeb (17:3–6) ─────────────────────────
def p03():
    stones = "".join(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="5" fill="#8A8478" stroke="#0D0D0F" stroke-width="1.4"></ellipse>' for x, y in [(160, 120), (300, 100), (470, 130)])
    s1 = f'''      {defs("b1", "Man", "ManUp", "Robe", "Tunic")}
      <path d="M-10 170 C 200 160 500 176 712 166 L 712 264 L -10 264 Z" fill="#E8B070" stroke="#0D0D0F" stroke-width="2"></path>
      {"".join(person("b1", x, y, s, body="#2A140C", cloth=c, kind="Tunic", sw=4, up=[(-22, -158), (-36, -214), (-24, -262)]) for x, y, s, c in [(150, 250, 0.5, "#8A6A4A"), (300, 240, 0.46, "#5A6E8A"), (470, 252, 0.52, "#C9A86A"), (580, 236, 0.4, "#8A3A1E")])}
      {crowd("b1", 24, -10, 712, 190, 250, 33, 0.18, 0.34)}
      {stones}'''
    o1 = (cap("And the people thirsted there for water; and the people murmured against Moses, and said,", "left: 12px; top: 12px", maxw=300)
          + balloon("Wherefore hast thou brought us up out of Egypt, to kill us and our children and our cattle with thirst?", "right: 14px; top: 10px", 330, size=13, pad="18px 30px")
          + stamp(17, "right: 16px; bottom: 12px"))
    P1 = panel("linear-gradient(180deg, #FF6A2A 0%, #FFC14D 60%)", 702, 254, s1, o1, "1 · Thirst")

    s2 = f'''      {face(FX["__FACE_MOSES_AFRAID__"], -70, 10, 0.8)}'''
    o2 = (cap("And Moses cried unto Jehovah, saying,", "left: 10px; top: 10px", size=10)
          + tail(114, 200, "l")
          + balloon("What shall I do unto this people? they are almost ready to stone me.", "left: 152px; top: 120px", 182, size=13.5, pad="20px 18px"))
    P2a = panel("radial-gradient(circle at 30% 40%, #FFE680 0 20px, #FF8A3D 160px, #5A1A3E 340px)", 342, 352, s2, o2, "2a · Ready to stone me")
    s3 = f'''      {Z.rock(-10, 352, 362, 250)}'''
    o3 = god("Behold, I will stand before thee there upon the rock in Horeb; and thou shalt smite the rock, and there shall come water out of it, that the people may drink.", "left: 10px; top: 10px; right: 10px", size=16)
    P2b = panel("linear-gradient(180deg, #2A1A5E, #7A2A5A)", 342, 352, s3, o3, "2b · The rock in Horeb")

    s4 = f'''      {defs("b4", "Man", "ManUp", "Robe", "Tunic")}
      <path d="M-10 330 C 200 320 500 336 712 326 L 712 384 L -10 384 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {Z.rock(300, 340, 300, 260)}
      {Z.gush(450, 170, 9, 1.1)}
      <path d="M200 360 C 300 350 560 350 712 364 L 712 384 L 160 384 Z" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="1.6"></path>
      {person("b4", 230, 350, 0.95, body="#3A1E14", cloth="#E2D8C4", flip=True, up=[(-22, -158), (-58, -196), (-92, -200)],
              extra='<path d="M-92 -200 L -230 -190" stroke="#0D0D0F" stroke-width="11" stroke-linecap="round"></path><path d="M-92 -200 L -230 -190" stroke="#8A5A30" stroke-width="7" stroke-linecap="round"></path>')}
      {crowd("b4", 20, -10, 150, 280, 370, 35, 0.2, 0.42)}'''
    o4 = (cap("And Moses did so in the sight of the elders of Israel.", "left: 12px; top: 12px", maxw=300)
          + sfx("ドバッ", "DOBA!", "right: 24px; top: 20px", size=60, fill="#8FD0E2", stroke="#0D0D0F", rot=8)
          + ref("EX 17:6", "right: 12px; bottom: 9px"))
    P3 = panel("radial-gradient(circle at 65% 45%, #FFF4C2 0 40px, #FFC98A 200px, #B5652E 460px)", 702, 374, s4, o4, "3 · Water out of the rock")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Exodus 17:3–6 — The Rock in Horeb", "260px minmax(0, 1fr) 380px", body, 3)
PAGES["EX4-P03-Rock"] = p03

# ───────────────────────── 04 · Hands Held Up (17:8–13) ─────────────────────────
def p04():
    s1 = f'''      {defs("h1", "Man", "ManUp", "Tunic")}
      <path d="M-10 190 C 200 180 500 196 712 186 L 712 254 L -10 254 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>
      {Z.warriors("h1", 16, 300, 712, 196, 250, 41, 0.22, 0.4, flip=True, body="#12090A", cloth=("#3A0E0E", "#5A1A16"))}'''
    o1 = (cap("Then came Amalek, and fought with Israel in Rephidim.", "left: 12px; top: 12px", maxw=300)
          + sfx("ウオオオ", "UOOOO", "left: 40px; top: 100px", size=40, fill="#D7261E", stroke="#F3EFE6", rot=-6, align="flex-start"))
    P1 = panel("linear-gradient(180deg, #7A0E1E 0%, #FF6A2A 100%)", 702, 244, s1, o1, "1 · Amalek")

    s2 = f'''      {defs("h2", "Man", "ManUp", "Robe", "Tunic")}
      <circle cx="351" cy="150" r="90" fill="#FFC14D"></circle><circle cx="351" cy="150" r="140" fill="#FFC14D" opacity="0.25"></circle>
      <path d="M100 300 C 200 210 500 210 610 300 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></path>
      <path d="M-10 300 L 712 300 L 712 482 L -10 482 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>
      <ellipse cx="351" cy="268" rx="34" ry="14" fill="#8A8478" stroke="#0D0D0F" stroke-width="2"></ellipse>
      {Z.figure_both(351, 262, 0.72, "#12090A", "#E2D8C4", ARMS_L, ARMS_R, "h2m", stroke="#FFE680")}
      {person("h2", 290, 270, 0.68, body="#12090A", cloth="#4A6A9A", stroke="#FFE680", flip=True, up=[(-22, -158), (-40, -230), (-52, -294)])}
      {person("h2", 412, 270, 0.68, body="#12090A", cloth="#8A6A4A", stroke="#FFE680", up=[(-22, -158), (-40, -230), (-52, -294)])}
      {Z.warriors("h2", 14, 360, 712, 330, 470, 43, 0.3, 0.55, flip=True, body="#12090A", cloth=("#3A0E0E", "#5A1A16"))}
      {Z.warriors("h2", 14, -10, 360, 330, 470, 44, 0.3, 0.55, body="#3A1E14", cloth=("#5A6E8A", "#C9A86A", "#8A6A4A"))}'''
    o2 = (cap("And it came to pass, when Moses held up his hand, that Israel prevailed; and when he let down his hand, Amalek prevailed.", "left: 12px; top: 12px", maxw=340)
          + cap("But Moses' hands were heavy; and they took a stone, and put it under him, and he sat thereon; and Aaron and Hur stayed up his hands, the one on the one side, and the other on the other side;", "right: 12px; top: 12px", maxw=300)
          + ref("MOSES · AARON · HUR", "left: 50%; top: 286px; transform: translateX(-50%)", color="#0D0D0F", bg="#F3EFE6"))
    P2 = panel("linear-gradient(180deg, #7A2A5A 0%, #FF6A2A 45%, #FFC14D 62%)", 702, 482, s2, o2, "2 · Hands held up")

    s3 = f'''      {speed(120, 160, 40, 120, 400, 13, color="#0D0D0F", sw=1.6, op=0.4)}
      {face(FX["__FACE_JOSHUA__"], -60, -20, 0.8)}'''
    o3 = cap("And Joshua discomfited Amalek and his people with the edge of the sword.", "right: 10px; bottom: 10px", size=10.5, maxw=170) + ref("JOSHUA", "left: 10px; bottom: 8px", color="#0D0D0F", bg="#F3EFE6")
    P3a = panel("radial-gradient(circle at 30% 40%, #FFE680 0 20px, #FF6A2A 160px, #5A0E16 340px)", 342, 254, s3, o3, "3a · Joshua")
    s4 = f'''      <circle cx="171" cy="200" r="70" fill="#D7261E"></circle>
      <path d="M-10 200 L 352 200 L 352 264 L -10 264 Z" fill="#2A140C"></path>
      <path d="M90 200 C 130 150 210 150 250 200 Z" fill="#12090A"></path>
      {Z.figure_both(171, 184, 0.3, "#12090A", "#12090A", ARMS_L, ARMS_R, "h4m")}'''
    o4 = cap("and his hands were steady until the going down of the sun.", "left: 10px; right: 10px; top: 10px", size=10.5) + ref("EX 17:12", "right: 10px; bottom: 8px")
    P3b = panel("linear-gradient(180deg, #4A1D55 0%, #FF6A2A 100%)", 342, 254, s4, o4, "3b · The going down of the sun")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Exodus 17:8–13 — Hands Held Up", "250px minmax(0, 1fr) 260px", body, 4)
PAGES["EX4-P04-Amalek"] = p04

# ───────────────────────── 05 · The Mountain Smoked (19:16–20) ─────────────────────────
def p05():
    s1 = f'''      {defs("m1", "Man", "Woman", "Robe", "Tunic")}
      {X.bolt(110, -10, 300, 21, w=1.2)}{X.bolt(600, -10, 260, 22, w=1.0)}
      {Z.sinai(351, 640, 640, 520, 23)}
      <path d="M-10 620 C 200 610 500 626 712 616 L 712 714 L -10 714 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>
      {crowd("m1", 70, -10, 712, 620, 710, 24, 0.12, 0.3, body=("#12090A",), cloth=("#3A2214", "#5A3A22", "#2A1A2E", "#4A2A1A"))}'''
    o1 = (cap("And it came to pass on the third day, when it was morning, that there were thunders and lightnings, and a thick cloud upon the mount, and the voice of a trumpet exceeding loud; and all the people that were in the camp trembled.", "left: 12px; top: 12px", maxw=330)
          + sfx("ブオオオオ", "BUOOOO", "right: 18px; top: 24px", size=44, fill="#FFF4C2", stroke="#4A1D55", rot=6, tagbg="#FFF4C2", tagfg="#4A1D55")
          + cap("And mount Sinai, the whole of it, smoked, because Jehovah descended upon it in fire; and the smoke thereof ascended as the smoke of a furnace, and the whole mount quaked greatly.", "right: 12px; bottom: 110px", maxw=320)
          + stamp(19, "left: 16px; bottom: 120px", rot=-4))
    P1 = panel("linear-gradient(180deg, #05050A 0%, #2A1A5E 40%, #7A2A5A 80%, #B5421E 100%)", 702, 704, s1, o1, "1 · The mountain smoked")

    s2 = f'''      {defs("m2", "Man", "Woman", "Hair", "Robe", "Tunic")}
      <path d="M200 -10 L 352 -10 L 352 120 C 300 100 240 60 200 -10 Z" fill="#2A2232"></path>
      <path d="M-10 150 C 100 140 240 156 352 146 L 352 304 L -10 304 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>
      {crowd("m2", 34, -10, 352, 160, 290, 25, 0.16, 0.4)}'''
    o2 = cap("And Moses brought forth the people out of the camp to meet God; and they stood at the nether part of the mount.", "left: 10px; right: 10px; top: 10px", size=10)
    P2a = panel("linear-gradient(180deg, #2A1A5E, #7A2A5A)", 342, 294, s2, o2, "2a · The nether part of the mount")
    s3 = f'''      {defs("m3", "Man", "Robe")}
      <path d="M-10 304 L 120 120 L 200 60 L 260 -10 L 352 -10 L 352 304 Z" fill="#3A2A3E" stroke="#0D0D0F" stroke-width="2.4"></path>
      {E.blaze(300, 60, 140, 120, 31, n=7)}
      <path d="M40 300 C 100 240 150 200 200 140" fill="none" stroke="#5A4A6E" stroke-width="3" stroke-dasharray="6 8"></path>
      {person("m3", 170, 196, 0.26, body="#12090A", cloth="#E2D8C4", stroke="#FFE680", sw=6)}'''
    o3 = cap("and Jehovah called Moses to the top of the mount; and Moses went up.", "left: 10px; bottom: 10px", size=10.5, maxw=220) + ref("EX 19:20", "right: 10px; bottom: 8px")
    P2b = panel("linear-gradient(180deg, #05050A, #4A1D55)", 342, 294, s3, o3, "2b · Moses went up")
    body = P1 + cols(P2a, P2b)
    return mk.page("Exodus 19:16–20 — The Mountain Smoked", "minmax(0, 1fr) 300px", body, 5)
PAGES["EX4-P05-Sinai"] = p05

# ───────────────────────── 06 · I Am Jehovah Thy God (20:1–7) ─────────────────────────
def word_panel(k, text, bg, art, h, size=19, maxw=520):
    o = Z.numeral(k, "left: 18px; top: 50%; transform: translateY(-50%)") + god(text, f"left: 130px; top: 50%; transform: translateY(-50%)", size=size, maxw=maxw)
    return panel(bg, 702, h, art, o, f"Word {k}")

def p06():
    s1 = f'''      {Z.sinai(560, 330, 360, 300, 41)}
      {speed(560, 120, 60, 120, 700, 42, color="#FFE680", sw=1.4, op=0.5)}'''
    o1 = (cap("And God spake all these words, saying,", "left: 12px; top: 12px")
          + god("I am Jehovah thy God, who brought thee out of the land of Egypt, out of the house of bondage.", "left: 12px; top: 60px", size=26, maxw=400)
          + stamp(20, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(180deg, #05050A 0%, #4A1D55 70%, #B5421E 100%)", 702, 314, s1, o1, "1 · I am Jehovah thy God")
    P2 = word_panel(1, "Thou shalt have no other gods before me.", "linear-gradient(90deg, #12113A 0%, #4A1D55 100%)", stars(40, 702, 164, 51), 164, size=24)
    idols = "".join(f'<g transform="translate({x} 330) rotate({rot})"><rect x="-20" y="-110" width="40" height="110" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2"></rect><circle cx="0" cy="-124" r="18" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2"></circle></g>' for x, rot in [(560, -70), (630, 20), (680, -100)])
    P3 = word_panel(2, "Thou shalt not make unto thee a graven image, nor any likeness of any thing that is in heaven above, or that is in the earth beneath, or that is in the water under the earth: thou shalt not bow down thyself unto them, nor serve them; …", "linear-gradient(90deg, #12113A 0%, #7A2A5A 100%)", idols, 304, size=16, maxw=400)
    P4 = word_panel(3, "Thou shalt not take the name of Jehovah thy God in vain; for Jehovah will not hold him guiltless that taketh his name in vain.", "linear-gradient(90deg, #12113A 0%, #2A1A5E 100%)", X.bolt(640, -10, 200, 51, w=0.8), 194, size=17, maxw=470)
    body = P1 + P2 + P3 + P4
    return mk.page("Exodus 20:1–7 — I Am Jehovah Thy God", "320px 170px minmax(0, 1fr) 200px", body, 6)
PAGES["EX4-P06-IAm"] = p06

# ───────────────────────── 07 · The Ten Words (20:8–17) ─────────────────────────
def small_word(k, text, bg, art, w, h, size=15):
    o = Z.numeral(k, "left: 12px; top: 10px", size=64) + god(text, "left: 12px; right: 12px; bottom: 12px", size=size)
    return panel(bg, w, h, art, o, f"Word {k}")

def p07():
    sab = f'''<circle cx="250" cy="150" r="50" fill="#FFC14D"></circle><path d="M-10 160 L 352 160 L 352 300 L -10 300 Z" fill="#5A3A22"></path>{Z.tent(270, 160, 80, 56)}'''
    P1a = small_word(4, "Remember the sabbath day, to keep it holy.", "linear-gradient(180deg, #4A1D55, #FF8A3D)", sab, 342, 294, size=17)
    fam = f'''{defs("t5", "Man", "Woman", "Hair", "Robe")}<path d="M-10 200 L 352 200 L 352 300 L -10 300 Z" fill="#5A3A22"></path>
      {person("t5", 220, 210, 0.5, body="#3A2214", cloth="#B8B2A6")}{person("t5", 270, 210, 0.46, body="#3A2214", cloth="#8A7A9A", woman=True, hair="#B8B2A6")}{person("t5", 310, 214, 0.34, body="#3A2214", cloth="#C2456A")}'''
    P1b = small_word(5, "Honor thy father and thy mother, that thy days may be long in the land which Jehovah thy God giveth thee.", "linear-gradient(180deg, #12113A, #7A2A5A)", fam, 342, 294, size=13.5)
    P2a = small_word(6, "Thou shalt not kill.", "linear-gradient(180deg, #5A0E16, #12040A)", "", 222, 224, size=18)
    P2b = small_word(7, "Thou shalt not commit adultery.", "linear-gradient(180deg, #4A1D55, #12113A)", "", 222, 224, size=17)
    P2c = small_word(8, "Thou shalt not steal.", "linear-gradient(180deg, #1F5FAD, #12113A)", "", 222, 224, size=18)
    witness = f'''{defs("t9", "Man", "ManUp", "Robe")}<path d="M-10 330 L 352 330 L 352 470 L -10 470 Z" fill="#2A1A2E"></path>
      {person("t9", 110, 330, 0.9, body="#12090A", cloth="#5A4A6E", stroke="#C8C2D6", flip=True, up=[(-22, -158), (-70, -168), (-118, -176)])}
      {person("t9", 250, 334, 0.8, body="#12090A", cloth="#3A2A3E", stroke="#C8C2D6")}'''
    P3a = small_word(9, "Thou shalt not bear false witness against thy neighbor.", "linear-gradient(180deg, #3A2A3E, #12113A)", witness, 342, 462, size=17)
    covet = f'''<path d="M-10 300 L 352 300 L 352 470 L -10 470 Z" fill="#5A3A22"></path>{Z.tent(110, 300, 150, 110)}
      <g transform="translate(196 238) scale(0.9)"><path d="{egypt.FAT}" transform="scale(-1 1) translate(-124 0)" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path></g>
      {E.sheep(300, 300, 0.7, flip=True)}'''
    P3b = small_word(10, "Thou shalt not covet thy neighbor's house, thou shalt not covet thy neighbor's wife, nor his man-servant, nor his maid-servant, nor his ox, nor his ass, nor anything that is thy neighbor's.", "linear-gradient(180deg, #7A2A5A, #12113A)", covet, 342, 462, size=15)
    body = cols(P1a, P1b) + cols(P2a, P2b, P2c) + cols(P3a, P3b)
    return mk.page("Exodus 20:8–17 — The Ten Words", "300px 230px minmax(0, 1fr)", body, 7)
PAGES["EX4-P07-TenWords"] = p07

# ───────────────────────── 08 · Afar Off (20:18–21) ─────────────────────────
_r = random.Random(77)
_puffs = [(_r.uniform(470, 730), _r.uniform(-20, 220), _r.uniform(40, 80)) for _ in range(22)]
_c = "".join(f'<circle cx="{a:.0f}" cy="{b:.0f}" r="{rr:.0f}"></circle>' for a, b, rr in _puffs)
DARK = (f'<g fill="#05050A" stroke="#FFD23F" stroke-width="3">{_c}</g><g fill="#05050A">{_c}</g>'
        '<ellipse cx="610" cy="100" rx="70" ry="44" fill="#FFD23F" opacity="0.18"></ellipse>'
        + "".join(f'<path d="M610 100 L {610 + 140*__import__("math").cos(a):.0f} {100 + 100*__import__("math").sin(a):.0f}" stroke="#FFD23F" stroke-width="1.2" opacity="0.35"></path>' for a in [i * 0.5 for i in range(13)]))

def p08():
    s1 = f'''      {defs("z1", "Man", "Woman", "Robe", "Tunic")}
      {X.bolt(560, -10, 200, 61, w=0.9)}
      {Z.sinai(560, 324, 340, 300, 62)}
      <path d="M-10 280 C 200 270 500 286 712 276 L 712 334 L -10 334 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>
      {crowd("z1", 40, -10, 300, 270, 330, 63, 0.14, 0.3, body=("#12090A",), cloth=("#3A2214", "#5A3A22", "#2A1A2E"))}'''
    o1 = cap("And all the people perceived the thunderings, and the lightnings, and the voice of the trumpet, and the mountain smoking: and when the people saw it, they trembled, and stood afar off.", "left: 12px; top: 12px", maxw=380)
    P1 = panel("linear-gradient(180deg, #05050A 0%, #2A1A5E 60%, #7A2A5A 100%)", 702, 324, s1, o1, "1 · They trembled")

    s2 = f'''      {face(FX["__FACE_WOMAN_FEAR__"], -70, 10, 0.8)}'''
    o2 = (cap("And they said unto Moses,", "left: 10px; top: 10px", size=10)
          + tail(116, 196, "l")
          + balloon("Speak thou with us, and we will hear; but let not God speak with us, lest we die.", "left: 154px; top: 110px", 180, size=13.5, pad="20px 18px"))
    P2a = panel("radial-gradient(circle at 30% 40%, #C8C2D6 0 20px, #5A6E8A 160px, #12113A 340px)", 342, 352, s2, o2, "2a · Lest we die")
    s3 = f'''      {face(FX["__FACE_MOSES_CALM__"], 412, 10, 0.8, flip=True)}'''
    o3 = (cap("And Moses said unto the people,", "right: 10px; top: 10px", size=10)
          + tail(186, 190, "r")
          + balloon("Fear not: for God is come to prove you, and that his fear may be before you, that ye sin not.", "left: 8px; top: 96px", 190, size=13, pad="22px 18px"))
    P2b = panel("radial-gradient(circle at 70% 40%, #FFF4C2 0 20px, #FFC14D 160px, #7A2A5A 340px)", 342, 352, s3, o3, "2b · Fear not")

    s4 = f'''      {defs("z4", "Man", "Woman", "Robe", "Tunic")}
      {DARK}
      <path d="M-10 290 C 200 280 500 296 712 286 L 712 334 L -10 334 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M300 290 C 380 240 440 200 500 150" fill="none" stroke="#C8C2D6" stroke-width="2" stroke-dasharray="5 7"></path>
      {person("z4", 470, 190, 0.3, body="#12090A", cloth="#E2D8C4", stroke="#FFD23F", sw=6)}
      {crowd("z4", 30, -10, 260, 280, 330, 65, 0.16, 0.3)}'''
    o4 = (cap("And the people stood afar off, and Moses drew near unto the thick darkness where God was.", "left: 12px; top: 12px", maxw=330)
          + '    <span style="position: absolute; right: 10px; bottom: 7px; font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">つづく · TO BE CONTINUED</span>\n')
    P3 = panel("linear-gradient(180deg, #4A1D55 0%, #C2456A 100%)", 702, 324, s4, o4, "3 · The thick darkness")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Exodus 20:18–21 — Afar Off", "330px minmax(0, 1fr) 330px", body, 8)
PAGES["EX4-P08-AfarOff"] = p08


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "exodus/project"))
