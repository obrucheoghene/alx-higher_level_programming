#!/usr/bin/python3
"""
A script that request to the URL and displays the value
of the X-Request-Id variable found in the header ofthe response.
"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    url = argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as res:
        print(dict(res.headers).get("X-Request-Id"))
