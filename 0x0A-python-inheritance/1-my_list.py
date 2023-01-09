#!/usr/bin/python3
"""class mylist that inherits from list"""


class MyList(list):
    """myList class inherits from the list class"""

    def print_sorted(self):
        """prints the list, but sorted asc"""

        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
