# Sidebar

The back office navigation: PAL mark, page links in the same order as WeWeb, the signed-in user, Log out and the version line.

**Products:** Back office.

**Consumer provides:** Nothing: the nav list lives in the shell.

Based on shadcn Sidebar on PAL's `chrome` ground (cod-950) with the white wordmark. 240px open, 64px collapsed; the toggle sits next to the wordmark and the width animates on `duration-base`.

- Items (shadcn SidebarMenuButton): 36px, 8px side padding, 8px between icon and label, 4px apart, `radius-control`, 14px/500 in `cod-400` with a 16px icon. Hover: `text-inverse` on cod-50 at 8%. Current page: `accent-fill` with `text-inverse` and a gold icon. Focus: the gold `shadow-focus` ring.
- Collapsed: 40px icon squares, centred. Each one shows its name in a Tooltip to the right on hover or keyboard focus, built on Reka UI `TooltipRoot`: a `cod-900` chip, 12px/500 `text-inverse`, `radius-control`.
- Footer, after a hairline: the signed-in user (24px Avatar and email), Log out as a menu item, then the version line in Geist Mono 11px.

Source: `PAL Backend/web/src/layouts/AppShell.vue`, `.tooltip` in `src/styles/backoffice.css`.
