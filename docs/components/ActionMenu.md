# ActionMenu

A labelled outline button that opens a short menu of secondary actions, such as More on Booking detail.

**Products:** Back office.

**Consumer provides:** `label`, `items` (`label`, `icon`, optional `disabled`, `onSelect`).

Based on shadcn Dropdown Menu, built on Reka UI `DropdownMenuRoot` for behaviour only. Arrow keys move between items, typing a letter jumps to an item, Enter or Space selects it, and Escape closes the menu and returns focus to the button. When an item opens a dialog, closing the dialog returns focus to the button too.

Look: `bg-surface`, `border` hairline, `radius-md` corners, `shadow-lifted`, 4px padding, 4px below the button and aligned to its right edge. Items are 14px in `text-primary` with a 16px icon in `text-muted`, 6px by 8px padding and `radius-sm` corners. The highlighted item fills with `accent-fill-soft`. Disabled items stay visible at 50% opacity so people learn they exist.

Use RowMenu for per-row actions in tables.

Source: `PAL Backend/web/src/components/ActionMenu.vue`, styles in `src/styles/backoffice.css` `.menu-content`, `.menu-item`.
