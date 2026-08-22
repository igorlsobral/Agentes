# Pendências — o que só Igor pode informar

**Role:** Lista explícita de lacunas. O agente não preenche estas linhas por palpite.

**Parent:** [documentation/README.md](README.md)

Atualizado em 2026-08-21. Quando Igor responder um item, mover para **Resolvidas** e atualizar o arquivo canônico.

Manual simples: [como-usar.md](como-usar.md).

## Bloqueiam o primeiro vídeo publicado

| ID | O que falta | Por que importa | O que o Igor faz |
|---|---|---|---|
| P6 | Logo, mascote, cores (incl. “cor Claude” se for uso real) | Prints de estilo já existem; o kit da marca ainda não | Soltar PNG em `brand/assets/` e dizer as cores |

## Qualidade (não trava o 1º rascunho)

| ID | O que falta | Por que importa | Onde vai entrar |
|---|---|---|---|
| P7 | Corte mais seco ou mais calmo (padrão) | Sem default, o agente pergunta no 1º clipe | `presets/` ou `video-editor/AGENTS.md` |
| P8 | Preset padrão se Igor **não** disser o formato | Gráficos não começam sem formato | `presets/README.md` |
| P16 | Layout de oferta / end card do **VSL** | Sem isto o VSL não inventa preço, CTA nem garantia | Print em `brand/references/` ou texto no chat |
| P17 | Wavs melhores de event sfx (passos, toc-toc, plim, bolha) | Sem o arquivo o agente sintetiza um hit discreto no PC | Soltar `.wav` / `.mp3` em `sfx/` |

## Operação do repo (pode esperar)

| ID | O que falta | Por que importa | Onde vai entrar |
|---|---|---|---|
| P9 | Contas pagas, se um dia quiser | Hoje o padrão é **zero gasto** | `documentation/services/pipeline.md` |
| P10 | Outras pastas/clones fora daqui | Grep só allowlist | `documentation/services/pipeline.md` |
| P12 | Confirmar idioma dos arquivos estruturais (EN) vs domínio (PT) | Evitar mix | `README.md` Language |
| P13 | Nomes de canal YouTube/TikTok | Não inventar end card | `documentation/people/igor.md` |
| P14 | Resolução / loudness master | Export consistente (fps já decidido: 60) | `presets/` |
| P15 | Downloads se não for `c:\Users\ig\Downloads\` | Skill de export | `skills/export-video.md` |

## Já decidido (não perguntar de novo)

| Decisão | Fonte |
|---|---|
| Humano = **Igor**; único aprovador; **não é programador**; falar português simples | 2026-08-19 / 2026-08-21 |
| Chat clear: conhecimento vive neste repo, não na conversa | Igor, 2026-08-21 |
| Bruto → `raw/`; logo/fonte → `brand/assets/` (Coolvetica também em `brand/`); prints → `brand/references/`; música → `music/`; swoosh → `sfx/` | 2026-08-21 |
| Aceitar `.mp4`, `.mov`, `.mkv`; normalizar mp4 | 2026-08-21 (mkv no raw) |
| Gasto padrão = **nenhum**. API paga só com proposta + ok no chat | 2026-08-21 |
| Estilo de gráfico alvo = cards brancos arredondados / liquid-glass (prints em `brand/references/`) | 2026-08-21 |
| **Tela cheia / estilo 3D** = Reel em `brand/references/` (fundo escuro, texto enorme, objeto 3D, 1–2 s); cor de destaque pelo contexto, sem verde fixo | Igor, 2026-08-22 |
| Talking-head long-form/VSL: cards à **direita**; títulos CAIXA ALTA (Coolvetica heavy); resto com 1ª maiúscula; cada card diferente | 2026-08-21 |
| Formatos: long-form, short-form-explainer, tiktok-raw, **VSL** | 2026-08-21 |
| Arquivo final e overlays de gráfico = **60 fps** (câmera pode ser 30) | 2026-08-21 |
| Swoosh pode ser outro arquivo; biblioteca = `sfx/` | 2026-08-21 |
| **Tela cheia** sempre disponível depois do lock; some o rosto; voz fica; **volta ao normal** no chat ou na fala; event sfx no movimento (passos, toc-toc, plim, bolha); imagens de `brand/assets/` ou pasta nomeada; sem B-roll pago | Igor, 2026-08-21 |
| Stack, pipeline, Git commit+push, sem Whisk, música −23 dB, silêncio relativo, lock antes de gráficos, partial render | já na tabela anterior |

## Resolvidas

| ID | Decisão | Quando |
|---|---|---|
| P11 | Sempre commit + push para `origin` | 2026-08-19 |
| P1 P2 P3 | FFmpeg, WhisperX, HyperFrames+Chrome locais | 2026-08-20 |
| P4 | Coolvetica `.otf` em `brand/` (default `Coolvetica Rg.otf`) | 2026-08-21 |
| P5 | Intake do bruto `raw/2026-04-01 11-30-15.mkv` → `projects/2026-04-01-11-30-15/`; rough cut locked | 2026-08-21 |
| P14 (fps) | Final e gráficos = **60 fps** | 2026-08-21 |
