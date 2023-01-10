#!/usr/bin/python3
"""Student function documentation"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """instance initializer"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionart"""

        dict = vars(self)
        if attrs is None:
            return dict

        j = {f: m for f, m in dict.items() if f in attrs}
        return j
