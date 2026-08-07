# Docx Layout

Layout intent for the final skill step, handed to the `document-skills:docx`
skill alongside the assembled markdown. Holds intent only — no docx-js
mechanics here.

## Source of truth

The generated markdown (matching `handover-template.md` exactly, filled)
*is* the content. The docx render is a direct conversion, not a
re-derivation — don't re-summarize or reorder anything while converting.

## Per-element formatting

- `**Zime Ignite**` / `**Sales → CS Handover Template**` → title block, left
  aligned (not centered — the live template has a vertical accent bar to the
  left of "Zime Ignite", not center-justified text). "Zime Ignite" is bold,
  large, dark navy (`#1F3864`). "Sales → CS Handover Template" directly
  below it, bold, medium blue (`#2E75B6`), smaller than the title.
- Every one-row `| field | value |` table → keep as a real table (not
  flattened to a bullet or paragraph) — this is a fillable form, tables are
  the point. Shade every field-label cell light blue-gray (`#DCE6F5`,
  `ShadingType.CLEAR` — never `SOLID`, see `document-skills:docx`'s own
  gotcha list, it renders black) so labels read as a form, not body text.
  Exception: shade the `Company Drive folder` label cell light green
  (`#D9EAD3`) instead — it's visually distinct in the live template, likely
  to flag it as the one field CS opens first.
- The `|  | Handover acceptance checklist |` row is a section banner, not a
  form field despite its table-row shape in `handover-template.md` — render
  it full-width, solid dark navy background (`#1F3864`), bold white text, no
  visible cell border. It must not blend into the field-label shading above
  or look like just another row (this is the #1 thing that breaks the
  visual match if skipped).
- Acceptance checklist → real Word checkboxes (or checkbox-style list) with
  strikethrough on checked items, matching the samples' `~~text~~` styling.
- Numbered section headers (`| 1 | Legal and commercial status |`) → Heading
  1, with the number kept in the heading text.
- Italic placeholder/instruction text (e.g. "*Complete this before handing
  over to CS...*") stays italic.
- Unknown markers (`TBC`, `TBD`, `TBA`, "requested, not yet received", etc.)
  render as plain text inline — never styled differently from filled
  content, since visually flagging them belongs to the Open gaps section,
  not scattered emphasis through the body.
- A filled link value (Company Drive folder, POC resources sheet, Sales
  Deck) renders as a pill/badge, not a bare URL: light gray rounded
  background, a small colored icon/marker before the link text, matching
  the live template's "chip" styling for these three fields specifically.
- Open gaps block renders as a distinct callout-style table, matching its
  position directly under the CS-accepts row in the samples.

These hex values are read off the live Google Doc template by eye, not
sourced from an official brand kit — close, not guaranteed pixel-exact.
Confirm against the real template next time someone reviews a render, and
correct this file if any are off.

## Filename

`<Client name> - Sales to CS Handover - <YYYY-MM-DD>.docx`, saved in the
current directory alongside the markdown source.
