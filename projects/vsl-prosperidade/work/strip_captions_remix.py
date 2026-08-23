"""Remove dark bottom captions and remix music a bit louder, especially at the start."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

FFMPEG = Path(r"C:\Users\ig\tools\ffmpeg\bin\ffmpeg.exe")
FFPROBE = Path(r"C:\Users\ig\tools\ffmpeg\bin\ffprobe.exe")
ROOT = Path(r"C:\Users\ig\Documents\Agentes")
PROJ = ROOT / "projects" / "vsl-prosperidade"
WORK = PROJ / "work"
PREV = PROJ / "previews"
ROUGH = PREV / "rough-cut.mp4"
BEATS_PATH = WORK / "beats.json"
CLIP_DIR = WORK / "gfx_clips_v2"
MUSIC = ROOT / "music" / "vsl-prosperity-bed.mp3"
W, H, FPS = 1080, 1920, 60
OUR_END = 1908.487
# Subtle lift from -23: body -20 dB, first 20 s -17 dB
BODY_DB = -20
START_DB = -17
START_S = 20.0


def run_ff(args: list[str]) -> None:
    r = subprocess.run([str(FFMPEG), "-hide_banner", "-loglevel", "error", "-y", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-2000:] if r.stderr else "ffmpeg failed")


def probe_dur(path: Path) -> float:
    return float(
        subprocess.check_output(
            [str(FFPROBE), "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
            text=True,
        ).strip()
    )


def encode_scene_plain(beat: dict, dest: Path) -> None:
    dur = beat["end"] - beat["start"]
    src = beat["path"]
    clip_dur = probe_dur(Path(src))
    loops = max(1, int(dur // max(clip_dur, 0.5)) + 1)
    tmp = dest.with_name(dest.stem + "_tmp.mp4")
    run_ff(
        [
            "-stream_loop",
            str(loops),
            "-i",
            src,
            "-t",
            f"{dur:.3f}",
            "-an",
            "-vf",
            f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            "-pix_fmt",
            "yuv420p",
            str(tmp),
        ]
    )
    if dest.exists():
        dest.unlink()
    tmp.rename(dest)


def hide_white_caption(dest: Path) -> None:
    tmp = dest.with_name(dest.stem + "_tmp.mp4")
    run_ff(
        [
            "-i",
            str(dest),
            "-an",
            "-vf",
            "drawbox=0:1580:1080:340:white:t=fill",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "19",
            "-pix_fmt",
            "yuv420p",
            str(tmp),
        ]
    )
    dest.unlink()
    tmp.rename(dest)


def write_concat(paths: list[Path], dest: Path) -> None:
    lines = []
    for p in paths:
        u = p.resolve().as_posix().replace("'", r"'\''")
        lines.append(f"file '{u}'")
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")


def concat_mux(concat_txt: Path, dest: Path) -> None:
    run_ff(
        [
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_txt),
            "-i",
            str(ROUGH),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-shortest",
            str(dest),
        ]
    )


def mix(src: Path, dest: Path) -> None:
    start_lin = 10 ** (START_DB / 20)
    body_lin = 10 ** (BODY_DB / 20)
    vol = (
        f"[1:a]volume=if(lt(t\\,{START_S:.1f})\\,{start_lin:.6f}\\,{body_lin:.6f}):eval=frame[m];"
        f"[0:a][m]amix=inputs=2:duration=first:normalize=0[a]"
    )
    run_ff(
        [
            "-i",
            str(src),
            "-stream_loop",
            "-1",
            "-i",
            str(MUSIC),
            "-filter_complex",
            vol,
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
    mode = sys.argv[1] if len(sys.argv) > 1 else "inicio"
    beats = json.loads(BEATS_PATH.read_text(encoding="utf-8"))
    until = 180.0 if mode == "inicio" else OUR_END + 1
    head = CLIP_DIR / "0000_head.mp4"
    if not head.exists():
        raise FileNotFoundError(head)
    paths = [head]
    n = sum(1 for b in beats if b["start"] < until)
    for i, beat in enumerate(beats, start=1):
        if beat["start"] >= until:
            break
        dest = CLIP_DIR / f"{i:04d}_{beat['kind']}.mp4"
        print(f"[{i}/{n}] {beat['kind']} {beat['start']:.1f}-{beat['end']:.1f}", flush=True)
        mark = dest.with_suffix(".nocap")
        if mark.exists() and dest.exists() and dest.stat().st_size > 1000:
            print("  skip", dest.name, flush=True)
        elif beat["kind"] == "white":
            if dest.exists() and dest.stat().st_size > 1000:
                hide_white_caption(dest)
            else:
                raise FileNotFoundError(dest)
            mark.write_text("ok", encoding="ascii")
        else:
            encode_scene_plain(beat, dest)
            mark.write_text("ok", encoding="ascii")
        paths.append(dest)

    tag = "inicio" if mode == "inicio" else "full"
    concat_txt = WORK / f"concat_gfx_{tag}.txt"
    write_concat(paths, concat_txt)
    pic = PREV / ("05-nocap-inicio.mp4" if mode == "inicio" else "05-nocap-pass.mp4")
    print("concat...", flush=True)
    concat_mux(concat_txt, pic)
    mixed = PREV / ("05-music-inicio.mp4" if mode == "inicio" else "05-music-pass.mp4")
    print("mix...", flush=True)
    mix(pic, mixed)
    print("done", mixed)


if __name__ == "__main__":
    main()
