# FlightPanel

Live flight details under the flight number on Booking detail and Create booking.

**Products:** Back office.

**Consumer provides:** `flight` (airline, number, status, departure and arrival with scheduled and revised times and terminals), `timeZone`.

Based on shadcn Card: `bg-surface`, a `border` hairline, `radius-md`, `shadow-app-card`. A header row with the flight number (Geist Mono 14px/600), the airline in 14px `text-muted` and the status tone Badge on the right, a hairline under it, then departure and arrival side by side split by a hairline. Each leg: a 16px plane icon in `text-muted`, the leg name 14px/500 and the airport code in a small outlined mono chip, then Scheduled, Revised and Terminal as 14px label and value pairs with tabular figures. Times are shown in the pickup's timezone; the status is a Badge (tone) (On time and Landed `ok`, Delayed `warn`, Cancelled `danger`) and a revised time that differs from the schedule turns `tone-warn-fg`. The driver app shows the same signal as FlightBadge.

Source: `PAL Backend/web/src/components/booking/FlightPanel.vue`.
