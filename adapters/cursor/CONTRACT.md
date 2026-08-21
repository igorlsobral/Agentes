# Cursor adapter contract

**Role:** Thin Cursor pointers. Canonical text lives in `skills/`, `agents/`, and `video-editor/AGENTS.md`.

**Parent:** [adapters/README.md](../README.md)

## Wiring

| Cursor path | Points at |
|---|---|
| `AGENTS.md` (repo root) | Process Caller + indexes |
| `.cursor/rules/context-repo-bootstrap.mdc` | Always-on pointers |
| `.cursor/rules/video-editor-pipeline.mdc` | Pipeline pointers |
| `.cursor/rules/speak-to-igor.mdc` | Portuguese, no jargon |
| `.cursor/skills/*/SKILL.md` | Matching `skills/*.md` |

## Rules

- Do not duplicate the Process Caller table here or in `.cursor/`.
- Change canonical files first, then wrappers.
- Manual skills keep `disable-model-invocation: true` on the wrapper.
