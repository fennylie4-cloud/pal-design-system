# Dialog

Modal window for creating or editing one record: customer, driver, zone, promotion, privilege discount.

**Products:** Back office.

**Consumer provides:** `title`, optional `description` (one line on what the dialog does), optional `width` in px (512 by default), body in the default slot, buttons in `#footer`.

Based on shadcn Dialog, built on Reka UI `DialogRoot` for behaviour only. Reka traps focus inside the dialog, puts it on the first field, gives it back to the button that opened the dialog, locks page scroll, and closes on Escape, the close button or a click on the dimmed page.

Look: the page dims to `cod-950` at 50%. The panel is `bg-surface` with a `border` hairline, `radius-card` corners and `shadow-lifted`, and it fades and scales in from 95% on `duration-base`. 24px padding. Title 18px/600 in `text-primary`, description 14px in `text-muted`, 8px apart. The close button is a 32px `icon-btn` 16px from the top right corner.

Footer: buttons on the right, 8px apart. Close (outline) sits to the left of the one primary action, which names what happens ("Create promotion", "Save changes").

PAL differences from shadcn:
- The body scrolls when it is taller than the window, so the footer keeps a `border` hairline above it and stays in view.
- `width` sets the panel width for wide forms (640 to 920px), capped at the window width less 32px.

Source: `PAL Backend/web/src/components/BaseModal.vue`, styles in `src/styles/backoffice.css` `.dialog`.
