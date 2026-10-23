# BookingCard

The driver's main list item: everything about one job at a glance.

**Consumer provides:** a `booking` object (`ref`, `day`, `time`, `state`, `service`, optional `flight`, `pax`, `bags`, `childSeats`, `from`, `to`, `stops`, urgency fields) and `onAccept` for new jobs.

Scan order, top to bottom: time (biggest), urgency or status pill, service with flight badge, requirement chips, route, Accept, reference.

Border tells state once the trip moves: amber 2px heading to pickup, green 2px with the passenger, a red pulse when a waiting pickup is under 2 hours. "Rescheduled by Ops" shows as a full-width `warn` ribbon above the hero.

This is a static rendition of the shipped card. Expand/collapse, the Assign shortcut and the driver chip are not reproduced.

Source: driver `booking-card.tsx`.
