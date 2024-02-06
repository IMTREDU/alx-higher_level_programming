#!/usr/bin/python3
"""
Module to create an object from a JSON file.
"""


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str)

    Returns:
        object
    """
    import json
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    load_from_json_file()
