#!/bin/bash
# This script takes a URL as an argument and displays all HTTP methods the server will accepti

curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
