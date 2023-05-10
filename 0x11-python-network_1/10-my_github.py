#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in
the header of the response"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    cpass = sys.argv[2]

    response = requests.get(url, auth=HTTPBasicAuth(user, cpass))
    print(response.json().get('id'))
