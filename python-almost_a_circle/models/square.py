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

    def __str__(self):
        """return square representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y}"\
            f" - {self.width}"
