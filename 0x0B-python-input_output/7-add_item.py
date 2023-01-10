#!/usr/bin/python3
"""adds arguments and save into file"""
import json
from sys import argv


def save_to_json_file(my_obj, filename):
    """a function that writes an Object
    to a text file, using a JSON representation
    """

    with open(filename, mode="w") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """function that creates an Object
    from a “JSON file”
    """

    with open(filename, mode="r") as file:
        return json.load(file)


argv.pop(0)


try:
    deserialized = load_from_json_file("add_item.json")

    if deserialized is None:
        save_to_json_file(argv, "add_item.json")
    else:
        deserialized.extend(argv)
        save_to_json_file(deserialized, "add_item.json")
except FileNotFoundError:
    save_to_json_file(argv, "add_item.json")
