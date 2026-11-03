# DateRangeMenu

The global date range used to filter lists and analytics: All time, Today, Last 7 and 30 days, this or last month, quarter and financial year, month, quarter and year to date, or Custom.

**Products:** Back office.

**Consumer provides:** `v-model` with `{ name, start, end }`.

Based on shadcn's Date Range Picker (Popover plus Calendar in range mode), built on Reka UI `PopoverRoot` and `RangeCalendarRoot` for behaviour only. The trigger is an outline Button with a calendar icon, the current range and a chevron.

The popover opens 4px below the trigger, aligned to its left edge, in two columns split by a hairline. Left: the 13 presets as 32px rows, 14px, `radius-sm`; hover fills `accent-fill-soft`, the current one sits on `accent-fill` in `accent-text` at 500. Right, 16px padding: "Custom range" (14px/600), then the range calendar.

Calendar (shadcn Calendar, range mode): two months side by side, weeks from Monday. Month captions 14px/500, centred, with 32px outline arrow buttons at the outer corners. Weekday letters 12px `text-muted`. Days are 32px squares, 14px, `radius-control`: hover `bg-elevated`; today `bg-elevated` at 600; the start and end days `accent` with `on-accent` text; the days between them a continuous `accent-fill-soft` run in `accent-text`; days from the next or last month at half strength. While picking the end, the run previews under the pointer.

Under the calendar, after a hairline: Start date and End date as read-outs (12px `text-muted` label, 14px value, "Pick a date" until set) and the outline "Apply range" button, disabled until both dates are set.

Keyboard: focus starts on today; arrow keys move by day and week, Page Up and Page Down by month, Enter or Space picks the start and then the end. Picking a preset or applying closes the popover and returns focus to the trigger; Escape or a click outside closes it without changes.

The financial year starts on 1 April, as in WeWeb.

**DateRangeField.** The Custom start and end dates on Operations and Calendar use the same calendar on its own: an outline Button with a calendar icon and "03 Nov 2026 to 10 Nov 2026", opening a popover with the range calendar and the Start date and End date read-outs. There is no Apply button: as in WeWeb, the range applies as soon as the end date is picked, and the popover closes.

Source: `PAL Backend/web/src/components/list/DateRangeMenu.vue`, `DateRangeField.vue`, the shared calendar in `RangeCalendar.vue`, `lib/ranges.ts`. Calendar styles in `src/styles/backoffice.css` `.cal-*`.
