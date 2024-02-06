#!/usr/bin/python3
"""
Module to convert an object to its JSON representation.
"""


def to_json_string(my_obj):
    """
    Convert an object to its JSON representation.

    Args:
        my_obj

    Returns:
        str
    """
    import json
    return json.dumps(my_obj)


if __name__ == "__main__":
    to_json_string()
