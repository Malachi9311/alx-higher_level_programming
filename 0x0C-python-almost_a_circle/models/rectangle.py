#!/usr/bin/python3
"""Defines a rectangle class that inherits 
from Base class
"""
from models.base import Base

class Rectangle(Base):
    """Represents a Rectangle object"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle object
        Args:
            width(int): Width of new Rectangle
            height(int): Height of new Rectangle
            x(int): x-coordinate of new Rectangle
            y(int): y-coordinate of new Rectangle
        Raises:
            TypeError: if any variable is not an integer
            ValueError: if any variable < 0
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of Rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set width of Rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x-coordinate"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Set x-coordinate"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y-coordinate"""
        return self.__y
    
    @y.setter
    def y(self,value):
        """Set y-coordinate"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        return self.__width * self.__height
    
    def display(self):
        """Print a Rectangle using the '#' character"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        
        [print("") for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print("")

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,self.__y,self.__width,self.__height)

    def update(self, *args, **kwargs):
        """Update the Rectangle
        Args:
            *args(int): New attribute values.
                -1st arg: id attribute
                -2nd arg: width attribute
                -3rd arg: height attribute
                -4th arg: x attribute
                -5th arg: y attribute
            
            *kwargs(dict): key/value pair attributes
        """
        if args and len(args) != 0:
            a = 0 #index number to iterate thru args
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.__width,self.__height,self.__x,self.__y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.__width = arg
                elif a == 2:
                    self.__height = arg
                elif a == 3:
                    self.__x = arg
                elif a == 4:
                    self.__y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.__width,self.__height,self.__x,self.__y)
                    else:
                        self.id == v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        return {
            "id":self.id,
            "width" : self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
