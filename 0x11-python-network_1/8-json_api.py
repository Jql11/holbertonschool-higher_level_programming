#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
display the id and name like this: [<id>] <name>
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    myobj = {'q': letter}
    x = requests.post(url, data=myobj)
    try:
        if x.json():
            print("[{}] {}".format(x.json().get('id'), x.json().get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
