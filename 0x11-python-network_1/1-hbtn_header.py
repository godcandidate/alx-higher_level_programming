#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in
the header of the response"""
import urllib.request
import sys


if __name__ == "__main__":
    requests = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(requests) as response:
        heading = response.headers
        print(heading["X-Request-Id"])
