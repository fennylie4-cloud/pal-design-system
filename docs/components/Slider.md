# Slider

Progress track plus chevron pair under every horizontal carousel.

**Consumer provides:** `position` (0–1 scroll progress), `thumb` (visible slice in %), `onPrev`, `onNext`. Wire them to the carousel's `scrollLeft`; step one card width plus 16px per click.

2px `border` track, `accent` thumb, 40px outline chevron buttons that turn gold on hover and dim at the ends. Hide it on desktop when the grid does not scroll.

Source: `font-rules.md` → `.pal-slider`.
