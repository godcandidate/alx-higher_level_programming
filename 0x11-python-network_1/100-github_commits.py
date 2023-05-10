#!/usr/bin/python3
""" displays the first 10 commits in github"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]
    url = f"https://api.github.com/repos/{user}/{repo}/commits"

    dict_ = requests.get(url)
    commits = dict_.json()

    try:
        for i in range(10):
            sha = commits[i].get("sha")
            name = commits[i].get("commit").get("author").get("name")
            print(f"{sha}: {name}")
    except IndexError:pass
