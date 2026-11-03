# MultiSelect

Every dropdown in the back office: pick one value (single mode, which replaces the native select) or several (vehicles for a rate rule, members of a driver group, countries for a promotion), from the same trigger and popover list.

**Products:** Back office.

**Consumer provides:** `v-model` (array, or one value with `single`), `options` (`value`, `label`, optional `hint`), `placeholder`, optional `searchPlaceholder`, `disabled`, `single` and `searchable` (true by default).

Based on shadcn's multi-select combobox (Popover plus Command), built on Reka UI `PopoverRoot` and `ListboxRoot` for behaviour only.

Closed, it looks like Input: 36px minimum, `border` hairline, `radius-control`, 12px side padding, a 16px chevron at half strength. Chosen values sit inside as Badges, each with a 16px remove button named "Remove Kenny Chan". The control grows to fit them.

Open, the popover matches the control's width (at least 240px), 4px below it: `bg-surface`, `border`, `radius-md`, `shadow-lifted`. A 36px search row with a 16px search icon and a hairline under it, then the options, 240px tall at most. Each option is 14px with a 16px checkbox on the left (`accent` when ticked, `on-accent` tick) and an optional hint in 12px `text-muted` on the right. The highlighted option fills with `accent-fill-soft`. "Nothing matches." when the search finds nothing.

Keyboard: Enter, Space or Down opens it with focus in the search box. Typing filters, Up and Down move through the options, Enter ticks or unticks one. Escape closes it and returns focus to the control. Inside a Dialog, Escape closes only the popover.

**Select** (`Select`, the drop-in for a native `<select>`): write the same `<option>` and `<optgroup>` children with `v-model` (`.number` works), `@change`, `disabled`, `aria-invalid` and `aria-label`, and it renders MultiSelect in single mode. A disabled option without a real value ("Select a company") becomes the placeholder; other disabled options stay in the list at 50% and can't be picked; an `<optgroup>` label becomes a small `text-muted` header with a hairline above it. Lists longer than eight options get the search row. Error: `aria-invalid="true"` turns the border `destructive`, with a red ring when open or focused.

**Single mode** (`single`): picks one value, as shadcn Select does, in the same trigger and popover. The trigger shows the chosen label as plain text; the list marks it with a 16px `accent-text` check on the right (no checkboxes) and closes as soon as one is picked. Add `:searchable="false"` to drop the search row for short lists. Used for the service country in RegionBar, the field picker in the search group (see Input), and through `Select` for every other one-value dropdown.

Use Segmented instead when there are two to four options that should all stay visible.

Source: `PAL Backend/web/src/components/list/MultiSelect.vue` and the drop-in `Select.ts`.
