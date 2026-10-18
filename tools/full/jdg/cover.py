import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus5 as V, joshua1 as J, judges2 as S
from mk import defs, speed
from crowds import samson_both
from jdg import G

def cover():
    """Samson between the two middle pillars of the house of Dagon, the wall breaking, his arms spread."""
    svg = (f'<svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">'
           f'{defs("cv", "Man", "ManUp", "Robe", "Tunic")}{V.rays(380, 720, 40, 80, 900, color="#FFF4C2", op=0.25)}'
           f'<g transform="translate(-10 400)">{S.temple(780, 690, 70, (250, 530), uid="cv", seed=701)}</g>'
           f'{S.cracks_on(240, 510, 1080, 702)}{S.cracks_on(520, 510, 1080, 703)}{J.collapse(-10, 770, 470, 120, 704)}'
           f'{samson_both(380, 1040, 1.5, [(-22, -158), (-60, -168), (-92, -180)], [(22, -158), (60, -168), (92, -180)], "cvs", stroke="#FFD23F")}'
           f'{speed(380, 800, 60, 120, 600, 705, color="#FFF4C2", sw=2, op=0.4)}</svg>')
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #F3EFE6">
    <span>The Book of</span>
  </div>
  <h1 style="position: absolute; top: 46px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 160px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6; text-shadow: 5px 5px 0 #0D0D0F">JUDGES</h1>
  <div style="position: absolute; top: 246px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 262px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #F3EFE6">
    <span>Volume Seven</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 21</span>
  </div>
  <div style="position: absolute; top: 236px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>士</span><span>師</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">SHISHIKI</span>
  </div>
  <div style="position: absolute; left: 38px; top: 330px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 280px; line-height: 1.45">{G.v("21:25", frm="every man did")}</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: #F3EFE6; opacity: 0.9">
    <span>ASV</span><span>Vol. 7</span>
  </div>'''
    root = ("position: relative; width: 760px; height: 1080px; overflow: hidden; background: linear-gradient(180deg, #2A0A1E 0%, #7A1A2A 35%, #D7261E 60%, #FF8A3D 85%, #FFC14D 100%); "
            "color: #F3EFE6; font-family: 'IBM Plex Mono', monospace")
    return mk.page("Judges — Volume Seven", None, body, root_style=root)
