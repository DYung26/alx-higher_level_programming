#!/usr/bin/python3
"""
Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the rectangle.
        y (int): Y-coordinate of the rectangle.
    Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the rectangle.
        y (int): Y-coordinate of the rectangle.
        id (int): Identifier of the rectangle.

    Methods:
        __init__: Initializes a new Rectangle instance.
        __str__: Returns a string representation of the rectangle.
        __check: Validates and checks the correctness of attribute values.
        width: Getter method for width attribute.
        width: Setter method for width attribute.
        height: Getter method for height attribute.
        height: Setter method for height attribute.
        x: Getter method for x attribute.
        x: Setter method for x attribute.
        y: Getter method for y attribute.
        y: Setter method for y attribute.
        area: Calculates and returns the area of the rectangle.
        display: Displays the rectangle using '#' characters.
        update: Updates the attributes of the rectangle.
        to_dictionary: Returns a dictionary representation of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
            id (int): Identifier of the rectangle.
        """
        self.__check(width, "width")
        self.__check(height, "height")
        self.__check(x, "x")
        self.__check(y, "y")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} "\
                "- {self.__width}/{self.__height}"

    @staticmethod
    def __check(value, attributeName):
        """
        Static method to validate the correctness of attribute values.

        Args:
            value: The value to be checked.
            attributeName (str): The name of the attribute being checked.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attributeName} must be an integer")
        if attributeName in ("height", "width"):
            if value <= 0:
                raise ValueError(f"{attributeName} must be > 0")
        if attributeName in ("x", "y"):
            if value < 0:
                raise ValueError(f"{attributeName} must be >= 0")

    @property
    def width(self):
        """
        Getter method for width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute.

        Args:
            value (int): The new width value for the rectangle.
        """
        self.__check(value, "width")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute.

        Args:
            value (int): The new height value for the rectangle.
        """
        self.__check(value, "height")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for x attribute.

        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for x attribute.

        Args:
            value (int): The new x-coordinate value for the rectangle.
        """
        self.__check(value, "x")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for y attribute.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y attribute.

        Args:
            value (int): The new y-coordinate value for the rectangle.
        """
        self.__check(value, "y")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle using '#' characters.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        Args:
            *args: Variable number of positional arguments.
            **kwargs: Variable number of keyword arguments.
        """
        if args:
            try:
                self.id = args[0]
            except IndexError:
                pass
            try:
                self.__width = args[1]
            except IndexError:
                pass
            try:
                self.__height = args[2]
            except IndexError:
                pass
            try:
                self.__x = args[3]
            except IndexError:
                pass
            try:
                self.__y = args[4]
            except IndexError:
                pass
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle.

        Returns:
            dict: A dictionary containing the attributes of the rectangle.
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
