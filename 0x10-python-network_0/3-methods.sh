#!/bin/bash
# script that takes in a URL and displays all HTTP methods
curl -sI "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
