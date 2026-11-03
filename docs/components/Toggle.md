# Toggle

On/off switch for a setting that takes effect straight away, such as a vehicle or zone being active.

**Products:** Back office.

**Consumer provides:** `v-model` (boolean), `label`, optional `hideLabel` when the column header already names it.

Based on shadcn Switch: a 32 by 18px track with a 16px thumb, `accent` when on and `border-strong` when off, the focus ring on the track, 50% when disabled. A native checkbox with `role="switch"` underneath, so keyboard and screen readers treat it as a switch. The label is 14px, 500 weight, and always says what is switched.

Source: `PAL Backend/web/src/components/list/ToggleSwitch.vue`.
