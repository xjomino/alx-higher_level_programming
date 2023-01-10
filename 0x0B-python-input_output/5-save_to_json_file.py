#!/usr/bin/python3
"""JSON handling"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object
    to a text file, using a JSON representation
    """

    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
