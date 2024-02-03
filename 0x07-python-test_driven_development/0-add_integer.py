#!/usr/bin/python3
"""Defines the add_integer function.
Functions:
    add_integer(a, b=98): Adds two numbers and returns the result.
If executed as a standalone script, it runs doctests from the 0-add_integer.txt file.
"""


def add_integer(a, b=98):
    """Returns:
        int: The sum of the two input numbers, a and b, as an integer.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
