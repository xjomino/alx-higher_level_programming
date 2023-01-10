#!/usr/bin/python3
"""read_file function documentation """


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""

    with open(filename, "r", encoding="utf8") as file:
        print(file.read())
