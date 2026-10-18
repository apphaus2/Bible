import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from kg2 import G
from kg2 import art as K

def cover():
    """The chariot of fire and horses of fire parting Elijah and Elisha, the whirlwind (full-bleed)."""
    art = lambda w, h: K.whirlwind("cv", w, h, 1)
    svg = (f'<svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">'
           f'<g transform="translate(0 260)">{art(760, 820)}</g></svg>'
           '<div style="position: absolute; left: 0; right: 0; top: 0; height: 460px; background: linear-gradient(180deg, rgba(58,20,10,1) 0%, rgba(58,20,10,0.85) 60%, rgba(58,20,10,0) 100%)"></div>')
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #F3EFE6">
    <span>The Second Book of the</span>
  </div>
  <h1 style="position: absolute; top: 56px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 136px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6; text-shadow: 5px 5px 0 #0D0D0F">KINGS</h1>
  <div style="position: absolute; top: 246px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 262px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #F3EFE6">
    <span>Volume Twelve</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 25</span>
  </div>
  <div style="position: absolute; top: 200px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 40px; line-height: 1.02; color: #F3EFE6"><span>列</span><span>王</span><span>記</span><span>下</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.14em; color: #F3EFE6">RETSUŌKI GE</span>
  </div>
  <div style="position: absolute; left: 38px; top: 330px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 300px; line-height: 1.45">{G.v("2:11", frm="and Elijah went up")}</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: #F3EFE6; opacity: 0.9">
    <span>ASV</span><span>Vol. 12</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: #3A140A; color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("2 Kings — Volume Twelve", None, body, root_style=root)
