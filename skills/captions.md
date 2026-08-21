# captions

Use for **short-form** captions only (`short-form-explainer`, `tiktok-raw`). Skip this stage on `long-form` unless Igor explicitly asks.

## Do

1. Reuse `projects/<clip>/transcript.json`. Do **not** retranscribe.
2. Default style unless the preset overrides: word-pop, Coolvetica, black box behind the word.
3. Font files on disk (2026-08-21), default **Regular** for word-pop:

   - `brand/Coolvetica Rg.otf` — default
   - `brand/Coolvetica Rg It.otf` — italic
   - `brand/Coolvetica Rg Cond.otf`, `brand/Coolvetica Rg Cram.otf`, `brand/Coolvetica Hv Comp.otf` — condensed/heavy variants

   Do not silently substitute a look-alike.
4. HyperFrames overlay synced to word timestamps.
5. Partial render if captions are the only change after a previous graphics render.
6. Preview in `projects/<clip>/previews/`.
