#!/usr/bin/python3
"""
The Holberton School staff evaluates candidates applying
for a back-end position with multiple technical challenges.
Write a Python script that takes 2 arguments in order to solve this challenge.
"""

import requests
import sys


def fetch_commits(owner, name):
    """
    Function that fetches 10 github commits.
    """

    base_url = "https://api.github.com/repos"
    endpoint = f"{base_url}/{owner}/{name}/commits"
    try:
        response = requests.get(endpoint)
        response.raise_for_status()

        commits = response.json()

        for commit in commits[:10]:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    fetch_commits(owner_name, repo_name)
