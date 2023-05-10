#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests
import sys


if __name__ == "__main__":
    heading = requests.get(sys.argv[1])
    print(heading.headers['X-Request-Id'])
