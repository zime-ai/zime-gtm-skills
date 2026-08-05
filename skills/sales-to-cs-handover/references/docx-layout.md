# Docx Layout

Layout intent for the final skill step, handed to the `document-skills:docx`
skill alongside the assembled markdown. Holds intent only — no docx-js
mechanics here.

## Source of truth

The generated markdown (matching `handover-template.md` exactly, filled)
*is* the content. The docx render is a direct conversion, not a
re-derivation — don't re-summarize or reorder anything while converting.

## Per-element formatting

- `**Zime Ignite**` / `**Sales → CS Handover Template**` → title block,
  centered, bold.
- Every one-row `| field | value |` table → keep as a real table (not
  flattened to a bullet or paragraph) — this is a fillable form, tables are
  the point.
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
- Open gaps block renders as a distinct callout-style table, matching its
  position directly under the CS-accepts row in the samples.

## Filename

`<Client name> - Sales to CS Handover - <YYYY-MM-DD>.docx`, saved in the
current directory alongside the markdown source.
