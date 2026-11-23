# Palimnote Tools

Index of small, dependency-light developer tools for AI-assisted work: agent guardrail hooks, an evidence gate for agent reports, a release privacy scanner, citation checkers, a local-first LLM router, an MCP server template, and pandoc, CI and database helpers. Plain CLIs and libraries that any coding agent can call. Each tool lives in its own repository.

## Agent safety

| Tool | What | Language | Requirements | Works with |
| --- | --- | --- | --- | --- |
| [ai-coding-agent-guardrail-hooks](https://github.com/hyderhusainarastu/ai-coding-agent-guardrail-hooks) | Guardrail CLI, Claude Code hook and git hooks that block .env reads, out-of-root writes and --no-verify. Advisory, not a sandbox. | Python | Python 3.10+, git | Any shell or git; Claude Code hook |
| [release-privacy-scanner](https://github.com/hyderhusainarastu/release-privacy-scanner) | Scans a repo, its history and release archives for local paths, identifiers, emails and secret-shaped strings before publishing. | Python | Python 3.10+, git | Any shell, CI, pre-commit; agent skill |

## Agent verification

| Tool | What | Language | Requirements | Works with |
| --- | --- | --- | --- | --- |
| [agent-report-evidence-gate](https://github.com/hyderhusainarastu/agent-report-evidence-gate) | Checks an AI agent's done report for evidence completeness: cited files exist, claims have evidence, commands, hashes and commits re-verify. | Python | Python 3.10+ | Any shell, CI; agent skill |

## LLM and local models

| Tool | What | Language | Requirements | Works with |
| --- | --- | --- | --- | --- |
| [local-first-llm-router](https://github.com/hyderhusainarastu/local-first-llm-router) | Policy layer that tries a script, then a local model, and escalates to a cloud model only when checks fail and the privacy tier allows it. | Python | Python 3.10+ | Python library; Ollama, llama.cpp or any OpenAI-compatible server |
| [ollama-memory-governor](https://github.com/hyderhusainarastu/ollama-memory-governor) | Keeps free RAM above a floor with several Ollama models: pins the primary, unloads others by priority, avoids the num_ctx reload trap. | Python | Python 3.10+, macOS or Linux, Ollama | Any shell; CLI or daemon |

## MCP

| Tool | What | Language | Requirements | Works with |
| --- | --- | --- | --- | --- |
| [safe-mcp-server-template](https://github.com/hyderhusainarastu/safe-mcp-server-template) | MCP server template that treats tool output as untrusted: closed tool list, fenced output, size caps, rate limits, confirm step. | Python | Python 3.10+, mcp SDK | MCP clients over stdio or HTTP |

## Research and citations

| Tool | What | Language | Requirements | Works with |
| --- | --- | --- | --- | --- |
| [hallucinated-citation-checker](https://github.com/hyderhusainarastu/hallucinated-citation-checker) | Checks every BibTeX entry against Crossref, OpenAlex, arXiv, Open Library and doi.org and writes a CSV verdict per key. Bibliography level. | Python | Python 3.10+, network | Any shell; agent skill |
| [scholarly-citation-resolver](https://github.com/hyderhusainarastu/scholarly-citation-resolver) | Resolves a messy free-text citation to verified metadata from six open sources and rejects matches that do not fit. Free text to metadata. | TypeScript | Node 20+, network | Any shell; Node or TypeScript library |

## Docs and publishing

| Tool | What | Language | Requirements | Works with |
| --- | --- | --- | --- | --- |
| [pandoc-table-width-filter](https://github.com/hyderhusainarastu/pandoc-table-width-filter) | Pandoc Lua filter that sizes pipe-table columns by content instead of separator dashes, so prose columns stop overflowing. | Lua | pandoc | Pandoc CLI |
| [pandoc-pdf-render-verify-kit](https://github.com/hyderhusainarastu/pandoc-pdf-render-verify-kit) | Renders Markdown to PDF with pandoc and LaTeX, then verifies page count, text overlap and hbox warnings, not just exit code 0. | Shell, Python | pandoc, LaTeX engine, Python 3 | Any shell |
| [project-status-page-generator](https://github.com/hyderhusainarastu/project-status-page-generator) | Renders a phases-and-status JSON file into a static HTML status page; --check fails CI when the page is stale. | Node.js | Node, no dependencies | Any shell, CI |

## CI and databases

| Tool | What | Language | Requirements | Works with |
| --- | --- | --- | --- | --- |
| [migration-ledger-preflight-gate](https://github.com/hyderhusainarastu/migration-ledger-preflight-gate) | Pre-push check that hashes SQL migrations and fails if any are unapplied or edited after being applied to the database ledger. | Node.js | Node | Any shell, git pre-push hook |
| [pnpm-monorepo-ci-template](https://github.com/hyderhusainarastu/pnpm-monorepo-ci-template) | GitHub Actions workflow for pnpm monorepos covering setup ordering, a pgvector Postgres service and a CI-safe E2E split. | YAML | GitHub Actions | GitHub Actions; any assistant can adapt it |

## Secrets

| Tool | What | Language | Requirements | Works with |
| --- | --- | --- | --- | --- |
| [dotenv-secret-prompt](https://github.com/hyderhusainarastu/dotenv-secret-prompt) | zsh script that writes secrets into .env with hidden input, a git-ignore guard, atomic writes and .env.example key discovery. | zsh | zsh | Any terminal |

## Also published

These are listed in other catalogs.

| Repo | What | Catalog |
| --- | --- | --- |
| [multi-agent-orchestration-playbook](https://github.com/hyderhusainarastu/multi-agent-orchestration-playbook) | Twelve rules for running teams of AI agents, an AGENTS.md template and small tested helper scripts. | [palimnote-agent-patterns](https://github.com/hyderhusainarastu/palimnote-agent-patterns) |
| [deep-research-skill](https://github.com/hyderhusainarastu/deep-research-skill) | Agent skill for auditable research: saturation stop rule, verification levels and bounded negative findings. | [palimnote-skills](https://github.com/hyderhusainarastu/palimnote-skills) |
| [cross-model-second-opinion](https://github.com/hyderhusainarastu/cross-model-second-opinion) | Agent skill for a budgeted, read-only second opinion from a different AI model. | [palimnote-skills](https://github.com/hyderhusainarastu/palimnote-skills) |

## How to use

Clone the tool's repository and follow its own README. Each one is self-contained, with no shared runtime. Every README has a capability table that says which assistants and surfaces were tested and which were not.

## Related catalogs

| Catalog | Description |
| --- | --- |
| [palimnote-skills](https://github.com/hyderhusainarastu/palimnote-skills) | Portable agent skills following the SKILL.md convention |
| [palimnote-templates](https://github.com/hyderhusainarastu/palimnote-templates) | Copy-and-fill project templates |
| [palimnote-agent-patterns](https://github.com/hyderhusainarastu/palimnote-agent-patterns) | Reusable multi-agent orchestration and role patterns |

## License

MIT. Each repository in this catalog carries its own LICENSE file.

Part of the Palimnote catalogs. More at [github.com/hyderhusainarastu](https://github.com/hyderhusainarastu) and [palimnote.com](https://palimnote.com).
