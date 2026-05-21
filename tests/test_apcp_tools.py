import importlib.util
import os
import shutil
import subprocess
import sys
import unittest
import uuid
from contextlib import contextmanager
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import apcp_core_files as core_files  # noqa: E402


def load_script_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@contextmanager
def temporary_project():
    parent = Path(os.environ.get("APCP_TEST_TMPDIR", ROOT / "tmp"))
    parent.mkdir(parents=True, exist_ok=True)
    path = parent / f"apcp-test-{uuid.uuid4().hex}"
    path.mkdir()
    try:
        yield str(path)
    finally:
        shutil.rmtree(path, ignore_errors=True)


class ApcpToolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gather = load_script_module("apcp_gather", SCRIPTS / "apcp-gather.py")

    def write_profile_files(self, root, profile):
        for relative in core_files.get_profile_files(profile):
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"# {relative}\n", encoding="utf-8")

    def test_all_profile_files_exist_in_repository(self):
        for profile in core_files.available_profiles():
            with self.subTest(profile=profile):
                for relative in core_files.get_profile_files(profile):
                    self.assertTrue((ROOT / relative).is_file(), relative)

    def test_default_gather_uses_core_profile(self):
        with temporary_project() as directory:
            root = Path(directory)
            self.write_profile_files(root, "core")
            (root / "AI_MAIN.md").write_text(
                "# AI_MAIN.md  \n\n\nBody line   \n",
                encoding="utf-8",
            )

            result = self.gather.gather_context(caveman_mode=True, root=root)

            self.assertEqual(result, 0)
            bundle = (root / "PROMPT_READY.txt").read_text(encoding="utf-8")
            self.assertIn("Profile: core", bundle)
            self.assertIn(
                "Compaction: whitespace-trimmed, repeated blank lines collapsed",
                bundle,
            )
            self.assertIn("=== START OF FILE: AI_MAIN.md ===", bundle)
            self.assertIn("# AI_MAIN.md\n\nBody line\n", bundle)
            self.assertNotIn("# AI_MAIN.md  \n\n\nBody line   \n", bundle)
            self.assertNotIn(
                "=== START OF FILE: WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md ===",
                bundle,
            )

    def test_gather_fails_when_selected_file_is_missing(self):
        with temporary_project() as directory:
            root = Path(directory)
            self.write_profile_files(root, "core")
            (root / "AI_MAIN.md").unlink()

            result = self.gather.gather_context(caveman_mode=True, root=root)

            self.assertEqual(result, 1)
            self.assertFalse((root / "PROMPT_READY.txt").exists())

    def test_profile_config_can_include_and_exclude_known_files(self):
        with temporary_project() as directory:
            root = Path(directory)
            self.write_profile_files(root, "web")
            config = root / "apcp-profile.json"
            config.write_text(
                '{\n'
                '  "profile": "web",\n'
                '  "include": ["MACP_IMPLEMENTATION_GUIDE.md"],\n'
                '  "exclude": ["WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md"]\n'
                '}\n',
                encoding="utf-8",
            )
            macp = root / "MACP_IMPLEMENTATION_GUIDE.md"
            macp.write_text("# MACP_IMPLEMENTATION_GUIDE.md\n", encoding="utf-8")

            result = self.gather.gather_context(caveman_mode=False, root=root)

            self.assertEqual(result, 0)
            bundle = (root / "PROMPT_READY.txt").read_text(encoding="utf-8")
            self.assertIn("Profile: web", bundle)
            self.assertIn("=== START OF FILE: MACP_IMPLEMENTATION_GUIDE.md ===", bundle)
            self.assertNotIn(
                "=== START OF FILE: WEBSITE_BACKEND_SECURITY_OPTIMIZATION_PROTOCOL.md ===",
                bundle,
            )

    def test_installer_dry_run_does_not_write_target_files(self):
        with temporary_project() as directory:
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS / "apcp-install.py"),
                    "--target",
                    directory,
                    "--profile",
                    "cli",
                    "--dry-run",
                ],
                cwd=ROOT,
                text=True,
                encoding="utf-8",
                errors="replace",
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=30,
            )

            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn("Installing Nexus-APCP profile: cli", result.stdout)
            self.assertFalse((Path(directory) / "apcp-profile.json").exists())

    def test_validator_supports_named_checks(self):
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "validate-repo.py"),
                "--only",
                "required-files",
            ],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=30,
        )

        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("OK: required files", result.stdout)


if __name__ == "__main__":
    unittest.main()
