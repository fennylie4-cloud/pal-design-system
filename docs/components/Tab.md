# Tab

Pill-style filter tab for one row of categories above a content panel, such as the city switcher.

**Consumer provides:** `children` (one word or short noun), `active`, `onClick`. Wrap a row in an element with `role="tablist"` and `overflow-x: auto`.

50px with 20/28 labels on desktop, 46px with 16/24 under 768px (or force `size="md"`). Rest: `border-strong` outline, `text-muted` label. Hover and active share one look: `accent-fill-soft`, `accent` border and text.

One tab row per surface; never mix sizes in a row. Active label is `accent` at 2.5:1, so the border and fill must carry the state too.

Source: `font-rules.md` → `.pal-tab`.
