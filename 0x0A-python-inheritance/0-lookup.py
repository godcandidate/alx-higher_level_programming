#!/usr/bin/python3
"""
    This module returns the list of available attributes
    and methods of an object
"""

def lookup(obj):
    """ A function that returns the list of available attributes
        and methods of an object

    Args:
        obj: instance of the class

    Returns:
        List of attributes
    """

    return dir(obj)
