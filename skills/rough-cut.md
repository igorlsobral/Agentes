# rough-cut

Use when the current clip needs transcription, silence-based cutting, EDL, assembly, or lock.

Requires: ingested source in `projects/<clip>/source/`. No word-level `transcript.json` → you may create it here; you may not cut without it.

## Do

1. Run WhisperX per [`documentation/services/whisperx.md`](../documentation/services/whisperx.md) → `projects/<clip>/transcript.json` (word-level timestamps).
2. Measure silence on the **audio**, relative to this take’s level. Never a fixed −35 dB.
3. Do not trust WhisperX word end-times as cut points — they stretch into following silence.
4. Always keep the last/best take.
5. Write `projects/<clip>/edl.json` (keep/drop ranges in source time).
6. FFmpeg assembly from the EDL → preview in `projects/<clip>/previews/`.
7. Mark the rough cut **locked** on the clip overview.
8. Stop. Next stage: graphics (1st pass), only after lock.

If WhisperX is not callable: stop; do not invent a transcript.

## Lock

After lock, graphics may start. Reopening the cut after graphics requires a cost warning and Igor’s confirmation.
