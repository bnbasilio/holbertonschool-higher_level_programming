#!/bin/bash
# takes URL, sends a POST request to URL and displays body of response
curl -sX POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
