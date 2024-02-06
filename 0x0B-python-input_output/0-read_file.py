#!/usr/bin/python3
"""
Module to read and print the contents of a text file.
"""


def read_file(filename=""):
    """
    Read and print the contents of a text file.

    Args:
        filename (str)

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")


if __name__ == "__main__":
    read_file()
