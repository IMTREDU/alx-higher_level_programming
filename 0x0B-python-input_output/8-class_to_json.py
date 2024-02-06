#!/usr/bin/python3
"""
Module to convert an object of a class to a dictionary for JSON serialization.
"""

def class_to_json(obj):
    """
    Convert an object of a class to a dictionary for JSON serialization.

    Args:
        obj

    Returns:
        dict
    """
    attributes = obj.__dict__

    serializable_attributes = {}

    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[key] = value

    return serializable_attributes

if __name__ == "__main__":
    class_to_json()
