# AGENTS.md

This repo is a catalog (an index), not a tool. It lists tools that each live in their own repository.

## Rules
- Edit `tools.json` to add, change or remove a catalog entry. Required fields per tool: name, repo, what (140 characters or fewer), language, requirements, works_with, group.
- Never edit `README.md` by hand. Run `python3 scripts/build_readme.py` to regenerate it.
- Run `python3 -m unittest discover tests` before committing. Tests are offline.
- Only list a tool once its repository exists and is public. Do not claim a tool was tested on an assistant unless that tool's own README says so.
- Do not commit secrets, `.env` files or local absolute paths.
- Do not add AI-authorship wording to commits or docs.

## Related
- Hub profile: https://github.com/hyderhusainarastu/hyderhusainarastu
- Sibling catalogs: palimnote-skills, palimnote-templates, palimnote-agent-patterns
