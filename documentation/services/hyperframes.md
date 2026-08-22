# HyperFrames

Motion graphics, overlays, captions: HTML/CSS/GSAP → MP4. One graphic per segment on 1st pass. Partial render on second pass. A marked **tela cheia** stretch is a full-frame composition (talking-head hidden, voice stays) until **volta ao normal**.

Brand tokens from `brand/`. Preset layout from `presets/`.

## Upstream (Igor, 2026-08-20)

- Source: [github.com/heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main)
- Docs: [hyperframes.dev](https://www.hyperframes.dev/)
- CLI via npx (not a clone of the monorepo)

## Local install (2026-08-20)

| Piece | Path / version |
|---|---|
| Node.js | `C:\Users\ig\tools\node\node.exe` — v22.23.2 |
| npx | `C:\Users\ig\tools\node\npx.cmd` |
| HyperFrames CLI | `npx --yes hyperframes` — v0.8.4 |
| Chrome Headless Shell | `C:\Users\ig\.cache\hyperframes\chrome\chrome-headless-shell\win64-152.0.7928.2\chrome-headless-shell-win64\chrome-headless-shell.exe` |
| Telemetry | disabled (`npx hyperframes telemetry disable`) |

User PATH includes `C:\Users\ig\tools\node`. `hyperframes doctor`: FFmpeg, ffprobe, Node, Chrome **OK**. Docker / whisper-cpp / Kokoro / MusicGen left uninstalled (optional; spend/policy).

Do **not** run `npx skills add heygen-com/hyperframes` here. Process Caller stays the only classifier.

## Invoke in this pipeline

```text
C:\Users\ig\tools\node\npx.cmd --yes hyperframes init projects/<clip>/graphics
cd projects/<clip>/graphics
C:\Users\ig\tools\node\npx.cmd --yes hyperframes preview
C:\Users\ig\tools\node\npx.cmd --yes hyperframes render -o ..\previews\<name>.mp4 --fps 60 --quality high
```

Keep a copy of the composition as `projects/<clip>/composition.html`. First graphics pass: full render allowed. Second pass: **partial** render of the changed stretch only.

## Do not (without Igor’s ok)

- `hyperframes cloud` / `lambda` / `cloudrun`
- `hyperframes tts` / `/media-use` paid generation
- `hyperframes auth` (HeyGen account)
- Invent brand tokens — `brand/` still wins
