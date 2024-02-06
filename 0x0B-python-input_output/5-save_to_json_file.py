#!/usr/bin/python3
"""
Module to save an object to a text file using JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """
    Save an object to a text file using JSON representation.

    Args:
        my_obj
        filename (str)

    Returns:
        None
    """
    import json
    with open(filename, mode='w', encoding="utf-8") as file:
        json.dump(my_obj, file)


if __name__ == "__main__":
    save_to_json_file()
