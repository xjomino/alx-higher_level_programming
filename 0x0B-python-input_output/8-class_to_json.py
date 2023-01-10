#!/usr/bin/python3
def class_to_json(obj):
    # Use the built-in function vars to get the object's attributes
    return vars(obj)

