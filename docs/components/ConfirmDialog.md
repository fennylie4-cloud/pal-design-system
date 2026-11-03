# ConfirmDialog

Asks before a destructive or bulk action, or explains why it can't happen.

**Products:** Back office.

**Consumer provides:** `title`, `description` (what PAL will do and what it affects), `confirmLabel` (the verb, such as "Delete company"), optional `keepLabel`, `blocked`.

Based on shadcn Alert Dialog, built on Reka UI `AlertDialogRoot` for behaviour only. It looks like Dialog at 512px with no close button and no footer hairline. A click on the dimmed page does not close it, and focus starts on the safe button, so Enter never confirms by accident. Escape keeps the record.

Footer: the keep button (outline, "Keep it" unless `keepLabel` says otherwise) and the destructive confirm button. The page runs the action on confirm and then closes the dialog.

When `blocked` is set the confirm button is hidden and the keep button reads Close, for cases like a zone that a pricing plan still uses. The description says what to change first.

Source: `PAL Backend/web/src/components/list/ConfirmDialog.vue`.
