# Source conflicts

The PAL sources disagreed on these values. Rule applied: what the live code renders wins, unless noted. Each row keeps the losing values so they can be overruled.

| Topic | Chosen | Also found | Where |
| --- | --- | --- | --- |
| Font family | Barlow for the marketing site, Geist for all apps (decision, 23 Oct 2026) | Barlow everywhere (DESIGN.md single-font rule); system font in native app | DESIGN.md, `v2-native/constants/theme.ts` |
| Mono font | Geist Mono | JetBrains Mono | driver web vs `design-system.css` |
| Primary hover | #cfc08a + 1px lift + `shadow-gold` (homepage and DESIGN.md agree) | husk-300 #c3b481; husk-500 #a28950 | `index.html` vs `design-system.css` vs `buttons.css` |
| Primary label weight | 500 (shared `.pal-btn` component and DESIGN.md agree) | 600 at 0.95rem | `buttons.css` vs legacy `index.html .btn-primary` |
| Section heading weight | 600 | 700 | `index.html` vs `design-system.css` |
| Eyebrow | 16/24, 500, 0.15em, gold | 14/20 gold; 14/20 cod-400 at 0.015em; 0.68rem/700 | `index.html` vs DESIGN.md vs `font-rules.md` vs `design-system.css` |
| Marketing card radius | 10px | 8px; 12px | `font-rules.md` vs `design-system.css` |
| Radius scale names | role names (`radius-card`, `radius-cta`) | lg = 10 / xl = 12; lg = 12 / xl = 16 | DESIGN.md vs `design-system.css` |
| Driver base radius | 0.5rem (control 6, card 8, sheet 14) | 0.75rem | `web/src/index.css` vs DESIGN.md table |
| Red | #b91c1c | #ef4444, #f73845, #d42844, #dc2626 | driver vs DESIGN.md / `buttons.css` / booking pulse |
| Outline hover colour | husk-600 #8b7043 | husk-500 #a28950 | DESIGN.md vs `buttons.css` |
| Status colours | driver web `data-pill` / `data-tone` | native `Palette.status`; old dark-site badges | `web/src/index.css` vs `v2-native` |
| Driver text-body | cod-900 (foreground) | cod-600 | web vs native `theme.ts` |
| Mid section band | dropped (#f6f6f6 is 1 step from #f5f5f5) | `bg-mid` #f6f6f6 | DESIGN.md |
| Footer ground | not tokenised | #000000 (nav is #0a0a0a) | `footer.js` |
| Dark theme | removed (decision) | full dark theme; driver `.dark` | `design-system.css`, driver web |

## Contrast failures kept from the source

| Pair | Ratio | Advice |
| --- | --- | --- |
| `accent` text on white / `bg-app` | 2.5 / 2.3 | Use `accent-text` for words that must be read (eyebrows, active tab labels, booking refs) |
| `text-muted` (marketing, cod-400) on white / `bg-app` | 2.5 / 2.3 | Move marketing meta text to cod-500 (4.8:1) |
| `focus` ring on white | 2.5 | Needs 3:1: use husk-600 for the ring, or add a dark inner ring |

## Housekeeping found

- `logo.svg` is a PNG inside an SVG wrapper; there is no vector master.
- The driver web app still ships Vite's default purple `favicon.svg` and `icons.svg`.
- `index.html` carries many `html.light-mode … !important` overrides from the old dark site. `design-system.css` still documents that dark site (noise overlay, orbs) as its default.
