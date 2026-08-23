# full-screen-visual

Use when Igor marks a stretch as **tela cheia**, says **volta ao normal**, or asks for event **sfx** on those visuals.

Always available after the rough cut is locked. Not a new pipeline stage — a graphics mode inside the existing graphics / second-pass work.

## Do

1. Requires locked rough cut (`edl.json` + lock). If unlocked, stop and resume rough-cut.
2. Find start and end of the stretch:
   - Prefer the chat: a quoted spoken phrase, a clock time on the cut, or “volta ao normal”.
   - Also accept a clear spoken cue in `transcript.json` if he said it on camera.
   - Do not invent the range. If start or end is missing, ask once.
3. For that range, cover the **entire frame**. Hide the talking-head. Keep the assembly voice.
4. Visuals follow what he actually said. Transcript is the timeline. Allowed: text, diagrams, images from [`brand/assets/`](../brand/README.md) or a folder he names (including `projects/<clip>/graphics/assets/`), and a matching stretch from [`cenas/`](../cenas/README.md) (skill [`match-cenas.md`](match-cenas.md)). Animate images (enter, slide, swap) when it helps the sentence. One visual beat per spoken idea. **cenas/** is the standing scene library for every format, not only tela cheia.
   Standing **tela cheia / 3D reel** taste (Igor, 2026-08-22; file in [`brand/references/`](../brand/references/README.md)): **clone the Reel’s motion**, do not restyle the same card. One continuous 3D world: camera keeps drifting, objects fly through Z (sheets, coins, lock, cross) with depth blur, text is huge and **changes place/angle every beat**, sometimes sitting on the object (lock + words to the right). Glow + RGB fringe. Accent color **follows the spoken idea**. Do not default to neon green. Do not reuse one centered stack.
   Standing **VSL frase de impacto** (Igor, 2026-08-22): when the reference VSL does it, **stop the scene**. The frame is **only** the phrase (full screen). Do not keep cenas moving under the words on that beat. Clock those hits from the reference before drawing. The **transition** to the white screen starts **at the first sound of the highlight word**. Keep the fade-to-white and the word animation. Do not flatten the motion (Igor, 2026-08-23).
5. **Event sfx** — when a visual needs a sound, mix a one-shot from [`sfx/`](../sfx/README.md) under the voice, timed to the motion. Not a music bed.
   Standing examples (Igor, 2026-08-21):
   - walking character → footsteps or a quieter step
   - door knock → toc-toc
   - correct check → plim
   - rising numbers → short bubble ticks (bubububu)
   Match the event. Do not sprinkle random hits.
   If the matching file is missing in `sfx/`, synthesize a short discreet one on this PC with FFmpeg. Do not download a library. If he later drops a better file, swap.
   Level: quieter than speech (same idea as whoosh). Never drown the voice.
6. Outside the stretch: standing taste (long-form / VSL: cards on the **right**, do not cover the face).
7. HyperFrames composition at **60 fps**. Preview in `projects/<clip>/previews/`.
8. If this is still the first graphics draft, a full render is allowed. If graphics already exist, **partial render** of the tela cheia stretch only.
9. VSL copy rules still hold: do not invent price, guarantee, or CTA.
10. Stop. Next stage: second pass unless he already named another.

## Do not

- Start tela cheia without a marked range.
- Pull paid B-roll, Veo, or stock from the internet. Local library is [`cenas/`](../cenas/README.md).
- Treat event sfx as the `music/` bed.
