# ADR 0001 — Attribute the translation as "ASV"

- **Status:** accepted
- **Date:** 2026-10-12

## Context

Every word of the manga is taken from the ASV (`ref/eng-asv`). The pages named it inconsistently:
the volume cover and chapter title pages spelled out the full name with the year, and the running
foot on story pages added the year after "ASV". The website footers and the e-book metadata spelled it out
with the year as well.

## Decision

The translation is always written **"ASV"**: never spelled out, never with the year, and on its own —
not inside a phrase such as "Every word from the ASV".

- **Story pages:** the running foot (`fx.page()`) shows the verses at the left, `— NN —` in the
  centre and `ASV` at the right.
- **Chapter title pages** (`fx.chapter_title()`): the credit line reads "Genesis · Volume One · ASV".
- **Volume covers:** "ASV" at the bottom left, opposite "Vol. N" (once only; the chapters line carries no credit).
- **Website** (`tools/site/build_site.py`): page footers read "ASV"; descriptions say "the ASV".
- **E-book** (`tools/book/export_book.py`): rights metadata reads "Scripture text: ASV, public domain."
- **Docs:** README and CLAUDE.md say "ASV".
- **Translations** (added later): each language's pages, site and e-books carry its own text's short credit in the same
  places (`credit` in `tools/lang/<code>.json`: RV1909, LUTHER 1912, LSG, Riveduta, BPM, Синод., 和合本, フリーダム訳, 개역).

## Consequences

- One short, consistent mark on every page, matching the verse labels (`GEN 1:1`) in style.
- The full name of the translation does not appear anywhere in the edition.
- The legacy digest pages that predated this decision have since been removed from the repo; the drawings they held
  survive only as reference art (`tools/full/reference/`), which is never published.
