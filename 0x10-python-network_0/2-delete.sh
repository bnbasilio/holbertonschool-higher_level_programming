#!/bin/bash
# send DELETE request to URL (1st argument) and displays body of response
curl -sLX DELETE "$1"
