import os
import time
from abc import ABC
from pathlib import Path
from typing import Set

from lit_junkie.logo import LOGO
from lit_junkie.paths import STORAGE_PATH
from lit_junkie.schemas import GoogleBookList
from lit_junkie.search import clean_subject, create_search_url, search_google_books
from lit_junkie.storage import drop_books, load_books, store_books


def clear_screen(header=None):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    if header:
        print(header)


clear_screen(header=LOGO)
time.sleep(1)

book_list = search_google_books("star    %& ! wars")

for book in book_list:
    print(book.authors)
    print(book.title)
    print(book.publisher)
    print()
# for index, book in enumerate(book_list.dict().items()):
# print(book)
# print(f"[{index}]")
# print(book.book.title)
# print(" ".join(book.book.authors))
# print(book.book.publisher)
# print()
# clear_screen(header=books)

# MAIN_MENU = "main"


# MAIN_MENU = """
# 1. Book Search
# 2. View Reading List
# 3. Dump Reading List
# """

# print(MAIN_MENU)
