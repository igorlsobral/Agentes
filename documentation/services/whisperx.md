# WhisperX

Word-level transcription. Output is the timeline: `projects/<clip>/transcript.json`.

WhisperX stretches a word’s timestamp until the following silence. Cutting only on those end times leaves dead air. Silence must be measured on audio, relative to the take.

Do not use Google Whisk. “Whisk X” means this tool.

## Upstream (Igor, 2026-08-20)

- Source: [github.com/m-bain/whisperX](https://github.com/m-bain/whisperX)
- Installed via `pip install whisperx` into this repo’s venv (do not vendor the GitHub tree)

## Local install (2026-08-20)

| Piece | Path |
|---|---|
| Python 3.12.10 | `C:\Users\ig\AppData\Local\Programs\Python\Python312\python.exe` |
| venv | `C:\Users\ig\Documents\Agentes\.venv\` (gitignored) |
| whisperx 3.8.6 | `C:\Users\ig\Documents\Agentes\.venv\Scripts\whisperx.exe` |

User PATH includes `.venv\Scripts`. Device default: **CPU** (`--device cpu --compute_type int8`) until a CUDA GPU stack is confirmed. This machine is an Intel i5-8400 with no CUDA install.

## Invoke

```text
C:\Users\ig\Documents\Agentes\.venv\Scripts\whisperx.exe projects/<clip>/source/<file>.mp4 --model large-v2 --language pt --device cpu --compute_type int8 --output_dir projects/<clip>/ --output_format json
```

Copy/normalize the word-level JSON to `projects/<clip>/transcript.json`. No word-level file → do not cut.

## Do not (without Igor’s ok)

- `--diarize` / Hugging Face token
- Replicate / other hosted WhisperX APIs
- Retranscribe for captions — reuse `transcript.json`
