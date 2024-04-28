#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token) and
uses the GitHub API to display the user's id.
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/IMTREDU/{}'.format(argv[1])
    r = requests.get(url,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
