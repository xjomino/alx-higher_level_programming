#!/usr/bin/python3
"""define class Square"""


class Square:
    """Defines a square:"""

    def __init__(self, size=0):
        """Initializer object"""

        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """return area of the Square in the atribute private __size"""

        return self._size ** 2

    def my_print(self):
        """Print a square with self.__size"""
        if self._size == 0:
            print()
        else:
            for i in range(self._size):
                print("#" * self._size)
