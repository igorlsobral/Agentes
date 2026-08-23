"""VSL clone 1st graphics pass: cenas full-frame + white impact phrases from 0:48."""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FFMPEG = Path(r"C:\Users\ig\tools\ffmpeg\bin\ffmpeg.exe")
FFPROBE = Path(r"C:\Users\ig\tools\ffmpeg\bin\ffprobe.exe")
ROOT = Path(r"C:\Users\ig\Documents\Agentes")
PROJ = ROOT / "projects" / "vsl-prosperidade"
WORK = PROJ / "work"
ROUGH = PROJ / "previews" / "rough-cut.mp4"
OUT_DIR = PROJ / "previews"
BEATS_PATH = WORK / "beats.json"
WHITE_JSON = WORK / "ref_study" / "white_ranges.json"
SEG_PATH = WORK / "segments_body.json"
FONT_HV = ROOT / "brand" / "Coolvetica Hv Comp.otf"
FONT_RG = ROOT / "brand" / "Coolvetica Rg.otf"
W, H = 1080, 1920
FPS = 60
OUR0 = 48.258
REF0 = 50.0
REF_END = 1637.39
OUR_END = 1908.487
SCALE = (OUR_END - OUR0) / (REF_END - REF0)

def _cena(*parts: str) -> Path:
    return ROOT.joinpath("cenas", *parts)


CENAS = {
    "biblia-ler-rezar": _cena("pixabay", "biblia", "biblia-ler-rezar.mp4"),
    "biblia-luz": _cena("pixabay", "biblia", "biblia-luz.mp4"),
    "biblia-vela": _cena("pixabay", "biblia", "biblia-vela.mp4"),
    "livro-vela": _cena("pixabay", "biblia", "livro-vela.mp4"),
    "culto-cruz": _cena("pixabay", "igreja", "culto-cruz.mp4"),
    "culto-oracao": _cena("pixabay", "igreja", "culto-oracao.mp4"),
    "cruz-oracao": _cena("pixabay", "igreja", "cruz-oracao.mp4"),
    "catedral-vitral": _cena("pixabay", "igreja", "catedral-vitral.mp4"),
    "igreja-arquitetura": _cena("pixabay", "igreja", "igreja-arquitetura.mp4"),
    "mosteiro-colina": _cena("pixabay", "igreja", "mosteiro-colina.mp4"),
    "deserto-biblico": _cena("pixabay", "terra-santa", "deserto-biblico.mp4"),
    "israel-paisagem": _cena("pixabay", "terra-santa", "israel-paisagem.mp4"),
    "qumran-montanhas": _cena("pixabay", "terra-santa", "qumran-montanhas.mp4"),
    "caverna-mar-morto": _cena("pixabay", "terra-santa", "caverna-mar-morto.mp4"),
    "familia-jantar": _cena("pexels", "familia", "familia-jantar.mp4"),
    "casamento-montanha": _cena("pexels", "familia", "casamento-montanha.mp4"),
    "casamento-noivos": _cena("pexels", "familia", "casamento-noivos.mp4"),
    "casal-chave": _cena("pexels", "familia", "casal-chave.mp4"),
    "montanha-por-do-sol": _cena("pexels", "paisagem", "montanha-por-do-sol.mp4"),
    "padre-livros": _cena("pexels", "padre", "padre-livros.mp4"),
    "rua-pedra-oriente": _cena("pexels", "cidade", "rua-pedra-oriente.mp4"),
    "beco-cidade-velha": _cena("pexels", "cidade", "beco-cidade-velha.mp4"),
    "manuscrito-vela": _cena("pexels", "manuscritos", "manuscrito-vela.mp4"),
    "tora-hebraico": _cena("pexels", "manuscritos", "tora-hebraico.mp4"),
    "cartao-celular": _cena("pexels", "dinheiro", "cartao-celular.mp4"),
    "pagamento-cartao": _cena("pexels", "dinheiro", "pagamento-cartao.mp4"),
    "moedas-ouro": _cena("pexels", "dinheiro", "moedas-ouro.mp4"),
    "crianca-moedas": _cena("pexels", "dinheiro", "crianca-moedas.mp4"),
    "telefone-toca": _cena("pexels", "vida", "telefone-toca.mp4"),
    "hotel-saguao": _cena("pexels", "viagem", "hotel-saguao.mp4"),
    "aviao-janela": _cena("pexels", "viagem", "aviao-janela.mp4"),
    "aviao-asa": _cena("pexels", "viagem", "aviao-asa.mp4"),
    "mercedes-rampa": _cena("pexels", "vida", "mercedes-rampa.mp4"),
    "roma-interior": _cena("pexels", "cidade", "roma-interior.mp4"),
}

RULES = [
    (["qumran", "1947", "archeologues", "archeologue"], "qumran-montanhas"),
    (["grotte", "grottes", "caverne"], "caverna-mar-morto"),
    (["2 000 ans", "2000 ans", "cachee"], "caverna-mar-morto"),
    (["jerusalem", "vieille ville"], "rua-pedra-oriente"),
    (["desert"], "deserto-biblico"),
    (["israel", "terre sainte"], "israel-paisagem"),
    (["cathedrale", "vitrail", "marbre"], "catedral-vitral"),
    (["monastere", "moines", "moine"], "mosteiro-colina"),
    (["eglise", "couloir"], "igreja-arquitetura"),
    (["pere marcus", "pretre", "sacerdoce", "bibliothecaire"], "padre-livros"),
    (["manuscrit", "rouleau", "rouleaux", "tomes", "textes anciens"], "manuscrito-vela"),
    (["arameen", "hebreu", "torah", "nouveau testament"], "tora-hebraico"),
    (["constantin", "vatican", "templiers", "medicis", "renaissance", "rome", "colisee"], "igreja-arquitetura"),
    (["bible", "verset", "traduction", "traducteur"], "biblia-ler-rezar"),
    (["jesus", "disciples", "saints", "sains", "prophetes"], "culto-cruz"),
    (["croix", "crucifix"], "cruz-oracao"),
    (["cartes refusees", "carte refusee", "refusee", "dette", "dettes"], "cartao-celular"),
    (["payer", "paiement", "addition", "euros", "26,90"], "pagamento-cartao"),
    (["or", "richesse", "tresor", "banque"], "moedas-ouro"),
    (["pieces", "collection", "grand-pere"], "crianca-moedas"),
    (["telephone", "telephone", "patron", "sonne", "7 h"], "telefone-toca"),
    (["hotel", "check-in", "check in"], "hotel-saguao"),
    (["avion", "vole", "vole", "voyage a"], "aviao-janela"),
    (["mercedes", "voiture", "garage"], "mercedes-rampa"),
    (["cle", "porte", "verrou"], "casal-chave"),
    (["diner", "pizza", "cartable", "ecole"], "familia-jantar"),
    (["enfants", "fille", "fils", "famille"], "familia-jantar"),
    (["epouse", "mariage", "marient", "ame soeur", "ma femme", "amour"], "casamento-noivos"),
    (["montagne de dettes"], "cartao-celular"),
    (["montagne", "provence", "vacances"], "casamento-montanha"),
    (["coucher", "soleil"], "montanha-por-do-sol"),
    (["ruelle", "section interdite"], "beco-cidade-velha"),
    (["livre", "guide", "journal"], "livro-vela"),
    (["bougie"], "biblia-vela"),
    (["priere", "reciter"], "biblia-luz"),
]

# priority, display, tokens (as spoken / WhisperX)
PHRASES = [
    (9, "Sur Commande", ["sur", "commande"]),
    (9, "Prière Complète", ["priere", "complete"]),
    (9, "2 000 Ans", ["2", "000", "ans"]),
    (9, "3 Minutes", ["3", "minutes"]),
    (9, "26,90 Euros", ["26,90"]),
    (9, "26,90 Euros", ["26", "90"]),
    (8, "Cartes Refusées", ["cartes", "refusees"]),
    (8, "Paiement Unique", ["paiement", "unique"]),
    (8, "90 Jours", ["90", "jours"]),
    (8, "Vie Nouvelle", ["vie", "nouvelle"]),
    (7, "Pierre Martin", ["pierre", "martin"]),
    (7, "Père Marcus", ["pere", "marcus"]),
    (7, "Ce Soir", ["ce", "soir"]),
    (6, "71 Pays", ["71", "pays"]),
    (6, "24 744", ["24", "744"]),
    (6, "24 744", ["24.744"]),
    (5, "Bénédictions", ["benedictions"]),
    (5, "Abondance", ["abondance"]),
    (5, "Guérison", ["guerison"]),
    (4, "Araméen", ["arameen"]),
    (3, "Miracles", ["miracles"]),
    (3, "Jésus", ["jesus"]),
    (3, "Vite", ["vite"]),
    (3, "Bouton", ["bouton"]),
    (2, "Prière Perdue", ["priere", "perdue"]),
]

STOP = {
    "le", "la", "les", "de", "des", "du", "un", "une", "et", "ou", "a", "à", "au",
    "aux", "en", "dans", "pour", "par", "avec", "que", "qui", "ce", "cette", "ces",
    "il", "elle", "ils", "vous", "je", "on", "est", "sont", "ont", "ne", "pas",
    "plus", "tres", "comme", "mais", "donc", "alors", "si", "votre", "vos", "mon",
    "ma", "mes", "leur", "leurs", "y", "se", "d", "l", "n", "s", "c", "qu", "the",
    "of", "to", "and", "ca", "ça", "ont", "été", "ete",
}

FALLBACKS = [
    "biblia-vela",
    "igreja-arquitetura",
    "montanha-por-do-sol",
    "catedral-vitral",
    "manuscrito-vela",
    "culto-oracao",
    "israel-paisagem",
    "padre-livros",
    "livro-vela",
    "mosteiro-colina",
    "moedas-ouro",
    "hotel-saguao",
    "aviao-janela",
    "casal-chave",
]


def fold(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def probe_dur(path: Path) -> float:
    r = subprocess.run(
        [str(FFPROBE), "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    return float(r.stdout.strip())


def load_segments() -> list[dict]:
    return json.loads(SEG_PATH.read_text(encoding="utf-8"))


def texts_at(segments: list[dict], t0: float, t1: float) -> str:
    bits = []
    for s in segments:
        if s["end"] <= t0 or s["start"] >= t1:
            continue
        bits.append(s["text"])
    return " ".join(bits)


def load_words() -> list[dict]:
    data = json.loads((PROJ / "transcript.json").read_text(encoding="utf-8"))
    out = []
    for s in data["segments"]:
        for w in s.get("words", []):
            t0 = float(w.get("start", 0))
            if t0 < OUR0 - 0.2:
                continue
            raw = w["word"].strip()
            key = re.sub(r"[^\wÀ-ÿ]+", "", raw, flags=re.UNICODE)
            if not key:
                continue
            out.append({"w": raw.strip(" ,.;:!?"), "f": fold(key), "s": t0, "e": float(w["end"])})
    out.sort(key=lambda x: x["s"])
    return out


def find_phrase_hits(words: list[dict]) -> list[dict]:
    hits = []
    folded = [w["f"] for w in words]
    for prio, display, tokens in PHRASES:
        tok = [fold(re.sub(r"[^\wÀ-ÿ]+", "", t, flags=re.UNICODE)) for t in tokens]
        n = len(tok)
        i = 0
        while i <= len(folded) - n:
            if folded[i : i + n] == tok:
                a = words[i]["s"]
                b = words[i + n - 1]["e"]
                hits.append({"start": a, "end": b, "headline": display, "n": n, "prio": prio})
                i += n
            else:
                i += 1
    hits.sort(key=lambda h: (-h["prio"], -h["n"], h["start"]))
    chosen = []
    for h in hits:
        if any(abs(h["start"] - c["start"]) < 6.5 for c in chosen):
            continue
        dur = max(1.35, min(3.2, (h["end"] - h["start"]) + 0.45))
        chosen.append(
            {
                "start": round(h["start"], 3),
                "end": round(min(OUR_END, h["start"] + dur), 3),
                "headline": h["headline"],
            }
        )
    chosen.sort(key=lambda h: h["start"])
    return chosen


def caption_at(words: list[dict], t0: float, t1: float) -> str:
    bits = [w["w"] for w in words if t0 - 0.05 <= w["s"] < t1]
    if not bits:
        return ""
    return " ".join(bits[:8]).strip(" ,.")


def title_words(s: str) -> str:
    parts = s.split()
    out = []
    for i, p in enumerate(parts):
        if i > 0 and fold(p) in STOP:
            out.append(p.lower())
        else:
            out.append(p[:1].upper() + p[1:] if p else p)
    return " ".join(out)


def pick_caption(text: str) -> str:
    words = re.findall(r"[A-Za-zÀ-ÿ0-9’',.]+", text)
    if not words:
        return ""
    chunk = words[:8] if len(words) <= 10 else words[:7]
    return " ".join(chunk).strip(" ,.")


def has_key(hay: str, needle: str) -> bool:
    h = fold(hay)
    n = fold(needle)
    if " " in n:
        return n in h
    return re.search(r"\b" + re.escape(n) + r"\b", h) is not None


def pick_scene(text: str, last: str | None, recent: list[str], idx: int) -> str:
    for keys, name in RULES:
        if name not in CENAS or not CENAS[name].exists():
            continue
        if any(has_key(text, k) for k in keys):
            if name != last and name not in recent[-2:]:
                return name
    for name in FALLBACKS:
        if name not in CENAS or not CENAS[name].exists():
            continue
        if name != last and name not in recent[-3:]:
            return name
    alive = [n for n in FALLBACKS if n in CENAS and CENAS[n].exists()]
    return alive[idx % len(alive)] if alive else "biblia-luz"


def build_beats() -> list[dict]:
    words = load_words()
    segments = load_segments()
    whites = find_phrase_hits(words)
    cursor = OUR0
    beats: list[dict] = []
    last_scene = None
    recent: list[str] = []
    scene_i = 0

    def add_scenes(t0: float, t1: float) -> None:
        nonlocal last_scene, scene_i, cursor
        t = t0
        while t1 - t > 0.35:
            remaining = t1 - t
            dur = 8.0 if remaining > 12 else remaining
            if remaining > 12 and remaining < 16:
                dur = remaining / 2
            t2 = min(t1, t + dur)
            txt = texts_at(segments, t, t2) or caption_at(words, t, t2)
            scene = pick_scene(txt, last_scene, recent, scene_i)
            last_scene = scene
            recent.append(scene)
            scene_i += 1
            beats.append(
                {
                    "kind": "scene",
                    "start": round(t, 3),
                    "end": round(t2, 3),
                    "scene": scene,
                    "path": str(CENAS[scene]),
                    "caption": caption_at(words, t, t2) or pick_caption(txt),
                    "headline": "",
                }
            )
            t = t2
        cursor = t1

    for w in whites:
        a, b = w["start"], w["end"]
        if a < OUR0:
            continue
        if a > cursor + 0.25:
            add_scenes(cursor, a)
        elif a < cursor:
            continue
        beats.append(
            {
                "kind": "white",
                "start": round(a, 3),
                "end": round(b, 3),
                "scene": "",
                "path": "",
                "caption": caption_at(words, a, b),
                "headline": w["headline"],
            }
        )
        cursor = b
        last_scene = None
    if cursor < OUR_END - 0.2:
        add_scenes(cursor, OUR_END)
    return beats


def wrap_words(text: str, n: int) -> list[str]:
    words = text.split()
    if not words:
        return []
    if len(words) <= n:
        return words
    # 3 lines max, pack evenly
    lines, row = [], []
    per = max(1, round(len(words) / n))
    for w in words:
        row.append(w)
        if len(row) >= per and len(lines) < n - 1:
            lines.append(" ".join(row))
            row = []
    if row:
        lines.append(" ".join(row))
    return lines[:n]


def draw_white(headline: str, caption: str, dest: Path) -> None:
    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    lines = wrap_words(headline, 3) or [headline]
    size = 168 if max(len(x) for x in lines) < 12 else 132
    if max(len(x) for x in lines) > 16:
        size = 108
    font = ImageFont.truetype(str(FONT_HV), size)
    heights = []
    widths = []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        widths.append(bbox[2] - bbox[0])
        heights.append(bbox[3] - bbox[1])
    gap = 28
    total_h = sum(heights) + gap * (len(lines) - 1)
    y = (H * 0.42) - total_h / 2
    for line, tw, th in zip(lines, widths, heights):
        x = (W - tw) / 2
        draw.text((x, y), line, font=font, fill=(8, 8, 10))
        y += th + gap
    if caption:
        cap_font = ImageFont.truetype(str(FONT_RG), 42)
        cap = caption[:42]
        bbox = draw.textbbox((0, 0), cap, font=cap_font)
        cw, ch = bbox[2] - bbox[0], bbox[3] - bbox[1]
        pad_x, pad_y = 36, 18
        bw, bh = cw + pad_x * 2, ch + pad_y * 2
        bx = (W - bw) / 2
        by = H - 280
        draw.rounded_rectangle((bx, by, bx + bw, by + bh), radius=14, fill=(48, 48, 52))
        draw.text((bx + pad_x, by + pad_y - 4), cap, font=cap_font, fill=(255, 255, 255))
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, "PNG")


def draw_caption_png(caption: str, dest: Path) -> None:
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if not caption:
        img.save(dest, "PNG")
        return
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(str(FONT_RG), 44)
    # two lines if long
    words = caption.split()
    if len(caption) > 28 and len(words) > 3:
        mid = max(1, len(words) // 2)
        lines = [" ".join(words[:mid]), " ".join(words[mid:])]
    else:
        lines = [caption]
    font_h = 44
    pad_x, pad_y = 34, 16
    widths, heights = [], []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        widths.append(bbox[2] - bbox[0])
        heights.append(bbox[3] - bbox[1])
    bw = max(widths) + pad_x * 2
    bh = sum(heights) + 10 * (len(lines) - 1) + pad_y * 2
    bx = (W - bw) / 2
    by = H - 260
    draw.rounded_rectangle((bx, by, bx + bw, by + bh), radius=12, fill=(0, 0, 0, 200))
    y = by + pad_y - 2
    for line, tw, th in zip(lines, widths, heights):
        x = bx + (bw - tw) / 2
        draw.text((x, y), line, font=font, fill=(255, 255, 255, 255))
        y += th + 10
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, "PNG")


def run_ff(args: list[str]) -> None:
    r = subprocess.run([str(FFMPEG), "-hide_banner", "-loglevel", "error", "-y", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-2000:] if r.stderr else "ffmpeg failed")


def encode_head(dest: Path, dur: float) -> None:
    if dest.exists() and dest.stat().st_size > 1000:
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    run_ff(
        [
            "-i",
            str(ROUGH),
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


def encode_scene(beat: dict, dest: Path, cap_png: Path) -> None:
    if dest.exists() and dest.stat().st_size > 1000:
        return
    dur = beat["end"] - beat["start"]
    src = beat["path"]
    clip_dur = probe_dur(Path(src))
    loops = max(1, int(dur // max(clip_dur, 0.5)) + 1)
    vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}"
    dest.parent.mkdir(parents=True, exist_ok=True)
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
            vf,
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


def encode_white(beat: dict, dest: Path, png: Path) -> None:
    if dest.exists() and dest.stat().st_size > 1000:
        return
    dur = beat["end"] - beat["start"]
    dest.parent.mkdir(parents=True, exist_ok=True)
    cache = WORK / "gfx_white_cache"
    cache.mkdir(parents=True, exist_ok=True)
    key = f"{beat['headline'].replace(' ', '_')}_{int(round(dur * 10)):03d}.mp4"
    cached = cache / key
    if cached.exists() and cached.stat().st_size > 1000:
        dest.write_bytes(cached.read_bytes())
        return
    sys.path.insert(0, str(WORK))
    from white_anim import encode_animated_white

    encode_animated_white(beat["headline"], "", dur, cached)
    dest.write_bytes(cached.read_bytes())


def write_concat(paths: list[Path], dest: Path) -> None:
    lines = []
    for p in paths:
        u = p.resolve().as_posix().replace("'", r"'\''")
        lines.append(f"file '{u}'")
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")


def concat_mux(concat_txt: Path, dest: Path, audio_from: Path) -> None:
    run_ff(
        [
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_txt),
            "-i",
            str(audio_from),
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


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else "plan"
    beats = build_beats()
    BEATS_PATH.write_text(json.dumps(beats, ensure_ascii=False, indent=2), encoding="utf-8")
    n_white = sum(1 for b in beats if b["kind"] == "white")
    n_scene = sum(1 for b in beats if b["kind"] == "scene")
    print(f"beats={len(beats)} scenes={n_scene} whites={n_white}")
    for b in beats[:22]:
        extra = b["headline"] or b["scene"]
        print(f"  {b['start']:7.2f}-{b['end']:7.2f}  {b['kind']:5}  {extra}  | {b['caption']}")
    if mode == "plan":
        return

    clip_dir = WORK / "gfx_clips_v2"
    asset_dir = WORK / "gfx_assets_v2"
    only_whites = mode in {"whites", "inicio"}
    clip_dir.mkdir(parents=True, exist_ok=True)
    asset_dir.mkdir(parents=True, exist_ok=True)

    head = clip_dir / "0000_head.mp4"
    old_head = WORK / "gfx_clips" / "0000_head.mp4"
    if not head.exists() and old_head.exists():
        head.parent.mkdir(parents=True, exist_ok=True)
        head.write_bytes(old_head.read_bytes())
    print("encoding testimonials head...", flush=True)
    encode_head(head, OUR0)

    paths = [head]
    until = OUR_END + 1
    if mode == "inicio":
        until = 180.0

    for i, beat in enumerate(beats, start=1):
        if beat["start"] >= until:
            break
        dest = clip_dir / f"{i:04d}_{beat['kind']}.mp4"
        print(f"[{i}/{len(beats)}] {beat['kind']} {beat['start']:.1f}-{beat['end']:.1f}", flush=True)
        if beat["kind"] == "white":
            if only_whites and dest.exists():
                dest.unlink()
            png = asset_dir / f"white_{i:04d}.png"
            encode_white(beat, dest, png)
        else:
            encode_scene(beat, dest, Path())
        paths.append(dest)

    tag = "inicio" if mode == "inicio" else "full"
    concat_txt = WORK / f"concat_gfx_{tag}.txt"
    write_concat(paths, concat_txt)
    dest = OUT_DIR / ("03-graphics-inicio.mp4" if mode == "inicio" else "03-graphics-pass.mp4")
    print(f"concat + audio -> {dest}", flush=True)
    concat_mux(concat_txt, dest, ROUGH)
    print("done", dest, dest.stat().st_size)


if __name__ == "__main__":
    main()
