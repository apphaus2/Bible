"""Exodus Book Two — The Plagues (Exodus 5–11). Writes the .dc.html pages into the given folder.
Usage: python3 exodus_book2.py <out_dir>"""
import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1] / "kit"))  # shared drawing kit
import sys, pathlib, random
import mk, exodus as E, exodus2 as X, egypt
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, speed, stars
FX = X.tokens()
PAGES = {}
NEMES = '<path d="M-17 -204 C -10 -214 10 -214 17 -204 L 24 -150 L 12 -156 L 10 -176 L -10 -176 L -12 -156 L -24 -150 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="3"></path><path d="M-19 -190 L 19 -190 M-21 -172 L 21 -172" stroke="#1F5FAD" stroke-width="4"></path>'
ROD_UP = '<path d="M-38 -276 L -24 -390" stroke="#0D0D0F" stroke-width="11" stroke-linecap="round"></path><path d="M-38 -276 L -24 -390" stroke="#8A5A30" stroke-width="7" stroke-linecap="round"></path>'
ARM_UP = [(-22, -158), (-44, -214), (-40, -272)]
KILT = '<path d="M-27 -108 L 27 -108 L 34 -58 L -34 -58 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="3"></path>'

# ───────────────────────── Cover ─────────────────────────
def cover():
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {defs("c2", "Man", "ManUp", "Robe")}
    {X.bolt(560, 300, 330, 7, w=1.4)}
    {X.locusts(46, 380, 760, 300, 640, 12, 0.18, 0.55)}
    {X.hail(40, 0, 760, 330, 820, 4)}
    {egypt.pyramid(150, 800, 300, 190, lit="#7A2A3A", dark="#3A0E1E", line="#5A1A2A", n=8)}
    {egypt.pyramid(330, 806, 200, 120, lit="#7A2A3A", dark="#3A0E1E", line="#5A1A2A", n=6)}
    <path d="M-10 800 C 160 790 300 810 480 798 C 600 790 700 800 770 796 L 770 1090 L -10 1090 Z" fill="#3A1A10" stroke="#0D0D0F" stroke-width="2"></path>
    <path d="M-10 860 C 200 840 400 880 600 856 C 680 846 730 852 770 850 L 770 940 C 560 950 360 930 160 950 C 80 958 30 954 -10 952 Z" fill="#8A0E16" stroke="#0D0D0F" stroke-width="2"></path>
    <g fill="none" stroke="#FF4B3E" stroke-width="2.4" opacity="0.8"><path d="M40 900 C 120 890 200 906 280 898"></path><path d="M360 912 C 440 902 520 918 600 908"></path><path d="M200 934 C 280 926 340 940 420 932"></path></g>
    {X.fish(260, 912, 0.6)}{X.fish(470, 900, 0.5, rot=170)}{X.fish(620, 924, 0.55, rot=190)}
    {person("c2", 600, 1010, 1.15, body="#12090A", cloth="#2A1A2E", stroke="#FF4B3E", sw=2.4, up=ARM_UP, extra=ROD_UP)}
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The Book of</span>
    <span>No. 02</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 168px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6">EXODUS</h1>
  <div style="position: absolute; top: 246px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 262px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book Two — The Plagues</span>
    <span style="font-weight: 500; opacity: 0.75">Chapters 5 – 11</span>
  </div>
  <div style="position: absolute; top: 236px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>出</span><span>エ</span><span>ジ</span><span>プ</span><span>ト</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">SHUTSU</span>
  </div>
  <div style="position: absolute; left: 38px; top: 330px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 12px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 240px; line-height: 1.45">Let my people go.</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 2</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #0B0A24 0%, #2A0E2E 30%, #7A0E1E 62%, #D7261E 78%, #3A1A10 100%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Exodus Book Two — Cover", None, body, root_style=root)
PAGES["EX2-Cover"] = cover

# ───────────────────────── 01 · Let My People Go (5:1–12) ─────────────────────────
def p01():
    s1 = f'''      {speed(500, 150, 50, 140, 700, 3, color="#FFE680", sw=1.2, op=0.4)}
      {face(FX["__FACE_AARON__"], -80, -10, 0.78)}
      {face(FX["__FACE_MOSES__"], 60, -30, 0.8)}'''
    o1 = (cap("And afterward Moses and Aaron came, and said unto Pharaoh,", "right: 12px; top: 12px", maxw=360)
          + tail(252, 152, "l")
          + balloon("Thus saith Jehovah, the God of Israel, Let my people go, that they may hold a feast unto me in the wilderness.", "left: 290px; top: 74px", 380, size=16, pad="22px 34px")
          + ref("AARON", "left: 12px; bottom: 10px", color="#0D0D0F", bg="#F3EFE6") + ref("MOSES", "left: 200px; bottom: 10px", color="#0D0D0F", bg="#F3EFE6")
          + stamp(5, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(90deg, #C9A86A 0%, #FFC98A 45%, #FF8A3D 100%)", 702, 294, s1, o1, "1 · Moses and Aaron")

    s2 = f'''      {X.columns([300, 400, 640], -10, 400, 46, color="#3A0E0E")}
      {face(FX["__FACE_PHARAOH_NEW__"], 760, -10, 1.0, flip=True)}'''
    o2 = (cap("And Pharaoh said,", "left: 12px; top: 12px")
          + tail(482, 222, "r")
          + balloon("Who is Jehovah, that I should hearken unto his voice to let Israel go? I know not Jehovah, and moreover I will not let Israel go.", "left: 24px; top: 96px", 466, size=19, pad="26px 40px")
          + ref("EX 5:2", "left: 12px; bottom: 9px"))
    P2 = panel("radial-gradient(circle at 80% 50%, #FF6A4A 0 40px, #8A1A1A 220px, #2A0A0A 460px)", 702, 392, s2, o2, "2 · Who is Jehovah?")

    s3 = f'''      {face(FX["__FACE_TASKMASTER__"], -84, 4, 0.76)}'''
    o3 = (cap("And the taskmasters of the people went out, and their officers, and they spake to the people, saying,", "left: 10px; right: 10px; top: 10px", size=10)
          + tail(96, 178, "l")
          + balloon("Thus saith Pharaoh, I will not give you straw. Go yourselves, get you straw where ye can find it: for nought of your work shall be diminished.", "left: 124px; top: 80px", 212, size=11.5, pad="22px 22px"))
    P3a = panel("linear-gradient(180deg, #FF8A3D, #8A3A1E)", 342, 294, s3, o3, "3a · No straw")

    r = random.Random(5)
    stub = "".join(f'<path d="M{x:.0f} {y:.0f} L {x + r.uniform(-3, 3):.0f} {y - r.uniform(6, 14):.0f}" stroke="#8A6A3A" stroke-width="1.6"></path>' for x, y in ((r.uniform(0, 342), r.uniform(170, 294)) for _ in range(220)))
    gather = "".join(E.kneel(x, y, s, color="#3A2214", rim="#0D0D0F", flip=fl) + f'<path d="{egypt.SHEAF}" transform="translate({x + (-34 if fl else 34) * s:.0f} {y:.0f}) scale({s * 1.2:.2f})" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></path>'
                     for x, y, s, fl in [(60, 230, 0.4, False), (150, 250, 0.5, True), (250, 222, 0.36, False), (300, 270, 0.6, True)])
    s4 = f'''      <circle cx="270" cy="70" r="34" fill="#FFF4C2"></circle>
      <path d="M-10 160 C 100 150 240 166 352 156 L 352 304 L -10 304 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {stub}
      {gather}'''
    o4 = cap("So the people were scattered abroad throughout all the land of Egypt to gather stubble for straw.", "left: 10px; right: 10px; top: 10px", size=10.5) + ref("EX 5:12", "right: 10px; bottom: 8px", color="#0D0D0F", bg="#F3EFE6")
    P3b = panel("linear-gradient(180deg, #FF6A2A 0%, #FFC14D 45%)", 342, 294, s4, o4, "3b · Stubble for straw")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Exodus 5:1–12 — Let My People Go", "300px minmax(0, 1fr) 300px", body, 1)
PAGES["EX2-P01-LetGo"] = p01

# ───────────────────────── 02 · Rod Against Rod (7:10–13) ─────────────────────────
def p02():
    s1 = f'''      {defs("s1", "Man", "ManUp", "Robe")}
      {X.columns([20, 640], -10, 290, 40, color="#3A0E0E")}
      <path d="M-10 290 L 712 290 L 712 334 L -10 334 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>
      <g stroke="#5A3A22" stroke-width="1.4"><path d="M-10 306 L 712 306 M100 290 L 80 334 M260 290 L 250 334 M420 290 L 430 334 M580 290 L 600 334"></path></g>
      <rect x="520" y="150" width="110" height="140" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></rect><rect x="534" y="164" width="82" height="70" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="2"></rect>
      {person("s1", 575, 290, 0.66, body="#5A2A16", cloth="#F3EFE6", extra=NEMES)}
      {person("s1", 470, 296, 0.5, body="#3A1A10", extra=KILT)}{person("s1", 680, 300, 0.5, body="#3A1A10", extra=KILT)}
      {person("s1", 120, 314, 0.86, body="#5A3A22", cloth="#4A6A9A", flip=True, up=[(-22, -158), (-62, -150), (-100, -136)])}
      {person("s1", 50, 318, 0.86, body="#5A3A22", cloth="#E2D8C4")}
      {X.serpent([(190, 312), (250, 300), (300, 318), (350, 300), (380, 260), (372, 220)], 14, "s1s", head_scale=1.0)}'''
    o1 = (cap("And Moses and Aaron went in unto Pharaoh, … and Aaron cast down his rod before Pharaoh and before his servants, and it became a serpent.", "left: 12px; top: 12px", maxw=430)
          + sfx("シュルル", "SHURURU", "left: 250px; top: 150px", size=34, fill="#3F8A44", stroke="#F3EFE6", rot=-6, tagbg="#0D0D0F", tagfg="#F3EFE6", align="flex-start")
          + stamp(7, "right: 16px; top: 14px", rot=-4))
    P1 = panel("linear-gradient(180deg, #5A1A16 0%, #B5652E 100%)", 702, 324, s1, o1, "1 · Aaron's rod")

    s2 = f'''      {face(FX["__FACE_MAGICIAN__"], -46, -20, 0.74)}'''
    o2 = cap("Then Pharaoh also called for the wise men and the sorcerers: and they also, the magicians of Egypt, did in like manner with their enchantments.", "right: 10px; bottom: 10px", size=10, maxw=200)
    P2a = panel("radial-gradient(circle at 70% 30%, #B07AE8 0 30px, #4A1D55 180px, #12113A 320px)", 342, 282, s2, o2, "2a · The magicians")
    s3 = f'''      <path d="M-10 170 L 352 170 L 352 292 L -10 292 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>
      {X.serpent([(10, 250), (70, 236), (120, 256), (170, 240)], 9, "s3a", brown=True)}
      {X.serpent([(330, 210), (270, 200), (220, 218), (170, 200)], 8, "s3b", brown=True)}
      {X.serpent([(120, 286), (190, 272), (250, 290), (320, 270)], 10, "s3c", brown=True)}'''
    o3 = cap("For they cast down every man his rod, and they became serpents:", "left: 10px; right: 10px; top: 10px", size=10.5)
    P2b = panel("linear-gradient(180deg, #4A1D55 0%, #B5652E 100%)", 342, 282, s3, o3, "2b · Every man his rod")

    s4 = f'''      {speed(500, 170, 70, 120, 800, 9, color="#FFF4C2", sw=1.6, op=0.6)}
      <path d="M-10 300 L 712 300 L 712 384 L -10 384 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>
      {X.serpent([(712, 60), (660, 96), (610, 118), (560, 126), (520, 132)], 13, "s4b", brown=True)}
      {X.serpent([(30, 350), (140, 318), (240, 352), (340, 318), (420, 250), (452, 210)], 26, "s4g", head_scale=1.9)}'''
    o4 = (cap("but Aaron's rod swallowed up their rods.", "left: 12px; top: 12px", size=13)
          + sfx("ゴクリ", "GOKURI", "left: 330px; top: 60px", size=58, fill="#F3EFE6", stroke="#0D0D0F", rot=-8)
          + cap("And Pharaoh's heart was hardened, and he hearkened not unto them; as Jehovah had spoken.", "right: 12px; bottom: 12px", maxw=360))
    P3 = panel("radial-gradient(circle at 70% 45%, #FFE680 0 40px, #FF8A3D 200px, #5A1A16 480px)", 702, 374, s4, o4, "3 · Swallowed up")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Exodus 7:10–13 — Rod Against Rod", "330px minmax(0, 1fr) 380px", body, 2)
PAGES["EX2-P02-Rods"] = p02

# ───────────────────────── 03 · Blood (7:20–24) ─────────────────────────
def p03():
    s1 = f'''      {defs("b1", "Man", "ManUp", "Robe")}
      <path d="M-10 180 C 200 170 500 186 712 176 L 712 284 L -10 284 Z" fill="#2C9DB8"></path>
      <path d="M-10 230 C 80 214 180 220 260 240 L 260 284 L -10 284 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M520 190 C 600 180 660 184 712 180 L 712 200 L 520 200 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="1.6"></path>
      {person("b1", 600, 196, 0.24, body="#2A140C", cloth="#F3EFE6", extra=NEMES)}{person("b1", 630, 196, 0.2, body="#2A140C", extra=KILT)}{person("b1", 652, 196, 0.2, body="#2A140C", extra=KILT)}{person("b1", 676, 196, 0.2, body="#2A140C", extra=KILT)}
      {person("b1", 70, 250, 0.62, body="#5A3A22", cloth="#E2D8C4")}
      {person("b1", 170, 252, 0.66, body="#5A3A22", cloth="#4A6A9A", flip=True, up=ARM_UP, extra=ROD_UP)}
      <g fill="#8FE3EE" stroke="#0D0D0F" stroke-width="1.4"><path d="M290 236 C 296 200 306 190 312 176 C 316 196 312 214 300 236 Z"></path><path d="M310 238 C 330 214 344 206 356 200 C 350 220 334 232 316 240 Z"></path><path d="M276 238 C 262 216 256 206 246 196 C 262 204 274 220 284 238 Z"></path></g>
      <ellipse cx="296" cy="240" rx="40" ry="8" fill="#D7261E" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'''
    o1 = (cap("And Moses and Aaron did so, as Jehovah commanded; and he lifted up the rod, and smote the waters that were in the river, in the sight of Pharaoh, and in the sight of his servants;", "left: 12px; top: 12px", maxw=440)
          + sfx("バシャッ", "BASHA!", "left: 360px; top: 160px", size=36, fill="#F3EFE6", stroke="#0F4C68", rot=-6, align="flex-start"))
    P1 = panel("linear-gradient(180deg, #FFC98A 0%, #FFE3B8 55%)", 702, 274, s1, o1, "1 · He smote the waters")

    fishes = "".join(X.fish(x, y, s, rot=rr) for x, y, s, rr in [(80, 300, 0.7, 180), (210, 340, 0.9, 170), (360, 290, 0.6, 195), (470, 350, 1.0, 175), (600, 310, 0.75, 188), (300, 380, 0.8, 182), (140, 392, 0.65, 176), (640, 384, 0.7, 170)])
    s2 = f'''      {egypt.pyramid(520, 210, 260, 150, lit="#5A1A2A", dark="#2A0A14", line="#3A0E1E", n=8)}
      {egypt.pyramid(660, 214, 160, 90, lit="#5A1A2A", dark="#2A0A14", line="#3A0E1E", n=6)}
      <path d="M-10 210 L 712 210 L 712 422 L -10 422 Z" fill="#8A0E16" stroke="#0D0D0F" stroke-width="2"></path>
      <g fill="none" stroke="#FF4B3E" stroke-width="3" opacity="0.8"><path d="M-10 240 C 80 226 160 252 240 236 C 320 222 400 248 480 234 C 560 222 640 244 712 232"></path><path d="M-10 280 C 100 262 200 290 300 272 C 400 256 500 284 600 268 L 712 262"></path></g>
      <g fill="none" stroke="#3A0408" stroke-width="2.4" opacity="0.7"><path d="M40 326 C 120 316 200 336 280 324"></path><path d="M360 340 C 440 328 520 348 600 336"></path><path d="M120 410 C 200 398 300 414 380 404"></path></g>
      {fishes}'''
    o2 = (cap("and all the waters that were in the river were turned to blood.", "left: 12px; top: 12px", size=13, maxw=360)
          + cap("And the fish that were in the river died; and the river became foul, and the Egyptians could not drink water from the river; and the blood was throughout all the land of Egypt.", "right: 12px; bottom: 12px", maxw=400)
          + sfx("ドロッ", "DORO", "left: 30px; top: 160px", size=54, fill="#D7261E", stroke="#F3EFE6", rot=-8, align="flex-start"))
    P2 = panel("linear-gradient(180deg, #2A0A14 0%, #7A0E1E 40%, #D7261E 52%)", 702, 412, s2, o2, "2 · Turned to blood")

    s3 = f'''      {defs("b3", "Man", "Robe")}
      <rect x="0" y="0" width="342" height="294" fill="#2A140C"></rect>
      <path d="M110 300 L 110 90 C 110 50 232 50 232 90 L 232 300 Z" fill="#FFC14D" stroke="#0D0D0F" stroke-width="3"></path>
      <rect x="96" y="60" width="150" height="20" fill="#5A1A16" stroke="#0D0D0F" stroke-width="2"></rect>
      {person("b3", 171, 284, 0.84, body="#12090A", cloth="#3A2214", stroke="#0D0D0F", extra=NEMES.replace("#E8B830", "#3A2A0E").replace("#1F5FAD", "#12090A"))}'''
    o3 = cap("And Pharaoh turned and went into his house, neither did he lay even this to heart.", "left: 10px; right: 10px; bottom: 10px", size=10.5) + ref("EX 7:23", "right: 10px; top: 8px")
    P3a = panel("#2A140C", 342, 294, s3, o3, "3a · Pharaoh turned")

    diggers = "".join(person("b4", x, y, s, body="#5A2A16", flip=fl, up=[(-22, -158), (-50, -200), (-60, -244)],
                             extra=KILT + '<path d="M-60 -244 L -36 -60" stroke="#3A2214" stroke-width="6" stroke-linecap="round"></path><path d="M-46 -66 L -24 -54 L -30 -44 Z" fill="#8A8478" stroke="#0D0D0F" stroke-width="2"></path>')
                      for x, y, s, fl in [(70, 250, 0.5, False), (190, 262, 0.56, True), (290, 244, 0.46, False)])
    s4 = f'''      {defs("b4", "Man", "ManUp")}
      <path d="M-10 170 L 352 160 L 352 304 L -10 304 Z" fill="#C8783E" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M-10 150 L 352 140 L 352 166 L -10 176 Z" fill="#8A0E16"></path>
      <g fill="#7A3E22" stroke="#0D0D0F" stroke-width="1.6"><ellipse cx="110" cy="262" rx="30" ry="9"></ellipse><ellipse cx="236" cy="272" rx="34" ry="10"></ellipse></g>
      {diggers}'''
    o4 = cap("And all the Egyptians digged round about the river for water to drink; for they could not drink of the water of the river.", "left: 10px; right: 10px; top: 10px", size=10)
    P3b = panel("linear-gradient(180deg, #FF8A3D, #FFC98A)", 342, 294, s4, o4, "3b · They digged")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Exodus 7:20–24 — The River Turned to Blood", "280px minmax(0, 1fr) 300px", body, 3)
PAGES["EX2-P03-Blood"] = p03

# ───────────────────────── 04 · Frogs, Lice, Flies (8:6–24) ─────────────────────────
def p04():
    s1 = f'''      <rect x="0" y="0" width="702" height="334" fill="#C8A06A"></rect>
      <path d="M0 210 L 702 210 L 702 334 L 0 334 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>
      <g stroke="#0D0D0F" stroke-width="2.4"><rect x="380" y="150" width="280" height="40" fill="#F3EFE6"></rect><path d="M392 190 L 392 230 M648 190 L 648 230" stroke-width="7"></path><rect x="380" y="128" width="40" height="26" fill="#E8B830"></rect></g>
      <rect x="60" y="170" width="150" height="50" fill="#B5652E" stroke="#0D0D0F" stroke-width="2.4"></rect><ellipse cx="135" cy="172" rx="70" ry="10" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2"></ellipse>
      {X.frogs(12, 400, 660, 150, 190, 21, 0.5, 0.7)}
      {X.frogs(8, 70, 200, 150, 172, 22, 0.45, 0.6)}
      {X.frogs(46, -10, 712, 220, 330, 23, 0.7, 1.5)}'''
    o1 = (cap("And Aaron stretched out his hand over the waters of Egypt; and the frogs came up, and covered the land of Egypt.", "left: 12px; top: 12px", maxw=400)
          + sfx("ゲコゲコ", "GEKO GEKO", "right: 20px; top: 40px", size=40, fill="#3F8A44", stroke="#F3EFE6", rot=6, tagbg="#0D0D0F", tagfg="#F3EFE6")
          + stamp(8, "left: 16px; bottom: 14px", rot=-4))
    P1 = panel("#C8A06A", 702, 334, s1, o1, "1 · Frogs")

    s2 = f'''      {defs("f2", "Man", "ManUp", "Robe")}
      <path d="M-10 250 L 352 250 L 352 342 L -10 342 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      <ellipse cx="200" cy="250" rx="90" ry="40" fill="#A88A5A" opacity="0.8"></ellipse>
      {X.lice(700, 60, 342, 120, 330, 8)}
      {person("f2", 90, 300, 0.74, body="#5A3A22", cloth="#4A6A9A", flip=True, up=[(-22, -158), (-70, -120), (-110, -60)],
              extra='<path d="M-110 -60 L -180 60" stroke="#0D0D0F" stroke-width="11" stroke-linecap="round"></path><path d="M-110 -60 L -180 60" stroke="#8A5A30" stroke-width="7" stroke-linecap="round"></path>')}'''
    o2 = (cap("And Aaron stretched out his hand with his rod, and smote the dust of the earth, and there were lice upon man, and upon beast;", "left: 10px; right: 10px; top: 10px", size=10)
          + ref("EX 8:17", "right: 10px; bottom: 8px", color="#0D0D0F", bg="#F3EFE6"))
    P2a = panel("linear-gradient(180deg, #E8B070, #C8783E)", 342, 332, s2, o2, "2a · Lice")
    s3 = f'''      {face(FX["__FACE_MAGICIAN_FEAR__"], -70, 10, 0.8)}
      {X.lice(90, 0, 342, 0, 332, 9)}'''
    o3 = (cap("Then the magicians said unto Pharaoh,", "left: 10px; top: 10px", size=10)
          + tail(118, 196, "l")
          + balloon("This is the finger of God:", "left: 156px; top: 132px", 176, size=17, pad="18px 16px")
          + cap("and Pharaoh's heart was hardened.", "right: 10px; bottom: 10px", size=10, maxw=170))
    P2b = panel("radial-gradient(circle at 80% 40%, #FFE680 0 20px, #7A3BA8 160px, #2A1A5E 320px)", 342, 332, s3, o3, "2b · The finger of God")

    s4 = f'''      <circle cx="640" cy="70" r="40" fill="#FFF4C2"></circle>
      <path d="M560 200 C 620 192 680 196 712 194 L 712 314 L 560 314 Z" fill="#9CCB5E" stroke="#0D0D0F" stroke-width="2"></path>
      <g stroke="#0D0D0F" stroke-width="2"><rect x="590" y="166" width="40" height="34" fill="#E8C88A"></rect><rect x="644" y="172" width="34" height="28" fill="#E8C88A"></rect></g>
      <path d="M-10 230 L 560 230 L 560 314 L -10 314 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>
      <rect x="60" y="110" width="420" height="130" fill="#B5652E" stroke="#0D0D0F" stroke-width="2.4"></rect>
      {X.columns([90, 180, 270, 360, 440], 120, 240, 24, color="#7A3E22")}
      <rect x="40" y="96" width="460" height="22" fill="#5A1A16" stroke="#0D0D0F" stroke-width="2"></rect>
      <ellipse cx="280" cy="160" rx="320" ry="150" fill="#12090A" opacity="0.35"></ellipse>
      {X.swarm(420, 280, 150, 300, 150, 31, 0.4, 1.3)}
      {X.swarm(26, 300, 280, 280, 30, 32, 1.4, 2.4)}'''
    o4 = (cap("And Jehovah did so; and there came grievous swarms of flies into the house of Pharaoh, and into his servants' houses: and in all the land of Egypt the land was corrupted by reason of the swarms of flies.", "left: 12px; top: 12px", maxw=430)
          + sfx("ブウウン", "BUUUN", "left: 380px; top: 210px", size=38, fill="#12090A", stroke="#F3EFE6", rot=-4, align="flex-start")
          + ref("GOSHEN", "right: 14px; bottom: 12px", color="#0D0D0F", bg="#F3EFE6"))
    P3 = panel("linear-gradient(180deg, #8A6A4A 0%, #C8A06A 50%, #FFE3B8 80%)", 702, 314, s4, o4, "3 · Swarms of flies")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Exodus 8:6–24 — Frogs, Lice and Flies", "340px minmax(0, 1fr) 320px", body, 4)
PAGES["EX2-P04-Frogs"] = p04

# ───────────────────────── 05 · Murrain, Boils, Hail (9:6–24) ─────────────────────────
def p05():
    vult = "".join(f'<path d="M{x} {y} C {x+8} {y-10} {x+16} {y-10} {x+22} {y-2} C {x+28} {y-10} {x+36} {y-10} {x+44} {y}" fill="none" stroke="#12090A" stroke-width="3" stroke-linecap="round"></path>' for x, y in [(60, 70), (150, 50), (230, 84)])
    s1 = f'''      {vult}
      <path d="M-10 140 C 100 130 240 146 352 136 L 352 294 L -10 294 Z" fill="#B8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {X.kine_dead(70, 186, 0.7, color="#6B5A4A")}{X.kine_dead(190, 200, 0.85, color="#8A7A6A", flip=True)}{X.kine_dead(290, 180, 0.6, color="#9A8A7A")}'''
    o1 = (cap("And Jehovah did that thing on the morrow; and all the cattle of Egypt died; but of the cattle of the children of Israel died not one.", "left: 10px; right: 10px; bottom: 10px", size=10)
          + stamp(9, "right: 12px; top: 12px"))
    P1a = panel("linear-gradient(180deg, #FF9A6B, #FFC98A)", 342, 284, s1, o1, "1a · The murrain")
    s2 = f'''      {defs("m2", "Man", "ManUp", "Robe")}
      <g fill="#8A8478" opacity="0.8">{"".join(f'<circle cx="{x}" cy="{y}" r="{r}"></circle>' for x, y, r in [(150, 60, 22), (180, 40, 18), (210, 70, 20), (120, 90, 16), (240, 40, 14), (170, 100, 12), (230, 104, 10)])}</g>
      {X.lice(160, 100, 280, 20, 140, 12, color="#5A5650")}
      <path d="M-10 230 L 352 222 L 352 294 L -10 294 Z" fill="#7A3E22" stroke="#0D0D0F" stroke-width="2"></path>
      {person("m2", 120, 262, 0.7, body="#5A3A22", cloth="#E2D8C4", flip=True, up=[(-22, -158), (-40, -210), (-26, -262)])}'''
    o2 = cap("and Moses sprinkled it up toward heaven; and it became a boil breaking forth with blains upon man and upon beast.", "left: 10px; right: 10px; bottom: 10px", size=10) + ref("EX 9:10", "right: 10px; top: 8px", color="#0D0D0F", bg="#F3EFE6")
    P1b = panel("linear-gradient(180deg, #5A5650, #C8A06A)", 342, 284, s2, o2, "1b · Ashes of the furnace")

    s3 = f'''      {face(FX["__FACE_MAGICIAN_BOILS__"], -30, -60, 0.9)}'''
    o3 = cap("And the magicians could not stand before Moses because of the boils; for the boils were upon the magicians, and upon all the Egyptians.", "right: 14px; top: 50%; transform: translateY(-50%)", size=12, maxw=380)
    P2 = panel("linear-gradient(90deg, #7A3BA8 0%, #2A1A5E 60%)", 702, 244, s3, o3, "2 · The boils")

    fires = "".join(E.flame(x, 444, 18, 60 + (i % 3) * 20, (-1) ** i * 6) for i, x in enumerate(range(240, 712, 34)))
    s4 = f'''      {defs("m4", "Man", "ManUp", "Robe")}
      {X.bolt(420, -10, 300, 3, w=1.3)}{X.bolt(620, -10, 220, 8, w=0.9)}
      {X.hail(70, 160, 712, 40, 430, 13)}
      <path d="M-10 452 L -10 330 C 60 300 140 300 220 330 C 280 360 400 390 712 400 L 712 462 Z" fill="#2A140C" stroke="#0D0D0F" stroke-width="2"></path>
      {fires}
      {person("m4", 120, 316, 0.9, body="#12090A", cloth="#2A1A2E", stroke="#FFD23F", sw=2.4, up=ARM_UP, extra=ROD_UP)}'''
    o4 = (cap("And Moses stretched forth his rod toward heaven: and Jehovah sent thunder and hail, and fire ran down unto the earth;", "left: 12px; top: 12px", maxw=330)
          + sfx("ゴロゴロ", "GORO GORO", "right: 20px; top: 20px", size=40, fill="#FFF4C2", stroke="#12113A", rot=6, tagbg="#FFF4C2", tagfg="#12113A")
          + cap("So there was hail, and fire mingled with the hail, very grievous, such as had not been in all the land of Egypt since it became a nation.", "right: 12px; bottom: 12px", maxw=330))
    P3 = panel("linear-gradient(180deg, #0B0A24 0%, #2A1A5E 60%, #7A2A5A 100%)", 702, 452, s4, o4, "3 · Hail and fire")
    body = cols(P1a, P1b) + P2 + P3
    return mk.page("Exodus 9:6–24 — Murrain, Boils and Hail", "290px 250px minmax(0, 1fr)", body, 5)
PAGES["EX2-P05-Hail"] = p05

# ───────────────────────── 06 · Locusts (10:3–16) ─────────────────────────
def p06():
    s1 = f'''      {face(FX["__FACE_MOSES_STERN__"], -40, -44, 0.78)}'''
    o1 = (tail(148, 136, "l")
          + balloon("Thus saith Jehovah, the God of the Hebrews, How long wilt thou refuse to humble thyself before me? let my people go, that they may serve me.", "left: 186px; top: 30px", 380, size=16, pad="22px 34px")
          + stamp(10, "right: 16px; bottom: 14px"))
    P1 = panel("radial-gradient(circle at 15% 50%, #FF6A4A 0 30px, #B5421E 180px, #3A0E0E 440px)", 702, 264, s1, o1, "1 · How long?")

    trees = "".join(f'<path d="M{x} 400 L {x} 330 M{x} 352 L {x-18} 328 M{x} 344 L {x+16} 320" stroke="#3A2214" stroke-width="4" stroke-linecap="round"></path>' for x in (70, 180, 300))
    wind = "".join(f'<path d="M{-10} {y} C 200 {y-14} 400 {y+10} 712 {y-6}" fill="none" stroke="#F3EFE6" stroke-width="1.4" opacity="0.4"></path>' for y in range(80, 340, 36))
    s2 = f'''      {defs("l2", "Man", "ManUp", "Robe")}
      {wind}
      <path d="M-10 370 C 200 360 400 376 712 366 L 712 442 L -10 442 Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2"></path>
      {trees}
      {person("l2", 520, 400, 0.22, body="#2A140C", extra=KILT, up=[(-22, -158), (-40, -210), (-30, -250)])}{person("l2", 560, 404, 0.2, body="#2A140C", extra=KILT)}
      {X.locusts(150, -10, 712, 60, 380, 41, 0.12, 0.42)}
      {X.locusts(12, -10, 712, 120, 420, 42, 0.8, 1.5)}'''
    o2 = (cap("And Moses stretched forth his rod over the land of Egypt, and Jehovah brought an east wind upon the land all that day, and all the night; and when it was morning, the east wind brought the locusts.", "left: 12px; top: 12px", maxw=440)
          + cap("For they covered the face of the whole earth, so that the land was darkened; … and there remained not any green thing, either tree or herb of the field, through all the land of Egypt.", "right: 12px; bottom: 12px", maxw=390)
          + sfx("ザザザザ", "ZAZAZAZA", "right: 16px; top: 120px", size=44, fill="#F3EFE6", stroke="#3A2214", rot=6))
    P2 = panel("linear-gradient(180deg, #3A2A1A 0%, #8A6A3A 60%, #C8A06A 100%)", 702, 432, s2, o2, "2 · The locusts")

    s3 = f'''      <path d="M200 300 C 196 220 204 140 190 40" fill="none" stroke="#6B5A3A" stroke-width="8" stroke-linecap="round"></path>
      {X.locust(170, 150, 3.0, rot=-8, flip=True)}'''
    o3 = ref("EX 10:15", "left: 10px; bottom: 8px")
    P3a = panel("radial-gradient(circle at 50% 45%, #E8C88A 0 40px, #8A6A3A 200px, #3A2A1A 340px)", 342, 284, s3, o3, "3a · No green thing")
    s4 = f'''      {face(FX["__FACE_PHARAOH_FEAR__"], 400, 6, 0.74, flip=True)}'''
    o4 = (cap("Then Pharaoh called for Moses and Aaron in haste; and he said,", "left: 10px; top: 10px", size=10, maxw=200)
          + tail(194, 176, "r")
          + balloon("I have sinned against Jehovah your God, and against you.", "left: 10px; top: 106px", 196, size=14, pad="20px 20px"))
    P3b = panel("linear-gradient(180deg, #8A6A3A, #3A2A1A)", 342, 284, s4, o4, "3b · I have sinned")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Exodus 10:3–16 — The Locusts", "270px minmax(0, 1fr) 290px", body, 6)
PAGES["EX2-P06-Locusts"] = p06

# ───────────────────────── 07 · Darkness (10:21–29) ─────────────────────────
def p07():
    ghosts = "".join(person("d1", x, y, s, body="none", stroke="#3A3A4A") .replace('fill="none"><use', 'fill="none" stroke="#2A2A3A" stroke-width="3"><use') for x, y, s in [(140, 330, 0.7), (300, 320, 0.6), (520, 334, 0.75)])
    s1 = f'''      {defs("d1", "Man")}
      {ghosts}'''
    o1 = (cap("And Moses stretched forth his hand toward heaven; and there was a thick darkness in all the land of Egypt three days;", "left: 12px; top: 12px", maxw=400)
          + cap("they saw not one another, neither rose any one from his place for three days:", "right: 12px; bottom: 12px", maxw=340)
          + sfx("シーン", "SHIIN", "left: 300px; top: 150px", size=52, fill="#12121A", stroke="#3A3A4A", rot=0, tagbg="#2A2A3A", tagfg="#8A8A9A", align="flex-start")
          + ref("EX 10:22–23", "left: 12px; bottom: 9px", color="#5A5A6A"))
    P1 = panel("#050508", 702, 354, s1, o1, "1 · Darkness which may be felt")

    houses = ""
    for i, (x, w, h) in enumerate([(40, 90, 60), (160, 70, 50), (260, 110, 70), (400, 80, 54), (510, 100, 64), (630, 60, 46)]):
        y = 200 - h
        houses += (f'<circle cx="{x + w/2}" cy="{y + h/2}" r="{w}" fill="#FFC14D" opacity="0.18"></circle>'
                   f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#3A2A1E" stroke="#0D0D0F" stroke-width="2"></rect>'
                   f'<rect x="{x + w*0.2}" y="{y + h*0.3}" width="{w*0.22}" height="{h*0.3}" fill="#FFE680" stroke="#0D0D0F" stroke-width="1.4"></rect>'
                   f'<rect x="{x + w*0.58}" y="{y + h*0.45}" width="{w*0.24}" height="{h*0.55}" fill="#FFC14D" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    s2 = f'''      <path d="M-10 200 L 712 200 L 712 254 L -10 254 Z" fill="#1A120E"></path>
      {houses}'''
    o2 = cap("but all the children of Israel had light in their dwellings.", "left: 50%; top: 12px; transform: translateX(-50%)", size=12, center=True)
    P2 = panel("linear-gradient(180deg, #050508 0%, #1A1220 100%)", 702, 244, s2, o2, "2 · Light in Goshen")

    s3 = f'''      {face(FX["__FACE_PHARAOH_NEW__"], -70, 10, 0.86)}'''
    o3 = (cap("And Pharaoh said unto him,", "left: 10px; top: 10px", size=10)
          + tail(146, 210, "ul")
          + balloon("Get thee from me, take heed to thyself, see my face no more; for in the day thou seest my face thou shalt die.", "left: 100px; top: 244px", 236, size=12, pad="20px 26px"))
    P3a = panel("radial-gradient(circle at 30% 40%, #FF6A4A 0 20px, #8A1A1A 200px, #1A0408 360px)", 342, 382, s3, o3, "3a · See my face no more")
    s4 = f'''      {face(FX["__FACE_MOSES_STERN__"], 412, 10, 0.86, flip=True)}'''
    o4 = (tail(160, 210, "ur")
          + balloon("Thou hast spoken well; I will see thy face again no more.", "left: 8px; top: 246px", 236, size=14, pad="20px 26px")
          + ref("EX 10:28–29", "right: 10px; top: 8px"))
    P3b = panel("radial-gradient(circle at 70% 40%, #FFE680 0 20px, #B5421E 200px, #1A0408 360px)", 342, 382, s4, o4, "3b · Thou hast spoken well")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Exodus 10:21–29 — Darkness", "360px 250px minmax(0, 1fr)", body, 7)
PAGES["EX2-P07-Darkness"] = p07

# ───────────────────────── 08 · One Plague More (11:1–8) ─────────────────────────
def p08():
    s1 = f'''      {stars(140, 702, 254, 51)}
      <circle cx="600" cy="80" r="44" fill="#F3EFE6"></circle><circle cx="618" cy="70" r="40" fill="#0B0A24"></circle>'''
    o1 = (cap("And Jehovah said unto Moses,", "left: 12px; top: 12px")
          + god("Yet one plague more will I bring upon Pharaoh, and upon Egypt; afterwards he will let you go hence:", "left: 12px; top: 60px", size=22, maxw=480)
          + stamp(11, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(180deg, #0B0A24, #2A1A5E)", 702, 254, s1, o1, "1 · One plague more")

    s2 = f'''      {speed(160, 260, 80, 200, 900, 19, color="#0D0D0F", sw=2, op=0.5)}
      {face(FX["__FACE_MOSES_STERN__"], -60, 10, 1.05)}'''
    o2 = (cap("And Moses said,", "left: 12px; top: 12px")
          + tail(192, 254, "l")
          + balloon("Thus saith Jehovah, About midnight will I go out into the midst of Egypt: and all the first-born in the land of Egypt shall die, from the first-born of Pharaoh that sitteth upon his throne, even unto the first-born of the maid-servant that is behind the mill; and all the first-born of cattle.", "left: 226px; top: 40px", 466, size=14.5, pad="44px 58px")
          + ref("EX 11:4–5", "right: 12px; bottom: 9px"))
    P2 = panel("radial-gradient(circle at 20% 55%, #FF6A4A 0 40px, #8A0E16 240px, #1A0408 480px)", 702, 432, s2, o2, "2 · About midnight")

    s3 = f'''      <circle cx="250" cy="90" r="60" fill="#D7261E"></circle><circle cx="250" cy="90" r="80" fill="#D7261E" opacity="0.25"></circle>
      {stars(40, 342, 160, 61)}
      {egypt.pyramid(110, 230, 170, 110, lit="#2A0A14", dark="#12040A", line="#3A0E1E", n=6)}
      <g fill="#12040A" stroke="#3A0E1E" stroke-width="1.6"><rect x="190" y="170" width="60" height="70"></rect><rect x="250" y="190" width="50" height="50"></rect><rect x="296" y="160" width="40" height="80"></rect><rect x="-10" y="200" width="60" height="40"></rect></g>
      <g fill="#FFC14D"><rect x="206" y="190" width="8" height="12"></rect><rect x="310" y="180" width="8" height="12"></rect></g>
      <path d="M-10 240 L 352 240 L 352 304 L -10 304 Z" fill="#0B0408"></path>'''
    o3 = balloon("And there shall be a great cry throughout all the land of Egypt, such as there hath not been, nor shall be any more.", "left: 10px; bottom: 10px", 230, size=12.5, pad="18px 22px") + ref("EX 11:6", "right: 10px; bottom: 8px")
    P3a = panel("linear-gradient(180deg, #0B0A24 0%, #3A0E1E 100%)", 342, 294, s3, o3, "3a · A great cry")
    s4 = f'''      {defs("o4", "Man", "Robe")}
      <rect x="0" y="0" width="342" height="294" fill="#1A0408"></rect>
      <path d="M90 300 L 90 70 C 90 30 252 30 252 70 L 252 300 Z" fill="#D7261E" stroke="#0D0D0F" stroke-width="3"></path>
      {X.columns([40, 266], -10, 300, 36, color="#3A0E0E")}
      {person("o4", 171, 286, 0.92, body="#12090A", cloth="#2A1A10", stroke="#FF6A4A", sw=2.4)}'''
    o4 = (cap("And he went out from Pharaoh in hot anger.", "left: 10px; right: 10px; top: 10px", size=11, center=True)
          + '    <span style="position: absolute; right: 10px; bottom: 7px; font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">つづく · TO BE CONTINUED</span>\n')
    P3b = panel("#1A0408", 342, 294, s4, o4, "3b · In hot anger")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Exodus 11:1–8 — One Plague More", "260px minmax(0, 1fr) 300px", body, 8)
PAGES["EX2-P08-Midnight"] = p08


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "exodus/project"))
