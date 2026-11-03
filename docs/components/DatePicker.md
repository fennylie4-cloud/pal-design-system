# DatePicker

One date, or a date and a time: pickup time on Create booking and Booking detail, and the time a status changed.

**Products:** Back office.

**Consumer provides:** `v-model` (`'YYYY-MM-DD'`, or `'YYYY-MM-DDTHH:mm'` with `time`), optional `time`, `placeholder` ("Pick a date") and `disabled`.

Based on shadcn's Date Picker (Popover plus Calendar), built on Reka UI `CalendarRoot` and `PopoverRoot` for keyboard and focus.

- Closed: looks like Input, with a 16px calendar icon in `text-muted` and the value as "03 Nov 2026, 08:15" (or the placeholder in `text-muted`). Open, it keeps Input's focus ring.
- Open: a popover 4px below with one month of the same calendar as DateRangeMenu: 32px day squares, today on `bg-elevated`, the picked day solid `accent` with `on-accent`, outline arrow buttons for the previous and next month. Focus starts on the picked day or today; arrow keys move by day and week, Enter picks.
- With `time`: a Time field under the calendar, after a hairline, in Geist Mono. Picking a day keeps the time; without `time`, picking a day closes the popover.

Use DateRangeMenu for a range.

Source: `PAL Backend/web/src/components/list/DatePicker.vue`, calendar styles in `src/styles/backoffice.css` `.cal-*`.
