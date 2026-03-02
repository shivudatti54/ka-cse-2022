# MiniMax Routing Rule

When the user explicitly says to "use minimax" (or equivalent wording), route the model-generation part of that task through `scripts/minimax_exec.sh` in this workspace.

## Required behavior

- Treat OpenAI Codex as the orchestrator.
- Use MiniMax only for the requested generation step(s) by calling `scripts/minimax_exec.sh`.
- Keep local file edits, shell work, and verification in Codex as normal.
- If MiniMax returns quota or balance errors, report the exact error and continue with non-MiniMax steps when possible.
- Never print the full API key in responses.
