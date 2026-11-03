# Input

Text field for quote and contact forms.

**Products:** Website, Driver app, Back office.

**Consumer provides:** `label`, `id`, `placeholder`, optional `icon` (left, 14px), `error` text, any native input props.

`bg-surface`, `border` hairline, `radius-md`, 12px × 8px padding. Focus changes only the border, to `accent`: no ring, no wash. Error: `destructive` border, a 12% red halo and a one-line message that says how to fix it.

Driver app inputs are shadcn `Input` at 14px (`app-body`) with `radius-control`.

Source: DESIGN.md `input-field`, `design-system.css` input notes.

## Back office

Based on shadcn Input, rebuilt in plain CSS with PAL tokens (`.input` in `styles/backoffice.css`). This guide covers the box, its states and its variants (textarea, money, unit after, input groups); the label, hint and error text around it are Field.

- 36px high (40px with `input-lg` on sign-in), 12px side padding, 14px text, `border` hairline on `bg-surface`.
- **Focus:** `focus` border plus the 3px `shadow-focus` ring, as in shadcn. This differs from the marketing input above, which changes the border only.
- **Error:** set `aria-invalid="true"`: `destructive` border, and a 3px red ring at 20% when focused.
- **Disabled:** 50% opacity. **Read-only** (PAL addition): `bg-elevated` with `text-soft`, so values that can't be edited don't look editable.
- **Textarea** (shadcn Textarea), `.textarea`: multi-line text for pickup instructions, driver notes and follow-up emails. 64px minimum height, 8px by 12px padding, 14px text at 1.5 line height, the same focus ring, error and disabled states, and it resizes vertically only. `rows` 2 for instructions, 3 for notes; the placeholder says what goes in it.
- **Money** (shadcn Input Group with a text addon): for an amount in a known currency, such as rates, add-ons, payouts and discounts. Wrap the input in `.money` with a `.money-unit` first: the currency code (or `%` for a percentage) sits inside on the left, 12px from the edge, in Geist Mono 12px/500 `text-muted`. The number is right-aligned in Geist Mono with tabular figures. Use `type="number"` with `v-model.number`.
- **Unit after**: the same with the unit after the number ("mins", "%"), wrapped in `.input-suffix`, the unit 12px from the right edge.
- **Input group** (shadcn Input Group), `.input-group`: two controls in one box, with one `border` hairline, one focus ring around the whole group and a hairline between the parts. A red border when either part is invalid.
  - **Phone** (`.input-group.phone`): the calling code, a read-only input (64px, on `bg-elevated`) or a single MultiSelect (96px) in Geist Mono, then the number.
  - **Search group** (`SearchFilter`): a MultiSelect in single mode (170px) picking the field to search, then the search Input with a 16px search icon 12px in from the left (text from 36px), 410px in all. Searching starts as you type, Escape clears it, and the browser's own clear button is hidden. When a list searches one field only, use the plain search Input.
- **PAL differences:** `radius-control` corners and no `shadow-xs`.
