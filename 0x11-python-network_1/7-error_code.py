#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])

    if (url.status_code >= 400):
        print(response.status_code)
    else:
        print(response.text)
