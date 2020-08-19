#!/bin/bash
# sends a request to URL passed as arg and displays status code of response
curl -so /dev/null -w "%{http_code}" "$1"
