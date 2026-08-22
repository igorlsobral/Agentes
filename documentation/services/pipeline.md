# Pipeline

Pipeline local: bruto → vídeo publicado. Ordem fixa: intake → rough cut (lock) → graphics 1st pass (60 fps overlay; **tela cheia** if marked) → second pass → captions (short-form) → music/sfx → export **60 fps**.

## Allowlist (grep / edit)

| Path or source | Status |
|---|---|
| `c:\Users\ig\Documents\Agentes` | this context + working editor — **edit + commit + push** |
| `C:\Users\ig\tools\ffmpeg\bin\` | local FFmpeg 9.0 (Gyan) |
| `C:\Users\ig\tools\node\` | local Node.js 22.23.2 |
| `C:\Users\ig\Documents\Agentes\.venv\` | WhisperX 3.8.6 (gitignored) |
| `C:\Users\ig\AppData\Local\Programs\Python\Python312\` | Python 3.12.10 |
| [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | confirmation source only — do not clone into this repo |
| [m-bain/whisperX](https://github.com/m-bain/whisperX) | confirmation source only |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | confirmation source only — invoke via `npx hyperframes` |

Other clones / extra `raw/` folders: still `INFORMAÇÃO AUSENTE` (P10).

Remote of **this** repo: `https://github.com/igorlsobral/Agentes.git`. Standing Git rule (Igor, 2026-08-19): after every meaningful change, commit then `git push` to `origin`. Never `push --force`. Never commit secrets.

PowerShell may not have `git` on PATH; use `C:\Program Files\Git\cmd\git.exe` when needed.

## Spend

Default **2026-08-21:** no paid calls. Local FFmpeg + WhisperX CPU + HyperFrames + Chrome only.

Do not call paid APIs (B-roll, TTS, Veo, HyperFrames cloud/Lambda, WhisperX diarization/HF token, unnamed others) without a **proposal in chat** and Igor’s explicit ok. He is not expected to open developer accounts. Tokens never go in Git.

Catalog of accounts he even has: none recorded (P9 still open as “none until he says otherwise”).

## Runtime folders

`raw/` · `music/` · `sfx/` · `cenas/` · `projects/<clip>/` · `presets/` · `brand/` · `scripts/` · `video-editor/`
