#!/usr/bin/python3
""" takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter """
import requests
from sys import argv


if __name__ == "__main__":
    if (len(argv) == 1):
        payload = {"q": ""}
        r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    else:
        payload = {"q": argv[1])
        r = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        user = r.json()
        if user:
            print("[{}] {}".format(user.get('id'), user.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
