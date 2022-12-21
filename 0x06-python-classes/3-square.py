#!/usr/bin/python3
"""define class Square"""


class Square:
    """Defines a square:"""

    def __init__(self, size=0):
        """Initializer object"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        """return area of the Square in the atribute
        private __size"""

        return self._size ** 2
