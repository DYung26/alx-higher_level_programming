#!/usr/bin/python3
# -*- coding_ utf-8 -*-
"""
Args: None
Attributes: None
"""


class Square:
    """
    Args:
        size (int): length of square
    Attributes:
        size (int): length of square
    """
    def __init__(self, size=0):
        self.__size = size

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
        Args:
        value (int): userInputted length of square
    Attributes:
        value (int): userInputted length of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns:
            Area
        """
        return self.__size**2

    def my_print(self):
        """
        Attributes:
            size (int): length of square
        """
        if self.__size == 0:
            print("")
        else:
            j = 0
            while j < self.__size:
                i = 0
                while i < self.__size:
                    print("#", end="")
                    i+=1
                j+=1
                print("")
