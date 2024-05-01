#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL

curl -sX GET $1 -L
