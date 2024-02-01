#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    A class with a restricted set of attributes using __slots__.

    Attributes:
    - first_name: A string representing the first name of an instance.

    Usage:
    obj = LockedClass()
    obj.first_name = "John"  # Valid assignment
    obj.last_name = "Doe"    # Raises AttributeError due to __slots__
    """

    __slots__ = ["first_name"]
