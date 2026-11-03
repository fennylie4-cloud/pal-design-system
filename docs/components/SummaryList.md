# SummaryList

Priced lines with their totals: the trip calculation on Create booking and Booking detail.

**Products:** Back office.

**Consumer provides:** `.summary-lines` holding `.summary-line` rows (a `.summary-main` with `.summary-label` and optional `.summary-sub`, then a `.summary-amount`), then `.summary-totals` holding `.summary-row` rows and one `.summary-row.grand`.

- Lines: label 14px/500 in `text-primary`, the detail under it 12px `text-muted` ("1 × HKD 1,300.00"), the amount on the right in Geist Mono 12px/500 with tabular figures. Dashed `border` hairlines between lines, 8px above and below each.
- A line can hold a NumberField (`sm`) under its label to change a quantity.
- Totals: on `bg-elevated` after a `border` hairline, rows 14px in `text-soft` with the amount on the right. The grand total sits after another hairline at 15px/600 in `text-primary`. An amount still to pay can use `.summary-amount.due` in `destructive`.

Source: `PAL Backend/web/src/styles/backoffice.css` `.summary-*`.
