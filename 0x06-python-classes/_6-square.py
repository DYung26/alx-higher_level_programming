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
        position (tuple): ...
    Attributes:
        size (int): length of square
        position (tuple): ...
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Args: None
        Attributes: None
        Returns:
            position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Args:
            size (int): ...
            position (tuple): ...
        Attributes:
            position (tuple): ...
        """
        if isinstance(position, tuple) and \
           len(position) == 2 and \
           all(isinstance(elem, int) for elem in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            lj (int): ...
            k (int): ...
            i (int): ...
            position (tuple): ...
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0 and len(self.__position) == 2:
                print()
            else:
                pass
            lj = 0
            while lj < self.__size:
                k = 0
                while k < self.__position[0]:
                    print(" ", end="")
                    k += 1
                i = 0
                while i < self.__size:
                    print("#", end="")
                    i += 1
                print()
                lj += 1
