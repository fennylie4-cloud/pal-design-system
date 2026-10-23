# TonedPill

Small status chip for flight status, urgency and trip requirements.

**Consumer provides:** `tone` (`ok`, `warn`, `danger`, `info`, `husk`; omit for neutral), optional `icon`, `children`.

Urgency rule from the booking card: pickup under 2 hours is `danger`, under 24 hours is `warn`, later is neutral. `husk` is for requirement chips (×2 passengers, ×3 bags).

Source: driver `badges.tsx` `TonedPill`, `index.css [data-tone]`.
