#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email_data = {"email": sys.argv[2]}
    encoded_data = urllib.parse.urlencode(email_data).encode("ascii")

    with urllib.request.urlopen(url, data=encoded_data) as response:
        print(response.read().decode("utf-8"))
