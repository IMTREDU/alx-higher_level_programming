#!/usr/bin/python3
"""
Module to convert a JSON string to an object (Python data structure)
"""


def from_json_string(my_str):
    """
    Convert a JSON string to an object (Python data structure)

    Args:
        my_str (str)

    Returns:
        object
    """
    import json
    return json.loads(my_str)


if __name__ == "__main__":
    from_json_string()
