# Agentes

**Role:** Context repository and local video-editing operating system for **Igor**.

**Parent:** none (repo root)

A model with no memory uses this folder to know who Igor is, how footage becomes a published video, and which skill to load. The agent does not invent cuts by eye and does not re-render a whole video for a local tweak.

## Who

**Igor** is the creator and the only human approver. He drops raw footage, directs in natural language, and signs off. The default agent is the Process Caller, which then loads the Video Editor for pipeline work.

## Map

Always-on: this file · [`agents/process-caller.md`](agents/process-caller.md) · [`skills/README.md`](skills/README.md) · Git status of **this** repo.

Pull after classification: the named activity, the relevant service note, the one skill the route needs.

Never always-inject: all of `documentation/`, archived `done/`, or any previous vault as live source.

## Standing restrictions

Do not ask Igor to waive these.

| Rule | Meaning |
|---|---|
| Search scope | Grep only this repo plus the **allowlist** in [`documentation/services/pipeline.md`](documentation/services/pipeline.md). |
| Implementation scope | Closed until Igor reopens it on the activity overview. |
| Git (this repo) | After every meaningful change: **commit, then `git push` to `origin`** so the work is saved in the cloud (`https://github.com/igorlsobral/Agentes.git`). Standing rule (Igor, 2026-08-19). Never `push --force`. Never skip hooks. Never commit secrets (`.env`, credentials, tokens). Media binaries stay gitignored. |
| Git (product clones) | Sync (fetch + fast-forward) before trust. Edit when asked. Do not commit or push clones unless Igor owns that policy. |
| No credentials | Never store API keys, tokens, or `.env` values in Git. |
| No invented stubs | Write `INFORMAÇÃO AUSENTE` instead of guessing. |
| One real question | Only genuine ambiguity — not to reconfirm closed decisions. |
| Tools do heavy work | WhisperX transcribes, FFmpeg cuts/joins/mixes/exports, HyperFrames renders graphics. The agent decides and fires tools. |
| Transcript is the timeline | No word-level `transcript.json` → no cut. |
| Silence from audio | Measure dB relative to the take. Never a fixed −35 dB. WhisperX stretches word timestamps into following silence — transcript-only cuts leave dead air. |
| Ingest | Accept `.mp4`, `.mov`, and `.mkv`; normalize to mp4 on ingest. |
| Rough cut lock | Lock before graphics. If the cut must change after graphics, warn cost and wait for confirmation. |
| Partial render | Mandatory on second pass. Full render only on first graphics pass, export, or explicit ask. |
| Feedback | Standing taste becomes a skill / `AGENTS.md` rule, not a one-clip patch. |
| Brand kit | `brand/` owns color, type, logo. Prints in `brand/references/`. Do not improvise identity. |
| Paid APIs | Default **off** (this PC only). Propose first; wait for explicit ok in chat. Never put tokens in Git. |
| Talk to Igor | Portuguese, didactic. He is not a programmer. |
| Definition of done | Real footage through the pipeline. A green unit test is not enough. |
| First render | Draft. Target “pretty good”, then iterate. |
| Whisk | Do not use Google Whisk. “Whisk X” means WhisperX. |

## Indexes

| Index | Path |
|---|---|
| Skills | [`skills/README.md`](skills/README.md) |
| Agents | [`agents/README.md`](agents/README.md) |
| Processes | [`processes/README.md`](processes/README.md) |
| Documentation | [`documentation/README.md`](documentation/README.md) |
| Adapters | [`adapters/README.md`](adapters/README.md) |
| Activities | [`documentation/.activities/README.md`](documentation/.activities/README.md) |
| Pendências (Igor) | [`documentation/pendencias.md`](documentation/pendencias.md) |
| Como usar | [`documentation/como-usar.md`](documentation/como-usar.md) |
| Video editor runtime | [`video-editor/README.md`](video-editor/README.md) |
| Presets | [`presets/README.md`](presets/README.md) |
| Brand | [`brand/README.md`](brand/README.md) |
| Scripts | [`scripts/README.md`](scripts/README.md) |
| Raw | [`raw/README.md`](raw/README.md) |
| Music | [`music/README.md`](music/README.md) |
| Projects | [`projects/README.md`](projects/README.md) |

## Pipeline (do not skip a stage)

1. Intake — bruto in `raw/` (or a pasted path) → `projects/<clip>/`
2. Rough cut — WhisperX → `transcript.json`; silence on audio; EDL in `edl.json`; FFmpeg assembly; keep last/best take; **lock**
3. Graphics (1st pass) — one graphic per segment via HyperFrames + format preset. Draft, not final
4. Second pass — Igor directs in natural language. Partial render only
5. Captions — short-form only. Reuse WhisperX transcript. Word-pop, Coolvetica, black box behind the word unless the preset says otherwise
6. Music — file path + level in dB (default **−23 dB** until Igor adjusts)
7. Export — MP4 in `projects/<clip>/outputs/` and a copy in Downloads. Never delete the project on export

Typical prompt: “começa um projeto neste bruto, preset long-form, faz o rough cut”.

Typical second pass: “no primeiro gráfico, move para baixo, deixa menor, usa a cor Claude e o PNG do mascote em `brand/assets/`”.

## Format presets

- `short-form-explainer` — graphics on top, face below, captions in the middle
- `tiktok-raw` — text hook + raw cut + captions
- `long-form` — cinematic YouTube-style intro (full face + punctual graphics)

If format is unclear, ask before generating graphics.

## Allowlist

See [`documentation/services/pipeline.md`](documentation/services/pipeline.md). This repo plus local tool dirs (`C:\Users\ig\tools\ffmpeg`, `C:\Users\ig\tools\node`, `.venv`) and the three upstream GitHub confirmation sources. Extra clones: P10.

## Language

- Structural files (skills, agents, processes, templates, this README): English
- Domain notes (people, glossary, pendências, clip overviews): Portuguese
- Domain terms are never translated (WhisperX, HyperFrames, EDL, Coolvetica)

## Gaps

Tool binaries and Coolvetica are on disk (2026-08-21). A `.mkv` bruto is in `raw/` (gitignored). Remaining: full brand kit, default format, cut feel, spend catalog if he ever wants paid extras — [`documentation/pendencias.md`](documentation/pendencias.md).

## Children

The Indexes table above. No extra routing table here.
