# FlightBadge

Flight code chip next to a booking's time.

**Consumer provides:** `code`, `incoming` (landing icon for airport pickups, takeoff for drop-offs), optional `status` `{label, delayMin}`.

No status: `accent-fill` with `accent-text`. With status it recolours to `ok` (on time) or `warn` (delayed, with a warning icon), so one component covers scheduled and live. Square-ish `radius-control`, mono 11px bold.

Source: driver `badges.tsx` `FlightBadge`. FlightStrip (the card-scale version) is not built here.
