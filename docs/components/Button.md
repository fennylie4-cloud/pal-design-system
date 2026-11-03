# Button

The one action control across PAL; the gold `primary` variant marks what to do next and appears at most once per visible surface.

**Products:** Website, Driver app, Back office.

**Consumer provides:** `children` (a verb-first label), `variant`, `size`, optional `icon`, `href` (renders a link), `block` for full width.

**Variants**
- `primary`: `accent` fill, `on-accent` text. Hover: `accent-hover`, 1px lift, `shadow-gold`. One per surface.
- `outline`: `border` hairline, `text-soft` label; hover tints to `accent-strong` over `accent-fill-soft`. Secondary actions.
- `ghost`: no chrome; hover `accent-fill`. A third action without extra weight.
- `secondary`: `cod-900` fill, `text-inverse`. Dark solid action on light grounds.
- `link`: text only, underlines on hover.
- `destructive`: `destructive` fill. Cancel booking, delete.

**Sizes:** `sm` 36px, `md` 46px, `lg` 50px for the marketing site (min-width 150px, `radius-md`). `app` is 40px with `radius-control`: use it for every driver-app button (Accept, Assign).

**Do:** "Request a Quote", "Accept", "Call passenger". **Don't:** two gold buttons side by side; white text on gold; "Click here".

Source: `buttons.css`, `index.html .btn-primary`, driver `components/ui/button.tsx` (shadcn, `size="lg"`). Hand-written from those paths.

## Back office

Based on shadcn Button, rebuilt in plain CSS with PAL tokens (`styles/backoffice.css`).

- **Sizes:** default 36px (`.btn`), `btn-sm` 32px, `btn-lg` 40px for sign-in, and `icon-btn` 32px square (shadcn `icon-sm`). 14px label, 500 weight, 16px icons; padding drops from 16px to 12px when the button has an icon.
- **Variants:** `btn-primary` (shadcn default), `btn-outline`, `btn-ghost`, `btn-destructive`, and `link-btn` (shadcn link) for inline actions such as Add stop. Outline and ghost hover to `accent-fill` with `accent-text`.
- **States:** focus is a 3px `shadow-focus` ring; disabled is 50% opacity and not clickable, as in shadcn.
- **PAL differences:** corners use `radius-control` (6px) instead of shadcn's 8px; no `shadow-xs`, because back office surfaces are flat; pressed primary goes to `accent-strong`. `btn-danger-outline` is a PAL addition: a red label on an outline button, for bulk delete and cancel in toolbars. shadcn's `secondary` isn't used.
