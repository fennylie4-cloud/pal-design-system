# RouteRow

Pickup → stops → drop-off, the way a driver scans a route.

**Products:** Driver app, Back office.

**Consumer provides:** `from`, `to` and optional `stops`, each `{title, sub}`.

A dashed `accent` line joins the dots. Pickup is a neutral dot, intermediate stops are hollow gold rings, drop-off is solid gold. Order carries the sequence; no numbers. Title 14px/500, sub 12px muted.

The source also offers a per-stop menu (copy address, open in maps); not reproduced here.

Source: driver `route-row.tsx`.

## Back office

The route editor on Booking detail and Create booking uses the same markers (dark pickup, gold drop-off, outlined stops on a dashed line) with a place search and instructions under each point.
