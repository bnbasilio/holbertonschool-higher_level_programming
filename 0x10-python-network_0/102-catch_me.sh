#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me and server will respond with You got me!, in the body of the response
curl -sLX PUT -d 'user_id=98' -H 'Origin: HolbertonSchool' 0.0.0.0:5000/catch_me
