#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- and displays the body of the response.
"""

import sys
import requests

def fetch_url(url):
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.RequestException as error:
        print(f"Failed to fetch URL: {error}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url_to_fetch = sys.argv[1]
        fetch_url(url_to_fetch)
