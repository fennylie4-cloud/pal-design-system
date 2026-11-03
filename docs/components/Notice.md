# Notice

A message: inline in a section (a flight PAL couldn't find, a seat-count warning, no pricing plan for a route, a feature that isn't available yet), or as a toast that confirms an action and goes away.

**Products:** Back office.

**Consumer provides:** `class="notice"`, optional `data-tone` (`ok`, `info`, `warn`, `danger`), an optional 16px icon first, an optional `.notice-title`, then one or two sentences.

Based on shadcn Alert: a grid with a 16px icon column and 12px gap, 12px by 16px padding, `radius-md`, 13px text in `text-primary`. Without a tone it is `bg-surface` with a `border` hairline and a `text-muted` icon. With a tone it takes the tone's `-bg` fill, a hairline in the tone's `-fg` at 25%, and the icon and title in the tone's `-fg`; the text stays `text-primary` so it reads easily. Without an icon the text takes the whole width.

Says what happened and what to do next.

**As a toast:** call `toast(message, tone)` with tone `ok` (default) or `danger`. The same Notice, 356px wide, floats at the top right, 24px from the edges, with `shadow-lifted` and the text at 500; a check icon for `ok`, an alert icon for `danger`. New toasts stack downward, 8px apart, slide in from 8px above and leave after 3.6 seconds. Success toasts are announced politely to screen readers, error toasts at once. One sentence, PAL as the subject where it fits, such as "Booking #15822 saved." or "PAL found no booking with reference #99999."

Use the inline Notice for problems on the page that need fixing; use the toast only for a confirmation that needs no action, or alongside a field error, never instead of one.

Source: `PAL Backend/web/src/styles/backoffice.css` `.notice`, `components/booking/NoRateNote.vue`, the toast in `components/ToastHost.vue` and `lib/toast.ts`.
