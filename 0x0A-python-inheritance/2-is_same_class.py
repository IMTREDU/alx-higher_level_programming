#!/usr/bin/python3
"""Defines a function to verify if an object belongs to a specific class."""

def is_same_class(obj, target_class):
    """Check if the type of an object matches a given class.

    Args:
        obj (any): The object to examine.
        target_class (type): The class to compare the object's type to.
    Returns:
        True if the object is precisely an instance of the target_class, otherwise False.
    """
    return type(obj) == target_class
