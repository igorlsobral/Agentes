# Pendências — o que só Igor pode informar

**Role:** Lista explícita de lacunas. O agente não preenche estas linhas por palpite.

**Parent:** [documentation/README.md](README.md)

Atualizado em 2026-08-21. Quando Igor responder um item, mover para **Resolvidas** e atualizar o arquivo canônico.

Manual simples: [como-usar.md](como-usar.md).

## Bloqueiam o primeiro vídeo publicado

| ID | O que falta | Por que importa | O que o Igor faz |
|---|---|---|---|
| P5 | Rodar o **intake** no bruto que já está em `raw/` (`2026-04-01 11-30-15.mkv`, gitignored) | Definition of done = footage real ponta a ponta | No chat: *começa um projeto neste bruto* + formato |
| P6 | Logo, mascote, cores (incl. “cor Claude” se for uso real) | Prints de estilo já existem; o kit da marca ainda não | Soltar PNG em `brand/assets/` e dizer as cores |

## Qualidade (não trava o 1º rascunho)

| ID | O que falta | Por que importa | Onde vai entrar |
|---|---|---|---|
| P7 | Corte mais seco ou mais calmo (padrão) | Sem default, o agente pergunta no 1º clipe | `presets/` ou `video-editor/AGENTS.md` |
| P8 | Preset padrão se Igor **não** disser o formato | Gráficos não começam sem formato | `presets/README.md` |

## Operação do repo (pode esperar)

| ID | O que falta | Por que importa | Onde vai entrar |
|---|---|---|---|
| P9 | Contas pagas, se um dia quiser | Hoje o padrão é **zero gasto** | `documentation/services/pipeline.md` |
| P10 | Outras pastas/clones fora daqui | Grep só allowlist | `documentation/services/pipeline.md` |
| P12 | Confirmar idioma dos arquivos estruturais (EN) vs domínio (PT) | Evitar mix | `README.md` Language |
| P13 | Nomes de canal YouTube/TikTok | Não inventar end card | `documentation/people/igor.md` |
| P14 | Resolução / fps / loudness master | Export consistente | `presets/` |
| P15 | Downloads se não for `c:\Users\ig\Downloads\` | Skill de export | `skills/export-video.md` |

## Já decidido (não perguntar de novo)

| Decisão | Fonte |
|---|---|
| Humano = **Igor**; único aprovador; **não é programador**; falar português simples | 2026-08-19 / 2026-08-21 |
| Chat clear: conhecimento vive neste repo, não na conversa | Igor, 2026-08-21 |
| Bruto → `raw/`; logo/fonte → `brand/assets/` (Coolvetica também em `brand/`); prints → `brand/references/` | 2026-08-21 |
| Aceitar `.mp4`, `.mov`, `.mkv`; normalizar mp4 | 2026-08-21 (mkv no raw) |
| Gasto padrão = **nenhum**. API paga só com proposta + ok no chat | 2026-08-21 |
| Estilo de gráfico alvo = cards brancos arredondados / liquid-glass (prints em `brand/references/`) | 2026-08-21 |
| Stack, pipeline, Git commit+push, sem Whisk, música −23 dB, silêncio relativo, lock antes de gráficos, partial render | já na tabela anterior |

## Resolvidas

| ID | Decisão | Quando |
|---|---|---|
| P11 | Sempre commit + push para `origin` | 2026-08-19 |
| P1 P2 P3 | FFmpeg, WhisperX, HyperFrames+Chrome locais | 2026-08-20 |
| P4 | Coolvetica `.otf` em `brand/` (default `Coolvetica Rg.otf`) | 2026-08-21 |
