#!/usr/bin/python3
"""
Square module

This module defines the Square class, which is a subclass of Rectangle.
The Square class represents a square shape and inherits attributes and methods
from the Rectangle class. It introduces additional methods specific to squares.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class representing a square shape.

    Args:
        size (int): The size of the square.
        x (int): The x-coordinate of the square (default is 0).
        y (int): The y-coordinate of the square (default is 0).
        id (int): The identifier of the square (default is None).

    Attributes:
        All attributes of the Rectangle class,
        as Square is a subclass of Rectangle.

    Methods:
        __init__: Initializes a new Square instance.
        __str__: Returns a string representation of the Square instance.
        size (property): Gets the size of the square.
        size (setter): Sets the size of the square.
        update: Updates the Square instance with new values.
        to_dictionary: Returns the dictionary representation
        of the Square instance.
    """

    def __init__(self, size, x=0, y=0, id=None):
        width = size
        height = size
        super().__init__(width, height, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: A string representing the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.
        """
        attributeName = "width"
        Rectangle._Rectangle__check(value, attributeName)
        # super().__check(value, attributeName)
        self.width = value
        attributeName = "height"
        Rectangle._Rectangle__check(value, attributeName)
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the Square instance with new values.

        Args:
            *args: Variable positional arguments.
            **kwargs: Variable keyword arguments.

        Note:
            If both args and kwargs are provided, args take precedence.

        Example:
            update(10, x=5, y=3) will update id to 10, x to 5, and y to 3.
        """
        """if args:
            super().update(*args)
        """
        if args:
            try:
                self.id = args[0]
            except IndexError:
                pass
            try:
                self.size = args[1]
            except IndexError:
                pass
            try:
                self.x = args[2]
            except IndexError:
                pass
            try:
                self.y = args[3]
            except IndexError:
                pass
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square instance.

        Returns:
            dict: A dictionary containing the attributes of the
            Square instance.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
