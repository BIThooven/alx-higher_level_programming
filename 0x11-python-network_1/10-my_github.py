#!/usr/bin/python3
"""Github API"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = argv[1]
    token = argv[2]
    r = requests.get(url, auth=(user, token))
    print(r.json().get('id'))
