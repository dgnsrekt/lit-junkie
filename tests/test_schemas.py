from lit_junkie.schemas import GoogleBookList

from .common import response_data_fixture, serialized_data_fixture


def test_google_book_list_schema_one(response_data_fixture):
    book_list = GoogleBookList(**response_data_fixture)
    assert len(book_list) == 5


def test_google_book_list_schema_two(response_data_fixture, serialized_data_fixture):
    book_list = GoogleBookList(**response_data_fixture)
    assert book_list.dict() == serialized_data_fixture
