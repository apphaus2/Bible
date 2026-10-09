"""Judges Book One — The Sword of Gideon (Judges 4–8). Writes the .dc.html pages into the given folder.
Usage: python3 judges_book1.py <out_dir>"""
import sys, pathlib, random
import mk, exodus as E, exodus3 as Y, exodus4 as Z, exodus5 as V, numbers1 as N, joshua1 as J, judges1 as G
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, speed, stars
from exodus_book3 import crowd
from numbers_book1 import badge, hills
FX = G.tokens()
PAGES = {}
DEBORAH = dict(body="#3A1E14", cloth="#E8B830", woman=True, hair=True)
GIDEON = dict(body="#2A140C", cloth="#C9A86A", kind="Tunic")
MIDIAN = ("#B5121B", "#7A3BA8", "#1F5FAD", "#E8B830")
WAR = ("#8A3A1E", "#5A2A16", "#3A2214", "#5A6E8A")


def shout(text, pos, size=30, maxw=320):
    return (f'    <div style="position: absolute; {pos}; padding: 10px 16px; background: #12113A; color: #FFD23F; box-shadow: inset 0 0 0 3px #FFD23F; '
            f'font-family: Anton, sans-serif; font-size: {size}px; line-height: 1.05; text-transform: uppercase; max-width: {maxw}px">{text}</div>\n')


def midian_camp(n, x0, x1, y0, y1, seed):
    r = random.Random(seed); items = sorted((r.uniform(y0, y1), r.uniform(x0, x1), r.random()) for _ in range(n)); o = []
    for y, x, q in items:
        k = (y - y0) / max(1, y1 - y0)
        if q < 0.3:
            o.append(G.camel(x, y, 0.2 + 0.25 * k, flip=q < 0.15, color="#8A6A4A"))
        else:
            w = 30 + 50 * k; o.append(Z.tent(x, y, w, w * 0.7, color=r.choice(["#2A1A2E", "#3A2A3E", "#4A2A1A"])))
    return "".join(o)


# ───────────────────────── Cover ─────────────────────────
def cover():
    r = random.Random(9)
    men = "".join(G.torchbearer("c1", x, y, sc, flip=x > 380, cloth=r.choice(WAR), seed=i)
                  + G.pitcher(x + (40 if x < 380 else -40) * sc, y - 4, 0.7 * sc, broken=True, seed=i)
                  for i, (x, y, sc) in enumerate([(60, 1010, 0.9), (160, 1036, 1.0), (260, 1000, 0.82), (500, 1000, 0.82), (600, 1036, 1.0), (700, 1010, 0.9)]))
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {defs("c1", "Man", "ManUp", "Robe", "Tunic")}
    {stars(90, 760, 600, 91)}
    {V.rays(380, 760, 40, 60, 900, color="#FFC14D", op=0.18)}
    <path d="M-10 820 C 200 790 500 800 770 780 L 770 1090 L -10 1090 Z" fill="#2A1A2E" stroke="#0D0D0F" stroke-width="2"></path>
    {midian_camp(30, 0, 760, 790, 860, 92)}
    <path d="M-10 880 C 200 870 500 886 770 876 L 770 1090 L -10 1090 Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></path>
    {men}
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The Book of</span>
    <span>No. 01</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 160px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6">JUDGES</h1>
  <div style="position: absolute; top: 246px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 262px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book One — The Sword of Gideon</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 4 – 8</span>
  </div>
  <div style="position: absolute; top: 236px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>士</span><span>師</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">SHISHIKI</span>
  </div>
  <div style="position: absolute; left: 38px; top: 330px; padding: 10px 14px; background: #12113A; color: #FFD23F; box-shadow: inset 0 0 0 3px #FFD23F; font-family: Anton, 'Archivo Narrow', sans-serif; font-size: 30px; line-height: 1.05; text-transform: uppercase; max-width: 280px">The sword of Jehovah and of Gideon.</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 1</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #05050A 0%, #12113A 40%, #4A1D55 70%, #B5421E 100%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Judges Book One — Cover", None, body, root_style=root)
PAGES["Main"] = cover


# ───────────────────────── 01 · The Palm-tree of Deborah (4:4–9) ─────────────────────────
def p01():
    s1 = f'''      {defs("d1", "Man", "Woman", "Hair", "Robe", "Tunic")}
      {hills(170, "#8A6A4A", 101, 40)}
      <path d="M-10 200 C 200 190 500 206 712 196 L 712 264 L -10 264 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {G.palm(150, 250, 1.0)}
      {person("d1", 210, 250, 0.62, stroke="#0D0D0F", **DEBORAH)}
      {crowd("d1", 18, 330, 712, 214, 256, 102, 0.24, 0.42)}'''
    o1 = (cap("Now Deborah, a prophetess, the wife of Lappidoth, she judged Israel at that time. And she dwelt under the palm-tree of Deborah between Ramah and Beth-el in the hill-country of Ephraim: and the children of Israel came up to her for judgment.", "right: 12px; top: 12px", maxw=400)
          + stamp(4, "left: 16px; top: 14px", rot=-4))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 70%)", 702, 254, s1, o1, "1 · Under the palm-tree")

    s2 = f'''      {face(FX["__FACE_DEBORAH__"], -70, 20, 0.7)}'''
    o2 = (cap("And she sent and called Barak the son of Abinoam out of Kedesh-naphtali, and said unto him,", "left: 10px; top: 8px", size=9.5, maxw=320)
          + tail(118, 188, "l")
          + balloon("Hath not Jehovah, the God of Israel, commanded, saying, Go and draw unto mount Tabor, and take with thee ten thousand men of the children of Naphtali and of the children of Zebulun?", "left: 128px; top: 70px", 208, size=10, pad="26px 16px"))
    P2a = panel("radial-gradient(circle at 30% 50%, #FFF4C2 0 20px, #FFC14D 150px, #4A1D55 330px)", 342, 314, s2, o2, "2a · Deborah calls Barak")
    s3 = f'''      {face(FX["__FACE_BARAK__"], 412, 30, 0.7, flip=True)}'''
    o3 = (cap("And Barak said unto her,", "left: 10px; top: 10px", size=10)
          + tail(196, 196, "r")
          + balloon("If thou wilt go with me, then I will go; but if thou wilt not go with me, I will not go.", "left: 8px; top: 70px", 196, size=13, pad="22px 18px"))
    P2b = panel("radial-gradient(circle at 70% 50%, #E8C8A0 0 20px, #5A6E8A 160px, #12113A 330px)", 342, 314, s3, o3, "2b · If thou wilt go with me")

    s4 = f'''      {defs("d4", "Man", "Woman", "Hair", "Robe", "Tunic")}
      {G.tabor(560, 300, 300, 200)}
      <path d="M-10 290 C 200 280 500 296 712 286 L 712 404 L -10 404 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("d4", 120, 390, 0.8, stroke="#0D0D0F", **DEBORAH)}
      {person("d4", 200, 396, 0.86, body="#2A140C", cloth="#5A6E8A", kind="Tunic", sw=4, extra=Z.SPEAR)}'''
    o4 = (cap("And she said,", "right: 12px; top: 12px", size=10)
          + tail(150, 136, "dl")
          + balloon("I will surely go with thee: notwithstanding, the journey that thou takest shall not be for thine honor; for Jehovah will sell Sisera into the hand of a woman.", "left: 12px; top: 12px", 400, size=14, pad="22px 40px")
          + cap("And Deborah arose, and went with Barak to Kedesh.", "right: 12px; bottom: 12px", size=11))
    P3 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 394, s4, o4, "3 · Into the hand of a woman")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Judges 4:4–9 — The Palm-tree of Deborah", "260px 320px minmax(0, 1fr)", body, 1)
PAGES["JG1-P01-Deborah"] = p01


# ───────────────────────── 02 · This Is the Day (4:14–15) ─────────────────────────
def p02():
    s1 = f'''      {face(FX["__FACE_DEBORAH__"], -60, 0, 0.82)}
      {V.rays(160, 150, 24, 60, 500, color="#FFF4C2", op=0.25)}'''
    o1 = (cap("And Deborah said unto Barak,", "right: 12px; top: 12px")
          + tail(250, 170, "l")
          + balloon("Up; for this is the day in which Jehovah hath delivered Sisera into thy hand; is not Jehovah gone out before thee?", "left: 290px; top: 70px", 390, size=18, pad="24px 40px"))
    P1 = panel("radial-gradient(circle at 25% 45%, #FFF4C2 0 30px, #FFC14D 200px, #B5421E 460px)", 702, 274, s1, o1, "1 · Up; for this is the day")

    s2 = f'''      {defs("t2", "Man", "ManUp", "Robe", "Tunic")}
      {speed(140, 60, 60, 120, 800, 201, color="#FFF4C2", sw=2, op=0.5)}
      <path d="M-10 60 C 120 40 200 80 330 200 C 440 300 560 340 712 360 L 712 404 L -10 404 Z" fill="#3F6A3A" stroke="#0D0D0F" stroke-width="2.4"></path>
      {Z.warriors("t2", 36, 40, 600, 90, 390, 202, 0.18, 0.6)}
      {person("t2", 640, 400, 0.9, body="#2A140C", cloth="#5A6E8A", kind="Tunic", sw=4, up=[(-22, -158), (-46, -196), (-60, -240)], extra=Z.SHIELD)}'''
    o2 = (cap("So Barak went down from mount Tabor, and ten thousand men after him.", "left: 12px; top: 12px", size=12, maxw=300)
          + sfx("ドドドド", "DODODODO", "right: 18px; top: 22px", size=46, fill="#F3EFE6", stroke="#0D0D0F", rot=8)
          + badge("一万人", "left: 12px; bottom: 12px", size=18))
    P2 = panel("linear-gradient(180deg, #FF8A3D 0%, #FFC14D 60%, #FFE3B8 100%)", 702, 394, s2, o2, "2 · Down from mount Tabor")

    s3 = f'''      {defs("t3", "Man", "Robe", "Tunic")}
      <path d="M-10 230 L 712 230 L 712 284 L -10 284 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>
      {Y.chariot(200, 270, 0.7, color="#2A2A3A", driver="#3A3A4A")}
      {Y.chariot(420, 262, 0.6, color="#2A2A3A", driver="#3A3A4A")}
      <g transform="rotate(14 600 250)">{Y.chariot(620, 270, 0.6, color="#2A2A3A", driver="#3A3A4A")}</g>
      {person("t3", 80, 270, 0.6, body="#12090A", cloth="#3A3A4A", kind="Tunic", sw=4, flip=True)}
      {speed(80, 180, 30, 40, 200, 203, color="#0D0D0F", sw=1.6, op=0.35)}'''
    o3 = (cap("And Jehovah discomfited Sisera, and all his chariots, and all his host, with the edge of the sword before Barak; and Sisera alighted from his chariot, and fled away on his feet.", "right: 12px; top: 12px", maxw=440)
          + ref("JDG 4:15", "left: 12px; top: 12px", color="#0D0D0F", bg="#F3EFE6"))
    P3 = panel("linear-gradient(180deg, #5A0E16 0%, #C2456A 60%, #FF8A3D 100%)", 702, 274, s3, o3, "3 · Sisera fled away on his feet")
    body = P1 + P2 + P3
    return mk.page("Judges 4:14–15 — This Is the Day", "280px minmax(0, 1fr) 280px", body, 2)
PAGES["JG1-P02-Tabor"] = p02


# ───────────────────────── 03 · The Tent of Jael (4:17–21) ─────────────────────────
def p03():
    s1 = f'''      {defs("j1", "Man", "Woman", "Hair", "Robe", "Tunic")}
      {stars(30, 702, 120, 301)}
      <path d="M-10 230 L 712 230 L 712 294 L -10 294 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>
      {G.tent_big(560, 240, 220, 170, glow="#FFC14D")}
      {person("j1", 600, 250, 0.5, body="#2A140C", cloth="#2E6A32", woman=True, hair=True)}
      {person("j1", 200, 250, 0.56, body="#12090A", cloth="#3A3A4A", kind="Tunic", sw=4)}
      {speed(40, 150, 30, 40, 200, 302, color="#F3EFE6", sw=1.4, op=0.3)}'''
    o1 = cap("Howbeit Sisera fled away on his feet to the tent of Jael the wife of Heber the Kenite; for there was peace between Jabin the king of Hazor and the house of Heber the Kenite.", "left: 12px; top: 12px", maxw=380)
    P1 = panel("linear-gradient(180deg, #12113A 0%, #4A1D55 60%, #C2456A 100%)", 702, 284, s1, o1, "1 · The tent of Jael")

    s2 = f'''      {face(FX["__FACE_JAEL__"], -70, 20, 0.72)}'''
    o2 = (cap("And Jael went out to meet Sisera, and said unto him,", "left: 10px; top: 10px", size=10, maxw=300)
          + tail(118, 180, "l")
          + balloon("Turn in, my lord, turn in to me; fear not.", "left: 152px; top: 130px", 180, size=15, pad="20px 16px"))
    P2a = panel("radial-gradient(circle at 30% 50%, #FFE680 0 20px, #B5421E 160px, #2A0A0A 330px)", 342, 294, s2, o2, "2a · Turn in, my lord")
    s3 = f'''      <rect width="342" height="304" fill="#3A2214"></rect>
      <path d="M-10 0 L 171 -40 L 352 0 L 352 60 L -10 60 Z" fill="#2A140C"></path>
      <path d="M-10 230 L 352 230 L 352 304 L -10 304 Z" fill="#5A3A22"></path>
      {G.rug_sleeper(170, 250, 1.2)}'''
    o3 = cap("And he turned in unto her into the tent, and she covered him with a rug.", "left: 10px; top: 10px", size=10.5, maxw=320)
    P2b = panel("#3A2214", 342, 294, s3, o3, "2b · Covered with a rug")

    hand = '<g transform="translate(-44 -240)">' + G.HAMMER + '</g>'
    pin = '<g transform="translate(26 -100) rotate(160)">' + G.PIN + '</g>'
    s4 = f'''      {defs("j4", "Woman", "WomanUp", "Hair", "Robe")}
      <rect width="702" height="404" fill="#12090A"></rect>
      <path d="M200 404 L 351 40 L 502 404 Z" fill="#B5421E" opacity="0.55"></path>
      {person("j4", 351, 380, 1.3, body="#05050A", cloth="#05050A", woman=True, hair="#05050A", up=[(-22, -158), (-40, -200), (-44, -240)], extra=hand + pin, stroke="#FF8A3D", sw=2)}'''
    o4 = (cap("Then Jael Heber's wife took a tent-pin, and took a hammer in her hand, and went softly unto him, and smote the pin into his temples, and it pierced through into the ground; for he was in a deep sleep; so he swooned and died.", "left: 12px; top: 12px", maxw=250)
          + ref("JDG 4:21", "right: 12px; bottom: 9px"))
    P3 = panel("#12090A", 702, 394, s4, o4, "3 · A tent-pin and a hammer")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Judges 4:17–21 — The Tent of Jael", "290px 300px minmax(0, 1fr)", body, 3)
PAGES["JG1-P03-Jael"] = p03


# ───────────────────────── 04 · Thou Mighty Man of Valor (6:11–15) ─────────────────────────
def p04():
    s1 = f'''      {defs("g1", "Man", "ManUp", "Robe", "Tunic", "Hair")}
      <path d="M-10 230 C 200 220 500 236 712 226 L 712 304 L -10 304 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>
      {J.oak(130, 270, 0.9, 401)}
      <g opacity="0.85">{N.angel("g1", 180, 270, 0.5, sword=False)}</g>
      {G.winepress(480, 268, 260, 70)}
      {person("g1", 480, 284, 0.5, **GIDEON, sw=4, up=[(-22, -158), (-44, -200), (-30, -250)], extra='<path d="M-30 -250 L 10 -170" stroke="#5A3A22" stroke-width="6" stroke-linecap="round"></path>')}
      {G.wheat(420, 262, 0.5, seed=402)}{G.wheat(540, 264, 0.5, seed=403)}
      {G.chaff(40, 400, 580, 150, 240, 404)}'''
    o1 = (cap("And the angel of Jehovah came, and sat under the oak which was in Ophrah, that pertained unto Joash the Abiezrite: and his son Gideon was beating out wheat in the winepress, to hide it from the Midianites.", "right: 12px; top: 12px", maxw=330)
          + stamp(6, "left: 16px; top: 14px", rot=-4))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 70%)", 702, 294, s1, o1, "1 · In the winepress")

    s2 = f'''      {V.rays(171, 170, 30, 40, 400, color="#FFFFFF", op=0.5)}'''
    o2 = (cap("And the angel of Jehovah appeared unto him, and said unto him,", "left: 10px; top: 10px", size=10, maxw=300)
          + god("Jehovah is with thee, thou mighty man of valor.", "left: 10px; top: 90px", size=24, maxw=300))
    P2a = panel("radial-gradient(circle at 50% 55%, #FFFFFF 0 40px, #FFF4C2 140px, #FFC14D 260px, #C2456A 360px)", 342, 294, s2, o2, "2a · Thou mighty man of valor")
    s3 = f'''      {face(FX["__FACE_GIDEON__"], 412, 20, 0.74, flip=True)}'''
    o3 = sfx("エッ", "EH?", "left: 20px; top: 30px", size=44, fill="#F3EFE6", stroke="#0D0D0F", rot=-8, align="flex-start") + ref("GIDEON", "left: 10px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6")
    P2b = panel("radial-gradient(circle at 70% 45%, #FFF4C2 0 20px, #E8A35A 160px, #4A1D55 330px)", 342, 294, s3, o3, "2b · Gideon")

    s4 = f'''      {face(FX["__FACE_GIDEON__"], -60, 20, 0.8)}'''
    o4 = (cap("And Jehovah looked upon him, and said,", "right: 12px; top: 12px", size=10)
          + god("Go in this thy might, and save Israel from the hand of Midian: have not I sent thee?", "right: 12px; top: 48px", size=17, maxw=380)
          + cap("And he said unto him,", "left: 270px; top: 168px", size=10)
          + tail(252, 236, "l")
          + balloon("Oh, Lord, wherewith shall I save Israel? behold, my family is the poorest in Manasseh, and I am the least in my father's house.", "left: 290px; top: 204px", 400, size=14, pad="22px 40px"))
    P3 = panel("radial-gradient(circle at 25% 50%, #FFF4C2 0 30px, #FFC14D 200px, #4A1D55 460px)", 702, 394, s4, o4, "3 · Have not I sent thee?")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Judges 6:11–15 — Thou Mighty Man of Valor", "300px 300px minmax(0, 1fr)", body, 4)
PAGES["JG1-P04-Valor"] = p04


# ───────────────────────── 05 · The Fleece (6:36–40) ─────────────────────────
def p05():
    s1 = f'''      {stars(70, 702, 200, 501)}
      <path d="M-10 230 C 200 220 500 236 712 226 L 712 304 L -10 304 Z" fill="#3A2A2E" stroke="#0D0D0F" stroke-width="2"></path>
      <ellipse cx="520" cy="262" rx="150" ry="24" fill="#5A4A3E" stroke="#0D0D0F" stroke-width="2"></ellipse>
      {G.fleece(520, 262, 1.0, wet=False)}
      {E.kneel(330, 270, 0.62, color="#3A2214", skin="#C98E66")}'''
    o1 = (cap("And Gideon said unto God,", "left: 12px; top: 12px", size=10)
          + balloon("If thou wilt save Israel by my hand, as thou hast spoken, behold, I will put a fleece of wool on the threshing-floor; if there be dew on the fleece only, and it be dry upon all the ground, then shall I know that thou wilt save Israel by my hand, as thou hast spoken.", "left: 12px; top: 46px", 470, size=11.5, pad="24px 48px"))
    P1 = panel("linear-gradient(180deg, #05050A 0%, #12113A 100%)", 702, 294, s1, o1, "1 · A fleece of wool")

    wring = [(-22, -158), (-6, -140), (10, -128)]
    s2 = f'''      {defs("f2", "Man", "ManUp", "Robe", "Tunic")}
      <path d="M-10 190 L 712 190 L 712 254 L -10 254 Z" fill="#8A6A4A"></path>
      {G.dew(60, 0, 712, 196, 250, 502)}
      {person("f2", 300, 240, 0.8, **GIDEON, sw=4, up=wring, extra=G.fleece(10, -122, 0.36, wet=True, seed=3))}
      {G.bowl(360, 244, 60)}
      {"".join(f'<path d="M{x} 120 L {x} 210" stroke="#8FD0E2" stroke-width="2.5" stroke-dasharray="4 8"></path>' for x in (306, 312, 318))}'''
    o2 = (cap("And it was so; for he rose up early on the morrow, and pressed the fleece together, and wrung the dew out of the fleece, a bowlful of water.", "right: 12px; top: 12px", maxw=320)
          + sfx("ジャーッ", "JAAA", "left: 40px; top: 30px", size=38, fill="#8FD0E2", stroke="#0D0D0F", rot=-6, align="flex-start"))
    P2 = panel("linear-gradient(180deg, #FFC98A 0%, #FFE3B8 100%)", 702, 244, s2, o2, "2 · A bowlful of water")

    s3 = f'''      {face(FX["__FACE_GIDEON__"], -70, 60, 0.66)}'''
    o3 = (cap("And Gideon said unto God,", "left: 10px; top: 10px", size=10)
          + tail(154, 180, "l")
          + balloon("Let not thine anger be kindled against me, and I will speak but this once: let me make trial, I pray thee, but this once with the fleece; let it now be dry only upon the fleece, and upon all the ground let there be dew.", "left: 186px; top: 42px", 210, size=11, pad="24px 18px"))
    P3a = panel("radial-gradient(circle at 25% 55%, #FFF4C2 0 20px, #8FA0E2 160px, #12113A 360px)", 402, 334, s3, o3, "3a · But this once")
    s4 = f'''      {stars(30, 288, 120, 503)}
      <path d="M-10 200 L 298 200 L 298 344 L -10 344 Z" fill="#3A2A2E"></path>
      {G.dew(120, 0, 288, 206, 340, 504)}
      <ellipse cx="144" cy="270" rx="100" ry="22" fill="#5A4A3E" stroke="#0D0D0F" stroke-width="2"></ellipse>
      {G.fleece(144, 270, 0.9, wet=False, seed=5)}'''
    o4 = cap("And God did so that night: for it was dry upon the fleece only, and there was dew on all the ground.", "left: 10px; top: 10px", size=10, maxw=260)
    P3b = panel("linear-gradient(180deg, #05050A 0%, #2A1A5E 100%)", 288, 334, s4, o4, "3b · Dew on all the ground")
    body = P1 + P2 + cols(P3a, P3b, tmpl="minmax(0, 1.4fr) minmax(0, 1fr)")
    return mk.page("Judges 6:36–40 — The Fleece", "300px 250px minmax(0, 1fr)", body, 5)
PAGES["JG1-P05-Fleece"] = p05


# ───────────────────────── 06 · Three Hundred Men (7:2, 7:5–7) ─────────────────────────
def p06():
    s1 = f'''      {defs("h1", "Man", "Robe", "Tunic")}
      {stars(40, 702, 120, 601)}
      <path d="M-10 200 L 712 200 L 712 274 L -10 274 Z" fill="#3A2214"></path>
      {Z.warriors("h1", 60, -10, 712, 200, 270, 602, 0.12, 0.3)}'''
    o1 = god("The people that are with thee are too many for me to give the Midianites into their hand, lest Israel vaunt themselves against me, saying, Mine own hand hath saved me.", "left: 12px; top: 12px", size=16, maxw=520) + stamp(7, "right: 16px; bottom: 14px")
    P1 = panel("linear-gradient(180deg, #12113A 0%, #4A1D55 100%)", 702, 264, s1, o1, "1 · Too many")

    r = random.Random(603)
    kneelers = "".join(E.kneel(x, 330 + r.uniform(-6, 10), r.uniform(0.34, 0.44), color=r.choice(["#3A2214", "#5A2A16", "#4A2A1A"])) for x in range(30, 380, 44))
    lappers = "".join(G.drinker_lap("h2", x, 300 + (i % 2) * 14, 0.62, flip=True, cloth=WAR[i % 4]) for i, x in enumerate(range(470, 700, 52)))
    s2 = f'''      {defs("h2", "Man", "ManUp", "Robe", "Tunic")}
      <path d="M-10 240 L 712 240 L 712 444 L -10 444 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M-10 340 C 200 330 500 360 712 340 L 712 444 L -10 444 Z" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M40 380 C 160 372 300 392 460 380 M200 410 C 320 402 480 420 640 408" fill="none" stroke="#E8F6FA" stroke-width="2" opacity="0.6"></path>
      {kneelers}
      {lappers}'''
    o2 = (cap("So he brought down the people unto the water: and Jehovah said unto Gideon, Every one that lappeth of the water with his tongue, as a dog lappeth, him shalt thou set by himself; likewise every one that boweth down upon his knees to drink.", "left: 12px; top: 12px", size=10, maxw=320)
          + cap("And the number of them that lapped, putting their hand to their mouth, was three hundred men: but all the rest of the people bowed down upon their knees to drink water.", "right: 12px; top: 12px", size=10, maxw=270))
    P2 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 60%)", 702, 434, s2, o2, "2 · They that lapped")

    s3 = f'''      {V.rays(560, 140, 30, 40, 500, color="#FFE680", op=0.3)}'''
    o3 = (cap("And Jehovah said unto Gideon,", "left: 12px; top: 12px", size=10)
          + god("By the three hundred men that lapped will I save you, and deliver the Midianites into thy hand; and let all the people go every man unto his place.", "left: 12px; top: 50px", size=17, maxw=440)
          + badge("三百人", "right: 20px; bottom: 20px", size=34))
    P3 = panel("linear-gradient(180deg, #4A1D55 0%, #C2456A 60%, #FF8A3D 100%)", 702, 274, s3, o3, "3 · Three hundred")
    body = P1 + P2 + P3
    return mk.page("Judges 7:2–7 — Three Hundred Men", "270px minmax(0, 1fr) 280px", body, 6)
PAGES["JG1-P06-Three"] = p06


# ───────────────────────── 07 · The Sword of Jehovah and of Gideon (7:16–20) ─────────────────────────
def p07():
    s1 = f'''      {defs("k1", "Man", "ManUp", "Robe", "Tunic")}
      {stars(40, 702, 160, 701)}
      <path d="M-10 210 L 712 210 L 712 264 L -10 264 Z" fill="#2A1A2E"></path>
      {"".join(G.pitcher(x, 250, 0.6, seed=x) + J.shofar(x + 14, 248, 0.5, rot=-10) for x in range(300, 700, 46))}
      {person("k1", 120, 258, 0.9, **GIDEON, sw=4, up=[(-22, -158), (-56, -176), (-84, -196)])}'''
    o1 = cap("And he divided the three hundred men into three companies, and he put into the hands of all of them trumpets, and empty pitchers, with torches within the pitchers.", "left: 180px; top: 12px", maxw=500)
    P1 = panel("linear-gradient(180deg, #05050A 0%, #12113A 100%)", 702, 254, s1, o1, "1 · Trumpets, pitchers and torches")

    r = random.Random(702)
    men = "".join(G.torchbearer("k2", x, y, sc, flip=x > 351, cloth=r.choice(WAR), seed=i)
                  + G.pitcher(x + (36 if x < 351 else -36) * sc, y - 2, 0.7 * sc, broken=True, seed=i)
                  for i, (x, y, sc) in enumerate([(50, 600, 0.9), (150, 630, 1.05), (250, 590, 0.82), (450, 590, 0.82), (550, 630, 1.05), (650, 600, 0.9)]))
    s2 = f'''      {defs("k2", "Man", "ManUp", "Robe", "Tunic")}
      {stars(60, 702, 260, 703)}
      {V.rays(351, 420, 40, 60, 700, color="#FFC14D", op=0.22)}
      <path d="M-10 420 C 200 400 500 410 712 396 L 712 644 L -10 644 Z" fill="#2A1A2E" stroke="#0D0D0F" stroke-width="2"></path>
      {midian_camp(24, 0, 712, 400, 470, 704)}
      <path d="M-10 480 C 200 470 500 486 712 476 L 712 644 L -10 644 Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></path>
      {men}
      {"".join(J.blasts(x, 380, 1.1) for x in (110, 520))}'''
    o2 = (cap("So Gideon, and the hundred men that were with him, came unto the outermost part of the camp in the beginning of the middle watch, when they had but newly set the watch: and they blew the trumpets, and brake in pieces the pitchers that were in their hands.", "left: 12px; top: 12px", size=10, maxw=330)
          + cap("And the three companies blew the trumpets, and brake the pitchers, and held the torches in their left hands, and the trumpets in their right hands wherewith to blow; and they cried,", "right: 12px; top: 12px", size=10, maxw=300)
          + shout("The sword of Jehovah and of Gideon.", "right: 12px; top: 170px", size=34, maxw=320)
          + sfx("ガシャーン", "GASHAAN", "left: 20px; top: 210px", size=44, fill="#F3EFE6", stroke="#0D0D0F", rot=-8, align="flex-start")
          + sfx("ブオーッ", "BUOOO", "left: 250px; top: 300px", size=38, fill="#FFE680", stroke="#0D0D0F", rot=6, align="flex-start"))
    P2 = panel("linear-gradient(180deg, #05050A 0%, #12113A 50%, #4A1D55 100%)", 702, 634, s2, o2, "2 · The sword of Jehovah and of Gideon")
    body = P1 + P2
    return mk.page("Judges 7:16–20 — The Sword of Jehovah and of Gideon", "260px minmax(0, 1fr)", body, 7)
PAGES["JG1-P07-Sword"] = p07


# ───────────────────────── 08 · Jehovah Shall Rule (7:21, 8:22–28) ─────────────────────────
def p08():
    r = random.Random(801)
    fleeing = "".join(G.camel(x, 250 + r.uniform(-10, 20), r.uniform(0.4, 0.55), flip=True, color="#8A6A4A", rider=r.choice(MIDIAN)) for x in range(120, 700, 120))
    s1 = f'''      {defs("z1", "Man", "Robe", "Tunic")}
      {V.rays(700, 280, 30, 40, 600, color="#FFC14D", op=0.3)}
      <path d="M-10 240 L 712 240 L 712 294 L -10 294 Z" fill="#3A2214"></path>
      {midian_camp(10, 400, 712, 230, 250, 802)}
      {fleeing}
      {speed(0, 200, 40, 50, 300, 803, color="#F3EFE6", sw=1.4, op=0.3)}'''
    o1 = (cap("And they stood every man in his place round about the camp; and all the host ran; and they shouted, and put them to flight.", "left: 12px; top: 12px", maxw=420)
          + sfx("ワーッ", "WAAA!", "right: 18px; top: 18px", size=42, fill="#D7261E", stroke="#F3EFE6", rot=8, tagbg="#0D0D0F", tagfg="#F3EFE6"))
    P1 = panel("linear-gradient(180deg, #12113A 0%, #4A1D55 50%, #FF8A3D 100%)", 702, 284, s1, o1, "1 · All the host ran")

    s2 = f'''      {defs("z2", "Man", "ManUp", "Woman", "Hair", "Robe", "Tunic")}
      <path d="M-10 220 L 352 220 L 352 324 L -10 324 Z" fill="#C8A06A"></path>
      {"".join(person("z2", x, 300 - (i % 2) * 18, 0.42 - (i % 2) * 0.06, body="#2A140C", cloth=WAR[i % 4], kind="Tunic", sw=4, up=[(-22, -158), (-40, -206), (-30, -250)]) for i, x in enumerate(range(30, 340, 44)))}'''
    o2 = (cap("Then the men of Israel said unto Gideon,", "left: 10px; top: 10px", size=10)
          + balloon("Rule thou over us, both thou, and thy son, and thy son's son also; for thou hast saved us out of the hand of Midian.", "left: 20px; top: 46px", 300, size=13, pad="20px 34px"))
    P2a = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 342, 314, s2, o2, "2a · Rule thou over us")
    s3 = f'''      {face(FX["__FACE_GIDEON_CALM__"], 412, 40, 0.72, flip=True)}'''
    o3 = (cap("And Gideon said unto them,", "left: 10px; top: 10px", size=10)
          + tail(196, 210, "r")
          + balloon("I will not rule over you, neither shall my son rule over you: Jehovah shall rule over you.", "left: 8px; top: 70px", 196, size=13.5, pad="24px 18px"))
    P2b = panel("radial-gradient(circle at 70% 50%, #FFF4C2 0 20px, #FFC14D 150px, #4A1D55 330px)", 342, 314, s3, o3, "2b · Jehovah shall rule over you")

    s4 = f'''      {defs("z4", "Man", "Robe")}
      {J.sun(560, 120, 40)}
      {hills(200, "#3F8A44", 804, 50)}
      <path d="M-10 250 C 200 240 500 256 712 246 L 712 384 L -10 384 Z" fill="#9CCB5E" stroke="#0D0D0F" stroke-width="2"></path>
      {"".join(E.sheep(x, 330 + (x * 7) % 30, 0.6, flip=x % 2 == 0) for x in range(80, 680, 70))}
      {G.wheat(40, 380, 1.2, seed=805)}{G.wheat(670, 380, 1.2, seed=806)}'''
    o4 = (cap("So Midian was subdued before the children of Israel, and they lifted up their heads no more. And the land had rest forty years in the days of Gideon.", "left: 12px; top: 12px", size=12, maxw=420)
          + stamp(8, "right: 16px; top: 14px")
          + '    <div style="position: absolute; right: 14px; bottom: 12px; display: flex; align-items: center; gap: 8px; padding: 4px 10px; background: #12113A; color: #FFD23F; box-shadow: inset 0 0 0 2px #FFD23F"><span style="font-family: \'Noto Sans JP\', sans-serif; font-weight: 900; font-size: 20px">つづく</span><span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em">TO BE CONTINUED</span></div>\n')
    P3 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 374, s4, o4, "3 · The land had rest")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("Judges 7:21–8:28 — Jehovah Shall Rule", "290px 320px minmax(0, 1fr)", body, 8)
PAGES["JG1-P08-Rule"] = p08


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "judges/project"))
