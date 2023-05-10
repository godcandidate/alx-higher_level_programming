#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in
the header of the response"""
import urllib.request
import sys


if __name__ == "__main__":
    link = sys.argv[1]
    try:
        with urllib.request.urlopen(link) as response:
            content = response.read()
            print(content.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
