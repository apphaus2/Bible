import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus5 as V, joshua1 as J
from mk import defs
from crowds import crowd, WAR
from jos import G

def cover():
    """The walls of Jericho falling at the shout, the ark borne in the midst of the host, rams'-horn trumpets on either side."""
    horns = "".join(J.trumpeter("cv", x, y, sc, flip=fl) + J.blasts(x + (-60 if fl else 30) * sc, y - 200 * sc, sc * 1.2)
                    for x, y, sc, fl in [(90, 1000, 0.8, False), (200, 1018, 0.88, False), (580, 1018, 0.88, True), (690, 1000, 0.8, True)])
    svg = (f'<svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">'
           f'{defs("cv", "Man", "ManUp", "Robe", "Tunic", "Hair")}{V.rays(380, 640, 40, 100, 900, color="#FFF4C2", op=0.2)}'
           f'{J.jericho(-20, 140, 640, 820, 601, towers=1)}{J.jericho(620, 790, 660, 820, 602, towers=1)}{J.collapse(120, 640, 840, 420, 603)}'
           f'<path d="M-10 830 C 200 820 500 836 770 826 L 770 1090 L -10 1090 Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>'
           f'{crowd("cv", 30, -10, 770, 850, 900, 4, 0.18, 0.3, body=("#2A140C", "#3A2214"), cloth=WAR)}{J.ark_borne("cv", 380, 990, 0.72, "cva")}{horns}</svg>')
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #F3EFE6">
    <span>The Book of</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 160px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6; text-shadow: 5px 5px 0 #0D0D0F">JOSHUA</h1>
  <div style="position: absolute; top: 246px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 262px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #F3EFE6">
    <span>Volume Six</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 24</span>
  </div>
  <div style="position: absolute; top: 236px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>ヨ</span><span>シ</span><span>ュ</span><span>ア</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">YOSHUA-KI</span>
  </div>
  <div style="position: absolute; left: 38px; top: 330px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 280px; line-height: 1.45">{G.v("6:20", frm="the wall fell down flat,", to="every man straight before him,")}</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: #F3EFE6; opacity: 0.9">
    <span>ASV</span><span>Vol. 6</span>
  </div>'''
    root = ("position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #12113A 0%, #5A0E16 30%, #D7261E 55%, #FF8A3D 75%, #FFC14D 100%); "
            "color: #F3EFE6; font-family: 'IBM Plex Mono', monospace")
    return mk.page("Joshua — Volume Six", None, body, root_style=root)
