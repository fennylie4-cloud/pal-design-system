# FileUpload

Attach files to a booking: welcome sign, itinerary, no-show photos.

**Products:** Back office.

**Consumer provides:** `v-model` (files with `name`, `url`, `size`), `label`, `hint` (accepted types), optional `accept` and `multiple`.

Based on the shadcn dropzone pattern (as in the diceui and Origin UI file upload components), in plain CSS.

- Drop zone: a button with a dashed `border-strong` outline, `radius-md`, `bg-surface`, 24px by 16px padding, centred. A 40px round tile with a `border` hairline holds a 16px upload icon in `text-muted`. Then "Upload a file or drag it here" (14px, the first words in `text-primary` at 500) and the accepted types in 12px `text-muted`. Hover `bg-elevated`; dragging a file over it turns the outline `accent` on `accent-fill-soft`; focus shows the gold ring. Clicking it opens the file picker.
- File row: `border` hairline, `radius-md`, 8px padding, 12px gap. A 40px thumbnail (the image, or a file icon on `bg-elevated`), the name in 14px/500 (cut with an ellipsis) over the size in 12px `text-muted`, then Download and Remove as 32px ghost icon buttons: `text-muted`, `text-primary` on `bg-elevated` when hovered. Remove uses an ✕, as shadcn does, not a bin.

With `multiple`, the drop zone stays under the list; otherwise it is replaced by the one file.

Source: `PAL Backend/web/src/components/booking/FileField.vue`, styles in `src/styles/backoffice.css` `.dropzone`, `.file-item`.
