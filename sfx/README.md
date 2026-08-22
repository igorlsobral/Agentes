# sfx

**Role:** One-shot sound effects (swoosh, whoosh, hit, **event sfx**). Not music beds.

**Parent:** [README.md](../README.md)

Drop files here. The agent may swap which file a clip uses. Binaries are gitignored; this folder is the library on disk.

Event sfx play on a **tela cheia** stretch, timed to the motion (skill [`skills/full-screen-visual.md`](../skills/full-screen-visual.md)). Quieter than speech. If the matching file is missing, the agent synthesizes a short discreet one on this PC — no download.

## Inventory

| Entry | When to open | Path |
|---|---|---|
| swoosh-in.wav (gitignored) | Default whoosh on this PC until Igor drops another | this folder |
| passos / walk | Character walking | `INFORMAÇÃO AUSENTE` — synthesize if needed |
| toc-toc / knock | Door knock | `INFORMAÇÃO AUSENTE` — synthesize if needed |
| plim / check | Correct check appears | `INFORMAÇÃO AUSENTE` — synthesize if needed |
| bolha / rising numbers | Numbers counting up | `INFORMAÇÃO AUSENTE` — synthesize if needed |

## Gaps

No packed library. Igor may drop any `.wav` / `.mp3` he prefers; the agent swaps.

## Children

None.
