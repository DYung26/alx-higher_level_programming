#!/usr/bin/python3
"""
Square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        width = size
        height = size
        super().__init__(width, height, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        attributeName = "width"
        Rectangle._Rectangle__check(value, attributeName) # super().__check(value, attributeName)
        self.width = value
        attributeName = "height"
        Rectangle._Rectangle__check(value, attributeName)
        self.height = value

    def update(self, *args, **kwargs):
        """if args:
            super().update(*args)
        """
        if args:
            try:
                self.id = args[0]
            except IndexError:
                pass
            try:
                self.size = args[1]
            except IndexError:
                pass
            try:
                self.x = args[2]
            except IndexError:
                pass
            try:
                self.y = args[3]
            except IndexError:
                pass
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
