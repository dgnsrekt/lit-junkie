import pytest

from lit_junkie import storage
from lit_junkie.paths import TEST_DIRECTORY
from lit_junkie.schemas import GoogleBookList

from .common import serialized_data_fixture


@pytest.fixture
def storage_path_fixture(tmpdir_factory):
    """Fixtures to represent a readinglist pickle file location"""
    return tmpdir_factory.mktemp("data").join("readinglist.pickle")


def test_store_and_load(storage_path_fixture, serialized_data_fixture):
    """Tests the ability to serialize/deserialize store/load books to a file"""
    target = GoogleBookList(**serialized_data_fixture)

    storage.store_books(target, path=storage_path_fixture)
    assert storage_path_fixture.exists()

    result = storage.load_books(path=storage_path_fixture)

    assert target == result
