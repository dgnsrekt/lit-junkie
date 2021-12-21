"""Schema for google books."""
from typing import List, Optional

from pydantic import BaseModel as Schema
from pydantic import Field


class Book(Schema):
    """Basic book information

    Args:
        title (str): title of the book.
        authors (List[str]): list of book authors
        publisher (str): the books publisher
    """

    title: str
    authors: Optional[List[str]]
    publisher: Optional[str]


class GoogleBook(Schema):
    """A single google book api response

    Args:
        book (Book): Basic book information
    """

    book: Book = Field(alias="volumeInfo")

    @property
    def title(self) -> str:
        """Helper which allows for querying books `title`

        Returns:
            str: book `title`
        """
        return self.book.title

    @property
    def authors(self) -> Optional[str]:
        """Helper which allows for querying books `authors`

        Returns:
            str: book `authors`
            None: if authors don't exists.
        """

        if self.book.authors:
            return " ".join(self.book.authors)
        return None  # TODO: Empty list maybe useful here.

    @property
    def publisher(self):
        """Helper which allows for querying books `publisher`

        Returns:
            str: book `publisher`
        """
        return self.book.publisher

    class Config:
        """pydantic config"""

        allow_population_by_field_name = True


class GoogleBookList(Schema):
    """List of Google Book Objects"""

    books: List[GoogleBook] = Field(alias="items")

    def __len__(self):
        """Amount of books in list"""
        return len(self.books)

    def __iter__(self):
        """Iterate over the books in the list"""
        return iter(self.books)

    class Config:
        """pydantic config"""

        allow_population_by_field_name = True
