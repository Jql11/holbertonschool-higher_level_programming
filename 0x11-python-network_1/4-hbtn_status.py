#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
must use the package requests
"""
import requests as req

if __name__ == "__main__":
    resp = req.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
