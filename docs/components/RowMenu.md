# RowMenu

The three-dot menu at the end of a table row: Edit, Duplicate, Activate or Deactivate, Delete.

**Products:** Back office.

**Consumer provides:** `label` (names the row, such as "Actions for PAL10"), `items` (`label`, `icon`, optional `danger`, `onSelect`).

Based on shadcn Dropdown Menu, the same menu as ActionMenu, opened from a 32px `icon-btn`. Clicking it never opens the row.

Danger items use shadcn's destructive item: `destructive` text and icon, a 10% `destructive` fill when highlighted. They come last, after a separator.

Source: `PAL Backend/web/src/components/list/RowMenu.vue`.
