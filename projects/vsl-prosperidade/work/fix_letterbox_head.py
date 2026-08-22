"""Fill white letterbox bars on landscape testimonials with blurred zoom."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

FFMPEG = Path(r"C:\Users\ig\tools\ffmpeg\bin\ffmpeg.exe")
FFPROBE = Path(r"C:\Users\ig\tools\ffmpeg\bin\ffprobe.exe")
ROOT = Path(r"C:\Users\ig\Documents\Agentes")
PROJ = ROOT / "projects" / "vsl-prosperidade"
WORK = PROJ / "work"
FRONT = WORK / "front"
META = WORK / "front_meta.json"
CLIP_DIR = WORK / "gfx_clips_v2"
OUT_DIR = PROJ / "previews"
ROUGH = OUT_DIR / "rough-cut.mp4"
W, H, FPS = 1080, 1920, 60
CONTENT_Y = 656
CONTENT_H = 608
LANDSCAPE_NAMES = {"FALA_1.mp4", "FALA_2.mp4", "FALA_5.mp4"}


def run_ff(args: list[str]) -> None:
    r = subprocess.run([str(FFMPEG), "-hide_banner", "-loglevel", "error", "-y", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-2000:] if r.stderr else "ffmpeg failed")


def duration(path: Path) -> float:
    return float(
        subprocess.check_output(
            [str(FFPROBE), "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
            text=True,
        ).strip()
    )


def letterbox_vf() -> str:
    # Center stays the 16:9 picture. Top/bottom = same picture, extra zoom + blur.
    return (
        f"[0:v]crop={W}:{CONTENT_H}:0:{CONTENT_Y},split=2[mid][mid2];"
        f"[mid]scale=4436:2496,crop={W}:{H},gblur=sigma=22,eq=brightness=-0.03:saturation=1.05[bg];"
        f"[mid2]setsar=1[fg];"
        f"[bg][fg]overlay=(W-w)/2:(H-h)/2,fps={FPS},format=yuv420p"
    )


def encode_blurred(src: Path, dest: Path, dur: float) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    run_ff(
        [
            "-i",
            str(src),
            "-t",
            f"{dur:.3f}",
            "-an",
            "-filter_complex",
            letterbox_vf(),
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            "-pix_fmt",
            "yuv420p",
            str(dest),
        ]
    )


def encode_plain(src: Path, dest: Path, dur: float) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    run_ff(
        [
            "-i",
            str(src),
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
            str(dest),
        ]
    )


def write_concat(paths: list[Path], dest: Path) -> None:
    lines = []
    for p in paths:
        u = p.resolve().as_posix().replace("'", r"'\''")
        lines.append(f"file '{u}'")
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    items = [x for x in json.loads(META.read_text(encoding="utf-8")) if x["kind"] == "depoimento"]
    if len(items) != 12:
        raise RuntimeError(f"expected 12 depoimentos, got {len(items)}")

    parts_dir = WORK / "head_parts_v3"
    parts_dir.mkdir(parents=True, exist_ok=True)
    parts: list[Path] = []

    for i, item in enumerate(items, start=1):
        src = Path(item["src"])
        dur = float(item["out_duration_s"])
        dest = parts_dir / f"{i:02d}.mp4"
        landscape = src.name in LANDSCAPE_NAMES
        print(f"{src.name}  {dur:.2f}s  {'BLUR' if landscape else 'keep'}", flush=True)
        if landscape:
            encode_blurred(src, dest, dur)
        else:
            encode_plain(src, dest, dur)
        parts.append(dest)

    concat_txt = WORK / "concat_head_v3.txt"
    write_concat(parts, concat_txt)
    head = CLIP_DIR / "0000_head.mp4"
    tmp_head = CLIP_DIR / "0000_head_new.mp4"
    run_ff(["-f", "concat", "-safe", "0", "-i", str(concat_txt), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-an", str(tmp_head)])
    if head.exists():
        head.unlink()
    tmp_head.rename(head)
    print("new head", duration(head), flush=True)

    full_list = (WORK / "concat_gfx_full.txt").read_text(encoding="utf-8").splitlines()
    inicio_list = (WORK / "concat_gfx_inicio.txt").read_text(encoding="utf-8").splitlines()
    write_concat([head] + [Path(line.split("'")[1]) for line in full_list[1:] if line.startswith("file ")], WORK / "concat_gfx_full.txt")
    write_concat([head] + [Path(line.split("'")[1]) for line in inicio_list[1:] if line.startswith("file ")], WORK / "concat_gfx_inicio.txt")

    def mux(concat_path: Path, dest: Path) -> None:
        run_ff(
            [
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                str(concat_path),
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

    dest_full = OUT_DIR / "03-graphics-pass.mp4"
    dest_inicio = OUT_DIR / "03-graphics-inicio.mp4"
    print("concat full...", flush=True)
    mux(WORK / "concat_gfx_full.txt", dest_full)
    print("concat inicio...", flush=True)
    mux(WORK / "concat_gfx_inicio.txt", dest_inicio)
    print("done", dest_inicio, dest_inicio.stat().st_size, dest_full, dest_full.stat().st_size)


if __name__ == "__main__":
    main()
