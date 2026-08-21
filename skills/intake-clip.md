# intake-clip

Use when Igor drops bruto, pastes a media path, or says “começa um projeto”.

## Ask only if the stage needs it

Format preset, cut aggressiveness, brand kit completeness, spend policy. If already stated this turn, do not re-ask.

## Do

1. Accept `.mp4`, `.mov`, or `.mkv`.
2. Copy/normalize into `raw/` if the file arrived from a pasted path outside the folder.
3. Normalize to mp4 on ingest with FFmpeg ([`documentation/services/ffmpeg.md`](../documentation/services/ffmpeg.md)). If `ffmpeg` is not callable, stop; do not fake an ingest.
4. Create `projects/<clip>/` with:

```
projects/<clip>/
  source/          (normalized mp4)
  transcript.json  (absent until rough cut)
  edl.json         (absent until rough cut)
  composition.html (absent until graphics)
  previews/
  outputs/
```

5. Name `<clip>` from the file stem unless Igor names it. Slug: lowercase, hyphens, no spaces.
6. Write or update `documentation/.activities/clips/<clip>/overview.md` (goal, preset if known, current stage = intake done).
7. Produce a preview of the ingested file in `projects/<clip>/previews/` when FFmpeg works.
8. Stop. Next stage: rough cut. Show paths.

Do not start WhisperX in this skill unless Igor asked for more than one stage.
