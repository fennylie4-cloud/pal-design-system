# Input

Text field for quote and contact forms.

**Consumer provides:** `label`, `id`, `placeholder`, optional `icon` (left, 14px), `error` text, any native input props.

`bg-surface`, `border` hairline, `radius-md`, 12px × 8px padding. Focus changes only the border, to `accent`: no ring, no wash. Error: `destructive` border, a 12% red halo and a one-line message that says how to fix it.

Driver app inputs are shadcn `Input` at 14px (`app-body`) with `radius-control`.

Source: DESIGN.md `input-field`, `design-system.css` input notes.
