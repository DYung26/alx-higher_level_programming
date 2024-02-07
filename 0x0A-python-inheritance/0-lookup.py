#!/usr/bin/python3

def lookup(obj):
    """
    Function to inspect and retrieve the attributes
    and methods of an object.

    Parameters:
    - obj: Any Python object for which you want to retrieve attributes
    and methods.

    Returns:
    - List of strings: A sorted list containing the names of attributes
    and methods of the provided object.
    """
    return dir(obj)  
