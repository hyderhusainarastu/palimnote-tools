#!/usr/bin/env python3
"""Generate README.md from tools.json. Use --check to fail when README.md is stale."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GH = "https://github.com/"


def render(data):
    owner = data["owner"]
    out = ["# Palimnote Tools", "",
           "Index of small, dependency-light developer tools for AI-assisted work: agent guardrail hooks, an evidence gate for agent reports, a release privacy scanner, citation checkers, a local-first LLM router, an MCP server template, and pandoc, CI and database helpers. Plain CLIs and libraries that any coding agent can call. Each tool lives in its own repository.", "",
           "**Works with:** ChatGPT, Codex, Claude Code, Cursor, Gemini, Copilot and local models. Each tool is a plain CLI or library, so any assistant that can run a shell command or read a repository can use it.", ""]
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
            "Clone the tool's repository and follow its own README. Each one is self-contained, with no shared runtime. Which assistants and surfaces a tool was tested with is stated in that tool's own README; treat anything not stated there as untested.", "",
            "## Quick start per platform", "",
            "| Platform | How |", "| --- | --- |",
            "| Claude Code | Clone the tool, run it from the Bash tool, or wire its hook or skill if it ships one. |",
            "| Codex | Clone the tool and read its AGENTS.md; the agent runs the CLI in the sandbox. |",
            "| Cursor | Clone the tool into the workspace; the agent runs the CLI from the terminal. |",
            "| ChatGPT, Gemini, Copilot chat | Run the CLI yourself and paste the output into the chat. |",
            "| Local models | Call the tool from a script or an agent harness that can run shell commands. |", "",
            "## Example", "",
            "```sh",
            f"git clone {GH}{owner}/release-privacy-scanner",
            "cd release-privacy-scanner",
            "python3 -m pip --version   # check the requirements listed in the table above",
            "# then follow the README in that repository",
            "```", "",
            "To add or change a catalog entry, edit `tools.json` and run `python3 scripts/build_readme.py`. Never edit this README by hand.", "",
            "## Keywords", "",
            "ai-agents, ai-coding-agents, agents-md, llm, mcp, git-hooks, cli, local-llm, citations, pandoc, ci-cd, developer-tools, chatgpt, codex, claude-code, cursor", "",
            "## Related catalogs", "",
            "| Catalog | Description |", "| --- | --- |"]
    for n, d in [("palimnote-skills", "Portable agent skills following the SKILL.md convention"),
                 ("palimnote-templates", "Copy-and-fill project templates"),
                 ("palimnote-agent-patterns", "Reusable multi-agent orchestration and role patterns")]:
        out.append(f"| [{n}]({GH}{owner}/{n}) | {d} |")
    out += ["", "## License", "",
            "MIT. Each repository in this catalog carries its own LICENSE file.", "",
            f"Part of the Palimnote catalogs. Hub profile: [{owner}/{owner}]({GH}{owner}/{owner}). This catalog: [{data['catalog']}]({GH}{owner}/{data['catalog']}). More at [palimnote.com](https://palimnote.com).", ""]
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
