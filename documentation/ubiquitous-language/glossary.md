# Glossary

Termos canônicos. Não traduzir a coluna **Term**.

| Term | Meaning | Notes |
|---|---|---|
| Igor | Criador, dono deste repositório, único aprovador humano | Registrado 2026-08-19 |
| HyperFrames | Motion graphics, overlays, captions (HTML/CSS/GSAP → MP4) | CLI: `npx hyperframes`; source [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) |
| WhisperX | Transcrição com timestamp por palavra; **é** a timeline | [m-bain/whisperX](https://github.com/m-bain/whisperX); não é Google Whisk |
| Whisk X | Apelido informal para WhisperX | Nunca Google Whisk |
| FFmpeg | Cortes, join, mix de áudio, export, normalização mp4 | Build local; source [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) |
| EDL | Edit decision list em `projects/<clip>/edl.json` | |
| transcript.json | Timeline word-level; cortes, captions e gráficos sincronizam nela | Sem isto, não cortar |
| rough cut lock | Trava o corte antes dos gráficos | Reabrir depois de gráficos exige aviso de custo + ok |
| partial render | Re-render só do trecho mudado | Obrigatório no second pass |
| brand kit | Identidade em `brand/` (cor, fonte, logo, mascote) | Não improvisar |
| Coolvetica | Fonte padrão de captions short-form | Arquivos em `brand/*.otf`; default `Coolvetica Rg.otf` (2026-08-21) |
| short-form-explainer | Gráficos em cima, rosto embaixo, captions no meio | |
| tiktok-raw | Hook de texto + corte cru + captions | |
| long-form | Intro cinematográfica YouTube (rosto cheio + gráficos pontuais) | |
| take | Uma passada de fala no bruto; manter sempre o último/melhor | |
| dead air | Silêncio residual quando se corta só no transcript | Detectar silêncio no áudio |
| INFORMAÇÃO AUSENTE | Lacuna explícita; não preencher com palpite | |
