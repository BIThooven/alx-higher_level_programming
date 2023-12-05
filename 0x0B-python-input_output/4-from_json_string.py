#!/usr/bin/python3
"""python data structure returned from a json string"""
import json


def from_json_string(my_str):
    """a function to retrieve data from a json file

    Args:
        my_str: a json string
    Return:
        returns python data from a json string
    """
    return json.loads(my_str)
