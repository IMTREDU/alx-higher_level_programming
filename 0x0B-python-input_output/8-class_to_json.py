#!/usr/bin/python3
"""
Module to convert an object of a class to a dictionary for JSON serialization.
"""



def class_to_json(obj):
    """
    Convert an object of a class to a dictionary for JSON serialization. 
    """
    return obj.__dict__
