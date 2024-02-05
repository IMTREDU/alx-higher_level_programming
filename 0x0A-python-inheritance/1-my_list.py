#!/usr/bin/python3
"""Module defining the MyList class."""

class MyList(list):
    """Custom MyList class that extends the built-in list class."""

    def print_sorted(self):
        """Prints the elements of the list in sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
