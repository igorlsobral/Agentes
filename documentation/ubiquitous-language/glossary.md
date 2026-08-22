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
| Coolvetica | Fonte padrão de captions short-form e de cards | Arquivos em `brand/*.otf`; corpo `Coolvetica Rg.otf`; títulos de card `Coolvetica Hv Comp.otf` (2026-08-21) |
| short-form-explainer | Gráficos em cima, rosto embaixo, captions no meio | |
| tiktok-raw | Hook de texto + corte cru + captions | |
| long-form | YouTube longo (rosto cheio + gráficos pontuais) | Cards à direita; 60 fps no overlay |
| VSL | Video Sales Letter — vídeo de vendas | Preset `vsl`; não inventar preço/CTA |
| sfx | Pasta de efeitos one-shot (swoosh, whoosh, event sfx) | `sfx/`; distinto de `music/` |
| tela cheia | Trecho em que o visual cobre o quadro inteiro; a fala continua; some o talking-head | Sempre disponível depois do lock; não é B-roll pago |
| cenas | Pasta de filmes longos usados como repertório visual | `cenas/`; qualquer formato depois do lock, não só tela cheia (Igor, 2026-08-22) |
| volta ao normal | Fim do trecho de tela cheia; volta talking-head + gráficos pontuais | Chat ou deixa claro no vídeo |
| event sfx | One-shot sincronizado com o movimento da tela cheia (passos, toc-toc, plim, bolha) | Mais baixo que a fala; sintetizar no PC se o arquivo faltar |
| take | Uma passada de fala no bruto; manter sempre o último/melhor | WhisperX pode colar dois takes num único carimbo — cortar pelo áudio |
| dead air | Silêncio residual quando se corta só no transcript | Detectar silêncio no áudio |
| INFORMAÇÃO AUSENTE | Lacuna explícita; não preencher com palpite | |
