#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- and displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <url>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Failed to send request to {url}: {e}")
        sys.exit(1)
    
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
