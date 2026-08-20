# FFmpeg

Cuts, join, audio mix, export, ingest normalize (`.mov`/`.mp4` → mp4).

Silence threshold: relative to the take’s volume. Never a fixed −35 dB.

Music default bed: −23 dB until Igor adjusts.

## Upstream (Igor, 2026-08-20)

- Source: [github.com/FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) (mirror of https://git.ffmpeg.org/ffmpeg.git)
- Tools we need: `ffmpeg`, `ffprobe` — **not** a clone of this source tree inside `Agentes`

## Local install (2026-08-20)

Gyan full build **9.0**, extracted to the user tools dir (winget extract into Program Files failed).

| Binary | Path |
|---|---|
| ffmpeg | `C:\Users\ig\tools\ffmpeg\bin\ffmpeg.exe` |
| ffprobe | `C:\Users\ig\tools\ffmpeg\bin\ffprobe.exe` |

Also on User PATH: `C:\Users\ig\tools\ffmpeg\bin`. New terminals pick this up; this Cursor session already can call `ffmpeg`.

## Invoke

```text
C:\Users\ig\tools\ffmpeg\bin\ffmpeg.exe  …
C:\Users\ig\tools\ffmpeg\bin\ffprobe.exe …
```

Or `ffmpeg` / `ffprobe` after PATH refresh.

## Typical jobs in this pipeline

| Job | Pattern |
|---|---|
| Ingest `.mov` → mp4 | `ffmpeg -i source.mov -c:v libx264 -c:a aac projects/<clip>/source/<stem>.mp4` |
| Assembly from EDL | concat demuxer or filter_complex from `edl.json` keep ranges |
| Music bed | mix at **−23 dB** until Igor adjusts |
| Silence | measure on **audio**, relative to this take — never a fixed −35 dB |
