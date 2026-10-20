# Bible Manga

**Read it: https://bible.apphaus.us**

The Bible as a full-color manga in a 1980s cyberpunk-manga style, in the words of the
ASV. On every push to `master` GitHub Actions builds the website and deploys it to Cloudflare
(the Worker `bible`, at bible.apphaus.us) and to GitHub Pages (apphaus2.github.io/Bible).

- **The manga** (`volumes/`): one volume per book of the Bible, every scene and every line of
  dialogue word for word. In progress: Genesis through 2 Kings so far.
- **The text** (`bible-asv.pdf` and `asv/<BOOK>.pdf` on the site): the whole ASV, Genesis to Revelation, as one PDF
  and as one small PDF per book; each manga page's "📖 p. N" button opens its book's PDF at that page's chapter.
- `tools/full/reference/` keeps the old first drafts' pages whose drawings the volumes reuse (never published).

## Build

```
python3 tools/full/build_volume.py genesis     # write volumes/genesis/ and check every line against ref/eng-asv
python3 tools/book/asv_pdf.py                  # _book/bible-asv.pdf and _book/asv/*.pdf (needs Playwright 1.49+ and pypdf)
python3 tools/site/rebuild_site.py --thumbs    # local preview in _site/ (needs node + Playwright + Pillow)
```

Text source: `ref/eng-asv/` (USFM from eBible.org, public domain). See `CLAUDE.md` for the full working notes.
