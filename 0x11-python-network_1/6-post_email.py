#!/usr/bin/python3
"""
takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter
and finally displays the body of the response.
"""
import requests as req
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    resp = req.post(url, data=payload)
    print(resp.text)