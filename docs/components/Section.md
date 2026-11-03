# Section

Driver-app card wrapper with a header row, used to group details on the booking screen.

**Products:** Driver app, Back office.

**Consumer provides:** `title`, optional `extra` (right-aligned meta), `children`, `bodyPadding` (`none` for flush row lists).

`bg-app` with `border`, `radius-app-card`, `shadow-lifted`. Header: `app-gutter` × `app-card` padding with a hairline under it. Pair with `KV` for label/value rows.

Source: driver `section.tsx`. The collapsible header variant is not built here.

## Back office

Based on shadcn Card. `.card` and `.section-card` are `bg-surface` with a `border` hairline, `radius-app-card` corners and `shadow-app-card`, set off from the white back office page by the hairline. `.card` holds page panels such as the Driver detail header and the Reports setup. List boards (tabs, toolbar, table, pager) are not cards: they sit straight on the page. `.section-card` adds the header row used on Booking detail, Create booking, Driver detail and Analytics:

- `.section-head`: 52px minimum, 12px by 16px padding, a hairline under it, the title on the left and actions on the right.
- `.section-title`: 16px/600 in `text-primary` (shadcn CardTitle). An optional `.section-desc` under it is 13px `text-muted` (CardDescription).
- `.section-body`: 16px padding, 16px between children. Field grids inside use `.grid` with `--cols`.
- `.section-foot`: buttons on the right after a hairline (CardFooter).

PAL difference from shadcn: the header keeps a hairline under it, because back office cards hold forms and tables rather than one block of content.

Source: `PAL Backend/web/src/styles/backoffice.css` `.card`, `.section-card`.
