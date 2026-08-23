"""Animated white impact screens — Coolvetica Rg + first-test motion (ease, icon, stagger)."""
from __future__ import annotations

import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FFMPEG = Path(r"C:\Users\ig\tools\ffmpeg\bin\ffmpeg.exe")
FONT_RG = Path(r"C:\Users\ig\Documents\Agentes\brand\Coolvetica Rg.otf")
W, H = 1080, 1920
FPS = 60
ACCENT = (124, 139, 205)
INK = (17, 19, 24)


def ease_out(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return 1.0 - (1.0 - t) ** 3


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def kind_for(headline: str) -> str:
    h = headline.lower()
    if "000" in h or "ans" in h:
        return "years"
    if "commande" in h:
        return "check"
    if "minute" in h:
        return "clock"
    if "vite" in h:
        return "gauge"
    if "744" in h or headline.replace(" ", "").isdigit():
        return "count"
    if "carte" in h or "refus" in h:
        return "card"
    if "abondance" in h or "26" in h or "euro" in h or "paiement" in h:
        return "coins"
    if "bénédict" in h or "benedict" in h:
        return "steps"
    if "guérison" in h or "guerison" in h:
        return "heart"
    if "jésus" in h or "jesus" in h:
        return "cross"
    if "marcus" in h:
        return "book"
    if "prière" in h or "priere" in h:
        return "book"
    if "aram" in h:
        return "scroll"
    if "soir" in h:
        return "moon"
    if "vie" in h or "nouvelle" in h:
        return "steps"
    if "pays" in h:
        return "globe"
    if "jour" in h:
        return "check"
    if "bouton" in h:
        return "button"
    if "pierre" in h:
        return "name"
    if "miracle" in h:
        return "spark"
    return "spark"


def wrap_lines(text: str) -> list[str]:
    words = text.split()
    if len(words) <= 2:
        return words
    if len(text) <= 14:
        return [text]
    mid = max(1, math.ceil(len(words) / 2))
    return [" ".join(words[:mid]), " ".join(words[mid:])]


def draw_icon(draw: ImageDraw.ImageDraw, kind: str, cx: int, cy: int, s: float, t: float) -> None:
    r = int(78 * s)
    # soft disc like the first-test icon tile
    box = (cx - r - 28, cy - r - 28, cx + r + 28, cy + r + 28)
    draw.rounded_rectangle(box, radius=36, fill=(ACCENT[0], ACCENT[1], ACCENT[2], 255))

    def w(x: float, y: float) -> tuple[int, int]:
        return int(cx + x * s), int(cy + y * s)

    col = (255, 255, 255, 255)
    if kind == "clock":
        draw.ellipse((cx - r + 8, cy - r + 8, cx + r - 8, cy + r - 8), outline=col, width=7)
        ang = -90 + 240 * ease_out(t)
        rad = math.radians(ang)
        x2 = cx + int(math.cos(rad) * (r - 28))
        y2 = cy + int(math.sin(rad) * (r - 28))
        draw.line((cx, cy, x2, y2), fill=col, width=7)
        draw.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), fill=col)
    elif kind == "gauge":
        draw.arc((cx - r + 6, cy - r + 18, cx + r - 6, cy + r + 10), 200, 340, fill=col, width=12)
        ang = 200 + 140 * ease_out(t)
        rad = math.radians(ang)
        x2 = cx + int(math.cos(rad) * (r - 22))
        y2 = cy + int(math.sin(rad) * (r - 22))
        draw.line((cx, cy + 16, x2, y2), fill=col, width=8)
        draw.ellipse((cx - 9, cy + 7, cx + 9, cy + 25), fill=INK)
    elif kind == "check":
        draw.line((cx - 36 * s, cy + 4 * s, cx - 8 * s, cy + 32 * s), fill=col, width=10)
        draw.line((cx - 8 * s, cy + 32 * s, cx + 40 * s, cy - 28 * s), fill=col, width=10)
    elif kind == "card":
        draw.rounded_rectangle((cx - 50 * s, cy - 34 * s, cx + 50 * s, cy + 34 * s), radius=12, outline=col, width=7)
        draw.line((cx - 28 * s, cy - 16 * s, cx + 28 * s, cy + 16 * s), fill=col, width=8)
        draw.line((cx + 28 * s, cy - 16 * s, cx - 28 * s, cy + 16 * s), fill=col, width=8)
    elif kind == "coins":
        for i, off in enumerate(((-22, 10), (18, -8), (0, 22))):
            grow = ease_out(max(0.0, t - i * 0.12))
            rr = 22 * s * (0.4 + 0.6 * grow)
            ox, oy = off
            draw.ellipse((cx + ox * s - rr, cy + oy * s - rr, cx + ox * s + rr, cy + oy * s + rr), outline=col, width=6)
    elif kind == "steps":
        h1 = 18 + 28 * ease_out(t)
        h2 = 18 + 48 * ease_out(max(0.0, t - 0.1))
        h3 = 18 + 70 * ease_out(max(0.0, t - 0.2))
        base = cy + 36 * s
        for i, hh in enumerate((h1, h2, h3)):
            x0 = cx - 52 * s + i * 36 * s
            draw.rounded_rectangle((x0, base - hh * s, x0 + 28 * s, base), radius=6, fill=col)
    elif kind == "heart":
        draw.ellipse((cx - 38 * s, cy - 28 * s, cx - 2 * s, cy + 8 * s), fill=col)
        draw.ellipse((cx + 2 * s, cy - 28 * s, cx + 38 * s, cy + 8 * s), fill=col)
        draw.polygon([(cx - 40 * s, cy - 4 * s), (cx + 40 * s, cy - 4 * s), (cx, cy + 42 * s)], fill=col)
    elif kind == "cross":
        draw.rounded_rectangle((cx - 10 * s, cy - 44 * s, cx + 10 * s, cy + 44 * s), radius=6, fill=col)
        draw.rounded_rectangle((cx - 32 * s, cy - 18 * s, cx + 32 * s, cy + 2 * s), radius=6, fill=col)
    elif kind == "book":
        draw.rounded_rectangle((cx - 42 * s, cy - 32 * s, cx + 42 * s, cy + 32 * s), radius=8, outline=col, width=6)
        draw.line((cx, cy - 28 * s, cx, cy + 28 * s), fill=col, width=5)
        draw.line((cx - 28 * s, cy - 10 * s, cx - 10 * s, cy - 10 * s), fill=col, width=5)
        draw.line((cx + 10 * s, cy - 10 * s, cx + 28 * s, cy - 10 * s), fill=col, width=5)
    elif kind == "scroll":
        draw.rounded_rectangle((cx - 36 * s, cy - 40 * s, cx + 36 * s, cy + 40 * s), radius=10, outline=col, width=6)
        for yy in (-16, 0, 16):
            draw.line((cx - 20 * s, cy + yy * s, cx + 20 * s, cy + yy * s), fill=col, width=5)
    elif kind == "moon":
        draw.ellipse((cx - 36 * s, cy - 36 * s, cx + 36 * s, cy + 36 * s), fill=col)
        draw.ellipse((cx - 12 * s, cy - 36 * s, cx + 44 * s, cy + 28 * s), fill=ACCENT)
    elif kind == "globe":
        draw.ellipse((cx - r + 10, cy - r + 10, cx + r - 10, cy + r - 10), outline=col, width=7)
        draw.ellipse((cx - 18 * s, cy - r + 10, cx + 18 * s, cy + r - 10), outline=col, width=5)
        draw.arc((cx - r + 10, cy - 16 * s, cx + r - 10, cy + 16 * s), 0, 360, fill=col, width=5)
    elif kind == "button":
        draw.rounded_rectangle((cx - 54 * s, cy - 22 * s, cx + 54 * s, cy + 22 * s), radius=24, fill=col)
        draw.ellipse((cx + 28 * s, cy - 8 * s, cx + 44 * s, cy + 8 * s), fill=ACCENT)
    elif kind == "name":
        draw.rounded_rectangle((cx - 48 * s, cy - 28 * s, cx + 48 * s, cy + 28 * s), radius=14, outline=col, width=6)
        draw.ellipse((cx - 14 * s, cy - 16 * s, cx + 14 * s, cy + 4 * s), outline=col, width=5)
        draw.arc((cx - 26 * s, cy + 6 * s, cx + 26 * s, cy + 28 * s), 200, 340, fill=col, width=5)
    elif kind == "years":
        draw.ellipse((cx - r + 4, cy - r + 4, cx + r - 4, cy + r - 4), outline=col, width=7)
        draw.ellipse((cx - r + 22, cy - r + 22, cx + r - 22, cy + r - 22), outline=col, width=5)
        draw.line((cx, cy - 20 * s, cx, cy + 8 * s), fill=col, width=6)
        draw.ellipse((cx - 6, cy + 16 * s, cx + 6, cy + 28 * s), fill=col)
    elif kind == "count":
        draw.rounded_rectangle((cx - 46 * s, cy - 28 * s, cx + 46 * s, cy + 28 * s), radius=12, outline=col, width=6)
        draw.line((cx - 28 * s, cy, cx + 28 * s, cy), fill=col, width=6)
    else:  # spark
        for ang in range(0, 360, 45):
            rad = math.radians(ang)
            x1 = cx + int(math.cos(rad) * 16 * s)
            y1 = cy + int(math.sin(rad) * 16 * s)
            x2 = cx + int(math.cos(rad) * 48 * s)
            y2 = cy + int(math.sin(rad) * 48 * s)
            draw.line((x1, y1, x2, y2), fill=col, width=7)
        draw.ellipse((cx - 14 * s, cy - 14 * s, cx + 14 * s, cy + 14 * s), fill=col)


def render_frame(headline: str, caption: str, t: float, dur: float) -> Image.Image:
    # Clip starts on the first sound of the highlight word.
    # Keep the fade-to-white and the word motion — do not flatten.
    fade = ease_out(min(1.0, t / 0.22))
    bg = tuple(int(lerp(216, 255, fade)) for _ in range(3))
    img = Image.new("RGBA", (W, H), bg + (255,))
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    kind = kind_for(headline)
    icon_t = ease_out((t - 0.10) / 0.38)
    icon_s = lerp(0.58, 1.0, icon_t)
    icon_a = int(255 * icon_t)
    icon_y = int(lerp(620, 560, icon_t))
    if icon_a > 0:
        tile = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        td = ImageDraw.Draw(tile)
        draw_icon(td, kind, W // 2, icon_y, icon_s, icon_t)
        tile.putalpha(tile.split()[-1].point(lambda p: int(p * icon_a / 255)))
        layer = Image.alpha_composite(layer, tile)
        draw = ImageDraw.Draw(layer)

    lines = wrap_lines(headline)
    # count-up for big numbers
    shown = list(lines)
    if kind == "count" and headline.replace(" ", "").replace(",", "").isdigit():
        target = int(headline.replace(" ", "").replace(",", ""))
        n = int(target * ease_out((t - 0.28) / 0.55))
        shown = [f"{n:,}".replace(",", " ")]

    size = 168 if max(len(x) for x in shown) < 12 else 140
    if max(len(x) for x in shown) > 16:
        size = 118
    font = ImageFont.truetype(str(FONT_RG), size)
    gap = 18
    heights, widths = [], []
    for line in shown:
        bbox = draw.textbbox((0, 0), line, font=font)
        widths.append(bbox[2] - bbox[0])
        heights.append(bbox[3] - bbox[1])
    total_h = sum(heights) + gap * (len(shown) - 1)
    y0 = 860
    for i, (line, tw, th) in enumerate(zip(shown, widths, heights)):
        lt = ease_out((t - 0.26 - i * 0.08) / 0.36)
        if lt <= 0:
            y0 += th + gap
            continue
        x = (W - tw) / 2
        y = y0 + lerp(36, 0, lt)
        a = int(255 * lt)
        # soft shadow
        draw.text((x + 3, y + 4), line, font=font, fill=(17, 19, 24, int(40 * lt)))
        draw.text((x, y), line, font=font, fill=INK + (a,))
        y0 += th + gap

    if caption:
        cap_t = ease_out((t - 0.42) / 0.28)
        if cap_t > 0:
            cap_font = ImageFont.truetype(str(FONT_RG), 40)
            cap = caption[:40]
            bbox = draw.textbbox((0, 0), cap, font=cap_font)
            cw, ch = bbox[2] - bbox[0], bbox[3] - bbox[1]
            pad_x, pad_y = 34, 16
            bw, bh = cw + pad_x * 2, ch + pad_y * 2
            bx = (W - bw) / 2
            by = H - 270 + lerp(24, 0, cap_t)
            a = int(200 * cap_t)
            draw.rounded_rectangle((bx, by, bx + bw, by + bh), radius=16, fill=(17, 19, 24, a))
            draw.text((bx + pad_x, by + pad_y - 3), cap, font=cap_font, fill=(255, 255, 255, int(255 * cap_t)))

    return Image.alpha_composite(img, layer).convert("RGB")


def encode_animated_white(headline: str, caption: str, dur: float, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    n = max(8, int(round(dur * FPS)))
    cmd = [
        str(FFMPEG),
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-f",
        "rawvideo",
        "-pix_fmt",
        "rgb24",
        "-s",
        f"{W}x{H}",
        "-r",
        str(FPS),
        "-i",
        "-",
        "-an",
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "19",
        "-pix_fmt",
        "yuv420p",
        str(dest),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    assert proc.stdin is not None
    for i in range(n):
        t = i / FPS
        frame = render_frame(headline, caption, t, dur)
        proc.stdin.write(frame.tobytes())
    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError(f"ffmpeg failed for {dest}")
