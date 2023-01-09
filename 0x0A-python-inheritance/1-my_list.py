#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """Create a copy of the list and sort it in ascending orderi"""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
