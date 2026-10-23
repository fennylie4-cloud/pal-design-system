# PAL Design System

Design tokens, rules and component guidelines for PAL (Prime Aces Limousine): the marketing website and the PAL Driver App. Light theme only.

## What's inside

| Path | What it is | Use it for |
| --- | --- | --- |
| `docs/BRAND-BOOK.md` | Voice, colour, type, spacing, shape, motion, icons, logo rules | Read first, by people and AI tools |
| `docs/components/*.md` | One guideline per component: when to use it, props, states | Building screens |
| `docs/SOURCE-CONFLICTS.md` | Where old sources disagreed and what was chosen; known contrast failures | Before changing a value |
| `tokens.json` | Every token with a usage note. The single source of truth. | Tools, Figma plugins, scripts |
| `tokens.css` | CSS custom properties + type classes | Plain HTML / any web project |
| `tailwind-theme.css` | Tailwind v4 `@theme` with shadcn/ui colours mapped to PAL | React + Tailwind apps |
| `theme.ts` | Colours, spacing, radius, type for React Native / Expo | Mobile apps |
| `assets/logos/` | PAL wordmark (white, PNG) | Headers, app icons, social |
| `CLAUDE.md`, `AGENTS.md` | The rules in short form, read automatically by AI coding tools | Claude Code, Cursor, Codex and similar |

## Fonts by product

- Marketing website: **Barlow**.
- Every app (driver app, future portal and back office): **Geist**.
- Refs, flight codes, pill labels: **Geist Mono**.

All three are free on Google Fonts. `tokens.css` loads them for web; Expo apps load them with `@expo-google-fonts/geist`.

## Quick start

**Plain HTML**

```html
<html data-app="marketing">
  <link rel="stylesheet" href="tokens.css">
  <button style="background: var(--accent); color: var(--on-accent); border-radius: var(--radius-md);">Request a Quote</button>
</html>
```

**React + Tailwind v4 (shadcn/ui)**

```css
/* src/index.css */
@import "tailwindcss";
@import "./pal/tailwind-theme.css";   /* copy tailwind-theme.css and tokens.css into src/pal/ */
```

Put `data-app="driver"` on `<html>`. Then `bg-primary`, `text-muted-foreground`, `p-app-card`, `rounded-app-card`, `shadow-lifted`, `text-app-body` all resolve to PAL values.

**React Native / Expo**

```ts
import { Colors, Spacing, Radius, Type, Fonts } from './pal/theme';
const c = Colors.driver;
```

**AI app builders (v0, Lovable, Bolt, Cursor)**

Give the tool `docs/BRAND-BOOK.md` and `tailwind-theme.css`, and tell it: "Follow the PAL brand book. Use only these tokens." Add the relevant `docs/components/*.md` when building a specific screen.

**Claude**

The same system exists as a Claude design system page. Ask Fenny to share it with you, then give Claude its link.

## Products are scopes

`data-app="driver"` overrides only semantic tokens (backgrounds, text, border, accent states) and the font. Primitives (`cod-*`, `husk-*`, spacing, radius, type scale) are shared by every product and never overridden.

## Changing a token

1. Edit `tokens.json` (keep the usage note accurate).
2. Run `python3 scripts/build.py` to regenerate `tokens.css`, `tailwind-theme.css` and `theme.ts`.
3. Commit all four files together.
4. Tell Fenny so the Claude design system page gets the same change.

Never edit the three generated files by hand.

## Not included

- Production component code. It lives in the PAL Driver App repo; `docs/components/` describes it.
- Fleet and city photography. It stays with the website.
- A vector logo. The shipped mark is a PNG only.
