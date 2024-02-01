#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Args: None
Attributes: None
"""


class Rectangle:
    """
    Represents a rectangle with specified width and height.

    Args:
        width (int, optional): The width of the rectangle. Defaults to 0.
        height (int, optional): The height of the rectangle. Defaults to 0.

    Attributes:
        __width (int): width of Rectangle
        __height (int): height of Rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
