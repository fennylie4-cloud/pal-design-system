# Tab

Pill-style filter tab for one row of categories above a content panel, such as the city switcher.

**Products:** Website, Back office.

**Consumer provides:** `children` (one word or short noun), `active`, `onClick`. Wrap a row in an element with `role="tablist"` and `overflow-x: auto`.

50px with 20/28 labels on desktop, 46px with 16/24 under 768px (or force `size="md"`). Rest: `border-strong` outline, `text-muted` label. Hover and active share one look: `accent-fill-soft`, `accent` border and text.

One tab row per surface; never mix sizes in a row. Active label is `accent` at 2.5:1, so the border and fill must carry the state too.

Source: `font-rules.md` → `.pal-tab`.

## Back office

Underline tabs at the top of a card: the Operations status tabs, Drivers, Driver detail.

Based on shadcn Tabs, line variant. 44px high, 8px side padding, 8px apart, 14px at 500. Rest: `text-muted`; hover and active: `text-primary`, and the active tab has a 2px `accent` underline sitting on the row's `border` hairline. An optional count follows the label: Geist Mono 11px/600 on `bg-elevated` with a `border` hairline, `accent-fill` with `accent-text` when its tab is active. Operations pushes its two flag tabs (Abandoned, At risk) to the right with `.tabs-gap`; they carry a Badge (tone) instead of a count.

Keyboard as Reka UI Tabs: only the active tab is in the Tab order, Left and Right arrows (and Home, End) move to another tab and select it, and the focus ring is the gold `shadow-focus` around the label. The `v-tablist` directive adds this to a row of `role="tab"` buttons, so pages keep their own panels.

Source: `PAL Backend/web/src/styles/backoffice.css` `.tabs`, `.tab`; keyboard in `src/lib/tablist.ts`.
