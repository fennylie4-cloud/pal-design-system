# Card

The white panel that holds one idea (an audience, a service, a city, a vehicle) on the grey marketing canvas.

**Consumer provides:** `title`, body `children`, optional `icon` (28px Lucide, gold), optional `action` (hover-revealed link text) and `href` to make the whole card a link.

- `bg-surface` on `bg-app`, `border` hairline, `radius-card` (10px), `card-padding` (28px), 12px gap between every slot.
- Hover is the same everywhere: border to `accent-border-hover`, `shadow-card-hover`, 3px lift, all on `ease-slow`. Never invent a per-page hover.
- With `action`, the link fades in on hover or focus but always reserves its space, so a row of cards keeps one height.
- On marketing pages the icon animates on card hover (lift, bounce or tilt keyframes in `font-rules.md`); not reproduced here.

Source: `font-rules.md` → `.pal-card`.
