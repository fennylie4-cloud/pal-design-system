# DataTable

The table every back office list is built from: bookings, customers, companies, drivers, vehicles, privilege discounts, settings and reports.

**Products:** Back office.

Based on shadcn Table and its data table guide (ui.shadcn.com/docs/components/base/data-table), rebuilt in plain CSS with PAL tokens. It comes in two layers, both documented here:

- **The parts** (`components/table/`), for tables with their own cells such as the Operations bookings table: `Table` (optional `minWidth` in px, an `#empty` slot) holding native `<thead>` and `<tbody>` with `TableRow` (`selected` tints it gold; `clickable` opens its record on click or Enter and emits `open`), `TableHead` (label in the slot; optional `align="right"`, `width`, `kind` `check` or `actions`, and `sort` `none`, `ascending` or `descending` with `sortLabel`, emitting `sort`) and `TableCell` (optional `align="right"` and `kind`; checkbox and actions cells don't open the row).
- **`DataTable`**, the ready-made list built from those parts for the simple lists. **Consumer provides:** `columns` (`key`, `label`, optional `size`, `wrap`, `sort`, `align`), `rows` (each with an `id`), `label` (names the rows for screen readers), optional `selectable` with `v-model:selected`, `emptyTitle`, `emptyText`, `emptyIcon`. Cells are customised with `#cell-<key>` slots; row actions go in `#actions`. It adds sorting, selection, the empty state and the pager.

**Anatomy**
- Box: the table stands alone, as in shadcn's data table: its own `border` hairline, `radius-control` corners (the same 6px as inputs, buttons and the segmented control) and `bg-surface`, straight on the white page and lined up with the page title. Tabs, toolbar and the bulk bar sit above it; TablePager sits below it, outside the box. It scrolls sideways inside the box when the table is wider; it never scrolls up and down on its own: the page does.
- Type: 14px with 20px line height, as shadcn's `text-sm`.
- Header: 40px, `bg-surface` with a `border` hairline under it. Labels 500 in `text-primary`, left-aligned, never wrapping.
- Rows: sized by their content with 8px cell padding on every side (about 37px for one line), `text-body`, cells centred vertically, a `border` hairline between rows and none under the last one.
- The first and last columns get 12px padding against the box edge.
- Checkbox column 32px plus its inset; actions column 48px, right-aligned, holding a RowMenu.

**States**
- Hover: `bg-elevated`.
- Selected: `accent-fill-soft`.
- Focus (clickable rows): a 2px `focus` outline inside the row.
- Sortable header: a 32px ghost button, `radius-control`, `bg-elevated` on hover, the gold focus ring, with a 16px up-down arrow in `text-muted`. The sorted column shows an up or down arrow in `accent-text` and sets `aria-sort` on its header cell.
- Empty: EmptyState in the `#empty` slot, under the header.

PAL differences from shadcn: the gold selected row (shadcn uses grey), and no filter box, column menu or "rows selected" line unless the page already has them in WeWeb.

**Cell content**
- One value: plain text. The name a row is about: `text-primary` at 500.
- Two lines: the value, then a 12px `text-muted` caption, stacked with 4px between.
- Refs, codes and times: Geist Mono. Refs in `accent-text`.
- States: Badge `variant="status"` for trips, `variant="tone"` for the rest. Names and codes: Badge (outline).
- Money and counts: right-aligned with tabular figures, header right-aligned too.
- Nothing to show: `text-muted` ("None", "Unassigned", "Individual").

**Column sizes** (DataTable, and the Operations table through `components/table/sizes.ts`): each column takes a `size` by what it holds, a step above its longest value and header so long text has room, and the table uses fixed column layout, so columns line up the same way on every page instead of each one following its longest value.

| Size | Width | For |
|---|---|---|
| `xs` | 80px | short codes, counts, toggles (Seats, Charger, Tax) |
| `sm` | 112px | refs, dates, country, money, status badges (Created, Country, Status) |
| `md` | 144px | badges with longer words, phone numbers, headers up to about 14 characters (Source, Type, Lowest rate) |
| `lg` | 200px | a name with a second line, or a long header (Company, Owner, Uses per customer) |
| `fill` | the rest, 200px at least | free text and lists: email, description, regions, pricing plan, vehicles |
| checkbox / actions | 40px / 56px | added by DataTable |

A fixed column must fit its header with the sort arrow (about 32px more than the text) and its usual value; when it doesn't, move it up a size. A fill column ends long values in an ellipsis. Add `wrap` to a column that holds a sentence or a list of dates or rates, so it wraps onto more lines instead. The table's minimum width is the sum of its fixed columns plus 200px per fill column; past that, the box scrolls sideways.

**Pager** (`TablePager`, under the box): "11–20 of 45" in `text-muted` on the left; on the right "Rows per page" with a 32px dropdown (10, 30 or 50), the page number ("2 / 5", Geist Mono) and two 32px outline icon buttons.

Pair with a toolbar (`.board-toolbar`) above the box and the pager below it, grouped in a `.board`. A board is not a Card: it has no fill, border or shadow.

Source: `PAL Backend/web/src/components/table/` (`Table.vue`, `TableRow.vue`, `TableHead.vue`, `TableCell.vue`), `components/list/DataTable.vue` and `TablePager.vue`, styles in `src/styles/backoffice.css` `.table-wrap`, `.table`.
