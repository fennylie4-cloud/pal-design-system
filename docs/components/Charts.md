# Charts

Analytics charts: headline numbers, B2B against B2C, ranked counts and a trend over time.

**Products:** Back office.

**Consumer provides:** `StatTile` (`title`, `caption`, `value`, or `soon`), `SplitBar` (two `parts`), `RankBars` (`items` with `label` and `count`), `TrendChart` (`points`, `unit`, `partialLast`).

Based on shadcn Chart and its dashboard cards, drawn in plain SVG and CSS.

- Chart cards: `.section-card` with 20px padding and 16px between parts. Title 16px/600, the note on the right ("Per month", "Active bookings") 13px `text-muted`.
- StatTile (shadcn section card): label 13px/500 `text-muted`, the number 24px/600 with tabular figures, caption 12px `text-muted`. Card, hairline and `shadow-app-card` like Card. A figure the API doesn't return yet sits on `bg-elevated` with a dashed border and no shadow, reading "Not available yet".
- Colours come from the `chart-*` tokens: `chart-mark` for single-series bars and lines, `chart-b2b` and `chart-b2c` for the two customer types everywhere, `chart-grid` for gridlines. Axis labels are 12px `text-muted`.
- Tooltip (shadcn ChartTooltip): `bg-surface`, `border` hairline, `radius-md`, `shadow-lifted`, 12px. The period on top at 500, then a row with a 10px swatch in the series colour, the series name in `text-muted` and the value in Geist Mono on the right. It stays inside the chart at either end.

Every value is also written as text next to its mark. The trend chart has a crosshair that follows the pointer and the arrow keys. A still-filling last period is drawn dashed and labelled "so far".

Source: `PAL Backend/web/src/components/analytics/*.vue`.
