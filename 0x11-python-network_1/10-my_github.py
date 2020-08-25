#!/usr/bin/python3
""" takes your Github credentials (username and password)
    and uses the Github API to display your id """
import requests
from sys import argv


if __name__ == "__main__":
    access = (argv[1], argv[2])
    r = requests.get('https://api.github.com/user', auth=access)
    try:
        print(r.json().get('id'))
    except ValueError:
        print("Not a valid JSON")
