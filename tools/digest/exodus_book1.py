"""Exodus Book One — The Bush That Burned (Exodus 1–4). Writes the .dc.html pages into the given folder.
Usage: python3 exodus_book1.py <out_dir>"""
import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1] / "kit"))  # shared drawing kit
import sys, pathlib, random
import mk, exodus as E, faces_ex, snake
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, speed, stars
FX = faces_ex.tokens()
PAGES = {}

# ───────────────────────── Cover ─────────────────────────
def cover():
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {defs("c1", "Man", "Robe")}
    <defs><radialGradient id="c1Glow" cx="470" cy="800" r="420" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFF4C2"></stop><stop offset="0.18" stop-color="#FFC14D" stop-opacity="0.85"></stop><stop offset="0.5" stop-color="#FF6A2A" stop-opacity="0.35"></stop><stop offset="1" stop-color="#FF6A2A" stop-opacity="0"></stop></radialGradient></defs>
    {stars(150, 760, 560, 11)}
    <path d="M-10 640 L 120 520 L 210 580 L 330 430 L 420 500 L 520 380 L 640 470 L 770 400 L 770 1090 L -10 1090 Z" fill="#2A1A3E" stroke="#0D0D0F" stroke-width="2"></path>
    <rect width="760" height="1080" fill="url(#c1Glow)"></rect>
    {speed(470, 800, 60, 230, 900, 5, color="#FFE680", sw=1.2, op=0.35)}
    <path d="M-10 900 C 120 880 260 860 400 880 C 520 896 640 870 770 880 L 770 1090 L -10 1090 Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="2.4"></path>
    <path d="M-10 900 C 120 880 260 860 400 880 C 520 896 640 870 770 880" fill="none" stroke="#FF8A3D" stroke-width="3" opacity="0.7"></path>
    {E.bush(480, 896, 300, 360, 21)}
    {person("c1", 170, 930, 1.15, body="#1A0E0A", cloth="#2A1A2E", stroke="#FF8A3D", sw=2.4)}
    <path d="M206 742 L 222 930" stroke="#1A0E0A" stroke-width="5" stroke-linecap="round"></path>
    <path d="M206 742 C 200 726 214 718 220 730" fill="none" stroke="#1A0E0A" stroke-width="5" stroke-linecap="round"></path>
    <g fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.6"><path d="{E.SANDAL}" transform="translate(96 948) rotate(-70) scale(0.7)"></path><path d="{E.SANDAL}" transform="translate(112 962) rotate(-58) scale(0.7)"></path></g>
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The Book of</span>
    <span>No. 01</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 168px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6">EXODUS</h1>
  <div style="position: absolute; top: 246px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 262px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book One — The Bush That Burned</span>
    <span style="font-weight: 500; opacity: 0.75">Chapters 1 – 4</span>
  </div>
  <div style="position: absolute; top: 236px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>出</span><span>エ</span><span>ジ</span><span>プ</span><span>ト</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">SHUTSU</span>
  </div>
  <div style="position: absolute; left: 38px; top: 380px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 12px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 240px; line-height: 1.45">And the bush was not consumed.</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 1</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #0B0A24 0%, #12113A 30%, #2A1A5E 52%, #7A2A5A 70%, #B5421E 100%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Exodus Book One — Cover", None, body, root_style=root)
PAGES["Main"] = cover

# ───────────────────────── 01 · A New King (1:8–14) ─────────────────────────
def p01():
    # panel 1: the new king
    s1 = f'''      <g stroke="#0D0D0F" stroke-width="2"><rect x="430" y="-10" width="46" height="344" fill="#5A1A16"></rect><rect x="560" y="-10" width="46" height="344" fill="#5A1A16"></rect><rect x="690" y="-10" width="46" height="344" fill="#5A1A16"></rect></g>
      <g fill="none" stroke="#E8B830" stroke-width="2" opacity="0.6"><path d="M430 60 L 476 60 M430 70 L 476 70 M560 60 L 606 60 M560 70 L 606 70 M690 60 L 736 60 M690 70 L 736 70"></path></g>
      {face(FX["__FACE_PHARAOH_NEW__"], -30, -40, 1.0)}'''
    o1 = (cap("Now there arose a new king over Egypt, who knew not Joseph.", "left: 12px; bottom: 12px", maxw=250)
          + tail(262, 150, "l")
          + balloon("Behold, the people of the children of Israel are more and mightier than we: come, let us deal wisely with them, lest they multiply.", "left: 298px; top: 30px", 360, size=15, pad="24px 34px")
          + stamp(1, "right: 16px; bottom: 14px"))
    P1 = panel("radial-gradient(circle at 20% 50%, #FF6A4A 0 40px, #B5421E 180px, #3A0E0E 420px)", 702, 324, s1, o1, "1 · The new king")

    # panel 2: store-cities — slaves hauling bricks up a ramp
    r = random.Random(4)
    hauling = []
    for i in range(9):
        t = i / 8; x = 120 + t * 470; y = 330 - t * 190; sc = 0.26 - t * 0.08
        hauling.append(person("p2", f"{x:.0f}", f"{y:.0f}", f"{sc:.2f}", body="#2A140C", cloth="#C9A86A", kind="Tunic", sw=4,
                              extra='<rect x="-26" y="-232" width="52" height="26" fill="#B5652E" stroke="#0D0D0F" stroke-width="4"></rect>'))
    s2 = f'''      {defs("p2", "Man", "ManUp", "Tunic", "Robe")}
      <defs><pattern id="p2Brick" width="40" height="20" patternUnits="userSpaceOnUse"><rect width="40" height="20" fill="#C8783E"></rect><path d="M0 0 L 40 0 M0 10 L 40 10 M10 0 L 10 10 M30 10 L 30 20" stroke="#7A3E22" stroke-width="1.6"></path></pattern></defs>
      <circle cx="600" cy="70" r="46" fill="#FFF4C2"></circle>
      <path d="M380 362 L 380 120 L 702 60 L 702 362 Z" fill="url(#p2Brick)" stroke="#0D0D0F" stroke-width="2.4"></path>
      <path d="M380 120 L 702 60 L 702 80 L 380 140 Z" fill="#7A3E22" opacity="0.6"></path>
      <path d="M60 362 L 640 130 L 702 130 L 702 362 Z" fill="#E8B070" stroke="#0D0D0F" stroke-width="2.4"></path>
      <g stroke="#B5652E" stroke-width="1.2" opacity="0.7"><path d="M160 330 L 700 150"></path><path d="M260 340 L 700 190"></path></g>
      {"".join(hauling)}
      {person("p2", 100, 380, 0.95, body="#7A3E22", stroke="#0D0D0F", up=[(-22, -158), (-53, -219), (-40, -282)], extra='<path d="M-27 -108 L 27 -108 L 34 -58 L -34 -58 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="3"></path><path d="M-27 -108 L 27 -108" stroke="#E8B830" stroke-width="5"></path>')}
      <path d="M62 112 C 80 40 180 30 240 80 C 280 114 310 170 330 220" fill="none" stroke="#2A140C" stroke-width="3.5" stroke-linecap="round"></path>
      <g stroke="#ffffff" stroke-width="2" opacity="0.8"><path d="M300 160 L 360 150"></path><path d="M310 190 L 370 196"></path><path d="M290 214 L 340 240"></path></g>'''
    o2 = (cap("Therefore they did set over them taskmasters to afflict them with their burdens. And they built for Pharaoh store-cities, Pithom and Raamses.", "left: 12px; top: 12px", maxw=420)
          + sfx("ビシッ", "BISHI!", "left: 340px; top: 220px", size=44, fill="#D7261E", stroke="#F3EFE6", rot=-10, tagbg="#0D0D0F", tagfg="#F3EFE6")
          + ref("EX 1:11", "right: 12px; bottom: 9px"))
    P2 = panel("linear-gradient(180deg, #FFC14D 0%, #FF8A3D 45%, #E8B070 46%, #C8783E 100%)", 702, 362, s2, o2, "2 · Pithom and Raamses")

    # panel 3a: the more they multiplied
    crowd = []
    r = random.Random(9)
    for row in range(5):
        for k in range(10 + row * 2):
            x = -10 + k * (362 / (10 + row * 2)) + r.uniform(-6, 6); y = 150 + row * 34; sc = 0.16 + row * 0.05
            crowd.append(person("q3", f"{x:.0f}", f"{y:.0f}", f"{sc:.2f}", body=r.choice(["#2A140C", "#3A2214", "#4A2A1A"]),
                                cloth=r.choice(["#C9A86A", "#B8A27A", "#8A6A4A"]), kind=r.choice(["Tunic", "Robe"]), sw=5, woman=r.random() < 0.4))
    s3 = f'''      {defs("q3", "Man", "Woman", "Tunic", "Robe")}
      <path d="M0 160 L 342 160" stroke="#0D0D0F" stroke-width="1.6"></path>
      {"".join(crowd)}'''
    o3 = (cap("But the more they afflicted them, the more they multiplied and the more they spread abroad.", "left: 10px; top: 10px; right: 10px", size=10.5)
          + ref("EX 1:12", "right: 10px; bottom: 8px", color="#0D0D0F", bg="#F3EFE6"))
    P3a = panel("linear-gradient(180deg, #FFC98A 0%, #FFE3B8 50%, #C8A06A 51%, #8A5A30 100%)", 342, 294, s3, o3, "3a · They multiplied")

    s4 = f'''      <defs><pattern id="q4Brick" width="60" height="30" patternUnits="userSpaceOnUse"><rect width="60" height="30" fill="#B5652E"></rect><path d="M0 0 L 60 0 M0 15 L 60 15 M15 0 L 15 15 M45 15 L 45 30" stroke="#5A2A16" stroke-width="2.4"></path></pattern></defs>
      <rect width="342" height="294" fill="url(#q4Brick)" opacity="0.55"></rect>
      {face(FX["__FACE_SLAVE__"], -10, -10, 0.92)}
      {speed(320, 150, 30, 120, 420, 3, color="#0D0D0F", sw=1, op=0.25)}'''
    o4 = cap("And they made their lives bitter with hard service, in mortar and in brick, and in all manner of service in the field.", "right: 10px; bottom: 10px", size=10.5, maxw=190)
    P3b = panel("linear-gradient(180deg, #8A3A1E, #3A140C)", 342, 294, s4, o4, "3b · Mortar and brick")

    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Exodus 1:8–14 — A New King", "330px minmax(0, 1fr) 300px", body, 1)
PAGES["EX1-P01-King"] = p01

# ───────────────────────── 02 · The Ark of Bulrushes (1:22–2:4) ─────────────────────────
def p02():
    s1 = f'''      <path d="M-10 210 C 120 200 260 220 400 206 C 520 196 620 214 712 204 L 712 304 L -10 304 Z" fill="#5A0E16"></path>
      <g fill="none" stroke="#D7261E" stroke-width="2" opacity="0.7"><path d="M10 236 C 90 228 170 244 250 236"></path><path d="M120 266 C 200 258 300 274 380 264"></path><path d="M20 290 C 100 282 180 298 260 290"></path></g>
      {face(FX["__FACE_PHARAOH_NEW__"], 720, -50, 0.95, flip=True)}'''
    o1 = (cap("And Pharaoh charged all his people, saying,", "left: 12px; top: 12px")
          + tail(446, 168, "r")
          + balloon("Every son that is born ye shall cast into the river, and every daughter ye shall save alive.", "left: 30px; top: 92px", 430, size=18, pad="22px 34px")
          + ref("EX 1:22", "left: 12px; bottom: 9px"))
    P1 = panel("linear-gradient(180deg, #3A0E0E 0%, #8A1A1A 60%, #3A0E0E 100%)", 702, 294, s1, o1, "1 · The decree")

    s2 = f'''      <defs><radialGradient id="q2Lamp" cx="290" cy="130" r="260" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFE680" stop-opacity="0.9"></stop><stop offset="1" stop-color="#FFE680" stop-opacity="0"></stop></radialGradient></defs>
      <rect width="342" height="362" fill="url(#q2Lamp)"></rect>
      {face(FX["__FACE_JOCHEBED__"], -50, 10, 0.85)}
      <g transform="rotate(-14 250 286)">
        <ellipse cx="250" cy="286" rx="78" ry="40" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2.4"></ellipse>
        <g fill="none" stroke="#B8B2A6" stroke-width="1.6"><path d="M190 280 C 220 300 260 304 300 296"></path><path d="M200 300 C 230 314 270 316 306 306"></path></g>
      </g>
      <circle cx="292" cy="250" r="24" fill="#E3B08A" stroke="#0D0D0F" stroke-width="2.2"></circle>
      <path d="M280 248 C 284 252 288 252 292 248" fill="none" stroke="#0D0D0F" stroke-width="1.8" stroke-linecap="round"></path>
      <path d="M300 238 C 306 236 310 238 312 242" fill="none" stroke="#5A3A22" stroke-width="3" stroke-linecap="round"></path>
      <path d="M262 238 C 268 220 300 214 316 232 C 320 256 312 276 296 282" fill="none" stroke="#E8E2D6" stroke-width="10" stroke-linecap="round"></path>
      <path d="M300 116 C 290 100 300 86 306 74 C 312 88 320 100 310 116 Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.4"></path>
      <path d="M284 116 L 328 116 C 326 128 290 128 284 116 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></path>'''
    o2 = (cap("And the woman conceived, and bare a son: and when she saw him that he was a goodly child, she hid him three months.", "left: 10px; right: 10px; bottom: 10px", size=10.5)
          + stamp(2, "right: 12px; top: 12px"))
    P2a = panel("radial-gradient(circle at 85% 30%, #8A4A22 0 40px, #3A1E14 220px, #12090A 400px)", 342, 362, s2, o2, "2a · Hid him three months")

    s3 = f'''      {E.reeds(-10, 352, 362, 260, 34, 12, color="#6FA35A", dark="#3E6A2E", heads=0.25)}
      {E.basket(171, 240, 250, 112, "q3")}
      <path d="M330 30 L 230 180" stroke="#6B3A10" stroke-width="7" stroke-linecap="round"></path>
      <path d="M236 170 C 226 180 222 190 230 196 C 240 194 244 184 240 174 Z" fill="#0D0D0F"></path>'''
    o3 = (cap("And when she could not longer hide him, she took for him an ark of bulrushes, and daubed it with slime and with pitch;", "left: 10px; right: 10px; top: 10px", size=10.5)
          + ref("EX 2:3", "right: 10px; bottom: 8px", color="#0D0D0F", bg="#F3EFE6"))
    P2b = panel("linear-gradient(180deg, #FFC98A 0%, #E8B070 100%)", 342, 362, s3, o3, "2b · The ark of bulrushes")

    s4 = f'''      <path d="M-10 170 C 160 160 360 176 520 166 C 600 160 660 168 712 164 L 712 334 L -10 334 Z" fill="#2C9DB8"></path>
      <g fill="none" stroke="#8FE3EE" stroke-width="2" opacity="0.8"><path d="M200 210 C 260 204 320 214 380 208"></path><path d="M420 290 C 500 282 580 296 660 288"></path><path d="M300 314 C 360 306 420 318 480 312"></path></g>
      {E.reeds(-10, 712, 190, 150, 70, 31, color="#4E7A3A", dark="#2E4A22", heads=0.3)}
      {face(FX["__FACE_MIRIAM__"], -40, 70, 0.6)}
      <ellipse cx="470" cy="262" rx="100" ry="14" fill="#0F4C68" opacity="0.6"></ellipse>
      {E.basket(470, 236, 160, 70, "q4")}
      <g fill="none" stroke="#F3EFE6" stroke-width="2" opacity="0.8"><path d="M380 268 C 420 276 520 276 560 268"></path></g>
      {E.reeds(-10, 712, 334, 140, 50, 77, color="#6FA35A", dark="#3E6A2E", heads=0.35)}'''
    o4 = (cap("And she put the child therein, and laid it in the flags by the river's brink.", "left: 12px; top: 12px", maxw=330)
          + cap("And his sister stood afar off, to know what would be done to him.", "right: 12px; bottom: 12px", maxw=300)
          + sfx("チャプ", "CHAPU", "left: 560px; top: 150px", size=34, fill="#F3EFE6", stroke="#0F4C68", rot=8))
    P3 = panel("linear-gradient(180deg, #FFB37A 0%, #FFE3B8 50%, #8FD0E2 51%)", 702, 324, s4, o4, "3 · In the flags")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Exodus 1:22–2:4 — The Ark of Bulrushes", "300px minmax(0, 1fr) 330px", body, 2)
PAGES["EX1-P02-Ark"] = p02

# ───────────────────────── 03 · Drawn Out of the Water (2:5–10) ─────────────────────────
def p03():
    sash = '<path d="M-28 -104 L 28 -104 L 28 -96 L -28 -96 Z" fill="#E8B830"></path><path d="M-20 -164 C -12 -150 12 -150 20 -164" fill="none" stroke="#0D0D0F" stroke-width="9"></path><path d="M-20 -164 C -12 -150 12 -150 20 -164" fill="none" stroke="#E8B830" stroke-width="6"></path>'
    s1 = f'''      {defs("r1", "Woman", "WomanUp", "Hair", "Robe")}
      <circle cx="560" cy="80" r="40" fill="#FFF4C2"></circle>
      <g fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.6">
        <path d="M640 200 C 636 150 644 110 650 70 L 656 70 C 652 110 646 150 650 200 Z" fill="#6B3A22"></path>
        <path d="M652 72 C 620 50 590 60 572 80 C 600 70 624 72 652 76 Z M652 72 C 680 46 708 54 720 70 C 696 66 674 70 652 76 Z M652 72 C 640 40 620 30 600 32 C 626 42 640 56 650 76 Z M654 72 C 670 40 690 34 708 38 C 684 48 668 60 656 76 Z"></path>
      </g>
      <path d="M-10 214 C 200 204 400 216 712 206 L 712 354 L -10 354 Z" fill="#2C9DB8"></path>
      <path d="M-10 270 C 80 250 200 250 330 264 C 380 300 400 330 420 354 L -10 354 Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("r1", 70, 300, 0.62, body="#7A4A2A", cloth="#DDEAF0", woman=True, hair="#0D0D0F", extra=sash)}
      {person("r1", 270, 312, 0.66, body="#7A4A2A", cloth="#DDEAF0", woman=True, hair="#0D0D0F", extra=sash)}
      {person("r1", 170, 336, 0.92, body="#7A4A2A", cloth="#F3EFE6", woman=True, hair="#0D0D0F", up=[(-22, -158), (-58, -196), (-70, -236)], extra=sash.replace("#E8B830", "#D7261E") + '<path d="M-12 -200 C -6 -208 6 -208 12 -200" fill="none" stroke="#E8B830" stroke-width="4"></path>', flip=True)}
      {person("r1", 520, 300, 0.6, body="#7A4A2A", cloth="#DDEAF0", woman=True, hair="#0D0D0F", up=[(-22, -158), (-62, -150), (-100, -156)], flip=True)}
      <path d="M440 262 C 480 252 560 252 600 262 L 600 354 L 440 354 Z" fill="#2C9DB8" opacity="0.85"></path>
      <g fill="none" stroke="#8FE3EE" stroke-width="2"><path d="M450 264 C 490 256 550 256 590 264"></path></g>
      {E.reeds(600, 712, 290, 140, 26, 8, color="#4E7A3A", dark="#2E4A22")}
      {E.basket(620, 270, 90, 40, "r1", lid=True)}
      {E.reeds(560, 712, 354, 90, 18, 81, color="#6FA35A", dark="#3E6A2E")}'''
    o1 = cap("And the daughter of Pharaoh came down to bathe at the river; and her maidens walked along by the river-side; and she saw the ark among the flags, and sent her handmaid to fetch it.", "left: 12px; top: 12px", maxw=470)
    P1 = panel("linear-gradient(180deg, #FFC98A 0%, #FFE3B8 60%)", 702, 344, s1, o1, "1 · The daughter of Pharaoh")

    s2 = f'''      {speed(171, 190, 40, 90, 400, 4, color="#ffffff", sw=1.6, op=0.7)}
      <path d="M40 342 C 30 250 60 200 100 190 L 250 190 C 290 200 316 250 304 342 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2.4"></path>
      <path d="M90 200 C 110 160 140 140 171 138 C 202 140 232 160 252 200 L 240 210 C 220 170 200 156 171 154 C 142 156 122 170 102 210 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2"></path>
      <circle cx="171" cy="200" r="50" fill="#E3B08A" stroke="#0D0D0F" stroke-width="2.6"></circle>
      <path d="M142 162 C 152 150 170 146 186 154" fill="none" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"></path>
      <g fill="none" stroke="#0D0D0F" stroke-width="2.6" stroke-linecap="round"><path d="M140 190 C 146 184 154 184 160 192"></path><path d="M182 192 C 188 184 196 184 202 190"></path><path d="M144 176 L 156 182 M200 176 L 188 182"></path></g>
      <ellipse cx="171" cy="224" rx="15" ry="13" fill="#8A1A1A" stroke="#0D0D0F" stroke-width="2"></ellipse>
      <ellipse cx="171" cy="230" rx="8" ry="5" fill="#D7261E"></ellipse>
      <g fill="#CFEFFF" stroke="#2C7DA0" stroke-width="1"><path d="M136 196 C 132 206 128 214 132 220 C 138 220 140 210 136 196 Z"></path><path d="M206 196 C 210 206 214 214 210 220 C 204 220 202 210 206 196 Z"></path></g>
      <path d="M-10 300 C 60 280 280 280 352 300 L 352 352 L -10 352 Z" fill="#C9A86A" stroke="#0D0D0F" stroke-width="2.4"></path>
      <path d="M-10 300 C 60 280 280 280 352 300" fill="none" stroke="#3A2412" stroke-width="10"></path>'''
    o2 = (cap("And she opened it, and saw the child: and, behold, the babe wept.", "left: 10px; right: 10px; bottom: 10px", size=10.5)
          + sfx("オギャア", "OGYAA!", "right: 10px; top: 14px", size=38, fill="#D7261E", stroke="#ffffff", rot=8, tagbg="#0D0D0F", tagfg="#ffffff"))
    P2a = panel("radial-gradient(circle at 50% 55%, #FFF4C2 0 60px, #FFC98A 160px, #E8A35A 320px)", 342, 342, s2, o2, "2a · The babe wept")

    s3 = f'''      {face(FX["__FACE_PRINCESS__"], 392, 10, 0.88, flip=True)}'''
    o3 = (cap("And she had compassion on him, and said,", "right: 10px; bottom: 10px", size=10.5, maxw=200)
          + tail(126, 172, "dr")
          + balloon("This is one of the Hebrews' children.", "left: 10px; top: 60px", 180, size=15, pad="20px 22px"))
    P2b = panel("linear-gradient(180deg, #2C9DB8 0%, #8FD0E2 100%)", 342, 342, s3, o3, "2b · Compassion")

    s4 = f'''      {face(FX["__FACE_MIRIAM__"], -70, -6, 0.76)}'''
    o4 = (tail(112, 168, "l")
          + balloon("Shall I go and call thee a nurse of the Hebrew women, that she may nurse the child for thee?", "left: 150px; top: 20px", 184, size=13, pad="22px 18px")
          + cap("And Pharaoh's daughter said to her, Go.", "right: 10px; bottom: 10px", size=10, maxw=180)
          + ref("EX 2:7–8", "left: 10px; bottom: 8px", color="#0D0D0F", bg="#F3EFE6"))
    P3a = panel("linear-gradient(180deg, #9CCB5E, #4E7A3A)", 342, 294, s4, o4, "3a · The sister")

    s5 = f'''      <g fill="none" stroke="#8FE3EE" stroke-width="2.4" opacity="0.8"><path d="M-10 230 C 60 220 120 240 200 230 C 260 222 300 236 352 230"></path><path d="M-10 262 C 60 252 140 272 220 262"></path></g>
      {E.reeds(-10, 352, 294, 110, 24, 55, color="#4E7A3A", dark="#2E4A22")}'''
    o5 = (cap("And the child grew, and she brought him unto Pharaoh's daughter, and he became her son. And she called his name Moses, and said,", "left: 10px; right: 10px; top: 10px", size=10)
          + '''    <div style="position: absolute; left: 0; right: 0; top: 104px; display: flex; flex-direction: column; align-items: center; transform: rotate(-3deg)">
      <span style="font-family: Anton, sans-serif; font-size: 64px; line-height: 1; letter-spacing: 0.08em; color: #F3EFE6; -webkit-text-stroke: 2px #0D0D0F">MOSES</span>
      <span style="margin-top: 2px; padding: 1px 6px; background: #0D0D0F; color: #F3EFE6; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 14px; letter-spacing: 0.3em">モーセ</span>
    </div>
'''
          + balloon("Because I drew him out of the water.", "right: 12px; bottom: 12px", 220, size=14, pad="12px 20px"))
    P3b = panel("linear-gradient(180deg, #12113A 0%, #1F5FAD 60%, #2C9DB8 100%)", 342, 294, s5, o5, "3b · Moses")
    body = P1 + cols(P2a, P2b) + cols(P3a, P3b)
    return mk.page("Exodus 2:5–10 — Drawn Out of the Water", "350px minmax(0, 1fr) 300px", body, 3)
PAGES["EX1-P03-Drawn"] = p03

# ───────────────────────── 04 · The Egyptian (2:11–15) ─────────────────────────
KILT = '<path d="M-27 -108 L 27 -108 L 34 -58 L -34 -58 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="3"></path><path d="M-27 -108 L 27 -108" stroke="#E8B830" stroke-width="5"></path>'
def p04():
    s1 = f'''      {speed(160, 140, 40, 150, 700, 8, color="#FFE680", sw=1.2, op=0.45)}
      {face(FX["__FACE_MOSES_PRINCE__"], -20, -50, 0.86)}'''
    o1 = (cap("And it came to pass in those days, when Moses was grown up, that he went out unto his brethren, and looked on their burdens: and he saw an Egyptian smiting a Hebrew, one of his brethren.", "right: 12px; top: 14px", maxw=400)
          + ref("EX 2:11", "right: 12px; bottom: 9px"))
    P1 = panel("linear-gradient(90deg, #E8B830 0%, #FF8A3D 40%, #7A2A5A 100%)", 702, 264, s1, o1, "1 · Moses grown")

    s2 = f'''      {defs("t2", "Man", "ManUp", "Tunic", "Bow")}
      {speed(120, 330, 40, 60, 500, 12, color="#ffffff", sw=1.4, op=0.5)}
      <path d="M-10 400 C 100 392 240 404 352 396 L 352 462 L -10 462 Z" fill="#E8B070" stroke="#0D0D0F" stroke-width="2"></path>
      {person("t2", 230, 420, 1.2, body="#7A3E22", up=[(-22, -158), (-56, -214), (-44, -276)], extra=KILT)}
      <path d="M177 84 C 150 110 120 170 96 236" fill="none" stroke="#3A1A10" stroke-width="6" stroke-linecap="round"></path>
      {E.kneel(96, 412, 1.35, color="#C9A86A", rim="#0D0D0F", flip=True, skin="#8A5A3E")}
      <g stroke="#0D0D0F" stroke-width="2.4"><path d="M70 230 L 40 210"></path><path d="M92 222 L 90 190"></path><path d="M110 228 L 136 206"></path></g>'''
    o2 = (cap("And he looked this way and that way, and when he saw that there was no man,", "left: 10px; right: 10px; top: 10px", size=10.5)
          + sfx("ビシッ", "BISHI!", "left: 16px; top: 160px", size=40, fill="#D7261E", stroke="#F3EFE6", rot=-12, align="flex-start"))
    P2a = panel("linear-gradient(180deg, #FF8A3D 0%, #D7261E 100%)", 342, 452, s2, o2, "2a · The Egyptian smiting a Hebrew")

    s3 = f'''      {speed(120, 220, 60, 160, 600, 21, color="#0D0D0F", sw=2, op=0.6)}
      {face(FX["__FACE_MOSES_ANGRY__"], -70, 20, 1.12)}'''
    o3 = (sfx("ドッ", "DOH!", "right: 14px; top: 40px", size=76, fill="#F3EFE6", stroke="#0D0D0F", rot=-8)
          + cap("he smote the Egyptian, and hid him in the sand.", "left: 10px; right: 10px; bottom: 10px", size=11, center=True))
    P2b = panel("radial-gradient(circle at 30% 50%, #FFE680 0 30px, #FF6A4A 160px, #5A0E16 420px)", 342, 452, s3, o3, "2b · He smote the Egyptian")

    s4 = f'''      {face(FX["__FACE_HEBREW_ANGRY__"], 404, 10, 0.72, flip=True)}'''
    o4 = (tail(196, 168, "r")
          + balloon("Who made thee a prince and a judge over us? thinkest thou to kill me, as thou killedst the Egyptian?", "left: 10px; top: 40px", 200, size=13, pad="22px 22px")
          + ref("EX 2:14", "left: 10px; bottom: 8px", color="#0D0D0F", bg="#F3EFE6"))
    P3a = panel("linear-gradient(180deg, #C8A06A, #8A5A30)", 342, 264, s4, o4, "3a · Who made thee a prince?")

    s5 = f'''      {defs("t5", "Man", "Robe")}
      <circle cx="80" cy="150" r="34" fill="#FFF4C2"></circle>
      <path d="M-10 170 C 80 150 160 176 240 160 C 290 150 320 166 352 160 L 352 274 L -10 274 Z" fill="#E8B070" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M-10 210 C 100 196 200 220 352 200 L 352 274 L -10 274 Z" fill="#C8783E"></path>
      <path d="M262 230 L 352 254 L 352 262 L 262 238 Z" fill="#7A3E22" opacity="0.6"></path>
      <g fill="#7A3E22" opacity="0.8"><ellipse cx="200" cy="240" rx="4" ry="2"></ellipse><ellipse cx="170" cy="246" rx="4" ry="2"></ellipse><ellipse cx="140" cy="250" rx="4" ry="2"></ellipse><ellipse cx="110" cy="256" rx="4" ry="2"></ellipse></g>
      {person("t5", 250, 236, 0.42, body="#3A1E14", cloth="#F3EFE6")}'''
    o5 = (cap("But Moses fled from the face of Pharaoh, and dwelt in the land of Midian: and he sat down by a well.", "left: 10px; right: 10px; top: 10px", size=10.5)
          + ref("EX 2:15", "right: 10px; bottom: 8px"))
    P3b = panel("linear-gradient(180deg, #7A2A5A 0%, #FF6A2A 55%, #FFC14D 70%)", 342, 264, s5, o5, "3b · Fled to Midian")
    body = P1 + cols(P2a, P2b) + cols(P3a, P3b)
    return mk.page("Exodus 2:11–15 — The Egyptian", "270px minmax(0, 1fr) 270px", body, 4)
PAGES["EX1-P04-Egyptian"] = p04

# ───────────────────────── 05 · The Well in Midian (2:16–25) ─────────────────────────
def p05():
    robes = ["#C2456A", "#E8B830", "#2C9DB8", "#7A3BA8", "#3F8A44", "#FF8A3D", "#D7261E"]
    daughters = "".join(person("u1", 30 + i * 34, 300 + (i % 2) * 12, 0.5 + (i % 2) * 0.04, body="#5A3A22", cloth=robes[i], woman=True, hair=True) for i in range(7))
    s1 = f'''      {defs("u1", "Man", "ManUp", "Woman", "Hair", "Robe")}
      <path d="M-10 230 C 200 220 500 236 712 226 L 712 354 L -10 354 Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></path>
      {daughters}
      {E.sheep(70, 330, 0.6)}{E.sheep(150, 344, 0.66)}{E.sheep(230, 336, 0.62, flip=True)}
      <rect x="250" y="290" width="70" height="20" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></rect><rect x="254" y="292" width="62" height="6" fill="#2C9DB8"></rect>
      <path d="M320 300 L 320 250 C 320 236 400 236 400 250 L 400 300 C 400 316 320 316 320 300 Z" fill="#A89E86" stroke="#0D0D0F" stroke-width="2.4"></path>
      <ellipse cx="360" cy="250" rx="40" ry="10" fill="#2A1A10" stroke="#0D0D0F" stroke-width="2"></ellipse>
      <g stroke="#6B6862" stroke-width="1.4"><path d="M320 270 L 400 270 M340 250 L 340 270 M380 250 L 380 270 M330 270 L 330 290 M360 270 L 360 290 M390 270 L 390 290"></path></g>
      {person("u1", 450, 330, 0.86, body="#7A4A2A", cloth="#F3EFE6", flip=True, up=[(-22, -158), (-64, -146), (-104, -158)])}
      {person("u1", 560, 316, 0.72, body="#2A1A10", cloth="#5A4A3E", up=[(-22, -158), (-40, -210), (-30, -250)])}
      <path d="M540 120 L 552 316" stroke="#3E2416" stroke-width="5" stroke-linecap="round"></path>
      {person("u1", 630, 320, 0.7, body="#2A1A10", cloth="#4A3A2E")}
      {person("u1", 690, 312, 0.66, body="#2A1A10", cloth="#5A4A3E")}'''
    o1 = (cap("Now the priest of Midian had seven daughters: and they came and drew water, and filled the troughs to water their father's flock.", "left: 12px; top: 12px", maxw=330)
          + cap("And the shepherds came and drove them away; but Moses stood up and helped them, and watered their flock.", "right: 12px; top: 12px", maxw=250))
    P1 = panel("linear-gradient(180deg, #FF9A6B 0%, #FFC98A 40%, #FFE3B8 64%)", 702, 354, s1, o1, "1 · At the well")

    s2 = f'''      {face(FX["__FACE_ZIPPORAH__"], -40, 0, 0.8)}'''
    o2 = cap("And Moses was content to dwell with the man: and he gave Moses Zipporah his daughter.", "right: 10px; bottom: 10px", size=10.5, maxw=190)
    P2a = panel("linear-gradient(180deg, #FFC98A, #C2456A)", 342, 312, s2, o2, "2a · Zipporah")
    s3 = f'''      {face(FX["__FACE_MOSES__"], 390, 0, 0.8, flip=True)}'''
    o3 = cap("And she bare a son, and he called his name Gershom; for he said, I have been a sojourner in a foreign land.", "left: 10px; bottom: 10px", size=10.5, maxw=190)
    P2b = panel("linear-gradient(180deg, #8FD0E2, #C8A06A)", 342, 312, s3, o3, "2b · A sojourner")

    bent = "".join(person("u4", 40 + i * 60, 300 - (i % 3) * 6, 0.32, body="#12090A", cloth="#2A1A10", kind="Tunic", sw=5,
                          extra='<rect x="-26" y="-232" width="52" height="26" fill="#5A2A16" stroke="#0D0D0F" stroke-width="4"></rect>') for i in range(12))
    cries = "".join(f'<path d="M{40 + i*60} {220 - (i%3)*6} C {20 + i*60} 170 {60 + i*60} 130 {40 + i*60} 80 C {20 + i*60} 40 {50 + i*60} 20 {42 + i*60} -10" fill="none" stroke="#FFD23F" stroke-width="2" stroke-dasharray="6 6" opacity="0.8"></path>' for i in range(12))
    s4 = f'''      {defs("u4", "Man", "Tunic")}
      {stars(120, 702, 220, 17)}
      <path d="M120 300 L 230 150 L 340 300 Z M420 300 L 500 190 L 580 300 Z" fill="#1A0E1E" stroke="#3A2A4E" stroke-width="2"></path>
      <path d="M-10 280 L 712 280 L 712 324 L -10 324 Z" fill="#2A140C"></path>
      {cries}
      {bent}'''
    o4 = (cap("And it came to pass in the course of those many days, that the king of Egypt died: and the children of Israel sighed by reason of the bondage, and they cried, and their cry came up unto God by reason of the bondage.", "left: 12px; top: 12px", maxw=420)
          + cap("And God heard their groaning, and God remembered his covenant with Abraham, with Isaac, and with Jacob.", "right: 12px; bottom: 12px", maxw=300))
    P3 = panel("radial-gradient(ellipse at 50% 0%, #FFD23F 0 20px, #7A3BA8 220px, #12113A 460px)", 702, 314, s4, o4, "3 · Their cry came up")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Exodus 2:16–25 — The Well in Midian", "360px minmax(0, 1fr) 320px", body, 5)
PAGES["EX1-P05-Midian"] = p05

# ───────────────────────── 06 · The Bush (3:1–5) ─────────────────────────
def p06():
    flock = "".join(E.sheep(40 + i * 40 + (i % 2) * 10, 214 + (i % 3) * 8, 0.4 + (i % 3) * 0.04, flip=i % 2 == 1) for i in range(8))
    s1 = f'''      {defs("v1", "Man", "Robe")}
      <path d="M380 244 L 520 40 L 560 70 L 600 20 L 712 160 L 712 244 Z" fill="#7A3E5A" stroke="#0D0D0F" stroke-width="2.4"></path>
      <path d="M520 40 L 560 70 L 600 20 L 640 70 L 600 90 L 560 120 Z" fill="#E8A35A" opacity="0.6"></path>
      <path d="M-10 200 C 160 190 320 210 712 196 L 712 244 L -10 244 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {flock}
      {person("v1", 380, 226, 0.5, body="#3A1E14", cloth="#C9A86A")}
      <path d="M398 120 L 404 226" stroke="#3E2416" stroke-width="3" stroke-linecap="round"></path><path d="M398 120 C 396 112 404 108 408 114" fill="none" stroke="#3E2416" stroke-width="3" stroke-linecap="round"></path>'''
    o1 = (cap("Now Moses was keeping the flock of Jethro his father-in-law, the priest of Midian: and he led the flock to the back of the wilderness, and came to the mountain of God, unto Horeb.", "left: 12px; top: 12px", maxw=360)
          + stamp(3, "right: 16px; bottom: 14px"))
    P1 = panel("linear-gradient(180deg, #FF9A6B 0%, #FFC98A 60%)", 702, 244, s1, o1, "1 · Horeb")

    s2 = f'''      {defs("v2", "Man", "Robe")}
      <defs><radialGradient id="v2Glow" cx="440" cy="300" r="420" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFF4C2"></stop><stop offset="0.3" stop-color="#FFC14D" stop-opacity="0.8"></stop><stop offset="1" stop-color="#7A2A5A" stop-opacity="0"></stop></radialGradient></defs>
      <rect width="702" height="472" fill="url(#v2Glow)"></rect>
      {speed(440, 300, 80, 200, 900, 33, color="#FFE680", sw=1.6, op=0.5)}
      <path d="M-10 420 C 160 404 320 430 480 416 C 600 406 660 416 712 412 L 712 482 L -10 482 Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="2.4"></path>
      {E.bush(440, 430, 340, 330, 7)}
      {person("v2", 100, 452, 0.78, body="#1A0E0A", cloth="#3A2214", stroke="#FF8A3D", sw=3)}
      <path d="M128 296 L 136 452" stroke="#2A140C" stroke-width="4" stroke-linecap="round"></path>'''
    o2 = (cap("And the angel of Jehovah appeared unto him in a flame of fire out of the midst of a bush: and he looked, and, behold, the bush burned with fire, and the bush was not consumed.", "left: 12px; top: 12px; right: 12px", center=True)
          + tail(94, 250, "dl")
          + balloon("I will turn aside now, and see this great sight, why the bush is not burnt.", "left: 16px; top: 128px", 220, size=13, pad="18px 20px")
          + sfx("ゴオオオ", "GOOOO", "right: 14px; top: 120px", size=48, fill="#FFF4C2", stroke="#D7261E", rot=6, tagbg="#0D0D0F", tagfg="#FFF4C2")
          + ref("EX 3:2–3", "right: 12px; bottom: 9px"))
    P2 = panel("linear-gradient(180deg, #12113A 0%, #2A1A5E 50%, #7A2A5A 100%)", 702, 472, s2, o2, "2 · The bush was not consumed")

    s3 = f'''      {face(FX["__FACE_MOSES_FIRE__"], -50, 40, 0.66)}'''
    o3 = (cap("God called unto him out of the midst of the bush, and said,", "left: 10px; top: 10px; right: 10px", size=10)
          + god("Moses, Moses.", "right: 12px; top: 74px", size=22)
          + tail(122, 182, "l")
          + balloon("Here am I.", "left: 160px; top: 168px", 150, size=17, pad="16px 14px"))
    P3a = panel("radial-gradient(circle at 100% 30%, #FFE680 0 30px, #FF8A3D 140px, #7A2A5A 340px)", 342, 264, s3, o3, "3a · Moses, Moses")

    s4 = f'''      <path d="M-10 190 C 100 180 240 196 352 186 L 352 274 L -10 274 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>
      {E.sandal(150, 238, 1.3, -78)}{E.sandal(206, 254, 1.3, -62)}'''
    o4 = (god("Draw not nigh hither: put off thy shoes from off thy feet, for the place whereon thou standest is holy ground.", "left: 10px; top: 10px; right: 10px", size=17)
          + ref("EX 3:5", "right: 10px; bottom: 8px"))
    P3b = panel("linear-gradient(180deg, #FF8A3D, #7A2A5A)", 342, 264, s4, o4, "3b · Holy ground")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Exodus 3:1–5 — The Bush", "250px minmax(0, 1fr) 270px", body, 6)
PAGES["EX1-P06-Bush"] = p06

# ───────────────────────── 07 · I AM (3:6–14) ─────────────────────────
IAM = '''    <div style="position: absolute; left: 0; right: 0; top: 140px; display: flex; flex-direction: column; align-items: center; gap: 4px; transform: rotate(-2deg)">
      <span style="font-family: Anton, sans-serif; font-size: 78px; line-height: 1; letter-spacing: 0.04em; white-space: nowrap; color: #12113A; -webkit-text-stroke: 3px #FFD23F; paint-order: stroke fill">I AM THAT I AM</span>
      <span style="padding: 1px 8px; background: #12113A; color: #FFD23F; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 14px; letter-spacing: 0.3em">わたしは有って有る者</span>
    </div>
'''
def p07():
    s1 = f'''            <defs><radialGradient id="w1Glow" cx="400" cy="220" r="380" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFF4C2"></stop><stop offset="0.35" stop-color="#FFC14D" stop-opacity="0.7"></stop><stop offset="1" stop-color="#12113A" stop-opacity="0"></stop></radialGradient></defs>
      <rect width="702" height="284" fill="url(#w1Glow)"></rect>
      <path d="M-10 250 C 200 240 400 256 712 244 L 712 294 L -10 294 Z" fill="#2A140C"></path>
      {E.bush(400, 256, 230, 230, 41)}
      {E.kneel(150, 262, 1.25, color="#2A1A2E", rim="#FF8A3D")}'''
    o1 = (god("I am the God of thy father, the God of Abraham, the God of Isaac, and the God of Jacob.", "right: 12px; top: 12px", size=15, maxw=220)
          + cap("And Moses hid his face; for he was afraid to look upon God.", "left: 12px; top: 12px", maxw=250))
    P1 = panel("linear-gradient(180deg, #12113A, #2A1A5E)", 702, 284, s1, o1, "1 · He hid his face")

    s2 = f'''      {E.blaze(171, 330, 380, 300, 5, n=9)}'''
    o2 = god("I have surely seen the affliction of my people that are in Egypt, and have heard their cry by reason of their taskmasters; … Come now therefore, and I will send thee unto Pharaoh.", "left: 10px; top: 10px; right: 10px", size=17)
    P2a = panel("linear-gradient(180deg, #2A1A5E, #7A2A5A)", 342, 302, s2, o2, "2a · I will send thee")
    s3 = f'''      {face(FX["__FACE_MOSES_AFRAID__"], 420, 10, 0.78, flip=True)}'''
    o3 = (tail(196, 178, "r")
          + balloon("Who am I, that I should go unto Pharaoh, and that I should bring forth the children of Israel out of Egypt?", "left: 8px; top: 30px", 206, size=12.5, pad="24px 20px")
          + god("Certainly I will be with thee.", "left: 10px; bottom: 10px", size=14, maxw=200))
    P2b = panel("radial-gradient(circle at 0% 40%, #FFE680 0 30px, #FF8A3D 150px, #5A1A3E 360px)", 342, 302, s3, o3, "2b · Who am I?")

    s4 = f'''      {speed(351, 210, 90, 140, 900, 77, color="#FFF4C2", sw=2, op=0.7)}
      {speed(351, 210, 60, 220, 900, 78, color="#D7261E", sw=1.4, op=0.5)}'''
    o4 = (tail(220, 92, "dl")
          + balloon("When I come unto the children of Israel … they shall say to me, What is his name? What shall I say unto them?", "left: 14px; top: 14px", 300, size=13, pad="16px 26px")
          + IAM
          + god("Thus shalt thou say unto the children of Israel, I AM hath sent me unto you.", "right: 12px; bottom: 12px", size=16, maxw=330)
          + ref("EX 3:13–14", "left: 12px; bottom: 9px", color="#0D0D0F", bg="#FFF4C2"))
    P3 = panel("radial-gradient(circle at 50% 55%, #FFFFFF 0 60px, #FFF4C2 140px, #FFC14D 260px, #FF6A2A 420px)", 702, 384, s4, o4, "3 · I AM THAT I AM")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Exodus 3:6–14 — I AM", "290px minmax(0, 1fr) 390px", body, 7)
PAGES["EX1-P07-IAM"] = p07

# ───────────────────────── 08 · The Rod (4:1–17) ─────────────────────────
def p08():
    s1 = f'''      {face(FX["__FACE_MOSES_FIRE__"], -40, -30, 0.8)}
      <path d="M300 300 L 236 -10" stroke="#0D0D0F" stroke-width="13" stroke-linecap="round"></path>
      <path d="M300 300 L 236 -10" stroke="#8A5A30" stroke-width="9" stroke-linecap="round"></path>
'''
    o1 = (god("What is that in thy hand?", "left: 330px; top: 20px", size=22)
          + tail(152, 158, "l")
          + balloon("A rod.", "left: 190px; top: 140px", 110, size=18, pad="14px 10px")
          + god("Cast it on the ground.", "left: 380px; top: 130px", size=22)
          + stamp(4, "right: 16px; bottom: 14px"))
    P1 = panel("radial-gradient(circle at 100% 50%, #FFE680 0 40px, #FF8A3D 200px, #5A1A3E 460px)", 702, 284, s1, o1, "1 · What is that in thy hand?")

    s2 = f'''      {defs("x2", "Man", "ManUp", "Robe")}
      {speed(250, 240, 50, 120, 700, 61, color="#FFE680", sw=1.4, op=0.4)}
      <path d="M-10 330 C 160 320 360 336 712 326 L 712 412 L -10 412 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      <ellipse cx="240" cy="372" rx="210" ry="22" fill="#8A5A30" opacity="0.5"></ellipse>
      {snake.snake([(40, 380), (120, 356), (200, 384), (290, 370), (350, 330), (370, 260), (360, 190), (400, 150), (450, 150)], 24, "x2s", head_scale=1.5)}
      {person("x2", 600, 380, 0.8, body="#1A0E0A", cloth="#3A2214", stroke="#FFC14D", up=[(-22, -158), (-50, -200), (-40, -250)], flip=True)}
      <g stroke="#0D0D0F" stroke-width="2.4" stroke-linecap="round"><path d="M650 220 L 690 200"></path><path d="M656 250 L 700 246"></path><path d="M650 280 L 692 292"></path></g>'''
    o2 = (cap("And he cast it on the ground, and it became a serpent; and Moses fled from before it.", "left: 12px; top: 12px", maxw=380)
          + sfx("シャーッ", "SHAAA!", "left: 440px; top: 40px", size=50, fill="#3F8A44", stroke="#F3EFE6", rot=-8, tagbg="#0D0D0F", tagfg="#F3EFE6", align="flex-start")
          + cap("And he put forth his hand, and laid hold of it, and it became a rod in his hand.", "right: 12px; bottom: 12px", maxw=330))
    P2 = panel("linear-gradient(180deg, #5A1A3E 0%, #B5421E 60%, #FF8A3D 100%)", 702, 402, s2, o2, "2 · It became a serpent")

    s3 = f'''      {E.hand(171, 200, 1.05, skin="#EDE9E0", spots=True)}'''
    o3 = (cap("And he put his hand into his bosom: and when he took it out, behold, his hand was leprous, as white as snow.", "left: 10px; right: 10px; top: 10px", size=10.5)
          + ref("EX 4:6", "right: 10px; bottom: 8px"))
    P3a = panel("radial-gradient(circle at 50% 70%, #7A3BA8 0 40px, #2A1A5E 200px, #12113A 360px)", 342, 294, s3, o3, "3a · White as snow")

    s4 = f'''      {face(FX["__FACE_MOSES__"], -60, 40, 0.62)}'''
    o4 = (tail(80, 104, "dr")
          + balloon("Oh, Lord, I am not eloquent … for I am slow of speech, and of a slow tongue.", "left: 8px; top: 8px", 210, size=12.5, pad="16px 20px")
          + god("Is there not Aaron thy brother the Levite? I know that he can speak well. … And thou shalt take in thy hand this rod, wherewith thou shalt do the signs.", "right: 8px; bottom: 28px", size=13, maxw=196)
          + '    <span style="position: absolute; right: 10px; bottom: 7px; font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">つづく · TO BE CONTINUED</span>\n')
    P3b = panel("linear-gradient(180deg, #FF8A3D, #5A1A3E)", 342, 294, s4, o4, "3b · Aaron thy brother")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("Exodus 4:1–17 — The Rod", "290px minmax(0, 1fr) 300px", body, 8)
PAGES["EX1-P08-Rod"] = p08


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "exodus/project"))
