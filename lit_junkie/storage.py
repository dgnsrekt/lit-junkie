"""Book data storage."""
import pickle
from pathlib import Path

from .paths import STORAGE_PATH
from .schemas import GoogleBookList


def exists(path: Path = STORAGE_PATH):
    """Helper function to check if reading list path exists."""
    return path.exists()


def load_books(path: Path = STORAGE_PATH) -> GoogleBookList:
    """Loads books from pickle file.

    Args:
        path (Path, optional): File to load pickled book data. Defaults to STORAGE_PATH.

    Returns:
        GoogleBookList: List of de-serialized Google Book Data.
        None: if path doesn't exist.
    """
    if not exists(path):
        return None

    with open(path, mode="rb") as file:
        book_list = pickle.load(file)

    return book_list


def store_books(book_list: GoogleBookList, path: Path = STORAGE_PATH) -> None:
    """Pickles and stores list of books.

    Args:
        book_list (GoogleBookList): List of google books to store
        path (Path, optional): File to store pickled book data. Defaults to STORAGE_PATH.
    """
    with open(path, mode="wb") as file:
        pickle.dump(book_list, file)


def drop_books(path: Path = STORAGE_PATH) -> None:
    """Removes list of books

    Args:
        path (Path, optional): File to remove. Defaults to STORAGE_PATH.
    """
    path.unlink(missing_ok=True)
