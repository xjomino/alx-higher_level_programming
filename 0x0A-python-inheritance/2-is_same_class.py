#!/usr/bin/python3
"""class instance checker"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an
    instance of the specified class ; otherwise False
    """
    return obj.__class__ == a_class
