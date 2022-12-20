#!/usr/bin/python3
"""Defines a class Square based on 3-square.py"""


class Square:
    """Defines a new square

    Args:
        size (int): size of the square
    """
    def __init__(self, size=0):
        """Initializes the square"""
        self.size = size

    @property
    def size(self):
        """Set the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return (self.__size * self.__size)
