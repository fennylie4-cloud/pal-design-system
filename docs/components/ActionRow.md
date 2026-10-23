# ActionRow

Tappable row with an icon tile, for trip actions and profile settings.

**Consumer provides:** `icon`, `title`, optional `sub`, `onClick`, `destructive`, `standalone`.

Flat by default for stacks inside a `Section` with `bodyPadding="none"`. `standalone` gives it its own border, `radius-app-card` and `shadow-app-card`. Icon tile is 36px (`icon-tile`) in `accent-fill` with `accent-text`; destructive rows switch to red.

Source: driver `action-row.tsx`.
