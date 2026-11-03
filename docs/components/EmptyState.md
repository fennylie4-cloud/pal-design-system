# EmptyState

Dashed panel for "nothing here yet" on bookings tabs, notifications and history.

**Products:** Driver app, Back office.

**Consumer provides:** `title`, optional `description`, `icon`, `action`.

Dashed `border`, `bg-surface`, `app-hero` padding, centred 32px muted icon. Title says what is empty; description says what will appear. "No new bookings" / "New jobs from Ops show up here."

Source: driver `empty-state.tsx`.

## Back office

Based on shadcn Empty. A 40px icon tile (`bg-elevated`, `radius-md`, 24px icon in `text-primary`), then the title in 16px/500 `text-primary` and one line in 14px `text-muted`, at most 384px wide, all centred with 48px above and below. An optional action goes under it.

Inside a table or card it has no border: DataTable, the Operations table, the Calendar agenda. Add `bordered` for the dashed panel when it stands alone, such as the payouts list on Driver detail.

Copy: the title says what is empty ("No bookings match these filters"), the line says what to change ("Change the date range, country or search to see more."). The icon defaults to a crossed-out search; pass one that fits, such as a calendar for the agenda.

Source: `PAL Backend/web/src/components/EmptyState.vue`.
