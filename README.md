# Bible Manga

**Read it: https://bible.apphaus.us**

The Bible as a full-color manga in a 1980s cyberpunk-manga style, in the words of the
ASV, with editions in Spanish, German, French, Italian, Portuguese, Russian, Chinese, Japanese and Korean. The site is
built locally and deployed to Cloudflare (the Worker `bible`, at bible.apphaus.us); on every push to `master` GitHub
Actions checks every page against the ASV.

- **The manga** (`volumes/`): one volume per book of the Bible, every scene and every line of
  dialogue word for word. The whole Old Testament so far; the New Testament is next.
- **The text** (`asv/<BOOK>.pdf` on the site): the whole ASV, Genesis to Revelation, as one small PDF per book; each manga
  page's "📖 p. N" button opens its book's PDF at that page's chapter.
- `tools/full/reference/` keeps the old first drafts' pages whose drawings the volumes reuse (never published).

## Build

```
python3 tools/full/build_volume.py genesis     # write volumes/genesis/ and check every line against ref/eng-asv
python3 tools/book/asv_pdf.py                  # _book/bible-asv.pdf and _book/asv/*.pdf (needs Playwright 1.49+ and pypdf)
python3 tools/site/rebuild_site.py --thumbs    # local preview in _site/ (needs node + Playwright + Pillow)
```

Text source: `ref/eng-asv/` (USFM from eBible.org, public domain). See `CLAUDE.md` for the full working notes.
