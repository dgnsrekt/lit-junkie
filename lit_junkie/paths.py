"""Commonly used paths."""

from pathlib import Path

SOURCE_ROOT = Path(__file__).parent

PROJECT_ROOT = SOURCE_ROOT.parent

TEST_DIRECTORY = PROJECT_ROOT / "tests"

STORAGE_PATH = Path.home() / "readinglist.pickle"

for path in [SOURCE_ROOT, PROJECT_ROOT, TEST_DIRECTORY, STORAGE_PATH.parent]:
    assert path.exists(), f"{path} path is missing."
