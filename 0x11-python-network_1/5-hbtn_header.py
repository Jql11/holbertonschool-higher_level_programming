#!/usr/bin/python3
"""
 sends a request to the URL and
 displays the value of the variable X-Request-Id
 in the response header
 must use the packages requests and sys
 """
import requests as req
import sys

if __name__ == "__main__":
    resp = req.head(sys.argv[1])
    print(resp.headers['X-Request-Id'])
