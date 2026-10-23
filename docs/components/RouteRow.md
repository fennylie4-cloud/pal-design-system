# RouteRow

Pickup → stops → drop-off, the way a driver scans a route.

**Consumer provides:** `from`, `to` and optional `stops`, each `{title, sub}`.

A dashed `accent` line joins the dots. Pickup is a neutral dot, intermediate stops are hollow gold rings, drop-off is solid gold. Order carries the sequence; no numbers. Title 14px/500, sub 12px muted.

The source also offers a per-stop menu (copy address, open in maps); not reproduced here.

Source: driver `route-row.tsx`.
