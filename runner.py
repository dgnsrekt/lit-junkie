import os
import time
from abc import ABC
from pathlib import Path
from typing import Set, List

from requests.api import head
from requests.sessions import extract_cookies_to_jar

from lit_junkie.logo import LOGO, LOGO_WIDTH
from lit_junkie.paths import STORAGE_PATH
from lit_junkie.schemas import GoogleBookList
from lit_junkie.search import clean_subject, create_search_url, search_google_books
from lit_junkie.storage import drop_books, load_books, store_books


def clear_screen():
    """Clears Screen"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def show_logo():
    """Displays Logo"""
    time.sleep(0.5)
    print(LOGO)


def show_header(header: str) -> None:
    """Displays menu headers"""

    header = header + " Menu"
    if len(header) > LOGO_WIDTH:
        raise ValueError("Header too long.")

    logo_header_difference = LOGO_WIDTH - len(header)
    spaces = " " * (logo_header_difference // 2)

    print("=" * LOGO_WIDTH)
    print(spaces + header)
    print("=" * LOGO_WIDTH)
    print("Press (CTRL + C) to exit the application.")
    print()


def show_menu_items(menu_items: List[str]):
    if not menu_items:
        raise ValueError("Menu items must exist.")

    for index, selection in enumerate(menu_items):
        print(f"[{index}]", selection)
    print()

    return list(range(len(menu_items)))


def select_prompt(choices: List[str]):
    print("Please select from", choices)
    user_input = input("> ")
    if user_input.isdigit():
        user_input = int(user_input)
    if user_input in choices:
        return user_input
    print("Invalid input.")
    return select_prompt(choices)


from abc import ABC, abstractmethod, abstractclassmethod
from enum import Enum


class Routes(str, Enum):
    MainMenu = "MainMenu"
    SearchMenu = "SearchMenu"
    ReadingListMenu = "ReadingListMenu"


class View(ABC):
    @property
    def view_name(self):
        return self.__class__.__name__

    @property
    def header(self):
        title, _ = self.view_name.split("Menu")
        return title

    @abstractmethod
    def display():
        pass


class MainMenu(View):
    router = {0: Routes.SearchMenu, 1: Routes.ReadingListMenu}

    def display(self):
        clear_screen()
        show_logo()
        show_header(self.header)

        menu = ["BOOK SEARCH"]

        if STORAGE_PATH.exists():
            menu.append("READING LIST")

        choices = show_menu_items(menu)
        selected = select_prompt(choices)
        return self.router[selected]


def search_prompt(infomation):
    print(infomation)
    user_input = input("> ")
    output = clean_subject(user_input)
    if len(output) > 0:
        return output
    print("Invalid input.")
    return search_prompt(infomation)


class SearchMenu(View):
    def display(self):
        clear_screen()
        show_logo()
        show_header(self.header)

        query = search_prompt("Please input your query.")
        books = search_google_books(query)

        books.pretty_print()

        book_count = len(books)
        print(f"[{book_count}]", "Go back to Main Menu\n")
        print("Which book would you like to store?\n")

        choices = list(range(book_count + 1))
        selected = select_prompt(choices)

        if selected == book_count:
            return Routes.MainMenu

        reading_list = load_books()
        selected_book = books[selected]

        if not reading_list:
            reading_list = GoogleBookList(books=[selected_book])
        else:
            reading_list.append(selected_book)

        store_books(reading_list)

        return Routes.ReadingListMenu


class ReadingListMenu(View):
    def display(self):
        clear_screen()
        show_logo()
        show_header(self.header)

        reading_list = load_books()
        reading_list.pretty_print()
        input("Hit Enter to Go Back to the Main Menu")
        return Routes.MainMenu


start = MainMenu()
VIEWS = [MainMenu(), SearchMenu(), ReadingListMenu()]
next_route = start.display()

while True:
    for view in VIEWS:
        if next_route.value == view.view_name:
            next_route = view.display()
            break
