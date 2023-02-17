#!/usr/bin/python3
"""Define a Square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represent a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size(int): Size of new square
            x(int): x-coordinate of square
            y(int): y-coordinate of square
        """
        super().__init__(size,size,x,y,id)

    @property
    def size(self):
        """Getter for size"""
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and the str() representation of a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
    
    def update(self, *args, **kwargs):
        """Update the square
        Args:
            *args(int) : New attribute values
                -1st arg: id attribute
                -2nd arg: size attribute
                -3rd arg: x attribute
                -4th arg: y attribute
            **kwargs(dict): key/value pair attributes
        """

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size,self.x,self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size,self.x,self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y 
        }
