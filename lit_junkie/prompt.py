import os
import time
from typing import List

from . import search
from .logo import LOGO, LOGO_WIDTH


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


def show_menu_items(menu_items: List[str]) -> List[int]:
    """Helper function to display menu choices"""
    if not menu_items:
        raise ValueError("Menu items must exist.")

    for index, selection in enumerate(menu_items):
        print(f"[{index}]", selection)
    print()

    return list(range(len(menu_items)))


def select_prompt(choices: List[str]):
    """Prompts user to select from a list of choices"""
    print("Please select from", choices)
    user_input = input("> ")
    if user_input.isdigit():
        user_input = int(user_input)
    if user_input in choices:
        return user_input
    print("Invalid input.")
    return select_prompt(choices)


def search_prompt(infomation):
    """Prompts user for search subject."""
    print(infomation)
    user_input = input("> ")
    output = search.clean_subject(user_input)
    if len(output) > 0:
        return output
    print("Invalid input.")
    return search_prompt(infomation)
