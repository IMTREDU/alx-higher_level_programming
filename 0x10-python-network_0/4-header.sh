#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL with a custom header X-School-User-Id: 98

curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L
