#!/usr/bin/python3
"""
Module to append a string to the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file and return the num.

    Args:
        filename (str)
        text (str)

    Returns:
        int
    """
    with open(filename, mode='a', encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    append_write()
