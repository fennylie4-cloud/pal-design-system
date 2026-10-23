# StatusPill

Trip lifecycle chip on booking cards and the booking detail screen.

**Consumer provides:** `state` (`new`, `accepted`, `ontheway`, `onlocation`, `pob`, `complete`, `cancelled`, `noshow`), optional `label`.

Each state has a `pill-<state>-bg` / `pill-<state>-fg` pair. The dot blinks only while the driver is working the trip (heading to pickup, at pickup, on trip), so at most one pill blinks at a time. Labels are fixed: New, Accepted, Heading to pickup, At pickup, On trip, Completed, Cancelled, No show.

All eight text colours pass 4.5:1 on white. Green and red states are also told apart by their label, never colour alone.

Source: driver `status-pill.tsx`, `index.css [data-pill]`.
