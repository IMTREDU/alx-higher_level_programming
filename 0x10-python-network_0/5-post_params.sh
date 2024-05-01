#!/bin/bash
# This script takes a URL as an argument, sends a POST request to the passed URL with specified parameters

curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
