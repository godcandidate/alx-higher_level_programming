#!/usr/bin/python3
""" displays the value of the X-Request-Id variable found in
the header of the response"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    dict_ = {'email' : sys.argv[2],}

    data = urllib.parse.urlencode(dict_)
    data = data.encode('ascii')
    requests = urllib.request.Request(url, data)
    with urllib.request.urlopen(requests) as response:
        html = response.read()
        print(html.decode("utf-8"))

