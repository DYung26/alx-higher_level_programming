#!/usr/bin/python3
# -*- coding_ utf-8 -*-
"""
Args: None
Attributes: None
"""


class Square:
    """
    Args:
        size (int): lenght of square
    Attributes:
        size (int): lenght of square
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """
        Returns:
            Area
        """
        return self.__size**2

    @property
    def size(self):
        """
        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
