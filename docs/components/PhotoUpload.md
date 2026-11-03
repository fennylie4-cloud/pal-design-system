# PhotoUpload

A single photo with preview, such as a driver photo or a vehicle image.

**Products:** Back office.

**Consumer provides:** `v-model` (image URL or null), `label`.

The same dropzone as FileUpload, square, with an image icon in the round tile and "Upload a photo or drag it here" over "PNG or JPG, square works best". Once set: the photo, square, with a `border` hairline and `radius-md`, then a small outline Replace button and a ghost ✕ remove button under it.

Source: `PAL Backend/web/src/components/list/PhotoField.vue`, styles in `src/styles/backoffice.css` `.dropzone`.
