#!/bin/bash
#takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response, with a header variable and value 98
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
