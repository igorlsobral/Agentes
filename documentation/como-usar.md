# Como usar (para o Igor)

**Role:** Manual em português, sem jargão. O agente lê isto depois de um chat novo.

**Parent:** [documentation/README.md](README.md)

Igor **não programa**. O agente fala português simples. Não despejar termos técnicos. Se um termo for inevitável (WhisperX, FFmpeg), explicar em uma frase.

## O que este projeto faz

Você solta o vídeo cru. O agente corta, põe gráfico e exporta um MP4. Você dirige em linguagem natural e aprova. As ferramentas pesadas já estão no PC (instaladas em 2026-08-20). **Não precisa gastar dinheiro** no fluxo normal.

## Onde soltar arquivos

| O que | Pasta no Explorer |
|---|---|
| Vídeo cru (`.mp4`, `.mov`, `.mkv`) | `C:\Users\ig\Documents\Agentes\raw` |
| Logo, mascote, fontes | `C:\Users\ig\Documents\Agentes\brand\assets` |
| Prints de vídeos / “quero assim” | `C:\Users\ig\Documents\Agentes\brand\references` |
| Música de fundo | `C:\Users\ig\Documents\Agentes\music` |
| Prévia que o agente gerar | `C:\Users\ig\Documents\Agentes\projects\<nome>\previews` |
| Arquivo final | `projects\<nome>\outputs` **e** `C:\Users\ig\Downloads` |

Vídeos grandes **não** sobem para o GitHub (de propósito). Ficam só no seu disco.

## Como pedir no chat novo

1. Coloque o bruto em `raw`.
2. Escreva: *começa um projeto neste bruto* e o formato:
   - YouTube longo (`long-form`)
   - explainer curto (`short-form-explainer`)
   - TikTok cru (`tiktok-raw`)
3. Abra a prévia no caminho que o agente mostrar.
4. Mande ajustes em português (“o gráfico mais baixo”, “menor”).

Um estágio por vez, a menos que você peça o pipeline inteiro.

## Dinheiro / contas

Fluxo local = **grátis**. Serviços pagos (voz de robô, vídeo inventado, render na nuvem, “quem falou o quê” com conta Hugging Face) **só se o agente propor e você disser ok neste chat**. Até lá: tudo no PC. Credenciais nunca vão para o GitHub.

## O que ainda só você pode completar

Lista viva: [pendencias.md](pendencias.md). Resumo: kit de cores/logo/mascote, quão seco o corte, formato padrão se você esquecer de dizer.
