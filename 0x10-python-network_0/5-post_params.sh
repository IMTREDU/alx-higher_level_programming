#!/bin/bash
# This script takes a URL as an argument, sends a POST request to the passed URL with specified parameters

curl -sX POST $1 -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -L
