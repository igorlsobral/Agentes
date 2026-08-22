# Process Caller

Session-default. Classify **this turn**, then load the minimum files. This file owns the **only** routing table.

After classification: read [`skills/README.md`](../skills/README.md) (index only), load the named skill, state the **route in one line**.

## Routing table

| Demand looks like | Route to |
|---|---|
| Continuation of a named clip (`projects/<clip>/` or an activity folder) | That folder first (`edl.json`, `transcript.json`, overview if any), then the skill for the **current unlocked stage** |
| New bruto / “começa um projeto” / path to `.mp4` or `.mov` | [`skills/intake-clip.md`](../skills/intake-clip.md) — one stage; do not skip to graphics |
| Rough cut / WhisperX / silêncio / EDL / assembly | [`skills/rough-cut.md`](../skills/rough-cut.md) |
| Graphics 1st pass / HyperFrames draft / preset layout | [`skills/graphics-pass.md`](../skills/graphics-pass.md) — only if rough cut is locked; if a **tela cheia** range is already marked, also load [`skills/full-screen-visual.md`](../skills/full-screen-visual.md); if `cenas/` has files, also load [`skills/match-cenas.md`](../skills/match-cenas.md) |
| Tela cheia / “volta ao normal” / full-screen visuals / event sfx on a stretch | [`skills/full-screen-visual.md`](../skills/full-screen-visual.md) — only if rough cut is locked; if the visual is a stretch from `cenas/`, also load [`skills/match-cenas.md`](../skills/match-cenas.md) |
| Matching scene from `cenas/` / “usa as cenas” / local B-roll on any format | [`skills/match-cenas.md`](../skills/match-cenas.md) — only if rough cut is locked; stacks with graphics-pass / full-screen-visual / second-pass |
| Second pass / natural-language direction on an existing graphic | [`skills/second-pass.md`](../skills/second-pass.md) — partial render; “tela cheia” / “volta ao normal” / event sfx → full-screen-visual; matching scene from `cenas/` → match-cenas |
| Captions / legendas / word-pop (short-form) | [`skills/captions.md`](../skills/captions.md) |
| Music / trilha / dB level | [`skills/music-mix.md`](../skills/music-mix.md) |
| Export / MP4 final / copy to Downloads | [`skills/export-video.md`](../skills/export-video.md) |
| “Remember this” / standing taste / brand correction | [`skills/promote-feedback.md`](../skills/promote-feedback.md) |
| Question about the pipeline or a tool | [`documentation/services/`](../documentation/services/) — do **not** open a new clip |
| How we work / confirmation of a rule | skill [`find-documentation.md`](../skills/find-documentation.md) — confirmation source first |
| Implementation / edit of scripts in this repo | [`agents/video-editor.md`](video-editor.md) + [`consult-local-project.md`](../skills/consult-local-project.md) |
| Review of analysis, plan, or structural diff | [`auditor.md`](auditor.md) |
| Indexes, adapters, skill or agent inventory | [`maintain-repo-index.md`](../skills/maintain-repo-index.md) then auditor |
| Raw new demand, no folder yet, planned-work shaped (not footage) | do **not** auto-run; tell Igor to invoke [`validate-task.md`](../skills/validate-task.md) |
| Nature of work changed mid-session | [`re-route-mid-session.md`](../skills/re-route-mid-session.md) (re-read this file; no second table) |

## Rules

- Adapters and `AGENTS.md` **point** here. They never copy this table.
- Multiple routes may stack. Archived `done/` is reference-only.
- If nothing fits: say so, one question, then consider [`identify-missing-processes.md`](../skills/identify-missing-processes.md) **after** Igor’s problem is handled.
- If format, cut aggressiveness, brand kit, or spend policy is missing **and** the current stage needs it, ask. Otherwise execute the current stage to a preview in `previews/`.
