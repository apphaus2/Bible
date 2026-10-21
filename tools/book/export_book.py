"""Export a full-edition volume as an e-book and a print-ready PDF, from the same pages the website uses.

Usage (from the repo root):  python3 tools/book/export_book.py genesis [--no-fonts] [--out _book] [--epub-only | --pdf-only]

Writes (git-ignored):
  _book/<vol>.epub         fixed-layout EPUB 3: one XHTML page per manga page (vector art, live text), 760×1080
                           viewport, a cover image, a table of contents by chapter and a page list with printed numbers
  _book/<vol>-print.pdf    print PDF, 7 × 10 in trim plus 0.125 in bleed (7.25 × 10.25 in sheets), all vector.
                           Story pages are fitted to the trim width on paper colour; full-bleed pages (cover, chapter
                           titles) are scaled to fill the bleed box, so trim the art, not white edges.

Fonts: the pages load Anton, IBM Plex Mono, Archivo Narrow and Noto Sans JP from Google Fonts, which an e-reader or
printer will not do. Unless --no-fonts is given, the exporter downloads each family from the Google Fonts API, subset to
just the characters the volume uses (all four are under the SIL Open Font License, so embedding is allowed), caches them
in _book/fonts/ and embeds them in both outputs.

Needs Node with Playwright (as for tools/site/shots.js) for the PDF and the cover image."""
import sys, re, json, html, uuid, zipfile, shutil, hashlib, pathlib, argparse, datetime, subprocess, urllib.parse, urllib.request
import xml.dom.minidom

ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
FAMILIES = {"Anton": [400], "IBM Plex Mono": [500, 600], "Archivo Narrow": [600, 700], "Noto Sans JP": [900]}
sys.path.insert(0, str(ROOT / "tools" / "lang"))
import langs                         # a translated edition adds the families its script needs (tools/lang/<code>.json)
LANG = "en"
TRIM, BLEED, DPI = (7.0, 10.0), 0.125, 96          # inches; CSS px per inch
W, H = 760, 1080                                    # page size in CSS px
ACCENT = "#D7261E"

# ---- reading the volume -------------------------------------------------------------------------------------------
def load_volume(vol, lang="en"):
    d = ROOT / "volumes" / (vol if lang == "en" else f"{lang}/{vol}")
    meta = json.loads((d / "volume.json").read_text(encoding="utf-8"))
    canvas = json.loads((d / "canvas.json").read_text(encoding="utf-8"))
    pages = []
    for i, name in enumerate(canvas["order"]):
        src = (d / "pages" / name).read_text(encoding="utf-8")
        title = canvas["boards"][name].get("title", name)
        chap = next((c for c in meta["books"] if any(name.startswith(p) for p in c["prefixes"])), None)
        m = re.match(r"(\d+) · ", title)
        pages.append({"i": i + 1, "name": name, "title": title, "chapter": chap, "printed": m.group(1) if m else None,
                      "root": root_div(src), "full": "padding: 28px 26px 30px" not in src.split("<x-dc>")[1][:2000]})
    return meta, pages

def root_div(src):
    """The page's own markup: everything inside <x-dc> after the <helmet> (fonts and styles are supplied by the book)."""
    body = src.split("</helmet>", 1)[1].split("</x-dc>", 1)[0]
    return body.strip().replace("{{accent}}", ACCENT)

# ---- fonts ------------------------------------------------------------------------------------------------------------
def page_chars(pages):
    text = "".join(html.unescape(re.sub(r"<[^>]+>", " ", p["root"])) for p in pages)
    return "".join(sorted(set(text) - set("\n\r\t")))

def fetch_fonts(pages, out):
    """Download every family subset to the characters in use; returns [(family, weight, file)] (cached by content hash)."""
    chars = page_chars(pages) + "0123456789—–·…'’ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    chars = "".join(sorted(set(chars)))
    key = hashlib.sha1(chars.encode()).hexdigest()[:10]
    fdir = out / "fonts"; fdir.mkdir(parents=True, exist_ok=True)
    index = fdir / f"fonts-{key}.json"
    if index.exists():
        return [tuple(x) for x in json.loads(index.read_text())]
    got = []
    pieces = langs.text_pieces(chars)                  # a CJK volume's characters go in several requests
    for fam, weights in FAMILIES.items():
      for n, (part, rng) in enumerate(pieces):
        q = urllib.parse.urlencode({"family": f"{fam}:wght@{';'.join(map(str, weights))}", "text": part, "display": "swap"})
        req = urllib.request.Request("https://fonts.googleapis.com/css2?" + q, headers={"User-Agent": "Wget/1.21"})   # plain UA → TrueType
        css = urllib.request.urlopen(req, timeout=30).read().decode()
        for block in re.findall(r"@font-face\s*{(.*?)}", css, re.S):
            wt = int(re.search(r"font-weight:\s*(\d+)", block).group(1))
            url = re.search(r"url\((.*?)\)", block).group(1)
            ext = "woff2" if "woff2" in block else "ttf"
            fn = f"{fam.replace(' ', '')}-{wt}-{key}{f'-{n}' if rng else ''}.{ext}"
            try: (fdir / fn).write_bytes(urllib.request.urlopen(url, timeout=60).read())
            except urllib.request.HTTPError:
                if rng: continue                       # a piece with no glyph in this family (Anton for kanji) is refused
                raise
            got.append((fam, wt, fn) + ((rng,) if rng else ()))
            print(f"  font {fam} {wt}: {(fdir / fn).stat().st_size // 1024} KB")
    index.write_text(json.dumps(got))
    return got

def font_css(fonts, prefix):
    mime = lambda fn: "woff2" if fn.endswith("woff2") else "truetype"
    return "".join(f"@font-face {{ font-family: '{fam}'; font-weight: {wt}; font-style: normal; src: url('{prefix}{fn}') format('{mime(fn)}');"
                   f"{f' unicode-range: {rng[0]};' if rng else ''} }}\n" for fam, wt, fn, *rng in fonts)

# ---- EPUB -------------------------------------------------------------------------------------------------------------
def to_xhtml(markup):
    """The page markup made into well-formed XHTML: SVG namespaces, xlink hrefs, valued attributes, closed void tags."""
    s = re.sub(r"\s(data-label)(?=[\s>])", r' \1=""', markup)
    s = re.sub(r"<br\s*>", "<br/>", s)
    s = re.sub(r"<svg(?![^>]*xmlns=)", '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"', s)
    s = s.replace("<use href=", "<use xlink:href=")
    return s

def xhtml_page(title, body, css="../css/book.css"):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html>\n'
            f'<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{LANG}" lang="{LANG}">\n'
            f'<head>\n<meta charset="utf-8"/>\n<title>{html.escape(title)}</title>\n<meta name="viewport" content="width={W}, height={H}"/>\n'
            f'<link rel="stylesheet" type="text/css" href="{css}"/>\n</head>\n<body>\n{body}\n</body>\n</html>\n')

def write_epub(vol, meta, pages, fonts, cover_jpg, out):
    book_id = f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, 'https://github.com/apphaus2/Bible/' + vol)}"
    E = langs.get(meta.get("lang", "en"))["epub"]
    title = f"{meta['name']} — {E['title']}"
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    files = {}                                                                  # path in OEBPS -> bytes
    files["css/book.css"] = (font_css(fonts, "../fonts/") + f"html, body {{ margin: 0; padding: 0; width: {W}px; height: {H}px; overflow: hidden; }}\n").encode()
    for fam, wt, fn, *_ in fonts:
        files[f"fonts/{fn}"] = (out / "fonts" / fn).read_bytes()
    items, spine = [], []
    for p in pages:
        x = xhtml_page(p["title"], to_xhtml(p["root"]))
        try: xml.dom.minidom.parseString(x.encode())
        except Exception as e: raise SystemExit(f"{p['name']}: not well-formed XHTML after conversion: {e}")
        fn = f"pages/p{p['i']:03d}.xhtml"
        files[fn] = x.encode()
        items.append(f'<item id="p{p["i"]:03d}" href="{fn}" media-type="application/xhtml+xml" properties="svg"/>')
        spine.append(f'<itemref idref="p{p["i"]:03d}"/>')
    # navigation: chapters (their title pages) and a page list with the printed numbers
    WD = (E["cover"], E["chapter"], E["contents"], E["pages"])
    toc = [f'<li><a href="pages/p001.xhtml">{WD[0]}</a></li>']
    for c in meta["books"]:
        first = next(p for p in pages if p["chapter"] is c and p["name"] != "Main.dc.html")
        toc.append(f'<li><a href="pages/p{first["i"]:03d}.xhtml">{langs.numbered(WD[1], c["num"])} · {html.escape(c["name"])} ({c["range"]})</a></li>')
    plist = [f'<li><a href="pages/p{p["i"]:03d}.xhtml">{p["printed"]}</a></li>' for p in pages if p["printed"]]
    nav = (f'<nav epub:type="toc" id="toc"><h1>{WD[2]}</h1><ol>{"".join(toc)}</ol></nav>\n'
           f'<nav epub:type="page-list" hidden=""><h1>{WD[3]}</h1><ol>{"".join(plist)}</ol></nav>')
    files["nav.xhtml"] = xhtml_page(WD[2], nav, css="css/book.css").replace(f'<meta name="viewport" content="width={W}, height={H}"/>\n', "").encode()
    items.append('<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>')
    items.append('<item id="css" href="css/book.css" media-type="text/css"/>')
    for k, (fam, wt, fn) in enumerate(fonts):
        items.append(f'<item id="font{k}" href="fonts/{fn}" media-type="{"font/woff2" if fn.endswith("woff2") else "font/ttf"}"/>')
    if cover_jpg:
        files["images/cover.jpg"] = cover_jpg.read_bytes()
        items.append('<item id="cover-image" href="images/cover.jpg" media-type="image/jpeg" properties="cover-image"/>')
    opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="{meta.get("lang", "en")}" prefix="rendition: http://www.idpf.org/vocab/rendition/#">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{book_id}</dc:identifier>
<dc:title>{html.escape(title)}</dc:title>
<dc:language>{meta.get("lang", "en")}</dc:language>
<dc:creator>Sky Morey</dc:creator>
<dc:description>{html.escape(meta["lede"])}</dc:description>
<dc:rights>Scripture text: {meta.get("translation", "ASV")}, public domain.</dc:rights>
<meta property="dcterms:modified">{now}</meta>
<meta property="rendition:layout">pre-paginated</meta>
<meta property="rendition:orientation">portrait</meta>
<meta property="rendition:spread">landscape</meta>
{'<meta name="cover" content="cover-image"/>' if cover_jpg else ''}
</metadata>
<manifest>
{chr(10).join(items)}
</manifest>
<spine page-progression-direction="ltr">
{chr(10).join(spine)}
</spine>
</package>
'''
    container = ('<?xml version="1.0" encoding="UTF-8"?>\n<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n'
                 '<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>\n</container>\n')
    path = out / f"{vol}.epub"
    with zipfile.ZipFile(path, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)   # must be first, uncompressed
        z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
        for fn, data in files.items():
            z.writestr("OEBPS/" + fn, data, compress_type=zipfile.ZIP_DEFLATED)
    return path

# ---- print PDF ----------------------------------------------------------------------------------------------------------
def prefix_ids(markup, p):
    """Make every SVG id unique to its page, so all pages can share one print document."""
    ids = set(re.findall(r'\sid="([^"]+)"', markup))
    def sub(m): return m.group(1) + p + m.group(2) + m.group(3) if m.group(2) in ids else m.group(0)
    markup = re.sub(r'(\sid=")([^"]+)(")', sub, markup)
    markup = re.sub(r'(href="#)([^"]+)(")', sub, markup)
    return re.sub(r'(url\(#)([^)]+)(\))', sub, markup)

def print_html(pages, fonts, fontdir):
    bw, bh = (TRIM[0] + 2 * BLEED) * DPI, (TRIM[1] + 2 * BLEED) * DPI
    sheets = []
    for p in pages:
        if p["full"]:                                   # full-bleed art: fill the bleed box
            s = max(bw / W, bh / H)
        else:                                           # story page: fit the trim width; the paper gutter fills the rest
            s = TRIM[0] * DPI / W
        left, top = (bw - W * s) / 2, (bh - H * s) / 2
        sheets.append(f'<section class="sheet"><div class="pg" style="left: {left:.2f}px; top: {top:.2f}px; transform: scale({s:.5f})">'
                      f'{prefix_ids(p["root"], f"s{p["i"]}_")}</div></section>')
    css = (font_css(fonts, fontdir.as_uri() + "/") +
           f"@page {{ size: {TRIM[0] + 2 * BLEED}in {TRIM[1] + 2 * BLEED}in; margin: 0; }}\n"
           "html, body { margin: 0; padding: 0; }\n"
           f".sheet {{ position: relative; width: {bw}px; height: {bh}px; overflow: hidden; background: #F3EFE6; break-after: page; }}\n"
           f".pg {{ position: absolute; width: {W}px; height: {H}px; transform-origin: 0 0; }}\n")
    return f'<!doctype html>\n<html lang="{LANG}"><head><meta charset="utf-8"><style>{css}</style></head><body>\n' + "\n".join(sheets) + "\n</body></html>\n"

def screen_html(pages, fonts, fontdir):
    """The reading PDF: every page at its own 760×1080 size, no bleed (for screens; the print PDF is print_html)."""
    sheets = [f'<section class="sheet">{prefix_ids(p["root"], f"s{p["i"]}_")}</section>' for p in pages]
    css = (font_css(fonts, fontdir.as_uri() + "/") +
           f"@page {{ size: {W}px {H}px; margin: 0; }}\n"
           "html, body { margin: 0; padding: 0; }\n"
           f".sheet {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #F3EFE6; break-after: page; }}\n")
    return f'<!doctype html>\n<html lang="{LANG}"><head><meta charset="utf-8"><style>{css}</style></head><body>\n' + "\n".join(sheets) + "\n</body></html>\n"

LIMIT = 24 * 1024 * 1024                     # Cloudflare serves no single file over 25 MiB: bigger books are split into parts

def screen_pdfs(vol, meta, pages, fonts, out, work):
    """<vol>.pdf, or <vol>-1.pdf, <vol>-2.pdf … split at chapter boundaries when one file would pass LIMIT.
    Returns [{"file", "size", "range", "pages"}], one per file."""
    chaps = meta["books"]
    groups = [[c] for c in chaps]
    def pages_of(group):
        first = group[0] is chaps[0]
        return [p for p in pages if p["chapter"] in group or (first and p["chapter"] is None)]
    def render(group, fn):
        (work / "screen.html").write_text(screen_html(pages_of(group), fonts, out / "fonts"), encoding="utf-8")
        node("pdf", work / "screen.html", out / fn)
        return (out / fn).stat().st_size
    size = render(chaps, f"{vol}.pdf")
    if size <= LIMIT:
        parts = [(chaps, f"{vol}.pdf", size)]
    else:
        (out / f"{vol}.pdf").unlink()
        k = -(-size * 11 // 10 // LIMIT)               # parts needed, with 10% to spare
        while True:
            per = -(-len(pages) // k); parts, cur = [], []
            for c in chaps:                            # fill each part with whole chapters up to ~len/k pages
                cur.append(c)
                if len(pages_of(cur)) >= per and len(parts) < k - 1: parts.append(cur); cur = []
            if cur: parts.append(cur)
            done = [(g, f"{vol}-{i + 1}.pdf", render(g, f"{vol}-{i + 1}.pdf")) for i, g in enumerate(parts)]
            if all(s <= LIMIT for _, _, s in done): parts = done; break
            for _, fn, _ in done: (out / fn).unlink()
            k += 1
    def rng(g):                                  # "Genesis 1–27": whole Bible chapters, even when a manga chapter ends mid-chapter
        a, b = g[0]["range"], g[-1]["range"]
        if a == b: return a
        start, end = a.rsplit(' ', 1)[1].split('–')[0], b.rsplit(' ', 1)[1].split('–')[-1]
        return f"{a.rsplit(' ', 1)[0]} {start.split(':')[0]}–{end.split(':')[0]}"
    return [{"file": fn, "size": s, "range": rng(g), "pages": len(pages_of(g))} for g, fn, s in parts]

def node(*args):
    subprocess.run(["node", str(HERE / "render.js"), *map(str, args)], check=True)

# ---- main -----------------------------------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("volume"); ap.add_argument("--out", default="_book"); ap.add_argument("--no-fonts", action="store_true")
    g = ap.add_mutually_exclusive_group(); g.add_argument("--epub-only", action="store_true"); g.add_argument("--pdf-only", action="store_true")
    ap.add_argument("--lang", default="en", help="build from volumes/<lang>/ (a translated edition)")
    ap.add_argument("--screen", action="store_true", help="the reading PDF(s) at page size, split under 24 MB, instead of the print PDF")
    a = ap.parse_args()
    global LANG
    LANG = a.lang
    FAMILIES.update(langs.get(LANG).get("fonts", {}).get("load", {}))
    out = (ROOT / a.out).resolve(); out.mkdir(parents=True, exist_ok=True)
    meta, pages = load_volume(a.volume, a.lang)
    print(f"{a.volume}: {len(pages)} pages in {len(meta['books'])} chapters")
    fonts = [] if a.no_fonts else fetch_fonts(pages, out)
    if not fonts: print("  (no fonts embedded: readers and printers will substitute their own)")
    work = out / "work"; work.mkdir(exist_ok=True)
    if a.screen and not a.epub_only:
        parts = screen_pdfs(a.volume, meta, pages, fonts, out, work)
        (out / f"{a.volume}.pdfs.json").write_text(json.dumps(parts))
        for x in parts: print(f"  {x['file']}  ({x['size'] // 1024} KB, {x['pages']} pages, {x['range']})")
    elif not a.epub_only:
        (work / "print.html").write_text(print_html(pages, fonts, out / "fonts"), encoding="utf-8")
        pdf = out / f"{a.volume}-print.pdf"
        node("pdf", work / "print.html", pdf)
        print(f"  {pdf.relative_to(ROOT)}  ({pdf.stat().st_size // 1024} KB, {TRIM[0]} x {TRIM[1]} in + {BLEED} in bleed)")
    if not a.pdf_only:
        cover, cover_jpg = pages[0], work / "cover.jpg"
        (work / "cover-page.html").write_text(
            f'<!doctype html><html><head><meta charset="utf-8"><style>{font_css(fonts, (out / "fonts").as_uri() + "/")}html,body{{margin:0}}</style></head>'
            f'<body>{cover["root"]}</body></html>', encoding="utf-8")
        node("cover", work / "cover-page.html", cover_jpg)
        epub = write_epub(a.volume, meta, pages, fonts, cover_jpg, out)
        print(f"  {epub.relative_to(ROOT)}  ({epub.stat().st_size // 1024} KB, fixed layout {W} x {H})")

if __name__ == "__main__":
    main()
