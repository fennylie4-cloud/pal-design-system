# Badge

A short label: a flag such as "Most Popular", a name or code, a trip's state, or any other state or signal.

**Products:** Website, Driver app, Back office.

**Consumer provides:** `children` (one or two words) and `variant`. For `status`, the trip `state` instead of children, and optional `live`. For `tone`, a `tone` (`ok`, `warn`, `danger`, `info`, `husk`; omit for neutral) and an optional `icon`.

**Variants**
- `solid` (website): `accent` fill, `cod-900` text, `radius-full`, 12px/600. "Most Popular" on fleet cards.
- `soft` (website): `accent-fill` with `accent-text`.
- `outline` (back office): a name or a code that isn't a state.
- `status` (driver app, back office): a trip's lifecycle state, with a dot.
- `tone` (driver app, back office): any other state or signal, coloured by tone: flight status, urgency, dispatch and payment, requirement chips.

Source: DESIGN.md `badge-pill`, driver `status-pill.tsx`, `badges.tsx` `TonedPill` and `index.css [data-pill]`, `[data-tone]`.

## Status variant

Trip lifecycle chip on booking cards, the booking detail screen and booking tables. States: `new`, `accepted`, `ontheway`, `onlocation`, `pob`, `complete`, `cancelled`, `noshow`, with an optional `label`.

Each state has a `pill-<state>-bg` / `pill-<state>-fg` pair. The dot blinks only while the driver is working the trip (heading to pickup, at pickup, on trip), so at most one badge blinks at a time. Driver app labels are fixed: New, Accepted, Heading to pickup, At pickup, On trip, Completed, Cancelled, No show.

All eight text colours pass 4.5:1 on white. Green and red states are also told apart by their label, never colour alone.

## Tone variant

Small state chip for flight status, urgency and trip requirements, the same shape and type as the status variant (22px, full pill, Geist Mono 10px upper case in the back office, 11px in the driver app) without the dot. Urgency rule from the booking card: pickup under 2 hours is `danger`, under 24 hours is `warn`, later is neutral. `husk` is for requirement chips (×2 passengers, ×3 bags). Without a tone it is neutral: `bg-elevated` with a `border` hairline and `text-soft`, so it stays visible on white.

A status or tone badge is a signal. Names and codes that aren't a state use the outline variant, so they never look like a status.

## Back office

`Badge.vue` with `variant="outline"` (the default), `variant="status"` or `variant="tone"`. Based on shadcn Badge: 22px, 8px padding, a 1px border and a 12px icon slot.

**Outline:** for names and codes that aren't a state: vehicle codes, zone names, transfer types, acquisition sources, providers, country codes and booking refs. `radius-control` corners, a `border` hairline on `bg-surface`, 12px Geist at 500 weight in `text-primary`, shown as typed rather than upper case. Add `mono` for codes (`E-CLASS`, `#15822`, `SG`), which sets Geist Mono at 10px. Group several in `.badge-list`, which wraps with a 4px gap.

**Status:** pass `status` with the WeWeb booking status; it maps onto the states above and keeps WeWeb's labels: Unscheduled (`new`), Assigned (`accepted`), En route (`ontheway`), Driver on location (`onlocation`), Passenger on board (`pob`), Completed (`complete`), Canceled and Late cancel (`cancelled`), No show (`noshow`). It keeps the full pill shape and Geist Mono labels at 10px (the one size below the back office 12px floor, user's decision 2026-11-04), 600 weight, upper case, with a 6px dot before the label.

**Blinking:** pass `live` only where one trip is shown on its own, which is the Booking detail header. Tables, the calendar and the status card keep the dot still, so at most one dot blinks on screen.

**Tone:** pass `tone`. Used for dispatch and payment status, active or inactive, promotion state (Live, Scheduled, Expired), event phase (On now, Upcoming, Ended), flight status and requirement chips (`husk`: 2 pax, 1 child seat).

Source: `PAL Backend/web/src/components/Badge.vue`, styles in `src/styles/backoffice.css` `.badge`, `.badge-list`, `.pill[data-pill]`, `.pill[data-tone]`.
