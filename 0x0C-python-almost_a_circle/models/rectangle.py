#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
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
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    @staticmethod
    def __check(value, attributeName):
        if not isinstance(value, int):
            raise TypeError(f"{attributeName} must be an integer")
        if attributeName == "height" or attributeName == "width":
            if value <= 0:
                raise ValueError(f"{attributeName} must be > 0")
        if attributeName == "x" or attributeName == "y":
            if value < 0:
                raise ValueError(f"{attributeName} must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__check(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__check(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__check(value, "x")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__check(value, "y")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args):
        