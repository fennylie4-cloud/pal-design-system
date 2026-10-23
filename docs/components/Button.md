# Button

The one action control across PAL; the gold `primary` variant marks what to do next and appears at most once per visible surface.

**Consumer provides:** `children` (a verb-first label), `variant`, `size`, optional `icon`, `href` (renders a link), `block` for full width.

**Variants**
- `primary` — `accent` fill, `on-accent` text. Hover: `accent-hover`, 1px lift, `shadow-gold`. One per surface.
- `outline` — `border` hairline, `text-soft` label; hover tints to `accent-strong` over `accent-fill-soft`. Secondary actions.
- `ghost` — no chrome; hover `accent-fill`. A third action without extra weight.
- `secondary` — `cod-900` fill, `text-inverse`. Dark solid action on light grounds.
- `link` — text only, underlines on hover.
- `destructive` — `destructive` fill. Cancel booking, delete.

**Sizes:** `sm` 36px, `md` 46px, `lg` 50px for the marketing site (min-width 150px, `radius-md`). `app` is 40px with `radius-control`: use it for every driver-app button (Accept, Assign).

**Do:** "Request a Quote", "Accept", "Call passenger". **Don't:** two gold buttons side by side; white text on gold; "Click here".

Source: `buttons.css`, `index.html .btn-primary`, driver `components/ui/button.tsx` (shadcn, `size="lg"`). Hand-written from those paths.
