#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.request
import urllib.parse

url = sys.argv[1]
email = sys.argv[2]

try:
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(f"{body}")
except Exception as e:
    print(f"An error occurred: {e}")
