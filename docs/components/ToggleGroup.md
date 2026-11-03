# ToggleGroup

A set of options where several can be on at once and all of them fit on screen, such as the countries a vehicle type operates in.

**Products:** Back office.

**Consumer provides:** `ToggleGroupRoot` with `type="multiple"`, `v-model` (array) and an `aria-label`; one `ToggleGroupItem` per option with `class="toggle-item"`.

Based on shadcn Toggle Group, outline variant, built on Reka UI for behaviour only. Items are 32px, 12px side padding, `radius-control`, a `border` hairline on `bg-surface`, 14px at 500 in `text-soft`, 8px apart and wrapping. Hover: `bg-elevated` with `text-primary`. On: `accent` border, `accent-fill` with `accent-text`. Focus ring as Button. Tab enters the group, arrow keys move between items, Space or Enter turns one on or off.

Use MultiSelect when the list is long or needs search. Use Segmented when only one option can be on.

Source: `PAL Backend/web/src/styles/backoffice.css` `.toggle-group`, `.toggle-item`, used in the vehicle dialog.
