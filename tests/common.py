import json

import pytest

from lit_junkie.paths import TEST_DIRECTORY


def open_file(file_path):
    with open(file_path, mode="r") as read_file:
        data = json.load(read_file)
    return data


@pytest.fixture
def response_data_fixture():
    data_path = TEST_DIRECTORY / "data" / "response.json"
    return open_file(data_path)


@pytest.fixture
def serialized_data_fixture():
    data_path = TEST_DIRECTORY / "data" / "serialized.json"
    return open_file(data_path)


@pytest.fixture
def good_search_response_fixture():
    data_path = TEST_DIRECTORY / "data" / "good_search_result_one.json"
    return open_file(data_path)
