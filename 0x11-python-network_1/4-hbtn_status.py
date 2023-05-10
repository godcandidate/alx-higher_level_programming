#!/usr/bin/python3
"""  a Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    requests = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    with urllib.request.urlopen(requests) as response:
        content = response.read().decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
