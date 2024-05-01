#!/bin/bash
# Check if the URL argument is provided
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
