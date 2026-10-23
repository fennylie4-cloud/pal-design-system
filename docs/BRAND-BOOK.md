# PAL Design System — Brand book

PAL (Prime Aces Limousine) is a corporate chauffeur company in Singapore, Kuala Lumpur, Bangkok and Hong Kong. Its clients are executives, hotels and travel managers, for whom a failed transfer is a professional failure. Every surface should look thought through: calm, controlled, credibly premium, never loud. The house style is **Editorial Precision**.

One system serves several products. Each product is a theme in the Claude design system and a `data-app` scope in code:

| Product | Theme id | In code | Status |
| --- | --- | --- | --- |
| Marketing site | `marketing` | `data-app="marketing"` (default, may be omitted) | Live, static HTML |
| Driver app | `driver` | `data-app="driver"` | Web (Vite, React, shadcn/ui) and native (Expo) |
| Customer portal, back office | — | `data-app="portal"`, `"backoffice"` | Future |

Both themes are light. There is no dark theme.

## Content fundamentals

- PAL is the subject in website and product copy: "PAL tracks your flight", not "we track". LinkedIn company posts may use "we".
- Plain, declarative sentences. No slogans, no lifestyle or luxury language, no exclamation marks, no emoji.
- No em dashes in PAL company copy.
- Sentence case for headings and buttons; uppercase only in eyebrows.
- Buttons start with a verb: "Request a Quote", "Accept", "Call passenger", "Log waiting time".
- Never invent client scenarios or numbers. The feeling to leave is "I didn't have to worry about it."
- Driver app copy is operational and short: "Heading to pickup", "Rescheduled by Ops", "No new bookings".

## Colour

- The palette is neutral **Cod** greys plus one warm accent, **Husk gold** (`husk-400` #b6a269). Blue, red and green never act as brand colours; they appear only as status.
- Gold means "this is what you do next". Use `accent` for the primary button, active tab, eyebrow, slider thumb, focus ring and icons. Never as decoration.
- Gold text fails contrast on light grounds (2.5:1 on white). When gold words must be read, set them in `accent-text` (husk-700, 6.8:1).
- Text on any gold fill is `on-accent` (cod-950, 7.9:1). Never white on gold.
- Marketing: `bg-app` grey canvas, white `bg-surface` cards, `bg-elevated` for alternating section bands. The nav bar is `chrome` (cod-950) and carries the white wordmark.
- Driver: whiter shell (`bg-app` white, cards `bg-surface` #fafafa, softer `border` #ececec).
- Headings `text-primary`; marketing body `text-body`; meta `text-muted`. Marketing `text-muted` (cod-400) fails contrast on light grounds: keep it to labels that are not essential.
- Trip states use the `pill-*` pairs; flight and urgency signals use the `tone-*` pairs. Always pair the colour with a word.

## Type

- **Typeface by product.** The marketing site uses **Barlow** (`font-sans`). Every app (driver web, driver native, and future portal and back office) uses **Geist** (`font-app`). Never mix the two on one screen.
- Barlow by weight: 600 for headlines and section headings, 500 for card titles, buttons, labels and eyebrows, 400 for body.
- Geist by weight: 700 for app display and headline, 600 for titles, 500 for labels and buttons, 400 for body.
- **Geist Mono** for booking refs, flight codes and pill labels only, in every product.
- Marketing scale: `hero-headline` once per page, `section-heading` 48/48 (30/36 under 768px), `card-title` 20/28, `body` 16/24, `eyebrow` 16/24 uppercase at 0.15em.
- Driver scale: denser, 14px `app-body` base, `app-title` 18, `app-headline` 24, `app-display` 36. Inputs are clamped to 14px.
- No italics except deliberate editorial callouts.

## Space and layout

- Every measure is a step of the 4/8 scale (`sp-*`).
- Marketing sections: `section-y` 120px top and bottom, `section-x` 48px sides (80 and 24 under 768px), content capped at `container-max` 1280px on a 12-column grid. Group related items tightly (8–16px); separate sections generously.
- Section backgrounds alternate `bg-app` and `bg-elevated` instead of horizontal rules.
- On mobile, multi-column marketing grids become horizontal carousels with a Slider under them.
- Driver: `app-page` 16px sides, `app-card` 16px card padding, `app-gutter` 12px between siblings, `tap` 44px minimum targets, shell capped at `container-app` 520px.

## Shape, depth and motion

- Corners are soft, never square, never playful. Marketing: `radius-md` 8px controls, `radius-card` 10px cards, `radius-cta` 12px CTA blocks. Driver: `radius-control` 6px, `radius-app-card` 8px, `radius-sheet` 14px. Pills and avatars `radius-full`.
- Marketing depth comes from white on grey, not shadow. The only marketing shadows are gold-tinted: `shadow-card-hover`, `shadow-gold`. No grey drop shadows.
- Card hover is one choreography everywhere: border to `accent-border-hover`, `shadow-card-hover`, 3px lift, on `ease-slow`.
- Driver cards use `shadow-lifted`; bottom sheets `shadow-sheet-up`.
- Scroll reveal: fade up 28px over 650ms on `ease-slow`, staggered 100ms. Respect reduced motion everywhere.

## Interaction rules

- One gold-filled button per visible surface.
- Focus: 2px `focus` outline with 2px offset. Inputs change only their border to `accent` on focus.
- Hover and active tabs share one gold-tinted look.
- Live driver states blink their pill dot; only one trip can be live at a time.

## Iconography

- Lucide outline icons, `currentColor`, 16px inline, 28px on marketing cards, stroke 1.33 on marketing and 1.5–2 in the driver app.
- Marketing card icons animate on card hover with one of three keyframes: lift, bounce or tilt.
- The native driver app currently uses Feather; move it to Lucide for one set.
- No emoji.

## Logo and imagery

- The PAL wordmark is white-only, triple-line letterforms. Place it on `chrome` or photography, never on a light ground. See the Logos group.
- There is no vector master: the shipped `logo.svg` wraps a 397×220 PNG. Request a true vector before using the mark large or in print.
- Photography: real vehicles on clean grounds (Fleet group) and city landmarks for coverage pages (Cities group).

## Using this in code

- Apps put `data-app="driver"` (or their own product id) on `<html>`, which switches text to Geist.
- Marketing pages: load Barlow from Google Fonts, link the tokens stylesheet, set `data-app="marketing"` on `<html>`.
- Driver web app (Tailwind v4 + shadcn): import the PAL `@theme` file and map shadcn's semantic vars to these tokens under `[data-app="driver"]`. Only semantic tokens may be overridden per product; primitives (`cod-*`, `husk-*`, spacing, radius, type scale) never change.
- Driver native app (Expo): import the generated `theme.ts`.
- Component guidelines are in `docs/components/`. They describe the shipped components; the production source lives in the PAL Driver App repo.
