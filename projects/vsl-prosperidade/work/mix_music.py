"""Loop a bed under the VSL voice at default -23 dB."""
from __future__ import annotations

import subprocess
from pathlib import Path

FFMPEG = Path(r"C:\Users\ig\tools\ffmpeg\bin\ffmpeg.exe")
PROJ = Path(r"C:\Users\ig\Documents\Agentes\projects\vsl-prosperidade")
PREV = PROJ / "previews"
MUSIC = Path(r"C:\Users\ig\Documents\Agentes\music\vsl-prosperity-bed.mp3")
# Igor 2026-08-22: a bit louder, especially the first seconds
BODY_DB = -20
START_DB = -17
START_S = 20.0


def run_ff(args: list[str]) -> None:
    r = subprocess.run([str(FFMPEG), "-hide_banner", "-loglevel", "error", "-y", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-2000:] if r.stderr else "ffmpeg failed")


def mix(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    run_ff(
        [
            "-i",
            str(src),
            "-stream_loop",
            "-1",
            "-i",
            str(MUSIC),
            "-filter_complex",
            (
                f"[1:a]volume=if(lt(t\\,{START_S:.1f})\\,{10 ** (START_DB / 20):.6f}\\,{10 ** (BODY_DB / 20):.6f}):eval=frame[m];"
                f"[0:a][m]amix=inputs=2:duration=first:normalize=0[a]"
            ),
            "-map",
            "0:v:0",
            "-map",
            "[a]",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-ar",
            "48000",
            "-ac",
            "2",
            "-shortest",
            "-movflags",
            "+faststart",
            str(dest),
        ]
    )
    print("mixed", dest, dest.stat().st_size, flush=True)


def main() -> None:
    mix(PREV / "03-graphics-inicio.mp4", PREV / "04-music-inicio.mp4")
    mix(PREV / "03-graphics-pass.mp4", PREV / "04-music-pass.mp4")
    # short check of the 3 landscape testimonials
    run_ff(
        [
            "-i",
            str(PREV / "04-music-inicio.mp4"),
            "-t",
            "22",
            "-c",
            "copy",
            "-movflags",
            "+faststart",
            str(PREV / "04-music-depoimentos.mp4"),
        ]
    )
    print("check", PREV / "04-music-depoimentos.mp4")


if __name__ == "__main__":
    main()
