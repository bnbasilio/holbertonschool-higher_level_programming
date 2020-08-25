#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest) of the
    repository “rails” by the user “rails """
import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    r = requests.get(url)
    n = 0
    for data in r.json():
        if n < 10:
            print("{}: {}".format(data.get('sha'),
                  data.get('commit').get('author').get('name')))
        n = n + 1
