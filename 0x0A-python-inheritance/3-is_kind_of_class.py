#!/usr/bin/python3
"""Defines a function to determine if an object is an instance or inherited instance of a class."""

def is_kind_of_class(obj, target_class):
    """Check if an object is an instance or inherited instance of a specific class.

    Args:
        obj (any): The object to examine.
        target_class (type): The class to match the type of obj to.
    Returns:
        True if obj is an instance or inherited instance of target_class, otherwise False.
    """
    return isinstance(obj, target_class)
