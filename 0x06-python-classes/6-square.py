#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self._size = size
        self._position = position

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

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        return self._size ** 2

    def my_print(self):
        if self._size == 0:
            print()
        else:
            for i in range(self._position[1]):
                print()
            for i in range(self._size):
                print(" " * self._position[0] + "#" * self._size)

