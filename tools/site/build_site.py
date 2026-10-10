"""Build the static website (_site/, deployed by GitHub Actions) from both editions.

Usage: python3 tools/site/build_site.py <out_dir> <key>=<dir> ...
  - a key naming a folder with volume.json is a FULL-EDITION volume (volumes/<id>/): canvas.json, volume.json, pages/
  - any other key is a DIGEST series flattened into one folder (its pages + canvas.json); its key is digest-<id>
The full edition is listed first on the home page; the digests follow in a second, smaller section.
Every page URL is <path>/<book-or-chapter>/<slug>.html, two levels deep, so relative links are the same everywhere."""
import json, re, sys, html, pathlib
out = pathlib.Path(sys.argv[1])
SRC = {k: pathlib.Path(v) for k, v in (a.split("=", 1) for a in sys.argv[2:])}

# ── the digest editions (first drafts: highlights only, 9–11 pages a book) ──
DIGEST = [
  {"id": "genesis", "name": "Genesis", "kanji": "創世記", "thumb": "",
   "lede": "The first book of the Bible — from the first light to Joseph in Egypt, in five books.",
   "books": [
    {"dir": "book-01", "num": "One",   "name": "The Beginning", "range": "Genesis 1–3",   "match": lambda n: not n.startswith(("B2-", "B3-", "B4-", "B5-")),
     "blurb": "Creation in seven days, the garden of Eden, the serpent, and the way east of Eden."},
    {"dir": "book-02", "num": "Two",   "name": "The Flood",     "range": "Genesis 4–9",   "match": lambda n: n.startswith("B2-"),
     "blurb": "Cain and Abel, the generations of Adam, the ark, the deluge, and the bow in the cloud."},
    {"dir": "book-03", "num": "Three", "name": "The Promise",   "range": "Genesis 11–22", "match": lambda n: n.startswith("B3-"),
     "blurb": "The tower of Babel, the call of Abram, Sodom and Gomorrah, and the mountain of Moriah."},
    {"dir": "book-04", "num": "Four",  "name": "The Ladder",    "range": "Genesis 25–33", "match": lambda n: n.startswith("B4-"),
     "blurb": "Jacob and Esau, the stolen blessing, the ladder at Bethel, and the night of wrestling at Peniel."},
    {"dir": "book-05", "num": "Five",  "name": "The Dreamer",   "range": "Genesis 37–50", "match": lambda n: n.startswith("B5-"),
     "blurb": "Joseph's coat of many colors, the pit, Pharaoh's dreams, the granaries of Egypt, and the brothers forgiven."},
  ]},
  {"id": "exodus", "name": "Exodus", "kanji": "出エジプト記", "thumb": "exodus-",
   "lede": "The second book of the Bible — the bondage in Egypt, Moses at the burning bush, the plagues, the Red Sea, Sinai, and the glory in the tabernacle — complete in five books.",
   "books": [
    {"dir": "book-01", "num": "One", "name": "The Bush That Burned", "range": "Exodus 1–4", "match": lambda n: n == "Main.dc.html" or n.startswith("EX1-"),
     "blurb": "The new king who knew not Joseph, the ark of bulrushes, Moses in Midian, the burning bush, I AM THAT I AM, and the rod."},
    {"dir": "book-02", "num": "Two", "name": "The Plagues", "range": "Exodus 5–11", "match": lambda n: n.startswith("EX2-"),
     "blurb": "Let my people go: the rods that became serpents, the river turned to blood, frogs, lice, flies, hail and fire, locusts, darkness, and the warning of midnight."},
    {"dir": "book-03", "num": "Three", "name": "The Red Sea", "range": "Exodus 12–15", "match": lambda n: n.startswith("EX3-"),
     "blurb": "The passover lamb, the blood on the doorposts, the great cry at midnight, the pillars of cloud and fire, the sea divided, and the song of Miriam."},
    {"dir": "book-04", "num": "Four", "name": "Sinai", "range": "Exodus 16–20", "match": lambda n: n.startswith("EX4-"),
     "blurb": "Manna and quails, water from the rock, Aaron and Hur holding up Moses' hands, the mountain on fire, and the ten commandments."},
    {"dir": "book-05", "num": "Five", "name": "The Glory", "range": "Exodus 24–40", "match": lambda n: n.startswith("EX5-"),
     "blurb": "The tables of stone, the golden calf, the tables broken, Moses in the cleft of the rock, his shining face, and the glory filling the tabernacle."},
  ]},
  {"id": "numbers", "name": "Numbers", "kanji": "民数記", "thumb": "numbers-",
   "lede": "The fourth book of the Bible — highlights from the wilderness: the twelve spies, forty years of wandering, water from the rock, the serpent of brass, and Balaam's ass.",
   "books": [
    {"dir": "book-01", "num": "One", "name": "In the Wilderness", "range": "Numbers 13–24", "match": lambda n: n == "Main.dc.html" or n.startswith("NU1-"),
     "blurb": "The twelve spies and the grapes of Eshcol, the evil report, forty years, the rock smitten twice, the fiery serpents and the serpent of brass, Balaam's ass, and a star out of Jacob."},
  ]},
  {"id": "joshua", "name": "Joshua", "kanji": "ヨシュア記", "thumb": "joshua-",
   "lede": "The sixth book of the Bible — Joshua leads Israel over Jordan: Rahab and the scarlet line, the walls of Jericho, the sun standing still, and choose you this day.",
   "books": [
    {"dir": "book-01", "num": "One", "name": "Jericho", "range": "Joshua 1–24", "match": lambda n: n == "Main.dc.html" or n.startswith("JO1-"),
     "blurb": "Be strong and of good courage, Rahab and the scarlet line, the Jordan heaped up, the prince of Jehovah's host, the walls of Jericho falling flat, the sun standing still, and Joshua's farewell."},
  ]},
  {"id": "judges", "name": "Judges", "kanji": "士師記", "thumb": "judges-",
   "lede": "The seventh book of the Bible — the judges Jehovah raised up: Deborah under her palm-tree, Jael's tent, Gideon's three hundred with trumpets, pitchers and torches, and Samson — complete in two books.",
   "books": [
    {"dir": "book-01", "num": "One", "name": "The Sword of Gideon", "range": "Judges 4–8", "match": lambda n: n == "Main.dc.html" or n.startswith("JG1-"),
     "blurb": "Deborah and Barak, Sisera's chariots routed, the tent of Jael, Gideon in the winepress, the fleece, the three hundred, and the sword of Jehovah and of Gideon."},
    {"dir": "book-02", "num": "Two", "name": "Samson", "range": "Judges 13–16", "match": lambda n: n.startswith("JG2-"),
     "blurb": "The Nazirite from the womb, the young lion, three hundred foxes, the jawbone, the gates of Gaza, Delilah, the seven locks, and the two middle pillars."},
  ]},
  {"id": "ruth", "name": "Ruth", "kanji": "ルツ記", "thumb": "ruth-",
   "lede": "The eighth book of the Bible — Ruth the Moabitess cleaves to Naomi, gleans in the field of Boaz, and becomes the great-grandmother of David.",
   "books": [
    {"dir": "book-01", "num": "One", "name": "Whither Thou Goest", "range": "Ruth 1–4", "match": lambda n: n == "Main.dc.html" or n.startswith("RU1-"),
     "blurb": "The famine and Moab, Orpah's kiss and Ruth's vow, Naomi who called herself Mara, the field of Boaz, the threshing-floor at midnight, and Obed, the father of Jesse, the father of David."},
  ]},
  {"id": "1samuel", "name": "1 Samuel", "kanji": "サムエル記上", "thumb": "1samuel-",
   "lede": "The ninth book of the Bible — Hannah's prayer, the child Samuel who answers in the night, the ark among the Philistines, Israel's first king, and David and Goliath.",
   "books": [
    {"dir": "book-01", "num": "One", "name": "Thy Servant Heareth", "range": "1 Samuel 1–10", "match": lambda n: n == "Main.dc.html" or n.startswith("SA1-"),
     "blurb": "Hannah's vow at Shiloh, the child given to Jehovah, the voice in the night and \"Speak; for thy servant heareth,\" the ark taken and Dagon fallen on his face, the kine that carried it home, and Saul anointed king."},
    {"dir": "book-02", "num": "Two", "name": "The Battle Is Jehovah's", "range": "1 Samuel 16–31", "match": lambda n: n.startswith("SA2-"),
     "blurb": "David anointed among his brethren, the harp for Saul, Goliath of Gath, five smooth stones and a sling, Jonathan's covenant, Saul's spear, the skirt of Saul's robe in the cave, and Saul's end on mount Gilboa."},
  ]},
  {"id": "2samuel", "name": "2 Samuel", "kanji": "サムエル記下", "thumb": "2samuel-",
   "lede": "The tenth book of the Bible — David king over all Israel, the ark brought up to Jerusalem, the promise of a throne for ever, Nathan's word to the king, and Absalom's revolt.",
   "books": [
    {"dir": "book-01", "num": "One", "name": "Thou Art the Man", "range": "2 Samuel 1–12", "match": lambda n: n == "Main.dc.html" or n.startswith("SB1-"),
     "blurb": "David mourns Saul and Jonathan, is anointed king in Hebron and takes Zion, dances before the ark, receives the promise of a house for ever, shows kindness to Mephibosheth, sends Uriah to the forefront of the battle, and hears Nathan's parable of the ewe lamb."},
    {"dir": "book-02", "num": "Two", "name": "O My Son Absalom", "range": "2 Samuel 14–24", "match": lambda n: n.startswith("SB2-"),
     "blurb": "Absalom's beauty and his hair, the hearts he stole at the gate, David's flight weeping up the mount of Olives, the forest of Ephraim and the great oak, the runner with tidings, the king's cry in the chamber over the gate, and the altar on Araunah's threshing-floor."},
  ]},
]
for S in DIGEST:
    S.update(edition="digest", path="digest-" + S["id"], key="digest-" + S["id"])
    for b in S["books"]: b["label"] = f"Book {b['num']}"

# ── the full edition: one volume per Bible book, described by volumes/<id>/volume.json ──
VOLUMES = []
for key, d in SRC.items():
    vj = d / "volume.json"
    if not vj.exists(): continue
    V = json.loads(vj.read_text())
    V.update(edition="full", path=V["id"], key=key)
    for c in V["books"]:
        c["label"] = f"Chapter {c['num']}"
        c["match"] = (lambda pre: (lambda n: n.startswith(tuple(pre))))(c["prefixes"])
    VOLUMES.append(V)
VOLUMES.sort(key=lambda v: v.get("order", 0))
SERIES = VOLUMES + [x for x in DIGEST if x["key"] in SRC]
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

def src_dir(S): return SRC[S["key"]] / ("pages" if S["edition"] == "full" else "")

out.mkdir(parents=True, exist_ok=True)
(out / "assets").mkdir(exist_ok=True); (out / "thumbs").mkdir(exist_ok=True)
manifest = {"title": "Bible Manga", "series": []}
FLAT = {"full": [], "digest": []}   # every book/chapter in reading order, per edition, for prev/next
for S in SERIES:
    canvas = json.loads((SRC[S["key"]] / "canvas.json").read_text())
    ms = {"id": S["id"], "path": S["path"], "edition": S["edition"], "title": S["name"], "books": []}
    for b in S["books"]:
        b["series"] = S
        names = [n for n in canvas["order"] if b["match"](n)]
        pages = []
        for i, n in enumerate(names):
            t = canvas["boards"][n].get("title", n)
            title, style, body = convert(src_dir(S) / n)
            ref, _, heading = title.partition(" — ")
            if "Cover" in t: ref, heading = b["range"], "Cover"
            if S["edition"] == "full":
                pm = re.search(r"— (\d+) —", body)
                num = f"Page {int(pm.group(1))}" if pm else ("Cover" if n == "Main.dc.html" else "Title")
            else:
                num = "Cover" if i == 0 else f"Page {i}"
            pages.append({"file": n, "slug": f"{i:02d}-{slug(t)}", "label": re.sub(r'^B\d+ · ', '', t), "heading": heading or t,
                          "ref": ref, "num": num, "style": style, "body": body})
        b["pages"] = pages; FLAT[S["edition"]].append(b)
        ms["books"].append({"id": b["dir"], "title": f"{b['label']}: {b['name']}", "range": b["range"], "url": f"{S['path']}/{b['dir']}/",
            "pages": [{"title": p["heading"], "ref": p["ref"], "url": f"{S['path']}/{b['dir']}/{p['slug']}.html",
                       "thumb": f"thumbs/{S['thumb']}{b['dir']}-{p['slug']}.jpg", "src": f"{S['key']}/{p['file']}"} for p in pages]})
    manifest["series"].append(ms)
def thumb(b, p): return f"{b['series']['thumb']}{b['dir']}-{p['slug']}.jpg"
def href(frm, b, p):
    """Relative link from book `frm` to page p of book b."""
    if b is frm: return f"{p['slug']}.html"
    if b["series"] is frm["series"]: return f"../{b['dir']}/{p['slug']}.html"
    return f"../../{b['series']['path']}/{b['dir']}/{p['slug']}.html"

def bar(crumbs, extra=""):
    c = ' <span aria-hidden="true">/</span> '.join(crumbs)
    return f'<header class="bar"><nav class="crumbs" aria-label="Breadcrumb">{c}</nav>{extra}</header>'

def edition_tag(S): return "" if S["edition"] == "full" else " (digest)"

# reader pages
for ed, chain in FLAT.items():
  for bi, b in enumerate(chain):
    S = b["series"]; SN = S["name"] + edition_tag(S); L = b["label"]
    P = b["pages"]; d = out / S["path"] / b["dir"]; d.mkdir(parents=True, exist_ok=True)
    crumbs0 = ['<a href="../../index.html">Bible Manga</a>', f'<a href="../../index.html#{S["path"]}">{SN}</a>']
    for i, p in enumerate(P):
        prev = P[i-1]["slug"] + ".html" if i > 0 else (href(b, chain[bi-1], chain[bi-1]["pages"][-1]) if bi > 0 else None)
        nxt = P[i+1]["slug"] + ".html" if i < len(P)-1 else (href(b, chain[bi+1], chain[bi+1]["pages"][0]) if bi < len(chain)-1 else None)
        links = (f'<link rel="prev" href="{prev}">' if prev else "") + (f'<link rel="next" href="{nxt}">' if nxt else "")
        pn = f'<a class="btn" href="{prev}" rel="prev">‹ Prev</a>' if prev else '<span class="btn off" aria-disabled="true">‹ Prev</span>'
        nn = f'<a class="btn" href="{nxt}" rel="next">Next ›</a>' if nxt else '<span class="btn off" aria-disabled="true">Next ›</span>'
        desc = f"{p['heading']} ({p['ref']}) — {SN} {L}: {b['name']}, a manga adaptation of the Bible."
        (d / f"{p['slug']}.html").write_text(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p['heading'])} · {SN} {L} · Bible Manga</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(p['heading'])} · {SN} {L}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="../../thumbs/{thumb(b, p)}">
{links}
{FONTS}
<link rel="stylesheet" href="../../assets/site.css">
<style>{p['style']}</style>
</head>
<body class="reader">
{bar(crumbs0 + [f'<a href="index.html">{L}</a>', f'<span aria-current="page">{esc(p["num"])}</span>'],
     f'<div class="pager">{pn}{nn}</div>')}
<main class="stage" id="stage"><h1 class="sr">{esc(p['heading'])} — {esc(p['ref'])}</h1><div class="sheet" id="sheet">{p['body']}</div></main>
<footer class="foot"><span>{esc(p['ref'])} · {esc(p['heading'])}</span><span>Adapted from the American Standard Version (1901)</span></footer>
<script src="../../assets/site.js"></script>
</body>
</html>
''')
    cards = "\n".join(f'''<li><a class="card" href="{p['slug']}.html"><img src="../../thumbs/{thumb(b, p)}" alt="{esc(p['heading'])}" width="380" height="540" loading="lazy"><span class="num">{esc(p['num'])}</span><span class="h">{esc(p['heading'])}</span><span class="ref">{esc(p['ref'])}</span></a></li>''' for p in P)
    note = "" if ed == "full" else '<p class="note">Digest edition: an early, abridged first draft (highlights only). The full edition is replacing it.</p>'
    (d / "index.html").write_text(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{SN} {L}: {b['name']} · Bible Manga</title>
<meta name="description" content="{esc(b['range'])}: {esc(b['blurb'])}">
<meta property="og:image" content="../../thumbs/{thumb(b, P[0])}">
{FONTS}
<link rel="stylesheet" href="../../assets/site.css">
</head>
<body class="index">
{bar(crumbs0 + [f'<span aria-current="page">{L}</span>'])}
<main class="wrap">
  <section class="hero">
    <p class="kicker">{SN} · {L} · {esc(b['range'])}</p>
    <h1>{esc(b['name'])}</h1>
    <p class="lede">{esc(b['blurb'])}</p>{note}
    <a class="cta" href="{P[0]['slug']}.html">Start reading ›</a>
  </section>
  <h2 class="sec">Pages</h2>
  <ol class="grid">
{cards}
  </ol>
</main>
<footer class="foot"><span>Bible Manga · {SN}</span><span>Adapted from the American Standard Version (1901)</span></footer>
</body>
</html>
''')

# home
def book_card(b):
    S = b["series"]; p0 = b["pages"][0]
    return f'''<li><a class="book" href="{S['path']}/{b['dir']}/index.html"><img src="thumbs/{thumb(b, p0)}" alt="{S['name']} {b['label']} cover" width="380" height="540" loading="lazy"><span class="kicker">{b['label']} · {esc(b['range'])}</span><span class="h">{esc(b['name'])}</span><span class="ref">{esc(b['blurb'])}</span><span class="count">{len(b['pages'])-1} pages</span></a></li>'''
def toc_entry(b):
    S = b["series"]
    return (f'''<li><h3><a href="{S['path']}/{b['dir']}/index.html">{S['name']}{edition_tag(S)} · {b['label']}: {esc(b['name'])}</a></h3><ol>'''
            + "".join(f'<li><a href="{S["path"]}/{b["dir"]}/{p["slug"]}.html"><span>{esc(p["num"])}</span> {esc(p["heading"])} <em>{esc(p["ref"])}</em></a></li>' for p in b["pages"]) + "</ol></li>")
def section(S, cls):
    return f'''  <h3 class="{cls}" id="{S['path']}">{S['name']} <span lang="ja">{S['kanji']}</span></h3>
  <p class="lede">{esc(S['lede'])}</p>
  <ol class="grid books {'digest' if S['edition'] == 'digest' else ''}">
{chr(10).join(book_card(b) for b in S['books'])}
  </ol>'''
full_secs = "\n".join(section(S, "sec") for S in VOLUMES)
digest_secs = "\n".join(section(S, "sec small") for S in SERIES if S["edition"] == "digest")
first = (FLAT["full"] or FLAT["digest"])[0]
vol_names = ", ".join(v["name"] for v in VOLUMES) or "—"
(out / "index.html").write_text(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bible Manga · The Full Edition</title>
<meta name="description" content="The Bible as a full-color manga, in the style of 1980s cyberpunk comics, in the words of the American Standard Version (1901).">
<meta property="og:image" content="thumbs/{thumb(first, first['pages'][0])}">
{FONTS}
<link rel="stylesheet" href="assets/site.css">
</head>
<body class="index home">
{bar(['<span aria-current="page">Bible Manga</span>'])}
<main class="wrap">
  <section class="hero">
    <p class="kicker">Bible Manga · {" · ".join(v["kanji"] for v in VOLUMES)}</p>
    <h1>Bible Manga</h1>
    <p class="lede">The Bible as a full-color manga — one volume per book of the Bible, every scene and every line of dialogue in the words of the American Standard Version (1901). Now in progress: {esc(vol_names)}.</p>
    <a class="cta" href="{first['series']['path']}/{first['dir']}/{first['pages'][0]['slug']}.html">Start at the beginning ›</a>
  </section>
  <h2 class="sec">The Full Edition</h2>
{full_secs}
  <h2 class="sec" id="digest">Digest Editions</h2>
  <p class="note">The first drafts: short books of highlights from Genesis to 2 Samuel. They are being replaced by the full edition, volume by volume.</p>
{digest_secs}
  <h2 class="sec">All pages</h2>
  <ol class="toc">
{chr(10).join(toc_entry(b) for b in FLAT["full"] + FLAT["digest"])}
  </ol>
</main>
<footer class="foot"><span>Bible Manga</span><span>Adapted from the American Standard Version (1901)</span></footer>
</body>
</html>
''')
(out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
(out / ".nojekyll").write_text("")
print("built", sum(len(b["pages"]) for e in FLAT.values() for b in e), "pages")
