#!/bin/bash
# send JSON POST request to URL (1st arg) and displays body of response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
