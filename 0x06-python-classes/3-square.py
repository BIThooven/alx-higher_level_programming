#!/usr/bin/python3
"""Create a Class for square with size and area"""


class Square:
    """Class of Square"""
    def __init__(self, size=0):
        """Initialize a Class for Square with size"""
        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """The method to get the area of a square"""
        return (self.__size ** 2)
