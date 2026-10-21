"""Build one volume of the full edition.

Usage (from the repo root):  python3 tools/full/build_volume.py genesis [--check]   (Exodus: build_volume.py exo)
  --check  writes nothing: regenerates every page in memory, fails if a committed page differs from what the
           plan would produce, and runs the ASV text check (GitHub Actions runs this on every push).

Reads tools/full/<volume>/ (META in __init__.py, cover.py, one module per manga chapter) and writes volumes/<volume>/:
  pages/*.dc.html   every page (Main.dc.html is the volume cover)
  canvas.json       the Claude Design canvas index (boards in reading order, one block of rows per chapter)
  volume.json       what the website needs (chapters, page prefixes, blurbs)
  coverage.md       every Bible verse in the chapters built so far: full / partial / omitted
Then it checks every caption, balloon and title quote against the ASV text and stops on any mismatch."""
import sys, json, re, html, pathlib, importlib, datetime

def save(path, text):
    """Write UTF-8 with LF line endings on every platform (Windows would otherwise write CRLF)."""
    path.write_bytes(text.encode("utf-8"))
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "kit"))

def main(vol, check=False):
    import asv                                                        # BIBLE_LANG=es builds the Spanish edition (see asv.py)
    pkg = importlib.import_module(vol)
    META, G = pkg.META, pkg.G
    out = ROOT / "volumes" / (META["id"] if asv.LANG == "en" else f"{asv.LANG}/{META['id']}")
    pages_dir = out / "pages"; pages_dir.mkdir(parents=True, exist_ok=True)
    if asv.LANG == "en": credit = lab = lambda h: h
    else:                                                             # another language: its credit, and every label translated
        import labels
        tab = labels.table(asv.LANG)
        credit = lambda h: labels.translate(h.replace(">ASV<", f">{asv.CREDIT}<").replace("· ASV<", f"· {asv.CREDIT}<"), asv.LANG, tab)
        lab = lambda t: labels.label(labels.norm(t), asv.LANG, tab)
    cover = importlib.import_module(f"{vol}.cover").cover
    order = [("Main.dc.html", "Cover", cover)]
    chapters = []
    for c in META["chapters"]:
        mod = importlib.import_module(f"{vol}.{c['module']}")
        names = [(f"{n}.dc.html", t, fn) for n, t, fn in mod.PAGES]
        order += names
        prefix = "-".join(names[0][0].split("-")[:2]) + "-"                # e.g. GEN-C01-
        chapters.append(dict(c, prefixes=(["Main.dc.html"] if c is META["chapters"][0] else []) + [prefix], files=[n for n, _, _ in names]))
    written = set()
    stale_pages = []
    for name, _, fn in order:
        html_ = credit(fn()); written.add(name)
        if check:
            f = pages_dir / name
            if not f.exists() or f.read_text() != html_: stale_pages.append(name)
        else:
            save(pages_dir / name, html_)
    for stale in pages_dir.glob("*.dc.html"):
        if stale.name not in written:
            stale_pages.append(stale.name) if check else stale.unlink()
    if check and stale_pages:
        print("OUT OF DATE (re-run build_volume.py and commit):", ", ".join(stale_pages)); sys.exit(1)

    # canvas: the cover, then each chapter as its own block of rows (5 boards a row), with a title note above each block
    cpath = out / "canvas.json"
    old = json.loads(cpath.read_text()) if cpath.exists() else {}
    boards, notes, y = {}, {}, 0
    blocks = [("Main", META["title"], ["Main.dc.html"])] + [(c["dir"], f"Chapter {c['num']} · {c['name']} ({c['range']})", c["files"]) for c in chapters]
    titles = {n: lab(t) for n, t, _ in order}
    for key, label, files in blocks:
        notes[key.replace("-", "")] = {"kind": "title1", "maxW": 4120, "text": label, "x": 0, "y": y}
        y += 300
        for i, n in enumerate(files):
            boards[n] = {"x": (i % 5) * 840, "y": y + (i // 5) * 1200, "w": 760, "h": 1080, "title": titles[n]}
        y += ((len(files) - 1) // 5 + 1) * 1200 + 200
    canvas = {"v": 3, "createdOnFiles": old.get("createdOnFiles") or {"v": 1, "at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")},
              "title": f"{META['name']} — Full Edition", "launch": {"view": "canvas"}, "pages": [],
              "boards": boards, "order": [n for n, _, _ in order], "notes": notes, "designSystems": [], "attachments": {}}
    if not check: save(cpath, json.dumps(canvas, indent=1, ensure_ascii=False))

    if not check: save(out / "volume.json", json.dumps({k: (lab(META[k]) if k in ("name", "lede") else META[k]) for k in ("id", "order", "name", "kanji", "thumb", "lede")}
        | ({"lang": asv.LANG, "en_name": META["name"]} if asv.LANG != "en" else {}) | {
        "books": [{k: (lab(c[k]) if k in ("name", "range", "blurb") else c[k]) for k in ("dir", "num", "name", "range", "blurb", "prefixes")} for c in chapters]}, indent=1, ensure_ascii=False))

    # coverage report
    lines = [f"# {META['name']} — coverage of the full edition", "",
             "Every verse of the chapters built so far, checked against `ref/eng-asv`. **full** = every word on the page; "
             "**partial** = abridged (cuts marked with …); **omitted** = not on any page.", ""]
    tot = {"full": 0, "partial": 0, "omitted": 0}
    for c in chapters:
        rows = G.coverage(c["bible_chapters"], c.get("span"))
        n = {s: sum(1 for r in rows if r[1] == s) for s in tot}
        for s in tot: tot[s] += n[s]
        lines += [f"## Chapter {c['num']} · {c['name']} ({c['range']})", "",
                  f"{len(rows)} verses: {n['full']} full, {n['partial']} partial, {n['omitted']} omitted.", ""]
        odd = [f"- {r[0]} — {r[1]} ({r[2]:.0%})" for r in rows if r[1] != "full"]
        lines += (odd or ["Every verse is on the page in full."]) + [""]
    if getattr(G, "borrowed", None):                                  # a translation's file lost these verses (asv.FALLBACK)
        lines += [f"Taken from `{asv.FALLBACK[asv.TEXTS[asv.LANG][0]]}` because the `{asv.TEXTS[asv.LANG][0]}` file lacks them: "
                  + ", ".join(f"{c}:{v}" for c, v in sorted(G.borrowed)) + ".", ""]
    allv = sum(tot.values())
    lines.insert(4, f"**So far:** {allv} verses — {tot['full']} full, {tot['partial']} partial, {tot['omitted']} omitted.\n")
    if not check: save(out / "coverage.md", "\n".join(lines))

    # text check: every uppercase text block must be a run of the ASV (… marks a cut). Labels that are not
    # scripture (titles, credits) carry data-label and are skipped.
    norm = lambda t: re.sub(r"\s+", " ", t.replace("\u2019", "'")).strip().lower()
    full = norm(G.text()); bad = n = 0
    for p in sorted(pages_dir.glob("*.dc.html")):
        # leaf text boxes only: a div/h1 whose body holds no tags but <br> (a wider match would swallow the first caption of a panel)
        for _, attrs, body in re.findall(r'<(div|h1)([^>]*)>((?:[^<]|<br\s*/?>)*)</\1>', p.read_text(), re.S):
            if "text-transform: uppercase" not in attrs or "data-label" in attrs: continue
            t = html.unescape(re.sub(r"<br\s*/?>", " ", body))
            for seg in [x for x in t.split("…") if x.strip()]:
                n += 1
                if norm(seg) not in full:
                    bad += 1; print("NOT ASV:", p.name, "|", seg[:100])
    # lost-text check: every piece of the ASV the plan cut out must be on some page (coverage counts the cuts, so a
    # page dropped by a layout bug would otherwise still count its verses as full)
    every = norm(html.unescape(re.sub(r"<[^>]+>", " ", " ".join(p.read_text() for p in pages_dir.glob("*.dc.html")))))
    lost = {}
    for r, t in G.cuts:
        if norm(t).rstrip(":;,.") not in every: lost.setdefault(r, t)   # a trailing stop may be trimmed on the page
    for r, t in lost.items(): print("CUT BUT NOT ON ANY PAGE:", r, "|", t[:80])
    print(f"{vol}: {len(order)} pages, {n} text blocks checked, {bad} not found, {len(lost)} lost; coverage {tot}")
    if bad or lost: sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1], check="--check" in sys.argv)
