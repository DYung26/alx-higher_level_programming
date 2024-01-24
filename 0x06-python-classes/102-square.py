#!/usr/bin/python3
"""
A module that defines a class Square
"""


class Square:
    """
    Class Square

    Attributes:
        size (int): Length of a side of the square.
    """
    def __init__(self, size=0):
        """
        The __init__ method initializes the attributes that are instantiated whenever an object is created.

        Args:
            size (int): Length of a side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """
        Private instance attribute: size
        """
    def area(self):
        """
        Calculates the area of the square

        Returns:
            Area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter method that returns the size

        Returns:
            Size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method that sets the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, value):
        return self.__size < value.size

    def __le__(self, value):
        return self.__size <= value.size

    def __eq__(self, value):
        return self.__size == value.size

    def __ne__(self, value):
        return self.__size != value.size

    def __ge__(self, value):
        return self.__size >= value.size

    def __gt__(self, value):
        return self.__size > value.size
