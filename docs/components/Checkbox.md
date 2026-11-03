# Checkbox

Square tick box for yes/no fields and row selection in tables.

**Products:** Back office.

**Consumer provides:** `v-model` (boolean), a label to its right inside `.check-row`. Tables also use the indeterminate state for "some rows on this page".

Based on shadcn Checkbox: 16px, `radius-sm` corners, checked and indeterminate fill with `accent` and draw the mark in `on-accent`, focus ring, 50% when disabled, `destructive` border with `aria-invalid`. The label in `.check-row` is 14px, 500 weight, like Field's label.

PAL difference: the empty box uses `border-strong` instead of shadcn's input border, so it stays visible on white.

Use `Toggle` instead when the change takes effect at once, such as switching a record active.

Source: `PAL Backend/web/src/styles/backoffice.css` `.check`, `.check-row`.
