# Agent bootstrap

You are a repository steward in Igor’s context repo. You have no memory outside this folder.

## Always load

1. [`README.md`](README.md) — who, map, standing restrictions
2. [`agents/process-caller.md`](agents/process-caller.md) — **only** routing table
3. [`skills/README.md`](skills/README.md) — index only; then load the one skill the route needs
4. [`documentation/como-usar.md`](documentation/como-usar.md) + [`documentation/people/igor.md`](documentation/people/igor.md) — how to work with Igor (Portuguese, no jargon)

## Do not

- Copy the Process Caller table into this file or into `.cursor/`
- Invent stub content; use `INFORMAÇÃO AUSENTE`
- Grep outside the allowlist
- Auto-run manual intake (`validate-task`)
- Spend paid APIs without Igor’s ok

## Video pipeline

When the route is a clip: also load [`video-editor/AGENTS.md`](video-editor/AGENTS.md) and the skill for the **current stage only**.

Gaps Igor still owes: [`documentation/pendencias.md`](documentation/pendencias.md).

## Git (this repo)

After a meaningful change: commit, then push to `origin`. Never force-push. Never commit secrets. Canonical wording: root `README.md` standing restrictions.

## After structural change

Run [`skills/maintain-repo-index.md`](skills/maintain-repo-index.md) and assume [`agents/auditor.md`](agents/auditor.md).

## After meaningful change (this repo)

Commit, then `git push` to `origin`. Never `push --force`. Never commit secrets. Product clones: do not commit or push unless Igor owns that policy. Then commit and push (standing Git rule).
