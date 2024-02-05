#!/usr/bin/python3
"""Defines a function for looking up object attributes."""

def lookup(obj):
    """Retrieve a list of available attributes for an object."""
    return dir(obj)
