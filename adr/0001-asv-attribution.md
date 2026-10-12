# ADR 0001 — Attribute the translation as "ASV"

- **Status:** accepted
- **Date:** 2026-10-12

## Context

Every word of the manga is taken from the ASV (`ref/asv`). The pages named it inconsistently:
the volume cover and chapter title pages spelled out the full name with the year, and the running
foot on story pages added the year after "ASV". The website footers and the e-book metadata spelled it out
with the year as well.

## Decision

The translation is always written **"ASV"**: never spelled out, and never with the year.

- **Story pages:** the running foot (`fx.page()`) shows the verses at the left, `— NN —` in the
  centre and `ASV` at the right.
- **Chapter title pages** (`fx.chapter_title()`): "Every word from the ASV" under the credit.
- **Volume covers:** "Chapters a – b · ASV" and "Every word from the ASV".
- **Website** (`tools/site/build_site.py`): page footers read "ASV"; descriptions say "the ASV".
- **E-book** (`tools/book/export_book.py`): rights metadata reads "Scripture text: ASV, public domain."
- **Docs:** README and CLAUDE.md say "ASV".

## Consequences

- One short, consistent mark on every page, matching the verse labels (`GEN 1:1`) in style.
- The full name of the translation does not appear anywhere in the edition.
- The legacy digest pages (`digest/`) predate this decision and still spell it out; they are not
  being extended and are left as they are.
