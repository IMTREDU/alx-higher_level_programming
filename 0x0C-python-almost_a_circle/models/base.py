#!/usr/bin/python3
"""Module defining Base class"""

import json

class Base:
    """Base class for managing IDs"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance

        Args:
            id (int): Optional ID of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert list of dictionaries to JSON string

        Args:
            list_dictionaries (list): List of dictionaries

        Returns:
            str: JSON string representation of the list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list of objects to a file in JSON format

        Args:
            list_objs (list): List of objects to be saved
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dictionary_list = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(dictionary_list)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Convert JSON string to list of dictionaries

        Args:
            json_string (str): JSON string representing a list of dictionaries

        Returns:
            list: List of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance

        Args:
            **dictionary: Dictionary containing attribute values

        Returns:
            Base: Instance with attributes set according to the dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise TypeError("Unknown class type")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load list of instances from file.

        Returns:
            list: List of instances loaded from file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionary_list = cls.from_json_string(json_string)
                instance_list = [cls.create(**d) for d in dictionary_list]
                return instance_list
        except FileNotFoundError:
            return []

if __name__ == "__main__":
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))
