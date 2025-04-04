#!/usr/bin/python3
"""
Fetches https://alu-intranet.hbtn.io/status
using urllib and displays the response body.
"""

import urllib.request

url = 'https://alu-intranet.hbtn.io/status'

if __name__ == '__main__':
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
