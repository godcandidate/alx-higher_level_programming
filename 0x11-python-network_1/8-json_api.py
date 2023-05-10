#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = {'q': ""}
    else:
        letter = {'q': sys.argv[1]}

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=letter)

    try:
        json_ = response.json()
        if json_ == {}:
            print("No result")
        else:
            print(f"[{json_.get('id')}] {json_.get('name')}")

    except ValueError:
        print("Not a valid JSON")
