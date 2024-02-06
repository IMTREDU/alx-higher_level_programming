#!/usr/bin/python3
"""
Module to write a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written.

    Args:
        filename (str)
        text (str)

    Returns:
        int
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    write_file()
