"""1 Samuel Book One — Thy Servant Heareth (1 Samuel 1–10). Writes the .dc.html pages into the given folder.
Usage: python3 samuel_book1.py <out_dir>"""
import sys, pathlib, random
import mk, exodus as E, exodus4 as Z, exodus5 as V, numbers1 as N, joshua1 as J, judges2 as S, ruth1 as R, samuel1 as A
from mk import panel, cols, cap, god, tail, balloon, stamp, sfx, ref, person, defs, face, stars
from exodus_book3 import crowd
from numbers_book1 import badge, hills
from judges_book1 import shout
from judges_book2 import end_mark
FX = A.tokens()
PAGES = {}
HANNAH = dict(body="#3A1E14", cloth="#1F7A8C", woman=True, hair="#2A1A10")
PENINNAH = dict(body="#3A1E14", cloth="#B5121B", woman=True, hair=True)
ELKANAH = dict(body="#2A140C", cloth="#8A6A4A")
SAMUEL = dict(body="#3A1E14", cloth="#12113A")
SAUL = dict(body="#2A140C", cloth="#8A1E2E", kind="Tunic", sw=4)
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")
PRAY = [(-22, -158), (-40, -196), (-34, -236)]
POINT = [(-22, -158), (-50, -170), (-80, -176)]
NIGHT = '<rect x="-10" y="-10" width="{w}" height="{h}" fill="#05050A" opacity="0.5"></rect>'


def D(p): return defs(p, *ALL)
def night(w, h): return NIGHT.format(w=w + 20, h=h + 20)


def philistine(p, x, y, s, flip=False, spear=False, up=None, cloth="#1F5FAD"):
    return person(p, round(x), round(y), round(s, 3), body="#5A2A16", cloth=cloth, kind="Tunic", sw=4, flip=flip, up=up,
                  extra=S.FEATHERS + S.FEATHER_BAND + (Z.SPEAR if spear else ""))


def ark_seized(p, x, y, s, uid):
    """Two Philistine warriors carrying off the ark on its staves, heading right."""
    gap = 170 * s; sh = y - 150 * s; sa = 0.9 * s
    return (philistine(p, x - gap, y, s, cloth="#B5121B")
            + J.ark(x, sh + 34 * sa, sa, uid, False, pole=(gap + 34 * s) / sa)
            + philistine(p, x + gap, y, s, cloth="#E8B830"))


def fleeing(p, n, x0, x1, y0, y1, seed, smin, smax):
    r = random.Random(seed); o = []
    for y, x in sorted((r.uniform(y0, y1), r.uniform(x0, x1)) for _ in range(n)):
        s = smin + (smax - smin) * (y - y0) / max(1, y1 - y0)
        o.append(person(p, round(x), round(y), round(s, 3), body="#2A140C", cloth=r.choice(["#8A6A4A", "#5A6E8A", "#C9A86A"]), kind="Tunic", sw=4, flip=True,
                        up=[(-22, -158), (-6, -196), (8, -226)]))
    return "".join(o)


def shouting(p, n, x0, x1, y0, y1, seed, smin, smax, gap=None):
    """A crowd of men and women with both fists in the air."""
    r = random.Random(seed); o = []
    for i, (y, x) in enumerate(sorted((r.uniform(y0, y1), r.uniform(x0, x1)) for _ in range(n))):
        if gap and gap[0] < x < gap[1]:
            continue
        s = smin + (smax - smin) * (y - y0) / max(1, y1 - y0)
        o.append(Z.figure_both(x, y, s, r.choice(["#2A140C", "#3A2214", "#4A2A1A"]), r.choice(["#C9A86A", "#8A6A4A", "#5A6E8A", "#C2456A", "#3F8A44", "#B8A27A"]),
                               [(-22, -158), (-34, -200), (-30, -240)], [(22, -158), (34, -200), (30, -240)], f"{p}{i}"))
    return "".join(o)


# ───────────────────────── Cover ─────────────────────────
def cover():
    svg = f'''  <svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">
    {D("c1")}
    <g transform="translate(0 420)">{A.sanctuary(760, 660, 520, seed=3)}</g>
    <rect x="0" y="400" width="760" height="700" fill="#05050A" opacity="0.45"></rect>
    {V.rays(380, 760, 40, 80, 900, color="#FFF4C2", op=0.16)}
    {J.ark(560, 940, 1.1, uid="cvA", glow=True)}
    {A.lamp(200, 960, 1.9)}
    {A.mat_sleeper(330, 1010, 1.1)}
    {A.boy("c1", 400, 1000, 1.25, flip=False)}
  </svg>'''
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase">
    <span>The First Book of</span>
    <span>No. 01</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 124px; line-height: 1.2; letter-spacing: -1px; color: #F3EFE6">SAMUEL</h1>
  <div style="position: absolute; top: 236px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 252px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase">
    <span>Book One — Thy Servant Heareth</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 10</span>
  </div>
  <div style="position: absolute; top: 40px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 40px; line-height: 1.04; color: #F3EFE6"><span>サ</span><span>ム</span><span>エ</span><span>ル</span><span>記</span><span>上</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.14em; color: #F3EFE6">SAMUERU-KI JŌ</span>
  </div>
  <div style="position: absolute; left: 38px; top: 322px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 250px; line-height: 1.45">Speak; for thy servant heareth.</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; opacity: 0.9">
    <span>Adapted from the American Standard Version (1901)</span>
    <span>Vol. 1</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #05050A 0%, #12113A 30%, #2A1A5E 50%, #4A1D55 70%); color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("1 Samuel Book One — Cover", None, body, root_style=root)
PAGES["Main"] = cover


# ───────────────────────── 01 · Hannah (1:2, 1:10–11) ─────────────────────────
def p01():
    s1 = f'''      {D("a1")}
      {hills(200, "#8A9A5A", 101, 36)}
      {A.shiloh(530, 250, 300, 190)}
      <path d="M-10 240 L 712 240 L 712 304 L -10 304 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("a1", 60, 284, 0.56, **ELKANAH)}
      {person("a1", 110, 286, 0.52, **PENINNAH)}
      {"".join(person("a1", x, 288, sc, body="#3A1E14", cloth=c, kind="Tunic", sw=4) for x, sc, c in [(150, 0.3, "#C9A86A"), (180, 0.26, "#5A6E8A"), (205, 0.3, "#3F8A44"), (88, 0.24, "#E8A317")])}
      {E.kneel(320, 286, 0.5, color="#1F7A8C", flip=True)}'''
    o1 = (cap("And he had two wives; the name of the one was Hannah, and the name of the other Peninnah: and Peninnah had children, but Hannah had no children.", "left: 12px; top: 12px", maxw=330, size=10.5)
          + stamp(1, "right: 16px; top: 14px"))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 294, s1, o1, "1 · Two wives")

    s2 = f'''      {face(FX["__FACE_HANNAH__"], -50, 20, 0.74)}'''
    o2 = cap("And she was in bitterness of soul, and prayed unto Jehovah, and wept sore.", "right: 10px; top: 10px", size=10, maxw=160) + ref("HANNAH", "left: 10px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6")
    P2a = panel("radial-gradient(circle at 30% 50%, #C8E8EE 0 20px, #1F7A8C 160px, #12113A 330px)", 342, 294, s2, o2, "2a · Hannah wept")
    s3 = f'''      {A.sanctuary(342, 294, 240, seed=2, glow=False)}
      {A.eli_seated("a3", 180, 276, 1.15)}'''
    o3 = ref("ELI THE PRIEST", "left: 10px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6")
    P2b = panel("#3A2214", 342, 294, s3, o3, "2b · Eli upon his seat")

    s4 = f'''      {D("a4")}
      {V.rays(160, 140, 30, 40, 700, color="#FFF4C2", op=0.25)}
      <path d="M40 -10 L 40 330 L 280 330 L 280 -10 Z" fill="#1F3F8A" stroke="#0D0D0F" stroke-width="2.4"></path>
      <path d="M100 -10 L 100 330 M160 -10 L 160 330 M220 -10 L 220 330" stroke="#8A1E2E" stroke-width="5"></path>
      <path d="M-10 330 L 712 330 L 712 404 L -10 404 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("a4", 220, 392, 1.0, **HANNAH, up=PRAY)}'''
    o4 = (cap("And she vowed a vow, and said,", "left: 300px; top: 14px", size=12)
          + tail(304, 180, "l")
          + balloon("O Jehovah of hosts, if thou wilt indeed look on the affliction of thy handmaid, and remember me, and not forget thy handmaid, but wilt give unto thy handmaid a man-child, then I will give him unto Jehovah all the days of his life, and there shall no razor come upon his head.", "left: 330px; top: 52px", 362, size=14, pad="44px 40px")
          + ref("1 SAMUEL 1:11", "left: 12px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6"))
    P3 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 394, s4, o4, "3 · She vowed a vow")
    body = P1 + cols(P2a, P2b) + P3
    return mk.page("1 Samuel 1:2–11 — Hannah", "300px 300px minmax(0, 1fr)", body, 1)
PAGES["SA1-P01-Hannah"] = p01


# ───────────────────────── 02 · Asked of Jehovah (1:20, 1:27–28, 3:1) ─────────────────────────
def p02():
    s1 = f'''      {D("b1")}
      {V.rays(200, 150, 36, 40, 700, color="#FFF4C2", op=0.35)}
      <path d="M-10 250 L 712 250 L 712 304 L -10 304 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>
      {A.hannah_with_child("b1", 200, 290, 1.15)}'''
    o1 = cap("And it came to pass, when the time was come about, that Hannah conceived, and bare a son; and she called his name Samuel, saying, Because I have asked him of Jehovah.", "right: 12px; top: 14px", size=12, maxw=360)
    o1 += badge("サムエル", "right: 14px; bottom: 14px", size=22)
    P1 = panel("radial-gradient(circle at 28% 50%, #FFF4C2 0 30px, #FFC14D 180px, #FF8A3D 420px)", 702, 294, s1, o1, "1 · She called his name Samuel")

    s2 = f'''      {D("b2")}
      {hills(170, "#8A9A5A", 201, 30)}
      {A.shiloh(560, 250, 330, 200)}
      <path d="M-10 250 L 712 250 L 712 404 L -10 404 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {A.eli("b2", 560, 384, 0.95, flip=True)}
      {A.boy("b2", 440, 388, 0.55)}
      {person("b2", 370, 390, 0.92, **HANNAH, up=[(-22, -158), (8, -120), (40, -118)])}'''
    o2 = (tail(260, 150, "dr")
          + balloon("For this child I prayed; and Jehovah hath given me my petition which I asked of him: therefore also I have granted him to Jehovah; as long as he liveth he is granted to Jehovah.", "left: 12px; top: 14px", 330, size=14, pad="26px 34px")
          + cap("And he worshipped Jehovah there.", "right: 12px; bottom: 12px", size=11))
    P2 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 394, s2, o2, "2 · For this child I prayed")

    s3 = f'''      {D("b3")}
      {A.sanctuary(702, 294, 250, seed=4)}
      {A.lamp(400, 250, 1.1)}
      {A.boy("b3", 330, 286, 0.62, up=[(-22, -158), (-50, -170), (-74, -186)])}
      {A.eli_seated("b3", 600, 284, 0.95, flip=True)}'''
    o3 = (cap("And the child Samuel ministered unto Jehovah before Eli. And the word of Jehovah was precious in those days; there was no frequent vision.", "left: 12px; top: 12px", size=10.5, maxw=290)
          + stamp(3, "right: 16px; top: 14px"))
    P3 = panel("#3A2214", 702, 294, s3, o3, "3 · The child Samuel ministered")
    body = P1 + P2 + P3
    return mk.page("1 Samuel 1:20 – 3:1 — Asked of Jehovah", "300px minmax(0, 1fr) 300px", body, 2)
PAGES["SA1-P02-Asked"] = p02


# ───────────────────────── 03 · Here Am I (3:3–8) ─────────────────────────
def p03():
    s1 = f'''      {A.sanctuary(702, 244, 200, seed=5)}
      {night(702, 244)}
      {J.ark(610, 200, 0.62, uid="nA", glow=True)}
      {A.lamp(470, 200, 0.8)}
      {A.mat_sleeper(230, 222, 0.9)}'''
    o1 = cap("and the lamp of God was not yet gone out, and Samuel was laid down to sleep, in the temple of Jehovah, where the ark of God was;", "left: 12px; top: 12px", size=10.5, maxw=330)
    P1 = panel("#05050A", 702, 244, s1, o1, "1 · The lamp of God")

    s2 = f'''      {face(FX["__FACE_SAMUEL_NIGHT__"], -40, 30, 0.7)}'''
    o2 = (cap("that Jehovah called Samuel: and he said,", "right: 10px; top: 10px", size=10, maxw=150)
          + balloon("Here am I.", "right: 16px; bottom: 30px", 130, size=17, pad="14px 12px"))
    P2a = panel("radial-gradient(circle at 30% 50%, #8FD0E2 0 20px, #2A3A6A 150px, #05050A 330px)", 342, 274, s2, o2, "2a · Here am I")
    s3 = f'''      {D("c3")}
      {A.sanctuary(342, 274, 220, seed=6, glow=False)}
      {night(342, 274)}
      {A.mat_sleeper(250, 250, 0.7, color="#2C5F9A", head="#E8E2D6", flip=True)}
      {A.boy("c3", 110, 262, 0.62, up=POINT)}
      {mk.speed(60, 180, 10, 30, 120, 7, color="#8FD0E2")}'''
    o3 = (cap("And he ran unto Eli, and said,", "left: 10px; top: 10px", size=10)
          + balloon("Here am I; for thou calledst me.", "right: 12px; top: 40px", 170, size=14, pad="16px 18px"))
    P2b = panel("#05050A", 342, 274, s3, o3, "2b · He ran unto Eli")

    s4 = f'''      {face(FX["__FACE_ELI__"], -30, -40, 0.66)}'''
    o4 = (cap("And he said,", "left: 290px; top: 14px", size=10)
          + tail(250, 80, "l")
          + balloon("I called not; lie down again.", "left: 292px; top: 50px", 220, size=17, pad="18px 22px")
          + cap("And he went and lay down.", "right: 12px; bottom: 12px", size=10))
    P3 = panel("radial-gradient(circle at 20% 50%, #5A6E8A 0 30px, #2A3A6A 160px, #05050A 420px)", 702, 214, s4, o4, "3 · I called not")

    s5 = f'''      {V.rays(560, 110, 30, 30, 500, color="#FFF4C2", op=0.3)}
      {face(FX["__FACE_ELI_AWE__"], 760, -40, 0.66, flip=True)}'''
    o5 = (cap("And Jehovah called Samuel again the third time. And he arose and went to Eli, and said, Here am I; for thou calledst me.", "left: 12px; top: 12px", size=10.5, maxw=380)
          + shout("And Eli perceived that Jehovah had called the child.", "left: 12px; bottom: 14px", size=19, maxw=400))
    P4 = panel("radial-gradient(circle at 80% 50%, #FFF4C2 0 30px, #FFC14D 160px, #4A1D55 460px)", 702, 230, s5, o5, "4 · Eli perceived")
    body = P1 + cols(P2a, P2b) + P3 + P4
    return mk.page("1 Samuel 3:3–8 — Here Am I", "250px 280px 220px minmax(0, 1fr)", body, 3)
PAGES["SA1-P03-HereAmI"] = p03


# ───────────────────────── 04 · Speak (3:9–10, 3:19–20) ─────────────────────────
def p04():
    s1 = f'''      {D("d1")}
      {A.sanctuary(702, 244, 210, seed=7, glow=False)}
      {night(702, 244)}
      {A.lamp(80, 210, 0.7)}
      {A.eli_seated("d1", 220, 236, 0.85)}
      {A.boy("d1", 330, 236, 0.55, flip=True)}'''
    o1 = (cap("Therefore Eli said unto Samuel,", "left: 12px; top: 12px", size=10)
          + tail(380, 120, "l")
          + balloon("Go, lie down: and it shall be, if he call thee, that thou shalt say, Speak, Jehovah; for thy servant heareth.", "left: 410px; top: 16px", 280, size=13.5, pad="22px 26px")
          + cap("So Samuel went and lay down in his place.", "right: 12px; bottom: 10px", size=9.5))
    P1 = panel("#05050A", 702, 244, s1, o1, "1 · Speak, Jehovah")

    s2 = f'''      {A.sanctuary(702, 394, 330, seed=8, glow=False)}
      <rect x="-10" y="-10" width="722" height="414" fill="#05050A" opacity="0.6"></rect>
      <defs><linearGradient id="pl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFF4C2" stop-opacity="0"></stop><stop offset="0.5" stop-color="#FFF4C2" stop-opacity="0.95"></stop><stop offset="1" stop-color="#FFF4C2" stop-opacity="0"></stop></linearGradient></defs>
      {V.rays(460, 200, 40, 60, 700, color="#FFF4C2", op=0.22)}
      <path d="M380 -10 L 540 -10 L 600 404 L 320 404 Z" fill="url(#pl)"></path>
      <ellipse cx="460" cy="340" rx="160" ry="22" fill="#FFF4C2" opacity="0.6"></ellipse>
      <path d="M70 360 L 290 360 L 286 348 L 74 348 Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2"></path>
      {E.kneel(180, 350, 0.9, color="#F3EFE6", skin="#3A1E14")}'''
    o2 = (cap("And Jehovah came, and stood, and called as at other times,", "left: 12px; top: 12px", size=11, maxw=300)
          + god("Samuel, Samuel.", "right: 24px; top: 30px", size=30))
    P2 = panel("#05050A", 702, 394, s2, o2, "2 · Jehovah came, and stood")

    s3 = f'''      {V.rays(120, 150, 30, 30, 400, color="#FFF4C2", op=0.3)}
      {face(FX["__FACE_SAMUEL_CHILD__"], -60, 20, 0.8)}'''
    o3 = (cap("Then Samuel said,", "right: 10px; top: 10px", size=10)
          + balloon("Speak; for thy servant heareth.", "right: 10px; bottom: 16px", 170, size=17, pad="20px 16px"))
    P3a = panel("radial-gradient(circle at 30% 50%, #FFF4C2 0 30px, #FFC14D 140px, #4A1D55 330px)", 342, 324, s3, o3, "3a · Thy servant heareth")
    s4 = f'''      {D("d4")}
      {J.sun(270, 70, 34)}
      {hills(190, "#8A9A5A", 401, 40, 342)}
      <path d="M-10 250 L 352 250 L 352 334 L -10 334 Z" fill="#C8A06A"></path>
      {crowd("d4", 14, -10, 352, 270, 330, 402, 0.2, 0.36)}
      {person("d4", 171, 250, 0.62, **SAMUEL)}'''
    o4 = cap("And Samuel grew, and Jehovah was with him, and did let none of his words fall to the ground. And all Israel from Dan even to Beer-sheba knew that Samuel was established to be a prophet of Jehovah.", "left: 10px; top: 10px", size=9.5, maxw=322)
    P3b = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 342, 324, s4, o4, "3b · A prophet of Jehovah")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("1 Samuel 3:9–20 — Speak", "250px minmax(0, 1fr) 330px", body, 4)
PAGES["SA1-P04-Speak"] = p04


# ───────────────────────── 05 · The Ark of God Was Taken (4:3–22) ─────────────────────────
def p05():
    s1 = f'''      {D("e1")}
      {"".join(Z.tent(x, 150, w, w * 0.7, color=c) for x, w, c in [(60, 90, "#3A2A3E"), (170, 70, "#4A2A1A"), (620, 100, "#2A1A2E"), (520, 60, "#3A2A3E")])}
      <path d="M-10 150 L 712 150 L 712 254 L -10 254 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>
      {"".join(person("e1", x, 236, 0.5, body="#3A1E14", cloth=c, sw=4, flip=x > 100) for x, c in [(40, "#8A6A4A"), (90, "#5A6E8A"), (150, "#C9A86A"), (210, "#8A6A4A")])}'''
    o1 = (cap("And when the people were come into the camp, the elders of Israel said,", "left: 12px; top: 12px", size=10, maxw=240)
          + balloon("Wherefore hath Jehovah smitten us to-day before the Philistines? Let us fetch the ark of the covenant of Jehovah out of Shiloh unto us, that it may come among us, and save us out of the hand of our enemies.", "left: 262px; top: 10px", 380, size=12.5, pad="22px 40px")
          + stamp(4, "left: 16px; bottom: 12px", rot=-4))
    P1 = panel("linear-gradient(180deg, #4A1D55 0%, #C2456A 60%, #FF8A3D 100%)", 702, 244, s1, o1, "1 · Let us fetch the ark")

    s2 = f'''      {D("e2")}
      {hills(160, "#5A2A1E", 501, 40)}
      <path d="M-10 200 L 712 200 L 712 334 L -10 334 Z" fill="#8A4A22" stroke="#0D0D0F" stroke-width="2"></path>
      {S.philistines("e2", 14, 420, 712, 200, 250, 502, 0.26, 0.4)}
      {fleeing("e2", 8, -10, 220, 220, 300, 503, 0.3, 0.46)}
      {ark_seized("e2", 400, 318, 0.6, "sA")}
      {mk.speed(400, 200, 40, 200, 600, 504, color="#FFD23F", op=0.4)}'''
    o2 = (cap("And the Philistines fought, and Israel was smitten, and they fled every man to his tent:", "left: 12px; top: 12px", size=10.5, maxw=330)
          + shout("And the ark of God was taken;", "right: 14px; top: 14px", size=26, maxw=290)
          + sfx("ドドド", "DODODO", "right: 20px; bottom: 16px", size=36, fill="#FFD23F", stroke="#0D0D0F", rot=-4))
    P2 = panel("linear-gradient(180deg, #2A0A0A 0%, #B5121B 60%, #FF8A3D 100%)", 702, 324, s2, o2, "2 · The ark of God was taken")

    s3 = f'''      {J.jericho(-10, 352, 120, 300, 505, color="#B5652E", towers=1, houses=False)}
      <path d="M180 300 L 180 200 C 180 170 280 170 280 200 L 280 300 Z" fill="#12090A" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M-10 300 L 352 300 L 352 404 L -10 404 Z" fill="#5A3A2E" stroke="#0D0D0F" stroke-width="2"></path>
      {A.seat(150, 360, 0.9, fallen=True)}'''
    o3 = cap("And it came to pass, when he made mention of the ark of God, that Eli fell from off his seat backward by the side of the gate; and his neck brake, and he died: for he was an old man, and heavy.", "left: 10px; top: 10px", size=9.5, maxw=322)
    o3 += ref("1 SAMUEL 4:18", "right: 10px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6")
    P3a = panel("linear-gradient(180deg, #2A1A5E 0%, #8A4A6A 100%)", 342, 394, s3, o3, "3a · Eli fell from off his seat")
    s4 = f'''      {A.sanctuary(342, 394, 330, seed=9, glow=False)}
      <rect x="-10" y="-10" width="362" height="414" fill="#05050A" opacity="0.62"></rect>
      {A.lamp(171, 330, 1.2, lit=False)}'''
    o4 = (cap("And she said,", "left: 10px; top: 10px", size=10)
          + god("The glory is departed from Israel; for the ark of God is taken.", "left: 14px; top: 46px", size=22, maxw=310)
          + ref("ICHABOD", "right: 10px; bottom: 9px", color="#0D0D0F", bg="#F3EFE6"))
    P3b = panel("#05050A", 342, 394, s4, o4, "3b · The glory is departed")
    body = P1 + P2 + cols(P3a, P3b)
    return mk.page("1 Samuel 4:3–22 — The Ark of God Was Taken", "250px 330px minmax(0, 1fr)", body, 5)
PAGES["SA1-P05-Taken"] = p05


# ───────────────────────── 06 · Dagon (5:2–4) ─────────────────────────
def dagon_house(W, H, floor, seed, dark=0.0):
    pil = "".join(f'<rect x="{x - 14}" y="-10" width="28" height="{floor + 10}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>'
                  f'<rect x="{x - 20}" y="-10" width="40" height="18" fill="#6A5E52" stroke="#0D0D0F" stroke-width="2"></rect>' for x in range(40, W, 160))
    o = (f'<rect x="-10" y="-10" width="{W + 20}" height="{floor + 10}" fill="#4A3A3E"></rect>' + pil
         + f'<path d="M-10 {floor} L {W + 10} {floor} L {W + 10} {H + 10} L -10 {H + 10} Z" fill="#6A5E52" stroke="#0D0D0F" stroke-width="2"></path>')
    if dark: o += f'<rect x="-10" y="-10" width="{W + 20}" height="{H + 20}" fill="#05050A" opacity="{dark}"></rect>'
    return o


def p06():
    s1 = f'''      {D("f1")}
      {dagon_house(702, 294, 270, 601, 0.25)}
      {A.dagon(470, 276, 0.62)}
      {J.ark(240, 276, 0.8, uid="dA", glow=True)}
      {philistine("f1", 90, 284, 0.5, flip=False, cloth="#B5121B")}
      {philistine("f1", 620, 284, 0.5, flip=True, cloth="#2C9DB8")}'''
    o1 = (cap("And the Philistines took the ark of God, and brought it into the house of Dagon, and set it by Dagon.", "left: 12px; top: 12px", size=10.5, maxw=260)
          + stamp(5, "right: 16px; top: 14px"))
    P1 = panel("#4A3A3E", 702, 294, s1, o1, "1 · Set it by Dagon")

    s2 = f'''      {D("f2")}
      {dagon_house(702, 294, 250, 602)}
      {V.rays(0, 0, 20, 40, 800, color="#FFF4C2", op=0.2)}
      <rect x="306" y="224" width="128" height="26" fill="#7A746A" stroke="#0D0D0F" stroke-width="2.4"></rect>
      {A.dagon(330, 290, 0.6, state=1)}
      {J.ark(580, 290, 0.8, uid="dB", glow=True)}
      {philistine("f2", 60, 286, 0.5, up=[(-22, -158), (-40, -196), (-34, -236)], cloth="#E8B830")}'''
    o2 = (cap("And when they of Ashdod arose early on the morrow, behold, Dagon was fallen upon his face to the ground before the ark of Jehovah.", "left: 12px; top: 12px", size=10.5, maxw=330)
          + cap("And they took Dagon, and set him in his place again.", "right: 12px; top: 12px", size=9, maxw=200)
          + sfx("ドサッ", "DOSA", "left: 250px; bottom: 80px", size=34, fill="#F3EFE6", stroke="#0D0D0F", rot=-8))
    P2 = panel("#4A3A3E", 702, 294, s2, o2, "2 · Dagon was fallen")

    s3 = f'''      {D("f3")}
      {dagon_house(702, 394, 300, 603)}
      {V.rays(560, 230, 30, 60, 700, color="#FFF4C2", op=0.25)}
      {J.ark(580, 320, 0.95, uid="dC", glow=True)}
      {A.threshold(-10, 712, 394, 50)}
      {A.dagon(330, 336, 0.62, state=2)}
      {A.head_alone(250, 340, 0.62, 80)}
      {A.palm(110, 340, 1.4, 90)}{A.palm(410, 342, 1.4, -80)}
      {E.kneel(60, 330, 0.5, color="#1F5FAD", flip=True)}'''
    o3 = (cap("And when they arose early on the morrow morning, behold, Dagon was fallen upon his face to the ground before the ark of Jehovah; and the head of Dagon and both the palms of his hands lay cut off upon the threshold;", "left: 12px; top: 12px", size=10.5, maxw=400)
          + shout("only the stump of Dagon was left to him.", "right: 14px; top: 14px", size=19, maxw=230))
    P3 = panel("#4A3A3E", 702, 394, s3, o3, "3 · Only the stump")
    body = P1 + P2 + P3
    return mk.page("1 Samuel 5:2–4 — Dagon", "300px 300px minmax(0, 1fr)", body, 6)
PAGES["SA1-P06-Dagon"] = p06


# ───────────────────────── 07 · The Kine (6:10–13) ─────────────────────────
def p07():
    s1 = f'''      {D("g1")}
      {hills(170, "#8A9A5A", 701, 30)}
      <path d="M-10 200 L 712 200 L 712 294 L -10 294 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M10 200 L 10 270 M60 200 L 60 270 M110 200 L 110 270 M160 200 L 160 270 M0 220 L 170 220 M0 248 L 170 248" stroke="#5A3A22" stroke-width="5"></path>
      {A.calf(60, 266, 0.7, color="#C9A27A")}{A.calf(110, 272, 0.66, flip=True, color="#8A5A30")}
      {A.team(260, 270, 0.62)}
      {philistine("g1", 600, 282, 0.5, flip=True, up=POINT, cloth="#2C9DB8")}'''
    o1 = (cap("And the men did so, and took two milch kine, and tied them to the cart, and shut up their calves at home;", "left: 190px; top: 12px", size=10.5, maxw=330)
          + stamp(6, "right: 16px; top: 14px"))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 294, s1, o1, "1 · Two milch kine")

    s2 = f'''      {D("g2")}
      {J.sun(600, 90, 40)}
      {hills(220, "#8A9A5A", 702, 40)}
      <path d="M-10 250 L 712 250 L 712 414 L -10 414 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      <path d="M-10 330 C 200 320 500 300 712 290 L 712 330 C 500 344 200 370 -10 380 Z" fill="#E8C88A" stroke="#8A6A3A" stroke-width="1.4"></path>
      {"".join(philistine("g2", x, 300 + i * 4, 0.3, cloth=c) for i, (x, c) in enumerate([(30, "#B5121B"), (60, "#E8B830"), (90, "#1F5FAD"), (118, "#2C9DB8"), (146, "#B5121B")]))}
      {A.team(250, 360, 0.82, low=True)}'''
    o2 = (cap("And the kine took the straight way by the way to Beth-shemesh; they went along the highway, lowing as they went, and turned not aside to the right hand or to the left; and the lords of the Philistines went after them unto the border of Beth-shemesh.", "left: 12px; top: 12px", size=10.5, maxw=420)
          + sfx("モォー", "MOOO", "right: 24px; top: 150px", size=40, fill="#F3EFE6", stroke="#0D0D0F", rot=-6))
    P2 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 404, s2, o2, "2 · The straight way")

    r = random.Random(7)
    s3 = f'''      {D("g3")}
      {hills(120, "#8A9A5A", 703, 30)}
      <path d="M-10 140 L 712 140 L 712 284 L -10 284 Z" fill="#E8A35A" stroke="#0D0D0F" stroke-width="2"></path>
      {A.team(560, 150, 0.22)}
      {R.field(-10, 712, 190, 26, 704, rows=2)}
      {"".join(person("g3", x, 266 + r.uniform(-6, 6), 0.5, body="#2A140C", cloth=c, kind="Tunic", sw=4, up=[(-22, -158), (-34, -200), (-30, -240)], extra=R.SICKLE.replace('-44 -240', '-30 -240')) for x, c in [(70, "#8A6A4A"), (170, "#5A6E8A"), (270, "#C9A86A"), (370, "#3F8A44")])}
      {R.field(-10, 712, 270, 30, 705, rows=1)}'''
    o3 = cap("And they of Beth-shemesh were reaping their wheat harvest in the valley; and they lifted up their eyes, and saw the ark, and rejoiced to see it.", "right: 12px; top: 12px", size=10.5, maxw=300)
    P3 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 284, s3, o3, "3 · They rejoiced to see it")
    body = P1 + P2 + P3
    return mk.page("1 Samuel 6:10–13 — The Kine", "300px minmax(0, 1fr) 290px", body, 7)
PAGES["SA1-P07-Kine"] = p07


# ───────────────────────── 08 · Give Us a King (8:4–20) ─────────────────────────
def p08():
    s1 = f'''      {D("h1")}
      {J.city_hill(560, 190, 220, 100, 801)}
      <path d="M-10 190 L 712 190 L 712 284 L -10 284 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {person("h1", 600, 270, 0.62, **SAMUEL, flip=True)}
      {"".join(person("h1", x, 272, 0.54, body="#3A1E14", cloth=c, sw=4) for x, c in [(330, "#8A6A4A"), (380, "#5A6E8A"), (430, "#C9A86A"), (480, "#4A3A6A")])}'''
    o1 = (cap("Then all the elders of Israel gathered themselves together, and came to Samuel unto Ramah; and they said unto him,", "left: 12px; top: 12px", size=10, maxw=290)
          + balloon("Behold, thou art old, and thy sons walk not in thy ways: now make us a king to judge us like all the nations.", "left: 12px; top: 120px", 290, size=13.5, pad="18px 26px")
          + tail(300, 140, "r")
          + stamp(8, "right: 16px; top: 14px"))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 284, s1, o1, "1 · Make us a king")

    s2 = f'''      {face(FX["__FACE_SAMUEL_GRIEVED__"], -60, -10, 0.7)}'''
    o2 = cap("But the thing displeased Samuel, when they said, Give us a king to judge us. And Samuel prayed unto Jehovah.", "left: 10px; bottom: 10px", size=9.5, maxw=266)
    P2a = panel("radial-gradient(circle at 40% 40%, #C8D0DE 0 30px, #5A6E8A 160px, #12113A 330px)", 288, 294, s2, o2, "2a · Samuel displeased")
    s3 = f'''      {V.rays(200, -40, 40, 40, 600, color="#FFF4C2", op=0.2)}'''
    o3 = (cap("And Jehovah said unto Samuel,", "left: 10px; top: 10px", size=10)
          + god("Hearken unto the voice of the people in all that they say unto thee; for they have not rejected thee, but they have rejected me, that I should not be king over them.", "left: 14px; top: 48px", size=17, maxw=370))
    P2b = panel("radial-gradient(circle at 50% 0%, #FFE680 0 30px, #4A1D55 220px, #12113A 400px)", 402, 294, s3, o3, "2b · They have rejected me")

    s4 = f'''      {J.sun(110, 90, 36)}
      {hills(180, "#8A9A5A", 802, 30)}
      <path d="M-10 220 L 712 220 L 712 404 L -10 404 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {shouting("hx", 22, -10, 712, 270, 380, 803, 0.4, 0.66)}'''
    o4 = (cap("But the people refused to hearken unto the voice of Samuel; and they said,", "left: 12px; top: 12px", size=10.5, maxw=300)
          + balloon("Nay: but we will have a king over us, that we also may be like all the nations, and that our king may judge us, and go out before us, and fight our battles.", "right: 14px; top: 12px", 360, size=14, pad="22px 34px")
          + sfx("ワーッ", "WAAH", "left: 30px; top: 100px", size=36, fill="#FFD23F", stroke="#0D0D0F", rot=-8, align="flex-start"))
    P3 = panel("linear-gradient(180deg, #FF8A3D 0%, #FFE3B8 100%)", 702, 394, s4, o4, "3 · We will have a king")
    body = P1 + cols(P2a, P2b, tmpl="minmax(0, 1fr) minmax(0, 1.4fr)") + P3
    return mk.page("1 Samuel 8:4–20 — Give Us a King", "290px 300px minmax(0, 1fr)", body, 8)
PAGES["SA1-P08-King"] = p08


# ───────────────────────── 09 · Long Live the King (9:2, 10:1, 10:24) ─────────────────────────
def p09():
    s1 = f'''      {D("i1")}
      {hills(150, "#6A8A4A", 901, 50)}
      {hills(200, "#8A9A5A", 902, 30)}
      <path d="M-10 230 L 712 230 L 712 274 L -10 274 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {N.ass(560, 180, 0.3)}{N.ass(620, 186, 0.28, flip=True)}
      {person("i1", 120, 262, 0.9, **SAUL, up=[(-22, -158), (-46, -176), (-66, -184)])}
      {person("i1", 200, 264, 0.58, body="#3A1E14", cloth="#8A6A4A", kind="Tunic", sw=4)}'''
    o1 = (cap("And he had a son, whose name was Saul, a young man and a goodly: and there was not among the children of Israel a goodlier person than he: from his shoulders and upward he was higher than any of the people.", "right: 12px; top: 12px", size=10, maxw=400)
          + stamp(9, "left: 260px; bottom: 14px", rot=-4))
    P1 = panel("linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)", 702, 264, s1, o1, "1 · Saul")

    s2 = f'''      {V.rays(200, 120, 36, 40, 700, color="#FFF4C2", op=0.3)}
      {face(FX["__FACE_SAUL_ANOINTED__"], -40, 40, 0.86)}
      {mk.arm([(400, -30), (300, 10), (200, 20)], "#3A1E14", 22)}
      <path d="M430 -30 L 340 0 L 310 44 L 410 10 Z" fill="#12113A" stroke="#0D0D0F" stroke-width="2.4"></path>
      {A.vial(182, 20, 1.5, rot=-130, pour=50)}
      {A.drops(150, 70, 12, 905, spread=40)}'''
    o2 = (cap("Then Samuel took the vial of oil, and poured it upon his head, and kissed him, and said,", "right: 12px; top: 12px", size=11, maxw=250)
          + tail(390, 250, "l")
          + balloon("Is it not that Jehovah hath anointed thee to be prince over his inheritance?", "right: 14px; top: 160px", 270, size=16, pad="24px 28px")
          + stamp(10, "right: 16px; bottom: 14px"))
    P2 = panel("radial-gradient(circle at 30% 50%, #FFF4C2 0 40px, #FFC14D 200px, #B5652E 460px)", 702, 384, s2, o2, "2 · The vial of oil")

    s3 = f'''      {D("i3")}
      {V.rays(351, 120, 40, 40, 700, color="#FFF4C2", op=0.3)}
      {hills(170, "#8A9A5A", 903, 30)}
      <path d="M-10 200 L 712 200 L 712 334 L -10 334 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="2"></path>
      {shouting("ix", 26, -10, 712, 240, 300, 904, 0.36, 0.5, gap=(300, 420))}
      {person("i3", 360, 314, 0.9, **SAUL)}
      {person("i3", 440, 316, 0.68, **SAMUEL, up=POINT, flip=True)}'''
    o3 = (cap("And Samuel said to all the people,", "left: 12px; top: 12px", size=10)
          + balloon("See ye him whom Jehovah hath chosen, that there is none like him among all the people?", "left: 12px; top: 44px", 250, size=13, pad="18px 22px")
          + cap("And all the people shouted, and said,", "right: 12px; top: 12px", size=10)
          + shout("Long live the king.", "right: 14px; top: 46px", size=30, maxw=280)
          + end_mark("TO BE CONTINUED", "right: 14px; bottom: 12px", ch="つづく"))
    P3 = panel("linear-gradient(180deg, #FFC14D 0%, #FFE3B8 100%)", 702, 334, s3, o3, "3 · Long live the king")
    body = P1 + P2 + P3
    return mk.page("1 Samuel 9:2 – 10:24 — Long Live the King", "270px minmax(0, 1fr) 340px", body, 9)
PAGES["SA1-P09-Anointed"] = p09


def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, fn in PAGES.items():
        (out / f"{name}.dc.html").write_text(fn())
    return list(PAGES)

if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "1samuel/project"))
