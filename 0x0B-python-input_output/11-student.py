#!/usr/bin/python3
"""
Module to define the Student class with methods for serialization and deserialization
"""

class Student:
    """
    Student class to represent a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance

        Args:
            attrs (list, optional)

        Returns:
            dict
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance using a dict rep

        Args:
            json (dict)
        """
        for key, value in json.items():
            setattr(self, key, value)
