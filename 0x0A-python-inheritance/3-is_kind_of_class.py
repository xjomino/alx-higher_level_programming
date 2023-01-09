#!/usr/bin/python3
"""inherited class checker"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is exactly an
    instance of the specified class ; otherwise False.
    """

    return isinstance(obj, a_class)
