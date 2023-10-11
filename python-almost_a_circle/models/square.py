#!/usr/bin/python3
"""
lsadgfshgjhdfhdgseasrdtfjyfjthrgaestr\
    dgfesasrgdhftrgserawestrdytfrte
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """yuitueryetawtrtyueyryet"""
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size
        self.size = size

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """return square representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y}"\
            f" - {self.width}"

    def update(self, *args, **kwargs):
        """update method"""
        for i, kargs in kwargs.items():
            if i == "id":
                self.id = kargs
            elif i == "size":
                self.size = kargs
            elif i == "x":
                self.x = kargs
            elif i == "y":
                self.y = kargs
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            elif i == 1:
                self.size = arg
            elif i == 2:
                self.x = arg
            elif i == 3:
                self.y = arg
