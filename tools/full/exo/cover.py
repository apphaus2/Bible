import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from reuse import panels
from exo import G

def cover():
    a = panels("digest/exodus/book-01/EX1-P06-Bush.dc.html")[1]
    svg = f'<svg width="760" height="1080" viewBox="120 0 470 472" preserveAspectRatio="xMidYMid slice" style="position: absolute; inset: 0; display: block">{a.svg}</svg>'
    svg += '<div style="position: absolute; left: 0; right: 0; top: 0; height: 420px; background: linear-gradient(180deg, rgba(13,13,15,0.92) 0%, rgba(13,13,15,0.75) 60%, rgba(13,13,15,0) 100%)"></div>'
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #F3EFE6">
    <span>The Second Book of Moses</span>
  </div>
  <h1 style="position: absolute; top: 50px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 128px; line-height: 1.2; letter-spacing: -1px; color: #F3EFE6; text-shadow: 5px 5px 0 #0D0D0F">EXODUS</h1>
  <div style="position: absolute; top: 250px; left: 38px; width: 300px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 266px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #F3EFE6">
    <span>Volume Two</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 40</span>
  </div>
  <div style="position: absolute; top: 40px; right: 38px; margin-top: 30px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 40px; line-height: 1.02; color: #F3EFE6"><span>出</span><span>エ</span><span>ジ</span><span>プ</span><span>ト</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">SHUTSU</span>
  </div>
  <div style="position: absolute; left: 38px; bottom: 80px; padding: 8px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 14px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 300px; line-height: 1.45">{G.v("3:14", frm="I AM THAT", to="I AM:").rstrip(":")}</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: #F3EFE6; opacity: 0.9">
    <span>ASV</span><span>Vol. 2</span>
  </div>'''
    root = f"position: relative; width: 760px; height: 1080px; overflow: hidden; background: {a.bg}; color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Exodus — Volume Two", None, body, root_style=root)
