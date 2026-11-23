#!/usr/bin/env python3
"""Generate README.md from tools.json. Use --check to fail when README.md is stale."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GH = "https://github.com/"


def render(data):
    owner = data["owner"]
    out = ["# Palimnote Tools", "",
           "Index of small, dependency-light developer tools for AI-assisted work: agent guardrail hooks, an evidence gate for agent reports, a release privacy scanner, citation checkers, a local-first LLM router, an MCP server template, and pandoc, CI and database helpers. Plain CLIs and libraries that any coding agent can call. Each tool lives in its own repository.", ""]
    for g in data["groups"]:
        rows = [t for t in data["tools"] if t["group"] == g]
        if not rows:
            continue
        out += [f"## {g}", "", "| Tool | What | Language | Requirements | Works with |", "| --- | --- | --- | --- | --- |"]
        for t in rows:
            out.append(f"| [{t['name']}]({GH}{owner}/{t['repo']}) | {t['what']} | {t['language']} | {t['requirements']} | {t['works_with']} |")
        out.append("")
    out += ["## Also published", "",
            "These are listed in other catalogs.", "",
            "| Repo | What | Catalog |", "| --- | --- | --- |"]
    for t in data["also_published"]:
        out.append(f"| [{t['name']}]({GH}{owner}/{t['repo']}) | {t['what']} | [{t['catalog']}]({GH}{owner}/{t['catalog']}) |")
    out += ["",
            "## How to use", "",
            "Clone the tool's repository and follow its own README. Each one is self-contained, with no shared runtime. Every README has a capability table that says which assistants and surfaces were tested and which were not.", "",
            "## Related catalogs", "",
            "| Catalog | Description |", "| --- | --- |"]
    for n, d in [("palimnote-skills", "Portable agent skills following the SKILL.md convention"),
                 ("palimnote-templates", "Copy-and-fill project templates"),
                 ("palimnote-agent-patterns", "Reusable multi-agent orchestration and role patterns")]:
        out.append(f"| [{n}]({GH}{owner}/{n}) | {d} |")
    out += ["", "## License", "",
            "MIT. Each repository in this catalog carries its own LICENSE file.", "",
            f"Part of the Palimnote catalogs. More at [github.com/{owner}]({GH}{owner}) and [palimnote.com](https://palimnote.com).", ""]
    return "\n".join(out)


def main():
    data = json.loads((ROOT / "tools.json").read_text())
    text = render(data)
    target = ROOT / "README.md"
    if "--check" in sys.argv:
        if target.read_text() != text:
            print("README.md is stale; run scripts/build_readme.py")
            return 1
        return 0
    target.write_text(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
