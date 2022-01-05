"""Functions used for searching Google Book API"""
import string
from typing import Optional

import requests

from .schemas import GoogleBookList


def strip_remove_punctuation(input_string: str) -> str:
    """Removes punctuation from the string.
    Removes the following punctuations: !"#$%&'()*+,-./:;<=>?@[]^_`{|}~\\

    Args:
        input_string (str): string to remove punctuation from.

    Returns:
        str: string without punctuation.
    """
    return input_string.translate(str.maketrans("", "", string.punctuation)).strip()


def replace_whitespaces_with_plus_signs(input_string: str) -> str:
    """Replaces whitespace with + sign. This is to separate search terms with + signs.
    https://developers.google.com/books/docs/v1/using#st_params

    Args:
        input_string (str): string to replace spaces with + signs.

    Returns:
        str: input_string with plus signs replaced with spaces.
    """
    output = " ".join(filter(lambda word: len(word) > 0, input_string.split(" ")))
    return output.replace(" ", "+")


def clean_subject(subject: str) -> str:
    """Clean subject string to prepare for url query.

    Example:
        input:
            "term1 term2  term3"
        output:
            "term1+term2+term3"

    Args:
        subject (str): string with multiple subjects to be cleaned.

    Returns:
        str: cleaned string with multiple subjects separated by + signs.
    """
    subject = strip_remove_punctuation(subject)
    return replace_whitespaces_with_plus_signs(subject)


def create_search_url(subject: str) -> Optional[str]:
    """Creates Google Books API search url with subject queries

    Args:
        subject (str): subjects to query googleapis

    Returns:
        Optional[str]: properly formatted url for
        None: if subject is malformed.
    """
    subject = clean_subject(subject)
    if len(subject) < 1:
        return None

    base_url = (
        f"https://www.googleapis.com/books/v1/volumes?q={subject}&maxResults=5&printType=books"
    )
    return base_url


def search_google_books(subject: str) -> Optional[GoogleBookList]:
    """Preforms a search for books that contain text strings related to the subject.

    Args:
        subject (str): subject to search google books for.

    Returns:
        Optional[GoogleBookList]: List of google book objects.
        None: if nothing was found or subject was malformed.
    """
    search_url = create_search_url(subject)
    if not search_url:
        return None

    response = requests.get(search_url)
    if not response.ok:
        return None

    data = response.json()
    if not data:
        return None

    total_items = data.get("totalItems")
    if not total_items:
        return None

    return GoogleBookList(**data)
