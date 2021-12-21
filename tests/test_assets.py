"""tests paths module"""

from lit_junkie.logo import LOGO
from lit_junkie.paths import PROJECT_ROOT, SOURCE_ROOT, TEST_DIRECTORY


def test_pyproject_path_exists():
    """Tests pyproject file exists"""
    pyproject_path = PROJECT_ROOT / "pyproject.toml"
    assert pyproject_path.exists()


def test_project_root_exists():
    """Tests projects root directory exists"""
    assert PROJECT_ROOT.exists()


def test_source_root_exists():
    """Tests projects source directory exists"""
    assert SOURCE_ROOT.exists()


def test_data_exists():
    """Tests projects source directory exists"""
    test_data_path = TEST_DIRECTORY / "data" / "response.json"
    test_data_path = TEST_DIRECTORY / "data" / "serialized.json"
    assert test_data_path.exists()


def test_logo_exists():
    """Tests logo is correct"""
    assert len(LOGO) == 432
