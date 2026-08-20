# maintain-repo-index

Run in the same session as any add, rename, delete, or material rewrite of a skill, agent, process folder, documentation index, or adapter wrapper.

## Do

1. Every index README matches the Index contract: Role, Parent, Inventory (`Entry | When to open | Path`), Gaps, Children.
2. Root README Indexes line ↔ folders that exist.
3. Every `skills/*.md` except README is in `skills/README.md`.
4. Every `.cursor/skills/*/SKILL.md` points at the same `skills/*.md` path.
5. Manual-only skills stay manual (`validate-task`).
6. Every `agents/*.md` except README is in `agents/README.md`.
7. Process Caller cites skills by path.
8. No second routing table in `.cursor/` or `AGENTS.md`.
9. Change policy: canonical files first, then pointers.

Then assume [`agents/auditor.md`](../agents/auditor.md) on the structural diff.
