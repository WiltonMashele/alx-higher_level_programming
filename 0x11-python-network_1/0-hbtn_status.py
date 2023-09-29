#!/usr/bin/python3
"""script that 
- fetches https://alx-intranet.hbtn.io/status
- use the package urllib
"""

if __name__ == "__main__":
    from urllib import request

    url = 'https://alx-intranet.hbtn.io/status'

    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
