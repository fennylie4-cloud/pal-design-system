# Field

A form field's frame: the label, the control, then a hint or an error under it.

**Products:** Back office.

**Consumer provides:** a `.field` wrapper holding a `.field-label`, one control (an Input or textarea, or a MultiSelect or Select dropdown), and optionally a `.field-hint` or a `.field-error`. Form-level messages at the end of a dialog use `.field-error` too.

Based on shadcn Field (FieldLabel, FieldDescription, FieldError). 8px between the parts. The label is 14px, 500 weight, `text-primary`, and fades to 50% when its control is disabled. The hint is 14px `text-muted` and says what to enter. The error is 14px `destructive` and says how to fix it, for example "Add the driver name, mobile number and plate number." Mark the control with `aria-invalid="true"` when the error is about it.

The control keeps its own look and states, set in its guide (Input, MultiSelect); Field only adds what goes around it.

One shared style for every form. Before this, 18 files styled their own error text and 9 their own hints.

Source: `PAL Backend/web/src/styles/backoffice.css` `.field`, `.field-label`, `.field-hint`, `.field-error`.
