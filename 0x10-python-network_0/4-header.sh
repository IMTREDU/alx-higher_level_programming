#!/bin/bash
# Sends a GET request with a custom header to a URL
curl -s -X GET -H "X-School-User-Id: 98" "$1" -o /dev/null -w "%{http_code}"
