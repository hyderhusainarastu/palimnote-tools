import json, re, subprocess, sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Catalog(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "tools.json").read_text())

    def test_readme_not_stale(self):
        r = subprocess.run([sys.executable, "-I", str(ROOT / "scripts/build_readme.py"), "--check"])
        self.assertEqual(r.returncode, 0)

    def test_fields_and_groups(self):
        for t in self.data["tools"]:
            for k in ("name", "repo", "what", "language", "requirements", "works_with", "group"):
                self.assertTrue(t.get(k), (t.get("name"), k))
            self.assertIn(t["group"], self.data["groups"])
            self.assertLessEqual(len(t["what"]), 140)

    def test_links_in_readme_match_json(self):
        text = (ROOT / "README.md").read_text()
        links = set(re.findall(r"github\.com/hyderhusainarastu/([A-Za-z0-9._-]+)\)", text))
        expected = {t["repo"] for t in self.data["tools"] + self.data["also_published"]}
        self.assertTrue(expected <= links)

    def test_no_dup_names(self):
        names = [t["name"] for t in self.data["tools"]]
        self.assertEqual(len(names), len(set(names)))


if __name__ == "__main__":
    unittest.main()
