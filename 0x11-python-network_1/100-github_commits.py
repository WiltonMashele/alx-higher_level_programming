#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the repository
"""
import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for i in range(min(10, len(commits))):
            sha = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    else:
        print("Unable to fetch commits.")
