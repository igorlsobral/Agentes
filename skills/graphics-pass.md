# graphics-pass

Use for the **first** HyperFrames pass. Draft, not final.

Requires: locked rough cut (`edl.json` + locked flag). If unlocked, stop and run or resume rough-cut.

## Do

1. If format preset is missing, ask before generating graphics.
2. Load [`presets/`](../presets/README.md) and [`brand/`](../brand/README.md). Missing brand tokens → `INFORMAÇÃO AUSENTE`; do not improvise identity.
3. One graphic per segment. HyperFrames CLI per [`documentation/services/hyperframes.md`](../documentation/services/hyperframes.md) (`npx hyperframes render` in `projects/<clip>/graphics/`).
4. Full render is allowed on this 1st pass.
5. Write `projects/<clip>/composition.html` and the HyperFrames `index.html` in `graphics/`.
6. Preview in `projects/<clip>/previews/`.
7. Stop. Next stage: second pass (Igor directs). Goal of this pass: “pretty good”.

Do not spend paid B-roll/TTS/Veo APIs.
