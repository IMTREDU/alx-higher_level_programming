#!/usr/bin/python3
"""Defines a function to check if an object is an inherited instance of a class."""

def inherits_from(obj, target_class):
    """Check if an object is an inherited instance of a specific class.

    Args:
        obj (any): The object to examine.
        target_class (type): The class to match the type of obj to.
    Returns:
        True if obj is an inherited instance of target_class, otherwise False.
    """
    return issubclass(type(obj), target_class) and type(obj) != target_class
