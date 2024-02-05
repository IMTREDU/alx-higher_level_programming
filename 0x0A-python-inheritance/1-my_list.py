#!/usr/bin/python3
"""Defines a subclass MyList inherited from the built-in list class."""

class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
