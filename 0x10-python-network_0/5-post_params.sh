#!/bin/bash
# Sends a POST request with specific parameters to a URL
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"
