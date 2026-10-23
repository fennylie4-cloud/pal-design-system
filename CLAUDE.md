# PAL Design System — rules for AI coding tools

Before building any PAL screen, read `docs/BRAND-BOOK.md`, then the `docs/components/*.md` file for each component you use. Token values and usage notes are in `tokens.json`.

Rules:

- Use tokens, never raw hex. Gold is `--accent` (husk-400 #b6a269). Gold text that must be read is `--accent-text`. Text on gold is `--on-accent`, never white.
- One gold-filled primary button per visible surface.
- Fonts by product: the marketing website uses Barlow (`--font-sans`). Every app uses Geist (`--font-app`). Never mix them on one screen. Geist Mono only for refs, flight codes and pill labels.
- Scope products with `data-app="marketing"` or `data-app="driver"` on `<html>`. A product may override semantic tokens only, never primitives (`cod-*`, `husk-*`, spacing, radius, type scale).
- Light theme only. Do not add dark mode styles.
- Marketing card hover is one choreography everywhere: border to `--accent-border-hover`, `--shadow-card-hover`, 3px lift on `--ease-slow`.
- Driver trip states use `data-pill="<state>"`; flight and urgency signals use `data-tone="ok|warn|info|danger|husk"`. Always pair colour with a word.
- Copy: PAL is the subject ("PAL tracks your flight"), no em dashes, no slogans, no emoji, verb-first buttons.
- The white PAL wordmark (`assets/logos/`) goes on `--chrome` (cod-950) or dark photography only. Never recolour or redraw it.

Editing this repo:

- `tokens.json` is the only file edited by hand for values. After changing it, run `python3 scripts/build.py` and commit the regenerated `tokens.css`, `tailwind-theme.css` and `theme.ts` with it.
- Check `docs/SOURCE-CONFLICTS.md` before changing a value; it records why each one was chosen.
