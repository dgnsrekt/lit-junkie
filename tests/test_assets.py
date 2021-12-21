from lit_junkie.logo import LOGO
from lit_junkie.paths import PROJECT_ROOT, SOURCE_ROOT, TEST_DIRECTORY


def test_pyproject_path_exists():
    pyproject_path = PROJECT_ROOT / "pyproject.toml"
    assert pyproject_path.exists()


def test_project_root_exists():
    assert PROJECT_ROOT.exists()


def test_source_root_exists():
    assert SOURCE_ROOT.exists()


def test_data_exists():
    test_data_path = TEST_DIRECTORY / "data" / "response.json"
    test_data_path = TEST_DIRECTORY / "data" / "serialized.json"
    assert test_data_path.exists()


def test_logo_exists():
    assert len(LOGO) == 432
