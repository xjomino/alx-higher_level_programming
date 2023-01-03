#!/usr/bin/python3
"""
    Module contains of a single class
"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing of a new instance of  data"""
        if not isinstance(width, (int, float)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves of `width` value """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of atribute `width` to a new value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves `height` value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets atribute `height` to a new value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """print the rectangle with the character `#` """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.width] * self.height)

    def __repr__(self):
        """return a string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
