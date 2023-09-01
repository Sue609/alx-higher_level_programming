#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response.
"""

import urllib.request
import sys

try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.getheader('X-Request-Id')
        if x_request_id:
            print(x_request_id)
except urllib.error.URLError as e:
    print(f"Eroor: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
