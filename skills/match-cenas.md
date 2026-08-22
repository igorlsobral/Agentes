# match-cenas

Use when a spoken idea should be illustrated with a stretch from [`cenas/`](../cenas/README.md). Any format after lock — not only **tela cheia**.

Igor, 2026-08-22: this folder is the standing repertoire. Use it whenever a beat needs a matching scene.

## Do

1. Requires locked rough cut (`edl.json` + lock). If unlocked, stop and resume rough-cut.
2. Library is **only** [`cenas/`](../cenas/README.md). Do not treat `raw/` as this library (`raw/` is the talking-head bruto).
3. If `cenas/` is empty: do not invent footage. If Igor asked to use a scene, tell him the folder is empty and the Explorer path. If he did not ask, skip and continue cards / tela cheia from `brand/assets/` as usual.
4. Pick the spoken beat from `transcript.json` (quoted phrase, clock on the cut, or a clear concrete visual: place, person, action). One scene per spoken idea. Do not wallpaper every sentence.
5. Search the library: detect scene changes with FFmpeg, extract a few stills per scene (start / middle / end), look at the stills, choose in/out that match **that** sentence. If nothing matches, say so — do not force a near-miss.
6. Cut that range into `projects/<clip>/graphics/assets/`. Discard (mute) library audio. Keep the assembly voice.
7. Placement:
   - Clone **VSL**: after the testimonials block, body beats are full-frame stretches timed to the reference ([`presets/vsl.md`](../presets/vsl.md)). **Frase de impacto** beats: scene stops; text only ([`full-screen-visual.md`](full-screen-visual.md)).
   - Marked **tela cheia** stretch → full frame + event sfx via [`full-screen-visual.md`](full-screen-visual.md).
   - Otherwise still allowed on every preset. Show the action clearly. Long-form / talking-head VSL: do not cover the face unless that beat needs the whole frame. `tiktok-raw` / `short-form-explainer`: the scene may occupy more of the frame at that moment.
8. Composite at **60 fps**. Preview in `projects/<clip>/previews/`.
9. First graphics pass: full render allowed. Later: **partial render** of the changed stretch only.
10. Stop. Next stage stays graphics / second pass unless he named another.

## Do not

- Pull paid B-roll, Veo, or stock from the internet.
- Start a new clip from a file in `cenas/` (that is intake of `raw/`).
- Invent a match, a price, a CTA, or a guarantee.
