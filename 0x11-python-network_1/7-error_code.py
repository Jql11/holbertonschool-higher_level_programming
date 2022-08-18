#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
must use the packages requests and sys
"""
import requests
from requests.exceptions import HTTPError
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code < 400:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
