# Bible Manga

**Read it: https://apphaus2.github.io/Bible/**

The Bible as a full-color manga in a 1980s cyberpunk-manga style, in the words of the
ASV. GitHub Actions builds the website and deploys it to
GitHub Pages on every push to `master`.

- **Full edition** (`volumes/`): one volume per book of the Bible, every scene and every line of
  dialogue word for word. In progress, starting with Genesis.
- **Digest edition** (`digest/`): the first drafts, short books of highlights from Genesis to 2 Samuel.
  Legacy; being replaced by the full edition.
- **The text** (`bible-asv.pdf` on the site): the whole ASV, Genesis to Revelation, as one PDF with
  bookmarks for every chapter; each manga page's "ASV" credit opens it at that page's chapter.

## Build

```
python3 tools/full/build_volume.py genesis     # write volumes/genesis/ and check every line against ref/asv
python3 tools/book/asv_pdf.py                  # _book/bible-asv.pdf, the ASV text (needs Playwright 1.49+ and pypdf)
python3 tools/site/rebuild_site.py --thumbs    # local preview in _site/ (needs node + Playwright + Pillow)
```

Text source: `ref/asv/` (USFM from eBible.org, public domain). See `CLAUDE.md` for the full working notes.
