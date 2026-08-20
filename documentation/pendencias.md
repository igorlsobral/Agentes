# Pendências — o que só Igor pode informar

**Role:** Lista explícita de lacunas. O agente não preenche estas linhas por palpite.

**Parent:** [documentation/README.md](README.md)

Atualizado em 2026-08-20. Quando Igor responder um item, mover para **Resolvidas** (com a decisão) e atualizar o arquivo canônico correspondente.

## Bloqueiam ferramenta (pipeline não roda de ponta a ponta)

| ID | O que falta | Por que importa | Onde vai entrar |
|---|---|---|---|
| P4 | Arquivo da fonte **Coolvetica** | Captions short-form | `brand/` |
| P5 | Um bruto real de teste (`.mp4` ou `.mov`) | Definition of done de mídia | `raw/` |

## Bloqueiam qualidade / identidade

| ID | O que falta | Por que importa | Onde vai entrar |
|---|---|---|---|
| P6 | Brand kit: cores (incl. “cor Claude” se for uso real), tipografia, logo, mascote PNG | `brand/` manda; agente não improvisa identidade | `brand/README.md` + `brand/assets/` |
| P7 | Agressividade padrão do rough cut (quanto silêncio corta, quanto “respira”) | Intake pergunta se faltar; sem default o agente para no 1º clip sem preset de corte | `presets/` ou `video-editor/AGENTS.md` |
| P8 | Preset padrão quando Igor **não** diz o formato | Gráficos não começam sem formato | `presets/README.md` |
| P9 | Política de gasto: quais APIs pagas existem (B-roll, TTS, Veo, outras), teto, quando “ok” vale | Standing restriction já proíbe gastar sem ok; falta o catálogo | `documentation/services/pipeline.md` |

## Operação do repo

| ID | O que falta | Por que importa | Onde vai entrar |
|---|---|---|---|
| P10 | Allowlist extra: outros clones, pastas de `raw/`/`music/` fora daqui, wiki | Grep só allowlist | `documentation/services/pipeline.md` |
| P12 | Idioma dos arquivos estruturais: manteve-se inglês (skills/agents) + português (domínio). Confirmar ou mandar tudo PT | Evitar mix silencioso | `README.md` Language |
| P13 | Contas/canais (YouTube, TikTok, nomes públicos) se o export precisar de metadata | Não inventar títulos/end cards | `documentation/people/igor.md` |
| P14 | Resolução / fps / loudness de master padrão | Export consistente | `presets/` |
| P15 | Pasta Downloads de destino se não for `c:\Users\ig\Downloads\` | Skill de export assume esse path | `skills/export-video.md` |

## Já decidido (não perguntar de novo)

| Decisão | Fonte |
|---|---|
| Humano = **Igor**; único aprovador | Este pedido, 2026-08-19 |
| Domínio = pipeline local bruto → vídeo publicado | Prompt de edição |
| Stack = WhisperX + FFmpeg + HyperFrames + Cursor | Prompt de edição |
| Sem Google Whisk; “Whisk X” = WhisperX | Prompt de edição |
| Música default −23 dB | Prompt de edição |
| Threshold de silêncio relativo ao take, nunca −35 dB fixo | Prompt de edição |
| Rough cut locked antes de gráficos; partial render no second pass | Prompt de edição |
| Aceitar `.mp4` e `.mov`; normalizar mp4 no ingest | Prompt de edição |
| Não apagar projeto no export | Prompt de edição |
| Presets: `short-form-explainer`, `tiktok-raw`, `long-form` | Prompt de edição |
| Paid API só com proposta + ok | Prompt de edição |
| IDE = Cursor | Uso desta sessão |
| Pipeline vive neste folder até P10 dizer o contrário | Inferência explícita por ausência de outros paths; **não** é um clone inventado |
| Git deste repo = commit + push para `origin` depois de mudança significativa; nunca force-push; nunca secrets | Igor, 2026-08-19 |
| FFmpeg upstream = [github.com/FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg); usar **build**, não clonar source neste repo | Igor, 2026-08-20 |
| WhisperX upstream = [github.com/m-bain/whisperX](https://github.com/m-bain/whisperX); install via pip/uvx | Igor, 2026-08-20 |
| HyperFrames upstream = [github.com/heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main); CLI `npx hyperframes`; não instalar as skills HeyGen neste repo (segundo roteador) | Igor, 2026-08-20 |

## Resolvidas

| ID | Decisão | Quando |
|---|---|---|
| P11 | Sempre commit + `git push` para `origin` (`https://github.com/igorlsobral/Agentes.git`) após mudança significativa neste repo, para ficar salvo na nuvem. Nunca `push --force`. Nunca commitar secrets. | 2026-08-19 |
| P1-source / P2-source / P3-source | URLs oficiais gravadas; allowlist de **confirmação** (não clone). Instalação **local** continua em P1–P3. | 2026-08-20 |
| P1 | FFmpeg 9.0 Gyan em `C:\Users\ig\tools\ffmpeg\bin\ffmpeg.exe` (+ ffprobe). User PATH. | 2026-08-20 |
| P2 | Python 3.12.10 + WhisperX 3.8.6 em `C:\Users\ig\Documents\Agentes\.venv\Scripts\whisperx.exe`. CPU default. | 2026-08-20 |
| P3 | Node.js 22.23.2 em `C:\Users\ig\tools\node\`; `npx --yes hyperframes` v0.8.4; Chrome Headless Shell no cache; telemetria off. | 2026-08-20 |
