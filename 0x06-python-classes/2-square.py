#!/usr/bin/python3
'''Create a Class for Square size'''


class Square:
    '''Class of a Square'''

    def __init__(self, size=0):
        '''Instantiaion of a square with size'''
        if (type(size) is not int):
            raise (TypeError("size must be integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size
