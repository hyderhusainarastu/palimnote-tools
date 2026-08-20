# Palimnote Tools

Small, sharp developer tools: a pandoc table-width Lua filter, a safe .env secret-entry helper, a SQL-migration preflight gate, a pnpm-monorepo CI template, a status-page generator, and a pandoc PDF render+verify kit. Each tool is self-contained and lives in its own repository.

## Document Pipeline

| Tool | Description |
| --- | --- |
| [pandoc-table-width-filter](https://github.com/hyderhusainarastu/pandoc-table-width-filter) | A Pandoc Lua filter that replaces Pandoc's separator-dash column-width heuristic for Markdown pipe tables with a content-aware water-filling allocation, preventing prose-heavy columns from overflowing while never squeezing a column below its longest unbreakable word |
| [pandoc-pdf-render-verify-kit](https://github.com/hyderhusainarastu/pandoc-pdf-render-verify-kit) | Shell scripts that render Markdown to PDF via pandoc/xelatex with a documented fallback path, then layer-verify the output (page count, text-overlap, hbox-warning scan) against the source instead of trusting a zero exit code |

## Engineering Workflow

| Tool | Description |
| --- | --- |
| [dotenv-secret-prompt](https://github.com/hyderhusainarastu/dotenv-secret-prompt) | A zsh script that interactively writes secrets into a .env file with a git-ignore guard, hidden input, atomic writes, and .env.example-driven key discovery |
| [migration-ledger-preflight-gate](https://github.com/hyderhusainarastu/migration-ledger-preflight-gate) | A local pre-push script that SHA-256-hashes SQL migration files and fails if any are missing from (or no longer match) the database's applied-migrations ledger, catching the not-yet-applied and edited-after-applied failure modes before an auto-deploying push ships schema-dependent code |
| [pnpm-monorepo-ci-template](https://github.com/hyderhusainarastu/pnpm-monorepo-ci-template) | A GitHub Actions CI workflow for pnpm-workspaces monorepos that documents three specific gotchas: the pnpm/action-setup-before-setup-node ordering trap, using the pgvector Postgres image as a service container, and a deliberate CI-safe-vs-manual E2E test split |
| [project-status-page-generator](https://github.com/hyderhusainarastu/project-status-page-generator) | A dependency-free Node script that renders a project's phases-and-status JSON into a static HTML status page, with a --check mode that fails CI when the checked-in page is stale relative to its source |

## How to use

Clone the individual tool's repository. Each one is self-contained — no shared runtime or umbrella install step — so pull the one you need and follow its own README.

## Related catalogs

| Catalog | Description |
| --- | --- |
| [palimnote-skills](https://github.com/hyderhusainarastu/palimnote-skills) | Portable agent skills following the SKILL.md convention |
| [palimnote-templates](https://github.com/hyderhusainarastu/palimnote-templates) | Copy-and-fill project templates |
| [palimnote-agent-patterns](https://github.com/hyderhusainarastu/palimnote-agent-patterns) | Reusable multi-agent orchestration and role patterns |

## License

MIT. Each repository in this catalog carries its own LICENSE file.
