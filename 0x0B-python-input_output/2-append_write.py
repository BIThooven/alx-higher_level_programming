#!/usr/bin/python3
"""appending a string to the end of a file"""


def append_write(filename="", text=""):
    """a function that appends a string to the end of a file if it exists

    Args:
        filename: the name of the file to append to
        text: strings to be appended
    Return:
        returns the appended file
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
