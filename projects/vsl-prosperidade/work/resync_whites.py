"""Rebuild white-screen clocks onto the first sound of the highlight, then remux."""
from __future__ import annotations

import json
import sys
from pathlib import Path

WORK = Path(r"C:\Users\ig\Documents\Agentes\projects\vsl-prosperidade\work")
sys.path.insert(0, str(WORK))

from compose_graphics import (  # noqa: E402
    OUR_END,
    OUT_DIR,
    ROUGH,
    build_beats,
    encode_scene,
    encode_white,
    probe_dur,
    write_concat,
    concat_mux,
)
from strip_captions_remix import mix  # noqa: E402

CLIP_DIR_V2 = WORK / "gfx_clips_v2"


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else "inicio"
    beats = build_beats()
    (WORK / "beats.json").write_text(json.dumps(beats, ensure_ascii=False, indent=2), encoding="utf-8")
    whites = [b for b in beats if b["kind"] == "white"]
    print(f"beats={len(beats)} whites={len(whites)}")
    for b in whites[:12]:
        print(f"  {b['start']:7.3f}-{b['end']:7.3f}  {b['headline']}")

    until = 180.0 if mode == "inicio" else OUR_END + 1
    head = CLIP_DIR_V2 / "0000_head.mp4"
    if not head.exists():
        raise FileNotFoundError(head)
    paths = [head]
    n = sum(1 for b in beats if b["start"] < until)
    asset_dir = WORK / "gfx_assets_v2"
    asset_dir.mkdir(parents=True, exist_ok=True)

    for i, beat in enumerate(beats, start=1):
        if beat["start"] >= until:
            break
        dest = CLIP_DIR_V2 / f"{i:04d}_{beat['kind']}.mp4"
        print(f"[{i}/{n}] {beat['kind']} {beat['start']:.2f}-{beat['end']:.2f} {beat['headline'] or beat['scene']}", flush=True)
        if beat["kind"] == "white":
            if dest.exists():
                dest.unlink()
            encode_white(beat, dest, asset_dir / f"white_{i:04d}.png")
        else:
            encode_scene(beat, dest, Path())
        paths.append(dest)

    tag = "inicio" if mode == "inicio" else "full"
    concat_txt = WORK / f"concat_gfx_{tag}.txt"
    write_concat(paths, concat_txt)
    pic = OUT_DIR / ("07-whites-inicio.mp4" if mode == "inicio" else "07-whites-pass.mp4")
    print("concat...", flush=True)
    concat_mux(concat_txt, pic, ROUGH)
    mixed = OUT_DIR / ("07-whites-music-inicio.mp4" if mode == "inicio" else "07-whites-music-pass.mp4")
    print("mix...", flush=True)
    mix(pic, mixed)
    print("done", mixed, "dur", probe_dur(mixed))


if __name__ == "__main__":
    main()
