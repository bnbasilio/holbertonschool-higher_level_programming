#!/bin/bash
# takes URL, sends request to URL and displays size of body as response
curl -sI "$1" | grep "Content-Length: " | awk '{print $2}'
