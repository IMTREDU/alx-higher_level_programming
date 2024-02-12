#!/usr/bin/python3
"""Module defining Square class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance

        Args:
            size (int): Size of the square.
            x (int): X coordinate of the square (default = 0)
            y (int): Y coordinate of the square (default = 0)
            id (int): Optional. ID of the square (default = None)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the square

        Args:
            *args (int): List of arguments in the order: id, size, x, y
            **kwargs (dict): Dictionary of key-value pairs representing attributes
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """Return string representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

if __name__ == "__main__":
    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)
