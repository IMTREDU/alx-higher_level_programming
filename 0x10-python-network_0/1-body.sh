#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL

curl -s -X GET -L -w "%{http_code}" "$1" -o /dev/null | grep -q 200 && curl -s "$1"
