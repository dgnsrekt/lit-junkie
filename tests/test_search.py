"""tests search module methods"""
import pytest

from lit_junkie import search
from .common import good_search_response_fixture

SUBJECT_DATA = [
    (" super & man ", "super+man"),
    (" @#$@$@#$@ ", ""),
    ("The C Programming Language ! ", "The+C+Programming+Language"),
    ("The Rust Programming Language?&@*#$ ", "The+Rust+Programming+Language"),
]


@pytest.mark.parametrize("subject,expected", SUBJECT_DATA)
def test_clean_subject(subject, expected):
    """Tests clean subject function properly creates search queries."""
    result = search.clean_subject(subject)
    assert result == expected


def test_good_search_returns_google_books(good_search_response_fixture):
    """Test search google books returns the correct response"""
    result = search.search_google_books("kevin")
    expected = good_search_response_fixture
    assert result == expected


def test_bad_search_returns_none():
    result = search.search_google_books("dafbohdfb")
    assert result == None
