#!/bin/bash
#sends a POST request, A variable email must be sent with the value test@gmail.comand A variable subject must be sent with the value I will always be here for PLD
curl -s -X POST "$1" -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD'
