# RouteRow

Pickup → stops → drop-off, the way a driver scans a route.

**Products:** Driver app, Back office.

**Consumer provides:** `from`, `to` and optional `stops`, each `{title, sub}`.

A dashed `accent` line joins the dots. Pickup is a neutral dot, intermediate stops are hollow gold rings, drop-off is solid gold. Order carries the sequence; no numbers. Title 14px/500, sub 12px muted.

The source also offers a per-stop menu (copy address, open in maps); not reproduced here.

Source: driver `route-row.tsx`.

## Back office

One shared marker, `.marker`, 10px, in the route editor on Booking detail and Create booking, the Trip column on Operations and the trip calculation's itinerary: `from` dark (`cod-900`), `mid` hollow with a 2px `accent` ring for a stop, `to` solid `accent`, and `ghost` dashed `border-strong` for "add a stop". A 1px dashed `border-strong` line joins them. The route editor puts a place search and instructions under each point.

Source: `PAL Backend/web/src/styles/backoffice.css` `.marker`.
