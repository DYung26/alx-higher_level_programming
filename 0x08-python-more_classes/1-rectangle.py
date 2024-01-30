#!/usr/bin/python3
"""
Args: None
Attributes: None
"""


class Rectangle:
    """
    Represents a rectangle with specified width and height.

    Attributes:
        __width (int): width of Rectangle
        __height (int): height of Rectangle
    Args:
        width (int, optional): The width of the rectangle. Defaults to 0.
        height (int, optional): The height of the rectangle. Defaults to 0.
    """

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class."""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
