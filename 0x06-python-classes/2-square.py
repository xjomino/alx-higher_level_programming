#!/usr/bin/python3
"""define class Square"""


class Square:
    """define Square"""

    def __init__(self, size=0):
        """initializer object"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size