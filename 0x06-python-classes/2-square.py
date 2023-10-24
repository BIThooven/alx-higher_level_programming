#!/usr/bin/python3
'''Create a Class for Square size'''


class Square:
    '''Class of a Square'''
    def __init__(self, size=0):
        '''Initialize a Class

        Args:
            size (int): The size of the square
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size == size
