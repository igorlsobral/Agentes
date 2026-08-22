# graphics-pass

Use for the **first** HyperFrames pass. Draft, not final.

Requires: locked rough cut (`edl.json` + locked flag). If unlocked, stop and run or resume rough-cut.

## Do

1. If format preset is missing, ask before generating graphics.
2. Load [`presets/`](../presets/README.md) and [`brand/`](../brand/README.md). Missing brand tokens → `INFORMAÇÃO AUSENTE`; do not improvise identity.
3. One graphic per segment. HyperFrames CLI per [`documentation/services/hyperframes.md`](../documentation/services/hyperframes.md) (`npx hyperframes render` in `projects/<clip>/graphics/`). **Motion graphics and any version treated as current picture: 60 fps** (`data-fps="60"` + `hyperframes render --fps 60 --quality high`). Camera footage may stay 30 fps underneath. A 30 fps overlay makes card tweens look like ~10 fps. Do not ship a 30 fps graphics preview as “the” file.
4. Full render is allowed on this 1st pass.
5. Write `projects/<clip>/composition.html` and the HyperFrames `index.html` in `graphics/`.
6. Whoosh/swoosh: prefer a file in [`sfx/`](../sfx/README.md). Igor may name a different file in that folder. If the folder is empty, generate a short quiet whoosh on this PC — do not download a library.
7. Preview in `projects/<clip>/previews/`.
8. Stop. Next stage: second pass (Igor directs). Goal of this pass: “pretty good”.

## Standing taste (Igor, 2026-08-21)

- Long-form and VSL talking-head: cards on the **right**. Do not cover the face or other important on-screen info — **except** a marked **tela cheia** stretch ([`full-screen-visual.md`](full-screen-visual.md)).
- If Igor already marked a tela cheia range (chat quote, clock, or spoken cue), build that stretch as full-frame visuals + event sfx, in the **3D reel** taste when that is the brief ([`full-screen-visual.md`](full-screen-visual.md)). Everywhere else: cards as usual.
- Headlines: ALL CAPS, heavy Coolvetica (`Coolvetica Hv Comp.otf`). Supporting text: sentence case (first letter only).
- Each card must look different — icons, gauge, contrast rows, rising steps — not four identical text boxes.
- Final (and graphics overlays) always **60 fps**.
- Swoosh is swappable; library is `sfx/`. Event sfx on tela cheia follow [`full-screen-visual.md`](full-screen-visual.md).

Do not spend paid B-roll/TTS/Veo APIs. Local tela cheia uses our folders only.
