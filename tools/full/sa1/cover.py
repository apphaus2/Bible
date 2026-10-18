import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from sa1 import G
from sa1.common import D

def cover():
    """David with his staff and sling before the battle, the hosts on the hills (the digest's panel, full-bleed)."""
    bg, art = D("B5", 2)
    svg = (f'<svg width="760" height="1080" viewBox="0 0 760 1080" style="position: absolute; inset: 0; display: block">'
           f'<g transform="translate(0 260)">{art(760, 820)}</g></svg>'
           '<div style="position: absolute; left: 0; right: 0; top: 0; height: 460px; background: linear-gradient(180deg, rgba(42,10,30,1) 0%, rgba(42,10,30,0.85) 60%, rgba(42,10,30,0) 100%)"></div>')
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #F3EFE6">
    <span>The First Book of</span>
  </div>
  <h1 style="position: absolute; top: 56px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 136px; line-height: 1.08; letter-spacing: -1px; color: #F3EFE6; text-shadow: 5px 5px 0 #0D0D0F">SAMUEL</h1>
  <div style="position: absolute; top: 246px; left: 38px; width: 280px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 262px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #F3EFE6">
    <span>Volume Nine</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 31</span>
  </div>
  <div style="position: absolute; top: 200px; right: 38px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 40px; line-height: 1.02; color: #F3EFE6"><span>サ</span><span>ム</span><span>エ</span><span>ル</span><span>記</span><span>上</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.14em; color: #F3EFE6">SAMUERU-KI JŌ</span>
  </div>
  <div style="position: absolute; left: 38px; top: 330px; padding: 7px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 13px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 300px; line-height: 1.45">{G.v("16:7", frm="for man looketh")}</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: #F3EFE6; opacity: 0.9">
    <span>ASV</span><span>Vol. 9</span>
  </div>'''
    root = "position: relative; width: 760px; height: 1080px; overflow: hidden; background: #2A0A1E; color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("1 Samuel — Volume Nine", None, body, root_style=root)
