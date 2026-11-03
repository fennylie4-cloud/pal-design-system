# NumberField

A whole number with − and + buttons: passengers, child and booster seats, hourly duration, add-on quantities.

**Products:** Back office.

**Consumer provides:** `v-model` (number), `label` (names the value for screen readers and the buttons: "One less Child seat"), optional `min` (0), `max`, `step` (1), `size` (`md` 36px, or `sm` 32px inside a list row) and `disabled`.

Based on shadcn-vue's NumberField, built on Reka UI `NumberFieldRoot` for behaviour: arrow keys step, Page Up and Page Down step by ten, Home and End jump to `min` and `max`, and the value never leaves its range.

One box with Input's `border` hairline, `radius-control` corners and gold focus ring around the whole group: a 34px ghost − button, the value centred in Geist Mono 14px with tabular figures, and a 34px ghost + button. The buttons are `text-muted`, `text-primary` on `bg-elevated` when hovered, and fade to 40% at the end of the range. `sm` makes it 32px with 30px buttons and a 14px value, for the quantity in the trip calculation.

Source: `PAL Backend/web/src/components/list/NumberField.vue`, styles in `src/styles/backoffice.css` `.number-field`.
