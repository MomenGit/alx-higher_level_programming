#!/bin/bash
# request to 0.0.0.0:5000/catch_me that causes the server to respond You got me!, in the body
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
