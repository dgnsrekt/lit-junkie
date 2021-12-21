"""tests search module methods"""
import pytest

from lit_junkie import search

SUBJECT_DATA = [
    (" super & man ", "super+man"),
    (" @#$@$@#$@ ", ""),
    ("The C Programming Language ! ", "The+C+Programming+Language"),
    ("The Rust Programming Language?&@*#$ ", "The+Rust+Programming+Language"),
]


@pytest.mark.parametrize("subject,expected", SUBJECT_DATA)
def test_clean_subject(subject, expected):
    result = search.clean_subject(subject)
    assert result == expected
