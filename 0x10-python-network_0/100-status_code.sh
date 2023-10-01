#!/bin/bash
# sends a request to a specified URL, and displays the size of the body of the response
curl -so /dev/null -w '%{http_code}' "$1"
