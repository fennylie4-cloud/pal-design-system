# AvatarInitials

Driver identity mark: initials in a gold circle.

**Products:** Driver app, Back office.

**Consumer provides:** `initials` (two letters), `size` (`sm` 24px in chips, `md` 36px in list rows and the header, `lg` 64px on the profile hero).

`accent` fill, `on-accent` text, 600 weight. Circle on purpose, so identity never reads as a button. A photo will replace it later with the same API.

Source: driver `avatar-initials.tsx`.

## Back office

The signed-in user in the sidebar and drivers in lists and on Driver detail. Based on shadcn Avatar with PAL's fallback: the solid `accent` circle with `on-accent` initials at 600, as in the driver app. 32px (`.avatar`, 12px initials) in table rows, 56px (`.avatar-lg`, 18px) on Driver detail, 26px in the sidebar. A driver photo replaces the initials when there is one, cropped to the circle.

Source: `PAL Backend/web/src/styles/backoffice.css` `.avatar`.
