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
| Logo, mascote, fontes, imagens de **tela cheia** | `C:\Users\ig\Documents\Agentes\brand\assets` |
| Prints de vídeos / “quero assim” / VSL de referência | `C:\Users\ig\Documents\Agentes\brand\references` |
| Depoimentos (abertura da VSL) | `C:\Users\ig\Documents\Agentes\brand\assets\depoimentos` |
| Música de fundo | `C:\Users\ig\Documents\Agentes\music` |
| Efeitos (swoosh, passos, toc-toc, plim, bolha) | `C:\Users\ig\Documents\Agentes\sfx` |
| Cenas longas (repertório visual) | `C:\Users\ig\Documents\Agentes\cenas` |
| Transcrição pronta (francês desta VSL) | `C:\Users\ig\Documents\Agentes\transcricao` |
| Prévia que o agente gerar | `C:\Users\ig\Documents\Agentes\projects\<nome>\previews` |
| Arquivo final | `projects\<nome>\outputs` **e** `C:\Users\ig\Downloads` |

Vídeos grandes **não** sobem para o GitHub (de propósito). Ficam só no seu disco.

## Como pedir no chat novo

1. Coloque o bruto em `raw`.
2. Escreva: *começa um projeto neste bruto* e o formato:
   - YouTube longo (`long-form`)
   - explainer curto (`short-form-explainer`)
   - TikTok cru (`tiktok-raw`)
   - vídeo de vendas / VSL (`vsl`)
3. Abra a prévia no caminho que o agente mostrar (melhor no Explorer do que na janelinha do Cursor).
4. Mande ajustes em português (“o gráfico mais baixo”, “menor”, “outro swoosh”).
5. Se um trecho deve **cobrir a tela inteira** (sumir a sua cara, só visual + sua voz): *a partir de [frase], tela cheia até [frase]* ou *volta ao normal*. Imagens em `C:\Users\ig\Documents\Agentes\brand\assets` (ou outra pasta que você apontar). Sons curtos (passos, toc-toc, plim, bolha) entram sozinhos quando o visual pedir; você pode soltar um `.wav` melhor em `C:\Users\ig\Documents\Agentes\sfx`.
6. Cenas longas (igreja, padre, milagre, etc.) vão em `C:\Users\ig\Documents\Agentes\cenas`. Servem para **qualquer** formato (TikTok, YouTube longo, explainer, VSL), não só tela cheia. O agente procura o trecho que combina com o que você falou.
7. VSL clone: o vídeo de referência longo vai em `C:\Users\ig\Documents\Agentes\brand\references`. Os depoimentos do começo vão em `C:\Users\ig\Documents\Agentes\brand\assets\depoimentos`. O agente estuda o ritmo da referência (quando a cena para e só a frase cobre a tela) e monta o nosso com as cenas da pasta `cenas`, sem gerar imagem por IA.

O **arquivo final** (com gráficos) sai a **60 fps**. Um estágio por vez, a menos que você peça o pipeline inteiro.

## Dinheiro / contas

Fluxo local = **grátis**. Serviços pagos (voz de robô, vídeo inventado, render na nuvem, “quem falou o quê” com conta Hugging Face) **só se o agente propor e você disser ok neste chat**. Até lá: tudo no PC. Credenciais nunca vão para o GitHub.

## O que ainda só você pode completar

Lista viva: [pendencias.md](pendencias.md). Resumo: kit de cores/logo/mascote, quão seco o corte, formato padrão se você esquecer de dizer. Layout de oferta da VSL: o vídeo de referência na pasta de referências (ainda não chegou).
