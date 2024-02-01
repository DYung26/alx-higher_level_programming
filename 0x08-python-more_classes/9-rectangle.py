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
        number_of_instances (int): A class attribute representing
        the total number of instances of the Rectangle class
        currently in existence.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class."""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1
        type(self).print_symbol = Rectangle.print_symbol

    def __str__(self):
        """
        Returns a string rep. of the rectangle using '#' characters.

        The resulting string represents a visual depiction of the
        rectangle, where each '#' character corresponds to
        one unit of width, and newline characters separate each row
        of the rectangle.

        Returns:
            str: A string repping the visual rep. of the rectangle.
        """
        a = ""
        for i in range(self.__height):
            if self.__width == 0 or self.__height == 0:
                return a
            a += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                a += "\n"
        return str(a)

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        suitable for debugging and development purposes.

        The returned string includes the class name and the values of width
        and height.

        Returns:
            str: A string representation of the rectangle, in the format
            "Rectangle(width, height)".
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """
        Destructor method that prints a farewell message
        when the Rectangle object is deleted.

        This method is automatically called when the Rectangle object
        is about to be destroyed.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle,
                calculated as the product of width and height.
        """
        return self.__height*self.__width

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle,
                calculated as twice the sum of width and height.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__height+self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest Rectangle based on the area
        Args:
            rect_1: Rectangle instance
            rect_2: Rectangle instance different from rect_1
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        new_rect = cls()
        new_rect.width = size
        new_rect.height = size
        return new_rect
