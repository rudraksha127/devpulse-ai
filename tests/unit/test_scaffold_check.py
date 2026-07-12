from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.quality.scaffold_check import (
    NON_EMPTY_FILES,
    REQUIRED_DIRECTORIES,
    REQUIRED_FILES,
    run_scaffold_check,
)


class ScaffoldCheckTests(unittest.TestCase):
    def _build_valid_structure(self, root: Path) -> None:
        for directory in REQUIRED_DIRECTORIES:
            (root / directory).mkdir(parents=True, exist_ok=True)

        for file_path in REQUIRED_FILES:
            target = root / file_path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("ok\n", encoding="utf-8")

    def test_passes_with_required_scaffold(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            self._build_valid_structure(repo_root)

            issues = run_scaffold_check(repo_root)

            self.assertEqual(issues, [])

    def test_fails_when_critical_doc_is_empty(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            self._build_valid_structure(repo_root)

            critical_file = repo_root / NON_EMPTY_FILES[0]
            critical_file.write_text("", encoding="utf-8")

            issues = run_scaffold_check(repo_root)

            self.assertTrue(any(issue.path == NON_EMPTY_FILES[0] for issue in issues))


if __name__ == "__main__":
    unittest.main()
