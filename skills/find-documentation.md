# find-documentation

Use for “how do we do X?” and for confirmation of a standing rule.

## Source order (confirmation source first)

1. Root [`README.md`](../README.md) standing restrictions
2. [`video-editor/AGENTS.md`](../video-editor/AGENTS.md) for pipeline hard rules
3. [`documentation/`](../documentation/) service notes and glossary
4. Upstream GitHub listed in [`documentation/services/pipeline.md`](../documentation/services/pipeline.md) (FFmpeg, WhisperX, HyperFrames) — confirmation for **how to invoke**, never as a clone inside this repo
5. The named skill for the current stage
6. Git history — **never** as the only source

If the answer is `INFORMAÇÃO AUSENTE`, point at [`documentation/pendencias.md`](../documentation/pendencias.md) instead of guessing.
