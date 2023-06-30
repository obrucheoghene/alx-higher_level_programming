#!/bin/bash
# Send a POST request to a given URL and display respose
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
