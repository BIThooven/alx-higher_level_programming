#!/usr/bin/python3


class Square:
    """Class for a Square"""
    def __init__(self, size=0):
        """Initialize a class for a square with size"""
        self.size = size

    @property
    def size(self):
        """get size of a square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size of a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of a square"""
        return (self.__size * self.__size)
