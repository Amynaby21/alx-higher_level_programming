#!/usr/bin/python3
"""Defines a class Square based on 2-square.py"""


class Square:
    """Defines a new square

    Args:
        size (int): size of the square
    """
    def __init__(self, size=0):
        """Initializes the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)