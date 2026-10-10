"""2 Samuel Book One — Thou Art the Man (2 Samuel 1–12). Writes the .dc.html pages into the given folder.
Usage: python3 samuel3_book1.py <out_dir>"""
import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1] / "kit"))  # shared drawing kit
import sys, pathlib, random
import mk, exodus as E, exodus4 as Z, exodus5 as V, numbers1 as N, joshua1 as J, judges2 as S, ruth1 as R, samuel1 as A, samuel2 as B, samuel3 as C
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, stars
from exodus_book3 import crowd
from numbers_book1 import badge, hills
from judges_book1 import shout
from judges_book2 import end_mark
from samuel_book1 import D, POINT, shouting
FX = C.tokens()
PAGES = {}
DK = C.DAVID_K
KING = C.KING
NATHAN = C.NATHAN
ELDER = dict(body="#3A1E14", sw=4)


def elders(p, xs, y, s, seed):
    r = random.Random(seed)
    return "".join(person(p, x, y, round(s * r.uniform(0.94, 1.0), 3), body="#3A1E14", cloth=r.choice(["#8A6A4A", "#5A6E8A", "#C9A86A", "#4A3A6A", "#6A5A4E"]), sw=4) for x in xs)


# ───────────────────────── Cover ─────────────────────────
def cover():
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {D("c1")}
    <g transform="translate(0 440)">{C.cedar(760, 640, 520)}</g>
    <rect x="0" y="420" width="760" height="700" fill="#12113A" opacity="0.35"></rect>
    {V.rays(520, 700, 40, 80, 900, color="#FFF4C2", op=0.14)}
    {C.throne(540, 960, 1.9)}
    {person("c1", 540, 990, 1.55, **DK, extra=KING)}
    {person("c1", 170, 1050, 1.9, **NATHAN, up=POINT, flip=True)}
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The Second Book of</span>
    <span>No. 01</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 124px; line-height: 1.2; letter-spacing: -1px; color: #F3EFE6">SAMUEL</h1>
  <div style="position: absolute; top: 236px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 252px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book One — Thou Art the Man</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 12</span>
  </div>
  <div style="position: absolute; top: 40px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 40px; line-height: 1.04; color: #F3EFE6"><span>サ</span><span>ム</span><span>エ</span><span>ル</span><span>記</span><span>下</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.14em; color: #F3EFE6">SAMUERU-KI GE</span>
  </div>
  <div style="position: absolute; left: 38px; top: 322px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 250px; line-height: 1.45">Thou art the man.</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 1</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #12113A 0%, #2A1A5E 30%, #4A2A7A 55%, #8A1E2E 80%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("2 Samuel Book One — Cover", None, body, root_style=root)
PAGES["Main"] = cover


# ───────────────────────── 01 · Mourning (1:11–17) ─────────────────────────
def p01():
    s1 = f'''      {face(FX["__FACE_DAVID_MOURN__"], -40, 10, 0.84)}'''
    o1 = (cap("Then David took hold on his clothes, and rent them; and likewise all the men that were with him: and they mourned, and wept, and fasted until even, for Saul, and for Jonathan his son, and for the people of Jehovah, and for the house of Israel; because they were fallen by the sword.", "right: 12px; top: 14px", size=11.5, maxw=360)
          + stamp(1, "right: 16px; bottom: 14px"))
    P1 = panel("radial-gradient(circle at 25% 50%, #C8D0DE 0 30px, #5A6E8A 220px, #12113A 460px)", 702, 324, s1, o1, "1 · David rent his clothes")

    r = random.Random(3)
    s2 = f'''      {J.sun(520, 210, 60)}
      {B.gilboa(702, 260, 110, 2101, color="#3A1E2A")}
      <path d="M-10 280 C 200 270 500 290 712 276 L 712 414 L -10 414 Z" fill="#2A1A1E" stroke="#0D0D0F" stroke-width="2"></path>
      {"".join(E.kneel(x, 380 + r.uniform(-8, 8), 0.5 + r.uniform(-0.05, 0.05), color=r.choice(["#4A3A3E", "#3A2A2E", "#5A4A4E"]), flip=x > 400) for x in range(60, 700, 70) if not 300 < x < 420)}
      {E.kneel(350, 396, 0.74, color="#C9A86A", skin="#5A2A16")}'''
    o2 = cap("And David lamented with this lamentation over Saul and over Jonathan his son", "left: 12px; top: 12px", size=12, maxw=420)
    P2 = panel("linear-gradient(180deg, #12113A 0%, #4A1D55 50%, #D7261E 100%)", 702, 404, s2, o2, "2 · The lamentation")

    s3 = f'''      <path d="M-10 180 L 712 180 L 712 264 L -10 264 Z" fill="#5A4A4E" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M220 190 C 240 150 460 150 480 190 Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></path>
      <path d="M250 150 C 320 90 400 90 460 150" fill="none" stroke="#0D0D0F" stroke-width="8"></path><path d="M250 150 C 320 90 400 90 460 150" fill="none" stroke="#8A5A30" stroke-width="5"></path>
      <path d="M250 150 L 460 150" stroke="#F3EFE6" stroke-width="1.6"></path>
      {B.crown(350, 172, 1.2, -8)}'''
    o3 = ref("SAUL · JONATHAN", "left: 12px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6")
    P3 = panel("linear-gradient(180deg, #4A1D55 0%, #8A4A6A 100%)", 702, 254, s3, o3, "3 · The bow and the crown")
    body = P1 + P2 + P3
    return mk.page("2 Samuel 1:11–17 — Mourning", "330px minmax(0, 1fr) 260px", body, 1)
PAGES["SB1-P01-Mourning"] = p01


# ───────────────────────── 02 · King over All Israel (5:3–12) ─────────────────────────
def p02():
    s1 = f'''      {D("b1")}
      {V.rays(351, -20, 36, 40, 600, color="#FFF4C2", op=0.3)}
      <path d="M-10 230 L 712 230 L 712 294 L -10 294 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {elders("b1", [50, 110, 170, 530, 590, 650], 282, 0.6, 2201)}
      {person("b1", 351, 286, 0.78, **DK)}
      {person("b1", 430, 288, 0.74, body="#3A1E14", cloth="#6A5A4E", sw=4, up=[(-22, -158), (-44, -190), (-58, -214)])}
      {A.vial(366, 128, 0.9, rot=-140, pour=14)}'''
    o1 = (cap("So all the elders of Israel came to the king to Hebron; and king David made a covenant with them in Hebron before Jehovah: and they anointed David king over Israel.", "left: 12px; top: 12px", size=10, maxw=320)
          + stamp(5, "right: 16px; top: 14px"))
    P1 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 294, s1, o1, "1 · King over Israel")

    s2 = f'''      {face(FX["__FACE_DAVID_KING__"], -50, 20, 0.74)}'''
    o2 = cap("David was thirty years old when he began to reign, and he reigned forty years.", "right: 10px; top: 10px", size=10, maxw=160)
    P2a = panel("radial-gradient(circle at 30% 50%, #FFE680 0 20px, #7A3BA8 150px, #12113A 330px)", 342, 294, s2, o2, "2a · Thirty years old")
    s3 = f'''      {J.sun(270, 70, 30)}
      {J.city_hill(171, 270, 300, 170, 2202)}
      <path d="M171 110 L 171 60" stroke="#0D0D0F" stroke-width="3"></path><path d="M171 60 L 210 70 L 171 82 Z" fill="#4A2A7A" stroke="#0D0D0F" stroke-width="1.6"></path>
      <path d="M-10 270 L 352 270 L 352 304 L -10 304 Z" fill="#8A7A5A"></path>'''
    o3 = cap("Nevertheless David took the stronghold of Zion; the same is the city of David.", "left: 10px; top: 10px", size=10, maxw=210)
    P2b = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 342, 294, s3, o3, "2b · The stronghold of Zion")

    s4 = f'''      {D("b4")}
      {J.city_hill(520, 250, 360, 160, 2203)}
      <path d="M-10 250 L 712 250 L 712 404 L -10 404 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {"".join(f'<g transform="translate({x} {y})"><rect x="-70" y="-14" width="140" height="22" rx="10" fill="#8A4A26" stroke="#0D0D0F" stroke-width="2"></rect><ellipse cx="70" cy="-3" rx="6" ry="11" fill="#C8803A" stroke="#0D0D0F" stroke-width="1.6"></ellipse></g>' for x, y in [(160, 330), (200, 370)])}
      {"".join(person("b4", x, 392, 0.56, body="#3A1E14", cloth=c, kind="Tunic", sw=4) for x, c in [(70, "#2C9DB8"), (300, "#8A6A4A"), (360, "#2C9DB8")])}'''
    o4 = (cap("And David waxed greater and greater; for Jehovah, the God of hosts, was with him.", "left: 12px; top: 12px", size=12, maxw=330)
          + cap("And Hiram king of Tyre sent messengers to David, and cedar-trees, and carpenters, and masons; and they built David a house.", "right: 12px; bottom: 12px", size=10, maxw=300))
    P3 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 394, s4, o4, "3 · Greater and greater")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("2 Samuel 5:3–11 — King over All Israel", "300px 300px minmax(0, 1fr)", body, 2)
PAGES["SB1-P02-King"] = p02


# ───────────────────────── 03 · The Ark Comes Up (6:2–12) ─────────────────────────
def p03():
    s1 = f'''      {D("c1")}
      {hills(130, "#6A8A4A", 2301, 40)}
      <path d="M-10 170 L 712 170 L 712 254 L -10 254 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {crowd("c1", 30, -10, 712, 180, 240, 2302, 0.2, 0.34)}'''
    o1 = cap("And David arose, and went with all the people that were with him, from Baale-judah, to bring up from thence the ark of God, which is called by the Name, even the name of Jehovah of hosts that sitteth above the cherubim.", "left: 12px; top: 12px", size=10.5, maxw=440)
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 244, s1, o1, "1 · To bring up the ark")

    s2 = f'''      {D("c2")}
      {hills(150, "#8A9A5A", 2303, 30)}
      <path d="M-10 190 L 712 190 L 712 444 L -10 444 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M-10 330 C 200 316 500 316 712 330 L 712 380 C 500 366 200 366 -10 380 Z" fill="#E8C88A"></path>
      {A.team(150, 360, 0.72)}
      {person("c2", 540, 372, 0.6, body="#3A1E14", cloth="#8A6A4A", kind="Tunic", sw=4, extra=E.STAFF if hasattr(E, "STAFF") else "")}
      {person("c2", 60, 370, 0.6, body="#3A1E14", cloth="#5A6E8A", kind="Tunic", sw=4)}
      {C.musician("c2", 80, 430, 0.62, "timbrel", "#C2456A")}
      {C.musician("c2", 170, 434, 0.64, "harp", "#3F8A44", woman=False)}
      {C.musician("c2", 470, 432, 0.64, "cymbals", "#E8A317", woman=False)}
      {C.musician("c2", 560, 430, 0.62, "timbrel", "#7A3BA8")}
      {C.musician("c2", 650, 434, 0.62, "harp", "#2C9DB8", woman=False)}
      {C.notes(330, 250, 6, 2304)}'''
    o2 = (cap("And they set the ark of God upon a new cart, and brought it out of the house of Abinadab that was in the hill: and Uzzah and Ahio, the sons of Abinadab, drove the new cart.", "left: 12px; top: 12px", size=10.5, maxw=330)
          + cap("And David and all the house of Israel played before Jehovah with all manner of instruments made of fir-wood, and with harps, and with psalteries, and with timbrels, and with castanets, and with cymbals.", "right: 12px; top: 12px", size=10, maxw=320)
          + stamp(6, "left: 16px; bottom: 14px", rot=-4))
    P2 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 434, s2, o2, "2 · A new cart")

    s3 = f'''      {D("c3")}
      {J.city_hill(560, 150, 260, 110, 2305)}
      <path d="M-10 150 L 712 150 L 712 224 L -10 224 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {J.ark_borne("c3", 300, 212, 0.5, "obA")}'''
    o3 = cap("And David went and brought up the ark of God from the house of Obed-edom into the city of David with joy.", "left: 12px; top: 12px", size=11, maxw=330)
    P3 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 224, s3, o3, "3 · With joy")
    body = P1 + P2 + P3
    return mk.page("2 Samuel 6:2–12 — The Ark Comes Up", "250px minmax(0, 1fr) 230px", body, 3)
PAGES["SB1-P03-Ark"] = p03


# ───────────────────────── 04 · Dancing before Jehovah (6:14–16) ─────────────────────────
def p04():
    s1 = f'''      {D("d1")}
      {V.rays(351, 200, 40, 60, 900, color="#FFF4C2", op=0.3)}
      {J.city_hill(560, 260, 300, 120, 2401)}
      <path d="M-10 260 L 712 260 L 712 654 L -10 654 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {shouting("dx", 18, -10, 712, 290, 360, 2402, 0.3, 0.42, gap=(220, 520))}
      {J.ark_borne("d1", 560, 450, 0.62, "dnA")}
      {J.trumpeter("d1", 90, 470, 0.7)}{J.trumpeter("d1", 170, 474, 0.66)}
      {C.dancer(330, 620, 1.55, "dvd", [(-22, -158), (-48, -196), (-56, -244)], [(22, -158), (40, -206), (30, -250)])}
      {mk.speed(330, 400, 30, 160, 400, 2403, color="#FFF4C2", op=0.5)}'''
    o1 = (cap("And David danced before Jehovah with all his might; and David was girded with a linen ephod.", "left: 12px; top: 12px", size=12, maxw=320)
          + cap("So David and all the house of Israel brought up the ark of Jehovah with shouting, and with the sound of the trumpet.", "right: 12px; top: 12px", size=10.5, maxw=280)
          + sfx("ワァーッ", "WAAAH", "right: 30px; top: 120px", size=36, fill="#FFD23F", stroke="#0D0D0F", rot=6))
    P1 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 644, s1, o1, "1 · With all his might")

    s2 = f'''      <rect x="-10" y="-10" width="362" height="334" fill="#A89A7E"></rect>
      {"".join(f'<path d="M-10 {y} L 352 {y}" stroke="#8A7A5E" stroke-width="2"></path>' for y in range(20, 320, 30))}
      {C.window(171, 120, 160, 150)}
      <clipPath id="mwin"><path d="M91 270 L 91 120 C 91 32 251 32 251 120 L 251 270 Z"></path></clipPath>
      <g clip-path="url(#mwin)"><rect x="91" y="30" width="160" height="240" fill="#4A1D55"></rect>{face(FX["__FACE_MICHAL__"], 290, 50, 0.46, flip=True)}</g>'''
    o2 = cap("that Michal the daughter of Saul looked out at the window, and saw king David leaping and dancing before Jehovah;", "left: 10px; bottom: 10px", size=9.5, maxw=322)
    P2a = panel("#A89A7E", 342, 324, s2, o2, "2a · Michal at the window")
    s3 = f'''      {face(FX["__FACE_MICHAL__"], 392, 20, 0.8, flip=True)}'''
    o3 = shout("and she despised him in her heart.", "left: 12px; bottom: 16px", size=20, maxw=200)
    P2b = panel("radial-gradient(circle at 70% 45%, #C2456A 0 30px, #4A1D55 160px, #12090A 330px)", 342, 324, s3, o3, "2b · She despised him")
    body = P1 + cols(P2a, P2b)
    return mk.page("2 Samuel 6:14–16 — Dancing before Jehovah", "minmax(0, 1fr) 330px", body, 4)
PAGES["SB1-P04-Dancing"] = p04


# ───────────────────────── 05 · For Ever (7:1–18) ─────────────────────────
def p05():
    s1 = f'''      {D("e1")}
      {C.cedar(702, 284, 240)}
      {C.throne(200, 270, 0.9)}
      {person("e1", 200, 272, 0.72, **DK, extra=KING)}
      {person("e1", 380, 276, 0.72, **NATHAN, flip=True)}'''
    o1 = (cap("And it came to pass, when the king dwelt in his house, and Jehovah had given him rest from all his enemies round about, that the king said unto Nathan the prophet,", "left: 430px; top: 12px", size=9.5, maxw=260)
          + balloon("See now, I dwell in a house of cedar, but the ark of God dwelleth within curtains.", "left: 430px; top: 120px", 260, size=13, pad="18px 26px")
          + stamp(7, "left: 16px; top: 14px", rot=-4))
    P1 = panel("#8A4A26", 702, 284, s1, o1, "1 · A house of cedar")

    r = random.Random(5)
    s2 = f'''      {stars(120, 702, 300, 2501)}
      {J.moon(600, 70, 30)}
      {hills(330, "#1A2A1E", 2502, 40)}
      {"".join(E.sheep(r.uniform(20, 300), r.uniform(350, 390), 0.3, wool="#8A8A9A") for _ in range(8))}
      {B.david("e2", 160, 384, 0.4)}
      <g transform="translate(560 384) scale(0.7)">{C.throne(0, 0, 1)}</g>
      {V.rays(560, 260, 30, 30, 300, color="#FFF4C2", op=0.25)}'''
    s2 = f'''      {D("e2")}''' + s2
    o2 = (cap("Thus saith Jehovah of hosts, I took thee from the sheepcote, from following the sheep, that thou shouldest be prince over my people, over Israel;", "left: 12px; top: 12px", size=10.5, maxw=330)
          + god("And thy house and thy kingdom shall be made sure for ever before thee: thy throne shall be established for ever.", "right: 14px; top: 110px", size=18, maxw=330))
    P2 = panel("linear-gradient(180deg, #05050A 0%, #12113A 60%, #2A1A5E 100%)", 702, 414, s2, o2, "2 · For ever")

    s3 = f'''      {A.sanctuary(702, 264, 220, seed=25)}
      {J.ark(560, 220, 0.6, uid="fvA", glow=True)}
      {E.kneel(330, 226, 0.66, color="#4A2A7A", skin="#5A2A16")}'''
    o3 = (cap("Then David the king went in, and sat before Jehovah; and he said,", "left: 12px; top: 12px", size=10, maxw=260)
          + balloon("Who am I, O Lord Jehovah, and what is my house, that thou hast brought me thus far?", "left: 12px; top: 70px", 260, size=13, pad="18px 24px"))
    P3 = panel("#3A2214", 702, 264, s3, o3, "3 · Who am I")
    body = P1 + P2 + P3
    return mk.page("2 Samuel 7:1–18 — For Ever", "290px minmax(0, 1fr) 270px", body, 5)
PAGES["SB1-P05-ForEver"] = p05


# ───────────────────────── 06 · Mephibosheth (9:3–13) ─────────────────────────
def p06():
    s1 = f'''      {D("f1")}
      {C.cedar(702, 254, 220)}
      {C.throne(150, 246, 0.8)}
      {person("f1", 150, 248, 0.64, **DK, extra=KING)}
      {person("f1", 560, 250, 0.62, body="#3A1E14", cloth="#8A6A4A", kind="Tunic", sw=4)}'''
    o1 = (cap("And the king said,", "left: 230px; top: 12px", size=10)
          + balloon("Is there not yet any of the house of Saul, that I may show the kindness of God unto him?", "left: 230px; top: 44px", 210, size=12, pad="16px 20px")
          + cap("And Ziba said unto the king,", "right: 12px; top: 12px", size=9.5)
          + balloon("Jonathan hath yet a son, who is lame of his feet.", "right: 150px; top: 120px", 170, size=12, pad="14px 18px")
          + stamp(9, "left: 16px; top: 14px", rot=-4))
    P1 = panel("#8A4A26", 702, 254, s1, o1, "1 · The kindness of God")

    s2 = f'''      {D("f2")}
      {C.cedar(702, 294, 250)}
      {C.throne(560, 286, 0.9)}
      {person("f2", 560, 288, 0.74, **DK, extra=KING)}
      {N.prostrate(300, 284, 1.1, color="#1F5FAD", skin="#3A1E14")}'''
    o2 = (cap("And Mephibosheth, the son of Jonathan, the son of Saul, came unto David, and fell on his face, and did obeisance.", "left: 12px; top: 12px", size=10, maxw=300)
          + cap("And David said,", "right: 12px; top: 12px", size=10)
          + balloon("Mephibosheth.", "right: 160px; top: 40px", 150, size=15, pad="12px 14px")
          + cap("And he answered,", "left: 12px; top: 110px", size=10)
          + balloon("Behold, thy servant!", "left: 140px; top: 140px", 160, size=14, pad="12px 14px"))
    P2 = panel("#8A4A26", 702, 294, s2, o2, "2 · Behold, thy servant")

    s3 = f'''      {face(FX["__FACE_DAVID_KING__"], -50, 20, 0.74)}'''
    o3 = (cap("And David said unto him,", "right: 10px; top: 10px", size=10)
          + balloon("Fear not; for I will surely show thee kindness for Jonathan thy father's sake, and will restore thee all the land of Saul thy father; and thou shalt eat bread at my table continually.", "right: 6px; bottom: 10px", 200, size=11, pad="22px 22px"))
    P3a = panel("radial-gradient(circle at 30% 50%, #FFE680 0 20px, #7A3BA8 150px, #12113A 330px)", 342, 394, s3, o3, "3a · Fear not")
    s4 = f'''      {D("f4")}
      {C.cedar(342, 394, 330)}
      {person("f4", 100, 330, 0.7, **DK, extra=KING)}
      {person("f4", 240, 330, 0.66, body="#3A1E14", cloth="#1F5FAD", kind="Tunic", sw=4)}
      {C.table(171, 330, 300)}'''
    o4 = cap("So Mephibosheth dwelt in Jerusalem; for he did eat continually at the king's table. And he was lame in both his feet.", "left: 10px; top: 10px", size=10, maxw=322)
    P3b = panel("#8A4A26", 342, 394, s4, o4, "3b · The king's table")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("2 Samuel 9:3–13 — Mephibosheth", "260px 300px minmax(0, 1fr)", body, 6)
PAGES["SB1-P06-Mephibosheth"] = p06


# ───────────────────────── 07 · The Letter (11:1–27) ─────────────────────────
def p07():
    s1 = f'''      {D("g1")}
      {J.moon(600, 60, 26)}
      {C.roof(702, 294, 150, 2701)}
      {person("g1", 200, 214, 0.72, body="#1A1210", cloth="#2A1A4A", kind="Tunic", sw=3, extra=KING)}'''
    o1 = (cap("But David tarried at Jerusalem.", "left: 12px; top: 12px", size=12)
          + cap("And it came to pass at eventide, that David arose from off his bed, and walked upon the roof of the king's house: and from the roof he saw a woman bathing;", "right: 12px; top: 12px", size=10, maxw=320)
          + stamp(11, "left: 16px; top: 56px", rot=-4))
    P1 = panel("linear-gradient(180deg, #2A1A5E 0%, #8A3A6A 50%, #FF8A3D 100%)", 702, 294, s1, o1, "1 · Upon the roof")

    s2 = f'''      {C.letter(130, 130, 1.8, rot=-8)}
      {mk.arm([(-20, 260), (60, 200), (120, 180)], "#5A2A16", 22)}'''
    o2 = (cap("And it came to pass in the morning, that David wrote a letter to Joab, and sent it by the hand of Uriah. And he wrote in the letter, saying,", "left: 280px; top: 12px", size=10, maxw=400)
          + '    <div style="position: absolute; left: 280px; top: 100px; max-width: 400px; padding: 12px 16px; background: #F3E0B8; color: #5A1A16; border: 2px solid #0D0D0F; font-family: \'Archivo Narrow\', sans-serif; font-weight: 700; font-size: 17px; line-height: 1.2; text-transform: uppercase">Set ye Uriah in the forefront of the hottest battle, and retire ye from him, that he may be smitten, and die.</div>\n')
    P2 = panel("radial-gradient(circle at 20% 50%, #FFE3B8 0 30px, #8A4A26 200px, #2A1A1E 460px)", 702, 244, s2, o2, "2 · The letter")

    s3 = f'''      {J.jericho(300, 712, 60, 200, 2702, color="#8A5A3A", towers=2, houses=False)}
      <path d="M-10 200 L 712 200 L 712 234 L -10 234 Z" fill="#5A2A1E" stroke="#0D0D0F" stroke-width="2"></path>
      {B.spears_down(range(20, 300, 22), 210, 2703)}
      {N.prostrate(220, 214, 0.5, color="#2A1A1E")}'''
    o3 = cap("And the men of the city went out, and fought with Joab: and there fell some of the people, even of the servants of David; and Uriah the Hittite died also.", "left: 12px; top: 12px", size=10, maxw=280)
    P3 = panel("linear-gradient(180deg, #2A0A0A 0%, #B5121B 100%)", 702, 224, s3, o3, "3 · Uriah died also")

    s4 = f'''      {"".join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#2A2A3E" stroke="#0D0D0F" stroke-width="2"></ellipse>' for x, y, rx, ry in [(100, 40, 160, 50), (350, 20, 200, 60), (620, 40, 180, 50)])}
      <path d="M600 60 L 570 130 L 600 128 L 560 210" fill="none" stroke="#FFF4C2" stroke-width="5"></path>'''
    o4 = shout("But the thing that David had done displeased Jehovah.", "left: 14px; bottom: 16px", size=24, maxw=420)
    P4 = panel("linear-gradient(180deg, #05050A 0%, #2A2A3E 100%)", 702, 222, s4, o4, "4 · Displeased Jehovah")
    body = P1 + P2 + P3 + P4
    return mk.page("2 Samuel 11:1–27 — The Letter", "300px 250px 230px minmax(0, 1fr)", body, 7)
PAGES["SB1-P07-Letter"] = p07


# ───────────────────────── 08 · The Ewe Lamb (12:1–5) ─────────────────────────
def p08():
    s1 = f'''      {D("h1")}
      {C.cedar(702, 244, 210)}
      {C.throne(560, 236, 0.8)}
      {person("h1", 560, 238, 0.64, **DK, extra=KING)}
      {person("h1", 400, 240, 0.66, **NATHAN, up=[(-22, -158), (-40, -176), (-60, -184)], flip=True)}'''
    o1 = (cap("And Jehovah sent Nathan unto David. And he came unto him, and said unto him,", "left: 12px; top: 12px", size=10, maxw=300)
          + balloon("There were two men in one city; the one rich, and the other poor.", "left: 12px; top: 90px", 280, size=14, pad="18px 26px")
          + stamp(12, "right: 16px; top: 14px"))
    P1 = panel("#8A4A26", 702, 244, s1, o1, "1 · Two men in one city")

    r = random.Random(8)
    s2 = f'''      {D("h2")}
      <path d="M-10 250 L 712 250 L 712 424 L -10 424 Z" fill="#C8A86A" stroke="#5A3A22" stroke-width="2"></path>
      <path d="M351 -10 L 351 424" stroke="#5A3A22" stroke-width="3" stroke-dasharray="10 8"></path>
      {"".join(E.sheep(r.uniform(20, 320), r.uniform(270, 330), 0.4, flip=r.random() < 0.5) for _ in range(14))}
      {A.cow(110, 380, 0.5, color="#8A5A30")}{A.cow(250, 390, 0.54, flip=True)}
      {person("h2", 320, 400, 0.8, body="#3A1E14", cloth="#C8962E", kind="Robe", sw=4)}
      {person("h2", 500, 400, 0.82, body="#3A1E14", cloth="#8A7A6A", kind="Tunic", sw=4, up=C.HOLD_LAMB, extra=C.lamb_held(6, -128, 1.1))}
      {person("h2", 580, 404, 0.42, body="#3A1E14", cloth="#5A6E8A", kind="Tunic", sw=4)}{person("h2", 630, 404, 0.38, body="#3A1E14", cloth="#C2456A", woman=True, hair=True, sw=4)}
      <rect x="-10" y="-10" width="722" height="444" fill="#8A5A30" opacity="0.16"></rect>'''
    o2 = (cap("The rich man had exceeding many flocks and herds;", "left: 12px; top: 12px", size=11, maxw=300)
          + cap("but the poor man had nothing, save one little ewe lamb, which he had bought and nourished up: and it grew up together with him, and with his children; it did eat of his own morsel, and drank of his own cup, and lay in his bosom, and was unto him as a daughter.", "right: 12px; top: 12px", size=9.5, maxw=320)
          + cap("but took the poor man's lamb, and dressed it for the man that was come to him.", "left: 12px; top: 200px", size=10, maxw=300))
    P2 = panel("linear-gradient(180deg, #F3E0B8 0%, #E8C890 100%)", 702, 424, s2, o2, "2 · One little ewe lamb")

    s3 = f'''      {mk.speed(200, 150, 50, 140, 600, 2801, color="#FFD23F", op=0.35)}
      {face(FX["__FACE_DAVID_KING_WRATH__"], -40, -10, 0.8)}'''
    o3 = (cap("And David's anger was greatly kindled against the man; and he said to Nathan,", "right: 12px; top: 12px", size=10.5, maxw=300)
          + tail(330, 180, "l")
          + balloon("As Jehovah liveth, the man that hath done this is worthy to die:", "left: 370px; top: 100px", 300, size=16, pad="22px 30px"))
    P3 = panel("radial-gradient(circle at 25% 50%, #FFD23F 0 30px, #D7261E 200px, #2A0A0A 460px)", 702, 294, s3, o3, "3 · Worthy to die")
    body = P1 + P2 + P3
    return mk.page("2 Samuel 12:1–5 — The Ewe Lamb", "250px minmax(0, 1fr) 300px", body, 8)
PAGES["SB1-P08-Lamb"] = p08


# ───────────────────────── 09 · Thou Art the Man (12:7–24) ─────────────────────────
def p09():
    s1 = f'''      {mk.speed(520, 150, 60, 140, 700, 2901, color="#FFF4C2", op=0.45)}
      {face(FX["__FACE_NATHAN_STERN__"], 760, -20, 0.8, flip=True)}
      {mk.arm([(620, 300), (480, 270), (350, 240)], "#3A1E14", 26)}
      <path d="M680 330 L 580 290 L 540 276 L 560 330 Z" fill="#5E7A4A" stroke="#0D0D0F" stroke-width="2.4"></path>'''
    o1 = (cap("And Nathan said to David,", "left: 12px; top: 12px", size=11)
          + shout("Thou art the man.", "left: 12px; top: 56px", size=48, maxw=300)
          + sfx("ドン", "DON", "left: 40px; bottom: 30px", size=56, fill="#F3EFE6", stroke="#0D0D0F", rot=-8, align="flex-start"))
    P1 = panel("radial-gradient(circle at 75% 45%, #FFF4C2 0 40px, #FFD23F 160px, #D7261E 360px, #2A0A0A 560px)", 702, 314, s1, o1, "1 · Thou art the man")

    s2 = f'''      {stars(60, 702, 214, 2902)}'''
    o2 = (cap("Thus saith Jehovah, the God of Israel,", "left: 12px; top: 12px", size=10)
          + god("Wherefore hast thou despised the word of Jehovah, to do that which is evil in his sight?", "left: 12px; top: 48px", size=20, maxw=640))
    P2 = panel("linear-gradient(180deg, #05050A 0%, #12113A 100%)", 702, 214, s2, o2, "2 · Wherefore hast thou despised")

    s3 = f'''      {face(FX["__FACE_DAVID_KING_GRIEF__"], -50, 0, 0.7)}'''
    o3 = (cap("And David said unto Nathan,", "right: 10px; top: 10px", size=10)
          + balloon("I have sinned against Jehovah.", "right: 10px; bottom: 16px", 160, size=15, pad="18px 16px"))
    P3a = panel("radial-gradient(circle at 30% 50%, #C8D0DE 0 20px, #5A6E8A 150px, #12113A 330px)", 342, 244, s3, o3, "3a · I have sinned")
    s4 = f'''      {face(FX["__FACE_NATHAN__"], 392, 0, 0.7, flip=True)}'''
    o4 = (cap("And Nathan said unto David,", "left: 10px; top: 10px", size=10)
          + balloon("Jehovah also hath put away thy sin; thou shalt not die.", "left: 10px; bottom: 14px", 180, size=13.5, pad="18px 18px"))
    P3b = panel("radial-gradient(circle at 70% 50%, #FFF4C2 0 20px, #8FD0E2 150px, #2A3A6A 330px)", 342, 244, s4, o4, "3b · Thou shalt not die")

    s5 = f'''      {D("i5")}
      {V.rays(120, 120, 30, 30, 400, color="#FFF4C2", op=0.4)}
      <path d="M-10 170 L 712 170 L 712 214 L -10 214 Z" fill="#8A5A30"></path>
      {mk.person("i5", 120, 206, 0.8, body="#3A1E14", cloth="#C2456A", woman=True, hair="#2A1A10", sw=4, up=R.HOLD_BABY, extra=R.baby(10, -130, 0.8))}'''
    o5 = (cap("and she bare a son, and he called his name Solomon. And Jehovah loved him;", "left: 220px; top: 14px", size=12, maxw=320)
          + badge("ソロモン", "left: 220px; top: 100px", size=20)
          + end_mark("TO BE CONTINUED", "right: 14px; bottom: 12px", ch="つづく"))
    P4 = panel("radial-gradient(circle at 17% 50%, #FFF4C2 0 30px, #FFC14D 160px, #FF8A3D 420px)", 702, 204, s5, o5, "4 · Solomon")
    body = P1 + P2 + cols(P3a, P3b) + P4
    return mk.page("2 Samuel 12:7–24 — Thou Art the Man", "320px 220px 250px minmax(0, 1fr)", body, 9)
PAGES["SB1-P09-Man"] = p09


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "2samuel/project"))
