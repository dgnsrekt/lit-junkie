"""Schema for google books."""
from typing import Iterable, List, Optional

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
            return ", ".join(self.book.authors)
        return None

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

    def __len__(self) -> int:
        """Amount of books in list"""
        return len(self.books)

    def __iter__(self) -> Iterable:
        """Iterate over the books in the list"""
        return iter(self.books)

    def pretty_print(self):
        """Pretty print each book in the list"""
        for index, book in enumerate(self):
            selector = f"[{index}]"
            space = " " * len(selector)
            print(selector, "Title:    ", book.title)
            print(space, "Authors:  ", book.authors)
            print(space, "Publisher:", book.publisher)
            print()

    def __getitem__(self, index: int) -> GoogleBook:
        """Get GoogleBook by index"""
        return self.books[index]

    def append(self, book: GoogleBook) -> None:
        """Append GoogleBook to GoogleBookList"""
        self.books.append(book)

    class Config:
        """pydantic config"""

        allow_population_by_field_name = True
