import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from reuse import panels
from genesis import G

def cover():
    a = panels("digest/genesis/book-01/P01-Darkness.dc.html")[3]
    svg = f'<svg width="760" height="1080" viewBox="0 0 480 592" preserveAspectRatio="xMidYMid slice" style="position: absolute; inset: 0; display: block">{a.svg}</svg>'
    svg += '<div style="position: absolute; left: 0; right: 0; top: 0; height: 420px; background: linear-gradient(180deg, rgba(13,13,15,0.92) 0%, rgba(13,13,15,0.75) 60%, rgba(13,13,15,0) 100%)"></div>'
    body = svg + f'''
  <div style="position: absolute; top: 40px; left: 38px; right: 38px; display: flex; justify-content: space-between; align-items: baseline; font-size: 11px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #F3EFE6">
    <span>The First Book of Moses</span>
    <span>The Full Edition</span>
  </div>
  <h1 style="position: absolute; top: 50px; left: 30px; margin: 0; font-family: Anton, 'Archivo Narrow', sans-serif; font-weight: 400; font-size: 128px; line-height: 1.2; letter-spacing: -1px; color: #F3EFE6; text-shadow: 5px 5px 0 #0D0D0F">GENESIS</h1>
  <div style="position: absolute; top: 250px; left: 38px; width: 300px; height: 3px; background: #F3EFE6"></div>
  <div style="position: absolute; top: 266px; left: 38px; display: flex; flex-direction: column; gap: 6px; font-size: 12px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; color: #F3EFE6">
    <span>Volume One</span>
    <span style="font-weight: 500; opacity: 0.85">Chapters 1 – 50 · American Standard Version</span>
  </div>
  <div style="position: absolute; top: 40px; right: 38px; margin-top: 30px; width: 92px; padding: 18px 0 14px; background: {{{{accent}}}}; display: flex; flex-direction: column; align-items: center; gap: 10px">
    <span style="display: flex; flex-direction: column; align-items: center; font-family: 'Noto Sans JP', sans-serif; font-weight: 900; font-size: 46px; line-height: 1.02; color: #F3EFE6"><span>創</span><span>世</span><span>記</span></span>
    <span style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: #F3EFE6">SŌSEIKI</span>
  </div>
  <div style="position: absolute; left: 38px; bottom: 80px; padding: 8px 12px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: 14px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; max-width: 300px; line-height: 1.45">{G.v("1:3", frm="Let")}</div>
  <div style="position: absolute; left: 38px; right: 38px; bottom: 34px; display: flex; justify-content: space-between; font-size: 10px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; color: #F3EFE6; opacity: 0.9">
    <span>The words of the American Standard Version (1901)</span><span>Vol. 1</span>
  </div>'''
    root = f"position: relative; width: 760px; height: 1080px; overflow: hidden; background: {a.bg}; color: #F3EFE6; font-family: 'IBM Plex Mono', monospace"
    return mk.page("Genesis — The Full Edition, Volume One", None, body, root_style=root)
