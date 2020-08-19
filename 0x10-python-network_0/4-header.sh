#!/bin/bash
# takes in URL, sends GET request to URL and displays the body of response
curl -sL "$1" -H "X-HolbertonSchool-User-Id: 98"
