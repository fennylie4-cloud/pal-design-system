# Segmented

Two to four mutually exclusive options shown side by side, such as Today, Next 7 days, Next 30 days, Custom.

**Products:** Back office.

**Consumer provides:** A row of buttons inside `.segmented`, each with `aria-pressed`.

Matches shadcn's Tabs list look. `bg-elevated` track with a `border` hairline and `radius-control`, the same corners as Button, Input and MultiSelect, 3px inset. Buttons are 28px with `radius-sm` with `text-soft` labels; the pressed one sits on `bg-surface` with `shadow-app-card` and `text-primary`. Not for navigation between pages: use Tab. When several options can be on at once, use ToggleGroup.

Source: `PAL Backend/web/src/styles/backoffice.css` `.segmented`, used on Operations and Calendar.
