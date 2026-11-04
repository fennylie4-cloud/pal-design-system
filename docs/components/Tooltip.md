# Tooltip

Names an icon-only button on hover and keyboard focus, such as Duplicate and Remove on the pricing plan rates in Settings.

**Products:** Back office.

**Consumer provides:** `label` (the button's name, the same as its `aria-label`), optional `side` (`top` by default), and the button in the default slot.

Based on shadcn Tooltip, built on Reka UI `TooltipRoot` for behaviour only. It opens after 200ms, 6px from the button. Look: `cod-900` fill, `text-inverse` text at 12px/500, 6px by 12px padding, `radius-control` corners, the shared `.tooltip` style that the sidebar also uses.

Every icon-only button inside a form or card gets one. Use it instead of the native `title` attribute. Danger icon buttons (Remove) are ghost icon buttons in `destructive`, with a `tone-danger-bg` fill on hover.

Source: `PAL Backend/web/src/components/list/IconTip.vue`. Style: `src/styles/backoffice.css` `.tooltip`.
