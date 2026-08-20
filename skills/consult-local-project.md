# consult-local-project

Use when implementing or editing code/scripts inside the allowlist.

## Allowlist

Canonical list: [`documentation/services/pipeline.md`](../documentation/services/pipeline.md).

Default: **this repository only** (`c:\Users\ig\Documents\Agentes`) for edits.

Local tool dirs (invoke, do not treat as product code to rewrite): `C:\Users\ig\tools\ffmpeg`, `C:\Users\ig\tools\node`, `.venv`.

Upstream GitHub (read/fetch only): FFmpeg, WhisperX, HyperFrames. Do not clone those trees into `Agentes`. Do not commit or push them.

## Do

1. Sync (fetch + fast-forward) a listed Git clone **before** trusting it. Skip if no remote or if the tree is dirty — fetch + report only; do not pull into uncommitted work.
2. Edit the working tree when Igor asked.
3. Do not commit or push a third-party clone unless Igor owns that policy.
4. **This** context repo is different: after a meaningful change here, commit then push to `origin` (standing rule). Never force-push. Never commit secrets.
5. Do not grep outside the allowlist.
