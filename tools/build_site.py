"""Build a static website (docs/) from the .dc.html manga pages.
Usage: python3 build_site.py <project_dir> <canvas.json> <out_dir>"""
import json, re, sys, html, pathlib, subprocess
src, canvas_path, out = map(pathlib.Path, sys.argv[1:4])
canvas = json.loads(canvas_path.read_text())
BOOKS = [
  {"dir": "book-01", "num": "One",   "name": "The Beginning", "range": "Genesis 1–3",   "match": lambda n: not n.startswith(("B2-", "B3-", "B4-")),
   "blurb": "Creation in seven days, the garden of Eden, the serpent, and the way east of Eden."},
  {"dir": "book-02", "num": "Two",   "name": "The Flood",     "range": "Genesis 4–9",   "match": lambda n: n.startswith("B2-"),
   "blurb": "Cain and Abel, the generations of Adam, the ark, the deluge, and the bow in the cloud."},
  {"dir": "book-03", "num": "Three", "name": "The Promise",   "range": "Genesis 11–22", "match": lambda n: n.startswith("B3-"),
   "blurb": "The tower of Babel, the call of Abram, Sodom and Gomorrah, and the mountain of Moriah."},
  {"dir": "book-04", "num": "Four",  "name": "The Ladder",    "range": "Genesis 25–33", "match": lambda n: n.startswith("B4-"),
   "blurb": "Jacob and Esau, the stolen blessing, the ladder at Bethel, and the night of wrestling at Peniel."},
]
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo+Narrow:wght@600;700&family=IBM+Plex+Mono:wght@500;600&family=Noto+Sans+JP:wght@900&display=swap" rel="stylesheet">'
def slug(t):
    t = re.sub(r"^(B\d+ · )?\d+ · ", "", t)
    return re.sub(r"[^a-z0-9]+", "-", t.lower().replace("·", " ")).strip("-")
def esc(s): return html.escape(s, quote=True)

def convert(path):
    s = path.read_text()
    title = re.search(r"<title>(.*?)</title>", s).group(1)
    body = re.search(r"<x-dc>(.*)</x-dc>", s, re.S).group(1)
    style = re.search(r"<helmet>.*?<style>(.*?)</style>.*?</helmet>", body, re.S).group(1)
    body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S).replace("{{accent}}", "#D7261E")
    return title, style.strip(), body.strip()

out.mkdir(parents=True, exist_ok=True)
(out / "assets").mkdir(exist_ok=True); (out / "thumbs").mkdir(exist_ok=True)
manifest = {"title": "Genesis — Bible Manga", "books": []}
for b in BOOKS:
    names = [n for n in canvas["order"] if b["match"](n)]
    pages = []
    for i, n in enumerate(names):
        t = canvas["boards"][n].get("title", n)
        title, style, body = convert(src / n)
        ref, _, heading = title.partition(" — ")
        if "Cover" in t: ref, heading = b["range"], "Cover"
        num = "Cover" if i == 0 else f"Page {i}"
        pages.append({"file": n, "slug": f"{i:02d}-{slug(t)}", "label": re.sub(r'^B\d+ · ', '', t), "heading": heading or t,
                      "ref": ref, "num": num, "style": style, "body": body})
    b["pages"] = pages
    manifest["books"].append({"id": b["dir"], "title": f"Book {b['num']}: {b['name']}", "range": b["range"], "url": f"genesis/{b['dir']}/",
        "pages": [{"title": p["heading"], "ref": p["ref"], "url": f"genesis/{b['dir']}/{p['slug']}.html", "thumb": f"thumbs/{b['dir']}-{p['slug']}.jpg"} for p in pages]})

def bar(crumbs, extra=""):
    c = ' <span aria-hidden="true">/</span> '.join(crumbs)
    return f'<header class="bar"><nav class="crumbs" aria-label="Breadcrumb">{c}</nav>{extra}</header>'

# reader pages
for bi, b in enumerate(BOOKS):
    P = b["pages"]; d = out / "genesis" / b["dir"]; d.mkdir(parents=True, exist_ok=True)
    for i, p in enumerate(P):
        prev = P[i-1]["slug"] + ".html" if i > 0 else (f"../{BOOKS[bi-1]['dir']}/{BOOKS[bi-1]['pages'][-1]['slug']}.html" if bi > 0 else None)
        nxt = P[i+1]["slug"] + ".html" if i < len(P)-1 else (f"../{BOOKS[bi+1]['dir']}/{BOOKS[bi+1]['pages'][0]['slug']}.html" if bi < len(BOOKS)-1 else None)
        links = (f'<link rel="prev" href="{prev}">' if prev else "") + (f'<link rel="next" href="{nxt}">' if nxt else "")
        pn = f'<a class="btn" href="{prev}" rel="prev">‹ Prev</a>' if prev else '<span class="btn off" aria-disabled="true">‹ Prev</span>'
        nn = f'<a class="btn" href="{nxt}" rel="next">Next ›</a>' if nxt else '<span class="btn off" aria-disabled="true">Next ›</span>'
        desc = f"{p['heading']} ({p['ref']}) — Genesis Book {b['num']}: {b['name']}, a manga adaptation of the Bible."
        (d / f"{p['slug']}.html").write_text(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p['heading'])} · Genesis Book {b['num']} · Bible Manga</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(p['heading'])} · Genesis Book {b['num']}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="../../thumbs/{b['dir']}-{p['slug']}.jpg">
{links}
{FONTS}
<link rel="stylesheet" href="../../assets/site.css">
<style>{p['style']}</style>
</head>
<body class="reader">
{bar(['<a href="../../index.html">Genesis</a>', f'<a href="index.html">Book {b["num"]}</a>', f'<span aria-current="page">{esc(p["num"])}</span>'],
     f'<div class="pager">{pn}{nn}</div>')}
<main class="stage" id="stage"><h1 class="sr">{esc(p['heading'])} — {esc(p['ref'])}</h1><div class="sheet" id="sheet">{p['body']}</div></main>
<footer class="foot"><span>{esc(p['ref'])} · {esc(p['heading'])}</span><span>Adapted from the American Standard Version (1901)</span></footer>
<script src="../../assets/site.js"></script>
</body>
</html>
''')
    # book index
    cards = "\n".join(f'''<li><a class="card" href="{p['slug']}.html"><img src="../../thumbs/{b['dir']}-{p['slug']}.jpg" alt="{esc(p['heading'])}" width="380" height="540" loading="lazy"><span class="num">{esc(p['num'])}</span><span class="h">{esc(p['heading'])}</span><span class="ref">{esc(p['ref'])}</span></a></li>''' for p in P)
    (d / "index.html").write_text(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Genesis Book {b['num']}: {b['name']} · Bible Manga</title>
<meta name="description" content="{esc(b['range'])}: {esc(b['blurb'])}">
<meta property="og:image" content="../../thumbs/{b['dir']}-{P[0]['slug']}.jpg">
{FONTS}
<link rel="stylesheet" href="../../assets/site.css">
</head>
<body class="index">
{bar(['<a href="../../index.html">Genesis</a>', f'<span aria-current="page">Book {b["num"]}</span>'])}
<main class="wrap">
  <section class="hero">
    <p class="kicker">Genesis · Book {b['num']} · {esc(b['range'])}</p>
    <h1>{esc(b['name'])}</h1>
    <p class="lede">{esc(b['blurb'])}</p>
    <a class="cta" href="{P[0]['slug']}.html">Start reading ›</a>
  </section>
  <h2 class="sec">Pages</h2>
  <ol class="grid">
{cards}
  </ol>
</main>
<footer class="foot"><span>Bible Manga · Genesis</span><span>Adapted from the American Standard Version (1901)</span></footer>
</body>
</html>
''')

# home
books = "\n".join(f'''<li><a class="book" href="genesis/{b['dir']}/index.html"><img src="thumbs/{b['dir']}-{b['pages'][0]['slug']}.jpg" alt="Genesis Book {b['num']} cover" width="380" height="540" loading="lazy"><span class="kicker">Book {b['num']} · {esc(b['range'])}</span><span class="h">{esc(b['name'])}</span><span class="ref">{esc(b['blurb'])}</span><span class="count">{len(b['pages'])-1} pages</span></a></li>''' for b in BOOKS)
toc = "\n".join(f'''<li><h3><a href="genesis/{b['dir']}/index.html">Book {b['num']}: {esc(b['name'])}</a></h3><ol>''' + "".join(f'<li><a href="genesis/{b["dir"]}/{p["slug"]}.html"><span>{esc(p["num"])}</span> {esc(p["heading"])} <em>{esc(p["ref"])}</em></a></li>' for p in b["pages"]) + "</ol></li>" for b in BOOKS)
(out / "index.html").write_text(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Genesis · Bible Manga</title>
<meta name="description" content="The book of Genesis as a full-color manga, in the style of 1980s cyberpunk comics, adapted from the American Standard Version.">
<meta property="og:image" content="thumbs/book-01-00-cover.jpg">
{FONTS}
<link rel="stylesheet" href="assets/site.css">
</head>
<body class="index home">
{bar(['<span aria-current="page">Genesis</span>'])}
<main class="wrap">
  <section class="hero">
    <p class="kicker">Bible Manga · 創世記</p>
    <h1>Genesis</h1>
    <p class="lede">The first book of the Bible as a full-color manga — from the first light to Jacob's ladder and the brothers' reunion. Adapted from the American Standard Version (1901).</p>
    <a class="cta" href="genesis/{BOOKS[0]['dir']}/{BOOKS[0]['pages'][0]['slug']}.html">Start at the beginning ›</a>
  </section>
  <h2 class="sec">Books</h2>
  <ol class="grid books">
{books}
  </ol>
  <h2 class="sec">All pages</h2>
  <ol class="toc">
{toc}
  </ol>
</main>
<footer class="foot"><span>Bible Manga · Genesis</span><span>Adapted from the American Standard Version (1901)</span></footer>
</body>
</html>
''')
(out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
(out / ".nojekyll").write_text("")
print("built", sum(len(b["pages"]) for b in BOOKS), "pages")
