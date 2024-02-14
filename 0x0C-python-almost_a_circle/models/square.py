#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        width = size
        height = size
        super().__init__(width, height, x, y, id)
        self.__size = size        

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__size}"

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        attributeName = "width"
        Rectangle._Rectangle__check(value, attributeName)
        self.__size = value
