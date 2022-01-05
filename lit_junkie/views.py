"""Views Module"""
from abc import ABC, abstractmethod
from enum import Enum
from collections import defaultdict

from . import prompt, search, storage
from .schemas import GoogleBookList


class Route(str, Enum):
    """Enum used to routed to next view."""

    Main = "Main"
    Search = "Search"
    ReadingList = "ReadingList"
    Quit = "Quit"

    @property
    def name(self):
        """Helper method to get the value."""
        return self.value


class View(ABC):
    """Abstract View class used to standardize how views are displayed"""

    @property
    def name(self):
        """Helper method to get the view name."""
        return self.__class__.__name__

    def display_header(self):
        """Displays the view header."""
        prompt.clear_screen()
        prompt.show_logo()
        prompt.show_header(self.name)

    @abstractmethod
    def display():
        """Abstract method to make sure all views have a display method."""
        pass


class Main(View):
    """Main View Page"""

    router = defaultdict(lambda: Route.Quit)

    def display(self):
        """Displays the Main Menu"""
        self.display_header()

        menu = ["BOOK SEARCH"]
        self.router[0] = Route.Search

        if storage.exists():
            menu.append("READING LIST")
            self.router[1] = Route.ReadingList

        menu.append("QUIT")

        choices = prompt.show_menu_items(menu)
        selected = prompt.select_prompt(choices)
        return self.router[selected]


class Quit(View):
    """Program Quit Page"""

    def display(self):
        prompt.clear_screen()
        print("Good bye. Hope to see you back soon.")


class Search(View):
    """Search View Page"""

    def display(self):
        """Displays the Search Menu"""
        self.display_header()

        query = prompt.search_prompt("Please input your query.")
        found_books = search.search_google_books(query)

        if not found_books:
            print("No books found.")
            prompt.continue_prompt()
            return Route.Main

        self.display_header()

        print("Which book would you like to store?\n")
        found_books.pretty_print()

        print(f"[{len(found_books)}]", "Go back to Main Menu\n")
        print(f"[{len(found_books) + 1}]", "Quit\n")

        choices = list(range(len(found_books) + 2))

        selected = prompt.select_prompt(choices)

        if selected == len(found_books):  # last menu option.
            return Route.Main
        if selected == len(found_books) + 1:  # last menu option.
            return Route.Quit

        reading_list = storage.load_books()

        selected_book = found_books[selected]

        if not reading_list:
            reading_list = GoogleBookList(books=[selected_book])
        else:
            reading_list.append(selected_book)

        storage.store_books(reading_list)

        return Route.ReadingList


class ReadingList(View):
    """Reading List View Page"""

    def display(self):
        """Displays the Reading List Menu"""
        self.display_header()

        reading_list = storage.load_books()
        reading_list.pretty_print()

        prompt.continue_prompt()

        return Route.Main


ALL_VIEWS = [Main(), Search(), ReadingList(), Quit()]
