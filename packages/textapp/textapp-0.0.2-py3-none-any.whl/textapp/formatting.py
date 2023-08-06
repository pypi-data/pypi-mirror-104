"""
This file takes care of our text formatting for the textapp package.
"""

import os

# light means light screen, so dark text!
LIGHT = "light"
DARK = "dark"
GREEN = "green"
RED = "red"
BLACK = "black"
WHITE = "white"
MAGENTA = "magenta"
CYAN = "cyan"
YELLOW = "yellow"
BLUE = "blue"
BOLD = "bold"
REVERSED = "reverse"

TEXT_MENU_MODE = "TEXT_MENU_MODE"

DEF_SEP_LEN = 60
DEF_SEP_CHAR = '*'

color_scheme = os.getenv(TEXT_MENU_MODE, DARK)  # some default!

HAS_TERMCOLOR = True
try:
    from termcolor import colored
except ImportError:
    HAS_TERMCOLOR = False


SEPERATOR = "SEPERATOR"
TITLE = "TITLE"
TEXT = "TEXT"
MENU_CHOICE = "MENU_CHOICE"
DEF_MARKER = "DEF_MARKER"

DARK_SCHEME = {
    SEPERATOR: {'color': GREEN, 'attrs': None},
    TITLE: {'color': YELLOW, 'attrs': [BOLD]},
    TEXT: {'color': YELLOW, 'attrs': [BOLD]},
    MENU_CHOICE: {'color': CYAN, 'attrs': [BOLD]},
    DEF_MARKER: {'color': YELLOW, 'attrs': [BOLD, REVERSED]},
}

LIGHT_SCHEME = {
    SEPERATOR: {'color': RED, 'attrs': None},
    TITLE: {'color': GREEN, 'attrs': [BOLD]},
    TEXT: {'color': GREEN, 'attrs': [BOLD]},
    MENU_CHOICE: {'color': BLUE, 'attrs': [BOLD]},
    DEF_MARKER: {'color': GREEN, 'attrs': [BOLD, REVERSED]},
}

color_map = DARK_SCHEME if color_scheme == DARK else LIGHT_SCHEME


def fmt_text(text, elem=TEXT):
    if HAS_TERMCOLOR:
        text = colored(text, color_map[elem]['color'],
                       attrs=color_map[elem]['attrs'])
    return text


def menu_choice(text):
    return fmt_text(text, elem=MENU_CHOICE)


def text(text):
    return fmt_text(text, elem=TEXT)


def marker(text):
    return fmt_text(text, elem=DEF_MARKER)


def sep(char=DEF_SEP_CHAR, length=DEF_SEP_LEN):
    return fmt_text(char*length, elem=SEPERATOR)


def title(text, sep_char=DEF_SEP_CHAR, sep_length=DEF_SEP_LEN):
    seper = f"{sep(char=DEF_SEP_CHAR, length=DEF_SEP_LEN)}"
    text = fmt_text(text, elem=TITLE)
    return f"\n{seper}\n{text}\n{seper}\n"


def main():
    print(title("Does this title get printed?"))


if __name__ == "__main__":
    main()
