#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in
the header of the response"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    dict_ = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(dict_)
    data = data.encode('ascii')

    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
        print(html.decode("utf-8"))
